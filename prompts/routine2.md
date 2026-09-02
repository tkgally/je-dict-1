# Unified Improvement Routine v3

**The single scheduled task for je-dict-1.** Each run does ONE focused unit of
work chosen by a deterministic selector, verifies its own changes with an
independent model before merging, records one line of quality metrics, and
merges its own pull request. It runs unattended twice a day and is written for
a mid-size model: follow it literally, in order, and do not improvise around it.

v3 (2026-09-02) replaces v2 after the assessment in
`enhancement/assessment-2026-09-02.md`. What changed: mechanical work (inline
links, cross-references, header and metadata normalization) is done by scripts,
so the `polish` mode does judgment work only; the external reviewer now checks
the notes field and filters its own noise; the wiki runs only when observations
pile up; new entries come from words the dictionary already uses; the site is
built by GitHub Actions on merge, so runs no longer commit `docs/`.

Scope is Japanese→English only. Never renumber or rename an entry (IDs are live
URLs). Never edit basic- or core-tier headwords or tiers.

---

## 0. Pre-flight (before reading any entry)

**0a. Rescue a green predecessor.** Call `mcp__github__list_pull_requests`
(`owner: "tkgally"`, `repo: "je-dict-1"`, `state: "open"`). For each open PR
whose head branch starts with `claude/` AND whose title starts with `routine`:
call `mcp__github__pull_request_read` with `method: "get"` and with
`method: "get_check_runs"` (never `get_status`). Merge it with
`mcp__github__merge_pull_request` (`merge_method: "squash"`) only if every
check run is `completed` with conclusion `success`, `neutral`, or `skipped`,
the PR is mergeable, and no human has commented or reviewed. Then
`git fetch origin main && git merge origin/main --no-edit`. Anything not
rescuable stays open; mention it in the session log.

**0b. Sweep strands.** For any other open `claude/*` PR, follow CLAUDE.md →
"Sweep stranded PRs via MCP" (close it only if every entry file it touches has
an ID below the `next:` value in `polishing/tasks/comprehensive/progress.txt`).
Then `mcp__github__list_branches`; for any `claude/*` branch that is neither
this session's branch nor an open PR's head, follow CLAUDE.md → "Sweep orphan
`claude/*` branches via MCP". Zero strands and zero orphans is the normal case.

There is no lock step: each run is a fresh container and the schedule never
overlaps runs.

## 1. Select the mode

```bash
python3 pipeline/routine_next.py
```

Read the JSON: `mode` is this run's focus, `params` its inputs, `reason` and
`signals` go in the session log. Do not second-guess the selector.

## 2. Execute the mode

| `mode` | Do this |
|---|---|
| `polish` | Follow **`prompts/comprehensive_polish.md`**. Two lanes: the priority lane (`polishing/priority/notes.txt` from the cursor in `polishing/tasks/comprehensive/priority-cursor.txt`) for about half the budget, then the sequential frontier from `params.start_id`. Judgment work only: correctness, the one contrast or warning a learner needs, trimming, tags. Scripts handle links and cross-references at wrap-up (§3). Target 25–40 entries. |
| `accuracy-review` | Follow **§A**: send a range of 800–1,200 entries starting at `params.start_id` to the external reviewer (gloss, translation, tags, notes), adjudicate every surviving flag, fix what is wrong, maintain the queue. No furigana screening pass. |
| `systemic-fix` | Follow **§B** with `params.backlog_item`: run its detector, verify each flagged entry, fix a bounded batch, update the item's status. |
| `new-entries` | Follow **`prompts/newentries.md`**. Create about `params.approx_count` (20) entries, taking candidates whose notes say "seen in entry" or "used in" first (internal closure); if fewer than 20 such candidates exist, take the rest from the queue and stop early rather than inventing headwords. Then run the post-creation sequence in that prompt, which links, cross-references, and re-checks homographs. |
| `candidates` | Follow **`prompts/newcandidates.md`**: restock the queue with words the dictionary already uses but has not defined (`check_stale_noentry.py` unresolved class, words seen during review), each vetted individually; at most ten curated additions from other lenses per run. |
| `wiki` | Follow **`planning/maintain-knowledge-base.md`**: harvest `polishing/observations.md` into `planning/wiki/ideas/backlog-queue.json`, write one short log entry, regenerate the metrics page with `python3 pipeline/metrics_report.py`. No essays, no new prose on the metrics page, no page may grow by more than 300 words. |

Before working a range, glance only at wiki pages directly relevant to it
(start from `planning/wiki/index.md`); do not read the wiki broadly.

## 3. Mechanical pass on every entry this run created or rewrote

Run this after the mode's content work and before the self-check, on the IDs
you changed (see §4 step 1 for the command that lists them):

```bash
python3 build/normalize_notes.py --ids <ids> --apply      # canonical headers, '- ' bullets
python3 build/auto_link.py --ids <ids> --apply            # unambiguous inline links
python3 build/harvest_crossrefs.py --ids <ids> --apply    # cross-references named in notes
python3 build/validate.py --id <id> ...                   # each changed entry
```

Never hand-place inline links; the linker leaves ambiguous tokens alone, and a
polish run may link those by hand only where the sentence makes the word
certain. Never add `noentry` markers by hand; log the missing word as a
candidate instead (`manage_candidates.py add "語" "ご" "gloss; seen in entry
NNNNN"`).

## 4. Verify your own changes (every run that changed entries)

One verification pass, one fix round, then stop; never re-verify the fix round.

1. List the changed IDs:
   ```bash
   git status --porcelain -- entries/ | sed -E 's/^.{3}//' | sed -E 's|.*/([0-9]{5})_.*|\1|' | sort -u
   ```
2. If the selector's `openrouter.remaining_usd` minus this run's spend is under
   $0.05, skip with "self-check skipped: budget" in the log.
3. Send the changed entries plus every neighbour you opened to the reviewer:
   ```bash
   python3 build/review_accuracy.py --ids <id1,id2,...> --budget 0.40
   ```
   It writes `reviews/accuracy/{id}.json` (local) and appends flagged entries
   to `reviews/accuracy_flags.jsonl`. Off-vocabulary tags are flagged by code;
   breadth complaints, unquoted register or notes flags, and `warn` severity
   are already filtered out.
4. Adjudicate every surviving issue per §C: APPLY clear errors (yours or
   pre-existing), REJECT model misreadings, FLAG genuine uncertainty to
   `reviews/needs_curator.txt`. A `notes` flag with a verbatim quote deserves a
   careful look: the notes are where past factual errors slipped through.
   Update `modified` on any entry you fix. Log every decision (§C).
5. Record spend in the ledger with the snippet in §A step 5, `phase: "self-check"`.
6. If the model found nothing, say so in the session log.

## 5. Metrics snapshot (every run)

```bash
python3 pipeline/metrics_snapshot.py --mode <mode> --changed <entries changed this run>
```

Flag tallies are derived from `reviews/decisions.jsonl` lines logged since the
previous snapshot. If the script errors, note it and continue.

## 6. Budget and context discipline

- Finish the mode's content work by about 55 percent of the context window.
  §3–§5 and the wrap-up need the rest. Running out of context mid-merge is the
  one failure that costs a whole run.
- Take stock every ten entries; wrap up early if tool output is truncating.
- Do not run `make build`; the site is built by GitHub Actions after merge.
  Run `make index` exactly once at wrap-up (validation plus index and kanji
  JSON refresh). After it, make no further edits: log anything you notice as an
  `[entry]` observation.

## 7. Wrap up

1. **Advance the cursors**: `polish` → `polishing/tasks/comprehensive/progress.txt`
   (`next: <after last frontier entry>`) and `priority-cursor.txt`;
   `accuracy-review` → `polishing/tasks/cross-model-review/progress.txt` and
   the queue (§A step 7); `new-entries` and `candidates` → the
   `PROJECT_STATUS.md` Recent Changes section (keep five); `wiki` →
   `planning/wiki/log.md`. The selector already persisted its state.
2. **Write the session log** `polishing/sessions/routine_{YYYY-MM-DD}_{NNN}.md`
   (next free NNN): mode and reason, range or params, per-item changes, the
   self-check outcome (clean / N applied / N rejected / N flagged), candidates
   added, observations logged, next cursor values.
3. **Refresh indexes**: `make index`.
4. **Commit and push everything** (`git add -A`), including
   `entries_index.json`, `build/word_id_lookup.json`, `kanji/`,
   `pipeline/routine-state.json`, `pipeline/openrouter-ledger.json`,
   `pipeline/metrics-history.jsonl`, `reviews/decisions.jsonl`,
   `reviews/accuracy_flags.jsonl`, `reviews/screening/screening_status.json`:
   ```bash
   git add -A && git commit -m "routine(<mode>): <short summary>"
   git push -u origin "$(git rev-parse --abbrev-ref HEAD)"
   ```
5. **PR → CI → merge**, the atomic tail (no other tool calls in between):
   1. `mcp__github__create_pull_request` (`owner: "tkgally"`, `repo:
      "je-dict-1"`, `head: <branch>`, `base: "main"`); title
      `routine(<mode>): …` and a body written per
      `.claude/skills/clear-reports/SKILL.md` (plain English for the curator,
      the self-check outcome included). Note the PR number.
   2. Poll `mcp__github__pull_request_read` with `method: "get_check_runs"`.
      Green = every run `completed` with conclusion `success`, `neutral`, or
      `skipped`; failed = any other completed conclusion; pending = otherwise.
      While pending, wait with a backgrounded `sleep 30` (Bash
      `run_in_background: true`) and re-poll, at most 16 times.
   3. Green → `mcp__github__merge_pull_request` with `merge_method: "squash"`.
      Failed → leave the PR open, name the failed check in the session log,
      stop. Still pending at the cap → leave it open and stop; the next run's
      §0a rescues it.
   - Never `enable_pr_auto_merge`, never `git checkout main`, never delete the
     branch.
6. **End with a clear report** per the `clear-reports` skill: what this run did
   and found, in plain English, and what if anything needs the curator.

---

## §A. accuracy-review playbook

Goal: a second model's opinion on the dimensions it is best placed to catch,
applied only where you independently agree, keeping `reviews/queue.txt`
converging.

1. **Budget.** `params.openrouter_session_budget_usd` is the cap for this run
   (0 or missing → do not call OpenRouter; log and stop). Cost is about $0.6
   per 1,000 entries with the notes dimension. Size the range to 800–1,200
   entries from `params.start_id`; shrink it if adjudication is running long.
2. **Do not run the furigana screener** (`review_runner.py`). Its flags ran at
   2 percent precision over the whole series; the accuracy reviewer and the
   deterministic furigana checks cover the ground.
3. **Review**:
   ```bash
   python3 build/review_accuracy.py --range <start> <end> --budget <budget>
   ```
   Each entry's surviving issues land in `reviews/accuracy/{id}.json`; flagged
   entries are also appended to `reviews/accuracy_flags.jsonl`. The `family`
   field tells you what kind of flag it is: `offvocab` (deterministic, always
   apply the migration to the suggested or best in-list tag),
   `wrong-category`, `register` (comes with a verbatim quote), `gloss-meaning`,
   `translation-meaning`, `notes-fact` (comes with a verbatim quote).
4. **Adjudicate** every issue: APPLY / REJECT / FLAG per §C. Never apply
   blindly; open the entry. For `notes-fact`, check the claim against your own
   knowledge and the rest of the entry. If more than 25 percent of entries
   come back flagged, that is reviewer noise: log a `[tooling]` observation
   with examples. Update `modified` on every entry you change.
5. **Ledger**:
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
6. **Cursor**: `polishing/tasks/cross-model-review/progress.txt` → `next: <end+1>`.
   When the cursor passes the highest entry ID, reset it to `next: 00001`; the
   second pass reviews with the notes dimension what the first pass reviewed
   without it.
7. **Queue**: remove the reviewed range from `reviews/queue.txt`:
   ```bash
   awk -v s=<start> -v e=<end> -F'[/_]' '!($1=="entries" && $3+0>=s && $3+0<=e)' reviews/queue.txt > /tmp/q.txt && mv /tmp/q.txt reviews/queue.txt
   ```
8. Run §3 on the entries you changed, then the §4 self-check is not needed
   for IDs in the reviewed range (the review was the check); skip §4 for them.

## §B. systemic-fix playbook

1. Read `params.backlog_item` (`notes`, `detect`, `filter`, `verify`) and its
   prose source in `planning/wiki/ideas/cleanup-backlog.md` or
   `tooling-backlog.md`.
2. Run the item's `detect` command; apply its `filter`. Detectors are
   read-only and emit a JSON queue; they never modify entries.
3. Fix a bounded batch (sized by §6): open each flagged entry, confirm the fix
   is right for that entry, apply it, update `modified`. Purely mechanical
   application without reading the entry is reserved for transformations that
   provably cannot introduce an error, and even those are validated and
   spot-checked. When in doubt, verify.
4. Run §3 and §4 on the changed entries.
5. Update the item's `status` and `scope_estimate` in `backlog-queue.json` and
   its prose page (RESOLVED, or the remaining scope), then wrap up.

## §C. Decision ledger

For every adjudicated flag append one line to `reviews/decisions.jsonl`
(always append; never rewrite):

```json
{"ts":"2026-09-02T03:12:00Z","entry":"00123","src":"accuracy","dim":"gloss","family":"gloss-meaning","sev":"error","decision":"apply","note":"gloss said borrow, word means lend"}
```

- `src`: `accuracy` | `self-check`
- `dim`: `gloss` | `translation` | `tags` | `notes`
- `family`: copy the issue's `family` field
- `decision`: `apply` | `reject` | `flag`
- `note`: at most ten words.

Use exactly these lowercase values. For a recurring noise family you rejected
in bulk, write ONE aggregated line with an `"n"` count and no `"entry"`.

---

## Quick reference

```bash
mcp__github__list_pull_requests / list_branches          # §0 rescue and sweeps
python3 pipeline/routine_next.py                         # §1 pick the mode
python3 build/normalize_notes.py --ids … --apply         # §3 mechanical pass
python3 build/auto_link.py --ids … --apply
python3 build/harvest_crossrefs.py --ids … --apply
python3 build/review_accuracy.py --ids … --budget 0.40   # §4 self-check
python3 build/review_accuracy.py --range S E --budget B  # §A sweep
python3 pipeline/metrics_snapshot.py --mode M --changed N
make index                                               # §7 indexes (no site build)
mcp__github__create_pull_request → get_check_runs → merge_pull_request (squash)
```
