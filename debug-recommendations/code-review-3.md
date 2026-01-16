# Code Review Report: je-dict-1

This review focuses on the Python build scripts and web frontend code, prioritizing code quality, maintainability, and robustness.

## Critical Issues (Must Fix)

### 1. Code Duplication in Cross-Reference Resolution
- **Files**: `build/build_flat.py`, `build/resolve_links.py`, `build/validate.py`
- **Issue**: Logic for resolving cross-references (mapping readings to entries, handling homonyms) is duplicated across these three files.
- **Impact**: Inconsistent behavior (e.g., `validate.py` might pass an entry that `build_flat.py` fails to link correctly). Any change to resolution logic requires updating three files.
- **Fix**: Centralize resolution logic in `resolve_links.py` and import it in `build_flat.py` and `validate.py`.

### 2. Risky Package Installation in Validation Script
- **File**: `build/validate.py` (Lines 24-34)
- **Issue**: The `ensure_package` function attempts to `pip install` packages at runtime.
- **Impact**: This is unsafe for CI/CD environments, shared systems, or sandboxed environments where network access or permissions might be restricted. It modifies the user's environment without explicit consent.
- **Fix**: Remove `ensure_package`. Rely on `requirements.txt` and document that dependencies must be installed before running scripts.

### 3. Inconsistent Source of Truth for Entries
- **Files**: `build/build_flat.py`, `build/validate.py`, `build/manage_candidates.py` vs `build/cleanup_candidates.py`
- **Issue**: Most scripts scan the `entries/` directory recursively to load data (O(N) I/O operations). `cleanup_candidates.py` reads `entries_index.json`.
- **Impact**: Inconsistency and potential performance bottlenecks as the dictionary grows. If `entries_index.json` is not updated, `cleanup_candidates.py` works on stale data.
- **Fix**: Create a central `EntryLoader` class in a utility module that handles loading entries efficiently (possibly caching) and use it everywhere.

## High Priority Issues (Should Fix)

### 4. Search Index Scalability
- **File**: `build/build_flat.py` (Line 524, `generate_search_index`)
- **Issue**: The entire search index is dumped into a single JavaScript object in `search-index.js`.
- **Impact**: As the dictionary grows (currently ~6000 entries), this file size will increase linearly, potentially causing slow page loads and high memory usage on mobile devices.
- **Fix**: Implement a more efficient index (e.g., trie-based or split by initial character) or move search logic to a lightweight backend/Edge function if static hosting limits are reached. For now, minimizing the JSON structure (removing redundant keys) would help.

### 5. Silent Overwriting of Duplicate IDs
- **File**: `build/build_flat.py` (Line 722)
- **Issue**: `entries_dict = {e['id']: e for e in entries}` silently overwrites entries if duplicate IDs exist.
- **Impact**: Data loss in the generated site. While `validate.py` checks for this, the build script should fail fast or warn if duplicates are encountered to prevent generating a broken site if validation wasn't run.
- **Fix**: Add a check for duplicates during dictionary construction in `build_flat.py`.

### 6. Brittle Japanese Processing Utilities
- **File**: `build/japanese_utils.py`
- **Issue**:
    - `hiragana_to_romaji`: Small tsu (`っ`) handling logic is simplistic and may fail on edge cases (e.g., `っ` at end of string or before vowel).
    - `romaji_to_hiragana`: Uses simple string replacement which depends heavily on order and regex for double consonants.
    - Missing normalization: `cleanup_candidates.py` implements its own katakana normalization instead of using a shared utility.
- **Fix**: Refactor `japanese_utils.py` to be more robust (token-based parsing) and include the normalization logic from `cleanup_candidates.py`.

### 7. Incomplete Furigana Validation
- **File**: `build/find_missing_furigana.py`
- **Issue**: Only scans the `notes` field for unannotated kanji.
- **Impact**: Kanji in `examples`, `definitions`, or `explanation` fields might be missing furigana but won't be detected.
- **Fix**: Update `scan_entries` to check all relevant fields (`examples.japanese`, `definitions.explanation`, etc.).

## Medium Priority Issues

### 8. Hardcoded Cross-Reference Types
- **Files**: `build/schema.json`, `build/validate.py`, `build/build_flat.py`
- **Issue**: Valid cross-reference types (pair, synonym, etc.) and their display labels are defined in multiple places.
- **Impact**: Maintenance burden. Adding a new type requires updates across 3 files.
- **Fix**: Define constants in a shared module (e.g., `build/constants.py` or `build/schema_defs.py`) and import them in scripts. Generate/validate `schema.json` from these constants if possible.

### 9. System Clock Dependency for Validation
- **File**: `build/validate.py` (Line 230, `check_timestamps`)
- **Issue**: Checks if timestamps are in the future relative to `datetime.now()`.
- **Impact**: CI runners with drifted clocks might falsely flag valid entries.
- **Fix**: Allow a small grace period (e.g., 24 hours) or remove the check if not strictly necessary.

### 10. Aggressive Directory Cleanup
- **File**: `build/build_flat.py` (Line 746)
- **Issue**: `shutil.rmtree` cleans up `docs/` but preserves `flat`.
- **Impact**: If a user manually places a file in `docs/` (e.g., `CNAME`, `robots.txt`, custom favicon), it gets deleted on every build.
- **Fix**: Only delete specific generated files/directories or use an allowlist of files to preserve.

## Suggestions & Improvements

### 11. Use of `html.escape`
- **File**: `build/build_flat.py`
- **Observation**: Good use of `html.escape` throughout. This is a positive finding for security.

### 12. CSS Variables
- **File**: `build/build_flat.py` (CSS generation)
- **Observation**: Good use of CSS variables for theming. This makes future design updates easier.

### 13. Hardcoded Timezone
- **File**: `build/build_flat.py`
- **Issue**: `JST = timezone(timedelta(hours=9))` is hardcoded.
- **Suggestion**: While acceptable for a specific project, considering moving configuration like this to a `config.py` or reading from `settings.json` would be more flexible.

## Refactoring Plan (Recommended First Steps)

1.  **Extract Shared Logic**: Move cross-reference resolution from `build_flat.py` and `validate.py` into `resolve_links.py`.
2.  **Centralize Constants**: Move cross-reference types and labels to a single definition file.
3.  **Enhance Utilities**: Move `normalize_reading` from `cleanup_candidates.py` to `japanese_utils.py`.
4.  **Fix Validation**: Remove `ensure_package` from `validate.py`.
