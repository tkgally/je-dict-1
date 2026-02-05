# Add Entries for Words Marked `noentry`

Create dictionary entries for words that were marked `noentry` in inline word links, then update those links with the correct entry IDs.

## Overview

When adding inline word links to example sentences, words without dictionary entries are marked with `noentry`:

```
⟦{暴走|ぼうそう}→暴走：noentry⟧
```

This task creates entries for these words and updates the links.

## Workflow

### Phase 1: Find All `noentry` Words

1. **Search for noentry occurrences**:
   ```bash
   grep -r "：noentry⟧" entries/ --include="*.json" -h | \
     grep -oE '⟦[^⟧]+：noentry⟧' | sort | uniq -c | sort -rn
   ```

2. **Extract unique words needing entries**:
   ```bash
   grep -r "：noentry⟧" entries/ --include="*.json" -h | \
     grep -oE '→[^：]+：noentry' | sed 's/→//;s/：noentry//' | sort -u
   ```

3. **Create a working list** of words to add, noting:
   - The word (baseform)
   - Its reading (from the surface form with furigana)
   - The part of speech
   - How many times it appears

### Phase 2: Create Entries for Each Word

For each word in your list:

1. **Check for duplicates** (the word might exist under a different ID):
   ```bash
   python3 build/check_duplicate.py --skip-candidates "暴走" "ぼうそう"
   ```

2. **Get timestamp**:
   ```bash
   python3 build/get_timestamp.py
   ```

3. **Determine the part of speech** and load the appropriate skill:
   - Verbs: `.claude/skills/verb-entry/SKILL.md`
   - Adjectives: `.claude/skills/adjective-entry/SKILL.md`
   - Nouns/Others: `.claude/skills/other-entries/SKILL.md`
   - Particles: `.claude/skills/particle-entry/SKILL.md`

4. **Create the entry** following these requirements:
   - Use `vocabulary_tier: "general"` for all new entries
   - Include at least 3 examples per sense
   - All kanji must have furigana in all fields
   - Include all required tags (pos, formality, politeness, semantic)

5. **Determine the entry ID**:
   - Find the next available ID:
     ```bash
     python3 -c "
     import json
     data = json.load(open('entries_index.json'))
     ids = [int(e['id'].split('_')[0]) for e in data['entries']]
     print(f'Next ID: {max(ids) + 1:05d}')
     "
     ```
   - Format: `{5-digit-number}_{romaji}` (e.g., `09478_bousou`)

6. **Write the entry file**:
   - Path: `entries/{id_range}/{id}_{romaji}.json`
   - `{id_range}` is the ID rounded down to nearest 500 (e.g., 09478 → 09000)
   - Example: Entry ID `09478_bousou` goes in `entries/09000/09478_bousou.json`

### Phase 3: Update `noentry` Links

After creating entries, update the inline links:

1. **Find files containing the specific noentry**:
   ```bash
   grep -r "→暴走：noentry⟧" entries/ --include="*.json" -l
   ```

2. **For each file**, update the link:
   - Old: `⟦{暴走|ぼうそう}→暴走：noentry⟧`
   - New: `⟦{暴走|ぼうそう}→暴走：09478_bousou⟧`

3. **Update the modified timestamp** for each changed entry

### Phase 4: Verify and Validate

1. **Run validation**:
   ```bash
   python3 build/validate.py 2>&1 | grep -A5 "Word link"
   ```

2. **Verify each updated link semantically**:
   - Read the example sentence in context
   - Confirm the new entry's gloss matches the word's meaning
   - Check that the link is grammatically appropriate

3. **Update indexes** (but do NOT build the site):
   ```bash
   python3 build/update_indexes.py
   ```

### Phase 5: Commit Changes

1. **Commit new entries**:
   ```bash
   git add entries/ && git commit -m "Add entries for noentry words: [list words]"
   ```

2. **Commit link updates separately**:
   ```bash
   git add entries/ && git commit -m "Update noentry links with new entry IDs"
   ```

**Note:** Do NOT run `build_flat.py` - the site build is skipped for this task.

## Quality Checklist

### For New Entries
- [ ] Duplicate check passed
- [ ] All kanji have furigana (headword, examples, notes)
- [ ] At least 3 examples per sense
- [ ] All examples have `sense_numbers`
- [ ] Tags complete (pos, formality, politeness, semantic)
- [ ] `vocabulary_tier: "general"`

### For Updated Links
- [ ] Entry ID is correct
- [ ] Meaning matches context in the original example
- [ ] Furigana preserved correctly
- [ ] No broken link syntax

## Common `noentry` Word Types

Based on inline linking work, these categories often need entries:

| Category | Examples | Notes |
|----------|----------|-------|
| Grammatical words | です, ます, た | Copulas, auxiliaries |
| Technical terms | 漢字, 部首 | Subject-specific vocabulary |
| Idiom components | つく (in 嘘をつく) | Verbs with idiomatic uses |
| Specialized verbs | 利く (brakes working) | Homographs with specific meanings |
| Loanwords | データ, グラフ | Katakana words |

## Prioritization

When multiple `noentry` words exist, prioritize:

1. **High frequency** - Words appearing in many examples
2. **Core vocabulary** - Basic words learners need
3. **Grammatical words** - Essential for understanding sentences
4. **Domain clusters** - Words from the same topic area

## Example Session

```
Found noentry words:
  15  暴走 (ぼうそう) - noun
   8  漢字 (かんじ) - noun
   5  です (です) - copula
   3  利く (きく) - verb

Creating entry for 暴走...
- Duplicate check: OK
- Entry ID: 09478_bousou
- Created: entries/09000/09478_bousou.json

Updating links...
- entries/00000/00022_bureeki.json: 1 link updated
- entries/01000/01234_example.json: 2 links updated

Validation: PASSED
```

## Session Output

At session end, report:
1. Number of entries created
2. Number of links updated
3. Any words skipped (with reason)
4. Remaining `noentry` count
