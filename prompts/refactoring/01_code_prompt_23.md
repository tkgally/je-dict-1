# Code & Structure — Prompt 23: Add kanji_list.json missing-file warning

**Source:** Agent Team 5 Report (Post-Refactoring Audit), Fix 3
**Priority:** Low
**Effort:** Very low

---

In je-dict-1, `build/entry_renderer.py` loads `kanji/kanji_list.json` at module import
time (around lines 32-38). If the file doesn't exist, it silently falls back to an
empty dict, which would cause all kanji links in entry pages to silently produce no
output.

Add a warning:

1. Read `build/entry_renderer.py` and find the `KANJI_LIST` loading code near the top
   of the file.
2. In the `except` branch where it falls back to `{}`, add a `print()` warning like:
   `"Warning: kanji/kanji_list.json not found — kanji links will be disabled"`
3. Run `python3 build/build_flat.py` to verify the build still works normally and no
   spurious warning appears (since the file does exist).
