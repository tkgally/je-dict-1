# Consolidate Dictionary Entries

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

Review the dictionary for entries that should be merged and candidates that should be removed as variants of existing entries. This is a **semantic task** — the detection script finds candidates deterministically, but you must judge each case using your knowledge of Japanese.

## Load the Skill

Load the `consolidate-entries` skill for detailed guidelines on merge decisions.

## Session Workflow

### Phase 1: Run Detection

```bash
python3 build/find_merge_candidates.py
```

This produces a report with:
- **Potential merges**: Entries with the same reading that may be the same word written differently
- **Candidate duplicates**: Candidates that may be spelling variants of existing entries
- **Missing cross-references**: Entry pairs that should reference each other (handled by a separate prompt)
- **Duplicate numeric IDs**: Entries sharing the same 5-digit number (handled by a separate prompt)

Focus on **potential merges** and **candidate duplicates** in this session.

### Phase 2: Evaluate Potential Merges

For each potential merge flagged by the script:

1. **Read both entries** in full — not just the headword and gloss
2. **Apply the semantic decision framework** from the skill:
   - Same POS? Same core meaning? Is the kanji distinction meaningful?
3. **Decide**: MERGE, KEEP SEPARATE (add cross-refs), or DISMISS (false positive)
4. **Record your decision** in the session log

#### If MERGE:
- Choose the keeper (prefer kanji form, better content, lower ID)
- Transfer unique content from the entry being deleted
- Update the keeper's `modified` timestamp: `python3 build/get_timestamp.py`
- Delete the duplicate entry file
- Search for and update any cross-references to the deleted entry:
  ```bash
  grep -r "deleted_entry_id" entries/ --include="*.json"
  ```

#### If KEEP SEPARATE:
- Verify both entries have `prominent_see_also` or `cross_references` pointing to each other
- Add cross-references if missing

#### If DISMISS:
- Note in the session log that this was evaluated and is a false positive

### Phase 3: Evaluate Candidate Duplicates

For each candidate flagged as a potential variant of an existing entry:

1. **Read the existing entry** to understand what it covers
2. **Compare** with the candidate word — is it the same lexical item?
3. If YES: Remove the candidate:
   ```bash
   python3 build/manage_candidates.py remove "word" "reading"
   ```
4. If NO: Keep the candidate (it's a genuinely different word)

### Phase 4: Validate and Build

After all changes:

```bash
python3 build/validate.py
python3 build/update_indexes.py
python3 build/build_flat.py
```

### Phase 5: Commit

```bash
git add -A && git commit -m "Consolidate entries: merge N entries, remove N candidates"
```

## Batch Size

Process all flagged items in one session if possible. If the list is very long, process in batches of ~20 and commit after each batch.

## Session Log

Write a session log to `polishing/sessions/consolidate_{date}.md`:

```markdown
## Session: Entry Consolidation
Date: YYYY-MM-DD

### Merges Performed
- Merged [deleted_id] into [keeper_id]: [reason]
- ...

### Entries Kept Separate
- [id1] / [id2]: [reason for keeping separate, cross-refs added]
- ...

### Candidates Removed
- [word] ([reading]): variant of [entry_id]
- ...

### False Positives Dismissed
- [reading]: [id1] / [id2] - [reason this is not a merge candidate]
- ...
```

## Important Reminders

- **Never merge entries purely based on shared reading** — semantic judgment is essential
- **Homophones with different kanji that signal different meanings are NOT merge candidates**
- **Noun + する pairs are NOT merge candidates** — they should be kept as separate entries with cross-references
- After deleting an entry, always search for references to it and update them
- **Never renumber existing entries** during merging — keep the keeper's original ID
