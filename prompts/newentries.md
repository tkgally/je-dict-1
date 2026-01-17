# New Entry Creation Prompt

Add 25 new entries to the Japanese-English learner's dictionary from candidate_words.json.

## Session Workflow

1. **Start**: Read PROJECT_STATUS.md for current counts and recent patterns

2. **For each entry**:
   - **DUPLICATE CHECK (MANDATORY)**: Before writing ANY entry, run:
     ```bash
     python3 build/check_duplicate.py --skip-candidates "食べる" "たべる"
     ```
     - Use `--skip-candidates` since you're picking FROM candidates (they're expected to be there)
     - This checks only against existing entries, not candidates
     - If it says "OK", proceed with creating the entry
     - If it says "DUPLICATE", SKIP this word - it's already an entry
   - Get timestamp: `python3 build/get_timestamp.py` (CRITICAL - always run this, never guess)
   - Write entry using the appropriate skill (auto-loaded based on part of speech)
   - **Include sense_numbers on all examples**: Every example must have a `sense_numbers` field
     - Single-sense entries: use `[1]` for all examples
     - Multi-sense entries: each example must specify which sense(s) it illustrates
   - Use Write tool to create file at: `entries/{kana_row}/{prefix}/{romaji}_{5digit_id}.json`

3. **After all 25 entries**:
   ```bash
   python3 build/validate.py          # Fix any errors before continuing
   python3 build/find_missing_furigana.py | head -25  # Check for missing furigana in notes
   python3 build/update_indexes.py    # Sync candidate_words.json
   python3 build/build_flat.py        # REQUIRED for live site update
   ```

   **Important**: If `find_missing_furigana.py` shows any entries from your session, fix them before committing.

4. **Finish**: Update PROJECT_STATUS.md with entry count and summary, then commit and push

## Critical Rules

- **NEVER create an entry without first running `check_duplicate.py`** - this is the #1 cause of duplicates
- Each entry must be written individually (no automation scripts)
- **ALL kanji require furigana in ALL fields**: headword, examples, AND notes
  - Format: `{漢字|かんじ}`
  - This includes idioms, collocations, and kanji orthography notes
  - Example: `{暖簾|のれん}に{腕押|うでお}し` NOT `暖簾に腕押し`
- Examples progress simple → complex, include at least one collocation
- **All examples require sense_numbers** - validation will fail without them
- Timestamps must be from get_timestamp.py - the Z suffix is UTC, not JST

## Duplicate Check Details

The `check_duplicate.py` script checks for duplicates before creating entries.

**When creating entries FROM candidates** (this task), use `--skip-candidates`:
```bash
python3 build/check_duplicate.py --skip-candidates "食べる" "たべる"
```
This checks only `entries_index.json` - we know the word is in candidates (that's where we picked it).

**Batch checking** (optional, for planning which candidates to work on):
```bash
python3 build/check_duplicate.py --batch --skip-candidates "食べる:たべる" "飲む:のむ" "書く:かく"
```

**Note**: When adding NEW candidates (not this task), omit `--skip-candidates` to check both entries and existing candidates.

## Example Structure Reminder

```json
"examples": [
  {
    "id": "word_00001_ex1",
    "japanese": "{例文|れいぶん}です。",
    "english": "This is an example sentence.",
    "sense_numbers": [1]
  }
]
```

## If Duplicates Are Found During Validation

If validate.py reports duplicates, use the resolve-duplicates skill to fix them before continuing.
