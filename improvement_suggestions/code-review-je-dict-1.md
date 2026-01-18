# Code Review: je-dict-1

**Date:** 2026-01-18
**Reviewer:** Claude Opus 4.5
**Project:** je-dict-1 - Japanese-English Learner's Dictionary Static Site Generator

## Overview

I've reviewed all Python scripts in `build/` and `scripts/`, the JSON schema, and the frontend JavaScript. Overall, this is a well-structured, thoughtfully designed codebase with good separation of concerns. The code is generally clean and readable. Below are the issues I found, organized by severity.

---

## Critical (must fix)

None found.

---

## High (should fix)

### 1. `build/japanese_utils.py:313` - `normalize_reading()` uses `.lower()` on Japanese text

**Problem:** The function calls `.lower()` on Japanese text at the end:
```python
return ''.join(result).lower()
```
Hiragana/katakana characters are not case-sensitive, so `.lower()` is a no-op for Japanese. However, if the string contains any Latin characters (which shouldn't happen for readings but could in edge cases), this would modify them.

**Impact:** Could cause subtle bugs if Latin characters appear in readings.

**Suggested fix:** Remove `.lower()` or explicitly handle only the conversion without it:
```python
return ''.join(result)
```

### 2. `build/schema.json:11` - ID pattern doesn't match all valid suffixes

**Problem:** The schema pattern `^[0-9]{5}_[a-z]+(_[a-z]+)?$` only allows lowercase letters in suffixes. Looking at the codebase, suffixes like `_chem` appear to be used for disambiguation (e.g., `kagaku_chem`), but this restricts to only one underscore-separated suffix.

**Impact:** If an entry needs multiple suffix segments or numeric suffixes, validation will fail.

**Suggested fix:** Consider whether the pattern should be more permissive: `^[0-9]{5}_[a-z]+(_[a-z0-9]+)*$`

### 3. `build/build_flat.py:2034` - Error message contains variable typo

**Problem:** The error message uses `{temp_dir}` without f-string prefix:
```python
print("  Build output remains in: {temp_dir}")
```

**Impact:** Error message won't show the actual temp directory path.

**Suggested fix:**
```python
print(f"  Build output remains in: {temp_dir}")
```

---

## Medium (consider fixing)

### 4. `build/validate.py:49-55` - Type annotation uses Python 3.9+ syntax

**Problem:** Uses `list[tuple[...]]` syntax for type hints in `ValidationResult` dataclass. This requires Python 3.9+ or `from __future__ import annotations`.

**Impact:** Won't work on Python 3.8.

**Suggested fix:** Either add `from __future__ import annotations` at the top, or use `List[Tuple[...]]` from typing module for compatibility.

### 5. `build/migrate_entries.py:140-145` - No deduplication check for `migrations` list

**Problem:** The `migrations` list is appended to in a loop without checking for duplicates. If the same file is somehow processed twice, it would appear twice.

**Impact:** Minor - mostly informational list, unlikely to have duplicates.

**Suggested fix:** Use a set or dict keyed by old_id.

### 6. `build/check_duplicate.py:95-109` and `build/manage_candidates.py:113-128` - Duplicate code

**Problem:** Both files contain nearly identical duplicate checking logic for entries and candidates. The code is duplicated rather than shared.

**Impact:** Maintenance burden - changes need to be made in two places.

**Suggested fix:** Extract the common logic into a shared module (perhaps `japanese_utils.py` or a new `duplicate_utils.py`).

### 7. `build/add_example_ids.py:87-93` - Uses `glob.glob` with nested patterns

**Problem:** The script searches for JSON files using two separate glob patterns:
```python
pattern = os.path.join(entries_dir, '*', '*.json')
pattern2 = os.path.join(entries_dir, '*', '*', '*.json')
```

**Impact:** This is fragile - if directory structure changes or nesting increases, the script will miss files.

**Suggested fix:** Use `pathlib.Path.rglob('*.json')` like other scripts do:
```python
from pathlib import Path
entries_dir = Path(__file__).parent.parent / 'entries'
files = list(entries_dir.rglob('*.json'))
```

### 8. `docs/search.js:74-80` - Uses `innerHTML` with potentially unescaped content

**Problem:** The search results are built using string concatenation and assigned via `innerHTML`:
```javascript
resultsList.innerHTML = results.map(function(entry) {
    return '<a href="entries/' + dirRange + '/' + entry.id + '.html" class="result-item">' +
        '<div class="result-headword">' + entry.headword + '</div>' + ...
```

**Impact:** XSS risk if entry data contains malicious HTML. However, the index generation in `build_flat.py:850-857` does HTML-escape the data, mitigating this risk.

**Note:** This is mitigated by proper escaping during index generation. No change needed.

### 9. `build/path_utils.py:36-46` - `get_numeric_id()` has fallback for old format

**Problem:** The function has fallback logic for an old ID format (`romaji_number`) that appears to no longer be used after migration:
```python
# Handle old format (romaji_number) during migration
if len(parts) >= 2:
    try:
        return int(parts[1])
```

**Impact:** Dead code that could be removed after confirming all entries are migrated.

**Suggested fix:** Remove the old format fallback after verifying migration is complete.

---

## Low (nice to have)

### 10. `build/build_flat.py` - `generate_search_js()` generates JS that's also stored in `docs/search.js`

**Problem:** The same JavaScript code exists both in `generate_search_js()` (lines 497-596) and as a standalone file `docs/search.js`. These can drift out of sync.

**Impact:** Maintenance confusion if files diverge.

**Suggested fix:** Either generate `search.js` from the function or remove the generation function and always use the standalone file.

### 11. `build/get_entry_path.py:86-91` - Validation doesn't handle all valid ID formats

**Problem:** The validation checks for exactly 2 parts:
```python
if len(parts) != 2:
    print(f"Error: Invalid entry ID format: '{entry_id}'")
```
But the schema allows for suffixes like `00001_taberu_v2`, which would have 3 parts.

**Impact:** Script would incorrectly reject valid IDs with suffixes.

**Suggested fix:**
```python
if len(parts) < 2:
    print(f"Error: Invalid entry ID format: '{entry_id}'")
```

### 12. `build/update_indexes.py:29` - Uses `os.chdir()` which affects global state

**Problem:** The script changes the current working directory:
```python
os.chdir(project_root)
```

**Impact:** Could cause issues if script is imported as a module or called from another script.

**Suggested fix:** Use absolute paths instead of changing directory.

### 13. Various scripts - Inconsistent error exit codes

**Problem:** Some scripts use `sys.exit(1)` for errors, some use `return 1`, and some use different exit codes (like 2 in `check_duplicate.py`).

**Impact:** Minor inconsistency in CI integration.

**Suggested fix:** Standardize on consistent exit codes (0=success, 1=validation error, 2=usage error).

### 14. `build/resolve_links.py:273` - Integer division for percentage

**Problem:**
```python
report.append(f"Resolved: {resolved_refs} ({resolved_refs * 100 // total_refs}%)")
```
Uses integer division which always rounds down.

**Impact:** Minor - 99.9% would display as 99%.

**Suggested fix:** Use proper rounding or keep as-is for simplicity.

---

## Suggestions (improvements/refactoring)

### 15. Consider adding `__all__` exports to utility modules

Modules like `japanese_utils.py`, `path_utils.py`, and `constants.py` would benefit from explicit `__all__` lists for clearer API documentation.

### 16. Add type hints consistently

Some functions have type hints, others don't. Consider adding them consistently across all scripts for better IDE support and maintainability.

### 17. Consider a shared `io_utils.py` module

Multiple scripts have similar patterns for:
- Loading/saving JSON with error handling
- Reading entries directories
- Building reading/ID indexes

Extracting these into a shared module would reduce duplication.

### 18. Add `if __name__ == '__main__'` guards to all scripts

Most scripts have this, but some modules that are primarily imported could benefit from test/demo code under this guard.

### 19. Consider `functools.lru_cache` for repeated index builds

Scripts like `harden_references.py` and `extract_references.py` both build similar reading indexes. If these are run in sequence, caching could help. However, this is a minor optimization since each script typically runs independently.

---

## Summary

| Severity | Count |
|----------|-------|
| Critical | 0 |
| High | 3 |
| Medium | 6 |
| Low | 5 |
| Suggestions | 5 |

The codebase is well-written and functional. The most actionable fixes are:

1. **Fix the f-string typo** in `build_flat.py:2034`
2. **Remove the unnecessary `.lower()`** in `japanese_utils.py:313`
3. **Update `add_example_ids.py`** to use `rglob` instead of manual glob patterns

---

## Files Reviewed

### Python Scripts (`build/` directory)
- `build_flat.py` (~2,060 lines) - Main HTML generator
- `validate.py` (~783 lines) - Entry validation
- `extract_references.py` (~588 lines) - Cross-reference extraction
- `harden_references.py` (~368 lines) - Reference hardening
- `migrate_entries.py` (~355 lines) - Data migration
- `manage_candidates.py` (~334 lines) - Candidate management
- `japanese_utils.py` (~313 lines) - Japanese language utilities
- `resolve_links.py` (~304 lines) - Cross-reference resolution
- `migrate_cross_references.py` (~235 lines) - Cross-reference migration
- `check_duplicate.py` (~218 lines) - Duplicate detection
- `find_missing_furigana.py` (~203 lines) - Furigana checker
- `verify_furigana.py` (~149 lines) - Furigana verification
- `cleanup_candidates.py` (~132 lines) - Candidate cleanup
- `add_example_ids.py` (~114 lines) - Example ID generator
- `path_utils.py` (~113 lines) - Path utilities
- `get_entry_path.py` (~109 lines) - Path lookup
- `update_entries_index.py` (~99 lines) - Index update
- `update_indexes.py` (~90 lines) - Index orchestration
- `constants.py` (~44 lines) - Constants

### Utility Scripts (`scripts/` directory)
- `update_single_sense.py` (~109 lines)
- `fix_sense_numbers_format.py` (~87 lines)

### Configuration
- `build/schema.json` - JSON Schema (draft-07)

### Frontend
- `docs/search.js` - Client-side search
