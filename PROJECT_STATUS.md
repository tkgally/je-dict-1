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

### 2026-04-21 (Vocabulary Expansion - 22 New Entries, Batch 18)
Added 22 new dictionary entries (IDs 24872-24893) from candidate_words.json. Mixed batch covering social/cultural concepts, education, politics, infrastructure, health, sports, and practical vocabulary.

- **Social / cultural (3)**: {嫌|きら}われる (to be disliked), {報|むく}われない (unrewarded), {通過儀礼|つうかぎれい} (rite of passage)
- **Education / research (4)**: {黒板消|こくばんけ}し (blackboard eraser), {試験監督|しけんかんとく} (exam proctor), {採点者|さいてんしゃ} (grader), {聞|き}き{取|と}り{調査|ちょうさ} (interview survey)
- **Politics / government (3)**: {超大国|ちょうたいこく} (superpower), {出入国|しゅつにゅうこく} (immigration/emigration), {禁止解除|きんしかいじょ} (lifting a ban)
- **Math / business (2)**: {概数|がいすう} (approximate number), {加算|かさん} (addition/surcharge)
- **Infrastructure / tech (3)**: {配電盤|はいでんばん} (electrical panel), {送風機|そうふうき} (blower), {焼却場|しょうきゃくじょう} (incineration plant)
- **Transport / urban (2)**: {停留|ていりゅう} (stopping), {通過点|つうかてん} (waypoint/milestone)
- **Nature / health / sports (3)**: {植栽|しょくさい} (planting/landscaping), {扁平足|へんぺいそく} (flat feet), {陸上選手|りくじょうせんしゅ} (track athlete)
- **Other (2)**: {助言者|じょげんしゃ} (advisor), {音楽隊|おんがくたい} (band/music corps)
- Conjugation tables auto-generated for 6 suru verbs and 1 ichidan verb, 1 i-adjective
- 1 new kanji added to index: 扁
- 22 candidates removed from candidate list

Total entries: 24,669 → 24,691.

### 2026-04-21 (Vocabulary Expansion - 28 New Entries, Batch 17)
Added 28 new dictionary entries (IDs 24844-24871) from candidate_words.json. Diverse batch covering expressions, business, culture, language, geography, and general vocabulary.

- **Expressions / idioms (4)**: {人|ひと}それぞれ (to each their own), {言葉|ことば}を{濁|にご}す (to equivocate), {八面六臂|はちめんろっぴ} (outstanding versatility), {気散|きさん}じ (diversion)
- **Business / finance (4)**: {個人事業|こじんじぎょう} (sole proprietorship), {顧客満足|こきゃくまんぞく} (customer satisfaction), {財務諸表|ざいむしょひょう} (financial statements), {省電力|しょうでんりょく} (power saving)
- **Culture / religion (3)**: ご{芳名|ほうめい} (your honored name), {頓首|とんしゅ} (respectfully yours), {経|きょう} (Buddhist sutra)
- **Language / linguistics (2)**: {口語体|こうごたい} (colloquial style), {未発表|みはっぴょう} (unpublished)
- **Geography / science (3)**: {震央|しんおう} (epicenter), {地底|ちてい} (underground depths), {郡部|ぐんぶ} (rural area)
- **People / society (3)**: {無職者|むしょくしゃ} (unemployed person), {見舞客|みまいきゃく} (hospital visitor), {創作者|そうさくしゃ} (creator)
- **Other (9)**: {牽引力|けんいんりょく} (traction), {対話力|たいわりょく} (dialogue skills), {下腹|したばら} (lower abdomen), {豪華版|ごうかばん} (deluxe edition), {普及版|ふきゅうばん} (popular edition), {局限|きょくげん} (restriction), {濃緑|のうりょく} (dark green), {惜敗感|せきはいかん} (feeling of near-miss), ヒル (leech)
- Conjugation table auto-generated for 1 suru verb entry ({局限|きょくげん})
- 1 new kanji added to index: 臂
- Removed 5 stale candidates (duplicates/variants of existing entries)

Total entries: 24,641 → 24,669.

### 2026-04-21 (Vocabulary Expansion - 28 New Entries, Batch 16)
Added 28 new dictionary entries (IDs 24816-24843) from candidate_words.json. Diverse batch covering culture, health, science, food, sports, economics, and daily life.

- **Culture / traditions (4)**: {好色|こうしょく} (lustful/amorous), {酒器|しゅき} (sake vessel), お{七夜|しちや} (baby naming ceremony), {百日|ももか}{祝|いわ}い (100-day celebration)
- **Health / medical (4)**: {失禁|しっきん} (incontinence), {聴覚|ちょうかく}{障害|しょうがい} (hearing impairment), {終末|しゅうまつ}{医療|いりょう} (end-of-life care), {交感|こうかん}{神経|しんけい} (sympathetic nerve)
- **Science / environment (3)**: {自然|しぜん}{科学|かがく} (natural science), {温室|おんしつ}{効果|こうか}ガス (greenhouse gas), {無人機|むじんき} (drone)
- **Business / economics (3)**: {上方|じょうほう}{修正|しゅうせい} (upward revision), {私有化|しゆうか} (privatization), {清涼|せいりょう}{飲料|いんりょう} (soft drink)
- **Education (2)**: {遠隔|えんかく}{教育|きょういく} (distance education), {学部長|がくぶちょう} (dean)
- **Food / drink (3)**: さやいんげん (green bean), ソーダ{水|すい} (soda water), {和|わ}{布団|ぶとん} (Japanese futon)
- **Sports / entertainment (3)**: {猛練習|もうれんしゅう} (intensive practice), {金属|きんぞく}バット (metal bat), {助演|じょえん}{女優|じょゆう} (supporting actress)
- **History / other (4)**: {打|う}ち{壊|こわ}し (Edo-period riot), {引|ひ}きずり{出|だ}す (to drag out), {将棋盤|しょうぎばん} (shogi board), {化粧|けしょう}{鏡|きょう} (vanity mirror), {印刷機|いんさつき} (printing press)
- Removed 1 stale candidate (望遠レンズ, duplicate of entry 24644)
- Conjugation tables auto-generated for 8 verb entries

Total entries: 24,613 -> 24,641.

### 2026-04-20 (Vocabulary Expansion - 30 New Entries, Batch 15)
Added 30 new dictionary entries (IDs 24786-24815) from candidate_words.json. Diverse batch covering military, history, culture, science, language, sports, daily life, and modern society.

- **Military / security (3)**: {匍匐|ほふく} (crawling), {着弾|ちゃくだん} (projectile impact), {化学|かがく}{兵器|へいき} (chemical weapon)
- **History / culture (5)**: {後宮|こうきゅう} (inner palace), {武家屋敷|ぶけやしき} (samurai residence), {文化勲章|ぶんかくんしょう} (Order of Culture), {進上|しんじょう} (formal gift-giving), {貴公|きこう} (archaic "you")
- **Science / education (3)**: {化学式|かがくしき} (chemical formula), {仮定形|かていけい} (hypothetical form), {化学|かがく}{薬品|やくひん} (chemicals)
- **Sports / entertainment (3)**: {白星|しろぼし}を{挙|あ}げる (score a win), {通|とお}し{稽古|げいこ} (full rehearsal), {着|き}せ{替|か}え{人形|にんぎょう} (dress-up doll)
- **Modern society (3)**: {転売|てんばい}{禁止|きんし} (resale prohibition), {命名権|めいめいけん} (naming rights), {入場|にゅうじょう}{禁止|きんし} (no admittance)
- **Health / daily life (4)**: {体脂肪率|たいしぼうりつ} (body fat percentage), {生理用品|せいりようひん} (sanitary products), {入院|にゅういん}{患者|かんじゃ} (inpatient), {滞在|たいざい}{日数|にっすう} (length of stay)
- **Language / register (2)**: てめえ (vulgar "you"), {返|かえ}し (comeback/sauce)
- **Other (7)**: ホワイトアウト (whiteout), {地場|じば}{産業|さんぎょう} (local industry), {追悼式|ついとうしき} (memorial service), {粒度|りゅうど} (granularity), {跳|は}ね{返|かえ}し (rebound), {素性|すじょう}が{知|し}れる (background revealed), {筋骨|きんこつ}たくましい (muscular)

Total entries: 24,583 → 24,613.

### 2026-04-20 (Vocabulary Expansion - 17 New Entries, Batch 14)
Added 17 new dictionary entries (IDs 24769-24785) from candidate_words.json. Diverse batch covering business/finance, culture, food, nature, geography, and daily life.

- **Business / finance (4)**: {売|う}り{手|て} (seller), {買|か}い{手|て} (buyer), {証券会社|しょうけんがいしゃ} (securities company), {信用金庫|しんようきんこ} (credit union)
- **Culture / history (4)**: {宿場町|しゅくばまち} (post town), {護符|ごふ} (protective talisman), {呪術|じゅじゅつ} (sorcery), {日帰|ひがえ}り{温泉|おんせん} (day-trip hot spring)
- **Food (1)**: {味噌漬|みそづ}け (miso pickles)
- **Nature (1)**: {雛鳥|ひなどり} (baby bird)
- **Formal / meetings (2)**: {散会|さんかい} (adjournment), {政令|せいれい} (cabinet order)
- **Other (5)**: {最終日|さいしゅうび} (final day), {浄水器|じょうすいき} (water purifier), {弟分|おとうとぶん} (younger-brother figure), {中間色|ちゅうかんしょく} (intermediate color), {放射状|ほうしゃじょう} (radial pattern)
- Conjugation table auto-generated for 1 suru verb entry (散会)
- Removed 1 stale candidate (他人事/たにんごと, covered by existing entry 09570)

Total entries: 24,566 → 24,583.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
