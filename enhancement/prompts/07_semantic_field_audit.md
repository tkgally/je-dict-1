# Semantic Field Audit System

**Enhancement plan section**: [1.3.1] Semantic Field Audit System

Build a system that defines essential semantic fields, checks dictionary coverage against them, and feeds gaps into the candidate pipeline.

## What This Prompt Creates/Modifies

| File | Action | Purpose |
|------|--------|---------|
| `build/data/semantic_fields.json` | **Create** | 50-100 semantic field definitions with expected vocabulary |
| `build/audit_semantic_field.py` | **Create** | Coverage audit script: cross-checks fields against entries |
| `prompts/newcandidates.md` | **Modify** | Add semantic field audit as a discovery strategy |
| `CLAUDE.md` | **Modify** | Document `audit_semantic_field.py` in essential commands |
| `Makefile` | **Modify** | Add `audit-fields` target |

---

## Part A: Define Semantic Fields [1.3.1 step 1-2]

**Goal**: Create a comprehensive set of semantic field definitions covering the vocabulary domains an intermediate Japanese learner needs. Use LLM knowledge to populate expected words (per project policy -- no external dictionary comparison).

### Step A1: Create the data directory

```bash
mkdir -p build/data
```

### Step A2: Create `build/data/semantic_fields.json`

Create a JSON file containing 50-100 semantic field definitions. The top-level structure is:

```json
{
  "version": "1.0",
  "description": "Semantic field definitions for dictionary coverage auditing",
  "fields": [
    {
      "id": "colors",
      "name": "Colors",
      "category": "basic_concepts",
      "description": "Basic and common color terms including i-adjective and noun forms",
      "expected_words": [
        {"word": "赤い", "reading": "あかい", "gloss": "red", "priority": "high"},
        {"word": "青い", "reading": "あおい", "gloss": "blue", "priority": "high"},
        {"word": "白い", "reading": "しろい", "gloss": "white", "priority": "high"},
        {"word": "黒い", "reading": "くろい", "gloss": "black", "priority": "high"},
        {"word": "黄色い", "reading": "きいろい", "gloss": "yellow", "priority": "high"},
        {"word": "緑", "reading": "みどり", "gloss": "green", "priority": "high"},
        {"word": "茶色", "reading": "ちゃいろ", "gloss": "brown", "priority": "medium"},
        {"word": "灰色", "reading": "はいいろ", "gloss": "gray", "priority": "medium"},
        {"word": "紫", "reading": "むらさき", "gloss": "purple", "priority": "medium"},
        {"word": "ピンク", "reading": "ぴんく", "gloss": "pink", "priority": "medium"},
        {"word": "オレンジ", "reading": "おれんじ", "gloss": "orange", "priority": "low"},
        {"word": "金色", "reading": "きんいろ", "gloss": "gold (color)", "priority": "low"},
        {"word": "銀色", "reading": "ぎんいろ", "gloss": "silver (color)", "priority": "low"}
      ]
    }
  ]
}
```

**Required categories** (aim for the target number of fields in each):

| Category | Target fields | Example fields |
|----------|--------------|----------------|
| `basic_concepts` | 5-8 | colors, numbers/counting, time expressions, directions/location, shapes |
| `body_and_health` | 5-8 | body parts, medical/symptoms, hygiene/health, emotions/feelings, senses |
| `daily_life` | 8-12 | food/cooking, clothing, housing/furniture, shopping/money, transportation, tools, household chores, personal items |
| `nature` | 5-8 | weather, seasons, animals, plants, nature/geography, natural disasters |
| `people` | 5-8 | family, occupations, personality traits, appearance, social relationships, life stages |
| `society` | 8-12 | work/office, education/academic, legal, government, religion, communication, technology, media, sports, music/arts |
| `language` | 3-5 | greetings/social, materials/substances, abstract concepts |

**Guidelines for populating expected words**:

- Each field should have 10-30 expected words
- Use three priority levels:
  - `high` -- words any intermediate learner must know (would appear in basic/core tiers)
  - `medium` -- words most intermediate learners should know (early general tier)
  - `low` -- words that complete the domain (later general tier)
- Include the most natural form of each word:
  - I-adjectives: dictionary form (e.g., "赤い" not "赤")
  - Na-adjectives: stem form without な (e.g., "静か" not "静かな")
  - Verbs: dictionary form (e.g., "食べる" not "食べます")
  - Nouns: standard form
- Readings must be in hiragana (katakana words get hiragana readings: ピンク → ぴんく)
- Include a brief English gloss for each word
- Focus on concrete, unambiguous vocabulary. Avoid words that belong equally to multiple fields -- put them in the most natural one.
- For words with multiple common readings, include the most common reading only

**Total target**: At least 1,500 expected words across all fields (average ~20 per field).

### Step A3: Validate the data file

After creating the file, verify it is valid JSON:

```bash
python3 -c "
import json
with open('build/data/semantic_fields.json') as f:
    data = json.load(f)
fields = data['fields']
print(f'Total fields: {len(fields)}')
total_words = sum(len(f['expected_words']) for f in fields)
print(f'Total expected words: {total_words}')
categories = set(f['category'] for f in fields)
print(f'Categories: {sorted(categories)}')
for f in fields:
    for w in f['expected_words']:
        assert 'word' in w and 'reading' in w and 'gloss' in w and 'priority' in w, f'Missing key in {f[\"id\"]}: {w}'
        assert w['priority'] in ('high', 'medium', 'low'), f'Bad priority in {f[\"id\"]}: {w}'
print('Validation passed')
"
```

---

## Part B: Build the Audit Script [1.3.1 step 3]

**Goal**: Create `build/audit_semantic_field.py` that cross-checks semantic fields against the dictionary's `entries_index.json`.

### Step B1: Create `build/audit_semantic_field.py`

The script should:

1. **Load semantic field definitions** from `build/data/semantic_fields.json`
2. **Load the entry index** from `entries_index.json`
3. **Match expected words against entries** by checking both headword and reading. A word is "found" if there is an entry with a matching headword (any of the entry's headwords) AND matching reading.
4. **Report coverage** per field and overall

**Command-line interface**:

```
usage: audit_semantic_field.py [-h] [--field FIELD_ID] [--category CATEGORY]
                                [--below N] [--priority PRIORITY]
                                [--json] [--candidates] [--add-candidates]
                                [--summary]

Audit dictionary coverage of semantic fields.

optional arguments:
  --field FIELD_ID     Audit a single field
  --category CATEGORY  Audit all fields in a category
  --below N            Show only fields with coverage below N%
  --priority PRIORITY  Filter expected words by priority (high, medium, low)
  --json               Output in JSON format
  --candidates         Output missing words in candidate-compatible format
  --add-candidates     Directly add missing words as candidates via manage_candidates.py
  --summary            Show only the summary table, not individual missing words
```

**Output format (default, human-readable)**:

```
=== Semantic Field Coverage Report ===

--- colors (Colors) ---
Coverage: 10/13 (76.9%)
Missing (high priority):
  (none)
Missing (medium priority):
  灰色 (はいいろ) - gray
Missing (low priority):
  金色 (きんいろ) - gold (color)
  銀色 (ぎんいろ) - silver (color)

--- body_parts (Body Parts) ---
Coverage: 18/25 (72.0%)
Missing (high priority):
  肩 (かた) - shoulder
...

=== Summary ===
Total fields: 65
Total expected words: 1,523
Found in dictionary: 1,102 (72.4%)
Missing: 421 (27.6%)
  High priority missing: 45
  Medium priority missing: 178
  Low priority missing: 198

Fields below 50% coverage:
  legal (Legal Terms): 8/22 (36.4%)
  medical (Medical Terms): 12/28 (42.9%)
```

**Output format (`--json`)**:

```json
{
  "audit_date": "2026-04-09",
  "total_fields": 65,
  "total_expected": 1523,
  "total_found": 1102,
  "coverage_percent": 72.4,
  "fields": [
    {
      "id": "colors",
      "name": "Colors",
      "category": "basic_concepts",
      "total": 13,
      "found": 10,
      "coverage_percent": 76.9,
      "missing": [
        {"word": "灰色", "reading": "はいいろ", "gloss": "gray", "priority": "medium"}
      ]
    }
  ]
}
```

**Output format (`--candidates`)**:

Print one line per missing word in a format suitable for piping to `manage_candidates.py`:

```
"灰色" "はいいろ" "gray"
"金色" "きんいろ" "gold (color)"
```

**Behavior for `--add-candidates`**:

Directly invoke `manage_candidates.py add` for each missing word via subprocess. Print results (added / already exists / error) for each word. This mode should:
- Process only `high` and `medium` priority words by default (override with `--priority low` to include all)
- Check `candidate_words.json` first to avoid redundant add attempts
- Print a summary: "Added N new candidates, M already existed, K errors"

### Step B2: Implementation details

**Matching logic**: When checking if a word exists in the dictionary:

1. Load `entries_index.json` which contains entries with `headword`, `reading`, and `alternate_forms` fields
2. For each expected word, check if any entry matches by:
   - `headword` matches the expected `word` AND `reading` matches the expected `reading`
   - OR any `alternate_forms` entry matches both word and reading
3. Also check kana-only entries: if the expected word is all kana (no kanji), match by reading alone

**Script structure**:

```python
#!/usr/bin/env python3
"""Audit dictionary coverage of semantic fields."""

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
FIELDS_FILE = SCRIPT_DIR / "data" / "semantic_fields.json"
INDEX_FILE = PROJECT_DIR / "entries_index.json"
CANDIDATES_FILE = PROJECT_DIR / "candidate_words.json"


def load_fields(fields_file=FIELDS_FILE):
    """Load semantic field definitions."""
    ...


def load_entry_index(index_file=INDEX_FILE):
    """Load entries_index.json and build a lookup set of (word, reading) pairs."""
    ...


def load_candidates(candidates_file=CANDIDATES_FILE):
    """Load candidate_words.json and build a lookup set of (word, reading) pairs."""
    ...


def audit_field(field, entry_lookup):
    """Check coverage for a single semantic field. Returns dict with results."""
    ...


def print_field_report(result, show_missing=True):
    """Print human-readable report for one field."""
    ...


def print_summary(results):
    """Print overall summary statistics."""
    ...


def main():
    parser = argparse.ArgumentParser(description="Audit dictionary coverage of semantic fields.")
    parser.add_argument("--field", help="Audit a single field by ID")
    parser.add_argument("--category", help="Audit all fields in a category")
    parser.add_argument("--below", type=float, metavar="N", help="Show only fields with coverage below N%%")
    parser.add_argument("--priority", choices=["high", "medium", "low"], help="Filter by priority level")
    parser.add_argument("--json", action="store_true", dest="json_output", help="Output in JSON format")
    parser.add_argument("--candidates", action="store_true", help="Output missing words in candidate format")
    parser.add_argument("--add-candidates", action="store_true", help="Directly add missing words as candidates")
    parser.add_argument("--summary", action="store_true", help="Show only summary, not individual missing words")
    args = parser.parse_args()
    ...


if __name__ == "__main__":
    main()
```

### Step B3: Test the script

After creating the script, run it and verify output:

```bash
# Full report
python3 build/audit_semantic_field.py --summary

# Single field
python3 build/audit_semantic_field.py --field colors

# Fields below 50%
python3 build/audit_semantic_field.py --below 50 --summary

# JSON output
python3 build/audit_semantic_field.py --json | python3 -m json.tool | head -30

# Candidate format
python3 build/audit_semantic_field.py --field colors --candidates
```

Fix any issues found during testing.

---

## Part C: Candidate Pipeline Integration [1.3.1 step 4]

**Goal**: Make it easy to feed semantic field gaps into the candidate pipeline.

### Step C1: Test the `--add-candidates` flow

Run on a small field to verify the pipeline works end to end:

```bash
# Dry run -- show what would be added
python3 build/audit_semantic_field.py --field colors --candidates

# Actually add (high+medium priority only by default)
python3 build/audit_semantic_field.py --field colors --add-candidates
```

Verify that `manage_candidates.py add` is called correctly and that candidates appear in `candidate_words.json`.

### Step C2: Verify duplicate prevention

The `--add-candidates` mode must not add words that are already candidates. Run the same command twice and verify the second run reports "already existed" for all words.

---

## Part D: Documentation

### Step D1: Update CLAUDE.md

In the "Essential commands" section of CLAUDE.md, find the "Reports" subsection and add:

```bash
# Semantic field coverage
python3 build/audit_semantic_field.py --summary          # Coverage overview for all fields
python3 build/audit_semantic_field.py --field FIELD_ID    # Audit one field
python3 build/audit_semantic_field.py --below 50          # Fields with poor coverage
python3 build/audit_semantic_field.py --add-candidates    # Add missing words as candidates
```

Also update the project structure section to include:

```
  build/data/                 # Static data files (semantic fields, scenarios, etc.)
  build/data/semantic_fields.json   # Semantic field definitions for coverage auditing
  build/audit_semantic_field.py     # Semantic field coverage audit
```

### Step D2: Update Makefile

Add a target for semantic field auditing:

```makefile
audit-fields:
	python3 build/audit_semantic_field.py --summary
```

Add `audit-fields` to the `.PHONY` line.

### Step D3: Update `prompts/newcandidates.md`

In the "Workflow" section (or add a new section after it), add a note about semantic field audits as a discovery strategy:

```markdown
## Discovery Strategies

In addition to brainstorming, you can use the semantic field audit to identify systematic gaps:

```bash
# See which semantic fields have the lowest coverage
python3 build/audit_semantic_field.py --below 60 --summary

# Get missing words for a specific field
python3 build/audit_semantic_field.py --field FIELD_ID --candidates

# Directly add missing words as candidates (high+medium priority)
python3 build/audit_semantic_field.py --field FIELD_ID --add-candidates
```

This is especially useful for finding vocabulary gaps in specialized domains (medical, legal, academic) that brainstorming tends to miss.
```

---

## Verification

After all parts are complete, run these checks:

```bash
# Verify data file exists and is valid
python3 -c "import json; d = json.load(open('build/data/semantic_fields.json')); print(f'{len(d[\"fields\"])} fields, {sum(len(f[\"expected_words\"]) for f in d[\"fields\"])} words')"

# Verify the audit script runs
python3 build/audit_semantic_field.py --summary

# Verify JSON output is valid
python3 build/audit_semantic_field.py --json | python3 -m json.tool > /dev/null && echo "JSON output valid"

# Verify single-field mode
python3 build/audit_semantic_field.py --field colors

# Verify candidate output format
python3 build/audit_semantic_field.py --field colors --candidates

# Full validation
make validate
```

Fix any issues found during verification.

---

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow."

1. **Run `make build`** to ensure all build artifacts are up to date
2. **Stage and commit all changes**:
   ```bash
   git add -A
   git commit -m "Semantic field audit system: field definitions and coverage tool [1.3.1]

   - Create build/data/semantic_fields.json with 50-100 semantic field definitions
   - Create build/audit_semantic_field.py for coverage auditing
   - Add --add-candidates mode for candidate pipeline integration
   - Update CLAUDE.md, Makefile, and newcandidates.md with documentation"
   ```
3. **Push** to the feature branch
4. **Create a PR**: `gh pr create --repo tkgally/je-dict-1 --head <branch> --base main --title "Semantic field audit system [1.3.1]" --body "..."`
5. **Poll CI status** every 60 seconds: `gh pr checks <number> --repo tkgally/je-dict-1` (allow up to 10 minutes)
6. **Squash-merge** once CI is green: `gh pr merge <number> --repo tkgally/je-dict-1 --squash`
7. **If CI fails**: read the error with `gh run view <run_id> --repo tkgally/je-dict-1 --log-failed`, fix, push, and repeat
8. **Post-merge cleanup**:
   ```bash
   git checkout main && git pull origin main
   git status  # Should show nothing to commit
   git branch -d <branch-name>
   git push origin --delete <branch-name>
   ```

**CRITICAL**: The PR must include rebuilt `docs/` files from `make build`. If you commit source changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.
