# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-12
**Current phase**: Phase 4 - N4 Vocabulary Expansion & Interface Enhancement

**Live site**: https://tkgally.github.io/je-dict-1/

## Current State

### Phase
**Phase 4: N4 Vocabulary Expansion & Interface Enhancement** - Adding N4 vocabulary while maintaining v2 quality standards, plus new web interface features.

### Infrastructure Status
- [x] Directory structure created (prefix-based subdirectories for scalability)
- [x] JSON schema defined (`build/schema.json`)
- [x] Validation script working (`build/validate.py`)
- [x] Build script working (`build/build.py`)
- [x] Static HTML site generation (`build/build_flat.py`)
- [x] Furigana system with toggle
- [x] Claude Code skills for entry guidelines
- [x] Quality specification v2 from multi-model evaluation
- [x] Vocabulary-notes skill for formatting guidelines
- [x] Notes field supports paragraph breaks and bullet points
- [x] Multiple interface modes (Search, Browse, Recent, Random)
- [x] Sticky header with interface toggle
- [x] Last updated date in footer
- [x] Cross-reference linking system with UI navigation (567 refs, 97% resolved)
- [x] Audio pronunciation for example sentences (1,028 audio files)
- [x] Prefix-based subdirectory structure for entries and audio (scalable to 10,000+ entries)
- [x] Shared utility modules (`path_utils.py`, `japanese_utils.py`)
- [x] Audio integrity validation in `validate.py`
- [x] Deterministic build output (clean before build)

### Content Status
- **Total entries**: 3,431
- **JLPT N5 coverage**: ~95% complete
- **JLPT N4 coverage**: ~450 entries added
- **JLPT N3 vocabulary**: ~1,090 entries added
- **Candidate words**: ~2,079 words tracked in `candidate_words.json`
- **Priority candidates**: 0 words remaining in `candidate_words_priority.json` (all 94 completed)
- **Cross-references**: 567 total (555 resolved, 97% resolution rate)
- **Audio files**: 1,028 MP3 files covering example sentences

### Entry Breakdown by JLPT Level
| Level | Count | Status |
|-------|-------|--------|
| N5 | ~761 | Complete |
| N4 | ~392 | In progress |

### Entry Breakdown by Type
| Type | Count | Notes |
|------|-------|-------|
| Verbs | ~220 | Includes 95 N4 verbs with transitivity info |
| Nouns | ~480 | Includes N4 nouns, katakana loanwords |
| Adjectives | ~100 | I-adjectives and na-adjectives |
| Adverbs | ~56 | Includes 11 new N4 adverbs |
| Particles | 10 | Core particles with predicate lists |
| Counters | ~21 | Common counting patterns |
| Keigo verbs | 12 | Honorific and humble forms |
| Other | ~150 | Expressions, suffixes, etc. |

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

## Claude Code Skills

Available in `.claude/skills/` (automatically loaded when relevant):

| Skill | Use When |
|-------|----------|
| `entry-guidelines` | Creating any entry |
| `verb-entry` | Creating/revising verb entries |
| `adjective-entry` | Creating/revising adjective entries |
| `particle-entry` | Creating/revising particle entries |
| `other-entries` | Creating nouns, counters, adverbs, expressions |
| `revise-entries` | Revising existing entries to v2 standards |
| `vocabulary-notes` | Formatting notes field content |
| `cross-reference-entry` | Adding cross-references between entries |

## Recent Changes

### 2026-01-12 (Vocabulary Expansion - 50 New Entries, Session 22)
- Added 50 new dictionary entries from candidate_words.json (3,381 → 3,431 total)
- Each entry written individually following entry-guidelines skill
- New entries are primarily N2/N3 vocabulary focused on れ/ろ/わ/り/ゆ/め/も/か/け/さ/あ rows:
  - Nouns: 礼儀, 連想, 連続, 老人, 労働, 論争, 論文, 別れ, 脇, 話題, 悪口, 湾, 料金, 例外, 量, 寮, 率, 郵便, 目上, 飯, 綿, 免許, 申し訳, 回復, 癖, 選手, ストレス, メッセージ, アンケート
  - Na-adjectives: 冷静 (calm), わがまま (selfish), 利口 (clever), 面倒 (troublesome), 上等 (first-class)
  - Adverbs: わざと (on purpose), 僅か (only), 滅多に (rarely), 必ずしも (not necessarily), 結局 (after all), 極 (quite), 更に (furthermore), 実に (indeed), いつでも (anytime)
  - Conjunctions: しかも (moreover), したがって (therefore), あるいは (or), もしも (if)
  - Pronouns: 我々 (we)
  - Pre-noun adjectival: あらゆる (all, every), 全て (all)
- Notable entry groups:
  - ろ-row academic terms: 老人, 労働, 論争, 論文
  - わ-row expressions: わがまま, わざと, 話題, 悪口
  - Formal conjunctions: したがって, しかも, あるいは
  - Common adverbs: 結局, 更に, 極, 実に
- Removed 47 candidates from candidate_words.json (2,126 → 2,079)

### 2026-01-12 (Vocabulary Expansion - 50 New Entries, Session 21)
- Added 50 new dictionary entries from candidate_words.json (3,331 → 3,381 total)
- Each entry written individually following entry-guidelines skill
- New entries are primarily N2/N3 vocabulary focused on ま/み/む/め/せ/ぜ/の/か rows:
  - Nouns: 孫, 間違い, 祭, 真似, 豆, 万一, 実, 見送り, 味方, 見舞い, 土産, 都, 未来, 魅力, 向かい, 夢中, 名人, 命令, 石炭, 禅, 前進, 農民, 書斎, 食物, 食糧, 声明, 姓名, 税, 章, 慣行, 降伏, 大戦, 先行, 選考, 密, 荒廃, 正規, 足袋
  - Na-adjectives: 真っ赤 (bright red), 見事 (splendid), 精巧 (elaborate)
  - I-adjectives: まぶしい (dazzling), 蒸し暑い (humid)
  - Adverbs: まさか (surely not), まるで (just like), 前もって (in advance), なぜなら (because)
  - Expressions: 違いない (must be), 無し (without)
- Notable homophone pairs:
  - 声明/姓名/生命 (せいめい - statement/full name/life)
  - 先行/選考/専攻 (せんこう - preceding/selection/major)
  - 成功/精巧 (せいこう - success/elaborate)
  - 降伏/幸福 (こうふく - surrender/happiness)
  - 荒廃/後輩 (こうはい - ruin/junior)
- Removed 49 candidates from candidate_words.json (2,175 → 2,126)

### 2026-01-12 (Vocabulary Expansion - 50 New Entries, Session 20)
- Added 50 new dictionary entries from candidate_words.json (3,281 → 3,331 total)
- Each entry written individually following entry-guidelines skill
- New entries are primarily N2 vocabulary focused on し/そ/は/ひ/ふ/ほ/ぼ/ま rows:
  - Nouns: 至急, 署名, 書物, 尻, 信仰, 進行, 申告, 捜査, 操縦, 相続, 像, 裸, 発行, 発車, 発射, 羽根, 班, 版, 場, 莫大, 場面, 非行, 引越し, 必死, 日付, 否定, 一言, 人込み, 品, 節, 振り, 部分, 文, 頬, 保証, 保障, 補償, 仏, 歩道, 炎, 堀, 棒, 迷子
  - Adverbs: しきりに, ばったり, ほっと, ぼんやり, まあ
  - I-adjective: 等しい (equal)
  - Expressions: 一人一人 (each person)
- Notable entry pairs:
  - 信仰/進行 (homophones しんこう - faith/progress)
  - 捜査/操作 (homophones そうさ - investigation/operation)
  - 発車/発射 (homophones はっしゃ - departure/firing)
  - 保証/保障/補償 (homophones ほしょう - warranty/security/compensation)
  - 否定/肯定 (antonym pair - negation/affirmation)
  - 部分/全体 (antonym pair - part/whole)
- Removed 50 candidates from candidate_words.json (2,225 → 2,175)

### 2026-01-12 (Vocabulary Expansion - 50 New Entries, Session 19)
- Added 50 new dictionary entries from candidate_words.json (3,231 → 3,281 total)
- Each entry written individually following entry-guidelines skill
- New entries are primarily N2/N3 vocabulary focused on も/や/ゆ/よ/り rows:
  - Nouns: 毛布, 目標, 文字, 物音, 物語, 模様, 文句, 役割, 家賃, 宿, 有機, 友好, 有効, 優秀, 優勝, 友情, 友人, 有能, 有利, 床, 夜明け, 容器, 陽気, 要求, 用心, 要素, 予期, 予算, 予想, 予測, 世の中, 余分, 予報, 予防, 嫁, 余裕, 喜び, 利益, 理解, 陸, 理想, 留学, 流行, 両替
  - Na-adjectives: 厄介 (troublesome), 愉快 (pleasant), 豊か (rich/abundant)
  - Adverbs: やがて (before long), やや (slightly), 要するに (in short)
- Notable entry pairs:
  - 友好/有効 (homophones ゆうこう - friendship/valid)
  - 容器/陽気 (homophones ようき - container/cheerful)
  - 予想/予測 (related words - expectation/prediction)
  - 予報/予防 (homophones よほう/よぼう - forecast/prevention)
  - 利益/損失 (antonym pair - profit/loss, cross-referenced)
- Removed 50 candidates from candidate_words.json (2,275 → 2,225)

### 2026-01-12 (Vocabulary Expansion - 50 New Entries, Session 18)
- Added 50 new dictionary entries from candidate_words.json (3,181 → 3,231 total)
- Each entry written individually following entry-guidelines skill
- New entries are primarily N2 vocabulary focused on ひ/ふ/へ/ほ/ぼ rows:
  - Nouns: 批判, 批評, 票, 評価, 表現, 表情, 評判, 表面, 費用, 風景, 夫婦, 笛, 服装, 不幸, 不自由, 夫人, 不足, 双子, 筆, 不平, 不利, 雰囲気, 武器, 舞台, 物価, 物質, 物理, 分析, 文明, 分野, 塀, 平均, 変化, 変更, 方向, 報告, 宝石, 豊富, 方法, 訪問, 誇り, 埃, 保護, 保存, 本人, 本物, 冒険
  - Na-adjectives: 微妙 (subtle/iffy), 平等 (equal)
- Notable entry pairs:
  - 批判/批評 (related words - criticism/critique)
  - 変化/変更 (related words - change/modification)
  - 誇り/埃 (homophones ほこり - pride/dust)
  - 本人/本物 (related words - the person himself/genuine article)
  - 不幸/幸福 (antonym pair - unhappiness/happiness)
  - 不利/有利 (antonym pair - disadvantage/advantage)
  - 不平/不満 (related words - complaint/dissatisfaction)
- Removed 50 candidates from candidate_words.json (2,325 → 2,275)

### 2026-01-12 (Vocabulary Expansion - 50 New Entries, Session 17)
- Added 50 new dictionary entries from candidate_words.json (3,131 → 3,181 total)
- Each entry written individually following entry-guidelines skill
- New entries are primarily N2/N3 vocabulary focused on な/に/ね/の/は/ば/ひ rows:
  - Nouns: 半ば, 眺め, 流れ, 謎, 納得, 縄, 日光, 日中, 入場, 人間, 根, 値, 願い, 熱帯, 年代, 野, 脳, 農家, 能力, 望み, 後, 俳優, 墓, 博士, 拍手, 破産, 働き, 発達, 発展, 発表, 母親, 幅, 針, 範囲, 反抗, 犯罪, 反省, 判断, 犯人, 販売, 爆発, 比較, 悲劇, 飛行, 額
  - Na-adjectives: 苦手 (weak at), 派手 (showy/flashy), 生 (raw/live)
  - Adverbs: にっこり (smilingly)
  - Slang/colloquial: 馬鹿 (fool/idiot)
- Notable entry pairs:
  - 根/値 (homophones ね - root/price)
  - 破産/倒産 (related words - personal/business bankruptcy)
  - 発達/発展 (related words - organic/societal development)
  - 苦手/得意 (antonym pair - weak at/good at)
  - 派手/地味 (antonym pair - showy/plain)
  - 悲劇/喜劇 (antonym pair - tragedy/comedy)
- Removed 50 candidates from candidate_words.json (2,375 → 2,325)

### 2026-01-12 (Vocabulary Expansion - 50 New Entries, Session 16)
- Added 50 new dictionary entries from candidate_words.json (3,081 → 3,131 total)
- Each entry written individually following entry-guidelines skill
- New entries are primarily N2/N3 vocabulary focused on た/ち/つ/て/と/ど/な rows:
  - Nouns: 盾, 違い, 茶, 注, 通行, 勤め, 務め, 釣り, 停留所, 出会い, 出来事, 伝言, 電子, 問い, 答案, 倒産, 投票, 東洋, 得意, 特徴, 登山, 年月, 図書, 年寄り, 道徳, 童謡, 動揺, 読書, 独身, 独立, 努力, 泥, 名, 仲間
  - Grammar terms: 動詞 (verb), 同士 (fellow/suffix)
  - Expressions: ちょうだい (please give me - casual), とんでもない (outrageous/not at all)
  - Adverbs: とにかく (anyway), 共に (together), どうしても (no matter what), どんなに (how much)
  - Na-adjectives: 適度 (moderate), 得意 (good at)
  - Counter/suffix: 度 (occasion)
- Notable entry pairs:
  - 動詞/同士 (homophones どうし - verb/fellow)
  - 童謡/動揺 (homophones どうよう - nursery rhyme/agitation)
  - 勤め/務め (homophones つとめ - employment/duty)
  - 特徴/特長 (homophones とくちょう - characteristic/strong point)
  - 得意/苦手 (antonym pair - good at/bad at)
  - 独身/既婚 (antonym pair - single/married)
  - 独立/依存 (antonym pair - independence/dependence)
- Removed 49 candidates from candidate_words.json (2,424 → 2,375)

### 2026-01-12 (Vocabulary Expansion - 50 New Entries, Session 15)
- Added 50 new dictionary entries from candidate_words.json (3,031 → 3,081 total)
- Each entry written individually following entry-guidelines skill
- New entries are primarily N2/N3 vocabulary focused on ち/つ/て rows:
  - Nouns: 地球, 地区, 遅刻, 知事, 父親, 知能, 地平線, 中央, 中学, 中古, 中止, 注目, 注文, 長期, 調査, 調子, 頂上, 挑戦, 貯金, 著者, 治療, 通過, 通貨, 通学, 通勤, 通信, 通訳, 疲れ, 付き合い, 包み, 続き, 翼, 罪, 連れ, 提案, 定期, 抵抗, 提出, 停電, 敵, 哲学, 鉄道, 徹夜, 手間, 典型, 天候, 天然
  - Adverbs: 次々 (one after another), つまり (in other words), 直接 (directly)
- Notable entry pairs:
  - 通過/通貨 (homophones つうか - passage/currency)
  - 天候/天気/気候 (weather-related: formal weather/casual weather/climate)
  - 通学/通勤 (related words - school commute/work commute)
  - 長期/短期 (antonym pair - long-term/short-term)
  - 直接/間接 (antonym pair - direct/indirect)
  - 天然/人工 (antonym pair - natural/artificial)
- Removed 50 candidates from candidate_words.json (2,474 → 2,424)

### 2026-01-12 (Vocabulary Expansion - 50 New Entries, Session 14)
- Added 50 new dictionary entries from candidate_words.json (2,981 → 3,031 total)
- Each entry written individually following entry-guidelines skill
- New entries are primarily N2/N3 vocabulary focused on た/だ/ち rows:
  - Nouns: 田, 他, 対, 隊, 体育, 体温, 大会, 退学, 大気, 滞在, 大使, 対象, 対照, 体重, 態度, 逮捕, 太陽, 大陸, 宝, 立場, 束, 旅, 試し, 便り, 単位, 単語, 代金, 大臣, 大統領, 代表, 大部分, 題名, 代理, 段, 男子, 団体, 地位, 知恵, 地下
  - Adjectives/Na-adjectives: 退屈 (boring), 大した (significant), 平ら (flat), 単純 (simple)
  - Adverbs: たっぷり (plenty), たとえ (even if), たまたま (by chance), 単に (simply)
  - Expressions: たまらない (unbearable), だって (but/because)
  - Other: 互い (mutual)
- Notable entry pairs:
  - 対象/対照 (homophones たいしょう - target/contrast)
  - 太陽/月 (antonym pair - sun/moon, cross-referenced)
  - 男子/女子 (antonym pair - male/female)
  - 立場/地位 (related words - standpoint/status)
  - 単位/単語/単純/単に (related 単 words)
- Removed 50 candidates from candidate_words.json (2,524 → 2,474)

### 2026-01-12 (Vocabulary Expansion - 50 New Entries, Session 13)
- Added 50 new dictionary entries from candidate_words.json (2,934 → 2,981 total; 3 duplicates from previous session removed)
- Each entry written individually following entry-guidelines skill
- New entries are primarily N2/N3 vocabulary focused on し/じ/す/ず/せ rows:
  - Nouns: 身体, 審判, 心理, 真理, 磁気, 磁器, 自殺, 字体, 辞退, 自動, 児童, 重視, 順, 情, 上京, 状態, 上達, 冗談, 情報, 女王, 女子, 助詞, 助手, 女優, 人種, 人生, 人物, 水準, 推薦, 睡眠, 数, 数字, 末, 姿, 筋, 図, 頭痛, 世紀, 請求, 制限, 精神, 成人, 成績
  - Adjectives: 正確 (accurate), 正式 (formal)
  - Adverbs: 少なくとも (at least), 少しも (not at all), すなわち (namely)
  - Verbs: ずれる (to shift)
- Notable entry pairs:
  - 心理/真理 (homophones しんり - psychology/truth)
  - 磁気/磁器 (homophones じき - magnetism/porcelain)
  - 字体/辞退 (homophones じたい - font/refusal)
  - 自動/児童 (homophones じどう - automatic/children)
  - 女子/助詞 (homophones じょし - female/particle)
  - 性格/正確 (homophones せいかく - personality/accurate)
  - 数/数字 (related words すう/すうじ - number/numeral)
- Removed 49 candidates from candidate_words.json (2,573 → 2,524)

### 2026-01-12 (Vocabulary Expansion - 50 New Entries, Session 12)
- Added 50 new dictionary entries from candidate_words.json (2,884 → 2,934 total)
- Each entry written individually following entry-guidelines skill
- New entries are primarily N2/N3 vocabulary focused on じゅ/じょ/せ/ぜ/そ/ぞ rows:
  - Nouns: 住宅, 住民, 順調, 順番, 乗客, 条件, 上司, 常識, 製造, 成長, 制度, 青年, 生年月日, 政府, 生物, 生命, 整理, 責任, 世間, 設計, 設備, 節約, 選挙, 洗剤, 選択, 宣伝, 税金, 全員, 全国, 前者, 全身, 全体, 騒音, 操作, 創造, 装置, 速度, 組織, 損, 存在, 尊重, 象, 増加
  - Adjectives: 贅沢 (extravagant), 粗末 (crude)
  - Adverbs: 精々 (at most), そっと (softly), そのまま (as is)
  - Conjunctions: それとも (or), 先日 (the other day)
- Notable entry pairs:
  - 上司/部下 (homophones - boss/subordinate, antonym)
  - 前者/後者 (antonym - former/latter)
  - 損/得 (antonym - loss/gain)
  - 増加/減少 (antonym - increase/decrease)
  - 創造/想像 (homophones そうぞう - creation/imagination)
  - 操作/捜査 (homophones そうさ - operation/investigation)
  - 尊重/尊敬 (related words - respect for values/respect for people)
- Removed 50 candidates from candidate_words.json (2,623 → 2,573)

### 2026-01-12 (Vocabulary Expansion - 50 New Entries, Session 11)
- Added 50 new dictionary entries from candidate_words.json (2,834 → 2,884 total)
- Each entry written individually following entry-guidelines skill
- New entries are primarily N2/N3 vocabulary focused on し/じ-row words:
  - Nouns: 奨学金, 正午, 少女, 症状, 衝突, 商人, 承認, 少年, 商売, 消費, 消防, 証明, 照明, 省略, 職業, 食卓, 食品, 植物, 食欲, 食料, 処理, 知らせ, 知り合い, 印, 城, 進学, 神経, 信号, 診察, 親戚, 心臓, 身長, 進歩, 親友, 信用, 信頼, 時期, 時刻, 事実, 事情, 実験, 実行, 実施, 実現, 実力, 自慢, 渋滞
  - Adjectives: 新鮮 (fresh), 慎重 (careful)
  - Adverb: 少々 (a little - formal)
- Notable entry pairs:
  - 証明/照明 (homophones しょうめい - proof/lighting)
  - 商人/承認 (homophones しょうにん - merchant/approval)
  - 身長/慎重 (homophones しんちょう - height/careful)
  - 信用/信頼 (similar words - practical trust/deeper trust)
  - 少年/少女 (antonym pair - boy/girl)
- Removed 49 candidates from candidate_words.json (2,672 → 2,623)

### 2026-01-11 (Vocabulary Expansion - 50 New Entries, Session 10)
- Added 50 new dictionary entries from candidate_words.json (2,784 → 2,834 total)
- Each entry written individually following entry-guidelines skill
- New entries are primarily N2/N3 vocabulary focused on し-row words:
  - Nouns: 刺激, 資源, 支出, 詩人, 思想, 次第, 湿気, 失業, 湿度, 失望, 支店, 視点, 指導, 品, 支払, 芝居, 芝生, 資本, 死亡, 脂肪, 志望, 姉妹, 霜, 借金, 週, 州, 周囲, 収穫, 宗教, 就職, 修正, 集団, 集中, 収入, 修理, 主義, 宿泊, 首相, 手術, 手段, 主張, 出身, 出版, 出場, 首都, 主婦, 瞬間, 賞, 障害, 生涯
- Notable entry pairs:
  - 死亡/脂肪/志望 (homophones しぼう)
  - 支店/視点 (homophones してん)
  - 障害/生涯 (homophones しょうがい)
  - 収入 ↔ 支出 (antonym pair: income/expenditure)
  - 就職 ↔ 失業 (antonym pair: employment/unemployment)
- Removed 53 candidates from candidate_words.json (2,725 → 2,672)

### 2026-01-11 (Vocabulary Expansion - 94 New Entries, Session 9)
- Added 94 new dictionary entries from candidate_words_priority.json (2,690 → 2,784 total)
- Completed ALL priority candidates - priority list now empty
- Each entry written individually following entry-guidelines skill
- New entries include N5/N4/N3 vocabulary:
  - N5 Suffixes/Grammar: 〜がる, 〜側, 〜ころ, 〜ずつ, 〜だけ, 〜時, 〜など, 〜屋, お〜, 何〜, そうです
  - N5 Nouns: テープレコーダー, ラジカセ
  - N4 Grammar: 〜てしまう, 〜について, 〜によると
  - N4 Nouns: 泳ぎ方, スーパー, パート, リポート
  - N4 Verbs: 回る, 回す (transitivity pair)
  - N3 Nouns: 前日, 早朝, 祖父母, 体育館, 大量, 大成功, 大都会, 代表者, 男女, 近道, 中心地, 長所, 朝食, 定食, 店内, 電球, 内緒, 仲直り, 長生き, 入社, 人数, 発生, 花束, 花屋, 歯磨き, 半年, 人々, 一人暮らし, 表示, 沸騰, 不用品, 無沙汰, 平方メートル, 返却, 弁護士, 歩行者, 本気, 窓口, ママ, 満点, 身近, 目覚まし時計, 免許証, 申し込み, 申込書, 木曜, 持ち運び, 持ち物, 遊園地, 郵送, 有料, 行き先, 翌朝, 翌年, 汚れ, 予想外, 利用者, 連絡先, 割
  - N3 Verbs: 立て直す, 話しかける, 引き受ける, 身につける, 役立つ, やり直す
  - N3 Adjectives: 力強い, 情けない, 不可能
  - N3 Adverbs: 早めに, 日夜
  - N3 Suffix: 放題
- Priority candidates reduced from 94 to 0

### 2026-01-11 (Vocabulary Expansion - 50 New Entries, Session 8)
- Added 50 new dictionary entries from candidate_words_priority.json (2,442 → 2,690 total)
- Each entry written individually following entry-guidelines skill
- New entries include N5/N3 vocabulary:
  - N5: 四つ (counter), じゃ (conjunction)
  - N3 Nouns: 裏側, 貸出, 片方, 川沿い, 管理人, 外国産, 記念品, 希望者, 共通点, 掲示板, 血液型, 研究所, 交通費, 購入, 最上, 参加者, 試食, 室内, 指導者, 始発, 社員, 車道, 市役所, 集合, 小学生, 小説家, 調べ物, 新入生, 信念, 時差, 実家, 実習, 自動販売機, 事務室, 上空, 正解, 政治家, 正常, 制服, 説明会, 専門家
  - N3 Verbs: 嫌がる, 語り合う, 仕舞う, 知り合う
  - N3 Adjectives: 恋しい, 上品
  - N3 Adverb: 徐々
- Removed 50 candidates from candidate_words_priority.json (144 → 94)

### 2026-01-11 (Vocabulary Expansion - 50 New Entries, Session 7)
- Added 50 new dictionary entries (2,392 → 2,442 total)
- Each entry written individually following entry-guidelines skill
- New entries include N1/N2/N3 vocabulary:
  - Nouns: 経由, 欠陥, 決行, 見当, 高価, 航海, 航空, 光景, 交際, 校舎, 後者, 拘束, 候補, 克服, 穀物, 故人, 今後, 混雑, 婚約, 混乱, 豪華, 合格, 合計, 強盗, 際, 最終, 最中, 境, 作物, 作曲, 作法, 左右, 騒ぎ, 参考, 賛成, 酸素, 材料, 座席, 資格, 支給, 四角, 視覚, 掲示, 語句
  - Adverbs: こんなに, ことによると, ざっと
  - Adjective: けち
  - Expression: こんにちは
  - Pronoun: これら
- Removed 50 candidates from candidate_words.json (2,675 → 2,625)

### 2026-01-11 (Vocabulary Expansion - 51 New Entries, Session 6)
- Added 51 new dictionary entries (2,341 → 2,392 total)
- Entries created from candidate_words.json following updated entry-guidelines skill
- Each entry written individually with proper quality standards
- New entries include N1/N2/N3 vocabulary:
  - Nouns: 経営, 刑事, 血管, 見解, 憲法, 硬貨, 交換, 広告, 攻撃, 高速, 幸福, 興奮, 考慮, 氷, 呼吸, 国籍, 黒板, 国民, 個人, 小銭, 国家, 国会, 国境, 骨折, 小包, 諺, 粉, 好み, 小屋, 誤解, 語学, 差, 才能, 裁判, 作業, 作品, 敬意, 経緯, 契機, 機構, 刑, 季刊, 刊行, 享受, 群, 方々
  - Adverbs: さっぱり, 幸い
  - Verbs: お目に掛かる (humble), チェックする
  - Adjective: 可哀想
- Fixed romanization issue: kooryo → kouryo (考慮)
- Removed 50 candidates from candidate_words.json (2,725 → 2,675)

### 2026-01-11 (Vocabulary Expansion - 47 New Entries, Session 5)
- Added 47 new dictionary entries (2,294 → 2,341 total)
- Added missing basic verb 切る (きる) - to cut
- New entries include N2/N3 vocabulary:
  - Nouns: 景気, 傾向, 警告, 計算, 契約, 化粧, 決心, 決定, 欠点, 血液, 結論, 煙, 健康, 検査, 建設, 建築, 検討, 権利, 芸術, 劇, 劇場, 限界, 現金, 言語, 現象, 減少, 現実, 現状, 現代, 現場, 恋人, 幸運, 効果, 交渉, 行動, 構成, 構造, 向上, 交流, 故郷, 根気, 講演, 考察, 貢献, 後悔, 国語
  - Verb: 切る (to cut)
- Removed 4 duplicate entries (kokusai, konnan, kouhei, kougi already existed)
- Added 1000 new candidates to candidate_words.json (total now 2,725)
- Removed 42 candidates that now exist as entries

### 2026-01-11 (Vocabulary Expansion - 50 New Entries, Session 4)
- Added 50 new dictionary entries (2,244 → 2,294 total)
- New entries include a mix of N2/N3 vocabulary:
  - Nouns: 禁止, 禁煙, 金属, 筋肉, 義務, 疑問, 議論, 銀, 苦痛, 課程, 鐘, 強力, 鎖, 下り, 議員, 議会, 行儀, 近代, 金融, 金額, 金, 切れ, 組, 組合, 暮らし, 暮れ, 苦労, 訓練, 偶然, 具体, 軍, 軍隊, 管, 技師, 議長, 菌, 近視, 金銭, 器官, 歓声, 局, 協調, 狩り, 計
  - Adjectives: 器用, 可哀そう, お洒落
  - Adverbs: ぐっすり
  - Verbs: 逆, 食う
- Fixed 10 prefix directory mismatches (gi*, gy*, ky* entries)
- Fixed 3 cross-reference format issues
- Removed 49 candidates from candidate_words.json

### 2026-01-11 (Vocabulary Expansion - 33 New Entries, Session 3)
- Added 33 new dictionary entries (2,211 → 2,244 total)
- Resolved 5 pending cross-references:
  - 絵 (え) - picture
  - 行き (いき) - going, outward journey
  - 損害 (そんがい) - damage
  - 需要 (じゅよう) - demand
  - 混んでいる (こんでいる) - to be crowded
- Added ~28 high-priority N3/N4 vocabulary including:
  - Nouns: 金, 髪の毛, 活用, 過程, 間隔, 記入, 片付け, 泳ぎ, 外交, 学歴, 癌, 機関, 生地, 気体, 協議, 笑い
  - Adjectives: 苦しい, 急激, 急速, 優しい, もったいない, 最高, 最低
  - Verbs: 苦しむ, 亡くなる, 無くなる
- Cross-references increased from 526 to 567 (97% resolution rate)
- Removed 25 candidates from candidate_words.json

### 2026-01-11 (Vocabulary Expansion - 47 New Entries, Session 2)
- Added 47 new dictionary entries (2,164 → 2,211 total)
- Resolved 11 pending cross-references:
  - Nouns: 終了, 恩人, 担当, 縮小, 負け, 視聴者, 被害, 研究者
  - Verbs: 転がる, 混む, くつろぐ
  - Adverb: つい
  - Expression: 本当は
- Added ~35 high-priority N3/N2 vocabulary candidates including:
  - Nouns: 勘定, 画家, 寄付, 恐怖, 休息, 救助, 教授, 共通, 共同, 株, 感覚, 依頼, 汚染, 絵画, 規制, 供給, 強調, 仮定, 加減, 解釈, 学問, 会合, 競技, 額, 吸収, 柄, 籠, 貸し, 借り
  - Adjectives: 巨大, 温暖, かわいそう, 気の毒
  - Pronoun: あなた
  - Expression: おしゃれ
- Cross-references increased from 491 to 526 (98% resolution rate)
- Removed 35 candidates from candidate_words.json

### 2026-01-11 (Vocabulary Expansion - 47 New Entries)
- Added 47 new dictionary entries (2,117 → 2,164 total)
- Resolved 16 pending cross-references:
  - Nouns: あさねぼう, おゆ, しょうさい, とうちゃく, ふよう, ぼうりょく, りこん, 会員, 会計, 観客, 休暇, 詳細, etc.
  - Verbs: えんきする, かんせいさせる, きえる, ころがす, まげる, りらっくす, すいている
  - Adjectives: しおからい
  - Adverbs/Expressions: じつは, およそ, いつの間にか, 思わず
- Added ~30 high-priority N3/N4 vocabulary candidates including:
  - Nouns: 恩, 覚悟, 係, 拡大, 活気, 感じ, 歓迎, 観察, 感心, 完了, 火災, 驚き, 活躍, 勝ち, etc.
  - Other: お前 (pronoun), 決まり (rule)
- Cross-references increased from 437 to 491 (96% resolution rate)
- Removed 34 candidates from candidate_words.json

### 2026-01-11 (Vocabulary Expansion - 42 New Entries)
- Added 42 new dictionary entries (2,074 → 2,116 total)
- Resolved pending cross-references including へ particle entry
- New entries include:
  - Particle: へ (direction marker)
  - Nouns: はじまり, とかい, やかん, はやおき, きんちょう, けっせき, まんぞく, ふまん, ゆうき, しんじん, こうはい, ひみつ, あいさつ, きずな, たいおう, たいさく, けっこん, etc.
  - Verbs: にがす, ゆらす, おくらせる
  - Adjectives: なつかしい, くわしい, しょっぱい, ふひつよう, らんぼう
  - Adverbs: たいてい, なかなか, ぜひ, まもなく, おそらく, とくに
- Cross-references increased from 400 to 437 (96% resolution rate)
- Removed 18 candidates from candidate_words.json

### 2026-01-11 (Code Quality Improvements)
- Created shared utility modules:
  - `build/path_utils.py`: Consolidated `get_entry_prefix()` from 5 files
  - `build/japanese_utils.py`: Hiragana/romaji conversion, kana mappings
- Made cross-reference resolution deterministic (headword disambiguation for 132 homophone readings)
- Added audio integrity check to `validate.py` (checks for missing/orphaned audio files)
- Made build output deterministic (cleans all generated files before rebuild)
- Fixed double-loading in validation (eliminated ~2074 redundant file reads)
- Migrated all cross-references to structured format (removed legacy string format from schema)
- Updated Python version requirement to 3.10+

### 2026-01-11 (Prefix-Based Subdirectory Reorganization)
- Reorganized entries into prefix-based subdirectories to avoid GitHub's 1,000 file/directory limit
- Entry structure: `entries/{kana}/{prefix}/{id}.json` (prefix = first 2 chars of entry ID)
- HTML output: `docs/entries/{kana}/{prefix}/{id}.html`
- Audio structure: `audio/{kana}/{prefix}/{id}-exN.mp3`
- Updated validation to check prefix directory placement
- Simplified `build/build.py` (SPA version removed, flat HTML is now the only output)
- All 2,074 entries migrated successfully
- Scalable to 10,000+ entries

### 2026-01-10 (Flat HTML Site Build)
- Static HTML site generation (`build/build_flat.py`)
- Each entry gets its own standalone HTML page
- Navigation pages: index.html, search.html, browse.html, recent.html, random.html
- Compact search index with minimal entry data for fast loading
- Works without JavaScript (native HTML5 audio controls, expandable browse sections)
- Cross-reference links work between entry pages

### 2026-01-10 (Audio Pronunciation Support)
- Implemented audio playback for example sentences
- Audio files stored as MP3 in `audio/{kana}/{prefix}/` directory structure
- Web interface shows play/stop buttons for examples with audio
- Created `build/merge_audio.py` for processing new audio files
- Build process copies audio to `docs/audio/` preserving folder structure
- Audio integrity validation added to `validate.py`

### 2026-01-10 (Cross-Reference Linking System)
- Implemented structured cross-reference schema (type, reading, headword, label)
- Added link resolution in build pipeline (`build/resolve_links.py`)
- Added "Related Words" section to entry display in web interface
- Added validation for cross-reference format
- Created `cross-reference-entry` skill for systematic additions
- Reference types: pair, synonym, antonym, keigo, related, see_also, contrast
- Deterministic resolution with headword disambiguation for homophones

### 2026-01-09 (N3 Vocabulary Expansion)
- Added 50 new N3 vocabulary entries from candidate_words.json
- New entries include: na-adjectives (完全, 様々, 正直, 真剣, 深刻, 地味, 重要, 清潔, 積極的, 適切, 奇妙, 公平), nouns (完成, 区別, 現在, 種類, 事件, 状況, 人類, 専攻, 当時, 昼食, 残り, 維持, 一種, 差別, 財産, 使用, 性質, 重大), adverbs (じっと, 既に, 相当, 当然, 常に, 非常, ますます, 主に, 大いに, さて, ただ, 多少, のんびり), verbs (まとまる, 見かける), and other types
- Updated entries_index.json (1,880 entries total)
- Removed 49 added words from candidate_words.json (2,117 remaining)

### 2026-01-08 (Entry Tracking System)
- Created `entries_index.json` listing all 1,153 entries with key metadata
- Created `candidate_words.json` with 1,992 candidate words for future addition
- Added build scripts: `update_entries_index.py`, `manage_candidates.py`, `update_indexes.py`
- Removed N3_VOCABULARY_TO_ADD.md and N4_VOCABULARY_TO_ADD.md (data now in candidate_words.json)

### 2026-01-08 (N4 Vocabulary Expansion)
- Added 183 new N4 vocabulary entries (nouns, katakana loanwords, adverbs, counters, suffixes)
- Total entries now 1,153
- Removed 34 duplicate entries from N3 vocabulary list

### 2026-01-09 (Interface Refinements)
- Removed Compare mode
- Added Recent mode showing most recently added/revised entries (250 entries)
- Added Random mode with word cloud display
- Fixed Browse mode display on narrow screens

### 2026-01-08 (Web Interface Update)
- Added multiple interface modes: Search, Browse
- Sticky header with interface toggle and furigana button
- Browse mode with filters for JLPT level, part of speech, starting kana

### Previous Sessions
- Added 62 N4 vocabulary entries (adverbs, keigo verbs, nouns, katakana loanwords)
- Removed "New" tag functionality from dictionary
- Added vocabulary-notes skill for formatting guidelines
- Updated web interface to handle paragraph breaks and bullet points in notes
- Reformatted 154 entries with proper bullet point formatting

## Next Steps

### Ongoing (Vocabulary Expansion)
1. Continue adding vocabulary from `candidate_words.json` (see workflow below)
2. Maintain v2 quality standards for all new entries
3. Add cross-references when creating new entries

### Future Enhancements
1. Add conjugation search
2. Export to Anki format
3. Create automated test suite for build scripts
4. Add PWA features for offline use

## Workflow: Adding Entries from Candidates

Follow this step-by-step process when adding new dictionary entries from `candidate_words.json`:

### Step 1: Select Candidates
1. Review `candidate_words.json` to choose words to add
2. Prioritize by JLPT level (N5 → N4 → N3) or thematic groups
3. Check that the candidate hasn't already been added to the dictionary

### Step 2: Create Entry Files
1. Create the JSON entry file following the schema (`build/schema.json`)
2. Use the appropriate Claude skill based on entry type:
   - Verbs: `verb-entry` skill
   - Adjectives: `adjective-entry` skill
   - Particles: `particle-entry` skill
   - Others: `other-entries` skill
3. Follow `vocabulary-notes` skill for notes formatting
4. Place file in correct directory based on reading and ID:
   - Directory: `entries/{kana}/{prefix}/` where:
     - `{kana}`: Based on first kana of reading (あ行 → `a/`, か行 → `ka/`, etc.)
     - `{prefix}`: First 2 characters of entry ID (e.g., `taberu_00001` → `ta/`)
   - Example: `entries/ta/ta/taberu_00001.json`
5. File naming: `{romaji}_{5-digit-id}.json`

### Step 3: Validate Entry
```bash
python3 build/validate.py --id {entry_id}
# Or validate all:
python3 build/validate.py
```

### Step 4: Update Indexes
**IMPORTANT: Run this after adding ANY entries:**
```bash
python3 build/update_indexes.py
```
This will:
- Update `entries_index.json` with the new entry
- Remove added words from `candidate_words.json` (sync)

### Step 5: Rebuild Website
**IMPORTANT: Run this to update the GitHub Pages site:**
```bash
python3 build/build_flat.py
```
This regenerates all HTML files in `docs/` which GitHub Pages serves. Without this step, new entries won't appear on the live site.

### Step 6: Add Cross-References
1. Use the `cross-reference-entry` skill for guidelines
2. Add structured references for:
   - Transitivity pairs (for verbs)
   - Keigo equivalents
   - Antonyms/opposites
   - Related vocabulary mentioned in notes
3. References can point to entries that don't exist yet

### Step 7: Commit Changes
Commit all changes including:
- New entry JSON files in `entries/`
- Updated `entries_index.json` and `candidate_words.json`
- Rebuilt `docs/` folder (required for GitHub Pages to update)

## Workflow: Adding Audio Files

### Step 1: Prepare Audio Files
Place MP3 files in `audio-to-add/` with the naming convention:
```
{entry_id}-ex{number}.mp3
```
Example: `taberu_00001-ex1.mp3` for the first example of entry `taberu_00001`

### Step 2: Merge Audio
```bash
python3 build/merge_audio.py
```
This will:
- Copy MP3 files to `audio/{kana}/{prefix}/` directory
- Update entry files to set `has_audio: true` on examples

### Step 3: Build and Test
```bash
python3 build/build.py
# Open docs/index.html to verify audio plays correctly
```

### Audio Directory Structure
Audio files are organized by kana and prefix (matching entries/):
```
audio/
├── a/           # あ行
│   ├── a_/      # Entries starting with 'a_'
│   ├── am/      # Entries starting with 'am'
│   └── ...
├── ka/          # か行
│   ├── ka/      # Entries starting with 'ka'
│   └── ...
└── ...
```

## Workflow: Adding Cross-References to Entries

### Cross-Reference Format
```json
"cross_references": [
  {
    "type": "pair",
    "reading": "しまる",
    "headword": "{閉|し}まる",
    "label": "intransitive"
  }
]
```

### Reference Types
| Type | Use For | Example |
|------|---------|---------|
| `pair` | Transitivity pairs | 閉める → 閉まる |
| `antonym` | Opposites | 大きい → 小さい |
| `keigo` | Honorific/humble | 食べる → 召し上がる |
| `synonym` | Similar meaning | 分かる → 理解する |
| `contrast` | Easily confused | は → が |
| `related` | Semantically connected | 食べる → 食べ物 |
| `see_also` | General reference | - |

## Technical Notes

### Build Commands
```bash
# Validate entries (includes schema, cross-refs, audio integrity)
python3 build/validate.py

# Validate a single entry
python3 build/validate.py --id taberu_00001

# Merge new audio files (from audio-to-add/)
python3 build/merge_audio.py

# Build dictionary
python3 build/build.py

# Update index files (after adding/removing entries)
python3 build/update_indexes.py

# Manage candidate words
python3 build/manage_candidates.py stats    # Show statistics
python3 build/manage_candidates.py add "漢字" "かんじ" "notes"  # Add candidate

# Cross-reference resolution report
python3 build/resolve_links.py

# View locally
open docs/index.html
```

### File Naming Convention
- Format: `{romanized_reading}_{5-digit-id}.json`
- Romanization: Modified Hepburn with kana-faithful long vowels
- Directory: `entries/{kana}/{prefix}/` where:
  - `{kana}`: Based on first kana of reading (あ → `a/`, か → `ka/`, etc.)
  - `{prefix}`: First 2 characters of entry ID (e.g., `taberu` → `ta/`)
- Example: `entries/ta/ta/taberu_00001.json`
- Katakana loanwords: Use hiragana reading (e.g., アルバイト → あるばいと)

### Entry and Candidate Tracking
- **entries_index.json**: Auto-generated index of all dictionary entries
- **candidate_words.json**: Words to potentially add (each has unique ID like C00001)
- Run `python build/update_indexes.py` after modifying entries to keep indexes in sync

## Notes for AI Assistants

### Before Starting Work
1. Read this file to understand current state
2. Check `project_specification_v2.md` for detailed quality standards
3. Relevant skills will be auto-loaded based on task type

### Entry Requirements
- All kanji must have furigana: `{漢字|かんじ}`
- 2-3 example sentences minimum
- Examples progress from simple to complex
- Include at least one collocation or fixed phrase
- Katakana loanwords use hiragana in reading field

### Quality Standards
See `project_specification_v2.md` for comprehensive guidelines. Key points:
- **Verbs**: Transitivity type, pair verb, aspect/ている behavior, collocations
- **Particles**: Predicates requiring particle, contrast with similar particles
- **Adjectives**: Forms (adverbial, noun), similar word distinctions
- **All entries**: Consistent depth with similar entries

### After Each Session
Update this file with:
- Entries added/revised
- Any issues encountered
- Next steps
