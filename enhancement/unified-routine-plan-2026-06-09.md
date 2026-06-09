# Unified Improvement Routine — Plan (2026-06-09)

A single scheduled prompt that, run unattended several times a day, makes steady,
balanced improvements to the dictionary's **quality, accuracy, consistency, and
usefulness** — drawing on insights accumulated in the knowledge wiki — while
preserving the dictionary's existing concept, headword range, sense inventory,
and example style.

> **Status**: proposal for curator review. Nothing here is wired up yet.
> Scope is **Japanese→English only**; the multilingual extension (simplified
> Chinese first) is explicitly deferred (see §11).

This plan reflects four design decisions confirmed with the curator on
2026-06-09:

1. **Replace all three** current scheduled tasks (comprehensive polish,
   new-entry creation, nightly wiki maintenance) with this one Routine.
2. **Quality-first** default mix (~45% polish, ~20% accuracy review,
   ~20% new entries, ~15% wiki).
3. **Weighted rotation + health nudges** for choosing each run's focus.
4. **Furigana now, extend next** for cross-model accuracy review (launch on the
   existing furigana reviewer; build gloss/definition/translation review as a
   fast-follow).

---

## 1. Why a dispatcher, not a "do-everything" prompt

Every existing scheduled prompt in this repo is deliberately **single-focus**
(`comprehensive_polish.md`, `newentries.md`, `maintain-knowledge-base.md`).
That is not an accident. The fragile part of an unattended session is the
**wrap-up**: `make build`, commit, push, create PR, wait up to ~10 min for CI,
then squash-merge. `comprehensive_polish.md` documents the failure mode plainly:
sessions that try to do too much run out of context mid-merge and **strand a
PR**, which leaves `main` un-advanced so the next session redoes the same work.
The whole "stop at ~60% context, single build, atomic merge tail" discipline
exists to prevent this.

A naive prompt that tried to check glosses *and* add links *and* create entries
*and* maintain the wiki **every run** would maximize the stranded-PR risk.

So the unified Routine is a **thin dispatcher**:

```
each run:
  0. pre-flight: sweep stranded PRs (self-healing)
  1. select ONE focus ("mode") for this run        ← pipeline/routine-next.py
  2. execute that mode with the existing per-task discipline
  3. always-on lightweight capture (candidates + observations) regardless of mode
  4. wrap up: build (if needed) → PR → wait-for-CI → squash-merge
```

Balance across the many improvement dimensions is achieved **over time, across
runs** — driven by tunable weights — not crammed into every run. With several
runs per day, a week of runs produces the quality-first mix while each
individual run stays focused enough to merge reliably.

This is a small, well-understood change in *control flow* layered on top of the
prompts and helper scripts that already work today.

---

## 2. How the curator's task list maps to modes

Everything in the request maps to a mode; nothing is dropped.

| Requested improvement | Handled by |
|---|---|
| Check/correct glosses, definitions | **accuracy-review** (Phase 2 build) + **polish** tier-1/2 |
| Check/correct example sentences + their translations | **accuracy-review** (Phase 2) + **polish** |
| Check/correct furigana | **accuracy-review** (Phase 1, furigana, available now) + **polish** tier-1 |
| Inter-entry links — inline (⟦…⟧) | **polish** tier-1 (full inline coverage) |
| Inter-entry links — cross-references | **polish** tier-2 + optional **cross-ref** sub-mode |
| Create new entries | **new-entries** |
| Enhance / improve notes | **polish** tier-2/3 |
| "Other aspects" / systemic improvements | **systemic-fix** (wiki-backlog-driven) |
| Maintain, expand, draw insights from the wiki | **wiki** + **systemic-fix** (insight→action) + consultation in every mode |

---

## 3. The modes

Five modes. Weights sum to the curator's quality-first mix. The two "polish
family" modes together make up the ~45% quality budget.

| Mode | Default weight | What one run does | Reuses |
|---|---:|---|---|
| `polish` | 0.35 | Comprehensive per-entry sweep (furigana, examples, inline links, cross-refs, notes, tags, transitivity, aspect). Advances the comprehensive cursor. | `prompts/comprehensive_polish.md` |
| `systemic-fix` | 0.10 | One targeted batch pass against a single open item from the wiki cleanup/tooling backlog (build detector if needed → run → fix flagged entries → update backlog status). | wiki backlog + `build/` scripts |
| `accuracy-review` | 0.20 | Cross-model (OpenRouter) verification under the daily $ cap, then apply/reject flagged corrections. Phase 1 = furigana; Phase 2 adds glosses/definitions/example translations. | `build/review_runner.py`, `prompts/polish_cross_model_review.md` |
| `new-entries` | 0.20 | Create ~20 entries from candidates (prefer "seen in entry"). | `prompts/newentries.md` |
| `wiki` | 0.15 | Harvest `polishing/observations.md` → backlog/articles; deepen/research pages; keep the backlog queue (§6) current. | `planning/maintain-knowledge-base.md` |

Notes:

- **`polish` delegates** — the Routine tells the session to follow
  `comprehensive_polish.md` for this run. We do **not** re-implement the tiered
  checklist inside `routine.md`; we keep one source of truth.
- **`systemic-fix` is the new capability** and the most direct embodiment of
  "draw on insights accumulated in the wiki." The sequential `polish` frontier
  is at entry ~05936 and crawls forward ~20 entries/run; many defect classes the
  wiki has already catalogued span the *entire* dictionary (e.g. the 2026-04-14
  tag-drift batch sits mostly **above** the polish frontier). `systemic-fix`
  attacks those dictionary-wide instead of waiting years for the frontier to
  reach them. See §6.
- **Cross-references**: covered inside `polish`. The selector may occasionally
  route a `polish` run to a dedicated cross-reference/symmetry pass
  (`add_cross-references.md` + `check_semantic_clusters.py` /
  `find_merge_candidates.py --asymmetry-only`) when the symmetry backlog is
  large — a `polish` sub-variant, not a separate top-level mode.

### Always-on capture (every mode)

Independent of the selected mode, every run:

- Adds any word it encounters that lacks an entry to `candidate_words.json`
  via `manage_candidates.py add "…" "…" "…; seen in entry XXXXX"`.
- Appends systemic observations to `polishing/observations.md` with the existing
  tags (`[pattern] [wiki] [article] [tooling] [skill] [entry]`).

This is what makes the loop *close*: `polish`/`new-entries` surface gaps →
`wiki` harvests them into the backlog → `systemic-fix` executes them → the
dictionary gets internally complete and consistent over time.

---

## 4. Mode selection: deterministic debt scheduler + health nudges

A small, dependency-free, unit-tested Python script
**`pipeline/routine-next.py`** chooses the mode. It is deterministic and
auditable (no hidden RNG), curator-tunable, and self-correcting.

### Algorithm (debt-based, largest-remainder)

Each mode carries a running **debt** that increases by its (nudged) weight every
run and resets to 0 when the mode is chosen. Pick the eligible mode with the
highest debt. Over many runs this makes realized proportions converge **exactly**
to the configured weights — no luck involved.

```
on each run:
  signals   = cheap_health_signals()           # see below
  weights   = base_weights * nudge(signals)     # bounded multipliers
  weights   = suppress_if_blocked(weights, signals)  # e.g. budget exhausted
  for m in modes: debt[m] += weights[m]
  eligible  = modes minus {anti-repeat set}     # avoid back-to-back heavy repeats
  choice    = argmax(debt[m] for m in eligible)
  debt[choice] = 0
  params    = mode_params(choice, signals)      # ID range, OpenRouter budget, backlog item id…
  persist(state)
  emit_json({mode: choice, params, reason, signals})
```

### Health signals (all cheap, read from files already on disk)

| Signal | Source | Nudges |
|---|---|---|
| candidate count | `candidate_words.json` | high → `new-entries` ↑; very low → `new-entries` ↓ (and flag corpus harvest) |
| "seen in entry" candidate count | grep `candidate_words.json` | high → `new-entries` ↑ (internal-completeness is high value) |
| comprehensive frontier lag | `polishing/tasks/comprehensive/progress.txt` vs max entry id | large → `polish` ↑ |
| un-reviewed range | `reviews/` coverage vs entry count; `reviews/queue.txt` | large → `accuracy-review` ↑ |
| unharvested observations | line count in `polishing/observations.md` | large → `wiki` ↑ |
| open backlog items | `planning/wiki/ideas/backlog-queue.json` (§6) | any open, batch-ready → `systemic-fix` ↑ |
| OpenRouter spent today | `pipeline/openrouter-ledger.json` (§5) | at/over cap → `accuracy-review` **suppressed** |

Nudges are **bounded** (e.g. ×0.5–×2.0) so health can tilt the mix without ever
starving a mode — this is the explicit guard against the "pure health-driven
fixates on one area" failure mode.

### Anti-repeat

Heavy modes (`new-entries`, `accuracy-review`, `systemic-fix`) are excluded from
eligibility if they ran in the immediately preceding run, *unless* their nudged
weight exceeds a high threshold (health override). Prevents two new-entry runs
back-to-back from monopolizing a quiet day.

### Curator controls

```bash
python3 pipeline/routine-next.py --dry-run     # show the choice + signals, write nothing
python3 pipeline/routine-next.py --explain     # full signal/nudge/debt breakdown
python3 pipeline/routine-next.py --force-mode polish   # override for one run
python3 pipeline/routine-next.py --simulate 50 # print the mode distribution over 50 runs
```

`--simulate` is the acceptance test: run it for, say, 7×(runs/day) and confirm
the realized proportions match the quality-first weights.

### Config and state files

**`pipeline/routine-config.json`** (curator-editable — the single tuning knob):

```json
{
  "runs_per_day_hint": 6,
  "weights": {
    "polish": 0.35,
    "systemic-fix": 0.10,
    "accuracy-review": 0.20,
    "new-entries": 0.20,
    "wiki": 0.15
  },
  "nudges": {
    "candidate_high_threshold": 400,
    "candidate_low_threshold": 80,
    "observations_unharvested_lines": 40,
    "max_multiplier": 2.0,
    "min_multiplier": 0.5
  },
  "anti_repeat_modes": ["new-entries", "accuracy-review", "systemic-fix"],
  "openrouter": { "daily_cap_usd": 5.0, "per_session_cap_usd": 1.50 }
}
```

**`pipeline/routine-state.json`** (script-managed — do not hand-edit):

```json
{
  "debt": { "polish": 0.0, "systemic-fix": 0.0, "accuracy-review": 0.0,
            "new-entries": 0.0, "wiki": 0.0 },
  "history": [ {"date":"2026-06-09T01:00Z","mode":"polish"}, "… last 20 …" ],
  "last_run_mode": "polish",
  "day_tally": { "date": "2026-06-09", "polish": 2, "new-entries": 1 }
}
```

Both live under `pipeline/`, are committed by the Routine alongside its work, and
are tiny — no merge-conflict risk because only one run executes at a time (§9).

---

## 5. OpenRouter budget: a real daily ledger

`review_runner.py` already supports `--budget AMOUNT`, but that cap is
**per-invocation and estimate-based** — it does not persist across runs, so it
cannot by itself enforce "$5 **per day** across all runs." We add a tiny ledger.

**`pipeline/openrouter-ledger.json`**:

```json
{
  "date": "2026-06-09",
  "daily_cap_usd": 5.0,
  "spent_usd": 1.42,
  "calls": [
    {"ts":"2026-06-09T01:14Z","mode":"accuracy-review","pass":"screening","est_usd":0.31}
  ]
}
```

Rules (enforced by the selector + the `accuracy-review` playbook):

1. If `date` ≠ today → reset `spent_usd` to 0 (mirrors `pipeline/budget.json`).
2. `remaining = daily_cap_usd − spent_usd`. If `remaining ≤ 0`, the selector
   sets `accuracy-review` weight to 0 (mode suppressed) for the rest of the day.
3. When `accuracy-review` runs, it calls
   `review_runner.py … --budget min(remaining, per_session_cap_usd)` so a single
   run can never blow the daily cap, and quiet days spread spend across runs.
4. After the run, the Routine appends the run's reported estimate to `calls` and
   adds it to `spent_usd`.

This keeps the dictionary's *Claude* session spend (governed separately by
`pipeline/budget.json`, $50/day, for the orchestrator) cleanly distinct from the
*OpenRouter* second-opinion spend ($5/day, this ledger).

**Prerequisites to verify before launch** (environment configuration, not code):

- `OPENROUTER_API_KEY` is present in the Routine's execution environment.
- The environment's **network policy** permits outbound `openrouter.ai`. If the
  policy is restrictive, `accuracy-review` runs will fail fast — in that case
  launch with `accuracy-review` weight 0 and revisit once egress is allowed.

---

## 6. Drawing on the wiki — the `systemic-fix` mode in detail

The wiki already contains a large, concrete, *batch-addressable* defect catalog.
A representative slice of what `systemic-fix` would work through (all sourced
from `planning/wiki/ideas/cleanup-backlog.md` and `…/tooling-backlog.md`):

| Backlog item | Scope | Fix type | Tool status |
|---|---|---|---|
| `[Register: …]` legacy trailer in notes (P16) | 188 entries | mechanical sweep + formality cross-check | tiny script to build |
| `{ている}` furigana-brace artifact (P15) | 49 entries | mechanical regex | one-liner |
| `するする` typo in TRANSITIVITY (P10) | unknown, grep | mechanical | one-liner |
| Duplicate `conjugation` JSON keys (P4) | pervasive (pre-retrofit verbs) | raw-text de-dupe | tooling item 1 |
| Malformed furigana wrappers (P9) | 624 entries / 859 instances; 68 high-severity | detector + tiered repair | `build/check_furigana_format.py` (tooling item 8) |
| Semantic tag drift (P11/P13) | 01490s–05900s+, scoped to a 2026-04-14 batch signature | detector → review queue → fix | `build/check_tag_drift.py` (tooling item 6) |
| Politeness tag conflation (P7) | ~100 entries | semantic review batch | parallels `polish_semantic_labels.md` |
| Cross-reference symmetry on thematic clusters (P3) | clusters | semi-mechanical | `check_semantic_clusters.py` |

**One `systemic-fix` run**:

1. Read `backlog-queue.json` (below); pick the highest-priority **open,
   batch-ready** item not recently touched.
2. If its detector script doesn't exist yet, build it (the wiki already
   specifies detection rules for each), commit it, and run it.
3. Fix a **bounded batch** of flagged entries this session — *all* of them if the
   fix is purely mechanical and validation-checkable (e.g. `{ている}`,
   `[Register:]`, `するする`); a capped batch (respecting the 60% context rule) if
   the fix needs per-entry judgment (e.g. tag drift, politeness).
4. Update the item's status/scope in `backlog-queue.json` **and** the prose
   backlog page (mark RESOLVED or record remaining scope), so `wiki` mode and the
   curator see live state.

**`planning/wiki/ideas/backlog-queue.json`** — a thin machine-readable index the
`wiki` mode keeps in sync with the prose backlog pages, so `systemic-fix` can
select deterministically:

```json
{
  "items": [
    {"id":"P16-register-trailer","title":"Remove [Register:] trailers",
     "detect":"grep -rl '\\[Register: ' entries/",
     "fix_type":"mechanical","status":"open","scope_estimate":188,
     "source":"ideas/cleanup-backlog.md#priority-16"},
    {"id":"P9-furigana-wrappers","title":"Malformed furigana wrappers",
     "detect":"build/check_furigana_format.py","fix_type":"mixed",
     "status":"open","scope_estimate":624,"source":"ideas/cleanup-backlog.md#priority-9"}
  ]
}
```

Mechanical items are low-risk, dictionary-wide wins; semantic items become a
recurring `systemic-fix` target until drained. Either way the wiki's accumulated
knowledge is converted into measurable site improvements instead of sitting in
prose.

**Wiki consultation in every mode** (not just `systemic-fix`): before working a
range or topic, a run glances at the relevant wiki page(s) — e.g.
`topics/verb-transitivity.md`, `topics/furigana-strategy.md`, the
cleanup-backlog priority covering the current ID range — exactly as
`comprehensive_polish.md` already instructs. The Routine strengthens this by
passing the selected ID range to the playbook so the consultation is targeted.

---

## 7. The Routine prompt (`prompts/routine.md`) — structure

A skeleton, not the final copy. It is intentionally short: it dispatches and
relies on the existing focused prompts for execution detail.

```markdown
# Unified Improvement Routine

The single scheduled task for je-dict-1. Each run does ONE focused unit of work
chosen by the selector, plus always-on capture, then merges its own PR.

## 0. Pre-flight (every run, before anything else)
- python3 pipeline/sweep-stranded-prs.py
- Acquire the Routine lock (pipeline/routine.lock); abort if a fresh lock exists.

## 1. Select the mode
- Run: python3 pipeline/routine-next.py
- Read the emitted JSON: {mode, params, reason, signals}.
- Echo the choice and reason into your eventual session log.

## 2. Execute the selected mode
Follow the matching playbook. Obey its budget/merge discipline exactly.
- polish          → follow prompts/comprehensive_polish.md, process params.id_range
- new-entries     → follow prompts/newentries.md (~20 entries; prefer "seen in entry")
- accuracy-review → §A below (review_runner.py within params.openrouter_budget,
                    then prompts/polish_cross_model_review.md to apply/reject)
- wiki            → follow planning/maintain-knowledge-base.md (+ keep backlog-queue.json current)
- systemic-fix    → §B below (pick params.backlog_item; build detector if needed; fix bounded batch)

## 3. Always-on capture (every mode)
- New unlinked words → candidate_words.json ("seen in entry XXXXX")
- Systemic observations → polishing/observations.md (tagged)

## 4. Budget & context discipline (inherited verbatim)
- Stop at ~60% context, then wrap up. Single make build. Atomic merge tail.

## 5. Wrap up
- Update the relevant progress cursor / state / ledger.
- Write a session log: polishing/sessions/routine_{date}_{nnn}.md (record mode + reason).
- make build IFF entries/build artifacts changed (skip for wiki-only runs).
- git add -A; commit; push -u origin <branch>.
- mcp__github__create_pull_request → Monitor pipeline/wait-for-pr-checks.sh <pr> 30
  → on exit 0, mcp__github__merge_pull_request squash. On non-zero, leave open + log.
- Release the Routine lock.

### §A accuracy-review playbook (Phase 1: furigana)
…run review_runner screening/deep within budget; update ledger; apply via cross-model-review…

### §B systemic-fix playbook
…read backlog-queue.json; build/run detector; fix bounded batch; update backlog status…
```

Key inherited invariants (do **not** re-derive — copy from the existing prompts):

- **60%-context budget**, **single `make build`**, **no post-build fix-up
  commits**, **atomic push→PR→wait→squash-merge tail**, **MCP path** for
  PR/merge (the `gh` CLI is not authorized in Routines).
- **Wiki-only runs skip `make build`** (markdown changes don't touch `docs/`),
  matching `maintain-knowledge-base.md`.

---

## 8. State & progress model

The Routine reuses the existing per-task progress files as the per-mode cursors —
no new bespoke tracking, so manual runs of the old prompts stay compatible.

| Mode | Cursor / state |
|---|---|
| polish | `polishing/tasks/comprehensive/progress.txt` (`next:`) |
| accuracy-review | `polishing/tasks/cross-model-review/progress.txt` + `reviews/` + ledger |
| new-entries | candidate selection order (no cursor needed) + `PROJECT_STATUS.md` |
| wiki | `planning/wiki/log.md` + `backlog-queue.json` |
| systemic-fix | `backlog-queue.json` item statuses |
| dispatcher | `pipeline/routine-state.json`, `pipeline/openrouter-ledger.json` |

Session logs all land in `polishing/sessions/routine_{date}_{nnn}.md` and name the
mode + selector reason, so the curator can audit the rotation from the log
directory alone.

---

## 9. Reliability & safety

| Risk | Mitigation |
|---|---|
| Stranded PR (context exhaustion mid-merge) | Inherited 60%-budget + atomic tail; pre-flight `sweep-stranded-prs.py` self-heals the previous run's strand. |
| Two runs overlapping (a long run still going when the next fires) | `pipeline/routine.lock` (PID + timestamp, ~2 h stale-expiry); second run aborts pre-flight if a fresh lock exists. (May be redundant if the web Routine serializes runs — harmless either way.) |
| Mode fixation | Debt scheduler guarantees long-run proportions; bounded nudges; anti-repeat on heavy modes. |
| OpenRouter overspend | Daily ledger + per-session cap + mode suppression at cap. |
| Bad cross-model correction applied | `polish_cross_model_review.md` APPLY/REJECT/FLAG discipline: never apply a single low-confidence flag; consult the calibration report; FLAG uncertainty for the curator. |
| Shared-file clobber (candidate_words.json, indexes) | Only one run at a time (lock); candidate adds are append-style; indexes regenerated by `make build` within the single run. |
| Selector bug picks nonsense | `--dry-run`/`--explain`/`--simulate` + unit tests; `--force-mode` escape hatch. |

---

## 10. Build plan

### Phase 1 — MVP (launchable on the existing furigana reviewer)

- [ ] `pipeline/routine-next.py` — debt scheduler + health nudges + ledger
      awareness; `--dry-run/--explain/--simulate/--force-mode`.
- [ ] `pipeline/routine-config.json`, `pipeline/routine-state.json`,
      `pipeline/openrouter-ledger.json` (seeded).
- [ ] `pipeline/routine.lock` handling (in the prompt + a tiny helper or inline).
- [ ] `prompts/routine.md` — dispatcher prompt (modes: polish, new-entries,
      accuracy-review[furigana], wiki) delegating to existing playbooks; full
      merge tail.
- [ ] `build/tests/test_routine_next.py` — proportions converge to weights;
      nudges bounded; budget suppression; anti-repeat.
- [ ] Docs: mark `routine.md` the single scheduled task in `CLAUDE.md`,
      `prompts/metaprompt_list.md`, and `PROJECT_CONTEXT_BRIEF.md`; note the
      three old prompts remain runnable manually but are now driven by the
      Routine.
- [ ] Verify launch prerequisites: `OPENROUTER_API_KEY` present; egress to
      `openrouter.ai` allowed (else launch with `accuracy-review` weight 0).

### Phase 2 — fast-follow

- [ ] `systemic-fix` mode + `planning/wiki/ideas/backlog-queue.json` + the
      first 2–3 mechanical batch scripts the backlog already specifies
      (`[Register:]`/`{ている}`/`するする` cleaners; duplicate-conjugation-key
      pruner; `check_furigana_format.py`; `check_tag_drift.py`).
- [ ] Extend `review_runner.py` to cross-check **glosses/definitions** and
      **example-sentence translations** (new prompt templates + response
      parsing), with a small calibration pass mirroring the furigana
      calibration (`reviews/calibration_report.md`).
- [ ] Fold a "selector health" line into `make report` so the curator sees what
      the next run would pick.

### Validation before scheduling

1. `routine-next.py --simulate $((7*runs_per_day))` → confirm the weekly mix.
2. Manually run `routine.md` once **per mode** (`--force-mode …`), each producing
   a clean merged PR.
3. Schedule conservatively (e.g. start at the existing cadence), watch for
   stranded PRs for a few days, then raise frequency.
4. Curator spot-checks per `pipeline/DAILY_WORKFLOW.md`.

---

## 11. Out of scope now — multilingual hook

Per the curator, this Routine targets **Japanese→English only**. The design
leaves clean seams for the later simplified-Chinese work without committing to it:

- The selector config could later gain a `language` dimension and per-language
  weights; today it ignores language entirely.
- A future `translation-sidecar` mode (see
  `planning/wiki/ideas/translation-sidecar-design.md`) and per-language
  false-friend accuracy checks (see
  `planning/wiki/research/japanese-chinese-adaptation-brief.md`) would slot in as
  additional modes with their own ledgers.
- Nothing in Phase 1/2 hard-codes "English" in a way that would block this; the
  accuracy-review templates are the only place that assumes the EN target, and
  they'd be parameterized when the time comes.

We revisit this only after the curator has run the JA→EN Routine for a while.

---

## 12. Open questions for the curator (non-blocking)

These don't block Phase 1; defaults are proposed so the Routine can launch and be
tuned later by editing `routine-config.json`.

1. **Runs per day**: the plan assumes ~6. Fewer means each run should lean
   slightly heavier (more entries/range per run); more means lighter runs.
   `runs_per_day_hint` tunes per-run sizing.
2. **systemic-fix aggressiveness**: should purely-mechanical, validation-checkable
   sweeps (e.g. `{ている}`) be allowed to fix **all** flagged entries in one run
   (potentially a large diff), or stay capped like semantic work? Default:
   mechanical = uncapped (still one `make build`, still 60% context), semantic =
   capped.
3. **new-entries vs. corpus harvesting**: when candidates run low, should the
   Routine auto-route to candidate discovery (`newcandidates.md` /
   `corpus_harvesting.md`), or just lower `new-entries` weight and let the
   curator top up candidates? Default: lower the weight + log a `[pattern]`
   note; keep discovery a manual/curated step for now.
```
