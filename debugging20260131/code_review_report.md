# Code Review Report: je-dict-1

This report details findings from a review of the `je-dict-1` codebase, focusing on the Python build scripts and static site generation logic.

## Severity Levels
- **Critical**: Bugs or errors that prevent the system from working.
- **High**: Significant issues affecting maintenance, scalability, or correctness.
- **Medium**: Issues affecting efficiency or consistency.
- **Low**: Minor code quality or style issues.
- **Suggestions**: Ideas for refactoring or improvement.

---

### Critical (must fix)
*No critical issues found that would prevent the site from building or functioning.*

### High (should fix)
- **File:** `build/build_kanji_html.py` and `build/build_flat.py`
  - **Description:** Significant code duplication in HTML generation. Functions like `process_furigana`, `generate_nav_header`, `generate_furigana_script`, `generate_examples_script`, and `generate_header_search_script` are duplicated in both files. `build_kanji_html.py` also re-implements `romaji_to_hiragana`.
  - **Impact:** Updates to the UI (e.g., changing the navigation menu or search script) must be applied in two places, doubling the maintenance effort and increasing the risk of inconsistency.
  - **Fix:** Extract these common HTML generation functions into a new module (e.g., `build/html_utils.py` or `build/ui_components.py`) and import them in both scripts.

### Medium (consider fixing)
- **File:** `docs/search.js` (lines 142-152)
  - **Description:** The script uses `setInterval` to poll for `window.SEARCH_INDEX` to handle URL parameters.
  - **Impact:** This is inefficient and can be flaky. If the index takes longer than 5 seconds (on a slow connection), the URL parameter check will timeout and fail silently.
  - **Fix:** Dispatch a custom event (e.g., `SearchIndexLoaded`) from `search-index.js` when it finishes loading, and add an event listener in `search.js` to handle the URL parameters immediately upon load.

- **File:** `build/validate.py` (lines 143-172)
  - **Description:** `is_valid_hiragana` and `contains_katakana` are defined locally, duplicating logic that should belong in `japanese_utils.py`. `japanese_utils.py` handles reading normalization but lacks these specific validation predicates.
  - **Impact:** Inconsistent validation rules if one file is updated but not the other.
  - **Fix:** Move these functions to `build/japanese_utils.py` and import them in `validate.py`.

- **File:** `build/build_kanji_html.py` (lines 125-156)
  - **Description:** `romaji_to_hiragana` is re-implemented locally with a `conversions` dictionary, whereas `japanese_utils.py` has a central implementation.
  - **Impact:** Inconsistency in romaji conversion. `japanese_utils.py` handles more edge cases (like double consonants `kk`, `tt`) which the local implementation in `build_kanji_html.py` might miss or handle differently.
  - **Fix:** Use `japanese_utils.romaji_to_hiragana`.

### Low (nice to have)
- **File:** `build/build_flat.py` (lines 535+) and `build/build_kanji_html.py`
  - **Description:** HTML is constructed using extensive string concatenation / f-strings.
  - **Impact:** Makes the code harder to read and maintain. Syntax errors in HTML are not caught until runtime or visual inspection.
  - **Fix:** Consider using a lightweight templating engine like `Jinja2` (would add a dependency) or separate HTML templates into their own files that are loaded and formatted.

- **File:** `build/extract_references.py` (line 342)
  - **Description:** Broad `try...except Exception` block in `process_all_entries`.
  - **Impact:** Might hide unexpected bugs or system errors (like `KeyboardInterrupt` if not handled separately) during batch processing.
  - **Fix:** Catch specific exceptions (e.g., `json.JSONDecodeError`, `IOError`) or ensure the exception is logged with full traceback (using `traceback` module) for debugging.

### Suggestions (improvements/refactoring)
- **File:** `build/japanese_utils.py`
  - **Description:** Add `romaji_to_katakana` to this utility module.
  - **Reason:** `build_kanji_html.py` implements this locally. It's a useful utility that likely has value for other parts of the system.

- **File:** `build/build_sitemap.py`
  - **Description:** The `SITE_URL` is hardcoded to "https://www.tkgje.jp".
  - **Reason:** Moving this to a config file (like `.claude/settings.json` or `constants.py`) would make it easier to test sitemap generation for staging environments or forks.
