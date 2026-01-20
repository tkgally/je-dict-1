# Definition Quality Review Task

This task reviews and improves the clarity, accuracy, and completeness of dictionary definitions.

## Definition Structure

Each entry may have:
- `gloss`: Brief English equivalent (required)
- `definitions`: Array of numbered senses (optional but recommended for multi-sense words)

### Definition Object Format
```json
{
  "sense_number": 1,
  "gloss": "brief equivalent",
  "explanation": "fuller description of meaning and usage"
}
```

## Quality Standards

### Gloss Requirements
- Concise (aim for under 60 characters)
- Captures primary meaning
- Uses common English equivalents
- Multiple meanings separated by commas
- No articles unless grammatically necessary

### Definition Requirements
- Each distinct meaning gets a separate sense
- Senses numbered sequentially from 1
- Gloss is distinct from other senses
- Explanation adds value (not just restating gloss)
- Senses ordered by frequency/importance

## Review Checklist

### Accuracy
- [ ] Gloss accurately represents the Japanese word
- [ ] No false friends or misleading equivalents
- [ ] Nuances are captured appropriately
- [ ] Register matches (formal word has formal gloss)

### Completeness
- [ ] All major senses are covered
- [ ] Common usages are documented
- [ ] Idiomatic meanings included where relevant

### Clarity
- [ ] Definitions distinguish between senses
- [ ] Explanations are helpful for learners
- [ ] Technical terms explained or avoided
- [ ] Examples referenced in explanations if helpful

### Consistency
- [ ] Similar words have similar definition styles
- [ ] Terminology matches project conventions
- [ ] Level of detail appropriate for word importance

## Common Issues

1. **Overly literal**: "to do the action of walking" instead of "to walk"
2. **Too many senses**: Minor variations split into separate senses
3. **Too few senses**: Distinct meanings lumped together
4. **Redundant explanations**: Explanation just restates gloss
5. **Missing context**: Definition accurate but doesn't show usage

## Improvement Strategies

### For verbs
- Include typical particles in gloss if helpful
- Note if meaning changes with different particles
- Distinguish physical/metaphorical uses

### For adjectives
- Capture emotional connotation
- Note if mainly used as predicate or modifier

### For nouns
- Include classifier hints if non-obvious
- Note count/mass distinction if applicable

### For particles
- Focus on function rather than translation
- Link to key predicates that use it

## Recording Changes

```json
{
  "entry_id": "00100_example",
  "definition_changes": [
    {
      "type": "added_sense",
      "sense_number": 2,
      "reason": "Idiomatic meaning was missing"
    },
    {
      "type": "improved_gloss",
      "old": "to make to become different",
      "new": "to change, to alter"
    }
  ]
}
```

## Priority Order

1. Basic tier entries (high impact)
2. Entries with only gloss (no definitions array)
3. Multi-sense words with poor differentiation
4. Entries flagged for definition issues
