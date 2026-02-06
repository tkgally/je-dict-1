# Workflow & Autonomy — Prompt 6: Create post-task validation gates

**Source:** Agent 2 Report (Workflow & Autonomy), Phase 2, Prompt 6
**Priority:** Medium (Phase 2: Build the Task Runner)
**Effort:** Medium

---

Create `pipeline/validate-task.sh` that takes a task type as argument and runs the
appropriate validation suite. For new-entries: validate.py + find_missing_furigana.py.
For inline-links: validate.py with word-link grep. For example-sentences: validate.py +
example count check. For semantic-labels: validate_tags.py + validate.py. For
corpus-harvesting: JSON syntax check on candidate_words.json. For all tasks: verify
that the progress file has advanced (detect stuck loops). Return exit code 0 for pass,
1 for fail.
