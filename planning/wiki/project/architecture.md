# Architecture and Build System

**Last updated**: 2026-06-06

## Overview

je-dict-1 is a static site generated from JSON source files. The architecture has three layers:

1. **Source entries** — JSON files in `entries/` organized by ID range
2. **Build pipeline** — Python scripts in `build/` that validate, transform, and generate HTML
3. **Static site** — Generated HTML/CSS/JS in `docs/` served by GitHub Pages

Around this core, a second architecture has grown up for editorial work: a claim-based task queue, an orchestrator that launches parallel Claude CLI sessions, a multi-model review pipeline, and a cluster of consistency and quality dashboards. These were added during the Enhancement Plan 2026 (see `enhancement/enhancement-plan-2026-04-09.md`), which was completed in a single-day bootstrapping sprint and is now the operational backbone of the project.

## Directory layout

```
entries/          # Source JSON, subdirectories by 500-ID range (entries/00000/, entries/00500/, ...)
docs/             # Generated static site (never edit by hand)
build/            # Python build scripts, templates, schema, tests
  build/data/     # Static data files (semantic fields, learner scenarios)
kanji/            # Kanji index data (JSON mapping kanji to entry IDs)
articles/         # Expository article source JSON (pilot feature)
reviews/          # Multi-model review reports (per-entry JSON)
pipeline/         # Task queue, orchestrator, monitor, status tracking
polishing/        # Progress tracking + priority files + session logs for polish tasks
prompts/          # Task prompts for LLM sessions
enhancement/      # Completed enhancement plan, per-phase implementation prompts
planning/         # This knowledge base and project planning
```

## Entry file structure

Each entry lives at `entries/{range}/{id}_{romaji}.json` where:
- `{range}` = ID rounded down to nearest 500 (e.g., ID 10327 → `entries/10000/`)
- `{id}` = zero-padded 5-digit number
- `{romaji}` = reading concatenated in romaji (no internal underscores for word boundaries)

IDs are permanent — they form part of the entry's URL on the live site and must never change.

## Core build pipeline

The core build sequence (`make build`):

1. **`validate.py`** — Checks all entries against `build/schema.json`. Catches structural errors, missing fields, invalid tags. Supports `--range START END` for faster validation of a slice.
2. **`update_indexes.py`** — Rebuilds `entries_index.json`, syncs `candidate_words.json`, generates `build/word_id_lookup.json` for inline-link resolution.
3. **`build_flat.py`** — Generates the static site in `docs/`. Entry pages via `entry_renderer.py`, navigation pages via `page_generators.py`, search index via `search_index_builder.py`, article pages via `article_renderer.py`.

Incremental builds (`build_flat.py --quick`) only regenerate changed entries, which is much faster for iterative work.

## Key build scripts

### Validation and generation
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
| `get_entry_path.py` | Correct file path for an entry |
| `get_timestamp.py` | UTC timestamp for metadata |

### Quality dashboards and auditing
| Script | Purpose |
|--------|---------|
| `report.py` | Unified health dashboard (tiers, POS, cross-refs, symmetry, examples, links, furigana, note quality, POS-section completeness, multi-model review, polishing progress, candidates, consistency, recent activity) |
| `check_consistency.py` | Entry consistency checker (note structure, transitivity, length, examples) with `--json` and `--fix-list` modes |
| `score_note_quality.py` | Note quality scorer (0-100) with POS-specific templates |
| `find_merge_candidates.py` | Detect duplicate/variant entries, asymmetric cross-refs, duplicate IDs |
| `check_semantic_clusters.py` | Lint transitivity/antonym/keigo clusters for missing links |
| `find_missing_transitivity.py` | Report verbs missing transitivity data |
| `audit_tiers.py` | Tier outlier detection |
| `audit_semantic_field.py` | Semantic field coverage audit |
| `analyze_scenarios.py` | Learner scenario gap analysis |

### Prioritization and review
| Script | Purpose |
|--------|---------|
| `prioritize_polishing.py` | Generate per-task priority lists under `polishing/priority/` |
| `review_runner.py` | Multi-model review via OpenRouter (two passes: cheap screening, then deep review of flagged entries) |
| `generate_word_lookup.py` | Build `word_id_lookup.json` for inline link lookups |

## Shared data files

Several JSON files shape editorial decisions without being part of the static site itself:

- `build/data/semantic_fields.json` — definitions of semantic fields for coverage auditing. Generated from per-category files under `build/data/semantic_fields/` via `assemble_semantic_fields.py`.
- `build/data/learner_scenarios.json` — definitions of real-world learner scenarios. Generated from `build/data/learner_scenarios/` via `assemble_learner_scenarios.py`.
- `candidate_words.json` — queue of candidate entries to be written.
- `entries_index.json` — master index of entries (id, headword, reading, tier, POS) used by the build.
- `build/word_id_lookup.json` — map of surface/base forms to entry IDs for inline links.

## Parallel and orchestrated editorial work

The `pipeline/` directory hosts the infrastructure for running multiple editorial sessions concurrently.

### Task queue (`pipeline/task_queue.py`)

A claim-based JSON queue. Each task is `{entry_id, task_type, status, session_id, claimed_at}`. Agents `claim` a batch, process it, then `complete` (or `release` on failure). `populate` scans entries for work that matches each task's predicate (e.g., verbs without transitivity data). `cleanup` reclaims stale claims.

The queue avoids the file-level conflicts that progress-file-based polishing would cause when two sessions run simultaneously: an entry can only be claimed by one session at a time.

### Orchestrator (`pipeline/orchestrator.py`)

Launches Claude CLI sessions in parallel, each of which claims tasks from the queue and processes them on a dedicated branch. Enforces a daily budget cap (`pipeline/budget.json`), a circuit breaker after 3 consecutive failures, and a lock file to prevent multiple orchestrator instances. `auto_merge` defaults to false — branches are left for curator review.

### Monitor (`pipeline/monitor.py`)

A real-time dashboard over the task queue, budget, and session logs. Supports `--json` for machine consumption.

### Entry locking (`build/entry_lock.py`)

Advisory locks over ID ranges, used by sessions that process blocks of contiguous entries (rather than queue-claimed entries). Locks expire after 30 minutes. Complements the task queue for workflows that are still progress-file-based.

## Multi-model review pipeline

`build/review_runner.py` sends entries to multiple frontier models via OpenRouter and stores per-entry reports under `reviews/`:

- **Pass 1 (screening)** — cheap bulk review flagging candidate issues; results under `reviews/screening/`.
- **Pass 2 (deep review)** — flagged entries re-reviewed by stronger models; results at `reviews/{entry_id}.json`.
- **Polishing integration** — `polish_cross_model_review.md` processes flagged entries, applying or rejecting suggested corrections.

Phase 1 calibration results are in `reviews/calibration_report.md`. The pipeline is the operationalization of the design in [Multi-Model Proofreading](../ideas/multi-model-proofreading.md).

## Polishing priority

`prioritize_polishing.py` produces ordered entry-ID lists under `polishing/priority/{task}.txt`. Polishing prompts consult these lists when present and fall back to sequential ID order otherwise. This lets quality work attack the worst entries first rather than waiting for a round-robin pass to reach them.

## Expository articles (pilot)

`articles/` contains JSON source for standalone expository articles (counters, keigo, onomatopoeia). These are validated against `build/article_schema.json` and rendered via `article_renderer.py`. The pilot set is three articles; see [Expository Articles](../ideas/expository-articles.md).

## Session continuity files

Two repo-root files support session startup:

- `PROJECT_STATUS.md` — rolling log of recent sessions and project state. Keeps the five most recent change entries; older content is rotated to `PROJECT_STATUS-archive.md`.
- `PROJECT_CONTEXT_BRIEF.md` — concise session-start reference (counts, critical rules, essential commands). Regenerated by `pipeline/update-brief.py` at session start and after each merge to main.

## Deployment

The `docs/` directory is deployed via GitHub Pages. Every merged PR that includes rebuilt `docs/` files triggers a site update. This is why build artifacts must be committed — without them, the live site doesn't update.

## CI/CD

GitHub Actions (`.github/workflows/validate.yml`) runs `validate.py` on every push. The pipeline workflow (`pipeline.yml`) handles automated batch tasks, including regenerating `PROJECT_CONTEXT_BRIEF.md` after merges.

## Search

Client-side search built on a pre-generated JavaScript index. The search index includes headwords, readings, glosses, and tags. Search is implemented in `build/templates/search.js` and `build/templates/tag-search.js`. See [Digital Dictionary UX](../research/digital-dictionary-ux.md) for the proposed search enhancements.

## Implications for multilingual versions

The proposed Japanese→multilingual expansion ([Multilingual Dictionary](../ideas/multilingual-dictionary.md))
extends this architecture rather than replacing it; the current static-from-JSON shape is
unusually well suited to it because the schema isolates the invariant Japanese spine from the
translatable fields. The concrete points where this build system would change:

- **Source layer stays put.** `entries/**` remains the English/invariant canonical source.
  Translations live in a parallel **sidecar** tree (`translations/<lang>/…`), validated by a
  new `translation_schema.json` and a `validate.py --lang` mode — the worked design is
  [Translation Sidecar Design](../ideas/translation-sidecar-design.md).
- **Build pipeline gains a language axis.** `build_flat.py --lang`/`--all-langs` joins
  canonical + sidecar; `entry_renderer.py` renders the chosen language with English field-level
  fallback and emits the `hreflang` cluster + language toggle; `search_index_builder.py` splits
  into a shared spine index + per-language gloss overlay; `page_generators.py` decides which
  navigation pages get per-language variants.
- **The static-host constraint is the binding one.** This site is already **~492 MB / ~31,454
  HTML files** (measured 2026-06-06), and GitHub Pages caps published sites at **1 GB**. Full
  per-language static rendering therefore reaches the ceiling at the *first* additional
  language — so the delivery design ([Multilingual Rendering and Delivery Architecture](../topics/multilingual-rendering-architecture.md))
  recommends a size-controlled hybrid and flags a hosting decision before a third language.
- **A staleness obligation joins the pipeline.** Because the English entry is the pivot and is
  polished daily ([Content Pipeline](content-pipeline.md)), a `check_translation_staleness.py`
  step and a per-language re-translation queue become part of the maintenance loop, and
  `report.py` gains a TRANSLATION COVERAGE block — all modeled on the existing review-queue /
  dashboard patterns above.

None of this is built; it is recorded here so the architecture page reflects the planned
extension and points at the worked designs.

## Related pages

- [Entry Design](entry-design.md)
- [Content Pipeline](content-pipeline.md)
- [Parallel Agent Architecture](../ideas/parallel-agent-architecture.md) — the design document that motivated the queue/orchestrator layer
- [Multi-Model Proofreading](../ideas/multi-model-proofreading.md) — the design document behind the review pipeline
- [Deterministic vs. Semantic Tasks](../topics/deterministic-vs-semantic-tasks.md) — which parts of the pipeline are programmatic and which require LLM judgment
- [Multilingual Dictionary](../ideas/multilingual-dictionary.md) — the planned Japanese→multilingual expansion this build system would extend
- [Translation Sidecar Design](../ideas/translation-sidecar-design.md) — the sidecar storage + staleness layer the build pipeline would join against
- [Multilingual Rendering and Delivery Architecture](../topics/multilingual-rendering-architecture.md) — the per-language rendering/delivery design and the GitHub Pages size constraint that binds it
