# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-29
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
- [x] Atomic build process (temp directory swap prevents broken states)
- [x] Centralized cross-reference type definitions (`build/cross_ref_types.py`)
- [x] Centralized furigana pattern and utilities (`build/japanese_utils.py`)
- [x] Enhanced validation with structured return types
- [x] Improved security (XSS prevention, no auto-install)

### Content Status
- **Total entries**: 8,981
- **Vocabulary tier assignment**: Basic: 795 | Core: 1,998 | General: 6,128 | Unassigned: 0 ✓
- **Candidate words**: 202 words tracked in `candidate_words.json`
- **Priority candidates**: 0 words remaining in `candidate_words_priority.json` (all 94 completed)
- **Cross-references**: 567 total (555 resolved, 97% resolution rate)
- **Audio files**: 1,028 MP3 files covering example sentences

### Vocabulary Tier System
The dictionary uses a three-tier vocabulary classification system (see vocabulary-tiers skill):
- **Basic**: 795 entries (target: 600-800) - fundamental words for basic communication
- **Core**: 1,998 entries (target: 1,600-2,000) - words for adult-level communication
- **General**: 5,046+ entries (no limit) - all other vocabulary useful for learners

**Tier realignment completed 2026-01-19.** All entries have tier assignments meeting target ranges. The basic and core tiers are curated to ensure semantic group integrity.

**Policy for new entries:** All new entries must be assigned to the **general** tier. The basic and core tiers are considered stable and should not be modified unless explicitly requested.

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

### 2026-01-30 (Candidate Collection Expansion - 102 New Candidates)
Added 102 new candidate words across diverse categories to reach 202 total candidates:

- **Social/Interpersonal (15)**: 親睦, 軋轢, 融和, 歩み寄り, 詰め寄る, 問い詰める, 折り合い, 譲歩, 世間体, etc.
- **Character/Personality (12)**: 慎む, 自重, 控え目, 厚かましい, 厚顔, 物静か, 快活, 溌剌, 愚直, 実直, etc.
- **Demeanor/Composure (8)**: 沈着, 悠然, 泰然, 毅然, 凛々しい, 威風, 風格, 佇まい
- **Psychology/Emotions (10)**: 抑圧, 発散, 困惑, 気後れ, 物怖じ, 臆する, 辟易, 悶える, 身悶える, etc.
- **Physical/Movement (6)**: 身構える, 食らいつく, 抗う, 屈する, 軽快, 機敏, 鈍重, 緩慢, 俊敏
- **Health/Body (5)**: 矍鑠, 壮健, 虚弱, 頑健, 屈強
- **Appearance/Quality (10)**: 品格, 華麗, 絢爛, 質素, 簡素, 精緻, 粗雑, 垢抜け, 野暮ったい, 無粋, 朴訥
- **Business/Finance (6)**: 露呈, 漏洩, 偽装, 装う, 見せかけ, 出費, 散財, 損益, 倹約, 浪費
- **Food/Cooking (4)**: まかない, 仕込み, 淹れ立て, まろやか
- **Other (26)**: 薄暗い, 陰る, 凍える, 鳴り響く, 反響, 払暁, 醸成, 飽和, 収束, 沈殿, 追及, 体裁, 面目, 沽券, 威嚇, 威圧, 虚勢, 雑多, 雑然, 整然, 散漫, 専念, 心酔, 盲信, 迷信, etc.

Focus on intermediate-to-advanced vocabulary for general tier, emphasizing character traits, social dynamics, and abstract concepts.

### 2026-01-30 (New Candidate Collection - 100 Candidates)
Rebuilt candidate_words.json from scratch with 100 high-quality candidates using diverse search strategies:

- **Emotional/Psychological (18)**: 挫折, 憔悴, 激昂, 感傷, 寂寥, 憫然, 惻隠, 共感, 情緒, 気概, 意気込み, 物憂い, etc.
- **Medical/Health (10)**: 麻痺, 硬直, 慢性, 急性, 発症, 再発, 寛解, 経過観察, 服薬, 嚥下
- **Business/Finance (8)**: 掲載, 脱税, 横領, 督促, 延滞, 辞令, 始末書, 談合
- **Movement/Travel (7)**: 雑踏, 迂回, 縦断, 蛇行, 徘徊, 立ち退く
- **Cooking/Food (4)**: 炙る, 漬け込む, 塩漬け, 煮詰める
- **Skills/Experience (6)**: 駆け出し, 玄人, 老練, 熟練, 円熟, 練達
- **Insight/Perception (5)**: 洞察, 慧眼, 先見, 予兆, 前兆
- **Quality/Character (12)**: 周到, 杜撰, 拙速, 稚拙, 陳腐, 斬新, 華奢, etc.
- **Aesthetic/Cultural (8)**: 幽玄, 風情, 雅, 趣, 興趣, 静寂, etc.
- **Verbs/Actions (8)**: 粘る, 堪える, 蓄える, 刷り込む, 差し替える, 媚びる, 咀嚼, 触発
- **Other (14)**: 膨大, 弾圧, 逆襲, 阿諛, 準ずる, 則る, 波及, 風刺, 揶揄, 嘲笑, etc.

Candidate categories emphasize general tier vocabulary appropriate for intermediate-to-advanced learners.

### 2026-01-29 (Vocabulary Expansion - 30 New Entries, Session 190)
Added 30 new dictionary entries from candidate_words.json, covering diverse vocabulary including abbreviations, technology terms, transportation, loanwords, and cultural vocabulary:

- **Abbreviations/Acronyms (7)**: SS (screenshot), PA (penalty area), AC (air conditioning/alternating current), RTA (real-time attack/speedrun), iOS (Apple operating system)
- **Technology/Computing (4)**: スループット (throughput), ワイヤレス{充電|じゅうでん} (wireless charging), オペレーティングシステム (operating system), デジタルネイティブ (digital native)
- **Transportation (3)**: {立|た}ち{乗|の}り (standing on train), {座席|ざせき}{争|あらそ}い (seat scramble), {車席|しゃせき} (car seat)
- **Loanwords (4)**: ショルダーバッグ (shoulder bag), ブラジャー (bra), ビデオゲーム (video game)
- **Food/Cooking (3)**: {注文品|ちゅうもんひん} (custom order), {半切|はんぎ}り (cutting in half), {店屋|みせや} (store/shop)
- **Expressions/Vocabulary (6)**: {顔色|かおいろ}をうかがう (watching someone's expression), {笑|わら}いすぎ (laughing too much), {場|ば}{見知|みし}り (shy in unfamiliar places), うっかり{忘|わす}れ (careless forgetfulness), {作|つく}りごたえ (satisfying to make), {麗々|れいれい}しい (formal/ceremonious)
- **Cultural/Traditional (2)**: {褌|ふんどし} (loincloth/fundoshi), {切手|きって}{収集|しゅうしゅう} (stamp collecting)
- **Other (4)**: {千円|せんえん} (1000 yen), {日日|ひにち} (date), あばた (pockmarks), {鬱血|うっけつ} (blood congestion)

Notable entry features:
- Multi-sense entries: AC (air conditioning/alternating current), {店屋|みせや} (store/shopkeeper)
- Gaming vocabulary: RTA ({走者|そうしゃ}), SS (スクショ), ビデオゲーム
- ～ごたえ pattern: {作|つく}りごたえ (satisfying to make)
- Medical vocabulary: {鬱血|うっけつ} (venous congestion)
- Famous proverb reference: あばたも{笑窪|えくぼ} (love is blind)
- 1 new kanji added: {褌|ふんどし} (02110)

Total entries: 8,951 → 8,981
Remaining candidates: ~9,055 → ~9,026
New kanji: 2,109 → 2,110

### 2026-01-29 (Vocabulary Expansion - 30 New Entries, Session 189)
Added 30 new dictionary entries from candidate_words.json, covering IT terminology, Japanese cultural vocabulary, loanwords, and 一 (ichi) compound words:

- **IT/Technical (1)**: {可用性|かようせい} (availability - IT term)
- **Japanese Cultural (5)**: お{彼岸|ひがん} (equinoctial week), お{茶屋|ちゃや} (tea house/geisha house), ご{当地|とうち} (local/regional), {一汁三菜|いちじゅうさんさい} (traditional meal format), {一升瓶|いっしょうびん} (1.8L sake bottle)
- **Common Loanwords (9)**: お{手頃|てごろ} (affordable), エコバッグ (eco bag), エントランス (entrance), オチ (punchline), キック (kick), クリニック (clinic), アルミ (aluminum), ガス{代|だい} (gas bill), ガラケー (flip phone)
- **Sports (2)**: ノーヒット (no-hitter), {一回戦|いっかいせん} (first round)
- **一-Compound Words (13)**: {一々|いちいち} (one by one), {一括|いっかつ} (lump sum), {一撃|いちげき} (one blow), {一方通行|いっぽうつうこう} (one-way), {一桁|ひとけた} (single digit), {一段|いちだん} (one level), {一番星|いちばんぼし} (first star), {一目散|いちもくさん} (at full speed), {一眼|いちがん} (SLR camera), {一人用|ひとりよう} (for one person), {一人娘|ひとりむすめ} (only daughter), {一卵性|いちらんせい} (identical twins), {一夜|いちや} (one night)

Notable entry features:
- Japanese cultural vocabulary: お{彼岸|ひがん} (Buddhist memorial period), {一汁三菜|いちじゅうさんさい} (traditional meal structure)
- Multi-sense entries: お{茶屋|ちゃや} (tea house/geisha house), お{手頃|てごろ} (affordable/convenient size), {一方通行|いっぽうつうこう} (traffic/figurative), {一段|いちだん} (level/degree)
- Modern Japanese vocabulary: ガラケー (Galapagos phone etymology), エコバッグ (post-plastic-bag-charge era)
- IT terminology: {可用性|かようせい} (availability in systems engineering)
- Photography: {一眼|いちがん} (DSLR/mirrorless cameras)

Total entries: 8,921 → 8,951
Remaining candidates: ~9,085 → ~9,055

### 2026-01-29 (Vocabulary Expansion - 30 New Entries, Session 188)
Added 30 new dictionary entries from candidate_words.json, covering technology abbreviations, sports leagues, loanwords, and Japanese quantity expressions with {一|いち}:

- **Technology/Computing (7)**: HP (homepage/website), SE (sound effect), IC (interchange/IC card), IH (induction heating), LCD (liquid crystal display), FPS (first-person shooter/frames per second), MMO (massively multiplayer online)
- **Sports Leagues (2)**: NBA (National Basketball Association), MLB (Major League Baseball)
- **Medical (1)**: ADHD (attention-deficit hyperactivity disorder)
- **Business/Work (2)**: OJT (on-the-job training), スキルアップ (skill improvement)
- **Common Loanwords (4)**: ショップ (shop), シーン (scene), タッチ (touch), キャラ (character)
- **Japanese Quantity Expressions with {一|いち} (14)**: {一周|いっしゅう} (one lap/anniversary), {一同|いちどう} (all members), {一品|いっぴん} (one dish/fine article), {一員|いちいん} (a member), {一声|ひとこえ} (a word/call), {一個|いっこ} (one piece), {一台|いちだい} (one machine/vehicle), {一刻|いっこく} (a moment), {一回|いっかい} (once/first inning), {一位|いちい} (first place), {一件|いっけん} (one matter), {一対|いっつい} (a pair), {一億|いちおく} (100 million), {一匹|いっぴき} (one animal)

Notable entry features:
- Multi-sense technology terms: IC (interchange/IC card), FPS (game genre/frame rate)
- Wasei-eigo vocabulary: スキルアップ (skill improvement - Japanese-made English)
- Japanese sports culture: MLB with Japanese player context ({大谷|おおたに}{翔平|しょうへい}, イチロー)
- Comprehensive {一|いち} quantity expressions: counters and number-based vocabulary
- Modern gaming vocabulary: FPS, MMO (with Japanese gaming culture context)
- Common loanwords with multiple senses: シーン (media scene/situation), タッチ (touch/style/involvement), キャラ (character/persona)

Total entries: 8,891 → 8,921
Remaining candidates: ~9,115 → ~9,085

### 2026-01-29 (Vocabulary Expansion - 30 New Entries, Session 187)
Added 30 new dictionary entries from candidate_words.json, covering media/technology abbreviations, soccer position terms, Japanese quantity expressions with {一|いち}, and medical/academic acronyms:

- **Media/Broadcasting (4)**: FM (FM radio), AM (AM radio), TV (television), CG (computer graphics)
- **Computing/Technology (4)**: FAQ (frequently asked questions), PDF (portable document format), URL (web address), EC (e-commerce)
- **Soccer Positions (5)**: PK (penalty kick), GK (goalkeeper), FW (forward), DF (defender), MF (midfielder)
- **Medical/Health (3)**: CPR (cardiopulmonary resuscitation), CT (CT scan), OTC (over-the-counter medicine)
- **Social/Cultural (3)**: LGBT (sexual/gender minorities), SF (science fiction), EQ (emotional quotient)
- **Emergency/Sports (2)**: SOS (distress signal), MVP (most valuable player)
- **Japanese Quantity Expressions (9)**: {一晩|ひとばん} (one night), {一本|いっぽん} (one long object/ippon), {一枚|いちまい} (one flat object), {一歩|いっぽ} (one step), {一気|いっき} (in one go), {一泊|いっぱく} (one night stay), {一滴|いってき} (one drop), {一点|いってん} (one point), {一発|いっぱつ} (one shot)

Notable entry features:
- Complete soccer position vocabulary: GK/DF/MF/FW with Japanese soccer context (Jリーグ, NPB)
- Japanese quantity compounds: {一本|いっぽん} (judo ippon scoring), {一気|いっき}{飲|の}み (chugging culture)
- Medical terminology: OTC medicine classification ({第|だい}1/2/3{類|るい}), CPR with AED context
- Multi-sense entries: {一本|いっぽん} (counter/judo/single-mindedness), {一発|いっぱつ} (shot/try/jackpot), SOS (distress/figurative)
- Japanese travel vocabulary: {一泊|いっぱく}{二|に}{食|しょく} (accommodation with meals)

Total entries: 8,861 → 8,891
Remaining candidates: ~9,145 → ~9,115

### 2026-01-28 (Vocabulary Expansion - 30 New Entries, Session 186)
Added 30 new dictionary entries from candidate_words.json, covering technology abbreviations, social media platforms, business loanwords, and general vocabulary:

- **Technology Abbreviations (10)**: GPS (navigation), USB (universal serial bus), LED (light-emitting diode), MRI (medical imaging), LCC (low-cost carrier), CD (compact disc), DVD (digital versatile disc), UV (ultraviolet), LAN (local area network), OS (operating system)
- **Organizations/Media (4)**: NHK (Japan Broadcasting Corporation), NGO (non-governmental organization), EU (European Union), UN (United Nations)
- **Social Media Platforms (4)**: YouTube, Zoom, Twitter, Instagram
- **Business Loanwords (6)**: CEO, ウェルビーイング (well-being), インクルーシブ (inclusive), ピボット (pivot), ファシリテーター (facilitator), エンゲージメント (engagement)
- **General Vocabulary (6)**: CO2 (carbon dioxide), ハード (hardware/hard), ペースト (paste), {上弦|じょうげん} (first quarter moon), {債権|さいけん} (credit/receivable), {防御率|ぼうぎょりつ} (ERA in baseball)

Notable entry features:
- Japan-specific media: NHK ({朝|あさ}ドラ, {紅白|こうはく}{歌合戦|うたがっせん} cultural references)
- Social media vocabulary: Twitter/{炎上|えんじょう}, Instagram/インスタ{映|ば}え
- Business buzzwords: ウェルビーイング{経営|けいえい}, {従業員|じゅうぎょういん}エンゲージメント
- COVID-era vocabulary: Zoom{飲|の}み{会|かい}, Zoom{疲|づか}れ
- Multi-sense entries: ハード (hardware/difficult), ペースト (food/computer), ピボット (business/sports)
- Japanese baseball: {防御率|ぼうぎょりつ} (pitcher effectiveness statistic)

Total entries: 8,831 → 8,861
Remaining candidates: ~9,175 → ~9,145

### 2026-01-28 (Vocabulary Expansion - 30 New Entries, Session 185)
Added 30 new dictionary entries from candidate_words.json, covering katakana loanwords, abbreviations/acronyms, cultural vocabulary, casual speech, and modern terms:

- **Katakana Loanwords (15)**: スキル (skill), ティッシュ (tissue), バードウォッチング (birdwatching), リフォーム (renovation), ステンレス (stainless steel), チェーン (chain), ニット (knit), ネオン (neon), サーモン (salmon), ライス (rice), リクエスト (request), パネル (panel), スロット (slot), シニア (senior), ノイローゼ (neurosis)
- **Abbreviations/Acronyms (4)**: TKG ({卵|たまご}かけご{飯|はん}), CV (character voice), PTA (parent-teacher association), DJ (disc jockey)
- **Cultural Vocabulary (5)**: {七福神|しちふくじん} (Seven Lucky Gods), {万葉集|まんようしゅう} (Man'yōshū), デパ{地下|ちか} (department store food hall), プロ{野球|やきゅう} (professional baseball), ボケ (blur/comedy/senility)
- **Casual Speech (2)**: おいおい (crying loudly), っす (casual です)
- **Modern Terms (4)**: コミュ{力|りょく} (communication skills), デジタル{化|か} (digitalization), {万能|ばんのう} (all-purpose), タンパク{質|しつ} (protein)

Notable entry features:
- Photography term: ボケ (bokeh - adopted into English as photography term for blur aesthetic)
- Japanese food culture: TKG (viral abbreviation for {卵|たまご}かけご{飯|はん}), サーモン (sushi context), デパ{地下|ちか} (gourmet food floors)
- Otaku culture: CV (voice actor credits), ボケとツッコミ (comedy roles)
- German loanword: ノイローゼ (from German 'Neurose')
- Classical literature: {万葉集|まんようしゅう} (source of {令和|れいわ} era name)
- Multi-sense entries: ボケ (photography blur / comedy role / senility), チェーン (links / franchise / tire chains)

Total entries: 8,801 → 8,831
Remaining candidates: ~9,221 → ~9,175

### 2026-01-28 (Vocabulary Expansion - 30 New Entries, Session 184)
Added 30 new dictionary entries from candidate_words.json, covering casual/slang expressions, work culture vocabulary, technology/computing terms, modern acronyms, beauty/lifestyle vocabulary, and laughter onomatopoeia:

- **Casual/Slang (5)**: すげー (amazing-slang), やべー (awesome/bad-slang), ちゃう (てしまう contraction), なきゃ (なければ contraction), わろた (LOL-internet slang)
- **Work Culture (2)**: ブラック (exploitative company), マタハラ (maternity harassment)
- **Modern Acronyms (4)**: SDGs, NPO, IoT, リツイート (retweet)
- **Technology/Computing (4)**: インターフェース (interface), プロセッサ (processor), ログアウト (logout), フラッシュ (flash)
- **Finance (2)**: キャッシュバック (cashback), ポイント{還元|かんげん} (point rewards)
- **Beauty/Lifestyle (3)**: ファンデーション (foundation makeup), リップ (lip/lipstick), ダンサー (dancer)
- **Modern Verbs (1)**: タピる (to drink bubble tea)
- **Music (1)**: バース (verse)
- **Expressions (1)**: それじゃ (well then)
- **Laughter Onomatopoeia (3)**: あはは (ha ha), うふふ (hee hee), えへへ (heh heh)
- **Formal/Hierarchy (3)**: {建|けん}{議|ぎ} (proposal), {目下|めした} (subordinate), {何分|なにぶん} (in any case)
- **Other (1)**: {切|き}り{取|と}り (cutting/clipping)

Notable entry features:
- Japanese casual speech: すげー/やべー (slang adjectives), ちゃう/なきゃ (grammatical contractions)
- Japanese work culture: ブラック{企業|きぎょう} (exploitative company), マタハラ (workplace harassment vocabulary)
- Internet/social media: わろた (LOL slang), リツイート (retweet)
- Japanese point culture: キャッシュバック/ポイント{還元|かんげん} (ubiquitous in Japanese retail)
- Laughter expressions: あはは/うふふ/えへへ (different nuances of laughter)
- Modern trends: タピる (bubble tea verb from 2019 boom)

Total entries: 8,771 → 8,801
Remaining candidates: ~9,251 → ~9,221

### 2026-01-28 (Vocabulary Expansion - 30 New Entries, Session 183)
Added 30 new dictionary entries from candidate_words.json, covering modern acronyms/loanwords, music vocabulary, counter questions, technology/computing terms, casual expressions, and cultural vocabulary:

- **Modern Acronyms (9)**: NEET (ニート), DINKS (ディンクス), VIP (ビップ), ATM (えーてぃーえむ), AED (えーいーでぃー), DNA (でぃーえぬえー), IQ (あいきゅー), PTSD (ぴーてぃーえすでぃー)
- **Music Terms (3)**: ハーモニー (harmony), ベース (bass), ボーカル (vocal)
- **Counter Questions (3)**: {何枚|なんまい} (how many flat things), {何冊|なんさつ} (how many books), {何杯|なんばい} (how many cups)
- **Technology/Computing (2)**: {非同期|ひどうき} (asynchronous), {帯域|たいいき} (bandwidth)
- **Casual Expressions (4)**: オッケー (OK), ほんと (really), そいつ (that guy), というのは (that is)
- **Japanese Culture (4)**: ご{縁|えん} (fate/connection), すり{身|み} (fish paste), お{客様|きゃくさま} (customer-honorific), どん{底|ぞこ} (rock bottom)
- **Transportation (2)**: {車内|しゃない}{放送|ほうそう} (train announcement), {運行状況|うんこうじょうきょう} (service status)
- **Writing/Publishing (3)**: {書|か}き{下|お}ろし (newly written), {再入荷|さいにゅうか} (restocking), {歳入|さいにゅう}/{歳出|さいしゅつ} (revenue/expenditure)

Notable entry features:
- Modern lifestyle acronyms: NEET/DINKS/VIP (wasei-eigo adaptations), medical terms (PTSD/AED/DNA/IQ)
- Financial technology: ATM with Japan-specific usage notes (convenience store availability, fee structures)
- Counter question pattern: {何|なん}+counter forms for flat objects, books, and cups/glasses
- Computing vocabulary: {非同期|ひどうき} (programming), {帯域|たいいき} (networking)
- Casual speech patterns: ほんと (casual form of 本当), そいつ (casual demonstrative pronoun)
- Japanese cultural concepts: ご{縁|えん} (Buddhist-influenced fate concept), どん{底|ぞこ} (emphatic expression)
- Multi-sense entries: ベース (music bass vs baseball base vs foundation), {帯域|たいいき} (internet bandwidth vs frequency band)

Total entries: 8,741 → 8,771
Remaining candidates: ~9,281 → ~9,251

### 2026-01-28 (Vocabulary Expansion - 30 New Entries, Session 182)
Added 30 new dictionary entries from candidate_words.json, covering diverse vocabulary including adverbs, pronouns, legal professions, technology/energy terms, anatomy/medical, and cultural expressions:

- **Adverbs/Pronouns (4)**: {絶対|ぜったい}に (absolutely), {一目|ひとめ} (a glance), {四方|しほう} (all sides), {種々|しゅじゅ} (various kinds)
- **Documents/ID (2)**: {身分|みぶん}{証明|しょうめい} (identification), {職務|しょくむ}{経歴|けいれき}{書|しょ} (work history/CV)
- **Legal Professions (2)**: {司法|しほう}{書士|しょし} (judicial scrivener), {行政|ぎょうせい}{書士|しょし} (administrative scrivener)
- **Business/Work (2)**: {営業|えいぎょう}マン (salesperson), ウェブ{会議|かいぎ} (web conference)
- **Technology/Energy (4)**: {液晶|えきしょう}{画面|がめん} (LCD screen), {携帯|けいたい}{充電|じゅうでん}{器|き} (phone charger), {風力|ふうりょく}{発電|はつでん} (wind power), {再生|さいせい}{可能|かのう}エネルギー (renewable energy)
- **Anatomy/Medical (3)**: {皮下|ひか} (subcutaneous), {表皮|ひょうひ} (epidermis), {播種|はしゅ} (sowing/dissemination)
- **Numbers/Senses (3)**: {六感|ろっかん} (sixth sense), {七色|なないろ} (seven colors), {二心|ふたごころ} (duplicity)
- **Na-Adjectives (2)**: {支配|しはい}{的|てき} (dominant), {物質|ぶっしつ}{的|てき} (materialistic)
- **Food/Culture (2)**: {酒|さけ}の{肴|さかな} (drinking snacks), {蛙|かえる}の{子|こ}は{蛙|かえる} (like father like son)
- **Education/Daily Life (4)**: {対角|たいかく} (diagonal), {百科|ひゃっか} (encyclopedia), {試験|しけん}{期間|きかん} (exam period), {鍵|かぎ}{掛|か}け (key hook)
- **Miscellaneous (2)**: ゴミ{分別|ぶんべつ} (garbage sorting), お{供|とも}する (to accompany-humble)

Notable entry features:
- Japanese legal profession vocabulary: {司法|しほう}{書士|しょし} and {行政|ぎょうせい}{書士|しょし} (unique to Japan's legal system)
- Renewable energy vocabulary: {風力|ふうりょく}{発電|はつでん}/{再生|さいせい}{可能|かのう}エネルギー (environmental policy terms)
- Medical/anatomy terms: {皮下|ひか}/{表皮|ひょうひ}/{播種|はしゅ} (technical vocabulary with layered meanings)
- Japanese proverb: {蛙|かえる}の{子|こ}は{蛙|かえる} (like father, like son)
- Modern work vocabulary: ウェブ{会議|かいぎ} (post-pandemic standard)
- Cultural vocabulary: {酒|さけ}の{肴|さかな} (etymology of さかな explained)
- 3 new kanji added to kanji index: {播|はん} (02106), {晶|しょう} (02107), {肴|こう} (02108)

Total entries: 8,711 → 8,741
Remaining candidates: ~9,310 → ~9,281
New kanji: 2,105 → 2,108

### 2026-01-28 (Vocabulary Expansion - 32 New Entries, Session 181)
Added 32 new dictionary entries from candidate_words.json, covering health/lifestyle vocabulary, transportation announcements, adverbs/function words, ability compounds, household chores, weather/seasonal terms, and personality types:

- **Health/Lifestyle (5)**: {睡眠|すいみん}{不足|ぶそく} (sleep deprivation), {気分|きぶん}{転換|てんかん} (change of pace), {気分屋|きぶんや} (moody person), {朝帰|あさがえ}り (coming home in morning), オールナイト (all-night)
- **Transportation (4)**: {運転|うんてん}{見合|みあ}わせ (service suspension), {運転|うんてん}{再開|さいかい} (resumption of service), {車両|しゃりょう}{点検|てんけん} (train inspection), {信号|しんごう}{故障|こしょう} (signal malfunction)
- **Adverbs/Function Words (6)**: いくら{何|なん}でも (no matter what), どうにか (somehow), どうにも (cannot do anything), {何|なん}となく (somehow/vaguely), {何|なに}かと (one way or another), {何|なに}やら (something or other)
- **Ability Compounds (3)**: {実行力|じっこうりょく} (execution ability), {分析力|ぶんせきりょく} (analytical ability), {理解力|りかいりょく} (comprehension ability)
- **Household Chores (2)**: {水撒|みずま}き (watering), {窓拭|まどふ}き (window cleaning)
- **Health/Life Stages (1)**: {更年期|こうねんき} (menopause)
- **Weather/Seasons (2)**: {五月晴|さつきば}れ (clear May weather), {初冬|しょとう} (early winter)
- **Language Skills (2)**: {聞|き}き{取|と}り (listening comprehension), {読|よ}み{取|と}り (reading/interpretation)
- **Culture (1)**: おとぎ{話|ばなし} (fairy tale)
- **Personality/Status (4)**: {泊|とま}りがけ (overnight stay), {検討中|けんとうちゅう} (under consideration), {世話好|せわず}き (helpful person), {恥|は}ずかしがり (shy person)
- **Writing/Both (2)**: {書|か}き{心地|ごこち} (writing feel), どちらも (both)

Notable entry features:
- Train announcement vocabulary: {運転|うんてん}{見合|みあ}わせ/{運転|うんてん}{再開|さいかい}/{車両|しゃりょう}{点検|てんけん}/{信号|しんごう}{故障|こしょう} (common commuter announcements)
- Vague/indefinite adverbs: どうにか/どうにも/{何|なん}となく/{何|なに}かと/{何|なに}やら (nuanced uncertainty expressions)
- ～{力|りょく} ability compounds: {実行力|じっこうりょく}/{分析力|ぶんせきりょく}/{理解力|りかいりょく} (cognitive abilities)
- Comprehension skills pair: {聞|き}き{取|と}り (listening) vs {読|よ}み{取|と}り (reading)
- Multi-sense entries: {読|よ}み{取|と}り (text interpretation vs data scanning), {更年期|こうねんき} (biological vs figurative "midlife crisis")
- Seasonal vocabulary: {五月晴|さつきば}れ (originally referred to rainy season clearing)

Total entries: 8,679 → 8,711
Remaining candidates: ~9,414 → ~9,310

### 2026-01-27 (Vocabulary Expansion - 30 New Entries, Session 180)
Added 30 new dictionary entries from candidate_words.json, covering Japanese gift culture vocabulary, scientific/abstract terminology, and emotion/reaction expressions:

- **Gift Culture (5)**: {出産|しゅっさん}{祝|いわ}い (baby gift), {入学|にゅうがく}{祝|いわ}い (school entrance gift), {卒業|そつぎょう}{祝|いわ}い (graduation gift), {快気|かいき}{祝|いわ}い (recovery gift), {就職|しゅうしょく}{祝|いわ}い (job celebration gift)
- **Memory/Health (3)**: {記憶|きおく}{違|ちが}い (faulty memory), {寝違|ねちが}い (stiff neck), {同期|どうき}する (to synchronize)
- **Science/Abstract (5)**: {凝固|ぎょうこ} (solidification), {循環|じゅんかん} (circulation), {抽象|ちゅうしょう} (abstraction), {繁殖|はんしょく} (breeding), {衝撃|しょうげき} (shock/impact)
- **Qualities/Adjectives (4)**: {執拗|しつよう} (persistent), {純粋|じゅんすい} (pure), {陰気|いんき} (gloomy), {愕然|がくぜん} (astonished)
- **Reactions/Emotions (8)**: {反感|はんかん} (antipathy), {反発|はんぱつ} (repulsion), {反論|はんろん} (counterargument), {誤算|ごさん} (miscalculation), {誇張|こちょう} (exaggeration), {激怒|げきど} (rage), {狼狽|ろうばい} (confusion), {窮地|きゅうち} (predicament)
- **Laugh/Smile Vocabulary (5)**: {驚愕|きょうがく} (astonishment), {爆笑|ばくしょう} (roar of laughter), {微笑|びしょう} (smile), {苦笑|くしょう} (wry smile), {失笑|しっしょう} (involuntary laugh)

Notable entry features:
- Japanese gift culture: Complete set of ceremonial gift vocabulary ({出産|しゅっさん}/{入学|にゅうがく}/{卒業|そつぎょう}/{快気|かいき}/{就職|しゅうしょく}{祝|いわ}い) with cultural context about return gifts and timing
- Reaction vocabulary cluster: {反感|はんかん}/{反発|はんぱつ}/{反論|はんろん} (anti- words), {愕然|がくぜん}/{狼狽|ろうばい} (shock states)
- Smile/laugh spectrum: {微笑|びしょう} (gentle) → {苦笑|くしょう} (wry) → {失笑|しっしょう} (involuntary) → {爆笑|ばくしょう} (roaring)
- Scientific terminology: {凝固|ぎょうこ}/{循環|じゅんかん} with physics and medical usage notes
- Multi-sense entries: {反発|はんぱつ} (opposition vs rebound), {衝撃|しょうげき} (physical vs emotional shock)
- 3 new kanji added to kanji index: {愕|がく} (02103), {狽|はい} (02104), {粋|すい} (02105)

Total entries: 8,649 → 8,679
Remaining candidates: ~9,443 → ~9,414
New kanji: 2,102 → 2,105

### 2026-01-27 (Vocabulary Expansion - 30 New Entries, Session 179)
Added 30 new dictionary entries from candidate_words.json, covering diverse vocabulary including Japanese food culture, business terms, health/medical, qualities/adjectives, and cultural concepts:

- **Japanese Food/Culture (4)**: {酒蔵|さかぐら} (sake brewery), {餃子|ぎょうざ} (gyoza), {餡子|あんこ} (sweet bean paste), {鯖|さば} (mackerel)
- **Business/Work (5)**: {顧客|こきゃく} (customer), {領収|りょうしゅう} (receipt), {必修|ひっしゅう} (required), {高級|こうきゅう} (high-class), {関与|かんよ} (involvement)
- **Health/Medical (3)**: {飲酒|いんしゅ} (drinking alcohol), {養生|ようじょう} (recuperation), {小児科|しょうにか} (pediatrics)
- **Qualities/Adjectives (4)**: {頻繁|ひんぱん} (frequent), {頑丈|がんじょう} (sturdy), {劣勢|れっせい} (disadvantage), {半端|はんぱ} (incomplete)
- **Actions/Concepts (6)**: {飛躍|ひやく} (leap/progress), {獲物|えもの} (prey), {破棄|はき} (destruction), {組|く}み{立|た}て (assembly), {養殖|ようしょく} (aquaculture), {独断|どくだん} (arbitrary decision)
- **Cultural/Philosophy (4)**: {風物詩|ふうぶつし} (seasonal feature), {初心|しょしん} (beginner's mind), {視野|しや} (field of vision/perspective), {漫画家|まんがか} (manga artist)
- **Language/Writing (2)**: {句読点|くとうてん} (punctuation marks), {饒舌|じょうぜつ} (talkative)
- **Housing/Household (2)**: {入居|にゅうきょ} (moving in), {飯椀|めしわん} (rice bowl)

Notable entry features:
- Japanese food culture: {酒蔵|さかぐら} (sake brewing traditions), {餃子|ぎょうざ} (Japanese-style gyoza), {餡子|あんこ} ({和菓子|わがし} ingredient)
- Multi-sense entries: {飛躍|ひやく} (physical leap vs rapid progress vs logical leap), {養生|ようじょう} (recuperation vs health maintenance vs construction curing), {視野|しや} (visual field vs perspective)
- Zen/cultural concepts: {初心|しょしん} (beginner's mind from Zeami's teaching)
- Japanese seasonal awareness: {風物詩|ふうぶつし} (things characteristic of seasons)
- Business Japanese: {顧客|こきゃく}/{領収|りょうしゅう}/{関与|かんよ} (formal business vocabulary)
- 7 new kanji added to kanji index: {殖|しょく} (02096), {頻|ひん} (02097), {顧|こ} (02098), {餃|ぎょう} (02099), {餡|あん} (02100), {饒|じょう} (02101), {鯖|さば} (02102)

Total entries: 8,619 → 8,649
Remaining candidates: ~9,573 → ~9,443
New kanji: 2,095 → 2,102

### 2026-01-27 (Vocabulary Expansion - 30 New Entries, Session 178)
Added 30 new dictionary entries from candidate_words.json, covering Japanese food, education, workplace, technology/social media, health/medical, social issues, and sports:

- **Japanese Food (3)**: {牛丼|ぎゅうどん} (beef bowl), {出汁巻|だしま}き{卵|たまご} (Japanese rolled omelet), {筑前煮|ちくぜんに} (simmered chicken and vegetables)
- **Education (6)**: {遠隔授業|えんかくじゅぎょう} (remote classes), {通知表|つうちひょう} (report card), {課外活動|かがいかつどう} (extracurricular activities), {卒論|そつろん} (graduation thesis), クラス{替|が}え (class reshuffling), {内申点|ないしんてん} (internal assessment score)
- **Workplace/Employment (5)**: {飛|と}び{込|こ}み{営業|えいぎょう} (cold calling), {配置転換|はいちてんかん} (job transfer), {窓際族|まどぎわぞく} (sidelined employees), ワーケーション (workcation), {雇用形態|こようけいたい} (employment type)
- **Technology/Social Media (5)**: SNS{映|ば}え (Instagram-worthy), リポスト (repost), クラウドサービス (cloud service), サブスクリプション (subscription), {二段階認証|にだんかいにんしょう} (two-factor authentication)
- **Health/Medical (5)**: オンライン{診療|しんりょう} (telemedicine), {生活習慣病|せいかつしゅうかんびょう} (lifestyle disease), {自律神経|じりつしんけい} (autonomic nervous system), {後遺症|こういしょう} (aftereffect), {既往症|きおうしょう} (medical history)
- **Social Issues/Health (4)**: {待機児童|たいきじどう} (daycare waiting list), {体力低下|たいりょくていか} (physical decline), {内臓脂肪|ないぞうしぼう} (visceral fat), {栄養不足|えいようぶそく} (nutritional deficiency)
- **Sports (2)**: {審判員|しんぱんいん} (referee), {線審|せんしん} (line judge)

Notable entry features:
- Japanese comfort food: {牛丼|ぎゅうどん} (popular fast food), {筑前煮|ちくぜんに} (traditional home cooking with regional origin)
- Japanese education system: {内申点|ないしんてん}/{通知表|つうちひょう} (school evaluation), クラス{替|が}え (annual class reshuffling), {卒論|そつろん} (graduation thesis)
- Japanese workplace culture: {窓際族|まどぎわぞく} (sidelined employees reflecting lifetime employment practices), {飛|と}び{込|こ}み{営業|えいぎょう} (traditional sales method)
- Modern technology vocabulary: SNS{映|ば}え (social media culture), {二段階認証|にだんかいにんしょう} (security), サブスクリプション (subscription services)
- Healthcare terminology: {生活習慣病|せいかつしゅうかんびょう} (lifestyle diseases), {後遺症|こういしょう} (including long COVID discussion), {既往症|きおうしょう} (medical history)
- Social issues: {待機児童|たいきじどう} (daycare crisis in Japan), {体力低下|たいりょくていか} (declining physical fitness concern)
- 1 new kanji added to kanji index: {筑|ちく} (02095)

Total entries: 8,589 → 8,619
Remaining candidates: ~9,603 → ~9,573
New kanji: 2,094 → 2,095

### 2026-01-27 (Vocabulary Expansion - 30 New Entries, Session 177)
Added 30 new dictionary entries from candidate_words.json, covering cooking techniques, mistake/error vocabulary, sports/baseball terms, modern work arrangements, technology/authentication, and health/mental health:

- **Cooking Techniques (8)**: ぶつ{切|ぎ}り (rough chopping), {細切|ほそぎ}り (thin strips), {湯通|ゆどお}し (blanching), {水切|みずき}り (draining water), {油切|あぶらき}り (draining oil), {塩加減|しおかげん} (saltiness), {焦|こ}げ{目|め} (char marks), とろ{火|び} (low heat)
- **Mistake/Error Vocabulary (6)**: {聞|き}き{間違|まちが}い (mishearing), {言|い}い{間違|まちが}い (slip of tongue), {書|か}き{間違|まちが}い (writing mistake), {読|よ}み{間違|まちが}い (misreading), {見|み}{間違|まちが}い (mistaken sight), {思|おも}い{違|ちが}い (misconception)
- **Sports/Baseball (6)**: {逆転勝|ぎゃくてんが}ち (comeback victory), {先制点|せんせいてん} (opening score), {同点|どうてん} (tie score), {空振|からぶ}り (swing and miss), {三振|さんしん} (strikeout), {打点|だてん} (RBI)
- **Modern Work (4)**: ハイブリッド{勤務|きんむ} (hybrid work), {時差出勤|じさしゅっきん} (staggered hours), フレックス{制|せい} (flextime)
- **Technology/Authentication (3)**: {音声入力|おんせいにゅうりょく} (voice input), {顔認証|かおにんしょう} (facial recognition), {指紋認証|しもんにんしょう} (fingerprint auth)
- **Health/Mental Health (4)**: メンタルヘルス (mental health), {燃|も}え{尽|つ}き{症候群|しょうこうぐん} (burnout syndrome), {適応障害|てきおうしょうがい} (adjustment disorder), {免疫力|めんえきりょく} (immunity)

Notable entry features:
- Japanese cooking terminology cluster: cutting techniques (ぶつ{切|ぎ}り/{細切|ほそぎ}り), preparation methods ({湯通|ゆどお}し/{水切|みずき}り/{油切|あぶらき}り), heat control (とろ{火|び})
- ～{間違|まちが}い pattern: systematic error vocabulary for different senses (hearing/speaking/writing/reading/seeing)
- Baseball statistics: {打点|だてん} (RBI), {三振|さんしん} (strikeout), {空振|からぶ}り (swing and miss with figurative use)
- Modern workplace vocabulary: post-pandemic work arrangements (ハイブリッド{勤務|きんむ}, {時差出勤|じさしゅっきん}, フレックス{制|せい})
- Biometric authentication: {顔認証|かおにんしょう}/{指紋認証|しもんにんしょう} (modern security technology)
- Mental health awareness: メンタルヘルス/{燃|も}え{尽|つ}き{症候群|しょうこうぐん}/{適応障害|てきおうしょうがい} (workplace health vocabulary)
- Multi-sense entry: {空振|からぶ}り (baseball swing and miss + figurative fruitless effort)

Total entries: 8,559 → 8,589
Remaining candidates: ~9,633 → ~9,603

### 2026-01-27 (Vocabulary Expansion - 30 New Entries, Session 176)
Added 30 new dictionary entries from candidate_words.json, covering body parts, sleep vocabulary, education terms, weather/seasons, and work/life balance:

- **Body Parts (8)**: {眉間|みけん} (between eyebrows), うなじ (nape of neck), みぞおち (solar plexus), {土踏|つちふ}まず (arch of foot), {鳥肌|とりはだ} (goosebumps), {青筋|あおすじ} (blue vein), {吹|ふ}き{出物|でもの} (pimple), {歯|は}ぎしり (teeth grinding)
- **Sleep Vocabulary (3)**: {寝|ね}つき (ability to fall asleep), {寝覚|ねざ}め (waking up), {目覚|めざ}まし (alarm clock)
- **Education (5)**: {学力|がくりょく} (academic ability), {時間割|じかんわり} (class schedule), {偏差値|へんさち} (deviation score), {終業式|しゅうぎょうしき} (closing ceremony), {始業式|しぎょうしき} (opening ceremony)
- **Weather/Seasons (6)**: {厳冬|げんとう} (severe winter), {木枯|こが}らし (wintry wind), {雪解|ゆきど}け (thaw), {残暑|ざんしょ} (lingering summer heat), {霜柱|しもばしら} (frost pillars), {晩秋|ばんしゅう} (late autumn)
- **Work/Life Balance (6)**: {兼業|けんぎょう} (side business), {過労|かろう} (overwork), {共働|ともばたら}き (dual-income), {育休|いくきゅう} (childcare leave), {介護休暇|かいごきゅうか} (nursing care leave), {運動不足|うんどうぶそく} (lack of exercise)
- **Transportation (2)**: {通勤電車|つうきんでんしゃ} (commuter train), {始発電車|しはつでんしゃ} (first train)

Notable entry features:
- Body part vocabulary cluster: face/head parts ({眉間|みけん}/うなじ), body areas (みぞおち/{土踏|つちふ}まず), physical reactions ({鳥肌|とりはだ}/{青筋|あおすじ})
- Sleep quality vocabulary: {寝|ね}つき (falling asleep) vs {寝覚|ねざ}め (waking up) contrast
- Japanese education system: {偏差値|へんさち} with explanation of statistical scoring system
- Seasonal vocabulary: {残暑|ざんしょ}お{見舞|みま}い greeting custom
- Work-life vocabulary: {育休|いくきゅう}/{介護休暇|かいごきゅうか} reflecting modern workplace benefits
- Multi-sense entries: {歯|は}ぎしり (physical grinding vs frustration), {雪解|ゆきど}け (snow thaw vs relationship thaw)
- 1 new kanji added to kanji index: {兼|けん} (02094)

Total entries: 8,529 → 8,559
Remaining candidates: ~10,495 → ~9,633
New kanji: 2,093 → 2,094

### 2026-01-27 (Vocabulary Expansion - 30 New Entries, Session 175)
Added 30 new dictionary entries from candidate_words.json, covering function words/adverbs, ability/力 compounds, household vocabulary, cooking equipment, and Japanese food:

- **Function Words/Adverbs (6)**: それとなく (indirectly), それなりに (in its own way), それにしても (nevertheless), {改|あらた}めて (anew), {思|おも}い{切|き}り (with all one's might), やむを{得|え}ず (unavoidably)
- **Self-Reliance (2)**: {自力|じりき} (one's own power), {他力|たりき} (help from others)
- **Physical Abilities (5)**: {気力|きりょく} (willpower), {脚力|きゃくりょく} (leg strength), {腕力|わんりょく} (arm strength), {握力|あくりょく} (grip strength), {持久力|じきゅうりょく} (endurance), {瞬発力|しゅんぱつりょく} (explosive power)
- **Mental/Leadership Abilities (5)**: {決断力|けつだんりょく} (decisiveness), {行動力|こうどうりょく} (action ability), {洞察力|どうさつりょく} (insight), {観察力|かんさつりょく} (observation), {説得力|せっとくりょく} (persuasiveness)
- **Household/Architecture (4)**: {書棚|しょだな} (bookshelf), {応接間|おうせつま} (reception room), {踊|おど}り{場|ば} (stair landing), {雑巾|ぞうきん}がけ (mopping)
- **Gardening Chores (2)**: {芝刈|しばか}り (lawn mowing), {草取|くさと}り (weeding)
- **Cooking Equipment (2)**: {圧力鍋|あつりょくなべ} (pressure cooker), {蒸|む}し{器|き} (steamer)
- **Japanese Food/Cooking (3)**: {炒|いた}め{物|もの} (stir-fry), きんぴら (kinpira), カツ{丼|どん} (katsudon)

Notable entry features:
- ～{力|りょく} compound cluster: comprehensive coverage of physical and mental abilities
- Self-reliance vocabulary: {自力|じりき} vs {他力|たりき} with Buddhist etymology
- Endurance vs explosive power contrast: {持久力|じきゅうりょく} vs {瞬発力|しゅんぱつりょく}
- それ～ function word pattern: それとなく/それなりに/それにしても
- Japanese home cooking: きんぴら/カツ{丼|どん} with cultural notes

Total entries: 8,499 → 8,529
Remaining candidates: ~472 → ~10,495 (large batch added)

### 2026-01-27 (Vocabulary Expansion - 30 New Entries, Session 173)
Added 30 new dictionary entries from candidate_words.json, covering expressions/emotions vocabulary, personality types, communication skills, transportation vocabulary, and work culture:

- **Smile/Laugh Expressions (7)**: {薄笑|うすわら}い (smirk), {高笑|たかわら}い (loud laugh), {照|て}れ{笑|わら}い (embarrassed smile), {泣|な}き{笑|わら}い (laughing through tears), {思|おも}い{出|だ}し{笑|わら}い (laughing at memory), {嘘泣|うそな}き (fake crying), {作|つく}り{笑|わら}い (fake smile)
- **Personality Types (6)**: {社交的|しゃこうてき} (sociable), {内向的|ないこうてき} (introverted), {外向的|がいこうてき} (extroverted), {無神経|むしんけい} (insensitive), {多弁|たべん} (talkative), {二面性|にめんせい} (two-faced nature)
- **Communication Skills (4)**: {話|はな}し{上手|じょうず} (good speaker), {聞|き}き{上手|じょうず} (good listener), {告|つ}げ{口|ぐち} (tattling), {揚|あ}げ{足取|あしと}り (nitpicking)
- **Social/Dining (4)**: {会費|かいひ} (membership fee), {別会計|べつかいけい} (separate checks), {持|も}ち{寄|よ}り (potluck), もらい{泣|な}き (sympathetic crying)
- **Transportation (4)**: {落|お}とし{物|もの} (lost property), {回数券|かいすうけん} (book of tickets), {人身事故|じんしんじこ} (rail accident), {遅延証明|ちえんしょうめい} (delay certificate)
- **Work Culture (3)**: サービス{残業|ざんぎょう} (unpaid overtime), {飲|の}みニケーション (drinking-based networking), {副業|ふくぎょう} (side job)
- **Conflict/Quarrel (1)**: {口喧嘩|くちげんか} (verbal argument)
- **Gift/Culture (1)**: お{年玉|としだま} (New Year's money gift)

Notable entry features:
- Facial expression vocabulary cluster: {薄笑|うすわら}い/{高笑|たかわら}い/{照|て}れ{笑|わら}い/{作|つく}り{笑|わら}い (types of smiles)
- Emotion vocabulary: {泣|な}き{笑|わら}い (complex emotion), もらい{泣|な}き (empathetic crying)
- Personality psychology terms: {内向的|ないこうてき}/{外向的|がいこうてき} (introversion/extroversion)
- ~{上手|じょうず} pattern: {話|はな}し{上手|じょうず}/{聞|き}き{上手|じょうず} (communication skills)
- Japanese work culture: サービス{残業|ざんぎょう}/{飲|の}みニケーション (workplace practices)
- Train culture: {人身事故|じんしんじこ}/{遅延証明|ちえんしょうめい} (commuter vocabulary)
- Japanese customs: お{年玉|としだま} (New Year's money gift tradition)

Total entries: 8,439 → 8,469
Remaining candidates: ~530 → ~500

### 2026-01-27 (Vocabulary Expansion - 30 New Entries, Session 172)
Added 30 new dictionary entries from candidate_words.json, covering health/medical terms, onomatopoeia, katakana loanwords, environmental vocabulary, personality types, compound verbs, and traditional Japanese vocabulary:

- **Health/Medical (6)**: {肌荒|はだあ}れ (rough skin), {食|しょく}あたり (food poisoning), {肺炎|はいえん} (pneumonia), {喘息|ぜんそく} (asthma), {関節炎|かんせつえん} (arthritis), {嘔吐|おうと} (vomiting)
- **Onomatopoeia (3)**: がちがち (rigid/stiff), じりじり (scorching/gradually), ごつごつ (rugged/bony)
- **Katakana Loanwords (5)**: コミュニケーション (communication), コミュニティ (community), ワンルーム (studio apartment), システム (system), エラー (error)
- **Environment (3)**: {伐採|ばっさい} (logging), {植林|しょくりん} (afforestation), {食物連鎖|しょくもつれんさ} (food chain)
- **Personality Types (3)**: {食|く}わず{嫌|ぎら}い (disliking without trying), {恥|は}ずかしがり{屋|や} (shy person), {寂|さび}しがり{屋|や} (lonely person)
- **Compound Verbs (2)**: {撒|ま}き{散|ち}らす (to scatter), {掻|か}き{消|け}す (to drown out)
- **Weather/Seasons (2)**: {花冷|はなび}え (late spring cold), {寝違|ねちが}える (stiff neck from sleep)
- **Household (1)**: {整理整頓|せいりせいとん} (organizing/tidying up)
- **Traditional (1)**: {弓|ゆみ} (bow)
- **Expression (1)**: もしかしたら (perhaps/maybe)
- **Miscellaneous (3)**: {方角|ほうがく} (direction), {試乗|しじょう} (test drive), {鉄筋|てっきん} (rebar/reinforced concrete)

Notable entry features:
- Medical vocabulary cluster: disease names ending in {炎|えん} ({肺炎|はいえん}/{関節炎|かんせつえん})
- Onomatopoeia with texture/sensation meanings: がちがち/じりじり/ごつごつ (mimetic words)
- Environmental vocabulary: {伐採|ばっさい}/{植林|しょくりん} (forestry), {食物連鎖|しょくもつれんさ} (ecology)
- Personality type patterns with {屋|や}: {恥|は}ずかしがり{屋|や}/{寂|さび}しがり{屋|や}
- Traditional Japanese culture: {弓|ゆみ} with notes on {弓道|きゅうどう} (kyudo)
- Wasei-eigo terms: ワンルーム (studio apartment), with housing terminology notes
- 5 new kanji added to kanji index: 伐 (02089), 喘 (02090), 嘔 (02091), 撒 (02092), 肺 (02093)

Total entries: 8,409 → 8,439
Remaining candidates: ~560 → ~530
New kanji: 2,088 → 2,093

### 2026-01-26 (Vocabulary Expansion - 30 New Entries, Session 171)
Added 30 new dictionary entries from candidate_words.json, covering counter questions, time/celestial vocabulary, weather terms, compound verbs, financial vocabulary, memory-related words, travel expressions, cognitive abilities, housing rooms, and Japanese food:

- **Counter Questions (3)**: {何度|なんど} (how many times), {何人|なんにん} (how many people), {何歳|なんさい} (how old)
- **Time/Celestial (5)**: {明|あ}け{方|がた} (dawn), {日|ひ}の{出|で} (sunrise), {三日月|みかづき} (crescent moon), {満月|まんげつ} (full moon), {新月|しんげつ} (new moon)
- **Weather (2)**: {通|とお}り{雨|あめ} (passing shower), {底冷|そこび}え (bone-chilling cold)
- **Compound Verbs (4)**: {聞|き}き{慣|な}れる (become used to hearing), {迷|まよ}い{込|こ}む (wander into), {引|ひ}き{抜|ぬ}く (pull out/headhunt), {投|な}げ{込|こ}む (throw into)
- **Financial (3)**: {利子|りし} (interest), {分割払|ぶんかつばら}い (installment payment), {一括払|いっかつばら}い (lump-sum payment)
- **Memory/Error (3)**: {勘違|かんちが}い (misunderstanding), {物忘|ものわす}れ (forgetfulness), {ど忘|わす}れ (memory lapse)
- **Travel (2)**: {日帰|ひがえ}り (day trip), {外泊|がいはく} (staying out overnight)
- **Cognitive Abilities (4)**: {集中力|しゅうちゅうりょく} (concentration), {想像力|そうぞうりょく} (imagination), {記憶力|きおくりょく} (memory), {判断力|はんだんりょく} (judgment)
- **Housing (2)**: {洗面所|せんめんじょ} (washroom), {脱衣所|だついじょ} (changing room)
- **Japanese Food (2)**: {肉|にく}じゃが (nikujaga), {親子丼|おやこどん} (oyakodon)

Notable entry features:
- Moon phase vocabulary cluster: {新月|しんげつ}/{三日月|みかづき}/{満月|まんげつ} with astronomical notes
- Cognitive ability cluster: {集中力|しゅうちゅうりょく}/{想像力|そうぞうりょく}/{記憶力|きおくりょく}/{判断力|はんだんりょく} (～{力|りょく} compounds)
- Payment vocabulary contrast: {分割払|ぶんかつばら}い vs {一括払|いっかつばら}い
- Memory-related words: {物忘|ものわす}れ (chronic) vs {ど忘|わす}れ (momentary) vs {勘違|かんちが}い (misinterpretation)
- Japanese bath culture: {洗面所|せんめんじょ}/{脱衣所|だついじょ} with house layout notes
- Home cooking classics: {肉|にく}じゃが/{親子丼|おやこどん} with recipe and cultural notes
- Multi-sense entry: {引|ひ}き{抜|ぬ}く (physical pulling vs. headhunting)

Total entries: 8,379 → 8,409
Remaining candidates: ~590 → ~560

### 2026-01-26 (New Candidates - 100 Words Added)
Added 100 new candidate words to `candidate_words.json` across diverse domains:

**Common Adverbs/Expressions (3)**: {改|あらた}めて (anew), {思|おも}い{切|き}り (with all one's might), やむを{得|え}ず (unavoidably)

**Housing/Architecture (6)**: {書棚|しょだな} (bookshelf), {洗面所|せんめんじょ} (washroom), {脱衣所|だついじょ} (changing room), {応接間|おうせつま} (reception room), {踊|おど}り{場|ば} (landing of stairs)

**Household Chores (5)**: {芝刈|しばか}り (lawn mowing), {草取|くさと}り (weeding), {水撒|みずま}き (watering), {雑巾|ぞうきん}がけ (mopping), {窓拭|まどふ}き (window cleaning)

**Cooking/Food (9)**: {圧力鍋|あつりょくなべ} (pressure cooker), {蒸|む}し{器|き} (steamer), {炒|いた}め{物|もの} (stir-fry), {出汁巻|だしま}き{卵|たまご} (rolled omelet), きんぴら (kinpira), {筑前煮|ちくぜんに} (chicken stew), {肉|にく}じゃが (nikujaga), {親子丼|おやこどん} (oyakodon), カツ{丼|どん} (katsudon), {牛丼|ぎゅうどん} (gyudon)

**Sports (9)**: {審判員|しんぱんいん} (referee), {線審|せんしん} (line judge), {逆転勝|ぎゃくてんが}ち (comeback victory), {先制点|せんせいてん} (opening goal), {同点|どうてん} (tie score), {空振|からぶ}り (swing and miss), {三振|さんしん} (strikeout), ノーヒット (no-hitter), {打点|だてん} (RBI)

**Technology/Social Media (9)**: SNS{映|ば}え (Instagram-worthy), リポスト (repost), エンゲージメント (engagement), {音声入力|おんせいにゅうりょく} (voice input), {顔認証|かおにんしょう} (facial recognition), {指紋認証|しもんにんしょう} (fingerprint auth), {二段階認証|にだんかいにんしょう} (2FA), クラウドサービス (cloud service), サブスクリプション (subscription)

**Work/Employment (9)**: オンライン{診療|しんりょう} (telemedicine), ハイブリッド{勤務|きんむ} (hybrid work), ワーケーション (workcation), {時差出勤|じさしゅっきん} (staggered hours), フレックス{制|せい} (flextime), {兼業|けんぎょう} (side business), {雇用形態|こようけいたい} (employment type)

**Health/Medical (11)**: メンタルヘルス (mental health), {燃|も}え{尽|つ}き{症候群|しょうこうぐん} (burnout syndrome), {適応障害|てきおうしょうがい} (adjustment disorder), {自律神経|じりつしんけい} (autonomic nervous system), {更年期|こうねんき} (menopause), {免疫力|めんえきりょく} (immunity), {後遺症|こういしょう} (aftereffect), {既往症|きおうしょう} (medical history), {生活習慣病|せいかつしゅうかんびょう} (lifestyle disease), {内臓脂肪|ないぞうしぼう} (visceral fat), {過労|かろう} (overwork)

**Family/Society (7)**: {栄養不足|えいようぶそく} (nutritional deficiency), {運動不足|うんどうぶそく} (lack of exercise), {体力低下|たいりょくていか} (physical decline), {共働|ともばたら}き (dual-income), {待機児童|たいきじどう} (daycare waitlist), {育休|いくきゅう} (childcare leave), {介護休暇|かいごきゅうか} (nursing care leave)

**Education (9)**: {遠隔授業|えんかくじゅぎょう} (remote classes), {学力|がくりょく} (academic ability), {終業式|しゅうぎょうしき} (closing ceremony), {始業式|しぎょうしき} (opening ceremony), クラス{替|が}え (class reshuffling), {通知表|つうちひょう} (report card), {時間割|じかんわり} (timetable), {内申点|ないしんてん} (internal assessment), {偏差値|へんさち} (deviation score), {課外活動|かがいかつどう} (extracurricular), {卒論|そつろん} (graduation thesis)

**Weather/Seasons (6)**: {厳冬|げんとう} (severe winter), {五月晴|さつきば}れ (May weather), {木枯|こが}らし (wintry wind), {雪解|ゆきど}け (thaw), {霜柱|しもばしら} (frost pillars), {残暑|ざんしょ} (lingering heat), {晩秋|ばんしゅう} (late autumn), {初冬|しょとう} (early winter)

**Body/Physical (9)**: {眉間|みけん} (between eyebrows), うなじ (nape of neck), みぞおち (solar plexus), {土踏|つちふ}まず (arch of foot), {青筋|あおすじ} (blue vein), {鳥肌|とりはだ} (goosebumps), {吹|ふ}き{出物|でもの} (pimple), あばた (pockmarks), {歯|は}ぎしり (teeth grinding)

**Sleep-related (6)**: {寝違|ねちが}い (stiff neck from sleep), {寝|ね}つき (sleep onset), {寝覚|ねざ}め (awakening), {目覚|めざ}まし (alarm clock)

**Transportation (2)**: {通勤電車|つうきんでんしゃ} (commuter train), {始発電車|しはつでんしゃ} (first train)

Notable patterns:
- Japanese food culture: Popular donburi dishes and home cooking terminology
- Modern work vocabulary: Remote/hybrid work, work-life balance terms
- Health awareness: Mental health, lifestyle diseases, medical terminology
- Daily life vocabulary: Sleep, body parts, household chores
- Sports terminology: Baseball and competition vocabulary

Candidate count: 490 → 590

### 2026-01-26 (New Candidates - 102 Words Added)
Added 102 new candidate words to `candidate_words.json` across diverse domains:

**Counter Questions (7)**: {何度|なんど} (how many times), {何回|なんかい} (how many times), {何人|なんにん} (how many people), {何枚|なんまい} (how many flat objects), {何冊|なんさつ} (how many books), {何杯|なんばい} (how many cups), {何歳|なんさい} (how old)

**Function Words/Demonstratives (12)**: どちらも (both), {誰|だれ}でも (anyone), そのため (therefore), {その後|そのご} (after that), {その前|そのまえ} (before that), {その間|そのあいだ} (meanwhile), {向|む}こう{側|がわ} (other side), それとなく (indirectly), それなりに (in its own way), それにしても (nevertheless), {何|なん}となく (somehow), {何|なに}かと (one way or another)

**Time Expressions (7)**: {明|あ}け{方|がた} (dawn), {日|ひ}の{出|で} (sunrise), {朝帰|あさがえ}り (coming home in the morning), {日帰|ひがえ}り (day trip), {泊|とま}りがけ (overnight stay), {外泊|がいはく} (staying out overnight), オールナイト (all-night)

**Celestial Bodies (4)**: {三日月|みかづき} (crescent moon), {満月|まんげつ} (full moon), {新月|しんげつ} (new moon), {半月|はんげつ} (half moon)

**Weather (3)**: {通|とお}り{雨|あめ} (passing shower), {底冷|そこび}え (bone-chilling cold), {上弦|じょうげん} (first quarter moon)

**Cooking Terms (12)**: ぶつ{切|ぎ}り (rough chopping), {半切|はんぎ}り (cutting in half), {細切|ほそぎ}り (thin strips), {湯通|ゆどお}し (blanching), {水切|みずき}り (draining water), {油切|あぶらき}り (draining oil), {塩加減|しおかげん} (saltiness), {焦|こ}げ{目|め} (char marks), とろ{火|び} (low heat)

**Compound Verbs (10)**: {聞|き}き{慣|な}れる (become used to hearing), {食|た}べ{慣|な}れる (become used to eating), {住|す}み{慣|な}れる (become accustomed to living), {引|ひ}き{抜|ぬ}く (to pull out), {投|な}げ{込|こ}む (to throw into), {迷|まよ}い{込|こ}む (to wander into)

**Financial Terms (4)**: {利子|りし} (interest), {分割払|ぶんかつばら}い (installment payment), {一括払|いっかつばら}い (lump-sum payment), {副業|ふくぎょう} (side job)

**Mistake/Error Terms (6)**: {聞|き}き{間違|まちが}い (mishearing), {言|い}い{間違|まちが}い (slip of tongue), {書|か}き{間違|まちが}い (writing mistake), {読|よ}み{間違|まちが}い (misreading), {見間違|みまちが}い (mistake in seeing), {勘違|かんちが}い (misunderstanding)

**Personality/Traits (10)**: {恥|は}ずかしがり (shy person), {世話好|せわず}き (likes to help), {物忘|ものわす}れ (forgetfulness), ど{忘|わす}れ (memory lapse), うっかり{忘|わす}れ (careless forgetfulness), {気分転換|きぶんてんかん} (change of pace), {気分屋|きぶんや} (moody person), {記憶違|きおくちが}い (faulty memory), {思|おも}い{違|ちが}い (misconception)

**Ability/力 Compounds (16)**: {気力|きりょく} (willpower), {脚力|きゃくりょく} (leg strength), {腕力|わんりょく} (arm strength), {握力|あくりょく} (grip strength), {持久力|じきゅうりょく} (endurance), {瞬発力|しゅんぱつりょく} (explosive power), {集中力|しゅうちゅうりょく} (concentration), {記憶力|きおくりょく} (memory), {判断力|はんだんりょく} (judgment), {決断力|けつだんりょく} (decisiveness), {行動力|こうどうりょく} (action ability), {実行力|じっこうりょく} (execution ability), {想像力|そうぞうりょく} (imagination), {洞察力|どうさつりょく} (insight), {観察力|かんさつりょく} (observation), {分析力|ぶんせきりょく} (analysis), {理解力|りかいりょく} (comprehension), {説得力|せっとくりょく} (persuasiveness)

**Transportation (5)**: {運転見合|うんてんみあ}わせ (service suspension), {運転再開|うんてんさいかい} (resumption of service), {車両点検|しゃりょうてんけん} (train inspection), {信号故障|しんごうこしょう} (signal malfunction), {睡眠不足|すいみんぶそく} (sleep deprivation)

**Other (6)**: {同期|どうき}する (to synchronize), ワイヤレス (wireless), じんわり (gradually), いくら{何|なん}でも (no matter what), {自力|じりき} (one's own power), {他力|たりき} (help from others)

Notable patterns:
- Counter question words: Complete {何|なん}+counter pattern
- Ability vocabulary: Comprehensive 〜{力|りょく} compounds covering physical, mental, and cognitive abilities
- Mistake vocabulary: Systematic 〜{間違|まちが}い patterns for different senses
- Transportation announcements: Common train delay/suspension vocabulary

Candidate count: 388 → 490

### 2026-01-26 (Vocabulary Expansion - 30 New Entries, Session 170)
Added 30 new dictionary entries from candidate_words.json, covering science/physics terminology, legal/government vocabulary, sports competition terms, infrastructure/location words, academic/publishing terms, and technology vocabulary:

- **Science/Physics (5)**: {反射|はんしゃ} (reflection/reflex), {共鳴|きょうめい} (resonance/sympathy), {屈折|くっせつ} (refraction), {融解|ゆうかい} (melting), {光合成|こうごうせい} (photosynthesis)
- **Legal/Government (7)**: {冤罪|えんざい} (false accusation), {黙秘|もくひ} (silence/refusing to answer), {公布|こうふ} (promulgation), {採決|さいけつ} (vote), {否決|ひけつ} (rejection), {訴状|そじょう} (complaint), {陳述|ちんじゅつ} (statement)
- **Sports/Competition (4)**: トーナメント (tournament), リーグ{戦|せん} (league match), {不戦勝|ふせんしょう} (win by default), {大差|たいさ} (big difference)
- **Infrastructure/Location (5)**: {舗装|ほそう} (paving), {石畳|いしだたみ} (cobblestone), {突|つ}き{当|あ}たり (dead end), {縁石|えんせき} (curb), {軒先|のきさき} (eaves/shopfront)
- **Academic/Publishing (3)**: {査読|さどく} (peer review), {凡例|はんれい} (legend/explanatory notes), {抄録|しょうろく} (abstract)
- **Technology (4)**: {暗号化|あんごうか} (encryption), {復号|ふくごう} (decryption), {並列|へいれつ} (parallel), {直列|ちょくれつ} (serial)
- **Household/Other (2)**: {窓際|まどぎわ} (by the window/sidelined), {追|お}い{焚|だ}き (reheating bath)

Notable entry features:
- Physics vocabulary cluster: {反射|はんしゃ}/{屈折|くっせつ} (reflection vs refraction), {融解|ゆうかい}/{光合成|こうごうせい}
- Legal process vocabulary: {訴状|そじょう}/{陳述|ちんじゅつ}/{黙秘|もくひ} (courtroom terms)
- Legislative process: {採決|さいけつ}/{否決|ひけつ}/{公布|こうふ} (voting and promulgation)
- Competition formats: トーナメント vs リーグ{戦|せん} (knockout vs round-robin)
- Circuit terminology: {並列|へいれつ} vs {直列|ちょくれつ} (parallel vs series)
- Multi-sense entries: {反射|はんしゃ} (light reflection vs physiological reflex), {共鳴|きょうめい} (physics vs sympathy), {屈折|くっせつ} (physics vs psychological), {窓際|まどぎわ} (location vs sidelined employee)
- 3 new kanji added to kanji index: 冤 (02086), 抄 (02087), 舗 (02088)

Total entries: 8,349 → 8,379
Remaining candidates: ~418 → ~388
New kanji: 2,085 → 2,088

### 2026-01-26 (Vocabulary Expansion - 30 New Entries, Session 169)
Added 30 new dictionary entries from candidate_words.json, covering workplace/business vocabulary, relationship conflicts, entertainment/media terminology, and technology terms:

- **Workplace/Career (8)**: {値切|ねぎ}る (to haggle), {勤務先|きんむさき} (workplace), {昇格|しょうかく} (promotion), {引|ひ}き{継|つ}ぎ (handover), {申|もう}し{送|おく}り (handover briefing), {半休|はんきゅう} (half-day off), {繁忙期|はんぼうき} (busy season), {閑散期|かんさんき} (slow season)
- **Relationship Conflicts (7)**: {揉|も}め{事|ごと} (trouble/dispute), {八|や}つ{当|あ}たり (taking out anger), {逆恨|さかうら}み (misplaced resentment), {口論|こうろん} (argument), {疎遠|そえん} (estranged), {破局|はきょく} (breakup), {絶縁|ぜつえん} (severing ties)
- **Entertainment/Media (8)**: {楽屋|がくや} (dressing room), {舞台裏|ぶたいうら} (backstage), {収録|しゅうろく} (recording), {予告|よこく} (preview/trailer), {上映|じょうえい} (screening), {視聴率|しちょうりつ} (viewer ratings), {観覧|かんらん} (viewing), {喝采|かっさい} (applause)
- **Business/Academic (4)**: {保留|ほりゅう} (pending/on hold), {審査|しんさ} (examination), {補足|ほそく} (supplement), {校閲|こうえつ} (proofreading)
- **Technology/Other (3)**: {課金|かきん} (billing/in-app purchase), {分解|ぶんかい} (disassembly), {抜|ぬ}け{道|みち} (shortcut/loophole)

Notable entry features:
- Workplace transition vocabulary: {引|ひ}き{継|つ}ぎ (handover tasks) vs {申|もう}し{送|おく}り (handover briefing)
- Seasonal business terms: {繁忙期|はんぼうき} vs {閑散期|かんさんき} (busy vs slow season)
- Relationship deterioration scale: {疎遠|そえん} → {破局|はきょく} → {絶縁|ぜつえん}
- Entertainment industry vocabulary: {楽屋|がくや}/{舞台裏|ぶたいうら} (behind the scenes)
- Multi-sense entries: {絶縁|ぜつえん} (severing ties vs electrical insulation), {分解|ぶんかい} (disassembly vs decomposition), {抜|ぬ}け{道|みち} (shortcut vs loophole)
- 4 new kanji added to kanji index: 喝 (02082), 繁 (02083), 閑 (02084), 閲 (02085)

Total entries: 8,319 → 8,349
Remaining candidates: ~448 → ~418
New kanji: 2,081 → 2,085

### 2026-01-26 (Vocabulary Expansion - 30 New Entries, Session 168)
Added 30 new dictionary entries from candidate_words.json, covering health/body vocabulary, weather/seasons, personality types, food/cooking, lifestyle/home, transportation, social customs/gifts, and emotions:

- **Health/Body (5)**: {熱中症|ねっちゅうしょう} (heatstroke), {二日酔|ふつかよ}い (hangover), {五月病|ごがつびょう} (May blues), {仮眠|かみん} (nap), {寝落|ねお}ち (falling asleep unintentionally)
- **Weather/Seasons (4)**: {秋晴|あきば}れ (clear autumn weather), {小春日和|こはるびより} (Indian summer), {梅雨入|つゆい}り (start of rainy season), {梅雨明|つゆあ}け (end of rainy season)
- **Personality/Eating Types (4)**: {甘党|あまとう} (sweet tooth), {辛党|からとう} (spice/alcohol lover), {大食|おおぐ}い (big eater), {怖|こわ}がり (scaredy-cat)
- **Food/Cooking (4)**: {出来立|できた}て (freshly made), {焼|や}き{立|た}て (freshly baked), {作|つく}り{置|お}き (meal prep), こだわり (commitment/obsession)
- **Lifestyle/Home (3)**: {大掃除|おおそうじ} (major cleaning), {断捨離|だんしゃり} (decluttering), {住|す}み{心地|ごこち} (livability)
- **Transportation (3)**: {満員電車|まんいんでんしゃ} (packed train), {吊|つ}り{革|かわ} (train strap), {振替輸送|ふりかえゆそう} (alternative transport)
- **Social/Gifts (4)**: {手土産|てみやげ} (visiting gift), お{返|かえ}し (return gift), {二次会|にじかい} (after-party), ご{祝儀|しゅうぎ} (congratulatory money)
- **Emotions/Expressions (2)**: {苦笑|にがわら}い (bitter smile), {愛想笑|あいそうわら}い (forced smile)
- **Work/Career (1)**: {出世|しゅっせ} (career advancement)

Notable entry features:
- Japanese health vocabulary: {熱中症|ねっちゅうしょう} (summer danger), {二日酔|ふつかよ}い (hangover remedies), {五月病|ごがつびょう} (adjustment disorder)
- Seasonal weather cluster: {秋晴|あきば}れ/{小春日和|こはるびより} (autumn), {梅雨入|つゆい}り/{梅雨明|つゆあ}け (rainy season)
- Eating preference types: {甘党|あまとう} vs {辛党|からとう} (sweets vs alcohol historically)
- ～{立|た}て pattern: {出来立|できた}て/{焼|や}き{立|た}て (freshness suffix)
- Commuting vocabulary: {満員電車|まんいんでんしゃ}/{吊|つ}り{革|かわ}/{振替輸送|ふりかえゆそう}
- Japanese gift culture: {手土産|てみやげ}/お{返|かえ}し/ご{祝儀|しゅうぎ}
- Multi-sense entries: {辛党|からとう} (alcohol lover vs spicy food lover), {大食|おおぐ}い (big eater vs eating contest), こだわり (positive dedication vs negative fixation)

Total entries: 8,289 → 8,319
Remaining candidates: ~478 → ~448

### 2026-01-25 (New Candidates - 100 Words Added)
Added 100 new candidate words to `candidate_words.json` across diverse domains:

**Health/Body (8)**: {寝違|ねちが}える (stiff neck), {肌荒|はだあ}れ (skin irritation), {五月病|ごがつびょう} (May blues), {熱中症|ねっちゅうしょう} (heatstroke), {食|しょく}あたり (food poisoning), {二日酔|ふつかよ}い (hangover), {湯冷|ゆざ}め (catching cold after bath), {仮眠|かみん} (nap), {寝落|ねお}ち (falling asleep unintentionally)

**Weather/Seasons (5)**: {花冷|はなび}え (late spring cold snap), {秋晴|あきば}れ (clear autumn weather), {小春日和|こはるびより} (Indian summer), {梅雨入|つゆい}り (start of rainy season), {梅雨明|つゆあ}け (end of rainy season)

**Household/Lifestyle (6)**: {大掃除|おおそうじ} (major cleaning), {整理整頓|せいりせいとん} (organizing), {断捨離|だんしゃり} (decluttering), {食|く}わず{嫌|ぎら}い (disliking without trying), {住|す}み{心地|ごこち} (livability), {書|か}き{心地|ごこち} (writing feel)

**Personality Types (8)**: {恥|は}ずかしがり{屋|や} (shy person), {寂|さび}しがり{屋|や} (lonely person), {怖|こわ}がり (scaredy-cat), {甘党|あまとう} (sweet tooth), {辛党|からとう} (spice lover), {大食|おおぐ}い (big eater), {少食|しょうしょく} (light eater), {早食|はやぐ}い (fast eater)

**Food/Cooking (8)**: {作|つく}り{置|お}き (meal prep), {出来立|できた}て (freshly made), {焼|や}き{立|た}て (freshly baked), {揚|あ}げ{立|た}て (freshly fried), {茹|ゆ}でたて (freshly boiled), {採|と}れたて (freshly harvested), こだわり (commitment/obsession)

**Transportation (12)**: {通勤|つうきん}ラッシュ (commuter rush), {満員電車|まんいんでんしゃ} (packed train), {帰宅|きたく}ラッシュ (evening rush), {駆|か}け{込|こ}み{乗車|じょうしゃ} (rushing onto train), {立|た}ち{乗|の}り (standing on train), {座席争|ざせきあらそ}い (seat competition), {吊|つ}り{革|かわ} (train strap), {車内放送|しゃないほうそう} (train announcement), {運行状況|うんこうじょうきょう} (service status), {振替輸送|ふりかえゆそう} (alternative transport), {落|お}とし{物|もの} (lost property), {回数券|かいすうけん} (book of tickets)

**Train/Transport Types (5)**: グリーン{車|しゃ} (first-class car), {女性専用車両|じょせいせんようしゃりょう} (women-only car), ホームドア (platform screen door), {人身事故|じんしんじこ} (injury accident), {遅延証明|ちえんしょうめい} (delay certificate)

**Work/Business (8)**: {飛|と}び{込|こ}み{営業|えいぎょう} (cold calling), サービス{残業|ざんぎょう} (unpaid overtime), {配置転換|はいちてんかん} (job transfer), {出世|しゅっせ} (career advancement), {窓際族|まどぎわぞく} (sidelined employees), {社内恋愛|しゃないれんあい} (office romance), {飲|の}みニケーション (drinking-based networking), {二次会|にじかい} (after-party)

**Social/Gifts (15)**: {会費|かいひ} (membership fee), {別会計|べつかいけい} (separate checks), {持|も}ち{寄|よ}り (potluck), {手土産|てみやげ} (visiting gift), お{返|かえ}し (return gift), ご{祝儀|しゅうぎ} (congratulatory money), のし{袋|ぶくろ} (money gift envelope), お{年玉|としだま} (New Year's money), {引|ひ}っ{越|こ}し{祝|いわ}い (housewarming gift), {出産祝|しゅっさんいわ}い (baby gift), {入学祝|にゅうがくいわ}い (school entrance gift), {卒業祝|そつぎょういわ}い (graduation gift), {就職祝|しゅうしょくいわ}い (job celebration gift), {快気祝|かいきいわ}い (recovery gift)

**Expressions/Smiles (13)**: {無神経|むしんけい} (insensitive), {顔色|かおいろ}をうかがう (watching expression), {愛想笑|あいそうわら}い (forced smile), {作|つく}り{笑|わら}い (fake smile), {笑|わら}いすぎ (laughing too much), {苦笑|にがわら}い (bitter smile), {照|て}れ{笑|わら}い (embarrassed smile), {泣|な}き{笑|わら}い (laughing through tears), {薄笑|うすわら}い (smirk), {高笑|たかわら}い (loud laugh), {思|おも}い{出|だ}し{笑|わら}い (laughing at memory), {嘘泣|うそな}き (fake crying), もらい{泣|な}き (sympathetic crying)

**Communication/Personality (12)**: {揚|あ}げ{足取|あしと}り (nitpicking), {告|つ}げ{口|ぐち} (tattling), {口喧嘩|くちげんか} (verbal argument), {多弁|たべん} (talkative), {話|はな}し{上手|じょうず} (good speaker), {聞|き}き{上手|じょうず} (good listener), {甘|あま}え{上手|じょうず} (good at being spoiled), {世渡|よわた}り{上手|じょうず} (socially adept), {場見知|ばみし}り (shy in new places), {社交的|しゃこうてき} (sociable), {内向的|ないこうてき} (introverted), {外向的|がいこうてき} (extroverted), {二面性|にめんせい} (two-faced nature)

Notable patterns:
- Japanese social customs: gift-giving occasions, celebration types
- Workplace culture: commuter experience, office dynamics
- Personality vocabulary: types and traits
- Expressions of laughter/crying: nuanced emotional vocabulary
- "Freshly made" patterns: ~{立|た}て compound words
- "-{上手|じょうず}" skill patterns: communication abilities

Candidate count: 438 → 538

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
4. Place file in correct directory based on numeric ID range:
   - Directory: `entries/{range}/` where `{range}` is based on the 5-digit ID:
     - IDs 00001-00499 → `entries/00000/`
     - IDs 00500-00999 → `entries/00500/`
     - IDs 01000-01499 → `entries/01000/`
     - etc. (500 entries per directory)
   - Example: `entries/00000/00396_taberu.json`
5. File naming: `{5-digit-id}_{romaji}.json`

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
python3 build/validate.py --id 00396_taberu

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
- Format: `{5-digit-id}_{romanized_reading}.json`
- Romanization: Modified Hepburn with kana-faithful long vowels
- Directory: `entries/{range}/` where `{range}` is based on the numeric ID:
  - IDs 00001-00499 → `entries/00000/`
  - IDs 00500-00999 → `entries/00500/`
  - IDs 01000-01499 → `entries/01000/`
  - etc. (500 entries per directory)
- Example: `entries/00000/00396_taberu.json`
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
