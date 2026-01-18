# Code Review Report: je-dict-1

## Critical (must fix)
- None found.

## High (should fix)
- `build/build_flat.py:840` Romaji indexing uses `hiragana_to_romaji(reading)` without normalizing katakana, so katakana/loanword entries (allowed by schema) get non-romaji keys and won’t show up in romaji search.
  - Impact: user-visible search misses results.
  - Suggested fix: normalize `reading` to hiragana (e.g., `normalize_reading`) before romaji conversion and indexing, and store that normalized romaji in `entries_data`.

## Medium (consider fixing)
- `build/validate.py:294` `datetime.fromisoformat(...)` yields naive datetimes when timestamps omit a timezone; comparing to timezone-aware `now` can raise `TypeError` and abort validation.
  - Impact: a single bad timestamp can crash `validate.py` and stop other checks.
  - Suggested fix: if `dt.tzinfo is None`, assume UTC (or treat as invalid) and catch `TypeError` to emit a warning instead of crashing.
- `build/build_flat.py:1848` `build_recent_entries` returns naive datetimes for timezone-less strings but the fallback is timezone-aware, which can raise `TypeError` during sorting.
  - Impact: recent list build can crash or misorder.
  - Suggested fix: normalize parsed timestamps to UTC when tzinfo is missing.
- `build/validate.py:172` `is_valid_hiragana` rejects iteration marks `ゝゞ` even though the schema allows them for cross-reference readings.
  - Impact: valid refs are flagged as invalid.
  - Suggested fix: align validation with the schema regex (include `\u309D`/`\u309E` or use a compiled pattern shared with schema).
- `build/extract_references.py:47` extraction regex allows katakana in readings but cross-reference schema/validator require hiragana.
  - Impact: `--apply` can generate refs that later fail validation or won’t resolve.
  - Suggested fix: normalize extracted readings to hiragana or update schema/validator to accept katakana.

## Low (nice to have)
- `build/build_flat.py:2034` error message uses a non-f-string literal "Build output remains in: {temp_dir}".
  - Impact: misleading debug output when swaps fail.
  - Suggested fix: change to `f"  Build output remains in: {temp_dir}"`.

## Suggestions (improvements/refactoring)
- `build/build_flat.py:530` search does a full key scan on each query; consider precomputing prefix maps or a trie/Map to reduce `O(n)` scans as the index grows.

## Open questions / assumptions
- Are katakana readings common in entries and notes? If yes, the romaji search and extracted cross-reference issues are user-visible; if not, consider normalizing readings to hiragana earlier to avoid drift.
- Do you enforce timezone offsets in metadata elsewhere? If not, the validation/build timestamp issues will surface as soon as one entry omits `Z`/offset.
