# Code & Structure — Prompt 11: Split build_flat.py search index generation

**Source:** Agent 1 Report (Code & Structure), Prompt 11
**Priority:** High
**Effort:** Medium

---

**Post-prompt-09/10 note:** Prompts 09 and 10 already extracted entry HTML generation
into `build/entry_renderer.py` and navigation page generators into
`build/page_generators.py`. build_flat.py now mainly contains the orchestration logic,
search index generation, and the main() entry point. This prompt extracts the search
index generation.

In je-dict-1, build/build_flat.py still contains the search index generation logic.
Extract these into a new file build/search_index_builder.py:

- generate_search_index() (the function that creates search-index.js content)
- Any helper functions used exclusively by search index generation

The search-index.js file is currently 5.7 MB. While extracting, consider whether
the index could be optimized (e.g., shorter field names, excluding fields not needed
for search).

Update build_flat.py to import from search_index_builder. Test with:
python3 build/build_flat.py
