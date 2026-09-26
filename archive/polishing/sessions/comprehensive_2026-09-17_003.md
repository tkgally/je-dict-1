# Comprehensive polish — 2026-09-17 (003)

Mode: `polish` (selector reason: highest scheduler debt among eligible modes).
Priority lane: `polishing/priority/notes.txt` from line 21. Frontier lane: `params.start_id` 07481.

## Priority lane

Screened priority lines 21–3066. Nearly every entry in that stretch had been
modified in the last 30 days (a broad prior touch, likely tag/metadata work)
and was skipped per the "skip entries modified in the last 30 days" rule.
Of the entries eligible for review, most were already solid; one genuine gap:

- **04513_benki** (便器, toilet bowl): `definitions[0].explanation` was a
  verbatim copy of the gloss. Rewrote it to explain the register (the fixture
  itself, used in cleaning/shopping/technical contexts, not casual
  conversation).

Read and left unchanged (already correct, no missing-required-field or
factual issue): 01007_wa, 04935_katsuobushi, 03122_choushoku, 04930_nattou,
00047_fusai, 06916_ze, 04947_kirin, 00929_gochisousama, 00075_gurando,
02592_kabu, 01541_rajio, 01683_akushu, 03894_niji, 03898_makura, 04390_bara,
05921_kifuku, 02235_namida.

## Frontier lane (07481–07981)

Read 07481–07485 in full per the checklist, then ran a programmatic screen
(missing `politeness`/`formality`, notes over the length ceiling, thin
duplicate explanations) across the rest of the range and opened every flagged
entry to verify before fixing. (Skipped `missing-transitivity`: that's
already an active systemic-fix item, `transitivity-review-queue`, moving
through the same range in the same series of runs — no need to duplicate it
by hand here.)

**Missing `politeness` tag** (schema requires it on every entry; these
predated the requirement) — added, with the value judged from the entry's
own examples and register:
- 07635_gouman (傲慢), 07636_hikutsu (卑屈), 07666_tsukaiwakeru (使い分ける),
  07672_misuborashii (みすぼらしい), 07700_hairyo (配慮), 07739_otoku (お得),
  07770_osomatsu (お粗末) → `plain`
- 07659_tamawaru (賜る) → `humble` (all three examples use it as the
  kenjougo "receive from a superior," matching もらう/いただく in its own
  cross-references)

**Notes over the length ceiling** (1,200 chars single-sense) — trimmed,
keeping the learner-relevant content (etymology, key collocations, the
contrast that matters) and cutting encyclopedic padding (brand names,
scandal trivia, redundant "USAGE" bullet lists repeating the domain tags):
07588_shukujitsu, 07890_kyuudan, 07891_funkyuu, 07892_tachiageru,
07908_hinan, 07930_kashigeru, 07936_mizumore, 07937_konpou, 07943_kaizan,
07944_mokunin, 07946_batteki, 07947_yuba, 07949_donabe, 07950_chakubarai.
All now under ceiling (660–1,041 chars). A few picked up a genuine addition
while trimming: 07936_mizumore got a WATCH OUT on who to contact for a leak
in a Japanese apartment; 07908_hinan got a WATCH OUT distinguishing itself
from the homophone 非難 (criticism).

## Self-check (google/gemini-2.5-flash, ~$0.011)

23 entries reviewed, 2 flagged:
- **07659_tamawaru**, gloss — confirmed. The entry's gloss included "to
  bestow (honorific)," but 賜る itself is kenjougo for *receiving*; the
  bestowing/giving sonkeigo sense belongs to the separate, archaic headword
  賜う (たまう), which the entry's own RELATED KEIGO note already names
  separately. Trimmed the gloss and explanation to the receiving sense only.
- **07930_kashigeru**, notes — rejected. The reviewer read the alternate
  reading {傾|かた}げる as a tautological restatement of the headword because
  the kanji surface (傾げる) is identical; かたげる is a real, if less
  common, reading of the same compound. Kept as written.

Link self-check (same model, ~$0.000) flagged one link: 07739_otoku's
example まとめて→02424_matomeru (まとめる). Verified: the target's sense 1
("to put together, to collect") is exactly the "buy in bulk" meaning in
context. Logged `keep`.

## Candidates / observations

None added this run — no undefined words surfaced in the entries touched.

## Cursors

- `polishing/tasks/comprehensive/progress.txt` → `next: 07982`
- `polishing/tasks/comprehensive/priority-cursor.txt` → `line: 3067`

## Entries changed

23: 04513, 07588, 07635, 07636, 07659, 07666, 07672, 07700, 07739, 07770,
07890, 07891, 07892, 07908, 07930, 07936, 07937, 07943, 07944, 07946, 07947,
07949, 07950.
