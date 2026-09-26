# Add Cross-References

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

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

The tracking file contains all general tier entries sorted by numeric ID. Basic and core tier entries were completed in earlier sessions and have been removed from the tracking file.

## Starting Point

```bash
grep "^pending" prompts/add-cross-references-tracking.txt | head -1
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

## Cluster Mode (Alternative Workflow)

Instead of processing entries one at a time by sequential ID, you can process **semantic clusters together**. This is more efficient for ensuring symmetric linking because you handle both sides of a relationship in the same batch.

### When to use Cluster Mode

Use cluster mode when:
- The asymmetry report shows many one-way references: `python3 build/find_merge_candidates.py --asymmetry-only`
- The cluster linter flags incomplete groups: `python3 build/check_semantic_clusters.py`
- You want to focus on a specific relationship type (transitivity, antonyms, keigo)

### Cluster Mode Workflow

1. **Generate a cluster report**:
   ```bash
   python3 build/check_semantic_clusters.py --type transitivity
   # or: --type antonym, --type keigo
   ```

2. **Pick a cluster** from the report (e.g., a transitivity pair with a missing link).

3. **Load all entries in the cluster** simultaneously (typically 2-5 entries):
   - Read each entry's full JSON
   - Map out all existing cross-references between cluster members

4. **Fix all links within the cluster**:
   - Add missing `prominent_see_also` links (transitivity pairs, homophones)
   - Add missing `cross_references` links (antonyms, keigo)
   - Ensure every link is bidirectional where required
   - Normalize relationship labels across the cluster (e.g., both sides of an antonym pair should use the same label format)

5. **Update timestamps** on all modified entries.

6. **Move to the next cluster** from the report.

### Cluster size guidelines

- **Transitivity pairs**: 2 entries per cluster
- **Antonym pairs**: 2 entries per cluster
- **Keigo groups**: 2-5 entries per cluster (plain + honorific + humble + any variants)
- **Homophone groups**: 2-4 entries per cluster

Process 5-10 clusters per commit batch (roughly 10-20 entries total).

## Batch Commits

After every 10-15 entries:

```bash
make build
git add -A && git commit -m "Add cross-references: XXXXX-XXXXX"
```
**In parallel mode**: Replace `git add -A` with `git add entries/ polishing/sessions/` to avoid staging shared files.

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
7. Estimated remaining general tier entries
8. If using cluster mode: number of clusters processed, cluster types

## Parallel Execution Mode

This task supports parallel execution when given an explicit ID range. Two or more sessions can run this task simultaneously on non-overlapping ID ranges.

### How to invoke

When starting the session, specify a range:
> "Process entries 10000-10499 only."

### Behavior in parallel mode

When an ID range is given:
1. **Ignore** the tracking file — do not read it or update it
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

Operate in **legacy sequential mode**: read the tracking file, process entries sequentially from that point, update the tracking file, and run `make build` as usual. This is the default behavior.

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow." The key points:

1. **Run `make build` BEFORE the final commit** so that `docs/` and all build artifacts are included
2. **`git add -A`** to stage everything (entries, docs, indexes, kanji, tracking file, session log, etc.)
3. **Commit and push** to the feature branch
4. **Create a PR** for the branch
5. **Wait for CI** with a single blocking call: `gh pr checks <number> --repo tkgally/je-dict-1 --watch --fail-fast` (exits 0 on success, non-zero on failure). Do NOT wrap this in a `while`/`sleep`/`curl` polling loop — `--watch` already waits, and hand-rolled streaming loops get routed through the `Monitor` tool (separate permission grant) which will deadlock an unattended session.
6. **Squash-merge the PR** once all checks are green
7. **If CI fails**: read the error, fix the issue, push again, and repeat from step 5
8. **Post-merge cleanup**: switch to main, pull, verify clean state, delete feature branch locally and remotely

**CRITICAL**: The PR must include rebuilt `docs/` files. If you commit entry changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.
