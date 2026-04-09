# Claim-Based Task Queue

**Enhancement plan section**: [2.2.2] Claim-Based Task Queue

Build a task queue system that allows multiple parallel polishing agents to claim and process tasks without conflicts. This is the infrastructure that enables scaling from one sequential agent to 3-4 parallel agents, each specializing in one quality dimension.

## What This Prompt Creates/Modifies

| File | Action | Purpose |
|------|--------|---------|
| `pipeline/task_queue.py` | **Create** | Task queue manager with claim/complete/populate commands |
| `pipeline/task_queue.json` | **Create** | Task queue data file (created by first `populate` run) |
| `prompts/queue_polishing_template.md` | **Create** | Template showing how polishing prompts use the queue |
| `pipeline/README.md` | **Modify** | Document the queue system |
| `CLAUDE.md` | **Modify** | Add task queue commands |
| `Makefile` | **Modify** | Add queue-related targets |

---

## Prerequisites

- Prompt 11 (Parallel-Safe Prompt Redesign) should be complete, but the task queue can be built independently. It will integrate with parallel-safe prompts once both exist.

---

## Part A: Build Task Queue

Create `pipeline/task_queue.py` — a command-line tool for managing a claim-based task queue.

### A1: Data Model

The queue data lives in `pipeline/task_queue.json`:

```json
{
  "version": "1.0",
  "tasks": [
    {
      "id": "furigana-00123",
      "entry_id": "00123",
      "task_type": "furigana",
      "status": "pending",
      "priority": 1,
      "claimed_by": null,
      "claimed_at": null,
      "completed_at": null,
      "created_at": "2026-04-09T12:00:00Z",
      "notes": null
    }
  ],
  "metadata": {
    "last_populated": "2026-04-09T12:00:00Z",
    "task_types": ["furigana", "notes", "examples", "cross_refs", "transitivity"],
    "total_tasks": 0,
    "pending": 0,
    "in_progress": 0,
    "completed": 0
  }
}
```

### A2: File Locking

Implement file-level locking to ensure atomic operations when multiple agents access the queue simultaneously:

```python
import fcntl
import contextlib

@contextlib.contextmanager
def locked_queue(filepath, mode='r+'):
    """Open the queue file with an exclusive lock."""
    with open(filepath, mode) as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        try:
            yield f
        finally:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
```

All read-modify-write operations on `task_queue.json` must use this locking mechanism. The lock ensures that two agents running `claim` simultaneously will not claim the same tasks.

### A3: Commands

Implement the following subcommands using `argparse` with subparsers:

#### `populate`

```bash
python3 pipeline/task_queue.py populate --task-type TYPE
python3 pipeline/task_queue.py populate --task-type TYPE --force   # Re-populate even if tasks exist
python3 pipeline/task_queue.py populate --all                      # Populate all task types
```

Scans entries to find work needed for the given task type. Adds new tasks to the queue for entries that:
- Do not already have a task of this type in the queue (pending or in_progress)
- Are not already marked completed for this task type

Details on population logic are in Part B below.

#### `claim`

```bash
python3 pipeline/task_queue.py claim --task-type TYPE --count N --session-id ID
```

Atomically claims up to N pending tasks of the specified type:
1. Acquire file lock
2. Find up to N tasks where `status == "pending"` and `task_type == TYPE`
3. Sort by priority (lower number = higher priority), then by entry_id
4. Set `status = "in_progress"`, `claimed_by = session_id`, `claimed_at = now`
5. Write the updated queue
6. Release lock
7. Print the claimed entry IDs, one per line (for easy piping to other scripts)

If fewer than N tasks are available, claim whatever is available and print a note.

#### `complete`

```bash
python3 pipeline/task_queue.py complete --task-ids ID1,ID2,...
python3 pipeline/task_queue.py complete --session-id ID            # Complete all tasks claimed by session
```

Marks tasks as completed:
1. Acquire file lock
2. For each specified task, set `status = "completed"`, `completed_at = now`
3. Update metadata counters
4. Write the updated queue
5. Release lock

#### `release`

```bash
python3 pipeline/task_queue.py release --session-id ID
```

Releases all tasks claimed by a session back to pending:
1. Acquire file lock
2. Find tasks where `claimed_by == session_id` and `status == "in_progress"`
3. Set `status = "pending"`, `claimed_by = null`, `claimed_at = null`
4. Update metadata counters
5. Release lock

This is used when an agent session crashes or is interrupted.

#### `status`

```bash
python3 pipeline/task_queue.py status
python3 pipeline/task_queue.py status --task-type TYPE    # Status for one type only
python3 pipeline/task_queue.py status --verbose           # Show claimed-by details
```

Prints queue statistics:

```
Task Queue Status
=================
Total tasks:    1000
Pending:         800
In progress:       5
Completed:       195

By task type:
  furigana:     400 pending /  50 in_progress / 100 completed
  notes:        200 pending /   0 in_progress /  50 completed
  examples:     100 pending /   5 in_progress /  30 completed
  cross_refs:    80 pending /   0 in_progress /  15 completed
  transitivity:  20 pending /   0 in_progress /   0 completed
```

#### `cleanup`

```bash
python3 pipeline/task_queue.py cleanup --timeout MINUTES
python3 pipeline/task_queue.py cleanup                      # Default: 30 minutes
```

Reclaims tasks that have been claimed for longer than the timeout:
1. Acquire file lock
2. Find tasks where `status == "in_progress"` and `claimed_at` is older than the timeout
3. Set `status = "pending"`, `claimed_by = null`, `claimed_at = null`
4. Print a summary of reclaimed tasks
5. Release lock

This handles agent crashes and abandoned sessions.

#### `reset`

```bash
python3 pipeline/task_queue.py reset --task-type TYPE      # Reset all tasks of a type to pending
python3 pipeline/task_queue.py reset --all                  # Reset entire queue
```

Resets tasks back to pending. Useful for re-running a task type after prompt changes.

### A4: Error Handling

- If `pipeline/task_queue.json` does not exist, `populate` creates it. All other commands print an error and exit: "Queue file not found. Run `populate` first."
- If a task ID passed to `complete` does not exist or is not in_progress, print a warning but continue processing other IDs.
- All timestamps use UTC ISO 8601 format.

### A5: Verification

```bash
# Script runs and shows help
python3 pipeline/task_queue.py --help
python3 pipeline/task_queue.py populate --help
python3 pipeline/task_queue.py claim --help

# Commands work end-to-end (will test more thoroughly in Part B)
python3 pipeline/task_queue.py populate --task-type furigana
python3 pipeline/task_queue.py status
```

---

## Part B: Task Population Logic

Implement the scanning logic for each task type. Each population function should:
1. Load all entries (or the entries index) to find candidates
2. Apply task-specific criteria to determine which entries need work
3. Assign a priority (1 = highest, 5 = lowest) based on vocabulary tier and severity

### B1: `furigana` — Entries with potential missing furigana

Scan entries for kanji characters that do not have furigana markup:

```python
import re

KANJI_PATTERN = re.compile(r'[\u4e00-\u9faf\u3400-\u4dbf]')
FURIGANA_PATTERN = re.compile(r'\{[^|]+\|[^}]+\}')

def find_missing_furigana(text):
    """Check if text contains kanji outside of furigana markup."""
    # Remove all furigana-marked text
    stripped = FURIGANA_PATTERN.sub('', text)
    # Check remaining text for kanji
    return bool(KANJI_PATTERN.search(stripped))
```

Check `headword`, all `examples[].japanese`, and `notes` fields. Priority:
- Priority 1: basic tier entries
- Priority 2: core tier entries
- Priority 3: general tier entries

### B2: `notes` — Entries with short notes

Flag entries where the `notes` field:
- Is missing entirely
- Has total text length < 100 characters (after stripping furigana markup)
- Has only 1 note item (most entries should have multiple)

Priority:
- Priority 1: basic/core tier with missing notes
- Priority 2: basic/core tier with short notes
- Priority 3: general tier with missing notes
- Priority 4: general tier with short notes

### B3: `examples` — Entries with insufficient examples

Flag entries that have fewer than the minimum required examples. Check the entry-guidelines skill for exact minimums, but a reasonable default:
- Verbs: need at least 4 examples
- Other POS: need at least 3 examples

Priority:
- Priority 1: basic/core entries with 0-1 examples
- Priority 2: basic/core entries below minimum
- Priority 3: general entries with 0-1 examples
- Priority 4: general entries below minimum

### B4: `cross_refs` — Entries with no cross-references

Flag entries where:
- `cross_references` is missing or empty
- `prominent_see_also` is missing or empty
- The entry has no outgoing references of any kind

Priority:
- Priority 1: basic/core entries (these should all be well-linked)
- Priority 3: general entries

### B5: `transitivity` — Verb entries without transitivity info

Flag verb entries (POS contains "verb") where:
- The notes field does not contain "自動詞", "他動詞", "intransitive", or "transitive"
- No cross-reference with type "pair" exists

Priority:
- Priority 1: basic/core verbs
- Priority 2: general verbs with suru-verb or godan patterns
- Priority 3: other general verbs

### B6: Population Verification

After implementing all population logic:

```bash
# Populate all task types
python3 pipeline/task_queue.py populate --all

# Check the results
python3 pipeline/task_queue.py status

# Verify reasonable numbers (should be > 0 for each type)
# If any type shows 0 tasks, investigate the detection logic
```

---

## Part C: Queue-Aware Prompt Template

Create `prompts/queue_polishing_template.md` — a template showing how polishing prompts should integrate with the task queue.

```markdown
# Queue-Based Polishing Template

This template shows how polishing prompts interact with the claim-based task queue. Adapt this pattern for each specific polishing task.

## Setup

Generate a unique session ID at the start of each session:

```bash
SESSION_ID="$(date +%Y%m%d-%H%M%S)-$$"
echo "Session ID: $SESSION_ID"
```

## Claim Tasks

```bash
# Claim a batch of entries to work on
python3 pipeline/task_queue.py claim --task-type TASK_TYPE --count 25 --session-id $SESSION_ID
```

Save the output (list of entry IDs) — these are the entries to process.

If fewer than 25 entries are returned, that means the queue is nearly empty for this task type.

## Process Entries

For each claimed entry ID:

1. Load the entry file
2. Perform the task-specific work
3. Save changes (if any)
4. Track which entries were actually modified

## Complete Tasks

After processing a batch:

```bash
# Mark processed entries as complete
python3 pipeline/task_queue.py complete --task-ids ID1,ID2,ID3,...
```

Only mark entries as complete if you actually reviewed them (even if no changes were needed). Do not mark entries as complete if you skipped them.

## Commit Cycle

After every batch of ~25 entries:

```bash
# Validate and build
make build

# Commit
git add -A
git commit -m "TASK_TYPE polish: entries XXXXX-XXXXX (via queue)"
```

## Claim Next Batch

After committing, claim the next batch:

```bash
python3 pipeline/task_queue.py claim --task-type TASK_TYPE --count 25 --session-id $SESSION_ID
```

Continue until the queue is empty or the session is ending.

## Session End

If ending before all claimed tasks are complete, release uncompleted tasks:

```bash
# Complete the ones you finished
python3 pipeline/task_queue.py complete --task-ids ID1,ID2,...

# Release any you did not get to
python3 pipeline/task_queue.py release --session-id $SESSION_ID
```

## Cleanup Stale Claims

If a previous session crashed, clean up its claims before starting:

```bash
python3 pipeline/task_queue.py cleanup --timeout 30
```

This releases any tasks claimed more than 30 minutes ago that were never completed.
```

---

## Part D: Documentation

### D1: Update CLAUDE.md

In the "Essential commands" section, add a new subsection:

```bash
# Task queue (parallel polishing)
python3 pipeline/task_queue.py populate --all              # Scan entries, populate queue for all task types
python3 pipeline/task_queue.py populate --task-type TYPE    # Populate queue for one task type
python3 pipeline/task_queue.py claim --task-type TYPE --count 25 --session-id ID  # Claim tasks
python3 pipeline/task_queue.py complete --task-ids ID1,ID2  # Mark tasks as done
python3 pipeline/task_queue.py release --session-id ID      # Release claimed tasks
python3 pipeline/task_queue.py status                       # Show queue statistics
python3 pipeline/task_queue.py cleanup --timeout 30         # Reclaim stale tasks (default 30 min)
```

In the "Project structure" section, update the pipeline/ listing to include:

```
  pipeline/task_queue.py    # Claim-based task queue for parallel polishing agents
  pipeline/task_queue.json  # Task queue data (auto-generated by populate)
```

In the "Task prompts" section, add:

```
- `queue_polishing_template.md` — template for queue-based polishing prompts
```

### D2: Update pipeline/README.md

Add a section documenting the task queue system. If `pipeline/README.md` does not exist, create it. The section should cover:

1. **Purpose**: Enable multiple parallel agents to work on polishing tasks without conflicts
2. **Task types**: List the five supported types (furigana, notes, examples, cross_refs, transitivity) with a one-line description of each
3. **Workflow**: populate -> claim -> process -> complete (with a diagram if helpful)
4. **Concurrency safety**: File-level locking ensures atomic claim/complete operations
5. **Stale task recovery**: The cleanup command reclaims tasks from crashed sessions
6. **Adding new task types**: Brief guide on how to add a new population function

### D3: Update Makefile

Add these targets:

```makefile
queue-populate:
	python3 pipeline/task_queue.py populate --all

queue-status:
	python3 pipeline/task_queue.py status

queue-cleanup:
	python3 pipeline/task_queue.py cleanup
```

Add all three to the `.PHONY` line.

---

## Verification

After all parts are complete:

```bash
# Script runs and shows help for all subcommands
python3 pipeline/task_queue.py --help
python3 pipeline/task_queue.py populate --help
python3 pipeline/task_queue.py claim --help
python3 pipeline/task_queue.py complete --help
python3 pipeline/task_queue.py release --help
python3 pipeline/task_queue.py status --help
python3 pipeline/task_queue.py cleanup --help

# End-to-end test
python3 pipeline/task_queue.py populate --all
python3 pipeline/task_queue.py status

# Test claim/complete cycle
SESSION_TEST="test-$(date +%s)"
CLAIMED=$(python3 pipeline/task_queue.py claim --task-type furigana --count 3 --session-id "$SESSION_TEST")
echo "Claimed: $CLAIMED"
python3 pipeline/task_queue.py status --verbose

# Complete the claimed tasks
python3 pipeline/task_queue.py complete --session-id "$SESSION_TEST"
python3 pipeline/task_queue.py status

# Test cleanup
python3 pipeline/task_queue.py cleanup --timeout 0

# Verify queue file is valid JSON
python3 -c "import json; json.load(open('pipeline/task_queue.json')); print('OK: queue file is valid JSON')"

# Full validation still passes
make validate

# Makefile targets work
make queue-status
```

Fix any issues found during verification.

---

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow."

1. **Create a feature branch**:
   ```bash
   git checkout -b enhancement/task-queue-system
   ```

2. **Run `make build`** to ensure all build artifacts are up to date

3. **Stage and commit all changes**:
   ```bash
   git add -A
   git commit -m "Add claim-based task queue for parallel polishing [2.2.2]

   - Create pipeline/task_queue.py with populate/claim/complete/release/status/cleanup commands
   - Support 5 task types: furigana, notes, examples, cross_refs, transitivity
   - File-level locking for concurrent agent safety
   - Stale task recovery via cleanup command
   - Create queue_polishing_template.md for prompt integration
   - Add queue targets to Makefile
   - Update CLAUDE.md and pipeline/README.md"
   ```

4. **Push** to the feature branch:
   ```bash
   git push -u origin enhancement/task-queue-system
   ```

5. **Create a PR**:
   ```bash
   gh pr create --repo tkgally/je-dict-1 \
     --head enhancement/task-queue-system \
     --base main \
     --title "Claim-based task queue for parallel polishing [2.2.2]" \
     --body "## Summary

   - New \`pipeline/task_queue.py\` enables multiple agents to claim and process polishing tasks without conflicts
   - Supports 5 task types: furigana, notes, examples, cross_refs, transitivity
   - File-level locking (\`fcntl\`) ensures atomic claim/complete operations
   - Stale task recovery via \`cleanup --timeout\` for crashed sessions
   - New \`prompts/queue_polishing_template.md\` shows prompt integration pattern

   ## Test plan
   - [ ] \`python3 pipeline/task_queue.py --help\` shows all subcommands
   - [ ] \`populate --all\` finds tasks for each type
   - [ ] \`claim\` + \`complete\` cycle works end-to-end
   - [ ] \`cleanup --timeout 0\` reclaims stale tasks
   - [ ] \`make validate\` passes
   - [ ] Queue file is valid JSON after all operations

   Enhancement plan: [2.2.2] Claim-Based Task Queue"
   ```

6. **Poll CI status** every 60 seconds:
   ```bash
   gh pr checks <number> --repo tkgally/je-dict-1
   ```
   Wait up to 10 minutes. If CI fails, read logs with `gh run view <run_id> --repo tkgally/je-dict-1 --log-failed`, fix, push, and repeat.

7. **Squash-merge** once CI is green:
   ```bash
   gh pr merge <number> --repo tkgally/je-dict-1 --squash
   ```

8. **Post-merge cleanup**:
   ```bash
   git checkout main && git pull origin main
   git status  # Should show nothing to commit
   git branch -d enhancement/task-queue-system
   git push origin --delete enhancement/task-queue-system
   ```

**CRITICAL**: The PR must include rebuilt `docs/` files from `make build`. If you commit source changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.
