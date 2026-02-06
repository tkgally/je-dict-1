# Workflow & Autonomy — Prompt 1: Create PROJECT_CONTEXT_BRIEF.md

**Source:** Agent 2 Report (Workflow & Autonomy), Phase 1, Prompt 1
**Priority:** High (Phase 1: Reduce Context Overhead)
**Effort:** Low

---

Create a new file `PROJECT_CONTEXT_BRIEF.md` that contains only the information Claude
needs at the start of a work session: current entry count, candidate count, next
available entry ID, vocabulary tier policy, polishing task progress pointers, and
critical rules. Target under 1,500 tokens. Do NOT include historical session logs.
Then update all prompts in `prompts/` to reference `PROJECT_CONTEXT_BRIEF.md` instead
of `PROJECT_STATUS.md` for session startup. Keep PROJECT_STATUS.md as-is for
historical reference.
