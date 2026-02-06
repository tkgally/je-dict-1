# Code & Structure — Prompt 19: Add incremental build capability

**Source:** Agent 1 Report (Code & Structure), Prompt 19
**Priority:** Low
**Effort:** Medium

---

**Post-prompt-09/10/11 note:** build_flat.py has been refactored into a modular
structure. Entry HTML generation is in `build/entry_renderer.py`, page generators in
`build/page_generators.py`, and search index in `build/search_index_builder.py`.
build_flat.py is now the orchestration layer. The --quick flag should be implemented
in the orchestration logic (build_flat.py), which decides whether to call
entry_renderer for each entry based on mtime comparison.

In je-dict-1, the build orchestrator (build/build_flat.py) calls entry_renderer.py to
regenerate all 10,306 entry HTML pages on every build. Add a --quick flag that only
regenerates entry pages whose source JSON file has been modified more recently than
the corresponding HTML file:

1. Add argument parsing to build_flat.py's main() function
2. When --quick is passed, compare mtime of each entries/{range}/{id}.json against
   docs/entries/{range}/{id}.html
3. Only call entry_renderer for entries where JSON is newer
4. Still regenerate all navigation pages (via page_generators) since they depend on
   all entries
5. Still regenerate the search index (via search_index_builder) since it depends on
   all entries
6. Print how many entries were skipped vs regenerated

Also update the Makefile (from prompt 08) to add a `quick` target:
`make quick` should run `python3 build/build_flat.py --quick`

Test with:
python3 build/build_flat.py --quick

Note: The full build (without --quick) should continue to work exactly as before.
