# Code & Structure — Prompt 19: Add incremental build capability

**Source:** Agent 1 Report (Code & Structure), Prompt 19
**Priority:** Low
**Effort:** Medium

---

In je-dict-1, build/build_flat.py regenerates all 10,306 entry HTML pages on every
build. Add a --quick flag that only regenerates entry pages whose source JSON file
has been modified more recently than the corresponding HTML file:

1. Add argument parsing to build_flat.py's main() function
2. When --quick is passed, compare mtime of each entries/{range}/{id}.json against
   docs/entries/{range}/{id}.html
3. Only regenerate HTML for entries where JSON is newer
4. Still regenerate all navigation pages (index, browse, recent, random) since they
   depend on all entries
5. Print how many entries were skipped vs regenerated

Test with:
python3 build/build_flat.py --quick

Note: The full build (without --quick) should continue to work exactly as before.
