# Code & Structure — Prompt 14: Investigate and document build performance

**Source:** Agent 1 Report (Code & Structure), Prompt 14
**Priority:** Low
**Effort:** Low

---

**Post-prompt-01/02/09/10/11 note:** By this point, build_flat.py has been significantly
refactored. CSS is in `build/templates/styles.css` (prompt 01), JavaScript in
`build/templates/search.js` and `build/templates/tag-search.js` (prompt 02), entry HTML
generation in `build/entry_renderer.py` (prompt 09), navigation pages in
`build/page_generators.py` (prompt 10), and search index in
`build/search_index_builder.py` (prompt 11). build_flat.py is now the orchestration
layer that imports from these modules.

In je-dict-1, the build (python3 build/build_flat.py) regenerates all 10,306 entry
pages every time. Profile the build to understand where time is spent:

1. Add timing instrumentation to build_flat.py's build_flat() function -- measure
   time for each major phase: entry HTML generation (via entry_renderer), navigation
   page generation (via page_generators), search index generation (via
   search_index_builder), kanji rebuild, and sitemap generation.
2. Run the build and report the timing breakdown.
3. Based on the results, add a comment block at the top of build_flat.py documenting
   the build time breakdown and potential optimization strategies. Reference the
   specific modules where the time is spent.

Do NOT implement optimizations yet -- just measure and document.
Run: python3 build/build_flat.py
