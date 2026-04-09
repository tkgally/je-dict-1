# Enhancement Plan Progress Tracker

Last updated: 2026-04-09

## Status Key
- `pending` — Not yet started
- `done` — Completed and merged to main
- `skipped` — Intentionally skipped (with reason)

## Progress

| # | Status | Prompt | Description | Completed |
|---|--------|--------|-------------|-----------|
| 01 | done | 01_infrastructure_quick_wins.md | Auto-refresh BRIEF, session continuity, incremental validation | 2026-04-09 |
| 02 | done | 02_verb_transitivity_tooling.md | Build find_missing_transitivity.py + polishing prompt | 2026-04-09 |
| 03 | done | 03_aspect_teiru_tooling.md | Create aspect/ている polishing prompt | 2026-04-09 |
| 04 | done | 04_note_quality_system.md | POS note templates + note quality scorer | 2026-04-09 |
| 05 | done | 05_cross_ref_symmetry.md | Cross-reference symmetry detection + cluster polishing | 2026-04-09 |
| 06 | pending | 06_polishing_priority.md | Priority-based polishing reordering | |
| 07 | pending | 07_semantic_field_audit.md | Semantic field definitions + coverage audit | |
| 08 | pending | 08_scenario_gap_analysis.md | Learner scenario definitions + gap analysis | |
| 09 | pending | 09_vocab_tier_reassessment.md | Vocabulary tier audit prompt + report | |
| 10 | pending | 10_consistency_and_dashboard.md | Consistency checker + enhanced dashboard | |
| 11 | pending | 11_parallel_safe_redesign.md | Parallel-safe prompts + entry locking | |
| 12 | pending | 12_multi_model_review_p1.md | Multi-model review Phase 1 (proof of concept) | |
| 13 | pending | 13_task_queue_system.md | Claim-based task queue for parallel agents | |
| 14 | pending | 14_multi_model_review_p2.md | Multi-model review Phases 2-3 (scaling) | |
| 15 | pending | 15_expository_articles.md | Article schema + 3 pilot articles | |
| 16 | pending | 16_automated_orchestration.md | Orchestrator + monitoring dashboard | |

## Dependencies

Prompts within the same phase have no mutual dependencies and can be run in any order.
Cross-phase dependencies (must be done first → then):

- 04 → 06 (note scorer feeds priority system)
- 04 → 10 (note templates feed consistency checker)
- 07 → 08 (semantic fields before scenarios)
- 11 → 13 (parallel-safe before task queue)
- 12 → 14 (multi-model P1 before P2)
- 13 → 16 (task queue before orchestration)
