# Code & Structure — Prompt 22: Add template file error handling

**Source:** Agent Team 5 Report (Post-Refactoring Audit), Fix 2
**Priority:** Low
**Effort:** Very low

---

In je-dict-1, prompts 01 and 02 extracted CSS and JavaScript from `build_flat.py`
into standalone template files under `build/templates/`. The functions that read these
files use `.read_text()` without error handling. If a template file is accidentally
deleted, the build crashes with a raw `FileNotFoundError`.

Add clear error messages:

1. In `build/build_flat.py`, find where `build/templates/styles.css` is read (in
   `generate_stylesheet()`). Wrap the read in a try/except `FileNotFoundError` that
   prints a clear message like:
   `"Error: Template file not found: build/templates/styles.css"`
   and exits with code 1.

2. In `build/search_index_builder.py`, find where `build/templates/search.js` and
   `build/templates/tag-search.js` are read (in `generate_search_js()` and
   `generate_tag_search_js()`). Add the same pattern.

3. Run `python3 build/build_flat.py` to verify the build still works normally.
