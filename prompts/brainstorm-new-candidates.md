# Brainstorm New Dictionary Candidates via OpenRouter

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

This prompt runs the automated candidate-brainstorming pipeline. It calls an
external LLM via OpenRouter to discover Japanese words that may be missing from
the dictionary, then adds survivors to `candidate_words.json`, rebuilds the
site, and merges the changes.

**Designed for unattended scheduled execution** (Claude Code for the Web
scheduling feature). No human supervision required.

---

## Configuration

These settings are used for the OpenRouter LLM call. To change them, edit the
values below and the corresponding `--flags` in the commands in the steps.

| Setting       | Value                     |
| ------------- | ------------------------- |
| Model         | `openai/gpt-4.1-mini`    |
| Temperature   | `0.8`                     |
| Max tokens    | `8192`                    |
| Batch size    | `15` (seed words per batch) |
| Batches       | `100` (override with `-n`)  |

**Relation types explored** (hardcoded in `build/archive/brainstorm_candidates.py`):
- synonyms and near-synonyms
- antonyms
- same semantic field
- same-kanji compounds
- register variants (formal/informal)
- collocational partners
- situationally related words

---

## Prerequisites

- `OPENROUTER_API_KEY` environment variable must be set.
  Verify before doing anything else: `echo $OPENROUTER_API_KEY | head -c8`
  If empty, abort immediately with a clear error message.
- Repository should have a clean working tree

---

## Steps

### 0. Ensure dependencies are installed

```bash
pip install -q requests
```

This is idempotent and fast if already installed.

### 1. Set up a feature branch

**If you are already on a feature branch** (assigned by the harness or
created before this prompt was invoked), skip branch creation and stay on
that branch. Just make sure it is up to date:

```bash
git pull origin main --no-edit  # merge latest main into current branch
```

**Otherwise** (you are on `main` with no pre-assigned branch):

```bash
git checkout main
git pull origin main
git checkout -b brainstorm/candidates-$(date +%Y%m%d-%H%M%S)
```

### 2. Initialize / update the brainstorming data file

This creates (first run) or updates (subsequent runs)
`prompts/entries-and-candidates-for-brainstorming.md` with the current contents
of `entries_index.json` and `candidate_words.json`. Checked values are
preserved across runs, and on first creation they are imported from
`brainstorming/entries_and_candidates_for_LLM_brainstorming_old.json`.

```bash
python3 build/archive/brainstorm_candidates.py init
```

### 3. Run the brainstorming pipeline

```bash
python3 build/archive/brainstorm_candidates.py brainstorm \
  -n 5 \
  --model "openai/gpt-4.1-mini" \
  --temperature 0.8 \
  --max-tokens 8192 \
  --batch-size 15
```

Use `-n 100` by default. The invoking metaprompt may specify a different number;
if so, use that value instead. To run more batches, repeat the cycle of
steps 3 → 4 (brainstorm then add-results) multiple times, since each
brainstorm run **overwrites** `brainstorm_results.json`. The persistent
`checked_seeds.json` ensures no seed word is reused across runs.

This selects batches of 15 random unchecked seed words, sends each batch to
the LLM, and filters the suggestions through flexible deduplication that
handles:

- Exact `(headword, reading)` matches against all entries and candidates
- Katakana-to-hiragana normalization in readings
- Kana-only vs kanji headword variants with the same reading
- Leading/trailing `〜` / `～` stripping
- Furigana notation stripping
- Cross-batch deduplication within the same run

Results are saved to `prompts/brainstorm_results.json`.

### 4. Import results into candidate_words.json

```bash
python3 build/archive/brainstorm_candidates.py add-results
```

This reads `prompts/brainstorm_results.json` and adds each surviving candidate
to `candidate_words.json`, running both exact and fuzzy duplicate checks against
current entries and candidates. The results file is deleted after successful
import.

### 5. Show statistics

```bash
python3 build/archive/brainstorm_candidates.py stats
```

Report the statistics to confirm the run completed. The `add-results` command
(step 4) prints each added word as `+ headword (reading): gloss` — use that
output to compile the list of newly added candidates for reporting.

### 6. Validate and build

```bash
make build
```

This runs validation, updates indexes, and rebuilds the static site.

If validation fails, investigate and fix the issue (most likely a malformed
candidate entry). Then re-run `make build`.

### 7. Commit all changes

Commit everything including build artifacts:

```bash
git add -A
git commit -m "brainstorm: add new candidates from $(date +%Y-%m-%d) LLM session"
```

### 8. Push and create PR

```bash
git push -u origin HEAD
```

Create a pull request. The title should be:
`Brainstorm: add N new candidates (YYYY-MM-DD)`

where N is the number of candidates added (from step 4 output).

The PR body should include:
- Number of batches run
- Number of candidates added
- Number skipped (exact + fuzzy duplicates)
- Model used

### 9. Wait for CI and squash-merge

Wait for CI with a single blocking call: `gh pr checks <number> --repo tkgally/je-dict-1 --watch --fail-fast`. It exits 0 when every check succeeds and non-zero on failure. Do NOT wrap it in a `while`/`sleep`/`curl` polling loop — `--watch` already handles the wait, and hand-rolled streaming loops get routed through the `Monitor` tool (separate permission grant) which will deadlock an unattended session. Once green, squash-merge the PR.

If CI fails, read the failure logs, fix the issue, commit, push, and re-check.

### 10. Post-merge cleanup

Follow the end-of-session PR and merge workflow from CLAUDE.md:

```bash
git checkout main
git pull origin main
git branch -d <branch-name>
git push origin --delete <branch-name>
```

Verify `git status` shows a clean working tree.

---

## Error handling

- If `OPENROUTER_API_KEY` is not set, abort with a clear error message.
- If the OpenRouter API returns errors, the script retries up to 4 times with
  exponential backoff (2s, 4s, 8s, 16s).
- If zero new candidates survive deduplication, skip steps 5-10 (nothing to
  commit). Just report the result.
- If `make build` fails, investigate and fix before committing.

## Notes

- The brainstorming data file (`prompts/entries-and-candidates-for-brainstorming.md`)
  is a large JSON array and should NOT be committed to the repository. It is in
  `.gitignore`.
- The results file (`prompts/brainstorm_results.json`) is a temporary file and
  should also not be committed.
- **Seed tracking persistence**: The record of which words have been used as
  seeds is stored in `brainstorming/checked_seeds.json`. This file IS committed
  to the repository, so checked state survives across sessions and branch
  merges. Each session picks up where the last one left off — no word is used
  as a seed twice until all words have been used.
- Once all words are checked, run
  `python3 build/archive/brainstorm_candidates.py reset-checked` to start a new cycle.
