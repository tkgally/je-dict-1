# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-16
**Current phase**: Phase 4 - N4 Vocabulary Expansion & Interface Enhancement

**Live site**: https://tkgally.github.io/je-dict-1/

## Current State

### Phase
**Phase 4: N4 Vocabulary Expansion & Interface Enhancement** - Adding N4 vocabulary while maintaining v2 quality standards, plus new web interface features.

### Infrastructure Status
- [x] Directory structure created (prefix-based subdirectories for scalability)
- [x] JSON schema defined (`build/schema.json`)
- [x] Validation script working (`build/validate.py`)
- [x] Build script working (`build/build_flat.py`)
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
- **Total entries**: 5,207
- **JLPT N5 coverage**: ~95% complete
- **JLPT N4 coverage**: ~500 entries added
- **JLPT N3 vocabulary**: ~2,600 entries added
- **Candidate words**: ~1,548 words tracked in `candidate_words.json`
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
| `find-candidates` | Finding new candidate words for the dictionary |
| `resolve-duplicates` | Identifying and resolving duplicate entries |
| `delete-entry` | Safely deleting entries with proper cleanup |

## Recent Changes

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 57)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Occupations (15): {看護師|かんごし} (nurse), {警察官|けいさつかん} (police officer), {消防士|しょうぼうし} (firefighter), {銀行員|ぎんこういん} (bank employee), エンジニア (engineer), プログラマー (programmer), デザイナー (designer), シェフ (chef), コック (cook), ウェイター (waiter), ウェイトレス (waitress), ガイド (guide), {役者|やくしゃ} (actor), アイドル (idol), モデル (model)
- Natural disasters (4): {津波|つなみ} (tsunami), {洪水|こうずい} (flood), {雪崩|なだれ} (avalanche), {干|ひ}ばつ (drought)
- Colors (2): {金色|きんいろ} (gold), {銀色|ぎんいろ} (silver)
- Household items (6): {扇風機|せんぷうき} (electric fan), {炬燵|こたつ} (kotatsu), アイロン (iron), ベランダ (balcony), ガレージ (garage), ドライヤー (hair dryer)
- Health/Medical (2): ワクチン (vaccine), マスク (mask)
- Vehicles (5): {救急車|きゅうきゅうしゃ} (ambulance), {消防車|しょうぼうしゃ} (fire engine), パトカー (police car), バイク (motorcycle), ヘリコプター (helicopter)
- Business terms (10): {競合|きょうごう} (competition), {卸売|おろしうり} (wholesale), {小売|こうり} (retail), {発注|はっちゅう} (ordering), {受注|じゅちゅう} (receiving orders), {納品|のうひん} (delivery), {出荷|しゅっか} (shipping), {関税|かんぜい} (tariff), {物流|ぶつりゅう} (logistics), {流通|りゅうつう} (distribution)
- Abstract concepts (18): {願望|がんぼう} (desire), {欲望|よくぼう} (craving), {情熱|じょうねつ} (passion), {熱意|ねつい} (enthusiasm), やる{気|き} (motivation), {認識|にんしき} (recognition), {了解|りょうかい} (acknowledgment), {同意|どうい} (consent), {合意|ごうい} (agreement), {連携|れんけい} (cooperation), {規模|きぼ} (scale), {運営|うんえい} (management), {正義|せいぎ} (justice), {倫理|りんり} (ethics), {発言|はつげん} (statement), {討論|とうろん} (debate), {辛抱|しんぼう} (patience), {世代|せだい} (generation)
- Technology (6): アカウント (account), ブログ (blog), モニター (monitor), {充電器|じゅうでんき} (charger), {録音|ろくおん} (recording), アップデート (update)
- Math/Science (11): {百科事典|ひゃっかじてん} (encyclopedia), {代数|だいすう} (algebra), {幾何|きか} (geometry), {微分|びぶん} (differentiation), {積分|せきぶん} (integration), {定数|ていすう} (constant), {演算|えんざん} (operation), ハードウェア (hardware), ウェブサイト (website), {見積|みつも}もり (estimate), {株価|かぶか} (stock price)
- Education (4): {不合格|ふごうかく} (failure), {休学|きゅうがく} (leave of absence), {留年|りゅうねん} (repeating a year), {参考書|さんこうしょ} (reference book), {法則|ほうそく} (law/rule)
- Other vocabulary (17): カラオケ (karaoke), {舅|しゅうと} (father-in-law), {姑|しゅうとめ} (mother-in-law), ジーパン (jeans), {化粧品|けしょうひん} (cosmetics), {日焼|ひや}け{止|ど}め (sunscreen), {山葵|わさび} (wasabi), {皺|しわ} (wrinkle), {黒子|ほくろ} (mole), {齧|かじ}る (to gnaw), {啜|すす}る (to sip), むせる (to choke), {浮|う}き{浮|う}き (cheerful), しゃっくり (hiccup), クワガタ (stag beetle), ゴキブリ (cockroach)

Notable entry features:
- Business vocabulary covers supply chain and commerce terminology
- Math/Science entries include calculus and computer science vocabulary
- Abstract concept entries useful for academic and philosophical discussions
- Cross-references added linking related terms (発注↔受注, 物流↔流通)

Total entries: 5,107 → 5,207
Remaining candidates: 1,652 → 1,548

### 2026-01-16 (Candidate Words Expansion - 200 New Candidates)
Added 200 new candidates to `candidate_words.json` using the balanced coverage strategy:

- **Tier 1 - Core Vocabulary Gaps** (20 candidates): Basic vocabulary including 事 (こと), 黄 (yellow), 白 (white), 多分 (probably), counters (個, 枚, 冊, 台), verbs (点ける, 返す), adjectives (早い, 速い, 可愛い, 固い, 素敵, 綺麗), and conjunctions (ただし, そうすると).

- **Tier 2 - Semantic Domain Completion** (42 candidates): Food/cooking (麺, ラーメン, 煮込む, 和える, 漬ける, 揚げる, すりおろす, 泡立てる), body parts (腸, 肺, 腎臓), cultural terms (床の間, 風呂敷, 提灯, 暖簾, 初詣, 七五三, 盆踊り, 鳥居, お守り), family terms (従兄弟, 叔父, 叔母, 甥, 彼氏), music (曲, 楽器, ライブ), sports (バスケ, バレー, 練習), everyday items (カバン, メガネ, エアコン, バイク, 乗り換え, 終電), work (不合格, 部下, ボーナス), and places (消防署, 役所).

- **Tier 3 - Related Word Networks** (54 candidates): Emotional terms (焦り, 苛立ち, 戸惑い, 安堵, 憂鬱, 苦悩, 葛藤, 羨望, 嫉妬, 悲しみ, 恐れ), antonym pairs (内外, 表裏, 出入り, 開閉, 長短, 大小, 強弱, 高低, 軽重, 善悪, 正誤), communication verbs (説明する, 質問する, 励ます, 感謝する, 同意する, 反対する, 賛成する, 提案する, 議論する), cognition verbs (気づく, 理解する, 想像する, 考慮する, 判断する, 否定する, 予想する, 期待する, 心配する, 安心する), and compound verbs (切り離す, 押し入る, 取り込む, 追いかける, 追い払う, 巻き込む, 呼びかける, 見分ける, 聞き直す, 引き返す, 降り立つ).

- **Tier 4 - Productive Patterns** (56 candidates): ～的 adjectives (経済的, 歴史的, 文化的, 国際的, 科学的, 精神的, 物理的, 心理的, 論理的, 感情的), reduplication (段々, 堂々, 延々, 粛々, 淡々), four-character idioms (三日坊主, 七転八起, 四面楚歌, 一朝一夕, 起死回生, 弱肉強食, 臨機応変, 有名無実, 一心不乱, 我田引水, 異口同音, 因果応報, 暗中模索, 五里霧中), proverbs (猿も木から落ちる, 七転び八起き, 石の上にも三年, 早起きは三文の徳, 百聞は一見に如かず, 井の中の蛙, 蛙の子は蛙, 花より団子, 二兎を追う者は一兎をも得ず, 急がば回れ), number compounds (二重, 四季, 五感, 六法, 七夕, 八方, 九九, 百万, 千円, 万人, 一人前, 二度と), and onomatopoeia (ぴかぴか, ふわふわ, さらさら, ぼろぼろ, がたがた, ばらばら, きらきら, しとしと, ざあざあ, ぽたぽた, もぐもぐ, ぺらぺら, ぐるぐる, ばたばた, にこにこ).

- **Tier 5 - Modern & Informal Vocabulary** (28 candidates): Technology (アップデート, クリック, タップ, スワイプ, ログイン, パスワード, シェア, いいね, コメント, バグ, アカウント, プロフィール, オンライン, オフライン), lifestyle abbreviations (就活, 婚活, 終活, バイト), and social media (炎上, 既読).

Total candidates: 1,452 → 1,652

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 56)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Sports (12): {野球|やきゅう} (baseball), サッカー (soccer), バスケットボール (basketball), バレーボール (volleyball), ゴルフ (golf), マラソン (marathon), ジム (gym), ヨガ (yoga), ジョギング (jogging), スポーツ (sports), {決勝|けっしょう} (final), {予選|よせん} (preliminary)
- Music terms (5): リズム (rhythm), テンポ (tempo), {和音|わおん} (chord), {旋律|せんりつ} (melody), {音階|おんかい} (scale)
- Technology/Computing (15): サーバー (server), クラウド (cloud), ネットワーク (network), アップロード (upload), インストール (install), {更新|こうしん} (update), {設定|せってい} (settings), {入力|にゅうりょく} (input), {出力|しゅつりょく} (output), セキュリティ (security), {暗号|あんごう} (encryption), バックアップ (backup), ブラウザ (browser), アプリケーション (application), クライアント (client)
- AI/Computing (2): {人工知能|じんこうちのう} (AI), {機械学習|きかいがくしゅう} (machine learning)
- Business/Finance (15): {株式|かぶしき} (stock), {融資|ゆうし} (financing), {返済|へんさい} (repayment), {合併|がっぺい} (merger), {買収|ばいしゅう} (acquisition), {消費税|しょうひぜい} (consumption tax), {賃金|ちんぎん} (wages), {不況|ふきょう} (recession), {好況|こうきょう} (boom), インフレ (inflation), デフレ (deflation), {円高|えんだか} (strong yen), {円安|えんやす} (weak yen), {金利|きんり} (interest rate), {雇用|こよう} (employment)
- Education (5): {大学院|だいがくいん} (graduate school), {予備校|よびこう} (prep school), {専門学校|せんもんがっこう} (vocational school), {履修|りしゅう} (course registration), {工学|こうがく} (engineering)
- Science (4): {仮説|かせつ} (hypothesis), {定義|ていぎ} (definition), {分類|ぶんるい} (classification), {検証|けんしょう} (verification)
- Math (4): {方程式|ほうていしき} (equation), {関数|かんすう} (function), {変数|へんすう} (variable), グラフ (graph)
- Society/Politics (8): {内閣|ないかく} (cabinet), {介護|かいご} (nursing care), {少子化|しょうしか} (declining birthrate), {高齢化|こうれいか} (aging), {貧困|ひんこん} (poverty), {格差|かくさ} (disparity), {条約|じょうやく} (treaty), {社会保障|しゃかいほしょう} (social security)
- Sports results (6): {勝敗|しょうはい} (victory/defeat), {引|ひ}き{分|わ}け (draw), {得点|とくてん} (score), {準優勝|じゅんゆうしょう} (runner-up), {準決勝|じゅんけっしょう} (semifinal), {所得税|しょとくぜい} (income tax)
- Communication (4): {発信|はっしん} (transmission), {受信|じゅしん} (reception), {配信|はいしん} (streaming), {合唱|がっしょう} (chorus)
- Abstract concepts (13): {本質|ほんしつ} (essence), {反応|はんのう} (reaction), {改革|かいかく} (reform), {達成|たっせい} (achievement), {可能性|かのうせい} (possibility), {必要性|ひつようせい} (necessity), {重要性|じゅうようせい} (importance), {多様性|たようせい} (diversity), {最大|さいだい} (maximum), {最小|さいしょう} (minimum), {最新|さいしん} (latest), {標準|ひょうじゅん} (standard), ボランティア (volunteer)
- Tech hardware (7): コピー (copy), {圧縮|あっしゅく} (compression), {容量|ようりょう} (capacity), {解像度|かいぞうど} (resolution), ディスプレイ (display), メモリ (memory), {筋|きん}トレ (strength training)

Notable entry features:
- Computing entries include both Japanese and English terminology used in tech contexts
- Business/Finance terms cover modern economic vocabulary
- Cross-references added linking related terms (発信↔受信, 合唱↔独唱)
- Sports vocabulary includes competition terminology

Total entries: 5,007 → 5,107
Remaining candidates: 1,552 → 1,452

### 2026-01-15 (Vocabulary Expansion - 100 New Entries, Session 55)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Core vocabulary (5): {豚|ぶた} (pig), {羊|ひつじ} (sheep), {本当|ほんとう}に (really), {確|たし}かに (certainly), ピンク (pink)
- Modern/Slang vocabulary (21): スマホ, アプリ, ダウンロード, {検索|けんさく}, フォロー, {投稿|とうこう}, バズる, {推|お}し, コスパ, タイパ, リモート, マジ, やばい, めっちゃ, ウザい, ダサい, キモい, エモい, ガチ, イケメン, ネタバレ
- 四字熟語 (7): {一石二鳥|いっせきにちょう}, {以心伝心|いしんでんしん}, {一期一会|いちごいちえ}, {十人十色|じゅうにんといろ}, {四苦八苦|しくはっく}, {一長一短|いっちょういったん}, {自業自得|じごうじとく}
- ～的 adjectives (13): {消極的|しょうきょくてき}, {具体的|ぐたいてき}, {抽象的|ちゅうしょうてき}, {一般的|いっぱんてき}, {基本的|きほんてき}, {個人的|こじんてき}, {社会的|しゃかいてき}, {効果的|こうかてき}, {現実的|げんじつてき}, {理想的|りそうてき}, {魅力的|みりょくてき}, {典型的|てんけいてき}, {伝統的|でんとうてき}
- Reduplication (4): {日々|ひび}, {国々|くにぐに}, {山々|やまやま}, {木々|きぎ}
- Compound verb (1): {呼|よ}び{出|だ}す (to call out)
- Onomatopoeia (12): ひらひら, ゆらゆら, すれすれ, がらがら, へらへら, むすっと, ぷりぷり, うんざり, げんなり, しんみり, ぱさぱさ, ほかほか
- Emotional vocabulary (15): {哀愁|あいしゅう}, {羞恥|しゅうち}, {孤独|こどく}, {充実|じゅうじつ}, {虚無|きょむ}, {軽蔑|けいべつ}, {惨|みじ}め, {屈辱|くつじょく}, {焦燥|しょうそう}, {切望|せつぼう}, {愛着|あいちゃく}, {落胆|らくたん}, {絶望|ぜつぼう}, {憎悪|ぞうお}, {未練|みれん}
- Business terms (11): {戦略|せんりゃく}, {方針|ほうしん}, {業績|ぎょうせき}, {損失|そんしつ}, {商談|しょうだん}, {企画|きかく}, {手当|てあて}, {福利厚生|ふくりこうせい}, {確定申告|かくていしんこく}, {源泉徴収|げんせんちょうしゅう}, {見積|みつも}り
- Household/Environment (11): インターホン, {表札|ひょうさつ}, {郵便受|ゆうびんう}け, ブラインド, ブレスレット, ブローチ, {世界遺産|せかいいさん}, {天然記念物|てんねんきねんぶつ}, {保護区|ほごく}, {給湯器|きゅうとうき}, {電化製品|でんかせいひん}

Notable entry features:
- Modern slang includes internet/social media terms popular with younger generations
- 四字熟語 entries include origin, literal meaning, and modern usage contexts
- ～的 adjectives cover common academic and formal vocabulary
- Emotional vocabulary useful for literature and nuanced expression
- Business terms cover tax, HR, and corporate planning terminology

Total entries: 4,907 → 5,007
Remaining candidates: 1,831 → 1,552

### 2026-01-15 (Candidate Words Expansion - 200 New Candidates)
Added 200 new candidates to `candidate_words.json` using the balanced coverage strategy outlined in `newcandidates.md`:

- **Tier 1 - Core Vocabulary Gaps** (70 candidates): Essential verbs missing from the dictionary including 行く, 来る, 見る, 聞く, 言う, 思う, 知る, 分かる, 食べる, 飲む, 書く, 読む, plus transitive/intransitive pairs like 開ける/開く, 閉める/閉じる, 始まる/始める, 終わる/終える. Also added missing basic adjectives (早い, 熱い), adverbs (本当に, 多分, 確かに), and nouns (事).

- **Tier 2 - Semantic Domain Completion** (70 candidates): Action verbs (走る, 歩く, 泳ぐ, 飛ぶ), emotion verbs (怒る, 笑う, 泣く, 喜ぶ, 驚く, 困る), change-of-state verbs (壊れる/壊す, 変わる/変える, 増える, 減る), plus missing colors (白, ピンク), animals (豚, 羊), family terms (叔父, 叔母).

- **Tier 3 & 4 - Related Word Networks & Productive Patterns** (35 candidates): Reduplication words (日々, 国々, 山々, 木々), ～的 adjectives (消極的, 具体的, 抽象的, 一般的, 基本的, 個人的, 社会的, 効果的, 現実的, 理想的, 魅力的, 典型的, 伝統的), compound verbs (追い出す, 取り出す, 持ち上げる, 引き受ける, 飛び出す, 思い出す, 呼び出す), and four-character idioms (一石二鳥, 以心伝心, 一期一会, 十人十色, 四苦八苦, 一長一短, 自業自得).

- **Tier 5 - Modern & Informal Vocabulary** (25 candidates): Technology terms (スマホ, アプリ, ダウンロード, 検索), social media vocabulary (フォロー, 投稿, バズる, 推し), lifestyle terms (コスパ, タイパ, リモート), and colloquial expressions (マジ, やばい, めっちゃ, ウザい, ダサい, キモい, エモい, ガチ, イケメン, 草, 神, ネタバレ).

Total candidates: 1,631 → 1,831

### 2026-01-15 (Vocabulary Expansion - 50 New Entries, Session 54)
Added 50 new dictionary entries from candidate_words.json, focusing on verbs, kitchen appliances, household items, accessories, work/business vocabulary, education, and technology:

- Verbs (4): {砕|くだ}ける (to break into pieces), {挟|はさ}まる (to be caught between), {照|て}らす (to illuminate), {落|お}ち{着|つ}く (to calm down)
- Kitchen Appliances (6): バター (butter), {乾燥機|かんそうき} (dryer), {食器洗|しょっきあら}い{機|き} (dishwasher), オーブン (oven), トースター (toaster), ミキサー (blender)
- Household Items (3): コンロ (stove), {換気扇|かんきせん} (ventilation fan), シンク (sink)
- Clothing/Accessories (8): {衣類|いるい} (clothing), ベスト (vest), ストッキング (stockings), タイツ (tights), イヤリング (clip-on earrings), ピアス (pierced earrings), {日傘|ひがさ} (parasol)
- Work/Business (14): {昇給|しょうきゅう} (salary increase), {降格|こうかく} (demotion), リストラ (restructuring), {求人|きゅうじん} (job offer), {履歴書|りれきしょ} (resume), {月給|げっきゅう} (monthly salary), {時給|じきゅう} (hourly wage), {賞与|しょうよ} (bonus), {年金|ねんきん} (pension), {経費|けいひ} (expenses), {領収書|りょうしゅうしょ} (receipt), {請求書|せいきゅうしょ} (invoice), {見積|みつも}り (estimate), {取引|とりひき} (transaction), {在庫|ざいこ} (inventory)
- Education (5): {塾|じゅく} (cram school), {幼稚園|ようちえん} (kindergarten), {保育園|ほいくえん} (nursery school), {入試|にゅうし} (entrance exam), {学費|がくひ} (tuition)
- Science/Technology (10): {辞書|じしょ} (dictionary), {理論|りろん} (theory), {概念|がいねん} (concept), {投資|とうし} (investment), {赤字|あかじ} (deficit), {黒字|くろじ} (surplus), アルゴリズム (algorithm), ソフトウェア (software), データベース (database), インターネット (internet)

Notable entry features:
- Verb entries include transitivity pairs and aspect notes
- Business vocabulary covers employment cycle, financial documents, and inventory management
- Education entries explain Japanese education system distinctions (幼稚園 vs 保育園, 塾 vs 予備校)
- Technology entries include modern IT terminology with Japanese usage notes

Total entries: 4,857 → 4,907
Remaining candidates: 1,680 → 1,631

### 2026-01-14 (Candidate Words Expansion - 201 New Candidates)
Added 201 new candidates to `candidate_words.json` using systematic semantic gap analysis across multiple domains:

- **Emotions/psychological terms** (21): 哀愁, 羞恥, 孤独, 充実, 虚無, 軽蔑, 惨め, 屈辱, 焦燥, 切望, 愛着, 落胆, 絶望, 憎悪, 未練, 恥辱, 怨念, 悔恨, 狂喜, 憤慨
- **Compound verbs** (24): 閉め出す, 売り出す, 送り出す, 抜け出す, 逃げ出す, 流れ出す, 染み出す, 溢れ出す, 浮き上がる, 舞い上がる, 呼び込む, 誘い込む, 突き刺す, 突き飛ばす, 投げ捨てる, 殴り倒す, 蹴り飛ばす, 踏みつける, 抱きしめる, 引きずる, 引き寄せる, 押し倒す, 張り付く, 絞り込む
- **Onomatopoeia** (11): ひらひら, ゆらゆら, すれすれ, がらがら, へらへら, むすっと, ぷりぷり, うんざり, げんなり, しんみり, ぱさぱさ, ほかほか
- **Modern/technology terms** (32): プログラミング, コーディング, デバッグ, バグ, プロフィール, プッシュ通知, リモートワーク, 在宅勤務, オンライン会議, ウェブ会議, ビデオ通話, 画面共有, コンテンツ, インフルエンサー, ユーチューバー, 投げ銭, スタートアップ, イノベーション, ソリューション, サステナブル, SDGs, カーボンニュートラル, 脱炭素, 電動, 蓄電, ドローン, 自動運転, ロボット, IoT, 仮想通貨, ブロックチェーン, QRコード
- **Traditional Japanese items & ceremonies** (18): 掛け軸, 屏風, 座布団, ちゃぶ台, 火鉢, 紋付, 手拭い, 番傘, 蛇の目傘, 硯, 香炉, お中元, お歳暮, 祝儀, 不祝儀, 香典, 年賀状, 喪中
- **四字熟語 & proverbs** (27): 我田引水, 森羅万象, 言語道断, 四面楚歌, 針小棒大, 馬耳東風, 青天霹靂, 晴耕雨読, 竜頭蛇尾, 呉越同舟, 画竜点睛, 二律背反, 天変地異, 自暴自棄, 有言実行, 能ある鷹は爪を隠す, 虻蜂取らず, 井の中の蛙, 鬼に金棒, 花より団子, 七転び八起き, 灯台下暗し, 良薬口に苦し, 情けは人の為ならず, 豚に真珠, 猫の手も借りたい, 馬の耳に念仏
- **Body/medical terms** (15): 骨格, 横隔膜, 粘膜, 皮下, 表皮, 発熱, 筋肉痛, 動悸, 息切れ, 痙攣
- **～的 adjectives** (9): 直接的, 間接的, 自発的, 強制的, 悲観的, 楽観的, 建設的, 破壊的, 支配的
- **Food/cooking terms** (14): すりおろす, 汁物, 具材, 冷凍食品, 加工食品, 生鮮食品, 保存料, 添加物, 賞味期限, 消費期限, カロリー, 栄養素, 炭水化物
- **Business/commerce terms** (30): 認定, 取消, 施行, 遵守, 保活, 朝活, ノマド, キャッシュレス, ペーパーレス, コワーキング, フリーランス, ベンチャー, 電子決済, キャッシュバック, ポイント還元, クーポン, 送料, 年会費, 入会金, 解約, 延長, 有効期限, 返金, 不具合, 問い合わせ, 納品書, 明細, 契約書, 同意書

Total candidates: 1,479 → 1,680

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 53)
Added 50 new dictionary entries from candidate_words.json, focusing on household items, clothing, accessories, and work vocabulary:

- Kitchen Utensils (10): ざる (colander), おたま (ladle), へら (spatula), {菜箸|さいばし} (cooking chopsticks), {汁椀|しるわん} (soup bowl), {小皿|こざら} (small plate), {大皿|おおざら} (large plate), {湯呑|ゆの}み (teacup), {箸置|はしお}き (chopstick rest), ボウル (mixing bowl)
- Home/Living Items (10): ソファ (sofa), テーブル (table), {本棚|ほんだな} (bookshelf), クローゼット (closet), {扉|とびら} (door), {縁側|えんがわ} (veranda), {絨毯|じゅうたん} (carpet), シーツ (sheets), ベッド (bed), シャワー (shower)
- Bathroom Items (5): スポンジ (sponge), シャンプー (shampoo), {歯|は}ブラシ (toothbrush), バスタオル (bath towel), {便器|べんき} (toilet bowl)
- Clothing (10): パジャマ (pajamas), ブラウス (blouse), カーディガン (cardigan), ジャケット (jacket), パーカー (hoodie), ワンピース (dress), スニーカー (sneakers), ブーツ (boots), スリッパ (slippers), マフラー (scarf)
- Accessories (5): サングラス (sunglasses), {腕時計|うでどけい} (wristwatch), ネックレス (necklace), リュック (backpack), {団扇|うちわ} (round fan)
- Work Vocabulary (10): {勤務|きんむ} (work), {出勤|しゅっきん} (going to work), {退勤|たいきん} (leaving work), {有給|ゆうきゅう} (paid leave), {昇進|しょうしん} (promotion), {転勤|てんきん} (job transfer), {転職|てんしょく} (job change), {退職|たいしょく} (resignation), {解雇|かいこ} (dismissal), {採用|さいよう} (hiring)

Notable entry features:
- Comprehensive household vocabulary useful for daily life in Japan
- Clothing entries include both loanwords and the casual/formal distinctions in Japanese
- Work vocabulary covers the full employment lifecycle with cultural notes on Japanese workplace culture
- All entries include common expressions and related vocabulary

Total entries: 4,807 → 4,857
Remaining candidates: 1,529 → 1,479

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 52)
Added 50 new dictionary entries from candidate_words.json, focusing on technology/electronics, media/broadcasting, and traditional Japanese arts:

- Technology/Electronics (15): {画面|がめん} (screen), キーボード (keyboard), マウス (mouse), プリンター (printer), カメラ (camera), スピーカー (speaker), イヤホン (earphones), ヘッドホン (headphones), バッテリー (battery), {充電|じゅうでん} (charging), {電源|でんげん} (power supply), コンセント (outlet), ケーブル (cable), {携帯電話|けいたいでんわ} (mobile phone), スマートフォン (smartphone)
- Media/Communication (12): メール (email), チャット (chat), ニュース (news), {報道|ほうどう} (news coverage), {編集|へんしゅう} (editing), {見出|みだ}し (headline), {録画|ろくが} (recording), {再生|さいせい} (playback), {動画|どうが} (video), {映像|えいぞう} (footage), {音声|おんせい} (audio), {字幕|じまく} (subtitles)
- Fine Arts (3): {美術|びじゅつ} (fine arts), {彫刻|ちょうこく} (sculpture), {陶芸|とうげい} (pottery)
- Traditional Japanese Arts (5): {華道|かどう} (flower arrangement), {茶道|さどう} (tea ceremony), {剣道|けんどう} (kendo), {弓道|きゅうどう} (archery), {空手|からて} (karate)
- Performing Arts (7): {歌舞伎|かぶき} (kabuki), {狂言|きょうげん} (kyogen), {落語|らくご} (rakugo), {漫才|まんざい} (manzai), {脚本|きゃくほん} (script), {演出|えんしゅつ} (direction), {視聴|しちょう} (viewing)
- Musical Instruments (5): ギター (guitar), フルート (flute), ドラム (drums), {三味線|しゃみせん} (shamisen), {尺八|しゃくはち} (shakuhachi)
- Other (3): オーケストラ (orchestra), {購読|こうどく} (subscription), チャンネル (channel)

Notable entry features:
- Comprehensive technology vocabulary for modern life and digital communication
- Traditional Japanese arts entries include major schools, equipment, and cultural context
- Performing arts entries cover traditional comedy, theater, and modern media
- Musical instrument entries include both Western and Japanese traditional instruments

Total entries: 4,757 → 4,807
Remaining candidates: 1,579 → 1,529

### 2026-01-14 (Candidate Words Expansion - 202 New Candidates)
Added 202 new candidates to `candidate_words.json` using systematic semantic gap analysis:

- **Medical/anatomical terms** (15): 肩甲骨, 肋骨, 骨盤, 脊椎, 靭帯, 軟骨, 毛細血管, リンパ, 通院, 処方, 感染, 炎症, 切り傷, 応急処置, 健康診断
- **Four-character idioms & proverbs** (9): 二束三文, 三日坊主, 青息吐息, 本末転倒, 猿も木から落ちる, 石の上にも三年, 塵も積もれば山となる, 棚から牡丹餅, 一朝一夕
- **Emotional/psychological terms** (8): 倦怠, 嫌悪, 渇望, 郷愁, 陶酔, 恍惚, 虚脱, 緊迫
- **Traditional culture** (6): 褌, 朱肉, 御神籤, お宮参り, 告別式, 初七日, 四十九日, 一周忌, 三回忌, 法要
- **Honorific vocabulary** (9): お越しになる, 存じる, 頂戴する, 拝借する, お供する, 恐れ入る, 差し支える, お手数, ご容赦
- **Sports & music terms** (14): ドリブル, シュート, オフサイド, ファウル, ゴールキーパー, フォワード, ミッドフィルダー, ディフェンダー, スタメン, アレンジ, リフ, ビート, アドリブ, アンコール
- **Business & finance** (10): 配当, 財務, 経理, 監査, 決算, 収益, 抵当, 担保, 手形, 小切手
- **Transportation** (9): 滑走路, 離陸, 着陸, 搭乗, 乗車, 優先席, 車内, 車掌, 運転士
- **Construction & architecture** (13): 施工, 骨組み, 外壁, 内装, 断熱, 防水, 耐震, 解体, 改築, 増築, 修繕, 塗装, 足場
- **Agriculture** (12): 耕作, 播種, 灌漑, 肥料, 害虫, 苗床, 果樹園, 酪農, 牧場, 飼育, 家畜, 堆肥
- **Modern vocabulary** (6): マウント, チルい, パワハラ, モラハラ, セクハラ, マタハラ
- **Social media slang** (6): リツイート, ハッシュタグ, ネタ, 空気を読む, KY, ガチ勢
- **Environment & energy** (8): 省エネ, ゴミ分別, 埋立地, 太陽光, 風力, 原子力, 水力, 炭素
- **Other categories** (77): Various nouns, verbs, adjectives, and number compounds

Total candidates: 1,377 → 1,579

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 51)
Added 50 new dictionary entries from candidate_words.json, focusing on animal classification, exotic animals, tree types, Japanese cooking methods, and household vocabulary:

- Loanwords (2): ルール (rule), レベル (level)
- Animal classification (6): {哺乳類|ほにゅうるい} (mammal), {爬虫類|はちゅうるい} (reptile), {両生類|りょうせいるい} (amphibian), {魚類|ぎょるい} (fish class), {鳥類|ちょうるい} (bird class), {甲虫|こうちゅう} (beetle)
- Insects/creatures (3): {蚯蚓|みみず} (earthworm), {毛虫|けむし} (caterpillar), {穴熊|あなぐま} (badger)
- Birds (4): {孔雀|くじゃく} (peacock), {白鳥|はくちょう} (swan), {鷺|さぎ} (heron), {鸚鵡|おうむ} (parrot)
- Exotic animals (5): {獅子|しし} (lion), {河馬|かば} (hippopotamus), {麒麟|きりん} (giraffe), {縞馬|しまうま} (zebra), {駱駝|らくだ} (camel)
- Tree classification (5): {樹木|じゅもく} (tree), {広葉樹|こうようじゅ} (broadleaf), {針葉樹|しんようじゅ} (conifer), {落葉樹|らくようじゅ} (deciduous), {常緑樹|じょうりょくじゅ} (evergreen)
- Plants (2): {菖蒲|あやめ} (iris), {蔦|つた} (ivy)
- Japanese cooking methods (7): {佃煮|つくだに} (tsukudani), {煮物|にもの} (simmered dish), {焼|や}き{物|もの} (grilled dish), {揚|あ}げ{物|もの} (fried food), {蒸|む}し{物|もの} (steamed dish), {和|あ}え{物|もの} (dressed dish), {酢|す}の{物|もの} (vinegared dish)
- Japanese dishes/food (7): {焼肉|やきにく} (yakiniku), {雑炊|ぞうすい} (rice porridge), {茶漬|ちゃづ}け (ochazuke), {吸|す}い{物|もの} (clear soup), {饅頭|まんじゅう} (manju), {羊羹|ようかん} (yokan), {洋菓子|ようがし} (Western sweets)
- Meal structure (3): {前菜|ぜんさい} (appetizer), {副菜|ふくさい} (side dish), {主菜|しゅさい} (main dish)
- Household/architecture (6): {玄関|げんかん} (entrance), {廊下|ろうか} (hallway), {天井|てんじょう} (ceiling), {柱|はしら} (pillar), {箪笥|たんす} (chest of drawers), {洋服|ようふく} (Western clothes)

Notable entry features:
- Complete animal classification system with related terms cross-referenced
- Comprehensive Japanese cooking method vocabulary with examples
- Tree classification entries cover both botanical and practical information
- All entries include cultural notes where relevant

Total entries: 4,707 → 4,757
Remaining candidates: 1,840 → 1,783

### 2026-01-14 (Duplicate Entry Cleanup)
Removed 112 duplicate entries (63 duplicate sets) using the new resolve-duplicates and delete-entry skills. Entry count reduced from 4,819 to 4,707.

Added two new Claude Code skills:
- `resolve-duplicates`: Guidelines for identifying, comparing, and safely removing duplicate entries
- `delete-entry`: Step-by-step process for safely deleting entries while updating indexes and cross-references

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 50)
Added 50 new dictionary entries from candidate_words.json, focusing on Japanese food, cooking ingredients, kitchen items, and nature vocabulary:

- Food ingredients (15): {出汁|だし} (soup stock), {味醂|みりん} (mirin), {胡麻油|ごまあぶら} (sesame oil), {小麦粉|こむぎこ} (wheat flour), {片栗粉|かたくりこ} (potato starch), パン{粉|こ} (breadcrumbs), {豆腐|とうふ} (tofu), {納豆|なっとう} (natto), こんにゃく (konjac), {昆布|こんぶ} (kelp), {鰹節|かつおぶし} (dried bonito), {漬物|つけもの} (pickles), {食材|しょくざい} (ingredient), {調味料|ちょうみりょう} (seasoning), {香辛料|こうしんりょう} (spice)
- Japanese dishes (10): {寿司|すし} (sushi), {天|てん}ぷら (tempura), {唐揚|からあ}げ (fried chicken), {焼|や}き{鳥|とり} (yakitori), {味噌汁|みそしる} (miso soup), おにぎり (rice ball), {煎餅|せんべい} (rice cracker), {団子|だんご} (dumpling), {和菓子|わがし} (Japanese sweets), {薬味|やくみ} (condiment)
- Kitchen & household (12): {家電|かでん} (appliances), {掃除機|そうじき} (vacuum), {洗濯機|せんたくき} (washing machine), {炊飯器|すいはんき} (rice cooker), {電子|でんし}レンジ (microwave), {包丁|ほうちょう} (kitchen knife), まな{板|いた} (cutting board), {急須|きゅうす} (teapot), {石鹸|せっけん} (soap), {歯磨|はみが}き{粉|こ} (toothpaste), {浴槽|よくそう} (bathtub), {洗面台|せんめんだい} (washstand)
- Nature & plants (8): {稲妻|いなずま} (lightning), {苔|こけ} (moss), {茸|きのこ} (mushroom), {雑草|ざっそう} (weed), {紫陽花|あじさい} (hydrangea), {向日葵|ひまわり} (sunflower), {朝顔|あさがお} (morning glory)
- Birds & insects (5): {鴉|からす} (crow), {雀|すずめ} (sparrow), {鳩|はと} (pigeon), {昆虫|こんちゅう} (insect), {蛾|が} (moth), {蠅|はえ} (fly)

Notable entry features:
- Extensive coverage of Japanese food culture with cooking terminology
- Kitchen appliance entries include Japanese-specific features and brands
- All food entries include types, preparation methods, and cultural context
- Nature entries feature seasonal significance and traditional associations

Total entries: 4,769 → 4,819
Remaining candidates: 1,904 → 1,840

---

**Archive Note**: Only the 10 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).


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
python3 build/build_flat.py

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
2. Relevant skills will be auto-loaded based on task type (see Claude Code Skills table above)
3. Use the `entry-guidelines` skill for general quality standards

### Entry Requirements
- All kanji must have furigana: `{漢字|かんじ}`
- 2-3 example sentences minimum
- Examples progress from simple to complex
- Include at least one collocation or fixed phrase
- Katakana loanwords use hiragana in reading field
- **sense_numbers required**: All examples must have `sense_numbers` field populated
  - Single-sense entries: use `[1]` for all examples
  - Multi-sense entries: each example must specify which sense(s) it illustrates

### Quality Standards
See the `entry-guidelines` skill for comprehensive guidelines. Key points:
- **Verbs**: Transitivity type, pair verb, aspect/ている behavior, collocations
- **Particles**: Predicates requiring particle, contrast with similar particles
- **Adjectives**: Forms (adverbial, noun), similar word distinctions
- **All entries**: Consistent depth with similar entries

### After Each Session
Update the "Recent Changes" section in this file with:
- Entries added/revised
- Any issues encountered

**Note**: Keep only the 10 most recent change entries. When adding a new entry, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
