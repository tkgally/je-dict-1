# New Entry Creation — Batch Mode

Add new entries to the Japanese-English learner's dictionary from candidate_words.json.

**This prompt is optimized for non-interactive (`claude --print`) execution.**

## Parameters

- `batch_size`: Number of entries to create (default: 30)
- `tier`: Vocabulary tier filter (ignored — all new entries are general)

## Workflow

1. **Read context**: Read `PROJECT_CONTEXT_BRIEF.md` for current counts and critical rules

2. **For each entry**:
   - **DUPLICATE CHECK (MANDATORY)**: Before writing ANY entry, run:
     ```bash
     python3 build/check_duplicate.py --skip-candidates "word" "reading"
     ```
     - Use `--skip-candidates` since you're picking FROM candidates
     - If it says "DUPLICATE", SKIP this word
   - **Get the next available ID** (run this before EACH entry — do not reuse a previous result):
     ```bash
     python3 build/get_next_id.py
     ```
   - Get timestamp: `python3 build/get_timestamp.py` (CRITICAL — always run this, never guess)
   - Write entry using the appropriate skill (auto-loaded based on part of speech)
   - **Include sense_numbers on all examples**: Every example must have a `sense_numbers` field
   - Use Write tool to create file at: `entries/{id_range}/{id}_{romaji}.json`
     - `{id_range}` is the ID rounded down to nearest 500 (e.g., 10207 → 10000)

3. **After all entries**:
   ```bash
   make validate                              # Fix any errors before continuing
   python3 build/find_missing_furigana.py | head -60  # Check furigana in notes
   python3 build/update_indexes.py            # Sync candidate_words.json
   python3 build/update_kanji_index.py --check-new  # Check for new kanji
   python3 build/build_flat.py --quick        # Rebuild only changed entries
   ```

   **If new kanji are found**: Assign on'yomi, kun'yomi, and gloss before building.

   **Important**: If `find_missing_furigana.py` shows entries from this session, fix them before committing.

4. **Commit** (do NOT push — the pipeline handles pushing):
   ```bash
   git add entries/ entries_index.json candidate_words.json kanji/
   git commit -m "Add N new entries from candidates"
   git add docs/
   git commit -m "Rebuild site with new entries"
   ```

5. **Exit cleanly**: After committing, stop. Do not start additional work.

## Critical Rules

- **NEVER add inline word links (⟦...⟧)** — links are added in a separate polishing step
- **NEVER create an entry without first running `check_duplicate.py`**
- **ALL kanji require furigana in ALL fields**: headword, examples, AND notes
  - Format: `{漢字|かんじ}`
- **All examples require sense_numbers** — validation will fail without them
- Timestamps must be from `get_timestamp.py` — the Z suffix is UTC, not JST
- **All new entries must have `vocabulary_tier: "general"`** — basic and core tiers are fixed
- Each entry must be written individually (no automation scripts)

## Example Sentence Requirements

| Requirement | Standard for General Tier |
|-------------|--------------------------|
| **Minimum count** | **3 examples PER SENSE** (not per entry!) |
| **Progressive length** | Examples get longer from first to last |
| **Vocabulary** | No restrictions (prefer dictionary words) |
| **Collocations** | At least one common collocation per sense |

### Per-Sense Minimums

| Senses | Minimum Examples Required |
|--------|--------------------------|
| 1 | 3 examples |
| 2 | 6 examples (3 x 2) |
| 3 | 9 examples (3 x 3) |
| 4 | 12 examples (3 x 4) |

### Progressive Length Pattern

1. **Example 1**: Short and simple (5-15 chars)
2. **Example 2**: Medium length (10-20 chars)
3. **Example 3**: Longer (15-30 chars)

## Duplicate Check Details

**When creating entries FROM candidates** (this task), use `--skip-candidates`:
```bash
python3 build/check_duplicate.py --skip-candidates "食べる" "たべる"
```

**Batch checking** (optional, for planning):
```bash
python3 build/check_duplicate.py --batch --skip-candidates "食べる:たべる" "飲む:のむ"
```

## Example JSON Format

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

If validate.py reports duplicates, use the resolve-duplicates skill to fix them before committing.
