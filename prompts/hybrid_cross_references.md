# Implement Hybrid Cross-Reference System

I want you to implement a hybrid cross-reference system for this Japanese dictionary project. The goal is to support both hard-coded entry IDs (for unambiguous resolution) and forward references (to entries that don't exist yet).

## Overview

Add an optional `target_id` field to cross-references. When present, it's the primary lookup. When absent, fall back to reading/headword resolution (the current system). This allows forward references to "harden" into ID-based references once the target entry is created.

## Data Structure

Update cross-references to support:

```json
{
  "type": "antonym",
  "target_id": "07159_yohaku",
  "reading": "よはく",
  "headword": "{余白|よはく}",
  "label": "margin"
}
```

## Resolution Logic

1. If `target_id` present AND entry exists → resolved (use ID)
2. If `target_id` present AND entry missing → ERROR (stale reference)
3. If no `target_id` → resolve by reading/headword (current behavior)
   - If found → valid, but could be hardened
   - If not found → pending forward reference

## Implementation Tasks

### 1. Update `build/schema.json`

Add `target_id` as an optional string field in the cross_references schema.

### 2. Create `build/harden_references.py`

New script that scans entries and adds `target_id` to resolvable cross-references:

- `--dry-run` (default): show what would change
- `--apply`: write changes to entry files
- `--id ENTRY_ID`: process single entry
- Skip ambiguous references (multiple matches, warn user)
- Skip unresolvable references (legitimate forward refs)

### 3. Update `build/validate.py`

- If `target_id` present: verify entry file exists, ERROR if not
- If no `target_id` but resolvable: WARNING that it can be hardened
- If no `target_id` and no `reading`: ERROR

### 4. Update `build/resolve_links.py`

- Check `target_id` first for direct resolution
- Fall back to reading/headword if no target_id
- The `resolved` and `target_id` fields in output should reflect actual resolution

### 5. Update `build/build_flat.py`

- When rendering cross-references, use `target_id` directly if present
- Fall back to current resolution logic otherwise

### 6. Update `build/extract_references.py`

- When extracting references from notes, attempt to resolve immediately
- If target exists, include `target_id` in the extracted reference
- If not, create forward reference (reading/headword only)

### 7. Update `.claude/skills/cross-reference-entry/SKILL.md`

Document:

- The new `target_id` field
- When to use target_id vs forward references
- The harden_references.py script
- Updated validation behavior

## Testing

After implementation:

1. Run `python build/harden_references.py` to see hardenable references
2. Run `python build/validate.py` to check for errors/warnings
3. Run `python build/build_flat.py` to verify HTML generation works
4. Verify a mix of:
   - References with target_id (should resolve directly)
   - Forward references without target_id (should show as pending)

## Constraints

- Maintain backward compatibility — existing references must continue working
- Do not modify any dictionary entry files except through harden_references.py --apply
- Follow existing code style in the build/ scripts
- Use the constants from build/constants.py for cross-reference types
