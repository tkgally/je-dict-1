# Debug Plan: LLM Code Review Recommendations

This document tracks fixes based on code reviews from three LLMs. Work through tasks in order, marking each as completed when done. **Target: 2-3 tasks per session.**

---

## Session 1: Security & Build Stability

### Task 1.1: Fix XSS vulnerability in search results
- [x] **COMPLETED**
- **Files**: `docs/search.js`, `build/build_flat.py`
- **Issue**: Search results use innerHTML with unescaped content (entry.headword, entry.gloss)
- **Fix**: Either escape gloss in `build_flat.py:generate_search_index()` OR use DOM methods in search.js
- **Reviews**: 1 (#5), 2 (#2)

### Task 1.2: Remove auto-install package pattern
- [x] **COMPLETED**
- **File**: `build/validate.py` (lines 24-38)
- **Issue**: `ensure_package()` runs pip install at runtime - security risk, breaks CI/CD
- **Fix**: Remove function, add clear error message if jsonschema not installed
- **Reviews**: 2 (#1), 3 (#2)

### Task 1.3: Fix null candidate field crash
- [x] **COMPLETED**
- **File**: `build/build_flat.py` (lines 800-802)
- **Issue**: `html.escape(candidate.get('reading', ''))` fails if value is explicitly `None`
- **Fix**: Change to `html.escape(candidate.get('reading') or '')`
- **Review**: 1 (#2)

---

## Session 2: Data Integrity

### Task 2.1: Fix cross-reference migration losing distinct refs
- [x] **COMPLETED**
- **File**: `build/migrate_cross_references.py`
- **Issue**: Deduplication uses only `reading`, dropping refs with same reading but different type/headword/label
- **Fix**: Use composite key `(type, reading, headword, label)` for deduplication
- **Review**: 1 (#1)

### Task 2.2: Add duplicate ID check to build
- [x] **COMPLETED**
- **File**: `build/build_flat.py` (around line 722)
- **Issue**: `entries_dict = {e['id']: e for e in entries}` silently overwrites duplicates
- **Fix**: Add explicit duplicate check with warning/error
- **Review**: 3 (#5)

### Task 2.3: Fix self-reference validation gap
- [x] **COMPLETED**
- **File**: `build/validate.py`
- **Issue**: Self-reference detection only fires when both reading AND headword match; same-reading refs without headword pass
- **Fix**: If reading matches and headword is missing, treat as potential self-reference
- **Review**: 1 (#3)

---

## Session 3: Robustness & Error Handling

### Task 3.1: Add error handling to utility scripts
- [x] **COMPLETED**
- **Files**: `build/cleanup_candidates.py`, `build/manage_candidates.py`
- **Issue**: JSON file operations lack try/except
- **Fix**: Add proper error handling with clear messages
- **Review**: 2 (#4)

### Task 3.2: Fix hardcoded relative paths
- [x] **COMPLETED**
- **File**: `build/manage_candidates.py` (line 27)
- **Issue**: `CANDIDATES_FILE = Path('candidate_words.json')` fails from non-root directory
- **Fix**: Calculate path relative to script location
- **Review**: 2 (#5)

### Task 3.3: Make build process atomic
- [x] **COMPLETED**
- **File**: `build/build_flat.py`
- **Issue**: Build deletes docs/ before generating - failed builds leave broken state
- **Fix**: Build to temp directory, then swap atomically (or add preserved files list)
- **Reviews**: 2 (#7), 3 (#10)

---

## Session 4: Performance

### Task 4.1: Fix double file read in add_example_ids.py
- [x] **COMPLETED**
- **File**: `build/add_example_ids.py` (lines 91-94)
- **Issue**: Main loop reads each file twice
- **Fix**: Pass loaded data to process_entry or refactor
- **Review**: 2 (#6)

### Task 4.2: Fix inefficient search index creation
- [x] **COMPLETED**
- **File**: `build/build_flat.py` (around line 883)
- **Issue**: O(n²) duplicate detection with list membership checks
- **Fix**: Use sets instead of lists, convert at end
- **Review**: 2 (#10)

### Task 4.3: Reuse validator instance
- [x] **COMPLETED**
- **File**: `build/validate.py`
- **Issue**: Creates new Draft7Validator for each entry
- **Fix**: Initialize once and reuse
- **Review**: 1 (Optional)

---

## Session 5: Code Quality & Consistency

### Task 5.1: Move imports to module top
- [x] **COMPLETED**
- **Files**: `build/build_flat.py` (line 1899), `build/japanese_utils.py` (line 215), `build/resolve_links.py` (line 31), `build/validate.py` (line 247)
- **Issue**: Various imports inside functions
- **Fix**: Move all imports to top of files
- **Reviews**: 2 (#3, #9, #13, #15)

### Task 5.2: Centralize furigana pattern
- [x] **COMPLETED**
- **Files**: Multiple (build_flat.py, extract_references.py, find_missing_furigana.py, verify_furigana.py, update_entries_index.py)
- **Issue**: Same regex pattern `r'\{([^|]+)\|([^}]+)\}'` duplicated across 5+ files
- **Fix**: Add FURIGANA_PATTERN and helper functions to japanese_utils.py
- **Review**: 2 (#17)

### Task 5.3: Refactor validate_all_entries return type
- [x] **COMPLETED**
- **File**: `build/validate.py` (line 350)
- **Issue**: Function returns 7-tuple, hard to use correctly
- **Fix**: Return a dataclass or TypedDict
- **Review**: 2 (#8)

---

## Session 6: Schema & Validation Consistency

### Task 6.1: Update schema for legacy cross-reference format
- [x] **COMPLETED**
- **File**: `build/schema.json`
- **Issue**: Schema only allows object cross-refs but code handles legacy strings
- **Fix**: Add oneOf to allow string OR object format
- **Review**: 1 (#4)

### Task 6.2: Expand reading pattern in schema
- [x] **COMPLETED**
- **File**: `build/schema.json` (line 21-23)
- **Issue**: Pattern `^[ぁ-んー]+$` misses voiced iteration marks (ゝ, ゞ)
- **Fix**: Expand character class to include rare kana
- **Review**: 2 (#11)

### Task 6.3: Fix system clock dependency in validation
- [x] **COMPLETED**
- **File**: `build/validate.py` (line 230)
- **Issue**: Checks if timestamps are "in future" based on current time
- **Fix**: Add small grace period (24h) to avoid CI clock drift issues
- **Review**: 3 (#9)

---

## Session 7: UX & Minor Fixes

### Task 7.1: Add furigana toggle to pending.html
- [x] **COMPLETED**
- **File**: `build/build_flat.py`
- **Issue**: pending.html missing furigana toggle script
- **Fix**: Add `generate_furigana_script()` call
- **Review**: 1 (#6)

### Task 7.2: Use return value in update_entries_index.py
- [x] **COMPLETED**
- **File**: `build/update_entries_index.py` (line 96)
- **Issue**: Function returns boolean but main ignores it
- **Fix**: Use return value for exit code
- **Review**: 2 (#16)

### Task 7.3: Extend furigana scanning to all text fields
- [x] **COMPLETED**
- **File**: `build/find_missing_furigana.py`
- **Issue**: Only scans notes field for missing furigana
- **Fix**: Also scan examples, definitions, explanation fields
- **Review**: 3 (#7)

---

## Session 8: Architecture (Larger Refactors)

### Task 8.1: Centralize cross-reference type definitions
- [ ] **PENDING**
- **Files**: `build/schema.json`, `build/validate.py`, `build/build_flat.py`
- **Issue**: Cross-ref types (pair, synonym, etc.) defined in 3 places
- **Fix**: Create constants module, import everywhere
- **Review**: 3 (#8)

### Task 8.2: Move normalize_reading to japanese_utils.py
- [ ] **PENDING**
- **Files**: `build/cleanup_candidates.py` → `build/japanese_utils.py`
- **Issue**: Katakana normalization logic isolated in cleanup script
- **Fix**: Move to shared utilities
- **Review**: 3 (#6)

---

## Future Considerations (Not Scheduled)

These are larger efforts noted by reviewers but not prioritized for immediate action:

- **Add unit tests** for japanese_utils.py, process_furigana(), schema validation (Review 2 #21)
- **Add type hints** throughout codebase (Review 2 #18)
- **Standardize on pathlib** vs os.path (Review 2 #19)
- **Add `__all__` exports** to utility modules (Review 2 #20)
- **Consider search index scalability** for future growth (Review 3 #4)
- **Create EntryLoader class** for consistent entry loading (Review 3 #3)
- **Extract CSS to separate file** from build_flat.py (Review 2 #12)

---

## Progress Log

| Session | Date | Tasks Completed |
|---------|------|-----------------|
| 1 | 2026-01-16 | 1.1, 1.2, 1.3 |
| 2 | 2026-01-16 | 2.1, 2.2, 2.3 |
| 3 | 2026-01-16 | 3.1, 3.2, 3.3 |
| 4 | 2026-01-16 | 4.1, 4.2, 4.3 |
| 5 | 2026-01-16 | 5.1, 5.2, 5.3 |
| 6 | 2026-01-16 | 6.1, 6.2, 6.3 |
| 7 | 2026-01-16 | 7.1, 7.2, 7.3 |
| 8 | - | - |

---

## Instructions for Claude

When resuming work on this plan:
1. Find the first session with **PENDING** tasks
2. Complete **2-3 tasks** from that session
3. Mark completed tasks by changing `- [ ] **PENDING**` to `- [x] **COMPLETED**`
4. Update the Progress Log with the date
5. Commit changes with a message like "Fix: [brief description of tasks completed]"
6. If a task turns out to be invalid or already fixed, mark it `- [x] **SKIPPED** (reason)`
