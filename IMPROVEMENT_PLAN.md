# Code Improvement Plan

**Created**: 2026-01-11
**Based on**: PROJECT_SUGGESTIONS_20260111.md (suggestions from Claude, GPT-5.2, Gemini)
**Status**: In Progress

## Summary

This document tracks the evaluation and implementation of 17 code improvement suggestions. Issues are organized into phases based on dependencies and complexity.

---

## Issue Priority Evaluation

| # | Issue | Priority | Effort | Phase |
|---|-------|----------|--------|-------|
| 1 | Duplicated `get_entry_prefix()` (5x) | HIGH | Easy | 1 |
| 4 | Duplicated hiragana-romaji conversion (3x) | HIGH | Medium | 1 |
| 10 | Duplicated kana-to-folder mapping | MEDIUM | Easy | 1 |
| 2 | Fix metadata file path in entry pages | MEDIUM | Easy | 2 |
| 5 | Guard recent-entry sorting | MEDIUM | Easy | 2 |
| 9 | Python version compatibility | HIGH | Easy | 2 |
| 13 | Error handling in subprocess calls | LOW | Easy | 2 |
| 14 | Inconsistent datetime handling | MEDIUM | Easy | 2 |
| 15 | Unused migrate_audio.py script | LOW | Trivial | 2 |
| 16 | Minimal requirements.txt | LOW | Easy | 2 |
| 6 | Inconsistent cross-reference format | HIGH | Medium | 3 |
| 17 | Schema allows deprecated legacy format | MEDIUM | Easy | 3 |
| 3 | Cross-reference resolution ambiguity | HIGH | Medium | 4 |
| 7 | Add audio integrity check | MEDIUM | Medium | 4 |
| 8 | Clean output deterministically | LOW | Easy | 4 |
| 11 | Double-loading during validation | LOW | Easy | 4 |
| 12 | No test suite | HIGH | Large | 5 |

---

## Phase 1: Code Consolidation

**Goal**: Eliminate code duplication by creating shared utility modules.

### 1.1 Create `build/path_utils.py`

**Issue #1**: `get_entry_prefix()` is defined 5 times in different files.

**Files to modify**:
- `validate.py` (line 81)
- `build_flat.py` (line 1861)
- `migrate_entries.py` (line 24)
- `merge_audio.py` (line 52)
- `migrate_audio.py` (line 15)

**Action**:
- [x] Create `build/path_utils.py` with `get_entry_prefix()`
- [x] Update all 5 files to import from `path_utils`
- [x] Verify build still works

**Status**: COMPLETED (2026-01-11)

---

### 1.2 Create `build/japanese_utils.py`

**Issues #4 + #10**: Hiragana-romaji conversion and kana-to-folder mapping duplicated.

**Files with duplication**:
- `validate.py`: HIRAGANA_TO_ROMAJI dict, COMBO_MAPPINGS, `hiragana_to_romaji()`, KANA_TO_DIRECTORY
- `build_flat.py`: `hiragana_to_romaji()`, KANA_ROWS, KANA_TO_FOLDER
- `resolve_links.py`: `romaji_to_hiragana()` (with bugs noted)

**Action**:
- [x] Create `build/japanese_utils.py` with:
  - `hiragana_to_romaji(reading: str) -> str`
  - `romaji_to_hiragana(romaji: str) -> str`
  - `KANA_ROWS` list
  - `KANA_TO_FOLDER` dict
  - `get_kana_folder(reading: str) -> str`
- [x] Fix bug in `romaji_to_hiragana()` (trailing 'k' issue) - fixed using regex
- [x] Update all 3 files to import from `japanese_utils`
- [x] Verify build still works

**Status**: COMPLETED (2026-01-11)

---

## Phase 2: Quick Fixes

**Goal**: Address small issues that improve code quality with minimal risk.

### 2.1 Fix Metadata File Path (#2)

**Issue**: `build_flat.py` writes `metadata-file` as `folder/id` but real path is `folder/prefix/id`.

**Action**:
- [x] Locate the code in `build_flat.py` that generates `metadata-file`
- [x] Update to include prefix in path
- [x] Rebuild and verify

**Status**: COMPLETED (2026-01-11)

---

### 2.2 Guard Recent-Entry Sorting (#5)

**Issue**: `build_recent_entries` may raise when mixing naive and aware datetimes.

**Action**:
- [x] Find `build_recent_entries` in `build_flat.py`
- [x] Add timezone-aware fallback (`datetime.min.replace(tzinfo=timezone.utc)`)
- [x] Verified build works

**Status**: COMPLETED (2026-01-11)

---

### 2.3 Python Version Compatibility (#9)

**Issue**: Type hints use Python 3.10+ syntax (`tuple[str, int] | None`) but README states 3.8+ support.

**Decision**: Update minimum Python version to 3.10+ (simpler, modern syntax).

**Action**:
- [x] Update README to specify Python 3.10+
- [x] Update `requirements.txt` with Python version comment

**Status**: COMPLETED (2026-01-11)

---

### 2.4 Error Handling in Subprocess Calls (#13)

**Issue**: `update_indexes.py` doesn't check if scripts exist before calling them.

**Action**:
- [x] Add existence checks in `update_indexes.py` before subprocess calls
- [x] Add clear error messages for missing scripts

**Status**: COMPLETED (2026-01-11)

---

### 2.5 Standardize Datetime Handling (#14)

**Issue**: Mixed use of deprecated `datetime.utcnow()` and modern `datetime.now(timezone.utc)`.

**Action**:
- [x] Found 1 use of `datetime.utcnow()` in `build_flat.py`
- [x] Replaced with `datetime.now(timezone.utc)`
- [x] Using `.isoformat()` (now includes timezone automatically)

**Status**: COMPLETED (2026-01-11)

---

### 2.6 Handle Orphan Script (#15)

**Issue**: `migrate_audio.py` exists but is not documented or called.

**Action**:
- [x] Determined script is obsolete (one-time migration already completed)
- [x] Deleted `build/migrate_audio.py`

**Status**: COMPLETED (2026-01-11)

---

### 2.7 Improve requirements.txt (#16)

**Issue**: Only `jsonschema>=4.0.0` listed; versions not pinned.

**Action**:
- [x] Added upper bound to jsonschema version (`>=4.0.0,<5.0.0`)
- [x] Added comments explaining requirements and Python version

**Status**: COMPLETED (2026-01-11)

---

## Phase 3: Data Migration

**Goal**: Complete cross-reference migration and remove legacy format support.

### 3.1 Migrate All Cross-References (#6)

**Issue**: Entries contain mixed legacy (string) and structured cross-reference formats.

**Action**:
- [ ] Identify all entries with legacy cross-references
- [ ] Create migration script to convert to structured format
- [ ] Run migration
- [ ] Verify all entries use structured format

**Status**: NOT STARTED

---

### 3.2 Update Schema (#17)

**Issue**: Schema allows deprecated legacy format via `oneOf`.

**Action** (after #6 complete):
- [ ] Update `build/schema.json` to only allow structured format
- [ ] Run validation to confirm no regressions

**Status**: NOT STARTED

---

## Phase 4: Feature Improvements

**Goal**: Improve functionality and reliability.

### 4.1 Deterministic Cross-Reference Resolution (#3)

**Issue**: `readings_to_ids` maps reading to single ID; breaks with multiple entries sharing a reading.

**Action**:
- [ ] Change to `reading -> [ids]` index
- [ ] Add headword matching or explicit `id` field support
- [ ] Update `resolve_links.py` accordingly

**Status**: NOT STARTED

---

### 4.2 Add Audio Integrity Check (#7)

**Issue**: No validation that `has_audio: true` examples have corresponding MP3 files.

**Action**:
- [ ] Add audio validation to `validate.py` or create new script
- [ ] Check for orphaned audio files
- [ ] Report mismatches

**Status**: NOT STARTED

---

### 4.3 Clean Output Deterministically (#8)

**Issue**: Build leaves stale artifacts in `docs/`.

**Action**:
- [ ] Consider wiping `docs/` (except `docs/flat/`) before build
- [ ] Or track generated files and remove stale ones

**Status**: NOT STARTED

---

### 4.4 Fix Double-Loading in Validation (#11)

**Issue**: `validate.py` loads each entry twice (schema validation + duplicate check).

**Action**:
- [ ] Refactor to load once and reuse data
- [ ] Measure performance improvement

**Status**: NOT STARTED

---

## Phase 5: Testing Infrastructure

**Goal**: Add automated test coverage.

### 5.1 Create Test Suite (#12)

**Issue**: No automated tests for 14 Python scripts.

**Action**:
- [ ] Set up pytest infrastructure
- [ ] Add tests for `japanese_utils.py` (edge cases: っ, ー, combinations)
- [ ] Add tests for entry validation
- [ ] Add tests for cross-reference resolution
- [ ] Add tests for HTML generation output

**Status**: NOT STARTED

---

## Session Log

### Session 1 (2026-01-11)

**Work completed**:
- Phase 1.1: Created `build/path_utils.py` with consolidated `get_entry_prefix()` and `get_audio_prefix()` functions
- Updated 5 files to import from path_utils: validate.py, build_flat.py, migrate_entries.py, merge_audio.py, migrate_audio.py
- Verified all scripts still run correctly (validation passes, build completes)
- Phase 1.2: Created `build/japanese_utils.py` with consolidated:
  - `hiragana_to_romaji()` - best implementation from validate.py with proper っ and ー handling
  - `romaji_to_hiragana()` - fixed bug using regex for double consonant handling
  - `KANA_ROWS`, `KANA_TO_FOLDER`, `KANA_TO_DIRECTORY` mappings
  - `get_kana_folder()`, `get_expected_directory()` helper functions
- Updated 3 files to import from japanese_utils: validate.py, build_flat.py, resolve_links.py
- Removed ~200 lines of duplicated code

- Phase 2 (Quick Fixes) completed:
  - #2: Fixed metadata file path to include prefix
  - #5: Fixed timezone-aware fallback in recent entries sorting
  - #9: Updated Python version requirement to 3.10+
  - #13: Added script existence checks in update_indexes.py
  - #14: Replaced deprecated datetime.utcnow() with datetime.now(timezone.utc)
  - #15: Deleted obsolete migrate_audio.py script
  - #16: Improved requirements.txt with version bounds and comments

**Next steps**:
- Continue with Phase 3: Data Migration (cross-reference format migration)
