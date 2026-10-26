# ezFurigana lookup reports

[ezFurigana](https://www.ezfurigana.com/) adds furigana to Japanese texts that its users paste
in, and links the words in those texts to this dictionary's entries. Its owner does this with
Tom's permission (since mid-2026), and from time to time sends Tom a report of the words his
users met that the dictionary could not serve. The reports are a record of words real learners
looked up in real texts: a demand signal for new entries, not a word list to copy. Every row is
vetted one by one against the `find-candidates` gates before anything reaches
`candidate_words.json` (stream 3 of `prompts/newcandidates.md`).

## Files

- `received/<date>_<name>.tsv`: each report as received, unchanged. Columns: `surface`,
  `reading`, `category`, `tkgje_existing_spelling`, `lookups`, `first_seen_utc`,
  `last_seen_utc`. The categories are `not in TKGJE`, `TKGJE has another kanji spelling`,
  `TKGJE has kana form only`, `TKGJE has this word with another reading` and
  `grammar expression/particle`.
- `ledger.jsonl`: one verdict per (surface, reading): `added` (a candidate was queued; `word`
  and `word_reading` name it when it differs from the row, as when 入管法 led to 入管), `exists`
  (an inflected or partial form of an existing entry: 与え → 与える), `variant` (another
  spelling or reading of an existing entry: 身体 → 体), `queued` (already a candidate) or
  `rejected` (with the gate it failed). A decided row is never served again.

## Adding a new report

Either attach the TSV to a Claude session and ask for it to be processed, or upload it to
`external/ezfurigana/received/` through GitHub (any file name ending in `.tsv`; a date prefix
keeps them in order). The Routine notices rows without a verdict: the selector
(`pipeline/routine_next.py`) keeps the `candidates` mode eligible while any wait, and that mode
works them first. By hand:

```bash
python3 build/ezfurigana_lookups.py ingest <file.tsv>            # copy it into received/ with today's date
python3 build/ezfurigana_lookups.py pending --n 150 > /tmp/ez.json   # rows still to vet, most looked-up first
python3 build/manage_candidates.py add-batch /tmp/ez_cands.json  # the survivors
python3 build/ezfurigana_lookups.py record /tmp/ez_verdicts.json # every verdict, added or not
python3 build/ezfurigana_lookups.py stats                        # verdicts by category
python3 build/ezfurigana_lookups.py variants                     # rows that are forms of existing entries
```

Later reports may repeat earlier rows with higher counts; `pending` keeps the most recently
seen row for each surface and reading and skips those already decided. A rejected word that
keeps being looked up can be reconsidered with `pending --include-decided`.

The `variants` output (surface, reading, entry ID) lists the spellings and forms ezFurigana
could link to an existing entry; Tom may pass it on to ezFurigana's owner.

## History

- 2026-10-26: first report, 1,384 rows, 1,382 distinct (1,076 not in the dictionary, 122
  another kanji spelling, 91 kana only, 45 another reading, 48 grammar). 498 candidates queued,
  228 variants and 48 forms of existing entries, 7 already queued, 601 rejected (mostly personal
  and place names of little weight, bare affixes, transparent compounds, number + counter
  strings and specialized terms).
