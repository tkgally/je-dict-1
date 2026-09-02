# Comprehensive Polish (the Routine's `polish` mode)

The default ongoing-improvement task for je-dict-1. Each run reads a batch of
entries and does the work only judgment can do: fix what is wrong, add the one
thing a learner needs, trim what is padding, and set the tags. Everything
mechanical (inline links, cross-references named in the notes, header and
bullet normalization) is done by scripts at wrap-up, so do not spend the
budget on it.

This prompt runs as `prompts/routine2.md`'s `polish` mode. Run standalone only
in an interactive session; the pre-flight, self-check, and merge steps are in
routine2.md and are not repeated here.

## Budget

- Target **25–40 entries** per run. Finish the content work by about 55 percent
  of the context window; the mechanical pass, self-check, indexes, and merge
  need the rest.
- Take stock every ten entries. Wrap up early if tool output is truncating.
- Open a neighbour only to add a back-link or to check a claim about it; do not
  polish the neighbour. Every neighbour you open goes into the self-check list.
- If an entry needs a rewrite bigger than a few minutes (wrong part of speech,
  conflated words, senses that belong to different entries), make the quick
  fixes, log it as `[entry]` in `polishing/observations.md`, and move on.

## Entry selection: two lanes

1. **Priority lane** (about half the budget). `polishing/priority/notes.txt`
   ranks entries by substantive need: never modified since creation, verbs
   without transitivity, notes that name words without cross-referencing them,
   missing register tags, unresolved reviewer flags, thin or bloated notes.
   Start at the line in `polishing/tasks/comprehensive/priority-cursor.txt`
   (create it with `line: 1` if missing); skip IDs with no file and entries
   modified in the last 30 days. If the priority file is older than 14 days,
   regenerate it at wrap-up with `make priorities` and reset the cursor to
   `line: 1`.
2. **Frontier lane** (the rest). Sequential from `params.start_id` (or the
   `next:` value in `polishing/tasks/comprehensive/progress.txt`); skip IDs
   with no file. At wrap-up set `next:` to the ID after the last one you read.

## Per-entry checklist

Read the whole entry first. Then, in this order:

### 1. Correctness (always)

- Headword, reading, romaji, and every gloss are right; the definitions match
  the examples; each example's English says what the Japanese says.
- Every factual, grammatical, and usage claim in the notes is true. This is
  where past errors were found (a reversed 内回り/外回り, "ものの attaches only to
  the past tense"). If you are not sure a claim is true, remove or soften it;
  do not leave a confident sentence you cannot vouch for.
- Furigana is present and correct on every kanji in headword, examples, and
  notes (`python3 build/verify_furigana.py <id>`).
- Tags reflect the word: `semantic` from the closed list in
  `build/validate_tags.py` (never leave a sole `general` when a concrete tag
  fits), `formality`, `politeness`, `transitivity` on every verb,
  `verb_class`. Never invent a tag.
- Cross-references and `prominent_see_also` point at the right entries with
  the right type (`cross-reference-entry` skill). Transitivity pairs and
  N/Nする pairs go in `prominent_see_also`, both directions.

### 2. What a learner needs (add only if missing)

Ask: what would an intermediate learner get wrong with this word? Add exactly
that, in the section where it belongs:

- the near-synonym or contrast that matters (SIMILAR WORDS), with the rule
  that separates them, not a list;
- the pitfall (WATCH OUT): a homophone trap, a false friend, a register
  mismatch, a collocation that does not transfer from English;
- for verbs: transitivity and pair (TRANSITIVITY) and, when non-obvious, what
  ている means with this verb (ASPECT (ている));
- for particles and grammar words: the distinct functions with a pattern each
  (FUNCTIONS, COMMON PATTERNS);
- collocations only if the entry has fewer than three (COMMON COLLOCATIONS).

Section headers must come from `build/data/note_headers.json` (the canonical
list is in the `vocabulary-notes` skill). Do not add a section the word does
not need.

### 3. Trim (always)

- Delete sentences that restate the gloss, repeat another section, or say
  nothing ("often used in literary contexts"). Delete a SIMILAR WORDS bullet
  that lists the entry itself.
- Notes ceiling: 1,200 characters for a single-sense entry, 2,000 for a
  multi-sense entry. A polish pass may not grow notes by more than 300
  characters unless it is adding a missing required section; if the entry is
  over the ceiling, cut before adding.
- Do not add a new sense unless the examples show a distinct meaning; do not
  split one meaning into two senses.
- Examples: at least 3 per sense (5 for basic and core), short to long, natural,
  each containing the headword. Replace a weak example rather than adding a
  fourth. New Japanese text gets furigana; do not hand-link it.

### 4. Timestamp

If you changed anything: `python3 build/get_timestamp.py` → `metadata.modified`.
Then `python3 build/validate.py --id <id>`.

## Capture as you go

- A word used in an example or note that has no entry: add it as a candidate
  with the source (`python3 build/manage_candidates.py add "語" "ご" "gloss; seen
  in entry NNNNN"`). Do not write `noentry` markers by hand.
- Systemic observations → `polishing/observations.md` with the usual tags
  (`[pattern] [wiki] [article] [tooling] [skill] [entry]`).

## Wrap-up (standalone runs; Routine runs follow routine2.md §3–§7)

1. Mechanical pass on the changed IDs: `normalize_notes.py`, `auto_link.py`,
   `harvest_crossrefs.py` with `--ids … --apply`, then `validate.py --id` for each.
2. Update both cursors.
3. Session log `polishing/sessions/comprehensive_{YYYY-MM-DD}_{NNN}.md`: range,
   one bullet per entry (what was wrong, what was added, what was cut),
   candidates added, observations, next cursor values.
4. `make index`, commit, push, PR, CI, merge (CLAUDE.md → "End-of-session PR
   and merge workflow"). The site builds itself after the merge.

## Useful commands

```bash
python3 build/verify_furigana.py <id>
python3 build/validate.py --id <id>
python3 build/check_duplicate.py "word" "reading"
python3 build/manage_candidates.py add "word" "reading" "gloss; seen in NNNNN"
python3 build/get_timestamp.py
python3 build/auto_link.py --ids <id,id> --apply
python3 build/harvest_crossrefs.py --ids <id,id> --apply
python3 build/normalize_notes.py --ids <id,id> --apply
```
