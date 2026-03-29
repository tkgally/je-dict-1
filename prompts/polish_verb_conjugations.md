# Add Verb Conjugation Data

Systematically add the `conjugation` field to existing verb entries that are missing it.

## Batch Processing Script

A helper script exists at `build/add_conjugations.py` that handles the vast majority of entries automatically. It:

- Identifies verb entries via POS string and `metadata.tags.pos` array
- Determines verb class (godan/ichidan/suru/kuru/aru) from POS, tags, and reading
- Extracts stems/endings/prefixes from headwords
- Adds overrides for known irregular verbs (行く, くれる, いらっしゃる, etc.)
- Flags ambiguous cases for manual review

**Usage:**
```bash
# Dry run — see what would change without writing files
python3 build/add_conjugations.py --start 1 --end 21000 --dry-run

# Process entries (writes files)
python3 build/add_conjugations.py --start 1 --end 21000
```

The script is safe to re-run: it skips entries that already have a `conjugation` field. Run it in ID-range batches (e.g., 2000 at a time) and commit between batches.

**After the script finishes**, review flagged entries manually and validate:
```bash
python3 build/validate.py
```

## Manual Review Required For

The script flags entries it cannot classify. These require manual attention:

1. **Ambiguous -iru/-eru godan verbs** not in the known-godan list (script defaults -eru to ichidan, which is correct ~95% of the time)
2. **Entries with unusual POS formats** not yet handled by the script
3. **Proverb/expression entries** — the script may flag these; most should NOT get conjugation

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

2. **Run `build/add_conjugations.py`** for the target ID range to handle the bulk automatically:
   ```bash
   python3 build/add_conjugations.py --start XXXXX --end YYYYY --dry-run  # preview
   python3 build/add_conjugations.py --start XXXXX --end YYYYY            # execute
   ```

3. **Review flagged entries** from the script output. For each flagged entry, manually determine:

   a. **Should it get conjugation?**
      - YES for verbs, verb phrases, auxiliary verbs
      - NO for proverbs, ている-form expressions, noun forms of verbs (e.g., 申し送り)

   b. **Verb class** (if yes): godan, ichidan, suru, kuru, or aru
      - **Ambiguous -ru verbs**: Use your knowledge. Common godan -ru verbs include: 帰る, 走る, 知る, 入る, 切る, 減る, 散る, 蹴る, 練る, 焦る, 滑る, 握る, 限る, etc.

   c. **Irregularities**: Check if the verb needs overrides (see skill file)

4. **Validate**:
   ```bash
   python3 build/validate.py
   ```

5. **Commit in batches** (every ~500-1000 entries by ID range):
   ```bash
   git add entries/
   git commit -m "Add verb conjugation data: XXXXX-YYYYY"
   ```

6. **Update the tracking file** with the next entry ID to process

7. **When finishing** (end of session or context getting long):
    a. Update tracking file with current progress
    b. Write session log to `polishing/sessions/verb-conjugations_{date}_{nnn}.md`:
       ```
       ## Session: Add Verb Conjugation Data
       Date: YYYY-MM-DD
       Entries processed: XXXXX-XXXXX (ID range scanned)

       ### Statistics
       - Verb entries updated this session: N
       - Flagged entries reviewed manually: N
       - Next entry ID: XXXXX

       ### Notes
       [Any issues encountered, new POS patterns discovered, etc.]
       ```
    c. Run validation and build:
       ```bash
       make build
       ```
    d. Commit all changes including build artifacts:
       ```bash
       git add -A && git commit -m "Add verb conjugation data: session YYYY-MM-DD"
       ```

## POS Detection: Known Pitfalls

When checking POS strings for "verb", be careful:

- **"adverb" contains "verb"** — use word-boundary-aware matching (e.g., regex `(?<!ad)verb`) to avoid false positives on adverbs, which are common in this dictionary
- **"noun (verbal)"** — indicates a する noun; treat as suru verb
- **"noun; noun (する)"** — another する noun variant
- **"noun, する-verb"** — full-width する character
- **Plain "noun" with `verb-suru` in `metadata.tags.pos`** — many entries have POS="noun" but their tags array contains "verb-suru"; check BOTH sources
- **"expression, verb phrase"** — these ARE verbs (e.g., 頭を抱える); add ichidan/godan conjugation for the main verb
- **"auxiliary verb"** — verbs like ～続ける should get conjugation
- **"expression (proverb)"** / **"proverb"** — these should NOT get conjugation
- **"expression (verb て-form + いる)"** — already conjugated ている forms (e.g., 空いている, 混んでいる); skip these

## Noun Forms of Verbs

Some entries have a verb-like POS (e.g., "noun, godan verb") but the headword is the **noun form** (連用形), not the dictionary form:
- 申し送り (もうしおくり) — ends in り, not る
- 仕送り, 手渡し, 逆戻り, etc.

**Guard**: Before adding godan conjugation, verify the reading ends in a valid godan ending kana (うくぐすつぬぶむる). If it ends in い, り, し, etc., it's likely a noun form and should be skipped.

## Edge Cases

1. **Entries that are both noun and する verb** (e.g., "noun, suru verb"): Add conjugation with type `"suru"`. The noun sense doesn't conjugate, but the verb sense does. The prefix is the headword itself (without する).

2. **Expression entries containing verbs** (e.g., "expression, verb (godan)"): Add conjugation for the main verb. The stem is everything before the final kana.

3. **Verb phrase expressions** (e.g., 頭を抱える): The entire phrase is the stem. For ichidan, stem = headword minus る.

4. **Compound verbs**: Treat the whole compound as the unit. For 食べ始める (ichidan), stem is `{食|た}べ{始|はじ}め`.

5. **Kana-only verbs**: Stem has no furigana notation needed. For する, prefix is `""`. For いる, stem is `い`.

6. **Verbs with multiple kanji**: Use the headword's kanji and furigana as-is. For 取り消す, stem is `{取|と}り{消|け}` and ending is `す`.

7. **Proverbs**: Do NOT add conjugation. Even if they contain verbs (猿も木から落ちる), these are fixed expressions.

8. **ている expressions**: Do NOT add conjugation. Entries like 空いている and 混んでいる are already in a specific conjugated form.

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
