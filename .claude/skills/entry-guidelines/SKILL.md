---
name: entry-guidelines
description: General quality standards for all je-dict-1 dictionary entries. Use when creating or revising any entry type.
---

# Dictionary Entry Quality Guidelines

When creating or revising dictionary entries for je-dict-1, follow these quality standards:

## CRITICAL: Write Each Entry Individually

**DO NOT use Python scripts or automation to mass-produce entries.**

Each dictionary entry must be written individually by hand, using:
- Your own linguistic knowledge
- The guidelines in this skill and related skills (`verb-entry`, `adjective-entry`, `particle-entry`, `other-entries`, `vocabulary-notes`)
- Careful consideration of each word's unique characteristics

**Why this matters:**
- Each word has nuances that require individual attention
- Examples must be natural and contextually appropriate
- Notes should address learner-specific challenges for that word
- Mass-produced entries lack the quality and depth learners need

**The correct workflow:**
1. Select a word from `candidate_words.json` or user request
2. Research/consider the word's usage, collocations, and common patterns
3. Write the entry JSON directly using the Write tool
4. Validate: `python3 build/validate.py`
5. Repeat for each entry

**After finishing all entries for a session:**
```bash
python3 build/validate.py           # Validate all entries
python3 build/update_indexes.py     # Update indexes and sync candidates
python3 build/build_flat.py         # Rebuild website (REQUIRED for GitHub Pages)
git add entries/ docs/ *.json PROJECT_STATUS.md
git commit -m "Add N new dictionary entries"
git push
```
The `build_flat.py` step is critical - without it, new entries won't appear on the live site.

**Never create scripts that generate entry content programmatically.**

## Before Creating a New Entry

**IMPORTANT**: Always check if an entry already exists before creating a new one.

1. **Search for existing entries** by reading or headword:
   ```bash
   # Search by reading
   grep -r '"reading": "たべる"' entries/

   # Search by headword pattern
   grep -r '食べる' entries/
   ```

2. **If an entry already exists**: Skip to the next word. Do NOT create a duplicate.

3. **If the word was in candidate_words.json**: Remove it from the candidate list after confirming an entry exists.

4. **Only create new entries** for words that have no existing entry in the dictionary.

This prevents duplicate entries and wasted effort on entries that must later be deleted.

## Content Guidelines

1. **Explain before exemplifying** - Definition first, then examples
2. **One meaning = one example minimum** - Every sense needs illustration
3. **Show grammatical connections** - Always demonstrate how words connect
4. **Prefer natural Japanese** - Avoid textbook stiffness
5. **Highlight non-obvious distinctions** - Focus on what learners cannot infer from English

## Consistency Guidelines

1. **Consistent depth across similar entries** - Don't over-explain one verb while under-explaining another
2. **Consistent structure within entry types** - All verbs should have same sections
3. **Consistent terminology** - Use same labels throughout (USAGE NOTES, not sometimes Notes)

## Example Sentence Guidelines

1. **First example should be simple** - Demonstrate the word clearly without complexity
2. **Progress to natural complexity** - Later examples can show real-world usage
3. **Include at least one fixed phrase** - High-frequency collocations aid memory
4. **Annotate non-obvious grammar** - Use [Note: ...] for grammatical explanations
5. **Longer sentences for more difficult vocabulary** - Words that will be classified as core or general tier vocabulary should have at least one full-sentence example. Such examples may have a complex structure (with relative clauses, etc.) or consist of two sentences.
6. **Always include sense_numbers** - Every example must specify which definition sense(s) it illustrates

### Sense Numbers Requirement

Every example sentence **must** have a `sense_numbers` field that links it to the definition(s) it illustrates:

```json
"examples": [
  {
    "id": "word_00001_ex1",
    "japanese": "...",
    "english": "...",
    "sense_numbers": [1]
  }
]
```

**Rules:**
- **Single-sense entries**: Use `[1]` for all examples
- **Multi-sense entries**: Each example must specify which sense(s) it demonstrates
- **Examples illustrating multiple senses**: Use `[1, 2]` format
- **Must reference valid senses**: Numbers must match `sense_number` values in definitions

**Example for multi-sense entry:**
```json
"definitions": [
  { "sense_number": 1, "gloss": "to stuff" },
  { "sense_number": 2, "gloss": "to cram (study)" }
],
"examples": [
  { "id": "..._ex1", "sense_numbers": [1], ... },  // illustrates sense 1
  { "id": "..._ex2", "sense_numbers": [2], ... },  // illustrates sense 2
  { "id": "..._ex3", "sense_numbers": [1, 2], ... } // illustrates both
]
```

The validation script checks that all examples in multi-sense entries have valid sense_numbers.

## Furigana Requirements (CRITICAL)

**All kanji MUST have furigana in ALL fields, including notes.**

Format: `{漢字|かんじ}`

This applies to:
- Headwords
- Example sentences
- **Notes field** (idioms, collocations, cultural notes, etc.)
- All explanatory text

**Common mistakes to avoid:**
```
✗ WRONG: 暖簾に腕押し
✓ RIGHT: {暖簾|のれん}に{腕押|うでお}し

✗ WRONG: 安堵の息をつく
✓ RIGHT: {安堵|あんど}の{息|いき}をつく

✗ WRONG: Sometimes written as 家鴨
✓ RIGHT: Sometimes written as {家鴨|あひる}
```

Use compound readings for jukugo: `{友達|ともだち}` not `{友|とも}{達|だち}`

**Verify before finalizing:**
```bash
python3 build/verify_furigana.py <entry_id>
```

## Entry Structure

Every entry must include:
- `id`: Format `{romaji}_{5-digit-number}`
- `headword`: With furigana notation
- `reading`: Hiragana only
- `part_of_speech`: Consistent terminology
- `gloss`: Brief English equivalent
- `definitions`: Array with sense_number, gloss, explanation
- `examples`: 2-3 minimum, with id, Japanese, English, sense_numbers, and optional notes
- `notes`: Usage notes, grammar patterns, common mistakes (see `vocabulary-notes` skill for formatting requirements)
- `metadata`: Including vocabulary_tier (null until assigned), created, modified timestamps

## Metadata Timestamps

**CRITICAL**: Timestamps MUST be actual current UTC time. The website converts UTC to JST (+9 hours) for display. Incorrect timestamps will show as wrong dates/times (often appearing hours or days in the future).

### How to Get the Correct Timestamp

**ALWAYS run this command** to get the current UTC timestamp before writing each entry:

```bash
python3 build/get_timestamp.py
```

This outputs the current UTC time, e.g.: `2026-01-12T10:45:30Z`

Copy this exact output into both `created` and `modified` fields (for new entries) or just `modified` (for revisions).

### Why This Matters

- The `Z` suffix means UTC (not local time, not JST)
- The build script adds 9 hours to convert to JST for display
- If you write `16:00:00Z` when actual UTC is `10:00`, it displays as **01:00 JST next day** (wrong!)
- If you write `10:00:00Z` when actual UTC is `10:00`, it displays as **19:00 JST same day** (correct!)

### Common Mistakes to Avoid

1. **DO NOT** guess or estimate the timestamp
2. **DO NOT** use your perception of current time - always run the script
3. **DO NOT** use round hours like `12:00:00Z` or `15:00:00Z` (these are almost certainly wrong)
4. **DO NOT** copy timestamps from other entries
5. **DO NOT** write JST time with a Z suffix (this causes 9-hour errors)

### Validation

Run `python3 build/validate.py` to check for:
- Future timestamps (timestamp is ahead of current UTC time)
- Suspiciously round timestamps (exactly `:00:00` seconds, likely not from the script)

## Quality Checklist

Before finalizing any entry, verify:
- [ ] **All kanji have furigana** (headword, examples, AND notes)
- [ ] Verify: `python3 build/verify_furigana.py <entry_id>` shows "✓ OK"
- [ ] Examples progress from simple to complex
- [ ] At least one collocation or fixed phrase is shown
- [ ] Grammar patterns are explicitly demonstrated
- [ ] Notes cover common learner mistakes
- [ ] Notes are properly formatted (see `vocabulary-notes` skill)
- [ ] Depth matches similar entries in the dictionary
- [ ] All examples have valid sense_numbers
