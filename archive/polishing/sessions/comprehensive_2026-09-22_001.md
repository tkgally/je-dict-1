# Comprehensive polish — 2026-09-22 #001

Mode: `polish` (selector reason: "highest scheduler debt among eligible modes").

## Priority lane

`polishing/priority/notes.txt` (generated 2026-09-19) was scanned in full from
`priority-cursor.txt` line 1 (27,477 ranked lines). Only 11 entries had not been
modified in the last 30 days — the rest were already touched by the intervening
accuracy-review/systemic-fix sweeps. Reviewed all 11:

- 02871_kirai, 03423_datte, 04765_koushin, 00928_fun, 01007_wa, 02877_kesa,
  04959_dango, 00817_tanoshii, 03039_yottsu, 00502_de, 01471_denwa, 00991_soko,
  01286_kanojo, 02849_ookina, 02851_okaasan, 02927_nanoka were all modified in
  the last 30 days and skipped per the rule (see `[pattern]` observation below).
- 03122_choushoku, 00929_gochisousama, 01541_rajio, 03894_niji, 02235_namida,
  04855_shousou: reviewed, already high quality, no changes needed.
- 01683_akushu (握手): semantic tag `action` → `greeting` (a handshake is a
  greeting gesture, matching 15858_eshaku's precedent).
- 05127_susuru (啜る): semantic tag `action` → `consumption` (matching
  00396_taberu's precedent for eating/drinking verbs).

Cursor exhausted (scanned the whole file); advanced past the end. Needs
regeneration well before its 14-day staleness threshold — see observations.

## Frontier lane

Sequential from 08142 (progress.txt). Reviewed 08142–08161 (20 entries):

- 08142_kaatorijji: removed spurious `language` semantic tag.
- 08144_amime: semantic tags `["descriptive","general","creation"]` (both
  "descriptive" and "creation" are categories for a different part of speech)
  → `["general"]`.
- 08146_baromeetaa, 08147_rifu, 08148_arenji, 08149_kontorabasu: same spurious
  `language` tag as 08142, removed. All five are from the same creation batch
  (2026-01-25T06:0x) — see `[tooling]` observation.
- 08152_tereru (照れる, "to be shy"): found the entry's own conjugated stem 照れ
  wrongly inline-linked to 00404_teru (照る, "to shine") in 3 examples and 3
  notes bullets — a real, user-facing wrong link. Unlinked by hand. Discovered
  `auto_link.py`'s forms-map re-adds this exact mislink on every run and that
  the homophone/decision-ledger guard does not protect kanji-bearing surfaces,
  so the fix required excluding 08152 from the mechanical-pass `auto_link.py`
  call rather than relying on logged `unlink` decisions. See `[tooling]`
  observation — this needs a code fix, not just a content fix.
- 08154_kewashii: fixed a furigana/reading error in a notes bullet —
  「先行き」was marked `{先行|せんこう}き` (the reading of 先行 "precede", wrong)
  instead of `{先行|さきゆ}き` (先行き "outlook, prospects", さきゆき — matches the
  dedicated entry 27497_sakiyuki).
- 08161_mochikaeri: trimmed a tautological "KANJI READING: Also pronounced
  もちかえり" note section (restated the entry's own reading as if it were an
  alternative) and folded the one useful fact (持って帰る as the source phrase)
  into the existing RELATED WORDS list.
- 08143_tokushitsu, 08145_doukaku, 08150_saku, 08151_kau, 08153_toboshii,
  08155_demae, 08156_warikan, 08157_ogoru, 08158_ajimi, 08159_fukubukuro,
  08160_omake: reviewed, already high quality, no changes needed.

Cursor advanced to `next: 08162`.

## Mechanical pass, self-check, candidates

- `normalize_notes.py`, `auto_link.py` (excluding 08152 after its first pass
  went wrong — see above), `harvest_crossrefs.py`, `validate.py`: all clean on
  the 11 changed entries.
- `review_accuracy.py --budget 0.40`: 0 issues on all 11 entries.
- `review_links.py --budget 0.10`: 7 kana links judged, 0 flagged.
- No new candidates found this run (no bare cross-referenced words without
  entries encountered in the reviewed batch).
- Ledger: self-check spend $0.0054 (total today $1.0663 of $5.00 cap).

## Observations logged

Three `[tooling]`/`[pattern]` entries in `polishing/observations.md`:
1. The `auto_link.py` guard-bypass bug for kanji-bearing surfaces (照れ/照る
   collision), with a generalization warning (any Xる/Xれる pair is at risk).
2. The spurious `language` semantic tag batch-mistagging (349 entries carry
   the tag dictionary-wide; ~17 katakana-loanword entries look wrong, several
   more still ahead in the 08138-08149 range not yet reached this run).
3. The priority-notes.txt staleness (exhausted in 3 days by the pace of other
   Routine sweeps; the 14-day regeneration trigger is too loose).

## Next cursors

- `polishing/tasks/comprehensive/priority-cursor.txt`: `line: 27478` (exhausted;
  regenerate with `make priorities` before the next polish run's priority lane).
- `polishing/tasks/comprehensive/progress.txt`: `next: 08162`.
