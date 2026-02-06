# Workflow & Autonomy — Prompt 8: Create batch-optimized prompt versions

**Source:** Agent 2 Report (Workflow & Autonomy), Phase 3, Prompt 8
**Priority:** Medium (Phase 3: Optimize Task Prompts)
**Effort:** Medium

---

The existing prompts in `prompts/` are designed for interactive sessions. Create
`prompts/batch/` versions optimized for `claude --print` (non-interactive) execution.
Key differences: (1) read PROJECT_CONTEXT_BRIEF.md instead of PROJECT_STATUS.md,
(2) do not include context reset procedures (each invocation is a fresh context),
(3) always commit at end, (4) do not push (the pipeline handles pushing),
(5) include explicit "exit cleanly" instructions. Create batch versions for:
newentries.md, polish_add_inline_links.md, corpus_harvesting.md,
polish_example_sentences.md.
