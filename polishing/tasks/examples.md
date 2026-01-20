# Example Quality Review Task

This task focuses on ensuring example sentences are high quality, properly formatted, and pedagogically valuable.

## Quality Standards for Examples

### Essential Requirements

1. **Natural Japanese**: Examples should sound like something a native speaker would say
2. **Clear context**: The usage should be understandable from the example
3. **Appropriate level**: Match the vocabulary tier (basic examples for basic words)
4. **Complete furigana**: All kanji must have `{kanji|reading}` markup

### Format Requirements

- ID format: `{entry_id}_ex{N}` (e.g., `00001_amaru_ex1`)
- `has_audio`: boolean indicating if audio file exists
- `sense_numbers`: array linking to definition sense(s)
- `notes`: optional clarifying information (null if not needed)

## Review Checklist

For each example:

### Japanese Text
- [ ] Grammar is correct
- [ ] Vocabulary is appropriate for the context
- [ ] All kanji have furigana markup
- [ ] Punctuation is correct (Japanese periods and commas)
- [ ] The target word is used naturally

### English Translation
- [ ] Translation is accurate
- [ ] English is natural (not overly literal)
- [ ] Matches the register of the Japanese
- [ ] Captures nuance where important

### Pedagogical Value
- [ ] Illustrates the specific sense clearly
- [ ] Uses common constructions
- [ ] Avoids overly complex grammar
- [ ] Shows typical collocations

### Metadata
- [ ] ID follows correct format
- [ ] sense_numbers are valid and appropriate
- [ ] has_audio is accurate

## Common Issues

1. **Missing furigana**: `お金が余った` instead of `お{金|かね}が{余|あま}った`
2. **Overly literal translations**: "As for me, I eat sushi" instead of "I eat sushi"
3. **Wrong sense_numbers**: Example linked to wrong definition
4. **Unnatural constructions**: Grammatically correct but rarely used patterns

## Improvement Opportunities

When examples are weak, consider:
- Adding a second example for complex words
- Replacing overly simple examples with more illustrative ones
- Adding notes to explain cultural context
- Creating examples that show common collocations

## Example Review Record

```json
{
  "entry_id": "00001_amaru",
  "example_id": "00001_amaru_ex1",
  "status": "improved",
  "changes": [
    "Added missing furigana to 金",
    "Made English translation more natural"
  ],
  "quality_score": "good"
}
```

## Batch Processing

Focus on:
1. Entries with no examples (critical gap)
2. Entries with examples missing furigana
3. Basic tier entries (high-value improvements)
4. Entries flagged for example issues
