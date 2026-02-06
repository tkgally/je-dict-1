# Workflow & Autonomy — Prompt 4: Create the pipeline configuration schema

**Source:** Agent 2 Report (Workflow & Autonomy), Phase 2, Prompt 4
**Priority:** Medium (Phase 2: Build the Task Runner)
**Effort:** Medium

---

Create `pipeline/pipeline-config.json` with a schema that defines a task queue. Each
task should specify: type (one of: corpus-harvesting, new-entries, inline-links,
example-sentences, furigana-completeness, furigana-correctness, semantic-labels,
noentry-resolution, expand-short-notes), count (number of invocations), and optional
parameters. Also create `pipeline/pipeline-config.example.json` with a sample
configuration. Store the schema documentation in `pipeline/README.md`.
