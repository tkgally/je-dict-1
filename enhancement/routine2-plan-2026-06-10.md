# Verified Improvement Routine (v2) — Plan (2026-06-10)

> **Status update (2026-06-11)**: adopted. `prompts/routine2.md` is the
> scheduled Routine; the v1 prompt (`prompts/routine.md`) was deleted (no
> rename — routine2.md keeps its name). The taxonomy-expansion tag policy and
> reviewer prompt v3 followed from the first two days of v2 runs; see
> `planning/wiki/topics/schema-tag-reliability.md`.

A revision of the unified Routine, prepared one day after v1
(`enhancement/unified-routine-plan-2026-06-09.md`, `prompts/routine.md`)
shipped and ran its first nine test sessions. v2 is **an evolution, not a
rewrite**: it keeps everything the test runs validated and changes the three
places where the evidence shows the design leaves quality, reliability, or
budget on the table.

> **Status**: proposal for curator review. `prompts/routine2.md` is written and
> is **runnable today** (Phase 0) using only scripts that already exist; the
> Phase 1 items below are small quality-of-life codifications, not
> prerequisites. Scope remains **Japanese→English only**; the multilingual
> seam (§9) is unchanged from v1.

---

## 1. What the v1 test runs taught us (evidence base)

Nine Routine runs executed on 2026-06-09 (see
`polishing/sessions/routine_2026-06-09_00*.md` and `main`'s merge history):

| Observation | Detail |
|---|---|
| **The chassis works** | 9 runs across all five modes; 8 self-merged cleanly. Selector, lock, sweep, ledger, atomic merge tail all behaved as designed. |
| **One strand, recoverable** | PR #2663 (polish) hit `wait-for-pr-checks.sh`'s 600 s default timeout while CI was merely slow; protocol left it for the curator, who merged it by hand. The *next* run could have merged it automatically — it was green. |
| **One tooling crash** | `review_runner.py` crashed on a null Gemini response mid-deep-pass (session 002). Completed per-entry results survived; the crash cost the rest of the pass. |
| **Budget underused** | $0.98 of the $5.00 daily OpenRouter cap was spent. At observed costs (**~$2 per 1,000 entries** all-in: screening + deep furigana + 3-dimension accuracy), the full ~29,000-entry dictionary costs ~$58 to sweep — i.e. the cap supports a **complete cross-model pass roughly monthly**, but v1's pacing (250 entries/run, ~2 review runs/day) delivers one pass per ~2 months and leaves >$4/day idle. |
| **The review queue is half a loop** | `.github/workflows/review-queue.yml` appends every entry changed on `main` to `reviews/queue.txt` — now **19,602 lines** — but nothing consumes it. The accuracy-review cursor (`next: 00451`) sweeps bottom-up by ID, blind to which entries actually changed. |
| **New entries are born unreviewed** | new-entries runs create ~20 entries/run (IDs 29xxx). The bottom-up review sweep is at 00451; at v1 pacing those entries wait **months to years** for their first independent check — yet fresh entries are where new gloss/translation errors enter. |
| **Sequential polish cannot catch up** | The comprehensive frontier is at 05990 of ~29,062. Polish advances ~54 entries/day (3 runs × ~18) while new-entries adds ~40/day — net ~14/day, i.e. **the frontier effectively never completes a pass** under the v1 mix. The full-coverage guarantee of ID-order polishing is illusory; only the cheap models can realistically visit every entry. |
| **Priority lists exist but are unused** | `make priorities` generated worst-first lists (`polishing/priority/*.txt`, 2026-06-04), and the infrastructure to use them exists, but comprehensive polish — and therefore the Routine — processes pure ID order. |
| **Flag adjudication works but isn't measured** | Sessions applied 28/“many” flags in entries 1–200 and only 4 in 201–450; the APPLY/REJECT discipline filters false positives well, but nothing records per-dimension precision, so there is no data with which to tune trust, add consensus checks, or retire a noisy dimension. |
| **No quality time series** | The Routine produces activity logs but no metric history. "Is the dictionary getting better?" is currently answered by anecdote. |

## 2. Design thesis

Keep the v1 chassis — it is tested and sound:

- thin dispatcher; **one focused mode per run**; balance achieved across runs
  via the deterministic debt scheduler (`pipeline/routine_next.py`) with
  bounded health nudges;
- delegation to the existing single-focus prompts (one source of truth);
- always-on candidate/observation capture;
- 60%-context rule, single build, atomic push→PR→CI→squash-merge tail;
- Routine lock + stranded-PR sweep; OpenRouter daily ledger;
- semantic-verification-first systemic fixes; manual candidate top-up.

Change three things:

### Upgrade A — Trust but verify, every run (close the loops)

v1 treats cross-model checking as **one mode among five**. v2 additionally
makes it a **guardrail on every content-producing run**:

1. **Self-verification (§4 of the prompt)**: any run that created or modified
   entries sends *exactly those entries* to an independent model before the
   single build (`review_accuracy.py --ids …`, or the furigana screener for
   format-only batches), adjudicates the findings (APPLY/REJECT/FLAG), and
   only then builds and merges. Cost: ~$0.01 per 25 entries. One pass, one fix
   round, no ping-pong.
2. **New-entry quality gate**: the same step applied to freshly created
   entries — they are checked at birth instead of waiting for the sweep.
3. **The review queue becomes a real loop**: accuracy-review runs remove the
   ranges they cover from `reviews/queue.txt`; CI keeps re-adding anything
   that changes (including the Routine's own fixes, which thereby get a
   second look). The queue converges to "changed since last reviewed" instead
   of growing monotonically.

Rationale: the biggest risk of months of unattended operation is not any
single error — it is the slow, unobserved accumulation of self-introduced
errors. v1 catches those only when the bottom-up sweep happens to reach them;
v2 catches most of them within the same run, for pennies.

### Upgrade B — Coverage from cheap models, judgment from Claude

The throughput math in §1 says: only the OpenRouter sweep can visit all
~29,000 entries on a useful cadence (~monthly at ~$2/day); sequential
Claude-polish cannot (it never completes a pass). So v2 allocates accordingly:

1. **accuracy-review becomes the coverage instrument**: per-session OpenRouter
   cap raised (1.50 → 2.50 USD, config knob) and its weight nudged up, so the
   sweep advances ~1,000+ entries/day and completes a full pass in ~4–6 weeks,
   then keeps cycling via the queue.
2. **polish gets a priority lane**: each polish run spends ~40% of its entry
   budget on the worst-scoring entries (from `polishing/priority/notes.txt`,
   skipping IDs below the frontier), and the rest on the sequential frontier
   as before. Priority files are regenerated when stale (`make priorities`).
   Claude's expensive judgment goes first to the entries most likely to need
   it, while the frontier still guarantees orderly constructive work (inline
   links, cross-refs, notes) and eventual full coverage.

### Upgrade C — Measure the slope

1. **Per-run metrics snapshot** → `pipeline/metrics-history.jsonl`: one JSON
   line per run (entries total, candidates, review-queue depth, observations
   backlog, frontier position, flags applied/rejected/escalated, OpenRouter
   spend). Inline fallback ships in the prompt; `pipeline/metrics_snapshot.py`
   (Phase 1) adds weekly deep collectors (consistency counts, note-quality
   distribution, inline-link coverage).
2. **Decision ledger** → `reviews/decisions.jsonl`: every APPLY/REJECT/FLAG on
   an external model's flag is logged with source, dimension, and severity.
   After a few weeks this yields per-dimension flag precision — the data
   needed to decide where to trust single models, where to require consensus,
   and which review dimensions to retire or expand.
3. **Wiki mode reviews the trends**: a new metrics-trend activity maintains
   `planning/wiki/topics/quality-metrics.md` and files `[pattern]`
   observations when a metric moves the wrong way. The curator gets a slope,
   not a feeling.

### Reliability patches (from observed failures)

| Observed failure | v2 response |
|---|---|
| PR #2663 stranded on a 600 s CI timeout; curator merged by hand | **§0a rescue-merge**: each run's pre-flight squash-merges a predecessor `routine(…)` PR that is green, mergeable, and untouched by humans, then fast-forwards onto it. Plus: CI wait raised to 20 min with one retry on timeout. |
| `review_runner.py` null-response crash mid-pass | Prompt-level resilience now (keep partial results, log `[tooling]`, continue); Phase 1 patches the script (guard + single retry). |
| Stale priority lists | polish regenerates them when >14 days old. |

### Deliberately NOT changed

- **Mode set, names, selector, state/config/ledger file formats** — v2 is
  drop-in compatible; `routine.md` and `routine2.md` share all state. (Never
  *schedule* both; the shared lock makes an accidental overlap abort safely.)
- **Semantic-verification-first** for systemic fixes — no auto-apply anywhere;
  every external flag passes through Claude's judgment. (A Phase 2 item lets
  the *curator* whitelist provably-safe classes once `decisions.jsonl` shows
  the data — default off.)
- **Manual candidate top-up** — no auto-discovery; always-on "seen in entry"
  capture continues.
- **JA→EN scope**; articles remain out of the Routine.
- **Single build, atomic merge tail, 60% rule** — verbatim.

## 3. The prompt

`prompts/routine2.md` — same skeleton as v1 with these deltas:

| Section | Delta vs v1 |
|---|---|
| §0 Pre-flight | + §0a rescue-merge (3 MCP calls, usually no-op) before sweep + lock |
| §1 Selector | unchanged (same JSON contract) |
| §2 polish | + priority lane (40% of budget, worst-first, cursor in `polishing/tasks/comprehensive/priority-cursor.txt`) before the sequential frontier; regenerate stale priority files |
| §2 new-entries | + §4 gate on the new IDs before the single build |
| §2 accuracy-review | §A v2: range sized to spend most of the session budget; queue maintenance; decision logging; crash resilience |
| §2 wiki | + metrics-trend activity (`topics/quality-metrics.md`) |
| §2 systemic-fix | + §4 self-check (furigana-screener variant) |
| §3 capture | unchanged |
| §4 Verify your own changes | **new** — the per-run guardrail |
| §5 Metrics snapshot | **new** — inline fallback until `metrics_snapshot.py` ships |
| §6 discipline | unchanged, with §4/§5 counted into the wrap-up budget (finish mode work by ~55%) |
| §7 Wrap up | + priority cursor; CI wait `30 1200` + one retry; commits the new JSONL files; same atomic tail |
| §C Decision ledger | **new** — JSONL conventions |

## 4. File-change plan

### Phase 0 — ships with this PR (no behavior change to the running v1)

- [x] `prompts/routine2.md` — the new prompt. Every new capability degrades
      gracefully: §0a uses only existing MCP tools; §4 uses the existing
      `--ids` flags on `review_accuracy.py` / `review_runner.py`; §5 has an
      inline fallback; the priority lane skips itself if files are missing.
- [x] `enhancement/routine2-plan-2026-06-10.md` — this document.

Nothing else changes. v1 keeps running until the curator swaps the schedule.

### Phase 1 — one implementation session (small PR, after curator approval)

1. **`pipeline/rescue-merge.py`** — codify §0a: list open `claude/*` PRs
   titled `routine…`; for each, check check-runs + mergeability + absence of
   human comments/reviews; squash-merge qualifying ones; print a report;
   `--dry-run` flag. Unit-test the gating predicate. §0a in the prompt then
   collapses to one command (keep the manual MCP fallback text for
   robustness).
2. **`pipeline/metrics_snapshot.py`** — replaces the §5 inline fallback.
   Cheap collectors every run (same fields as the fallback, plus decision
   tallies read from `reviews/decisions.jsonl`); expensive collectors
   (`check_consistency.py --json` issue counts, `score_note_quality.py
   --summary` mean/p25, inline-link coverage %, detector queue depths from the
   three `check_*` scripts) run only when the last full snapshot is ≥7 days
   old. Also regenerates `polishing/priority/*` via `prioritize_polishing.py`
   when stale, so the polish prompt's wrap-up step can drop that
   responsibility later. Unit tests for the JSONL append and staleness gates.
3. **`build/review_runner.py`** — guard the null/empty-response crash
   (observed at the response-parsing site, session 002): treat as
   `model_error`, retry once, then skip that entry and continue the pass.
4. **`pipeline/routine_next.py` + `pipeline/routine-config.json`** —
   - new signals: `review_queue_len` (line count of `reviews/queue.txt`),
     `priority_file_age_days`;
   - `polish` params gain `{priority_file, priority_cursor_line}` (the prompt
     currently reads these itself; moving them into the selector keeps all
     run-shaping in one place);
   - config: `openrouter.per_session_cap_usd: 1.5 → 2.5`, new
     `openrouter.self_check_cap_usd: 0.25`;
   - **proposed weights** (curator-tunable, rationale in §2-B):
     `polish 0.35, accuracy-review 0.25, new-entries 0.15, wiki 0.15,
     systemic-fix 0.10` (v1: 0.35/0.20/0.20/0.15/0.10);
   - update `build/tests/test_routine_next.py` accordingly.
5. **Seed files**: `polishing/tasks/comprehensive/priority-cursor.txt`
   (`line: 1`), empty `reviews/decisions.jsonl`, skeleton
   `planning/wiki/topics/quality-metrics.md` (+ `index.md` entry).
6. **Docs**: point the Routine paragraph in `CLAUDE.md` and
   `prompts/metaprompt_list.md` at `routine2.md`; add the metrics-trend
   activity (H) to `planning/maintain-knowledge-base.md`; note the two new
   JSONL files in the project-structure tree.
7. *(Optional, low priority)* `build/review_accuracy.py --from-queue N /
   --update-queue` to formalize the queue operations the prompt currently does
   with `awk`.

### Phase 2 — later, each gated on accumulated data + curator sign-off

- **Consensus reviews for noisy dimensions**: if `decisions.jsonl` shows a
  dimension's apply-rate below ~40% (the `tags` dimension is the likely
  candidate), run it with two different cheap models and only surface
  intersecting flags.
- **Curator-approved auto-apply whitelist** for provably-safe correction
  classes (e.g. two-model-agreed okurigana truncations that also match
  `word_id_lookup.json`) — default off; this is the only place v2 would ever
  relax verification, and only by explicit curator decision.
- **Selector reads the metrics**: e.g. raise accuracy-review weight while
  applied-flags-per-dollar is high, decay it as the dictionary gets cleaner —
  closing the measure→allocate loop end-to-end.
- **`review_accuracy.py` calibration report** mirroring
  `reviews/calibration_report.md`.
- **Multilingual modes** (simplified Chinese first) — unchanged seam from v1
  §11: per-language weights, a translation-sidecar mode, per-language ledgers.

## 5. Rollout

1. **This PR** merges the prompt + plan. No schedule change yet.
2. **Curator validation**: run `routine2.md` manually once per mode
   (`routine_next.py --force-mode <mode>` then follow the prompt), confirming
   each produces a clean merged PR, a metrics line, ledger entries, and (for
   content modes) a §4 self-check section in the session log.
3. **Implement Phase 1** (one focused session).
4. **Swap the schedule**: point the Routine at `prompts/routine2.md` at the
   same cadence (6/day). Keep `routine.md` as a manual fallback; never
   schedule both.
5. After a clean week, optionally rename `routine2.md` → `routine.md` so the
   project keeps a single canonical name (git history preserves v1).

## 6. Budget projection (OpenRouter, $5/day cap unchanged)

| Lane | Typical day | Notes |
|---|---|---|
| accuracy-review sweep | ~$2.0–2.5 (1–2 runs) | ~1,000–1,250 entries/day → full pass in ~4–6 weeks, then queue-driven |
| §4 self-checks | ~$0.10–0.30 (4–5 content runs × $0.02–0.06) | 20–90 entries each |
| **Total** | **~$2.5–3.0** | hard-capped by the existing ledger + per-session caps |

## 7. Risks (delta from v1's risk table)

| Risk | Mitigation |
|---|---|
| §4 fix round introduces new errors → re-verify loop | Hard rule: one verification pass, one fix round, never re-verify. CI re-queues the fixed entries for the next sweep anyway. |
| Rescue-merge merges something the curator wanted held | Gates: `routine` title prefix + all checks green + mergeable + zero human comments/reviews. A failed check or one curator comment disqualifies. Phase 1 script adds `--dry-run` for the first scheduled week. |
| Priority lane and frontier lane double-process an entry | Priority lane skips IDs below the frontier; both lanes have cursors. Worst case is a harmless re-polish. |
| Self-check spend erodes the sweep budget | Separate `self_check_cap_usd` (0.25/run) + the same daily ledger; §4 skips itself below $0.05 remaining. |
| Two more JSONL files to commit → merge conflicts | Both are append-only and only one run holds the lock at a time — same posture as the ledger, which had no conflicts in testing. |
| Longer prompt → more context per run | v2 adds ~80 lines over v1; the §4/§5 work replaces (cheaper) what would otherwise surface as future corrective runs. The 55% checkpoint compensates. |

## 8. How v2 differs from the 2026-06-09 plan — and why

**What Opus 4.8's v1 got right** (verified by its own test runs, and kept
wholesale): the dispatcher architecture and one-mode-per-run focus; the
deterministic, auditable debt scheduler with bounded nudges; reusing the
existing prompts instead of re-implementing them; the daily OpenRouter ledger;
the lock + sweep self-healing; the atomic merge tail; semantic-verification-
first; manual candidate top-up. v2 deliberately changes none of this — eight
of nine first-day runs self-merged cleanly, which is strong evidence the
chassis is correct.

**Where v2 differs, and the evidence behind each change:**

| Dimension | v1 (2026-06-09) | v2 (this plan) | Why |
|---|---|---|---|
| Role of OpenRouter models | A separate audit mode (~20% of runs) | That, **plus a guardrail on every content run** (§4) and a birth-check on new entries | Unattended operation's main risk is self-introduced error accumulating unobserved; v1 only catches it when the bottom-up sweep arrives (months–years for new entries) |
| `reviews/queue.txt` | Written by CI, never read | Consumed and converging | 19,602 queued entries with no consumer is a half-built loop |
| Polish targeting | Pure ID order from the frontier | Priority lane (worst-first) + frontier | Frontier advances ~54/day vs ~40 new entries/day — it never finishes a pass, so ID order spends scarce judgment on arbitrary entries while known-bad ones wait years; priority lists already exist, unused |
| Review pacing | ~250 entries/run, $0.98 of $5/day used | Range sized to the session budget, per-session cap 1.5→2.5 | The cap supports a full-dictionary pass ~monthly; v1's pacing delivers ~bi-monthly while idling >80% of budget |
| Measurement | Session logs (activity) | + per-run metrics history, + decision ledger, + wiki trend page | "Steadily better" needs a slope; flag-precision data is what lets Phase 2 add consensus/auto-apply *safely* |
| CI-timeout strand | Left for the curator (happened on day one, PR #2663) | §0a rescue-merge + 20-min CI wait + one retry | The strand was green and self-rescuable; the curator should not be the retry mechanism |
| `review_runner.py` crash | Unhandled (lost the rest of a pass) | Prompt-level resilience now; script guard in Phase 1 | Observed failure, cheap fix |
| Weights | 0.35 / 0.20 / 0.20 / 0.15 / 0.10 (polish/review/new/wiki/sysfix) | 0.35 / 0.25 / 0.15 / 0.15 / 0.10 proposed | Reviews are the cheapest quality per dollar; creation currently outruns polishing — one config knob, curator-tunable either way |

**The one-sentence version**: v1 built the correct *scheduler*; v2 keeps it
and adds the correct *control loops* — every change verified at the moment it
is made, coverage delegated to models that can actually afford it, and a
metrics trail that turns "is it getting better?" into a measurement. The
practical effect over months: errors are caught within the run that makes
them rather than discovered by a sweep much later; the worst entries improve
first; the curator can watch the quality slope (and the reviewers' precision)
rather than reading activity logs; and strands self-heal instead of waiting
for a human.

**Honest costs of v2**: a slightly longer prompt (~80 lines); a few cents and
one extra fix round per content run; 1–3 extra MCP calls in pre-flight; two
new append-only JSONL files to track. All bounded, all visible in the metrics.

## 9. Post-test revisions (2026-06-10, after the five forced-mode runs)

All five manual test runs (PRs #2666–#2670, one per mode) executed and
**self-merged cleanly**; every v2 mechanism worked on first contact (priority
lane, new-entry gate, queue maintenance, decision ledger, metrics snapshot,
§0a rescue check, wiki trend page). The runs also produced the first hard
data, which drove these same-day revisions:

| Finding (evidence) | Revision |
|---|---|
| **Reviewer-flag noise dominates**: run 003 adjudicated 417 flags to apply 6; ledger shows warn-severity flags 0.7–2.1% applicable, error-severity 4–13%. Rejection families were predictable: style rewordings, project conventions (politeness "plain", suru-verb "action" tag, kinship "humble"), invented tags outside the schema enum. | `review_accuracy.py` prompt v2 (`PROMPT_VERSION = 2`): embeds the `VALID_SEMANTIC` vocabulary, states project conventions as do-not-flag, raises the materiality bar ("expected response is []"), defines severities. Review files now record `prompt_version` so calibration can compare. |
| **Deep furigana pass = 83% of run cost, 0 applies**: $0.4461 for 45 entries; its 4 flags were 3 documented FP-family rejects + 1 curator escalation. Both deep models agreed on the FPs, so consensus did not filter them. | Screening prompt gains a known-correct-patterns block (rendaku incl. 〜好き→ずき, standalone noun readings, compound splits, counter sound changes). §A caps deep spend at ~⅓ of session budget. |
| **`--pass deep --range` bug**: deep-reviewed the whole range, not the screening-flagged subset; run 003 caught it mid-burn and recovered with `--ids`. | Fixed in `review_runner.py`: a range now intersects with screening flags (explicit `--ids` unchanged). |
| **Model-response parse failures**: gemini-2.5-pro returns empty `content` with text in `reasoning` (06-10), and null content crashed the runner (06-09). | Shared `extract_message_text()` guard: tolerates null/empty content, falls back to `reasoning`, accepts object-wrapped arrays. |
| **Priority lane skipped 105 of its first 110 lines** chasing the below-frontier exclusion — yet the worst-scoring entries *are* mostly below the frontier (scored after their long-ago polish) and the 6 lane entries it did process yielded real fixes. | Lane rule changed: worst-first regardless of frontier; skip only missing entries and entries modified in the last 30 days; cursor resets to `line: 1` when priorities are regenerated. |
| **Adjudication effort, not dollars, is the binding constraint** on review-range size. | §A guidance: ~400–600 entries/run; work `error` flags individually, sample `warn` flags and bulk-reject recurring noise families with one aggregated §C line (`"n"` count); >20% entries flagged ⇒ treat as reviewer noise and file `[tooling]`. |
| **Manual metrics heredoc is clumsy** (sessions hand-counted flags). | `pipeline/metrics_snapshot.py` shipped: derives flag tallies from today's `decisions.jsonl`, adds weekly detector-depth collectors; §5 slimmed to one command. |
| **Queue convergence concern** (wiki run filed it: 19,602 → 19,450 in a day). | Root cause is sweep throughput, addressed by the cost fixes above + `per_session_cap_usd` 1.5 → 2.5: ~1,000+ entries/day ⇒ queue drains in ~3–5 weeks of normal rotation. Re-adds from content runs (~+15/day) are noise against that. |
| Proposed weight shift (plan §4 item 4). | Applied: accuracy-review 0.20 → 0.25, new-entries 0.20 → 0.15. |

Still deliberately deferred: `pipeline/rescue-merge.py` (§0a's manual MCP steps
were a clean no-op in all five runs; codify later), selector signal additions,
`--from-queue` convenience flags, and the inline-link **target-correctness**
gate (`validate.py` verifies link IDs resolve but not that the baseform matches
the target entry — run 001 caught a データ→クラウド mislink only by hand; filed
as Tooling Backlog item 11, best built as a read-only `check_link_targets.py`
detector feeding `systemic-fix`).

## 10. Out of scope now — multilingual hook (unchanged from v1)

Per the curator, this Routine targets **Japanese→English only**. The v1 seams
are preserved untouched: a future `language` dimension in the selector config,
a `translation-sidecar` mode, and per-language accuracy templates/ledgers
would slot in without disturbing anything above. Revisit after the JA→EN
Routine has run for a while.
