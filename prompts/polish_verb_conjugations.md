# Add Verb Conjugation Data

Systematically add the `conjugation` field to existing verb entries that are missing it. This is a **semantic task** that requires your knowledge of Japanese verb conjugation classes — it cannot be fully automated because:

- The `part_of_speech` field uses dozens of inconsistent formats across entries
- Correctly classifying godan vs ichidan requires understanding the verb (e.g., 帰る is godan despite ending in -iru)
- Stem extraction with correct furigana requires reading the headword carefully
- Irregular verbs need manual override identification
- する verb entries have many different POS labels that must be recognized

## Task Focus

**Single focus**: Add a correct `conjugation` field and `verb_class` tag to each verb entry.

## Reference Skill

Load the skill file for the complete specification:
```
.claude/skills/verb-conjugations/SKILL.md
```

## Tracking

Progress is tracked in:
```
polishing/tasks/verb-conjugations/progress.txt
```

Format: `next: XXXXX` — the next entry ID to process (entries are processed in ID order).

## Starting Point

```bash
cat polishing/tasks/verb-conjugations/progress.txt
```

## Workflow

1. **Read the tracking file** to find the starting entry ID

2. **Scan entries in ID order** from the starting point. For each entry:
   - Read the entry JSON
   - Skip if not a verb (check `part_of_speech` and `metadata.tags.pos` — look for any verb-related value)
   - Skip if `conjugation` field already exists
   - Otherwise, process it

3. **For each verb entry needing conjugation**, determine:

   a. **Verb class**: godan, ichidan, suru, kuru, or aru
      - Check `metadata.tags.verb_class` if present
      - Check `part_of_speech` for clues (many inconsistent formats exist)
      - Check the headword ending and your linguistic knowledge
      - **Ambiguous -ru verbs**: Use your knowledge. Common godan -ru verbs include: 帰る, 走る, 知る, 入る, 切る, 減る, 散る, 蹴る, 練る, 焦る, 滑る, 握る, 限る, etc.

   b. **Stem/ending/prefix**:
      - Godan: stem = headword minus final kana (with furigana); ending = final kana
      - Ichidan: stem = headword minus る (with furigana)
      - する: prefix = noun part before する (with furigana)
      - 来る: prefix = anything before 来る (often empty)

   c. **Irregularities**: Check if the verb needs overrides
      - 行く → irregular て/た forms
      - いらっしゃる, おっしゃる, くださる, なさる → irregular ます forms
      - ある → use type `"aru"`
      - くれる → irregular imperative (くれ not くれろ)
      - Any other verb with non-standard conjugation

4. **Add the conjugation field** to the entry JSON, placed after `gloss` and before `definitions`:
   ```json
   "conjugation": {
     "type": "godan",
     "ending": "つ",
     "stem": "{立|た}"
   },
   ```

5. **Add/verify the `verb_class` tag** in `metadata.tags`:
   ```json
   "verb_class": "godan-tsu"
   ```

6. **Update the `modified` timestamp**:
   ```bash
   python3 build/get_timestamp.py
   ```

7. **Verify**:
   ```bash
   python3 build/validate.py
   ```

8. **After every 20-30 entries**, commit:
   ```bash
   git add entries/
   git commit -m "Add verb conjugation data: XXXXX-XXXXX"
   ```

9. **Update the tracking file** with the next entry ID to process

10. **When finishing** (end of session or context getting long):
    a. Update tracking file with current progress
    b. Write session log to `polishing/sessions/verb-conjugations_{date}_{nnn}.md`:
       ```
       ## Session: Add Verb Conjugation Data
       Date: YYYY-MM-DD
       Entries processed: XXXXX-XXXXX (ID range scanned)

       ### Verbs Updated
       - [entry_id]: [headword] — [type] ([any notes about irregularities])

       ### Entries Skipped
       - Non-verb entries: N
       - Already had conjugation: N

       ### Statistics
       - Verb entries updated this session: N
       - Next entry ID: XXXXX

       ### Notes
       [Any issues encountered, ambiguous cases, etc.]
       ```
    c. Run validation and build:
       ```bash
       make build
       ```
    d. Commit all changes including build artifacts:
       ```bash
       git add -A && git commit -m "Add verb conjugation data: session YYYY-MM-DD"
       ```

## Common Part-of-Speech Patterns to Recognize

The POS field is inconsistent. Here are the major patterns that indicate a verb entry:

**Godan verbs**: "verb (godan)", "godan verb", "verb-godan", "verb, godan", "verb godan", "godan verb (transitive)", "verb (godan, transitive)", "verb (godan, intransitive)", "verb (五段, ...)"

**Ichidan verbs**: "verb (ichidan)", "ichidan verb", "verb-ichidan", "verb, ichidan", "verb ichidan", "ichidan verb (transitive)", "verb (ichidan, transitive)", "verb (一段, ...)"

**する verbs**: "noun, suru verb", "noun, verb (suru)", "noun, suru-verb", "noun / suru verb", "noun / suru-verb", "noun, verb-suru", "verb (suru)", "suru verb", "verb-suru", "noun, verb (する)", "noun / verb (する)", "suru-verb", "adverb, suru verb", "adverb, verb (suru)", "noun; suru verb", "noun; verb (suru)", "noun/suru-verb", "noun/suru verb", etc.

**来る verbs**: "verb-kuru", "verb (kuru compound)"

**Generic "verb"**: "verb" — must determine class from headword/reading

**Expression verbs**: "expression, verb phrase", "expression, verb (godan)", "expression / verb (ichidan)" — these are verb entries that need conjugation too

## Edge Cases

1. **Entries that are both noun and する verb** (e.g., "noun, suru verb"): Add conjugation with type `"suru"`. The noun sense doesn't conjugate, but the verb sense does.

2. **Expression entries containing verbs** (e.g., "expression, verb (godan)"): Add conjugation for the main verb.

3. **Compound verbs**: Treat the whole compound as the unit. For 食べ始める (ichidan), stem is `{食|た}べ{始|はじ}め`.

4. **Kana-only verbs**: Stem has no furigana notation needed. For する, prefix is `""`. For いる, stem is `い`.

5. **Verbs with multiple kanji**: Use the headword's kanji and furigana as-is. For 取り消す, stem is `{取|と}り{消|け}` and ending is `す`.

## Why This Cannot Be Fully Automated

- **POS field chaos**: Over 150 different POS string formats for verbs, with no reliable regex to parse them all
- **Godan vs ichidan ambiguity**: Verbs ending in -iru/-eru may be either class (帰る is godan, 食べる is ichidan)
- **Stem extraction**: Requires understanding which kanji map to which readings in compound words
- **Irregular identification**: Must know which verbs conjugate irregularly
- **Expression entries**: Judgment needed on whether/how to add conjugation to verb expressions

However, for any single verb, the correct conjugation data is deterministic once the class is known. The semantic knowledge is in the classification step, not the form generation.

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow." The key points:

1. **Run `make build` BEFORE the final commit** so that `docs/` and all build artifacts are included
2. **`git add -A`** to stage everything (entries, docs, indexes, tracking file, session log, etc.)
3. **Commit and push** to the feature branch
4. **Create a PR** for the branch
5. **Poll CI status** every 60 seconds until all checks pass (allow up to 10 minutes)
6. **Squash-merge the PR** once all checks are green
7. **If CI fails**: read the error, fix the issue, push again, and repeat from step 5
8. **Post-merge cleanup**: switch to main, pull, verify clean state, delete feature branch locally and remotely

**CRITICAL**: The PR must include rebuilt `docs/` files. If you commit entry changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.
