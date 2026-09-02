# Vocabulary Tier Reassessment Audit

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

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
  path=$(find entries/ -name "${id}_*" -type f | head -1)
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
