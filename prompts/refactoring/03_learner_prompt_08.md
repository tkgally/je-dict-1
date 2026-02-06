# Learner Experience — Prompt 8: Create learner-facing tier study lists

**Source:** Agent 3 Report (Learner Experience), Proposal 8
**Priority:** Medium
**Effort:** Medium

---

**Post-prompt notes:**
- **01_code_prompt_01:** CSS is now in `build/templates/styles.css`, not embedded in
  Python. The tier pages should link to the same stylesheet.
- **01_code_prompt_07:** `entries_index.json` is enriched with `vocabulary_tier` and
  `pos_tags`, so the tier pages can be generated from the index without loading every
  entry file.
- **01_code_prompt_10:** Navigation page generation patterns are in
  `build/page_generators.py`. Use the browse page generator as a model for structure.

Write a build script (build/build_tier_pages.py) that generates three
HTML pages in docs/: basic.html, core.html, general.html. Each page
lists all entries in that tier, organized by semantic category (from
metadata.tags.semantic), with headword, reading, and gloss. Include
a count per category. Use the same styling (referencing `styles.css`)
and page structure as browse.html (see `build/page_generators.py` for
the pattern). Add links to these pages from the main navigation
(update the nav bar in `build/page_generators.py` and
`build/entry_renderer.py`). Rebuild with `make build`.
