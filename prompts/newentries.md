# New Entry Creation Prompt

Add new entries to the Japanese-English learner's dictionary from candidate_words.json.

## Pre-flight: sweep stranded PRs

**Run this as the first step of every session, before you read any candidate or entry data.**

Perform the stranded-PR sweep **via MCP**, as described in `CLAUDE.md` → "Sweep stranded PRs via MCP" (`mcp__github__list_pull_requests` → for each open `claude/*` PR, `mcp__github__pull_request_read` `method: "get_files"` → close the ones whose maximum entry ID is below `polishing/tasks/comprehensive/progress.txt`'s `next:` value). It will never close a new-entries PR by accident — those entries always have IDs far above the comprehensive-polish cursor.

**Do not run `pipeline/sweep-stranded-prs.py`** — direct GitHub REST returns HTTP 403 in the Routine/web environment, so it's a no-op there (it now exits cleanly with a pointer to the MCP procedure).

## Per-session budget

This prompt is run unattended on a schedule. Plan the session so the wrap-up phase has enough context to complete reliably.

- **Target: 20–25 entries per session.** Stop earlier if you reach ~60% of your context window before that — the wrap-up phase (build, commit, push, PR creation, up-to-~8-minute MCP CI-poll wait, merge call) needs ~40% headroom.
- **Match the size of recent entries — do not exceed it.** See "Length targets" below for per-field budgets. A well-formed entry in this dictionary is concise, not maximally thorough.
- **Stop earlier than 20 entries if** tool outputs are getting truncated, you've already done a fix-up round (e.g., resolving a duplicate after creation), or `find_missing_furigana.py` has reported issues you need to chase. Better to wrap up with fewer entries than to leave a stranded PR.
- **Take stock periodically**: every ~10 entries, briefly check how full context feels and decide whether to continue or wrap up.

## Length targets (MANDATORY — read before writing any entry)

Entries in this dictionary are **short by design**. The gloss is for scanning; the definition gives the longer explanation; the notes add usage and collocations. None of these fields should balloon. Match the shape of recent reference entries like `entries/27000/27261_motenashi.json` (single-sense noun, ~75 lines) or `entries/27000/27264_hokorimamire.json` (na-adjective, ~65 lines) — **not** the verbose entries from the 27386–27421 range (those were a quality regression and are not the target).

### Per-field budgets

| Field | Target | Hard ceiling |
|-------|--------|--------------|
| `gloss` (top-level) | 3–8 words, semicolon-separated | ~80 chars |
| `definitions[i].gloss` (per sense) | 3–10 words, semicolon-separated | ~80 chars |
| `definitions[i].explanation` | 1–3 sentences, ~150–400 chars | ~500 chars |
| `notes` (single-sense entry) | ~400–900 chars | ~1,200 chars |
| `notes` (multi-sense entry) | ~700–1,500 chars | ~2,000 chars |
| `examples[].japanese` per sense | meet the per-sense minimum, exceed by 0–1 | — |

If any field exceeds its hard ceiling, **cut before moving on to the next entry**. Bloat is contagious: later entries inherit the shape of earlier ones in the same session.

### Gloss vs. definition (CRITICAL)

The top-level `gloss` is a scanning aid, not a definition. It must NOT contain:

- Parenthetical mini-definitions like `(from English "cloth")` or `(a tablecloth, cleaning cloth, or wallpaper-class wall covering)`
- Numbered clauses like `(1) cloth — …; (2) cross — …`
- Etymology, scope qualifications, register notes, or examples of usage
- Complete sentences

Multi-sense entries: the top-level `gloss` should be a short semicolon-joined list of the senses' headline words (e.g. `cloth; cross`), not a paragraph that explains each sense. The per-sense explanations belong in `definitions[i].explanation`.

```
✗ BAD top-level gloss:
"(1) cloth — a tablecloth, cleaning cloth, or wallpaper-class wall covering
(from English \"cloth\"); (2) cross — an X-shape, a crossing, a Christian
cross, or a sports cross-pass (from English \"cross\")"

✓ GOOD top-level gloss:
"cloth; cross"

✓ GOOD per-sense gloss:
"cloth; cleaning cloth; wallpaper-class wall covering"
```

### Notes: target shape, not maximum thoroughness

The `vocabulary-notes` skill lists six possible content categories. **You do not need to hit all of them.** Aim for:

- One short opening sentence on core meaning (often redundant if the gloss already covers it — skip in that case).
- One bulleted list of 3–6 collocations or common expressions.
- One additional section if (and only if) it adds something the gloss + collocations don't: a similar-word distinction, a register note, or a brief cultural context.

Three sections is the target; **four is usually too many; six or more is always too many**. Do not invent extra sections like "WHICH ENGLISH SOURCE WORD", "TYPICAL CONTEXTS", or duplicate "COMMON COMPOUNDS"/"COMMON COLLOCATIONS" pairs just to fill out the entry.

## Candidate Selection Priority

Prefer candidates whose notes mention `seen in entry XXXXX` (or similar phrasing indicating the word appeared in an existing entry's examples or notes). These are added by the comprehensive-polish workflow and represent **internal-completeness gaps** — words the dictionary already references but does not yet define. Filling these closes the dictionary in on itself and is higher priority than adding brainstormed or corpus-harvested candidates.

To find such candidates:

```bash
grep -B1 -A3 '"seen in entry' candidate_words.json | head -40
```

If you've worked through all "seen in entry" candidates, fall back to the standard order (oldest unprocessed candidates first).

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
   python3 build/validate.py                        # Fix any errors before continuing
   python3 build/find_missing_furigana.py | head -60 # Check for missing furigana in notes
   python3 build/add_conjugations.py                 # Add conjugation to any new verbs
   python3 build/add_adjective_conjugations.py       # Add conjugation to any new i-adjectives
   python3 build/update_indexes.py                   # Sync candidate_words.json and check for new kanji
   python3 build/update_kanji_index.py --check-new   # Check for new kanji needing IDs
   python3 build/build_flat.py                       # REQUIRED for live site update
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

## ⚠️ Entry ID and Romaji Format (CRITICAL — validation will fail if wrong)

The entry ID consists of a 5-digit number, an underscore, and the **romaji reading concatenated into one or two lowercase segments**. The schema regex is: `^[0-9]{5}_[a-z]+(_[a-z]+)?$`

### Key rules:
1. **Concatenate the full reading into the romaji** — do NOT split at word boundaries with underscores
2. The ID allows **at most one underscore** after the number (two segments max)
3. The romaji must match the full reading — the validator checks this

### Examples:
```
✓ 21022_ketteisuru        (決定する — けっていする)
✓ 06899_kaowodasu         (顔を出す — かおをだす)
✓ 21019_shitekina         (私的な — してきな)
✓ 21114_shiromizakana     (白身魚 — しろみざかな)
✓ 21409_moushiwakearimasen (申し訳ありません — もうしわけありません)

✗ 21391_kasoku_suru       ← WRONG: splits "suru" as separate segment
✗ 21399_koe_wo_dasu       ← WRONG: three segments after the number
✗ 21410_fushizen_na       ← WRONG: splits "na" as separate segment
```

### File naming matches the ID:
- Entry `21022_ketteisuru` → file `entries/21000/21022_ketteisuru.json`
- Use `python3 build/get_entry_path.py <id> <romaji>` to confirm

## ⚠️ POS Tag Values (CRITICAL — schema enforces exact enum)

The `metadata.tags.pos` array must use **only** these exact values:

| Category | Valid values |
|----------|-------------|
| **Verbs** | `verb-godan`, `verb-ichidan`, `verb-suru`, `verb-kuru`, `verb-irregular` |
| **Adjectives** | `adjective-i`, `adjective-na`, `adjective-no`, `adjective-taru` |
| **Other** | `noun`, `adverb`, `particle`, `conjunction`, `interjection`, `pronoun`, `counter`, `prefix`, `suffix`, `expression`, `pre-noun-adjectival`, `number`, `auxiliary`, `onomatopoeia` |

### Common mistakes to avoid:
```
✗ "verb"          → use verb-godan, verb-ichidan, verb-suru, etc.
✗ "suru-verb"     → use "verb-suru"
✗ "godan-verb"    → use "verb-godan"
✗ "na-adjective"  → use "adjective-na"
✗ "no-adjective"  → use "adjective-no"
✗ "adjective"     → use adjective-i, adjective-na, etc.
✗ "compound-verb" → not a valid tag; use verb-godan or verb-ichidan
```

### POS tag patterns by entry type:
- **Suru verb (with する in headword)**: `["verb-suru"]`
- **Noun that can take する**: `["noun", "verb-suru"]`
- **Godan verb**: `["verb-godan"]`
- **Na-adjective**: `["adjective-na"]`
- **Noun usable with の**: `["noun", "adjective-no"]`
- **Expression**: `["expression"]`

## ⚠️ Semantic Tag Values (closed taxonomy — anything else is flagged by validate_tags.py and the §4 self-check)

`metadata.tags.semantic` must use **only** tags from `VALID_SEMANTIC` in `build/validate_tags.py` (authoritative; expanded 2026-06-11):

| Group | Valid values |
|----------|-------------|
| **Time** | `time-day-of-week`, `time-month`, `time-season`, `time-period`, `time-general` |
| **Nature** | `animal-mammal`, `animal-bird`, `animal-fish`, `animal-insect`, `animal-general`, `plant-tree`, `plant-flower`, `plant-general`, `weather`, `geography`, `nature` |
| **Human** | `body-part`, `body-internal`, `family`, `occupation`, `person`, `personality`, `appearance` |
| **Abstract** | `emotion`, `color`, `number`, `direction`, `size`, `quantity`, `abstract`, `change`, `evaluation` |
| **Objects** | `food`, `clothing`, `building`, `transportation`, `tool`, `furniture`, `electronics`, `money` |
| **Actions** | `movement`, `communication`, `cognition`, `existence`, `creation`, `consumption` |
| **Social life** | `greeting`, `education`, `work`, `leisure`, `daily-life`, `shopping`, `travel`, `cooking` |
| **Fields & topics** | `business`, `economics`, `finance`, `law`, `politics`, `society`, `culture`, `religion`, `history`, `science`, `technology`, `health`, `language`, `media`, `music`, `art`, `entertainment`, `sports`, `military` |
| **Special** | `proverb`, `idiom` |
| **Proper nouns** | `proper-noun` (umbrella — required on every proper-noun entry) plus at least one of: `place-name`, `person-name`, `organization-name`, `work-name`, `event-name`, `brand-name` |
| **Fallbacks** | `general`, `action`, `descriptive`, `grammatical`, `expression`, `onomatopoeia` |

### Common mistakes to avoid:
```
✗ "time"                 → use "time-general"
✗ "people"               → use "person"
✗ "social"               → use "society"
✗ "medical"/"medicine"   → use "health" (medical is a domain tag, not semantic)
✗ "transport"            → use "transportation"
✗ "description"          → use "descriptive"
✗ "animals"              → use "animal-general"
✗ "economy"              → use "economics"
✗ "object"/"place"/"body" → too vague; pick the specific in-list tag
```

Fallback conventions: internal organs use `body-internal`; external anatomy uses `body-part`; `health` is for conditions/procedures. Mimetic adverbs use `descriptive`. Suru-verbs and action nouns carry `action`. Domain tags (`metadata.tags.domain`) have their own closed list: `business`, `academic`, `technical`, `legal`, `medical`, `colloquial`, `internet`.

## Proper-Noun Entries (policy adopted 2026-08-11)

Proper nouns that learners of Japanese should know are in scope: place names, personal names, organization names, work titles, event names, and brand names. Candidates arriving from the queue are already vetted for learner value; create them like any other entry, with these conventions:

- **`part_of_speech`**: `"noun (proper)"` (the established free-text value — 日本, 北海道, and 日本銀行 already use it). **`metadata.tags.pos`**: `["noun"]` (the closed POS list has no proper-noun value; the semantic tags carry the categorization).
- **Semantic tags**: `proper-noun` **plus** the specific category — `place-name`, `person-name`, `organization-name`, `work-name`, `event-name` (incl. awards, festivals, competitions), or `brand-name`. `validate_tags.py` enforces the pairing (category without umbrella = error). Keep any ordinary topical tag that applies too (e.g. 富士山 is `geography`, `proper-noun`, `place-name`).
- **Explanation covers the connotations, not just the referent.** The reason a proper noun earns an entry is its cultural and collocational weight. 銀座 is not just a Tokyo district — it connotes up-scale shopping, and 〜の銀座 labels any bustling shopping street. 甲子園 is a stadium and, by metonymy, the high-school baseball championship and by extension the pinnacle of any youth pursuit. Notes should carry a COMMON EXPRESSIONS or CULTURAL CONTEXT section with these fixed phrases and figurative uses.
- **Examples show the name doing real work** — in set phrases, metonymy, and typical collocations (東京タワー, 京都らしい町並み, 漱石の小説) — not just "X is in Japan."
- **Readings**: hiragana as always; furigana on all kanji including the headword (e.g. `{夏目漱石|なつめそうせき}`).
- **Tier**: general, like all new entries.
- **People**: prefer historical and canonical cultural figures (夏目漱石, 紫式部, 織田信長) whose names appear in idioms, work titles, school curricula, or everyday references (福沢諭吉 → the 10,000-yen note). Avoid current celebrities whose prominence may fade.

## Notes Field Requirements

**See the `vocabulary-notes` skill for complete guidelines and the "Length targets" section above for size budgets.** The notes field is short and useful — neither sparse-and-unstructured nor maximally thorough.

### Structure and Formatting (MANDATORY)

| Requirement | Standard |
|-------------|----------|
| **Section headers** | Use labeled headers (USAGE:, COMMON COLLOCATIONS:, SIMILAR WORDS:, TRANSITIVITY:, ASPECT:, etc.) for distinct categories of information |
| **Paragraph breaks** | Separate sections with blank lines (`\n\n` in JSON) — never pack multiple topics into one paragraph |
| **Bullet points** | Any list of 2+ items MUST use `- ` bullet points, not inline comma-separated lists |
| **Language** | All explanatory prose in English; Japanese only in example phrases and collocations |
| **Furigana** | All kanji in notes must have furigana: `{漢字|かんじ}` |

### Content (target shape)

Aim for exactly the sections the entry needs — typically two or three:

1. **Core semantic explanation** — 1–2 sentences, only if the gloss doesn't already cover it. Skip when redundant.
2. **Collocations or common expressions** — a bulleted list of 3–6 items with translations.
3. **At most one additional section** from: similar word distinctions, register notes, cultural context, common mistakes. Add only if it conveys something the gloss + collocations don't.

**Hard caps:** four sections is the maximum. Six or more is always too many. Total notes length should fit the "Length targets" table above (~400–900 chars for single-sense, ~700–1,500 for multi-sense; hard ceilings ~1,200 / ~2,000). If you find yourself adding a fifth section, stop and cut.

### Format Example (in JSON)

```json
"notes": "Core explanation of the word.\n\nCOMMON COLLOCATIONS:\n- {例|れい}one: translation\n- {例|れい}two: translation\n\nSIMILAR WORDS:\n- word1: gloss — how it differs\n- word2: gloss — how it differs"
```

### Anti-Patterns to Avoid

```
✗ TOO SPARSE: "Composed of X + Y. Common collocations: A, B, C. Related: D."
  (Single paragraph, no headers, inline list instead of bullets)

✗ TOO VERBOSE: Six+ sections including USAGE NOTES, TYPICAL CONTEXTS,
  WHICH ENGLISH SOURCE WORD, separate "COMMON COMPOUNDS" and "COMMON
  COLLOCATIONS" lists, exhaustive related-terms enumeration, etc.

✓ GOOD: "Composed of X + Y.\n\nCOMMON COLLOCATIONS:\n- A: translation\n- B: translation\n- C: translation\n\nSIMILAR WORDS:\n- D: gloss — explanation"
  (Two or three focused sections, headers, bullet points, under the char budget)
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

## PR and merge workflow

Follow the workflow described in CLAUDE.md under "End-of-session PR and merge workflow." For Routine and any unattended session, use the **MCP path** — the `gh` CLI is not authorized in those environments.

### Before the PR

1. **Run `make build`** so `docs/` and all build artifacts are included.
2. **Stage everything** with `git add -A` (entries, `docs/`, `entries_index.json`, `build/word_id_lookup.json`, `kanji/`, session logs, etc.).
3. **Commit and push** to the feature branch.

### MCP path (Routine / unattended default)

1. Call `mcp__github__create_pull_request` with `owner: "tkgally"`, `repo: "je-dict-1"`, `head: "<your branch>"`, `base: "main"`, plus a clear title and body. Note the PR number.
2. **Wait for CI by polling check-runs over MCP** (`pipeline/wait-for-pr-checks.sh` 403s here — do not use it; full loop in `CLAUDE.md` → "MCP path" step 5). Call `mcp__github__pull_request_read` with `method: "get_check_runs"` (**not** `get_status`). *green* = `total_count >= 1` and every run `completed` with `conclusion` `success`/`neutral`/`skipped`; *failed* = any other completed conclusion; *pending* = otherwise. While pending, wait with a backgrounded `sleep 30` (Bash `run_in_background: true`) and re-poll, up to ~16 times (~8 min).
3. **Merge based on the result**:
   - **green**: call `mcp__github__merge_pull_request` with `merge_method: "squash"`. The session is done.
   - **failed / still pending at the cap**: leave the PR open, add a one-line note to your session log, and stop. The next Routine session's pre-flight MCP sweep cleans up once main has advanced past the entry range.
4. **Do not** `git checkout main`, **do not** delete the feature branch from inside this session — the session is on that branch. The repo's "Automatically delete head branches" setting handles remote cleanup once the merge fires.

Do **not** call `mcp__github__enable_pr_auto_merge` from a Routine — it usually fails because the PR is in `unstable` state immediately after creation.

### `gh` path (interactive sessions only)

If `gh` is on PATH and authorized (only true for interactive curator sessions), the equivalent is `gh pr create --repo tkgally/je-dict-1 --head <branch> --base main --title "..." --body "..."` → `gh pr checks <number> --repo tkgally/je-dict-1 --watch --fail-fast` → `gh pr merge <number> --repo tkgally/je-dict-1 --squash`. Do not wrap `gh pr checks --watch` in a `while`/`sleep`/`curl` loop — `--watch` already waits, and hand-rolled streaming loops get routed through Monitor, which can deadlock unattended sessions.

### CRITICAL — both paths

The PR must include rebuilt `docs/` files. If you commit entry changes but not the build output, the live site won't update after merge and the repo will be left in a dirty state for the next session.

## If Duplicates Are Found During Validation

If validate.py reports duplicates, use the resolve-duplicates skill to fix them before continuing.
