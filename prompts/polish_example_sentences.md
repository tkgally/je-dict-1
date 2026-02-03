# Polish Example Sentences

Check dictionary entries one by one for **example sentence quality**: count, vocabulary level compliance, and appropriateness. While counting examples is mechanical, evaluating vocabulary levels and sentence appropriateness is a **semantic task** that requires your knowledge of Japanese - it cannot be automated.

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

2. **Load the entry** and examine the examples against all requirements

3. **For each entry**:
   - Check example count against tier requirements
   - For basic/core entries, verify vocabulary restrictions
   - Check progressive length (shorter to longer)
   - Evaluate naturalness and usefulness

   If issues found: Fix or add examples, update `modified` timestamp, save

   **CRITICAL - Timestamp requirement**:
   ```bash
   # Run IMMEDIATELY BEFORE saving each modified entry
   python3 build/get_timestamp.py
   ```

4. **After every ~20 entries** (or when you make changes):
   - Update `polishing/tasks/example-sentences/progress.txt`
   - Run validation:
     ```bash
     python3 build/validate.py
     python3 build/update_indexes.py
     python3 build/build_flat.py
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Example sentences: check entries XXXXX-XXXXX"
     ```

5. **Check remaining context** using `/context`:
   - **30% or more**: Continue to next batch
   - **Less than 30%**: Perform context reset (step 6)

6. **Context Reset Procedure**:
   a. Update `polishing/tasks/example-sentences/progress.txt`
   b. Write session log to `polishing/sessions/example-sentences_{date}_{nnn}.md`:
      ```
      ## Session: Example Sentences
      Date: YYYY-MM-DD
      Entries checked: XXXXX-XXXXX

      ### Changes Made
      - [entry_id]: [issue type] - [brief description]

      ### Next Entry
      XXXXX
      ```
   c. Commit all changes
   d. Use `/compact` to reset context
   e. Re-read this prompt and continue from step 1

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

## What Cannot Be Automated

### Vocabulary Level Assessment
- Determining if a word is "basic", "core", or "general" requires knowledge
- Some words aren't in the dictionary - you must judge if appropriate
- Compound expressions need semantic analysis

### Appropriateness Evaluation
- Is this example natural Japanese?
- Does it demonstrate the word's usage clearly?
- Is the context appropriate for learners?
- Does it show important collocations or patterns?

### Writing New Examples
When count is insufficient, you must write new examples that:
- Follow vocabulary restrictions for the tier
- Progress in length appropriately
- Sound natural to native speakers
- Demonstrate the word meaningfully

## Common Issues to Fix

0. **Inline links**: Do NOT add inline word links (⟦...⟧) in this task. Links are added separately via `prompts/polish_add_inline_links.md`.
1. **Insufficient count**: Add examples to meet minimum
2. **Vocabulary violation**: Replace non-compliant words
   - `{購入|こうにゅう}する` → `{買|か}う` (for basic tier)
   - `{使用|しよう}する` → `{使|つか}う`
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

## Progress Update Format

Keep the progress file minimal:
```
next: XXXXX
```

## Output at Session End

When stopping (user request or context reset), report:
1. Entry range checked
2. Number of entries modified
3. Types of issues found and fixed
4. Next entry to continue from
