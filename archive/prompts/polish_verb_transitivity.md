# Polish Verb Transitivity

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

Add transitivity information to verb entries. This is a **semantic task** that requires
your knowledge of Japanese — determining whether a verb is transitive or intransitive
(and identifying its pair) requires understanding how the verb is actually used.

## Task Focus

**Three-part focus** for each verb entry:
1. Add `transitivity` tag to `metadata.tags` if missing
2. Add or verify TRANSITIVITY section in `notes` field
3. Look up and link the pair verb (transitive/intransitive counterpart) via `prominent_see_also`

## Starting Point

```bash
cat polishing/tasks/verb-transitivity/progress.txt
```

Read `entries_index.json` (or scan filesystem) to find the next verb entry at or after that ID number. Skip non-verb entries — only process entries whose `metadata.tags.pos` contains a `verb-*` tag.

## Workflow

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

## Common Transitivity Pairs

Reference table of common pairs for quick lookup:

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

## Verbs That Are Typically "both" or Special

- {吹|ふ}く — both (wind blows / person blows)
- {増|ふ}える/{増|ふ}やす — separate verbs but sometimes confused
- する-compound verbs — almost always transitive unless the base noun is inherently intransitive (e.g., {散歩|さんぽ}する is intransitive)

## Why This Cannot Be Fully Automated

- Determining transitivity requires understanding how the verb is actually used in Japanese
- Some verbs have shifted transitivity in modern usage
- Pair identification requires semantic knowledge (not just morphological pattern matching)
- する-compound verbs need individual assessment — some are transitive, some intransitive, some both
- Back-link verification requires reading the pair entry and judging whether existing references are correct

## Progress Update Format

```
next: XXXXX
```

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
1. Entry range checked
2. Number of verbs processed (how many had changes vs. already complete)
3. Number of pair links added (including back-links)
4. Any unusual cases encountered (verbs with ambiguous transitivity, missing pairs, etc.)
5. Next entry to continue from
