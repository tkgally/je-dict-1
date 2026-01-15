# New Entry Creation Prompt

Add 50 new entries to the Japanese-English learner's dictionary from candidate_words.json.

## Session Workflow

1. **Start**: Read PROJECT_STATUS.md for current counts and recent patterns

2. **For each entry**:
   - **DUPLICATE CHECK (MANDATORY)**: Before writing ANY entry, search the entries directory:
     ```bash
     grep -r '"reading": "たべる"' entries/
     grep -r '食べる' entries/
     ```
     If either returns results, SKIP this word - it already exists. Move to next candidate.
   - Get timestamp: `python3 build/get_timestamp.py` (CRITICAL - always run this, never guess)
   - Write entry using the appropriate skill (auto-loaded based on part of speech)
   - **Include sense_numbers on all examples**: Every example must have a `sense_numbers` field
     - Single-sense entries: use `[1]` for all examples
     - Multi-sense entries: each example must specify which sense(s) it illustrates
   - Use Write tool to create file at: `entries/{kana_row}/{prefix}/{romaji}_{5digit_id}.json`

3. **After all 50 entries**:
   ```bash
   python3 build/validate.py          # Fix any errors before continuing
   python3 build/update_indexes.py    # Sync candidate_words.json
   python3 build/build_flat.py        # REQUIRED for live site update
   ```

4. **Finish**: Update PROJECT_STATUS.md with entry count and summary, then commit and push

## Critical Rules

- **NEVER create an entry without first searching entries/ for that word** - this is the #1 cause of duplicates
- Each entry must be written individually (no automation scripts)
- All kanji require furigana: `{漢字|かんじ}`
- Examples progress simple → complex, include at least one collocation
- **All examples require sense_numbers** - validation will fail without them
- Timestamps must be from get_timestamp.py - the Z suffix is UTC, not JST

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
