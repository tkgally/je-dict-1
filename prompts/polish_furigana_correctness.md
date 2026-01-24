# Polish Furigana Correctness

Check dictionary entries one by one for **incorrect furigana readings**. This is a **semantic task** that requires your knowledge of Japanese - it cannot be automated because determining whether a reading is correct requires understanding context, compound word rules, and knowing when special or irregular readings apply.

## Task Focus

**Single focus**: Are all existing furigana readings correct?

For each entry, verify readings in:
- `headword`
- `reading` (should match headword furigana)
- `examples[].japanese`
- `notes`
- `cross_references[].headword` and `.reading`

If any reading is incorrect, fix it using your knowledge of Japanese.

## Starting Point

```bash
cat polishing/tasks/furigana-correctness/progress.txt
```

Find the first entry file that starts with that number.

## Workflow

1. **Read the progress file** to find the next entry to check

2. **Load the entry** and verify all furigana readings are correct

3. **For each entry**:
   - If all readings are correct: Move to the next entry (no changes needed)
   - If incorrect readings found: Fix them, update the `modified` timestamp, and save

   **CRITICAL - Timestamp requirement**:
   ```bash
   # Run IMMEDIATELY BEFORE saving each modified entry
   python3 build/get_timestamp.py
   ```

4. **After every ~50 entries** (or when you make changes):
   - Update `polishing/tasks/furigana-correctness/progress.txt` with the next entry number
   - Run validation:
     ```bash
     python3 build/validate.py
     python3 build/update_indexes.py
     python3 build/build_flat.py
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Furigana correctness: check entries XXXXX-XXXXX"
     ```

5. **Check remaining context** using `/context`:
   - **30% or more**: Continue to next batch
   - **Less than 30%**: Perform context reset (step 6)

6. **Context Reset Procedure**:
   a. Update `polishing/tasks/furigana-correctness/progress.txt`
   b. Write session log to `polishing/sessions/furigana-correctness_{date}_{nnn}.md`:
      ```
      ## Session: Furigana Correctness
      Date: YYYY-MM-DD
      Entries checked: XXXXX-XXXXX

      ### Corrections Made
      - [entry_id]: [field] - changed {kanji|wrong} to {kanji|correct}

      ### Next Entry
      XXXXX
      ```
   c. Commit all changes
   d. Use `/compact` to reset context
   e. Re-read this prompt and continue from step 1

## What to Verify

### Common Error Types

1. **Wrong on/kun reading**:
   - Error: `{人|にん}` when standalone (should be `{人|ひと}`)
   - Error: `{日|にち}` for "day" in general (context-dependent)

2. **Missed rendaku**:
   - Error: `{花火|はなひ}` (should be `{花火|はなび}`)
   - Error: `{手紙|てかみ}` (should be `{手紙|てがみ}`)

3. **Wrong compound reading**:
   - Error: `{今日|きょうにち}` for "today" (should be `{今日|きょう}`)
   - Error: `{大人|だいじん}` (should be `{大人|おとな}`)

4. **Irregular readings missed**:
   - Error: `{明日|みょうにち}` for casual "tomorrow" (often `{明日|あした}`)
   - Error: `{昨日|さくじつ}` for casual "yesterday" (often `{昨日|きのう}`)

5. **Reading/headword mismatch**:
   - The `reading` field must match the hiragana rendering of the `headword` furigana

### Fields to Cross-Check

- **headword** vs **reading**: Must match
- **cross_references[].headword** vs **.reading**: Must match
- **examples**: Each kanji should have appropriate contextual reading

## Why This Cannot Be Automated

Verifying furigana correctness requires semantic knowledge:
- **Context-dependent readings**: 生 has many readings depending on word
- **Stylistic choices**: 今日 as きょう vs こんにち depends on tone
- **Historical vs modern**: Some words have alternative readings
- **Domain-specific**: Technical terms may have special readings
- **Recognizing compounds**: Understanding where word boundaries are

Only a knowledgeable reader can verify readings are contextually correct.

## Common Problem Patterns

1. **Systematic errors**: Same kanji misread consistently
2. **Compound confusion**: Wrong reading for multi-kanji words
3. **Copy-paste errors**: Reading from one word applied to another
4. **Over-regularization**: Applying common reading when irregular one is correct
5. **Reading field drift**: `reading` field not updated when headword changed

## Verification Process

For each entry:
1. Read the headword aloud mentally - does the furigana match?
2. Check that `reading` field equals headword with kanji removed
3. Read each example - are the readings natural?
4. Check notes for any technical terms
5. Verify cross-reference readings match their targets

## Progress Update Format

Keep the progress file minimal:
```
next: XXXXX
```

## Output at Session End

When stopping (user request or context reset), report:
1. Entry range checked
2. Number of entries with corrections
3. Summary of correction types
4. Next entry to continue from
