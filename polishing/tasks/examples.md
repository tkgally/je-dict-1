# Example Quality Review Task

This task focuses on ensuring example sentences meet the minimum count requirements, vocabulary tier restrictions, and quality standards.

**Reference:** See the `example-sentences` skill for complete guidelines.

## Minimum Example Requirements

### By Vocabulary Tier

| Tier | Minimum Examples per Sense |
|------|---------------------------|
| Basic | 5 |
| Core | 5 |
| General | 3 |

**Multi-sense entries:** Requirements apply per sense. A basic-tier entry with 3 senses needs 15+ examples total.

### Progressive Length

Examples within each sense should progress from shorter to longer:

| Example | Target Length |
|---------|---------------|
| 1 | Short (5-15 chars) |
| 2 | Short-medium (10-20 chars) |
| 3 | Medium (15-30 chars) |
| 4 | Medium-long (25-45 chars) |
| 5+ | Long or multi-sentence (35-70 chars) |

## Vocabulary Tier Restrictions

### Basic Tier Entries

| Examples | Restriction |
|----------|-------------|
| 1-2 | **Basic vocabulary only** |
| 3-5 | **Basic + Core vocabulary only** |

No general-tier or unlisted vocabulary allowed in any basic-tier examples.

### Core Tier Entries

| Examples | Restriction |
|----------|-------------|
| 1-2 | **Basic + Core vocabulary only** |
| 3-5 | No restriction (prefer dictionary words) |

### General Tier Entries

No restrictions (prefer dictionary words).

## Quality Standards for Examples

### Essential Requirements

1. **Natural Japanese**: Examples should sound like something a native speaker would say
2. **Clear context**: The usage should be understandable from the example
3. **Appropriate level**: Match the vocabulary tier restrictions
4. **Complete furigana**: All kanji must have `{kanji|reading}` markup

### Format Requirements

- ID format: `{entry_id}_ex{N}` (e.g., `00001_amaru_ex1`)
- `has_audio`: boolean indicating if audio file exists
- `sense_numbers`: array linking to definition sense(s)
- `notes`: optional clarifying information (null if not needed)

## Review Checklist

### Count and Distribution
- [ ] Entry has minimum examples for its tier (5 for basic/core, 3 for general)
- [ ] Each sense has adequate coverage
- [ ] Examples are properly distributed across senses

### Progressive Length
- [ ] Examples progress from shorter to longer
- [ ] Final examples are substantially longer or multi-sentence

### Vocabulary Compliance (Basic/Core Tiers)
- [ ] Examples 1-2 use only tier-appropriate vocabulary
- [ ] Examples 3+ use only allowed vocabulary
- [ ] No unlisted vocabulary in restricted examples

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
- [ ] Shows typical collocations
- [ ] At least one example shows a fixed phrase

### Metadata
- [ ] ID follows correct format
- [ ] IDs are sequential (ex1, ex2, ex3...)
- [ ] sense_numbers are valid and appropriate
- [ ] has_audio is accurate

## Common Issues

1. **Insufficient examples**: Entry doesn't meet minimum count for tier
2. **Missing furigana**: `お金が余った` instead of `お{金|かね}が{余|あま}った`
3. **Vocabulary violation**: Using general-tier words in basic-tier examples 1-2
4. **No length progression**: All examples are similar length
5. **Overly literal translations**: "As for me, I eat sushi" instead of "I eat sushi"
6. **Wrong sense_numbers**: Example linked to wrong definition
7. **Unnatural constructions**: Grammatically correct but rarely used patterns
8. **Missing sense coverage**: Some senses have no examples

## Remediation Steps

### When Examples Don't Meet Requirements

1. **Insufficient count**
   - Write new examples to meet minimum
   - Follow progressive length guidelines
   - Respect vocabulary tier restrictions

2. **Vocabulary tier violations**
   - Identify non-compliant vocabulary
   - Replace with tier-appropriate alternatives
   - Common substitutions:
     - {購入|こうにゅう}する → {買|か}う
     - {使用|しよう}する → {使|つか}う
     - {非常|ひじょう}に → とても

3. **No length progression**
   - Reorder existing examples by length
   - Revise examples to vary length
   - Add longer examples at the end

4. **Missing sense coverage**
   - Identify senses without examples
   - Write examples specifically for those senses
   - Update sense_numbers appropriately

### Preserving Existing Quality

- Keep existing high-quality examples
- Add to them rather than replacing
- Only replace examples with quality issues
- Maintain natural, idiomatic language

## Example Review Record

```json
{
  "entry_id": "00001_amaru",
  "tier": "core",
  "senses": 1,
  "required_examples": 5,
  "current_examples": 3,
  "status": "needs_examples",
  "changes": [
    "Added 2 new examples for sense 1",
    "Reordered examples by length",
    "Fixed furigana in example 2"
  ],
  "vocabulary_compliance": "passed",
  "quality_score": "good"
}
```

## Batch Processing Priority

Focus on entries in this order:

1. **Basic tier entries with <5 examples** (highest priority - most learner impact)
2. **Core tier entries with <5 examples**
3. **Basic tier entries with vocabulary violations**
4. **Core tier entries with vocabulary violations in ex 1-2**
5. **General tier entries with <3 examples**
6. **Entries flagged for example quality issues**
7. **Random sampling of reviewed entries**
