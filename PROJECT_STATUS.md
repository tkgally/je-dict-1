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
| Total entries | ~11,260 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~8,461 (open) |
| Candidate words | ~318 |
| Cross-references | ~3,336 |
| Example sentences | ~42,160 |
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

### 2026-02-14 (Vocabulary Expansion - 30 New Entries, Session 248)
Added 30 new dictionary entries (IDs 11145-11174) from candidate_words.json:

- **Native Japanese (2)**: まし (better/preferable of bad options), ナス (eggplant)
- **Loanwords with Japanese nuance (8)**: ドライ (dry/unemotional), ドリル (drill/practice workbook), フラグ (flag/foreshadowing), マニア (enthusiast), パフォーマンス (performance/publicity stunt), ムード (mood/romantic atmosphere), ヒット (hit/search result), フリーズ (freeze/computer crash)
- **Food/dining (3)**: ビュッフェ (buffet), メニュー (menu/training regimen), ポテト (potato/french fries)
- **Wasei-eigo (3)**: ホームセンター (home improvement store), バリアフリー (barrier-free/accessible), ベビーカー (baby stroller)
- **Business/work (3)**: ビジネス (business), メーカー (maker/manufacturer), ネイティブ (native speaker)
- **Fashion/beauty (2)**: ファッション (fashion), メイク (makeup)
- **Occupation (1)**: パティシエ (pastry chef)
- **Entertainment/culture (3)**: ホール (hall/front-of-house), メディア (media), モチーフ (motif/inspiration)
- **General vocabulary (5)**: メイン (main/primary), パニック (panic), ペース (pace), ピーク (peak), フェリー (ferry)

Notable features:
- Japanese-specific meanings: フラグ ({死亡|しぼう}フラグ internet culture), ドライ (personality type contrast with ウェット), パフォーマンス (publicity stunt sense), ムード (romantic atmosphere)
- Wasei-eigo cluster: ホームセンター, バリアフリー, ベビーカー with etymology notes
- Multi-sense entries: ドライ (physical/personality), ドリル (tool/workbook), ヒット (popularity/baseball/search), メニュー (restaurant/training), ポテト (vegetable/fries), ホール (auditorium/restaurant front), フリーズ (computer/person)
- Restaurant/food vocabulary: ビュッフェ (バイキング contrast), ポテト (じゃがいも contrast), メニュー, パティシエ

Total entries: 11,192 → 11,222
Remaining candidates: 271 → 241

### 2026-02-14 (Vocabulary Expansion - 30 New Entries, Session 247)
Added 30 new dictionary entries (IDs 11115-11144) from candidate_words.json:

- **Food/condiments (7)**: ポン{酢|ず} (ponzu sauce), マヨネーズ (mayonnaise), ドレッシング (salad dressing), メンマ (seasoned bamboo shoots), ピリ{辛|から} (mildly spicy), ドーナツ (doughnut), フライ (deep-fried food)
- **Vegetables/plants (4)**: ブロッコリー (broccoli), ピーマン (green pepper), ヨモギ (mugwort), ヨーグルト (yogurt)
- **Fish/seafood (2)**: マグロ (tuna), ヒラメ (flounder)
- **Desserts (2)**: パフェ (parfait), プリン (pudding)
- **Culture/society (3)**: バツイチ (once-divorced), ファミレス (family restaurant), マナー (manners/etiquette)
- **Business/abstract (3)**: ノウハウ (know-how), ニュアンス (nuance), メンタル (mental state)
- **Daily life (4)**: バケツ (bucket), ビニール (vinyl/plastic), フローリング (hardwood flooring), ヒント (hint/clue)
- **General (5)**: {山場|やまば} (climax/critical moment), ハードル (hurdle/obstacle), バブル (bubble/economic bubble), ベテラン (veteran/seasoned professional), ピンチ (crisis/tight spot)

Notable features:
- Food/cooking cluster with condiments, vegetables, and cooking terms
- Cultural context entries: バツイチ ({戸籍|こせき} × mark), ファミレス (Japanese dining culture), マナー (マナーモード)
- Japanese economic history: バブル with bubble era ({景気|けいき}) vocabulary
- Wasei-eigo notes: ファミレス, ピーマン (from French), マナーモード
- Multi-sense entries: フライ (deep-fried food/fly ball), バブル (physical bubble/economic bubble), ハードル (athletics/figurative obstacle)

Total entries: 11,162 → 11,192
Remaining candidates: 301 → 271

### 2026-02-13 (Vocabulary Expansion - 30 New Entries, Session 246)
Added 30 new dictionary entries (IDs 11085-11114) from candidate_words.json:

- **Legal/criminal justice (4)**: {原告|げんこく} (plaintiff), {検察|けんさつ} (prosecution), {懲役|ちょうえき} (imprisonment), {証言|しょうげん} (testimony)
- **Medical/nutrition (4)**: {抗生物質|こうせいぶっしつ} (antibiotic), {初診|しょしん} (first medical visit), {糖質|とうしつ} (carbohydrates), {脂質|ししつ} (lipids)
- **Health/body (2)**: {新陳代謝|しんちんたいしゃ} (metabolism), {体幹|たいかん} (core/trunk)
- **Education (2)**: {修士|しゅうし} (master's degree), {模試|もし} (mock exam)
- **Business/work (2)**: {決裁|けっさい} (approval), {着工|ちゃっこう} (start of construction)
- **Music (2)**: {指揮|しき} (conducting/command), {譜面|ふめん} (musical score)
- **〜{化|か} compounds (2)**: {深刻化|しんこくか} (worsening), {長期化|ちょうきか} (prolongation)
- **Infrastructure/science (3)**: {回線|かいせん} (line/circuit), {排水|はいすい} (drainage), {窒素|ちっそ} (nitrogen)
- **Culture/people (2)**: {冠婚葬祭|かんこんそうさい} (ceremonial occasions), {忍者|にんじゃ} (ninja)
- **General vocabulary (5)**: {反復|はんぷく} (repetition), {燃|も}え{尽|つ}き (burnout), {内覧|ないらん} (property viewing), コマ (frame/panel; class period), ニラ (Chinese chives)
- **Grammar/expression (1)**: {羽目|はめ} (predicament — 〜する{羽目|はめ}になる pattern)
- **Verb (1)**: ばらす (to reveal/to dismantle)

Notable features:
- Legal vocabulary cluster: {原告|げんこく}/{検察|けんさつ}/{懲役|ちょうえき}/{証言|しょうげん} with cross-reference to {被告|ひこく}
- Nutrition label terms: {糖質|とうしつ}/{脂質|ししつ} with Japanese food labeling explanation
- Multi-sense entries: {指揮|しき} (military command/music conducting), {内覧|ないらん} (property viewing/exhibition preview), コマ (manga panel/class period), ばらす (reveal secret/dismantle)
- Cultural notes: {冠婚葬祭|かんこんそうさい} (four life ceremony categories), {忍者|にんじゃ} (Iga/Koka history), {模試|もし} ({偏差値|へんさち} system)
- Homophone distinctions: {決裁|けっさい} vs {決済|けっさい}, {回線|かいせん} vs {海鮮|かいせん}
- New kanji: 2,295 → 2,296 (窒)

Total entries: 11,132 → 11,162
Remaining candidates: 211 → 181

### 2026-02-13 (Vocabulary Expansion - 30 New Entries, Session 245)
Added 30 new dictionary entries (IDs 11055-11084) from candidate_words.json:

- **I-adjectives (3)**: {騒|さわ}がしい (noisy/turbulent), {慌|あわ}ただしい (hectic), めでたい (auspicious/naive)
- **Calendar nouns (2)**: {年末|ねんまつ} (year-end), {年始|ねんし} (beginning of year)
- **Communication/digital (3)**: {口|くち}コミ (word of mouth/reviews), {閲覧|えつらん} (browsing/viewing), {送信|そうしん} (sending/transmission)
- **Social/cultural (3)**: {恩返|おんがえ}し (returning a favor), {見返|みかえ}り (something in return), {社交辞令|しゃこうじれい} (social pleasantry)
- **Medical (7)**: {予防接種|よぼうせっしゅ} (vaccination), カルテ (medical chart), {問診|もんしん} (medical interview), {眼科|がんか} (ophthalmology), {歯科|しか} (dentistry), {皮膚科|ひふか} (dermatology), {採血|さいけつ} (blood draw)
- **Health/body (3)**: {悪化|あっか} (deterioration), {不眠|ふみん} (insomnia), {熟睡|じゅくすい} (deep sleep)
- **Verb (1)**: {繕|つくろ}う (to mend/keep up appearances)
- **Business/legal (2)**: {取引先|とりひきさき} (business partner), {被告|ひこく} (defendant)
- **Other nouns (6)**: {泥沼|どろぬま} (quagmire), {番狂|ばんくる}わせ (upset), {花壇|かだん} (flower bed), {自尊心|じそんしん} (self-esteem), {膨張|ぼうちょう} (expansion), {結露|けつろ} (condensation)

Notable features:
- Medical department cluster ({眼科|がんか}/{歯科|しか}/{皮膚科|ひふか}) with cross-references between them
- Antonym pairs: {不眠|ふみん} ↔ {熟睡|じゅくすい}, {恩返|おんがえ}し ↔ {見返|みかえ}り (related)
- Multi-sense entries: {騒|さわ}がしい (noise/turmoil), めでたい (auspicious/naive), {繕|つくろ}う (mend/appearances), {泥沼|どろぬま} (literal/figurative)
- Cultural notes: めでたい (鯛 pun), {社交辞令|しゃこうじれい} (reading Japanese sincerity), カルテ (German medical influence)
- Calendar pair: {年末|ねんまつ}/{年始|ねんし} with {年末年始|ねんまつねんし} compound

Total entries: 11,102 → 11,132
Remaining candidates: 241 → 211

### 2026-02-12 (New Candidate Words - 55 Words, Session 244)
Added 55 new candidate words to candidate_words.json across diverse domains:

- **Legal/criminal justice (5)**: 被告 (defendant), 原告 (plaintiff), 検察 (prosecution), 懲役 (imprisonment), 証言 (testimony)
- **Medical specialties & visits (9)**: 予防接種 (vaccination), カルテ (medical chart), 問診 (medical interview), 抗生物質 (antibiotic), 眼科 (ophthalmology), 歯科 (dentistry), 皮膚科 (dermatology), 初診 (first visit), 採血 (blood draw)
- **Health/nutrition (4)**: 糖質 (carbohydrates), 脂質 (lipids), 新陳代謝 (metabolism), コレステロール (cholesterol)
- **Internet/communication (4)**: 口コミ (word of mouth/reviews), 閲覧 (browsing), 送信 (sending), 回線 (circuit/line)
- **Sports/fitness (3)**: 体幹 (core/trunk), 反復 (repetition), 番狂わせ (upset)
- **Social/cultural (4)**: 社交辞令 (social pleasantry), 冠婚葬祭 (ceremonial occasions), 恩返し (returning a favor), 見返り (something in return)
- **Calendar (2)**: 年末 (year-end), 年始 (beginning of year)
- **Education (2)**: 修士 (master's degree), 模試 (mock exam)
- **Business/construction (2)**: 決裁 (approval), 着工 (start of construction)
- **Music (2)**: 指揮 (conducting/command), 譜面 (musical score)
- **Home/daily life (3)**: 排水 (drainage), 結露 (condensation), 繕う (to mend)
- **Psychology (2)**: 自尊心 (self-respect), 燃え尽き (burnout)
- **Science (2)**: 膨張 (expansion), 窒素 (nitrogen)
- **Adjectives (3)**: 騒がしい (noisy), 慌ただしい (hectic), めでたい (auspicious)
- **～化 compounds (3)**: 悪化 (deterioration), 深刻化 (worsening), 長期化 (prolongation)
- **Sleep (2)**: 不眠 (insomnia), 熟睡 (deep sleep)
- **Other (3)**: 取引先 (business partner), 内覧 (property viewing), 花壇 (flower bed)

Strategies used: semantic domain exploration (medical, legal, nutrition, home), practical situation vocabulary, corpus-driven gap analysis, collocational mining, productive pattern completion (～化 compounds)

Candidate words: 130 → 185

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
