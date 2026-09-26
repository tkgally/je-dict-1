# Vocabulary Tier Reassessment

**Enhancement plan section**: [1.2.2] Vocabulary Tier Reassessment

Create an audit prompt and helper script for reviewing vocabulary tier assignments. This produces a report for curator decision-making -- it does NOT make automatic tier changes.

## What This Prompt Creates/Modifies

| File | Action | Purpose |
|------|--------|---------|
| `prompts/audit_vocabulary_tiers.md` | **Create** | One-time/periodic audit prompt for reviewing tier assignments |
| `build/audit_tiers.py` | **Create** | Helper script: tier statistics, outlier detection, filtering |
| `prompts/metaprompt_list.md` | **Modify** | Add the audit prompt to the master prompt catalog |
| `CLAUDE.md` | **Modify** | Document `audit_tiers.py` in essential commands |

---

## Part A: Create the Tier Audit Helper Script

**Goal**: Build `build/audit_tiers.py`, a deterministic script that provides the data foundation for tier review. The script does not make judgments -- it surfaces statistics and outliers that the audit prompt (Part B) will evaluate.

### Step A1: Create `build/audit_tiers.py`

The script should:

1. **Load all entries** from `entries_index.json`
2. **Group entries by tier** (basic, core, general)
3. **Provide detailed breakdowns** and outlier detection

**Command-line interface**:

```
usage: audit_tiers.py [-h] [--tier {basic,core,general}]
                       [--pos POS] [--tags]
                       [--outliers] [--json]
                       [--list] [--ids-only]

Analyze vocabulary tier assignments and detect potential misclassifications.

optional arguments:
  --tier TIER           Filter to a specific tier (basic, core, general)
  --pos POS             Filter to a specific POS tag (e.g., noun, verb-ichidan)
  --tags                Show semantic tag distribution per tier
  --outliers            Flag statistical outliers (specialized words in basic/core)
  --json                Output in JSON format
  --list                List all entries in the filtered tier (with ID, word, reading, POS)
  --ids-only            Output only entry IDs (for piping to other scripts)
```

**Default output (no flags)**: Summary statistics.

```
=== Vocabulary Tier Summary ===

Basic tier: 801 entries
  Nouns:          342 (42.7%)
  Verbs:          198 (24.7%)
    verb-ichidan:  87
    verb-godan:    92
    verb-suru:     19
  Adjectives:     121 (15.1%)
    adjective-i:   78
    adjective-na:  43
  Adverbs:         62 (7.7%)
  Particles:       28 (3.5%)
  Expressions:     34 (4.2%)
  Other:           16 (2.0%)

Core tier: 1,982 entries
  Nouns:          891 (45.0%)
  ...

General tier: 20,217+ entries
  Nouns:          ...
  ...

=== Tier Boundary Statistics ===
Basic tier semantic tags (top 20):
  daily-life: 145, body: 42, food: 38, time: 35, ...
Core tier semantic tags (top 20):
  emotion: 89, business: 72, academic: 65, ...
```

**`--outliers` mode**:

Flag entries that may be misclassified based on heuristics:

1. **Specialized tags in basic tier**: Basic-tier entries with semantic tags like `legal`, `medical`, `academic`, `technical`, `literary`, `archaic` -- these may be too specialized for "survival communication"
2. **Specialized tags in core tier**: Core-tier entries with very narrow semantic tags
3. **Common tags in general tier**: General-tier entries with tags like `daily-life`, `greeting`, `body`, `family`, `food` that have high-priority feel -- these may belong in basic/core
4. **POS-based heuristics**: Particles and basic counters in general tier (these tend to be foundational)

Output format for `--outliers`:

```
=== Potential Tier Outliers ===

Basic tier -- potentially too specialized (12 entries):
  ID 00045: 裁判 (さいばん) [noun, legal] - trial/court case
  ID 00123: 症状 (しょうじょう) [noun, medical] - symptom
  ...

Core tier -- potentially too specialized (28 entries):
  ID 01234: 抽象的 (ちゅうしょうてき) [adjective-na, academic] - abstract
  ...

General tier -- potentially under-tiered (45 entries):
  ID 05678: ありがとう [expression, greeting] - thank you (informal)
  ID 06789: お母さん (おかあさん) [noun, family] - mother
  ...
```

**`--list` mode**: Show all entries for the filtered tier in a table:

```
ID      Word          Reading       POS             Tags
00001   食べる        たべる        verb-ichidan    food, daily-life
00002   飲む          のむ          verb-godan      food, daily-life
...
```

**`--ids-only` mode**: Output just the IDs, one per line. Useful for piping:

```bash
python3 build/audit_tiers.py --tier basic --ids-only | head -20
```

### Step A2: Implementation details

**Loading entries**: Use `entries_index.json` which contains all entry metadata including tier, POS, semantic tags, headword, and reading.

```python
#!/usr/bin/env python3
"""Analyze vocabulary tier assignments and detect potential misclassifications."""

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
INDEX_FILE = PROJECT_DIR / "entries_index.json"

# Semantic tags that suggest specialized vocabulary
SPECIALIZED_TAGS = {
    "legal", "medical", "academic", "technical", "literary",
    "archaic", "scientific", "financial", "military", "religious",
    "computing", "linguistics", "philosophy", "political"
}

# Semantic tags that suggest foundational vocabulary
FOUNDATIONAL_TAGS = {
    "daily-life", "greeting", "body", "family", "food",
    "time", "number", "direction", "color", "weather",
    "clothing", "house", "school"
}


def load_entries(index_file=INDEX_FILE):
    """Load entries from entries_index.json."""
    ...


def get_tier_stats(entries, tier=None):
    """Compute POS and tag statistics for entries in a tier."""
    ...


def find_outliers(entries):
    """Flag entries that may be misclassified based on heuristics."""
    ...


def print_summary(entries):
    """Print tier summary statistics."""
    ...


def print_outliers(entries):
    """Print potential misclassification report."""
    ...


def print_list(entries, tier, pos=None):
    """Print detailed entry list for a tier."""
    ...


def main():
    parser = argparse.ArgumentParser(
        description="Analyze vocabulary tier assignments and detect potential misclassifications."
    )
    parser.add_argument("--tier", choices=["basic", "core", "general"],
                        help="Filter to a specific tier")
    parser.add_argument("--pos", help="Filter to a specific POS tag")
    parser.add_argument("--tags", action="store_true",
                        help="Show semantic tag distribution per tier")
    parser.add_argument("--outliers", action="store_true",
                        help="Flag statistical outliers")
    parser.add_argument("--json", action="store_true", dest="json_output",
                        help="Output in JSON format")
    parser.add_argument("--list", action="store_true",
                        help="List all entries in the filtered tier")
    parser.add_argument("--ids-only", action="store_true",
                        help="Output only entry IDs")
    args = parser.parse_args()
    ...


if __name__ == "__main__":
    main()
```

**Heuristic tuning**: The outlier detection is intentionally broad. It flags *candidates* for review, not definitive misclassifications. False positives are expected and acceptable -- the audit prompt (Part B) evaluates each flagged entry.

**Handling tag variations**: Semantic tags in entries may use slightly different naming than the sets defined above. When matching, strip hyphens and normalize to lowercase. Check the actual tags used in `entries_index.json` (run `python3 build/tag_statistics.py` to see what tags exist) and adjust the `SPECIALIZED_TAGS` and `FOUNDATIONAL_TAGS` sets accordingly.

### Step A3: Test the script

```bash
# Default summary
python3 build/audit_tiers.py

# Filter by tier
python3 build/audit_tiers.py --tier basic
python3 build/audit_tiers.py --tier core

# Show tag distribution
python3 build/audit_tiers.py --tier basic --tags

# Outlier detection
python3 build/audit_tiers.py --outliers

# List mode
python3 build/audit_tiers.py --tier basic --list | head -30

# JSON output
python3 build/audit_tiers.py --tier basic --json | python3 -m json.tool | head -30

# IDs only
python3 build/audit_tiers.py --tier basic --ids-only | wc -l
```

Fix any issues found during testing.

---

## Part B: Create the Tier Audit Prompt

**Goal**: Create `prompts/audit_vocabulary_tiers.md` -- a prompt for Claude Code that systematically reviews tier assignments and produces a report. This is a one-time or periodic audit, not a repeating polishing task.

### Step B1: Create `prompts/audit_vocabulary_tiers.md`

Write the prompt file with these sections:

```markdown
# Vocabulary Tier Reassessment Audit

A periodic audit to verify that vocabulary tier assignments (basic, core, general) are appropriate. This produces a REPORT for curator review -- it does NOT make automatic changes.

## Background

The dictionary uses three vocabulary tiers:
- **Basic** (~800 entries): Foundational survival vocabulary. This tier is closed.
- **Core** (~2,000 entries): Essential vocabulary for adult communication. This tier is closed.
- **General** (20,000+ entries, growing): All other vocabulary.

Tier assignments were made during entry creation and have not been systematically reviewed. Some entries may be misclassified -- either too specialized for basic/core, or too foundational for general.

**Important**: This audit produces recommendations only. Tier changes are a curator decision because:
1. Moving entries between tiers affects vocabulary self-containment rules
2. Basic/core tiers are officially closed
3. Tier labels appear on the live site

## Step 1: Run the statistical helper

Start by running the audit helper script to get a data-driven overview:

```bash
# Get overall tier statistics
python3 build/audit_tiers.py

# Get outlier candidates
python3 build/audit_tiers.py --outliers

# Get detailed tag breakdown for basic tier
python3 build/audit_tiers.py --tier basic --tags

# Get detailed tag breakdown for core tier
python3 build/audit_tiers.py --tier core --tags
```

Review the outlier report. Note which entries are flagged and why.

## Step 2: Audit the basic tier

Read all basic-tier entries and evaluate each one:

```bash
# Get the list of basic-tier entry IDs
python3 build/audit_tiers.py --tier basic --ids-only > /tmp/basic_ids.txt
wc -l /tmp/basic_ids.txt
```

Process entries in batches of ~50. For each entry, evaluate:

1. **Is this genuinely foundational?** Would a learner need this word for basic survival communication (ordering food, asking directions, understanding simple signs, emergency situations)?
2. **Is it too specialized?** Words like medical terminology, legal terms, or academic vocabulary that require intermediate knowledge to encounter.
3. **Is the POS appropriate for basic tier?** Particles, basic greetings, numbers, and body parts are strong basic candidates. Specialized compound nouns are weaker.

For each questionable entry, note:
- Entry ID and word
- Current tier
- Reason it seems misclassified
- Suggested action (move to core, move to general, or keep with note)

**Read entries in batches**:

```bash
# Read a batch of basic-tier entries (adjust the range as you progress)
for id in $(python3 build/audit_tiers.py --tier basic --ids-only | head -50); do
  path=$(python3 build/get_entry_path.py $id "" 2>/dev/null || find entries/ -name "${id}_*" -type f | head -1)
  if [ -n "$path" ]; then
    echo "=== $path ==="
    cat "$path" | python3 -m json.tool | head -20
    echo ""
  fi
done
```

Or read individual entries that were flagged by the outlier detector:

```bash
# Read a specific entry
python3 build/get_entry_path.py ENTRY_ID ROMAJI
```

## Step 3: Audit the core tier

Same process as Step 2, but for core-tier entries:

```bash
python3 build/audit_tiers.py --tier core --ids-only > /tmp/core_ids.txt
wc -l /tmp/core_ids.txt
```

Evaluation criteria for core tier:
1. **Is this essential for adult communication?** Would a competent adult speaker use this word regularly in daily life, work, or social interactions?
2. **Is it too specialized?** Words needed only in narrow professional or academic contexts.
3. **Is it too basic?** Some core words might actually be foundational enough for the basic tier.

## Step 4: Reverse audit -- general tier words that may be under-tiered

Scan general-tier entries for words that arguably belong in basic or core:

```bash
# Get general-tier entries flagged as potentially under-tiered
python3 build/audit_tiers.py --outliers
```

Focus on:
1. General-tier entries with foundational semantic tags (daily-life, body, family, food, time)
2. General-tier particles and basic counters
3. General-tier greetings and set phrases
4. Very common verbs and adjectives that ended up in general tier because they were created after the basic/core tiers were closed

## Step 5: Produce the report

Write the report as your final output (do NOT create a file -- output it directly). Format:

```
## Tier Reassessment Report
Date: YYYY-MM-DD
Audited by: Claude Code (automated review)

### Summary
- Basic tier entries reviewed: N
- Core tier entries reviewed: N
- General tier entries scanned for under-tiering: N
- Total entries flagged for review: N

### Basic Tier (801 entries)

#### Potentially too specialized for basic (N entries):
- ID XXXXX: WORD (READING) [POS, tags] -- REASON
- ...

#### Appropriately placed but borderline (N entries):
- ID XXXXX: WORD (READING) [POS, tags] -- NOTE
- ...

### Core Tier (1,982 entries)

#### Potentially too specialized for core (N entries):
- ID XXXXX: WORD (READING) [POS, tags] -- REASON
- ...

#### Appropriately placed but borderline (N entries):
- ID XXXXX: WORD (READING) [POS, tags] -- NOTE
- ...

### General Tier -- Potentially Under-tiered

#### Candidates for basic tier (N entries):
- ID XXXXX: WORD (READING) [POS, tags] -- REASON

#### Candidates for core tier (N entries):
- ID XXXXX: WORD (READING) [POS, tags] -- REASON

### Recommendations
(Summary of findings and suggested next steps for the curator)
```

**Important**: This is a REPORT, not a set of changes. Do not modify any entry files. The curator will review the report and decide which changes (if any) to make.

## Notes

- This audit is expected to take a full session. If the session runs long, prioritize completing the basic tier audit and the outlier review, then note where you stopped for core tier.
- Be conservative in flagging entries. "Questionable" means genuinely uncertain -- do not flag entries that are clearly appropriate for their tier.
- The report should be informative enough for the curator to make decisions without re-reading every flagged entry.
```

---

## Part C: Documentation

### Step C1: Update `prompts/metaprompt_list.md`

In the "Project Health & Planning" section, add:

```markdown
### Audit vocabulary tiers
```
Read prompts/audit_vocabulary_tiers.md and follow the instructions to review vocabulary tier assignments and produce a reassessment report.
```
```

### Step C2: Update CLAUDE.md

In the "Essential commands" section, add in a "Reports" or "Auditing" subsection:

```bash
# Vocabulary tier analysis
python3 build/audit_tiers.py                    # Tier summary statistics
python3 build/audit_tiers.py --tier basic       # Basic tier breakdown
python3 build/audit_tiers.py --outliers         # Flag potential misclassifications
python3 build/audit_tiers.py --tier basic --list | head -30  # List basic entries
```

Update the project structure section to include:

```
  build/audit_tiers.py              # Vocabulary tier analysis and outlier detection
```

Also add `prompts/audit_vocabulary_tiers.md` to the "Task prompts" section description:

```
  prompts/audit_vocabulary_tiers.md   # Periodic tier reassessment audit (produces report)
```

### Step C3: Update Makefile

Add a target:

```makefile
audit-tiers:
	python3 build/audit_tiers.py --outliers
```

Add `audit-tiers` to the `.PHONY` line.

---

## Verification

After all parts are complete, run these checks:

```bash
# Verify the audit script runs
python3 build/audit_tiers.py

# Verify tier filtering
python3 build/audit_tiers.py --tier basic
python3 build/audit_tiers.py --tier core

# Verify outlier detection
python3 build/audit_tiers.py --outliers

# Verify tag breakdown
python3 build/audit_tiers.py --tier basic --tags

# Verify list mode
python3 build/audit_tiers.py --tier basic --list | head -10

# Verify JSON output
python3 build/audit_tiers.py --tier basic --json | python3 -m json.tool > /dev/null && echo "JSON output valid"

# Verify IDs-only mode
python3 build/audit_tiers.py --tier basic --ids-only | wc -l

# Verify the audit prompt exists
test -f prompts/audit_vocabulary_tiers.md && echo "OK: audit prompt exists" || echo "MISSING"

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
   git commit -m "Vocabulary tier reassessment: audit script and review prompt [1.2.2]

   - Create build/audit_tiers.py for tier statistics and outlier detection
   - Create prompts/audit_vocabulary_tiers.md for systematic tier review
   - Add --outliers mode to flag potential misclassifications
   - Update CLAUDE.md, Makefile, and metaprompt_list.md with documentation"
   ```
3. **Push** to the feature branch
4. **Create a PR**: `gh pr create --repo tkgally/je-dict-1 --head <branch> --base main --title "Vocabulary tier reassessment tools [1.2.2]" --body "..."`
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
