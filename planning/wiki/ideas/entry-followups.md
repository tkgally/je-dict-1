# Entry Follow-ups

**Last updated**: 2026-07-27 (added **03794_warukuchi / 12672_waruguchi 悪口** — the same word split across two standard readings (わるくち / わるぐち), a variant-reading consolidation rather than a delete, needing a curator call on which reading leads the headword; and **08169_chuubi / 17946_nakabi 中火** — one of the two is simply wrong: 中火 is read ちゅうび, and なかび is the reading of 中日, so 17946 is either a mis-created duplicate or an entry that was meant to be 中日 and got the wrong kanji, notable because a 2026-07-20 furigana screen flagged its reading and the run *correctly* rejected the flag as an alternate reading — the real defect was invisible from inside the entry.) Prior 2026-07-26

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

**Status (resolved 2026-06-08):** The spurious `conjugation` field and stray `verb_class` tag were removed from all twelve by the one-time non-verb conjugation sweep (`build/prune_nonverb_conjugations.py`; 133 entries cleaned in total). Eleven were stripped by this sweep; 05646_gyuugyuu had already been cleaned by the 2026-06-07 comprehensive-polish session. The exact-enum verb-POS guard now in `build/add_conjugations.py` prevents regeneration (the old guard's `'verb' in p` substring test matched "adverb"). See [Cleanup Backlog](cleanup-backlog.md) → Priority 6 and [Tooling Backlog](tooling-backlog.md) → item 5.

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

**Status (resolved 2026-06-08):** The `conjugation` field and stray `verb_class` tag were removed by the one-time non-verb conjugation sweep, and the new exact-enum verb-POS guard in `add_conjugations.py` prevents regeneration.

**Source**: Comprehensive-polish 2026-05-11 session 006

Entry 00536_itsu ({何時|いつ}, when) has `part_of_speech: "adverb"` but carries a full godan-tsu conjugation block with nonsensical forms (`いちます`, `いたない`) and a stray `verb_class: "godan-tsu"` tag. This is another instance of the broader pattern documented in [Cleanup Backlog](cleanup-backlog.md) → Priority 6 (130 non-verb entries with spurious conjugations).

**Recommended fix**: Remove the `conjugation` field and the `verb_class` tag. Will be covered by the one-shot pruner proposed in [Tooling Backlog](tooling-backlog.md) → item 5.

## 00601_yoku and 00602_mou — Spurious godan conjugations on adverbs

**Status (resolved 2026-06-08):** The `conjugation` field and stray `verb_class` tag were removed from both by the one-time non-verb conjugation sweep, and the new exact-enum verb-POS guard in `add_conjugations.py` prevents regeneration.

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

## 01495_hatsumei — Unicode replacement character in cross-reference headword

**Source**: Comprehensive-polish 2026-05-15 sessions 001–007

Entry 01495_hatsumei ({発明|はつめい}) has a Unicode replacement character (U+FFFD) in a cross-reference headword — likely introduced during a bulk edit. This may indicate a broader data-corruption issue in entries within similar ID ranges that were bulk-edited at the same time.

**Recommended fix**: Open the entry JSON and replace or remove the U+FFFD character in the cross-reference. Also run a grep across the entry set to check for other U+FFFD occurrences:

```bash
grep -r $'\xef\xbf\xbd' entries/ | head -20
```

## Semantic tag "furniture" misapplied in 01490–01511 range

**Source**: Comprehensive-polish 2026-05-15 sessions 001–007

Several entries in the 01490–01511 range had wrong semantic tags: `furniture` applied to non-furniture items. This is the same stale-auto-label pattern documented in [Schema Tag Reliability](../topics/schema-tag-reliability.md) — `furniture` as a semantic tag keeps appearing on entries with no connection to furniture (cf. 02008_ikuratemo above). The polish session fixed individual entries, but this observation suggests the mislabeling may be systematic in this ID range.

**Recommended fix**: Spot-check entries in the 01400–01600 range for `semantic: ["furniture"]` tags that don't match the entry content. If the pattern is widespread, it may warrant a targeted scanner or batch fix.

## 02617_kondeiru (混んでいる) — Conjugation table generated incorrectly

**Status (resolved 2026-06-08):** The one-time non-verb conjugation sweep applied **option (a)** — the bogus `conjugation` table and stray `verb_class` tag were removed. The entry already links its base verb {混|こ}む (00719_komu) in both the notes and a `related` cross-reference labeled "(base verb)", which carries the real conjugation, so no further linking was needed. The exact-enum verb-POS guard in `add_conjugations.py` now skips `expression`-tagged compound-ている entries. (Edge-case note retained below for the curator: a custom ている template for these compounds remains a possible future enhancement, but option (a) is the project-standard handling.)

**Source**: Comprehensive-polish 2026-05-21 session 004

Entry 02617_kondeiru ({混|こ}んでいる, "to be crowded") has a badly wrong conjugation table. The conjugation was generated as if いる were a standalone godan verb rather than recognizing the entry as a compound ている form. Results include forms like {混}んでいった (past) instead of {混}んでいた, and {混}んでいります (polite) instead of {混}んでいます.

**Recommended fix**: Either (a) remove the conjugation table and rely on the notes to explain that this is a ている stative form of {混|こ}む (godan), or (b) manually write a custom conjugation table that treats the いる portion as ichidan rather than godan. Option (a) is simpler and more consistent with how other compound-ている entries are handled. Cross-reference to the base verb {混|こ}む for full conjugation.

**Connection**: This is an edge case for `add_conjugations.py` — the script cannot correctly conjugate entries whose headword is a compound ている form. Similar to the 01300_gozaimasu issue (polite-only verb template).

## 02525_suiteiru (空いている) — Spurious conjugation on a compound-ている expression

**Source**: One-time non-verb conjugation sweep 2026-06-08

Entry 02525_suiteiru ({空|す}いている, "to be empty/uncrowded") is the known sibling of 02617_kondeiru: it had a bogus godan table generated as if it were a `godan-ru` verb (forms like {空}いていらない, {空}いていります, {空}いていった) plus a stray `verb_class: "godan-ru"` tag. It is tagged `pos: ["expression"]`.

**Status (resolved 2026-06-08):** The one-time sweep removed the `conjugation` field and the stray `verb_class` tag (option (a), matching 02617). The base verb {空|す}く (00756_suku) — which carries the real conjugation — is already linked in the notes ("BASE VERB:" section and inline) and the entry has antonym cross-references, so no further linking was needed. The new verb-POS guard in `add_conjugations.py` prevents regeneration.

## 22190_oaisuru (お会いする) — Humble keigo expression stripped; possible re-tag

**Source**: One-time non-verb conjugation sweep 2026-06-08

Entry 22190_oaisuru (お{会|あ}いする, the humble form of {会|あ}う) is tagged `pos: ["expression"]` and had a generated `suru` conjugation table plus a stray `verb_class` tag, both removed by the sweep. Unlike the other 31 swept expressions (multi-word idioms, proverbs, adverbial phrases, and two compound-ている forms), this one is a fixed honorific お〜する construction that *does* inflate like a する verb (お会いします, お会いした). The sweep stripped it (per the prompt's "when unsure, strip and log") rather than re-tagging it `verb-suru`.

**Recommended action (curator):** decide whether お会いする (and any sibling お〜する humble entries) should stay `expression` with the paradigm explained in notes, or be re-tagged `verb-suru` + `verb_class: "suru"` and given a real (correct) conjugation table. The project convention so far treats keigo constructions as expressions, which is why the table was removed rather than regenerated.

## 03032_doukyuusei (同級生) — Near-duplicate example sentences

**Source**: Comprehensive-polish 2026-05-23 session 003

Entry 03032_doukyuusei ({同級生|どうきゅうせい}, classmate) has examples 2 and 3 that are nearly identical ("I ran into a high school classmate" vs. "I met a classmate"). The examples don't offer enough variety to demonstrate different usage contexts.

**Recommended fix**: Replace one of the near-duplicate examples with a sentence showing 同級生 in a different context — e.g., a reunion, nostalgia, comparing professional trajectories, or childhood memories. Maintain progressive length.

## 03370_zureru — Verb conjugation class misclassification (godan → ichidan)

**Source**: Comprehensive-polish 2026-05-25 session 012

Entry 03370_zureru ({ずれる}) was classified as godan but is actually ichidan (ズレる follows the ichidan pattern: ずれない, ずれます, ずれて). The originating polish session corrected the classification. This is the same class of error as 01293_yogoreru (also misclassified godan → ichidan). Both are -eru ending verbs where the godan/ichidan distinction is ambiguous from the romaji alone.

**Recommended action**: Spot-check other -eru/-iru ending verbs in the 03300–03500 range for godan/ichidan misclassification. The pattern suggests batch creation may have defaulted to godan for ambiguous endings.

## 03591_fuukei — Furigana error with 描 kanji; check other entries

**Source**: Comprehensive-polish 2026-05-26 session 004

Entry 03591_fuukei ({風景|ふうけい}) had the furigana error `{描|か}く` (wrong reading for 描 in the "depict" sense) — corrected to `{描|えが}く` (egaku). Worth checking other entries that use 描 kanji, as the wrong reading か is from the homograph 書く/描く ambiguity (かく = "to write/draw" vs. えがく = "to depict/portray").

**Recommended fix**: Grep for `{描|か}` across all entries and verify each instance uses the correct reading for context: かく for informal "to draw" and えがく for "to depict/portray."

## 03707_hitei — Duplicate example sentences

**Source**: Comprehensive-polish 2026-05-26 session 010

Entry 03707_hitei ({否定|ひてい}) has ex2 and ex4 as identical Japanese sentences: both read `{否定|ひてい}{形|けい}を{使|つか}って{文|ぶん}を{作|つく}りなさい。` One should be replaced with a different example showing 否定 in another context (e.g., denying a rumor, negative attitude, negation in logic).

## Compound entries as inline link targets (observation)

**Source**: Comprehensive-polish 2026-05-26 session 008

When compound entries like 天気予報 (01678) or 予防接種 (11068) appear in examples or notes, they should be linked as whole compounds pointing to their own entry, not as separate links to individual components. This is a general linking principle: if a compound has its own entry, the compound is the right link target.

**Status**: Not a single-entry fix but a principle for inline-link polishing sessions to follow.

## 03881_kugi — Semantic tag "body-part" should be "tool"

**Source**: Comprehensive-polish 2026-05-27 session 009

Entry 03881_kugi ({釘|くぎ}, nail) has `semantic: ["body-part"]` — clearly wrong. A nail is a tool/hardware item.

**Recommended fix**: Change `semantic: ["body-part"]` to `semantic: ["tool"]`. Another instance of the wrong-semantic-tag pattern documented in [Cleanup Backlog](cleanup-backlog.md) → Priority 11, extending the confirmed range into the 03800s.

## 03883_kuzu — Semantic tag "furniture" misapplied

**Source**: Comprehensive-polish 2026-05-27 session 009

Entry 03883_kuzu ({屑|くず}, scrap/waste/worthless person) has `semantic: ["furniture"]` — does not match meaning. The word refers to scraps, waste material, or (derogatorily) a worthless person.

**Recommended fix**: Change `semantic: ["furniture"]` to `semantic: ["general"]` or a more appropriate tag. Another instance of the stale-auto-label pattern in [Cleanup Backlog](cleanup-backlog.md) → Priority 11.

## 04312_hatsuden — Semantic tags "geography"/"time-general" incorrect

**Source**: Comprehensive-polish 2026-05-30 session 005

Entry 04312_hatsuden ({発電|はつでん}, power generation) has semantic tags "geography" and "time-general" — neither fits a power-generation entry. Should be "action" or "technology" or a similar neutral tag.

**Recommended fix**: Replace the semantic tags with something appropriate for the entry's domain.

## 04316_same — Semantic tag "general" should be "animal-fish"

**Source**: Comprehensive-polish 2026-05-30 session 005

Entry 04316_same ({鮫|さめ}, shark) has `semantic: ["general"]` while neighboring entries 04319_ika (squid) and 04323_tako (octopus) use `"animal-fish"`. Should be updated for consistency with the same cluster.

**Recommended fix**: Change `semantic: ["general"]` to `semantic: ["animal-fish"]`.

## 04347_shika — Redundant/wrong furigana in example sentence

**Source**: Comprehensive-polish 2026-05-30 session 006

Entry 04347_shika ({鹿|しか}, deer) has ex2 with the unusual furigana `{あげ|あげ}た` — already-hiragana text wrapped in a furigana wrapper with the same reading. Likely should be `{上|あ}げた`. Should be corrected in a future polish pass.

**Recommended fix**: Change `{あげ|あげ}た` to `{上|あ}げた` or simply leave as bare hiragana `あげた`.

## 挙げる (27889) vs 上げる (02443) — Distinct entries, linking awareness

**Source**: Comprehensive-polish 2026-05-30 session 001

挙げる (27889, "to cite/name") is distinct from 上げる (02443, "to raise/give"). Both exist as separate entries with different meanings. Future inline-linking sessions should be aware of the distinction to avoid linking to the wrong entry when either かな form あげる appears in examples or notes.

**Status**: Informational — no entry fix needed, but noting for linking-session awareness.

## 04730_foroo — Semantic tags "building"/"transportation" incorrect

**Source**: Comprehensive-polish 2026-06-02 session (entry 04730)

Entry 04730_foroo (フォロー) had semantic tags "building" and "transportation" — corrected to "communication" and "action" during the polishing session. Another instance of the wrong-semantic-tag pattern in [Cleanup Backlog](cleanup-backlog.md) → Priority 11, extending the confirmed range into the 04700s.

**Status**: Already fixed in the originating session.

## 04770 十人十色 — Furigana reading error pattern ({好|す}み → {好|この}み)

**Source**: Comprehensive-polish 2026-06-02 session 003

Entry 04770 十人十色 had `{好|す}み` — the wrong reading for 好み (should be このみ from 好む = このむ, not すみ). This type of error (wrong on'yomi/kun'yomi choice for a kanji in context) may appear elsewhere in the 04700–05000 range.

**Status**: Already fixed in the originating session. Worth a spot-check for similar wrong-reading furigana errors in neighboring entries.

## 05037_kyoukoku — 浸食 vs 侵食 kanji variant in notes

**Source**: Comprehensive-polish 2026-06-03 session 008

Entry 05037_kyoukoku ({峡谷|きょうこく}, canyon/gorge) uses `{浸食|しんしょく}` (浸 kanji, "soak/permeate") in its notes, but the dictionary only has entry 10927_shinshoku for {侵食|しんしょく} (侵 kanji, "erode/encroach"). The entry was marked `noentry` for 浸食.

Both kanji are used for しんしょく in geological contexts (浸食 emphasizes water seepage, 侵食 emphasizes erosion/encroachment), but 侵食 is the standard geological term. The two are near-synonyms with overlapping usage.

**Recommended fix**: Either (a) add 浸食 as a kanji-variant cross-reference or note in entry 10927_shinshoku, or (b) create a separate entry for 浸食 if the distinction between water-driven erosion (浸食) and general encroachment (侵食) is pedagogically valuable. Option (a) is simpler and aligns with the dictionary's handling of other kanji variants.

## 05124_shiwa — Furigana reading error ({笑|え}い → {笑|わら}い)

**Source**: Comprehensive-polish 2026-06-04 session 013

Entry 05124_shiwa ({皺|しわ}, wrinkle) notes contain `{笑|え}い{皺|じわ}` — the reading え for 笑 looks wrong. In 笑い皺 (laugh lines/crow's feet), the correct reading is `{笑|わら}い{皺|じわ}` (from 笑う = わらう). The え reading of 笑 does not apply in this compound.

**Recommended fix**: Change `{笑|え}い{皺|じわ}` to `{笑|わら}い{皺|じわ}` in the notes field.

## 05134_nouhin — Semantic tag "communication" incorrect

**Source**: Comprehensive-polish 2026-06-04 session 013

Entry 05134_nouhin ({納品|のうひん}, delivery of goods) has semantic tag "communication" — delivery of goods is logistics/action, not communication. Part of the business/logistics cluster (05132–05138: 受注, 発注, 納品, 出荷, 関税, 物流, 流通).

**Recommended fix**: Replace "communication" with "action" or a logistics-appropriate tag.

## 05173/05175 — Spurious verb_class and conjugation on mimetic adverbs

**Status (resolved 2026-06-08):** The stray `verb_class` tag and `conjugation` field were removed from both by the one-time non-verb conjugation sweep, and the new exact-enum verb-POS guard in `add_conjugations.py` prevents regeneration.

**Source**: Comprehensive-polish 2026-06-04 session 015

Entries 05173_nurunuru (ぬるぬる) and 05175_tsurutsuru (つるつる) had spurious `verb_class: "godan-ru"` and full conjugation tables producing nonsense like ぬるぬらない and つるつらない. These are mimetic adverbs, not verbs.

**Status**: Instances of the broader P6 pattern in [Cleanup Backlog](cleanup-backlog.md). Will be addressed by the batch pruner proposed in [Tooling Backlog](tooling-backlog.md) → item 5.

## 05176_gorogoro — 河原 (riverbed) noentry resolved

**Source**: Comprehensive-polish 2026-06-04 session 015

Entry 05176_gorogoro noted that 河原 (かわら, riverbed) appeared as noentry because 03902_kawara is 瓦 (roof tile), a different word.

**Status**: Resolved — 河原 was created as a new entry in the 2026-06-05 vocabulary expansion batch.

## 05318_tairyoku (体力) — Semantic tag "leisure" should be health/body

**Source**: Comprehensive-polish 2026-06-05 session 022

Entry 05318_tairyoku ({体力|たいりょく}, physical strength/stamina) carries `semantic: ["leisure"]`, which does not fit physical stamina. Should be "health" or "body".

**Recommended fix**: Replace "leisure" with "health" (or "body"). Also check the related 〜力 cluster — 気力, 精力, 忍耐力 — for the same misapplied tag, since they were likely created in the same batch.

## 05332–05335 (足し算, 引き算, 掛け算, 割り算) — Math cluster mis-tagged

**Source**: Comprehensive-polish 2026-06-05 session 023

The four arithmetic-operation entries (addition, subtraction, multiplication, division) all carry wrong semantic tags ("body-part", "furniture", "time-general") instead of "mathematics". Created by claude-opus-4-5, modified 2026-04-14 — the same cross-contaminated batch documented in [Cleanup Backlog](cleanup-backlog.md) → Priority 11.

**Recommended fix**: Set `semantic: ["mathematics"]` on all four. Best handled as a small cluster fix.

## 05381_toshoshitsu (図書室) — Duplicate example sentences

**Source**: Comprehensive-polish 2026-06-05 session 025

Entry 05381 ({図書室|としょしつ}, library room) has ex1 and ex4 as identical Japanese sentences. One should be replaced with a different example showing 図書室 in another context (e.g., school library use, quiet-study rules, borrowing). Maintain progressive length.

## 05478_doraibaa (ドライバー) — Notes reference non-existent sense 4

**Source**: Comprehensive-polish 2026-06-06 session 029

Entry 05478_doraibaa (ドライバー) notes mention a "MEANING 4 - COMPUTING" (device driver) but sense 4 is not listed in the definitions array. Either add a computing sense (device driver) as a fourth definition, or remove the dangling reference from the notes.

**Recommended fix**: If the device-driver sense is worth covering (it is a common meaning of ドライバー), add it as sense 4. If not, remove the notes section that references it.

## 05501_shashinka (写真家) — Stale noentry link for カメラマン

**Source**: Comprehensive-polish 2026-06-06 session 030

Entry 05501_shashinka ({写真家|しゃしんか}) notes contain `⟦カメラマン→カメラマン：noentry⟧` but entry 28387_kameraman now exists. The inline link should be updated to point to the correct entry ID.

**Recommended fix**: Update the inline link from `noentry` to `28387`.

## 05629_shushi (主旨) — Near-duplicate example sentences

**Source**: Comprehensive-polish 2026-06-07 session 037

Entry 05629 has ex2 and ex3 as near-duplicates — both illustrate "understanding the 主旨 of a document." One should be rewritten to show 主旨 in a different context (e.g., the gist of a speech or proposal, the main point of an argument, restating a meeting's purpose). Maintain progressive length.

## 05747_kirisuteru (切り捨てる) — Wrong semantic tag "body-part"

**Source**: Comprehensive-polish sessions 2026-06-08 (sessions 045 and pre-session standalone)

Entry 05747_kirisuteru ({切|き}り{捨|す}てる, "to cut down/discard/round down") carries `semantic: ["body-part"]` — incorrect. The word means to lop off, discard, or abandon, and in math contexts to round down. None of these senses relate to body parts.

**Recommended fix**: Replace `"body-part"` with `"action"` (or remove if the entry already has a more appropriate semantic tag). Standard P11 pattern — wrong tag from a 2026-04-14 batch run.

## 08116_rokku (ロック) — Missing lock/locking sense

**Source**: Comprehensive-polish session 049 (entries 05891–05915), 2026-06-08

Entry 08116_rokku (ロック) currently covers only the rock music sense. A lock/locking sense (as in a door lock, phone screen lock, social media account lock) is missing. These senses are frequent in everyday Japanese (鍵をロックする, スマホがロックされた, アカウントがロックされた).

**Recommended fix**: Expand 08116 to include a second sense covering the lock/locking meaning, with examples across door locks, digital locks, and account locks. This is distinct from the rock-music sense and from any existing 錠前 (jōmae) lock entry, since ロック specifically marks the loanword usage.

## 空前絶後 (くうぜんぜつご) — Missing yojijukugo entry

**Source**: Comprehensive-polish session 050 (entries 05936–05953), 2026-06-09

The four-character compound 空前絶後 (unprecedented and never to be repeated) was referenced in the cross_references field of entry 05949. No entry exists; a noentry inline link was added.

**Recommended fix**: Create an entry for 空前絶後 as a yojijukugo expression. It appears in formal writing and news media to describe historic firsts or unprecedented events. Added as candidate C21844.

## 01385_kimochi & 02485_kimochi (気持ち) — Duplicate entries needing consolidation

**Source**: Routine v2 polish session, 2026-06-10

Two entries cover 気持ち (きもち, "feeling, mood"): **01385_kimochi** (basic tier,
gloss "feeling, sensation", headword `{気持ち|きもち}`) and **02485_kimochi** (core
tier, gloss "feeling, emotion", headword `{気持|きも}ち`). They are the same word
with the same reading and near-identical glosses — almost certainly a duplicate
pair that should be consolidated rather than maintained as two diverging sources
of truth (cf. the いくら〜ても pair in [Cleanup Backlog](cleanup-backlog.md) → P8).

Two complications to resolve during the merge:
- **Tier conflict**: one is `basic`, the other `core` — both closed tiers. The
  curator should decide which entry survives; the lower ID (01385) is basic.
  Inline-link polishing this session pointed links at 01385.
- **Malformed headword on 01385**: `{気持ち|きもち}` has the okurigana inside the
  wrapper (non-canonical; should be `{気持|きも}ち`, which is exactly what 02485
  already uses). 01385 is on the [Tooling Backlog](tooling-backlog.md) → item 9
  headword-fix list for this reason. If 01385 is kept, fix the headword as part
  of the same edit.

**Recommended fix**: Follow the `consolidate-entries` / `resolve-duplicates`
skills. Run `python3 build/find_merge_candidates.py --merge-only` to confirm and
check for sibling duplicates, pick the survivor, transfer unique
examples/notes/cross-refs, fix the survivor's headword to canonical form, and
delete the other. Curator decision needed on which tier/ID survives.

## Compound-verb morpheme gaps: 〜込む suffix and 掛かる "be about to" sense

**Source**: Routine v2 polish session, 2026-06-10

Inline-link polishing of 06xxx godan compound verbs hit two recurring `noentry`
gaps in FORMATION glosses:
- **Productive suffix 〜込む** ("into / thoroughly", as in 放り込む, 浮かび上がる's
  neighbours): only the standalone verb 込む ("to be crowded; to cost / take
  time") has an entry, so the compound-forming suffix sense can't be linked.
- **掛かる "to hang over / be about to (do)" sense**: the existing かかる entry
  covers "to be crowded / to cost / take," not the 差し掛かる-style "be on the
  verge of" sense, forcing `noentry`.

These are the compound-verb-morpheme linkability question — see
[Compound Verb Representation](../topics/compound-verbs.md) for the
entry-vs-pattern design context. If the project wants compound-verb morphemes to
be linkable, candidate additions would be a suffix entry for 〜込む and an added
sense (or grammar-pattern entry) for the 掛かる "be about to" meaning. Otherwise
this is informational — the `noentry` markers are correct given current scope.

## 06917_zo — wrong formality tag and wrong semantic tags for a sentence-final particle

**Source**: accuracy-review session 003 (2026-06-11)

Entry `06917_zo` (ぞ, sentence-final particle) has two tag errors:
- `formality: "formal"` — the notes explicitly say "Casual to rough. Never used in formal situations." This is a P17 error (over-applied `formal` to an informal/rough word).
- `semantic: ["clothing", "time-general", "tool"]` — these tags make no sense for a sentence-final particle. Likely batch tag-drift from an adjacent entry or a creation-time error.

**Recommended fix**: Set `formality: "informal"` (or `"rough"`/`"casual"` if the schema supports it — otherwise `"informal"`). Replace the semantic tags with something appropriate for a masculine/emphatic sentence-final particle (e.g., `["expression"]` or `["grammar"]`). Update the `modified` timestamp.

## 06109_karorii (カロリー) — Inline links needed

**Source**: 2026-06-13 polish session 008 (entry encountered but not processed)

Entry 06109_karorii (カロリー, calorie) was identified during the session covering
entries 06101–06110 but was not processed in that session. It likely needs ⟦...⟧
inline-link wrappers added to content words in its examples and notes.

**Recommended fix**: Review examples and notes for words that have dictionary entries
and add inline links. This is standard tier-2 polishing work; no structural changes
expected.

## 06131_toiawase (問い合わせ) — Noun headword but verb-lemma examples and conjugation

**Source**: 2026-06-14 routine polish session 004

Entry 06131_toiawase has the **noun** headword 問い合わせ (inquiry), but both ex1 and ex2
demonstrate the **compound verb** 問い合わせる (a separate entry, 17737_toiawaseru), and the
conjugation table lists the unnatural 問い合わせする (suru) paradigm — 問い合わせ is a 連用形
noun, not a する-verb. The polish session linked the verb forms to 17737, but the entry
would benefit from restructuring: either separate the noun headword cleanly from the verb
lemma (give the noun its own noun-appropriate examples) or point the verb examples
explicitly at 17737 and drop the spurious 問い合わせする conjugation.

**Recommended fix**: Remove the suru conjugation table (問い合わせ as a noun doesn't conjugate;
the verb lives at 17737). Replace the verb-form examples with genuine noun examples of
問い合わせ (e.g. お問い合わせはこちら, 問い合わせが殺到する) or, if kept, ensure they link to
17737. Needs per-entry judgment.

## 05803_sougyousha & 05720 — Stale `noentry` inline links (now resolvable)

**Source**: 2026-06-16 accuracy-review run

Two more stale `⟦…：noentry⟧` markers surfaced during review, the same class as the
05528/05530/00012 cases under [Tooling Backlog](tooling-backlog.md) → item 19:
- **05803** links `創業者→noentry`, but the entry now exists: **29027_sougyousha** (founder).
- **05720** links `ぼりぼり→noentry`, but the entry now exists: **28996_boribori**.

**Recommended fix**: Re-resolve both markers to the existing IDs (a deterministic
lookup against `build/word_id_lookup.json`). These are concrete instances for the
proposed `check_noentry_links.py` self-healing scan (Tooling item 19); until that ships,
fix them in the next inline-link refresh pass that touches the 0570x–0580x range.

## 00304_nandemo (何でも) — sense 3 "by all means / at any cost" likely not standard usage

**Source**: 2026-06-20 routine polish session (inline-link pass over the priority lane)

00304 何でも carries a sense 3 glossed "by all means / at any cost" (examples ex11–15)
that rests on 何でも **alone** carrying an adverbial "at any cost" meaning. That reading
is dubious as standard usage: the natural phrasings for "at any cost" are 何が何でも or
どうしても, where the force comes from the fuller idiom, not from 何でも by itself. 何でも
on its own means "anything / everything" (sense 1) and "I hear that… / apparently"
(sense 2, 何でも〜らしい).

**Recommended action**: a deeper review of sense 3 — likely either remove it or
re-scope it as the fixed idiom 何が何でも (and add/point to a 何が何でも entry if warranted).
Out of scope for a link-only polish pass; needs a sense-level editorial decision, so
parked here rather than fixed inline. If sense 3 is removed, re-check that ex11–15 are
relocated or dropped, and that no cross-reference points at sense 3.

## 00642_kinyoubi (金曜日, Friday) — no cross_references to the other weekdays

**Source**: 2026-06-22 routine polish session (priority lane)

00642 金曜日 has **no `cross_references` field populated** — it does not link to any of the
other six weekday entries (日曜日 / 月曜日 / 火曜日 / 水曜日 / 木曜日 / 土曜日). Days of the week
are a tight closed thematic cluster and are exactly the kind of set a learner browses
laterally, so each weekday should `cross_references` the other six (the
[Cross-Reference Design](../topics/cross-references.md) thematic-cluster case). The polish
run left it untouched to avoid a **6-entry back-link cascade** in a single-entry pass.

**Recommended action**: a small one-shot pass that adds the symmetric six-way back-links
across all seven weekday entries at once (find them by reading 〜ようび / gloss "…day"),
rather than fixing one in isolation. This is the same thematic-cluster symmetry work as
[Cleanup Backlog](cleanup-backlog.md) → Priority 3.

## 29452 (猿人) — wrong reading さるじん → corrected to えんじん — RESOLVED 2026-06-25

**Status (resolved 2026-06-25 routine new-entries run, harvested 2026-06-26)**: A 2026-06-25 new-entries
run corrected the entry: **reading → えんじん**, the headword and examples were re-furiganaed (the old
headword was also bare/unwrapped), and the file was renamed **29452_sarujin → 29452_enjin**. The standard
reading was confirmed by entry **29467 原人**, which cross-references 猿人 / えんじん. The run took the
filename-romaji change (URL change on the `_sarujin`→`_enjin` suffix; the five-digit ID is unchanged).
Candidate **C22059** (猿人 / えんじん) is now redundant and should be dropped on the next candidate sync.
The observing run flagged a follow-on watch item: **other rare-reading slips may exist in the 29400+
corpus-harvest block** — worth a spot-check as polishing/review reaches that range.

**Source**: 2026-06-24 new-entries run (flagged by the 2026-06-24 routine, harvested 2026-06-25)

Entry 29452 猿人 was created with reading **さるじん**, but the standard paleoanthropology reading
is **えんじん** ("ape-man"), parallel to the established series 原人 (げんじん) / 旧人 (きゅうじん) /
新人 (しんじん). This looks like a wrong-reading slip from the 2026-06-24 new-entries run. The same
run added candidate **猿人 / えんじん (C22059)** with the correct reading, so the dictionary now has the
word queued twice under two readings.

## 書き替える (かきかえる, candidate C22065) — 替-orthography variant of 08225 書き換える, not a distinct word

**Source**: 2026-06-25 routine new-entries run

A new-entries run hit candidate **書き替える (かきかえる, C22065)** and recognised it as a 替-kanji
orthographic variant of the existing entry **08225 書き換える (書き*換*える)** — the same word, same
reading (かきかえる), differing only in the 替/換 kanji choice. The run **skipped it** rather than create
a near-duplicate entry.

**Recommended action (curator)**: fold 書き替える into 08225 as an **alternate-orthography note / variant
headword** (the dictionary's standard handling of kanji variants — see
[Word Variants](../topics/word-variants.md)), then drop candidate C22065 on the next sync. Until then the
candidate is parked for the curator; it should **not** be drawn as a fresh entry by a future new-entries run.

## 07105_enshi (遠視) — no inline links + weak `general` tag, needs a full frontier polish

**Source**: 2026-07-02 routine polish session 004

07105 遠視 (farsightedness) predates the inline-link polishing step: its examples and notes carry **no
`⟦...⟧` links at all**, and its sole semantic tag is the weak catch-all **`general`**, whereas its
sibling ophthalmic-condition entries 近視 (nearsightedness) and 乱視 (astigmatism) use **`health`**. The
observing run only touched it for a back-link (per the no-recurse rule) and did not do the full pass.

**Recommended action**: a full frontier-style polish — add inline links to examples and notes, and
re-tag `general`→`health` to match the 近視/乱視 siblings.

## 06372_hikinobasu (引き伸ばす) — dubious related-compound list in notes

**Source**: 2026-07-02 routine polish session 004

The "RELATED ～伸ばす COMPOUND VERBS" note in 06372 引き伸ばす lists **書き伸ばす** and **押し伸ばす**, which
appear non-standard/rare — neither has an entry and both are dubious as real dictionary words. They were
left marked `noentry` without candidates (correctly, since they may not be real words).

**Recommended action**: revise the note's related-compound list to more common, genuinely-standard
～伸ばす compounds (e.g. 引き伸ばす's actual near-relatives), or drop the questionable entries from the list.

## 04265_kakato (踵, heel) — semantic tag `clothing` should be `body-part`

**Source**: 2026-07-14 routine polish (frontier 06480–06486)

04265 踵 (heel) carries the semantic tag **`clothing`**, which is wrong — it is a body part. Its sibling
body-part entries 足首 (ankle), 爪先 (toe), and 踝 (ankle bone) all use **`body-part`**. The observing run
noticed this while polishing an unrelated frontier range and flagged it as out of scope for that run.

**Recommended action**: re-tag 04265 踵 `clothing`→`body-part` to match the 足首/爪先/踝 siblings, and bump
`modified`. A trivial single-entry fix; also a good candidate for a `check_tag_drift` semantic-mismatch
catch (a `clothing` tag on a body-part word).

## 01385_kimochi / 02485_kimochi (気持ち) — duplicate entries, merge candidate

> **Filing note (2026-07-26)**: this duplicates the earlier section
> [01385_kimochi & 02485_kimochi — Duplicate entries needing consolidation](#01385_kimochi--02485_kimochi-気持ち--duplicate-entries-needing-consolidation),
> which is the **canonical** one (it also records the malformed `{気持ち|きもち}` headword on 01385).
> Both are kept for now because each carries detail the other lacks; merge them the next time this
> page is linted. A **third** report arrived from a 2026-07-26 polish run, adding one operational
> datum: **every polisher that links 気持ち has to pick an ID arbitrarily** — that run linked to
> 01385 (the older/basic one), earlier runs picked 02485 — so inbound inline links are accumulating
> against *both* IDs while the pair stays unresolved. That raises the cost of the eventual merge on
> every polish run, which is the argument for doing it sooner rather than at the frontier's pace.

**Source**: 2026-07-25 routine polish run

Two entries cover 気持ち, both glossed "feeling, mood": **01385_kimochi** and **02485_kimochi**.
This is the classic parallel-sources-of-truth case that
[Cleanup P8](cleanup-backlog.md#priority-8-unconsolidated-duplicate-expression-entries) describes —
each polishing pass improves one of them and they drift further apart.

**Recommended action**: a consolidation session (`prompts/consolidate_entries.md`, `resolve-duplicates`
skill). Keep the lower ID (01385) per the usual rule unless the higher one is materially richer, merge
the senses/examples/notes, and redirect inbound cross-references and inline links to the keeper.
Because 気持ち is a high-frequency word, check `build/word_id_lookup.json` and inbound `⟦…：02485_kimochi⟧`
links before deleting anything. `find_merge_candidates.py --merge-only` should already list this pair.

## 00969_mata (また) — sense 3 "or" required また, not the bare adverb (fixed 2026-07-25; check the pattern elsewhere)

**Source**: 2026-07-25 routine polish run

00969 また's **sense 3 ("or")** carried **four examples using bare また** where the compound **または**
is required. Corrected in-run.

The reason it is filed here is the **generalisation the observing run drew**, which no detector covers:
an entry for a bare adverb can grow a sense that only the *compound* form expresses, and the examples
will then illustrate a form the headword does not have. **Recommended action**: when polishing any entry
that glosses a bare adverb or particle with a sense that feels compound-only (また/または, もし/もしも,
たとえ/たとえば, など/などと), check that each example actually uses the form the headword names. Worth
raising as a checklist line in `prompts/comprehensive_polish.md` (curator call — Routine `wiki` runs may
not edit prompts) rather than a script, since the judgment is semantic.

## 18554_kundoku (訓読) — conflates 訓読 (kanbun kundoku) with 訓読み

**Source**: 2026-07-25 accuracy-review run

18554 訓読 treats two distinct things as one word:

- **訓読 (くんどく)** — reading classical Chinese (漢文) as Japanese, the 漢文訓読 tradition;
- **訓読み (くんよみ)** — the native-Japanese reading of a kanji, as opposed to 音読み.

They are related historically but are not the same lexeme, and a learner looking up either one gets
a muddled answer. The run **corrected the furigana and extended the gloss** so the entry is no longer
wrong, but the underlying conflation remains.

**Recommended fix**: split. Keep 18554 for 訓読 (くんどく) with the 漢文 sense, and create a separate
entry for 訓読み (くんよみ), cross-referenced to 音読み if that entry exists (and to each other via
`contrast`). Check `build/word_id_lookup.json` for inbound links to 18554 that actually meant 訓読み
before splitting. **Curator decision** — an entry split is out of scope for a polish pass.

## 00475 / 00765 / 02640 (やさしい) — three entries across two words

**Source**: 2026-07-26 routine polish run; corrected and re-measured by the 2026-07-28 wiki harvest
after a second 2026-07-27 polish run reported the *opposite* entry as the offender.

やさしい is spread across three entries covering two distinct words (易しい "easy" and 優しい "kind"),
and the split does not follow the words. **The two reports disagreed, so this harvest read all three
files — and both were right.** The structure is worse than either described:

| Entry | Headword | Sense 1 (ex1–5) | Sense 2 (ex6–10) |
|---|---|---|---|
| 00475 | combined 易しい／優しい | easy, simple | kind, gentle, tender |
| 00765 | 易しい | easy (易しい) | **kind (優しい)** |
| 02640 | 優しい | kind (優しい) | **easy (易しい)** |

**All three entries are near-complete treatments of both words** — 00765 and 02640 are mirror images
of each other, each leading with its own headword's sense and then documenting the other word in
full underneath, ten examples apiece. The duplication reaches the example level: 00765's ex1 and
02640's ex7 are the same sentence (この問題は易しい), as are 00765's ex2 and 02640's ex8
(易しい日本語で書いてある). This is not "one entry has some misfiled examples"; it is the same
content written three times under three headwords.

That also explains the contradictory reports, and is worth noting as a general caution: an entry
whose *second* sense belongs to a different lemma looks correct from the inside — each sense is
internally consistent, the examples match their glosses, and the furigana is right. Only a
side-by-side read of the sibling entries reveals it. Any polisher reaching one of these has to
decide the structure before making any per-entry fix, which is why the sequential frontier keeps
deferring it.

**Recommended fix**: decide the target shape first — the natural one is **two entries, one per word**
(易しい and 優しい), with a `homophone` or `contrast` cross-reference between them, retiring or
redirecting the third. Then move the misfiled 優しい examples out of 00765. Follow `/resolve-duplicates`
for the retirement, and check inbound `⟦…⟧` links to all three IDs first — やさしい is high-frequency.
**Curator decision** (which ID survives is an external-URL question — see `CLAUDE.md`, "Never renumber
existing entries").

## 04467_shichou — bound morphemes and honorific prefixes routed through `noentry`

**Source**: 2026-07-26 routine polish run

04467's notes contain `⟦{視|し}→視：noentry⟧` and `⟦ご→ご：noentry⟧` — a bound morpheme and an
honorific prefix marked as "no entry exists." The marker is technically true and permanently
unresolvable: 視 as a bound morpheme and ご- as a prefix will never become headwords, so these links
sit in the `noentry` pool forever, and the [stale-`noentry` re-resolution scan](tooling-backlog.md#19-stale-noentry-inline-link-detector)
will re-check them on every pass with no possible outcome.

This is a **convention gap, not an entry defect**: etymology lines that decompose a compound into its
morphemes have nowhere to point. Three coherent options — (a) don't link bound morphemes at all
(leave them as plain text with furigana); (b) link them to the kanji index rather than to an entry;
(c) keep `noentry` but add a distinct sentinel (e.g. `nolink`) so the re-resolution scan can skip
them permanently.

**Recommended**: (a) or (c). The `inline-word-links` skill should state the rule explicitly — this is
the second skill-level linking gap found in the same cycle (see
[Tooling 37](tooling-backlog.md#37-detector-copula-て-form-で-inline-linked-to-the-particle-で) for the
copula `で` case). **Curator action** — `wiki` runs may not edit skills.

## 03794_warukuchi & 12672_waruguchi (悪口) — same word under two readings, merge candidate

**Source**: 2026-07-27 routine polish observation.

`03794_warukuchi` (わるくち) and `12672_waruguchi` (わるぐち) are the same word — 悪口,
"speaking ill of someone" — split across two entries by reading alone. Both readings are
standard and dictionary-attested (わるぐち is the more common in modern speech; わるくち is
the older/more formal), which makes this a **variant-reading consolidation**, not a
duplicate-and-delete: the surviving entry should document both readings in a VARIANTS
section rather than silently drop one.

**Recommended resolution**: keep the lower ID (`03794`) as the surviving entry per the
consolidation convention, fold in anything `12672` has that it lacks, add both readings to
the notes, and redirect inbound cross-references and inline links. This needs the
`consolidate-entries` skill and a curator decision on which reading leads the headword — the
reading is filename-romaji-affecting, so it is not a Routine-side call.

**Related**: [Cleanup P8](cleanup-backlog.md#priority-8-unconsolidated-duplicate-expression-entries).

## 08169_chuubi & 17946_nakabi (中火) — one entry has the wrong reading entirely

**Source**: 2026-07-27 routine polish observation (found while inline-linking 06656 火加減).

Both entries carry the headword 中火 with the same gloss ("medium heat (cooking)"), under two
different readings:

| Entry | Headword | Reading |
|---|---|---|
| `08169_chuubi` | `{中火\|ちゅうび}` | ちゅうび |
| `17946_nakabi` | `{中火\|なかび}` | なかび |

**中火 is read ちゅうび.** なかび is the reading of **中日** (the middle day of a period —
a different word with different kanji), so `17946` is not a variant reading: it is either a
mis-created duplicate of 08169 or an entry that was *meant* to be 中日 and got the wrong
kanji at creation.

**Two possible resolutions, and the choice is a curator call**:
1. **Duplicate** → delete/merge `17946` into `08169` per the `delete-entry` skill, redirecting
   any inbound references.
2. **Wrong kanji** → fix `17946`'s headword to 中日 and rewrite its gloss/examples, keeping
   the ID and reading.

Resolution (2) preserves an entry for a word the dictionary otherwise lacks, so it is worth
checking whether 中日 has an entry before defaulting to deletion. Note that `17946` was
already touched once, on 2026-07-20, when a furigana screen flagged its reading and the run
**correctly rejected the flag as an alternate reading** — the deeper problem was not visible
from inside the entry.

**Related**: [Cleanup P8](cleanup-backlog.md#priority-8-unconsolidated-duplicate-expression-entries),
`resolve-duplicates` skill.

## 00719_komu & 02574_komu (込む) — duplicate entries, and the 〜込む suffix is a third item with no entry

**Source**: 2026-07-28 routine polish run (noticed while resolving a `込む：noentry` marker in
06852_hourikomu).

`00719_komu` ("to be crowded") and `02574_komu` ("to be crowded, to be congested") are the same
lemma with the same reading and overlapping glosses — a straightforward merge candidate for a
`consolidate_entries` pass. Which ID survives is a curator call (see `CLAUDE.md`, "Never renumber
existing entries"); check inbound `⟦…⟧` links to both first.

**The more interesting half is the third item.** The compound-forming suffix **〜込む** (書き込む,
飛び込む, 放り込む, 話し込む) is a genuinely different morpheme from either entry — it does not mean
"be crowded", it contributes a directional/thoroughness sense to a V1 stem — and it has **no entry
at all**. So the merge does not resolve the `noentry` marker that surfaced this: a compound-verb
entry linking its own 〜込む component has nowhere correct to point, and pointing it at the
"crowded" entry would be actively wrong.

This is the bound-morpheme gap that [04467_shichou](#04467_shichou--bound-morphemes-and-honorific-prefixes-routed-through-noentry)
documents from the other direction, and it is the concrete case behind
[topics/compound-verbs.md](../topics/compound-verbs.md)'s open question about whether productive V2
suffixes deserve entries. Sequence the merge first (it is decidable now), then treat 〜込む as a
separate curator decision.

## でも (particle, "any ~" / "even ~") — no entry, and the candidate list will not accept it

**Source**: 2026-07-28 routine polish run (00304_nandemo).

The particle でも — the one in 何でも / 誰でも / いつでも "any ~", and in the concessive "even ~" —
has no entry. The two entries occupying the surface form are different words: `00925_demo` is the
sentence-initial conjunction "but, however", and `19416_demo` is デモ "demonstration". Inline links
in 00304_nandemo therefore had to fall back to `：noentry⟧`, and the same gap almost certainly
affects `08498_daredemo`, `03826_itsudemo`, and `08499_dokodemo`.

**It cannot be queued through the normal route.** `manage_candidates.py add` rejects でも as a
duplicate of the conjunction, because its duplicate check keys on (surface, reading) and cannot
represent a homograph — see [Tooling item 41](tooling-backlog.md#41-manage_candidatespy-cannot-queue-a-homograph--the-duplicate-check-is-surface-reading-not-surface-reading-sense).
Until that is fixed the curator would need `--force` or a separately-disambiguated candidate.

**Why it is worth the workaround.** This is a high-frequency function word, it is the head of a
small productive family (question word + でも), and the four entries that need it are all already
written — so the `noentry` markers pointing at it are permanent dead ends rather than temporary
ones. A particle entry here would also give the 〜でも cluster a common target, which is exactly
what `particle-entry`'s contrast-and-pattern format is for.

## Related pages

- [Cleanup Backlog](cleanup-backlog.md) — systemic patterns
- [Tooling Backlog](tooling-backlog.md) — tool improvements
- [Content Pipeline](../project/content-pipeline.md) — polishing workflow
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis covering several of these
