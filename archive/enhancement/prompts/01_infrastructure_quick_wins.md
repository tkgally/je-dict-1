# Infrastructure Quick Wins

**Enhancement plan sections**: [2.1.1] Auto-refresh BRIEF + [2.1.3] Session continuity + [2.3.1] Incremental validation

Three small, independent infrastructure improvements that reduce friction across all sessions.

## What This Prompt Creates/Modifies

| File | Action | Purpose |
|------|--------|---------|
| `.github/workflows/update-brief.yml` | **Create** | Post-merge workflow to auto-refresh PROJECT_CONTEXT_BRIEF.md |
| `prompts/resume-session.md` | **Create** | Session resume prompt template |
| `build/validate.py` | **Modify** | Add `--changed-only` and `--range` flags |
| `Makefile` | **Modify** | Add `validate-changed` target |
| `CLAUDE.md` | **Modify** | Document new commands and session-start guidance |

---

## Part A: Auto-refresh PROJECT_CONTEXT_BRIEF.md [2.1.1]

**Goal**: Ensure PROJECT_CONTEXT_BRIEF.md is always up to date when a session reads it. Two prongs: (1) auto-update after every merge to main, and (2) instruct sessions to refresh it at start.

### Step A1: Verify the existing script works

```bash
python3 pipeline/update-brief.py --dry-run
```

Confirm it runs without errors and produces reasonable output. If it fails, fix the issue before proceeding.

### Step A2: Create a post-merge GitHub Actions workflow

Create `.github/workflows/update-brief.yml` with these requirements:

- Triggers on `push` to `main` (this fires after every squash-merge)
- Checks out the repo
- Sets up Python 3.12
- Installs dependencies from `build/requirements.txt`
- Runs `python3 build/update_indexes.py` (to ensure entries_index.json is current)
- Runs `python3 pipeline/update-brief.py`
- If PROJECT_CONTEXT_BRIEF.md changed, commits and pushes directly to main
- Uses `github-actions[bot]` as the committer
- The commit message should be: `Auto-refresh PROJECT_CONTEXT_BRIEF.md [skip ci]`
- The `[skip ci]` in the commit message prevents an infinite loop of workflow triggers
- Needs `contents: write` permission

Here is the workflow structure:

```yaml
name: Update Brief

on:
  push:
    branches: [main]

permissions:
  contents: write

jobs:
  update-brief:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r build/requirements.txt

      - name: Update indexes and brief
        run: |
          python3 build/update_indexes.py
          python3 pipeline/update-brief.py

      - name: Commit if changed
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          if ! git diff --quiet PROJECT_CONTEXT_BRIEF.md; then
            git add PROJECT_CONTEXT_BRIEF.md
            git commit -m "Auto-refresh PROJECT_CONTEXT_BRIEF.md [skip ci]"
            git push
          else
            echo "PROJECT_CONTEXT_BRIEF.md is already up to date."
          fi
```

### Step A3: Update CLAUDE.md

In the "Essential commands" section, add under the existing commands:

```bash
python3 pipeline/update-brief.py          # Refresh PROJECT_CONTEXT_BRIEF.md from current data
```

Also add a note near the top of CLAUDE.md (after the "Entry basics" section or in a new "Session start" section) advising:

> **At session start**: Run `python3 pipeline/update-brief.py` before reading PROJECT_CONTEXT_BRIEF.md to ensure counts are current. (This is also run automatically after each merge to main via GitHub Actions.)

---

## Part B: Session Continuity [2.1.3]

**Goal**: Make it easier to resume multi-session tasks by standardizing session logs and providing a resume prompt.

### Step B1: Create `prompts/resume-session.md`

Create a prompt template that helps Claude resume a polishing task where the previous session left off. The prompt should:

1. Accept a task name parameter (the caller fills this in when invoking)
2. Read the progress file for that task (`polishing/tasks/{task}/progress.txt`)
3. Find and read the most recent session log for that task in `polishing/sessions/`
4. Summarize what the last session did, what entry to start from, and any notes
5. Then hand off to the task's main prompt

Write the file at `prompts/resume-session.md` with this content:

```markdown
# Resume Session

Resume a polishing task from where the previous session left off.

## Usage

Replace `{TASK}` below with the task name, then follow the instructions.

**Task to resume**: {TASK}

(Examples: `inline-links`, `example-sentences`, `furigana-completeness`, `furigana-correctness`, `semantic-labels`, `add_cross_references`)

## Steps

### 1. Read progress state

```bash
cat polishing/tasks/{TASK}/progress.txt
```

Note the `next:` value — this is where to resume.

If the progress file also contains a `last_session:` line, read that summary.

### 2. Find the most recent session log

```bash
ls -t polishing/sessions/{TASK}_* 2>/dev/null | head -1
```

If a log exists, read it to understand:
- What entry range was processed
- How many entries were modified
- Any unusual cases or decisions noted
- The "Next Entry" value (should match the progress file)

### 3. Summarize context

Before starting work, briefly state:
- **Resuming task**: {TASK}
- **Starting from entry**: (from progress file)
- **Last session processed**: (entry range from log, if available)
- **Notes from last session**: (anything relevant)

### 4. Begin the task

Now read and follow the main task prompt:

```bash
# Map task name to prompt file
```

| Task name | Prompt file |
|-----------|-------------|
| `inline-links` | `prompts/polish_add_inline_links.md` |
| `example-sentences` | `prompts/polish_example_sentences.md` |
| `furigana-completeness` | `prompts/polish_furigana_completeness.md` |
| `furigana-correctness` | `prompts/polish_furigana_correctness.md` |
| `semantic-labels` | `prompts/polish_semantic_labels.md` |
| `add_cross_references` | `prompts/add_cross-references.md` |

Read the corresponding prompt file and follow its instructions, starting from the entry indicated by the progress file.
```

### Step B2: Enhance progress file format

Update the convention for progress files to optionally include a brief last-session summary. This is a non-breaking change — the existing `next: XXXXX` format still works, and the extra line is ignored by scripts that only parse the `next:` line.

The enhanced format:

```
next: XXXXX
last_session: YYYY-MM-DD, entries AAAAA-BBBBB, N entries modified
```

Do NOT retroactively modify existing progress files. Instead, document this convention so that future sessions adopt it naturally.

Add a brief note to each of these polishing prompts, in their "Progress Update Format" or "When finishing" section, mentioning the optional `last_session:` line:

1. `prompts/polish_add_inline_links.md` — in the "Progress Update Format" section
2. `prompts/polish_example_sentences.md` — in its progress/finishing section
3. `prompts/polish_furigana_completeness.md` — in its progress/finishing section
4. `prompts/polish_furigana_correctness.md` — in its progress/finishing section
5. `prompts/polish_semantic_labels.md` — in its progress/finishing section

For each file, find the section that describes updating the progress file (typically showing `next: XXXXX`), and add:

```
Optionally, add a summary line for the next session:
```
next: XXXXX
last_session: YYYY-MM-DD, entries AAAAA-BBBBB, N entries modified
```
```

This is a minimal addition — do not restructure the existing prompts.

### Step B3: Document session log standard

In CLAUDE.md, in the section about polishing tasks (or near the "Task prompts" section), add a brief note:

> **Session log standard**: All polishing sessions should write a structured log to `polishing/sessions/{task}_{date}_{nnn}.md` when finishing. The log should include: date, entry range processed, list of changes made, any notes, and the next entry number. See existing logs in `polishing/sessions/` for examples.

---

## Part C: Incremental Validation [2.3.1]

**Goal**: Allow faster validation of just the entries that changed, useful during development and in CI for PRs.

### Step C1: Add `--changed-only` flag to `build/validate.py`

Modify the `main()` function in `build/validate.py` to add two new argument flags:

```python
parser.add_argument('--changed-only', action='store_true',
                    help='Validate only entry files changed since the last commit on main')
parser.add_argument('--range', nargs=2, metavar=('START', 'END'), type=int,
                    help='Validate entries in a specific numeric ID range (e.g., --range 10000 10499)')
```

**Implementation for `--changed-only`**:

1. Run `git diff --name-only origin/main...HEAD -- entries/` using `subprocess` to get the list of changed entry files (compared to main branch)
2. If on main (not a branch), fall back to `git diff --name-only HEAD~1 -- entries/` to compare against the previous commit
3. Filter to only `.json` files in the `entries/` directory
4. If no changed files are found, print "No changed entry files found." and exit 0
5. Validate only those files (still using the full schema and all checks)
6. Important: the duplicate-checking and cross-reference checks that depend on *all* entries still need the full entry set loaded. The simplest approach: load all entries for reference, but only report errors for the changed files. Alternatively, skip cross-reference and duplicate checks in `--changed-only` mode and note that limitation in the output.

The simpler approach (skip cross-entry checks) is acceptable and preferred:
- Validate each changed file against the schema
- Run per-file checks (filename, directory, furigana, etc.)
- Skip duplicate checks and cross-reference validation (those require the full corpus)
- Print a note: "Note: Cross-reference and duplicate checks skipped in --changed-only mode. Run full validation (`make validate`) to check those."

**Implementation for `--range`**:

1. Parse the START and END arguments as integers
2. When collecting entry files, filter to only those whose numeric ID (extracted from filename) falls within START..END inclusive
3. Run full validation (including duplicates and cross-refs) on that subset
4. This is useful for parallel sessions that work on non-overlapping ID ranges

**Both flags are mutually exclusive with `--entry` and `--id`**. Add a check: if `--changed-only` or `--range` is used together with `--entry` or `--id`, print an error and exit.

### Step C2: Update the Makefile

Add a new target to the Makefile:

```makefile
validate-changed:
	python3 build/validate.py --changed-only
```

Add `validate-changed` to the `.PHONY` line at the top.

Keep the existing `validate` target unchanged — it remains the full validation.

### Step C3: Update CLAUDE.md Essential Commands

In the "Essential commands" section of CLAUDE.md, add:

```bash
make validate-changed             # Validate only entries changed vs. main (fast)
python3 build/validate.py --range 10000 10499  # Validate a specific ID range
```

---

## Verification

After all three parts are complete, run these checks:

```bash
# Part A: verify the workflow file is valid YAML
python3 -c "import yaml; yaml.safe_load(open('.github/workflows/update-brief.yml'))" 2>/dev/null || python3 -c "import json; print('YAML check skipped — no yaml module, will be validated by CI')"

# Part B: verify the resume prompt exists
test -f prompts/resume-session.md && echo "OK: resume-session.md exists" || echo "MISSING"

# Part C: verify the new flags work
python3 build/validate.py --changed-only
python3 build/validate.py --range 1 100

# Full validation still works
make validate
```

Fix any issues found during verification.

---

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow."

1. **Run `make build`** to ensure all build artifacts are up to date
2. **Stage and commit all changes**:
   ```bash
   git add -A
   git commit -m "Infrastructure quick wins: auto-refresh BRIEF, session continuity, incremental validation

   - Add post-merge workflow to auto-refresh PROJECT_CONTEXT_BRIEF.md [2.1.1]
   - Create prompts/resume-session.md for session continuity [2.1.3]
   - Add --changed-only and --range flags to validate.py [2.3.1]
   - Add make validate-changed target
   - Update CLAUDE.md and polishing prompts with new conventions"
   ```
3. **Push** to the feature branch
4. **Create a PR**: `gh pr create --repo tkgally/je-dict-1 --head <branch> --base main --title "Infrastructure quick wins [2.1.1, 2.1.3, 2.3.1]" --body "..."`
5. **Poll CI status** every 60 seconds: `gh pr checks <number> --repo tkgally/je-dict-1` (allow up to 10 minutes)
6. **Squash-merge** once CI is green: `gh pr merge <number> --repo tkgally/je-dict-1 --squash`
7. **If CI fails**: read the error with `gh run view <run_id> --repo tkgally/je-dict-1 --log-failed`, fix, push, and repeat
8. **Post-merge cleanup**:
   ```bash
   git checkout main && git pull origin main
   git status  # Should show nothing to commit
   git branch -d <branch-name>
   git push origin --delete <branch-name>
   ```

**CRITICAL**: The PR must include rebuilt `docs/` files from `make build`. If you commit source changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.
