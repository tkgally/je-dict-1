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

### 2026-05-02 (Vocabulary Expansion - 25 New Entries, Batch 77)
Added 25 new dictionary entries (IDs 26475-26499) from candidate_words.json. Practical vocabulary spanning business, medical, academic, banking, and daily life domains.

- **Business/commerce (4)**: {料金改定|りょうきんかいてい} (fee revision), {交換品|こうかんひん} (replacement item), {即日発送|そくじつはっそう} (same-day shipping), {仮採用|かりさいよう} (provisional hiring)
- **Banking (2)**: {普通口座|ふつうこうざ} (ordinary savings account), {当座口座|とうざこうざ} (current/checking account)
- **Medical (3)**: {投与量|とうよりょう} (dosage), {体外受精|たいがいじゅせい} (IVF), {分包|ぶんぽう} (individual dose packaging)
- **Academic (3)**: {学位論文|がくいろんぶん} (degree thesis), {指導教官|しどうきょうかん} (academic advisor), {欠席率|けっせきりつ} (absence rate)
- **Science/tech (2)**: {遺伝情報|いでんじょうほう} (genetic information), {記憶装置|きおくそうち} (storage device)
- **Creative/media (2)**: {自主制作|じしゅせいさく} (independent production), {再撮影|さいさつえい} (reshooting)
- **Daily life/general (5)**: {移動中|いどうちゅう} (in transit), {一組|ひとくみ} (one set/pair), {矛盾点|むじゅんてん} (point of contradiction), {事件簿|じけんぼ} (casebook), {指|ゆび}しゃぶり (thumb sucking)
- **Political (1)**: {国家管理|こっかかんり} (state control)
- **Art/design (2)**: {無彩色|むさいしょく} (achromatic color), {最終報告|さいしゅうほうこく} (final report)
- **People (1)**: {促進者|そくしんしゃ} (promoter/facilitator)
- Conjugation tables auto-generated for 2 suru-verb entries
- 25 candidates synced from candidate list

Total entries: 26,267 → 26,292.

### 2026-05-02 (Vocabulary Expansion - 25 New Entries, Batch 76)
Added 25 new dictionary entries (IDs 26450-26474) from candidate_words.json. Diverse batch spanning science, culture, history, technology, daily life, and nature.

- **Science/technology (3)**: {遺伝性|いでんせい} (hereditary nature), {素子|そし} (electronic element/component), {防振|ぼうしん} (vibration damping)
- **Culture/history (5)**: {繭糸|けんし} (silk thread), {膝行|しっこう} (crawling on knees), {羅刹|らせつ} (rakshasa demon), {男色|なんしょく} (male homosexuality), {練功|れんこう} (martial arts training)
- **Nature/agriculture (3)**: {土中|どちゅう} (in the soil), {土石|どせき} (earth and stone), {播種期|はしゅき} (sowing season)
- **Daily life/food (3)**: {早飲|はやの}み (quick drinking), もたれ (stomach heaviness/backrest), {右党|うとう} (teetotaler)
- **Legal/admin (1)**: {正本|せいほん} (original/official copy)
- **Maritime (1)**: {曳航|えいこう} (towing)
- **Sports/body (1)**: {徒手|としゅ} (bare-handed)
- **Weather/culture (1)**: {晴|は}れ{乞|ご}い (praying for clear weather)
- **Relationships (1)**: {仲裂|なかざ}き (estrangement)
- **Regional/cultural (2)**: {郷土性|きょうどせい} (local character), {兄貴肌|あにきはだ} (big-brother type personality)
- **Art (1)**: {多色|たしょく} (multiple colors)
- **Architecture (1)**: {防塀|ぼうへい} (protective wall)
- **Thermal science (1)**: {冷熱|れいねつ} (cold and heat)
- **History/survival (1)**: {遺存|いそん} (surviving remains)
- Conjugation tables auto-generated for 4 suru-verb entries
- 25 candidates synced from candidate list; 1 new kanji (曳) added to kanji index

Total entries: 26,242 → 26,267.

### 2026-05-01 (Vocabulary Expansion - 20 New Entries, Batch 74)
Added 20 new dictionary entries (IDs 26430-26449) from candidate_words.json. Diverse batch covering transport, business, technology, daily life, and more.

- **Transport (2)**: {降車口|こうしゃぐち} (exit door on vehicles), {軽車両|けいしゃりょう} (light vehicle/bicycle category)
- **Business/industry (3)**: {個人客|こじんきゃく} (individual customer), {半製品|はんせいひん} (semi-finished product), {純正部品|じゅんせいぶひん} (genuine OEM parts)
- **Technology/audio (3)**: {計測器|けいそくき} (measuring instrument), {受信|じゅしん}メール (received email), {雑音除去|ざつおんじょきょ} (noise cancellation)
- **Daily life (4)**: {海外在住|かいがいざいじゅう} (living abroad), {卓上鏡|たくじょうきょう} (tabletop mirror), カーボン{紙|し} (carbon paper), {人数分|にんずうぶん} (enough for the group)
- **Geography/science (2)**: {海水面|かいすいめん} (sea level), {先史時代|せんしじだい} (prehistoric era)
- **Communication/work (2)**: {連絡板|れんらくばん} (message board), {資格証明|しかくしょうめい} (proof of qualification)
- **Education/family (1)**: {幼児向|ようじむ}け (for young children)
- **Policy/strategy (1)**: {路線変更|ろせんへんこう} (route change/policy shift)
- **Expression (1)**: {生身|なまみ}の{人間|にんげん} (flesh-and-blood human being)
- **Safety (1)**: {衝撃吸収|しょうげききゅうしゅう} (shock absorption)
- Conjugation tables auto-generated for 2 suru-verb entries
- 20 candidates synced from candidate list

Total entries: 26,222 → 26,242.

### 2026-05-01 (Vocabulary Expansion - 20 New Entries, Batch 73)
Added 20 new dictionary entries (IDs 26410-26429) from candidate_words.json. Diverse batch spanning life stages, transport, sports, linguistics, arts, science, business, and more.

- **Life stages/society (2)**: {壮年期|そうねんき} (middle age/prime of life), {隠居人|いんきょにん} (retired person/recluse)
- **Transport (3)**: {牽引車|けんいんしゃ} (tow truck/tractor), {定期運行|ていきうんこう} (regular service), {副機長|ふくきちょう} (copilot)
- **Sports (1)**: {交代選手|こうたいせんしゅ} (substitute player)
- **Linguistics (3)**: {有声音|ゆうせいおん} (voiced sound), {無声音|むせいおん} (voiceless sound), {五七調|ごしっちょう} (five-seven meter)
- **Arts/music (1)**: {指揮台|しきだい} (conductor's podium)
- **Science/chemistry (1)**: {塩化物|えんかぶつ} (chloride)
- **Urban/environment (1)**: {都市景観|としけいかん} (urban landscape/cityscape)
- **History/politics (1)**: {植民地主義|しょくみんちしゅぎ} (colonialism)
- **Business (1)**: {社内秘|しゃないひ} (confidential/internal use only)
- **Publishing (1)**: {編纂者|へんさんしゃ} (compiler/editor of reference works)
- **Medicine (1)**: {前立腺|ぜんりつせん} (prostate gland)
- **Material (1)**: {磁器製|じきせい} (made of porcelain)
- **Measurement (1)**: {中間点|ちゅうかんてん} (midpoint/halfway point)
- **Nature (1)**: {造園士|ぞうえんし} (landscape gardener)
- **Forensics (1)**: {掌紋|しょうもん} (palm print)
- 20 candidates synced from candidate list

Total entries: 26,202 → 26,222.

### 2026-05-01 (Vocabulary Expansion - 12 New Entries, Batch 72)
Added 12 new dictionary entries (IDs 26398-26409) from candidate_words.json. Focus on practical vocabulary covering media, daily life, business, politics, and industry.

- **Media/entertainment (2)**: {連続|れんぞく}ドラマ (serial drama/TV series), {原作家|げんさくか} (original author)
- **Leisure (1)**: {絶叫|ぜっきょう}マシン (thrill ride)
- **Daily life/food (2)**: {白砂糖|しろざとう} (white sugar), {調乳|ちょうにゅう} (preparing formula)
- **Business/real estate (2)**: {立地|りっち}{条件|じょうけん} (location conditions), {利害|りがい}{調整|ちょうせい} (coordination of interests)
- **Politics (1)**: {国務大臣|こくむだいじん} (minister of state)
- **Education (1)**: {出題者|しゅつだいしゃ} (question setter)
- **Industry/technology (2)**: {電子|でんし}{部品|ぶひん} (electronic components), {水産|すいさん}{加工|かこう} (seafood processing)
- **Insurance (1)**: {自動車|じどうしゃ}{保険|ほけん} (car insurance)
- Conjugation table auto-generated for 1 suru-verb entry (調乳する)
- 12 candidates synced from candidate list; 1 stale duplicate removed

Total entries: 26,190 → 26,202.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
