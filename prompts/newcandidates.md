# Candidate Restock (the Routine's `candidates` mode)

Restock `candidate_words.json` with words the dictionary already uses but has
never defined. Since 2026-09-02 the queue is an **internal-closure** queue:
its job is to close the dictionary on itself, so that a learner who clicks a
word in an example or a note lands on an entry. Growth for its own sake has
stopped; common vocabulary is saturated at 30,000 entries and the last
thematic sweeps found nothing new.

Runs as `prompts/routine2.md`'s `candidates` mode when the queue falls below
the restock threshold (100). `params.approx_new` is the target (30–60).

## Sources, in priority order

1. **Words marked as missing inside entries.** The detector lists every
   `noentry` marker whose word still has no entry, classified:
   ```bash
   python3 build/check_stale_noentry.py --json > /tmp/stale.json
   ```
   Take the `unresolved` class. Rank by `instances` (how many entries use the
   word). Skip: suffixes and prefixes standing alone (権, 化, 系, 製, 書),
   number-plus-counter strings (三冊, 五階), inflected or partial forms,
   proper nouns of no cultural weight, and anything that is a variant
   spelling of an existing entry (check with the duplicate probe below).
2. **Words the reviewer or a polish run noticed.** `polishing/observations.md`
   `[entry]` lines and session logs often name a word an example needs.
3. **Curated stream (at most ten per run).** Idioms, proverbs, and proper nouns
   that pass the `find-candidates` skill's richness gate. Rotate lenses; record
   which you used.

## Workflow

1. Load the `find-candidates` skill (gates G1–G7).
2. Build a proposal list of about 1.5× the target from the sources above.
3. **Probe first, then vet.** Run the duplicate check on the whole list before
   writing a single gloss; it is seconds and it tells you which sources are
   fertile:
   ```bash
   python3 build/check_duplicate.py --batch --skip-candidates 'word:reading' 'word:reading' …
   ```
   Drop every duplicate and every variant spelling the probe reports.
4. Vet each survivor against the gates: real, lemma-form, headword-worthy,
   correct hiragana reading, correct gloss, learner value. When in doubt, skip.
5. Write the survivors to a scratch JSON file outside the repo:
   ```json
   [{"word": "湯呑", "reading": "ゆのみ", "notes": "teacup (handleless); seen in entry 05612"}]
   ```
   The `notes` field MUST name the source: `seen in entry NNNNN` for source 1
   and 2, or the lens for source 3.
6. Batch-add with automatic duplicate checking:
   ```bash
   python3 build/manage_candidates.py add-batch <scratch-file>.json
   ```
7. Re-read `git diff candidate_words.json` once and remove any slip
   (`manage_candidates.py remove C12345`). One pass, no ping-pong.
8. Wrap up per routine2.md §5–§7 (standalone: update PROJECT_STATUS.md Recent
   Changes, `make index`, commit, push, PR, merge).

## Quality bar

- Real, stable, lemma-form headwords with correct readings and glosses; useful
  to intermediate learners; general tier.
- Not: bulk-extracted lists, uncertain words, conjugated or derived forms, free
  phrases, number+counter strings, ephemeral slang, vulgar or discriminatory
  terms, archaic or dialect items, hyper-specialized jargon.

## Report

At the end: proposed / added / rejected as duplicates; counts per source;
queue total; which sources still have depth.
