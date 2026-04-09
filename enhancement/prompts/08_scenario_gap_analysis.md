# Scenario-Based Gap Analysis

**Enhancement plan section**: [1.3.2] Scenario-Based Gap Analysis

Build a system that defines common learner scenarios, checks whether the dictionary covers the vocabulary needed for each scenario, and identifies the highest-impact missing words across scenarios.

## What This Prompt Creates/Modifies

| File | Action | Purpose |
|------|--------|---------|
| `build/data/learner_scenarios.json` | **Create** | 100-200 scenario definitions with expected vocabulary |
| `build/analyze_scenarios.py` | **Create** | Scenario coverage analysis and cross-scenario gap detection |
| `prompts/newcandidates.md` | **Modify** | Add scenario analysis as a discovery strategy |
| `CLAUDE.md` | **Modify** | Document `analyze_scenarios.py` in essential commands |
| `Makefile` | **Modify** | Add `audit-scenarios` target |

**Depends on**: Prompt 07 (semantic field audit) should be merged first. This prompt shares infrastructure patterns (the `build/data/` directory, candidate pipeline integration) and complements the semantic field approach.

---

## Part A: Define Learner Scenarios [1.3.2 step 1-2]

**Goal**: Create a comprehensive set of real-world scenarios an intermediate Japanese learner encounters. Each scenario lists the vocabulary needed to navigate that situation. Where semantic fields organize by topic, scenarios organize by communicative need.

### Step A1: Create `build/data/learner_scenarios.json`

The `build/data/` directory should already exist (created by Prompt 07). If not:

```bash
mkdir -p build/data
```

Create the scenarios file with this structure:

```json
{
  "version": "1.0",
  "description": "Learner scenario definitions for vocabulary gap analysis",
  "categories": {
    "daily_life": "Everyday routines and household tasks",
    "travel": "Transportation, navigation, accommodation",
    "work": "Office, meetings, business communication",
    "education": "School, studying, academic settings",
    "healthcare": "Medical visits, pharmacy, health management",
    "shopping": "Stores, online shopping, payments",
    "dining": "Restaurants, cafes, food ordering",
    "housing": "Apartments, moving, utilities, neighbors",
    "government": "City hall, documents, taxes, post office",
    "social": "Friendships, events, polite interaction",
    "emergency": "Accidents, police, natural disasters",
    "technology": "Phones, computers, internet, apps",
    "entertainment": "Movies, games, hobbies, books",
    "sports": "Exercise, gym, spectator sports",
    "finance": "Banks, payments, budgeting, insurance"
  },
  "scenarios": [
    {
      "id": "doctor_visit",
      "name": "Visiting a Doctor",
      "category": "healthcare",
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

**Required categories and target scenario counts**:

| Category | Target scenarios | Example scenarios |
|----------|-----------------|-------------------|
| `daily_life` | 10-15 | morning routine, doing laundry, grocery shopping, cooking a meal, cleaning, trash sorting, bathing, getting dressed, commuting |
| `travel` | 10-15 | buying train tickets, asking directions, hotel check-in, airport/immigration, renting a car, using a taxi, sightseeing, reading a map, making reservations |
| `work` | 8-12 | job interview, office greetings, meetings, email correspondence, making a phone call, giving a presentation, business card exchange, overtime/scheduling, quitting a job |
| `education` | 6-10 | enrolling in a class, taking an exam, library usage, asking a teacher, group study, school events, graduation, parent-teacher meeting |
| `healthcare` | 6-10 | visiting a doctor, pharmacy, dental visit, describing pain, allergies, calling an ambulance, mental health, getting a checkup |
| `shopping` | 6-10 | convenience store, clothing store, electronics store, returning an item, online shopping, bargaining/sales, paying (cash/card), wrapping/bags |
| `dining` | 6-10 | ordering at a restaurant, making a reservation, izakaya, cafe, fast food, food allergies/preferences, splitting the bill, complimenting food |
| `housing` | 6-10 | apartment hunting, signing a lease, moving in, reporting a problem, meeting neighbors, utilities setup, home maintenance |
| `government` | 5-8 | city hall registration, getting an ID, filing taxes, post office, renewing a visa, reporting to police, voting |
| `social` | 6-10 | self-introduction, party/gathering, giving gifts, apologizing, congratulating, visiting someone's home, seasonal greetings, making plans |
| `emergency` | 4-6 | calling 110/119, earthquake response, reporting a crime, lost/stolen items, fire evacuation, typhoon preparation |
| `technology` | 5-8 | setting up a phone, connecting to wifi, using an ATM, troubleshooting, social media, online forms, printing/copying |
| `entertainment` | 5-8 | going to a movie, karaoke, visiting a museum, reading manga/books, playing games, attending a concert, watching sports |
| `sports` | 4-6 | joining a gym, playing a team sport, swimming, hiking/outdoor activities, describing exercise |
| `finance` | 5-8 | opening a bank account, transferring money, paying bills, understanding a receipt, insurance, budgeting, currency exchange |

**Guidelines for populating scenario vocabulary**:

- Each scenario should have 10-30 expected vocabulary items
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

**Total target**: At least 2,000 expected vocabulary items across all scenarios. Many words will overlap across scenarios -- that overlap is the signal for high-impact gaps.

### Step A2: Validate the data file

```bash
python3 -c "
import json
with open('build/data/learner_scenarios.json') as f:
    data = json.load(f)
scenarios = data['scenarios']
categories = data['categories']
print(f'Total scenarios: {len(scenarios)}')
total_words = sum(len(s['expected_vocabulary']) for s in scenarios)
print(f'Total vocabulary items: {total_words}')
# Count unique words
unique = set()
for s in scenarios:
    for w in s['expected_vocabulary']:
        unique.add((w['word'], w['reading']))
print(f'Unique words: {len(unique)}')
# Check categories
used_cats = set(s['category'] for s in scenarios)
defined_cats = set(categories.keys())
print(f'Categories defined: {len(defined_cats)}')
print(f'Categories used: {len(used_cats)}')
unused = defined_cats - used_cats
if unused:
    print(f'WARNING: Unused categories: {unused}')
# Validate structure
for s in scenarios:
    assert s['category'] in categories, f'Unknown category: {s[\"category\"]} in {s[\"id\"]}'
    for w in s['expected_vocabulary']:
        assert all(k in w for k in ('word', 'reading', 'gloss', 'priority')), f'Missing key in {s[\"id\"]}: {w}'
        assert w['priority'] in ('high', 'medium', 'low'), f'Bad priority in {s[\"id\"]}: {w}'
# Category distribution
from collections import Counter
cat_counts = Counter(s['category'] for s in scenarios)
for cat, count in sorted(cat_counts.items()):
    print(f'  {cat}: {count} scenarios')
print('Validation passed')
"
```

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
  build/data/learner_scenarios.json   # Learner scenario definitions for gap analysis
  build/analyze_scenarios.py          # Scenario-based vocabulary gap analysis
```

If a shared utility was created:

```
  build/coverage_utils.py             # Shared lookup utilities for coverage auditing
```

### Step D2: Update Makefile

Add a target:

```makefile
audit-scenarios:
	python3 build/analyze_scenarios.py --summary
```

Add `audit-scenarios` to the `.PHONY` line.

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
# Verify data file
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

   - Create build/data/learner_scenarios.json with 100-200 scenario definitions
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
