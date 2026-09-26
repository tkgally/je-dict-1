# Comprehensive polish — 2026-09-20 (routine)

Mode: `polish` (routine2.md selector; reason: "polish: highest scheduler debt among eligible modes").

## Priority lane (16 entries, cursor lines 1488–21389 of `polishing/priority/notes.txt`)

Scanning from line 1488 took 19,902 lines to find 16 entries not modified in the last 30 days
(see `[tooling]` observation below — most of the priority list is currently stale against the
30-day skip filter).

Entries read: 04390_bara, 02235_namida, 00412_uisukii, 04981_sekken, 02713_geki, 05127_susuru,
04926_panko, 05459_ryouiki, 00109_hobo, 04731_gorufu, 05262_zukizuki, 05375_meramera,
06920_teiuka, 02208_koi, 04855_shousou, 05168_urouro.

- **00109_hobo (ほぼ)**: removed a `style: [written]` tag that directly contradicted the entry's
  own notes ("Register: Neutral. Common in both spoken and written Japanese."). ほぼ is used
  naturally in speech; the tag was wrong.
- **05459_ryouiki (領域)**: added `abstract` to the semantic tags. The entry was tagged only
  `geography`, but its primary sense (domain/field of expertise) is abstract, not geographic;
  sense 2 (territory) is the geographic one.
- The other 14 entries were already correct, complete, and within the notes-length ceiling; no
  changes needed.

## Frontier lane (16 entries, IDs 08060–08075)

All 16 entries (08060_fumeiryou through 08075_tsuidegai) were already in good shape — correct
glosses, furigana, tags, transitivity/verb_class where applicable, and useful notes sections. No
content edits needed. While reading, three words named in notes but lacking their own entries
were logged as candidates:

- 希望退職 (きぼうたいしょく, "voluntary retirement") — seen in 08070_soukitaishoku
- やけ酒 (やけざけ, "drinking out of frustration") — seen in 08073_yakegui
- 見がい (みがい, "worth seeing") — seen in 08074_yomigai

## Mechanical pass and self-check

`normalize_notes.py`, `auto_link.py`, `harvest_crossrefs.py` ran on the two changed IDs (00109,
05459); nothing to change (headers already canonical, no unlinked in-vocabulary tokens, existing
cross-references already covered the SIMILAR WORDS bullets). `validate.py` passed on both.

`review_accuracy.py --ids 00109,05459 --budget 0.40`: 0 issues on both entries.
`review_links.py --ids 00109,05459 --skip-decided --budget 0.10`: 12 links judged, 0 flagged.

Self-check outcome: clean — nothing further to fix.

## Observations logged

- `[tooling]` 2026-09-20: third consecutive run where the priority-lane 30-day skip filter forced
  a very long scan (19,902/27,481 lines for 16 usable entries) even against a freshly regenerated
  priority file. Suggested shortening the skip window or excluding recently-modified entries from
  `prioritize_polishing.py`'s scoring.

## Candidates added

3 (see frontier lane above).

## Cursors

- `polishing/tasks/comprehensive/priority-cursor.txt`: line 1488 → 21390
- `polishing/tasks/comprehensive/progress.txt`: next 08060 → 08076

## Next

Priority lane continues at line 21390 of `polishing/priority/notes.txt`; frontier lane continues
at entry 08076.
