# Multi-Agent New Entry Creation Prompt

Add 50+ new entries to the Japanese-English learner's dictionary from candidate_words.json using parallel subagents. Each subagent runs in its own context window, allowing significantly more entries per batch than the single-agent workflow.

## Architecture Overview

- **Coordinator (you)**: Extracts candidates, assigns IDs, distributes work, runs validation/build
- **Subagents (5+)**: Each independently creates ~10 entries using pre-assigned IDs and candidates
- Each subagent operates within its own context window — they do NOT share context with each other or with you

## Session Workflow

### Phase 1: Preparation (Coordinator)

1. **Read context**: Read `PROJECT_CONTEXT_BRIEF.md` for current counts and critical rules.

2. **Select candidates**: Read `candidate_words.json` and select 50+ candidates to create entries for. Choose a diverse mix of parts of speech. Note the word, reading, and notes/gloss for each.

3. **Batch duplicate check**: Run a batch duplicate check on all selected candidates:
   ```bash
   python3 build/check_duplicate.py --batch --skip-candidates "word1:reading1" "word2:reading2" ...
   ```
   Remove any candidates that come back as DUPLICATE.

4. **Reserve IDs**: Run `python3 build/get_next_id.py` once to get the starting ID. Then assign sequential IDs to each candidate (starting_id, starting_id+1, starting_id+2, ...). Since you are the only agent creating entries in this session and subagents run in parallel, pre-assigning sequential IDs avoids conflicts. **Do not let subagents call `get_next_id.py`** — the coordinator owns all ID assignment.

5. **Get timestamp**: Run `python3 build/get_timestamp.py` once and provide the same timestamp to all subagents for metadata.created and metadata.modified fields.

6. **Compute file paths**: For each entry, compute the file path:
   - `{id_range}` = ID rounded down to nearest 500 (e.g., 16542 → `entries/16500/`)
   - Romaji = reading converted to romaji (e.g., ひきょう → hikyou)
   - Path: `entries/{id_range}/{id}_{romaji}.json`

7. **Read a sample entry**: Read one recent entry file to provide as a structural reference for subagents.

8. **Group assignments**: Divide the candidates into groups of ~10 entries each, one group per subagent. Aim for 5–7 subagents. Try to group candidates by part of speech when possible (all verbs together, all nouns together, etc.) so that each subagent can focus on one entry type's requirements.

### Phase 2: Parallel Entry Creation (Subagents)

Launch all subagents in parallel using the Agent tool. Each subagent receives:

- Its assigned list of candidates with pre-assigned IDs, file paths, and romaji
- The timestamp to use
- A sample entry for structural reference
- The full set of entry creation rules (included in the subagent prompt below)

**Subagent prompt template:**

```
You are creating dictionary entries for a Japanese-English learner's dictionary.
Create each entry as a JSON file using the Write tool.

## Your Assignments

[List each entry with: ID, romaji, file path, word, reading, gloss/notes, part of speech]

## Timestamp

Use this exact timestamp for both metadata.created and metadata.modified:
[timestamp from get_timestamp.py]

## Sample Entry (structural reference)

[Paste a complete sample entry JSON here]

## Entry Creation Rules

For EACH entry, create a JSON file at the specified path with these requirements:

### Structure
- `schema_version`: "2.0"
- `id`: "{numeric_id}_{romaji}" (e.g., "16542_yunomi")
- `headword`: The word with furigana on all kanji: `{漢字|かんじ}`
- `reading`: Hiragana reading (always hiragana, never katakana)
- `part_of_speech`: One of: noun, verb, adjective, い-adjective, な-adjective, adverb, particle, counter, expression, conjunction, prefix, suffix
- `gloss`: Brief English gloss (the short definition)
- `definitions`: Array of sense objects, each with sense_number, gloss, and explanation (in English)
- `examples`: See example requirements below
- `notes`: See notes requirements below
- `cross_references`: Empty array [] for new entries
- `metadata`: See metadata requirements below

### Furigana — CRITICAL
ALL kanji must have furigana in ALL fields — headword, examples, AND notes.
Format: `{漢字|かんじ}` — curly braces, kanji, pipe, reading in hiragana.
This includes kanji in idioms, collocations, and explanatory Japanese text.
Example: `{暖簾|のれん}に{腕押|うでお}し` NOT `暖簾に腕押し`

### All explanations in English
Definitions, notes, etymology, usage explanations, and cultural context must be in English.
Japanese text appears only in example phrases, collocations, and patterns — never as explanatory prose.

### NEVER add inline word links
Do NOT add ⟦...⟧ links — those are added in a separate polishing step.

### Examples — Minimum 3 PER SENSE
- Each sense needs at least 3 examples (2 senses = 6 examples, 3 senses = 9, etc.)
- Examples progress from shorter to longer within each sense:
  1. Short (5-15 chars Japanese) — demonstrates the word clearly
  2. Medium (10-20 chars) — shows basic context
  3. Longer (15-30 chars) — natural usage with fuller context
- Every example must have `sense_numbers` field (e.g., `[1]`)
- Example ID format: `{entry_id}_ex{N}` where N is sequential (ex1, ex2, ex3...)
- `has_audio`: false
- `notes`: null (unless a specific note is needed)
- Include at least one common collocation per sense

### Notes Field
Structure the notes with these sections as appropriate:
- USAGE: (how the word is used, register, context)
- COMMON COLLOCATIONS: (list with format `- {漢字|かんじ}パターン (English gloss)`)
- SIMILAR WORDS: (comparisons with related words, include furigana)
- KANJI: (etymology or character breakdown, if helpful)
- CULTURAL NOTE: (if relevant)
All Japanese text in notes must have furigana on kanji.

### Part-of-Speech-Specific Rules

**Verbs**: Include transitivity ("transitive verb" or "intransitive verb" in gloss or definition). Note aspect/ている behavior if noteworthy. Include common particle patterns in collocations (e.g., ～を{食|た}べる).

**Adjectives**: For い-adjectives, use part_of_speech "い-adjective". For な-adjectives, use "な-adjective". Show common predicate and modifier forms in collocations.

**Nouns**: Note if the noun can function as a する verb (e.g., {勉強|べんきょう}する). Include counter patterns if applicable.

### Metadata
```json
"metadata": {
  "created": "[USE PROVIDED TIMESTAMP]",
  "modified": "[USE PROVIDED TIMESTAMP]",
  "ai_model": "claude-opus-4-6",
  "vocabulary_tier": "general",
  "tags": {
    "pos": ["[part of speech]"],
    "formality": "neutral",
    "politeness": "plain",
    "semantic": ["[1-3 relevant semantic tags]"]
  }
}
```

All entries must have `vocabulary_tier: "general"`.

## Important
- Write each entry file using the Write tool at the EXACT path specified
- Do NOT run any validation scripts — the coordinator will handle that
- Do NOT run get_next_id.py or get_timestamp.py — use the values provided
- Do NOT run check_duplicate.py — the coordinator already checked
- Focus entirely on writing high-quality entry JSON files
```

**Launch subagents**: Use the Agent tool to launch all subagents simultaneously (in a single message with multiple Agent tool calls). Set `mode: "bypassPermissions"` so they can write files without prompts. Give each subagent a descriptive name like `entries-batch-1`, `entries-batch-2`, etc.

### Phase 3: Validation and Build (Coordinator)

After ALL subagents complete:

1. **Verify file creation**: Glob for all newly created entry files and confirm the count matches expectations. Check that filenames follow the `{id}_{romaji}.json` pattern.

2. **Spot-check entries**: Read 2-3 entries from different subagents to verify structural correctness (furigana present, sense_numbers on examples, English-only explanations, no inline links, correct schema_version, etc.).

3. **Run validation**:
   ```bash
   python3 build/validate.py
   ```
   If errors are found, fix them directly (do not relaunch subagents for small fixes).

4. **Check furigana** (restrict to new entries only):
   ```bash
   python3 build/find_missing_furigana.py | head -80
   ```
   Fix any missing furigana in entries from this session.

5. **Update indexes and check kanji**:
   ```bash
   python3 build/update_indexes.py
   python3 build/update_kanji_index.py --check-new
   ```
   If new kanji are found, assign on'yomi, kun'yomi, and gloss before building.

6. **Build the site**:
   ```bash
   python3 build/build_flat.py
   ```

7. **Update PROJECT_STATUS.md** Recent Changes section with entry count and summary.

8. **Commit and push**.

## Critical Rules

- **The coordinator owns all ID assignment** — subagents must never call `get_next_id.py`
- **The coordinator runs all duplicate checks** — subagents must never call `check_duplicate.py`
- **The coordinator runs all validation/build** — subagents only write JSON files
- **NEVER add inline word links (⟦...⟧)** — added in a separate polishing step
- **ALL kanji require furigana** in headwords, examples, AND notes: `{漢字|かんじ}`
- **All explanations must be in English** — Japanese only in example phrases and collocations
- **All examples require sense_numbers** — validation will fail without them
- **All new entries must have `vocabulary_tier: "general"`** — basic and core tiers are fixed
- **Timestamps from get_timestamp.py only** — run once, share with all subagents

## Duplicate Check Details

The coordinator runs batch duplicate checking before distributing work:
```bash
python3 build/check_duplicate.py --batch --skip-candidates "word1:reading1" "word2:reading2" ...
```
Use `--skip-candidates` since candidates are expected to be in candidate_words.json.
Any words that come back as DUPLICATE are removed from the work queue before subagent assignment.

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

If validate.py reports duplicates, use the resolve-duplicates skill to fix them before continuing.

## Scaling Notes

- With 5 subagents at ~10 entries each, expect ~50 entries per batch
- With 7 subagents at ~10 entries each, expect ~70 entries per batch
- Each subagent has its own context window, so the per-entry quality should match single-agent mode
- The coordinator's context is mainly used for preparation and validation, not entry authoring
- If a subagent fails or produces fewer entries than expected, the coordinator can either fix the entries directly or launch a replacement subagent for the remaining work
