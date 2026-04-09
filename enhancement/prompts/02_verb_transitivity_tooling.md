# 02 — Verb Transitivity Tooling

**Enhancement plan section**: [1.1.1] Verb Transitivity Completion Campaign

## What This Prompt Creates/Modifies

| Action | File |
|--------|------|
| **Create** | `build/find_missing_transitivity.py` — detection script for verbs missing transitivity data |
| **Create** | `prompts/polish_verb_transitivity.md` — polishing prompt for adding transitivity info |
| **Create** | `polishing/tasks/verb-transitivity/progress.txt` — progress tracking for the polishing task |
| **Modify** | `CLAUDE.md` — add `find_missing_transitivity.py` to Essential Commands |
| **Modify** | `.claude/skills/verb-entry/SKILL.md` — verify/strengthen transitivity tag documentation |

---

## Part A: Build the Detection Script

Create `build/find_missing_transitivity.py`. Follow the patterns established by `build/find_missing_furigana.py` and `build/find_merge_candidates.py` — use the same project structure conventions (SCRIPT_DIR, PROJECT_ROOT, entries directory scanning).

### Requirements

The script must:

1. **Load entries** by scanning entry JSON files in `entries/` (preferred for accuracy) or loading `entries_index.json`. Since the index may not contain all tag detail, scan the actual JSON files.

2. **Identify all verb entries** where `metadata.tags.pos` contains any of:
   - `verb-godan`
   - `verb-ichidan`
   - `verb-suru`
   - `verb-kuru`
   - `verb-irregular`

3. **For each verb, check three things**:
   - **Tag present?** Does `metadata.tags` have a `transitivity` field with a non-null value (`"transitive"`, `"intransitive"`, or `"both"`)?
   - **Notes mention?** Does the `notes` field contain `自動詞` or `他動詞` (or the TRANSITIVITY: header)?
   - **Pair linked?** Does the entry have a `prominent_see_also` entry, or a `cross_references` entry with type `"pair"`, suggesting a transitive/intransitive pair verb is linked?

4. **Classify each verb into one of**:
   - **Complete**: Has transitivity tag AND notes mention AND pair link (or is inherently unpaired, e.g., `verb-suru` compound verbs which are typically only transitive)
   - **Partial**: Has some but not all of the above
   - **Missing**: Has none of the above

5. **Output a report** (to stdout by default):
   ```
   === Verb Transitivity Report ===

   Total verbs: NNNN
   With transitivity tag: NNNN (NN.N%)
   With transitivity in notes: NNNN (NN.N%)
   With pair link: NNNN (NN.N%)
   Fully complete: NNNN (NN.N%)
   Missing (no transitivity data at all): NNNN (NN.N%)

   --- By Tier ---
   basic:   NNN verbs, NNN missing (NN.N%)
   core:    NNN verbs, NNN missing (NN.N%)
   general: NNNN verbs, NNNN missing (NN.N%)

   --- Verbs Missing Transitivity (sorted by tier priority) ---
   [id] [headword] [reading] [tier] [what's missing: tag/notes/pair]
   ...
   ```

6. **Support these command-line flags**:
   - `--tier basic|core|general` — filter output to only one tier
   - `--limit N` — limit the number of entries in the missing list (default: show all)
   - `--json` — output machine-readable JSON instead of the text report
   - `--missing-only` — only print the list of verbs missing transitivity (skip summary stats)

### Implementation notes

- Add `#!/usr/bin/env python3` and a module docstring with usage examples
- Use `argparse` for flag handling
- Use `pathlib.Path` for all file paths
- Import from `japanese_utils` if you need `strip_furigana`
- Add `sys.path.insert(0, str(SCRIPT_DIR))` so imports from the build directory work
- Sort output: basic tier first, then core, then general; within each tier sort by numeric ID
- For the `--json` flag, output a JSON object with keys `summary` (the statistics) and `entries` (the list)
- Status messages (like "Scanning entries...") go to stderr; report output goes to stdout
- The script should work correctly even if `entries_index.json` is stale — prefer scanning the filesystem

### Verification

After creating the script, run:

```bash
python3 build/find_missing_transitivity.py --limit 20
```

Verify the output is sensible — there should be verb entries missing transitivity data. If the script produces an error, fix it before proceeding.

Also run:

```bash
python3 build/find_missing_transitivity.py --json --limit 5 | python3 -m json.tool
```

Verify the JSON output is valid and well-structured.

---

## Part B: Create the Polishing Prompt

Create `prompts/polish_verb_transitivity.md` following the exact structure of existing polishing prompts (use `prompts/polish_furigana_completeness.md` and `prompts/polish_semantic_labels.md` as templates).

### Full content of the polishing prompt

The prompt must include all of the following sections:

#### Title and task description

```
# Polish Verb Transitivity

Add transitivity information to verb entries. This is a **semantic task** that requires
your knowledge of Japanese — determining whether a verb is transitive or intransitive
(and identifying its pair) requires understanding how the verb is actually used.
```

#### Task focus

**Three-part focus** for each verb entry:
1. Add `transitivity` tag to `metadata.tags` if missing
2. Add or verify TRANSITIVITY section in `notes` field
3. Look up and link the pair verb (transitive/intransitive counterpart) via `prominent_see_also`

#### Starting point

```bash
cat polishing/tasks/verb-transitivity/progress.txt
```

Read `entries_index.json` (or scan filesystem) to find the next verb entry at or after that ID number. Skip non-verb entries — only process entries whose `metadata.tags.pos` contains a `verb-*` tag.

#### Workflow (detailed step-by-step)

1. **Read the progress file** to find the starting ID.

2. **For each verb entry** (in ID order, skipping non-verbs):

   a. **Determine transitivity**: Using your knowledge of Japanese, classify the verb as:
      - `"transitive"` ({他動詞|たどうし}) — takes a direct object with を
      - `"intransitive"` ({自動詞|じどうし}) — subject marked with が, no direct object
      - `"both"` — genuinely usable as both (rare; e.g., {吹|ふ}く can be both)

   b. **Add the `transitivity` tag** to `metadata.tags` if missing or null:
      ```json
      "tags": {
        "pos": ["verb-godan"],
        "transitivity": "transitive",
        ...
      }
      ```

   c. **Add or verify the TRANSITIVITY section in notes**. If the notes field already contains a TRANSITIVITY section, verify it is correct. If not present, add it. The format is:
      ```
      TRANSITIVITY:
      - Type: {他動詞|たどうし} (transitive)
      - Pair: {開|あ}く (intransitive)
      - Pattern: [noun]を{開|あ}ける
      ```
      If no pair exists (e.g., many する-verbs), write:
      ```
      TRANSITIVITY:
      - Type: {他動詞|たどうし} (transitive)
      - No standard intransitive pair
      - Pattern: [noun]を[verb]
      ```
      Place the TRANSITIVITY section near the top of notes, after any opening sentence but before ASPECT, COMMON PATTERNS, or other sections.

   d. **Look up the pair verb** in the dictionary:
      - If the pair verb exists as an entry, add a `prominent_see_also` reference:
        ```json
        "prominent_see_also": [
          {
            "target_id": "XXXXX_reading",
            "reading": "あく",
            "headword": "{開|あ}く",
            "note": "intransitive"
          }
        ]
        ```
      - **Verify the back-link**: Open the pair verb's entry and ensure it has a reciprocal `prominent_see_also` pointing back. If missing, add it.
      - For the `note` field, use `"transitive"` or `"intransitive"` to indicate what the *target* entry is.
      - If the pair verb does not exist in the dictionary, do NOT add a broken link. Instead, note in the TRANSITIVITY section that the pair is not yet in the dictionary.

   e. **Update the `modified` timestamp**:
      ```bash
      python3 build/get_timestamp.py
      ```
      Run this immediately before saving each modified entry. Set `metadata.modified` to the returned value.

   f. **If the entry already has complete transitivity data** (tag present, notes correct, pair linked correctly): skip it and move to the next verb.

3. **After every ~25 entries**:
   - Update `polishing/tasks/verb-transitivity/progress.txt` with the next entry number
   - Validate and build:
     ```bash
     make build
     ```
   - Commit changes:
     ```bash
     git add -A && git commit -m "Verb transitivity: entries XXXXX-XXXXX"
     ```

4. **When finishing** (end of session or context getting long):
   a. Update `polishing/tasks/verb-transitivity/progress.txt`
   b. Write session log to `polishing/sessions/verb-transitivity_{date}_{nnn}.md`:
      ```
      ## Session: Verb Transitivity
      Date: YYYY-MM-DD
      Entries checked: XXXXX-XXXXX (NNN verbs processed)

      ### Changes Made
      - [entry_id] [headword]: Added transitivity tag ([value]), linked pair [pair_headword]
      - [entry_id] [headword]: Added transitivity tag ([value]), no pair exists
      - [entry_id] [headword]: Added back-link from pair [pair_id]

      ### Already Complete
      - NNN entries already had full transitivity data

      ### Next Entry
      XXXXX
      ```
   c. Commit all changes

#### Common transitivity pairs to know

Include a reference table of common pairs for quick lookup:

| Intransitive ({自動詞|じどうし}) | Transitive ({他動詞|たどうし}) | Pattern |
|---|---|---|
| {開|あ}く | {開|あ}ける | -ku / -keru |
| {閉|し}まる | {閉|し}める | -maru / -meru |
| {始|はじ}まる | {始|はじ}める | -maru / -meru |
| {終|お}わる | {終|お}える | -waru / -eru |
| {出|で}る | {出|だ}す | -ru / -su |
| {入|はい}る | {入|い}れる | -ru / -reru |
| {付|つ}く | {付|つ}ける | -ku / -keru |
| {消|き}える | {消|け}す | -eru / -su |
| {割|わ}れる | {割|わ}る | -reru / -ru |
| {壊|こわ}れる | {壊|こわ}す | -reru / -su |
| {決|き}まる | {決|き}める | -maru / -meru |
| {変|か}わる | {変|か}える | -waru / -eru |
| {集|あつ}まる | {集|あつ}める | -maru / -meru |
| {止|と}まる | {止|と}める | -maru / -meru |
| {上|あ}がる | {上|あ}げる | -garu / -geru |
| {下|さ}がる | {下|さ}げる | -garu / -geru |
| {見|み}つかる | {見|み}つける | -karu / -keru |
| {落|お}ちる | {落|お}とす | -chiru / -tosu |
| {育|そだ}つ | {育|そだ}てる | -tsu / -teru |
| {治|なお}る | {治|なお}す | -ru / -su |

#### Verbs that are typically "both" or special

- {吹|ふ}く — both (wind blows / person blows)
- {増|ふ}える/{増|ふ}やす — separate verbs but sometimes confused
- する-compound verbs — almost always transitive unless the base noun is inherently intransitive (e.g., {散歩|さんぽ}する is intransitive)

#### Why this cannot be fully automated

- Determining transitivity requires understanding how the verb is actually used in Japanese
- Some verbs have shifted transitivity in modern usage
- Pair identification requires semantic knowledge (not just morphological pattern matching)
- する-compound verbs need individual assessment — some are transitive, some intransitive, some both
- Back-link verification requires reading the pair entry and judging whether existing references are correct

#### Progress update format

```
next: XXXXX
```

#### PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow." The key points:

1. **Run `make build` BEFORE the final commit** so that `docs/` and all build artifacts are included
2. **`git add -A`** to stage everything (entries, docs, indexes, kanji, progress file, session log, etc.)
3. **Commit and push** to the feature branch
4. **Create a PR** for the branch
5. **Poll CI status** every 60 seconds until all checks pass (allow up to 10 minutes)
6. **Squash-merge the PR** once all checks are green
7. **If CI fails**: read the error, fix the issue, push again, and repeat from step 5
8. **Post-merge cleanup**: switch to main, pull, verify clean state, delete feature branch locally and remotely

**CRITICAL**: The PR must include rebuilt `docs/` files. If you commit entry changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.

#### Output at session end

When stopping, report:
1. Entry range checked
2. Number of verbs processed (how many had changes vs. already complete)
3. Number of pair links added (including back-links)
4. Any unusual cases encountered (verbs with ambiguous transitivity, missing pairs, etc.)
5. Next entry to continue from

---

## Part C: Initialize Tracking

### 1. Create the progress file

```bash
mkdir -p polishing/tasks/verb-transitivity
```

Write `polishing/tasks/verb-transitivity/progress.txt` with content:
```
next: 00001
```

### 2. Verify the detection script works

```bash
python3 build/find_missing_transitivity.py --limit 20
```

Review the output. There should be verbs listed as missing transitivity data. If the output is empty or an error occurs, debug and fix before continuing.

Also run:
```bash
python3 build/find_missing_transitivity.py --json --limit 5 | python3 -m json.tool
```

Verify the JSON is valid.

### 3. Add to CLAUDE.md Essential Commands

In `CLAUDE.md`, find the `## Essential commands` section. Within the existing comment groups, add `find_missing_transitivity.py` in a logical location. Add it after the "Entry consolidation" group and before the "Reports" group, as a new group:

```bash
# Verb transitivity
python3 build/find_missing_transitivity.py              # Report on verbs missing transitivity data
python3 build/find_missing_transitivity.py --tier basic  # Filter to one tier
python3 build/find_missing_transitivity.py --json        # Machine-readable output
```

Also add a reference in the "Project structure" section under `build/` if there is a natural place for it, next to the other `find_*.py` scripts.

---

## Part D: Update verb-entry Skill

Read `.claude/skills/verb-entry/SKILL.md` carefully. Check:

1. **Is the `transitivity` tag clearly documented as REQUIRED in `metadata.tags`?**
   - It should be listed in the "Required Tags for Verbs" section with the three valid values: `"transitive"`, `"intransitive"`, `"both"`
   - If already documented, no changes needed

2. **Does the TRANSITIVITY notes section format match what the polishing prompt expects?**
   - The skill should show the same TRANSITIVITY: format used in the polishing prompt
   - The skill currently shows this format in section "1. Transitivity Information" — verify it is consistent

3. **Is `prominent_see_also` mentioned as the correct mechanism for pair links?**
   - The skill should clearly state that transitive/intransitive pairs use `prominent_see_also`, NOT `cross_references`
   - If this is not explicit, add a note

4. **If any of the above is missing or unclear**, make targeted edits to `.claude/skills/verb-entry/SKILL.md`. Do not rewrite the entire file — only add or clarify what is needed.

---

## Final Steps

### Validate

```bash
make validate
```

Fix any validation errors before proceeding.

### Branch, commit, and PR

```bash
git checkout -b enhancement/verb-transitivity-tooling
git add -A
git commit -m "Add verb transitivity detection script and polishing prompt

- Create build/find_missing_transitivity.py for detecting verbs missing transitivity data
- Create prompts/polish_verb_transitivity.md for the polishing workflow
- Initialize polishing/tasks/verb-transitivity/progress.txt
- Add find_missing_transitivity.py to CLAUDE.md essential commands
- Verify verb-entry skill transitivity documentation

Implements enhancement plan [1.1.1] Verb Transitivity Completion Campaign."
git push -u origin enhancement/verb-transitivity-tooling
```

### PR, CI, and merge

```bash
gh pr create --repo tkgally/je-dict-1 \
  --head enhancement/verb-transitivity-tooling \
  --base main \
  --title "Add verb transitivity detection script and polishing prompt" \
  --body "$(cat <<'EOF'
## Summary
- Create `build/find_missing_transitivity.py` to scan verbs for missing transitivity tags, notes, and pair links
- Create `prompts/polish_verb_transitivity.md` polishing prompt with progress tracking
- Initialize `polishing/tasks/verb-transitivity/progress.txt`
- Add script to CLAUDE.md essential commands
- Verify verb-entry skill documentation

Implements enhancement plan [1.1.1] Verb Transitivity Completion Campaign.
EOF
)"
```

Poll CI every 60 seconds (up to 10 minutes):
```bash
gh pr checks <PR_NUMBER> --repo tkgally/je-dict-1
```

Once all checks pass:
```bash
gh pr merge <PR_NUMBER> --repo tkgally/je-dict-1 --squash
```

If CI fails: read logs with `gh run view <run_id> --repo tkgally/je-dict-1 --log-failed`, fix, push, repeat.

### Post-merge cleanup

```bash
git checkout main && git pull origin main
git status                                       # Should show nothing to commit
git branch -d enhancement/verb-transitivity-tooling
git push origin --delete enhancement/verb-transitivity-tooling
```
