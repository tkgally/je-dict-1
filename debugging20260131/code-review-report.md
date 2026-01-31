# Code Review Report: je-dict-1

## Critical (must fix)
- None found.

## High (should fix)
- None found.

## Medium (consider fixing)
- `build/update_entries_index.py:41` + `build/build_sitemap.py:139` — `entries_index.json` stores OS-native paths; on Windows this becomes backslashes, and sitemap URLs will embed `\` which are invalid in URLs. Impact: broken sitemap entries (and any tooling that expects URL paths). Fix: write POSIX-style paths in the index (`entry_path.relative_to(project_root).as_posix()`), or normalize in sitemap generation.
- `build/build_flat.py:3693` + `build/build_kanji_json.py:61` + `build/build_sitemap.py:128` — `build_flat.py` rebuilds kanji JSON/HTML and sitemap using `entries_index.json`, but doesn’t refresh `entries_index.json` itself. Impact: running `build_flat.py` directly after entry edits can generate inconsistent kanji pages/sitemaps (stale/missing entries). Fix: either call `update_entries_index.py` inside `build_flat.py` or pass the in‑memory `entries` list to those builders and avoid the file dependency.
- `build/resolve_links.py:46-75` — `normalize_legacy_reference` linearly scans `reading_index` for IDs and, on fallback, uses only `parts[1]` of `ref.split('_')`. If IDs contain multiple underscores (multiword romanization), this drops segments and yields incorrect readings; plus the scan is O(N) per ref. Impact: wrong or unresolved legacy references; slow on large ref sets. Fix: build and use an `id_index` for O(1) lookup, and derive romaji with `'_'.join(parts[1:])`.

## Low (nice to have)
- `build/build_kanji_html.py:338-343` — Uses cwd-relative paths and `output_dir.mkdir(exist_ok=True)` without `parents=True`. Impact: running the script outside the repo root or when `docs/` doesn’t exist throws `FileNotFoundError`. Fix: derive paths from `Path(__file__).parent.parent` and `mkdir(parents=True, exist_ok=True)`.
- `docs/tag-search.js:167-176` — When there are 0 results, the UI displays “showing 1-0”. Impact: confusing UX. Fix: guard `total === 0` and render “showing 0-0” (and optionally a “no results” message).

## Suggestions (improvements/refactoring)
- `build/build_kanji_html.py` + `build/japanese_utils.py` — There’s duplicate romaji→kana conversion logic; consider centralizing in `japanese_utils.py` to avoid drift.
- `docs/search.js` — Search scans all keys each time. If search performance becomes an issue with growth, consider a prefix index or precomputed token maps to avoid O(N) scans.

## Open questions / assumptions
- I assumed entry IDs may include multiple underscores for multiword readings; if that’s not true, the `normalize_legacy_reference` parsing issue is less critical.
- I assumed Windows builds are possible; if builds are always on Unix, the path-separator sitemap issue is lower priority.
