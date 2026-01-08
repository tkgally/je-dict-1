# Suggestions for je-dict-1 Project Improvement from LLM 1

## Search & Data Correctness
- **Strip furigana markup before indexing kanji headwords** (`build/build.py:24-81`). The search index currently stores headwords exactly as written in the entry (e.g., `{学校|がっこう}`), so a user typing `学校` never matches because the braces stay in the key while `performSearch` (`web/app.js:243-332`) compares the raw query string. Normalize both the display form and the search key (e.g., keep the furigana-rich string for rendering but add a brace-free version plus kana/romaji) so kanji searches work and the index remains debuggable.
- **Validate `cross_references` during builds** (`build/validate.py:115-205`). The validator never checks whether linked IDs actually exist, so Compare mode can silently render empty panels when a typo slips into `cross_references`. Extend validation to track every ID that appears and emit an error when a referenced ID is missing—this makes debugging broken relationships straightforward before shipping.

## Automation & Tooling
- **Make `build/update_indexes.py` fail fast on subprocess errors** (`build/update_indexes.py:36-64`). The script prints child stdout/stderr but ignores `returncode`, so `entries_index.json` may stay stale if `update_entries_index.py` fails. Capture the exit code, surface it, and propagate non-zero status so CI/local scripts clearly signal what needs debugging.
- **Add targeted entry validation for faster debugging loops** (`build/validate.py`). Troubleshooting a single JSON file currently requires re-validating all 1,100+ entries. Add a CLI flag such as `--entry path/to/file.json` (or `--id foo_00001`) to run schema and placement checks on just that entry—this shortens the edit/validate loop and prevents spewing unrelated errors when iterating on one word.
- **Copy nested web assets during builds** (`build/build.py:85-92`). `copy_web_files` only copies top-level files, so adding `/web/assets/…` images, fonts, or JS modules will silently be missing from `docs/`. Switching to `shutil.copytree` with `dirs_exist_ok=True` (or walking the tree manually) keeps the deployment folder in sync and avoids hard-to-debug missing-resource errors in the static site.

## Schema & Content Organization
- **Update the JSON schema to match the v2 specification** (`build/schema.json`, `project_specification_v2.md`). High-priority fields like structured `transitivity`, `aspect`, `collocations`, adjective `forms`, and particle `requires_particle` live inside free-form `notes` today, so validators cannot enforce them nor can the UI render them consistently. Extend the schema/validator to require these objects, bump `build.py` to include them in `data.js`, and teach `web/app.js` to render dedicated sections instead of parsing ad-hoc prose.
- **Replace the deprecated vocabulary import workflow** (`build/manage_candidates.py:169-198`). The `import-vocab` command still looks for `N3_VOCABULARY_TO_ADD.md` / `N4_VOCABULARY_TO_ADD.md`, which README/PROJECT_STATUS say were deleted. Either re-home the source data (e.g., under `data/`) or remove the code path and documentation so the candidate toolchain reflects reality and onboarding contributors aren’t sent on a scavenger hunt.

## Front-End Behavior & Structure
- **Finish furigana toggling in Compare mode** (`web/app.js:823-833`). When the user disables/enables furigana, Search and Browse re-render entries but Compare cards keep whatever markup they had when first rendered, leaving the toggle seemingly broken. Store the entry ID on each card and call `createEntryDisplay` again inside `toggleFurigana` so all three interfaces stay in sync.
- **Modularize the 800+ line UI script** (`web/app.js`). Search, Browse, and Compare logic plus all rendering helpers live in one closure, which makes debugging any single feature error-prone. Consider splitting into interface-specific modules (or ES modules bundled into `data.js`) so each mode can be unit-tested in isolation and regressions don’t require wading through unrelated code paths. A small test harness for functions like `detectQueryType`, `processNotesText`, and `hiragana_to_romaji` would also catch regressions early.

# Suggestions for je-dict-1 Project Improvement from LLM 2

Based on an analysis of the codebase, documentation, and build process, here are recommendations for improving the project's organization, robustness, and developer workflow.

## 1. Data Integrity & Validation

The current `validate.py` is strong but can be expanded to catch deeper consistency issues, especially with the new v2 specification.

- **Referential Integrity Checks**: Add validation to ensure that any ID referenced in fields like `transitivity.pair`, `cross_references`, or `collocations` actually exists in the dictionary. Currently, a typo in a reference ID would go unnoticed until runtime.
- **Schema Migration Script**: Since `project_specification_v2.md` introduces new structured fields (e.g., `transitivity` object vs simple text), a script is needed to:
    1. Identify entries using the old format.
    2. Automatically convert them or flag them for manual update.
    3. Ensure all fields required by v2 (like `aspect` for verbs) are present or explicitly marked as "todo".
- **Broken Link Detection**: Scan `gloss` and `notes` fields for any internal links or references that might be broken.

## 2. Testing Strategy

While data validation is in place, the *tooling* itself lacks a test suite.

- **Unit Tests for Build Scripts**: Create a `tests/` directory to test core logic in `build/*.py`.
    - Test `hiragana_to_romaji` with edge cases (small tsu, long vowels, katakana).
    - Test schema validation logic with known bad entries.
    - Test the search index generation to ensure it correctly tokenizes English glosses.
- **Frontend Testing**: If `web/app.js` logic becomes complex (e.g., advanced search filtering), consider adding lightweight JS tests (using `Jest` or similar) to ensure the search algorithm works as expected.

## 3. Developer Workflow & Code Quality

- **Linting & Formatting**:
    - Add a `pyproject.toml` to configure tools like `ruff` (for linting) and `black` (for formatting). This ensures consistent Python code style.
    - Add a linter for JavaScript (like `ESLint`) to catch potential bugs in `web/app.js`.
- **Pre-commit Hooks**: Set up `pre-commit` to automatically run `validate.py` and linters before a commit is allowed. This prevents invalid data from entering the repository.
- **Candidate Management**:
    - Enhance `manage_candidates.py` to support an "assign" or "checkout" workflow. This would allow an agent or developer to mark a candidate as "in progress" to prevent duplicate work.
    - Add a command to generate a "skeleton" entry file from a candidate word to speed up creation.

## 4. Architecture & Organization

- **Frontend Modularity**: The `web/app.js` is currently a single file. As the interface features grow (Search, Browse, Compare modes), consider splitting this into ES modules (e.g., `search.js`, `ui.js`, `data-loader.js`) and using a simple bundler (like `esbuild` or `Rollup`) or native ES module imports if strictly targeting modern browsers.
- **Documentation**: Explicitly clarify the relationship between `web/` and `docs/` in the README. While `docs/` is clearly the build artifact for GitHub Pages, explicit documentation prevents well-meaning contributors from editing files in `docs/` by mistake.

## 5. Feature Suggestions (Low Priority)

- **Hot Reloading**: For easier frontend development, a simple Python HTTP server script that watches for changes and reloads the browser would be a nice quality-of-life improvement over manually refreshing `index.html`.
- **Stats Dashboard**: A script to generate a visual report of v2 adoption (e.g., "40% of verbs have transitivity pairs") to track progress against the new specification.

## Summary of Immediate Action Items

1.  **Create `tests/` directory** and add unit tests for `hiragana_to_romaji`.
2.  **Update `validate.py`** to check for existence of referenced IDs.
3.  **Write a `migrate_v2.py` script** to help standardize existing entries to the new schema.

# Suggestions for je-dict-1 Project Improvement from LLM 3

## 1. Build System Issues

### 1.1 Missing `variants` Directory Reference
**File**: `build/build.py:155`, `build/validate.py:235-245`

**Issue**: Both scripts reference a `variants` directory that doesn't exist:
```python
variants_dir = project_root / 'variants'
for file_path in list(entries_dir.glob('**/*.json')) + list(variants_dir.glob('**/*.json')):
```

**Impact**: Currently benign (empty glob result), but creates confusion and potential for silent failures.

**Suggestion**: Either:
1. Remove the variants directory references if not needed
2. Create the directory and document its purpose
3. Add a check: `if variants_dir.exists()` before globbing

### 1.2 Working Directory Assumption
**File**: `build/update_entries_index.py:53-54`

**Issue**: Script assumes it's run from project root:
```python
entries_dir = Path('entries')
index_file = Path('entries_index.json')
```

Other scripts use `script_dir.parent` pattern correctly.

**Suggestion**: Use consistent path resolution:
```python
script_dir = Path(__file__).parent
project_root = script_dir.parent
entries_dir = project_root / 'entries'
```

### 1.3 Bare Exception Handling
**File**: `build/validate.py:259-260`

**Issue**: Bare except clause swallows all exceptions:
```python
except:
    pass  # Already handled by validate_entry_file
```

**Suggestion**: Catch specific exceptions:
```python
except (json.JSONDecodeError, KeyError, IOError):
    pass  # Entry already flagged as invalid
```

---

## 2. Schema & Validation Issues

### 2.1 Schema Doesn't Match Entry Structure
**File**: `build/schema.json`

**Issue**: The schema doesn't define several fields that appear in entries:
- `predicates_requiring` (used in particle entries like `ga_00001.json`)
- `particle_contrasts`
- `fixed_patterns`
- `common_mistakes`

**Impact**: These fields aren't validated, could have inconsistent structure.

**Suggestion**: Update `schema.json` to include optional fields for particle-specific content:
```json
{
  "predicates_requiring": {
    "type": "object",
    "properties": {
      "description": {"type": "string"},
      "verbs": {"type": "array"},
      "adjectives": {"type": "array"}
    }
  },
  "particle_contrasts": {"type": "array"},
  "fixed_patterns": {"type": "array"},
  "common_mistakes": {"type": "array"}
}
```

### 2.2 ID Pattern May Be Too Restrictive
**File**: `build/schema.json:11`

**Issue**: Pattern `^[a-z]+_[0-9]{5}$` may not handle all romanization cases (e.g., entries starting with numbers or hyphens).

**Current**: Works for standard entries but worth noting if edge cases arise.

---

## 3. JavaScript Application Issues

### 3.1 Incomplete Compare Card Re-render
**File**: `web/app.js:825-833`

**Issue**: The furigana toggle re-render for compare cards is incomplete:
```javascript
// Re-render compare cards
if (!compareDisplay.classList.contains('hidden')) {
    compareCards.querySelectorAll('.compare-card').forEach(card => {
        const headword = card.querySelector('.entry-headword');
        if (headword) {
            // Find entry by headword text and re-render
            const entryId = card.querySelector('.metadata-badges')?.closest('.compare-card')?.dataset?.entryId;
            // Simplified: just toggle existing ruby elements
        }
    });
}
```

**Impact**: Compare cards don't properly re-render when furigana is toggled.

**Suggestion**: Store entry IDs on compare cards and re-render:
```javascript
if (!compareDisplay.classList.contains('hidden')) {
    const currentRomajis = Array.from(compareCards.querySelectorAll('.compare-card'))
        .map(card => card.dataset.romaji)
        .filter(r => r);
    if (currentRomajis.length) {
        showComparison(currentRomajis);
    }
}
```

### 3.2 Search Performance with Large Datasets
**File**: `web/app.js:334-364`

**Issue**: English search iterates through all index keys for prefix matching:
```javascript
Object.keys(index.english).forEach(key => {
    if (key.startsWith(word) && key !== word) {
        index.english[key].forEach(id => entryIds.add(id));
    }
});
```

**Impact**: O(n) complexity for each word in query; may slow down with larger dictionaries.

**Suggestion**: Consider building a trie or sorted array for prefix search, or accept current performance for the expected scale (~1000-5000 entries).

### 3.3 No Error Handling for Missing Data
**File**: `web/app.js:216-233`

**Issue**: No graceful handling if `DICTIONARY_DATA` or `DICTIONARY_INDEX` is malformed:
```javascript
if (typeof DICTIONARY_DATA !== 'undefined' && typeof DICTIONARY_INDEX !== 'undefined') {
    entriesData = DICTIONARY_DATA;
    // ... no validation of structure
}
```

**Suggestion**: Add basic structure validation:
```javascript
if (typeof DICTIONARY_DATA !== 'undefined' &&
    DICTIONARY_DATA.entries &&
    typeof DICTIONARY_INDEX !== 'undefined' &&
    DICTIONARY_INDEX.index) {
    // ...
}
```

---

## 4. Data Organization Suggestions

### 4.1 Entry File Duplication Check
**Observation**: Both `validate.py` and `build.py` re-load entries separately.

**Suggestion**: Consider caching validated entries for the build step to avoid double parsing ~1000+ JSON files.

### 4.2 Index File Redundancy
**Files**: `entries_index.json`, `candidate_words.json`

**Observation**: These are manually managed and can drift from actual entry state.

**Suggestion**: Add a pre-commit hook or CI check to ensure indexes stay synchronized:
```bash
# In .git/hooks/pre-commit or CI
python build/update_indexes.py
git diff --exit-code entries_index.json candidate_words.json
```

### 4.3 Entry Path Storage
**File**: `build/update_entries_index.py:47`

**Issue**: Stores absolute path which may vary between machines:
```python
'path': relative_path  # Actually stores str(entry_path) which could be absolute
```

**Suggestion**: Store path relative to project root:
```python
'path': str(entry_path.relative_to(project_root))
```

---

## 5. Missing Features (as documented in PROJECT_STATUS.md)

### 5.1 Cross-References Not Functional
The `cross_references` field exists in entries (e.g., `taberu_00001.json` references `nomu_00003`) but the web interface doesn't render them as clickable links.

**Suggestion**: Add cross-reference rendering in `createEntryDisplay()`:
```javascript
if (entry.cross_references && entry.cross_references.length > 0) {
    html += `<div class="cross-references"><h3>See Also</h3>`;
    entry.cross_references.forEach(ref => {
        const refEntry = entriesData.entries[ref];
        if (refEntry) {
            html += `<a class="cross-ref-link" data-entry-id="${ref}">
                ${processJapaneseText(refEntry.headword)} (${refEntry.reading})
            </a>`;
        }
    });
    html += `</div>`;
}
```

### 5.2 Missing `.claude/skills/` Directory
The README and PROJECT_STATUS reference Claude Code skills in `.claude/skills/` but this directory doesn't exist in the repository.

**Impact**: AI assistants won't have access to documented entry guidelines.

**Suggestion**: Either create the skills directory with documented skills, or update documentation to reflect current state.

---

## 6. Code Quality Improvements

### 6.1 Add Type Hints to Python Scripts
**Files**: All Python scripts in `build/`

Current code uses minimal type hints. Adding them improves maintainability:
```python
def validate_entry_file(file_path: Path, schema: dict, all_ids: set[str]) -> list[str]:
```

### 6.2 Add JSDoc Comments to JavaScript
**File**: `web/app.js`

Functions have basic comments but formal JSDoc would improve tooling:
```javascript
/**
 * Perform search based on query and type
 * @param {string} query - Search query
 * @param {('auto'|'japanese'|'romaji'|'english')} searchType - Type of search
 * @returns {Array<Object>} Matching entry objects
 */
function performSearch(query, searchType) {
```

### 6.3 Consider ESLint/Prettier Configuration
Adding `.eslintrc.json` and `.prettierrc` would ensure consistent code style.

---

## 7. Testing Recommendations

### 7.1 No Automated Tests
The project has no test files.

**Suggestion**: Add basic tests for:
1. `hiragana_to_romaji()` conversion (edge cases: っ, ー, combinations)
2. JSON schema validation
3. Build script output verification
4. Search functionality

Example test file structure:
```
build/
  tests/
    test_validate.py
    test_romanization.py
web/
  tests/
    app.test.js
```

### 7.2 Manual Testing Checklist
Consider documenting a manual QA checklist:
- [ ] Search by Japanese text works
- [ ] Search by romaji works
- [ ] Search by English works
- [ ] Furigana toggle works in all views
- [ ] Browse filters work correctly
- [ ] Compare view displays entries side-by-side

---

## 8. Security Considerations

### 8.1 XSS Prevention
**File**: `web/app.js:690-695`

The `escapeHtml()` function is used appropriately throughout, which is good. However, ensure all user-facing text passes through it.

**Verified safe**: Search queries are escaped before display in results heading.

### 8.2 No Server-Side Code
Being a static site with embedded data, there are no server-side security concerns. This is a strength of the architecture.

---

## 9. Performance Observations

### 9.1 Large `data.js` File
**File**: `docs/data.js` (2MB)

**Observation**: All dictionary data is embedded in a single JavaScript file.

**Current impact**: Acceptable for ~1000 entries, but may become slow to load as dictionary grows.

**Future consideration**: For 5000+ entries, consider:
1. Lazy loading by kana group
2. IndexedDB caching
3. Service worker for offline support

### 9.2 Full Re-render on Furigana Toggle
Each furigana toggle re-renders multiple views. For current scale this is fine, but consider virtual DOM or targeted updates for larger datasets.

---

## 10. Documentation Gaps

### 10.1 No Contributing Guidelines
Consider adding `CONTRIBUTING.md` with:
- How to create new entries
- Quality standards (reference `project_specification_v2.md`)
- Build/validation workflow

### 10.2 No Changelog
Consider adding `CHANGELOG.md` to track version history beyond the "Recent Changes" in PROJECT_STATUS.md.

### 10.3 README References Wrong Repo Name
**File**: `README.md:134`

References `je-dict-1` directory but current directory is `je-dict-evaluation-2/main/`.

---

## Summary Priority List

### High Priority (Bugs/Issues)
1. Fix compare card furigana re-render (incomplete code)
2. Add missing schema fields for particle entries
3. Fix working directory assumption in `update_entries_index.py`

### Medium Priority (Code Quality)
4. Remove or document `variants` directory references
5. Create missing `.claude/skills/` directory or update docs
6. Add specific exception handling in validate.py

### Low Priority (Enhancements)
7. Implement cross-reference linking in web interface
8. Add automated tests
9. Add type hints to Python code
10. Consider performance optimizations for future scale

