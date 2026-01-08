---
name: entry-guidelines
description: General quality standards for all je-dict-1 dictionary entries. Use when creating or revising any entry type.
---

# Dictionary Entry Quality Guidelines

When creating or revising dictionary entries for je-dict-1, follow these quality standards:

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
- `metadata`: Including jlpt_level

## Quality Checklist

Before finalizing any entry, verify:
- [ ] All kanji have furigana
- [ ] Examples progress from simple to complex
- [ ] At least one collocation or fixed phrase is shown
- [ ] Grammar patterns are explicitly demonstrated
- [ ] Notes cover common learner mistakes
- [ ] Notes are properly formatted (see `vocabulary-notes` skill)
- [ ] Depth matches similar entries in the dictionary
