# Entry Follow-ups

**Last updated**: 2026-05-15

Specific entries identified during comprehensive-polish sessions as needing work beyond what fits a single polishing pass. Items below 00607 are likely to be addressed by the comprehensive-polish task as it advances. Each item includes the entry ID, the issue, and a recommended fix.

## 00004_aogu — Conflated verbs

**Source**: Comprehensive-polish 2026-05-08 session 001

Entry 00004_aogu (扇ぐ) conflates two distinct verbs:
- Sense 1: 扇ぐ (godan-gu, "to fan")
- Sense 2: 煽る/扇る (godan-ru, "to incite") — examples ex3, ex5, ex6 use the form 扇る with okurigana る, which is the wrong conjugation class for the godan-gu headword

Entry 07924_aoru already covers fan/incite/tailgate comprehensively.

**Recommended fix**: Remove sense 2 and its three examples from 00004_aogu; let 07924_aoru carry the incite meaning. A cross-reference between the two has already been added.

## 00007_auto — フライ missing baseball sense

**Source**: Comprehensive-polish 2026-05-08 session 002

The existing entry 11124_furai is glossed only as "deep-fried food." The baseball sense (fly ball) is missing. An example sentence in 00007_auto uses a `noentry` marker for this sense.

**Recommended fix**: Add sense 2 (baseball fly ball) to 11124_furai, since both senses share the katakana form フライ.

## 00040_fubuki — しかける suffix-verb sense undocumented

**Source**: Comprehensive-polish 2026-05-09 session 001

Example ex3 in 00040_fubuki references しかける (04243_shikakeru) for the auxiliary "almost did" sense (`{遭難|そうなん}しかけた`). Entry 04243 is glossed only as "to set up; to start; to challenge" — the suffix-verb sense ("almost ~", "be on the verge of ~ing") is distinct.

**Options**: Expand 04243 with an additional sense, or create a separate grammar-pattern entry for 〜しかける.

## 00051_ga — Particle structured fields need dedicated polish

**Source**: Comprehensive-polish 2026-05-09 session 002

Entry 00051_ga (が) received tier-1 notes linking but its structured fields (`predicates_requiring`, `particle_contrasts`, `fixed_patterns`, `common_mistakes`) contain dozens of bare Japanese phrase fragments. Same applies to 00079_ha (は). See [Cleanup Backlog](cleanup-backlog.md) → Priority 5 for the broader particle-polish proposal.

## 00084_haitatsu — Split-compound 宅配便

**Source**: Comprehensive-polish 2026-05-09 session 003

Had a split-compound issue: `{宅配|たくはい}{便|びん}` appeared as two adjacent furigana spans with no link, while 09534_takuhaibin (宅配便) exists. Fixed to use the compound as a single link target.

**Action needed**: Check if other entries mentioning 宅配便 have the same split. See [Tooling Backlog](tooling-backlog.md) → item 4 for the general split-compound detector proposal.

## 02008_ikuratemo & 02461_ikuratemo — Duplicate expression entries

**Source**: Wiki maintenance 2026-05-11 entry exploration

Both entries cover いくら〜ても ("no matter how much…"). They are linked via `prominent_see_also` but never merged. The two entries have overlapping examples (`いくら食べても太らない`, `いくら待っても来なかった`) and similar notes; differences are cosmetic. Two parallel sources of truth that will keep diverging on every polishing pass.

Additionally, 02008_ikuratemo carries `semantic: ["furniture"]` — a clearly stale auto-label. The expression has nothing to do with furniture.

**Recommended fix**: Merge into a single entry (likely keep 02008's lower ID; rewrite the notes to combine the best of both; transfer 02461's unique examples) and remove 02461. Follow the `consolidate-entries` skill. As part of the same edit, drop the `furniture` semantic tag and replace it with something appropriate (`grammatical` or `descriptive`).

See also: [Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Stale auto-labels" for the broader pattern.

## Twelve onomatopoeia entries — Strip spurious godan conjugations

**Source**: Wiki maintenance 2026-05-11 entry exploration

The following adverbial onomatopoeia entries have a full godan conjugation block with nonsense forms (e.g., ぐつぐつ → ぐつぐたない). They have `pos: ["adverb", "onomatopoeia"]` (no verb POS) and a stray `verb_class: "godan-tsu"` tag that triggered `add_conjugations.py` at some point.

| Entry ID | Headword |
|----------|----------|
| 05646_gyuugyuu | ぎゅうぎゅう |
| 05723_pakupaku | ぱくぱく |
| 05724_jabujabu | じゃぶじゃぶ |
| 05726_boubou | ぼうぼう |
| 06683_potsupotsu | ぽつぽつ |
| 08432_gotsugotsu | ごつごつ |
| 18531_gutsugutsu | ぐつぐつ |
| 21888_mukumuku | むくむく |
| 22356_gougou | ごうごう |
| 26081_pukupuku | ぷくぷく |
| 26864_buruburu | ぶるぶる |
| 27085_kotsukotsu | こつこつ |

**Recommended fix**: Remove the `conjugation` field and the `verb_class` tag from each. Best done as a single deterministic pass (see [Tooling Backlog](tooling-backlog.md) → item 5) rather than as separate polishing-session work. Then add a defensive guard in `add_conjugations.py` so this can't regenerate.

## 01525_wakai (若い) — Missing conjugation table due to malformed headword

**Source**: Wiki maintenance 2026-05-12 entry exploration

Basic-tier i-adjective 若い is currently on the live site **without** an i-adjective conjugation table. The cause is the headword `{若い|わかい}`: the okurigana い is inside the wrapper, so `add_adjective_conjugations.py` couldn't extract a clean stem and skipped the entry. The other 453 i-adjective entries have conjugation tables; only this one is missing because of the format issue.

**Recommended fix**: Change the headword from `{若い|わかい}` to `{若|わか}い`, then re-run `python3 build/add_adjective_conjugations.py --start 1525 --end 1525` to backfill the conjugation table. The same pattern applies to the other 21 entries listed in [Tooling Backlog](tooling-backlog.md) → item 9.

## 08261_totonoenaosu (整え直す) — Mis-tagged POS

**Source**: Wiki maintenance 2026-05-12 entry exploration

Entry 08261_totonoenaosu (整え直す) is tagged `pos: ["verb-ichidan"]` but its headword ends in す and it is in fact a godan-su verb (compound of 整える + 直す, where 直す is godan-su). The mis-tag prevents `add_conjugations.py` from generating a conjugation table: the script sees `verb-ichidan` but the form doesn't end in る, so it skips.

**Recommended fix**: Change `verb-ichidan` to `verb-godan` in the POS tag, set `verb_class: "godan-su"`, then run `add_conjugations.py` on just that entry.

A similar review may be needed for 17582_urazuke (裏付け), 08385_moushiokuri (申し送り), and 08016_sashiosae (差し押さえ) — these are tagged with verb POS but the headwords are noun (連用形) forms rather than verb citation forms, so the conjugation pipeline skips them. Either retag (drop the verb POS, keep noun) or replace the headword with the verb citation form.

## 00565_toru sense 2 — Overlap with 00760_toru (撮る)

**Source**: Wiki maintenance 2026-05-11 entry exploration

Entry 00565_toru (取る) has sense 2 explicitly glossed "to take (a photo)" with three examples that all write the verb as 撮る (`{撮|と}る`), not 取る. Meanwhile 00760_toru exists as a dedicated entry for 撮る. The relationship is captured in `prominent_see_also` ({撮|と}る → 00760_toru, "take a photo"), but the duplicated sense and examples mean any future polish/revision will need to keep two locations synchronized.

This is a representative case of the polysemic kanji-variant overlap pattern documented in [Word Variants](../topics/word-variants.md) and surfaced for tooling in [Tooling Backlog](tooling-backlog.md) → item 7.

**Options**:
1. Demote sense 2 to a brief pointer ("for the 'take a photo' sense, see 撮る") and remove the sense's examples.
2. Keep the redundant sense but mark it explicitly as "covered also at 00760_toru" and accept that the two entries are kept in sync by hand.
3. Merge 00760_toru into 00565_toru and pivot 00760 into a redirect-only entry.

Option 1 is closest to existing project practice for kanji-variant near-synonyms; option 3 would conflict with the policy of keeping different kanji as separate entries documented in [Handling Homographs](../topics/homographs.md). Decision needed from the curator.

## 03537_nou — Semantic tag "clothing" should be "body"

**Source**: Comprehensive-polish 2026-05-11 session 003

Entry 03537_nou ({脳|のう}, brain) has `semantic: ["clothing"]` — clearly wrong. The brain is a body part.

**Recommended fix**: Change `semantic: ["clothing"]` to `semantic: ["body"]`.

## 00536_itsu — Spurious godan-tsu conjugation on an adverb

**Source**: Comprehensive-polish 2026-05-11 session 006

Entry 00536_itsu ({何時|いつ}, when) has `part_of_speech: "adverb"` but carries a full godan-tsu conjugation block with nonsensical forms (`いちます`, `いたない`) and a stray `verb_class: "godan-tsu"` tag. This is another instance of the broader pattern documented in [Cleanup Backlog](cleanup-backlog.md) → Priority 6 (130 non-verb entries with spurious conjugations).

**Recommended fix**: Remove the `conjugation` field and the `verb_class` tag. Will be covered by the one-shot pruner proposed in [Tooling Backlog](tooling-backlog.md) → item 5.

## 00601_yoku and 00602_mou — Spurious godan conjugations on adverbs

**Source**: Comprehensive-polish 2026-05-12 session 001

Two more adverb entries carrying fabricated godan conjugation forms:
- 00601_yoku ({良|よ}く, well/often): forms like `よかない`, `よきます`
- 00602_mou ({もう}, already/soon): forms like `もわない`

Same pattern as 00536_itsu and the 130-entry set in [Cleanup Backlog](cleanup-backlog.md) → Priority 6.

**Recommended fix**: Same as 00536 — remove `conjugation` and `verb_class` tag. Will be covered by the one-shot pruner.

## 01026_hashi — Example sentence word order error

**Source**: Comprehensive-polish 2026-05-13 session 007

Example ex5 in 01026_hashi ({箸|はし}) has a word order error: `ご飯を箸の中に立てること` should be `ご飯の中に箸を立てること` — the subjects 箸 and ご飯 are swapped. The intended meaning is "sticking chopsticks upright in rice" (a funeral taboo), so 箸 should be the object being inserted and ご飯の中 should be the location.

**Recommended fix**: Swap the particles in ex5 so that 箸を is the direct object and ご飯の中に is the locative. Needs human review to confirm the exact phrasing.

## 01300_gozaimasu — Conjugation table uses wrong template

**Source**: Comprehensive-polish 2026-05-14 session 007

Entry 01300_gozaimasu (ございます) has a conjugation table generated using the regular godan/ichidan verb template. ございます is a polite-only verb (the polite form of ある/ござる) and doesn't follow standard conjugation patterns — it has no plain form, no te-form, no imperative in normal use. The current conjugation table likely contains inappropriate forms like a dictionary form or casual negative that learners would never use.

**Recommended fix**: Either (a) remove the conjugation table entirely and rely on the notes to explain the limited paradigm, or (b) create a custom conjugation template for polite-only verbs that lists only the forms actually used (ございます, ございません, ございました, ございませんでした). This is an edge case that `add_conjugations.py` doesn't handle.

## 01293_yogoreru — POS misclassification (godan → ichidan)

**Source**: Comprehensive-polish 2026-05-14 session 007

Entry 01293_yogoreru ({汚|よご}れる) was misclassified as `verb-godan` in its POS tag and `verb_class`; the originating polish session corrected it to `verb-ichidan` and regenerated conjugations. The note recommends spot-checking other entries near this range for similar misclassifications.

**Status**: Fixed in the originating session. No further action needed on this entry. Logged here to note the spot-check recommendation for nearby entries.

## Related pages

- [Cleanup Backlog](cleanup-backlog.md) — systemic patterns
- [Tooling Backlog](tooling-backlog.md) — tool improvements
- [Content Pipeline](../project/content-pipeline.md) — polishing workflow
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis covering several of these
