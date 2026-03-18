# Multi-Agent New Entry Creation Prompt

Add 50+ new entries to the Japanese-English learner's dictionary from candidate_words.json using parallel subagents. Each subagent runs in its own context window, allowing significantly more entries per batch than the single-agent workflow.

## Architecture Overview

- **Coordinator (you)**: Extracts candidates, assigns IDs, reads skill files, distributes work, runs validation/build
- **Subagents (5+)**: Each independently creates ~10 entries using pre-assigned IDs and candidates
- Each subagent operates within its own context window — they do NOT share context with each other or with you
- **Subagents cannot load skills.** The coordinator must read the relevant skill files and include their full text in each subagent's prompt. This is critical for entry quality.

## Session Workflow

### Phase 1: Preparation (Coordinator)

1. **Read context**: Read `PROJECT_CONTEXT_BRIEF.md` for current counts and critical rules.

2. **Select candidates**: Read `candidate_words.json` and select 50+ candidates to create entries for. Choose a diverse mix of parts of speech. Note the word, reading, notes/gloss, and likely part of speech for each.

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

7. **Read sample entries**: Read 2–3 recent entry files of different types (a verb, a noun, an adjective) to provide as structural references for subagents.

8. **Read skill files**: Read the following skill files so you can include their full text in subagent prompts:
   - `.claude/skills/entry-guidelines/SKILL.md` — general quality standards (include in ALL subagent prompts)
   - `.claude/skills/example-sentences/SKILL.md` — example sentence requirements (include in ALL subagent prompts)
   - `.claude/skills/vocabulary-notes/SKILL.md` — notes field formatting (include in ALL subagent prompts)
   - `.claude/skills/verb-entry/SKILL.md` — verb-specific requirements (include for verb subagents)
   - `.claude/skills/adjective-entry/SKILL.md` — adjective-specific requirements (include for adjective subagents)
   - `.claude/skills/other-entries/SKILL.md` — noun/counter/adverb/expression requirements (include for those subagents)
   - `.claude/skills/particle-entry/SKILL.md` — particle-specific requirements (include for particle subagents, if any)

9. **Group assignments by part of speech**: Divide the candidates into groups of ~10 entries each, one group per subagent. Aim for 5–7 subagents. **Group by part of speech** so that each subagent only needs the skills relevant to its entry type:
   - Verb group(s): gets verb-entry skill + general skills
   - Adjective group(s): gets adjective-entry skill + general skills
   - Noun/adverb/expression group(s): gets other-entries skill + general skills
   - Particle group (if any): gets particle-entry skill + general skills

   This keeps each subagent's prompt focused and avoids wasting context on irrelevant skills.

### Phase 2: Parallel Entry Creation (Subagents)

Launch all subagents in parallel using the Agent tool. Set `mode: "bypassPermissions"` so they can write files without prompts. Give each subagent a descriptive name like `entries-verbs-1`, `entries-nouns-1`, etc.

**Each subagent prompt must include ALL of the following sections:**

#### Section 1: Task Description and Assignments

```
You are creating dictionary entries for a Japanese-English learner's dictionary.
Create each entry as a JSON file using the Write tool.

## Your Assignments

[List each entry with: ID, romaji, file path, word, reading, gloss/notes, part of speech]

## Timestamp

Use this exact timestamp for both metadata.created and metadata.modified:
[timestamp from get_timestamp.py]
```

#### Section 2: Sample Entries

Include 1–2 complete sample entry JSON files that match the part of speech this subagent is creating. For example, give verb subagents a sample verb entry, noun subagents a sample noun entry.

```
## Sample Entry (structural reference)

[Paste complete sample entry JSON here — choose one matching this subagent's part of speech]
```

#### Section 3: Full Skill Text — General Skills (ALL subagents)

Include the **complete, unabridged text** of these three skill files in every subagent prompt. Do not summarize — paste the full content:

1. **entry-guidelines** (from `.claude/skills/entry-guidelines/SKILL.md`)
   - Covers: file placement, furigana requirements, reading format, metadata tags (pos values, formality, politeness, semantic categories, transitivity), vocabulary tier policy, timestamps, duplicate definitions, quality checklist

2. **example-sentences** (from `.claude/skills/example-sentences/SKILL.md`)
   - Covers: minimum counts per sense per tier, progressive length requirements, vocabulary restrictions, sense_numbers rules, quality standards, example format reference

3. **vocabulary-notes** (from `.claude/skills/vocabulary-notes/SKILL.md`)
   - Covers: section headers, line breaks between sections, bullet points for lists, newlines in JSON, furigana in notes, structure templates

**Why full text is required:** These skills contain specific tag values (e.g., valid `pos` tags like `verb-godan`, `verb-ichidan`, `adjective-i`, `adjective-na`), formatting rules (e.g., `\n\n` between sections in JSON notes), and quality checklists that cannot be adequately conveyed in a summary. Subagents cannot load skills themselves, so this is their only source of these requirements.

#### Section 4: Full Skill Text — Part-of-Speech Skill (per subagent type)

Include the **complete, unabridged text** of the relevant POS skill:

| Subagent type | Skill to include |
|---------------|------------------|
| Verbs | `verb-entry` — transitivity (自動詞/他動詞), pair verbs, aspect/ている behavior, particle patterns, collocations, verb-specific tags (`verb-godan`/`verb-ichidan`/`verb-suru`/etc., `transitivity` tag) |
| Adjectives | `adjective-entry` — い-adjective vs な-adjective, forms, conjugations, predicate vs modifier usage, similar words, adjective-specific tags (`adjective-i`/`adjective-na`/etc.) |
| Nouns, counters, adverbs, expressions | `other-entries` — noun collocations, scope clarification, counter counting patterns (1–10), adverb position/modification, expression situational context and response pairs, type-specific tags |
| Particles | `particle-entry` — predicate lists, particle contrasts, fixed patterns, information structure |

#### Section 5: Operational Instructions

Include these instructions at the end of every subagent prompt:

```
## Operational Instructions

- Write each entry file using the Write tool at the EXACT path specified in your assignments
- Do NOT run any validation scripts — the coordinator will handle that
- Do NOT run get_next_id.py or get_timestamp.py — use the values provided above
- Do NOT run check_duplicate.py — the coordinator already checked all assignments
- Do NOT add inline word links (⟦...⟧) — those are added in a separate polishing step
- Focus entirely on writing high-quality entry JSON files
- Apply the skill guidelines carefully — they define the quality standard for this dictionary
- All explanations must be in English — Japanese text appears only in example phrases, collocations, and patterns
- All kanji must have furigana in ALL fields (headword, examples, AND notes): {漢字|かんじ}
- All readings must be hiragana, never katakana (even for katakana loanwords)
- All examples must have sense_numbers
- All entries must have vocabulary_tier: "general"
- Use schema_version: "2.0"
```

### Phase 3: Validation and Build (Coordinator)

After ALL subagents complete:

1. **Verify file creation**: Glob for all newly created entry files and confirm the count matches expectations. Check that filenames follow the `{id}_{romaji}.json` pattern.

2. **Spot-check entries**: Read 2–3 entries from different subagents to verify:
   - Furigana on all kanji (in headword, examples, AND notes)
   - sense_numbers on all examples
   - English-only explanations (no Japanese prose)
   - No inline word links (⟦...⟧)
   - Correct schema_version ("2.0")
   - Correct vocabulary_tier ("general")
   - Proper metadata tags (correct pos values like `verb-godan` not just `verb`, transitivity tag on verbs, etc.)
   - Notes field properly formatted (section headers, bullet points, `\n\n` between sections)
   - Verb entries have transitivity, aspect, particle patterns
   - Adjective entries specify い-adjective vs な-adjective correctly

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
- **Subagents cannot load skills** — the coordinator must read skill files and paste their full text into subagent prompts
- **NEVER add inline word links (⟦...⟧)** — added in a separate polishing step
- **ALL kanji require furigana** in headwords, examples, AND notes: `{漢字|かんじ}`
- **All explanations must be in English** — Japanese only in example phrases and collocations
- **All examples require sense_numbers** — validation will fail without them
- **All new entries must have `vocabulary_tier: "general"`** — basic and core tiers are fixed
- **Timestamps from get_timestamp.py only** — run once, share with all subagents
- **Include full skill text in subagent prompts** — do not summarize or abbreviate skills

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
- Grouping by part of speech keeps subagent prompts focused: each subagent only needs 3 general skills + 1 POS-specific skill, rather than all skills
- If a subagent fails or produces fewer entries than expected, the coordinator can either fix the entries directly or launch a replacement subagent for the remaining work

## Context Budget Considerations

Each subagent's prompt will be substantial due to the included skill text. Approximate sizes:
- General skills (entry-guidelines + example-sentences + vocabulary-notes): ~700 lines
- POS-specific skill (verb-entry, adjective-entry, etc.): ~150–200 lines
- Sample entry: ~80 lines
- Assignments + operational instructions: ~50 lines
- **Total per subagent: ~1,000 lines of prompt**

This leaves ample context for the subagent to write ~10 high-quality entries. If you find subagents are running low on context, reduce the batch size per subagent to ~7–8 entries and increase the number of subagents.
