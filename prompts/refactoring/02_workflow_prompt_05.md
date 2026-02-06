# Workflow & Autonomy — Prompt 5: Create the pipeline runner script

**Source:** Agent 2 Report (Workflow & Autonomy), Phase 2, Prompt 5
**Priority:** Medium (Phase 2: Build the Task Runner)
**Effort:** High

---

**Post-01_code_prompt_08 note:** A Makefile now exists at the project root with targets
including `validate`, `index`, `build`, `check-furigana`, `check-kanji`, `stats`,
`clean`, and `full`. The pipeline script can use `make validate` and `make build`
instead of calling Python scripts directly.

Create `pipeline/run-pipeline.sh`, a bash script that reads `pipeline/pipeline-config.json`
and executes each task in sequence. For each task: (1) check that git working tree is
clean, (2) invoke `claude --print` with the appropriate prompt from `prompts/`,
(3) run `make validate` as a quality gate (or `python3 build/validate.py` as fallback),
(4) if validation passes, commit to the configured branch, (5) if validation fails,
log the error and either stop or skip based on config, (6) update
`pipeline/pipeline-status.json` with results. At the end, generate a summary report
to `pipeline/pipeline-report.txt` and optionally create a PR. Use the existing
`run-inline-links-batch.sh` as reference for the `claude --print` invocation pattern.
