# Polish Furigana Completeness

Check dictionary entries one by one for **missing furigana on kanji**. This is a **semantic task** that requires your knowledge of Japanese - it cannot be automated because determining the correct reading for each kanji requires understanding context, compound words, and special readings.

## Task Focus

**Single focus**: Are all kanji in the entry marked with furigana `{kanji|reading}`?

For each entry, check these fields:
- `headword`
- `examples[].japanese`
- `notes`
- `cross_references[].headword`

If any kanji lacks furigana, add the appropriate reading using your knowledge of Japanese.

## Starting Point

```bash
cat polishing/tasks/furigana-completeness/progress.txt
```

Find the first entry file that starts with that number.

## Workflow

1. **Read the progress file** to find the next entry to check

2. **Load the entry** and examine all text fields for kanji without furigana

3. **For each entry**:
   - If all kanji have furigana: Move to the next entry (no changes needed)
   - If missing furigana found: Add the correct readings, update the `modified` timestamp, and save

   **CRITICAL - Timestamp requirement**:
   ```bash
   # Run IMMEDIATELY BEFORE saving each modified entry
   python3 build/get_timestamp.py
   ```

4. **After every ~50 entries** (or when you make changes):
   - Update `polishing/tasks/furigana-completeness/progress.txt` with the next entry number
   - Run validation:
     ```bash
     python3 build/validate.py
     python3 build/update_indexes.py
     python3 build/build_flat.py
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Furigana completeness: check entries XXXXX-XXXXX"
     ```

5. **Check remaining context** using `/context`:
   - **30% or more**: Continue to next batch
   - **Less than 30%**: Perform context reset (step 6)

6. **Context Reset Procedure**:
   a. Update `polishing/tasks/furigana-completeness/progress.txt`
   b. Write session log to `polishing/sessions/furigana-completeness_{date}_{nnn}.md`:
      ```
      ## Session: Furigana Completeness
      Date: YYYY-MM-DD
      Entries checked: XXXXX-XXXXX

      ### Changes Made
      - [entry_id]: Added furigana to [field] - [details]

      ### Next Entry
      XXXXX
      ```
   c. Commit all changes
   d. Use `/compact` to reset context
   e. Re-read this prompt and continue from step 1

## What to Check

### Headword
The headword should have furigana on all kanji:
- Good: `{食|た}べる`
- Bad: `食べる`

### Examples
All kanji in example sentences need furigana:
- Good: `{朝|あさ}ごはんを{食|た}べる。`
- Bad: `朝ごはんを食べる。`

### Notes
The notes field often contains kanji that need furigana:
- Transitivity pairs: `{自動詞|じどうし}`, `{他動詞|たどうし}`
- Related words: `{言葉|ことば}`, `{表現|ひょうげん}`
- Grammar terms: `{連用形|れんようけい}`

### Cross-references
Cross-reference headwords need furigana:
- Good: `"headword": "{余|あま}す"`
- Bad: `"headword": "余す"`

## Why This Cannot Be Automated

Adding furigana requires semantic knowledge:
- **Compound readings**: 今日 can be きょう or こんにち depending on meaning
- **Rendaku**: 人 is usually ひと but にん in compounds
- **Kun vs on readings**: Context determines which reading applies
- **Irregular readings**: 大人(おとな), 明日(あした)
- **Name readings**: Special readings for proper nouns

Only a knowledgeable reader can determine the correct reading in context.

## Common Patterns to Watch

1. **Notes field**: Often has technical terms or related words missing furigana
2. **Longer examples**: More likely to have missed kanji
3. **Compound words**: May need careful attention for readings
4. **Cross-references**: Sometimes added without furigana on the headword

## Progress Update Format

Keep the progress file minimal:
```
next: XXXXX
```

That's all. This allows quick loading into context.

## Output at Session End

When stopping (user request or context reset), report:
1. Entry range checked
2. Number of entries modified
3. Summary of changes made
4. Next entry to continue from
