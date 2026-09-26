# Run Next Enhancement Prompt

You are executing the next step in the je-dict-1 enhancement plan. This is an autonomous workflow — read the tracker, determine the next prompt, execute it fully through to merge, then update the tracker.

## Step 1: Read the Tracker

```bash
cat enhancement/tracking.md
```

Find the first row where Status = `pending`. That is the prompt to execute this session.

**Before proceeding, check dependencies.** The dependency list is at the bottom of `tracking.md`. If the next pending prompt depends on another prompt that is not yet `done`, skip to the next pending prompt that has no unmet dependencies. If ALL remaining prompts have unmet dependencies, report this and stop.

## Step 2: Announce

Tell the user which prompt you are about to execute:
> Executing enhancement prompt **NN — [Description]** (`enhancement/prompts/NN_filename.md`)

## Step 3: Execute the Prompt

Read the full prompt file:
```bash
cat enhancement/prompts/[FILENAME]
```

Follow every instruction in that prompt. This includes:
- Building scripts, creating files, modifying existing files
- Running validation (`make validate` or `make build`)
- Committing to the feature branch
- Creating a PR
- Polling CI until green
- Squash-merging the PR
- Post-merge cleanup (switch to main, pull, verify clean, delete branch)

Use the branch name pattern: `enhancement/NN-short-name` (e.g., `enhancement/01-infrastructure`).

## Step 4: Update the Tracker

After the merge is complete and you are on a clean main branch:

1. Edit `enhancement/tracking.md`:
   - Change the row's Status from `pending` to `done`
   - Add today's date in the Completed column
2. Commit and push directly to main:
   ```bash
   git add enhancement/tracking.md
   git commit -m "Mark enhancement prompt NN as done"
   git push origin main
   ```

## Step 5: Report

Tell the user:
- Which prompt was completed
- What was created/modified
- What the next pending prompt is
- How many prompts remain

## Rules

- **One prompt per session.** After completing one prompt, stop. Do not start the next one.
- **If the prompt fails** (CI won't pass, a dependency is missing, etc.), report the failure clearly and do NOT mark it as done.
- **If you need to skip a prompt**, change its status to `skipped` with a reason in the Description column, and move to the next one.
- **Always leave main clean.** The tracker update commit should be the last thing you do.
