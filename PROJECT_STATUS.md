# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-14
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
- **Total entries**: 4,857
- **JLPT N5 coverage**: ~95% complete
- **JLPT N4 coverage**: ~450 entries added
- **JLPT N3 vocabulary**: ~2,300 entries added
- **Candidate words**: ~1,680 words tracked in `candidate_words.json`
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

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 49)
Added 50 new dictionary entries from candidate_words.json, focusing on verbs, environmental/scientific terms, medical vocabulary, and useful suffixes:

- Verbs (27): {透|す}ける (to be transparent), {滲|にじ}む (to blur), {滴|したた}る (to drip), {舞|ま}う (to dance/flutter), {暴|あば}れる (to act violently), {荒|あ}れる (to be rough), {静|しず}まる (to become quiet), {老|お}いる (to grow old), {衰|おとろ}える (to decline), {早|はや}まる (to quicken), {早|はや}める (to hasten), {枯|か}れる (to wither), {萎|しお}れる (to wilt), {芽生|めば}える (to sprout), {蒸|む}れる (to be stuffy), {揺|ゆ}する (to shake), {括|くく}る (to bundle), {絡|から}める (to entwine), {着替|きが}える (to change clothes), {漁|あさ}る (to rummage), {暴|あば}く (to expose), {晒|さら}す (to expose), {逃|のが}す (to let escape), {拒|こば}む (to refuse), {跳|は}ね{上|あ}がる (to jump up), {吹|ふ}き{飛|と}ばす (to blow away), {焦|あせ}る (to be impatient)
- Environmental terms (11): {温暖化|おんだんか} (global warming), リサイクル (recycling), {生態系|せいたいけい} (ecosystem), {気候変動|きこうへんどう} (climate change), {二酸化炭素|にさんかたんそ} (carbon dioxide), {排出|はいしゅつ} (emission), {廃棄物|はいきぶつ} (waste), {再生可能|さいせいかのう} (renewable), {持続可能|じぞくかのう} (sustainable), {生物多様性|せいぶつたようせい} (biodiversity), {絶滅危惧種|ぜつめつきぐしゅ} (endangered species)
- Medical/Health terms (5): {体調|たいちょう} (physical condition), アレルギー (allergy), {脳卒中|のうそっちゅう} (stroke), {鬱病|うつびょう} (depression), {関節痛|かんせつつう} (joint pain)
- Nature/Time terms (3): {言|い}い{訳|わけ} (excuse), {朝焼|あさや}け (morning glow), {日没|にちぼつ} (sunset)
- Suffixes (4): 〜{社|しゃ} (company), 〜{者|しゃ} (person), 〜{団|だん} (group), 〜{長|ちょう} (head/leader)

Notable entry features:
- Comprehensive verb entries with transitivity pairs and ている aspect behavior
- Environmental vocabulary highly relevant for current events discussions
- Medical terms cover common conditions and health-related expressions
- All suffixes include extensive compound word lists

Total entries: 4,719 → 4,769
Remaining candidates: 1,950 → 1,904

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 48)
Added 50 new dictionary entries from candidate_words.json, focusing on animals, plants/trees, and medical/health terms:

- Insects (5): {蝶|ちょう} (butterfly), {蟻|あり} (ant), {蚊|か} (mosquito), {蝸牛|かたつむり} (snail), {蛙|かえる} (frog)
- Reptiles/Sea creatures (8): {蜥蜴|とかげ} (lizard), {鰐|わに} (crocodile), {鯨|くじら} (whale), {海豚|いるか} (dolphin), {鮫|さめ} (shark), {烏賊|いか} (squid), {蛸|たこ} (octopus), {蟹|かに} (crab)
- Birds (4): {鷲|わし} (eagle), {梟|ふくろう} (owl), {鶴|つる} (crane), {燕|つばめ} (swallow)
- Mammals (8): {狼|おおかみ} (wolf), {狐|きつね} (fox), {狸|たぬき} (raccoon dog), {熊|くま} (bear), {鹿|しか} (deer), {猪|いのしし} (wild boar), {栗鼠|りす} (squirrel), {蝙蝠|こうもり} (bat)
- Plants/Trees (15): {幹|みき} (trunk), {蕾|つぼみ} (bud), {花弁|かべん} (petal), {花粉|かふん} (pollen), {楓|かえで} (maple), {銀杏|いちょう} (ginkgo), {桃|もも} (peach), {柿|かき} (persimmon), {栗|くり} (chestnut), {薔薇|ばら} (rose), {百合|ゆり} (lily), {藤|ふじ} (wisteria), {椿|つばき} (camellia), {檜|ひのき} (Japanese cypress), {笹|ささ} (bamboo grass)
- Medical/Health (10): {花粉症|かふんしょう} (hay fever), {糖尿病|とうにょうびょう} (diabetes), {高血圧|こうけつあつ} (high blood pressure), {心臓病|しんぞうびょう} (heart disease), {認知症|にんちしょう} (dementia), {嗅覚|きゅうかく} (sense of smell), {味覚|みかく} (sense of taste), {触覚|しょっかく} (sense of touch), くしゃみ (sneeze), {鼻水|はなみず} (runny nose)

Notable entry features:
- Animal entries include counters, cultural notes, and figurative expressions (e.g., {狐|きつね}と{狸|たぬき}の{化|ば}かし{合|あ}い)
- Plant entries feature seasonal significance and traditional uses (e.g., {笹|ささ} for Tanabata)
- Medical terms cover common conditions relevant to aging society (diabetes, dementia, hypertension)
- All entries include common collocations, proverbs where relevant, and cross-references

Total entries: 4,669 → 4,719
Remaining candidates: 2,000 → 1,950

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 47)
Added 50 new dictionary entries from candidate_words.json, focusing on health/medical vocabulary, nature/geography terms, and astronomy:

- Katakana loanwords (10): ユーモア, ヨット, ヨーロッパ, ライター, ラケット, ラベル, ロケット, パイプ, ノー, タイプライター
- Health/medical terms (10): {副作用|ふくさよう}, {捻挫|ねんざ}, {打撲|だぼく}, {凍傷|とうしょう}, {腹痛|ふくつう}, {腰痛|ようつう}, {吐|は}き{気|け}, {眩暈|めまい}, {倦怠感|けんたいかん}, {不眠症|ふみんしょう}
- Body parts & biology (10): {歯茎|はぐき}, {太腿|ふともも}, {脹脛|ふくらはぎ}, {内臓|ないぞう}, {肝臓|かんぞう}, {細胞|さいぼう}, {遺伝子|いでんし}, {免疫|めんえき}, {視力|しりょく}, {聴力|ちょうりょく}
- Nature/geography (10): {草原|そうげん}, {湿地|しっち}, {峡谷|きょうこく}, {洞窟|どうくつ}, {断崖|だんがい}, {入|い}り{江|え}, {浜|はま}, {霞|かすみ}, {木陰|こかげ}, {日向|ひなた}
- Astronomy/sky (10): {夕焼|ゆうや}け, {黄昏|たそがれ}, {月明|つきあ}かり, {星空|ほしぞら}, {流|なが}れ{星|ぼし}, {天|あま}の{川|がわ}, {銀河|ぎんが}, {惑星|わくせい}, {彗星|すいせい}, {隕石|いんせき}

Notable entry features:
- Medical terms include symptoms, conditions, and body parts useful for healthcare situations
- Nature terms cover diverse landscapes and weather phenomena
- Astronomy entries include cultural references (Tanabata, seasonal observations)
- All entries include common expressions, collocations, and related vocabulary

Total entries: 4,619 → 4,669
Remaining candidates: 2,043 → 2,000

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
