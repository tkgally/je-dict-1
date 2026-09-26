# Add Inline Word Links

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

Add cross-reference links to example sentences and notes, allowing users to click any word to navigate to its dictionary entry. This is a **semantic task** that requires your knowledge of Japanese - it cannot be automated.

## Task Focus

**Single focus**: Add inline word links to example sentences and notes.

For each entry, you will:
1. Read each example sentence and note carefully
2. Identify each word and its grammatical function
3. Look up or verify the correct entry ID for each word
4. Add link markup, ensuring semantic correctness
5. Save the updated entry

Load the skill file for detailed requirements and the common words reference table:
```
.claude/skills/inline-word-links/SKILL.md
```

## Starting Point

```bash
cat polishing/tasks/inline-links/progress.txt
```

Find the first entry file that starts with that number.

## Priority Mode (Optional)

If a priority file exists, process entries in priority order instead of sequentially by ID:

```bash
ls polishing/priority/cross_refs.txt 2>/dev/null
```

**If the file exists**:
1. Read the priority file to get the ordered list of entry IDs
2. Find your current position: check `polishing/tasks/inline-links/progress.txt` for the last processed entry
3. Skip any entries in the priority list that come before your last processed entry
4. Process entries in priority file order (highest priority first)
5. Update `polishing/tasks/inline-links/progress.txt` with the ID of the last entry processed (NOT the next sequential ID, but the next entry in the priority list)

**If the file does not exist**: Fall back to sequential processing by ID (the standard behavior described in "Starting Point" above).

**Regenerating priorities**: Run `python3 build/prioritize_polishing.py --task cross_refs` to refresh the priority list. This is useful after many entries have been polished and priorities have shifted.

## Link Format

```
⟦{surface|reading}→baseform：entry_id⟧
```

**Example:**
```
⟦{本|ほん}→本：00111_hon⟧⟦を→を：00422_wo⟧⟦{読|よ}む→読む：00426_yomu⟧。
```

## CRITICAL: Semantic Verification

**Every link MUST be verified semantically.**

This means:
- Reading the full sentence to understand context
- Confirming each word's meaning matches the target entry
- Verifying correct word boundaries
- NOT blindly matching by reading alone

### Common Mistakes to Avoid

| Mistake | Example | Correct Approach |
|---------|---------|------------------|
| Wrong homograph | の → 野 (field) | の is usually the particle (09472_no), not 野 (03535_no) |
| Wrong word | ある as noun | Verify: is this the verb ある (00006_aru) or a different word? |
| Bad boundaries | もの + です | Consider if ものです is a grammatical pattern |

## Workflow

1. **Read the progress file** to find the next entry

2. **Load and examine the entry**:
   - Read each example sentence fully
   - Read the notes section if present

3. **For each example sentence**:
   a. Identify every word (content words and particles)
   b. For each word:
      - Determine its meaning in this context
      - Look up the entry ID (use skill reference table or search)
      - Verify the gloss matches the intended meaning
   c. Add link markup to the japanese field
   d. Do NOT link the entry's own headword (no self-reference)
   e. Do NOT link punctuation

4. **For notes with Japanese text**:
   - Apply the same process to Japanese phrases in notes
   - Skip section headers and non-sentence text

5. **Update timestamp and save**:
   ```bash
   python3 build/get_timestamp.py
   ```
   Use this timestamp for the `modified` field.

6. **After every 4-6 entries** (smaller batches work better for context management):
   - Update `polishing/tasks/inline-links/progress.txt`
   - Validate and build:
     ```bash
     make build
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Inline links: add links to entries XXXXX-XXXXX"
     ```
     **In parallel mode**: Replace `git add -A` with `git add entries/ polishing/sessions/` to avoid staging shared files.

7. **When finishing** (end of session or context getting long):
   a. Update `polishing/tasks/inline-links/progress.txt`
   b. Write session log to `polishing/sessions/inline-links_{date}_{nnn}.md`:
      ```
      ## Session: Inline Links
      Date: YYYY-MM-DD
      Entries processed: XXXXX-XXXXX

      ### Entries Modified
      - [entry_id]: [number of examples linked]

      ### Words Marked noentry (candidates for future entries)
      - word1 (meaning)
      - word2 (meaning)

      ### Notes
      - Any unusual cases or decisions made

      ### Next Entry
      XXXXX
      ```
   c. Commit all changes

## Looking Up Entry IDs

### For Common Words
Use the reference table in the skill file. Key entries:

**Particles:**
- が: 00051_ga
- は: 00079_ha
- を: 00422_wo
- に: 00314_ni
- で: 00502_de
- の: 09472_no (possessive particle, NOT 野)
- と: 00512_to
- も: 00484_mo
- から: 00504_kara
- まで: 00490_made
- か: 09473_ka
- ね: 09474_ne
- よ: 09475_yo

**Common Verbs:**
- する: 00392_suru
- ある: 00006_aru
- いる: 00495_iru
- 行く: 00119_iku
- 来る: 00254_kuru
- 見る: 00283_miru
- 食べる: 00396_taberu

### For Other Words
Use the pre-built word lookup table at `build/word_id_lookup.json`:
```bash
python3 -c "
import json
with open('build/word_id_lookup.json') as f:
    lookup = json.load(f)
reading = 'TARGET_READING'
matches = lookup['by_reading'].get(reading, [])
for m in matches:
    print(f\"{m['id']}: {m.get('gloss', '')[:50]}\")
"
```

Replace `TARGET_READING` with the hiragana reading. For headword lookups, use `lookup['by_headword']` instead.

## Example Transformation

**Before:**
```json
"japanese": "{私|わたし}は{日本語|にほんご}を{勉強|べんきょう}しています。"
```

**After:**
```json
"japanese": "⟦{私|わたし}→私：02988_watashi⟧⟦は→は：00079_ha⟧⟦{日本語|にほんご}→日本語：00614_nihongo⟧⟦を→を：00422_wo⟧⟦{勉強|べんきょう}しています→勉強する：00527_benkyousuru⟧。"
```

Note:
- Punctuation (。) is NOT linked
- Conjugated form (しています) links to dictionary form (勉強する)
- Each word verified semantically

## Using `noentry`

For words not in the dictionary:
```
⟦{矍鑠|かくしゃく}→矍鑠：noentry⟧
```

## Quality Checklist

Before saving each entry:
- [ ] All words semantically verified
- [ ] No self-references (headword not linked in own examples)
- [ ] Punctuation not linked
- [ ] Conjugations link to dictionary forms
- [ ] Entry IDs are valid
- [ ] Furigana preserved within links

## Progress Update Format

Keep the progress file minimal:
```
next: XXXXX
```

Optionally, add a summary line for the next session:
```
next: XXXXX
last_session: YYYY-MM-DD, entries AAAAA-BBBBB, N entries modified
```

## Parallel Execution Mode

This task supports parallel execution when given an explicit ID range. Two or more sessions can run this task simultaneously on non-overlapping ID ranges.

### How to invoke

When starting the session, specify a range:
> "Process entries 10000-10499 only."

### Behavior in parallel mode

When an ID range is given:
1. **Ignore** `progress.txt` — do not read it or update it
2. **Process only** entry files whose numeric ID falls within the given range (inclusive)
3. **Skip shared-file updates**: do NOT run `update_indexes.py`, `build_flat.py`, or `update_kanji_index.py`
4. **Commit entry changes only**: `git add entries/ polishing/sessions/ && git commit -m "..."`
5. **Do NOT run `make build`** — a coordinator will do this after all parallel sessions complete
6. **Do NOT push to main** — push to a feature branch and create a PR, but do NOT merge it. The coordinator will handle merging.

### After parallel sessions complete

A coordinator step (run manually or via `build/parallel_coordinator.py`) will:
1. Merge all parallel session branches
2. Run `update_indexes.py`, `build_flat.py`, and other shared-file regeneration
3. Create a single combined PR

### When NO range is given

Operate in **legacy sequential mode**: read `progress.txt`, process entries sequentially from that point, update `progress.txt`, and run `make build` as usual. This is the default behavior.

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow." The key points:

1. **Run `make build` BEFORE the final commit** so that `docs/` and all build artifacts are included
2. **`git add -A`** to stage everything (entries, docs, indexes, kanji, progress file, session log, etc.)
3. **Commit and push** to the feature branch
4. **Create a PR** for the branch
5. **Wait for CI** with a single blocking call: `gh pr checks <number> --repo tkgally/je-dict-1 --watch --fail-fast` (exits 0 on success, non-zero on failure). Do NOT wrap this in a `while`/`sleep`/`curl` polling loop — `--watch` already waits, and hand-rolled streaming loops get routed through the `Monitor` tool (separate permission grant) which will deadlock an unattended session.
6. **Squash-merge the PR** once all checks are green
7. **If CI fails**: read the error, fix the issue, push again, and repeat from step 5
8. **Post-merge cleanup**: switch to main, pull, verify clean state, delete feature branch locally and remotely

**CRITICAL**: The PR must include rebuilt `docs/` files. If you commit entry changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.

## Output at Session End

When stopping, report:
1. Entry range processed
2. Number of entries modified
3. Any unusual cases encountered
4. Next entry to continue from
