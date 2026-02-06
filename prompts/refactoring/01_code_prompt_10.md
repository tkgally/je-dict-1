# Code & Structure — Prompt 10: Split build_flat.py page generators

**Source:** Agent 1 Report (Code & Structure), Prompt 10
**Priority:** High
**Effort:** Medium

---

In je-dict-1, build/build_flat.py contains generator functions for navigation pages.
Extract these into a new file build/page_generators.py:

- generate_index_page()
- generate_advanced_page()
- generate_browse_page()
- generate_recent_page()
- generate_random_page()
- generate_pending_page()
- generate_html_head() (if not already in html_utils.py)
- generate_header_search_redirect_script()
- build_recent_entries()
- format_jst_datetime()

Update build_flat.py to import from page_generators. After this extraction,
build_flat.py should mainly contain the build_flat() orchestration function
and the main() entry point.

Test with: python3 build/build_flat.py
