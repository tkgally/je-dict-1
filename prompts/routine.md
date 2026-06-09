# Unified Improvement Routine

**The single scheduled task for je-dict-1.** Each run does ONE focused unit of
high-quality work chosen by a selector, plus always-on lightweight capture, then
reliably merges its own PR. Designed to run unattended several times a day and to
make the dictionary steadily more accurate, consistent, and useful over weeks and
months — drawing on insights accumulated in the knowledge wiki — while keeping the
dictionary's existing concept, headword range, sense inventory, and example style.

This Routine **replaces** the three previously-separate scheduled tasks
(comprehensive polish, new-entry creation, nightly wiki maintenance). It does not
re-implement them — it **selects one mode per run and follows that mode's existing
prompt**. Balance across the work types is achieved across runs, by tunable
weights, not crammed into any single run. Scope is **Japanese→English only**.

> Design and rationale: `enhancement/unified-routine-plan-2026-06-09.md`.

---

## 0. Pre-flight (every run, before reading any entry/wiki data)

```bash
python3 pipeline/sweep-stranded-prs.py                  # self-heal a previous strand
python3 pipeline/routine_lock.py acquire --session "$(git rev-parse --abbrev-ref HEAD)"
```

- The sweep closes obsolete `claude/*` PRs whose entry range is already on main.
- If `routine_lock.py acquire` exits non-zero, another Routine run appears active —
  **stop now** (do not proceed). Otherwise you hold the lock; release it at the
  very end (step 5).

## 1. Select this run's mode

```bash
python3 pipeline/routine_next.py
```

This prints a JSON object and persists selector state. Read it:

```json
{ "mode": "polish", "params": { "start_id": 5936 },
  "reason": "...", "signals": { ... },
  "openrouter": { "remaining_usd": 5.0, "session_budget_usd": null }, ... }
```

- **`mode`** is your focus for this run. **`params`** carries the working range /
  budget / flags. **`reason`** and **`signals`** are for your session log.
- Do **not** second-guess the selector. Execute the mode it chose. (For manual
  testing the curator may instead run `routine_next.py --force-mode <mode>`, which
  prints the same JSON without perturbing the rotation.)

## 2. Execute the selected mode

Follow the matching playbook below. **Obey that prompt's per-session budget and
its PR/CI/merge discipline** — they are the same disciplines this Routine uses in
steps 4–5, so there is no conflict. Process the range/params the selector gave you.

| `mode` | Do this |
|---|---|
| `polish` | Follow **`prompts/comprehensive_polish.md`**, starting at `params.start_id`. Skip its own pre-flight sweep (already done in step 0). |
| `new-entries` | Follow **`prompts/newentries.md`**. Create ~`params.approx_count` (≈20) entries; prefer candidates whose notes say "seen in entry". If `params.candidates_low` is true, create what you sensibly can, then append `- [pattern] candidate_words.json running low — curator restock requested` to `polishing/observations.md`. **Never** auto-route to corpus harvesting or candidate discovery; the curator tops up candidates manually. |
| `accuracy-review` | Follow **§A** below (furigana cross-model review within budget, then apply corrections). |
| `wiki` | Follow **`planning/maintain-knowledge-base.md`** (harvest `polishing/observations.md`, then 2–4 wiki activities). Also keep `planning/wiki/ideas/backlog-queue.json` in sync if it exists (Phase 2). |
| `systemic-fix` | Follow **§B** below, working `params.backlog_item`. Semantic-verification-first: verify every flagged entry before changing it. |

**Wiki consultation (all modes).** Before working a range or topic, glance at the
wiki page(s) relevant to what you're touching — e.g.
`planning/wiki/topics/verb-transitivity.md`, `…/furigana-strategy.md`, or the
`planning/wiki/ideas/cleanup-backlog.md` priority covering your ID range. Read
only what's directly applicable; don't read the whole wiki.

## 3. Always-on capture (every mode, regardless of focus)

- **Missing words → candidates.** Any Japanese word you encounter in an example or
  note that lacks an entry: add it immediately with a source tag:
  ```bash
  python3 build/manage_candidates.py add "言葉" "ことば" "brief gloss; seen in entry XXXXX"
  ```
- **Systemic observations → `polishing/observations.md`**, using the existing tags
  (`[pattern] [wiki] [article] [tooling] [skill] [entry]`). This is what feeds the
  `wiki` and (Phase 2) `systemic-fix` modes.

## 4. Budget & context discipline (inherited verbatim — do not relax)

- **Keep working until ~60% of your context window, then wrap up.** The wrap-up
  (build, push, PR, up-to-10-min CI wait, merge) needs ~40% headroom. Running out
  of context mid-merge is the single biggest cause of stranded PRs.
- **Take stock periodically.** If tool outputs are truncating or you've read
  several large files, wrap up early. Better one fewer entry than a stranded PR.
- **Single build.** Run `make build` **exactly once** per run (step 5), and only if
  entries/build artifacts changed. **Wiki-only runs skip `make build`** (markdown
  changes don't touch `docs/`). After the build, do **not** make fix-up edits — log
  any newly-spotted issue as a `[entry]` observation and proceed to merge.

## 5. Wrap up

1. **Update the mode's cursor/state** so the next run advances:
   - `polish` → set `polishing/tasks/comprehensive/progress.txt` to `next: <after last entry>`.
   - `accuracy-review` → set `polishing/tasks/cross-model-review/progress.txt`; update the ledger (see §A).
   - `new-entries` → update `PROJECT_STATUS.md` Recent Changes (keep 5 most recent).
   - `wiki` → append to `planning/wiki/log.md`; update `index.md` for new pages.
   - The selector already advanced `pipeline/routine-state.json` in step 1.
2. **Write a session log** `polishing/sessions/routine_{YYYY-MM-DD}_{NNN}.md`
   (next free NNN). Record: **mode and the selector's `reason`**, the
   range/params worked, per-item changes, candidates added, observations logged,
   and the next cursor value.
3. **Build** (skip for `wiki`-only runs):
   ```bash
   make build
   ```
4. **Commit and push** everything (`git add -A`), including build artifacts
   (`docs/`, `entries_index.json`, `build/word_id_lookup.json`, `kanji/`) plus the
   updated `pipeline/routine-state.json` / `pipeline/openrouter-ledger.json`:
   ```bash
   git add -A && git commit -m "routine(<mode>): <short summary>"
   git push -u origin "$(git rev-parse --abbrev-ref HEAD)"
   ```
5. **PR → wait for CI → merge** (MCP path; `gh` is not authorized in Routines).
   This is an **atomic tail**: after push, the only tool calls are these three, in
   order — do not interleave edits.
   1. `mcp__github__create_pull_request` (`owner: "tkgally"`, `repo: "je-dict-1"`,
      `head: <branch>`, `base: "main"`, title `routine(<mode>): …`, body
      summarizing the run). Note the PR number.
   2. Run `pipeline/wait-for-pr-checks.sh <pr_number> 30` via the **Monitor** tool.
      Exit 0 = all green; 1 = a check failed; 2 = timeout; 3 = auth/API error;
      4 = no checks appeared.
   3. **Exit 0** → `mcp__github__merge_pull_request` with `merge_method: "squash"`.
      **Any non-zero** → leave the PR open, add a one-line note to the session log
      explaining what the helper reported, and stop.
   - Do **not** `mcp__github__enable_pr_auto_merge` (it rejects on the `unstable`
     state right after creation). Do **not** `git checkout main` or delete the
     branch — the session is on that branch; the repo's "Automatically delete head
     branches" setting cleans up after the squash-merge.
6. **Release the lock** (after the merge call, or before stopping on a non-zero CI
   result):
   ```bash
   python3 pipeline/routine_lock.py release --session "$(git rev-parse --abbrev-ref HEAD)"
   ```

---

## §A. accuracy-review playbook (Phase 1: furigana)

Goal: get a **second model's** opinion on furigana correctness, then apply only the
corrections you independently agree with. The OpenRouter spend is capped per-run by
the selector and per-day by the ledger.

1. **Budget.** Use `params.openrouter_session_budget_usd` (already = the smaller of
   the per-session cap and the remaining daily budget). If it is `0` or missing, the
   daily cap is spent — **do not call OpenRouter**; pick up by re-running
   `routine_next.py` is not needed (the selector won't choose this mode when the cap
   is reached). In the rare case you still got here with $0, log a note and stop.
2. **Screen + deep-review a range** starting at `params.start_id`:
   ```bash
   python3 build/review_runner.py --pass screening --range <start> <end> --budget <session_budget>
   python3 build/review_runner.py --pass deep --range <start> <end> --budget <remaining_session_budget>
   ```
   Choose `<end>` to stay within budget (screening is cheap; deep covers only
   flagged entries). `review_runner.py` prints an `Est. cost: $X` total.
3. **Apply corrections** by following **`prompts/polish_cross_model_review.md`**:
   read each flagged entry, evaluate with your own knowledge of Japanese, and
   **APPLY / REJECT / FLAG**. Never apply a single low-confidence flag; consult
   `reviews/calibration_report.md` for known false-positive patterns; FLAG genuine
   uncertainty for the curator. Update `modified` timestamps on entries you change.
4. **Record spend in the ledger** (so the daily $5 cap is enforced across runs):
   ```bash
   python3 - "$EST_COST" <<'PY'
   import json, sys, datetime, pathlib
   est = float(sys.argv[1])
   p = pathlib.Path("pipeline/openrouter-ledger.json")
   L = json.loads(p.read_text(encoding="utf-8"))
   today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
   if L.get("date") != today:
       L["date"], L["spent_usd"], L["calls"] = today, 0.0, []
   L["spent_usd"] = round(float(L.get("spent_usd", 0)) + est, 4)
   L["calls"].append({"ts": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                      "mode": "accuracy-review", "est_usd": round(est, 4)})
   p.write_text(json.dumps(L, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
   print("ledger spent_usd:", L["spent_usd"])
   PY
   ```
   Replace `$EST_COST` with the number `review_runner.py` reported.
5. **Cursor.** Set `polishing/tasks/cross-model-review/progress.txt` to the next
   un-reviewed entry id. Then wrap up (step 5). The ledger JSON is committed with
   the run.

## §B. systemic-fix playbook (semantic-verification-first)

Turns one accumulated wiki insight into a dictionary-wide correction. **The default
is per-entry semantic verification**, because the project's worst regressions came
from overly-ambitious mechanical sweeps.

1. Use `params.backlog_item` (the selector already picked the top open,
   batch-ready item from `planning/wiki/ideas/backlog-queue.json`). Read its
   `notes`/`verify` fields and cross-check its prose `source` in
   `planning/wiki/ideas/cleanup-backlog.md` / `tooling-backlog.md`.
2. Run the item's `detect` command and apply its `filter` if present. The
   detectors — `build/check_furigana_format.py`, `build/check_artifacts.py`,
   `build/check_tag_drift.py` — are **read-only** and emit a JSON review queue
   (`--json`); they never modify entries. (If a future item ever needs a detector
   that doesn't exist, build it from the wiki's detection rules, commit it, then
   run it.)
3. **Fix a bounded, semantically-verified batch** (sized by the 60%-context rule):
   open each flagged entry, confirm the fix is correct *for that entry*, then apply
   it and update its `modified` timestamp. For furigana rewraps, validate against
   `build/word_id_lookup.json` so inline-link lookups still resolve. **Purely-
   mechanical application — transforming every match without reading the entry — is
   reserved for transformations that provably cannot introduce an error**, and even
   those are validated and spot-checked before commit. When in doubt, verify.
4. Update the item's `status`/`scope_estimate` in `backlog-queue.json` **and** its
   prose backlog page (mark RESOLVED or record remaining scope), then wrap up
   (step 5).

---

## Quick reference

```bash
python3 pipeline/sweep-stranded-prs.py                 # pre-flight
python3 pipeline/routine_lock.py acquire --session X   # pre-flight lock (exit 1 = stop)
python3 pipeline/routine_next.py                       # pick mode (persists state)
python3 pipeline/routine_next.py --explain             # why this mode (no persist)
python3 pipeline/routine_next.py --simulate 60         # mode distribution over 60 runs
python3 pipeline/routine_next.py --force-mode polish   # manual per-mode test (no persist)
make build                                             # once, at wrap-up (skip for wiki-only)
python3 pipeline/routine_lock.py release --session X   # at the very end
```
