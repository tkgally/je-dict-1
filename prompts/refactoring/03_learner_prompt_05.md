# Learner Experience — Prompt 5: Add tier badge to search results

**Source:** Agent 3 Report (Learner Experience), Proposal 5
**Priority:** Medium
**Effort:** Medium

---

**Post-prompt notes:**
- **01_code_prompt_02:** JavaScript has been extracted from build_flat.py. The search
  logic is now in `build/templates/search.js` (not embedded in Python).
- **01_code_prompt_07:** `entries_index.json` already includes `vocabulary_tier` for
  every entry. This data is available for the search index builder to use.
- **01_code_prompt_11:** Search index generation has been extracted into
  `build/search_index_builder.py`.

Read `build/templates/search.js` for the client-side search display logic and
`build/search_index_builder.py` for how the search index is generated. Modify
the search index builder to include vocabulary_tier in search index entries (the
data is already in entries_index.json from prompt 07). Then update the
displayResults function in `build/templates/search.js` to show a small tier badge
(styled like the one on entry pages) next to each search result. This helps
learners prioritize which words to study based on their level. Rebuild with
`python3 build/build_flat.py` (or `make build`) and verify.
