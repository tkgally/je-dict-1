# Polish Furigana Correctness

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

Check dictionary entries one by one for **incorrect furigana readings**. This is a **semantic task** that requires your knowledge of Japanese - it cannot be automated because determining whether a reading is correct requires understanding context, compound word rules, and knowing when special or irregular readings apply.

## Task Focus

**Single focus**: Are all existing furigana readings correct?

For each entry, verify readings in:
- `headword`
- `reading` (should match headword furigana)
- `examples[].japanese`
- `notes`
- `cross_references[].headword` and `.reading`

If any reading is incorrect, fix it using your knowledge of Japanese.

## Starting Point

```bash
cat polishing/tasks/furigana-correctness/progress.txt
```

Find the first entry file that starts with that number.

## Priority Mode (Optional)

If a priority file exists, process entries in priority order instead of sequentially by ID:

```bash
ls polishing/priority/furigana.txt 2>/dev/null
```

**If the file exists**:
1. Read the priority file to get the ordered list of entry IDs
2. Find your current position: check `polishing/tasks/furigana-correctness/progress.txt` for the last processed entry
3. Skip any entries in the priority list that come before your last processed entry
4. Process entries in priority file order (highest priority first)
5. Update `polishing/tasks/furigana-correctness/progress.txt` with the ID of the last entry processed (NOT the next sequential ID, but the next entry in the priority list)

**If the file does not exist**: Fall back to sequential processing by ID (the standard behavior described in "Starting Point" above).

**Regenerating priorities**: Run `python3 build/prioritize_polishing.py --task furigana` to refresh the priority list. This is useful after many entries have been polished and priorities have shifted.

## Workflow

1. **Read the progress file** to find the next entry to check

2. **Load the entry** and verify all furigana readings are correct

3. **For each entry**:
   - If all readings are correct: Move to the next entry (no changes needed)
   - If incorrect readings found: Fix them, update the `modified` timestamp, and save

   **CRITICAL - Timestamp requirement**:
   ```bash
   # Run IMMEDIATELY BEFORE saving each modified entry
   python3 build/get_timestamp.py
   ```

4. **After every ~50 entries** (or when you make changes):
   - Update `polishing/tasks/furigana-correctness/progress.txt` with the next entry number
   - Validate and build:
     ```bash
     make build
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Furigana correctness: check entries XXXXX-XXXXX"
     ```
     **In parallel mode**: Replace `git add -A` with `git add entries/ polishing/sessions/` to avoid staging shared files.

5. **When finishing** (end of session or context getting long):
   a. Update `polishing/tasks/furigana-correctness/progress.txt`
   b. Write session log to `polishing/sessions/furigana-correctness_{date}_{nnn}.md`:
      ```
      ## Session: Furigana Correctness
      Date: YYYY-MM-DD
      Entries checked: XXXXX-XXXXX

      ### Corrections Made
      - [entry_id]: [field] - changed {kanji|wrong} to {kanji|correct}

      ### Next Entry
      XXXXX
      ```
   c. Commit all changes
   e. Re-read this prompt and continue from step 1

## What to Verify

### Common Error Types

1. **Wrong on/kun reading**:
   - Error: `{人|にん}` when standalone (should be `{人|ひと}`)
   - Error: `{日|にち}` for "day" in general (context-dependent)

2. **Missed rendaku**:
   - Error: `{花火|はなひ}` (should be `{花火|はなび}`)
   - Error: `{手紙|てかみ}` (should be `{手紙|てがみ}`)

3. **Wrong compound reading**:
   - Error: `{今日|きょうにち}` for "today" (should be `{今日|きょう}`)
   - Error: `{大人|だいじん}` (should be `{大人|おとな}`)

4. **Irregular readings missed**:
   - Error: `{明日|みょうにち}` for casual "tomorrow" (often `{明日|あした}`)
   - Error: `{昨日|さくじつ}` for casual "yesterday" (often `{昨日|きのう}`)

5. **Reading/headword mismatch**:
   - The `reading` field must match the hiragana rendering of the `headword` furigana

### Fields to Cross-Check

- **headword** vs **reading**: Must match
- **cross_references[].headword** vs **.reading**: Must match
- **examples**: Each kanji should have appropriate contextual reading

## Why This Cannot Be Automated

Verifying furigana correctness requires semantic knowledge:
- **Context-dependent readings**: 生 has many readings depending on word
- **Stylistic choices**: 今日 as きょう vs こんにち depends on tone
- **Historical vs modern**: Some words have alternative readings
- **Domain-specific**: Technical terms may have special readings
- **Recognizing compounds**: Understanding where word boundaries are

Only a knowledgeable reader can verify readings are contextually correct.

## Common Problem Patterns

1. **Systematic errors**: Same kanji misread consistently
2. **Compound confusion**: Wrong reading for multi-kanji words
3. **Copy-paste errors**: Reading from one word applied to another
4. **Over-regularization**: Applying common reading when irregular one is correct
5. **Reading field drift**: `reading` field not updated when headword changed

## Verification Process

For each entry:
1. Read the headword aloud mentally - does the furigana match?
2. Check that `reading` field equals headword with kanji removed
3. Read each example - are the readings natural?
4. Check notes for any technical terms
5. Verify cross-reference readings match their targets

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

## Output at Session End

When stopping (user request or context reset), report:
1. Entry range checked
2. Number of entries with corrections
3. Summary of correction types
4. Next entry to continue from
