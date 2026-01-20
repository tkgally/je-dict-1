# Full Entry Review Task

This task performs a complete quality review of dictionary entries, checking all fields against the project's quality standards.

## Before Starting

1. Read `polishing/progress.json` to identify entries not yet reviewed
2. Read `polishing/queue.json` to check for prioritized entries
3. Read `polishing/issues.json` to understand known patterns to watch for
4. Read the most recent session log in `polishing/sessions/` for context

## Entry Selection

Choose entries based on this priority:
1. Entries in `queue.json` high_priority list
2. Entries never reviewed (not in progress.json)
3. Entries with stale reviews (> 90 days)
4. Random sampling from remaining entries

Default batch size: 20 entries per session

## Review Checklist

For each entry, verify:

### 1. Structural Validity
- [ ] ID format: `{5-digit}_{romaji}[_suffix].json`
- [ ] Filename matches ID exactly
- [ ] Entry is in correct numeric directory

### 2. Headword and Reading
- [ ] Headword has furigana on ALL kanji: `{kanji|reading}`
- [ ] Reading is hiragana only (long vowel marker ー is also allowed)
- [ ] Reading matches the actual pronunciation
- [ ] ID romanization matches reading correctly

### 3. Part of Speech
- [ ] part_of_speech is accurate
- [ ] metadata.tags.pos array matches part_of_speech
- [ ] For verbs: verb_class is correct (godan-u, ichidan, etc.)
- [ ] For verbs: transitivity is specified and accurate

### 4. Gloss
- [ ] Gloss is concise (generally under 60 characters)
- [ ] Gloss captures the primary meaning
- [ ] Multiple meanings separated by commas if needed
- [ ] No redundancy with definitions

### 5. Definitions
- [ ] Each sense is numbered sequentially starting from 1
- [ ] Glosses are distinct (not redundant)
- [ ] Explanations add value beyond the gloss
- [ ] Definitions cover the word's main usages

### 6. Examples
- [ ] At least one example per definition sense
- [ ] Examples use natural, common constructions
- [ ] Japanese text has complete furigana
- [ ] English translations are accurate and natural
- [ ] sense_numbers correctly reference definitions
- [ ] Example IDs follow format: `{entry_id}_ex{N}`

### 7. Notes
- [ ] Notes follow formatting conventions (see vocabulary-notes skill)
- [ ] Information is accurate and helpful for learners
- [ ] No redundancy with other fields
- [ ] Headers are uppercase with colons
- [ ] Appropriate level of detail

### 8. Cross-References
- [ ] All references point to valid entries (or targets are added to candidates)
- [ ] Reference types are appropriate (pair, synonym, antonym, etc.)
- [ ] Labels accurately describe relationships
- [ ] No broken or stale references

**When a cross-reference target does not exist:**
Add the target word to `candidate_words.json`:
```bash
python3 build/manage_candidates.py add "headword" "reading" "brief note"
```
The script automatically checks for duplicates.

### 9. Metadata
- [ ] vocabulary_tier is set appropriately
- [ ] tags.formality is accurate
- [ ] tags.politeness is correct
- [ ] tags.semantic categories are appropriate
- [ ] tags.domain is set if applicable

### 10. Overall Quality
- [ ] Entry is helpful for Japanese learners
- [ ] Information is accurate
- [ ] Consistent with similar entries
- [ ] No typos or grammatical errors

## Recording Changes

For each entry reviewed, record:

```json
{
  "entry_id": "00001_amaru",
  "reviewed": "2026-01-20T12:00:00Z",
  "status": "current",
  "changes_made": [
    "Added missing furigana to example 2",
    "Corrected transitivity tag"
  ],
  "issues_found": [],
  "reviewer_notes": "Good quality entry overall"
}
```

## Updating Tracking Files

After each batch:

1. Update `progress.json`:
   - Add/update entry records
   - Update statistics
   - Add to review_history

2. Update `issues.json`:
   - Add any new issues found
   - Note any patterns observed
   - Add improvement ideas if applicable

3. Update `queue.json`:
   - Remove reviewed entries from queue
   - Add any entries needing follow-up
   - Update current_batch progress

4. Create/update session log in `sessions/`

5. Build static website for review:
   ```bash
   python3 build/build_flat.py
   ```

## Session Summary

At the end of each session, provide a summary including:
- Number of entries reviewed
- Number of entries modified
- Types of changes made
- Issues found requiring attention
- Patterns observed
- Recommendations for next session
