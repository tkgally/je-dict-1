# Workflow & Autonomy — Prompt 7: Create status update and reporting system

**Source:** Agent 2 Report (Workflow & Autonomy), Phase 2, Prompt 7
**Priority:** Medium (Phase 2: Build the Task Runner)
**Effort:** Medium

---

Create `pipeline/update-status.py` that: (1) reads the current pipeline-status.json,
(2) accepts task results as arguments (type, duration, items processed, status),
(3) updates the status file, (4) when called with --report flag, generates a
human-readable summary of the pipeline run. Also create `pipeline/update-brief.py`
that reads the current state of the project (entry count from entries_index.json,
candidate count from candidate_words.json, polishing progress from progress.txt files)
and regenerates PROJECT_CONTEXT_BRIEF.md automatically.
