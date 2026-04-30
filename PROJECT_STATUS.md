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

### 2026-04-30 (Vocabulary Expansion - 30 New Entries, Batch 64)
Added 30 new dictionary entries (IDs 26186-26215) from candidate_words.json. Diverse batch covering history, business, geography, science, food, art, architecture, medicine, nature, education, entertainment, and technology.

- **History/culture (3)**: {藩主|はんしゅ} (feudal domain lord), {蛮族|ばんぞく} (barbarian tribe), {公女|こうじょ} (princess/noblewoman)
- **Business/keigo (4)**: {資金源|しきんげん} (funding source), {先方様|せんぽうさま} (the other party - honorific), {専売店|せんばいてん} (exclusive dealer), {会社名|かいしゃめい} (company name)
- **Geography/science (3)**: {緯線|いせん} (latitude line), {西経|せいけい} (west longitude), {高層雲|こうそううん} (altostratus cloud)
- **Food/cooking (3)**: {焼|や}き{網|あみ} (grill net), {赤|あか}ピーマン (red bell pepper), {焙煎機|ばいせんき} (coffee roaster)
- **Architecture/urban (3)**: {超高層|ちょうこうそう} (super high-rise), {工事現場|こうじげんば} (construction site), {中央広場|ちゅうおうひろば} (central plaza)
- **Entertainment/media (2)**: {娯楽映画|ごらくえいが} (entertainment film), ホラー{小説|しょうせつ} (horror novel)
- **Agriculture (1)**: {施肥|せひ} (fertilization)
- **Art/craft (2)**: {彫刻刀|ちょうこくとう} (carving chisel), {色付|いろづ}ける (to color/tint)
- **Medicine/body (2)**: {血小板|けっしょうばん} (platelet), {低身長|ていしんちょう} (short stature)
- **Housing (1)**: お{屋敷|やしき} (mansion)
- **Education (1)**: {学習指導要領|がくしゅうしどうようりょう} (curriculum guidelines)
- **Technology (1)**: {高解像度|こうかいぞうど} (high resolution)
- **Literary (1)**: {場景|ばけい} (scene/setting)
- **Transportation (1)**: {自動車道|じどうしゃどう} (motorway/expressway)
- **Planning (1)**: {方案|ほうあん} (plan/proposal)
- **Nature (1)**: {鹿角|ろっかく} (antler)
- Conjugation table auto-generated for 1 ichidan verb entry
- 30 candidates synced from candidate list

Total entries: 25,978 → 26,008.

### 2026-04-29 (Vocabulary Expansion - 15 New Entries, Batch 63)
Added 15 new dictionary entries (IDs 26171-26185) from candidate_words.json. Diverse batch covering education, emergency services, daily life, manufacturing, medicine, nature, religion, transportation, and commerce.

- **Education/documents (2)**: {教案|きょうあん} (lesson plan), {合格証|ごうかくしょう} (passing certificate)
- **Emergency services (3)**: {救急隊|きゅうきゅうたい} (rescue squad), ポンプ{車|しゃ} (pumper truck), {誘導路|ゆうどうろ} (taxiway)
- **Daily life (3)**: {郵便箱|ゆうびんばこ} (mailbox), {電気剃刀|でんきかみそり} (electric razor), {価格表示|かかくひょうじ} (price display)
- **Medicine (1)**: {頓服薬|とんぷくやく} (as-needed medication)
- **Nature/agriculture (2)**: {稲田|いなだ} (rice paddy), {留鳥|りゅうちょう} (resident bird)
- **Manufacturing (1)**: {旋盤|せんばん} (lathe)
- **Social/formal (2)**: {紹介者|しょうかいしゃ} (introducer/referrer), ご{労苦|ろうく} (hard work/toil)
- **Religion (1)**: {奉献|ほうけん} (dedication/offering)
- Removed 3 stale candidates (duplicates of existing entries)
- 15 candidates synced from candidate list

Total entries: 25,963 → 25,978.

### 2026-04-29 (Vocabulary Expansion - 25 New Entries, Batch 62)
Added 25 new dictionary entries (IDs 26146-26170) from candidate_words.json. Mixed batch covering daily life, business, culture, health, and modern technology.

- **Food/culture (2)**: {柏|かしわ} (oak leaf / chicken in Kansai), お{惣菜屋|そうざいや} (deli, prepared-food shop)
- **Business/finance (5)**: {稟議書|りんぎしょ} (approval document), {着金|ちゃっきん} (payment received), {価格上昇|かかくじょうしょう} (price increase), {部品代|ぶひんだい} (parts cost), {印刷会社|いんさつがいしゃ} (printing company)
- **Technology/modern life (3)**: キャッシュレス{決済|けっさい} (cashless payment), オンライン{取引|とりひき} (online transaction), {重低音|じゅうていおん} (deep bass)
- **Health/body (2)**: {便|べん} (stool), {半月板|はんげつばん} (meniscus)
- **Transportation (3)**: {車内広告|しゃないこうこく} (in-train ads), {移動距離|いどうきょり} (travel distance), {走行速度|そうこうそくど} (travel speed)
- **Daily life/practical (5)**: {建築中|けんちくちゅう} (under construction), {巻|ま}き{取|と}り (winding/reeling), {連|つ}れて{帰|かえ}る (bring someone home), {淡|あわ}い{色|いろ} (pale color), {適正使用|てきせいしよう} (proper use)
- **Language/culture (3)**: こいつら (these guys), {色欲|しきよく} (lust), ネガ (negative film/pessimistic)
- **Education (1)**: {発声練習|はっせいれんしゅう} (vocal practice)
- **Counter (1)**: {一通|いっつう} (one letter/document)
- Conjugation tables auto-generated for 4 suru-verb entries
- 25 candidates synced from candidate list

Total entries: 25,938 → 25,963.

### 2026-04-29 (Vocabulary Expansion - 21 New Entries, Batch 61)
Added 21 new dictionary entries (IDs 26125-26145) from candidate_words.json. Diverse batch covering psychology, cooking, science, medicine, law, history, and grammar.

- **Psychology/cognition (2)**: {内観|ないかん} (introspection), {妄想癖|もうそうへき} (habit of fantasizing)
- **Cooking/food (4)**: {丸揚|まるあ}げ (whole deep-frying), {醤油焼|しょうゆや}き (soy sauce grilling), {丸煮|まるに} (simmered whole), {生豆|なままめ} (raw/green beans)
- **Science/geology (2)**: {火成岩|かせいがん} (igneous rock), {変成岩|へんせいがん} (metamorphic rock)
- **Medical (3)**: {低体温症|ていたいおんしょう} (hypothermia), {癒合|ゆごう} (bone healing/fusion), {抗菌薬|こうきんやく} (antibacterial drug)
- **Law/politics (3)**: {不敬罪|ふけいざい} (lese-majeste), {免官|めんかん} (dismissal from office), {脱会|だっかい} (withdrawal from organization)
- **Practical/daily life (3)**: {防寒具|ぼうかんぐ} (cold-weather gear), {国名|こくめい} (country name), {操業中|そうぎょうちゅう} (in operation)
- **Education/grammar (1)**: {普通体|ふつうたい} (plain style)
- **Culture/history (1)**: {孔子|こうし} (Confucius)
- **Other (2)**: {救助者|きゅうじょしゃ} (rescuer), {相対性|そうたいせい} (relativity)
- Conjugation tables auto-generated for 4 suru-verb entries
- 21 candidates synced from candidate list

Total entries: 25,917 → 25,938.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
