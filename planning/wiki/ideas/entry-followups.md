# Entry Follow-ups

**Last updated**: 2026-08-13 (added **08989 車席**, a probably-fabricated headword flagged five times by the reviewer and escalated rather than deleted; **08985 日日**, the wrong orthography for ひにち; **17576 摺り寄る**, a rare spelling as headword, found only because a duplicate-check mislabelled its common variant as a homophone; **06899 顔を出す**, whose top-level gloss covers one of two senses and which needs a convention ruling before it needs an edit; and **00743 音**, parked at sole-`general` because the tag vocabulary has no sound/perception slot. Also corrected a dangling "Cleanup P56" forward reference in the 06886 follow-up.) Prior 2026-08-12 (added **28358_buri** — the manner/style sense of 〜ぶり belongs in the existing time-interval entry, the second instance after 03515 日光 of a candidate that is real, is not a duplicate entry, and cannot be created because `check_duplicate.py` sees the headword as taken; **06886 haragatatsu** — 腹が立たしい corrected to 腹立たしい, with the sibling-idiom spot-check deferred to the frontier pass over the same creation cohort (P56); **00823/01525 若い** re-filed, a *second* report of a duplicate already on this page since 2026-08-08, recorded to make the re-filing cost visible — polish runs can only file consolidations, never perform them, so four are now open here; and a ruling recommendation for **historical era names**, filed as `event-name` for want of a fit when `time-period` + `proper-noun` are both already in `VALID_SEMANTIC` and say what an era actually is.) Prior 2026-07-27 (added **03794_warukuchi / 12672_waruguchi 悪口** — the same word split across two standard readings (わるくち / わるぐち), a variant-reading consolidation rather than a delete, needing a curator call on which reading leads the headword; and **08169_chuubi / 17946_nakabi 中火** — one of the two is simply wrong: 中火 is read ちゅうび, and なかび is the reading of 中日, so 17946 is either a mis-created duplicate or an entry that was meant to be 中日 and got the wrong kanji, notable because a 2026-07-20 furigana screen flagged its reading and the run *correctly* rejected the flag as an alternate reading — the real defect was invisible from inside the entry.) Prior 2026-07-26

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

## 20891 {紆余|うよ} — the examples use the word the entry says is not used that way

**Source**: 2026-07-29 routine accuracy-review (20703–21300)

The entry's own explanation states that 紆余 is "rarely used on its own in modern
Japanese" — which is correct; in practice it lives almost entirely inside the
yojijukugo 紆余曲折 (うよきょくせつ, "twists and turns, ups and downs"). But examples 1 and
2 use it as a standalone suru-verb: **紆余した道**, **川は紆余しながら**.

The accuracy reviewer flagged the gloss; the flag was **rejected**, correctly, because
the caveat the reviewer wanted is already in the notes. The defect is therefore invisible
to the review dimension that found it: the *explanation* is right, and the *examples*
contradict it, and nothing checks an entry's examples against its own usage note.

**Why this needs a curator rather than a polish pass**: the fix is not a wording change.
Either the examples are replaced with 紆余曲折 sentences — in which case the headword is
arguably 紆余曲折 and this entry should be about the compound — or the entry keeps 紆余 as
its headword and the examples become citation-style ("紆余 appears in 紆余曲折…"), which is
not the house example format. Both are entry-identity decisions of the same kind as the
やさしい and 込む follow-ups below.

**Generalisable check worth sizing**: entries whose notes contain a "rarely used on its
own" / "mainly in compounds" caveat, where the examples nonetheless use the bare
headword. Probably a small class — bound morphemes and cranberry morphemes — but it is
the one shape where an entry's prose and its examples can each be right in isolation and
wrong together, which is precisely what no current check can see.

## ば (conditional particle) and 逆転する — the two words the dead-link sweep could not link to

**Source**: 2026-07-29 routine systemic-fix (the Tooling 11 dead-link sweep)

The 2026-07-29 sweep repaired all 291 dead inline links by resolving each link's base form
through `word_id_lookup.json`. **Two could not be repaired, because the word has no entry to
link to.** Both were set to `noentry` and queued as candidates:

| Word | Reading | Source entry | Note |
|---|---|---|---|
| 逆転する | ぎゃくてん-する | 05510 | "to reverse a situation" — an ordinary suru-verb gap |
| **ば** | — | 05595 | the **conditional particle** |

**ば is the one worth the curator's attention.** It is a core intermediate grammar point —
one of the four main conditional forms a learner has to distinguish (ば / たら / と / なら) —
and the dictionary has no entry for it at all. Everything else in that group is the kind of
thing this dictionary exists to explain.

Three things make it awkward rather than merely missing:

1. **It is a bound form, not a free word.** ば attaches to a verb stem (行けば, 見れば), so it
   belongs with the `〜` affix headwords (`〜的`, `〜者`, `〜中`) rather than as a bare entry —
   a headword-form decision before it is a writing task.
2. **The candidate list will not accept it**, for the same reason it refused でも: the
   duplicate check keys on (surface, reading), and ば collides with existing entries. See
   [Tooling 41](tooling-backlog.md#41-manage_candidatespy-cannot-queue-a-homograph--the-duplicate-check-is-surface-reading-not-surface-reading-sense).
   So the normal capture path cannot queue it and it will not resurface on its own.
3. **A homophone trap sits directly behind it.** The sweep's own lookup resolved ば to
   `03699_ba` (場, "place") as a *single confident candidate* — the one false resolution in
   111 mappings, caught only because the run read it in situ. Any future automated link repair
   that trusts a single-candidate answer will make this exact mistake again. See
   [P27](cleanup-backlog.md#priority-27-dead-inline-link-target-ids).

**Recommended**: create ば as an affix-form particle entry alongside たら/と/なら (the
`particle-entry` skill covers the predicate-list and contrast structure this needs), and note
that until it exists, links to it must stay `noentry` rather than being resolved.
逆転する is an ordinary candidate needing no decision.

## 06703_furikiru — 15 examples, zero inline links, core tier

**Source**: 2026-07-30 routine polish run (frontier 06698–06704; left untouched deliberately)

振り切る sits in the [P21](cleanup-backlog.md#priority-21-unlinked-自動詞他動詞-labels-and-particles-in-compound-verb-notes)
zero-link band with **15 examples and no `⟦…⟧` links anywhere**, and it is **core tier**, so its
examples are read by more learners than a general-tier entry's. Linking it from scratch is on the
order of 90 dictionary lookups — several times a normal frontier slot.

The polish run made the right call in skipping it rather than half-linking it (a half-linked entry
looks finished and stops attracting attention), but the consequence is that the frontier has now
moved past it and nothing will return to it on its own.

**Recommended**: a dedicated pass for this entry alone, or hold it until
[Tooling 49](tooling-backlog.md#49-read-only-inline-link-suggester-propose--never-write)
(the read-only link suggester) exists — this is precisely the entry that tool would pay for
itself on. Also worth checking while it is open: the entry is a compound verb, so the
`自動詞`/`他動詞` label and particle links that P21 was originally named for apply too.

## 00759 {飛|と}ぶ — only the two literal senses, none of the frequent extended ones

**Source**: 2026-07-31 routine polish run (priority lane)

The entry documents 'fly' and 'jump' and stops there. Missing, all common and all unmarked:

| Pattern | Sense |
|---|---|
| {帽子\|ぼうし}が飛ぶ | to be blown off |
| ページが飛ぶ / {順番\|じゅんばん}が飛ぶ | to be skipped |
| データが飛ぶ | to be lost (data) |
| {現場\|げんば}に飛ぶ | to rush off to |

The polish run also had to **rewrite two of the existing 'jump' examples**, which were wrong
rather than merely thin — 子供が飛んでいます reads as *flying*, not jumping, and the sense the
example was written to teach is 跳ぶ/跳ねる territory.

Adding four senses with examples and reworking the sense ordering is more than a polish slot
affords; this is a rewrite. Basic tier, so it is also high-traffic. Note that 飛ぶ/跳ぶ is a
[homograph pair](../topics/homographs.md) — whatever is added should say which spelling belongs
to which sense.

## 00711 かかる — missing 罠にかかる and 病気にかかる

**Source**: 2026-07-31 routine polish run

The entry glosses only "to take (time/money), to cost". But かかる is the standard verb in
{罠|わな}にかかる (to be caught in a trap) and {病気|びょうき}にかかる (to fall ill), and neither
is covered.

This is already costing other entries: 06716 まんまと has to inline-link 罠にかかる *to this
entry* regardless, so a reader following that link lands on "to cost" and learns nothing.

Either add the senses here, or split — the に-marked "be caught by / come down with" sense is
arguably a different verb from the "require (time, money)" one and is written 罹る in the medical
case. Related: [Tooling 52](tooling-backlog.md) already flags this entry's transitivity pair
(00711 かかる / 00854 かける) as having prose and `prominent_see_also` but no structured
`cross_references` link.

## 06718 かりかり — two obvious mimetic neighbours unlinked

**Source**: 2026-08-01 routine polish run

06718 かりかり links さくさく (05887) but not ぱりぱり (05259) or ばりばり (05720), which are the
nearest members of the same crunchy-texture mimetic set. Left this run to avoid widening the
run's neighbor edits past its frontier block. Small, and best done together with the rest of the
05xxx/067xx mimetic cluster rather than alone.

## The calendar family (00624–00672 and neighbours) — cross-references half-wired

**Source**: 2026-08-01 routine polish run

Before that run, essentially the whole day/month/date family carried **empty
`cross_references`** — 00624, 00625, 00634, 00635, 00653, 00665, 00667, 00672, 00631, 00636,
00640, 00642, 00646, 00657, 00662, 00668, 03877, with only 00621 and 00656 having any. The
series structure — Monday↔Tuesday, January↔February, 何月↔月 — lived entirely in prose notes,
so it was invisible to site navigation and to `check_semantic_clusters.py`.

The run wired up the entries it touched plus their direct neighbours. **Still needing the same
treatment**: 00631 (January), 00636 (December), 00640 (Tuesday), 00642 (Friday), 00646
(September), 00657 (February), 00662 (June), 00668 (April), 22086 (何月).

A second, related gap in the same family: several of these entries' notes are **entirely
kanji-etymology plus a set list, with no usage information at all** — no particle, no "on
Saturday", no frequency expressions (00621 土曜日 is the type specimen). Because the set is
formulaically similar, adding a USAGE section to each is an unusually well-bounded
`systemic-fix` batch: one template, ~17 entries, no per-entry judgment beyond the word itself.

## The 00680–00760 calendar/time band: notes whose series lists are naked Japanese

**Source**: 2026-08-01 routine polish run (priority lane, 00687–00745).

Every entry the notes-priority lane surfaced in this band failed the *same* tier-1 requirement,
and it is not the one the notes scorer thinks it is measuring. Their notes carry a **series list**
— {先月|せんげつ}/{今月|こんげつ}/{来月|らいげつ}, the 毎- series, the 来- series — written as
naked `{漢字|かな}` with **no inline links at all**, while the same entries' example sentences are
fully linked. They are early basic-tier entries created before full note-link coverage became a
requirement.

The band 00680–00760 is dense with them (time words, counters, calendar vocabulary) and the
formulaic shape makes it a good bounded batch rather than one-at-a-time priority-lane work. Note
the overlap with two other filings on the same vocabulary: the closed-paradigm cross-reference gap
([Tooling 57](tooling-backlog.md#57-check_semantic_clusterspy-has-no-closed-paradigm-symmetry-rule))
and the weekday USAGE-section batch above. **All three are the same ~20 entries** and would be
cheaper as one pass than as three.

## Prohibitive sentence-final な has no entry and cannot be queued as a candidate

**Source**: 2026-08-01 routine polish run (06737).

The prohibitive な (⟦{言|い}うな⟧ — "don't say it") is a real gap: high-frequency, distinctly
learner-relevant, and absent from the dictionary. It cannot currently be added to the queue
because `manage_candidates.py` refuses the candidate — `09497_na` (attributive copula な) already
occupies the (surface, reading) key. It was marked `noentry` in 06737, which is the correct
local treatment.

This is [Tooling 41](tooling-backlog.md#41-manage_candidatespy-cannot-queue-a-homograph--the-duplicate-check-is-surface-reading-not-surface-reading-sense)
(sense-keyed duplicate checking) showing up on the *candidate* path rather than the entry path,
and it is the cleanest concrete example that item has: a genuine gap the tooling actively prevents
anyone from recording. Until it is fixed, the entry has to be created directly rather than via a
candidate.

## Checked and clear: the 義-family invented address forms

The same 2026-08-01 run corrected 06724/06725, which documented 「{義|ぎ}のお{母|かあ}さん」/
「{義|ぎ}のお{父|とう}さん」 — not standard Japanese — to 「{義理|ぎり}のお{母|かあ}さん」/
「{義理|ぎり}のお{父|とう}さん」, and flagged that other 義-family entries from the same creation
batch might carry the same invented form. **Measured 2026-08-02: zero remaining occurrences of
`{義|ぎ}の` anywhere in the corpus.** The concern is closed; recorded here so it is not
re-investigated a third time.

## 06742 告白: a removed collocation that may have had a real word behind it

**Source**: 2026-08-02 routine polish run (frontier 06739–06744).

The notes listed `{告白|こくはく}{記|き}` as a collocation. 告白記 is not a standard word, so the
run removed it rather than trying to repair it — the right call for a frontier pass that cannot
research each item. But the shape suggests a mistyped real compound: **告白文** (a written
confession/statement) and **告白録** (a confessional memoir, the usual translation of
*Confessions*) are both plausible intents, and 録 in particular is easy to lose. Worth one
second opinion; if either is right the collocation should come back with the correct kanji, and
if neither is, this note closes the question.

## 04477 大皿: inline link whose base label and target are different words

**Source**: 2026-08-02 routine polish run.

The entry carries `→得：07739_otoku` — the base form is labelled 得 but the target is the お得
entry. Either the label should be お得 (matching the target) or the target should be
`12563_toku` (matching the label); which one depends on what the example sentence actually says.
A concrete instance of the class
[Tooling 65](tooling-backlog.md#65-validatepy-accepts-an-inline-link-whose-base-form-contradicts-its-target)
proposes to catch at validation time, and one that `check_link_baseform.py` should already
surface today.

## 24314 等身: the headword may be a bound morpheme

**Source**: 2026-08-03 routine accuracy-review run (23908–24500 window).

等身 is effectively bound in modern Japanese — every natural example the reviewing run could
construct used 等身大 (life-size), not bare 等身. The run added an example containing the bare
headword so the entry is not self-contradictory, but flagged the real question for the curator:
**should the entry live at 等身大?**

This is a **headword change, so it is not Routine work** — the five-digit ID is part of the live
URL and the romaji is part of the filename, so moving the headword means either a new entry plus
a redirect-by-cross-reference, or an accepted URL change. Related in kind to the 29452 猿人 reading
correction (resolved 2026-06-26), but that one was caught before the entry had been indexed for
long; this one has been live since April.

## 07994 陳謝: off-vocabulary semantic tags

**Source**: 2026-08-02 routine polish run, which spotted `apology` and `official` in
`tags.semantic` while working a different range and correctly left them alone rather than reaching
outside its own range.

Both labels are outside `VALID_SEMANTIC`. This is an instance of
[Cleanup P20](cleanup-backlog.md#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration),
recorded here only so the ID is not lost — `apology` is a context-dependent label with no forced
rename (the drop-vs-migrate rule says drop it), while `official` most plausibly maps to `formal`
register rather than a semantic tag at all. It should be swept with the surrounding block rather
than fixed alone.

## 17662 格安SIM: a literal `\n` inside the notes field

**Source**: 2026-08-04 wiki harvest, measuring a 2026-08-03 polish run's warning that notes
rewritten programmatically can store `"\\n"` (backslash + n) where a newline was meant.

**Scope: exactly one entry in 30,187.** `17662_kakuyasushimu` has it in the COMMON COLLOCATIONS
block, one bullet in:

```
- {格安|かくやす}SIMに{乗|の}り{換|か}える: to switch to a budget SIM\n- {格安|かくやす}SIMを{契約|けいやく}する: …
```

The two collocation bullets therefore render as one run-on line with a visible `\n` between them.
The fix is a single character: replace the literal `\n` with a real newline. `validate.py` cannot
see it — a literal backslash-n is a valid JSON string — which is why it is filed as a permanent
cheap guard in [Tooling Backlog item 74](tooling-backlog.md#74-check_consistencypy-literal-n-stored-in-a-notes-field)
rather than as a sweep.

## 03654 豊か: an inline link with no correct target

**Source**: 2026-08-04 systemic-fix run (link-target-baseform batch 4), which stopped rather than
guess.

`03654_yutaka` example [3] uses `{採|と}れる` in the "to be harvested / to be gathered" sense but
links base 取れる to `00565_toru` (取る "to take"). The detector proposed `02376_toreru` (取れる
"to come off"). **Neither fits**: the harvest sense of 採れる is a third word that the dictionary
does not currently have an entry for. The honest resolutions are (a) rewrite the link to `noentry`
and add 採れる as a candidate, or (b) create the entry and link it — the pattern the 2026-08-03
harvest recorded for exactly this situation (see Tooling 59's update: *when the correct word has
no entry and the same-kanji entry would mislead, rewrite to `noentry` and add a candidate, do not
find a less-wrong target*). Left for the curator because 採れる may deserve its own entry.

## 30380 使いやすい: a cross-reference with no `target_id`

**Source**: 2026-08-04 routine polish run.

`30380_tsukaiyasui` carries a `cross_references` entry for 使いにくい with the `target_id` field
absent — `validate.py` reports it as a note rather than an error (the schema gap written up in
[Tooling 51](tooling-backlog.md#51-a-cross-reference-with-no-target_id-validates-cleanly--but-the-obvious-schema-fix-would-break-59-intentional-refs)),
so it renders as an unlinked label.

Self-resolving: the run added 使いにくい to the candidate list, and the ref becomes valid the
moment that entry exists. Filed so that whoever creates 使いにくい knows to come back and fill in
the `target_id` — and as one more instance of the pattern that makes 51's "intentional
target-less ref" population hard to separate from the accidental one.

## 00486 年: no sense-1 example uses the headword on its own

**Source**: 2026-08-05 routine polish run (notes-priority lane).

`00486_toshi` 年 is a basic-tier entry, and its sense-1 examples (ex1–ex3) illustrate 今年, 去年
and 来年 — compounds that each have their own entry. The headword never appears standalone in a
sense-1 example, so the entry teaches its own compounds instead of itself.

The fix is one added example using 年 alone (年を取る is the obvious candidate, or a counting use:
三年前). Worth doing carefully because this is a basic-tier, high-traffic entry, and worth noting
as a shape: an entry whose examples are all *compounds containing* the headword is a defect the
example-count checks cannot see, and one that would be mechanically detectable for
single-character noun headwords.

## 26031 {格上|かくじょう} — an entry built on a reading that does not exist (curator, URL-changing)

**Source**: 2026-08-05 routine accuracy-review (25872–26188); already escalated by that run to
`reviews/needs_curator.txt`.

The headword reading is wrong in a way that cannot be patched in place. 格上 is **かくうえ**;
格上げ is **かくあげ**. This entry's ID encodes かくじょう, its gloss and all three examples are
actually 格上げ, and they carry the furigana かくじょうげ — a reading of a word that does not
exist. It also duplicates two entries that are already correct: **07405 格上 / かくうえ** and
**13122 格上げ / かくあげ**.

Every honest repair (fix the reading, or merge into 13122) changes the filename and therefore the
live URL, which CLAUDE.md reserves to the curator. Recorded here so the next reviewer that reaches
this range does not re-derive it. Note the shape for the ratchet pile: **a five-digit ID is a
promise about the reading**, and nothing currently checks that `id`'s romaji agrees with
`reading`.

## 04230_uchiakeru — an etymology note whose component gloss has no correct target

**Source**: 2026-08-05 routine polish.

The notes derive 打ち明ける from 打つ + 明ける and gloss the second component as "(to open)".
Neither existing entry supports that: **00563_akeru is 開ける** "to open", **21288_akeru is 明ける**
"to dawn; to end (a period)". The link currently points at 00563, which matches the English gloss
but the wrong kanji; pointing it at 21288 matches the kanji but contradicts the gloss the note
itself wrote.

The real issue is the note, not the link: in 打ち明ける the 明 component carries a "reveal / bring
into the open" sense that neither entry heads. Either rewrite the etymology to say so without
claiming it is the entry 明ける, or drop the component gloss. A curator call because it is a
content decision, not a link repair.

## 02918_toki ({時|とき}) & 10077_toki (とき) — near-duplicate entries for the same word

**Source**: 2026-08-05 routine systemic-fix (`check_link_baseform.py` batch).

Two entries for とき differing only in whether the headword is written in kanji. Consolidation
candidate for `prompts/consolidate_entries.md`, with the usual "keep the lower ID, redirect the
links" default.

Worth recording *how it surfaced*, because that is the more useful part: the pair is the sole
cause of the one remaining "ambiguous" finding in `check_link_baseform.py`
(05020_youtsuu's 持ち上げたとき). That finding is not a link error at all — it is this duplication
seen from the link side. **A detector's residual ambiguity bucket can be a symptom of a data
defect rather than a limit of the detector.**

## Missing hundreds: 二百 … 九百 (五百 has an entry, its eight siblings do not)

**Source**: 2026-08-05 routine polish (00780).

12738 covers 五百; 二百/三百/四百/六百/七百/八百/九百 have no entries, so 00780's SOUND CHANGES
list mixes one live link with eight `noentry` markers — which is exactly the shape that later gets
refiled as a stale-`noentry` finding ([P35](cleanup-backlog.md#priority-35-stale-noentry-inline-links--3797-markers-now-resolve-2887-mechanically)).
This is a **decision, not a task**: either the hundreds are in scope (in which case eight entries
close it permanently, and they are among the cheapest entries the project could create, since the
sound changes are the entire content) or they are out of scope, in which case the exclusion should
be written down somewhere the next run will find it. What should not happen is a third run
rediscovering the asymmetry. Related: [Cleanup P35](cleanup-backlog.md), and the number/date
cluster its 2026-08-03 update describes.

## Added 2026-08-07 (wiki harvest)

**01385 気持ち / 02485 気持ち — refiled.** Two entries, same headword, same gloss ("feeling,
mood"). This pair was first filed in the 2026-06-10 harvest and has now been reported again by a
2026-08-06 polish run, which means it survived two months and at least one
`find_merge_candidates.py` pass. It belongs with the `entry-pair-consolidation` queue item
rather than here — the item is a *decision* the curator has not made, not a task waiting for
someone to notice it. Adding **02586 巨大 / 25544 巨大な** to that item's list as well: it is the
same one-word-two-entries shape, and it is also the source of a
`check_link_baseform.py` false-positive class ([Tooling 83](tooling-backlog.md)).

**Fixed in the run that found them** (recorded so a future run does not refile them):

- **00897 店員** — the note linked 店長 to `07537_tenchou`, which is 転調 "modulation (in
  music)": a live link to the wrong word, not a missing one. Corrected to `noentry` and 店長
  added as a candidate. The class is now [Tooling 78](tooling-backlog.md) shape 1.
- **00445 開放的 / 02627 外交的な** — the adjectival suffix 〜的 linked to `03546_teki` 敵
  "enemy" instead of `09839_teki` 〜的. Repaired; the class is [Tooling 78](tooling-backlog.md)
  shape 2.
- **06809 下味** — sole `semantic: ["general"]`, retagged `["cooking","food"]`.
- **03654 豊か** — the 採れる link had sat deferred through two `systemic-fix` batches because
  two candidate targets (取る, `02376_toreru`) were compared against each other and neither fit.
  The answer was a *third* entry nobody had searched for: **20862 採る**. Worth keeping as a
  worked example — when both the declared target and the detector's proposal are wrong, the
  answer is usually a fourth entry rather than `noentry`.

## Added 2026-08-08 (wiki harvest)

### The five furigana wrappers whose reading does not match the wrapped kana

A 2026-08-07 accuracy-review run found `27447` carrying `{弟|おとうと}{さん|くん}` — ruby くん over
the kana さん, where the intended text was 弟くん — and proposed tightening
`check_furigana_format.py` to separate "kana wrapped with its own reading" (cosmetic) from
"kana wrapped with a *different* reading" (a real content error). **Measured: the second class
is 5 instances corpus-wide** (against 339 cosmetic), and 27447 is not among them because that
run fixed it. A five-item list is a fix-on-sight batch, not a detector — and the five are not
even one class:

| Entry | Instance | What it actually is |
|---|---|---|
| 23394 `二枚貝` | `{カキ\|がき}` | Oyster かき given the rendaku form がき, stranded from a compound |
| 28929 `苦悶` | `{に\|み}` | **A dropped kanji**: 苦悶に満ちた声 lost the 満 from `{満\|み}ちた` |
| 00961 `ここ` | `{どこ\|}` | Empty reading slot |
| 23799 `野宿` | `{キャンプ\|}` | Empty reading slot |
| 25376 `循環する` | `{うまく\|}` | Empty reading slot |

The proposed detector category would have **mislabelled the most serious one**: 28929 is not a
mis-wrapped kana at all but a kanji deletion that happens to leave a well-formed-looking
wrapper behind. Three of the remaining four are a third shape — `{X|}`, empty after the pipe —
which is the degenerate form the [P9 update of 2026-06-20](cleanup-backlog.md) flagged as an
open question about whether the detector sees it. It does not, and at scope 3 it does not need
to.

### 00823_wakai / 01525_wakai — 若い held by two entries

Both entries have headword `{若|わか}い`, reading わかい, and the gloss "young". Surfaced twice
independently by 2026-08-07 polish runs, both times via `word_id_lookup.json` returning two
identical-looking hits while linking a frontier entry. Note the pair is already implicated
elsewhere on this page's sibling analysis: `01525_wakai` is the entry
[Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) records as **missing its
i-adjective conjugation table** because `{若い|わかい}` over-wraps the okurigana and
`add_adjective_conjugations.py` cannot extract the stem. Whichever entry survives
consolidation, the surviving headword must be `{若|わか}い` or the conjugation table will still
not generate. Candidate for `consolidate_entries.md` / `resolve-duplicates`; add to the
`entry-pair-consolidation` queue item.

### 02005_nikui / 02458_nikui — にくい held by two entries

Same shape, found in the same run: both glossed "hard to ~, difficult to ~". Add to
`entry-pair-consolidation`.

### 30493 {百十番|ひゃくとおばん} — a figure-form headword written in kanji

Created by a 2026-08-07 new-entries run because `01393_keisatsu` referenced it as
`⟦{百十番|ひゃくとおばん}→百十番：noentry⟧`. The standard orthography is **110番**. The entry and the
inline link have to be revisited together — and the underlying question is the curator's, not
a polish run's: **does the dictionary admit figure-form headwords at all?** It bears directly
on the number+counter scope question already routed to the curator (C22795 三十人), because
both are asking when a numeral-containing string is entry-worthy and in what orthography.

## Added 2026-08-08 (wiki harvest, run 2)

**28655 `{高層建|こうそうだ}て` — two model passes read the headword differently, and the entry
now hedges.** An accuracy-review run got directly contradictory readings from two passes: the
construction *style* versus the *building itself*. The gloss was rewritten to cover both and the
entry escalated to `reviews/needs_curator.txt`. Recorded here as well because the hedge is a
holding action, not a resolution — the headword segmentation itself
(`{高層建|こうそうだ}て` for 高層建て) is the thing to check first, since a wrapper spanning
高層建 as a unit is unusual and may be what confused both passes.

**The proper-noun scope question now has corpus evidence against the standing policy — third
filing.** A curator note holds that "the dictionary holds no person or place names", and
new-entries runs use it to reject candidates. The 2026-08-08 accuracy-review found the corpus
disagrees: **28138 {横浜|よこはま}, 28139 {札幌|さっぽろ}, 28144 オーストラリア,
28145 {青森県|あおもりけん}, 28283 イギリス, 28300 {中国|ちゅうごく}** are all live entries, and
all six carried off-vocabulary `place-name`/`country` tags (migrated to `geography` in-run).
Place names are therefore *in* the dictionary in practice while the policy says they are not.
Two candidates are blocked on this and have been re-picked by successive runs: **C22806 夏目漱石**
(personal name) and **C22820 成田**. The policy and the corpus need to be reconciled in one
direction or the other; until then every new-entries run re-litigates it. **C22851 画期** is a
separate and easier call — a bound morpheme occurring only in 画期的, which already exists as
06826, so it should simply be dropped from the candidate list.

**06830 {劇的|げきてき} — fixed in-run, but check its siblings.** The entry carried
`domain: ["medical"]` although only one of its four examples is medical and the word is
general-register; the tag was dropped. The shape is single-example contamination, identical to
the P11 semantic drift, and `〜的` adjectives are a plausible cohort for it — they take their
examples from whatever field the base noun suggests. See
[Cleanup Backlog → Updates 2026-08-08 run 2](cleanup-backlog.md#updates-2026-08-08-wiki-harvest-run-2)
for the corpus-wide `domain` measurement this belongs to.

## 2026-08-09 (wiki harvest)

**04262 {擦|こす}る — `vocabulary_tier: basic` is almost certainly a mislabel.** 擦る (to rub,
to scrub) is not plausibly a member of the closed ~800-word basic tier. The tier lists are
closed and must not be edited casually, so this is a **tier-audit item, not a polish fix**: it
belongs in the next `audit_vocabulary_tiers.md` pass, which produces a report rather than
changing entries. Flagged by the 2026-08-09 polish run, which correctly left it alone.

**02992 {色|いろ}んな — the POS is wrong in a way the schema has no slot for.** The entry's
`part_of_speech` is "adjectival noun" and its `pos` tags were `adjective-na` + `noun`, but
色んな is a **連体詞** (pre-nominal adjectival): it modifies nouns directly and cannot be a
predicate. *The entry's own notes say so.* The 2026-08-09 polish run removed the `noun` tag,
which is unambiguous, and correctly stopped there — the remaining question is whether the
project should have a 連体詞 category at all, which is a curator call with dictionary-wide
consequences (こんな/そんな/あんな/大きな/小さな and the ある/あらゆる set are the same class).
Until then `adjective-na` is a compromise that mislabels the predicate behaviour of every member.

**00806 {両親|りょうしん} — fixed in-run, and it names a class.** The entry was tagged
`formality: formal` + `politeness: honorific`; the honorific form is ご両親, while 両親 itself
is the plain word. The 2026-08-09 polish run fixed it and suggested other family terms may
carry the same drift. **Measured**: 16 noun entries are tagged honorific/humble without an
お/ご prefix and without a gloss that says so —
`03189_riyousha` 利用者 "user, customer" (honorific), `01454_sonkei` 尊敬 "respect, esteem"
(honorific), `04142_kenson` 謙遜 "modesty" (humble), `07430_haiguusha` 配偶者 "spouse" (humble),
`03147_busata` 無沙汰, `04987_chazuke` 茶漬け, `07059_haikanryou` 拝観料, `15316_futoku` 不徳,
`27410_kouhai` 高配, `27411_hikitate` 引き立て, `00987_shujin` 主人, `01902_ousama` 王様,
`02853_okusan` 奥さん, `03597_fujin` 夫人, `14566_heika` 陛下, `23324_sunshi` 寸志.

The list is **not** a fix list — several are correct (陛下, 閣下, 寸志, 高配 and 引き立て are
genuinely deferential in use). The four at the top are the 両親 error repeated: a word whose
*meaning* is deference tagged as a word whose *use* is deferential. Needs per-entry judgment;
sizing and rationale in
[Cleanup Backlog → Updates 2026-08-09](cleanup-backlog.md#updates-2026-08-09-wiki-harvest).

**06844 {切|き}り{崩|くず}す — parked deliberately, and the next polish run should expect it.**
15 examples and a full notes block with **zero** inline-link coverage, too large to link inside
one polish run's budget alongside other entries. The 2026-08-09 run left the frontier cursor at
06844 so the next `polish` run can spend most of its frontier budget on this single entry. The
entry's *content* is good (3 senses, well distributed) — this is a linking cost, not a quality
problem. It is also a member of [Cleanup P50](cleanup-backlog.md#priority-50-zero-links-anywhere-behind-the-frontier-55-entries--the-other-half-of-p46).

**Proper-noun scope — fourth filing, now with a fresh candidate.** C22806 夏目漱石 was captured
again by the 2026-08-09 polish run ("seen in entry 06801") and left in the candidate list
pending the curator's decision. Nothing new to add to the argument above; recording the repeat
because the re-capture rate is itself the point — every polishing run that meets a proper noun
in an example will keep filing one until the policy and the corpus agree.

## Added 2026-08-10 (wiki harvest)

**01328 {内|うち} — two examples use the entry against its own advice.** ex13
「{建物|たてもの}の{内|うち}は{涼|すず}しかったです」 and ex17
「{箱|はこ}の{内|うち}に{何|なに}が{入|はい}っていますか」 both use 内 for a concrete physical
interior, where natural Japanese takes ⟦{中|なか}⟧ — and the entry's **own notes say so**
("for physical interiors, 中 is more common"). An example that a learner would be marked wrong
for imitating, sitting under a note explaining why. Fix: replace both with sense-1 uses —
abstract or bounded-set interiors such as {心|こころ}の{内|うち} or {予算|よさん}の{内|うち} —
with full inline-link coverage on the replacements. Needs a small rewrite rather than a tweak,
which is why it is here rather than fixed in passing.

**The conflict/dispute cluster — three entries left deliberately for one decision.** 05758 紛争
was tagged `action` and was corrected to `society`/`politics` in the 2026-08-10 polish run. Its
neighbours are no better: **01450 戦争** `action`, **04500 対立** `general`, **09992 争い**
`general`. `action` on an abstract noun is exactly the semantic-mismatch failure
`build/check_tag_drift.py` detects, and sole `general` is its sole-general check, so the whole
cluster is already visible to existing instruments. They were left for a systemic-fix pass so
the four get **one consistent decision** rather than four independent guesses months apart —
which is the right instinct and worth generalising: near-synonym clusters should be retagged
together or not at all.

**Transitive/intransitive leakage in the 06850s compound-verb block.** 06853 {焼|や}き{付|つ}ける
had its ex1 written with the *intransitive* 焼き付いている under a transitive headword; the
2026-08-10 polish run rewrote it and added the missing `pair` link to 26882 焼き付く in both
directions. The block is full of transitive/intransitive compound pairs created in the same
batch, so the same leak plausibly sits in its neighbours. **Targeted check**: examples whose
verb form does not match the headword's transitivity — mechanically approximable by looking for
自動詞-shaped inflections (〜が … 〜ている with no を) in entries tagged transitive, then verifying
per entry.

**Sole-`general` on obviously-specific words — the curator question behind a recurring reject.**
The standing §A policy rejects "sole `general` → specific tag" flags, and this window rejected
40 of them (27% of all tag-flag volume, the third consecutive window at roughly that share). The
policy is defensible, but the examples make the opposite case honestly: {湿疹|しっしん} (eczema)
and {音符|おんぷ} (musical note) carry sole `general` when `medicine` and `music` are sitting
right there in the vocabulary. Either the reviewer is wrong 40 times a sweep, or these entries
should be retagged and the policy narrowed to genuinely-unclassifiable words. Recorded here as
an entry-level question with a concrete two-entry starting sample; the tooling consequence is
[Tooling 95](tooling-backlog.md).

**Proper-noun scope — fifth filing.** C22806 夏目漱石 was re-captured by the 2026-08-10
new-entries run and skipped again, with the reasoning restated independently: the dictionary has
place names (東京, 富士山, 大阪) and award names (芥川賞) but no person names, so admitting an
author name is a scope decision rather than an entry decision. Nothing new in the argument. The
re-filing rate is now roughly one per two days.

## Added 2026-08-11 (wiki harvest)

**Proper-noun scope — RESOLVED, and the thread closes.** The curator ruled on 2026-08-11 that
proper nouns are in scope (place / person / organization / work / event / brand names, with
collocationally and semantically rich ones prioritized), tagged `proper-noun` plus a type tag,
as ordinary entries under the existing schema. **C22806 夏目漱石 no longer needs a ruling** and
can be created by any `new-entries` run that reaches it. This was the sixth filing of the same
question across five sessions; see [open issues](../project/open-issues.md#proper-names-and-encyclopedic-entries)
and [vocabulary tiers](../project/vocabulary-tiers.md) for the decision as recorded.

**03515 {日光|にっこう} — add the place sense (Nikko).** The entry covers only "sunlight". The
place name cannot be routed through the candidate queue at all, because
`check_duplicate.py` sees an exact word+reading match against this entry and rejects it. With
proper nouns now in scope, the fix is a **second sense on the existing entry** rather than a
second entry: sunlight (common noun) + Nikko, the city in Tochigi (proper noun), with
`proper-noun` + `place-name` on the sense's tags and examples showing the usual collocations
(日光に行く, 日光東照宮). Worth doing during polish rather than as a special task; it is the
template case for every future proper-noun/common-noun homograph collision.

**09497_na needs a prohibitive sense — or the duplicate checker needs a way to say "same
surface, different word".** The sentence-final prohibitive な (「{言|い}うな」 "don't say") has
no entry and, as things stand, **cannot be given one**:
`manage_candidates.py check "な" "な"` reports an exact duplicate against 09497_na, the
na-adjective attributive copula, which occupies the same surface and the same reading while
being an entirely different morpheme. The practical consequence is that every prohibitive な in
an example has to be marked `noentry` with no candidate trail behind it — a defect that is
invisible because the marker looks like an ordinary not-yet-created word. Seen in 01674.

Two possible fixes, and they are not equivalent: add a second sense to 09497_na (cheap,
slightly dishonest — these are unrelated morphemes that a learner should not see grouped), or
create a separate entry and give `check_duplicate.py` an override for genuine homographs
(correct, and needed anyway — 日光 above is the same problem wearing different clothes). The
second is the better investment because the class is now known to have at least two members and
the proper-noun decision guarantees more.

## Added 2026-08-13 (wiki harvest)

### 08989 車席 — probably not a word

The 2026-08-12 accuracy-review's reviewer flagged this headword **five times** as not a real
Japanese word, and the entry undermines itself: its own notes give 助手席 and 後部座席 as the
ordinary terms, while its examples invent 助手車席 and 後部車席 to use the headword. The run
escalated rather than deleting, correctly — deletion retires a live URL — and it is in
`reviews/needs_curator.txt`. **This needs a curator decision, not another run's opinion**; the
evidence is unlikely to get better with a fourth reading.

### 08985 日日 — wrong orthography for ひにち

The headword is 日日 with reading ひにち. The ordinary modern spelling is 日にち; 日日 normally
reads ひび ("day after day"). The 2026-08-12 accuracy-review tightened the gloss and left the
orthography alone, on the reasoning that changing a headword deserves the same care as a
deletion. Filed rather than fixed for the same reason.

### 17576_suriyoru — rare orthography as the headword

The entry heads with {摺|す}り{寄|よ}る. 擦り寄る is the far more common modern spelling, and the
entry's KANJI NOTE mentions the hiragana form but not this variant. Found by the 2026-08-13
new-entries run when 擦り寄る arrived as a candidate and duplicate-checking reported only
"homophones exist" (see Tooling 112). Headword/variant review.

### 06899 顔を出す — the top-level gloss covers only sense 1

The entry has two senses, the second ("to peek out", of the sun or a landmark) carrying three
examples, but the top-level `gloss` advertises only sense 1. The `definitions` list both. The
2026-08-12 polish run left it, noting that the convention for two-sense idioms — does the
top-level gloss summarise all senses or lead with the dominant one? — is worth a ruling before
entries start being edited toward one answer. **This is a convention question first and an entry
fix second**; if the ruling is "summarise all senses", it becomes a sweep rather than a
follow-up.

### 00743 音 — kept at sole-`general` for want of a tag

A 2026-08-13 polish run left 音's semantic tag as `general` because `VALID_SEMANTIC` has no
sound or perception tag. Same for 物音 (03633), 騒音 (03315), 足音 (02991). Revisit if the
curator adds one — see the ruling request in
[Cleanup Backlog](cleanup-backlog.md#updates-2026-08-13-wiki-harvest).

## Added 2026-08-12 (wiki harvest)

### 28358_buri — the manner/style sense belongs in the existing entry, not a new one

The 2026-08-12 new-entries run reached candidate C23011 (ぶり, "suffix: manner or style of doing
something", as in {仕事|しごと}ぶり) and correctly declined to create it: `28358_buri` already
holds the headword 〜ぶり, but covers only the time-interval sense ("for the first time in
[period]"). The manner/style sense is a second sense of the same suffix, so it belongs in 28358.
C23011 was left in the candidate queue, which means the next new-entries run will meet the same
decision unless the entry is extended first — the queue has no way to say "this word exists but
one of its senses does not."

That gap is worth noting beyond this row: it is the same shape as the 03515 日光 follow-up filed
2026-08-11 (add the Nikko sense to the existing entry rather than create a second one). Two
instances now of a candidate that is *real*, *not a duplicate entry*, and *not creatable* —
`check_duplicate.py` reports the headword as taken, which is true and not the relevant fact.

### 06886 haragatatsu — malformed derived form, and the spot-check it asks for

The entry's notes gave the adjective form as 腹が立たしい, which is not a word; corrected to
腹立たしい (21455) by the 2026-08-12 polish run. The run asked for a spot-check of sibling idiom
entries for similarly malformed derived forms. Not measured this harvest — the check needs to
read each entry's notes prose to find claimed derived forms, which no existing detector does, and
the natural moment for it is the frontier lane's pass over 06896–06980 (the
`inline-link-block-06800-07100` queue item; the "P56" in the original filing was a forward
reference to an item that was never created — P56 is now the idiom/body-part cross-reference
gap), which is
the same creation cohort and is about to be read entry-by-entry anyway.

### 00823_wakai / 01525_wakai — second filing of the same duplicate

Re-filed by the 2026-08-12 polish run: both entries are 若い / わかい, i-adjective, glossed
"young" (one basic tier, one core), and 01525's headword carries a malformed wrapper
`{若い|わかい}` where it should be `{若|わか}い`. This is already on this page under
"Added 2026-08-08", where it was filed with the same two facts.

Recording the re-filing rather than merging it silently, because the cost is now measurable: a
duplicate that a polish run meets in the priority lane will be re-reported every time the lane
reaches it, and each report costs a run's attention plus a harvest's. Consolidations need an
owner — they are explicitly out of scope for polish sessions (`consolidate-entries` is a
separate task), so a polish run can only ever file them. Three consolidation follow-ups are now
open on this page (悪口, 中火, 若い) plus 02005/02458 にくい.

### Era names (平安時代, 鎌倉時代, 室町時代, 大正時代) — filed as `event-name` for want of a fit

The 2026-08-11 candidates run found no clean category in the find-candidates proper-noun scheme
for historical periods — "neither place, person, organization, work, nor really `event`" — and
filed them as `event-name`.

Checked against `VALID_SEMANTIC`: `event-name`, `time-period`, `history`, and `proper-noun` are
all in the list. So the vocabulary already contains a better fit than the one the run settled
for, and no new tag is needed: **`time-period` + `proper-noun`**, optionally with `history`, says
what an era name is — a named span of time — where `event-name` says it is a happening, which a
250-year period is not. A ruling has to come from the `find-candidates` skill, which this session
cannot edit; recorded here and routed to the curator. Worth settling before the next candidates
run, since that run's own measurement puts proper nouns at ~80% survival against ~10–28% for
common vocabulary, so era names will keep arriving.

## Related pages

- [Cleanup Backlog](cleanup-backlog.md) — systemic patterns
- [Tooling Backlog](tooling-backlog.md) — tool improvements
- [Content Pipeline](../project/content-pipeline.md) — polishing workflow
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis covering several of these
