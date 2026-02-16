# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-16
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
| Total entries | ~11,459 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~8,660 (open) |
| Candidate words | ~222 |
| Cross-references | ~3,340 |
| Example sentences | ~42,500 |
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

### 2026-02-16 (Vocabulary Expansion - 30 New Entries, Session 255)
Added 30 new dictionary entries (IDs 11374-11403) from candidate_words.json:

- **Japanese compounds - positional (5)**: {上記|じょうき} (above-mentioned), {下記|かき} (below-mentioned), {上部|じょうぶ} (upper part), {下部|かぶ} (lower part), {下限|かげん} (lower limit)
- **Japanese compounds - 不- prefix (5)**: {不快|ふかい} (unpleasant), {不揃|ふぞろ}い (uneven/mismatched), {不向|ふむ}き (unsuited), {不人気|ふにんき} (unpopular), {不定期|ふていき} (irregular)
- **Japanese compounds - other (5)**: {並|なみ} (ordinary/medium), {中頃|なかごろ} (around the middle), {中卒|ちゅうそつ} (middle school graduate), {一揆|いっき} (uprising), {一堂|いちどう} (in one place)
- **Japanese compounds - time/quantity (2)**: {丸々|まるまる} (completely/plump), {一端|いったん} (one end/a part)
- **Loanwords (13)**: ハイブリッド (hybrid), マジック (magic/marker), ユニーク (unique/quirky), リゾート (resort), リーズナブル (reasonable in price), レギュラー (regular/starter), ローカル (local), バラエティ (variety/variety show), ブレンド (blend), パンデミック (pandemic), プラチナ (platinum), ロマンス (romance), ワイド (wide)

Notable features:
- Antonym pairs: {上記|じょうき} ↔ {下記|かき}, {上部|じょうぶ} ↔ {下部|かぶ}
- Homophone warnings: {上部|じょうぶ} vs {丈夫|じょうぶ}, {下限|かげん} vs {加減|かげん}, {不快|ふかい} vs {深|ふか}い, {一端|いったん} vs {一旦|いったん}
- False friend notes: ユニーク (quirky, not just "unique"), リーズナブル (price only, not general "reasonable")
- Multi-sense entries: {丸々|まるまる} (completely/plump), マジック (magic/marker), レギュラー (starter/standard), バラエティ (variety/TV show), {一端|いったん} (physical end/glimpse)
- Cultural context: {並|なみ} (restaurant sizing), ブレンド (coffee shop culture), ワイドショー (Japanese TV genre), プラチナチケット (hard-to-get tickets)
- New kanji: 2,302 → 2,303 ({揆|き})

Total entries: 11,429 → 11,459
Remaining candidates: 252 → 222

### 2026-02-16 (Vocabulary Expansion - 30 New Entries, Session 254)
Added 30 new dictionary entries (IDs 11344-11373) from candidate_words.json:

- **下- compounds (4)**: {下剋上|げこくじょう} (overthrowing superiors), {下手|へた}くそ (terrible at), {下敷|したじ}き (desk pad/pinned underneath), {下級|かきゅう} (lower grade), {下座|げざ} (lower seat), {下層|かそう} (lower stratum)
- **不- compounds (13)**: {不倫|ふりん} (adultery), {不審者|ふしんしゃ} (suspicious person), {不死身|ふじみ} (invulnerable), {不自然|ふしぜん} (unnatural), {不意|ふい} (unexpected), {不明|ふめい} (unknown), {不適切|ふてきせつ} (inappropriate), {不平等|ふびょうどう} (inequality), {不法|ふほう} (illegal), {不確|ふたし}か (uncertain), {不本意|ふほんい} (reluctant), {不完全|ふかんぜん} (incomplete), {不透明|ふとうめい} (opaque/unclear)
- **中- compounds (5)**: {中華街|ちゅうかがい} (Chinatown), {中退|ちゅうたい} (dropping out), {中部|ちゅうぶ} (central region), {中流|ちゅうりゅう} (middle class/midstream), {中核|ちゅうかく} (nucleus/core), {中枢|ちゅうすう} (nerve center)
- **両- compounds (3)**: {両端|りょうたん} (both ends), {両者|りょうしゃ} (both parties), {両面|りょうめん} (both sides)
- **Other (2)**: {串|くし}カツ (deep-fried skewers), {世紀末|せいきまつ} (end of century)

Notable features:
- Systematic 不- prefix cluster covering negation patterns: from everyday ({不自然|ふしぜん}, {不明|ふめい}) to formal/legal ({不法|ふほう}, {不適切|ふてきせつ})
- Multi-sense entries: {下敷|したじ}き (stationery/disaster), {不透明|ふとうめい} (physical/figurative), {中流|ちゅうりゅう} (social class/river)
- Cultural context: {下剋上|げこくじょう} (Sengoku history/sports upsets), {下座|げざ} (seating etiquette), {中華街|ちゅうかがい} (Yokohama/Kobe/Nagasaki), {串|くし}カツ (Osaka food culture), {世紀末|せいきまつ} (North Star/fin de siecle)
- Antonym cross-references: {不自然|ふしぜん} ↔ {自然|しぜん}, {不平等|ふびょうどう} ↔ {平等|びょうどう}, {不完全|ふかんぜん} ↔ {完全|かんぜん}, {下級|かきゅう} ↔ {上級|じょうきゅう}, {下座|げざ} ↔ {上座|かみざ}
- New kanji: 2,299 → 2,302 ({剋|こく}, {枢|すう}, {核|かく})

Total entries: 11,399 → 11,429
Remaining candidates: 282 → 252

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
