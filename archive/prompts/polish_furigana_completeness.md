# Polish Furigana Completeness

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

Check dictionary entries one by one for **missing furigana on kanji**. This is a **semantic task** that requires your knowledge of Japanese - it cannot be automated because determining the correct reading for each kanji requires understanding context, compound words, and special readings.

## Task Focus

**Single focus**: Are all kanji in the entry marked with furigana `{kanji|reading}`?

For each entry, check these fields:
- `headword`
- `examples[].japanese`
- `notes`
- `cross_references[].headword`

If any kanji lacks furigana, add the appropriate reading using your knowledge of Japanese.

## Starting Point

```bash
cat polishing/tasks/furigana-completeness/progress.txt
```

Find the first entry file that starts with that number.

## Priority Mode (Optional)

If a priority file exists, process entries in priority order instead of sequentially by ID:

```bash
ls polishing/priority/furigana.txt 2>/dev/null
```

**If the file exists**:
1. Read the priority file to get the ordered list of entry IDs
2. Find your current position: check `polishing/tasks/furigana-completeness/progress.txt` for the last processed entry
3. Skip any entries in the priority list that come before your last processed entry
4. Process entries in priority file order (highest priority first)
5. Update `polishing/tasks/furigana-completeness/progress.txt` with the ID of the last entry processed (NOT the next sequential ID, but the next entry in the priority list)

**If the file does not exist**: Fall back to sequential processing by ID (the standard behavior described in "Starting Point" above).

**Regenerating priorities**: Run `python3 build/prioritize_polishing.py --task furigana` to refresh the priority list. This is useful after many entries have been polished and priorities have shifted.

## Workflow

1. **Read the progress file** to find the next entry to check

2. **Load the entry** and examine all text fields for kanji without furigana

3. **For each entry**:
   - If all kanji have furigana: Move to the next entry (no changes needed)
   - If missing furigana found: Add the correct readings, update the `modified` timestamp, and save

   **CRITICAL - Timestamp requirement**:
   ```bash
   # Run IMMEDIATELY BEFORE saving each modified entry
   python3 build/get_timestamp.py
   ```

4. **After every ~50 entries** (or when you make changes):
   - Update `polishing/tasks/furigana-completeness/progress.txt` with the next entry number
   - Validate and build:
     ```bash
     make build
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Furigana completeness: check entries XXXXX-XXXXX"
     ```
     **In parallel mode**: Replace `git add -A` with `git add entries/ polishing/sessions/` to avoid staging shared files.

5. **When finishing** (end of session or context getting long):
   a. Update `polishing/tasks/furigana-completeness/progress.txt`
   b. Write session log to `polishing/sessions/furigana-completeness_{date}_{nnn}.md`:
      ```
      ## Session: Furigana Completeness
      Date: YYYY-MM-DD
      Entries checked: XXXXX-XXXXX

      ### Changes Made
      - [entry_id]: Added furigana to [field] - [details]

      ### Next Entry
      XXXXX
      ```
   c. Commit all changes

## What to Check

### Headword
The headword should have furigana on all kanji:
- Good: `{食|た}べる`
- Bad: `食べる`

### Examples
All kanji in example sentences need furigana:
- Good: `{朝|あさ}ごはんを{食|た}べる。`
- Bad: `朝ごはんを食べる。`

### Notes
The notes field often contains kanji that need furigana:
- Transitivity pairs: `{自動詞|じどうし}`, `{他動詞|たどうし}`
- Related words: `{言葉|ことば}`, `{表現|ひょうげん}`
- Grammar terms: `{連用形|れんようけい}`

### Cross-references
Cross-reference headwords need furigana:
- Good: `"headword": "{余|あま}す"`
- Bad: `"headword": "余す"`

## Why This Cannot Be Automated

Adding furigana requires semantic knowledge:
- **Compound readings**: 今日 can be きょう or こんにち depending on meaning
- **Rendaku**: 人 is usually ひと but にん in compounds
- **Kun vs on readings**: Context determines which reading applies
- **Irregular readings**: 大人(おとな), 明日(あした)
- **Name readings**: Special readings for proper nouns

Only a knowledgeable reader can determine the correct reading in context.

## Common Patterns to Watch

1. **Notes field**: Often has technical terms or related words missing furigana
2. **Longer examples**: More likely to have missed kanji
3. **Compound words**: May need careful attention for readings
4. **Cross-references**: Sometimes added without furigana on the headword

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

That's all. This allows quick loading into context.

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

## Output at Session End

When stopping (user request or context reset), report:
1. Entry range checked
2. Number of entries modified
3. Summary of changes made
4. Next entry to continue from
