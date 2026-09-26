# Expand Short Notes

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

Check dictionary entries one by one and **expand entries with inadequate notes**. An entry's notes field should provide learners with enough context to understand and use the word correctly — including usage patterns, similar word contrasts, register information, and cultural context where relevant.

## Task Focus

**Single focus**: Does this entry have adequate notes?

For each entry, check:
1. **Length**: Notes should be substantial enough to help learners (not just a single sentence)
2. **Structure**: Notes should cover the relevant categories for the POS type
3. **Content**: Notes should include useful information that goes beyond the definition

Load the skill file for detailed requirements:
```
.claude/skills/vocabulary-notes/SKILL.md
```

## What to Add

When expanding notes, consider adding (as appropriate for the word type):

- **Core explanation** of what the word means and how it's used
- **Common patterns and collocations** (grammatical patterns, set phrases)
- **Similar word contrasts** (how this word differs from related words)
- **Register and usage context** (formal/informal, spoken/written)
- **Cultural context** (customs, conventions, background knowledge)
- **Kanji breakdown** (for compound words, what each kanji contributes)
- **Forms and variations** (alternate readings, casual forms)
- **Aspect/ている behavior** (for verbs with non-obvious aspect)
- **Transitivity information** (for verb pairs)

Not every entry needs all of these — use judgment based on the word type and what would help a learner most.

## Starting Point

```bash
cat polishing/tasks/expand-short-notes/progress.txt
```

Find the first entry file that starts with that number.

## Priority Mode (Optional)

If a priority file exists, process entries in priority order instead of sequentially by ID:

```bash
ls polishing/priority/notes.txt 2>/dev/null
```

**If the file exists**:
1. Read the priority file to get the ordered list of entry IDs
2. Find your current position: check `polishing/tasks/expand-short-notes/progress.txt` for the last processed entry
3. Skip any entries in the priority list that come before your last processed entry
4. Process entries in priority file order (highest priority first)
5. Update `polishing/tasks/expand-short-notes/progress.txt` with the ID of the last entry processed

**If the file does not exist**: Fall back to sequential processing by ID.

**Regenerating priorities**: Run `python3 build/prioritize_polishing.py --task notes` to refresh the priority list.

## Workflow

1. **Read the progress file** to find the next entry to check

2. **Load the entry** and examine the notes field

3. **For each entry**:
   - Check note quality using `python3 build/score_note_quality.py --id ENTRY_ID` if available
   - Evaluate whether notes are adequate for the word type and tier
   - If notes are thin, missing key sections, or only have a single sentence: expand them
   - If notes are already adequate: skip (no change needed)

   When expanding: update the `modified` timestamp in metadata.

   **CRITICAL - Timestamp requirement**:
   ```bash
   # Run IMMEDIATELY BEFORE saving each modified entry
   python3 build/get_timestamp.py
   ```

4. **After every ~20 entries** (or when you make changes):
   - Update `polishing/tasks/expand-short-notes/progress.txt`
   - Validate and build:
     ```bash
     make build
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Expand short notes: entries XXXXX-XXXXX"
     ```
     **In parallel mode**: Replace `git add -A` with `git add entries/ polishing/sessions/` to avoid staging shared files.

5. **When finishing** (end of session or context getting long):
   a. Update `polishing/tasks/expand-short-notes/progress.txt`
   b. Write session log to `polishing/sessions/expand-short-notes_{date}_{nnn}.md`:
      ```
      ## Session: Expand Short Notes
      Date: YYYY-MM-DD
      Entries processed: XXXXX-XXXXX

      ### Entries Expanded
      - [entry_id]: [word] - [brief description of what was added]

      ### Entries Skipped
      [entries that already had adequate notes]

      ### Statistics
      - Entries completed this session: N
      - Total remaining: N

      ### Next Entry
      XXXXX
      ```
   c. Commit all changes

## Parallel Execution Mode

When running on a restricted ID range (e.g., "Process entries 10000-10499 only"):

1. **Only process entries in your assigned range**
2. **Do NOT run** `make build` or `python3 build/update_indexes.py`
3. **Stage only entry files and session logs**: `git add entries/ polishing/sessions/`
4. **Commit to your session branch** (not main)
5. After all parallel sessions complete, the coordinator merges and rebuilds

## Quality Guidelines

- All kanji in notes must have furigana: `{漢字|かんじ}`
- All explanations must be in English — Japanese text appears only in example phrases, patterns, and collocations
- Do not add inline word links (⟦...⟧) — those are added in a separate polishing step
- Keep notes focused and useful — avoid padding with obvious information
- Match the note style of well-written entries in the dictionary
