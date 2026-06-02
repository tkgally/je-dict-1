# Enhancement Plan 2026: Retrospective and Post-Implementation State

**Last updated**: 2026-05-31

## Overview

On 2026-04-09 the curator drafted a 16-item comprehensive enhancement plan (`enhancement/enhancement-plan-2026-04-09.md`). The plan grew directly from wiki pages that had accumulated over previous maintenance sessions — especially `topics/deterministic-vs-semantic-tasks.md`, `ideas/parallel-agent-architecture.md`, `ideas/multi-model-proofreading.md`, `topics/entry-consistency.md`, and the tier reassessment thread in `project/vocabulary-tiers.md`. All 16 items were implemented and merged on the same day (see `enhancement/tracking.md`).

This page is a post-hoc synthesis: what was built, what held up to contact with reality, where gaps remain, and what the wiki should direct future work toward. It exists so that subsequent maintenance sessions have a single entry point into the delta between "the project described in 2026-04-08 wiki pages" and the project that exists today.

## What was built

### Content-quality infrastructure (plan items 01-05, 07-10)

| Phase | Output | Replaces / enables |
|-------|--------|--------------------|
| 01 | Auto-refresh `PROJECT_CONTEXT_BRIEF.md`, session continuity prompts, `validate.py --range`, `validate-changed` | Stale brief counts; slow full-corpus validation |
| 02 | `find_missing_transitivity.py`, `polish_verb_transitivity.md` | Verb transitivity polish only had a semantic-labels prompt |
| 03 | `polish_aspect_notes.md` | No dedicated ている pass existed |
| 04 | POS note templates, `score_note_quality.py`, `--score` field in consistency tooling | Notes were assessed only ad hoc |
| 05 | Symmetry report, `check_semantic_clusters.py`, cluster-mode review | Cross-refs created one entry at a time |
| 07 | `build/data/semantic_fields.json` + per-category source files, `audit_semantic_field.py`, `assemble_semantic_fields.py` | Field coverage was not measurable |
| 08 | `build/data/learner_scenarios.json` + per-category source files, `analyze_scenarios.py` | No structural view of scenario completeness |
| 09 | Tier reassessment prompt (`audit_vocabulary_tiers.md`), audit report | Tier assignments had never been systematically reviewed |
| 10 | `check_consistency.py`, expanded `report.py` dashboard with note quality, symmetry, POS-section completeness, polishing progress, multi-model review, consistency summary | Health signal was scattered across many ad-hoc scripts |

### Workflow scaling (plan items 06, 11, 13, 16)

| Phase | Output | Replaces / enables |
|-------|--------|--------------------|
| 06 | `prioritize_polishing.py`, `polishing/priority/{task}.txt`, priority-aware polishing prompts | Linear ID-order processing always did the worst entries last |
| 11 | Entry locking (`build/entry_lock.py`), parallel-safe prompt variants, range-directive guidance in CLAUDE.md, `parallel_coordinator.py` | Sequential sessions only |
| 13 | `pipeline/task_queue.py` (claim/complete/release), `queue_polishing_template.md` | File-level conflicts on `progress.txt` prevented parallel polishing at scale |
| 16 | `pipeline/orchestrator.py`, `pipeline/monitor.py`, `pipeline/budget.json`, circuit breaker, single-instance lock, auto_merge default-off | Curator had to start every session manually |

### Cross-model proofreading (plan items 12, 14)

| Phase | Output |
|-------|--------|
| 12 | `review_runner.py`, initial OpenRouter integration, calibration report (`reviews/calibration_report.md`), `polish_cross_model_review.md` |
| 14 | Two-pass architecture: cheap screening (`reviews/screening/`) + deep review on flagged entries (`reviews/{entry_id}.json`); `queue.txt` queue updated by CI |

### Expository articles (plan item 15)

Three pilot articles (counters, keigo, onomatopoeia) with JSON source under `articles/`, schema (`build/article_schema.json`), and renderer (`build/article_renderer.py`). This is the smallest of the Enhancement Plan deliverables and the one whose curve of value is least clear; see [Expository Articles](../ideas/expository-articles.md) for the design logic and open questions.

## What the plan validated

Several long-standing wiki hypotheses survived contact with reality:

1. **"Automate detection, not decision" holds.** Every deterministic script built (transitivity, note quality, consistency, symmetry, semantic fields, scenarios) produces a *report* or *priority list*; the editorial act is still done by an LLM reading the report and choosing what to change. The boundary drawn in [Deterministic vs. Semantic Tasks](deterministic-vs-semantic-tasks.md) proved durable under pressure.
2. **Claim-based coordination was the right choice.** Option C in the `parallel-agent-architecture.md` analysis won out over branch-per-agent or ID-partitioning. The queue is the coordination point; branches are short-lived; `auto_merge` defaults off so the curator can review.
3. **Shared files are the real scaling bottleneck.** `entries_index.json`, `candidate_words.json`, `docs/`, and `progress.txt` all needed distinct handling: generated on main (index, docs), modified only by one session type (candidates), replaced entirely by the queue (progress). The design writeup anticipated each of these.
4. **Two-pass review is cost-justified.** Deep review on flagged entries only, not the full corpus, keeps OpenRouter spend bounded while preserving the signal.
5. **Priority-based polishing matters.** Running `make priorities` and feeding polishing prompts from worst-first lists visibly improves the average entry during a session in a way that round-robin never did.

## What the plan under-specified

Several things the plan glossed over have become visible as the new infrastructure runs:

### 1. Queue population policy

The plan specified "populate for work that matches each task's predicate." The predicate for some tasks (e.g., *which* verbs need aspect notes, *which* notes are "too short") requires semantic judgment that the populator doesn't have. Current behavior approximates this with thresholds (note-length cutoffs, presence/absence of transitivity tags). A better populator would use the note quality scorer and the multi-model screening results, but the cross-feeds aren't yet wired up.

### 2. Budget accounting granularity

`pipeline/budget.json` caps total daily spend. It doesn't allocate across task types, so a chatty task could exhaust the budget and starve higher-value tasks. Per-task budget pools would help.

### 3. "Regression from parallel runs" hasn't been audited

The parallel architecture document named "regression — an agent makes a change that undoes a previous improvement" as a risk. There is no automated detector for this. A diff-watcher that compares successive agent edits to the same entry could flag regressions, but nothing in the Enhancement Plan built one.

### 4. Consistency checker as a gate vs. a report

`check_consistency.py` produces a report. It is *not* currently a CI gate. The health dashboard shows 2,820 note-structure issues, 7,731 asymmetric references, etc. — numbers that drift rather than monotonically decrease. Making the checker a gate on *new* entries (while leaving historical entries as report-only) would prevent new debt.

### 5. Multi-model review feedback loops

Screening results flag entries, deep review produces suggestions, the polishing prompt applies/rejects. There is no signal yet from "applied vs. rejected" back into model calibration. Over time that signal would tell us which models to trust on which issue types.

## Quality metrics: where we are vs. where the plan aimed

From the 2026-04-09 plan's target table, compared against `make report` on 2026-06-02 (28,403 entries):

| Metric | Plan target | 2026-06-02 | Notes |
|--------|-------------|------------|-------|
| Verbs with transitivity | 100% | ~32.4% | ~4,748 verbs still missing; transitivity queue slowly progressing |
| Entries with note score ≥ 60 | 80% | ~84% | Target reached |
| Cross-reference symmetry | 98% | ~41.1% | 7,824 asymmetric directed refs; largest remaining gap |
| Verbs with ている docs | 80% (of those needing it) | 17.1% | aspect-notes queue at entry 02317 |
| Multi-model review coverage | 100% (furigana) | 0.4% (queue: ~18,704) | Queue growing as entries outpace review |
| Examples per entry (avg) | ≥ 4 | 3.9 | Near target; **~112,108 total examples** |
| Cross-references per entry | ≥ 0.5 | 0.57 | **Target reached**; stable at 0.57–0.58 |
| Parallel sessions | 2–4 | Infrastructure ready | Actual utilization TBD |

Three targets have been met (note quality, examples, cross-reference density). Three are making steady progress (aspect notes, multi-model review, priority polishing throughput). Two remain well below target (transitivity, symmetry) and should drive the next round of work. **Cross-reference density is at 0.57 per entry**, stable as new entries and cross-references grow in proportion. Total cross-references have reached 16,265. Of 18,748 directed references, approximately 41.1% are symmetric — 7,824 asymmetric directed references remain.

## Implications for future maintenance sessions

### For content polishing
- The three biggest remaining gaps — transitivity, symmetry, cross-reference density — are all amenable to the queue + priority infrastructure. The next curator-directed sprint might do the same one-day push against these, now that the tooling exists.
- Note-structure issues (2,820) and example-count gaps are smaller buckets where a completionist pass is feasible.

### For tooling
- Wire the note quality scorer and multi-model screening results into the queue populator so prioritization uses quality signal, not just field presence/absence.
- Add per-task budget pools to `pipeline/budget.json`.
- Promote `check_consistency.py` to a CI gate on new-only issues.
- Build a diff-watcher that flags agent-on-agent regressions in the same entry.

### For the wiki
- The `ideas/` pages for [Parallel Agent Architecture](../ideas/parallel-agent-architecture.md) and [Multi-Model Proofreading](../ideas/multi-model-proofreading.md) now carry implementation-status banners. Future sessions should either migrate their "open questions" sections into new `open-issues.md` entries as those questions get resolved, or annotate them with answers.
- The tier reassessment thread in [Vocabulary Tier System](../project/vocabulary-tiers.md) was addressed by Enhancement Phase 9 but the audit report hasn't driven any actual tier changes. A followup: summarize the audit's findings in a dedicated wiki page and document which reclassifications (if any) were ultimately applied.
- Expository articles need more content before the pattern can be evaluated as a feature. This is a wiki-curatable question: should the next five articles be chosen by semantic field coverage, by scenario value, or by learner-query analysis?

## Related pages

- [Architecture and Build System](../project/architecture.md) — the current system description (post-enhancement)
- [Content Pipeline](../project/content-pipeline.md) — the updated pipeline description
- [Deterministic vs. Semantic Tasks](deterministic-vs-semantic-tasks.md) — the design philosophy the plan implemented
- [Parallel Agent Architecture](../ideas/parallel-agent-architecture.md) — the design doc, now marked implemented
- [Multi-Model Proofreading](../ideas/multi-model-proofreading.md) — the design doc, now marked implemented
- [Entry Consistency](entry-consistency.md) — consistency problems that motivated the checker
- [Cross-Reference Design](cross-references.md) — the cluster-linting and symmetry ideas now realized
