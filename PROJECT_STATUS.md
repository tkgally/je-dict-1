# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-07-03
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

### 2026-07-06 (Routine v2: new-entries — 13 New Entries, IDs 29707–29719)
Created 13 general-tier entries, all from the high-priority "seen in entry" pool (candidates C22231–C22243, cited from entries 05432, 06423, 06424, 06426) — internal-completeness gaps referenced by existing entries. This **cleared the entire remaining seen-in-entry queue** (13 candidates). Three coherent clusters: casual tag-question endings (じゃないか, やん), page-annotation terms ({頭注|とうちゅう}/{傍注|ぼうちゅう}/{巻末注|かんまつちゅう}/{後注|こうちゅう}, siblings of {脚注|きゃくちゅう}) plus source-citation nouns ({典拠|てんきょ}, {原典|げんてん}), and exterior/interior-wall materials ({内壁|ないへき}, サイディング, モルタル, タイル, siblings of {外壁|がいへき}). Conjugation table added to the 1 new ichidan verb ({剥|は}げる, intransitive; pair {剥|は}がす); no new kanji. §4 cross-model self-check on all 13 changed entries: **10 clean, 3 flagged; 0 applied, 3 rejected** — all three were identical in-list `general`→`building` breadth nits on the wall/material nouns, rejected per the semantic-tag policy (reject too-broad substitutions between in-list tags) and for consistency with the sibling {外壁|がいへき}/コンクリート entries, which also use `general`. $0.0056. The non-"seen in entry" candidate tail remains heavily contaminated (derived compounds, bare numerals/counters, mis-glossed items), so no padding from the oldest queue; logged a `[pattern]` observation.

- **Casual endings (2)**: じゃないか (isn't it?; tag-question, expression), やん (isn't it?; Kansai particle)
- **Annotation/citation (6)**: {頭注|とうちゅう} (headnote), {傍注|ぼうちゅう} (marginal note), {巻末注|かんまつちゅう} (endnote), {後注|こうちゅう} (endnote), {典拠|てんきょ} (documentary authority), {原典|げんてん} (original text)
- **Walls/materials (5)**: {内壁|ないへき} (interior wall), サイディング (siding), モルタル (mortar), タイル (tile), {剥|は}げる (to peel off; to fade; ichidan)

### 2026-07-06 (Routine v2: new-entries — 16 New Entries, IDs 29691–29706)
Created 16 general-tier entries, all from the high-priority "seen in entry" pool (candidates C22215–C22230, cited from entries 06411–06421 and 29684) — internal-completeness gaps referenced by existing entries. This **cleared the entire remaining seen-in-entry queue** (16 candidates). A tech / green-economy / childcare / dessert-baking cluster. Conjugation tables added to the 3 new suru-verbs (アシスト, リコール, {結婚活動|けっこんかつどう}); no new kanji. §4 cross-model self-check on all 16 changed entries: **fully clean — 0 flagged, 0 applied, 0 rejected**. $0.0070. The non-"seen in entry" candidate tail remains heavily contaminated (fabricated words, compositional compounds, bare counters), so no padding from the oldest queue.

- **Tech/robots (3)**: アンドロイド (android; human-like robot), ニュートラル (neutral; impartial; gear neutral; na-adj), インスタグラマー (Instagrammer)
- **Green economy (3)**: カーボンオフセット (carbon offset), {炭素中立|たんそちゅうりつ} (carbon neutrality; native term), リコール (product recall; official recall; suru)
- **Everyday/childcare (5)**: キックボード (kick scooter), アシスト (assistance; sports assist; suru), {永年|えいねん} (many years; long service), ローテンション (low-energy; subdued; na-adj), {認可外|にんかがい} (unlicensed; esp. daycare), {結婚活動|けっこんかつどう} (marriage hunting; full form of {婚活|こんかつ}; suru)
- **Dessert baking (4)**: メレンゲ (meringue), ハンドミキサー (hand mixer), {七分立|しちぶだ}て (whipped to soft peaks), {八分立|はちぶだ}て (whipped to firm peaks)

### 2026-07-05 (Routine v2: new-entries — 9 New Entries, IDs 29682–29690)
Created 9 general-tier entries, all from the high-priority "seen in entry" pool (candidates C22206–C22214, cited from entries 06402–06406 and 29680) — internal-completeness gaps referenced by existing entries. This **cleared the entire remaining seen-in-entry queue** (9 candidates). A robotics / fintech / facilities cluster: several were `noentry` inline-link targets inside the ロボット (06404) and coworking (06405/06406) entries. Conjugation table added to the 1 new suru-verb ({配膳|はいぜん}); no new kanji. §4 cross-model self-check on all 9 changed entries: **fully clean — 0 flagged, 0 applied, 0 rejected**. $0.0039. The non-"seen in entry" candidate tail remains heavily contaminated (fabricated/nonexistent words like 権使・些道・個尊・怒燥, compositional compounds, bare counters), so no padding from the oldest queue; captured アンドロイド as a referenced-but-missing candidate.

- **Robotics (4)**: {人型|ひとがた} (humanoid; human-shaped; noun/adjective-no), ヒューマノイド (humanoid robot), アーム (mechanical/robot arm; not the body part {腕|うで}), {配膳|はいぜん} (serving food; setting out dishes; suru)
- **Fintech (2)**: デビットカード (debit card), スマートコントラクト (smart contract; blockchain)
- **Facilities/work (3)**: ラウンジ (lounge; hotel/airport lounge), ワーカー (worker; loanword suffix), ドロップイン (drop-in; day use of a coworking space)

### 2026-07-04 (Routine v2: new-entries — 12 New Entries, IDs 29670–29681)
Created 12 general-tier entries, all from the high-priority "seen in entry" pool (candidates C22194–C22205, cited from entries 06394–06401) — internal-completeness gaps referenced by existing entries. This **cleared the entire remaining seen-in-entry queue** (12 candidates). A coherent crowdfunding / crypto / ideation cluster. Conjugation tables added to the 3 conjugating entries (1 verb-kuru {付|つ}いてくる, 2 suru-verbs ブレスト and マイニング); no new kanji. §4 cross-model self-check on all 12 changed entries: **11 clean; 0 applied, 1 rejected** — rejected a tag flag on ウォレット (`finance`→`technology`; in-list narrowness nit, and `finance` is well-justified since a wallet holds money/crypto). $0.0052. The non-"seen in entry" candidate tail remains heavily contaminated (typos, coined compounds, wrong glosses), so no padding from the oldest queue; logged a `[pattern]` observation and captured スマートコントラクト as a referenced-but-missing candidate.

- **Crowdfunding (3)**: クラファン (crowdfunding; casual abbr.), リターン (return/yield; crowdfunding reward), ブレスト (brainstorming; casual abbr., suru)
- **Crypto (5)**: ウォレット (digital/crypto wallet), マイニング (mining; suru), ビットコイン (Bitcoin), イーサリアム (Ethereum), {分散型|ぶんさんがた} (distributed; decentralized)
- **Other (4)**: {付|つ}いてくる (to follow along; verb-kuru), {発想法|はっそうほう} (ideation technique), ゲストハウス (guest house; budget shared lodging), ポジティブ (positive; upbeat; na-adjective)

### 2026-07-03 (Routine v2: new-entries — 15 New Entries, IDs 29655–29669)
Created 15 general-tier entries, all from the high-priority "seen in entry" pool (candidates C22178–C22193, cited from entries 06382–06392 and 04376) — internal-completeness gaps referenced by existing entries. The one katakana squirrel candidate (リス) was dropped as a variant duplicate of the existing {栗鼠|りす} (04352_risu) before creation. Conjugation tables added to the 5 new verbs (2 godan, 2 ichidan, 1 suru-verb {侵犯|しんぱん}); no new kanji. §4 cross-model self-check on all 15 changed entries: **fully clean — 0 flagged, 0 applied, 0 rejected**. $0.0065.

- **Verbs (5)**: {流|なが}し{込|こ}む (to pour into; to wash down; godan), {吹|ふ}き{流|なが}す (to blow away; godan), {押|お}し{止|と}める (to hold back by force; ichidan), {呼|よ}び{止|と}める (to call out and stop; to hail; ichidan), {侵犯|しんぱん} (violation; infringement; suru)
- **Money/bills (3)**: {飲食代|いんしょくだい} (food and drink bill), {飲|の}み{代|だい} (drinking expenses; bar tab), ツケ (tab; running account; deferred payment)
- **Other nouns (6)**: {宿主|しゅくしゅ} (host of a parasite/virus), {海里|かいり} (nautical mile), {使用権|しようけん} (right to use; license), {論理和|ろんりわ} (logical OR), {洗面器|せんめんき} (wash basin), {意気|いき} (spirit; morale; drive)
- **Adjective (1)**: {差別的|さべつてき} (discriminatory; na-adjective)

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
