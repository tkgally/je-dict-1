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
articles/           Expository articles (JSON; ten as of 2026-09-09). See "Articles" below
audio/              Example audio, text only: config.json, manifest/ (recorded examples), needs_human.jsonl,
                    runs.jsonl, regression/ (163 known-answer clips), testset/. MP3s live in the audio repository
                    (tkgally/je-dict-audio-1, GitHub Pages), never here. See AUDIO_WORKFLOW.md
pipeline/           Routine selector (routine_next.py), config, metrics, ledgers
prompts/            Task prompts; prompts/routine2.md is the scheduled Routine
planning/wiki/      Knowledge base (research library + backlog); planning/maintain-knowledge-base.md
polishing/          Cursors (tasks/), priority lists (priority/), session logs (sessions/), observations.md
reviews/            decisions.jsonl (adjudications), accuracy_flags.jsonl, screening/screening_status.json,
                    queue.txt (appended by `make index`), needs_curator.txt. Per-entry review files are local
                    artifacts (gitignored).
candidate_words.json  Words queued for entry creation (internal-closure queue)
.claude/skills/     Detailed guidelines (entry-guidelines, verb-entry, vocabulary-notes, inline-word-links, …)
.github/workflows/  validate.yml (PR gates + tests), pages.yml (site build + deploy)
archive/            Retired prompts, plans, old session logs and sweep snapshots (nothing reads them; archive/README.md)
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
  sentence makes certain. A kana word can name the wrong lexeme even when its reading has one
  entry (そうして the conjunction vs. the て-form of そうする): `build/data/kana_link_homophones.json`
  tiers every such base (`unique` / `verify` / `block`), the linker never links a `block` base,
  and `reviews/link_decisions.jsonl` records per-occurrence `keep` / `unlink` verdicts, which the
  linker and the CI gate (`check_link_homophones.py --gate`) honour. A hand link to a `block` base
  needs a `keep` line. **Cross-references named in notes are harvested by
  `build/harvest_crossrefs.py`.** Never write `noentry` markers; add the missing word as a
  candidate with `manage_candidates.py add "語" "ご" "gloss; seen in entry NNNNN"`.
- Notes ceiling: 1,200 characters single-sense, 2,000 multi-sense. Trim before adding.

## Articles

`articles/*.json` are expository articles for learners (schema `build/article_schema.json`; ten as of
2026-09-09, listed on the site's Articles page). The body is markdown with the same furigana and
inline-link markup as entries, and the same rules apply: furigana on every kanji, English prose,
Japanese only in examples. `build/article_utils.py` reads and writes the files in the repository
layout. After writing or revising an article:

```bash
python3 build/link_articles.py --ids <id> --apply   # deterministic inline links (auto_link.py rules and guards)
python3 build/link_articles.py --ids <id> --list    # every link in the body; KANA marks kana-surface links to review
python3 build/link_articles.py --unlinked           # Japanese words left without a link
python3 build/validate_articles.py                  # schema, furigana, link targets, related entries (CI gate)
```

Hand-link what the linker leaves bare when the context makes it certain (a kana homophone such as
あげる, a verb stem the linker reads as a noun, a set phrase the tokenizer splits such as こちらこそ);
a word that has no entry gets an entry. The linker never touches an existing link; a string it must
never link goes in the article's optional `no_link` list. Articles link to one another with
`[text](other-id.html)`. `related_entries` is the curated list shown at the foot of the article and
on each listed entry's page; use the entry's own headword.

## The Routine

`prompts/routine2.md` is the one scheduled task (every three hours). Each run: pre-flight rescue and
sweep → `python3 pipeline/routine_next.py` picks a mode → the mode's prompt → mechanical pass on
changed entries → independent-model self-check → metrics snapshot → `make index` → commit → PR →
CI → squash-merge. Modes and weights (`pipeline/routine-config.json`): audio 0.25 (off until
`audio/config.json` enables production), polish 0.22, accuracy-review 0.22, systemic-fix 0.19,
new-entries 0.08, candidates 0.04 (self-suppressing), wiki (trigger-only). Mode prompts:
`audio.md`, `comprehensive_polish.md`, `newentries.md`, `newcandidates.md`,
`planning/maintain-knowledge-base.md`; the accuracy-review and systemic-fix playbooks are inside
`routine2.md`.

## Sessions: start, work, finish

**Start**: `python3 pipeline/update-brief.py`, then read `PROJECT_CONTEXT_BRIEF.md`. Load the
skill for the entry type you touch.

**After changing entries**, in this order:

```bash
make mechanical IDS=<ids>      # normalize_notes → auto_link → harvest_crossrefs → validate each
python3 build/review_accuracy.py --ids <ids> --budget 0.40   # independent check (needs OPENROUTER_API_KEY)
python3 build/review_links.py --ids <ids> --skip-decided --budget 0.10   # kana links checked in context (same key)
```

Adjudicate every surviving flag (apply / reject / flag to `reviews/needs_curator.txt`) and log each
decision to `reviews/decisions.jsonl`. A link flag is adjudicated with a `keep` or `unlink` line
in `reviews/link_decisions.jsonl`; `review_links.py --apply-decisions --ids <ids>` applies the
unlinks.

**Finish**: `make gate` (exactly the checks CI runs on a PR: unit tests, full validation, the
ratchet gates on changed entries; fix what it reports), then `make index` (`entries_index.json`,
`build/word_id_lookup.json`, `kanji/`, the examples' `has_audio` flags, this branch's changed entries in
`reviews/queue.txt`, and `PROJECT_CONTEXT_BRIEF.md`). Do not run `make build` and do not commit `docs/`: the site
is built and deployed by GitHub Actions when the PR merges. Commit everything else with
`git add -A`, push, open the PR, wait for CI, squash-merge. Push nothing more after opening the
PR: each push starts a new CI run.

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
   = otherwise. While pending, wait in the foreground with `python3 pipeline/wait.py 60` via
   Bash, then re-poll; at most 15 polls (the check takes five to seven minutes). Never a
   backgrounded `sleep`: it returns immediately, so the loop finishes long before CI does.
3. Green → `mcp__github__merge_pull_request` with `merge_method: "squash"`. Failed → read the
   failing step's log (`mcp__github__get_job_logs`, `failed_only: true`), fix, `make gate`, push
   once more and re-poll; if it fails again leave the PR open and report it (the next Routine
   run's pre-flight absorbs it). Pending at the cap → leave it open; the next Routine run's
   pre-flight rescues it.
4. Do not `enable_pr_auto_merge`, do not `git checkout main`, do not delete the branch (the repo
   deletes merged head branches automatically).

**`gh` path (interactive sessions with `gh` authorized).** Always pass `--repo tkgally/je-dict-1`:
`gh pr create --head <branch> --base main --title … --body …` → `gh pr checks <n> --watch
--fail-fast` (no hand-rolled polling loops) → `gh pr merge <n> --squash` → then `git checkout main
&& git pull origin main`, `git branch -d <branch>`.

**Sweep stranded PRs via MCP** (Routine pre-flight). For each open PR whose head starts with
`claude/` and whose title starts with `routine`: check runs all green, mergeable, no human comment
→ merge it (squash). Check run still pending → leave it (the next run rescues it). Check run
failed → take its content over into this session's branch with
`python3 pipeline/absorb_branch.py <head-branch> --pr <number>` (per-file merge policy: entries
and code merge normally, generated files and cursors keep main's version, ledgers take the union,
a colliding session log is renamed, the candidate queue is reconciled; an entry or code conflict
aborts the merge and names the files), run `make gate`, fix what it reports, and after this
session's own PR merges comment "absorbed into PR #N" on the old PR and close it. An aborted
absorb gets one line in `reviews/needs_curator.txt` and the PR stays open. Never close a routine
PR because the polishing frontier has moved past its entries; that rule lost a run's work on
2026-09-14.

**Sweep orphan `claude/*` branches via MCP.** `mcp__github__list_branches`; for each `claude/*`
branch that is neither this session's branch nor an open PR's head:
`python3 pipeline/absorb_branch.py --residue <branch>`. No residue → append
`<UTC> prune-branch <branch> — absorbed` to `reviews/needs_curator.txt` unless a line naming the
branch is already there (MCP cannot delete branches). Residue → absorb it as above, unless a person
closed its PR (find it with `mcp__github__list_pull_requests`, `state: "closed"`,
`head: "tkgally:<branch>"`; a closing comment that is not Claude-signed means a person decided):
then one line in `reviews/needs_curator.txt` and no action.

## Example audio

Examples get recorded MP3 readings (Gemini TTS, four AI checkers, `AUDIO_WORKFLOW.md`). A recording
is valid only while the example's text and furigana are unchanged (text hash in
`audio/manifest/`); the site then shows a play button, otherwise browser speech. Editing an example
is always fine: the audio mode re-records stale examples first. Never commit an MP3 to je-dict-1
(`build/check_no_binaries.py` is a CI gate). Any change to the TTS model, prompt, checkers or
acceptance rule needs `python3 build/audio_regression.py` and a changelog entry in
`AUDIO_WORKFLOW.md` first.

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
