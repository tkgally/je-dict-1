# Workflow & Autonomy — Prompt 7: Create status update and reporting system

**Source:** Agent 2 Report (Workflow & Autonomy), Phase 2, Prompt 7
**Priority:** Medium (Phase 2: Build the Task Runner)
**Effort:** Medium

---

**Post-01_code_prompt_12 note:** `build/report.py` already exists and provides a
dashboard summary of dictionary health (tier breakdown, POS stats, cross-reference
stats, example counts, inline link coverage, recent activity). The pipeline reporting
should complement it -- `build/report.py` is for overall dictionary health, while
`pipeline/update-status.py` is for tracking pipeline run progress.

**Post-01_code_prompt_07 note:** `entries_index.json` is now enriched with
`vocabulary_tier`, `part_of_speech`, `pos_tags`, `cross_reference_count`,
`example_count`, and `has_inline_links`. The update-brief.py script can use these
fields directly without loading individual entry files.

Create `pipeline/update-status.py` that: (1) reads the current pipeline-status.json,
(2) accepts task results as arguments (type, duration, items processed, status),
(3) updates the status file, (4) when called with --report flag, generates a
human-readable summary of the pipeline run. Consider calling `build/report.py`
at the end of a pipeline run to include a dictionary health snapshot in the report.

Also create `pipeline/update-brief.py` that reads the current state of the project
(entry count and stats from the enriched entries_index.json, candidate count from
candidate_words.json, polishing progress from progress.txt files) and regenerates
PROJECT_CONTEXT_BRIEF.md automatically.
