---
name: consolidate-entries
description: Guidelines for identifying and merging duplicate or variant dictionary entries. Covers kana/kanji variants, overlapping entries, and candidate deduplication.
---

# Consolidating Dictionary Entries

Use this skill when checking whether entries should be merged, or when verifying that a new entry or candidate is not a variant of something that already exists.

## When to Use This Skill

1. **During polishing sessions** — systematically reviewing entries for merge candidates
2. **Before creating a new entry** — verify the word isn't a spelling variant of an existing entry
3. **Before adding a candidate** — verify the candidate isn't a variant of an existing entry or candidate
4. **When `find_merge_candidates.py` flags potential issues** — evaluate each case semantically

## What Counts as a Merge Candidate?

Merge candidates are entries that represent **the same lexical item** but with different surface forms. This is distinct from homophones (different words that happen to share a reading).

### SHOULD be merged (same word, different spelling)

- **Kana vs kanji variant**: なくなる (01966) and {無|な}くなる (01101) — same word, one written in kana, one with kanji
- **Alternative kanji**: {匂|にお}い and {臭|にお}い when used for the same sense — same word, different kanji choices
- **Okurigana variants**: {行|おこな}う and {行|おこ}なう — same word, different okurigana conventions

### SHOULD NOT be merged (different words)

- **Homophones with different meanings**: {無|な}くなる (to disappear) and {亡|な}くなる (to pass away) — different words sharing a reading, distinguished by kanji
- **Noun + する pairs**: {喧嘩|けんか} and {喧嘩|けんか}する — these are kept as separate entries with cross-references
- **Related but distinct words**: {見|み}る and {見|み}える — different verbs

## The Key Distinction: Semantic Judgment

The `find_merge_candidates.py` script can identify entries that share a reading. But determining whether they are the same word requires **semantic judgment**:

- **Same meaning, same usage, just different writing** → MERGE
- **Different meanings distinguished by kanji** → Keep separate, add cross-references
- **Same root but different grammatical function** → Keep separate, add cross-references

### Decision Framework

Ask these questions in order:

1. **Do the entries have the same part of speech?** If not, they are almost certainly different lexical items (keep separate).

2. **Do the entries have overlapping definitions?** If the core meanings are the same, they may be the same word.

3. **Is the kanji distinction meaningful to learners?** If Japanese speakers use different kanji to signal different meanings (e.g., {聞|き}く "hear" vs {聴|き}く "listen attentively"), keep them separate. If the kanji is just an optional writing convention (e.g., {無|な}くなる vs なくなる for "disappear"), merge.

4. **Would a Japanese dictionary list them as separate headwords?** Consult your knowledge of how major Japanese dictionaries handle the distinction.

## Merge Procedure

When you determine that two entries should be merged:

### Step 1: Choose the Keeper

Select the entry to keep using these criteria (in priority order):

| Criterion | Preference |
|-----------|-----------|
| **Headword form** | Prefer the kanji form (more informative for learners) |
| **Content quality** | More complete definitions, better examples, richer notes |
| **Vocabulary tier** | If one is basic/core, keep that one |
| **Lower ID** | Tie-breaker: keep the older entry |

### Step 2: Merge Content

Before deleting, transfer valuable content from the entry being removed:

- Unique example sentences (renumber IDs to fit the keeper)
- Additional notes sections
- Cross-references
- Any senses not covered by the keeper

**Update the keeper's `modified` timestamp** using `python3 build/get_timestamp.py`.

### Step 3: Delete the Duplicate

Follow the `delete-entry` skill:

1. Delete the entry file
2. Search for cross-references pointing to the deleted entry and update them
3. Run `python3 build/update_indexes.py`
4. Run `make index   # indexes + kanji JSON; the site builds in CI after merge`
5. Run `python3 build/validate.py`

### Step 4: Add Cross-References if Needed

If the merged entry has an alternative kanji form that learners might look up, mention it in the notes field. For example, if merging the kana form なくなる into {無|な}くなる, the notes should mention that the word is also commonly written in kana only.

## Integration with Entry Creation

### When Creating Entries from Candidates

Before creating any entry, the existing `check_duplicate.py` checks for exact matches (same reading AND same headword). However, it does NOT catch spelling variants. You must also consider:

1. **Is there an existing entry with the same reading but different headword?**
   - If `check_duplicate.py` reports homophones, examine each one
   - If a homophone has the same meaning and part of speech, this is a variant, not a new entry
   - Instead of creating a new entry, consider updating the existing entry's notes to mention the alternative spelling

2. **Run the extended check** when homophones are flagged:
   ```bash
   python3 build/check_duplicate.py --skip-candidates "word" "reading"
   ```
   If the output shows "Homophones exist", read those entries and determine whether your candidate is truly a distinct word.

### When Adding Candidates

Apply the same logic: if a candidate has the same reading as an existing entry or candidate, verify that it represents a genuinely different word before adding it.

## Running the Detection Script

```bash
# Full report of all issues
python3 build/find_merge_candidates.py

# Only potential merges
python3 build/find_merge_candidates.py --merge-only

# Machine-readable output
python3 build/find_merge_candidates.py --json
```

The script identifies candidates deterministically. Your job is to evaluate each case semantically and decide the correct action: merge, keep separate with cross-references, or dismiss as a false positive.

## Checklist

- [ ] Ran `find_merge_candidates.py` to identify candidates
- [ ] Evaluated each candidate semantically (not just mechanically)
- [ ] For merges: chose keeper, transferred content, deleted duplicate
- [ ] For non-merges: verified cross-references exist between related entries
- [ ] Updated indexes and rebuilt after changes
- [ ] Validation passes
