# Polish Example Sentences

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

Check dictionary entries one by one for **example sentence quality**: count, vocabulary level compliance, and appropriateness. While counting examples is mechanical, evaluating vocabulary levels and sentence appropriateness is a **semantic task** that requires your knowledge of Japanese - it cannot be automated.

## Task Focus

**Single focus**: Do the example sentences meet all requirements?

For each entry, check:
1. **Count**: Minimum examples per sense (5 for basic/core, 3 for general)
2. **Vocabulary levels**: Tier restrictions for basic and core entries
3. **Appropriateness**: Natural, useful examples with progressive length

Load the skill file for detailed requirements:
```
.claude/skills/example-sentences/SKILL.md
```

## Starting Point

```bash
cat polishing/tasks/example-sentences/progress.txt
```

Find the first entry file that starts with that number.

## Priority Mode (Optional)

If a priority file exists, process entries in priority order instead of sequentially by ID:

```bash
ls polishing/priority/examples.txt 2>/dev/null
```

**If the file exists**:
1. Read the priority file to get the ordered list of entry IDs
2. Find your current position: check `polishing/tasks/example-sentences/progress.txt` for the last processed entry
3. Skip any entries in the priority list that come before your last processed entry
4. Process entries in priority file order (highest priority first)
5. Update `polishing/tasks/example-sentences/progress.txt` with the ID of the last entry processed (NOT the next sequential ID, but the next entry in the priority list)

**If the file does not exist**: Fall back to sequential processing by ID (the standard behavior described in "Starting Point" above).

**Regenerating priorities**: Run `python3 build/prioritize_polishing.py --task examples` to refresh the priority list. This is useful after many entries have been polished and priorities have shifted.

## Workflow

1. **Read the progress file** to find the next entry to check

2. **Load the entry** and examine the examples against all requirements

3. **For each entry**:
   - Check example count against tier requirements
   - For basic/core entries, verify vocabulary restrictions
   - Check progressive length (shorter to longer)
   - Evaluate naturalness and usefulness

   If issues found: Fix or add examples, update `modified` timestamp, save

   **CRITICAL - Timestamp requirement**:
   ```bash
   # Run IMMEDIATELY BEFORE saving each modified entry
   python3 build/get_timestamp.py
   ```

4. **After every ~20 entries** (or when you make changes):
   - Update `polishing/tasks/example-sentences/progress.txt`
   - Validate and build:
     ```bash
     make build
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Example sentences: check entries XXXXX-XXXXX"
     ```
     **In parallel mode**: Replace `git add -A` with `git add entries/ polishing/sessions/` to avoid staging shared files.

5. **When finishing** (end of session or context getting long):
   a. Update `polishing/tasks/example-sentences/progress.txt`
   b. Write session log to `polishing/sessions/example-sentences_{date}_{nnn}.md`:
      ```
      ## Session: Example Sentences
      Date: YYYY-MM-DD
      Entries checked: XXXXX-XXXXX

      ### Changes Made
      - [entry_id]: [issue type] - [brief description]

      ### Next Entry
      XXXXX
      ```
   c. Commit all changes

## Requirements Summary

### Minimum Counts by Tier

| Tier | Min Examples per Sense |
|------|------------------------|
| Basic | 5 |
| Core | 5 |
| General | 3 |

### Vocabulary Restrictions

| Tier | Examples 1-2 | Examples 3+ |
|------|--------------|-------------|
| **Basic** | Basic vocab only | Basic + Core only |
| **Core** | Basic + Core only | Any (prefer dictionary words) |
| **General** | Any | Any |

To verify vocabulary tier:
```bash
python3 build/check_duplicate.py "word" "reading"
```

### Progressive Length

| Example | Target Length |
|---------|---------------|
| 1 | 5-15 chars |
| 2 | 10-20 chars |
| 3 | 15-30 chars |
| 4 | 25-45 chars |
| 5+ | 35-70 chars |

## What Cannot Be Automated

### Vocabulary Level Assessment
- Determining if a word is "basic", "core", or "general" requires knowledge
- Some words aren't in the dictionary - you must judge if appropriate
- Compound expressions need semantic analysis

### Appropriateness Evaluation
- Is this example natural Japanese?
- Does it demonstrate the word's usage clearly?
- Is the context appropriate for learners?
- Does it show important collocations or patterns?

### Writing New Examples
When count is insufficient, you must write new examples that:
- Follow vocabulary restrictions for the tier
- Progress in length appropriately
- Sound natural to native speakers
- Demonstrate the word meaningfully

## Common Issues to Fix

0. **Inline links**: Do NOT add inline word links (⟦...⟧) in this task. Links are added separately via `prompts/polish_add_inline_links.md`.
1. **Insufficient count**: Add examples to meet minimum
2. **Vocabulary violation**: Replace non-compliant words
   - `{購入|こうにゅう}する` → `{買|か}う` (for basic tier)
   - `{使用|しよう}する` → `{使|つか}う`
3. **No length progression**: Reorder or rewrite examples
4. **Unnatural expressions**: Rewrite to sound natural
5. **Missing sense coverage**: Ensure all senses have examples

## Example Format Reminder

```json
{
  "id": "00001_word_ex1",
  "japanese": "{漢字|かんじ}の{例文|れいぶん}。",
  "english": "Example sentence with kanji.",
  "sense_numbers": [1],
  "has_audio": false,
  "notes": null
}
```

- IDs: `{entry_id}_ex{N}` format, sequential
- All kanji must have furigana
- `sense_numbers` must reference valid definition senses

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
2. Number of entries modified
3. Types of issues found and fixed
4. Next entry to continue from
