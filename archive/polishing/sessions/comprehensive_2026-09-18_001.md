# Comprehensive polish — 2026-09-18 #001

Mode: `polish` (routine2.md). Selector reason: "polish: highest scheduler debt
among eligible modes."

## Priority lane

Started at `priority-cursor.txt` line 27484 (past the end of the 27479-entry
priority file — the previous run's fast skip-through had exhausted this pass).
Restarted from line 1 rather than regenerating (the file is only one day old).
Scanned lines 1–1736; almost all entries in that span had been modified within
the last 30 days (the usual pattern lately) and were skipped per the lane
rule. 16 entries not recently modified were opened and read in full:
01007_wa, 04935_katsuobushi, 03122_choushoku, 04930_nattou, 00047_fusai,
06916_ze, 04947_kirin, 00929_gochisousama, 00075_gurando, 02592_kabu,
01541_rajio, 01683_akushu, 03894_niji, 03898_makura, 04390_bara,
05921_kifuku. All were already correct and complete except one:

- **05921_kifuku** (起伏, suru-verb noun): missing the required
  `transitivity` tag. Added `"intransitive"` (起伏する takes no direct
  object — terrain or emotions undulate/fluctuate on their own). While
  editing, also renamed two non-canonical notes headers this touch exposed
  to the CI header gate: "PHYSICAL USAGE (terrain)" and "FIGURATIVE USAGE
  (emotions/events)" merged into one canonical `USAGE:` section (each bullet
  tagged physical/figurative inline instead), and "KEY PATTERN" renamed to
  `COMMON PATTERNS`.

New cursor: line 1737.

## Frontier lane

Sequential from `params.start_id` 07998. Read 16 entries: 07998_shikinguri,
07999_kokuhatsu, 08000_donka, 08001_daichou, 08002_bankou, 08003_senou,
08004_kesshutsu, 08005_juutou, 08006_keijou, 08007_benmei, 08008_bensai,
08009_shoukan, 08010_kokuso, 08011_kussaku, 08012_asatsuyu, 08013_seiyakusho.
These are a January-2026 batch of formal/business vocabulary, already in good
shape. Two fixes:

- **08007_benmei** (弁明) and **07640_shakumei** (釈明, opened as a neighbour
  via 08007's cross-reference and 08010's contrast note — both missing the
  same tag): missing `transitivity`. Added `"intransitive"` to both — neither
  word's examples show a direct-object (を) pattern for the suru-verb; both
  pattern with について or bare の, matching the already-correct
  `"intransitive"` tag on the near-synonym 07993_benkai. This looks like a
  systemic gap in the same January-2026 creation batch (08005–08013 mostly
  have transitivity set correctly, but a few in this batch and its
  cross-linked neighbours don't) — logged as a `[pattern]` observation below
  for a possible future systemic-fix pass over that batch.

New cursor: next: 08014.

## Candidates added

- 余剰金 (よじょうきん) "surplus funds" — seen in 08005_juutou, no entry.
- 設備投資 (せつびとうし) "capital investment, capital expenditure" — seen in
  08005_juutou, no entry.
- (新規事業, checked, already has an entry: 17985_shinkijigyou — the mechanical
  pass's auto_link run will link it in 08005's example 4.)

## Self-check (§4)

3 entries sent to the external reviewer (review_accuracy.py) and the link
reviewer (review_links.py): clean on both — 0 issues, 0 link flags. Cost
~$0.0015.

## Observations

- `[pattern]` The January-2026 batch of ~08000–08013 formal-vocabulary
  suru-verb entries (created 2026-01-24/25) has scattered missing
  `transitivity` tags — found 3 in this run (05921, 07640, 08007) among
  ~20 entries checked. Worth a `check_missing_transitivity.py`-style sweep
  restricted to entries with `created` in that date range, rather than
  waiting for the polish frontier to hit each one individually.

## Cursors

- `polishing/tasks/comprehensive/priority-cursor.txt` → `line: 1737`
- `polishing/tasks/comprehensive/progress.txt` → `next: 08014`

## Entries changed

3: 05921, 07640, 08007.
