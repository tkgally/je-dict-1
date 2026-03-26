# New Entry Creation Prompt

Add new entries to the Japanese-English learner's dictionary from candidate_words.json.

## Session Workflow

1. **Start**: Read PROJECT_CONTEXT_BRIEF.md for current counts and critical rules

2. **For each entry**:
   - **DUPLICATE CHECK (MANDATORY)**: Before writing ANY entry, run:
     ```bash
     python3 build/check_duplicate.py --skip-candidates "食べる" "たべる"
     ```
     - Use `--skip-candidates` since you're picking FROM candidates (they're expected to be there)
     - This checks only against existing entries, not candidates
     - If it says "OK", proceed with creating the entry
     - If it says "DUPLICATE", SKIP this word - it's already an entry
   - **Get the next available ID** (run this before EACH entry — do not reuse a previous result):
     ```bash
     python3 build/get_next_id.py
     ```
   - Get timestamp: `python3 build/get_timestamp.py` (CRITICAL - always run this, never guess)
   - Write entry using the appropriate skill (auto-loaded based on part of speech)
   - **Include sense_numbers on all examples**: Every example must have a `sense_numbers` field
     - Single-sense entries: use `[1]` for all examples
     - Multi-sense entries: each example must specify which sense(s) it illustrates
   - Use Write tool to create file at: `entries/{id_range}/{id}_{romaji}.json`
     - `{id_range}` is the ID rounded down to nearest 500 (e.g., 10207 → 10000)
     - `{id}_{romaji}` is the entry ID (e.g., 10207_asari)

3. **After all entries**:
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

4. **Finish**: Update PROJECT_STATUS.md Recent Changes section with entry count and summary, then commit and push

## Critical Rules

- **NEVER add inline word links (⟦...⟧)** - Inline links are added in a separate polishing step using `prompts/polish_add_inline_links.md`. Do NOT add links when creating entries.
- **NEVER create an entry without first running `check_duplicate.py`** - this is the #1 cause of duplicates
- Each entry must be written individually (no automation scripts)
- **All explanations must be in English** - Definitions, notes, etymology, usage explanations, and cultural context must be in English. Japanese text appears only in example phrases, collocations, and patterns — never as explanatory prose. This is a bilingual dictionary for English-speaking learners.
- **ALL kanji require furigana in ALL fields**: headword, examples, AND notes
  - Format: `{漢字|かんじ}`
  - This includes idioms, collocations, and kanji orthography notes
  - Example: `{暖簾|のれん}に{腕押|うでお}し` NOT `暖簾に腕押し`
- **All examples require sense_numbers** - validation will fail without them
- Timestamps must be from get_timestamp.py - the Z suffix is UTC, not JST
- **All new entries must have `vocabulary_tier: "general"`** - basic and core tiers are fixed

## Notes Field Requirements

**See the `vocabulary-notes` skill for complete guidelines.** The notes field is a critical part of each entry. Short, unstructured notes are a common quality problem — follow these requirements carefully:

### Structure and Formatting (MANDATORY)

| Requirement | Standard |
|-------------|----------|
| **Section headers** | Use labeled headers (USAGE:, COMMON COLLOCATIONS:, SIMILAR WORDS:, TRANSITIVITY:, ASPECT:, etc.) for distinct categories of information |
| **Paragraph breaks** | Separate sections with blank lines (`\n\n` in JSON) — never pack multiple topics into one paragraph |
| **Bullet points** | Any list of 2+ items MUST use `- ` bullet points, not inline comma-separated lists |
| **Language** | All explanatory prose in English; Japanese only in example phrases and collocations |
| **Furigana** | All kanji in notes must have furigana: `{漢字|かんじ}` |

### Minimum Content

Every entry's notes should include at least:

1. **Core semantic explanation** — what the word fundamentally means beyond the gloss (1-2 sentences)
2. **Collocations or common expressions** — as a bulleted list with translations
3. **At least one additional section** from: similar word distinctions, register notes, cultural context, common mistakes, etymology, related terms

### Format Example (in JSON)

```json
"notes": "Core explanation of the word.\n\nCOMMON COLLOCATIONS:\n- {例|れい}one: translation\n- {例|れい}two: translation\n\nSIMILAR WORDS:\n- word1: gloss — how it differs\n- word2: gloss — how it differs"
```

### Anti-Patterns to Avoid

These patterns indicate the notes field is too short or poorly structured:

```
✗ BAD: "Composed of X + Y. Common collocations: A, B, C. Related: D."
  (Single paragraph, no headers, inline list instead of bullets)

✓ GOOD: "Composed of X + Y.\n\nCOMMON COLLOCATIONS:\n- A: translation\n- B: translation\n- C: translation\n\nRELATED TERMS:\n- D: gloss — explanation"
  (Separated sections, headers, bullet points)
```

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

### Removing Stale Candidates

When the duplicate check reveals that a candidate is effectively a duplicate of an existing entry — whether an exact match, a variant reading of the same word (e.g., だったんそ vs だつたんそ for 脱炭素), or a spelling variant (e.g., ふぉーく vs ふおーく for フォーク) — **remove it from candidate_words.json** directly. Use a script like:

```python
python3 -c "
import json
with open('candidate_words.json') as f:
    data = json.load(f)
remove_ids = {'C12345', 'C12346'}  # IDs of stale candidates
data['candidates'] = [c for c in data['candidates'] if c['id'] not in remove_ids]
data['metadata']['total_candidates'] = len(data['candidates'])
with open('candidate_words.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')
"
```

These stale candidates waste time in future sessions if left in the list. Remove them as you encounter them during the batch duplicate check phase, before you start creating entries. Common causes of stale candidates:
- Variant readings (やぎょうせい vs やこうせい)
- Typos in readings (どうふゅう instead of どうふう)
- Alternative romanizations of the same sound (ふぉーく vs ふおーく)
- Candidates with する that match existing entries without する

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

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow." The key points:

1. **Run `make build` BEFORE the final commit** so that `docs/` and all build artifacts are included
2. **`git add -A`** to stage everything (entries, docs, indexes, kanji, session logs, etc.)
3. **Commit and push** to the feature branch
4. **Create a PR** for the branch
5. **Poll CI status** every 60 seconds until all checks pass (allow up to 10 minutes)
6. **Squash-merge the PR** once all checks are green
7. **If CI fails**: read the error, fix the issue, push again, and repeat from step 5
8. **Post-merge cleanup**: switch to main, pull, verify clean state, delete feature branch locally and remotely

**CRITICAL**: The PR must include rebuilt `docs/` files. If you commit entry changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.

## If Duplicates Are Found During Validation

If validate.py reports duplicates, use the resolve-duplicates skill to fix them before continuing.
