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

### 2026-04-24 (Vocabulary Expansion - 26 New Entries, Batch 32)
Added 26 new dictionary entries (IDs 25220-25245) from candidate_words.json. Focused on common, high-utility vocabulary for intermediate learners.

- **Na-adjectives (5)**: {透明|とうめい} (transparent), {単純|たんじゅん} (simple), {豊富|ほうふ} (abundant), {失礼|しつれい} (rude/excuse me), {世界的|せかいてき} (worldwide)
- **Suru verbs (14)**: {支配|しはい}する (to rule), {加工|かこう}する (to process), {分類|ぶんるい}する (to classify), {節約|せつやく}する (to economize), {登録|とうろく}する (to register), {申請|しんせい}する (to apply), {展開|てんかい}する (to develop), {消費|しょうひ}する (to consume), {発表|はっぴょう}する (to announce), {口出|くちだ}しする (to meddle), {選|よ}り{好|ごの}みする (to be picky), {浪費|ろうひ}する (to waste), {補充|ほじゅう}する (to replenish), {推察|すいさつ}する (to surmise), {接着|せっちゃく}する (to adhere)
- **Godan verb (1)**: {引|ひ}き{立|た}つ (to stand out)
- **I-adjective (1)**: {油|あぶら}っぽい (oily/greasy)
- **Nouns (2)**: {乗|の}り{物酔|ものよ}い (motion sickness), {割|わ}り{込|こ}み (cutting in line)
- **Expressions (2)**: {正々堂々|せいせいどうどう} (fair and square), {粉々|こなごな}になる (to shatter)
- 21 candidates synced from candidate list

Total entries: 25,017 → 25,043.

### 2026-04-23 (Vocabulary Expansion - 24 New Entries, Batch 31)
Added 24 new dictionary entries (IDs 25196-25219) from candidate_words.json. Diverse batch covering onomatopoeia, food culture, traditional vocabulary, nature, and more.

- **Onomatopoeia / mimetic (3)**: ぐにゃぐにゃ (floppy/limp), なでなでする (to gently stroke), ぱたぱたする (to flap)
- **Nature / geography (3)**: {飛瀑|ひばく} (waterfall), {礁|しょう} (reef), {毒茸|どくきのこ} (poisonous mushroom)
- **Culture / tradition (4)**: {三代目|さんだいめ} (third generation), {楽日|らくじつ} (closing day), {命名式|めいめいしき} (naming ceremony), {霊地|れいち} (sacred place)
- **Body / medical (2)**: {咽喉|いんこう} (throat/pharynx), {両耳|りょうみみ} (both ears)
- **Society / law (2)**: {門地|もんち} (family status/pedigree), {共有者|きょうゆうしゃ} (co-owner)
- **Food culture (1)**: {米麹|こめこうじ} (rice koji)
- **Travel (1)**: {温泉旅館|おんせんりょかん} (hot spring inn)
- **Feelings / qualities (2)**: {愛撫|あいぶ} (caress), {大度|たいど} (magnanimity)
- **Language / vocabulary (2)**: {何程|なにほど} (how much/to what extent), {仲春|ちゅうしゅん} (mid-spring)
- **Family / nature (2)**: {初子|ういご} (firstborn child), {天道|てんとう} (way of heaven/the sun)
- **Other (2)**: {雄雌|ゆうし} (male and female), {緒|お} (cord/strap)
- 4 stale candidates removed (overlapping with existing entries)
- 23 candidates synced from candidate list

Total entries: 24,993 → 25,017.

### 2026-04-23 (Vocabulary Expansion - 30 New Entries, Batch 30)
Added 30 new dictionary entries (IDs 25166-25195) from candidate_words.json. Diverse batch covering travel, health, science, education, business, culture, food, and technology.

- **Health / science (4)**: {接触感染|せっしょくかんせん} (contact transmission), {空気感染|くうきかんせん} (airborne transmission), {移植手術|いしょくしゅじゅつ} (transplant surgery), {司法解剖|しほうかいぼう} (forensic autopsy)
- **Science / technology (3)**: {電気抵抗|でんきていこう} (electrical resistance), {永久磁石|えいきゅうじしゃく} (permanent magnet), {天体望遠鏡|てんたいぼうえんきょう} (astronomical telescope)
- **Business / economy (2)**: {市場投入|しじょうとうにゅう} (market launch), {特典券|とくてんけん} (bonus ticket)
- **Material / industry (3)**: {耐水性|たいすいせい} (water resistance), {天然素材|てんねんそざい} (natural material), {粉状|ふんじょう} (powdered form)
- **Education (3)**: {大学教員|だいがくきょういん} (university faculty), {大学生協|だいがくせいきょう} (university co-op), {児童向|じどうむ}け (for children)
- **Travel / daily life (3)**: {泊数|はくすう} (number of nights), {引換所|ひきかえじょ} (exchange counter), {家族向|かぞくむ}け (for families)
- **Entertainment / media (2)**: {新作映画|しんさくえいが} (new film), {内幕話|ないまくばなし} (inside story)
- **Food / culture (2)**: {酒麹|さけこうじ} (sake koji), {麹菌|こうじきん} (koji mold)
- **Technology / industry (2)**: {再始動|さいしどう} (restart), {型式|けいしき} (model type)
- **Other (6)**: {中継点|ちゅうけいてん} (relay point), {体操選手|たいそうせんしゅ} (gymnast), {急傾斜|きゅうけいしゃ} (steep slope), {温暖化対策|おんだんかたいさく} (global warming measures), {王后|おうごう} (queen consort), {異性愛|いせいあい} (heterosexuality)
- 30 candidates synced from candidate list

Total entries: 24,963 → 24,993.

### 2026-04-23 (Vocabulary Expansion - 30 New Entries, Batch 29)
Added 30 new dictionary entries (IDs 25136-25165) from candidate_words.json. Diverse batch covering politics, culture, daily life, food, law, sports, body, and communication.

- **Politics / international (4)**: {票数|ひょうすう} (vote count), {得票数|とくひょうすう} (votes received), {世論戦|よろんせん} (battle for public opinion), {強大国|きょうだいこく} (great power)
- **Culture / religion (3)**: {服喪|ふくもう} (mourning period), {過去帳|かこちょう} (death register), {二十四節気|にじゅうしせっき} (24 solar terms)
- **Daily life / practical (5)**: {管理料|かんりりょう} (management fee), {保冷|ほれい}バッグ (cooler bag), {配達時間|はいたつじかん} (delivery time), {弁当袋|べんとうぶくろ} (lunch bag), {上白糖|じょうはくとう} (refined white sugar)
- **Body / expression (5)**: つま{先立|さきだ}ち (standing on tiptoe), {包帯|ほうたい}を{巻|ま}く (to bandage), {唾|つば}を{吐|は}く (to spit), {脂汗|あぶらあせ}をかく (cold sweat), {間|ま}の{抜|ぬ}けた (foolish, dopey)
- **Sports / activities (2)**: {騎乗|きじょう} (horse riding), ウィンタースポーツ (winter sports)
- **Law / safety (3)**: {自損|じそん} (self-inflicted damage), {冤罪事件|えんざいじけん} (wrongful conviction case), {害虫駆除|がいちゅうくじょ} (pest control)
- **Abstract / academic (3)**: {我慢強|がまんづよ}さ (patience), {主観性|しゅかんせい} (subjectivity), {過剰使用|かじょうしよう} (overuse)
- **Communication (2)**: {説得力|せっとくりょく}がある (to be persuasive), {鼻歌|はなうた}まじり (humming cheerfully)
- **Architecture (2)**: レンガ{造|づく}り (brick construction), {十割|じゅうわり} (100 percent)
- Multi-sense entries: {過去帳|かこちょう} (2 senses), {唾|つば}を{吐|は}く (2 senses)
- 2 stale candidates removed (duplicates of existing entries)
- 29 candidates synced from candidate list

Total entries: 24,933 → 24,963.

### 2026-04-23 (Vocabulary Expansion - 25 New Entries, Batch 28)
Added 25 new dictionary entries (IDs 25111-25135) from candidate_words.json. Mixed batch covering daily life, politics, culture, sports, health, education, economy, and nature.

- **Politics / government (2)**: {連立政権|れんりつせいけん} (coalition government), {擁護者|ようごしゃ} (advocate/defender)
- **Economy / finance (2)**: {大台乗|おおだいの}せ (crossing a major milestone), {緩和策|かんわさく} (mitigation measure)
- **Health / medicine (2)**: {服用量|ふくようりょう} (dosage), {油分|ゆぶん} (oil content)
- **Daily life / transportation (3)**: {通過駅|つうかえき} (non-stop station), {表側|おもてがわ} (front side), {缶飲料|かんいんりょう} (canned drink)
- **Education / science (2)**: {研究科|けんきゅうか} (graduate department), {命名法|めいめいほう} (nomenclature)
- **Culture / mythology (2)**: {織姫|おりひめ} (Orihime/Weaver Princess), {魔法|まほう}の{杖|つえ} (magic wand)
- **Sports / martial arts (2)**: {壁打|かべう}ち (wall practice/brainstorming), {一本勝|いっぽんが}ち (ippon victory)
- **People / society (3)**: {該当者|がいとうしゃ} (eligible person), {低所得者|ていしょとくしゃ} (low-income person), {顔役|かおやく} (influential figure)
- **Nature / materials (2)**: {水族|すいぞく} (aquatic life), {綿布|めんぷ} (cotton cloth)
- **Other (3)**: {躓|つまず}き (stumble/setback), {縦線|たてせん} (vertical line), しおしお (dejectedly/wilted), {初年|しょねん} (first year)
- Multi-sense entries: {躓|つまず}き (2 senses), {壁打|かべう}ち (2 senses), {織姫|おりひめ} (2 senses)
- 1 stale candidate removed (duplicate of existing entry)
- 25 candidates synced from candidate list

Total entries: 24,908 → 24,933.

### 2026-04-22 (Vocabulary Expansion - 29 New Entries, Batch 27)
Added 29 new dictionary entries (IDs 25082-25110) from candidate_words.json. Mixed batch covering daily life, law, food, culture, society, stationery, and more.

- **Law / society (5)**: {不正行為|ふせいこうい} (misconduct), {法的責任|ほうてきせきにん} (legal responsibility), {酒酔|しゅよ}い{運転|うんてん} (drunk driving), {放置駐車|ほうちちゅうしゃ} (abandoned parking), {風紀|ふうき}を{乱|みだ}す (disturb public morals)
- **Daily life / stationery (3)**: {水性|すいせい}ペン (water-based pen), {付箋紙|ふせんし} (sticky note), {紙質|ししつ} (paper quality)
- **Food / cooking (2)**: いんげんまめ (kidney bean), {幼児食|ようじしょく} (toddler food)
- **People / family (4)**: フランス{人|じん} (French person), やんちゃ{坊主|ぼうず} (mischievous boy), いたずらっこ (mischievous child), {身贔屓|みびいき} (favoritism)
- **Industry / work (3)**: {運搬車|うんぱんしゃ} (transport vehicle), {予備部品|よびぶひん} (spare part), {変則勤務|へんそくきんむ} (irregular working hours)
- **Hobbies / nature (3)**: {観賞魚|かんしょうぎょ} (ornamental fish), {観賞植物|かんしょうしょくぶつ} (ornamental plant), {風船|ふうせん}ガム (bubble gum)
- **Culture / religion (1)**: {阿弥陀仏|あみだぶつ} (Amitabha Buddha)
- **Commerce (2)**: {取次店|とりつぎてん} (agency/dealer), コーダー (coder)
- **Appearance (1)**: {地顔|じがお} (natural face)
- **Expression / emotion (3)**: {募|つの}る{思|おも}い (growing feelings), {盗|ぬす}み{撮|ど}り (secret photography), {出来心|できごころ}で (on impulse)
- **Geography (2)**: パリ (Paris), {砂|すな}まみれ (covered in sand)
- Multi-sense entry: いんげんまめ (2 senses)
- 49 candidates synced from candidate list

Total entries: 24,879 → 24,908.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
