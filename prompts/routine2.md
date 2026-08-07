# Unified Improvement Routine v2 — the Verified Routine

**The single scheduled task for je-dict-1.** Each run does ONE focused unit of
high-quality work chosen by a deterministic selector, **verifies its own changes
with an independent model before merging them**, records a one-line quality
metrics snapshot, then reliably merges its own PR. Designed to run unattended
several times a day and make the dictionary steadily more accurate, consistent,
and useful over weeks and months — drawing on insights accumulated in the
knowledge wiki — while keeping the dictionary's existing concept, headword
range, sense inventory, and example style. Scope is **Japanese→English only**.

v2 keeps v1's proven chassis (deterministic selector, five modes, delegation to
the existing per-task prompts, always-on capture, 60%-context rule, atomic
merge tail, Routine lock, OpenRouter ledger) and changes three things, based on
the 2026-06-09 test runs:

1. **Trust but verify, every run** (§4): any run that creates or modifies
   entries sends *exactly those entries* to an independent model (pennies per
   run) and adjudicates the findings before the PR. New entries are checked at
   birth instead of waiting months for a sweep to reach them.
2. **Coverage from cheap models, judgment from Claude** (§2, §A): the
   accuracy-review sweep is the whole-dictionary surveillance instrument (it
   can cover the entire dictionary roughly monthly within the $5/day budget);
   the polish mode spends part of each run on the worst-scoring entries
   (priority lane) instead of pure ID order, because the sequential frontier
   alone cannot outpace new-entry growth.
3. **Measure the slope** (§5, §C): every run appends one line of quality
   metrics to `pipeline/metrics-history.jsonl`, and every APPLY/REJECT/FLAG
   decision on an external model's flag is logged to `reviews/decisions.jsonl`,
   so both dictionary quality and reviewer-flag precision become measurable
   over weeks instead of anecdotal.

This prompt assumes any current Anthropic model; nothing in it is
model-specific. External second opinions go through OpenRouter under the
daily ledger.

> Design, rationale, evidence, and the file-change plan:
> `enhancement/routine2-plan-2026-06-10.md`.
> v1 design (kept foundations): `enhancement/unified-routine-plan-2026-06-09.md`.

---

## 0. Pre-flight (every run, before reading any entry/wiki data)

**0a. Rescue a green predecessor** (usually a no-op; this is what recovers a
previous run's CI-timeout strand instead of leaving it for the curator):

1. Call `mcp__github__list_pull_requests` (`owner: "tkgally"`,
   `repo: "je-dict-1"`, `state: "open"`).
2. For each open PR whose head branch starts with `claude/` AND whose title
   starts with `routine`: fetch its state with `mcp__github__pull_request_read`
   (methods `get` and `get_check_runs` — use `get_check_runs`, **not**
   `get_status`, which is blind to GitHub Actions check-runs and always reports
   `state: "pending"`, `total_count: 0` here). **Rescue it** — call
   `mcp__github__merge_pull_request` with `merge_method: "squash"` — only if
   ALL of the following hold:
   - `get_check_runs` shows `total_count >= 1` and every run `completed` with a
     `conclusion` of `success`, `neutral`, or `skipped`;
   - the PR is mergeable (no conflicts with main);
   - no human has commented on or reviewed the PR (a curator comment means
     the curator owns it now — leave it).
   This merely completes a merge that run was already authorized to perform
   but missed (CI timeout, context exhaustion).
3. If you rescued anything: `git fetch origin main && git merge origin/main
   --no-edit` so this run builds on the rescued work (the branch has no local
   changes yet, so this is a clean fast-forward).
4. Anything not rescuable (failed checks, conflicts, human comments): leave it
   open and mention it in your session log.

**0b. Sweep and lock:**

- **Sweep superseded strands via MCP.** Perform the stranded-PR sweep described
  in `CLAUDE.md` → "Sweep stranded PRs via MCP": reuse the open-PR list from §0a,
  and for any `claude/*` PR you did **not** rescue, close it (with an explanatory
  comment via `mcp__github__add_issue_comment` + `mcp__github__update_pull_request`
  `state: "closed"`) when the maximum entry ID among the entry files it touches is
  below `polishing/tasks/comprehensive/progress.txt`'s `next:` value. **Do not run
  `pipeline/sweep-stranded-prs.py`** — direct GitHub REST 403s in this environment,
  so the script is a no-op here; the MCP sweep is the working safety net.
- **Sweep orphan branches via MCP.** A run that pushes its branch but dies before
  `create_pull_request` (e.g. the 2026-08-07 GitHub-API outage,
  `polishing/sessions/routine_2026-08-07_005.md`) leaves work no PR-based check
  can see. Perform the orphan-branch sweep described in `CLAUDE.md` → "Sweep
  orphan `claude/*` branches via MCP": `mcp__github__list_branches`; for each
  `claude/*` branch that is neither this session's branch nor an open PR's head,
  classify it using its PR history (`mcp__github__list_pull_requests`,
  `head: "tkgally:<branch>"`, `state: "all"`) plus the local-git absorption test
  defined there, then (a) absorbed → append a `prune-branch` line to
  `reviews/needs_curator.txt` (MCP cannot delete branches), (b) never-PR'd live
  work that merges cleanly → rescue it with `mcp__github__create_pull_request`
  so the §0a machinery owns it from now on, (c) anything else → flag it for the
  curator. Zero orphans is the normal case; this costs one `list_branches` call.
- **Acquire the lock:**
  ```bash
  python3 pipeline/routine_lock.py acquire --session "$(git rev-parse --abbrev-ref HEAD)"
  ```
  If it exits non-zero, another Routine run appears active — **stop now**.
  Otherwise you hold the lock; release it at the very end (§7).

## 1. Select this run's mode

```bash
python3 pipeline/routine_next.py
```

This prints a JSON object and persists selector state. Read it:

```json
{ "mode": "polish", "params": { "start_id": 5990 },
  "reason": "...", "signals": { ... },
  "openrouter": { "remaining_usd": 5.0, "session_budget_usd": null }, ... }
```

- **`mode`** is your focus for this run; **`params`** carries the working
  range / budget / flags; **`reason`** and **`signals`** go in your session log.
- Do **not** second-guess the selector. Execute the mode it chose. (For manual
  testing the curator may run `routine_next.py --force-mode <mode>`, which
  prints the same JSON without perturbing the rotation.)

## 2. Execute the selected mode

Follow the matching playbook. **Obey that prompt's per-session budget and its
PR/CI/merge discipline** — they are the same disciplines this Routine uses in
§6–7. Process the range/params the selector gave you.

| `mode` | Do this |
|---|---|
| `polish` | Apply **`prompts/comprehensive_polish.md`**'s per-entry checklist in **two lanes**. **Priority lane first**: if `polishing/priority/notes.txt` exists and is less than 14 days old, spend roughly the first 40% of your entry budget on IDs taken from it in order, starting at the line recorded in `polishing/tasks/comprehensive/priority-cursor.txt` (create the file with `line: 1` if missing). Skip only IDs with no entry file and entries whose `modified` date is within the last 30 days — worst-scoring entries are eligible **regardless of the comprehensive frontier**: a low-ID entry that was polished long ago but still scores at the bottom is exactly what this lane is for. **Frontier lane second**: spend the rest of the budget sequentially from `params.start_id` as in v1. Update both cursors at wrap-up. If the priority file is missing or stale, run frontier-only, regenerate priorities at wrap-up (`make priorities`, before `make build`), and reset the priority cursor to `line: 1` (regeneration re-ranks, so old line numbers are meaningless). **Also regenerate + reset at wrap-up if more than half of the priority-lane entries you processed turned out to need no changes** — that means the rankings have gone stale relative to recent polishing. Skip comprehensive_polish.md's own pre-flight sweep (already done in §0). |
| `new-entries` | Follow **`prompts/newentries.md`**. Create ~`params.approx_count` (≈20) entries; prefer candidates whose notes say "seen in entry". **Tag from the closed lists**: semantic tags MUST come from `VALID_SEMANTIC` and domain tags from `VALID_DOMAIN` in `build/validate_tags.py` (newentries.md has the table) — after validation, `python3 build/validate_tags.py` must report no "Unknown semantic tag" warnings for your new IDs. After the post-creation validation sequence and **before** the single build, run the §4 self-verification on the new entry IDs — this is the new-entry quality gate. If `params.candidates_low` is true, create what you sensibly can, then append `- [pattern] candidate_words.json running low — curator restock requested` to `polishing/observations.md`. **Never** auto-route to corpus harvesting or candidate discovery; the curator tops up candidates manually. |
| `accuracy-review` | Follow **§A** below (cross-model review of furigana + glosses/translations/tags within budget, apply corrections, maintain the review queue). |
| `wiki` | Follow **`planning/maintain-knowledge-base.md`** (harvest `polishing/observations.md`, then 2–4 wiki activities). Keep `planning/wiki/ideas/backlog-queue.json` in sync with the prose backlog pages. **Metrics trend activity**: if `pipeline/metrics-history.jsonl` has ≥10 lines newer than the last update of `planning/wiki/topics/quality-metrics.md` (or that page doesn't exist yet), create/update it with a dated trend table (entry count, flags applied/rejected by dimension from `reviews/decisions.jsonl`, review-queue depth, OpenRouter spend) and log any metric moving the wrong way as a `[pattern]` observation. |
| `systemic-fix` | Follow **§B** below, working `params.backlog_item`. Semantic-verification-first: verify every flagged entry before changing it. |

**Wiki consultation (all modes).** Before working a range or topic, glance at
the wiki page(s) relevant to what you're touching — e.g.
`planning/wiki/topics/verb-transitivity.md`, `…/furigana-strategy.md`,
`…/schema-tag-reliability.md`, or the `planning/wiki/ideas/cleanup-backlog.md`
priority covering your ID range. Read only what's directly applicable; don't
read the whole wiki.

## 3. Always-on capture (every mode, regardless of focus)

- **Missing words → candidates.** Any Japanese word you encounter in an example
  or note that lacks an entry: add it immediately with a source tag:
  ```bash
  python3 build/manage_candidates.py add "言葉" "ことば" "brief gloss; seen in entry XXXXX"
  ```
- **Systemic observations → `polishing/observations.md`**, using the existing
  tags (`[pattern] [wiki] [article] [tooling] [skill] [entry]`). This feeds the
  `wiki` and `systemic-fix` modes.

## 4. Verify your own changes (every run that created or modified entries)

Run this AFTER the mode's content work (and, for `new-entries`, after its
post-creation validation sequence) and BEFORE the single `make build`.
**One verification pass, one fix round, then stop** — never re-verify the fix
round (no ping-pong loops).

1. **List the entry IDs you changed this run:**
   ```bash
   git status --porcelain -- entries/ | sed -E 's/^.{3}//' | sed -E 's|.*/([0-9]{5})_.*|\1|' | sort -u
   ```
2. **Check budget.** Compute remaining = the selector's
   `openrouter.remaining_usd` minus anything this run has already spent (§A).
   If remaining < $0.05, skip this section and note "self-check skipped:
   budget" in the session log.
3. **Send exactly those entries to an independent model** (typically ~$0.01
   per 25 entries):
   - Content changes (glosses, examples, notes, tags, new entries):
     ```bash
     python3 build/review_accuracy.py --ids <id1,id2,...> --budget 0.25
     ```
   - Furigana/format-only changes (typical for `systemic-fix`): use the
     furigana screener instead, and deep-review only what it flags:
     ```bash
     python3 build/review_runner.py --pass screening --ids <ids> --budget 0.15
     ```
   - In `accuracy-review` mode, skip IDs already covered by §A this run (the
     review itself was the check).
4. **Adjudicate every reported issue with your own judgment** per §C:
   **APPLY** clear errors (your own slips, and pre-existing errors the model
   caught); **REJECT** stylistic nits and model misreadings; **FLAG** genuine
   uncertainty by appending to `reviews/needs_curator.txt`. Tag-vocabulary
   flags follow the semantic-tag policy in §A step 4 (not-in-list = apply the
   migration; in-list narrowness nit = reject). Log every decision
   per §C. Update the `modified` timestamp on any entry you fix.
5. **Record spend in the ledger** using the snippet in §A step 5, with
   `phase: "self-check"`.
6. **If the model found nothing, say so in the session log** — a clean
   self-check is the expected steady state and is worth recording.

## 5. Metrics snapshot (every run, including wiki-only runs)

Append one line to `pipeline/metrics-history.jsonl` just before the session
log is written:

```bash
python3 pipeline/metrics_snapshot.py --mode <mode> --changed <entries changed this run>
```

Flag tallies are derived automatically from today's `reviews/decisions.jsonl`
lines (pass `--applied/--rejected/--flagged` only to override), and detector
queue depths are collected automatically about once a week. If the script is
missing or errors, note that in the session log and continue — never let
metrics block the wrap-up. This costs seconds and gives the curator (and the
weekly wiki trend review) a real time series instead of impressions.

## 6. Budget & context discipline (inherited from v1 — do not relax)

- **Plan to finish the mode's content work by ~55% of your context window.**
  §4 (self-verification) and §5 (metrics) are part of the wrap-up budget; the
  full wrap-up (verify, build, push, PR, CI wait, merge) needs ~40% headroom.
  Running out of context mid-merge is the single biggest cause of stranded PRs.
- **Take stock periodically.** If tool outputs are truncating or you've read
  several large files, wrap up early. Better one fewer entry than a stranded PR.
- **Single build.** Run `make build` **exactly once** per run (§7), and only if
  entries/build artifacts changed. **Wiki-only runs skip `make build`**
  (markdown changes don't touch `docs/`). After the build, do **not** make
  fix-up edits — log any newly-spotted issue as an `[entry]` observation and
  proceed to merge. (§4 runs *before* the build precisely so its fix round is
  included in the single build.)

## 7. Wrap up

1. **Update the mode's cursor/state** so the next run advances:
   - `polish` → `polishing/tasks/comprehensive/progress.txt` (`next: <after
     last frontier entry>`) AND `polishing/tasks/comprehensive/priority-cursor.txt`
     (`line: <next unprocessed priority line>`) if the priority lane ran.
   - `accuracy-review` → `polishing/tasks/cross-model-review/progress.txt`;
     ledger updated per §A; queue maintained per §A step 7.
   - `new-entries` → update `PROJECT_STATUS.md` Recent Changes (keep 5 most
     recent).
   - `wiki` → append to `planning/wiki/log.md`; update `index.md` for new pages.
   - The selector already advanced `pipeline/routine-state.json` in §1.
2. **Write a session log** `polishing/sessions/routine_{YYYY-MM-DD}_{NNN}.md`
   (next free NNN). Record: mode and the selector's `reason`, range/params
   worked, per-item changes, **§4 self-check outcome (clean / N applied / N
   rejected / N flagged)**, candidates added, observations logged, and the
   next cursor value(s).
3. **Build** (skip for `wiki`-only runs):
   ```bash
   make build
   ```
4. **Commit and push** everything (`git add -A`), including build artifacts
   (`docs/`, `entries_index.json`, `build/word_id_lookup.json`, `kanji/`) plus
   `pipeline/routine-state.json`, `pipeline/openrouter-ledger.json`,
   `pipeline/metrics-history.jsonl`, `reviews/decisions.jsonl`, and any
   `reviews/` artifacts:
   ```bash
   git add -A && git commit -m "routine(<mode>): <short summary>"
   git push -u origin "$(git rev-parse --abbrev-ref HEAD)"
   ```
5. **PR → wait for CI → merge** (MCP path; `gh` is not authorized in
   Routines). This is an **atomic tail**: after push, the only tool calls are
   these, in order — do not interleave edits.
   1. `mcp__github__create_pull_request` (`owner: "tkgally"`,
      `repo: "je-dict-1"`, `head: <branch>`, `base: "main"`, title
      `routine(<mode>): …`, body summarizing the run incl. the §4 outcome).
      Note the PR number.
   2. **Wait for CI by polling check-runs over MCP** (full loop in `CLAUDE.md`
      → "MCP path" step 5; `pipeline/wait-for-pr-checks.sh` 403s here and is not
      used). Call `mcp__github__pull_request_read` with `method: "get_check_runs"`
      (**not** `get_status`, which is blind to Actions checks). Classify: *green*
      = `total_count >= 1` and every run `completed` with `conclusion`
      `success`/`neutral`/`skipped`; *failed* = any other completed conclusion;
      *pending* = otherwise. While pending, wait with a backgrounded `sleep 30`
      (Bash `run_in_background: true`, since foreground `sleep` is disabled) and
      re-poll, up to ~16 times (~8 min).
   3. **green** → `mcp__github__merge_pull_request` with `merge_method: "squash"`.
      **failed** → leave the PR open, add a one-line note to the session log
      naming the failed check, and stop.
      **still pending at the cap** → leave the PR open and stop; the next run's
      §0a rescue merges it once green.
   - Do **not** `mcp__github__enable_pr_auto_merge` (it rejects on the
     `unstable` state right after creation). Do **not** `git checkout main` or
     delete the branch — the session is on that branch; the repo's
     "Automatically delete head branches" setting cleans up after the
     squash-merge.
6. **Release the lock** (after the merge call, or before stopping on a
   non-green CI result):
   ```bash
   python3 pipeline/routine_lock.py release --session "$(git rev-parse --abbrev-ref HEAD)"
   ```

---

## §A. accuracy-review playbook (furigana + glosses/translations/tags + queue)

Goal: get a **second model's** opinion on the dimensions another model is best
placed to catch, apply only the corrections you independently agree with, and
keep `reviews/queue.txt` (the CI-maintained "changed since last review" list)
converging instead of growing. Spend is capped per-run by the selector
(`params.openrouter_session_budget_usd`) and per-day by the ledger.

1. **Budget.** Read `params.openrouter_session_budget_usd` (already = the
   smaller of the per-session cap and the remaining daily budget). If it is
   `0` or missing, the daily cap is spent — **do not call OpenRouter**; log a
   note and stop. Otherwise size this run's ID range to the budget: screening
   + accuracy cost **~$0.5 per 1,000 entries**; the deep furigana pass is the
   expensive part (~$0.01/entry × flagged), so **cap deep spend at roughly
   one-third of the session budget**. Target ~400–600 entries per run. The
   binding constraint is usually adjudication effort, not dollars — shrink the
   range if step 4 is running long.
2. **Furigana correctness** — `build/review_runner.py` over a range starting
   at `params.start_id`:
   ```bash
   python3 build/review_runner.py --pass screening --range <start> <end> --budget <part>
   python3 build/review_runner.py --pass deep --range <start> <end> --budget <deep_cap>
   ```
   Screening is cheap; `--pass deep --range` deep-reviews **only the
   screening-flagged entries inside the range**. **Known-noise shortcut:** if
   every screening flag falls within the documented false-positive families
   (rendaku in compounds, okurigana/compound reading splits, readings the
   entry itself discusses — see `reviews/calibration_report.md`), bulk-reject
   them with one aggregated §C line and **skip the deep pass** (measured
   2026-06-10/11: screening over already-polished ranges ran 0–5% precision).
   **Resilience:** if the runner
   exits abnormally mid-pass, keep the per-entry results already written,
   append a `[tooling]` observation, and continue with step 3 — do not retry
   the whole pass.
3. **Glosses, example translations, and semantic tags** —
   `build/review_accuracy.py` over the same range (the `tags` dimension is the
   scalable fix for tag drift: it judges each semantic tag against the
   *headword*, not the example topics):
   ```bash
   python3 build/review_accuracy.py --range <start> <end> --budget <remaining>
   ```
   Each entry's issues land in `reviews/accuracy/{id}.json`. To front-load the
   contaminated P11 block (5700–6340 and the residue above the polish frontier),
   **`prompts/fix_semantic_tag_drift.md`** Phase 2 walks
   `polishing/tasks/semantic-tag-drift/progress.txt` with `--dimensions tags` —
   it is the authoritative path for the single-sole-wrong-category tags
   (朱肉→`animal-mammal`) that the deterministic checks cannot see.
4. **Apply corrections with judgment.** For furigana, follow
   **`prompts/polish_cross_model_review.md`** (consult
   `reviews/calibration_report.md` for known false positives). For each
   `reviews/accuracy/{id}.json`, decide **APPLY / REJECT / FLAG** per §C:
   - **APPLY** a clear gloss/translation fix or a clearly-wrong
     semantic/register tag; update the entry's `modified` timestamp.
   - **REJECT** stylistic nits or cases where the model is wrong.
   - **FLAG** genuine uncertainty for the curator
     (append to `reviews/needs_curator.txt`).
   **Semantic-tag policy (2026-06-11):** `VALID_SEMANTIC` in
   `build/validate_tags.py` is the single source of truth for tag vocabulary —
   the reviewer prompt embeds it. A flag that a tag is **not in the list is
   correct by definition**: APPLY it by migrating to the suggested or best
   in-list tag (`build/check_tag_drift.py` has the 1:1 migration map). Never
   reject such a flag on the grounds that the tag is "widely used" — usage
   counts are not the standard, and `schema.json` deliberately has no tag enum.
   Conversely, REJECT "too narrow/too broad" substitutions between in-list
   tags, and APPLY a formality flag only when the entry's own notes/register
   description contradicts the label.
   Never apply blindly; never add inline links in this mode. **Log every
   decision to `reviews/decisions.jsonl`** (§C). **Adjudication effort scales
   with flag quality** (measured 2026-06-10: error-severity flags ~4–13%
   applicable, warn-severity ~1%): work every `error`-severity issue
   individually; for `warn`-severity issues, sample ~10 per dimension, and if
   a recurring noise family emerges (same rejection reason repeating),
   bulk-reject the rest of that family with ONE aggregated §C line instead of
   reading hundreds of items. If more than ~20% of entries come back flagged,
   that is reviewer noise, not dictionary error — log a `[tooling]`
   observation with examples so the reviewer prompt can be tuned further.
5. **Record spend in the ledger** (enforces the daily $5 cap across runs).
   Replace the three arguments with the combined `Est. cost` reported by the
   review scripts, the phase label, and the entry count:
   ```bash
   python3 - "$EST_COST" "<phase>" "<n_entries>" <<'PY'
   import json, sys, datetime, pathlib
   est, phase, n = float(sys.argv[1]), sys.argv[2], int(sys.argv[3])
   p = pathlib.Path("pipeline/openrouter-ledger.json")
   L = json.loads(p.read_text(encoding="utf-8"))
   today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
   if L.get("date") != today:
       L["date"], L["spent_usd"], L["calls"] = today, 0.0, []
   L["spent_usd"] = round(float(L.get("spent_usd", 0)) + est, 4)
   L["calls"].append({"ts": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                      "mode": "accuracy-review" if phase != "self-check" else "self-check",
                      "phase": phase, "entries": n, "est_usd": round(est, 4)})
   p.write_text(json.dumps(L, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
   print("ledger spent_usd:", L["spent_usd"])
   PY
   ```
6. **Cursor.** Set `polishing/tasks/cross-model-review/progress.txt` to the
   next un-reviewed entry ID.
7. **Queue maintenance.** Remove the range you just reviewed from
   `reviews/queue.txt` so the queue converges to "changed since last review"
   (CI re-adds anything that changes later, including your own fixes — they
   get a second look by design):
   ```bash
   awk -v s=<start> -v e=<end> -F'[/_]' '!($1=="entries" && $3+0>=s && $3+0<=e)' reviews/queue.txt > /tmp/q.txt && mv /tmp/q.txt reviews/queue.txt
   ```
   Then wrap up (§7). The ledger, queue, decisions, and `reviews/` files are
   committed with the run.

## §B. systemic-fix playbook (semantic-verification-first)

Turns one accumulated wiki insight into a dictionary-wide correction. **The
default is per-entry semantic verification**, because the project's worst
regressions came from overly-ambitious mechanical sweeps.

1. Use `params.backlog_item` (the selector already picked the top open,
   batch-ready item from `planning/wiki/ideas/backlog-queue.json`). Read its
   `notes`/`verify` fields and cross-check its prose `source` in
   `planning/wiki/ideas/cleanup-backlog.md` / `tooling-backlog.md`.
2. Run the item's `detect` command and apply its `filter` if present. The
   detectors — `build/check_furigana_format.py`, `build/check_artifacts.py`,
   `build/check_tag_drift.py`, `build/check_example_headword.py` — are
   **read-only** and emit a JSON review queue (`--json`); they never modify
   entries. (If a future item needs a detector that doesn't exist, build it
   from the wiki's detection rules, commit it, then run it.) For the two
   high-precision P11 tag-drift items (`tag-proverb-idiom-mismatch`,
   `tag-concrete-noun-domain-mismatch`), follow **`prompts/fix_semantic_tag_drift.md`**
   — it has the per-check fix recipe (correct destination tag, the
   polysemy false-positive family to reject) and the cursor.
3. **Fix a bounded, semantically-verified batch** (sized by the §6 context
   rule): open each flagged entry, confirm the fix is correct *for that
   entry*, then apply it and update its `modified` timestamp. For furigana
   rewraps, validate against `build/word_id_lookup.json` so inline-link
   lookups still resolve. **Purely-mechanical application — transforming every
   match without reading the entry — is reserved for transformations that
   provably cannot introduce an error**, and even those are validated and
   spot-checked before commit. When in doubt, verify.
4. Run the §4 self-verification on the entries you changed (the furigana
   screener variant for format-only batches).
5. Update the item's `status`/`scope_estimate` in `backlog-queue.json` **and**
   its prose backlog page (mark RESOLVED or record remaining scope), then wrap
   up (§7).

## §C. Decision ledger (flag adjudication record)

Whenever you adjudicate an external model's flag — in §A step 4 or §4 step 4 —
append one line to `reviews/decisions.jsonl` (always append with `>>` or in
append mode; never rewrite the file):

```json
{"ts":"2026-06-10T03:12:00Z","entry":"00123","src":"accuracy","dim":"gloss","sev":"error","decision":"apply","note":"gloss said borrow, word means lend"}
```

- `src`: `accuracy` | `furigana` | `self-check`
- `dim`: `gloss` | `translation` | `tags` | `furigana`
- `decision`: `apply` | `reject` | `flag`
- `note`: ≤10 words, telegraphic.

Use **exactly these lowercase values** — mixed-case (`APPLY`) or ad-hoc `src`
values (`accuracy-review`) break the precision statistics. (Both drifts were
observed in the first week's ledger.)

When bulk-rejecting a recurring noise family (§A step 4), write ONE aggregated
line with an `"n"` count and no `"entry"` field:

```json
{"ts":"2026-06-10T03:12:00Z","src":"accuracy","dim":"translation","sev":"warn","decision":"reject","n":57,"note":"family: stylistic rewording suggestions"}
```

Aggregated lines keep precision statistics countable without spending context
on items already known to be noise.

This is what makes reviewer-flag **precision** measurable per dimension over
weeks (e.g. "translation flags: 80% applied; tags flags: 35% applied"). The
`wiki` mode's metrics-trend activity summarizes it, and the curator can use it
to tune which dimensions deserve trust, consensus checks, or retirement.

---

## Quick reference

```bash
# Pre-flight
mcp__github__list_pull_requests                         # §0a rescue check + §0b sweep source (MCP)
# §0b sweep: for un-rescued claude/* PRs, get_files → close superseded via MCP (sweep-stranded-prs.py 403s here)
mcp__github__list_branches                              # §0b orphan-branch sweep (CLAUDE.md → "Sweep orphan claude/* branches")
python3 pipeline/routine_lock.py acquire --session X    # §0b lock (exit 1 = stop)
python3 pipeline/routine_next.py                        # §1 pick mode (persists state)
python3 pipeline/routine_next.py --explain              # why this mode (no persist)
python3 pipeline/routine_next.py --force-mode polish    # manual per-mode test (no persist)

# Verification & metrics
python3 build/review_accuracy.py --ids 00123,00456 --budget 0.25      # §4 self-check (content)
python3 build/review_runner.py --pass screening --ids 00123 --budget 0.15  # §4 self-check (furigana)
python3 pipeline/metrics_snapshot.py --mode M --changed N ...         # §5 (or inline fallback)

# Wrap-up
make build                                              # once, at wrap-up (skip wiki-only)
mcp__github__pull_request_read method=get_check_runs    # §7 CI gate: poll until green (Bash run_in_background sleep 30 between polls)
mcp__github__merge_pull_request merge_method=squash     # §7 merge once green
python3 pipeline/routine_lock.py release --session X    # at the very end
```
