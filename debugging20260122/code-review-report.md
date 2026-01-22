# Code Review Report: je-dict-1

## Critical (must fix)
- None found.

## High (should fix)
- `build/duplicate_utils.py:62`: `check_for_duplicate` returns on the first reading-only match, which can happen before an exact match later in the list. Impact: exact duplicates can be misclassified as reading-only, blocking valid entries/candidates or hiding true exact duplicates. Suggested fix: scan the full list for exact matches first (or keep searching after a reading-only hit and only return reading-only if no exact match exists).
- `build/extract_references.py:31`: `extract_furigana_words` treats each `{kanji|reading}` group as a separate “word,” so multi-kanji terms like multiple adjacent furigana groups are split into multiple cross-references. Impact: broken/incorrect related-word links. Suggested fix: parse contiguous furigana groups + kana into a single token (reuse the logic from `extract_word_after_keyword` or implement a small tokenizer).

## Medium (consider fixing)
- `build/extract_references.py:59`: `extract_word_after_keyword` preserves katakana in the extracted reading; schema and resolution expect hiragana. Impact: extracted refs for katakana words can fail validation or remain unresolved. Suggested fix: normalize readings to hiragana (e.g., `normalize_reading`) before returning/adding refs.
- `build/resolve_links.py:69`: `normalize_legacy_reference` assumes new `00000_romaji` IDs and uses `parts[1]` as romaji, which mis-parses legacy `romaji_00000` IDs. Impact: legacy string references may never resolve and stay pending. Suggested fix: detect which segment is numeric and use the non-numeric portion(s) as romaji, or validate via regex.

## Low (nice to have)
- `docs/search.js:74`: result rendering uses `innerHTML` with unescaped `entry.headword/reading/gloss`. Impact: markup breakage or XSS risk if data ever contains `<` or `&`. Suggested fix: build DOM nodes and set `textContent`, or escape before concatenation.

## Suggestions (improvements/refactoring)
- `docs/search.js:15`: `detectQueryType` routes romaji to English when length > 10, which misclassifies longer romaji words. Suggested fix: classify by character set only, or attempt both romaji/english and merge results.
- `build/resolve_links.py:57`: legacy reference normalization scans the entire reading index per ref. Suggested fix: use `id_index` (already built) for O(1) lookup and only fall back to parsing if missing.

## Open questions/assumptions
- Assuming cross-reference readings are required to be hiragana per schema and validation; if katakana readings are intended to be valid, the schema and validators may need adjusting instead of normalization.
- Assuming legacy `romaji_00000` IDs still appear in data; if they have been fully migrated, the legacy-parsing issue is lower priority.
