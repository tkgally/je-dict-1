# Workflow & Autonomy — Prompt 5: Create the pipeline runner script

**Source:** Agent 2 Report (Workflow & Autonomy), Phase 2, Prompt 5
**Priority:** Medium (Phase 2: Build the Task Runner)
**Effort:** High

---

Create `pipeline/run-pipeline.sh`, a bash script that reads `pipeline/pipeline-config.json`
and executes each task in sequence. For each task: (1) check that git working tree is
clean, (2) invoke `claude --print` with the appropriate prompt from `prompts/`,
(3) run `python3 build/validate.py` as a quality gate, (4) if validation passes,
commit to the configured branch, (5) if validation fails, log the error and either
stop or skip based on config, (6) update `pipeline/pipeline-status.json` with results.
At the end, generate a summary report to `pipeline/pipeline-report.txt` and optionally
create a PR. Use the existing `run-inline-links-batch.sh` as reference for the
`claude --print` invocation pattern.
