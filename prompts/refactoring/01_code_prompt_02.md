# Code & Structure — Prompt 2: Extract JavaScript from build_flat.py

**Source:** Agent 1 Report (Code & Structure), Prompt 2
**Priority:** High
**Effort:** Medium

---

In je-dict-1, build/build_flat.py contains several functions that return JavaScript
as Python strings: generate_search_js(), generate_tag_search_js(), and any inline
<script> blocks. Extract these into standalone .js files under build/templates/:

1. build/templates/search.js (from generate_search_js())
2. build/templates/tag-search.js (from generate_tag_search_js())

Modify the generator functions to read from these files instead. Test with:
python3 build/build_flat.py

Note: The small inline scripts in html_utils.py (furigana toggle, examples toggle,
word links toggle, header search) can stay inline for now since they're short.
