# Pipeline Configuration

Automated task queue for je-dict-1 dictionary maintenance. A pipeline config defines an ordered list of tasks that a runner script can execute sequentially, committing after each successful invocation.

## Files

| File | Purpose |
|------|---------|
| `run-pipeline.sh` | Runner script — executes tasks from config |
| `validate-task.sh` | Post-task validation gates — task-specific checks |
| `update-status.py` | Status tracking and report generation |
| `update-brief.py` | Regenerates PROJECT_CONTEXT_BRIEF.md from current data |
| `recommend-tasks.py` | Analyzes project state and recommends pipeline tasks |
| `pipeline-config.schema.json` | JSON Schema defining the config format |
| `pipeline-config.json` | Active pipeline configuration (edit this) |
| `pipeline-config.example.json` | Sample configuration for reference |
| `pipeline-status.json` | Generated: per-invocation results (gitignored) |
| `pipeline-report.txt` | Generated: summary report (gitignored) |
| `pipeline-*.log` | Generated: timestamped log files (gitignored) |

## Configuration format

```jsonc
{
  "description": "Human-readable label for this pipeline run",
  "branch": "main",          // default git branch for commits
  "on_failure": "stop",      // "stop" or "skip" — default failure behavior
  "tasks": [
    {
      "type": "new-entries",         // required — task type (see list below)
      "count": 3,                    // required — number of invocations
      "branch": "feature-branch",   // optional — override default branch
      "on_failure": "skip",          // optional — override default failure behavior
      "parameters": {                // optional — task-specific settings
        "batch_size": 30,
        "tier": "core"
      }
    }
  ]
}
```

## Task types

Each type maps to a prompt file in `prompts/`. The runner automatically uses batch-optimized versions from `prompts/batch/` when available (these are designed for non-interactive `claude --print` execution). If no batch version exists, the interactive version in `prompts/` is used as a fallback.

| Type | Interactive prompt | Batch prompt | Description |
|------|-------------------|--------------|-------------|
| `corpus-harvesting` | `corpus_harvesting.md` | `batch/corpus_harvesting.md` | Process corpus text to identify candidate words |
| `new-entries` | `newentries.md` | `batch/newentries.md` | Create new dictionary entries from candidates |
| `new-candidates` | `newcandidates.md` | — | Add new words to candidate_words.json |
| `clean-candidates` | `clean_up_candidates_list.md` | — | Review candidates for suitability |
| `inline-links` | `polish_add_inline_links.md` | `batch/polish_add_inline_links.md` | Add cross-reference links in examples and notes |
| `example-sentences` | `polish_example_sentences.md` | `batch/polish_example_sentences.md` | Improve example sentence quality |
| `furigana-completeness` | `polish_furigana_completeness.md` | — | Ensure all kanji have furigana |
| `furigana-correctness` | `polish_furigana_correctness.md` | — | Verify furigana readings are accurate |
| `semantic-labels` | `polish_semantic_labels.md` | — | Add/verify semantic labels on senses |
| `noentry-resolution` | `polish_add_entries_for_noentry_example_words.md` | — | Create entries for words used in examples |
| `expand-short-notes` | `expand-short-notes.md` | — | Expand abbreviated or shallow notes fields |

### Batch vs interactive prompts

Batch prompts (`prompts/batch/`) differ from interactive prompts in these ways:

- **No context reset**: Each invocation starts with a fresh context — no `/compact` or session continuity
- **Always commit**: Every batch invocation commits its work at the end
- **Never push**: The pipeline runner handles pushing after all tasks complete
- **Explicit exit**: Prompts include "exit cleanly" instructions to prevent extra work
- **Make targets**: Use `make validate` and `make build` (or `--quick`) for validation

## Top-level properties

| Property | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `description` | string | no | — | Label for this pipeline run |
| `branch` | string | no | `"main"` | Default git branch for commits |
| `on_failure` | `"stop"` \| `"skip"` | no | `"stop"` | What to do when a task fails validation |
| `tasks` | array | **yes** | — | Ordered list of tasks (at least one) |

## Task properties

| Property | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `type` | string | **yes** | — | One of the task types listed above |
| `count` | integer | **yes** | — | Number of invocations (≥ 1) |
| `branch` | string | no | top-level `branch` | Git branch override for this task |
| `on_failure` | string | no | top-level `on_failure` | Failure behavior override |
| `parameters` | object | no | — | Task-specific settings (see below) |

## Common parameters

These parameters are recognized by multiple task types. Tasks may also accept additional parameters specific to their prompt.

| Parameter | Type | Description |
|-----------|------|-------------|
| `batch_size` | integer | Number of entries to process per invocation |
| `entry_ids` | string[] | Specific entry IDs to target (e.g., `["01234", "05678"]`) |
| `tier` | `"basic"` \| `"core"` \| `"general"` | Restrict to entries in this vocabulary tier |
| `pos` | string | Restrict to entries with this part of speech |

## Usage

1. Copy `pipeline-config.example.json` to `pipeline-config.json`
2. Edit the tasks list to match your needs
3. Run the pipeline:

```bash
# Default config (pipeline/pipeline-config.json)
./pipeline/run-pipeline.sh

# Custom config file
./pipeline/run-pipeline.sh path/to/config.json

# Preview what would run without executing
./pipeline/run-pipeline.sh --dry-run

# Create a PR after completion
./pipeline/run-pipeline.sh --create-pr

# Combine flags
./pipeline/run-pipeline.sh --dry-run --create-pr path/to/config.json
```

### Runner behavior

For each task invocation, the runner:
1. Checks that the git working tree is clean
2. Switches to the configured branch (if different from current)
3. Snapshots progress tracking files (for stuck-loop detection)
4. Invokes `claude --print` with the task's prompt file, appending any parameters
5. Runs `validate-task.sh` with the task type as the quality gate
6. If validation passes, commits changes to the configured branch
7. If validation fails, discards changes and either stops or skips (per `on_failure`)
8. Records the result in `pipeline-status.json`

After all tasks complete:
- A summary report (with dictionary health snapshot) is written to `pipeline-report.txt`
- `PROJECT_CONTEXT_BRIEF.md` is regenerated with updated counts

### Validation gates

`validate-task.sh` provides task-type-specific validation beyond baseline `validate.py`:

| Task type | Additional checks |
|-----------|-------------------|
| `new-entries` | `find_missing_furigana.py` for new entries |
| `new-candidates` | `candidate_words.json` structure and count consistency |
| `clean-candidates` | `candidate_words.json` structure and count consistency |
| `corpus-harvesting` | `candidate_words.json` structure and count consistency |
| `inline-links` | Word link format check (`⟦surface→base：id⟧`) |
| `example-sentences` | Basic/core entries have ≥ 3 examples |
| `furigana-completeness` | `find_missing_furigana.py` gap report |
| `furigana-correctness` | Baseline validation (manual review recommended) |
| `semantic-labels` | `validate_tags.py` + `check_tag_consistency.py` |
| `noentry-resolution` | Same as `new-entries` |
| `expand-short-notes` | `find_missing_furigana.py` for notes fields |

All task types also check for stuck loops (progress file unchanged after task runs).

You can also run `validate-task.sh` standalone:

```bash
# Validate as if a new-entries task just ran
./pipeline/validate-task.sh new-entries

# With stuck-loop detection
./pipeline/validate-task.sh new-entries \
  --progress-file prompts/refactoring/progress.json \
  --pre-snapshot /tmp/snapshot-before.json
```

## Execution model

- Tasks execute in array order
- Each task's `count` determines how many separate Claude sessions are spawned
- After each session, `validate-task.sh` runs task-specific checks as a quality gate
- On validation failure, `on_failure` determines whether the pipeline stops or skips to the next invocation
- Each successful invocation is committed to the configured branch

## Status tracking (`update-status.py`)

Tracks pipeline run progress in `pipeline-status.json`. Called automatically by `run-pipeline.sh`, but can also be used standalone.

```bash
# Initialize a new status file
python3 pipeline/update-status.py init

# Record a task result
python3 pipeline/update-status.py record \
  --type new-entries --index 0 --invocation 1 \
  --status passed --message "OK" --duration 120

# Mark the pipeline run as finished
python3 pipeline/update-status.py finalize

# Generate a full report (written to pipeline-report.txt)
python3 pipeline/update-status.py report

# Generate report with dictionary health snapshot appended
python3 pipeline/update-status.py report --include-health

# One-line summary
python3 pipeline/update-status.py summary
```

## Task recommendations (`recommend-tasks.py`)

Analyzes the current project state (candidate count, inline link coverage, polishing backlogs) and suggests a pipeline configuration.

```bash
# Print recommendations with explanation
python3 pipeline/recommend-tasks.py

# Output only the JSON config
python3 pipeline/recommend-tasks.py --json

# Write directly to pipeline-config.json
python3 pipeline/recommend-tasks.py --write
```

Decision logic:
1. If `candidate_words.json` has < 100 candidates, recommend corpus harvesting
2. If candidates >= 100, recommend entry creation sessions (count = candidates / 30, capped at 5)
3. If more than 500 entries lack inline links, recommend inline-link sessions
4. Recommend one polishing session for whichever task has the most entries remaining

## Brief regeneration (`update-brief.py`)

Regenerates `PROJECT_CONTEXT_BRIEF.md` from `entries_index.json` and `candidate_words.json` without loading individual entry files. Called automatically at the end of a pipeline run.

```bash
# Regenerate the brief
python3 pipeline/update-brief.py

# Preview without writing
python3 pipeline/update-brief.py --dry-run
```
