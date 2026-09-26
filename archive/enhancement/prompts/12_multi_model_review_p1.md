# Multi-Model Proofreading — Phase 1

**Enhancement plan section**: [1.2.1] Multi-Model Proofreading, Phase 1

Build a multi-model review runner for furigana correctness and calibrate it on 100 entries. This is the highest-leverage quality intervention remaining: different models have different Japanese-language biases, particularly for furigana readings, which directly mislead learners when wrong.

## What This Prompt Creates/Modifies

| File | Action | Purpose |
|------|--------|---------|
| `build/review_runner.py` | **Create** | Multi-model review runner (OpenRouter API) |
| `reviews/` | **Create** | Directory for review reports |
| `reviews/calibration_report.md` | **Create** | Phase 1 calibration results |
| `reviews/{entry_id}.json` | **Create** | Per-entry review reports (100 entries for calibration) |
| `CLAUDE.md` | **Modify** | Document review_runner.py commands |
| `.gitignore` | **Modify** | Add reviews/ directory exclusion rules if needed |

---

## Prerequisites

Before starting, verify the OpenRouter API key is available:

```bash
if [ -z "$OPENROUTER_API_KEY" ]; then
  echo "ERROR: OPENROUTER_API_KEY environment variable is not set."
  echo "Set it with: export OPENROUTER_API_KEY='your-key-here'"
  echo "Cannot proceed without API access."
  exit 1
fi
echo "OK: OpenRouter API key is available."
```

If the key is not available, stop and report this to the user. Do not proceed without API access.

---

## Part A: Build Review Runner

Create `build/review_runner.py` — a script that sends dictionary entries to external models via OpenRouter for furigana correctness review.

### A1: Script Structure

The script should use only standard library modules plus `requests` (check if available; if not, use `urllib.request`). Structure:

```python
#!/usr/bin/env python3
"""Multi-model review runner for dictionary entry proofreading.

Sends entries to external models via OpenRouter API to cross-check
furigana readings. Stores structured review reports.

Usage:
    python3 build/review_runner.py --range 1 100
    python3 build/review_runner.py --ids 00123,00456,00789
    python3 build/review_runner.py --range 1 100 --model gpt-4.1
    python3 build/review_runner.py --range 1 100 --dry-run
    python3 build/review_runner.py --range 1 100 --pass screening
"""
```

### A2: Furigana Extraction

Implement a function that extracts all `{kanji|reading}` pairs from an entry. It must scan:

- `headword` field
- All `examples[].japanese` fields
- `notes` field (which may contain furigana markup)
- Any other text fields that may contain furigana

The extraction function should return a list of dictionaries:
```python
[
    {"field": "headword", "text": "{漢字|かんじ}", "kanji": "漢字", "reading": "かんじ"},
    {"field": "examples[0].japanese", "text": "{今日|きょう}は...", "kanji": "今日", "reading": "きょう"},
    ...
]
```

Use a regex pattern like `\{([^|]+)\|([^}]+)\}` to find all furigana pairs.

### A3: Review Prompt Construction

For each entry, construct a structured review prompt. The prompt sent to the external model should:

1. Present the entry's word, reading, and part of speech for context
2. List every `{kanji|reading}` pair found in the entry
3. Ask the model to verify each reading, considering:
   - Whether the reading is correct for this kanji/compound
   - Whether the reading is appropriate in this specific context
   - Whether rendaku rules are correctly applied
   - Whether irregular/special readings are correct
4. Request a structured JSON response

The review prompt template should look approximately like this (adjust for clarity):

```
You are reviewing furigana readings in a Japanese-English dictionary entry.

Entry: {word} ({reading}) — {pos}

The following kanji-reading pairs appear in this entry. For each one, verify whether the reading is correct in context.

Pairs to check:
1. Field: headword — {漢字|かんじ}
2. Field: examples[0].japanese — {今日|きょう}は{天気|てんき}がいい
3. ...

For each pair, respond with a JSON array:
[
  {
    "index": 1,
    "kanji": "漢字",
    "reading": "かんじ",
    "field": "headword",
    "correct": true,
    "concern": null
  },
  {
    "index": 2,
    "kanji": "今日",
    "reading": "きょう",
    "field": "examples[0].japanese",
    "correct": true,
    "concern": null
  }
]

If a reading is incorrect or questionable, set "correct" to false and explain in "concern".
Only flag genuinely incorrect readings — do not flag acceptable alternative readings unless they are wrong for this specific context.

Respond ONLY with the JSON array, no other text.
```

### A4: OpenRouter API Integration

Implement the API caller with these requirements:

1. **API endpoint**: `https://openrouter.ai/api/v1/chat/completions`
2. **Authentication**: Bearer token from `OPENROUTER_API_KEY` environment variable
3. **Target models** (use OpenRouter model identifiers):
   - `openai/gpt-4.1` (primary)
   - `google/gemini-2.5-flash` (secondary)
4. **Rate limiting**: Maximum 10 requests per minute per model. Implement a simple rate limiter that sleeps between requests if needed.
5. **Retry logic**: On HTTP 429 (rate limit) or 5xx errors, retry up to 3 times with exponential backoff (2s, 4s, 8s). On other errors, log and skip the entry.
6. **Timeout**: 60 seconds per request.
7. **Response parsing**: Extract JSON from the model's response. Handle cases where the model wraps JSON in markdown code blocks (strip ```json and ``` markers). If parsing fails, log the raw response and mark the entry as "parse_error".

### A5: Report Storage

Store review reports in `reviews/{entry_id}.json` with this structure:

```json
{
  "entry_id": "00123",
  "word": "漢字",
  "reading": "かんじ",
  "reviewed_at": "2026-04-09T12:34:56Z",
  "models_used": ["openai/gpt-4.1", "google/gemini-2.5-flash"],
  "furigana_pairs_checked": 15,
  "issues": [
    {
      "field": "examples[2].japanese",
      "kanji": "今日",
      "reading": "きょう",
      "model": "openai/gpt-4.1",
      "correct": true,
      "concern": null,
      "severity": "ok"
    },
    {
      "field": "notes",
      "kanji": "生物",
      "reading": "せいぶつ",
      "model": "google/gemini-2.5-flash",
      "correct": false,
      "concern": "In this context (living creature), the reading should be いきもの, not せいぶつ",
      "severity": "error"
    }
  ],
  "summary": {
    "total_checked": 15,
    "flagged": 2,
    "ok": 13,
    "models_agreeing_on_flags": 1
  }
}
```

**Severity classification**:
- `"ok"` — all models agree the reading is correct
- `"warning"` — one model flags it but others say it is correct
- `"error"` — multiple models agree the reading is wrong

### A6: Command-Line Interface

Implement with `argparse`:

```
python3 build/review_runner.py --range START END    # Review entries in ID range
python3 build/review_runner.py --ids ID1,ID2,...    # Review specific entries
python3 build/review_runner.py --dry-run            # Format prompts, print them, do not send
python3 build/review_runner.py --model MODEL        # Use only one model (for testing)
python3 build/review_runner.py --pass screening     # Screening pass (cheap model, fast)
python3 build/review_runner.py --pass deep          # Deep review (multiple strong models)
python3 build/review_runner.py --report             # Summarize existing review results
```

For Phase 1, only `--range`, `--ids`, `--dry-run`, `--model`, and `--report` need to work. The `--pass` flag can be stubbed with a message saying "Two-pass pipeline available in Phase 2."

### A7: Verification

After building the script, verify it works:

```bash
# Check the script runs without import errors
python3 build/review_runner.py --help

# Dry-run on 3 entries to inspect the generated prompts
python3 build/review_runner.py --range 1 10 --dry-run 2>&1 | head -100

# If prompts look reasonable, run on 3 entries with one model
python3 build/review_runner.py --ids 00001,00002,00003 --model openai/gpt-4.1
```

Fix any issues before proceeding to Part B.

---

## Part B: Phase 1 Calibration

Run the reviewer on 100 entries and evaluate accuracy.

### B1: Select Calibration Entries

Choose 100 entries across all three vocabulary tiers to test:

```bash
# Get a sample: ~10 basic, ~20 core, ~70 general (roughly proportional to tier sizes)
# Use entries_index.json to find entries by tier
python3 -c "
import json
with open('entries_index.json') as f:
    index = json.load(f)

basic = [e['id'] for e in index if e.get('tier') == 'basic'][:10]
core = [e['id'] for e in index if e.get('tier') == 'core'][:20]
general = [e['id'] for e in index if e.get('tier') == 'general'][:70]

all_ids = basic + core + general
print(','.join(all_ids))
"
```

Adjust the selection logic as needed based on what `entries_index.json` actually contains. The goal is 100 entries with representation from all tiers.

### B2: Run the Calibration

```bash
# Run review on the 100 selected entries
python3 build/review_runner.py --ids <comma-separated-ids>
```

This will take some time due to rate limiting. Monitor progress output.

### B3: Analyze Results

After the run completes, examine the reports:

```bash
# Get a summary
python3 build/review_runner.py --report
```

Then manually examine flagged issues:

1. Count the total number of flagged issues (severity "warning" or "error")
2. For each flagged issue, read the entry and determine if the flag is:
   - **True positive**: The model correctly identified a wrong reading
   - **False positive**: The reading is actually correct; the model was wrong
   - **Ambiguous**: The reading is a valid alternative but another reading would be more standard
3. Calculate the false-positive rate: `false_positives / total_flagged * 100`

### B4: Calibration Threshold

- If the false-positive rate is **<= 20%**: The prompt is calibrated. Proceed to documentation.
- If the false-positive rate is **> 20%**: Adjust the review prompt to reduce false positives:
  - Add more specific instructions about acceptable alternative readings
  - Add examples of correct readings that should not be flagged
  - Be more explicit about context-dependent readings (e.g., 今日 as きょう is standard in everyday contexts)
  - Re-run on a fresh set of 20 entries to verify improvement
  - Repeat until the rate is <= 20%

### B5: Document Calibration Results

Create `reviews/calibration_report.md`:

```markdown
# Multi-Model Review Calibration Report

**Date**: YYYY-MM-DD
**Entries reviewed**: 100
**Models used**: [list models]

## Results

| Metric | Value |
|--------|-------|
| Total furigana pairs checked | N |
| Flagged by at least one model | N |
| True positives (genuine errors) | N |
| False positives (incorrect flags) | N |
| Ambiguous | N |
| False-positive rate | X% |

## Prompt Iterations

(If the prompt was adjusted, document each iteration and its results.)

### Iteration 1
- Prompt version: (describe)
- Entries tested: 100
- False-positive rate: X%
- Issues found: (describe)

### Iteration 2 (if needed)
- Changes made: (describe)
- Entries tested: 20
- False-positive rate: X%

## True Positive Examples

(List 3-5 genuine errors found, with entry ID and details.)

## False Positive Examples

(List 3-5 false positives, explaining why the reading was actually correct.)

## Recommendations for Phase 2

(Based on calibration results, note any adjustments needed for scaling.)
```

---

## Part C: Directory Structure

Create the reviews directory:

```bash
mkdir -p reviews
```

The review JSON files will be created automatically by the runner. Decide on version control policy:

- Review JSON files can be large in aggregate. For Phase 1 (100 entries), committing them is fine.
- Add a note in the calibration report about whether reviews/ should be committed long-term or added to .gitignore.
- For now, **commit the calibration results** (they document a project decision) but add a `.gitignore` entry for bulk review files if the directory will grow to thousands of files:

```bash
# Add to .gitignore if reviews/ will grow large:
# reviews/*.json
# !reviews/calibration_report.md
```

For Phase 1, commit everything in reviews/. The Phase 2 prompt will decide on the long-term policy.

---

## Part D: Documentation

### D1: Update CLAUDE.md

In the "Essential commands" section, add a new subsection:

```bash
# Multi-model review (requires OPENROUTER_API_KEY)
python3 build/review_runner.py --range START END       # Review entries in ID range
python3 build/review_runner.py --ids ID1,ID2,...       # Review specific entries
python3 build/review_runner.py --dry-run --range 1 10  # Preview prompts without sending
python3 build/review_runner.py --model openai/gpt-4.1  # Test with one model
python3 build/review_runner.py --report                # Summarize review results
```

In the "Project structure" section, add:

```
reviews/          # Multi-model review reports (furigana correctness)
  reviews/calibration_report.md  # Phase 1 calibration results
  reviews/{entry_id}.json        # Per-entry review reports
```

Add `build/review_runner.py` to the build/ file listing with description: `# Multi-model furigana review via OpenRouter API`.

### D2: Update enhancement/prompts/README.md

Verify that prompt 12 is already listed in the README (it should be from initial setup). If its description needs updating based on what was actually built, update it.

---

## Verification

After all parts are complete:

```bash
# Script runs and shows help
python3 build/review_runner.py --help

# Dry-run produces valid prompt output
python3 build/review_runner.py --range 1 5 --dry-run

# Reviews directory exists with calibration results
test -d reviews && echo "OK: reviews/ exists" || echo "MISSING: reviews/"
test -f reviews/calibration_report.md && echo "OK: calibration report exists" || echo "MISSING: calibration report"

# Review files are valid JSON
for f in reviews/*.json; do python3 -c "import json; json.load(open('$f'))" && echo "OK: $f" || echo "INVALID: $f"; done

# Full validation still passes
make validate
```

Fix any issues found during verification.

---

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow."

1. **Create a feature branch**:
   ```bash
   git checkout -b enhancement/multi-model-review-p1
   ```

2. **Run `make build`** to ensure all build artifacts are up to date

3. **Stage and commit all changes**:
   ```bash
   git add -A
   git commit -m "Add multi-model review runner and Phase 1 calibration [1.2.1]

   - Create build/review_runner.py for furigana correctness review via OpenRouter
   - Support GPT-4.1 and Gemini 2.5 Flash models
   - Run Phase 1 calibration on 100 entries across all tiers
   - Document calibration results in reviews/calibration_report.md
   - Add review commands to CLAUDE.md"
   ```

4. **Push** to the feature branch:
   ```bash
   git push -u origin enhancement/multi-model-review-p1
   ```

5. **Create a PR**:
   ```bash
   gh pr create --repo tkgally/je-dict-1 \
     --head enhancement/multi-model-review-p1 \
     --base main \
     --title "Multi-model review runner + Phase 1 calibration [1.2.1]" \
     --body "## Summary

   - New \`build/review_runner.py\` sends entries to external models (GPT-4.1, Gemini 2.5 Flash) via OpenRouter API for furigana correctness review
   - Phase 1 calibration: reviewed 100 entries, documented false-positive rate and prompt tuning in \`reviews/calibration_report.md\`
   - Structured JSON review reports stored in \`reviews/\`
   - Supports \`--dry-run\`, \`--model\`, \`--range\`, \`--ids\`, \`--report\` flags

   ## Test plan
   - [ ] \`python3 build/review_runner.py --help\` runs without errors
   - [ ] \`python3 build/review_runner.py --dry-run --range 1 5\` produces valid prompts
   - [ ] Calibration report documents results and false-positive rate
   - [ ] \`make validate\` passes

   Enhancement plan: [1.2.1] Multi-Model Proofreading, Phase 1"
   ```

6. **Poll CI status** every 60 seconds:
   ```bash
   gh pr checks <number> --repo tkgally/je-dict-1
   ```
   Wait up to 10 minutes. If CI fails, read logs with `gh run view <run_id> --repo tkgally/je-dict-1 --log-failed`, fix, push, and repeat.

7. **Squash-merge** once CI is green:
   ```bash
   gh pr merge <number> --repo tkgally/je-dict-1 --squash
   ```

8. **Post-merge cleanup**:
   ```bash
   git checkout main && git pull origin main
   git status  # Should show nothing to commit
   git branch -d enhancement/multi-model-review-p1
   git push origin --delete enhancement/multi-model-review-p1
   ```

**CRITICAL**: The PR must include rebuilt `docs/` files from `make build`. If you commit source changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.
