# Code & Structure — Prompt 4: Add unit tests for japanese_utils.py

**Source:** Agent 1 Report (Code & Structure), Prompt 4
**Priority:** Medium
**Effort:** Low

---

Create a test file at build/tests/test_japanese_utils.py with unit tests for the
functions in build/japanese_utils.py. Test at minimum:

- hiragana_to_romaji: basic cases, combo characters, gemination (っ), long vowels (ー)
- romaji_to_hiragana: basic cases, double consonants
- strip_furigana: simple and nested cases, empty input
- is_kanji: single kanji, non-kanji characters, edge cases (added by prompt 03)
- is_valid_hiragana: valid hiragana, katakana (should fail), romaji (should fail)
- normalize_reading: katakana to hiragana conversion
- contains_katakana: with and without katakana, long vowel mark edge case
- get_kana_folder: various starting characters

**Post-prompt-03 note:** Prompt 03 added `is_kanji()` and consolidated `FURIGANA_PATTERN`
into japanese_utils.py. Include tests for these additions.

Use the docstring examples as initial test cases. Run with:
cd /home/user/je-dict-1 && python3 -m pytest build/tests/test_japanese_utils.py -v

If pytest is not installed, install it first: pip install pytest
