# Add Entries for Words Marked `noentry`

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

Create dictionary entries for words that were marked `noentry` in inline word links, then update those links with the correct entry IDs.

## Overview

When adding inline word links to example sentences, words without dictionary entries are marked with `noentry`:

```
⟦{暴走|ぼうそう}→暴走：noentry⟧
```

This task creates entries for these words and updates the links. Since the `noentry` tags may have been added weeks or months ago, some words may already have entries that were created after the tag was written. The duplicate-checking process below accounts for this.

## Session Workflow

### Step 1: Preparation

1. **Read PROJECT_CONTEXT_BRIEF.md** for current counts and critical rules.

2. **Find all `noentry` words** and build a working list:
   ```bash
   grep -r "：noentry⟧" entries/ --include="*.json" -h | \
     grep -oE '⟦[^⟧]+：noentry⟧' | sort | uniq -c | sort -rn
   ```

3. **Extract the unique base words**:
   ```bash
   grep -r "：noentry⟧" entries/ --include="*.json" -h | \
     grep -oE '→[^：]+：noentry' | sed 's/→//;s/：noentry//' | sort -u
   ```

4. **Create a working list** of words, noting for each:
   - The base word (dictionary form)
   - Its reading (from the surface form with furigana)
   - The likely part of speech
   - How many times it appears (higher frequency = higher priority)

### Step 2: Check Each Word for Existing Entries

For each word on your list, determine whether it genuinely needs a new entry or whether an existing entry already covers it. This is a multi-step check because exact-match tools can miss orthographic variants.

#### 2a. Run the duplicate check script

```bash
python3 build/check_duplicate.py "暴走" "ぼうそう"
```

**Do NOT use `--skip-candidates` for this task** — these words are not coming from `candidate_words.json`, so you need the full check against both entries and candidates.

- If it says **DUPLICATE** → the entry already exists. Skip to Step 3 (link update only).
- If it says **OK** → proceed to step 2b.
- If it reports **homophones** → evaluate whether any is a spelling variant of the same word.

#### 2b. Semantic / orthographic variant check

The `noentry` tag records the base form as written in the original example. But an entry may exist under a different orthographic form. Common variations:

| Variation | Example |
|-----------|---------|
| Kanji vs kana spelling | 見つかる vs みつかる |
| Alternative kanji | 聞く vs 聴く |
| する compound vs standalone | 勉強する → existing entry for 勉強 |
| Inflected form used as base | 作り方 → existing entries for 作る + 方 |
| Kana long vowel mark | おおきい vs おーきい |

**How to check**: Search the entries index for the reading (ignoring headword form):

```bash
grep -i "reading_hiragana" entries_index.json | grep "ぼうそう"
```

Also try searching by a key kanji or substring if the word is a compound:

```bash
grep "暴走" entries_index.json
```

**Decision**:
- If an existing entry covers the same word with the same meaning → skip entry creation, go to Step 3 (update the link to point to the existing entry).
- If the word is a compound like 作り方 and the components already have entries → skip entry creation, just remove the `noentry` link or update it to point to the most relevant component.
- If no existing entry covers this word → proceed to entry creation (Step 2c).

#### 2c. Check the candidate list

```bash
python3 build/manage_candidates.py check "暴走" "ぼうそう"
```

If the word is already a candidate, note this — you will create the entry (and `update_indexes.py` will remove the candidate automatically).

### Step 3: Process Each Word

For each word on your list, do ONE of the following:

#### Option A: Entry already exists — update the link only

If step 2 found an existing entry:

1. Find files containing the noentry link:
   ```bash
   grep -rl "→暴走：noentry⟧" entries/ --include="*.json"
   ```

2. In each file, replace `noentry` with the correct entry ID:
   - Old: `⟦{暴走|ぼうそう}→暴走：noentry⟧`
   - New: `⟦{暴走|ぼうそう}→暴走：09478_bousou⟧`

3. Verify the existing entry's meaning matches the context where the link appears. If the word is used with a different sense, note this and decide whether a separate entry is warranted.

4. **Update the `modified` timestamp** (from `python3 build/get_timestamp.py`) for each entry file you changed.

#### Option B: No entry exists — create a new entry, then update the link

1. **Get the next available ID** (run before EACH new entry — never reuse):
   ```bash
   python3 build/get_next_id.py
   ```

2. **Get timestamp**:
   ```bash
   python3 build/get_timestamp.py
   ```

3. **Determine the part of speech** and load the appropriate skill:
   - Verbs: `/verb-entry`
   - Adjectives: `/adjective-entry`
   - Nouns/Others: `/other-entries`
   - Particles: `/particle-entry`

4. **Create the entry** following standard quality requirements:
   - `vocabulary_tier: "general"` for all new entries
   - `schema_version: "2.0"`
   - At least 3 examples **per sense**, with progressive length. For multi-sense entries, this means 3+ examples for EACH sense (e.g., a 2-sense entry needs at least 6 examples total). Do NOT split 3 examples across senses — each sense must independently have 3+.
   - All kanji must have furigana in all fields (headword, examples, notes)
   - All required tags (pos, formality, politeness, semantic)
   - All examples must have `sense_numbers`
   - **NEVER add inline word links (⟦...⟧)** in the new entry — those are added in a separate polishing step
   - All explanations in English; Japanese only in examples, collocations, patterns
   - Notes must follow the Notes Field Requirements below (this is critical — see the dedicated section)

5. **Write the entry file**:
   - Use `python3 build/get_entry_path.py <reading> <id>` to get the correct path
   - Example: `entries/09000/09478_bousou.json`

6. **Update the noentry links** (same as Option A steps 1-4, using the new entry ID).

#### Option C: Word is a sub-component or inflection — remove or simplify the link

If the `noentry` word is a compound like 作り方 where the components (作る, 方) already have entries, or if it's a grammatical form that doesn't warrant its own entry:

1. Either remove the `⟦...：noentry⟧` wrapper entirely (leaving the plain Japanese text), or replace the link with one pointing to the most relevant component entry.
2. Update the `modified` timestamp for each changed file.

### Step 4: Validate and Build

After processing all words (or a batch, if stopping mid-list):

```bash
python3 build/validate.py                          # Fix any errors before continuing
python3 build/find_missing_furigana.py | head -60   # Check for missing furigana
python3 build/add_conjugations.py                   # Add conjugation to any new verbs
python3 build/add_adjective_conjugations.py         # Add conjugation to any new i-adjectives
python3 build/update_indexes.py                     # Sync indexes and candidate list
python3 build/update_kanji_index.py --check-new     # Check for new kanji needing IDs
python3 build/build_flat.py                         # Rebuild the static site
```

**If `find_missing_furigana.py` shows entries from your session**, fix them before building.

**If new kanji are found**, assign on'yomi, kun'yomi, and gloss before building.

### Step 5: Commit, Push, and Merge

1. **Update PROJECT_STATUS.md** Recent Changes section with a summary (keep only 5 most recent entries; rotate oldest to archive).

2. **Commit** (combine new entries and link updates):
   ```bash
   git add entries/ docs/ *.json PROJECT_STATUS.md
   git commit -m "Add entries for noentry words and update links: [summary]"
   ```

3. **Push** to the current branch.

4. **PR and merge workflow**:
   - Create a PR for the branch
   - Wait for CI with a single blocking call: `gh pr checks <number> --repo tkgally/je-dict-1 --watch --fail-fast` (exits 0 on success, non-zero on failure). Do NOT drive a polling loop via `pull_request_read` or shell `while`/`sleep`/`curl` — streaming loops get routed through the `Monitor` tool (separate permission grant) and will deadlock an unattended session.
   - Squash-merge the PR once all checks are green
   - If CI fails: read the error, fix the issue, push again, and repeat

## Prioritization

When multiple `noentry` words exist, prioritize:

1. **Easy link-only fixes** — Words that already have entries (just update the link; fast wins)
2. **High frequency** — Words appearing in many examples
3. **Core vocabulary** — Basic words learners need
4. **Domain clusters** — Words from the same topic area (efficient to create together)

## Notes Field Requirements

**See the `vocabulary-notes` skill for complete guidelines.** The notes field is a critical part of each entry. Short, unstructured notes are a common quality problem — follow these requirements carefully:

### Structure and Formatting (MANDATORY)

| Requirement | Standard |
|-------------|----------|
| **Section headers** | Use labeled headers (USAGE:, COMMON COLLOCATIONS:, SIMILAR WORDS:, TRANSITIVITY:, ASPECT:, etc.) for distinct categories of information. **Do NOT use `##` markdown headers** — use `UPPERCASE HEADER:` format instead. |
| **Paragraph breaks** | Separate sections with blank lines (`\n\n` in JSON) — never pack multiple topics into one paragraph |
| **Bullet points** | Any list of 2+ items MUST use `- ` bullet points, not inline comma-separated lists |
| **Language** | All explanatory prose in English; Japanese only in example phrases and collocations |
| **Furigana** | All kanji in notes must have furigana: `{漢字|かんじ}` |

### Minimum Content

Every entry's notes should include at least:

1. **Core semantic explanation** — what the word fundamentally means beyond the gloss (1-2 sentences). This MUST be the opening paragraph. Do not start notes with "From English" or a compound structure — always lead with what the word means.
2. **Collocations or common expressions** — as a bulleted list with translations
3. **At least one additional section** from: similar word distinctions, register notes, cultural context, common mistakes, etymology, related terms

### Format Example (in JSON)

```json
"notes": "Core explanation of the word.\n\nCOMMON COLLOCATIONS:\n- {例|れい}one: translation\n- {例|れい}two: translation\n\nSIMILAR WORDS:\n- word1: gloss — how it differs\n- word2: gloss — how it differs"
```

### Anti-Patterns to Avoid

These patterns indicate the notes field is too short or poorly structured:

```
✗ BAD: "From English 'cement'.\n\nCOMMON COLLOCATIONS:\n- A: translation"
  (No core explanation, starts with etymology, only 2 sections)

✗ BAD: "## Common Patterns\n- A: meaning\n- B: meaning"
  (Uses ## markdown headers which render incorrectly on the site)

✗ BAD: "Composed of X + Y. Common collocations: A, B, C. Related: D."
  (Single paragraph, no headers, inline list instead of bullets)

✓ GOOD: "Cement is a powdery building material mixed with water and aggregate to form concrete.\n\nCOMMON COLLOCATIONS:\n- A: translation\n- B: translation\n\nRELATED TERMS:\n- D: gloss — explanation"
  (Core explanation first, separated sections, UPPERCASE headers, bullet points)
```

## Quality Checklist

### For New Entries
- [ ] Duplicate + variant check passed (steps 2a and 2b)
- [ ] All kanji have furigana (headword, examples, notes)
- [ ] At least 3 examples **per sense** with progressive length (multi-sense entries need 3× number of senses)
- [ ] All examples have `sense_numbers`
- [ ] Tags complete (pos, formality, politeness, semantic)
- [ ] `vocabulary_tier: "general"` and `schema_version: "2.0"`
- [ ] Notes have core semantic explanation as opening paragraph
- [ ] Notes use `HEADER:` format (not `## Header`)
- [ ] Notes have at least 3 sections (core explanation + collocations + one additional)
- [ ] No inline word links (⟦...⟧) in the new entry

### For Updated Links
- [ ] Entry ID is correct
- [ ] Meaning matches context in the original example
- [ ] Furigana preserved correctly in the link
- [ ] No broken link syntax

## Session Output

At session end, report:
1. Number of new entries created
2. Number of links updated (broken down: link-only fixes vs new-entry links)
3. Any words skipped (with reason)
4. Remaining `noentry` count
