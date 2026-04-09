#!/usr/bin/env python3
"""Claim-based task queue for parallel polishing agents.

Enables multiple agents to claim and process polishing tasks without conflicts.
Uses file-level locking (fcntl) for atomic operations on the shared queue file.

Usage:
    python3 pipeline/task_queue.py populate --all
    python3 pipeline/task_queue.py claim --task-type furigana --count 25 --session-id mysession
    python3 pipeline/task_queue.py complete --session-id mysession
    python3 pipeline/task_queue.py status
"""

import argparse
import contextlib
import fcntl
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
QUEUE_FILE = SCRIPT_DIR / "task_queue.json"
ENTRIES_DIR = PROJECT_ROOT / "entries"
INDEX_FILE = PROJECT_ROOT / "entries_index.json"

TASK_TYPES = ["furigana", "notes", "examples", "cross_refs", "transitivity"]

KANJI_PATTERN = re.compile(r'[\u4e00-\u9faf\u3400-\u4dbf]')
FURIGANA_PATTERN = re.compile(r'\{[^|]+\|[^}]+\}')


def utcnow():
    """Return current UTC time as ISO 8601 string."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@contextlib.contextmanager
def locked_queue(filepath, mode='r+'):
    """Open the queue file with an exclusive lock."""
    with open(filepath, mode) as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        try:
            yield f
        finally:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)


def load_queue():
    """Load the queue file (without locking — use inside locked_queue)."""
    with open(QUEUE_FILE) as f:
        return json.load(f)


def save_queue(data, f):
    """Write queue data to an open file handle (must be locked)."""
    f.seek(0)
    f.truncate()
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write("\n")


def update_metadata(data):
    """Recompute metadata counters from task list."""
    tasks = data["tasks"]
    data["metadata"]["total_tasks"] = len(tasks)
    data["metadata"]["pending"] = sum(1 for t in tasks if t["status"] == "pending")
    data["metadata"]["in_progress"] = sum(1 for t in tasks if t["status"] == "in_progress")
    data["metadata"]["completed"] = sum(1 for t in tasks if t["status"] == "completed")


def create_empty_queue():
    """Create an empty queue data structure."""
    return {
        "version": "1.0",
        "tasks": [],
        "metadata": {
            "last_populated": None,
            "task_types": TASK_TYPES,
            "total_tasks": 0,
            "pending": 0,
            "in_progress": 0,
            "completed": 0
        }
    }


def require_queue_exists():
    """Exit with error if queue file doesn't exist."""
    if not QUEUE_FILE.exists():
        print("Error: Queue file not found. Run `populate` first.", file=sys.stderr)
        sys.exit(1)


# --- Entry loading ---

def load_all_entries():
    """Load all entry JSON files from the entries directory."""
    entries = []
    for filepath in sorted(glob.glob(str(ENTRIES_DIR / "**" / "*.json"), recursive=True)):
        try:
            with open(filepath) as f:
                entry = json.load(f)
            entries.append(entry)
        except (json.JSONDecodeError, OSError):
            continue
    return entries


def get_tier_priority(tier, base_priority):
    """Map vocabulary tier to a priority offset. Lower = higher priority."""
    if tier in ("basic", "core"):
        return base_priority
    return base_priority + 2  # general tier gets +2


# --- Population functions ---

def has_missing_furigana(text):
    """Check if text contains kanji outside of furigana markup."""
    if not text:
        return False
    stripped = FURIGANA_PATTERN.sub('', text)
    return bool(KANJI_PATTERN.search(stripped))


def check_entry_furigana(entry):
    """Check if an entry has missing furigana in any field."""
    # Check headword
    if has_missing_furigana(entry.get("headword", "")):
        return True
    # Check examples
    for ex in entry.get("examples", []):
        if has_missing_furigana(ex.get("japanese", "")):
            return True
    # Check notes
    notes = entry.get("notes", "")
    if isinstance(notes, list):
        for note in notes:
            if isinstance(note, str) and has_missing_furigana(note):
                return True
            elif isinstance(note, dict) and has_missing_furigana(note.get("text", "")):
                return True
    elif isinstance(notes, str) and has_missing_furigana(notes):
        return True
    return False


def populate_furigana(entries, existing_task_ids):
    """Find entries with missing furigana."""
    tasks = []
    for entry in entries:
        entry_id = entry.get("id", "")
        task_id = f"furigana-{entry_id}"
        if task_id in existing_task_ids:
            continue
        if check_entry_furigana(entry):
            tier = entry.get("metadata", {}).get("vocabulary_tier",
                   entry.get("vocabulary_tier", "general"))
            priority = get_tier_priority(tier, 1)
            tasks.append(make_task(task_id, entry_id, "furigana", priority))
    return tasks


def strip_furigana(text):
    """Remove furigana markup from text, keeping the kanji."""
    if not text:
        return ""
    return FURIGANA_PATTERN.sub(lambda m: m.group(0).split("|")[0].lstrip("{"), text)


def get_notes_text(entry):
    """Extract all notes text from an entry as a single string."""
    notes = entry.get("notes", "")
    if isinstance(notes, list):
        parts = []
        for note in notes:
            if isinstance(note, str):
                parts.append(note)
            elif isinstance(note, dict):
                parts.append(note.get("text", ""))
        return "\n".join(parts)
    elif isinstance(notes, str):
        return notes
    return ""


def populate_notes(entries, existing_task_ids):
    """Find entries with short or missing notes."""
    tasks = []
    for entry in entries:
        entry_id = entry.get("id", "")
        task_id = f"notes-{entry_id}"
        if task_id in existing_task_ids:
            continue

        notes_text = get_notes_text(entry)
        stripped = strip_furigana(notes_text)
        tier = entry.get("metadata", {}).get("vocabulary_tier",
               entry.get("vocabulary_tier", "general"))

        needs_work = False
        severity = "short"  # "missing" or "short"

        if not notes_text.strip():
            needs_work = True
            severity = "missing"
        elif len(stripped.strip()) < 100:
            needs_work = True
            severity = "short"
        elif isinstance(entry.get("notes"), list) and len(entry["notes"]) <= 1:
            needs_work = True
            severity = "short"
        elif isinstance(entry.get("notes"), str) and len(stripped.strip()) < 100:
            needs_work = True
            severity = "short"

        if needs_work:
            if tier in ("basic", "core"):
                priority = 1 if severity == "missing" else 2
            else:
                priority = 3 if severity == "missing" else 4
            tasks.append(make_task(task_id, entry_id, "notes", priority))
    return tasks


def populate_examples(entries, existing_task_ids):
    """Find entries with insufficient examples."""
    tasks = []
    for entry in entries:
        entry_id = entry.get("id", "")
        task_id = f"examples-{entry_id}"
        if task_id in existing_task_ids:
            continue

        pos = entry.get("part_of_speech", "")
        examples = entry.get("examples", [])
        count = len(examples)
        tier = entry.get("metadata", {}).get("vocabulary_tier",
               entry.get("vocabulary_tier", "general"))

        # Minimum requirements
        min_required = 4 if "verb" in pos else 3

        if count < min_required:
            if tier in ("basic", "core"):
                priority = 1 if count <= 1 else 2
            else:
                priority = 3 if count <= 1 else 4
            tasks.append(make_task(task_id, entry_id, "examples", priority))
    return tasks


def populate_cross_refs(entries, existing_task_ids):
    """Find entries with no cross-references."""
    tasks = []
    for entry in entries:
        entry_id = entry.get("id", "")
        task_id = f"cross_refs-{entry_id}"
        if task_id in existing_task_ids:
            continue

        cross_refs = entry.get("cross_references", [])
        prominent = entry.get("prominent_see_also", [])
        tier = entry.get("metadata", {}).get("vocabulary_tier",
               entry.get("vocabulary_tier", "general"))

        if not cross_refs and not prominent:
            priority = 1 if tier in ("basic", "core") else 3
            tasks.append(make_task(task_id, entry_id, "cross_refs", priority))
    return tasks


def populate_transitivity(entries, existing_task_ids):
    """Find verb entries without transitivity info."""
    tasks = []
    transitivity_keywords = ["自動詞", "他動詞", "intransitive", "transitive"]

    for entry in entries:
        entry_id = entry.get("id", "")
        task_id = f"transitivity-{entry_id}"
        if task_id in existing_task_ids:
            continue

        pos = entry.get("part_of_speech", "")
        if "verb" not in pos.lower():
            continue

        # Check notes for transitivity info
        notes_text = get_notes_text(entry)
        has_transitivity = any(kw in notes_text for kw in transitivity_keywords)

        # Check cross-references for pair type
        cross_refs = entry.get("cross_references", [])
        has_pair = any(ref.get("type") == "pair" for ref in cross_refs)

        if not has_transitivity and not has_pair:
            tier = entry.get("metadata", {}).get("vocabulary_tier",
                   entry.get("vocabulary_tier", "general"))
            if tier in ("basic", "core"):
                priority = 1
            elif "suru" in pos.lower() or "godan" in pos.lower():
                priority = 2
            else:
                priority = 3
            tasks.append(make_task(task_id, entry_id, "transitivity", priority))
    return tasks


POPULATE_FUNCTIONS = {
    "furigana": populate_furigana,
    "notes": populate_notes,
    "examples": populate_examples,
    "cross_refs": populate_cross_refs,
    "transitivity": populate_transitivity,
}


def make_task(task_id, entry_id, task_type, priority):
    """Create a task dict."""
    return {
        "id": task_id,
        "entry_id": entry_id,
        "task_type": task_type,
        "status": "pending",
        "priority": priority,
        "claimed_by": None,
        "claimed_at": None,
        "completed_at": None,
        "created_at": utcnow(),
        "notes": None
    }


# --- Subcommands ---

def cmd_populate(args):
    """Populate the queue with tasks by scanning entries."""
    task_types = TASK_TYPES if args.all else [args.task_type]

    # Load or create queue
    if QUEUE_FILE.exists():
        data = load_queue()
    else:
        data = create_empty_queue()

    # Build set of existing task IDs (non-completed, unless --force)
    if args.force:
        # Remove all tasks of the target types
        data["tasks"] = [t for t in data["tasks"] if t["task_type"] not in task_types]
        existing_task_ids = {t["id"] for t in data["tasks"]}
    else:
        existing_task_ids = {t["id"] for t in data["tasks"]}

    print("Loading entries...")
    entries = load_all_entries()
    print(f"Loaded {len(entries)} entries.")

    total_added = 0
    for tt in task_types:
        populate_fn = POPULATE_FUNCTIONS[tt]
        new_tasks = populate_fn(entries, existing_task_ids)
        data["tasks"].extend(new_tasks)
        # Update existing_task_ids for subsequent types
        existing_task_ids.update(t["id"] for t in new_tasks)
        print(f"  {tt}: {len(new_tasks)} new tasks added")
        total_added += len(new_tasks)

    data["metadata"]["last_populated"] = utcnow()
    update_metadata(data)

    # Write the queue file (with lock to avoid clobbering concurrent operations)
    mode = 'r+' if QUEUE_FILE.exists() else 'w'
    if mode == 'w':
        with open(QUEUE_FILE, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")
    else:
        with locked_queue(QUEUE_FILE) as f:
            save_queue(data, f)

    print(f"\nTotal: {total_added} new tasks added ({data['metadata']['total_tasks']} total in queue)")


def cmd_claim(args):
    """Claim tasks from the queue."""
    require_queue_exists()

    with locked_queue(QUEUE_FILE) as f:
        data = json.load(f)

        # Find pending tasks of the requested type
        candidates = [t for t in data["tasks"]
                      if t["status"] == "pending" and t["task_type"] == args.task_type]

        # Sort by priority (ascending), then entry_id
        candidates.sort(key=lambda t: (t["priority"], t["entry_id"]))

        # Claim up to count
        to_claim = candidates[:args.count]
        now = utcnow()

        claimed_ids = []
        for task in to_claim:
            task["status"] = "in_progress"
            task["claimed_by"] = args.session_id
            task["claimed_at"] = now
            claimed_ids.append(task["entry_id"])

        update_metadata(data)
        save_queue(data, f)

    # Print claimed entry IDs (for piping)
    for eid in claimed_ids:
        print(eid)

    if len(to_claim) < args.count:
        remaining = args.count - len(to_claim)
        print(f"Note: only {len(to_claim)} tasks available ({remaining} fewer than requested)",
              file=sys.stderr)


def cmd_complete(args):
    """Mark tasks as completed."""
    if not args.session_id and not args.task_ids:
        print("Error: must provide --session-id or --task-ids", file=sys.stderr)
        sys.exit(1)

    require_queue_exists()

    with locked_queue(QUEUE_FILE) as f:
        data = json.load(f)
        now = utcnow()
        completed_count = 0

        if args.session_id:
            # Complete all tasks claimed by this session
            for task in data["tasks"]:
                if task["claimed_by"] == args.session_id and task["status"] == "in_progress":
                    task["status"] = "completed"
                    task["completed_at"] = now
                    completed_count += 1
        elif args.task_ids:
            # Complete specific task IDs
            target_ids = set(args.task_ids.split(","))
            task_map = {t["id"]: t for t in data["tasks"]}
            for tid in target_ids:
                if tid not in task_map:
                    print(f"Warning: task '{tid}' not found in queue", file=sys.stderr)
                    continue
                task = task_map[tid]
                if task["status"] != "in_progress":
                    print(f"Warning: task '{tid}' is not in_progress (status: {task['status']})",
                          file=sys.stderr)
                    continue
                task["status"] = "completed"
                task["completed_at"] = now
                completed_count += 1

        update_metadata(data)
        save_queue(data, f)

    print(f"Completed {completed_count} tasks")


def cmd_release(args):
    """Release claimed tasks back to pending."""
    require_queue_exists()

    with locked_queue(QUEUE_FILE) as f:
        data = json.load(f)
        released_count = 0

        for task in data["tasks"]:
            if task["claimed_by"] == args.session_id and task["status"] == "in_progress":
                task["status"] = "pending"
                task["claimed_by"] = None
                task["claimed_at"] = None
                released_count += 1

        update_metadata(data)
        save_queue(data, f)

    print(f"Released {released_count} tasks back to pending")


def cmd_status(args):
    """Show queue statistics."""
    require_queue_exists()
    data = load_queue()
    tasks = data["tasks"]

    # Filter by task type if specified
    if args.task_type:
        tasks = [t for t in tasks if t["task_type"] == args.task_type]

    total = len(tasks)
    pending = sum(1 for t in tasks if t["status"] == "pending")
    in_progress = sum(1 for t in tasks if t["status"] == "in_progress")
    completed = sum(1 for t in tasks if t["status"] == "completed")

    print("Task Queue Status")
    print("=================")
    print(f"Total tasks:    {total}")
    print(f"Pending:        {pending}")
    print(f"In progress:    {in_progress}")
    print(f"Completed:      {completed}")

    if not args.task_type:
        # Show breakdown by type
        print("\nBy task type:")
        for tt in TASK_TYPES:
            tt_tasks = [t for t in data["tasks"] if t["task_type"] == tt]
            tp = sum(1 for t in tt_tasks if t["status"] == "pending")
            ti = sum(1 for t in tt_tasks if t["status"] == "in_progress")
            tc = sum(1 for t in tt_tasks if t["status"] == "completed")
            print(f"  {tt:15s} {tp:5d} pending / {ti:3d} in_progress / {tc:5d} completed")

    if args.verbose:
        # Show claimed-by details
        in_prog = [t for t in tasks if t["status"] == "in_progress"]
        if in_prog:
            print("\nIn-progress tasks:")
            for t in in_prog:
                print(f"  {t['id']:30s}  claimed_by={t['claimed_by']}  at={t['claimed_at']}")
        else:
            print("\nNo tasks currently in progress.")


def cmd_cleanup(args):
    """Reclaim stale tasks."""
    require_queue_exists()

    timeout_minutes = args.timeout
    cutoff = datetime.now(timezone.utc) - timedelta(minutes=timeout_minutes)

    with locked_queue(QUEUE_FILE) as f:
        data = json.load(f)
        reclaimed = 0

        for task in data["tasks"]:
            if task["status"] == "in_progress" and task["claimed_at"]:
                claimed_at = datetime.fromisoformat(task["claimed_at"].replace("Z", "+00:00"))
                if claimed_at < cutoff:
                    task["status"] = "pending"
                    old_session = task["claimed_by"]
                    task["claimed_by"] = None
                    task["claimed_at"] = None
                    reclaimed += 1
                    if reclaimed <= 10:  # Only print first 10
                        print(f"  Reclaimed {task['id']} (was claimed by {old_session})")

        if reclaimed > 10:
            print(f"  ... and {reclaimed - 10} more")

        update_metadata(data)
        save_queue(data, f)

    print(f"\nReclaimed {reclaimed} stale tasks (timeout: {timeout_minutes} minutes)")


def cmd_reset(args):
    """Reset tasks back to pending."""
    require_queue_exists()

    with locked_queue(QUEUE_FILE) as f:
        data = json.load(f)
        reset_count = 0

        for task in data["tasks"]:
            if args.all or task["task_type"] == args.task_type:
                if task["status"] != "pending":
                    task["status"] = "pending"
                    task["claimed_by"] = None
                    task["claimed_at"] = None
                    task["completed_at"] = None
                    reset_count += 1

        update_metadata(data)
        save_queue(data, f)

    print(f"Reset {reset_count} tasks to pending")


# --- CLI ---

def main():
    parser = argparse.ArgumentParser(
        description="Claim-based task queue for parallel polishing agents")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # populate
    p_populate = subparsers.add_parser("populate",
        help="Scan entries and populate the queue with tasks")
    p_populate.add_argument("--task-type", choices=TASK_TYPES,
        help="Task type to populate")
    p_populate.add_argument("--all", action="store_true",
        help="Populate all task types")
    p_populate.add_argument("--force", action="store_true",
        help="Re-populate even if tasks already exist (removes existing tasks of target types)")

    # claim
    p_claim = subparsers.add_parser("claim",
        help="Claim pending tasks for processing")
    p_claim.add_argument("--task-type", choices=TASK_TYPES, required=True,
        help="Task type to claim")
    p_claim.add_argument("--count", type=int, default=25,
        help="Number of tasks to claim (default: 25)")
    p_claim.add_argument("--session-id", required=True,
        help="Unique session identifier")

    # complete
    p_complete = subparsers.add_parser("complete",
        help="Mark tasks as completed")
    p_complete.add_argument("--task-ids",
        help="Comma-separated task IDs to complete")
    p_complete.add_argument("--session-id",
        help="Complete all tasks claimed by this session")

    # release
    p_release = subparsers.add_parser("release",
        help="Release claimed tasks back to pending")
    p_release.add_argument("--session-id", required=True,
        help="Session whose tasks to release")

    # status
    p_status = subparsers.add_parser("status",
        help="Show queue statistics")
    p_status.add_argument("--task-type", choices=TASK_TYPES,
        help="Show status for one task type only")
    p_status.add_argument("--verbose", action="store_true",
        help="Show claimed-by details")

    # cleanup
    p_cleanup = subparsers.add_parser("cleanup",
        help="Reclaim stale tasks from crashed sessions")
    p_cleanup.add_argument("--timeout", type=int, default=30,
        help="Minutes after which a claimed task is considered stale (default: 30)")

    # reset
    p_reset = subparsers.add_parser("reset",
        help="Reset tasks back to pending")
    p_reset.add_argument("--task-type", choices=TASK_TYPES,
        help="Task type to reset")
    p_reset.add_argument("--all", action="store_true",
        help="Reset all tasks")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Validation
    if args.command == "populate" and not args.all and not args.task_type:
        print("Error: specify --task-type TYPE or --all", file=sys.stderr)
        sys.exit(1)

    if args.command == "complete" and not args.task_ids and not args.session_id:
        print("Error: specify --task-ids or --session-id", file=sys.stderr)
        sys.exit(1)

    if args.command == "reset" and not args.all and not args.task_type:
        print("Error: specify --task-type TYPE or --all", file=sys.stderr)
        sys.exit(1)

    commands = {
        "populate": cmd_populate,
        "claim": cmd_claim,
        "complete": cmd_complete,
        "release": cmd_release,
        "status": cmd_status,
        "cleanup": cmd_cleanup,
        "reset": cmd_reset,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
