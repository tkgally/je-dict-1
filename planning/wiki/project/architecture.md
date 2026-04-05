# Architecture and Build System

**Last updated**: 2026-04-05

## Overview

je-dict-1 is a static site generated from JSON source files. The architecture has three layers:

1. **Source entries** — JSON files in `entries/` organized by ID range
2. **Build pipeline** — Python scripts in `build/` that validate, transform, and generate HTML
3. **Static site** — Generated HTML/CSS/JS in `docs/` served by GitHub Pages

## Directory layout

```
entries/          # Source JSON, subdirectories by 500-ID range (entries/00000/, entries/00500/, ...)
docs/             # Generated static site (never edit by hand)
build/            # Python build scripts, templates, schema, tests
kanji/            # Kanji index data (JSON mapping kanji to entry IDs)
pipeline/         # Automated batch pipeline (shell scripts, status tracking)
polishing/        # Progress tracking for iterative polish tasks
prompts/          # Task prompts for LLM sessions
planning/         # This knowledge base and project planning
```

## Entry file structure

Each entry lives at `entries/{range}/{id}_{romaji}.json` where:
- `{range}` = ID rounded down to nearest 500 (e.g., ID 10327 → `entries/10000/`)
- `{id}` = zero-padded 5-digit number
- `{romaji}` = reading concatenated in romaji (no internal underscores for word boundaries)

IDs are permanent — they form part of the entry's URL on the live site and must never change.

## Build pipeline

The core build sequence (`make build`):

1. **`validate.py`** — Checks all entries against `build/schema.json`. Catches structural errors, missing fields, invalid tags.
2. **`update_indexes.py`** — Rebuilds `entries_index.json`, syncs candidate list, generates word lookup.
3. **`build_flat.py`** — Generates the static site in `docs/`. Entry pages via `entry_renderer.py`, navigation pages via `page_generators.py`, search index via `search_index_builder.py`.

Incremental builds (`build_flat.py --quick`) only regenerate changed entries, which is much faster for development.

## Key build scripts

| Script | Purpose |
|--------|---------|
| `validate.py` | Schema validation for all entries |
| `validate_tags.py` | Semantic and POS tag consistency checks |
| `build_flat.py` | Static site generation |
| `update_indexes.py` | Index and candidate list sync |
| `add_conjugations.py` | Generate verb conjugation tables |
| `add_adjective_conjugations.py` | Generate i-adjective conjugation tables |
| `find_missing_furigana.py` | Scan for kanji without furigana |
| `update_kanji_index.py` | Maintain kanji-to-entry mappings |
| `check_duplicate.py` | Pre-creation duplicate detection |
| `get_next_id.py` | Filesystem scan for next available ID |
| `report.py` | Dictionary health dashboard |
| `find_merge_candidates.py` | Detect duplicate/variant entries |

## Deployment

The `docs/` directory is deployed via GitHub Pages. Every merged PR that includes rebuilt `docs/` files triggers a site update. This is why build artifacts must be committed — without them, the live site doesn't update.

## CI/CD

GitHub Actions (`.github/workflows/validate.yml`) runs `validate.py` on every push. The pipeline workflow (`pipeline.yml`) handles automated batch tasks.

## Search

Client-side search built on a pre-generated JavaScript index. The search index includes headwords, readings, glosses, and tags. Search is implemented in `build/templates/search.js` and `build/templates/tag-search.js`.

## Related pages

- [Entry Design](entry-design.md)
- [Content Pipeline](content-pipeline.md)
