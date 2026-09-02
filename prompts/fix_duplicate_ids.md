# Fix Duplicate Numeric IDs

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

Identify and resolve entries that share the same 5-digit numeric ID prefix. Each entry must have a unique numeric ID because the ID forms part of the entry's URL on the live site.

## Background

Entry IDs follow the format `NNNNN_romaji` (e.g., `01234_taberu`). The 5-digit numeric prefix must be unique across the dictionary. Duplicate numeric IDs can occur when entries are created concurrently or when `get_next_id.py` is not used properly.

## Session Workflow

### Phase 1: Detect duplicates

```bash
python3 build/find_merge_candidates.py --dupid-only
```

This lists all groups of entries sharing the same numeric ID.

### Phase 2: For each duplicate group

1. **Read all entries** in the group to understand what they are
2. **Determine which entry keeps the ID** — prefer the entry that was created first (earlier `created` timestamp)
3. **Assign a new ID to the other entry(ies)**:
   ```bash
   python3 build/get_next_id.py
   ```
4. **Rename the file** to the new ID:
   - Calculate the new path: `python3 build/get_entry_path.py <reading> <new_id>`
   - Update the `id` field inside the JSON
   - Update all `id` fields in the `examples` array (they contain the entry ID prefix)
   - Move the file to the correct directory
5. **Update references** — search for the old ID and update:
   ```bash
   grep -r "old_id" entries/ --include="*.json"
   ```
   Update `target_id` fields in cross-references and inline word links pointing to the renamed entry.
6. **Update the `modified` timestamp**: `python3 build/get_timestamp.py`

### Phase 3: Validate and build

```bash
python3 build/validate.py
python3 build/update_indexes.py
python3 build/build_flat.py
```

### Phase 4: Commit

```bash
git add -A && git commit -m "Fix duplicate numeric IDs: reassign N entries"
```

## Important Notes

- **Never delete an entry** to resolve a duplicate ID — always reassign
- **The older entry keeps its ID** — this minimizes broken external links
- After renaming, the old URL will 404. This is acceptable because:
  - The entry is very recent (the duplicate was just created)
  - Search engines will re-index
  - The `entries_index.json` and site search will be updated by the build
- **Run `get_next_id.py` fresh** for each entry that needs a new ID — do not reuse previously obtained IDs
