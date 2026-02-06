# Workflow & Autonomy — Prompt 10: Create a task scheduler recommendation script

**Source:** Agent 2 Report (Workflow & Autonomy), Phase 3, Prompt 10
**Priority:** Medium (Phase 3: Optimize Task Prompts)
**Effort:** Medium

---

Create `pipeline/recommend-tasks.py` that examines the current project state and
recommends what the next pipeline run should contain. Logic: (1) if candidate_words.json
has fewer than 100 candidates, recommend corpus harvesting, (2) if candidate count is
over 100, recommend entry creation sessions (count = candidates / 30, capped at 5),
(3) if inline links progress is more than 500 entries behind the latest entry,
recommend inline link sessions, (4) recommend one polishing session for whichever
polishing task has the most entries remaining. Output a suggested pipeline-config.json.
