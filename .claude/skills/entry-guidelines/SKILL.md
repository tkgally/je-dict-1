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
5. **Longer sentences for more difficult vocabulary** - Words of level N2 or N1 should have at least one full-sentence example. Such examples may have a complex structure (with relative clauses, etc.) or consist of two sentences.

## Furigana Requirements

- All kanji MUST have furigana: `{漢字|かんじ}`
- Use compound readings for jukugo: `{友達|ともだち}` not `{友|とも}{達|だち}`
- Apply to headword, examples, notes, and all explanatory text

## Entry Structure

Every entry must include:
- `id`: Format `{romaji}_{5-digit-number}`
- `headword`: With furigana notation
- `reading`: Hiragana only
- `part_of_speech`: Consistent terminology
- `gloss`: Brief English equivalent
- `definitions`: Array with sense_number, gloss, explanation
- `examples`: 2-3 minimum, with Japanese, English, and optional notes
- `notes`: Usage notes, grammar patterns, common mistakes (see `vocabulary-notes` skill for formatting requirements)
- `metadata`: Including jlpt_level, created, modified timestamps

## Metadata Timestamps

**IMPORTANT**: Use actual current **UTC time** for `created` and `modified` fields. The website automatically converts to JST for display.

Generate timestamps dynamically:
```python
from datetime import datetime, timezone
timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
```

This produces: `"2026-01-11T04:15:42Z"` (UTC) → displays as `2026.1.11 13:15` (JST)

**Never use hardcoded timestamps** like `"2026-01-09T12:00:00Z"` - this causes incorrect dates in the Recent view.

**Validation checks for timestamp issues:**
- Future timestamps (created/modified time is in the future)
- Suspiciously round timestamps (exactly on the hour with :00:00 seconds, likely hardcoded)

Run `python3 build/validate.py` to check for these issues.

## Quality Checklist

Before finalizing any entry, verify:
- [ ] All kanji have furigana
- [ ] Examples progress from simple to complex
- [ ] At least one collocation or fixed phrase is shown
- [ ] Grammar patterns are explicitly demonstrated
- [ ] Notes cover common learner mistakes
- [ ] Notes are properly formatted (see `vocabulary-notes` skill)
- [ ] Depth matches similar entries in the dictionary
