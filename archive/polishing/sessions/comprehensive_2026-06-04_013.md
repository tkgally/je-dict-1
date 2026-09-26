# Comprehensive Polish Session 013 — 2026-06-04

**Entry range processed:** 05121–05141 (21 entries)
**Next entry:** 05142

## Changes made

Added inline word links (⟦...⟧) to examples and notes for all 21 entries. Updated `modified` timestamps throughout.

**Entries processed:**
- 05121_wasabi — 5 examples, notes updated (from prior session)
- 05122_kanbatsu — 3 examples, notes updated (from prior session)
- 05123_ukiuki — 5 examples, notes updated (from prior session)
- 05124_shiwa — 5 examples, notes updated (from prior session); noted possible furigana error {笑|え}い{皺|じわ} in notes
- 05125_hokuro — 3 examples, notes updated (from prior session)
- 05126_kajiru — 6 examples, notes updated (from prior session)
- 05127_susuru — 3 examples, notes updated (from prior session); **fixed broken conjugation** (add_conjugations.py false positive: godan verb with reading ending in する was classified as suru type; manually wrote correct godan conjugation; changed verb_class to "godan-ru")
- 05128_museru — 3 examples, notes updated (from prior session)
- 05129_shakkuri — 5 examples, notes updated (from prior session)
- 05130_kuwagata — 3 examples, notes updated (from prior session)
- 05131_gokiburi — 3 examples, notes updated (from prior session)
- 05132_hacchuu — 3 examples, notes updated (from prior session)
- 05133_juchuu — 3 examples, notes updated (continued from prior session)
- 05134_nouhin — 3 examples, notes updated
- 05135_shukka — 3 examples, notes updated
- 05136_kanzei — 3 examples, notes updated
- 05137_butsuryuu — 5 examples, notes updated; **fixed furigana error** {会社|がいしゃ} → {会社|かいしゃ} (in ex4 and notes)
- 05138_ryuutsuu — 3 examples, notes updated
- 05139_fugoukaku — 3 examples, notes updated
- 05140_kyuugaku — 3 examples, notes updated
- 05141_ryuunen — 3 examples, notes updated

## Candidates added

- 件数 (けんすう) — number of cases/items/orders [from 05133 ex2]
- 記録的 (きろくてき) — record-breaking, unprecedented [from 05122]
- 日照り (にっしょうり) — drought, dry spell [from 05122]
- 皺寄せ (しわよせ) — burden shifted onto someone else [from 05124]

## Notable findings

- **Tooling bug (05127_susuru):** `add_conjugations.py` falsely detects readings ending in する as suru compounds. 啜る (godan-ru) was given malformed forms. Fixed manually. See observations.md.
- **Furigana error (05137_butsuryuu):** {会社|がいしゃ} in example and notes — corrected to {会社|かいしゃ}.
- **Possible furigana error (05124_shiwa):** {笑|え}い{皺|じわ} in notes — え for 笑 seems wrong (should be わら). Flagged in observations.md for furigana review.
- **Semantic tag issue (05134_nouhin):** Tagged "communication" — should be "action" for a delivery verb.
