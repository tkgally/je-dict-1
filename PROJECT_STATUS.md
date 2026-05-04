# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-17
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

### 2026-05-04 (Vocabulary Expansion - 30 New Entries, Batch 88)
Added 30 new dictionary entries (IDs 26702-26731) from candidate_words.json. Vocabulary covers shapes/math, product categories, education, transportation, culture/language, family, society, finance, stationery, and more.

- **Shapes/math (2)**: {六角|ろっかく} (hexagonal), {商|しょう} (quotient)
- **Product categories (3)**: {一般用|いっぱんよう} (for general use), {個人用|こじんよう} (for personal use), {農業用|のうぎょうよう} (for agricultural use)
- **Education (2)**: {男子学生|だんしがくせい} (male student), {非専門|ひせんもん} (non-specialist)
- **Transportation (1)**: {左車線|ひだりしゃせん} (left lane)
- **Culture/entertainment (2)**: {西洋映画|せいようえいが} (Western film), {文化週間|ぶんかしゅうかん} (Culture Week)
- **Language/writing (2)**: {和字|わじ} (Japanese-made characters), {罫線入|けいせんい}り (ruled/lined)
- **Law/politics (2)**: {国籍法|こくせきほう} (nationality law), {再就任|さいしゅうにん} (reappointment)
- **Society/people (4)**: {非常識人|ひじょうしきじん} (person lacking common sense), {貧困者|ひんこんしゃ} (person in poverty), {徘徊者|はいかいしゃ} (wanderer), {遭遇者|そうぐうしゃ} (witness/person who encounters)
- **Family (1)**: {恋女房|こいにょうぼう} (beloved wife)
- **Technology/daily life (2)**: フロアマップ (floor map), {画面|がめん}サイズ (screen size)
- **Finance (1)**: {残高証明|ざんだかしょうめい} (balance certificate)
- **Material (1)**: {天然皮革|てんねんひかく} (natural leather)
- **Work (2)**: {社外活動|しゃがいかつどう} (outside-company activities), {起用法|きようほう} (personnel deployment method)
- **Nature (1)**: {白々明|しらじらあ}ける (to dawn — literary)
- **Health (1)**: {放屁|ほうひ} (flatulence — formal)
- **Science (1)**: {結晶体|けっしょうたい} (crystalline body)
- **Quantity (1)**: {数冊|すうさつ} (several books)
- **Technology change (1)**: {精巧化|せいこうか} (increasing sophistication)
- 1 stale candidate removed (灰色 — duplicate of existing entry)
- 30 candidates synced from candidate list

Total entries: 26,494 → 26,524.

### 2026-05-04 (Vocabulary Expansion - 18 New Entries, Batch 87)
Added 18 new dictionary entries (IDs 26684-26701) from candidate_words.json. Diverse vocabulary covering description, environment, food/cooking, counters, daily life, entertainment, games, sports, technology, business, literature, and media.

- **Na-adjectives (2)**: {多発的|たはつてき} (frequent; repeated), {地球的|ちきゅうてき} (global; planetary)
- **Food/cooking (2)**: {副料理長|ふくりょうりちょう} (sous chef), すき{焼|や}き{鍋|なべ} (sukiyaki pot)
- **Daily life (2)**: ビニールシート (vinyl sheet/tarp), {床磨|ゆかみが}き (floor polishing)
- **Counter/question (1)**: {何個|なんこ} (how many small objects)
- **Entertainment (1)**: クラシック{映画|えいが} (classic film)
- **Games (1)**: {手番|てばん} (one's turn in a game)
- **Evaluation (1)**: {見外|みはず}れ (misjudgment; disappointment)
- **Consumer/tech (2)**: {最新|さいしん}モデル (latest model), タスク{管理|かんり} (task management)
- **Technology/business (1)**: データ{入力|にゅうりょく} (data entry)
- **Loanwords (2)**: ミドルエイジ (middle age), セービング (save in sports)
- **Literature/media (1)**: あとがたり (afterword; epilogue)
- **Sports (1)**: {真芯|ましん} (sweet spot)
- **Expression (1)**: すました{顔|かお} (composed/straight face)
- 1 stale candidate removed (duplicate of existing entry)
- 17 candidates synced from candidate list

Total entries: 26,476 → 26,494.

### 2026-05-04 (Vocabulary Expansion - 15 New Entries, Batch 86)
Added 15 new dictionary entries (IDs 26669-26683) from candidate_words.json. Diverse vocabulary covering language/writing, culture, daily life, science, geopolitics, sports, and body parts.

- **Language/writing (3)**: {行|ぎょう} (line/row of text), {愛称語|あいしょうご} (term of endearment), {片|かた} (one of a pair — prefix)
- **Culture/food (1)**: {三色団子|さんしょくだんご} (three-colored dango)
- **Daily life/community (1)**: {資源回収|しげんかいしゅう} (recyclable collection)
- **Politics/news (1)**: {投票数|とうひょうすう} (vote count)
- **Business (1)**: {卸売価格|おろしうりかかく} (wholesale price)
- **Science (1)**: {液体窒素|えきたいちっそ} (liquid nitrogen)
- **Pop culture (1)**: {火星人|かせいじん} (Martian)
- **Sports (1)**: {完封勝利|かんぷうしょうり} (shutout victory)
- **Geopolitics (1)**: {海洋国家|かいようこっか} (maritime nation)
- **Photography (1)**: {一眼|いちがん}カメラ (single-lens camera)
- **People (2)**: {援助者|えんじょしゃ} (aid worker), {異国人|いこくじん} (foreigner — literary)
- **Body part (1)**: {腓|こむら} (calf of the leg)
- 1 new kanji added to kanji index: 腓
- 15 candidates synced from candidate list

Total entries: 26,461 → 26,476.

### 2026-05-03 (Vocabulary Expansion - 15 New Entries, Batch 85)
Added 15 new dictionary entries (IDs 26639-26653) from candidate_words.json. Diverse vocabulary covering news/media, architecture, education, food culture, workplace, linguistics, literature, computing, business, and color terms.

- **News/media (2)**: {速報値|そくほうち} (preliminary figure), {隔週刊|かくしゅうかん} (biweekly publication)
- **Architecture (1)**: {三階建|さんがいだ}て (three-story building)
- **Education (1)**: {第二志望|だいにしぼう} (second choice)
- **Food culture (1)**: {寿司盛|すしも}り (sushi platter)
- **Workplace (1)**: {連続勤務|れんぞくきんむ} (consecutive work days)
- **Linguistics (1)**: {新造語|しんぞうご} (neologism)
- **Literature (2)**: {女主人公|じょしゅじんこう} (female protagonist), {通俗文学|つうぞくぶんがく} (popular literature)
- **Computing (1)**: {再読|さいよ}み{込|こ}み (reload/refresh)
- **Business (1)**: {一人会社|ひとりがいしゃ} (one-person company)
- **Color terms (2)**: {薄灰色|うすはいいろ} (light gray), {濃灰色|のうはいいろ} (dark gray)
- **Medical/daily life (1)**: {寝小便|ねしょうべん} (bedwetting)
- **Na-adjective (1)**: {外観的|がいかんてき} (external, superficial)
- 15 candidates synced from candidate list

Total entries: 26,431 → 26,446.

### 2026-05-03 (Vocabulary Expansion - 28 New Entries, Batch 84)
Added 28 new dictionary entries (IDs 26611-26638) from candidate_words.json. Vocabulary covers Japanese culture, science, logistics, military history, nature, and specialized domains.

- **Culture/tradition (6)**: {刀鞘|かたなざや} (sword sheath), {弓弦|ゆみづる} (bowstring), {社務|しゃむ} (shrine duties), {祭殿|さいでん} (ceremonial hall), {良日|りょうじつ} (auspicious day), {馬車道|ばしゃみち} (carriage road)
- **Performing arts/games (3)**: {立役|たてやく} (leading kabuki role), {点棒|てんぼう} (mahjong scoring sticks), {咥|くわ}え{煙草|たばこ} (cigarette dangling from mouth)
- **Science/physics (3)**: {電導|でんどう} (electrical conduction), {導熱|どうねつ} (heat conduction), {孵卵|ふらん} (incubation)
- **Military/historical (2)**: {兵馬|へいば} (troops and horses), {空拳|くうけん} (bare fists)
- **Geography/nature (4)**: {海湾|かいわん} (bay/gulf), {土質|どしつ} (soil quality), {夏虫|なつむし} (summer insect), {放魚|ほうぎょ} (fish stocking)
- **Construction/materials (3)**: {新造|しんぞう} (new construction), {芯材|しんざい} (core material), {冷温|れいおん} (cold and warm)
- **Business/logistics (2)**: {着荷|ちゃくに} (arrival of goods), {転所|てんしょ} (facility transfer)
- **Transportation (3)**: {手車|てぐるま} (handcart), {副翼|ふくよく} (aileron), {乱走|らんそう} (reckless driving)
- **Food/biology (1)**: {種実|しゅじつ} (nuts and seeds)
- **Law/sports (1)**: {誤判|ごはん} (misjudgment)
- 2 stale duplicate candidates removed (律詩, 銅色); 28 candidates synced

Total entries: 26,403 → 26,431.

### 2026-05-03 (Vocabulary Expansion - 20 New Entries, Batch 83)
Added 20 new dictionary entries (IDs 26591-26610) from candidate_words.json. Mix of essential grammar patterns, cultural vocabulary, sports terminology, and practical words across diverse domains.

- **Grammar patterns/expressions (6)**: はずだ (should be/expected to), べきだ (should/ought to), ようだ (seems/like/so that), {問題|もんだい}ない (no problem), どれぐらい (how much/long), ごとし (like/as if — literary)
- **Sports/baseball (2)**: {先発|せんぱつ}{投手|とうしゅ} (starting pitcher), {首位|しゅい}{打者|だしゃ} (batting champion)
- **Culture/history (3)**: {縄文|じょうもん}{土器|どき} (Jomon pottery), {民俗|みんぞく}{芸能|げいのう} (folk performing arts), {記念|きねん}アルバム (commemorative album)
- **Academic/education (3)**: {環境学|かんきょうがく} (environmental studies), {授業案|じゅぎょうあん} (lesson plan), {接続|せつぞく}{助詞|じょし} (conjunctive particle)
- **Science (1)**: {古生物|こせいぶつ} (fossil organism)
- **Entertainment (1)**: {名|めい}{脇役|わきやく} (great supporting actor)
- **Physical description (1)**: {高身長|こうしんちょう} (tall stature)
- **Food/cooking (1)**: {拍子木|ひょうしぎ}{切|ぎ}り (baton cut)
- **Politics (1)**: {核拡散|かくかくさん} (nuclear proliferation)
- **Legal (1)**: {在留権|ざいりゅうけん} (right of residence)
- 20 candidates synced from candidate list

Total entries: 26,383 → 26,403.


### 2026-05-02 (Vocabulary Expansion - 18 New Entries, Batch 80)
Added 18 new dictionary entries (IDs 26535-26552) from candidate_words.json. Diverse vocabulary spanning medical, business, technology, food culture, martial arts, and family terminology.

- **Medical (2)**: {既往歴|きおうれき} (medical history), {瘢痕|はんこん} (scar tissue)
- **Business/economics (2)**: {製造原価|せいぞうげんか} (manufacturing cost), {通貨流通|つうかりゅうつう} (currency circulation)
- **Technology/media (3)**: {中継局|ちゅうけいきょく} (relay station), {再生画面|さいせいがめん} (playback screen), {内燃機関|ないねんきかん} (internal combustion engine)
- **Food/drink culture (2)**: {四合瓶|よんごうびん} (720ml sake bottle), {焙煎度|ばいせんど} (coffee roast level)
- **Society/politics (2)**: {癒着関係|ゆちゃくかんけい} (collusive relationship), {標準世帯|ひょうじゅんせたい} (standard household)
- **Publishing (1)**: {商業出版|しょうぎょうしゅっぱん} (commercial publishing)
- **Music (1)**: {演奏技術|えんそうぎじゅつ} (performance technique)
- **Martial arts (1)**: {組み技|くみわざ} (grappling technique)
- **Shopping (1)**: {新品未使用|しんぴんみしよう} (brand new, unused)
- **Entertainment (1)**: {席種|せきしゅ} (seat category)
- **Gardening (1)**: {追い肥|おいごえ} (additional fertilizer)
- **Family (1)**: {長孫|ちょうそん} (eldest grandchild)
- Conjugation tables auto-generated for 2 suru-verb entries
- 1 new kanji added to index: 瘢 (ID 02728)
- 18 candidates synced from candidate list

Total entries: 26,327 → 26,345.

### 2026-05-02 (Vocabulary Expansion - 20 New Entries, Batch 79)
Added 20 new dictionary entries (IDs 26515-26534) from candidate_words.json. Focused on practical vocabulary spanning business, technology, daily life, culture, and language.

- **Business/legal (4)**: {実績主義|じっせきしゅぎ} (meritocracy), {秘密保持|ひみつほじ} (confidentiality), リスク{管理|かんり} (risk management), {危険管理|きけんかんり} (hazard management)
- **Daily life (3)**: {不用品回収|ふようひんかいしゅう} (junk removal), {自宅学習|じたくがくしゅう} (home study), {貸し会議室|かしかいぎしつ} (rental conference room)
- **Language/honorifics (1)**: お{召し上がり|めしあがり} (please help yourself — honorific)
- **Technology (1)**: {薄型化|うすがたか} (making thinner — electronics)
- **Character/personality (3)**: {我勝手|わがかって} (selfishness), {不忠実|ふちゅうじつ} (unfaithful), {正直一途|しょうじきいちず} (earnestly honest)
- **Entertainment/culture (2)**: {完成披露|かんせいひろう} (premiere), {終わりよければすべてよし|おわりよければすべてよし} (all's well that ends well)
- **Crafts/media (1)**: {嵌め込み|はめこみ} (inlay; compositing)
- **Cognition (1)**: {読み過ぎる|よみすぎる} (to overinterpret)
- **Society (2)**: {過密都市|かみつとし} (overcrowded city), {同胞愛|どうほうあい} (brotherly love)
- **Psychology (1)**: {舞台恐怖症|ぶたいきょうふしょう} (stage fright)
- **Agriculture (1)**: {有機肥料|ゆうきひりょう} (organic fertilizer)
- Conjugation tables auto-generated for 1 ichidan verb and 1 suru-verb
- 19 candidates synced; 4 stale duplicate candidates removed

Total entries: 26,307 → 26,327.

### 2026-05-02 (Vocabulary Expansion - 15 New Entries, Batch 78)
Added 15 new dictionary entries (IDs 26500-26514) from candidate_words.json. Mixed vocabulary spanning civil engineering, linguistics, medicine, business, photography, cultural traditions, and daily life.

- **Civil engineering (1)**: {法面|のりめん} (embankment slope)
- **Linguistics (1)**: {廃語|はいご} (obsolete word)
- **Medical/pharmaceutical (2)**: {満量|まんりょう} (full dose), {術前|じゅつぜん} (preoperative)
- **Business/formal (3)**: {返答書|へんとうしょ} (written reply), {如上|じょじょう} (as stated above), {遅答|ちとう} (delayed reply)
- **Photography/optics (1)**: {合焦|ごうしょう} (focusing)
- **Daily life/products (2)**: {浴用|よくよう} (for bathing use), {箱|はこ}ティッシュ (box tissues)
- **Culture/food (2)**: {春|はる}の{七草|ななくさ} (seven spring herbs), {米粉|こめこ}パン (rice flour bread)
- **Games (1)**: {場札|ばふだ} (table card)
- **Language/formal (2)**: {称辞|しょうじ} (words of praise), {荷受人|にうけにん} (consignee)
- Conjugation tables auto-generated for 2 suru-verb entries
- 15 candidates synced from candidate list

Total entries: 26,292 → 26,307.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
