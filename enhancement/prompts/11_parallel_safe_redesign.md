# 11 — Parallel-Safe Prompt Redesign

**Enhancement plan section**: [2.2.1] Parallel-Safe Prompt Redesign
**Depends on**: None (but benefits from all earlier prompt work being complete)
**Estimated scope**: Medium — prompt modifications + new locking mechanism + coordinator script + docs

## What This Prompt Creates/Modifies

| Action | Path | Description |
|--------|------|-------------|
| Create | `build/entry_lock.py` | Entry-level locking with session IDs and expiry |
| Create | `build/parallel_coordinator.py` | Post-session branch merger and shared-file rebuilder |
| Modify | `prompts/polish_add_inline_links.md` | Add "Parallel Execution Mode" section |
| Modify | `prompts/polish_example_sentences.md` | Add "Parallel Execution Mode" section |
| Modify | `prompts/polish_furigana_completeness.md` | Add "Parallel Execution Mode" section |
| Modify | `prompts/polish_furigana_correctness.md` | Add "Parallel Execution Mode" section |
| Modify | `prompts/polish_semantic_labels.md` | Add "Parallel Execution Mode" section |
| Modify | `prompts/polish_aspect_notes.md` | Add "Parallel Execution Mode" section (if exists) |
| Modify | `prompts/add_cross-references.md` | Add "Parallel Execution Mode" section |
| Modify | `Makefile` | Add `lock-status` target |
| Modify | `CLAUDE.md` | Document parallel execution model |

---

## Part A: Analyze Conflict Points

Before writing any code, read the following files and understand their shared-resource patterns. This analysis drives the design of Parts B-E.

### Step A1: Map shared resources

Read each polishing prompt and identify what shared resources it touches:

```bash
# Read all polishing prompts
cat prompts/polish_add_inline_links.md
cat prompts/polish_example_sentences.md
cat prompts/polish_furigana_completeness.md
cat prompts/polish_furigana_correctness.md
cat prompts/polish_semantic_labels.md
cat prompts/add_cross-references.md
```

If `prompts/polish_aspect_notes.md` exists (created by enhancement prompt 03), read it too.

Confirm the following shared-resource inventory:

| Resource | Modified by | Conflict risk |
|----------|-------------|---------------|
| `polishing/tasks/{task}/progress.txt` | Each polishing prompt (its own file) | **Low** — each task has its own file; parallel sessions doing DIFFERENT tasks won't conflict |
| `entries/{range}/{id}_{romaji}.json` | All polishing prompts | **HIGH** — two sessions modifying the same entry will conflict |
| `entries_index.json` | `update_indexes.py` (called during `make build`) | **Medium** — regenerated from entries, so the last writer wins |
| `candidate_words.json` | `update_indexes.py` sync, entry creation prompts | **Medium** — entry creation removes candidates; polishing doesn't touch it |
| `build/word_id_lookup.json` | `update_indexes.py` / `generate_word_lookup.py` | **Low** — fully regenerated |
| `docs/` | `build_flat.py` (called during `make build`) | **Low** — fully regenerated; conflicts are meaningless |
| `kanji/` | `update_kanji_index.py` | **Low** — only after new entry creation with new kanji |

### Step A2: Identify the safe parallel patterns

From the analysis above, two sessions can run safely in parallel if:

1. **They don't modify the same entries** (non-overlapping ID ranges).
2. **They defer shared-file regeneration** (skip `update_indexes.py`, `build_flat.py`, `update_kanji_index.py`).
3. **A coordinator step runs after both sessions complete** to regenerate shared files.

The design principle: **entry files are the source of truth; everything else is derived**. Parallel sessions only modify entry files. A single coordinator pass regenerates all derived files afterward.

---

## Part B: Add ID Range Parameters to Polishing Prompts

**Goal**: Allow each polishing prompt to operate on a specific ID range instead of sequential progress-file tracking. This makes it safe for two sessions to run the same polishing task simultaneously on non-overlapping ranges.

### Step B1: Design the "Parallel Execution Mode" section

Create a standard section that will be added to each polishing prompt. The section text is:

```markdown
## Parallel Execution Mode

This task supports parallel execution when given an explicit ID range. Two or more sessions can run this task simultaneously on non-overlapping ID ranges.

### How to invoke

When starting the session, specify a range:
> "Process entries 10000-10499 only."

### Behavior in parallel mode

When an ID range is given:
1. **Ignore** `progress.txt` — do not read it or update it
2. **Process only** entry files whose numeric ID falls within the given range (inclusive)
3. **Skip shared-file updates**: do NOT run `update_indexes.py`, `build_flat.py`, or `update_kanji_index.py`
4. **Commit entry changes only**: `git add entries/ polishing/sessions/ && git commit -m "..."`
5. **Do NOT run `make build`** — a coordinator will do this after all parallel sessions complete
6. **Do NOT push to main** — push to a feature branch and create a PR, but do NOT merge it. The coordinator will handle merging.

### After parallel sessions complete

A coordinator step (run manually or via `build/parallel_coordinator.py`) will:
1. Merge all parallel session branches
2. Run `update_indexes.py`, `build_flat.py`, and other shared-file regeneration
3. Create a single combined PR

### When NO range is given

Operate in **legacy sequential mode**: read `progress.txt`, process entries sequentially from that point, update `progress.txt`, and run `make build` as usual. This is the default behavior.
```

### Step B2: Add the section to each polishing prompt

For each of the following files, add the "Parallel Execution Mode" section **immediately before** the "PR and Merge Workflow" section (or, if the prompt lacks that section, at the end before any "Output at Session End" section):

1. **`prompts/polish_add_inline_links.md`**
   - Find the line `## PR and Merge Workflow` and insert the parallel execution section above it.

2. **`prompts/polish_example_sentences.md`**
   - This prompt may not have a "PR and Merge Workflow" section. If so, add the parallel execution section before "Output at Session End".

3. **`prompts/polish_furigana_completeness.md`**
   - Same approach: insert before "PR and Merge Workflow" or "Output at Session End".

4. **`prompts/polish_furigana_correctness.md`**
   - Same approach.

5. **`prompts/polish_semantic_labels.md`**
   - Same approach.

6. **`prompts/add_cross-references.md`**
   - This prompt uses a different tracking mechanism (tracking file, not progress.txt). In parallel mode, the range still applies: process only entries in the given ID range, skip the tracking file.
   - Adjust the parallel section text to say "Ignore the tracking file" instead of "Ignore progress.txt".

7. **`prompts/polish_aspect_notes.md`** (if it exists — created by enhancement prompt 03)
   - Same approach as other polishing prompts.

**Important**: Do NOT restructure or rewrite the existing prompts. Only ADD the new section in the appropriate location. Preserve all existing content exactly as-is.

### Step B3: Modify the batch commit instructions

In each prompt's "After every N entries" section (the periodic commit step), add a conditional note:

```
   **In parallel mode**: Replace `git add -A` with `git add entries/ polishing/sessions/` to avoid staging shared files.
```

Find the relevant commit instruction in each prompt (typically `git add -A && git commit`) and add this note directly below it. Do not change the existing command — just add the note as a line below.

---

## Part C: Create Entry-Level Locking

**Goal**: Provide a lightweight locking mechanism so parallel sessions can detect if another session is working on an entry range. This is advisory (not enforced) — it helps prevent accidental overlap but doesn't block execution.

### Step C1: Create `build/entry_lock.py`

Create the file at `build/entry_lock.py` with the following functionality:

```python
#!/usr/bin/env python3
"""
Advisory entry-level locking for parallel dictionary sessions.

Provides a lightweight mechanism to signal which entry ranges are being
worked on by active sessions. Locks are advisory — they help prevent
accidental overlap but do not block execution.

Usage:
    python3 build/entry_lock.py lock --range 10000 10499 --session "inline-links-session-1"
    python3 build/entry_lock.py unlock --range 10000 10499 --session "inline-links-session-1"
    python3 build/entry_lock.py check --range 10000 10499
    python3 build/entry_lock.py status
    python3 build/entry_lock.py clean
"""
```

**Commands**:

1. **`lock --range START END --session SESSION_ID`**
   - Creates a lock file at `polishing/locks/{START}_{END}_{SESSION_ID}.lock`
   - The lock file content is JSON:
     ```json
     {
       "range_start": 10000,
       "range_end": 10499,
       "session_id": "inline-links-session-1",
       "locked_at": "2026-04-09T12:00:00Z",
       "expires_at": "2026-04-09T12:30:00Z"
     }
     ```
   - Before creating, check if any existing lock overlaps with the requested range. If overlap found, print a warning (but still create the lock — it's advisory).
   - Create the `polishing/locks/` directory if it doesn't exist.

2. **`unlock --range START END --session SESSION_ID`**
   - Removes the matching lock file.
   - If no matching lock exists, print a warning and exit 0.

3. **`check --range START END`**
   - Scans all lock files for any that overlap with the given range.
   - Reports overlapping locks (session ID, time remaining).
   - Skips expired locks (older than 30 minutes).
   - Exits 0 if no active overlapping locks, exits 1 if overlaps found.

4. **`status`**
   - Lists all active (non-expired) locks.
   - Reports: range, session ID, time remaining.
   - If no active locks, prints "No active locks."

5. **`clean`**
   - Removes all expired lock files (those older than 30 minutes).
   - Reports how many were cleaned.

**Implementation notes**:
- Lock expiry is 30 minutes from creation.
- Use UTC timestamps consistently.
- Range overlap detection: two ranges [A, B] and [C, D] overlap if A <= D and C <= B.
- Add `polishing/locks/` to `.gitignore` (lock files should NOT be committed).
- Make the script executable (`#!/usr/bin/env python3`).
- Use `argparse` for subcommands.

### Step C2: Update `.gitignore`

Check if `.gitignore` exists at the project root. If it does, add:

```
polishing/locks/
```

If `.gitignore` does not exist, create it with that single line.

---

## Part D: Create Coordinator Script

**Goal**: After parallel sessions complete, a coordinator merges their changes and regenerates all shared files in a single pass.

### Step D1: Create `build/parallel_coordinator.py`

Create the file at `build/parallel_coordinator.py` with the following functionality:

```python
#!/usr/bin/env python3
"""
Coordinate parallel session results into a single clean merge.

After two or more parallel sessions have completed (each on its own branch
with only entry-file changes committed), this script:
1. Validates that the branches modify non-overlapping entry files
2. Merges each branch into the current branch
3. Runs shared-file regeneration (update_indexes, build_flat, etc.)
4. Reports the combined result

Usage:
    python3 build/parallel_coordinator.py branch1 branch2 [branch3 ...]
    python3 build/parallel_coordinator.py --dry-run branch1 branch2
    python3 build/parallel_coordinator.py --validate-only branch1 branch2
"""
```

**Arguments**:
```python
parser = argparse.ArgumentParser(description='Coordinate parallel session branches.')
parser.add_argument('branches', nargs='+', help='Branch names to merge')
parser.add_argument('--dry-run', action='store_true',
                    help='Show what would be done without making changes')
parser.add_argument('--validate-only', action='store_true',
                    help='Check for conflicts without merging')
parser.add_argument('--skip-build', action='store_true',
                    help='Skip the build step after merging')
```

**Step 1 — Validate branches**:
1. For each branch, run `git diff --name-only main...<branch> -- entries/` to get the list of modified entry files.
2. Check for overlap: if any entry file appears in more than one branch, report the conflict and abort (unless `--dry-run`).
3. Also check for non-entry modifications: warn if any branch modifies files outside `entries/` and `polishing/sessions/` (these should not be committed in parallel mode).

**Step 2 — Merge branches** (skip if `--dry-run` or `--validate-only`):
1. Ensure we're on a clean working tree (`git status --porcelain` is empty).
2. For each branch in order:
   ```bash
   git merge --no-ff <branch> -m "Merge parallel session: <branch>"
   ```
3. If a merge conflict occurs, abort the merge, report the conflicting files, and exit with an error.

**Step 3 — Regenerate shared files** (skip if `--skip-build`):
1. Run the full post-creation sequence:
   ```bash
   python3 build/validate.py
   python3 build/update_indexes.py
   python3 build/update_kanji_index.py --check-new
   python3 build/build_flat.py
   ```
2. If any step fails, report the error and stop.

**Step 4 — Report**:
1. Print a summary:
   ```
   === PARALLEL COORDINATION COMPLETE ===
   Branches merged: N
     - branch1: M entries modified
     - branch2: K entries modified
   Total entries modified: M+K
   Shared files regenerated: yes
   Ready to commit and push.
   ```

**Step 5 — Commit** (skip if `--dry-run`):
1. Stage all changes: `git add -A`
2. Do NOT commit automatically — print a message telling the operator to review and commit:
   ```
   All changes staged. Review with 'git diff --cached' and commit:
     git commit -m "Coordinated merge of N parallel sessions"
   ```

**Implementation notes**:
- Use `subprocess.run` for all git commands, with `check=True` and `capture_output=True`.
- Handle the case where a branch doesn't exist (print error, skip it).
- Handle the case where we're not on the expected base branch (warn).
- The script should be run from the project root directory.
- Make the script executable (`#!/usr/bin/env python3`).

---

## Part E: Update CLAUDE.md

**Goal**: Document the parallel execution model so future sessions know how to use it.

### Step E1: Add a "Parallel Execution" section

In `CLAUDE.md`, add a new section after the "Task prompts" section and before "Skills (detailed guidelines)". Title it `## Parallel Execution`.

Content:

```markdown
## Parallel Execution

Two or more Claude Code sessions can safely run polishing tasks simultaneously on non-overlapping ID ranges.

### How to run two sessions simultaneously

1. **Choose non-overlapping ID ranges**: Divide the entry space (roughly 00001-23000) into ranges. Use 500-entry blocks aligned with directory boundaries (e.g., 10000-10499, 10500-10999).

2. **Start each session with a range directive**: Tell each session which range to process:
   > "Read prompts/polish_furigana_completeness.md and follow the instructions. Process entries 10000-10499 only."

3. **Each session creates its own branch**: Sessions commit only entry changes and session logs to their branch. They do NOT run `make build` or `update_indexes.py`.

4. **After all sessions complete, run the coordinator**:
   ```bash
   python3 build/parallel_coordinator.py branch1 branch2
   ```
   This validates non-overlap, merges branches, and regenerates all shared files.

5. **Create a single PR from the coordinated result**.

### ID range assignment guidelines

- Use 500-entry blocks aligned with directory boundaries: 00000-00499, 00500-00999, etc.
- For two sessions: split the remaining entry space roughly in half.
- For polishing tasks with progress tracking: start from the current `next:` value and assign consecutive blocks.
- Record the range assignments so they don't overlap.

### Entry locking (advisory)

```bash
python3 build/entry_lock.py lock --range 10000 10499 --session "session-1"
python3 build/entry_lock.py check --range 10500 10999   # Check before starting
python3 build/entry_lock.py status                       # See all active locks
python3 build/entry_lock.py unlock --range 10000 10499 --session "session-1"
python3 build/entry_lock.py clean                        # Remove expired locks
```

Locks are advisory and expire after 30 minutes. They help prevent accidental overlap but do not block execution.

### What CAN run in parallel

- Two different polishing tasks (e.g., furigana + inline links) on the same entries — generally safe if they modify different fields, but use separate branches to be safe.
- The same polishing task on non-overlapping ID ranges — fully safe.
- One polishing session + one entry creation session — safe if the polishing session doesn't touch newly created entries.

### What CANNOT run in parallel

- Two sessions modifying the same entry file — will cause merge conflicts.
- Two sessions both running `make build` — unnecessary and may produce different outputs.
- Two entry creation sessions — both modify `candidate_words.json`.
```

### Step E2: Add commands to "Essential commands"

In the "Essential commands" section, add:

```bash
# Parallel execution
python3 build/entry_lock.py status            # Show active entry locks
python3 build/entry_lock.py lock --range 10000 10499 --session "my-session"
python3 build/entry_lock.py unlock --range 10000 10499 --session "my-session"
python3 build/parallel_coordinator.py branch1 branch2  # Merge parallel session branches
```

### Step E3: Add Makefile target

Add to the Makefile:

```makefile
lock-status:
	python3 build/entry_lock.py status
```

Add `lock-status` to the `.PHONY` line.

---

## Verification

After all parts are complete, run these checks:

```bash
# Verify entry_lock.py works
python3 build/entry_lock.py status
python3 build/entry_lock.py lock --range 10000 10499 --session "test-session"
python3 build/entry_lock.py check --range 10200 10300
python3 build/entry_lock.py status
python3 build/entry_lock.py unlock --range 10000 10499 --session "test-session"
python3 build/entry_lock.py status
python3 build/entry_lock.py clean

# Verify parallel_coordinator.py parses arguments (no branches to merge, should show usage or error)
python3 build/parallel_coordinator.py --dry-run nonexistent-branch 2>&1 || true

# Verify each modified polishing prompt still has valid structure
# (Just check that the parallel section was added)
grep -l "Parallel Execution Mode" prompts/polish_*.md prompts/add_cross-references.md

# Verify CLAUDE.md was updated
grep "Parallel Execution" CLAUDE.md

# Verify .gitignore has locks directory
grep "polishing/locks" .gitignore

# Full validation still passes
make validate

# Makefile target works
make lock-status
```

Fix any errors found during verification.

---

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow."

1. **Run `make build`** to ensure all build artifacts are up to date
2. **Create a feature branch, stage, and commit all changes**:
   ```bash
   git checkout -b enhancement/11-parallel-safe-redesign
   git add -A
   git commit -m "Add parallel-safe execution support for polishing tasks [2.2.1]

   - Create build/entry_lock.py for advisory entry-range locking
   - Create build/parallel_coordinator.py for post-session branch merging
   - Add Parallel Execution Mode section to all polishing prompts
   - Add parallel execution documentation to CLAUDE.md
   - Add make lock-status target
   - Add polishing/locks/ to .gitignore"
   ```
3. **Push** to the feature branch:
   ```bash
   git push -u origin enhancement/11-parallel-safe-redesign
   ```
4. **Create a PR**:
   ```bash
   gh pr create --repo tkgally/je-dict-1 \
     --head enhancement/11-parallel-safe-redesign \
     --base main \
     --title "Parallel-safe prompt redesign [2.2.1]" \
     --body "$(cat <<'EOF'
   ## Summary
   - All polishing prompts now support an optional ID range parameter for parallel execution
   - New `build/entry_lock.py` provides advisory entry-range locking with 30-minute expiry
   - New `build/parallel_coordinator.py` validates and merges parallel session branches, then regenerates shared files
   - CLAUDE.md documents the parallel execution model with guidelines for range assignment and coordination
   - Lock files excluded from git via .gitignore

   Implements enhancement plan section [2.2.1].

   ## Test plan
   - [ ] `python3 build/entry_lock.py status` runs without errors
   - [ ] Lock/check/unlock cycle works correctly
   - [ ] `python3 build/parallel_coordinator.py --dry-run nonexistent` handles missing branch gracefully
   - [ ] All polishing prompts contain "Parallel Execution Mode" section
   - [ ] CLAUDE.md contains "Parallel Execution" section
   - [ ] `polishing/locks/` is in .gitignore
   - [ ] `make lock-status` works
   - [ ] `make validate` passes
   - [ ] `make build` succeeds
   - [ ] Existing polishing prompt behavior unchanged when no range is given
   EOF
   )"
   ```
5. **Poll CI status** every 60 seconds: `gh pr checks <number> --repo tkgally/je-dict-1` (allow up to 10 minutes)
6. **Squash-merge** once CI is green: `gh pr merge <number> --repo tkgally/je-dict-1 --squash`
7. **If CI fails**: read logs with `gh run view <run_id> --repo tkgally/je-dict-1 --log-failed`, fix, push, and repeat from step 5
8. **Post-merge cleanup**:
   ```bash
   git checkout main && git pull origin main
   git status  # Should show nothing to commit
   git branch -d enhancement/11-parallel-safe-redesign
   git push origin --delete enhancement/11-parallel-safe-redesign
   ```

**CRITICAL**: The PR must include rebuilt `docs/` files from `make build`. If you commit source changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.
