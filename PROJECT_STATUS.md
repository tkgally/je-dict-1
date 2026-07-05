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

### 2026-07-03 (Routine v2: new-entries — 13 New Entries, IDs 29642–29654)
Created 13 general-tier noun entries. The one remaining "seen in entry" candidate was created first ({規則遵守|きそくじゅんしゅ}, rule compliance, cited from 06379); the rest are genuinely real, useful vocabulary hand-picked from the noisy candidate tail — the oldest/non-seen candidates are dominated by corpus-harvest garbage (fabricated words, compositional compounds, wrong glosses), so only ~13 defensible entries could be responsibly sourced rather than padding to 20. Picks skew to loanwords and news vocabulary: business franchise pair (フランチャイザー/フランチャイジー), a missile-range set ({誘導|ゆうどう}/{短距離|たんきょり}/{長距離|ちょうきょり}ミサイル), and everyday loanwords (アクションゲーム, フルカラー, コンペティション, マイナーリーグ, ハンドセット, ディップソース, プレイメーカー). §4 cross-model self-check on all 13: **12 clean; 0 applied, 1 rejected** — rejected a tag flag on コンペティション (`leisure`→`action`; in-list narrowness nit and "action" is a worse fit for a contest noun). Logged a `[pattern]` observation requesting a curator restock/cleanup of the polluted candidate list. $0.0056.

- **Business (3)**: {規則遵守|きそくじゅんしゅ} (rule compliance), フランチャイザー (franchisor), フランチャイジー (franchisee)
- **Military/news (3)**: {誘導|ゆうどう}ミサイル (guided missile), {短距離|たんきょり}ミサイル (short-range missile), {長距離|ちょうきょり}ミサイル (long-range missile)
- **Everyday loanwords (7)**: アクションゲーム (action game), フルカラー (full color), コンペティション (competition; contest), マイナーリーグ (minor league), ハンドセット (handset), ディップソース (dipping sauce; dip), プレイメーカー (playmaker)

### 2026-07-02 (Routine v2: new-entries — 12 New Entries, IDs 29630–29641)
Created 12 general-tier entries, all from the high-priority "seen in entry" pool — internal-completeness gaps referenced by existing entries (a photography cluster from 06362, geology terms, an optometry/vision-surgery cluster from 06370/06366, and single terms cited from the {正史|せいし}, {威圧的|いあつてき}, and {大器晩成|たいきばんせい} entries). This **cleared the entire remaining seen-in-entry queue** (12 candidates). The non-seen candidate tail remains heavy corpus-harvest noise ({小鼻|こばな}を{挟|はさ}む, 権使, がまま, 些道, 個尊, 怒燥, compositional phrases, bare counters), so no padding from the oldest queue. Conjugation tables added to the 3 new suru-verbs ({堆積|たいせき}, {褶曲|しゅうきょく}, {検眼|けんがん}); one new kanji assigned an ID ({褶|しゅう} from 褶曲 → 02780). §4 cross-model self-check on all 12 changed entries: **10 fully clean; 2 applied, 0 rejected** — applied 29634 ネガティブ semantic `technology` removed (core sense is attitude; kept `evaluation`) and 29640 {強圧的|きょうあつてき} semantic `personality`→`descriptive` (matches near-synonym {威圧的|いあつてき} and the -teki adjective convention; the model's `action` suggestion was not used). $0.0052.

- **Photography (2)**: {現像液|げんぞうえき} (developer / developing solution), ネガティブ (negative — attitude; photographic negative)
- **Geology (2)**: {堆積|たいせき} (deposition; sedimentation; suru), {褶曲|しゅうきょく} (geological fold; suru)
- **Vision (2)**: {検眼|けんがん} (eye examination; suru), {屈折矯正手術|くっせつきょうせいしゅじゅつ} (refractive surgery)
- **Other (6)**: {肌感覚|はだかんかく} (gut feeling; intuitive sense), {野史|やし} (unofficial history), {使用料|しようりょう} (usage fee), ロイヤリティ (royalty; licensing fee), {強圧的|きょうあつてき} (coercive; high-handed), {大器|たいき} (person of great talent)

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
