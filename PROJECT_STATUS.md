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

### 2026-04-22 (Vocabulary Expansion - 20 New Entries, Batch 26)
Added 20 new dictionary entries (IDs 25062-25081) from candidate_words.json. Mixed batch covering daily life, culture, travel, food, nature, fashion, sport, and history.

- **Daily life / facilities (4)**: パウダールーム (powder room), {相談室|そうだんしつ} (consultation room), レンタルルーム (rental room), フェイスタオル (face towel)
- **Culture / religion (3)**: {大凶|だいきょう} (great misfortune / omikuji), {剃髪|ていはつ} (head shaving / tonsure), {儒者|じゅしゃ} (Confucian scholar)
- **Travel / transport (2)**: {渡航先|とこうさき} (destination abroad), パーキングエリア (parking area)
- **Food / nature (3)**: カシューナッツ (cashew nut), {片栗|かたくり} (dogtooth violet / starch), {羽虫|はむし} (gnat / small flying insect)
- **Sport / leisure (2)**: セーリング (sailing), クルーザー (cruiser / yacht)
- **Fashion (1)**: バングル (bangle)
- **People / society (3)**: {女主人|おんなしゅじん} (female proprietor), {長子|ちょうし} (eldest child), {素|そ}っ{気|け} (bluntness / coldness)
- **Expression (1)**: {昼日中|ひるひなか} (broad daylight)
- **Tools (1)**: {噴霧器|ふんむき} (sprayer / atomizer)
- Multi-sense entry: {片栗|かたくり} (2 senses)
- Conjugation table auto-generated for 1 suru verb entry ({剃髪|ていはつ})
- 20 candidates synced from candidate list

Total entries: 24,859 → 24,879.

### 2026-04-22 (Vocabulary Expansion - 25 New Entries, Batch 25)
Added 25 new dictionary entries (IDs 25037-25061) from candidate_words.json. Mixed batch covering daily life, culture, history, business, science, economics, and expressions.

- **Daily life (3)**: キッチンペーパー (kitchen paper towel), {必携品|ひっけいひん} (essential item), {美顔|びがん} (facial beauty/care)
- **Business / work (3)**: {進行役|しんこうやく} (facilitator/moderator), {繁盛期|はんじょうき} (peak season), サービス{出勤|しゅっきん} (unpaid work attendance)
- **Culture / history (3)**: {百獣|ひゃくじゅう} (all beasts), {廓|くるわ} (pleasure quarter/castle bailey), {一寸|いっすん} (one sun measurement)
- **Science / technology (3)**: {周波数|しゅうはすう} (frequency), {無生物|むせいぶつ} (inanimate object), {再設定|さいせってい} (resetting)
- **Economics / general (3)**: インフレーション (inflation), その{他|た} (others/the rest), {介在|かいざい} (mediation/intervention)
- **Expressions / literary (2)**: {胸|むね}がきゅんとする (heart flutter), よすが (means of support/keepsake)
- **Education (1)**: {女子学生|じょしがくせい} (female student)
- **Transport (1)**: {乗合|のりあい}バス (public bus)
- **Agriculture (1)**: {輪作|りんさく} (crop rotation)
- **Religion (1)**: イスラム{教|きょう} (Islam)
- **Military (1)**: {手榴弾|しゅりゅうだん} (hand grenade)
- **Multi-sense entries (3)**: {上|あ}がり (3 senses), {廓|くるわ} (2 senses), {絵札|えふだ} (2 senses), よすが (2 senses)
- Conjugation tables auto-generated for 5 suru verb entries
- 2 new kanji added to index: 廓, 榴
- 25 candidates synced from candidate list

Total entries: 24,834 → 24,859.

### 2026-04-22 (Vocabulary Expansion - 20 New Entries, Batch 24)
Added 20 new dictionary entries (IDs 25017-25036) from candidate_words.json. Mixed batch covering expressions, loanwords, food, sports, daily life, science, and business vocabulary.

- **Expressions (3)**: どちらかというと (if anything/rather), {影響|えいきょう}を{受|う}ける (to be influenced), {再々|さいさい} (again and again)
- **Loanwords / daily life (4)**: エントリーシート (job application form), チェックリスト (checklist), コンディショナー (hair conditioner), ウェットティッシュ (wet wipe)
- **Food / dining (2)**: {計量|けいりょう}カップ (measuring cup), {刺身盛|さしみも}り (sashimi platter)
- **Onomatopoeia (1)**: ぽこぽこ (bubbling; one after another)
- **Sports (1)**: {内野手|ないやしゅ} (infielder)
- **Science / technology (2)**: {化合物|かごうぶつ} (chemical compound), データ{解析|かいせき} (data analysis)
- **Business / administration (3)**: {名称変更|めいしょうへんこう} (name change), {募集期間|ぼしゅうきかん} (application period), {予約受付|よやくうけつけ} (reservation reception)
- **Shopping (1)**: {購入予約|こうにゅうよやく} (pre-order)
- **Transport / education (2)**: {進路変更|しんろへんこう} (change of course), {車線規制|しゃせんきせい} (lane restriction)
- **Exploration (1)**: {探検隊|たんけんたい} (expedition)
- Conjugation tables auto-generated for 4 suru verb entries
- 3 stale candidates removed (duplicates of existing entries)
- 20 candidates synced from candidate list

Total entries: 24,814 → 24,834.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
