# Daily Workflow Guide

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

How to use the je-dict-1 pipeline for routine dictionary maintenance.

## Prerequisites

- Python 3.12+
- `claude` CLI installed and authenticated
- `gh` CLI installed (only needed for `--create-pr`)
- Repository cloned with a clean working tree

## Quick start

```bash
# 1. Get task recommendations based on project state
python3 pipeline/recommend-tasks.py

# 2. Write recommendations directly to pipeline-config.json
python3 pipeline/recommend-tasks.py --write

# 3. Preview what will run
./pipeline/run-pipeline.sh --dry-run

# 4. Launch the pipeline
./pipeline/run-pipeline.sh
```

---

## 1. Configuring a pipeline run

### Option A: Use the recommender

The recommender analyzes candidate counts, inline link coverage, and polishing backlogs to suggest a balanced workload:

```bash
python3 pipeline/recommend-tasks.py          # print recommendations
python3 pipeline/recommend-tasks.py --json   # JSON only
python3 pipeline/recommend-tasks.py --write  # write to pipeline-config.json
```

### Option B: Edit the config manually

Edit `pipeline/pipeline-config.json` directly. Use the example config as a starting point:

```bash
cp pipeline/pipeline-config.example.json pipeline/pipeline-config.json
```

Then adjust the `tasks` array. Each task needs a `type` and `count`:

```json
{
  "description": "Tuesday maintenance run",
  "branch": "main",
  "on_failure": "skip",
  "tasks": [
    { "type": "new-entries", "count": 3, "parameters": { "batch_size": 30 } },
    { "type": "inline-links", "count": 2, "parameters": { "batch_size": 15 } }
  ]
}
```

Available task types: `corpus-harvesting`, `new-entries`, `new-candidates`, `clean-candidates`, `inline-links`, `example-sentences`, `furigana-completeness`, `furigana-correctness`, `semantic-labels`, `noentry-resolution`, `expand-short-notes`.

See `pipeline/README.md` for full parameter documentation.

### Option C: Use a separate config file

Keep named configs for different workflows:

```bash
./pipeline/run-pipeline.sh configs/heavy-entry-creation.json
./pipeline/run-pipeline.sh configs/polish-only.json
```

## 2. Launching a pipeline run

### From the terminal

```bash
# Dry run first to verify the config
./pipeline/run-pipeline.sh --dry-run

# Run for real
./pipeline/run-pipeline.sh

# Run and create a PR when finished
./pipeline/run-pipeline.sh --create-pr
```

### From GitHub Actions (browser/phone)

You can trigger a pipeline run from any browser without a terminal:

1. Go to **Actions** → **Run Pipeline** in the GitHub repository
2. Click **Run workflow**
3. Configure inputs (config file, branch name, dry run, create PR)
4. Click **Run workflow**

This requires an `ANTHROPIC_API_KEY` repository secret. See `pipeline/README.md` for setup details.

### What the runner does

The runner executes tasks sequentially. For each invocation it:
1. Calls `claude --print` with the task's prompt
2. Runs task-specific validation via `validate-task.sh`
3. Commits on success, discards on failure
4. Records results in `pipeline-status.json`

You can leave this running unattended. Output is logged to a timestamped file in `pipeline/`.

## 3. Reviewing results

### Summary report

After a run completes, check the generated report:

```bash
cat pipeline/pipeline-report.txt
```

This shows pass/fail counts per task, overall success rate, and (if available) a dictionary health snapshot.

### Status details

For per-invocation detail:

```bash
# One-line summary
python3 pipeline/update-status.py summary

# Full report (regenerates pipeline-report.txt)
python3 pipeline/update-status.py report

# With dictionary health snapshot
python3 pipeline/update-status.py report --include-health
```

### Dictionary health dashboard

Run the health dashboard independently to see tier breakdown, cross-reference stats, example counts, and more:

```bash
make report
```

### Pull request review

If you used `--create-pr`, review the PR on GitHub. The PR body includes a summary of what changed. Review the diff for:
- Correct furigana on new entries
- Reasonable example sentences
- Accurate cross-references
- No regressions in existing entries

## 4. Spot-check reviews

Periodically review a sample of pipeline-generated work for quality. Focus on these areas:

### Entry quality checks

```bash
# Pick a few recent entries and read them
python3 build/report.py                     # see recent activity
python3 build/verify_furigana.py <entry_id> # check furigana for an entry
make validate                               # full validation pass
```

### What to look for

- **Furigana accuracy**: Are readings correct? Any missing furigana on kanji?
- **Example sentences**: Do they sound natural? Are they at the right difficulty level for the entry's tier?
- **Notes quality**: Are notes helpful for learners? Any factual errors?
- **Cross-references**: Do linked entries actually exist? Are relationships accurate?
- **Inline word links**: Do `⟦surface→base：id⟧` links point to the right entries?

### Spot-check process

1. Run `make report` and note entries modified in the last pipeline run
2. Open 5-10 entries at random from the output
3. Read through headwords, senses, examples, and notes
4. Fix any issues manually or queue them as pipeline tasks
5. Run `make validate` after any manual fixes

## 5. Handling validation failures

When a task invocation fails validation, the pipeline either stops or skips based on the `on_failure` setting.

### Diagnosing failures

```bash
# Check the log file for error details
cat pipeline/pipeline-*.log | tail -50

# Check the status file for which task failed
python3 pipeline/update-status.py summary

# Run validation manually to see the errors
make validate
```

### Common failure causes

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Missing furigana | Claude forgot to add readings | Run `furigana-completeness` task |
| Schema validation error | Malformed entry JSON | Manually fix the entry, run `make validate` |
| Stuck loop detected | Claude made no progress | Check the prompt — the task may be finished |
| Candidate count unchanged | Corpus harvesting found nothing | Try a different corpus source |
| Invalid word link format | Malformed `⟦...⟧` syntax | Run `inline-links` again or fix manually |

### Recovery steps

1. Check the log to understand what happened
2. If the entry is salvageable, fix it manually and commit
3. If not, the pipeline already discarded the bad changes
4. Adjust the config (e.g., reduce `batch_size`) and re-run
5. Set `"on_failure": "skip"` if you want the pipeline to continue past failures

## 6. Adding new task types

To add a new task type to the pipeline:

### Step 1: Create the prompt

Write a prompt file in `prompts/`. For pipeline use, also create a batch version in `prompts/batch/` with these adjustments:
- No context reset or `/compact` instructions
- Always commit at the end
- Never push (the runner handles this)
- Include "exit cleanly" instructions

### Step 2: Update the schema

Add the new type name to the `type` enum in `pipeline/pipeline-config.schema.json`:

```json
"enum": [
  "corpus-harvesting",
  "new-entries",
  ...
  "your-new-type"
]
```

### Step 3: Add validation

Add a case for the new type in `pipeline/validate-task.sh`:

```bash
your-new-type)
  log "Running your-new-type specific checks..."
  # Add validation commands here
  ;;
```

### Step 4: Map the prompt

Add the type-to-prompt mapping in `run-pipeline.sh`'s `prompt_file_for_type()` function. The runner checks for a batch version at `prompts/batch/<filename>` first, then falls back to `prompts/<filename>`.

### Step 5: Update documentation

Add the new type to the task type table in `pipeline/README.md`.

---

## Example daily routines

### Morning launch

Set up the pipeline before starting other work.

```bash
cd /path/to/je-dict-1
git pull origin main

# Let the recommender pick tasks
python3 pipeline/recommend-tasks.py --write

# Preview and launch
./pipeline/run-pipeline.sh --dry-run
./pipeline/run-pipeline.sh --create-pr
```

The pipeline runs in the background. Check back later.

### Evening review

Review what the pipeline produced during the day.

```bash
# Check the summary
python3 pipeline/update-status.py summary

# Read the full report
cat pipeline/pipeline-report.txt

# Run the health dashboard
make report

# Review the PR if one was created
gh pr list

# Spot-check a few entries from the run
# (pick entry IDs from the report or git log)
git log --oneline -20
```

If everything looks good, merge the PR. If adjustments are needed, fix them manually and push, or adjust the config for the next run.

### Weekend audit

A more thorough review of the week's work.

```bash
# Full validation
make validate

# Health dashboard
make report

# Review the week's commits
git log --oneline --since="7 days ago"

# Check for entries with potential issues
python3 build/find_missing_furigana.py
python3 build/validate_tags.py

# Rebuild the site to verify rendering
make build

# Plan next week's tasks
python3 pipeline/recommend-tasks.py
```

Focus areas for the weekend audit:
- Read through 15-20 entries created during the week
- Verify cross-references point to real entries
- Check that example sentences use appropriate vocabulary for their tier
- Look for duplicate or near-duplicate entries
- Update `candidate_words.json` if needed
- Adjust pipeline config for the coming week based on what you find
