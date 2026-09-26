---
name: polish-entries
description: Systematic review and improvement of dictionary entries. Use when starting a polishing session to review entries for accuracy, completeness, and consistency.
---

# Dictionary Polishing

This skill describes the polishing system used by je-dict-1. The **default ongoing task is comprehensive polish** (`prompts/comprehensive_polish.md`), which walks through entries one at a time and applies a tiered quality checklist. Several targeted polish prompts also exist for special-purpose sweeps.

When a polishing session starts, read this skill, then read the specific prompt file for the task being run.

## Comprehensive polish (default)

`prompts/comprehensive_polish.md` is the standing improvement task. Each session:

1. Reads `polishing/tasks/comprehensive/progress.txt` for the next entry ID.
2. Processes **20–30 entries** (target ~70% context use), applying a tiered checklist (tier 1 required-for-every-entry, tier 2 should-do judgment items, tier 3 nice-to-have polish).
3. For each entry, does the judgment work (correctness, the contrast or warning a learner needs, trimming, tags); inline links and notes-named cross-references are added by `build/auto_link.py` and `build/harvest_crossrefs.py` at wrap-up, never by hand
4. For each entry, checks **back-link symmetry on direct neighbors** — adds a back-link on the linked entry where appropriate, but does **not** recurse.
5. Logs words found in examples/notes that lack entries to `candidate_words.json` with "seen in entry XXXXX" notes (these become highest-priority candidates).
6. Logs systemic patterns and longer-horizon ideas to `polishing/observations.md`.
7. Writes a session log to `polishing/sessions/comprehensive_{YYYY-MM-DD}_{NNN}.md`.
8. Runs `make index`, commits, and creates a PR following the end-of-session workflow in `CLAUDE.md` (the site is built by GitHub Actions after the merge).

The comprehensive task subsumes the older targeted polish prompts (furigana, example sentences,
inline links, semantic labels, transitivity, aspect notes, short notes, cross-references,
cross-model review). Those prompts are retired and kept for reference in `archive/prompts/`;
inline links and cross-references named in notes are now placed by deterministic scripts
(`build/auto_link.py`, `build/harvest_crossrefs.py`).

## Progress files

Per-task progress is a minimal text file:

```
next: 12345
```

A `last_session:` line may also be present as a hint for resumption. The format is the same across all tasks (comprehensive and targeted).

## Session logs

After every session, write a markdown log:

```
polishing/sessions/{task}_{YYYY-MM-DD}_{NNN}.md
```

Where `{task}` matches the task type (`comprehensive`, `furigana-completeness`, etc.) and `NNN` is the next zero-padded sequence number for that task. The log records what was processed, what changed, candidates added, observations logged, and the next entry to process.

## Quality standards

When polishing entries, the same quality standards used during creation apply:

- All kanji have furigana in **all** fields including notes (`{漢字|かんじ}`)
- Readings are hiragana-only (long-vowel `ー` allowed)
- Romaji concatenates the full reading (`ketteisuru`, not `kettei_suru`)
- POS tags use the hyphenated names (`verb-suru`, `adjective-na`, etc.)
- All explanatory prose is in English; Japanese only appears in headwords, examples, collocations, and patterns
- Examples have valid `sense_numbers`
- See `entry-guidelines` skill for the full list, plus the type-specific skills (`verb-entry`, `adjective-entry`, `particle-entry`, `other-entries`)

## Per-entry timestamps (CRITICAL)

When you modify an entry, run `python3 build/get_timestamp.py` immediately before saving and write that exact timestamp to the `modified` field. **One entry, one timestamp** — do not reuse a timestamp across multiple entries.

## Cross-reference targets that don't exist

If a cross-reference points at an entry that doesn't exist yet, add the target word to candidates:

```bash
python3 build/manage_candidates.py add "headword" "reading" "brief gloss"
```

The script checks for duplicates and refuses if the word already exists.

## Polishing priority files (optional)

`build/prioritize_polishing.py` produces priority files in `polishing/priority/` (currently `cross_refs.txt`, `examples.txt`, `furigana.txt`, `notes.txt`) that order entries worst-first for the targeted polish tasks. The targeted polish prompts use these when present and fall back to sequential ID order. **Comprehensive polish does not use priority files** — it walks sequentially through the dictionary so coverage advances predictably.

## Long-term tracking

The comprehensive polish workflow logs higher-level observations to `polishing/observations.md` using tag conventions (`[pattern]`, `[wiki]`, `[article]`, `[tooling]`, `[skill]`, `[entry]`). The daily wiki-maintenance session (`planning/maintain-knowledge-base.md`) harvests this file.

## Parallel execution

The targeted polish prompts support parallel execution when given an explicit ID range — see the "Parallel Execution Mode" section in any of the `polish_*` prompts and the "Parallel Execution" section in `CLAUDE.md`. Comprehensive polish currently runs single-agent; entry-level claim coordination for parallel comprehensive polish is planned but not yet implemented.

## Important reminders

1. **One timestamp per entry** — run `get_timestamp.py` before saving each entry.
2. **Don't recurse on neighbors** in comprehensive polish — direct neighbors only, no further hops.
3. **Don't run `make index` mid-session** for parallel-mode runs; the coordinator handles it.
4. **Always write a session log** before stopping — even short sessions.
5. **End-of-session workflow** (build, commit including `docs/`, push, PR, CI watch, squash-merge, branch cleanup) is documented in `CLAUDE.md`. Follow it exactly.
