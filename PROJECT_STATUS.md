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

### 2026-05-01 (Vocabulary Expansion - 20 New Entries, Batch 69)
Added 20 new dictionary entries (IDs 26341-26360) from candidate_words.json. Batch covering nature, food, culture, daily life, recreation, agriculture, and color vocabulary.

- **Nature/animals (2)**: {鮒|ふな} (crucian carp), {川鵜|かわう} (great cormorant)
- **Food/culture (3)**: ソース{焼|や}きそば (sauce yakisoba), {抹茶碗|まっちゃわん} (matcha bowl), {一飲|いちの}み (one gulp)
- **Colors (2)**: {麦色|むぎいろ} (wheat color/golden brown), {黒茶|くろちゃ} (dark brown)
- **Agriculture (2)**: {元肥|もとごえ} (base fertilizer), {液肥|えきひ} (liquid fertilizer)
- **Recreation/sports (2)**: ローラースケート (roller skating), スケート{靴|ぐつ} (ice skates)
- **Daily life (3)**: パーキングメーター (parking meter), {横見|よこみ} (sideways glance), {無帽|むぼう} (bareheaded)
- **Education/evaluation (1)**: {百点|ひゃくてん} (perfect score)
- **Business/finance (1)**: {月割|つきわ}り (monthly installment)
- **Strategy (1)**: {必中|ひっちゅう} (sure hit)
- **Society (1)**: {遅進|ちしん} (backwardness/slow progress)
- **Traditional arts (1)**: まり (ball/temari)
- 1 new kanji added (鮒)
- 20 candidates synced from candidate list

Total entries: 26,133 → 26,153.

### 2026-04-30 (Vocabulary Expansion - 28 New Entries, Batch 68)
Added 28 new dictionary entries (IDs 26313-26340) from candidate_words.json. Varied batch covering arts, health, science, daily life, culture, and more.

- **Arts/culture (4)**: {改作|かいさく} (adaptation/rewriting), {阿修羅|あしゅら} (Asura/scene of carnage), ボーイズラブ (BL/boys' love genre), はかなくなる (to pass away, euphemism)
- **Health/body (7)**: {排尿|はいにょう} (urination), {排便|はいべん} (defecation), {低体温|ていたいおん} (hypothermia), {乳腺|にゅうせん} (mammary gland), {洗浴|せんよく} (bathing), {手肌|てはだ} (hand skin), {真菌|しんきん} (fungus)
- **Science/technology (4)**: {核酸|かくさん} (nucleic acid), {酢酸|さくさん} (acetic acid), {解像|かいぞう} (image resolution), {線分|せんぶん} (line segment)
- **Society/business (3)**: {転籍|てんせき} (change of domicile/company transfer), {娼婦|しょうふ} (prostitute), {従量制|じゅうりょうせい} (usage-based pricing)
- **Daily life/food (3)**: {粉茶|こなちゃ} (powdered tea), {片耳|かたみみ} (one ear), {休室|きゅうしつ} (room closure)
- **Language/grammar (3)**: {付|つ}き (with/per), どっちか (either one), {耽溺|たんでき} (indulgence/addiction)
- **Nature (1)**: {幼鳥|ようちょう} (young bird)
- **Expressions (2)**: {取|と}り{憑|つ}かれる (to be possessed/obsessed), {細|こま}かいことを{言|い}う (to nitpick)
- 1 new kanji added (娼)
- Conjugation tables auto-generated for 8 verb entries
- 28 candidates synced from candidate list

Total entries: 26,105 → 26,133.

### 2026-04-30 (Vocabulary Expansion - 30 New Entries, Batch 67)
Added 30 new dictionary entries (IDs 26283-26312) from candidate_words.json. Diverse batch covering daily life, science, business, culture, history, health, and more.

- **Colors/body (2)**: {肌色|はだいろ} (skin color/flesh color), {毛根|もうこん} (hair root)
- **Daily objects (2)**: {長傘|なががさ} (long umbrella), {密閉容器|みっぺいようき} (airtight container)
- **Seasonal/calendar (3)**: {立秋|りっしゅう} (start of autumn), {立冬|りっとう} (start of winter), {凝固点|ぎょうこてん} (freezing point)
- **Business/work (4)**: {変動費|へんどうひ} (variable costs), {未経験者|みけいけんしゃ} (inexperienced person), {現状報告|げんじょうほうこく} (status report), {個人事業主|こじんじぎょうぬし} (sole proprietor)
- **Science/technical (4)**: {融解点|ゆうかいてん} (melting point), {定量分析|ていりょうぶんせき} (quantitative analysis), {鋳鉄|ちゅうてつ} (cast iron), {潤滑剤|じゅんかつざい} (lubricant)
- **Geography/nature (2)**: {水系|すいけい} (water system), {分流|ぶんりゅう} (branching stream)
- **People/roles (3)**: {撮影者|さつえいしゃ} (photographer), {当選者|とうせんしゃ} (winner/elected person), {原始人|げんしじん} (primitive man)
- **Culture/writing (2)**: {乱筆|らんぴつ} (poor handwriting), {不忠|ふちゅう} (disloyalty)
- **Architecture (1)**: {建築設計|けんちくせっけい} (architectural design)
- **Security (1)**: {監視塔|かんしとう} (watchtower)
- **General (2)**: {連続性|れんぞくせい} (continuity), {時限爆弾|じげんばくだん} (time bomb)
- **Abstract (1)**: {無拘束|むこうそく} (unrestrained)
- **Medical (2)**: {脱毛症|だつもうしょう} (alopecia), {外皮|がいひ} (outer skin)
- Conjugation tables auto-generated for 3 suru-verb entries
- 29 candidates synced from candidate list

Total entries: 26,075 → 26,105.

### 2026-04-30 (Vocabulary Expansion - 24 New Entries, Batch 66)
Added 24 new dictionary entries (IDs 26236-26259) from candidate_words.json. Diverse batch covering employment, patterns/textiles, business, geography, culture, food, science, politics, and more.

- **Employment/social (2)**: {非正規|ひせいき} (non-regular employment), {媒酌人|ばいしゃくにん} (matchmaker/go-between)
- **Patterns/textiles (3)**: {縞模様|しまもよう} (striped pattern), {花柄|はながら} (floral pattern), {革製|かわせい} (leather-made)
- **Business/admin (4)**: {見|み}える{化|か} (visualization), {保留中|ほりゅうちゅう} (on hold/pending), {懸案事項|けんあんじこう} (pending matter), {登録者|とうろくしゃ} (subscriber)
- **Geography/nature (1)**: {湖岸|こがん} (lakeshore)
- **Science/facilities (2)**: {観測所|かんそくじょ} (observatory), {接種率|せっしゅりつ} (vaccination rate)
- **Politics/history (2)**: {中央集権|ちゅうおうしゅうけん} (centralization of power), {行政区|ぎょうせいく} (administrative district)
- **Religion/culture (2)**: {使徒|しと} (apostle/disciple), {俗世間|ぞくせけん} (secular world)
- **Medical/body (2)**: {拍動|はくどう} (pulsation), {律動|りつどう} (rhythm)
- **Tourism (1)**: {誘客|ゆうきゃく} (attracting visitors)
- **Mental health (1)**: {精神病|せいしんびょう} (mental illness)
- **Food (2)**: {揚|あ}げかまぼこ (deep-fried fish cake), {粉乳|ふんにゅう} (powdered milk)
- **Transportation (1)**: {通行可|つうこうか} (passable/open to traffic)
- **Descriptive (1)**: おどろおどろしい (eerie/ghastly)
- Conjugation tables auto-generated for 4 suru-verb and 1 i-adjective entries
- 24 candidates synced from candidate list

Total entries: 26,028 → 26,052.

### 2026-04-30 (Vocabulary Expansion - 20 New Entries, Batch 65)
Added 20 new dictionary entries (IDs 26216-26235) from candidate_words.json. Mixed batch covering language, sports, culture, geography, food, nature, and practical daily life.

- **Language/grammar (1)**: {分|ぶん} (portion; share; extent)
- **Geography (2)**: {低所|ていしょ} (low place), {異郷|いきょう} (foreign land)
- **Photography/media (2)**: {写|うつ}り{映|ば}え (photogenic quality), {素材感|そざいかん} (texture; material feel)
- **Sports (2)**: シュートする (to shoot), {体格差|たいかくさ} (size gap)
- **Rankings/numbers (1)**: {三位|さんい} (third place)
- **Communication (1)**: {空話|からばなし} (idle talk; tall tale)
- **Daily life (3)**: {月|つき}めくり (monthly calendar), {駐車場代|ちゅうしゃじょうだい} (parking fee), {現地解散|げんちかいさん} (disbanding at venue)
- **Business (3)**: {地元企業|じもときぎょう} (local company), {調整役|ちょうせいやく} (coordinator), {最有力|さいゆうりょく} (frontrunner)
- **Food/commerce (2)**: {砂糖菓子|さとうがし} (sugar confection), {生産地|せいさんち} (production area)
- **Ability (1)**: {総合力|そうごうりょく} (overall ability)
- **Nature (1)**: {蜻蛉|かげろう} (mayfly)
- **Games (1)**: {盤上|ばんじょう} (on the board)
- Conjugation tables auto-generated for 2 suru-verb entries
- 20 candidates synced from candidate list

Total entries: 26,008 → 26,028.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
