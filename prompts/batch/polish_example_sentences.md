# Polish Example Sentences — Batch Mode

Check dictionary entries for **example sentence quality**: count, vocabulary level compliance, and appropriateness. Evaluating vocabulary levels and sentence appropriateness is a **semantic task** that requires knowledge of Japanese.

**This prompt is optimized for non-interactive (`claude --print`) execution.**

## Parameters

- `batch_size`: Number of entries to check (default: 10)
- `tier`: Vocabulary tier to focus on (optional — e.g., "basic", "core")

## Task Focus

**Single focus**: Do the example sentences meet all requirements?

For each entry, check:
1. **Count**: Minimum examples per sense (5 for basic/core, 3 for general)
2. **Vocabulary levels**: Tier restrictions for basic and core entries
3. **Appropriateness**: Natural, useful examples with progressive length

Load the skill file for detailed requirements:
```
.claude/skills/example-sentences/SKILL.md
```

## Starting Point

```bash
cat polishing/tasks/example-sentences/progress.txt
```

Find the first entry file that starts with that number.

## Workflow

1. **Read the progress file** to find the next entry to check

2. **Load the entry** and examine examples against all requirements

3. **For each entry**:
   - Check example count against tier requirements
   - For basic/core entries, verify vocabulary restrictions
   - Check progressive length (shorter to longer)
   - Evaluate naturalness and usefulness

   If issues found: Fix or add examples, update `modified` timestamp, save

   **CRITICAL — Timestamp requirement**:
   ```bash
   python3 build/get_timestamp.py
   ```

4. **After processing all entries in the batch**:
   - Update `polishing/tasks/example-sentences/progress.txt`
   - Validate and build:
     ```bash
     make validate
     python3 build/update_indexes.py
     python3 build/build_flat.py --quick
     ```

5. **Commit** (do NOT push — the pipeline handles pushing):
   ```bash
   git add entries/ polishing/
   git commit -m "Example sentences: check entries XXXXX-XXXXX"
   git add docs/
   git commit -m "Rebuild site with example sentence updates"
   ```

6. **Exit cleanly**: After committing, stop. Do not start additional work.

## Requirements Summary

### Minimum Counts by Tier

| Tier | Min Examples per Sense |
|------|------------------------|
| Basic | 5 |
| Core | 5 |
| General | 3 |

### Vocabulary Restrictions

| Tier | Examples 1-2 | Examples 3+ |
|------|--------------|-------------|
| **Basic** | Basic vocab only | Basic + Core only |
| **Core** | Basic + Core only | Any (prefer dictionary words) |
| **General** | Any | Any |

To verify vocabulary tier:
```bash
python3 build/check_duplicate.py "word" "reading"
```

### Progressive Length

| Example | Target Length |
|---------|---------------|
| 1 | 5-15 chars |
| 2 | 10-20 chars |
| 3 | 15-30 chars |
| 4 | 25-45 chars |
| 5+ | 35-70 chars |

## Common Issues to Fix

0. **Inline links**: Do NOT add inline word links (⟦...⟧) in this task
1. **Insufficient count**: Add examples to meet minimum
2. **Vocabulary violation**: Replace non-compliant words
3. **No length progression**: Reorder or rewrite examples
4. **Unnatural expressions**: Rewrite to sound natural
5. **Missing sense coverage**: Ensure all senses have examples

## Example Format Reminder

```json
{
  "id": "00001_word_ex1",
  "japanese": "{漢字|かんじ}の{例文|れいぶん}。",
  "english": "Example sentence with kanji.",
  "sense_numbers": [1],
  "has_audio": false,
  "notes": null
}
```

- IDs: `{entry_id}_ex{N}` format, sequential
- All kanji must have furigana
- `sense_numbers` must reference valid definition senses
