# Code & Structure — Prompt 9: Split build_flat.py entry HTML generation

**Source:** Agent 1 Report (Code & Structure), Prompt 9
**Priority:** High
**Effort:** Medium

---

In je-dict-1, build/build_flat.py is 3,664 lines long. Extract the entry page HTML
generation into a separate module. Specifically, move these functions to a new file
build/entry_renderer.py:

- generate_entry_html()
- process_headword_with_kanji_links()
- process_notes_text()
- render_examples() (the inner function)
- Any helper functions used only by the above

The new module should import from the existing shared utilities (japanese_utils,
constants, html_utils, path_utils). Update build_flat.py to import from entry_renderer.

Test with: python3 build/build_flat.py
