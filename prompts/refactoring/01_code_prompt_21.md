# Code & Structure — Prompt 21: Remove duplicate is_kanji() from entry_renderer.py

**Source:** Agent Team 5 Report (Post-Refactoring Audit), Fix 1
**Priority:** Medium
**Effort:** Very low

---

In je-dict-1, prompt 03 centralized `is_kanji()` in `build/japanese_utils.py` and
updated five files to import it from there instead of defining their own copies.
However, `build/entry_renderer.py` still has a local `is_kanji()` definition inside
the `process_headword_with_kanji_links()` function (around line 87).

Fix this:

1. Read `build/entry_renderer.py` and find the local `is_kanji()` function inside
   `process_headword_with_kanji_links()`
2. Add `is_kanji` to the existing import from `japanese_utils` at the top of the file
3. Remove the local `is_kanji()` definition from inside the function
4. Run `python3 build/build_flat.py` to verify the build still works
5. Run `python3 -m pytest build/tests/ -v` to verify tests still pass
