# Scenario-Based Gap Analysis

**Enhancement plan section**: [1.3.2] Scenario-Based Gap Analysis

Build a system that defines common learner scenarios, checks whether the dictionary covers the vocabulary needed for each scenario, and identifies the highest-impact missing words across scenarios.

## What This Prompt Creates/Modifies

| File | Action | Purpose |
|------|--------|---------|
| `build/data/learner_scenarios/` | **Create** | Directory of per-category JSON files defining learner scenarios |
| `build/assemble_learner_scenarios.py` | **Create** | Merges per-category files into `build/data/learner_scenarios.json` |
| `build/data/learner_scenarios.json` | **Generated** | Combined scenario definitions (built by assemble script) |
| `build/analyze_scenarios.py` | **Create** | Scenario coverage analysis and cross-scenario gap detection |
| `prompts/newcandidates.md` | **Modify** | Add scenario analysis as a discovery strategy |
| `CLAUDE.md` | **Modify** | Document `analyze_scenarios.py` in essential commands |
| `Makefile` | **Modify** | Add `audit-scenarios` and `assemble-scenarios` targets |

**Depends on**: Prompt 07 (semantic field audit) should be merged first. This prompt shares infrastructure patterns (the `build/data/` directory, candidate pipeline integration) and complements the semantic field approach.

---

## Part A: Define Learner Scenarios [1.3.2 step 1-2]

**Goal**: Create a comprehensive set of real-world scenarios an intermediate Japanese learner encounters. Each scenario lists the vocabulary needed to navigate that situation. Where semantic fields organize by topic, scenarios organize by communicative need.

### CRITICAL: Why this part is split into per-category steps

Previous attempts to create all scenarios in a single JSON file (100+ scenarios, 1,500+ vocabulary items) caused timeouts. The fix: create **one small JSON file per category**, then assemble them with a script. Each category file contains 4-10 scenarios and ~60-150 vocabulary items — easily manageable in a single write.

**You MUST follow the per-category approach below. Do NOT attempt to write all scenarios into a single file at once.**

### Step A1: Create the data directory

The `build/data/` directory should already exist (created by Prompt 07). Create the scenarios subdirectory:

```bash
mkdir -p build/data/learner_scenarios
```

### Step A2: Create per-category scenario files

Create **fifteen** separate JSON files, one per category. Work through them **one at a time**, writing each file, then validating it before moving to the next.

Each file has the same structure:

```json
{
  "category": "healthcare",
  "category_name": "Medical visits, pharmacy, health management",
  "scenarios": [
    {
      "id": "doctor_visit",
      "name": "Visiting a Doctor",
      "level": "intermediate",
      "description": "Describing symptoms, understanding a diagnosis, and following treatment instructions at a clinic or hospital",
      "expected_vocabulary": [
        {"word": "症状", "reading": "しょうじょう", "gloss": "symptom", "priority": "high"},
        {"word": "診察", "reading": "しんさつ", "gloss": "medical examination", "priority": "high"},
        {"word": "処方", "reading": "しょほう", "gloss": "prescription", "priority": "high"},
        {"word": "熱", "reading": "ねつ", "gloss": "fever", "priority": "high"},
        {"word": "痛い", "reading": "いたい", "gloss": "painful", "priority": "high"},
        {"word": "薬", "reading": "くすり", "gloss": "medicine", "priority": "high"},
        {"word": "保険証", "reading": "ほけんしょう", "gloss": "insurance card", "priority": "medium"},
        {"word": "受付", "reading": "うけつけ", "gloss": "reception", "priority": "medium"},
        {"word": "血圧", "reading": "けつあつ", "gloss": "blood pressure", "priority": "medium"},
        {"word": "検査", "reading": "けんさ", "gloss": "examination/test", "priority": "medium"},
        {"word": "注射", "reading": "ちゅうしゃ", "gloss": "injection", "priority": "medium"},
        {"word": "入院", "reading": "にゅういん", "gloss": "hospitalization", "priority": "low"},
        {"word": "退院", "reading": "たいいん", "gloss": "discharge from hospital", "priority": "low"}
      ]
    }
  ]
}
```

**After writing each file**, validate it immediately:

```bash
python3 -c "
import json, sys
with open(sys.argv[1]) as f:
    data = json.load(f)
scenarios = data['scenarios']
total = sum(len(s['expected_vocabulary']) for s in scenarios)
print(f'{data[\"category\"]}: {len(scenarios)} scenarios, {total} words')
for s in scenarios:
    assert 'id' in s and 'name' in s and 'level' in s and 'description' in s, f'Missing key in scenario: {s.get(\"id\",\"?\")}'
    for w in s['expected_vocabulary']:
        assert all(k in w for k in ('word','reading','gloss','priority')), f'Missing key in {s[\"id\"]}: {w}'
        assert w['priority'] in ('high','medium','low'), f'Bad priority in {s[\"id\"]}: {w}'
print('OK')
" build/data/learner_scenarios/FILENAME.json
```

If validation fails, fix the file before proceeding to the next category.

#### Category files to create:

**File 1: `build/data/learner_scenarios/daily_life.json`**
- Category: `daily_life` — "Everyday routines and household tasks"
- Target: 8-10 scenarios
- Example scenarios: morning routine, doing laundry, grocery shopping, cooking a meal, cleaning, trash sorting, commuting
- Target words per scenario: 8-15

**File 2: `build/data/learner_scenarios/travel.json`**
- Category: `travel` — "Transportation, navigation, accommodation"
- Target: 8-10 scenarios
- Example scenarios: buying train tickets, asking directions, hotel check-in, airport/immigration, renting a car, using a taxi, sightseeing, making reservations
- Target words per scenario: 8-15

**File 3: `build/data/learner_scenarios/work.json`**
- Category: `work` — "Office, meetings, business communication"
- Target: 6-8 scenarios
- Example scenarios: job interview, office greetings, meetings, email correspondence, giving a presentation, business card exchange, overtime/scheduling
- Target words per scenario: 8-15

**File 4: `build/data/learner_scenarios/education.json`**
- Category: `education` — "School, studying, academic settings"
- Target: 5-7 scenarios
- Example scenarios: enrolling in a class, taking an exam, library usage, asking a teacher, group study, school events
- Target words per scenario: 8-15

**File 5: `build/data/learner_scenarios/healthcare.json`**
- Category: `healthcare` — "Medical visits, pharmacy, health management"
- Target: 5-7 scenarios
- Example scenarios: visiting a doctor, pharmacy, dental visit, describing pain, allergies, getting a checkup
- Target words per scenario: 8-15

**File 6: `build/data/learner_scenarios/shopping.json`**
- Category: `shopping` — "Stores, online shopping, payments"
- Target: 5-7 scenarios
- Example scenarios: convenience store, clothing store, returning an item, online shopping, paying (cash/card)
- Target words per scenario: 8-15

**File 7: `build/data/learner_scenarios/dining.json`**
- Category: `dining` — "Restaurants, cafes, food ordering"
- Target: 5-7 scenarios
- Example scenarios: ordering at a restaurant, making a reservation, izakaya, cafe, food allergies/preferences, splitting the bill
- Target words per scenario: 8-15

**File 8: `build/data/learner_scenarios/housing.json`**
- Category: `housing` — "Apartments, moving, utilities, neighbors"
- Target: 5-7 scenarios
- Example scenarios: apartment hunting, signing a lease, moving in, reporting a problem, utilities setup
- Target words per scenario: 8-15

**File 9: `build/data/learner_scenarios/government.json`**
- Category: `government` — "City hall, documents, taxes, post office"
- Target: 4-6 scenarios
- Example scenarios: city hall registration, getting an ID, filing taxes, post office, renewing a visa
- Target words per scenario: 8-15

**File 10: `build/data/learner_scenarios/social.json`**
- Category: `social` — "Friendships, events, polite interaction"
- Target: 5-7 scenarios
- Example scenarios: self-introduction, party/gathering, giving gifts, apologizing, visiting someone's home, making plans
- Target words per scenario: 8-15

**File 11: `build/data/learner_scenarios/emergency.json`**
- Category: `emergency` — "Accidents, police, natural disasters"
- Target: 4-5 scenarios
- Example scenarios: calling 110/119, earthquake response, reporting a crime, lost/stolen items, typhoon preparation
- Target words per scenario: 8-15

**File 12: `build/data/learner_scenarios/technology.json`**
- Category: `technology` — "Phones, computers, internet, apps"
- Target: 4-6 scenarios
- Example scenarios: setting up a phone, connecting to wifi, using an ATM, troubleshooting, online forms
- Target words per scenario: 8-15

**File 13: `build/data/learner_scenarios/entertainment.json`**
- Category: `entertainment` — "Movies, games, hobbies, books"
- Target: 4-6 scenarios
- Example scenarios: going to a movie, karaoke, visiting a museum, reading manga/books, attending a concert
- Target words per scenario: 8-15

**File 14: `build/data/learner_scenarios/sports.json`**
- Category: `sports` — "Exercise, gym, spectator sports"
- Target: 3-5 scenarios
- Example scenarios: joining a gym, playing a team sport, swimming, hiking/outdoor activities
- Target words per scenario: 8-15

**File 15: `build/data/learner_scenarios/finance.json`**
- Category: `finance` — "Banks, payments, budgeting, insurance"
- Target: 4-6 scenarios
- Example scenarios: opening a bank account, transferring money, paying bills, insurance, currency exchange
- Target words per scenario: 8-15

**Guidelines for populating scenario vocabulary**:

- Each scenario should have **8-15** expected vocabulary items (focus on the essentials)
- Focus on words specifically needed for that scenario (not general vocabulary)
- Use the same three priority levels as semantic fields:
  - `high` -- cannot navigate the scenario without this word
  - `medium` -- important for competent handling of the scenario
  - `low` -- useful for nuanced handling or edge cases
- Words may appear in multiple scenarios (this is expected and valuable -- cross-scenario frequency is a key metric)
- Include verbs, nouns, and adjectives as appropriate for the scenario
- Include set phrases or expressions when they are single dictionary entries (e.g., "お会計" for asking for the bill)
- Readings must be in hiragana
- Include a brief English gloss

**Total target**: At least 1,200 expected vocabulary items across all category files. Many words will overlap across scenarios -- that overlap is the signal for high-impact gaps.

### Step A3: Create the assembly script

Create `build/assemble_learner_scenarios.py`:

```python
#!/usr/bin/env python3
"""Assemble per-category learner scenario files into a single learner_scenarios.json."""

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PARTS_DIR = SCRIPT_DIR / "data" / "learner_scenarios"
OUTPUT_FILE = SCRIPT_DIR / "data" / "learner_scenarios.json"


def main():
    if not PARTS_DIR.is_dir():
        print(f"Error: {PARTS_DIR} not found", file=sys.stderr)
        sys.exit(1)

    all_scenarios = []
    categories = {}
    category_files = sorted(PARTS_DIR.glob("*.json"))

    if not category_files:
        print(f"Error: no JSON files found in {PARTS_DIR}", file=sys.stderr)
        sys.exit(1)

    for path in category_files:
        with open(path) as f:
            data = json.load(f)
        category_id = data["category"]
        categories[category_id] = data["category_name"]
        for scenario in data["scenarios"]:
            scenario["category"] = category_id
            all_scenarios.append(scenario)

    combined = {
        "version": "1.0",
        "description": "Learner scenario definitions for vocabulary gap analysis",
        "categories": categories,
        "scenarios": all_scenarios
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)

    total_words = sum(len(s["expected_vocabulary"]) for s in all_scenarios)
    unique = set()
    for s in all_scenarios:
        for w in s["expected_vocabulary"]:
            unique.add((w["word"], w["reading"]))
    print(f"Assembled {len(all_scenarios)} scenarios ({total_words} vocab items, {len(unique)} unique) from {len(category_files)} category files")
    print(f"Written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
```

### Step A4: Assemble and validate

After all 15 category files are created and individually validated:

```bash
# Assemble the combined file
python3 build/assemble_learner_scenarios.py

# Validate the assembled file
python3 -c "
import json
with open('build/data/learner_scenarios.json') as f:
    data = json.load(f)
scenarios = data['scenarios']
categories = data['categories']
print(f'Total scenarios: {len(scenarios)}')
total_words = sum(len(s['expected_vocabulary']) for s in scenarios)
print(f'Total vocabulary items: {total_words}')
unique = set()
for s in scenarios:
    for w in s['expected_vocabulary']:
        unique.add((w['word'], w['reading']))
print(f'Unique words: {len(unique)}')
print(f'Categories defined: {len(categories)}')
used_cats = set(s['category'] for s in scenarios)
print(f'Categories used: {len(used_cats)}')
unused = set(categories.keys()) - used_cats
if unused:
    print(f'WARNING: Unused categories: {unused}')
for s in scenarios:
    assert s['category'] in categories, f'Unknown category: {s[\"category\"]} in {s[\"id\"]}'
    for w in s['expected_vocabulary']:
        assert all(k in w for k in ('word', 'reading', 'gloss', 'priority')), f'Missing key in {s[\"id\"]}: {w}'
        assert w['priority'] in ('high', 'medium', 'low'), f'Bad priority in {s[\"id\"]}: {w}'
from collections import Counter
cat_counts = Counter(s['category'] for s in scenarios)
for cat, count in sorted(cat_counts.items()):
    print(f'  {cat}: {count} scenarios')
print('Validation passed')
"
```

If the total is below 1,200 vocabulary items, go back and add more words to the thinnest scenarios before proceeding.

---

## Part B: Build the Analysis Script [1.3.2 step 2-4]

**Goal**: Create `build/analyze_scenarios.py` that cross-checks scenarios against the dictionary and identifies the highest-impact missing words.

### Step B1: Create `build/analyze_scenarios.py`

The script should:

1. **Load scenario definitions** from `build/data/learner_scenarios.json`
2. **Load the entry index** from `entries_index.json`
3. **Match expected words against entries** (same matching logic as `audit_semantic_field.py`)
4. **Report per-scenario coverage**
5. **Compute cross-scenario frequency** for missing words -- words needed by many scenarios but absent from the dictionary are the highest-impact gaps

**Command-line interface**:

```
usage: analyze_scenarios.py [-h] [--scenario SCENARIO_ID] [--category CATEGORY]
                             [--below N] [--priority PRIORITY]
                             [--top-gaps N] [--json]
                             [--candidates] [--add-candidates]
                             [--summary]

Analyze dictionary coverage for learner scenarios.

optional arguments:
  --scenario SCENARIO_ID  Analyze a single scenario
  --category CATEGORY     Analyze all scenarios in a category
  --below N               Show only scenarios with coverage below N%
  --priority PRIORITY     Filter vocabulary by priority (high, medium, low)
  --top-gaps N            Show the N highest-impact missing words (default: 50)
  --json                  Output in JSON format
  --candidates            Output missing words in candidate format, ordered by impact
  --add-candidates        Directly add missing words as candidates
  --summary               Show only summary, not per-scenario details
```

**Key feature: Cross-Scenario Impact Ranking**

The script's unique value is identifying words that appear in many scenarios but are missing from the dictionary. The impact score for a missing word is:

```
impact = scenario_count * priority_weight
```

Where `priority_weight` is: high=3, medium=2, low=1.

A word missing from 5 scenarios with high priority (impact=15) is more important than a word missing from 2 scenarios with low priority (impact=2).

**Output format (default, human-readable)**:

```
=== Scenario Coverage Report ===

--- doctor_visit (Visiting a Doctor) [healthcare] ---
Coverage: 10/13 (76.9%)
Missing:
  [high] 保険証 (ほけんしょう) - insurance card (also needed in: pharmacy, hospital_stay)
  [medium] 血圧 (けつあつ) - blood pressure

--- apartment_hunting (Looking for an Apartment) [housing] ---
Coverage: 8/18 (44.4%)
...

=== Top 50 Highest-Impact Gaps ===
Rank  Word            Reading       Scenarios  Impact  Gloss
  1.  契約            けいやく      7          21      contract
  2.  手続き          てつづき      6          18      procedure
  3.  確認            かくにん      6          16      confirmation
  4.  予約            よやく        5          15      reservation
...

=== Summary ===
Total scenarios: 150
Total vocabulary items: 2,847
Unique words: 1,432
Found in dictionary: 1,089 (76.1%)
Missing unique words: 343
  In 3+ scenarios: 87
  In 5+ scenarios: 23
```

**Output format (`--top-gaps N`)**:

Show the top N missing words ranked by impact score. Default N=50.

**Output format (`--candidates`)**:

Print missing words ordered by impact score (highest first), one per line:

```
"契約" "けいやく" "contract (needed in 7 scenarios)"
"手続き" "てつづき" "procedure (needed in 6 scenarios)"
```

**Behavior for `--add-candidates`**:

Same pattern as `audit_semantic_field.py`:
- Invoke `manage_candidates.py add` for each missing word
- Process in impact-score order (highest impact first)
- Default: only `high` and `medium` priority words
- Check `candidate_words.json` first to skip existing candidates
- Print a summary of results

### Step B2: Implementation details

**Shared matching logic**: The word-matching logic (checking entries_index.json) should be the same as in `audit_semantic_field.py`. If possible, extract a shared utility function. Options:

1. **Preferred**: Create a small shared module `build/coverage_utils.py` with the lookup-building and matching functions, imported by both scripts
2. **Acceptable**: Duplicate the matching logic in both scripts (simpler, avoids import issues)

Choose option 1 if it is straightforward. If import path issues arise (since `build/` is not a proper package), use option 2.

**Cross-scenario frequency calculation**:

```python
def compute_impact_scores(scenarios, entry_lookup):
    """Compute cross-scenario impact for each missing word.

    Returns a list of dicts sorted by impact score (descending):
    [
        {
            "word": "契約",
            "reading": "けいやく",
            "gloss": "contract",
            "scenarios": ["apartment_lease", "job_contract", ...],
            "scenario_count": 7,
            "max_priority": "high",
            "impact_score": 21
        },
        ...
    ]
    """
    ...
```

### Step B3: Test the script

```bash
# Full summary
python3 build/analyze_scenarios.py --summary

# Single scenario
python3 build/analyze_scenarios.py --scenario doctor_visit

# Single category
python3 build/analyze_scenarios.py --category healthcare --summary

# Scenarios below 50% coverage
python3 build/analyze_scenarios.py --below 50 --summary

# Top gaps
python3 build/analyze_scenarios.py --top-gaps 20

# JSON output
python3 build/analyze_scenarios.py --json | python3 -m json.tool | head -40

# Candidate format
python3 build/analyze_scenarios.py --top-gaps 10 --candidates
```

Fix any issues found during testing.

---

## Part C: Candidate Pipeline Integration [1.3.2 step 4]

**Goal**: Feed scenario gaps into the candidate pipeline, prioritized by cross-scenario frequency.

### Step C1: Test the `--add-candidates` flow

```bash
# Show what the top gaps look like
python3 build/analyze_scenarios.py --top-gaps 10 --candidates

# Add the top 10 highest-impact missing words as candidates
python3 build/analyze_scenarios.py --top-gaps 10 --add-candidates
```

Verify candidates are correctly added. Run `manage_candidates.py` to confirm:

```bash
python3 build/manage_candidates.py stats
```

### Step C2: Verify deduplication

Run the same `--add-candidates` command again and verify all words report "already existed."

---

## Part D: Documentation

### Step D1: Update CLAUDE.md

In the "Essential commands" section, in the "Reports" or a new "Coverage audits" subsection (near the semantic field commands if Prompt 07 was already merged), add:

```bash
# Scenario gap analysis
python3 build/analyze_scenarios.py --summary              # Coverage overview for all scenarios
python3 build/analyze_scenarios.py --scenario SCENARIO_ID  # Analyze one scenario
python3 build/analyze_scenarios.py --top-gaps 20           # Highest-impact missing words
python3 build/analyze_scenarios.py --add-candidates        # Add missing words as candidates
```

Update the project structure section to include:

```
  build/data/learner_scenarios.json    # Learner scenario definitions for gap analysis (generated)
  build/data/learner_scenarios/        # Per-category source files for learner scenarios
  build/assemble_learner_scenarios.py  # Assembles per-category files into learner_scenarios.json
  build/analyze_scenarios.py           # Scenario-based vocabulary gap analysis
```

If a shared utility was created:

```
  build/coverage_utils.py             # Shared lookup utilities for coverage auditing
```

### Step D2: Update Makefile

Add targets:

```makefile
audit-scenarios:
	python3 build/analyze_scenarios.py --summary

assemble-scenarios:
	python3 build/assemble_learner_scenarios.py
```

Add `audit-scenarios` and `assemble-scenarios` to the `.PHONY` line.

### Step D3: Update `prompts/newcandidates.md`

In the "Discovery Strategies" section (added by Prompt 07, or create if it doesn't exist), add scenario analysis:

```markdown
### Scenario-based gap analysis

Scenarios identify vocabulary needed for real-world situations. Missing words that appear across many scenarios are the highest-impact candidates:

```bash
# See the most impactful missing words across all scenarios
python3 build/analyze_scenarios.py --top-gaps 30

# See which scenario categories have the worst coverage
python3 build/analyze_scenarios.py --summary

# Add the highest-impact gaps as candidates
python3 build/analyze_scenarios.py --top-gaps 20 --add-candidates
```

This complements semantic field audits: fields find topical gaps, scenarios find communicative gaps.
```

---

## Verification

After all parts are complete, run these checks:

```bash
# Verify per-category files exist and are valid
for f in build/data/learner_scenarios/*.json; do
  python3 -c "
import json, sys
with open(sys.argv[1]) as f:
    data = json.load(f)
total = sum(len(s['expected_vocabulary']) for s in data['scenarios'])
print(f'{sys.argv[1]}: {len(data[\"scenarios\"])} scenarios, {total} words — OK')
" "$f"
done

# Verify assembly works
python3 build/assemble_learner_scenarios.py

# Verify the assembled data file
python3 -c "
import json
d = json.load(open('build/data/learner_scenarios.json'))
s = d['scenarios']
unique = set()
for sc in s:
    for w in sc['expected_vocabulary']:
        unique.add((w['word'], w['reading']))
print(f'{len(s)} scenarios, {sum(len(x[\"expected_vocabulary\"]) for x in s)} items, {len(unique)} unique words')
"

# Verify the script runs
python3 build/analyze_scenarios.py --summary

# Verify top-gaps output
python3 build/analyze_scenarios.py --top-gaps 10

# Verify JSON output
python3 build/analyze_scenarios.py --json | python3 -m json.tool > /dev/null && echo "JSON output valid"

# Verify candidate output
python3 build/analyze_scenarios.py --top-gaps 5 --candidates

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
   git commit -m "Scenario-based gap analysis: scenario definitions and analysis tools [1.3.2]

   - Create per-category scenario definitions in build/data/learner_scenarios/
   - Create build/assemble_learner_scenarios.py to merge category files
   - Create build/analyze_scenarios.py for coverage analysis and impact ranking
   - Add cross-scenario impact scoring to identify highest-value missing words
   - Add --add-candidates mode for candidate pipeline integration
   - Update CLAUDE.md, Makefile, and newcandidates.md with documentation"
   ```
3. **Push** to the feature branch
4. **Create a PR**: `gh pr create --repo tkgally/je-dict-1 --head <branch> --base main --title "Scenario-based gap analysis [1.3.2]" --body "..."`
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
