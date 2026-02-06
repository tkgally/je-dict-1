# Workflow & Autonomy — Prompt 12: Integrate with GitHub Actions

**Source:** Agent 2 Report (Workflow & Autonomy), Phase 4, Prompt 12
**Priority:** Low (Phase 4: User Workflow Integration)
**Effort:** High

---

Create a GitHub Actions workflow that can be manually triggered to run the pipeline.
The workflow would: (1) check out the repo, (2) read pipeline-config.json,
(3) run pipeline/run-pipeline.sh, (4) create a PR with the results. This allows the
user to trigger a pipeline run from their phone or any browser without needing a
terminal. Note: this requires the Claude CLI to be available in the CI environment,
which may require a custom runner or API-based approach.
