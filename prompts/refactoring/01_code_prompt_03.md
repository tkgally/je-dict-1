# Code & Structure — Prompt 3: Eliminate strip_furigana and is_kanji duplication

**Source:** Agent 1 Report (Code & Structure), Prompt 3
**Priority:** High
**Effort:** Low

---

In je-dict-1, the functions strip_furigana() and is_kanji() are duplicated across
multiple files instead of being imported from the shared utility module. Fix this:

1. Ensure japanese_utils.py exports strip_furigana (it already does) and add
   is_kanji() to japanese_utils.py (it's currently not there)
2. Update these files to import from japanese_utils instead of defining their own:
   - build/build_kanji_json.py (has its own strip_furigana, is_kanji, FURIGANA_PATTERN)
   - build/extract_kanji_from_entries.py (has its own strip_furigana, is_kanji, FURIGANA_PATTERN)
   - build/update_kanji_index.py (has its own strip_furigana, is_kanji, FURIGANA_PATTERN)
   - build/verify_kanji_index.py (has its own strip_furigana, is_kanji, FURIGANA_PATTERN)
   - build/check_tag_consistency.py (has its own strip_furigana)
3. Verify the build still works: python3 build/validate.py && python3 build/build_flat.py
