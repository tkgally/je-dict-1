# je-dict-1 — Japanese-English Learner's Dictionary

A dictionary for intermediate learners of Japanese who can read kana and are building
vocabulary. Live site: https://www.tkgje.jp/, a static site built by GitHub Actions from the
entry JSON and served by GitHub Pages. About 30,600 entries as of September 2026. The
dictionary is in a maintenance phase: entries are polished, verified, and connected to each
other; new entries are added only to define words the dictionary already uses.

Full command catalog: `build/COMMANDS.md`. Current numbers: `PROJECT_CONTEXT_BRIEF.md`
(run `python3 pipeline/update-brief.py` at session start). Recent history:
`PROJECT_STATUS.md`. Design of the current process:
`enhancement/assessment-2026-09-02.md`.

## Project structure

```
entries/            Source entries, JSON, 500 per directory by ID (entries/07000/07061_toraburu.json)
build/              Python build, validation, detectors, mechanical passes, review tooling
  build/schema.json           Entry schema
  build/data/                 Closed vocabularies and baselines (note_headers.json, semantic_fields.json, …)
  build/templates/            Site CSS and JS
  build/tests/                Unit tests (unittest)
  build/archive/              Retired scripts
  build/COMMANDS.md           Every command, grouped by job
kanji/              Kanji index JSON (tracked; rebuilt by update_kanji_index.py)
entries_index.json  Master index (rebuilt by update_indexes.py)
build/word_id_lookup.json   Word → entry ID lookup (rebuilt by update_indexes.py)
docs/               Generated site. NOT tracked since 2026-09-02; built by .github/workflows/pages.yml
articles/           Expository articles (JSON)
pipeline/           Routine selector (routine_next.py), config, metrics, ledgers
prompts/            Task prompts; prompts/routine2.md is the scheduled Routine
planning/wiki/      Knowledge base (research library + backlog); planning/maintain-knowledge-base.md
polishing/          Cursors (tasks/), priority lists (priority/), session logs (sessions/), observations.md
reviews/            decisions.jsonl (adjudications), accuracy_flags.jsonl, screening/screening_status.json,
                    queue.txt, needs_curator.txt. Per-entry review files are local artifacts (gitignored).
candidate_words.json  Words queued for entry creation (internal-closure queue)
.claude/skills/     Detailed guidelines (entry-guidelines, verb-entry, vocabulary-notes, inline-word-links, …)
.github/workflows/  validate.yml (PR gates + tests), pages.yml (site build + deploy), review-queue.yml, update-brief.yml
```

## Entry rules

- Path `entries/{range}/{id}_{romaji}.json`; range = ID rounded down to 500. Use
  `python3 build/get_entry_path.py <id> <romaji>`.
- **IDs are live URLs: never renumber, rename, or reuse an ID.** Get a fresh ID with
  `python3 build/get_next_id.py` immediately before each new entry.
- Romaji in IDs is the full reading with no internal underscores (`ketteisuru`, `kaowodasu`).
- POS tags are hyphenated (`verb-suru`, `adjective-na`); semantic tags come from the closed list in
  `build/validate_tags.py`; notes section headers come from `build/data/note_headers.json`.
- All kanji carry furigana `{漢字|かんじ}` in headword, examples, and notes. Readings are hiragana.
- Explanations are English; Japanese appears only in examples, collocations, patterns.
- Every verb and i-adjective entry carries a `conjugation` table
  (`python3 build/add_conjugations.py`, `python3 build/add_adjective_conjugations.py`).
- Every entry carries `formality`, `politeness`, and (verbs) `transitivity`; CI enforces this on
  changed entries.
- New entries: general tier, `"schema_version": "2.0"`, duplicate-checked first.
- Basic (801) and core (1,982) tiers are closed: do not add to them or modify their headwords.
- **Inline links are placed by `build/auto_link.py`**, never by hand except for a kana homophone the
  sentence makes certain. **Cross-references named in notes are harvested by
  `build/harvest_crossrefs.py`.** Never write `noentry` markers; add the missing word as a
  candidate with `manage_candidates.py add "語" "ご" "gloss; seen in entry NNNNN"`.
- Notes ceiling: 1,200 characters single-sense, 2,000 multi-sense. Trim before adding.

## The Routine

`prompts/routine2.md` is the one scheduled task (twice a day). Each run: pre-flight rescue and
sweep → `python3 pipeline/routine_next.py` picks a mode → the mode's prompt → mechanical pass on
changed entries → independent-model self-check → metrics snapshot → `make index` → commit → PR →
CI → squash-merge. Modes and weights (`pipeline/routine-config.json`): polish 0.30,
accuracy-review 0.30, systemic-fix 0.25, new-entries 0.10, candidates 0.05 (self-suppressing),
wiki (trigger-only). Mode prompts: `comprehensive_polish.md`, `newentries.md`,
`newcandidates.md`, `planning/maintain-knowledge-base.md`; the accuracy-review and systemic-fix
playbooks are inside `routine2.md`.

## Sessions: start, work, finish

**Start**: `python3 pipeline/update-brief.py`, then read `PROJECT_CONTEXT_BRIEF.md`. Load the
skill for the entry type you touch.

**After changing entries**, in this order:

```bash
python3 build/normalize_notes.py --ids <ids> --apply
python3 build/auto_link.py --ids <ids> --apply
python3 build/harvest_crossrefs.py --ids <ids> --apply
python3 build/validate.py --id <id>            # each changed entry
python3 build/review_accuracy.py --ids <ids> --budget 0.40   # independent check (needs OPENROUTER_API_KEY)
```

Adjudicate every surviving flag (apply / reject / flag to `reviews/needs_curator.txt`) and log each
decision to `reviews/decisions.jsonl`.

**Finish**: `make index` (validation, `entries_index.json`, `build/word_id_lookup.json`, `kanji/`).
Do not run `make build` and do not commit `docs/`: the site is built and deployed by GitHub
Actions when the PR merges. Commit everything else with `git add -A`, push, open the PR, wait for
CI, squash-merge.

## PR, CI, and merge workflow

PR titles and bodies are reports to Tom: plain, self-contained English per the `clear-reports`
skill. Keep the `routine(<mode>):` prefix on Routine PRs (the sweep parses it).

**MCP path (Routines and any session without `gh`).** Direct GitHub REST returns 403 here; only
the GitHub MCP tools reach GitHub.

1. `mcp__github__create_pull_request` (`owner: "tkgally"`, `repo: "je-dict-1"`, `head: <branch>`,
   `base: "main"`, title, body). Note the PR number.
2. Poll `mcp__github__pull_request_read` with `method: "get_check_runs"` (never `get_status`,
   which is blind to Actions checks). Green = `total_count >= 1` and every run `completed` with
   conclusion `success`, `neutral`, or `skipped`; failed = any other completed conclusion; pending
   = otherwise. While pending, `sleep 30` via Bash with `run_in_background: true`, then re-poll; at
   most 16 polls.
3. Green → `mcp__github__merge_pull_request` with `merge_method: "squash"`. Failed → leave the PR
   open, note the failed check in the session log, stop. Pending at the cap → leave it open; the
   next Routine run's pre-flight rescues it.
4. Do not `enable_pr_auto_merge`, do not `git checkout main`, do not delete the branch (the repo
   deletes merged head branches automatically).

**`gh` path (interactive sessions with `gh` authorized).** Always pass `--repo tkgally/je-dict-1`:
`gh pr create --head <branch> --base main --title … --body …` → `gh pr checks <n> --watch
--fail-fast` (no hand-rolled polling loops) → `gh pr merge <n> --squash` → then `git checkout main
&& git pull origin main`, `git branch -d <branch>`.

**Sweep stranded PRs via MCP** (Routine pre-flight). For each open PR whose head starts with
`claude/`: if its title starts with `routine` and its check runs are all green, it is mergeable,
and no human commented, merge it (squash). Otherwise, `mcp__github__pull_request_read` with
`method: "get_files"`; if it touches entry files and the highest entry ID among them is below the
`next:` value in `polishing/tasks/comprehensive/progress.txt`, comment
(`mcp__github__add_issue_comment`) and close it (`mcp__github__update_pull_request`,
`state: "closed"`). Leave anything else open.

**Sweep orphan `claude/*` branches via MCP.** `mcp__github__list_branches`; for each `claude/*`
branch that is neither this session's branch nor an open PR's head: fetch it, diff its durable
files against `origin/main` (ignore generated files: `entries_index.json`,
`build/word_id_lookup.json`, `kanji/`, `pipeline/routine-state.json`, ledgers, metrics). No
residue → append `<UTC> prune-branch <branch> — absorbed` to `reviews/needs_curator.txt` (MCP
cannot delete branches). Residue and never had a PR and merges cleanly → open a PR for it. Anything
else → one line in `reviews/needs_curator.txt` saying why no action was taken.

## Parallel work

Two sessions may work non-overlapping 500-entry blocks on separate branches; only one session
runs `make index`. Never two sessions on the same entry file; never two new-entries sessions at
once (both modify `candidate_words.json`). Advisory locks: `python3 build/entry_lock.py`.

## Skills

`entry-guidelines` (start here), `verb-entry`, `verb-conjugations`, `adjective-entry`,
`particle-entry`, `other-entries`, `example-sentences`, `vocabulary-notes` (canonical headers),
`cross-reference-entry`, `inline-word-links`, `find-candidates`, `vocabulary-tiers`,
`kanji-index`, `revise-entries`, `polish-entries`, `consolidate-entries`, `delete-entry`,
`resolve-duplicates`, `clear-reports` (every PR body and end-of-run summary).
