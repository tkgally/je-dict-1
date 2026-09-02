# Queue-Based Polishing Template

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

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
