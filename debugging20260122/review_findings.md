# Code Review Findings: je-dict-1

## Critical (must fix)

- **File: `docs/search.js` (Lines 30-50)**
    - **Problem:** Inefficient search algorithm using $O(N)$ linear scans of all index keys on every keystroke.
    - **Impact:** As the dictionary grows (~7,800 entries), the search becomes sluggish, especially on mobile devices. English search is particularly slow as it performs a full linear scan of thousands of keys for *every word* in the query.
    - **Suggested Fix:** Use direct dictionary lookups for full-word matches and implement a more efficient data structure (like a Prefix Tree/Trie) for "starts with" searches.

- **File: `je-dict-1-main/build/build_flat.py` (Lines 1000-1400)**
    - **Problem:** Hardcoded tag list in the `generate_tag_search_section` function.
    - **Impact:** The advanced search interface is not synchronized with `build/tag_taxonomy.json`. If new tags are added to the taxonomy, they will not appear in the UI without manual code changes to `build_flat.py`, leading to "missing" tags in search.
    - **Suggested Fix:** Dynamically generate the tag checkboxes by reading `build/tag_taxonomy.json` during the build process.

## High (should fix)

- **File: `je-dict-1-main/build/build_flat.py` (Lines 1879-1950)**
    - **Problem:** Excessive search index size due to inclusion of full entry data in `window.SEARCH_ENTRIES`.
    - **Impact:** The generated `search-index.js` becomes several megabytes because it includes pre-processed HTML (`<ruby>` tags) and redundant metadata. This significantly increases initial page load time and memory usage.
    - **Suggested Fix:** Store only essential fields in the search index and generate the HTML display dynamically in `search.js` or include only what's necessary for the result list.

- **Files: Multiple (`build_flat.py`, `build_kanji_html.py`, `japanese_utils.py`, `extract_references.py`)**
    - **Problem:** Massive code duplication of core utilities.
    - **Impact:** Functions like `process_furigana`, `romaji_to_hiragana`, and `is_kanji` are redefined multiple times. This makes maintenance difficult and error-prone, as a fix in one file must be manually copied to several others.
    - **Suggested Fix:** Centralize all Japanese language utilities in `build/japanese_utils.py` and ensure all scripts import from there.

## Medium (consider fixing)

- **Files: `validate.py`, `harden_references.py`, `tag_statistics.py`, `extract_references.py`**
    - **Problem:** Redundant entry indexing. Every script independently walks the `entries/` directory and reads all 7,839 JSON files to build a reading-to-entry index.
    - **Impact:** Extremely inefficient I/O. A full build process reads the entire data set 4-5 times unnecessarily.
    - **Suggested Fix:** Implement a shared caching mechanism or a single orchestrator script that loads the data once and passes it to the various processing modules.

- **File: `je-dict-1-main/build/build_flat.py` (Line 3465)**
    - **Problem:** Using `['python3', ...]` in `subprocess.run` calls.
    - **Impact:** This assumes `python3` is in the user's PATH, which may not be true in all environments (e.g., Windows or specific CI environments).
    - **Suggested Fix:** Use `sys.executable` instead of the literal string `'python3'`.

- **File: `je-dict-1-main/build/harden_references.py` (Line 126)**
    - **Problem:** Unsafe dictionary access in `apply_changes`.
    - **Impact:** The code assumes `entry['metadata']` always exists. While the schema requires it, if a file is malformed, the entire hardening build will crash with a `KeyError`.
    - **Suggested Fix:** Use `entry.get('metadata', {}).get('modified', ...)` or add a check before assignment.

## Low (nice to have)

- **File: `docs/search.js`**
    - **Problem:** Missing search debounce.
    - **Impact:** The expensive search function runs on every single character typed, which can cause typing lag.
    - **Suggested Fix:** Wrap the search handler in a 150ms debounce function.

- **File: `build/validate.py` (Lines 429, 485)**
    - **Problem:** Redundant internal index building in specific validation functions.
    - **Impact:** Minor performance hit within the validation script itself.
    - **Suggested Fix:** Pass the pre-built `reading_index` into these functions as an argument.

## Suggestions (improvements/refactoring)

1.  **Template Engine:** The codebase relies heavily on large F-strings for HTML generation. Migrating to a template engine like **Jinja2** would significantly improve readability and maintainability of the UI code.
2.  **Consolidated Build:** Create a single `build_all.py` script that manages the dependency graph of the build process and shares loaded data between steps.
3.  **Search Index Optimization:** For the English search, consider a pre-computed inverted index where each English word maps directly to a list of Entry IDs, eliminating the need for linear scans during search.
