# New Entry Creation Prompt

Add 30 new entries to the Japanese-English learner's dictionary from candidate_words.json.

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

3. **After all 30 entries**:
   ```bash
   python3 build/validate.py          # Fix any errors before continuing
   python3 build/find_missing_furigana.py | head -60  # Check for missing furigana in notes
   python3 build/update_indexes.py    # Sync candidate_words.json and check for new kanji
   python3 build/update_kanji_index.py --check-new  # Check for new kanji needing IDs
   python3 build/build_flat.py        # REQUIRED for live site update
   ```

   **If new kanji are found**: New kanji need on'yomi, kun'yomi, and gloss assigned.
   Run the kanji ID assignment process before building.

   **Important**: Restrict the search range of `find_missing_furigana.py` to the entries that you have created in this session. If `find_missing_furigana.py` shows any entries from your session, fix them before committing.

4. **Finish**: Update PROJECT_STATUS.md with entry count and summary, then commit and push

## Critical Rules

- **NEVER add inline word links (⟦...⟧)** - Inline links are added in a separate polishing step using `prompts/polish_add_inline_links.md`. Do NOT add links when creating entries.
- **NEVER create an entry without first running `check_duplicate.py`** - this is the #1 cause of duplicates
- Each entry must be written individually (no automation scripts)
- **ALL kanji require furigana in ALL fields**: headword, examples, AND notes
  - Format: `{漢字|かんじ}`
  - This includes idioms, collocations, and kanji orthography notes
  - Example: `{暖簾|のれん}に{腕押|うでお}し` NOT `暖簾に腕押し`
- **All examples require sense_numbers** - validation will fail without them
- Timestamps must be from get_timestamp.py - the Z suffix is UTC, not JST
- **All new entries must have `vocabulary_tier: "general"`** - basic and core tiers are fixed

## Example Sentence Requirements

**See the `example-sentences` skill for complete guidelines.** Key requirements for new entries:

| Requirement | Standard for General Tier |
|-------------|--------------------------|
| **Minimum count** | **3 examples PER SENSE** (not per entry!) |
| **Progressive length** | Examples get longer from first to last |
| **Vocabulary** | No restrictions (prefer dictionary words) |
| **Collocations** | At least one common collocation per sense |

### ⚠️ CRITICAL: Example Counts Are Per Sense

**The minimum of 3 examples applies to EACH SENSE, not to the entry as a whole.**

| Entry Type | Senses | Minimum Examples Required |
|------------|--------|--------------------------|
| Single-sense | 1 | 3 examples |
| Two-sense | 2 | 6 examples (3 × 2) |
| Three-sense | 3 | 9 examples (3 × 3) |
| Four-sense | 4 | 12 examples (3 × 4) |

**Example:** If creating a verb entry with two senses (e.g., literal and figurative meanings), you must create at least 6 examples total—3 for sense 1 and 3 for sense 2.

### Progressive Length Pattern

Each sense should have examples that progress from shorter to longer:

1. **Example 1**: Short and simple (5-15 chars) - demonstrates the word clearly
2. **Example 2**: Medium length (10-20 chars) - shows basic context
3. **Example 3**: Longer (15-30 chars) - natural usage with fuller context

**For multi-sense entries, apply this progression within EACH sense.** A two-sense entry needs 6 progressively-lengthened examples: ex1-ex3 for sense 1, ex4-ex6 for sense 2.

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

## Example JSON Format

All required fields per the `example-sentences` skill:

```json
"examples": [
  {
    "id": "00001_word_ex1",
    "japanese": "{例文|れいぶん}です。",
    "english": "This is an example sentence.",
    "sense_numbers": [1],
    "has_audio": false,
    "notes": null
  }
]
```

**ID format**: `{entry_id}_ex{N}` where N is sequential (ex1, ex2, ex3...)

## If Duplicates Are Found During Validation

If validate.py reports duplicates, use the resolve-duplicates skill to fix them before continuing.
