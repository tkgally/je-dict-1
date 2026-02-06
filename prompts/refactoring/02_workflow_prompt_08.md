# Workflow & Autonomy — Prompt 8: Create batch-optimized prompt versions

**Source:** Agent 2 Report (Workflow & Autonomy), Phase 3, Prompt 8
**Priority:** Medium (Phase 3: Optimize Task Prompts)
**Effort:** Medium

---

**Post-02_workflow_prompt_01 note:** Prompt 02_workflow_prompt_01 already created
`PROJECT_CONTEXT_BRIEF.md` and updated the interactive prompts in `prompts/` to
reference it instead of `PROJECT_STATUS.md`. The interactive prompts already use the
brief file for session startup.

The existing prompts in `prompts/` are designed for interactive sessions (they now
reference PROJECT_CONTEXT_BRIEF.md for startup context). Create `prompts/batch/`
versions optimized for `claude --print` (non-interactive) execution. Key differences
from the interactive versions: (1) do not include context reset procedures (each
invocation is a fresh context), (2) always commit at end, (3) do not push (the pipeline
handles pushing), (4) include explicit "exit cleanly" instructions, (5) use `make
validate` and `make build` (from the Makefile created by 01_code_prompt_08) for
post-task validation. Create batch versions for: newentries.md,
polish_add_inline_links.md, corpus_harvesting.md, polish_example_sentences.md.
