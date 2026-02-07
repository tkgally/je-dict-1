# Refactoring Master Prompt

You are working through a series of refactoring and improvement prompts for the je-dict-1 project. These prompts come from four assessment reports and are tracked in `prompts/refactoring/progress.json`.

## Your task

1. **Read the progress file** at `prompts/refactoring/progress.json`
2. **Find the next pending prompt** — the first entry in the `prompts` array with `"status": "pending"`
3. **Read that prompt file** at `prompts/refactoring/{id}.md`
4. **Execute the prompt** — follow its instructions completely
5. **Update progress** — after completing the work:
   - Edit `prompts/refactoring/progress.json`:
     - Set the completed prompt's `status` to `"completed"`
     - Set its `completed_date` to today's date (YYYY-MM-DD format)
     - Optionally add any relevant `notes` (e.g., "skipped 3 files that didn't exist", "also fixed related issue in X")
     - Update `last_updated` to today's date
6. **Run validation** — always run `python3 build/validate.py` after making changes
7. **Commit your work** with a descriptive commit message referencing the prompt ID

## Important rules

- Do **one prompt per session**. After completing a prompt and updating progress, stop.
- If a prompt cannot be completed (e.g., a prerequisite prompt hasn't been done yet, or the task no longer applies), set its status to `"skipped"` with a note explaining why, then move on to the next pending prompt.
- If a prompt is marked as repeating (e.g., "session 1 of ~10"), complete one session's worth of work and mark it as `"completed"`. The user will re-queue it if more sessions are needed.
- Always validate and test as specified in each prompt before marking complete.

## Progress summary

To see a quick summary of progress, you can count statuses in progress.json:
- **pending**: Not yet started
- **completed**: Done
- **skipped**: Intentionally skipped (with reason in notes)

## Prompt categories

| Prefix | Category | Count | Source Report |
|--------|----------|-------|---------------|
| `01_code_prompt_*` | Code & Structure | 23 | Agent 1 + Agent Team 5 |
| `02_workflow_prompt_*` | Workflow & Autonomy | 12 | Agent 2 |
| `03_learner_prompt_*` | Learner Experience | 10 | Agent 3 |
| `04_lexicographic_prompt_*` | Lexicographic Quality | 10 | Agent 4 |

**Total: 55 prompts**

## Execution order

The prompts are listed in progress.json in the recommended execution order:
1. Code & Structure prompts first (infrastructure improvements)
2. Workflow & Autonomy prompts second (process improvements)
3. Learner Experience prompts third (content/UI improvements)
4. Lexicographic Quality prompts last (content quality improvements)

This order ensures infrastructure is solid before building on it.
