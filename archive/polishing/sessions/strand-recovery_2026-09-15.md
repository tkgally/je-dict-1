# Interactive session 2026-09-15 — stranded Routine branches: diagnosis and recovery

Tom paused the twice-daily Routine and asked for the stranded, unmerged `claude/*` branches to be
examined, the causes found, and every unmerged change either merged or reverted.

## State found

| Branch | PR | State | Content |
|---|---|---|---|
| `claude/trusting-mendel-gqtngu` | #3299 | open, CI green | systemic-fix (katakana noentry demotion), no entries |
| `claude/trusting-mendel-1b7wtk` | #3293 | open, CI **failed** | 20 new entries 30893–30912 + 3 neighbours |
| `claude/trusting-mendel-o9cv7c` | #3290 | **closed unmerged** by the sweep, CI failed | polish of 27 entries (priority lane + frontier 07340–07354) |
| `claude/trusting-mendel-u8emu6` | #3294 | merged | nothing beyond main (ledger lines only) |

## Causes

1. **The CI wait never waited.** §7 told the run to poll `get_check_runs` at most 16 times with a
   backgrounded `sleep 30` between polls. A backgrounded sleep returns immediately, so the 16
   polls finished in one to three minutes while the `validate` check takes five to seven. Every
   run logged "CI still pending after 16 polls (~8 min)"; the timestamps show the truth:

   | PR | created | "CI still pending" note pushed | first CI run finished |
   |---|---|---|---|
   | #3299 | 12:45:55 | 12:48:10 (+2m15s) | 12:52:15 (+6m20s) |
   | #3298 | 08:53:24 | 08:55:37 (+2m13s) | ~08:59 |
   | #3294 | 13:00:11 | 13:01:37 (+1m26s) | 13:05:16 |
   | #3290 | 01:01:53 | 01:04:57 (+3m04s) | 01:07:29 |

2. **Pushing the "still pending" note restarted CI.** Each run then committed that note to its
   session log and pushed, which triggered a fresh CI run on the new head, so even a patient poll
   would have seen "pending" again. The PRs were rescued only by the next run's pre-flight four
   hours later. That is why nearly every PR since 2026-09-13 was merged by a later run rather
   than its own.

3. **Two PRs had real CI failures that no rule was allowed to fix.** #3293 failed the ratchet on
   kana-only furigana braces in two new entries (`{を|を}` in 30906, `{フルコース|ふるこーす}` in
   30907); #3290 failed the notes-header gate on 07345 (`SIMILAR WORDS (least to most formal):`).
   Neither `make index` nor anything else in the wrap-up runs those gates, so the runs pushed
   red PRs, and §7 said "failed → leave it open, stop".

4. **The "stale PR" sweep closed real work.** The rule closed a routine PR when every entry it
   touched had an ID below the polishing frontier. #3290's range (07340–07354) fell below the
   frontier only because the next polish run had deliberately *skipped* that range to avoid the
   open PR, so the sweep closed 27 entries' worth of polish that nobody had redone.

5. **The orphan-branch residue check was unreliable by hand.** u8emu6 (merged) was reported twice
   as carrying "18 unmerged entries"; it carried none. Ledgers differ from main whenever main has
   appended more lines, which a by-eye diff reads as residue.

6. Minor: the prompt's `auto_link.py --ids … --apply` line lacks `--confirm-real-entries`, which
   the script requires to write into `entries/`; `validate.py --id` did not accept a bare number.

## What this session did

- Merged #3299 (green, mergeable, no human comment).
- Wrote `pipeline/absorb_branch.py`: merges a stranded branch into the current branch with a
  per-file policy (entries and code merge normally; indexes, cursors, ledgers of the run keep
  main's version; append-only ledgers take the union; a colliding session log is renamed to the
  next free number; `candidate_words.json` is reconciled — candidates the branch turned into
  entries are dropped, candidates it queued are re-added with fresh IDs; PROJECT_STATUS.md gets
  the branch's Recent Changes section in date order; any entry or code conflict aborts). Its
  `--residue` mode is the deterministic orphan check. Unit tests in
  `build/tests/test_absorb_branch.py`.
- Absorbed #3293 (23 entries) and #3290 (27 entries) with it. No entry had been changed on main
  since either branch diverged, so every entry merged clean. The 14 candidates #3290 had queued
  under IDs C23427–C23440 (which main had since reused for other words) were re-queued as
  C23460–C23473. #3293's consumed candidates (20 crab/harbor-porpoise/etc. words) were removed.
  Session logs renamed to `routine_2026-09-14_006.md` (#3293) and `routine_2026-09-14_007.md`
  (#3290).
- Fixed the three gate failures (30906, 30907, 07345), ran the mechanical pass on all 50 entries
  (the linker added links in 19 of the 20 new entries to words that gained entries after that
  branch was written), and the kana-link review on the 20 new entries.
- Added `make gate` (exactly the CI steps) and `pipeline/wait.py` (a foreground wait that prints
  its elapsed time).
- Rewrote `prompts/routine2.md` §0 and §7 and the matching CLAUDE.md sections: absorb a red
  predecessor instead of leaving or closing it; never close a routine PR by cursor position;
  `make gate` before the push; no commit or push after the PR is opened; wait with
  `pipeline/wait.py 60`, at most 15 polls; on a failed check, fix and push once.
- Closed #3293 with an "absorbed" comment after this session's PR (#3300) merged. Tried to delete
  the three fully absorbed branches (`1b7wtk`, `o9cv7c`, `u8emu6`): the git proxy in this
  environment refuses branch deletion (HTTP 403), so they are recorded in
  `pipeline/absorbed-branches.jsonl` (the tool's ledger of absorbed branch tips, so no later run
  re-absorbs them) and left for Tom to delete; three `prune-branch` lines are in
  `reviews/needs_curator.txt`.

## Self-check

The two absorbed runs had already passed their own independent review; this session's edits to
entries are the three one-token gate fixes and deterministic linker output. The kana-link review
on the 20 new entries judged the 4 newly added kana links and flagged none (about $0.000). No
accuracy review was re-run.
