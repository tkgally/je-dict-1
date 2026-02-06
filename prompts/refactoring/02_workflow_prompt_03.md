# Workflow & Autonomy — Prompt 3: Update the PreCompact hook

**Source:** Agent 2 Report (Workflow & Autonomy), Phase 1, Prompt 3
**Priority:** High (Phase 1: Reduce Context Overhead)
**Effort:** Low

---

Update `.claude/remind-resume-update.sh` to be a general-purpose pre-compact reminder.
Instead of the old semantic assignment task, it should remind Claude to: (1) update the
relevant progress.txt file, (2) write a session log if one is expected, and (3) commit
all changes. Remove the outdated multi-sense entry counting loop.
