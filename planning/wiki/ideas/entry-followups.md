# Entry Follow-ups

**Last updated**: 2026-05-11

Specific entries identified during comprehensive-polish sessions as needing work beyond what fits a single polishing pass. Each item includes the entry ID, the issue, and a recommended fix.

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

## 00565_toru sense 2 — Overlap with 00760_toru (撮る)

**Source**: Wiki maintenance 2026-05-11 entry exploration

Entry 00565_toru (取る) has sense 2 explicitly glossed "to take (a photo)" with three examples that all write the verb as 撮る (`{撮|と}る`), not 取る. Meanwhile 00760_toru exists as a dedicated entry for 撮る. The relationship is captured in `prominent_see_also` ({撮|と}る → 00760_toru, "take a photo"), but the duplicated sense and examples mean any future polish/revision will need to keep two locations synchronized.

This is a representative case of the polysemic kanji-variant overlap pattern documented in [Word Variants](../topics/word-variants.md) and surfaced for tooling in [Tooling Backlog](tooling-backlog.md) → item 7.

**Options**:
1. Demote sense 2 to a brief pointer ("for the 'take a photo' sense, see 撮る") and remove the sense's examples.
2. Keep the redundant sense but mark it explicitly as "covered also at 00760_toru" and accept that the two entries are kept in sync by hand.
3. Merge 00760_toru into 00565_toru and pivot 00760 into a redirect-only entry.

Option 1 is closest to existing project practice for kanji-variant near-synonyms; option 3 would conflict with the policy of keeping different kanji as separate entries documented in [Handling Homographs](../topics/homographs.md). Decision needed from the curator.

## Related pages

- [Cleanup Backlog](cleanup-backlog.md) — systemic patterns
- [Tooling Backlog](tooling-backlog.md) — tool improvements
- [Content Pipeline](../project/content-pipeline.md) — polishing workflow
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis covering several of these
