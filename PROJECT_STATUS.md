# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-15
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
| Total entries | ~11,380 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~8,581 (open) |
| Candidate words | ~282 |
| Cross-references | ~3,338 |
| Example sentences | ~42,400 |
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

### 2026-02-15 (Vocabulary Expansion - 30 New Entries, Session 253)
Added 30 new dictionary entries (IDs 11295-11324) from candidate_words.json:

- **上- compounds (5)**: {上座|かみざ} (seat of honor), {上昇|じょうしょう} (rise/ascent), {上演|じょうえん} (performance/staging), {上級|じょうきゅう} (advanced level), {上限|じょうげん} (upper limit)
- **下- compounds (3)**: {下山|げざん} (descending a mountain), {下準備|したじゅんび} (preparation/prep work), {下落|げらく} (decline in prices)
- **不- compounds (6)**: {不在|ふざい} (absence), {不調|ふちょう} (poor condition/slump), {不穏|ふおん} (ominous/unsettling), {不毛|ふもう} (barren/fruitless), {不登校|ふとうこう} (school refusal), {不安定|ふあんてい} (unstable)
- **不- compounds continued (3)**: {不当|ふとう} (unfair/unjust), {不良|ふりょう} (bad/delinquent), (see above for {不穏|ふおん} etc.)
- **中- compounds (8)**: {中途半端|ちゅうとはんぱ} (half-hearted), {中継|ちゅうけい} (live broadcast), {中年|ちゅうねん} (middle-aged), {中庭|なかにわ} (courtyard), {中旬|ちゅうじゅん} (mid-month), {中傷|ちゅうしょう} (slander), {中盤|ちゅうばん} (middle stage), {中立|ちゅうりつ} (neutrality)
- **Other (5)**: {両立|りょうりつ} (balancing two things), {並行|へいこう} (parallel/concurrent), {世界観|せかいかん} (worldview/world-setting), {丸|まる}める (to roll up/smooth-talk), {中二病|ちゅうにびょう} (adolescent delusions)

Notable features:
- Systematic kanji compound clusters: 上-, 下-, 不-, 中- prefix families showing how a single kanji generates many useful words
- Multi-sense entries: {不良|ふりょう} (defective/delinquent), {不毛|ふもう} (barren land/fruitless effort), {世界観|せかいかん} (philosophical worldview/fictional world-setting), {丸|まる}める (physical rolling/figurative smooth-talking), {中華|ちゅうか} (Chinese food/Chinese culture)
- Cultural context: {上座|かみざ}/{下座|げざ} (seating etiquette), {中二病|ちゅうにびょう} (anime/internet culture), {不登校|ふとうこう} (Japanese social issue), {不良|ふりょう} (delinquent manga culture)
- Cross-references: {上限|じょうげん} ↔ {下限|かげん}, {上座|かみざ} ↔ {下座|げざ}, {並行|へいこう} ↔ {平行|へいこう}
- Level/stage hierarchies documented: {初級|しょきゅう}/{中級|ちゅうきゅう}/{上級|じょうきゅう}, {序盤|じょばん}/{中盤|ちゅうばん}/{終盤|しゅうばん}, {上旬|じょうじゅん}/{中旬|ちゅうじゅん}/{下旬|げじゅん}

Total entries: 11,350 → 11,380
Remaining candidates: 228 → 282 (30 removed, new candidates added by update_indexes)

### 2026-02-15 (Vocabulary Expansion - 30 New Entries, Session 252)
Added 30 new dictionary entries (IDs 11265-11294) from candidate_words.json:

- **Loanwords - daily life (8)**: ペア (pair/couple), ボトル (bottle), パーツ (parts/components), ブース (booth/stall), ポイント (point/reward points), ヘルパー (helper/care worker), バージョン (version), パートナー (partner)
- **Loanwords - descriptive (5)**: ブルー (blue/feeling down), プライベート (private/personal), マイナー (minor/niche), プレミアム (premium/deluxe), フォーマル (formal)
- **Loanwords - culture/entertainment (5)**: バトル (battle/contest), バトン (baton), ヒロイン (heroine), パレード (parade), バレンタイン (Valentine's Day)
- **Loanwords - society (3)**: ハラスメント (harassment), フェイク (fake/counterfeit), プロセス (process/procedure)
- **Loanwords - food (1)**: ビスケット (biscuit/cookie)
- **Loanwords - body/fashion (2)**: ベロ (tongue, colloquial), マント (cloak/cape)
- **Loanwords - other (6)**: ボス (boss), パワー (power/energy), ポーズ (pose/pause), ファミリー (family in commercial contexts), ベストセラー (bestseller), ピラミッド (pyramid)

Notable features:
- Multi-sense entries: ポーズ (pose/pause from different English words), ポイント (key point/reward points), ブルー (color/emotion)
- Japanese cultural context: バレンタイン ({本命|ほんめい}チョコ/{義理|ぎり}チョコ culture), ハラスメント (パワハラ, セクハラ, etc.), ポイント (Japanese loyalty point culture), ヘルパー (home care system), ファミリー (commercial/marketing usage)
- Wasei-eigo notes: バトンタッチ, バージョンアップ, ボトルキープ
- Cross-references: ヒロイン ↔ ヒーロー
- Contrast pairs noted: マイナー vs メジャー, フォーマル vs カジュアル, プライベート vs {仕事|しごと}

Total entries: 11,320 → 11,350
Remaining candidates: 258 → 228

### 2026-02-15 (Vocabulary Expansion - 30 New Entries, Session 251)
Added 30 new dictionary entries (IDs 11235-11264) from candidate_words.json:

- **{一|いち}- compounds (5)**: {一回|ひとまわ}り (one round/one size/12 years), {一心|いっしん} (wholeheartedness), {一助|いちじょ} (a help/contribution), {一味|いちみ} (gang/ichimi chili), {一命|いちめい} (one's life)
- **Loanwords - food/cooking (5)**: ハーブ (herb), フルーツ (fruit), ナッツ (nuts), ホイル (aluminum foil), レバー (lever/liver)
- **Loanwords - general (10)**: ニーズ (needs/demand), ノイズ (noise/static), レート (rate/exchange rate), ルーツ (roots/origins), ルート (route/channel), ラッキー (lucky), リボン (ribbon), メロディ (melody), ランプ (lamp/indicator light), ロゴ (logo)
- **Loanwords - descriptive (3)**: レア (rare/rare steak), ニッチ (niche), リフレッシュ (refresh)
- **Loanwords - people/culture (2)**: ヒーロー (hero), パンダ (panda)
- **Other (5)**: ビラ (flyer/leaflet), メモ{帳|ちょう} (memo pad), {三|み}つ{葉|ば} (mitsuba herb), {雌|めす} (female animal), パンチ (punch/impact/hole punch)

Notable features:
- Continued {一|いち}- compound expansion: {一回|ひとまわ}り (3 senses), {一味|いちみ} (2 senses: gang/chili), {一命|いちめい} (literary register)
- Multi-sense entries: レア (rare/cooking), レバー (lever/liver), ルート (physical route/business channel), ランプ (lamp/indicator light), パンチ (strike/impact/hole punch)
- Food/herb cluster: ハーブ, フルーツ, ナッツ, ホイル, {三|み}つ{葉|ば}, レバー with cooking collocations
- Cross-references: {雌|めす} ↔ {雄|おす}, ヒーロー ↔ ヒロイン
- New kanji: 2,298 → 2,299 ({雌|し})

Total entries: 11,290 → 11,320
Remaining candidates: 288 → 258

### 2026-02-15 (Vocabulary Expansion - 30 New Entries, Session 250)
Added 30 new dictionary entries (IDs 11205-11234) from candidate_words.json:

- **Loanword abbreviations (3)**: ラノベ (light novel), ラブコメ (romantic comedy), レンチン (microwaving)
- **Wasei-eigo (7)**: ランクイン (charting on a ranking), ワンマン (autocratic/solo-operated), チャームポイント (attractive feature), ピンポイント (precisely targeted), ロングセラー (perennial favorite), ロングラン (extended showing), ベースアップ (base pay raise)
- **Standard loanwords (7)**: リノベーション (renovation), リピーター (repeat customer), ロールモデル (role model), レントゲン (X-ray), ライトアップ (illumination), ラッシュ (rush/surge), リスペクト (respect)
- **Japanese nuance loanwords (4)**: ロマン (grand dream), ロス (waste/emotional loss), レパートリー (repertoire), モノクロ (monochrome)
- **Food (1)**: ラー{油|ゆ} (chili oil)
- **Writing/education (1)**: ローマ{字|じ} (Roman letters/romaji)
- **{一|いち}- compounds (7)**: {一列|いちれつ} (a row), {一族|いちぞく} (clan), {一転|いってん} (sudden change), {一角|いっかく} (a corner/section), {一様|いちよう} (uniform), {一説|いっせつ} (one theory), {一挙|いっきょ} (at a stroke)

Notable features:
- Wasei-eigo cluster with usage notes on Japanese-specific meanings: ランクイン, ワンマン, チャームポイント, ベースアップ, ロングセラー, ロングラン
- Multi-sense entries: ワンマン (autocratic/solo-operated), ラッシュ (rush hour/surge), ロス (waste/emotional loss)
- Cultural context: レンチン ({食|た}べるラー{油|ゆ} trend), ベースアップ ({春闘|しゅんとう} labor negotiations), ロス (あまロス phenomenon)
- Continued {一|いち}- compound expansion from Session 249
- Contrast pairs noted: リスペクト vs {尊敬|そんけい}, モノクロ vs {白黒|しろくろ}, リノベーション vs リフォーム

Total entries: 11,260 → 11,290
Remaining candidates: 318 → 288

### 2026-02-15 (Vocabulary Expansion - 30 New Entries, Session 249)
Added 30 new dictionary entries (IDs 11175-11204) from candidate_words.json:

- **一- compounds (14)**: {万|まん}が{一|いち} (just in case), {一覧|いちらん} (list/overview), {一方的|いっぽうてき} (one-sided), {一環|いっかん} (part of), {一服|いっぷく} (a break/a dose), {一概|いちがい}に (sweepingly — with negative), {一見|いっけん} (at first glance), {一貫|いっかん} (consistency), {一躍|いちやく} (at one bound), {一面|いちめん} (one side/entire surface), {一筋|ひとすじ} (one line/single-minded), {一騎打|いっきう}ち (showdown), {一変|いっぺん} (complete transformation), {一律|いちりつ} (uniform/across the board)
- **上- compounds (3)**: {上々|じょうじょう} (excellent), {上位|じょうい} (upper rank), {上場|じょうじょう} (stock listing)
- **Loanwords (8)**: ランドセル (school backpack), リハビリ (rehabilitation), レビュー (review), レンタル (rental), ランキング (ranking), ランチ (lunch), ライバル (rival), リビング (living room)
- **Other (5)**: リセット (reset), レジャー (leisure), ワイワイ (noisily/merrily), {上乗|うわの}せ (surcharge), {七草|ななくさ} (seven herbs of spring)

Notable features:
- Large cluster of {一|いち}-prefixed compounds covering formal/written Japanese
- Homophone pairs with cross-references: {一環|いっかん}/{一貫|いっかん}, {上々|じょうじょう}/{上場|じょうじょう}, {一見|いっけん}/{一件|いっけん}
- Multi-sense entries: {一服|いっぷく} (break/dose), {一面|いちめん} (aspect/entire surface), {一筋|ひとすじ} (line/devotion)
- Cultural context: ランドセル (ラン{活|かつ} culture), {七草|ななくさ} (Heian-period tradition), ライバル (positive rival archetype in anime/manga)
- Business vocabulary cluster: {上場|じょうじょう}, {上位|じょうい}, {一律|いちりつ}, {上乗|うわの}せ, {一覧|いちらん}, ランキング, レンタル, レビュー
- New kanji: 2,297 → 2,298 ({騎|き})

Total entries: 11,222 → 11,260 (includes 8 entries created between sessions)
Remaining candidates: 348 → 318

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
