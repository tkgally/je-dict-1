# Add Cross-References

Systematically review dictionary entries and add or verify `prominent_see_also` and `cross_references` links. This is a **semantic task** that requires knowledge of Japanese vocabulary relationships — it cannot be automated because deciding which words should be cross-referenced requires understanding meaning, usage, and learner needs.

## Reference Skill

Load the cross-reference skill for detailed format and type requirements:
```
.claude/skills/cross-reference-entry/SKILL.md
```

## The Three Cross-Reference Mechanisms

1. **`prominent_see_also`** — Top-of-entry links displayed below the headword. Used for homophones, transitive/intransitive pairs, N/Nする pairs, informal/formal pairs, and other closely related word groups.

2. **`cross_references`** — "Related Words" box at the bottom. Used for antonyms, keigo, synonyms, contrasts, and other semantic relationships.

3. **Inline word links (⟦...⟧)** — Contextual links in example sentences and notes. **This task does NOT touch inline word links.**

## Tracking File

Progress is tracked in:
```
prompts/add-cross-references-tracking.txt
```

Format: `STATUS | ENTRY_ID | HEADWORD | TIER | POS`

Status values:
- `pending` — Not yet processed
- `in_progress` — Currently being worked on
- `completed` — Cross-references reviewed and updated
- `skipped` — Intentionally skipped (with reason noted in session log)

The tracking file is pre-populated with all basic and core tier entries. After those are exhausted, continue with general tier entries sequentially by numeric ID.

## Starting Point

```bash
grep "^pending" prompts/add-cross-references-tracking.txt | head -1
```

If all entries in the tracking file are completed, find the highest completed ID and continue with the next general-tier entry by ID:

```bash
# Find the next general entry to process
python3 -c "
import json
with open('entries_index.json') as f:
    idx = json.load(f)
# Get highest completed ID from tracking file
import re
max_id = 0
with open('prompts/add-cross-references-tracking.txt') as f:
    for line in f:
        if line.startswith('completed'):
            m = re.search(r'\| (\d{5})_', line)
            if m:
                max_id = max(max_id, int(m.group(1)))
# Find next general entry
entries = sorted(idx['entries'], key=lambda e: e['id'])
for e in entries:
    num = int(e['id'].split('_')[0])
    if num > max_id:
        print(f\"Next: {e['id']} | {e.get('headword','')} | {e.get('vocabulary_tier','')}\")
        break
"
```

## Workflow for Each Entry

### Step 1: Read the entry

Read the full entry JSON file. Note:
- Current `prominent_see_also` (if any)
- Current `cross_references` (if any)
- Part of speech, headword, reading, definitions
- Notes content (may mention related words)

### Step 2: Think about relationships

Consider what cross-references this entry should have:

**For `prominent_see_also`** (high-visibility, bidirectional):
- Does this word have a **transitive/intransitive pair**? (e.g., {開|あ}く ↔ {開|あ}ける)
- Is this a **noun with a する verb form** (or vice versa)? (e.g., {勉強|べんきょう} ↔ {勉強|べんきょう}する)
- Are there **homophones** that learners might confuse? (e.g., {聞|き}く ↔ {効|き}く)
- Is there an **informal/formal pair**? (e.g., うまい ↔ {美味|おい}しい)
- Any other **closely related words** learners would want to navigate between?

**For `cross_references`** (structured, at bottom of page):
- Does this word have a direct **antonym**?
- Does this word have **keigo** equivalents (honorific/humble forms)?
- Are there close **synonyms** with distinct nuance?
- Are there words often **contrasted** with this one?
- Are there **related** compounds or derived forms?

### Step 3: Verify existing references

Check any existing `prominent_see_also` and `cross_references`:
- Are they correct and appropriate?
- Are any `target_id` values stale (pointing to non-existent entries)?
- Can any unresolved references (no `target_id`) now be resolved because the target entry exists?
- **Migration check**: If there is a `pair`-type entry in `cross_references`, it should be removed and the relationship should be expressed via `prominent_see_also` instead. The `pair` type is deprecated.

### Step 4: Look up target entries

For each cross-reference you plan to add:

```bash
python3 build/check_duplicate.py "WORD" "READING"
```

- If the target entry exists: include `target_id` in the reference
- If the target entry does not exist: create a forward reference (reading + headword only, no `target_id`)

### Step 5: Update the starting entry

- Add new `prominent_see_also` entries
- Add new `cross_references` entries
- Remove or fix incorrect existing references
- Migrate any `pair`-type `cross_references` to `prominent_see_also`
- Resolve any previously unresolved references that can now be resolved
- Update the `modified` timestamp:
  ```bash
  python3 build/get_timestamp.py
  ```

### Step 6: Update target entries (back-links only)

For each cross-reference you added or modified on the starting entry, visit the target entry and consider whether it needs a **reciprocal back-link**:

- **Transitive/intransitive pairs**: Always add `prominent_see_also` both ways
- **N/Nする pairs**: Always add `prominent_see_also` both ways
- **Homophones**: Always add `prominent_see_also` both ways
- **Antonyms**: Usually add both ways
- **Keigo**: Usually add both ways
- **Synonyms, related, see_also**: Case-by-case — add if it genuinely helps the learner

**IMPORTANT**: When visiting target entries, ONLY add the reciprocal back-link to the starting entry. Do NOT do a full audit of the target entry's other cross-references — the target entry will get its own full audit when it comes up as a starting entry.

Update the `modified` timestamp on any target entry you modify.

### Step 7: Update tracking

Change the status in the tracking file from `pending` to `completed`.

### Step 8: Verify furigana

```bash
python3 build/verify_furigana.py ENTRY_ID
```

Fix any missing furigana before continuing.

## Batch Commits

After every 10-15 entries:

```bash
make build
git add -A && git commit -m "Add cross-references: XXXXX-XXXXX"
```

## When General Tier Entries Are Reached

Once all basic and core entries in the tracking file are completed, continue with general tier entries:

1. Find the next general entry by ID (see "Starting Point" above)
2. Process it using the same workflow
3. Append a `completed` line to the tracking file for each processed general entry:
   ```
   completed | XXXXX_word | {漢字|かな} | general | pos
   ```
4. Continue sequentially through general entries by ID

## Session End

When finishing (end of session or context getting long):

1. **Update tracking file** with current progress
2. **Run validation and build**:
   ```bash
   make build
   ```
3. **Write session log** to `polishing/sessions/add_cross_references_{date}_{nnn}.md`:
   ```markdown
   ## Session: Add Cross-References
   Date: YYYY-MM-DD

   ### prominent_see_also Added
   - [entry_id] ↔ [target_id]: [relationship type]
   - ...

   ### cross_references Added
   - [entry_id] → [target_id]: [type] - [description]
   - ...

   ### References Fixed/Migrated
   - [entry_id]: [what was changed and why]
   - ...

   ### Entries Skipped (if any)
   - [entry_id]: [reason]

   ### Statistics
   - Entries reviewed this session: N
   - prominent_see_also links added: N
   - cross_references links added: N
   - References fixed/migrated: N
   - Entry range: XXXXX through XXXXX

   ### Next Entry
   XXXXX
   ```
4. **Commit all changes** (entries, tracking file, session log, build artifacts)

## Output at Session End

Report:
1. Entry range processed
2. Number of entries reviewed
3. Number of prominent_see_also links added
4. Number of cross_references links added
5. Number of references fixed or migrated
6. Next entry to continue from
7. Estimated remaining entries (for basic/core phase)

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow." The key points:

1. **Run `make build` BEFORE the final commit** so that `docs/` and all build artifacts are included
2. **`git add -A`** to stage everything (entries, docs, indexes, kanji, tracking file, session log, etc.)
3. **Commit and push** to the feature branch
4. **Create a PR** for the branch
5. **Poll CI status** every 60 seconds until all checks pass (allow up to 10 minutes)
6. **Squash-merge the PR** once all checks are green
7. **If CI fails**: read the error, fix the issue, push again, and repeat from step 5
8. **Post-merge cleanup**: switch to main, pull, verify clean state, delete feature branch locally and remotely

**CRITICAL**: The PR must include rebuilt `docs/` files. If you commit entry changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.
