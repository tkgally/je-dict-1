# Tag Accuracy Review Task

This task verifies that all entry tags are accurate and consistent with the tag taxonomy.

## Tag Categories

Tags are stored in `metadata.tags` and include:

### pos (Part of Speech)
Valid values from `build/tag_taxonomy.json`:
- verb-godan, verb-ichidan, verb-suru, verb-kuru, verb-special
- adjective-i, adjective-na, adjective-no
- noun, noun-verbal, noun-adverbial, noun-temporal
- particle, adverb, counter, expression, prefix, suffix, conjunction, interjection

### verb_class (Verb Conjugation)
- godan-u, godan-ku, godan-gu, godan-su, godan-tsu, godan-nu, godan-bu, godan-mu, godan-ru
- ichidan
- irregular-suru, irregular-kuru, irregular-other

### transitivity
- transitive
- intransitive
- both

### formality
- formal
- neutral
- informal
- vulgar

### politeness
- honorific
- humble
- polite
- plain

### style
Array that may include: written, spoken, literary, archaic, slang, colloquial

### domain
Array that may include: business, academic, technical, medical, legal, religious, culinary, sports, etc.

### semantic
Array from comprehensive taxonomy covering: time, nature, human, abstract, objects, actions, social, linguistic categories

## Review Checklist

### Part of Speech Tags
- [ ] pos array matches part_of_speech field
- [ ] Correct verb type (godan vs ichidan)
- [ ] Correct adjective type (i vs na)

### Verb-Specific Tags
- [ ] verb_class is accurate for conjugation pattern
- [ ] transitivity correctly identified
- [ ] Both transitivity and verb_class set for all verbs

### Register Tags
- [ ] formality reflects actual usage level
- [ ] politeness correctly identifies keigo level
- [ ] style tags capture written/spoken preference

### Semantic Tags
- [ ] At least one semantic tag assigned
- [ ] Tags are from valid taxonomy
- [ ] Tags accurately describe the word's meaning

## Common Issues

1. **Wrong verb class**: godan-ru vs ichidan confusion
2. **Missing transitivity**: Verbs without transitivity tag
3. **Over-tagging**: Too many semantic tags
4. **Under-tagging**: Missing obvious categories
5. **Inconsistent formality**: Similar words tagged differently

## Validation

Run tag validation:
```bash
python3 build/validate_tags.py
```

This checks:
- Valid part_of_speech values
- Valid verb_class for verb types
- Valid formality/politeness values
- Valid style/domain values
- Valid semantic tags from taxonomy

## Tag Selection Guidelines

### Formality
- formal: Used in official documents, ceremonies
- neutral: Standard polite conversation (default)
- informal: Casual speech between friends
- vulgar: Crude or offensive

### Politeness
- honorific: Elevates the subject (尊敬語)
- humble: Lowers the speaker (謙譲語)
- polite: Standard polite forms (丁寧語)
- plain: Dictionary form, casual

### Style
- written: Primarily seen in text
- spoken: Primarily in conversation
- literary: Formal written style
- archaic: Older usage

## Recording Changes

```json
{
  "entry_id": "00100_example",
  "tag_changes": [
    {
      "field": "transitivity",
      "old": null,
      "new": "intransitive",
      "reason": "Verb was missing transitivity tag"
    },
    {
      "field": "semantic",
      "old": ["action"],
      "new": ["action", "movement"],
      "reason": "Added movement category for motion verb"
    }
  ]
}
```

## Priority

1. Entries failing tag validation
2. Verbs missing verb_class or transitivity
3. Entries with no semantic tags
4. Basic tier entries (high visibility)
