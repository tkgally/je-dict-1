# Fix Spurious Conjugations on Non-Verb Entries (one-time task)

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

A **one-time, deterministic cleanup task**. Strip the fabricated verb conjugation
tables that were generated onto adverbs, onomatopoeia, expressions, and other
non-verb / non-i-adjective entries, then add a defensive guard so they can never
regenerate. Also catalogue any *other* conjugation problems you notice (verbs
with the wrong conjugation class, verbs or i-adjectives missing a table) into the
knowledge base for future sessions.

This is not a progress-tracked polishing task — it runs once, sweeps the whole
dictionary, and closes out a set of long-standing backlog items. When it is
merged, the originating problem (Cleanup Backlog → Priority 6; Tooling Backlog →
item 5; Entry Follow-ups → "Twelve onomatopoeia entries" and four sibling
sections) is resolved.

## Pre-flight: sweep stranded PRs

**Run this as the first step of the session, before any other work.**

Perform the stranded-PR sweep **via MCP**, as described in `CLAUDE.md` → "Sweep
stranded PRs via MCP": `mcp__github__list_pull_requests`, and for each open
`claude/*` PR, close (with a comment) the ones whose maximum entry ID is below
`polishing/tasks/comprehensive/progress.txt`'s `next:` value. This task will not
be auto-closed by accident — it touches build scripts and wiki pages, not just a
narrow entry range. **Do not run `pipeline/sweep-stranded-prs.py`** — direct
GitHub REST returns HTTP 403 here, so it's a no-op (it now exits cleanly with a
pointer to the MCP procedure).

## Background — why this task exists

`build/add_conjugations.py` reads `metadata.tags.verb_class` and treats it as
authoritative. A large batch of non-verb entries carries a **stray `verb_class`
tag** (e.g., an adverb tagged `verb_class: "godan-tsu"`). That stray tag drove
the retrofit to generate a full 17-form godan table of nonsense — for example
ぐつぐつ ("simmering", an adverb/onomatopoeia) acquired forms like
`ぐつぐたない` (present negative) and `ぐつぐちます` (polite). Roughly **130
entries** are affected (91 adverbs incl. 12 onomatopoeia, ~32 expressions, a
handful of noun-adverbs, 2 auxiliaries, a few na-adjectives).

**The live root cause (important — the cleanup will not stick without it):** the
guard at the top of `_detect_verb_type` is

```python
if not any('verb' in p for p in ([pos] + pos_tags)):
    return None, None
```

The substring test `'verb' in p` is **true for `"adverb"`** — the string
"adverb" literally contains "verb". So adverbs pass the guard, and a stray
`verb_class: "godan-*"` then drives godan generation. Because
`add_conjugations.py` runs as part of every new-entries build, **simply deleting
the tables would let the next build regenerate them.** You must fix the guard
*first*.

`build/add_adjective_conjugations.py` is **already** correctly guarded
(`if 'adjective-i' not in pos_tags: return None, None`) and there are currently
**zero** spurious i-adjective tables — so only `add_conjugations.py` needs a code
change.

Further reading (skim only what you need):
- `planning/wiki/ideas/cleanup-backlog.md` → Priority 6 (the 130-entry breakdown + detection one-liner)
- `planning/wiki/ideas/tooling-backlog.md` → item 5 (the two-part fix: pruner + guard)
- `planning/wiki/ideas/entry-followups.md` → the "Twelve onomatopoeia…", `00536_itsu`, `00601_yoku`/`00602_mou`, `05173`/`05175` sections (all resolved by this sweep)
- `planning/wiki/topics/schema-tag-reliability.md` → "Runaway automation"

## Scope

**In scope — fix now (deterministic):**

1. **Defensive guard** in `build/add_conjugations.py` so non-verb POS entries can
   never get a conjugation table again.
2. **Strip** the `conjugation` field **and** the stray `verb_class` tag from every
   entry whose `metadata.tags.pos` contains **none** of `verb-godan`,
   `verb-ichidan`, `verb-suru`, `verb-kuru`, `verb-irregular`, `adjective-i`.
   (In this dictionary only verbs and i-adjectives carry conjugation tables;
   na/no/taru adjectives, adverbs, onomatopoeia, nouns, expressions, particles,
   auxiliaries, etc. never do.)

**Judgment — review each before acting (the ~32 `expression` entries):**

3. Most idioms (反応を見る, 場を和ませる, 手を打つ) do **not** conjugate as a unit
   → strip, same as above. Compound-`ている` forms tagged `expression`
   (空いている, 混んでいる) → strip; the *base* verb (空く, 混む) carries the real
   conjugation. If an "expression" entry is in fact a single verb mis-tagged as
   `expression` (rare), prefer **re-tagging** it to the correct `verb-*` POS +
   `verb_class` and regenerating a *correct* table — but if there is any doubt,
   strip and log it under Entry Follow-ups for a curator's second look.

**Out of scope — do NOT fix here, just LOG to Entry Follow-ups (see step 5):**
verbs with the *wrong* conjugation class, polite-only verbs with a bad template,
compound-`ている` *verb* entries, and i-adjectives/verbs *missing* a table because
of a malformed headword or mis-tagged POS. Several are already logged
(`00004_aogu`, `08261_totonoenaosu`, `01300_gozaimasu`, `02617_kondeiru`,
`01525_wakai`, `17582`/`08385`/`08016`). Add any new ones you discover; do not
try to repair them in this session (it would blow the budget and mix concerns).

## Step 1 — Add the defensive guard (do this first)

Edit `build/add_conjugations.py`. In `_detect_verb_type`, replace the substring
guard:

```python
    if not any('verb' in p for p in ([pos] + pos_tags)):
        return None, None
```

with an exact-enum guard:

```python
    # Defensive guard: only generate conjugations for entries explicitly tagged
    # with a verb POS in metadata.tags.pos. The previous check used the substring
    # 'verb', which matches "adverb" (it contains "verb") and let adverbs with a
    # stray verb_class tag generate nonsense godan tables. See planning/wiki
    # tooling-backlog.md item 5 and schema-tag-reliability.md "Runaway automation".
    VERB_POS_TAGS = {'verb-godan', 'verb-ichidan', 'verb-suru',
                     'verb-kuru', 'verb-irregular'}
    if not any(p in VERB_POS_TAGS for p in pos_tags):
        return None, None
```

`add_adjective_conjugations.py` already has the equivalent guard
(`if 'adjective-i' not in pos_tags`). Confirm it is present; no edit needed.

**Prove the guard is safe and effective** before touching any entry:

```bash
# Should report it would (re)generate tables for ALL legitimate verbs (~7,000)
# and ZERO of the non-verbs — i.e., the spurious entries are now skipped.
python3 build/add_conjugations.py --force --dry-run --stats
```

Sanity-check (optional but reassuring): the count of "Would add" should match the
number of entries that carry a `verb-*` POS tag:

```bash
python3 -c "
import json, glob
v = sum(1 for p in glob.glob('entries/*/*.json')
        if any(x in (json.load(open(p)).get('metadata') or {}).get('tags',{}).get('pos',[])
               for x in ['verb-godan','verb-ichidan','verb-suru','verb-kuru','verb-irregular']))
print('entries with a verb-* POS tag:', v)
"
```

## Step 2 — Build the pruner

Create `build/prune_nonverb_conjugations.py`. This is the one-shot pruner that
Tooling Backlog item 5 proposed; keep it in the repo as a reusable audit tool.
Review the implementation before running it, and **always dry-run first**.

```python
#!/usr/bin/env python3
"""
Prune spurious conjugation tables and stray verb_class tags from non-verb,
non-i-adjective entries.

An entry is "spurious" when metadata.tags.pos contains NONE of
verb-godan / verb-ichidan / verb-suru / verb-kuru / verb-irregular / adjective-i
yet the entry has a `conjugation` field and/or a `verb_class` tag.

By default, entries whose POS includes `expression` are NOT pruned — they are
printed for manual review (some are mis-tagged single verbs that should be
re-tagged rather than stripped). Pass --include-expressions to prune them too
once you have reviewed the list.

Usage:
    python3 build/prune_nonverb_conjugations.py                      # dry run
    python3 build/prune_nonverb_conjugations.py --apply              # prune non-expressions
    python3 build/prune_nonverb_conjugations.py --apply --include-expressions
"""
import json
import glob
import argparse
from datetime import datetime, timezone

VERB_POS = {'verb-godan', 'verb-ichidan', 'verb-suru', 'verb-kuru', 'verb-irregular'}
KEEP_POS = VERB_POS | {'adjective-i'}


def is_spurious(d: dict) -> bool:
    tags = (d.get('metadata') or {}).get('tags', {})
    pos = tags.get('pos', []) or []
    if any(p in KEEP_POS for p in pos):
        return False
    return bool(d.get('conjugation')) or bool(tags.get('verb_class'))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='write changes')
    ap.add_argument('--include-expressions', action='store_true',
                    help='also prune entries whose POS includes "expression"')
    args = ap.parse_args()

    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    pruned, review = 0, 0

    for path in sorted(glob.glob('entries/*/*.json')):
        with open(path, encoding='utf-8') as f:
            d = json.load(f)
        if not is_spurious(d):
            continue
        pos = (d.get('metadata') or {}).get('tags', {}).get('pos', []) or []
        ctype = (d.get('conjugation') or {}).get('type')

        if 'expression' in pos and not args.include_expressions:
            print(f"REVIEW (expression, skipped): {d['id']}  pos={'|'.join(pos)}  type={ctype}")
            review += 1
            continue

        print(f"{'PRUNE' if args.apply else 'WOULD PRUNE'}: {d['id']}  "
              f"pos={'|'.join(pos)}  type={ctype}")
        if args.apply:
            d.pop('conjugation', None)
            d['metadata']['tags'].pop('verb_class', None)
            d['metadata']['modified'] = now
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
                f.write('\n')
            pruned += 1

    print(f"\n{'Pruned' if args.apply else 'Would prune'}: {pruned}")
    if review:
        print(f"Expression entries needing review (not touched): {review}")


if __name__ == '__main__':
    main()
```

## Step 3 — Run the sweep

```bash
# 3a. Dry run. Read the full output. Confirm every listed entry really is a
#     non-verb (adverb / onomatopoeia / noun / na-adjective / auxiliary). The
#     12 named onomatopoeia (ぐつぐつ, ぱくぱく, …) and the four already-logged
#     adverb cases (00536_itsu, 00601_yoku, 00602_mou, 05173/05175) must appear.
python3 build/prune_nonverb_conjugations.py

# 3b. Review the "REVIEW (expression…)" list printed at the end. For each:
#       - multi-word idiom or compound-ている form  -> will be stripped in 3d
#       - actually a single mis-tagged verb         -> handle separately:
#           fix its pos to the correct verb-*, set verb_class, then
#           `python3 build/add_conjugations.py --force --start ID --end ID`
#     (Expect few or none of the latter. When unsure, leave it to be stripped
#      and log it under Entry Follow-ups.)

# 3c. Apply to the unambiguous non-verbs (everything except expressions):
python3 build/prune_nonverb_conjugations.py --apply

# 3d. After reviewing 3b, apply to the expression entries you've cleared:
python3 build/prune_nonverb_conjugations.py --apply --include-expressions
```

Do **not** renumber, move, or delete any entry file — you are only removing two
fields and bumping `modified`.

## Step 4 — Verify (decisive)

```bash
# (a) All entries still valid after field removal.
python3 build/validate.py

# (b) THE decisive check: re-running the retrofit must NOT re-add any table to a
#     stripped entry. With the guard in place this is a no-op for non-verbs.
python3 build/add_conjugations.py
python3 build/add_adjective_conjugations.py

# (c) The Priority-6 detector must now return 0 (or only expression entries you
#     deliberately chose to keep — ideally 0).
python3 -c "
import json, glob
n = 0
for p in sorted(glob.glob('entries/*/*.json')):
    d = json.load(open(p))
    pos = (d.get('metadata') or {}).get('tags', {}).get('pos', []) or []
    if d.get('conjugation') and not any(x in pos for x in ['verb-godan','verb-ichidan','verb-suru','verb-irregular','verb-kuru','adjective-i']):
        print(d['id'], pos); n += 1
print('REMAINING SPURIOUS:', n)
"

# (d) No non-verb should retain a stray verb_class tag either.
python3 -c "
import json, glob
n = 0
for p in sorted(glob.glob('entries/*/*.json')):
    d = json.load(open(p))
    t = (d.get('metadata') or {}).get('tags', {})
    pos = t.get('pos', []) or []
    if t.get('verb_class') and not any(x in pos for x in ['verb-godan','verb-ichidan','verb-suru','verb-irregular','verb-kuru']):
        print(d['id'], pos, t.get('verb_class')); n += 1
print('REMAINING STRAY verb_class:', n)
"
```

If (c) or (d) is non-zero for anything other than a consciously-kept expression,
investigate before proceeding.

## Step 5 — Log other conjugation problems you noticed

While sweeping you will pass entries with *different* conjugation defects. Do not
fix them here — record them in `planning/wiki/ideas/entry-followups.md` so a
future session can pick them up. Add a short section per item (entry ID, the
problem, a recommended fix), matching the existing format on that page. Watch for:

- **Verb with the wrong conjugation class** (e.g., an `-eru`/`-iru` verb tagged
  godan that is actually ichidan, or vice versa) — note it; do not regenerate.
- **Verb or i-adjective missing a table** because of a malformed headword
  (okurigana inside the furigana wrapper, e.g., `{若い|わかい}`) or a mis-tagged
  POS — note it (cross-link Tooling Backlog item 9 for the headword cases).
- **Compound-`ている` entries** (空いている, 混んでいる …) whose stripped table was
  bogus — when you strip one, note in Entry Follow-ups that its base verb carries
  the real conjugation, and add a `prominent_see_also`/cross-reference to that
  base verb if one is missing. `02617_kondeiru` is already logged; `02525_suiteiru`
  is a known sibling — confirm and log any others.
- **Polite-only / irregular verbs** (ございます-class) that need a custom table —
  note, don't attempt a template fix here.

Also append a one-line `[tooling]` or `[pattern]` note to
`polishing/observations.md` only if you find something genuinely new beyond what
this prompt already anticipates (the wiki updates in step 6 cover the known
patterns, so most sessions will add nothing here).

## Step 6 — Update the knowledge base

These edits are part of the task — the cleanup is not "done" until the wiki
reflects it. Markdown only; no rebuild needed for these files.

1. **`planning/wiki/ideas/entry-followups.md`** — bump "Last updated". For each of
   these sections, prepend a bold **Status (resolved YYYY-MM-DD):** line stating
   the conjugation field + stray `verb_class` were removed by the batch sweep and
   the guard now prevents regeneration:
   - "Twelve onomatopoeia entries — Strip spurious godan conjugations"
   - "00536_itsu — Spurious godan-tsu conjugation on an adverb"
   - "00601_yoku and 00602_mou — Spurious godan conjugations on adverbs"
   - "05173/05175 — Spurious verb_class and conjugation on mimetic adverbs"

   For **"02617_kondeiru"**, note that the sweep applied option (a) (table
   removed). Add new resolved sections for any sibling compound-`ている`
   expressions you stripped (e.g., `02525_suiteiru`). Leave the *non-spurious*
   items open (`00004_aogu`, `08261_totonoenaosu`, `01300_gozaimasu`,
   `01525_wakai`, `17582`/`08385`/`08016`) and add any new ones from step 5.

2. **`planning/wiki/ideas/cleanup-backlog.md`** — Priority 6: add a bold
   **RESOLVED (YYYY-MM-DD)** note: pruner `build/prune_nonverb_conjugations.py`
   built; N entries cleaned; defensive guard added to `add_conjugations.py`;
   detector now returns 0. Bump "Last updated".

3. **`planning/wiki/ideas/tooling-backlog.md`** — item 5: mark **RESOLVED** with
   the same details, plus the root-cause note (the `'verb' in 'adverb'` substring
   bug) and the fact that `add_adjective_conjugations.py` was already guarded.
   Bump "Last updated".

4. **`planning/wiki/topics/schema-tag-reliability.md`** — in "Runaway automation"
   → "Cleanup vs. defense in depth", add a short **resolved** note and the
   substring-bug root cause (it sharpens the lesson: the guard didn't just read a
   stale tag, it mis-parsed the POS itself). Bump "Last updated".

5. **`planning/wiki/index.md`** — refresh the top "Last updated" line to mention
   this session's cleanup.

6. **`planning/wiki/log.md`** — append a dated entry, e.g.:

   ```markdown
   ## [YYYY-MM-DD] maintenance | Spurious non-verb conjugation cleanup

   **Session type**: Manual one-time task

   **Activities**:
   - Added exact-enum verb-POS guard to build/add_conjugations.py (fixes the
     'verb' ∈ 'adverb' substring bug)
   - Built build/prune_nonverb_conjugations.py; pruned N non-verb entries
   - Resolved Cleanup Backlog P6, Tooling Backlog item 5, and five Entry
     Follow-ups sections; logged M new verb-conjugation follow-ups
   ```

7. **`PROJECT_STATUS.md`** — add a bullet to the Recent Changes section
   summarizing the cleanup (entries cleaned, guard added, pruner added). Keep the
   five-most-recent convention.

## Step 7 — Build, commit, PR, merge

Single-build rule: run `make build` exactly once, at the end.

```bash
make build      # validate + update_indexes + full static rebuild
```

Then stage everything (entry edits, the new + edited build scripts, `docs/`,
`entries_index.json`, `build/word_id_lookup.json`, `kanji/`, the wiki edits, and
`PROJECT_STATUS.md`), commit, and push to your session's feature branch:

```bash
git add -A
git commit -m "Strip spurious conjugations from non-verb entries; guard add_conjugations.py"
git push -u origin <your-branch>
```

**PR + merge — MCP path (Routine / unattended default; `gh` is not authorized).**
After `git push`, the tail is exactly: create PR → poll check-runs over MCP until
green → squash-merge, with nothing interleaved (full loop in `CLAUDE.md` → "MCP
path" step 5):

1. `mcp__github__create_pull_request` — `owner: "tkgally"`, `repo: "je-dict-1"`,
   `head: "<your branch>"`, `base: "main"`, with a clear title/body. Note the PR
   number.
2. Poll `mcp__github__pull_request_read` with `method: "get_check_runs"` (**not**
   `get_status`; `pipeline/wait-for-pr-checks.sh` 403s here). *green* =
   `total_count >= 1` and every run `completed` with `conclusion`
   `success`/`neutral`/`skipped`; *failed* = any other completed conclusion;
   *pending* = otherwise. While pending, wait with a backgrounded `sleep 30`
   (Bash `run_in_background: true`) and re-poll, up to ~16 times (~8 min).
3. On **green**: `mcp__github__merge_pull_request` with `merge_method: "squash"`.
   On **failed** or **still pending at the cap**: leave the PR open, add a
   one-line note to the wiki log / PROJECT_STATUS, and stop.

Do **not** call `mcp__github__enable_pr_auto_merge` from an unattended session,
and do **not** `git checkout main` or delete the feature branch from inside the
session — the repo's "Automatically delete head branches" setting handles remote
cleanup when the merge fires.

**Interactive curator session (only when `gh` is on PATH and authorized):** use
the `gh` path from CLAUDE.md instead — `gh pr create --repo tkgally/je-dict-1 …`
→ `gh pr checks <n> --repo tkgally/je-dict-1 --watch --fail-fast`
→ `gh pr merge <n> --repo tkgally/je-dict-1 --squash` → checkout-main cleanup.

## Useful commands

```bash
python3 build/get_timestamp.py                       # UTC timestamp for modified fields
python3 build/validate.py                            # schema validation
python3 build/validate.py --id <id>                  # single-entry validation
python3 build/add_conjugations.py --force --dry-run --stats   # prove the guard
python3 build/prune_nonverb_conjugations.py          # dry-run the sweep
make build                                           # end-of-session full build
```

## What "done" looks like

- `build/add_conjugations.py` has the exact-enum guard; re-running it (and
  `add_adjective_conjugations.py`) re-adds nothing to the stripped entries.
- The Priority-6 detector and the stray-`verb_class` detector both return 0
  (modulo any consciously-kept expression).
- `build/prune_nonverb_conjugations.py` exists and is committed.
- Entry Follow-ups, Cleanup Backlog P6, Tooling Backlog item 5, Schema Tag
  Reliability, the wiki index, and the wiki log all record the resolution; any
  newly noticed verb-conjugation defects are logged for future sessions.
- `make build` ran once; the PR contains source + rebuilt `docs/` and was merged
  green.
- This prompt file (`prompts/fix_spurious_conjugations.md`) can be deleted or
  archived afterward — it is a one-time task.
