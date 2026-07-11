# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-07-11
**Current phase**: Phase 6 - Continued Expansion & Polish

**Live site**: https://www.tkgje.jp/

> **Full history**: Older change logs are archived in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
> **Quick reference**: See [PROJECT_CONTEXT_BRIEF.md](PROJECT_CONTEXT_BRIEF.md) for a concise session-start overview.
> **Project setup**: See [CLAUDE.md](CLAUDE.md) for commands, file placement, and skills.

## Current State

**Phase 6: Continued Expansion & Polish** — Adding vocabulary while maintaining v2 quality standards, with an automated pipeline for batch maintenance tasks. The dictionary uses an original three-tier vocabulary classification (basic, core, general) instead of JLPT levels.

### Content Status

These counts are approximate. Run `make report` for accurate, up-to-date numbers.

| Metric | Value |
|--------|-------|
| Total entries | ~19,088 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,289 (open) |
| Candidate words | ~5,472 |
| Cross-references | ~3,400 |
| Example sentences | ~53,200 |
| Audio files | 1,028 |

## v2 Quality Standards

Based on multi-model LLM evaluation (Claude Haiku 4.5, GPT-5.2, Gemini 3 Flash), these are the priority enhancements:

### HIGH PRIORITY
1. **Verb transitivity** - Add 自動詞/他動詞 and pair verbs to all verb entries
2. **Aspect notes** - Explain ている behavior for verbs with non-obvious meanings
3. **Particle predicate lists** - List verbs/adjectives requiring each particle
4. **Collocation patterns** - Add common noun-verb pairings

### MEDIUM PRIORITY
1. **Register labels** - Mark casual/neutral/formal for all entries
2. **Similar words** - Add contrastive sections for semantic neighbors
3. **Adjective forms** - Add adverbial (〜く/〜に) and noun forms (〜さ)
4. **Example progression** - Ensure simple → complex ordering

### LOW PRIORITY
1. **Kanji orthography notes** - When to use kanji vs. hiragana
2. **Cultural notes** - Expand where significant
3. **Keigo references** - Link to honorific forms

## Recent Changes

### 2026-07-11 (Routine v2: new-entries — 18 New Entries, IDs 29774–29791)
Created 18 general-tier entries. The **10 "seen in entry" candidates** (C22290–C22299, cited from entries 06449–06452 and 29763/29766/29773) were created first — internal-completeness gaps referenced by existing entries: {御令嬢|ごれいじょう} (your daughter; honorific, female counterpart of the just-added {御令息|ごれいそく}), {冷媒|れいばい} (refrigerant), {濃墨|こずみ} (dark sumi ink; counterpart of {薄墨|うすずみ}), {終末|しゅうまつ} (end; demise), {承諾書|しょうだくしょ} (letter of consent), {実用化|じつようか} (putting into practical use; suru), {移動手段|いどうしゅだん} (means of transportation), センサー (sensor), {唐傘|からかさ} (traditional oiled-paper umbrella), {写真撮影|しゃしんさつえい} (photography; suru). This **cleared the seen-in-entry queue**. The remaining 8 are hand-picked genuine standalone lexemes from the general pool: {電磁気学|でんじきがく} (electromagnetism), {好気性|こうきせい} (aerobic; noun + adjective-no), {腋窩|えきか} (armpit; anatomical), {分泌腺|ぶんぴつせん} (secretory gland), {非該当|ひがいとう} (not applicable), {党大会|とうたいかい} (party convention), {数量化|すうりょうか} (quantification; suru), {装丁家|そうていか} (book designer). Conjugation tables added to the 3 new suru-verbs; no i-adjectives. Two new kanji ({腋}, {窩}) assigned IDs 02782/02783. §4 cross-model self-check on all 18 changed entries: **fully clean — 0 flagged, 0 applied, 0 rejected**. $0.0078. The non-"seen in entry" candidate tail remains heavily contaminated with compositional/derivable junk (~600 candidates surveyed to find the 8 standalone words); logged a `[pattern]` observation recommending a candidate-cleanup pass.

- **Seen-in-entry priority (10)**: {御令嬢|ごれいじょう} (your daughter; honorific), {冷媒|れいばい} (refrigerant), {濃墨|こずみ} (dark ink), {終末|しゅうまつ} (end; demise), {承諾書|しょうだくしょ} (letter of consent), {実用化|じつようか} (putting into practical use; suru), {移動手段|いどうしゅだん} (means of transportation), センサー (sensor), {唐傘|からかさ} (paper umbrella), {写真撮影|しゃしんさつえい} (photography; suru)
- **Technical/anatomy nouns (4)**: {電磁気学|でんじきがく} (electromagnetism), {好気性|こうきせい} (aerobic), {腋窩|えきか} (armpit; anatomical), {分泌腺|ぶんぴつせん} (secretory gland)
- **Topical/abstract nouns (4)**: {非該当|ひがいとう} (not applicable), {党大会|とうたいかい} (party convention), {数量化|すうりょうか} (quantification; suru), {装丁家|そうていか} (book designer)

### 2026-07-11 (Routine v2: new-entries — 12 New Entries, IDs 29762–29773)
Created 12 general-tier entries. The four highest-priority "seen in entry" candidates (C22286–C22289, cited from entries 06445/06447 — funeral-vocabulary and sports gaps) were created first: {関係性|かんけいせい} (relationship, relatedness), {薄墨|うすずみ} (pale sumi ink; funeral custom), {御仏前|ごぶつぜん} (before the Buddha; condolence-envelope inscription), ホームチーム (home team). The remaining eight are hand-picked genuine standalone lexemes from the general candidate pool: an honorific ({御令息|ごれいそく}), a math/figurative antonym pair ({低次元|ていじげん}/{高次元|こうじげん}, both noun + na-adjective, two senses each), and single-sense technical/topical nouns ({甜菜糖|てんさいとう} beet sugar, {網点|あみてん} halftone dot, {駆動軸|くどうじく} drive shaft, {地域研究|ちいきけんきゅう} area studies, {熱伝達|ねつでんたつ} heat transfer). No verbs/i-adjectives, so no conjugation tables; one new kanji ({甜|てん}) assigned ID 02781. §4 cross-model self-check on all 12 changed entries: **11 clean, 1 flagged — 1 applied, 1 rejected** — applied a 49th-day gloss-timing precision fix on {御仏前|ごぶつぜん} ("after"→"from"), rejected a "def gloss too restrictive" misread. $0.0053. Added {御令嬢|ごれいじょう}, {冷媒|れいばい}, {濃墨|こずみ} as referenced-but-missing candidates. The general candidate pool is heavily contaminated with compositional/derivable junk, so ~600 candidates were surveyed to find these; logged a `[pattern]` observation recommending a candidate-cleanup pass. The seen-in-entry queue is empty again.

- **Seen-in-entry priority (4)**: {関係性|かんけいせい} (relationship, relatedness), {薄墨|うすずみ} (pale ink; funeral custom), {御仏前|ごぶつぜん} (before the Buddha; condolence inscription), ホームチーム (home team)
- **Honorific / dimension pair (3)**: {御令息|ごれいそく} (your son; honorific), {低次元|ていじげん} (low-dimensional; petty), {高次元|こうじげん} (high-dimensional; high-level)
- **Technical / topical nouns (5)**: {甜菜糖|てんさいとう} (beet sugar), {網点|あみてん} (halftone dot), {駆動軸|くどうじく} (drive shaft), {地域研究|ちいきけんきゅう} (area studies), {熱伝達|ねつでんたつ} (heat transfer)

### 2026-07-10 (Routine v2: new-entries — 15 New Entries, IDs 29747–29761)
Created 15 general-tier entries, all from the high-priority "seen in entry" pool (candidates C22271–C22285, cited from entries 05775, 06438–06444, 29735, 29742, 29746) — internal-completeness gaps referenced by existing entries. This **cleared the entire remaining seen-in-entry queue** (15 candidates). Three clusters: weight-training/anatomy (バーベル, {鉄|てつ}アレイ, {上腕二頭筋|じょうわんにとうきん}, siblings of the existing ダンベル/エクササイズ fitness set, plus {加湿|かしつ}), streaming/social media (フィード, ネットショッピング, スーパーチャット + abbreviation スパチャ, マネージャー), and everyday nouns/mimetic (もごもご, ひび{割|わ}れ, {足|あし}の{甲|こう}, {仕訳|しわけ}, {大道芸人|だいどうげいにん}, ギターケース). Conjugation tables added to the 5 new suru-verbs; no i-adjectives, no new kanji. §4 cross-model self-check on all 15 changed entries: **fully clean — 0 flagged, 0 applied, 0 rejected**. $0.0065. No new candidates or observations captured (examples reuse existing vocabulary). The non-"seen in entry" candidate tail remains heavily contaminated, so no padding from the oldest queue; the seen-in-entry queue is empty again and awaits curator/polish restock.

- **Weight-training/anatomy (4)**: バーベル (barbell), {鉄|てつ}アレイ (dumbbell, traditional term), {上腕二頭筋|じょうわんにとうきん} (biceps), {加湿|かしつ} (humidification; suru)
- **Streaming/social media (5)**: フィード (feed), ネットショッピング (online shopping; suru), スーパーチャット (Super Chat), スパチャ (Super Chat; abbreviation; suru), マネージャー (manager)
- **Everyday nouns/mimetic (6)**: もごもご (mumbling; mimetic), ひび{割|わ}れ (crack; chapping), {足|あし}の{甲|こう} (instep), {仕訳|しわけ} (journal entry; accounting; suru), {大道芸人|だいどうげいにん} (street performer), ギターケース (guitar case)

### 2026-07-09 (Routine v2: new-entries — 12 New Entries, IDs 29735–29746)
Created 12 general-tier entries, all from the high-priority "seen in entry" pool (candidates C22259–C22270, cited from entries 06433–06437 and 29724) — internal-completeness gaps referenced by existing entries. This **cleared the entire remaining seen-in-entry queue** (12 candidates). Two coherent clusters: a nuclear/hydro energy set ({調湿|ちょうしつ}, {再稼働|さいかどう}, {廃炉|はいろ}, {揚水|ようすい}, siblings of {原子力|げんしりょく}/{水力|すいりょく}) and an arm-anatomy/fitness set ({上腕|じょうわん}, {前腕|ぜんわん}, たるみ, エクササイズ, ダンベル, cited from {二|に}の{腕|うで} 06437), plus {乱舞|らんぶ} and {有頂天|うちょうてん}/{慨嘆|がいたん} (emotion siblings of {狂喜|きょうき}). Conjugation tables added to the 6 new suru-verbs; no i-adjectives, no new kanji. §4 cross-model self-check on all 12 changed entries: **fully clean — 0 flagged, 0 applied, 0 rejected**. $0.0052. Added バーベル, 加湿, 鉄アレイ, and 上腕二頭筋 as referenced-but-missing candidates. The non-"seen in entry" candidate tail remains heavily contaminated (transparent compounds, numeral+counter combos, phrase fragments, dubious coinages), so no padding from the oldest queue; logged a `[pattern]` observation.

- **Nuclear/hydro energy (4)**: {調湿|ちょうしつ} (humidity regulation; suru), {再稼働|さいかどう} (restart of a plant/reactor; suru), {廃炉|はいろ} (reactor decommissioning), {揚水|ようすい} (pumping water up; pumped storage; suru)
- **Arm anatomy/fitness (5)**: {上腕|じょうわん} (upper arm; anatomical), {前腕|ぜんわん} (forearm), たるみ (sagging; slack; flab), エクササイズ (exercise; workout; suru), ダンベル (dumbbell)
- **Emotion/movement (3)**: {乱舞|らんぶ} (wild dancing; whirling; suru), {有頂天|うちょうてん} (ecstasy; being on cloud nine), {慨嘆|がいたん} (lamentation; deploring; formal, suru)

### 2026-07-09 (Routine v2: new-entries — 15 New Entries, IDs 29720–29734)
Created 15 general-tier entries, all from the high-priority "seen in entry" pool (candidates C22244–C22258, cited from entries 06427–06432) — internal-completeness gaps referenced by existing entries in the energy/insulation and agriculture domains. This **cleared the entire remaining seen-in-entry queue** (15 candidates). Coherent clusters: home-insulation materials (グラスウール, ウレタンフォーム, セルロースファイバー, plus {遮熱|しゃねつ} and {冷暖房費|れいだんぼうひ}, siblings of {断熱|だんねつ}), agricultural water ({用水|ようすい}, {溜|た}め{池|いけ}, {水利|すいり}, siblings of {灌漑|かんがい}), crop/structural pests (シロアリ, アブラムシ, ウンカ, siblings of {害虫|がいちゅう}), and renewable-energy terms ({発電機|はつでんき}, {洋上|ようじょう}, クリーン). No verbs or i-adjectives, so no conjugation tables; no new kanji. §4 cross-model self-check on all 15 changed entries: **fully clean — 0 flagged, 0 applied, 0 rejected**. $0.0065. Added 調湿 (ちょうしつ) as a new candidate (referenced in a note but not yet an entry). The non-"seen in entry" candidate tail remains heavily contaminated (rare coinages, dubious readings, proper nouns), so no padding from the oldest queue.

- **Insulation/energy-saving (5)**: {冷暖房費|れいだんぼうひ} (heating and cooling costs), {遮熱|しゃねつ} (heat shielding), グラスウール (glass wool), ウレタンフォーム (urethane foam), セルロースファイバー (cellulose fiber)
- **Agricultural water (3)**: {用水|ようすい} (service/irrigation water), {溜|た}め{池|いけ} (reservoir pond), {水利|すいり} (water use/rights)
- **Pests (3)**: シロアリ (termite), アブラムシ (aphid), ウンカ (planthopper)
- **Health/energy (4)**: {伝染病|でんせんびょう} (infectious disease), {発電機|はつでんき} (generator), {洋上|ようじょう} (on the open sea; offshore), クリーン (clean; na-adjective)

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
