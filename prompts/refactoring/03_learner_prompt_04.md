# Learner Experience — Prompt 4: Improve navigation on entry pages

**Source:** Agent 3 Report (Learner Experience), Proposal 4
**Priority:** Medium
**Effort:** Low

---

**Post-01_code_prompt_09/10 note:** Entry HTML generation has been extracted from
build_flat.py. The entry page template is now in `build/entry_renderer.py` (created
by prompt 09). Navigation page generation (including the full nav bar used on
non-entry pages) is in `build/page_generators.py` (created by prompt 10). Shared
HTML helpers may be in `build/html_utils.py`.

Read `build/entry_renderer.py` to understand how entry HTML pages are generated, and
`build/page_generators.py` to see how the full navigation bar is constructed for other
pages. Then modify the entry page template in `build/entry_renderer.py` to include
the full navigation bar (Home, Advanced, Browse, Recent, Random, Pending, About)
instead of the reduced set (Home, Random, About). Also add a "Back to Browse" link
in the entry header area. Rebuild with `python3 build/build_flat.py` (or `make build`)
and verify a few entry pages look correct.
