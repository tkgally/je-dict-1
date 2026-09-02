---
name: entry-guidelines
description: General quality standards for all je-dict-1 dictionary entries. Use when creating or revising any entry type.
---

# Dictionary Entry Quality Guidelines

When creating or revising dictionary entries for je-dict-1, follow these quality standards:

## CRITICAL: Write Each Entry Individually

**DO NOT use Python scripts or automation to mass-produce entries.**

Each dictionary entry must be written individually by hand, using:
- Your own linguistic knowledge
- The guidelines in this skill and related skills (`verb-entry`, `adjective-entry`, `particle-entry`, `other-entries`, `vocabulary-notes`)
- Careful consideration of each word's unique characteristics

**Why this matters:**
- Each word has nuances that require individual attention
- Examples must be natural and contextually appropriate
- Notes should address learner-specific challenges for that word
- Mass-produced entries lack the quality and depth learners need

**The correct workflow:**
1. Select a word from `candidate_words.json` or user request
2. Research/consider the word's usage, collocations, and common patterns
3. Write the entry JSON directly using the Write tool
4. Validate: `python3 build/validate.py`
5. Repeat for each entry

**After finishing all entries for a session:**
```bash
python3 build/validate.py                    # Validate all entries
python3 build/add_conjugations.py            # Add conjugation to any new verbs
python3 build/add_adjective_conjugations.py  # Add conjugation to any new i-adjectives
python3 build/update_indexes.py              # Update indexes and sync candidates
make index                                   # Refresh indexes and kanji JSON (the site builds in CI after merge)
git add entries/ docs/ *.json PROJECT_STATUS.md
git commit -m "Add N new dictionary entries"
git push
```
**Recent Changes rotation:** PROJECT_STATUS.md keeps only the 5 most recent change entries. When adding a new entry to the "Recent Changes" section, move the oldest one to PROJECT_STATUS-archive.md.
The `make index` step refreshes `entries_index.json`, `build/word_id_lookup.json`, and `kanji/`; the live site is rebuilt by GitHub Actions when the PR merges, so `docs/` is never committed.

**Never create scripts that generate entry content programmatically.**

## Before Creating a New Entry

**IMPORTANT**: Always check if an entry already exists before creating a new one.

### Duplicate Definition

**A word is a duplicate ONLY if BOTH the headword AND reading match exactly.**

- **Homophones** (same reading, different headword) are **NOT duplicates** and should have separate entries
  - Example: 線香 (せんこう) and 先行 (せんこう) are different words
  - Example: 橋/箸/端 (all はし) are different words
- **Homographs** (same headword, different reading) are **NOT duplicates** and should have separate entries
  - Example: 行く (いく) and 行く (ゆく) are different readings
  - Example: 明日 (あした) and 明日 (あす) are different readings

### Duplicate Check Process

1. **Run the duplicate check script**:
   ```bash
   python3 build/check_duplicate.py "食べる" "たべる"
   ```

   - If it says "OK: ... is not in the dictionary or candidates" → Safe to create entry
   - If it says "DUPLICATE: ..." → SKIP this word, do NOT create a duplicate
   - **Informational notes** about homophones/homographs do NOT block entry creation — **BUT** you must evaluate them (see step 2)

2. **If homophones are reported, check for spelling variants**:
   The script reports entries with the same reading but different headwords. Most are genuine homophones (different words), but some may be **spelling variants of the same word** (e.g., a kana-only form alongside a kanji form). Before creating the entry, verify:
   - Does an existing entry with the same reading cover the same meaning?
   - Is the new headword just a different way to write the same word (kana vs kanji, alternative kanji)?
   - If YES: do NOT create a new entry. Instead, consider updating the existing entry's notes to mention the alternative spelling.
   - If NO (genuinely different word): proceed with entry creation.

   See the `consolidate-entries` skill for the full decision framework.

3. **Batch checking** (optional, to plan which candidates to work on):
   ```bash
   python3 build/check_duplicate.py --batch "食べる:たべる" "飲む:のむ" "書く:かく"
   ```

4. **If the word was in candidate_words.json**: It will be automatically removed when you run `python3 build/update_indexes.py` after creating the entry.

5. **Only create new entries** for words that pass the duplicate check AND the variant check.

This prevents duplicate entries and wasted effort on entries that must later be deleted or merged.

## Verb Conjugation (REQUIRED for all verb entries)

All verb entries must include a `conjugation` field with the full set of conjugated forms hard-coded in the JSON. See the `verb-conjugations` skill for the complete specification.

After creating verb entries, run `python3 build/add_conjugations.py` to automatically generate and write the conjugation data. Or include the full conjugation field directly when writing the entry JSON.

## I-Adjective Conjugation (REQUIRED for all i-adjective entries)

All i-adjective entries must include a `conjugation` field with 6 conjugated forms (Present, Past, て form, Adverbial, Conditional ば, Conditional たら). See the `verb-conjugations` skill for the JSON structure (same format, `type` is `"i-adjective"` or `"ii"` for いい compounds).

After creating i-adjective entries, run `python3 build/add_adjective_conjugations.py` to automatically generate and write the conjugation data. Or include the full conjugation field directly when writing the entry JSON.

**Na-adjectives do NOT have a `conjugation` field.** Their conjugation is shown in the notes field instead.

## Content Guidelines

1. **Explain before exemplifying** - Definition first, then examples
2. **One meaning = one example minimum** - Every sense needs illustration
3. **Show grammatical connections** - Always demonstrate how words connect
4. **Prefer natural Japanese** - Avoid textbook stiffness
5. **Highlight non-obvious distinctions** - Focus on what learners cannot infer from English
6. **All explanations in English** - Definitions, explanations, usage notes, etymology, and cultural context must be written in English. Japanese text should only appear in example phrases, collocations, patterns, and headwords — never as explanatory prose. This is a bilingual learner's dictionary, not a monolingual one.
7. **Concise, not maximally thorough** - Each field has a job. `gloss` is for scanning (≤8 words, semicolons), `definitions[i].explanation` carries the longer description (~150–400 chars), `notes` adds usage and collocations in 2–3 focused sections. Per-field length budgets live in `prompts/newentries.md` under "Length targets" — defer to those numbers. Bloated entries (long parenthetical glosses, six-section notes, redundant "COMMON COMPOUNDS" + "COMMON COLLOCATIONS" pairs) are a quality regression, not a quality improvement.

## Consistency Guidelines

1. **Consistent depth across similar entries** - Match the shape of recent reference entries (e.g. `entries/27000/27261_motenashi.json`, `entries/27000/27364_komentarii.json`); don't over-explain one verb while under-explaining another, and don't introduce a much denser style than neighboring entries
2. **Consistent structure within entry types** - All verbs should use the same section headers, but a section is only included when it has something to say
3. **Consistent terminology** - Use same labels throughout (USAGE NOTES, not sometimes Notes)

## Example Sentence Guidelines

**See the `example-sentences` skill for complete guidelines on:**
- Minimum example counts per tier (5 for basic/core, 3 for general)
- Progressive length requirements
- Vocabulary restrictions by tier
- Quality standards and formatting

### Key Requirements Summary

1. **Minimum counts**: Basic/core tiers need 5 examples per sense; general tier needs 3
2. **Progressive length**: Examples should get longer from first to last
3. **Vocabulary restrictions**: Basic tier examples must use tier-appropriate vocabulary
4. **Always include sense_numbers**: Every example must specify which definition sense(s) it illustrates

### Sense Numbers Requirement

Every example sentence **must** have a `sense_numbers` field that links it to the definition(s) it illustrates:

```json
"examples": [
  {
    "id": "00001_word_ex1",
    "japanese": "...",
    "english": "...",
    "sense_numbers": [1]
  }
]
```

**Rules:**
- **Single-sense entries**: Use `[1]` for all examples
- **Multi-sense entries**: Each example must specify which sense(s) it demonstrates
- **Examples illustrating multiple senses**: Use `[1, 2]` format
- **Must reference valid senses**: Numbers must match `sense_number` values in definitions

The validation script checks that all examples in multi-sense entries have valid sense_numbers.

## Furigana Requirements (CRITICAL)

**All kanji MUST have furigana in ALL fields, including notes.**

Format: `{漢字|かんじ}`

This applies to:
- Headwords
- Example sentences
- **Notes field** (idioms, collocations, cultural notes, etc.)
- All explanatory text

**Common mistakes to avoid:**
```
✗ WRONG: 暖簾に腕押し
✓ RIGHT: {暖簾|のれん}に{腕押|うでお}し

✗ WRONG: 安堵の息をつく
✓ RIGHT: {安堵|あんど}の{息|いき}をつく

✗ WRONG: Sometimes written as 家鴨
✓ RIGHT: Sometimes written as {家鴨|あひる}
```

Use compound readings for jukugo: `{友達|ともだち}` not `{友|とも}{達|だち}`

**Verify before finalizing:**
```bash
python3 build/verify_furigana.py <entry_id>
```

## Entry Structure

Every entry must include:
- `id`: Format `{5-digit-number}_{romaji}` (e.g., `00396_taberu`). See **Romaji/ID Format** below for critical rules.
- `headword`: With furigana notation
- `reading`: **Hiragana only** (see Reading Format below)
- `romaji`: Must match the full reading, concatenated without internal underscores
- `part_of_speech`: Consistent terminology
- `gloss`: Brief English equivalent — 3–8 words, semicolon-separated. **Not a definition.** No parenthetical mini-definitions, etymology, numbered clauses, or sentences. The longer description belongs in `definitions[i].explanation`.
  - **Negative-polarity items** (words or senses used only with negatives — めったに, ちっとも, 必ずしも, しか, the way/method sense of 仕様, etc.): append the marker `(with negative)` to the gloss, and render the English with `(not) …` where that reads naturally — e.g. `rarely, seldom (with negative)`, `(not) properly; (not) satisfactorily (with negative)`, `(no) way, means (with negative)`. If only one sense is negative-only, mark that sense's gloss (and the corresponding part of the top-level gloss), and say so in the explanation.
- `definitions`: Array with sense_number, gloss (3–10 words), and explanation (1–3 sentences, ~150–400 chars)
- `examples`: Meet the per-sense minimum from the `example-sentences` skill (3 for general tier, 5 for basic/core). Exceeding the minimum by 0–1 is fine; exceeding by more is rarely warranted.
- `notes`: Usage notes, grammar patterns, common mistakes (see `vocabulary-notes` skill for formatting requirements and length budgets)
- `schema_version`: Set to `"2.0"` for all new entries (top-level field, optional for existing entries)
- `metadata`: Including vocabulary_tier (**always "general" for new entries**), created, modified timestamps

## Reading Format (CRITICAL)

**All readings MUST be in hiragana, never katakana.**

This applies to ALL entries, including:
- Loanwords (katakana headwords like スキー, ストレージ)
- Abbreviations (DM, PC, etc.)
- Any word regardless of how the headword is written

**Examples:**
```
✓ CORRECT:
  headword: "スキー"
  reading: "すきー"

✓ CORRECT:
  headword: "DM"
  reading: "でぃーえむ"

✗ WRONG:
  headword: "スキー"
  reading: "スキー"  ← Katakana readings cause duplicates!
```

**Why this matters:**
- Katakana readings cause duplicate entries (same word with two different reading formats)
- The dictionary uses readings for indexing and deduplication
- Consistent hiragana readings ensure proper sorting and lookup

**Note:** The long vowel mark `ー` is acceptable in hiragana readings (e.g., `すきー`, `すとれーじ`) since there is no hiragana equivalent.

The validation script (`validate.py`) will report errors for entries with katakana readings.

## Romaji/ID Format (CRITICAL)

The entry ID and `romaji` field must follow this format. The schema regex is: `^[0-9]{5}_[a-z]+(_[a-z]+)?$`

**Rules:**
1. **Concatenate the full reading** into the romaji — do NOT split at word boundaries with underscores
2. At most **one underscore** after the 5-digit number (i.e., at most two lowercase segments)
3. The romaji **must match the full reading** — the validator checks this

**Correct examples:**
- `21022_ketteisuru` ← 決定する (けっていする) — suru concatenated
- `06899_kaowodasu` ← 顔を出す (かおをだす) — particles concatenated
- `21019_shitekina` ← 私的な (してきな) — na concatenated
- `21409_moushiwakearimasen` ← 申し訳ありません (もうしわけありません)

**Wrong examples:**
- `21391_kasoku_suru` ← splits "suru" as a second segment (use `kasokusuru`)
- `21399_koe_wo_dasu` ← three segments after the number (use `koewodasu`)
- `21410_fushizen_na` ← splits "na" as a second segment (use `fushizenna`)

## File Placement (CRITICAL)

**Entries MUST be placed in the correct numeric range directory.**

The path follows this pattern: `entries/{range}/{entry_id}.json`

The **range directory** is determined by the numeric portion of the entry ID, rounded down to the nearest 500:
- IDs 00000-00499 → `entries/00000/`
- IDs 00500-00999 → `entries/00500/`
- IDs 01000-01499 → `entries/01000/`
- etc.

### Examples

- Entry `00396_taberu` → `entries/00000/00396_taberu.json`
- Entry `00538_aruku` → `entries/00500/00538_aruku.json`
- Entry `01186_mukau` → `entries/01000/01186_mukau.json`
- Entry `06237_fumikiru` → `entries/06000/06237_fumikiru.json`

### How to Get the Correct Path

**ALWAYS run this command** to determine the correct path before writing:

```bash
python3 build/get_entry_path.py <reading> <entry_id>
```

Example:
```bash
python3 build/get_entry_path.py ふみきる 06237_fumikiru
# Output: entries/06000/06237_fumikiru.json

python3 build/get_entry_path.py こうりつてき 06240_kouritsuteki
# Output: entries/06000/06240_kouritsuteki.json
```

The `validate.py` script checks for directory mismatches and will report errors.

## Metadata Timestamps

**CRITICAL**: Timestamps MUST be actual current UTC time. The website converts UTC to JST (+9 hours) for display. Incorrect timestamps will show as wrong dates/times (often appearing hours or days in the future).

### How to Get the Correct Timestamp

**ALWAYS run this command** to get the current UTC timestamp before writing each entry:

```bash
python3 build/get_timestamp.py
```

This outputs the current UTC time, e.g.: `2026-01-12T10:45:30Z`

Copy this exact output into both `created` and `modified` fields (for new entries) or just `modified` (for revisions).

### Why This Matters

- The `Z` suffix means UTC (not local time, not JST)
- The build script adds 9 hours to convert to JST for display
- If you write `16:00:00Z` when actual UTC is `10:00`, it displays as **01:00 JST next day** (wrong!)
- If you write `10:00:00Z` when actual UTC is `10:00`, it displays as **19:00 JST same day** (correct!)

### Common Mistakes to Avoid

1. **DO NOT** guess or estimate the timestamp
2. **DO NOT** use your perception of current time - always run the script
3. **DO NOT** use round hours like `12:00:00Z` or `15:00:00Z` (these are almost certainly wrong)
4. **DO NOT** copy timestamps from other entries
5. **DO NOT** write JST time with a Z suffix (this causes 9-hour errors)

### Validation

Run `python3 build/validate.py` to check for:
- Future timestamps (timestamp more than 24 hours ahead of current UTC time)
- Suspiciously round timestamps (exactly `:00:00` seconds, likely not from the script)

Note: The validator allows a 24-hour grace period for timestamps to accommodate CI/CD clock drift.

## Vocabulary Tier Policy

**All new entries must be assigned to the "general" tier.**

As of January 2026, the vocabulary tier realignment is complete:
- **Basic tier** (795 entries): Fixed - contains foundational vocabulary
- **Core tier** (1,998 entries): Fixed - contains essential adult communication vocabulary
- **General tier** (4,566+ entries): All other vocabulary, including all new entries

**Do NOT assign new entries to basic or core tiers** unless explicitly instructed by the user. The basic and core tiers have been curated to meet specific word count targets and maintain semantic group integrity.

In `metadata.vocabulary_tier`, always use `"general"`:
```json
"metadata": {
  "vocabulary_tier": "general",
  "created": "...",
  "modified": "..."
}
```

## Metadata Tags (REQUIRED)

All entries must have properly structured tags in `metadata.tags`. This enables search, filtering, and export functionality.

### Required Tag Categories

```json
"metadata": {
  "vocabulary_tier": "general",
  "tags": {
    "pos": ["noun"],                    // REQUIRED: Part of speech (array)
    "formality": "neutral",             // REQUIRED: formal/neutral/informal/vulgar
    "politeness": "plain",              // REQUIRED: honorific/humble/polite/plain
    "semantic": ["food"]                // REQUIRED: Semantic category (array)
  },
  "created": "...",
  "modified": "..."
}
```

### Part of Speech (`pos`)

Valid values: `noun`, `verb-godan`, `verb-ichidan`, `verb-suru`, `verb-kuru`, `verb-irregular`, `adjective-i`, `adjective-na`, `adjective-no`, `adjective-taru`, `adverb`, `particle`, `conjunction`, `interjection`, `pronoun`, `counter`, `prefix`, `suffix`, `expression`, `pre-noun-adjectival`, `number`, `onomatopoeia`, `auxiliary`

- Use arrays for multi-function words: `["noun", "verb-suru"]`
- The array should list the most common/primary POS first

### Formality

- `formal`: Used in formal/written contexts (敬語, 硬い表現)
- `neutral`: Standard usage appropriate for most contexts (default)
- `informal`: Casual/colloquial usage (くだけた表現)
- `vulgar`: Strong/offensive language (use sparingly)

### Politeness (Keigo Classification)

- `honorific`: 尊敬語 - Elevates the subject (いらっしゃる, おっしゃる)
- `humble`: 謙譲語 - Lowers the speaker (申す, 参る)
- `polite`: 丁寧語 - General polite forms (です/ます base forms)
- `plain`: 普通体 - Plain/dictionary forms (default for most entries)

### Semantic Categories

Choose the most appropriate category(ies) for the word's meaning. The closed
taxonomy lives in `VALID_SEMANTIC` in `build/validate_tags.py` (authoritative;
expanded 2026-06-11 with established-by-usage categories). **Use only tags from
this list** — anything else produces an "Unknown semantic tag" warning and gets
flagged by cross-model review:

**Specific categories** (use when applicable):
- Time: `time-day-of-week`, `time-month`, `time-season`, `time-period`, `time-general`
- Nature: `animal-mammal`, `animal-bird`, `animal-fish`, `animal-insect`, `animal-general`, `plant-tree`, `plant-flower`, `plant-general`, `weather`, `geography`, `nature`
- Human: `body-part`, `body-internal`, `family`, `person`, `occupation`, `personality`, `appearance`
- Objects: `food`, `clothing`, `building`, `transportation`, `tool`, `furniture`, `electronics`, `money`
- Abstract: `emotion`, `color`, `number`, `direction`, `size`, `quantity`, `abstract`, `change`, `evaluation`
- Actions: `movement`, `communication`, `cognition`, `existence`, `creation`, `consumption`
- Social life: `greeting`, `education`, `work`, `leisure`, `daily-life`, `shopping`, `travel`, `cooking`
- Fields & topics: `business`, `economics`, `finance`, `law`, `politics`, `society`, `culture`, `religion`, `history`, `science`, `technology`, `health`, `language`, `media`, `music`, `art`, `entertainment`, `sports`, `military`
- Special: `proverb`, `idiom`
- Proper nouns (policy adopted 2026-08-11): `proper-noun` (umbrella) plus at
  least one of `place-name`, `person-name`, `organization-name`, `work-name`,
  `event-name` (incl. awards, festivals, competitions), `brand-name`.
  **The pairing is enforced**: a specific category without `proper-noun` is a
  validation error; `proper-noun` without a specific category is a warning.
  Keep ordinary topical tags alongside (富士山 → `geography`, `proper-noun`,
  `place-name`). Proper-noun entries use `part_of_speech` `"noun (proper)"`
  and `metadata.tags.pos` `["noun"]`; see `prompts/newentries.md`
  ("Proper-Noun Entries") for full conventions.

**Fallback categories** (when no specific category fits):
- `general`: For nouns without a specific semantic category
- `action`: For verbs not fitting other action categories
- `descriptive`: For adjectives, adverbs, and mimetic manner/quality words
- `grammatical`: For particles and conjunctions
- `expression`: For fixed expressions and interjections
- `onomatopoeia`: For mimetic words

**Conventions**: internal organs use `body-internal`; external anatomy uses
`body-part`; `health` is for conditions/procedures, not anatomy. Common
near-misses: use `time-general` (not `time`), `person` (not `people`),
`society` (not `social`), `health` (not `medical`/`medicine` — `medical` is a
domain tag), `transportation` (not `transport`), `animal-general` (not
`animals`), `economics` (not `economy`).

### Optional Tag Categories

```json
"tags": {
  // ... required tags above ...
  "transitivity": "transitive",     // For verbs: transitive/intransitive/both
  "style": ["spoken"],              // written/spoken/literary/archaic/slang
  "domain": ["business"]            // business/academic/technical/legal/medical/etc.
}
```

- `transitivity`: Required for verbs - indicates if verb takes a direct object
- `style`: Use when word is strongly associated with a medium
- `domain`: Use when word is specialized/technical

### Tag Selection Tips

1. **Be specific when possible**: Use `food` not `general` for 寿司
2. **Multiple tags allowed**: 朝ご飯 can be `["food", "time-period"]`
3. **Match the primary meaning**: Tag based on the word's core meaning
4. **Check similar entries**: Ensure consistency with related words

## Quality Checklist

Before finalizing any entry, verify:
- [ ] **File placed in correct directory** (use `python3 build/get_entry_path.py <reading> <entry_id>`)
- [ ] **All kanji have furigana** (headword, examples, AND notes)
- [ ] Verify: `python3 build/verify_furigana.py <entry_id>` shows "✓ OK"
- [ ] **Tags are complete**: pos, formality, politeness, semantic all present
- [ ] Examples progress from simple to complex
- [ ] At least one collocation or fixed phrase is shown
- [ ] Grammar patterns are explicitly demonstrated
- [ ] Notes cover common learner mistakes
- [ ] Notes are properly formatted (see `vocabulary-notes` skill)
- [ ] Depth matches similar entries in the dictionary
- [ ] All examples have valid sense_numbers
- [ ] Run `python3 build/validate.py` to catch any directory or other errors
