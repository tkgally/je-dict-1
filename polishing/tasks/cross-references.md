# Cross-Reference Review Task

This task focuses on validating and improving the cross-reference system, ensuring all links are valid and relationships are properly documented.

## Objectives

1. Validate that all cross-references point to existing entries
2. Ensure reference types accurately describe relationships
3. Add missing cross-references (pairs, synonyms, antonyms)
4. Verify bidirectional links where appropriate

## Reference Types

Valid cross_reference types (from `build/constants.py`):
- `pair` - Transitive/intransitive verb pairs
- `synonym` - Words with similar meanings
- `antonym` - Words with opposite meanings
- `keigo` - Honorific/humble equivalents
- `related` - Conceptually related words
- `see_also` - Entries worth consulting
- `contrast` - Words that learners often confuse
- `homophone` - Words with the same reading

## Review Process

### 1. Validation Check

For each entry with cross_references:
- [ ] target_id (if present) points to an existing entry
- [ ] reading matches an existing entry's reading
- [ ] headword is accurate
- [ ] label describes the relationship correctly
- [ ] type is appropriate for the relationship

### 2. Missing References

Look for entries that should have cross-references:
- Transitive/intransitive verb pairs (check notes for "pair" mentions)
- Synonyms mentioned in notes
- Antonyms mentioned in definitions
- Related words in the same semantic field

### 3. Bidirectional Links

When entry A references entry B:
- Check if B should reference A
- For pairs: both should reference each other
- For synonyms: typically bidirectional
- For see_also: may be unidirectional

### 4. Reference Quality

Improve existing references:
- Add missing labels for clarity
- Update stale headwords/readings
- Convert soft references (reading only) to hard references (with target_id) where beneficial

## Tools

Run validation to check for broken references:
```bash
python3 build/validate.py
```

Check for potential references to add:
```bash
grep -r '"pair"' entries/ | head -20
```

## Recording Changes

Document each reference change:
```json
{
  "entry_id": "00001_amaru",
  "action": "added_reference",
  "details": {
    "type": "pair",
    "target": "00002_amasu",
    "reason": "Transitive pair mentioned in notes"
  }
}
```

## Common Patterns to Fix

1. **Missing pair links**: Notes mention a pair but no cross_reference exists
2. **Stale references**: Reading/headword no longer matches the target
3. **Missing bidirectional**: A references B but B doesn't reference A
4. **Wrong type**: "synonym" used where "contrast" would be more accurate

## Session Output

Report should include:
- Number of references validated
- Number of broken references fixed
- Number of new references added
- Entries flagged for manual review
