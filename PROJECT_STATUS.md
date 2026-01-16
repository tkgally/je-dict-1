# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-16
**Current phase**: Phase 4 - Vocabulary Expansion & Interface Enhancement

**Live site**: https://tkgally.github.io/je-dict-1/

## Current State

### Phase
**Phase 4: Vocabulary Expansion & Interface Enhancement** - Adding vocabulary while maintaining v2 quality standards, plus new web interface features. The dictionary uses an original three-tier vocabulary classification (basic, core, general) instead of JLPT levels.

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
- **Total entries**: 5,807
- **Vocabulary tier assignment**: Pending (all entries have vocabulary_tier: null)
- **Candidate words**: ~1,067 words tracked in `candidate_words.json`
- **Priority candidates**: 0 words remaining in `candidate_words_priority.json` (all 94 completed)
- **Cross-references**: 567 total (555 resolved, 97% resolution rate)
- **Audio files**: 1,028 MP3 files covering example sentences

### Vocabulary Tier System
The dictionary uses a three-tier vocabulary classification system (see vocabulary-tiers skill):
- **Basic**: 600-800 fundamental words for basic communication
- **Core**: 1,600-2,000 words for adult-level communication
- **General**: All other vocabulary useful for learners

Tier assignment is pending. Once complete, entries will be categorized for progressive learning.

### Entry Breakdown by Type
| Type | Count | Notes |
|------|-------|-------|
| Verbs | ~1,200 | Includes transitivity and aspect info |
| Nouns | ~2,500 | Includes katakana loanwords |
| Adjectives | ~400 | I-adjectives and na-adjectives |
| Adverbs | ~200 | Time, manner, degree adverbs |
| Particles | 10 | Core particles with predicate lists |
| Counters | ~50 | Common counting patterns |
| Keigo verbs | 12 | Honorific and humble forms |
| Other | ~1,100 | Expressions, onomatopoeia, suffixes, etc. |

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

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 64)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Suru verbs (10): {質問|しつもん}する (to ask), {説明|せつめい}する (to explain), {紹介|しょうかい}する (to introduce), {約束|やくそく}する (to promise), {報告|ほうこく}する (to report), {賛成|さんせい}する (to agree), {反対|はんたい}する (to oppose), {邪魔|じゃま}する (to disturb), {電話|でんわ}する (to call), お{願|ねが}いする (to request)
- Four-character idioms (7): {試行錯誤|しこうさくご} (trial and error), {自画自賛|じがじさん} (self-praise), {無我夢中|むがむちゅう} (being absorbed), {臨機応変|りんきおうへん} (flexibility), {五里霧中|ごりむちゅう} (bewilderment), {異口同音|いくどうおん} (unanimous), {油断大敵|ゆだんたいてき} (complacency warning)
- ～的 adjectives (15): {歴史的|れきしてき} (historical), {論理的|ろんりてき} (logical), {経済的|けいざいてき} (economical), {科学的|かがくてき} (scientific), {感情的|かんじょうてき} (emotional), {本格的|ほんかくてき} (full-scale), {技術的|ぎじゅつてき} (technical), {政治的|せいじてき} (political), {心理的|しんりてき} (psychological), {文化的|ぶんかてき} (cultural), {実践的|じっせんてき} (practical), {理論的|りろんてき} (theoretical), {創造的|そうぞうてき} (creative), {客観的|きゃっかんてき} (objective), {主観的|しゅかんてき} (subjective)
- ～やか adjectives (6): {爽|さわ}やか (refreshing), {鮮|あざ}やか (vivid), {和|なご}やか (harmonious), {健|すこ}やか (healthy), のどか (peaceful), {朗|ほが}らか (cheerful)
- Adverbs (12): もしかして (perhaps), いっそ (rather), {何|なに}しろ (after all), いかにも (indeed), かろうじて (barely), ひたすら (earnestly), もっぱら (exclusively), ひそかに (secretly), まれに (rarely), ひとまず (for now), おおむね (generally), あらかじめ (beforehand)
- Compound verbs (15): {引|ひ}き{込|こ}む (to draw in), {持|も}ち{歩|ある}く (to carry around), {生|い}き{返|かえ}る (to revive), {締|し}め{切|き}る (to close off), {切|き}り{開|ひら}く (to pioneer), {切|き}り{捨|す}てる (to cut off), {流|なが}れ{込|こ}む (to flow in), {落|お}ち{込|こ}む (to fall into), {巻|ま}き{込|こ}む (to involve), {受|う}け{入|い}れる (to accept), {受|う}け{止|と}める (to catch), {立|た}て{替|か}える (to pay for), {乗|の}り{出|だ}す (to set out), {切|き}り{離|はな}す (to separate), {押|お}し{出|だ}す (to push out)
- Onomatopoeia (10): にやにや (grinning), げらげら (guffawing), くすくす (giggling), めそめそ (sobbing), もぐもぐ (munching), ごくごく (gulping), ちびちび (sipping), ずるずる (slurping), すやすや (sleeping soundly), ぽかぽか (warmly)
- Cultural vocabulary (8): {床|とこ}の{間|ま} (alcove), {風呂敷|ふろしき} (wrapping cloth), {提灯|ちょうちん} (paper lantern), {暖簾|のれん} (shop curtain), {初詣|はつもうで} (first shrine visit), {還暦|かんれき} (60th birthday), {厄年|やくどし} (unlucky year), {大晦日|おおみそか} (New Year's Eve)
- Emotional nouns (5): {焦|あせ}り (impatience), {苛立|いらだ}ち (irritation), {戸惑|とまど}い (confusion), {安堵|あんど} (relief), {憂鬱|ゆううつ} (depression)
- Cooking vocabulary (5): {煮込|にこ}む (to simmer), {和|あ}える (to dress food), {惣菜|そうざい} (prepared food), {下|した}ごしらえ (food prep), {味付|あじつ}け (seasoning)
- Modern abbreviations (2): {就活|しゅうかつ} (job hunting), {婚活|こんかつ} (marriage hunting)
- Additional onomatopoeia (5): ぬくぬく (snugly warm), じめじめ (damp), からっと (dry/crispy), こそこそ (sneakily), さっさと (quickly)

Notable entry features:
- Common suru verbs essential for basic communication
- Four-character idioms with explanations of origins and usage
- Comprehensive ～的 adjective coverage for academic contexts
- Traditional Japanese cultural vocabulary with detailed notes
- Emotional noun entries useful for nuanced expression
- Cooking terms covering food preparation methods
- Cross-references added linking antonym pairs ({賛成|さんせい}↔{反対|はんたい}, {客観的|きゃっかんてき}↔{主観的|しゅかんてき})

Total entries: 5,707 → 5,807
Remaining candidates: 1,167 → 1,067

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 63)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Body postures/verbs (8): しゃがむ (to squat), {跪|ひざまず}く (to kneel), {屈|かが}む (to crouch), {反|そ}る (to bend backward), {捻|ひね}る (to twist), うつ{伏|ぶ}せ (face down), {仰向|あおむ}け (face up), {膝枕|ひざまくら} (lap pillow)
- Geometry (8): {立方体|りっぽうたい} (cube), {円錐|えんすい} (cone), {円柱|えんちゅう} (cylinder), {球|きゅう} (sphere), {多角形|たかっけい} (polygon), {対角線|たいかくせん} (diagonal), {弧|こ} (arc), {放物線|ほうぶつせん} (parabola)
- Opposite pairs (10): {内外|ないがい} (inside and outside), {大小|だいしょう} (large and small), {長短|ちょうたん} (long and short), {表裏|ひょうり} (front and back), {出入|でい}り (going in and out), {開閉|かいへい} (opening and closing), {高低|こうてい} (high and low), {軽重|けいちょう} (light and heavy), {善悪|ぜんあく} (good and evil), {正誤|せいご} (right and wrong)
- Abstract concepts (15): {信頼性|しんらいせい} (reliability), {効率性|こうりつせい} (efficiency), {透明性|とうめいせい} (transparency), {柔軟性|じゅうなんせい} (flexibility), {汎用性|はんようせい} (versatility), {利便性|りべんせい} (convenience), {耐久性|たいきゅうせい} (durability), {整合性|せいごうせい} (consistency), {持続性|じぞくせい} (sustainability), {即効性|そっこうせい} (quick effectiveness), {再現性|さいげんせい} (reproducibility), {公平性|こうへいせい} (fairness), {合理性|ごうりせい} (rationality), {独自性|どくじせい} (originality), {普遍性|ふへんせい} (universality)
- Events/Ceremonies (7): {卒業式|そつぎょうしき} (graduation ceremony), お{正月|しょうがつ} (New Year), お{盆|ぼん} (Obon festival), {七五三|しちごさん} (Shichi-Go-San), {節分|せつぶん} (Setsubun), {歓迎会|かんげいかい} (welcome party), {送別会|そうべつかい} (farewell party)
- Nature/Geography (6): {干潟|ひがた} (tidal flat), {荒野|こうや} (wilderness), {湿原|しつげん} (wetland), {水源|すいげん} (water source), {原野|げんや} (prairie), {河口|かこう} (river mouth)
- Tools (6): コンパス (compass), {分度器|ぶんどき} (protractor), {虫眼鏡|むしめがね} (magnifying glass), {巻|ま}き{尺|じゃく} (tape measure), {万力|まんりき} (vise), {梃子|てこ} (lever)
- Technology (8): SNS (social media), ウェブ (web), サイト (site), ブラウザ (browser), スクリーンショット (screenshot), {英和|えいわ} (English-Japanese), ハッシュタグ (hashtag), {画像|がぞう}{編集|へんしゅう} (image editing)
- Modern vocabulary (8): タピオカ (tapioca), ペットボトル (plastic bottle), フリーター (freeter), ニート (NEET), {非正規|ひせいき} (non-regular), {正社員|せいしゃいん} (full-time employee), {派遣|はけん} (temporary worker), {契約|けいやく}{社員|しゃいん} (contract employee)
- Business/formal (24): {委託|いたく} (consignment), {懸念|けねん} (concern), {顕著|けんちょ} (remarkable), {獲得|かくとく} (acquisition), {把握|はあく} (grasp), {暫定|ざんてい} (provisional), {妥当|だとう} (appropriate), {端末|たんまつ} (terminal), {拠点|きょてん} (base), {趣旨|しゅし} (gist), {指摘|してき} (pointing out), {是正|ぜせい} (correction), {促進|そくしん} (promotion), {抑制|よくせい} (suppression), {固有|こゆう} (inherent), {不十分|ふじゅうぶん} (insufficient), {革新|かくしん} (innovation), {保持|ほじ} (retention), {遂行|すいこう} (accomplishment), {簡潔|かんけつ} (concise)

Notable entry features:
- Comprehensive geometry vocabulary extending beyond basic shapes
- Abstract concept entries useful for academic and business discussions
- Opposite pair vocabulary commonly used in formal writing
- Employment status terms reflecting modern Japanese workforce categories
- Cross-reference added linking antonyms ({促進|そくしん}↔{抑制|よくせい})

Total entries: 5,607 → 5,707
Remaining candidates: 1,252 → 1,167

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 62)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Geometry (13): {三角形|さんかくけい} (triangle), {四角形|しかくけい} (quadrilateral), {正方形|せいほうけい} (square), {長方形|ちょうほうけい} (rectangle), {直線|ちょくせん} (straight line), {曲線|きょくせん} (curve), {円周|えんしゅう} (circumference), {直径|ちょっけい} (diameter), {直角|ちょっかく} (right angle), {平行|へいこう} (parallel), {垂直|すいちょく} (perpendicular), {傾斜|けいしゃ} (slope), {頂点|ちょうてん} (vertex)
- Position/Process (12): {内側|うちがわ} (inside), {外側|そとがわ} (outside), {由来|ゆらい} (origin), {手順|てじゅん} (procedure), {手続|てつづ}き (procedure), {方式|ほうしき} (method), {様式|ようしき} (style), パターン (pattern), {終点|しゅうてん} (terminal), {中間|ちゅうかん} (middle), {領域|りょういき} (domain), {順序|じゅんじょ} (order)
- Business/Finance (15): {配送|はいそう} (delivery), {返品|へんぴん} (return), {決済|けっさい} (settlement), {入金|にゅうきん} (deposit), {出金|しゅっきん} (withdrawal), {利息|りそく} (interest), {原価|げんか} (cost), {単価|たんか} (unit price), {総額|そうがく} (total amount), {数量|すうりょう} (quantity), {分量|ぶんりょう} (amount), {重量|じゅうりょう} (weight), {年収|ねんしゅう} (annual income), プレゼン (presentation), ミーティング (meeting)
- Tools (10): {金槌|かなづち} (hammer), {鋸|のこぎり} (saw), ドライバー (screwdriver), {懐中電灯|かいちゅうでんとう} (flashlight), {物差|ものさ}し (ruler), {電卓|でんたく} (calculator), {顕微鏡|けんびきょう} (microscope), {望遠鏡|ぼうえんきょう} (telescope), {体温計|たいおんけい} (thermometer), {体重計|たいじゅうけい} (scale)
- Plants/Nature (5): たんぽぽ (dandelion), チューリップ (tulip), サボテン (cactus), {苗|なえ} (seedling), {蝋燭|ろうそく} (candle)
- Ceremonies (3): {結婚式|けっこんしき} (wedding), {成人式|せいじんしき} (coming-of-age), {入学式|にゅうがくしき} (entrance ceremony)
- Geography (5): ジャングル (jungle), {高原|こうげん} (plateau), {海辺|うみべ} (seaside), {群島|ぐんとう} (archipelago), {本土|ほんど} (mainland)
- Occupations (3): {写真家|しゃしんか} (photographer), {秘書|ひしょ} (secretary), {駅員|えきいん} (station staff)
- Culture (2): {茶道|ちゃどう} (tea ceremony), バンド (band)
- Body/Sleep (2): いびき (snoring), {寝返|ねがえ}り (turning over in sleep)
- Office supplies (2): ホッチキス (stapler), クリップ (clip)
- Advice (3): {助言|じょげん} (advice), {忠告|ちゅうこく} (warning), {要請|ようせい} (request)
- Abstract (20): ブーム (boom), {名声|めいせい} (fame), {任務|にんむ} (duty), {役職|やくしょく} (position), {階級|かいきゅう} (class), {描写|びょうしゃ} (description), {苦悩|くのう} (anguish), {対処|たいしょ} (dealing with), {措置|そち} (measure), {処分|しょぶん} (disposal), {監視|かんし} (surveillance), {修行|しゅぎょう} (training), {慣習|かんしゅう} (custom), {中世|ちゅうせい} (medieval), {活力|かつりょく} (vitality), {精力|せいりょく} (energy), {見識|けんしき} (insight), {野望|やぼう} (ambition), {必然|ひつぜん} (inevitability), {象徴|しょうちょう} (symbol)
- Adverbs (5): {極|きわ}めて (extremely), {若干|じゃっかん} (some), {次第|しだい}に (gradually), {無論|むろん} (of course), {仲直|なかなお}り (reconciliation)

Notable entry features:
- Comprehensive geometry vocabulary for mathematical contexts
- Business/finance terms covering transactions and measurements
- Tool vocabulary useful for daily life and DIY contexts
- Abstract concepts covering emotions, social status, and philosophical terms

Total entries: 5,507 → 5,607
Remaining candidates: 1,351 → 1,252

### 2026-01-16 (Candidate Words Expansion - 200 New Candidates, Session 61)
Added 200 new candidates to `candidate_words.json` using balanced coverage strategy:

- **Semantic Domain Completion** (~73 candidates): Body functions (欠伸, げっぷ, 瞬き, 咳払い), body parts (舌先, 踝), animals (ゴリラ, チンパンジー, アザラシ, ペンギン, バッタ, カマキリ, てんとう虫, クワガタムシ, 蜜蜂), weather (靄, 霙, 竜巻), clothing (襟, 裾, チャック, マフラー), kitchen items (鍋敷き, お椀, マグカップ), appliances (下駄箱, 加湿器, 除湿機, 空気清浄機), transportation (踏切, 横断歩道, 歩道橋, 地下道, 路地, ガードレール), medical (処方箋, 抗体), occupations (建築家, 会計士, 税理士, 司法書士, 行政書士, 不動産屋, 営業マン, サラリーマン), sports (連覇, 打者, 投手, 自己ベスト), music (不協和音, 伴奏, 奏者, 指揮者, バース, コーラス), housing (間取り, 敷金, 礼金, 退去, 管理費, 共益費, 賃貸, 分譲, 新築), finance (電子マネー, クレジットカード, ローン, 債務), education (試験期間, 期末試験, 中間試験, 追試験)

- **Related Word Networks** (~31 candidates): Compound verbs (取り返す, 振り回す, 叩き込む, 見過ごす, 切り抜く), conjunctions (然しながら, にも関わらず), adverbs (わざわざ, 敢えて, 残らず, 強いて, 否応なく, 尚更, 一切, 最早), discourse markers (いずれにせよ, ともかく, どうせ, どのみち, さすがに, 到底, どうやら), onomatopoeia (きっぱり, こってり, いよいよ, じわじわ, ぽつぽつ), personality adjectives (愚か, 素直, しつこい, 健気)

- **Productive Patterns** (~41 candidates): ～的 adjectives (物質的, 公的, 私的, 内的, 外的), four-character idioms (取捨選択, 創意工夫, 全身全霊, 心機一転, 絶体絶命), grammatical expressions (に関して, において, に対して, によって, として, にとって, をもって, に際して), shape adjectives (細長い, 平たい), compound verbs with ～出す/～上がる/～替える (吹き出す, 泣き出す, 笑い出す, 走り出す, 飛び上がる, 盛り上がる, 履き替える, 出直す, 焦がす)

- **Modern & Informal Vocabulary** (~36 candidates): Casual expressions (ムカつく, イケてる, ググる, ぴえん, ガチで), business/IT loanwords (アジェンダ, フィードバック, ストレージ, IT, テイクアウト, デリバリー, ドリンクバー, コーデ, トレンド, アイテム, フェス, カバー, ID, Bluetooth, デバイス), casual speech patterns (なんて, っていう, ていうか, つーか, なんだかんだ, 知らんけど), fillers/particles (えーと, あのー, ほら, ねえ, よね, やっぱ), contracted forms (ちゃう, なきゃ, っぽい, そこそこ)

- **Domain-Specific Vocabulary** (~19 candidates): Emotions (悔い, 情け, 悩み), cooking (火加減, 手際, コツ, 隠し味, 香ばしい, 瑞々しい), nature (小川), housing (ロフト, バルコニー), personality/character traits (物覚え, 思いやり, 気配り, 心掛け, 志, やり甲斐, 生き甲斐, 甲斐甲斐しい, 億劫, 鈍感, 敏感, 不器用, 頑固, 図太い, 生真面目, 無口, 口下手, せっかち, そそっかしい)

Total candidates: 1,151 → 1,351

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 60)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Verbs (15): {映|ば}える (to look good), {手放|てばな}す (to let go), {垂|た}らす (to drip), {怒鳴|どな}る (to shout), {呟|つぶや}く (to mutter), {膨|ふく}らむ (to swell), {萎|しぼ}む (to wilt), {焦|こ}げる (to burn), {喚|わめ}く (to scream), {咎|とが}める (to blame), {寝|ね}ぼける (to be drowsy), {抓|つね}る (to pinch), しゃぶる (to suck), {欠伸|あくび}する (to yawn), くしゃみする (to sneeze)
- Onomatopoeia (25): くるくる (spinning), ばたばた (flapping), きゅっと (tightly), ぎゅっと (squeezing), ぱっと (suddenly), さっと (quickly), はっと (startled), ぎらぎら (glaring), てかてか (shiny), もこもこ (fluffy), ぼこぼこ (bumpy), すらすら (smoothly), ぶつぶつ (grumbling), ぴんぴん (lively), びしょびしょ (soaked), ふらふら (unsteady), よろよろ (tottering), おろおろ (flustered), いそいそ (eagerly), おどおど (timidly), ちくちく (prickly), しくしく (sobbing), ひやひや (anxious), めらめら (blazing), ぺたぺた (sticking)
- School terms (5): {部活|ぶかつ} (club activities), {生徒会|せいとかい} (student council), {職員室|しょくいんしつ} (staff room), {保健室|ほけんしつ} (nurse's office), {図書室|としょしつ} (library room)
- Health (5): {下痢|げり} (diarrhea), {便秘|べんぴ} (constipation), インフルエンザ (influenza), {包帯|ほうたい} (bandage), {絆創膏|ばんそうこう} (adhesive bandage)
- Nature (6): {紅葉|もみじ} (maple/autumn leaves), {葉|は}っぱ (leaf), {磯|いそ} (rocky shore), {珊瑚|さんご} (coral), {崖|がけ} (cliff), あられ (hail)
- Technology (8): ユーザー (user), フォルダ (folder), タップ (tap), サブスク (subscription), テレワーク (telework), ワイファイ (WiFi), {生配信|なまはいしん} (live streaming), エコ (eco)
- Media controls (3): {一時停止|いちじていし} (pause), {早送|はやおく}り (fast forward), {巻|ま}き{戻|もど}し (rewind)
- Emotions (4): {悲|かな}しみ (sadness), {恐|おそ}れ (fear), {嫉妬|しっと} (jealousy), {葛藤|かっとう} (conflict)
- Arts/crafts (4): {折|お}り{紙|がみ} (origami), {生|い}け{花|ばな} (ikebana), {舞踊|ぶよう} (dance), {刺繍|ししゅう} (embroidery)
- Political terms (4): {民主主義|みんしゅしゅぎ} (democracy), {資本主義|しほんしゅぎ} (capitalism), {社会主義|しゃかいしゅぎ} (socialism), {人権|じんけん} (human rights)
- Finance (6): {口座|こうざ} (bank account), {預金|よきん} (deposit), {振込|ふりこみ} (transfer), {残高|ざんだか} (balance), {手数料|てすうりょう} (handling fee), {値引|ねび}き (discount)
- Games (2): パズル (puzzle), オセロ (Othello)
- Live performance (1): ライブ (live concert)
- Misc (3): {真夜中|まよなか} (midnight), {染|し}み (stain), {麦|むぎ} (wheat/barley)
- Animal sounds (2): わんわん (bow-wow), にゃんにゃん (meow)
- Expressions (3): まあまあ (so-so), みたいな (like), じゃん (isn't it)
- Clothing (4): Tシャツ (T-shirt), ジャンパー (jacket), キャップ (cap), スニーカー (sneakers)

Notable entry features:
- Comprehensive onomatopoeia covering movement, texture, emotions, and states
- Japanese school-specific vocabulary (部活, 生徒会, etc.)
- Cross-references added linking antonyms (下痢↔便秘, 早送り↔巻き戻し)
- Political vocabulary useful for news and academic contexts
- Finance terms essential for daily life in Japan

Total entries: 5,407 → 5,507
Remaining candidates: 1,354 → 1,247

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 59)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Onomatopoeia (20): さらさら (smooth/rustling), ぺらぺら (fluent), とろとろ (thick/gooey), ねばねば (sticky), ぱりぱり (crispy), もちもち (chewy), がんがん (pounding), ずきずき (throbbing), ひりひり (stinging), じんじん (tingling), むかむか (nauseous), びくびく (nervous), そわそわ (restless), はらはら (anxious), ぼーっと (spaced out), うとうと (drowsy), うっとり (enchanted), ぞっと (shuddering), へとへと (exhausted), がたがた (rattling)
- Technology (7): クリック (click), ログイン (login), パスワード (password), オンライン (online), ネット (internet), ファイル (file), タブレット (tablet)
- Household items (10): エアコン (air conditioner), ヒーター (heater), リモコン (remote), ケトル (kettle), ポット (pot), {爪切|つめき}り (nail clippers), しゃもじ (rice paddle), ぬいぐるみ (stuffed toy), {印鑑|いんかん} (seal), レシート (receipt)
- Body parts (3): {眉毛|まゆげ} (eyebrow), こめかみ (temple), {手|て}のひら (palm)
- Transportation (5): バス{停|てい} (bus stop), {終電|しゅうでん} (last train), {車両|しゃりょう} (vehicle/train car), {乗車券|じょうしゃけん} (ticket), {運賃|うんちん} (fare)
- Rooms (2): {寝室|しんしつ} (bedroom), {浴室|よくしつ} (bathroom)
- Verbs (3): {憧|あこが}れる (to admire), {叶|かな}う (to come true), {励|はげ}ます (to encourage)
- Expressions (8): じゃあね (see ya), またね (see you later), だるい (sluggish), {面倒臭|めんどくさ}い (bothersome), なんか (like/somehow), ぶっちゃけ (to be honest), ぼちぼち (so-so), ほどほど (moderation)
- Abstract nouns (12): {難民|なんみん} (refugee), {移民|いみん} (immigrant), {世論|せろん} (public opinion), {真実|しんじつ} (truth), {意欲|いよく} (motivation), {体力|たいりょく} (stamina), {自覚|じかく} (self-awareness), {協定|きょうてい} (agreement), {同盟|どうめい} (alliance), {研修|けんしゅう} (training), {練習|れんしゅう} (practice), {古代|こだい} (ancient times)
- Measurements/Math (18): {産業|さんぎょう} (industry), {資源|しげん} (resources), {強力|きょうりょく} (powerful), {探査|たんさ} (exploration), {哲学|てつがく} (philosophy), {心理|しんり} (psychology), {楽|たの}しむ (to enjoy), {苦|くる}しむ (to suffer), {長|なが}さ (length), {高|たか}さ (height), {深|ふか}さ (depth), {厚|あつ}さ (thickness), {広|ひろ}さ (width), {面積|めんせき} (area), {体積|たいせき} (volume), {距離|きょり} (distance), {速度|そくど} (speed), {割合|わりあい} (ratio)
- Academic subjects (12): {平均|へいきん} (average), {合計|ごうけい} (total), {足|た}し{算|ざん} (addition), {引|ひ}き{算|ざん} (subtraction), {掛|か}け{算|ざん} (multiplication), {割|わ}り{算|ざん} (division), {数学|すうがく} (mathematics), {科学|かがく} (science), {化学|かがく} (chemistry), {物理|ぶつり} (physics), {生物|せいぶつ} (biology), {歴史|れきし} (history)

Notable entry features:
- Comprehensive onomatopoeia for textures, sensations, and emotional states
- Complete set of basic math operations (四則演算)
- Academic subjects useful for educational contexts
- Measurement vocabulary with related adjective notes
- Cross-references added linking homophones ({科学|かがく}↔{化学|かがく})

Total entries: 5,307 → 5,407
Remaining candidates: 1,441 → 1,354

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 58)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Onomatopoeia (26): ぴかぴか (sparkling), ふわふわ (fluffy), どきどき (heart pounding), わくわく (excited), きらきら (glittering), ぐるぐる (spinning), ぺこぺこ (hungry/bowing), のろのろ (slowly), すべすべ (smooth), ぼろぼろ (worn out), ばらばら (scattered), ぎりぎり (barely), ぶらぶら (wandering), うろうろ (loitering), くたくた (exhausted), ぐちゃぐちゃ (messy), べたべた (sticky), からから (parched), ぬるぬる (slimy), ざらざら (rough), つるつる (slippery), ごろごろ (rumbling), にこにこ (smiling), めちゃくちゃ (absurd), ぐっと (firmly), すっきり (refreshed)
- Food/Noodles (3): ラーメン (ramen), うどん (udon), チョコレート (chocolate)
- Vegetables (13): じゃがいも (potato), {人参|にんじん} (carrot), {大根|だいこん} (daikon), キャベツ (cabbage), {法蓮草|ほうれんそう} (spinach), {葱|ねぎ} (green onion), にんにく (garlic), {生姜|しょうが} (ginger), トマト (tomato), レタス (lettuce), メロン (melon), {胡瓜|きゅうり} (cucumber), {玉葱|たまねぎ} (onion)
- Animals (8): ライオン (lion), かもめ (seagull), カブトムシ (beetle), {蝉|せみ} (cicada), アヒル (duck), {鶏|にわとり} (chicken), {山羊|やぎ} (goat), {蜻蛉|とんぼ} (dragonfly)
- Daily expressions (5): おはよう (good morning), おやすみ (good night), どういたしまして (you're welcome), {お疲|おつか}れ{様|さま} (thank you for your work), とりあえず (for now)
- Adverbs (2): ちなみに (by the way), そもそも (in the first place)
- Abstract concepts (8): {忍耐|にんたい} (patience), {好奇心|こうきしん} (curiosity), {創造性|そうぞうせい} (creativity), {矛盾|むじゅん} (contradiction), {調和|ちょうわ} (harmony), {均衡|きんこう} (equilibrium), {中断|ちゅうだん} (interruption), {再開|さいかい} (resumption)
- Technology/Media (15): ブランド (brand), マーケティング (marketing), ウイルス (virus), {貼|は}り{付|つ}け (paste), {画素|がそ} (pixel), タッチパネル (touchscreen), {取材|しゅざい} (news gathering), {広報|こうほう} (PR), {吹|ふ}き{替|か}え (dubbing), スキャナー (scanner), テレビ{電話|でんわ} (video call), ドキュメンタリー (documentary), アダプター (adapter), ビッグデータ (big data), {和英|わえい} (Japanese-English)
- Music/Arts (5): {和歌|わか} (waka poetry), {和楽器|わがっき} (Japanese instruments), {独唱|どくしょう} (solo), {作詞|さくし} (lyrics writing), {編曲|へんきょく} (arrangement)
- Sports/Exercise (7): ボクシング (boxing), レスリング (wrestling), サーフィン (surfing), ダイビング (diving), ストレッチ (stretching), ウォーキング (walking)
- Science/Politics (8): {与党|よとう} (ruling party), {過疎化|かそか} (depopulation), {染色体|せんしょくたい} (chromosome), {小惑星|しょうわくせい} (asteroid), {成層圏|せいそうけん} (stratosphere), オゾン{層|そう} (ozone layer), {脈|みゃく} (pulse), {塵紙|ちりがみ} (tissue paper)

Notable entry features:
- Comprehensive onomatopoeia coverage for common sensory descriptions
- Vegetable vocabulary useful for cooking and shopping contexts
- Science vocabulary includes space and environmental terms
- Cross-references added linking antonym pairs ({中断|ちゅうだん}↔{再開|さいかい})

Total entries: 5,207 → 5,307
Remaining candidates: 1,548 → 1,441

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
