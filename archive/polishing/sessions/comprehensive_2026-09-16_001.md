# Comprehensive polish session — 2026-09-16 #001

Mode: `polish` (Routine v3, `pipeline/routine_next.py` reason: "polish: highest
scheduler debt among eligible modes").

## Priority lane (`polishing/priority/notes.txt`, cursor 1008 → 8914)

Scanned lines 1008–8913 of the priority list. Nearly the entire stretch was
skipped under the "modified in the last 30 days" rule: most entries in this
range were bulk-touched by mechanical passes on 2026-08-08/09/12/14/16 and
2026-06 (transitivity/tag backfills), so only 20 entries in that 7,906-line
span were eligible for review. Read all 20 in full:

00624_getsuyoubi, 00075_gurando, 02592_kabu, 01541_rajio, 01683_akushu,
03894_niji, 03898_makura, 04390_bara, 05921_kifuku, 00288_mokuji,
00239_kiyoi, 00795_man, 02235_namida, 00412_uisukii, 04981_sekken,
04939_sagi, 02713_geki, 05127_susuru, 04677_konro, 04926_panko.

Findings and fixes:
- **00795_man** (万, basic tier): example 3 had a hand-placed `⟦…→一千万人：noentry⟧`
  link marker, which the current process forbids. Removed the marker (plain
  furigana kept), added `一千万` (いっせんまん) as a candidate.
- **04939_sagi** (鷺): two `noentry` markers. `脚` (あし) turned out to be
  *stale* — entry `28733_ashi` already exists — so the marker was removed and
  `auto_link.py` relinked it correctly at wrap-up. `五位鷺` (ごいさぎ, night
  heron) is genuinely missing; marker replaced with plain text and the word
  added as a candidate.
- **04677_konro**: found a third `noentry` marker (消し忘れる, correctly
  marked as genuinely missing) with no matching candidate queued yet; added
  the candidate. Left the entry's marker alone (pre-existing, correct
  convention, not a defect — see below).
- The other 17 entries were already accurate, complete, and well-tagged; no
  changes needed.

Note for the curator: the dictionary has ~2,100 entries with `⟦…→…：noentry⟧`
markers dictionary-wide (this is the long-tracked, already-tooled Priority 35
item in `planning/wiki/ideas/cleanup-backlog.md`, not a new finding — this
run's fixes were incidental, found while reading these specific entries for
other reasons, not from a dedicated sweep).

## Frontier lane (`polishing/tasks/comprehensive/progress.txt`, 07405 → 07421)

Read entries 07405–07420 in full (格上, 格下, ちらちら, めきめき, ぴりぴり,
晴れ晴れ, しんどい, 錆びる, 軋む, 籠もる, 溜め込む, 染み付く, 引っ込む,
燻る, 方言, 訛り). All 16 were high quality — correct glosses, accurate
notes, complete conjugations, clean furigana, sensible tags and
cross-references. No defects found; no changes made.

## Self-check

`build/review_accuracy.py --ids 00795,04939 --budget 0.40`: 0 issues, ~$0.001.
`build/review_links.py --ids 00795,04939 --skip-decided --budget 0.10`: 3
links judged, 0 flagged.

## Totals

- Entries changed: 2 (00795_man, 04939_sagi)
- Entries reviewed with no change needed: 34
- Candidates added: 3 (一千万/いっせんまん, 五位鷺/ごいさぎ, 消し忘れる/けしわすれる)
- Self-check: clean
- Cursors: priority-cursor.txt → line 8914; progress.txt → next 07421
