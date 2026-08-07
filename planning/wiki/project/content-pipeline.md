# Content Pipeline

**Last updated**: 2026-08-07 (added the CI-outage incident record and the recovery
procedure that actually worked)

## Overview

Entries flow through a multi-stage pipeline from discovery to publication:

```
Candidate Discovery → Candidate Queue → Entry Creation → Validation → Polishing → Publication
```

Each stage has its own tools, prompts, and quality gates.

## Stage 1: Candidate discovery

New words are identified and added to `candidate_words.json`. The primary method is now **LLM-based brainstorming**:

- **LLM brainstorming** (primary) — `prompts/brainstorm-new-candidates.md` runs an automated pipeline that seeds an external LLM (via OpenRouter) with existing dictionary words and asks it to suggest related words that are missing. Explores synonyms, antonyms, same-field words, kanji compounds, register variants, collocational partners, and situationally related words. Produces large batches of candidates efficiently with built-in deduplication. See [Word Discovery Strategies](../ideas/word-discovery-strategies.md) for analysis of this and other approaches.
- **Manual identification** — the curator notices gaps in coverage
- **Corpus harvesting** — processing frequency lists to find missing common words (`prompts/corpus_harvesting.md`); an earlier approach that has been largely superseded by brainstorming
- **Systematic search** — scanning for words in specific semantic domains (`prompts/newcandidates.md`)
- **Cross-reference gaps** — words mentioned in existing entries but lacking their own entry
- **No-entry link detection** — words marked `noentry` in inline links (`prompts/polish_add_entries_for_noentry_example_words.md`)
- **"Seen in entry" internal-completeness candidates** — words already referenced inside existing entries (examples, notes, collocations) but lacking their own entry. These are flagged when candidates are added with a `seen_in_entry` field and are prioritized during entry creation because filling them improves internal cross-linking. As of June 2026, this is one of the most productive candidate sources.

Candidates are managed via `build/manage_candidates.py` (add, check, sync, stats).

## Stage 2: Entry creation

Entries are created in batch sessions of ~20-25 entries each, following `prompts/newentries.md`:

1. Duplicate check (`check_duplicate.py`)
2. Get next ID (`get_next_id.py`) — run fresh before every entry
3. Get timestamp (`get_timestamp.py`)
4. Write entry JSON following the appropriate skill (verb-entry, adjective-entry, etc.)
5. Post-batch validation, conjugation generation, index update, site build

Per-field budgets follow a compact reference shape: top-level glosses 3-8 words, notes scoped to 2-3 focused sections. As of June 2026, entry creation sessions typically produce 20-25 entries and prioritize "seen in entry" internal-completeness candidates.

## Stage 3: Polishing

Created entries are improved through iterative polishing passes. There are two coexisting polishing modes:

**Progress-file mode** (original) — each task has `polishing/tasks/{task}/progress.txt` recording the next entry ID to process. Sessions resume sequentially from there.

**Queue mode** (post-enhancement) — tasks are placed on `pipeline/task_queue.json` by `pipeline/task_queue.py populate`. Sessions `claim` a batch of tasks, process them, then `complete`. This avoids conflicts when multiple sessions run in parallel. See `queue_polishing_template.md`.

### Unified Improvement Routine v2 (the scheduled driver)

As of June 2026, the **primary scheduled task** is `prompts/routine2.md` — the "Verified Routine" — which supersedes running `comprehensive_polish.md` directly on a schedule. Each Routine run does **one focused unit of work** chosen by a deterministic selector (`pipeline/routine_next.py`), currently rotating among five modes:

| Mode | What it does |
|------|-------------|
| `polish` | Comprehensive polish in two lanes: **priority lane** (worst-scoring entries first, from `polishing/priority/notes.txt`) then **frontier lane** (sequential from `comprehensive_polish.md` progress file). Typically ~20–30 entries per run. |
| `new-entries` | Creates ~20 entries from `candidate_words.json`, preferring "seen in entry" candidates. |
| `accuracy-review` | Runs `review_runner.py` + `review_accuracy.py` over a range; applies/rejects flags; drains `reviews/queue.txt`. |
| `systemic-fix` | Works one open item from `planning/wiki/ideas/backlog-queue.json` with per-entry semantic verification. |
| `wiki` | Harvests `polishing/observations.md`, runs 2–4 wiki activities, maintains the knowledge base. |

The Routine adds two quality gates absent from the individual prompts:

1. **§4 self-verification** — every run that creates or modifies entries sends exactly those entries to an independent model (via OpenRouter, ~$0.01/25 entries) before the single `make build`. Issues are adjudicated (APPLY / REJECT / FLAG) and logged to `reviews/decisions.jsonl`.
2. **§5 metrics snapshot** — every run appends one line to `pipeline/metrics-history.jsonl` (mode, entries changed, flags applied/rejected, dictionary-wide counters, OpenRouter spend). This makes quality trends measurable over weeks. See [Quality Metrics Trend](../topics/quality-metrics.md).

The selector persists its rotation state in `pipeline/routine-state.json`; tuning knobs (mode weights, OpenRouter caps) are in `pipeline/routine-config.json`. Daily OpenRouter spend is capped at $5 via `pipeline/openrouter-ledger.json`.

### Targeted polishing tasks (still runnable manually)

| Task | Prompt | What it does |
|------|--------|-------------|
| **Comprehensive** | `comprehensive_polish.md` | Unified checklist; up to 5 entries per session; run by Routine `polish` mode. Logs observations to `polishing/observations.md`. |
| Inline links | `polish_add_inline_links.md` | Add ⟦...⟧ cross-reference links |
| Example sentences | `polish_example_sentences.md` | Check count, quality, tier compliance |
| Furigana completeness | `polish_furigana_completeness.md` | Find and add missing furigana |
| Furigana correctness | `polish_furigana_correctness.md` | Verify readings are correct |
| Semantic labels | `polish_semantic_labels.md` | Verify tags match meanings |
| Short notes | `expand-short-notes.md` | Expand inadequate notes |
| Verb transitivity | `polish_verb_transitivity.md` | Add transitivity tags, notes, and pair links |
| Aspect notes | `polish_aspect_notes.md` | Document non-obvious ている behavior |
| Cross-model review | `polish_cross_model_review.md` | Apply or reject multi-model proofreading suggestions |

**Priority ordering**: `make priorities` writes ordered ID lists to `polishing/priority/{task}.txt`. When a priority file exists, polishing prompts process entries worst-first rather than sequentially by ID.

### Review queue

`reviews/queue.txt` lists entries that have changed since their last cross-model review (maintained by CI — every push re-adds changed entry paths). As of June 2026, the queue holds ~19,400 entries (~67% of the dictionary). This is **structural, not a convergence target**: every polishing or creation session adds new entries to the queue, while `accuracy-review` runs drain roughly 150–200 entries per run. The queue is best understood as a surveillance instrument that ensures every recently-changed entry eventually gets a second opinion, not a backlog that polishing will burn down. See [Quality Metrics Trend](../topics/quality-metrics.md) for the measured drain rate.

## Stage 4: Consolidation

Periodic maintenance to keep entries clean:

- **Duplicate detection** — `find_merge_candidates.py` identifies entries that should be merged
- **Cross-reference addition** — `prompts/add_cross-references.md` systematically links related entries
- **Candidate cleanup** — `prompts/clean_up_candidates_list.md` reviews the candidate queue

## Automated pipeline and orchestration

The `pipeline/` directory contains:

- `run-pipeline.sh` and `recommend-tasks.py` — batch execution and task recommendation
- `task_queue.py` — claim-based task queue for parallel agents
- `orchestrator.py` — launches parallel Claude CLI sessions against the queue, enforcing a daily budget and a circuit breaker
- `monitor.py` — real-time dashboard over sessions, queue, and budget
- `update-brief.py` / `update-status.py` — regenerate `PROJECT_CONTEXT_BRIEF.md` and `PROJECT_STATUS.md` metadata

`make orchestrate` starts the orchestrator loop; `make monitor` shows the dashboard. Budget, circuit breaker, and a single-instance lock file prevent runaway cost or duplicated agents.

## Quality gates

Every stage has validation:
- **Schema validation** — `validate.py` checks structure against `build/schema.json`
- **Tag validation** — `validate_tags.py` checks semantic/POS tag consistency
- **Furigana check** — `find_missing_furigana.py` catches unmarked kanji
- **Duplicate check** — `check_duplicate.py` prevents duplicate entries
- **CI** — GitHub Actions runs validation on every push

### The 2026-08-06 CI outage — an incident record, and what actually recovered it

On 2026-08-06 a `systemic-fix` run reported that "GitHub Actions has dispatched no workflow
run repo-wide since 2026-08-06 15:50 UTC" and that "three consecutive Routine runs have now
been unable to reach the §7 CI gate". Two PRs (#3130, #3131) were left open with
`total_count: 0` check runs and hand-written "do not sweep me" comments. The proposed fix was
to add `workflow_dispatch:` to `validate.yml`'s `on:` block so a stranded run could
re-trigger its own checks.

The 2026-08-07 wiki run measured it against the workflow-run history rather than filing it,
and all three parts of the picture changed:

**The outage was real and is bounded.** `Validate Entries` runs form an almost perfectly
regular series — one per Routine run, ~2.5–3.5 h apart, 30 of the last 30 concluding
`success`. There is exactly one gap in it: **2026-08-06T15:43Z → 2026-08-07T00:37Z, 8 h 54 m**,
about three scheduled slots. The `total_count: 0` observation is the strong evidence, because
a PR that exists with zero check runs cannot be explained by "no PR was opened".

**The outage is over.** Three consecutive `Validate Entries` runs since the gap (00:37, 03:28,
06:36 on 2026-08-07) all completed `success`, alongside the usual push-triggered `Update
Brief` and `Queue Reviews` on main. Whatever it was, it was on GitHub's side and it
self-resolved; nothing in the repository was changed to fix it.

**No work was lost, and the thing that saved it is not written down anywhere.** #3130 and
#3131 never merged as themselves — main's history goes #3129 → #3132 — but their content is
on main: `build/check_link_baseform.py` is present, and both 的 repairs the batch made
(00445 開放的, 02627 外交的な) now point at `09839_teki`. The next run **fetched the stranded
branch and absorbed its commits into its own branch**, so the work rode in under #3132 and
got CI coverage there. That is the recovery procedure, it is proven, and it should be the
documented response to a stranded PR whose checks never appear:

> When a PR has `total_count: 0` check runs and the head branch is not the branch you are on,
> merge that branch into your own before pushing. Its commits get CI coverage under your PR
> and reach main; the stranded PR can then be closed as superseded truthfully rather than
> heuristically.

The `workflow_dispatch:` proposal survives, but as **preparedness, not repair**. Dispatched
against the PR's head branch it would attach a check run to the PR's head SHA, so
`get_check_runs` would see it — the escape hatch works. It is worth adding because the next
outage will look the same and commit absorption only works while a *later* run is still
scheduled. It is filed as [Tooling 80](../ideas/tooling-backlog.md), not as an emergency.

One further consequence for the §0b stranded-PR sweep: during the gap, two runs had to leave
manual "do not sweep me" comments because the sweep's rule — close a `claude/*` PR when the
maximum entry ID it touches is below the comprehensive frontier — misfires on `systemic-fix`
work, which touches low IDs by nature (#3130 spanned 00445–06031, all below the 6809
frontier). A sweep that fires during an outage can therefore discard exactly the work the
outage stranded. See [Tooling 81](../ideas/tooling-backlog.md).

## Session workflow

A typical entry creation session:
1. Read `PROJECT_CONTEXT_BRIEF.md` for current state
2. Create entries (with duplicate checks and fresh IDs)
3. Run validation sequence (validate → furigana → conjugation → indexes → kanji → build)
4. Update `PROJECT_STATUS.md`
5. Commit, push, PR, CI check, squash-merge, cleanup

## Related pages

- [Architecture and Build System](architecture.md)
- [Quality Standards](quality-standards.md)
- [Entry Design](entry-design.md)
- [Deterministic vs. Semantic Tasks](../topics/deterministic-vs-semantic-tasks.md) — which pipeline steps are automated and which require editorial judgment
