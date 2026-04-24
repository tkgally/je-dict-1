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

### 2026-04-24 (Vocabulary Expansion - 30 New Entries, Batch 35)
Added 30 new dictionary entries (IDs 25301-25330) from candidate_words.json. Focused on useful two-kanji compounds and common vocabulary across science, politics, food, culture, and daily life.

- **Nouns (18)**: {重力|じゅうりょく} (gravity), {自伝|じでん} (autobiography), {範疇|はんちゅう} (category), {内情|ないじょう} (inside story), {室温|しつおん} (room temperature), {純愛|じゅんあい} (pure love), {氷河|ひょうが} (glacier), {苦難|くなん} (hardship), {炭火|すみび} (charcoal fire), {酢豚|すぶた} (sweet and sour pork), {錠前|じょうまえ} (lock), {翌週|よくしゅう} (following week), {長屋|ながや} (row house)
- **Suru verbs (8)**: {従属|じゅうぞく}する (to be subordinate), {倒壊|とうかい}する (to collapse), {退陣|たいじん}する (to step down), {討議|とうぎ}する (to discuss), {湾曲|わんきょく}する (to curve), {発育|はついく}する (to grow), {始業|しぎょう}する (to start work), {出頭|しゅっとう}する (to turn oneself in)
- **Adverb (1)**: {俄然|がぜん} (suddenly/dramatically)
- **Na-adjectives (2)**: {変則|へんそく} (irregular), {早熟|そうじゅく} (precocious)
- **Other (1)**: {食用|しょくよう} (edible), {儀礼|ぎれい} (ceremony/etiquette), {沸点|ふってん} (boiling point), {思慮|しりょ} (prudence), {平常|へいじょう} (normal), {造語|ぞうご} (coined word)
- 1 new kanji added: 疇
- 30 candidates synced from candidate list

Total entries: 25,093 → 25,123.

### 2026-04-24 (Vocabulary Expansion - 30 New Entries, Batch 34)
Added 30 new dictionary entries (IDs 25271-25300) from candidate_words.json. Diverse batch covering culture, daily life, science, work, food, and more.

- **Nouns (18)**: かぶれ (skin rash), {挑戦者|ちょうせんしゃ} (challenger), {引力|いんりょく} (gravity), {大空|おおぞら} (vast sky), {重病|じゅうびょう} (serious illness), バレンタインデー (Valentine's Day), ホワイトデー (White Day), {製鉄所|せいてつじょ} (steel mill), {芸名|げいめい} (stage name), {床暖房|ゆかだんぼう} (floor heating), {夏疲|なつづか}れ (summer fatigue), サービス{業|ぎょう} (service industry), {透明度|とうめいど} (transparency), {返却期限|へんきゃくきげん} (return deadline), {図画工作|ずがこうさく} (arts and crafts), {市場経済|しじょうけいざい} (market economy), {有用性|ゆうようせい} (usefulness), {鶏卵|けいらん} (chicken egg)
- **Suru verbs (5)**: {攻略|こうりゃく}する (to capture/to clear a game), {慰労|いろう}する (to appreciate effort), {奪取|だっしゅ}する (to seize), {内職|ないしょく}する (to do side jobs), {配備|はいび}する (to deploy)
- **Other (7)**: くすくす{笑|わら}う (to giggle), {横入|よこい}り (cutting in line), {未処理|みしょり} (unprocessed), {休暇明|きゅうかあ}け (post-vacation), もも{肉|にく} (thigh meat), {顧客対応|こきゃくたいおう} (customer service), {鳥|とり}のさえずり (birdsong)
- 30 candidates synced from candidate list

Total entries: 25,063 → 25,093.

### 2026-04-24 (Vocabulary Expansion - 25 New Entries, Batch 33)
Added 25 new dictionary entries (IDs 25246-25270) from candidate_words.json. Focused on expressive verbs, useful nouns, and common expressions. 25 stale candidates removed as duplicates of existing base-form entries.

- **Ichidan verbs (3)**: {膨|ふく}れる (to swell/pout), {悔|く}いる (to regret), {弾|はじ}ける (to burst/pop)
- **Godan verbs (9)**: はしゃぐ (to frolic), {口|くち}ごもる (to mumble), {貢|みつ}ぐ (to lavish gifts on), {出|で}っ{張|ぱ}る (to protrude), {謎|なぞ}めく (to be mysterious), {見|み}くびる (to underestimate), {怖気|おじけ}づく (to get cold feet), {見放|みはな}す (to abandon), {忌|い}み{嫌|きら}う (to detest)
- **Compound verb (1)**: {汲|く}み{取|と}る (to scoop up/to grasp feelings)
- **I-adjective (1)**: {堅苦|かたくる}しい (stiff/overly formal)
- **Nouns (8)**: {粉飾|ふんしょく} (embellishment), {逆行|ぎゃっこう} (retrogression), {恩情|おんじょう} (benevolence), {運転免許証|うんてんめんきょしょう} (driver's license), {教育者|きょういくしゃ} (educator), {経験値|けいけんち} (experience points), {事務員|じむいん} (office clerk), {初年度|しょねんど} (first year)
- **Other (3)**: この{前|まえ} (the other day), パートタイム (part-time), {段違|だんちが}い (a world apart)
- 25 stale candidates removed, 25 candidates synced from candidate list

Total entries: 25,038 → 25,063.

### 2026-04-24 (Vocabulary Expansion - 21 New Entries, Batch 32)
Added 21 new dictionary entries (IDs 25222-25245) from candidate_words.json. Focused on common, high-utility vocabulary for intermediate learners. 5 candidates removed as duplicates of existing entries.

- **Suru verbs (14)**: {支配|しはい}する (to rule), {加工|かこう}する (to process), {分類|ぶんるい}する (to classify), {節約|せつやく}する (to economize), {登録|とうろく}する (to register), {申請|しんせい}する (to apply), {展開|てんかい}する (to develop), {消費|しょうひ}する (to consume), {発表|はっぴょう}する (to announce), {口出|くちだ}しする (to meddle), {選|よ}り{好|ごの}みする (to be picky), {浪費|ろうひ}する (to waste), {補充|ほじゅう}する (to replenish), {推察|すいさつ}する (to surmise), {接着|せっちゃく}する (to adhere)
- **Godan verb (1)**: {引|ひ}き{立|た}つ (to stand out)
- **I-adjective (1)**: {油|あぶら}っぽい (oily/greasy)
- **Nouns (2)**: {乗|の}り{物酔|ものよ}い (motion sickness), {割|わ}り{込|こ}み (cutting in line)
- **Expressions (2)**: {正々堂々|せいせいどうどう} (fair and square), {粉々|こなごな}になる (to shatter)
- 21 candidates synced from candidate list

Total entries: 25,017 → 25,038.

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

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
