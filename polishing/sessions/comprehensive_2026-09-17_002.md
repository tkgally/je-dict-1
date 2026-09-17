# Comprehensive Polish — 2026-09-17 (Routine, session 002)

Mode: `polish`, selected by `pipeline/routine_next.py` (reason: highest scheduler
debt among eligible modes). Priority lane: `polishing/priority/notes.txt`
lines 1-20 (freshly regenerated today). Frontier lane: 07466-07480.

## Priority lane (16 entries read, 9 changed)

- `00928_fun`: rule for ふん/ぷん pronunciation already correct (fixed in a
  prior session); decision logged to clear the outstanding accuracy flag.
- `01471_denwa`: notes wrongly claimed 電話をかける is "more formal" than
  電話する — softened to say both are common, neither markedly more formal.
- `02871_kirai`: semantic tag already includes "emotion" (fixed prior
  session); no change needed.
- `00820_tsuyoi`: top-level gloss was "strong" only, missing the resilient/
  resistant sense covered by definitions and half the examples — widened to
  "strong, resilient".
- `02980_yaru`: accuracy flag questioned the "informal" formality tag;
  rejected — notes explicitly document sense 1 as informal, and that's
  accurate.
- `03968_mai`: formality tag was "formal", directly contradicting its own
  `domain: ["colloquial"]` tag — changed to "neutral".
- `00768_abunai`: ex9 translation "The test was close, but I somehow passed"
  was ambiguous (could mean a narrow pass); changed to "I almost failed the
  test, but I somehow passed."
- `02974_muttsu`, `02979_yattsu`: semantic tags already fixed to "number"
  (prior session); flags cleared.
- `01990_keredo`: accuracy flag claimed the けれど/けれども formality order
  was reversed; rejected — the entry's けど＜けれど＜けれども ordering is
  standard.
- `00914_aida`: semantic tag was a bare "general" for a word centrally about
  time; changed to "time-general".
- `02473_he`: notes said "へ cannot replace に for recipients" then examples
  6-9 use へ for addressees — clarified that the "recipients" rule is about
  indirect objects of giving/receiving verbs, distinct from the addressee
  use in letters/messages. Also removed a hand-placed `noentry` link marker
  on 田中様 (policy violation, pre-existing) and fixed a garbled
  cross-reference label on 三時 that read "✓ —, not (✗)".
- `03094_toki`: semantic tag "general" → "time-general".
- `03423_datte`: ex7 translation "I eat anything" narrowed per flag to
  "I'll eat anything" to better match the generic/volitional nuance.
- `00240_ko`: semantic tag already fixed to "size" (prior session); a
  `warn`-severity translation nit on ex3 rejected as consistent with the
  dictionary's bare dictionary-form example convention.
- `00736_ni`: notes-fact flag about the ふたり reading was a reviewer
  misreading of an ambiguous bullet ("二人 / 二人" displays identically
  without furigana); reworded so both readings are labeled distinctly. Also
  removed three hand-placed `noentry` markers (二度, 言, 者, 択) — two of the
  three words already have entries (二度と → 06482_nidoto, 二者択一 →
  10045_nishatakuitsu, now auto-linked); added 二言目には as new candidate
  C23487 (no entry exists).

## Frontier lane (15 entries read, 1 changed)

07466-07480: all well-formed. Five entries (07472-07476, the giri/kiri
cutting-style words) had outstanding `culinary-technique` off-vocab tag
flags already migrated to `cooking` in a prior session; decisions logged to
clear them. `07470_soshina` semantic tag was a bare "general" alongside
`domain: ["business"]` — changed semantic to "business" too.

## Self-check

`review_accuracy.py` on the 10 changed entries: 6 flagged. Adjudicated:
1 applied (00736_ni's ambiguous ににん/ふたり bullet reworded for clarity),
5 rejected as reviewer misreadings (00768 translation truncation would drop
real content; 00914's kan/ma readings were already correctly labeled; 01471
denwasuru genuinely takes no を-object; 03094's dictionary-form/た-form
contrast is standard grammar; 07470's formal+polite tags aren't
contradictory). `review_links.py` on the same 10: 29 links judged, 0
flagged.

## Candidates added

- 二言目には (ふたことめには) — "at every opportunity"; seen in entry 00736.

## Checks

`make gate`: see PR. `make index` run once at wrap-up.

## Cursors

- `polishing/tasks/comprehensive/priority-cursor.txt`: line 21
- `polishing/tasks/comprehensive/progress.txt`: next: 07481
