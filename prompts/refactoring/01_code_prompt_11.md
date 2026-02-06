# Code & Structure — Prompt 11: Split build_flat.py search index generation

**Source:** Agent 1 Report (Code & Structure), Prompt 11
**Priority:** High
**Effort:** Medium

---

In je-dict-1, build/build_flat.py contains the search index generation logic.
Extract these into a new file build/search_index_builder.py:

- generate_search_index() (the function that creates search-index.js content)
- Any helper functions used exclusively by search index generation

The search-index.js file is currently 5.7 MB. While extracting, consider whether
the index could be optimized (e.g., shorter field names, excluding fields not needed
for search).

Update build_flat.py to import from search_index_builder. Test with:
python3 build/build_flat.py
