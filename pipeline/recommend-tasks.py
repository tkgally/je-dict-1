#!/usr/bin/env python3
"""
Task scheduler recommendation script for je-dict-1 pipeline.

Examines the current project state and recommends what the next pipeline
run should contain. Outputs a suggested pipeline-config.json.

Logic:
  1. If candidate_words.json has < 100 candidates, recommend corpus harvesting
  2. If candidates >= 100, recommend entry creation (count = candidates / 30, capped at 5)
  3. If inline links progress is > 500 entries behind the latest entry, recommend
     inline link sessions
  4. Recommend one polishing session for whichever polishing task has the most
     entries remaining

Usage:
    python3 pipeline/recommend-tasks.py              # Print recommendations
    python3 pipeline/recommend-tasks.py --write      # Write to pipeline-config.json
    python3 pipeline/recommend-tasks.py --json       # Output raw JSON only
"""

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_INDEX = PROJECT_ROOT / "entries_index.json"
CANDIDATES_FILE = PROJECT_ROOT / "candidate_words.json"
CONFIG_OUTPUT = PROJECT_ROOT / "pipeline" / "pipeline-config.json"

# Thresholds
CANDIDATE_LOW = 100
ENTRIES_PER_SESSION = 30
MAX_ENTRY_SESSIONS = 5
INLINE_LINK_LAG_THRESHOLD = 500


def load_json(path: Path) -> dict:
    """Load a JSON file, returning empty dict on error."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Warning: could not load {path}: {e}", file=sys.stderr)
        return {}


def get_candidate_count(candidates_data: dict) -> int:
    """Return the number of candidates in candidate_words.json."""
    return len(candidates_data.get("candidates", []))


def get_entry_stats(index_data: dict) -> dict:
    """Extract relevant statistics from entries_index.json."""
    entries = index_data.get("entries", [])
    total = len(entries)
    with_inline_links = sum(1 for e in entries if e.get("has_inline_links"))
    without_inline_links = total - with_inline_links

    # Example count gaps by tier
    basic_core_low_examples = sum(
        1
        for e in entries
        if e.get("vocabulary_tier") in ("basic", "core")
        and e.get("example_count", 0) < 3
    )

    # Furigana: entries without inline links can serve as a proxy for
    # "entries that haven't been polished yet"
    # For polishing recommendations, count entries needing various improvements
    entries_without_links = without_inline_links
    entries_low_examples = sum(
        1 for e in entries if e.get("example_count", 0) < 3
    )
    entries_no_xrefs = sum(
        1 for e in entries if e.get("cross_reference_count", 0) == 0
    )

    return {
        "total": total,
        "with_inline_links": with_inline_links,
        "without_inline_links": entries_without_links,
        "basic_core_low_examples": basic_core_low_examples,
        "entries_low_examples": entries_low_examples,
        "entries_no_xrefs": entries_no_xrefs,
    }


def build_recommendations(candidate_count: int, entry_stats: dict) -> list[dict]:
    """Build a list of recommended tasks based on current project state."""
    tasks = []
    reasons = []

    # 1. Candidate count drives harvesting vs entry creation
    if candidate_count < CANDIDATE_LOW:
        tasks.append({
            "type": "corpus-harvesting",
            "count": 1,
            "parameters": {"batch_size": 150},
        })
        reasons.append(
            f"Candidates low ({candidate_count} < {CANDIDATE_LOW}) "
            f"— recommending corpus harvesting"
        )
    else:
        sessions = min(candidate_count // ENTRIES_PER_SESSION, MAX_ENTRY_SESSIONS)
        sessions = max(sessions, 1)
        tasks.append({
            "type": "new-entries",
            "count": sessions,
            "parameters": {"batch_size": ENTRIES_PER_SESSION},
        })
        reasons.append(
            f"Candidates available ({candidate_count}) "
            f"— recommending {sessions} entry creation session(s)"
        )

    # 2. Inline links lag
    without_links = entry_stats["without_inline_links"]
    if without_links > INLINE_LINK_LAG_THRESHOLD:
        link_sessions = min(without_links // 500, 3)
        link_sessions = max(link_sessions, 1)
        tasks.append({
            "type": "inline-links",
            "count": link_sessions,
            "parameters": {"batch_size": 15},
        })
        reasons.append(
            f"Inline links behind ({without_links} entries without links, "
            f"threshold {INLINE_LINK_LAG_THRESHOLD}) "
            f"— recommending {link_sessions} inline-link session(s)"
        )

    # 3. Pick the polishing task with the most entries remaining
    polishing_tasks = {
        "example-sentences": entry_stats["basic_core_low_examples"],
        "expand-short-notes": entry_stats["entries_low_examples"],
        "furigana-completeness": 0,  # placeholder — would need full scan
    }

    # Find the task with the most remaining work
    best_polish = max(polishing_tasks, key=polishing_tasks.get)
    best_count = polishing_tasks[best_polish]

    if best_count > 0:
        params = {"batch_size": 10}
        if best_polish == "example-sentences":
            params["tier"] = "core"
        tasks.append({
            "type": best_polish,
            "count": 1,
            "parameters": params,
        })
        reasons.append(
            f"Polishing: {best_polish} has {best_count} entries needing work "
            f"— recommending 1 session"
        )
    else:
        reasons.append("No polishing tasks with remaining work detected")

    return tasks, reasons


def format_config(tasks: list[dict]) -> dict:
    """Format tasks into a pipeline-config.json structure."""
    return {
        "description": "Auto-recommended pipeline run",
        "branch": "main",
        "on_failure": "skip",
        "tasks": tasks,
    }


def print_recommendations(reasons: list[str], config: dict) -> None:
    """Print human-readable recommendations."""
    print("=" * 50)
    print("  PIPELINE TASK RECOMMENDATIONS")
    print("=" * 50)
    print()

    print("Analysis:")
    for i, reason in enumerate(reasons, 1):
        print(f"  {i}. {reason}")
    print()

    print("Recommended pipeline config:")
    print("-" * 50)
    print(json.dumps(config, indent=2, ensure_ascii=False))
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Recommend pipeline tasks based on current project state"
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write recommended config to pipeline-config.json",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output only the JSON config (no explanation)",
    )
    args = parser.parse_args()

    # Load data
    index_data = load_json(ENTRIES_INDEX)
    candidates_data = load_json(CANDIDATES_FILE)

    if not index_data.get("entries"):
        print("Error: entries_index.json is empty or missing. Run: python3 build/update_indexes.py",
              file=sys.stderr)
        return 1

    candidate_count = get_candidate_count(candidates_data)
    entry_stats = get_entry_stats(index_data)

    tasks, reasons = build_recommendations(candidate_count, entry_stats)
    config = format_config(tasks)

    if args.json:
        print(json.dumps(config, indent=2, ensure_ascii=False))
    else:
        print_recommendations(reasons, config)

    if args.write:
        with open(CONFIG_OUTPUT, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
            f.write("\n")
        if not args.json:
            print(f"Written to {CONFIG_OUTPUT}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
