# Notes Field Consistency Review Task

This task standardizes the formatting and content of the notes field across all entries, following the guidelines in the vocabulary-notes skill.

## Standard Notes Structure

Notes should follow a consistent format:

```
Brief introductory paragraph about the word.

SECTION HEADER:
- Bullet points with information
- Additional details

ANOTHER SECTION:
Content as appropriate...
```

## Common Section Headers

Depending on word type, notes may include:

### For Verbs
- TRANSITIVITY
- ASPECT (ている)
- COMMON PATTERNS
- USAGE NOTES
- RELATED EXPRESSIONS

### For Adjectives
- USAGE AS PREDICATE
- USAGE AS MODIFIER
- CONJUGATION NOTES
- SIMILAR WORDS

### For Particles
- BASIC FUNCTION
- COMMON PATTERNS
- CONTRAST WITH [other particle]
- REGISTER

### For All Words
- CULTURAL NOTES
- COMMON MISTAKES
- REGISTER/FORMALITY
- ETYMOLOGY (when helpful)

## Formatting Rules

1. **Headers**: ALL CAPS followed by colon
2. **Lists**: Use bullet points with hyphens
3. **Furigana**: Include on all kanji `{kanji|reading}`
4. **Examples in notes**: Italicize with context
5. **Line breaks**: Double line break between sections

## Review Checklist

- [ ] Introductory sentence is present and helpful
- [ ] Section headers follow ALL CAPS: format
- [ ] Content is organized logically
- [ ] No redundancy with definitions or examples
- [ ] Furigana is complete
- [ ] Appropriate level of detail
- [ ] Consistent terminology with other entries

## Common Issues to Fix

1. **Inconsistent headers**: "Usage Notes" vs "USAGE NOTES" vs "Usage:"
2. **Missing structure**: Wall of text without sections
3. **Redundant information**: Repeating the gloss
4. **Missing furigana**: Kanji without readings
5. **Overly technical**: Linguistic jargon not helpful for learners

## Standardization Examples

### Before
```
This verb means to remain. It's intransitive. The transitive form is amasu.
You can say "okane ga amatta" for money left over.
```

### After
```
{余|あま}る is an intransitive verb meaning to be left over or remain.

TRANSITIVITY:
- Type: {自動詞|じどうし} (intransitive)
- Pair: {余|あま}す (transitive, to leave over)

ASPECT (ている):
- {余|あま}っている indicates a resulting state: "there is [something] left over"
```

## Recording Changes

```json
{
  "entry_id": "00001_amaru",
  "notes_status": "reformatted",
  "changes": [
    "Added section headers",
    "Reorganized content into TRANSITIVITY and ASPECT sections",
    "Added furigana to kanji"
  ]
}
```

## Priority

1. Basic tier entries (most viewed)
2. Entries with substantial notes but poor formatting
3. Verb and particle entries (benefit most from structure)
4. Entries with user-reported confusion
