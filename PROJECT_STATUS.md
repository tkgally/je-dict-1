# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-20
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
| Total entries | ~12,380 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~9,581 (open) |
| Candidate words | ~461 |
| Cross-references | ~3,380 |
| Example sentences | ~44,050 |
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

### 2026-02-20 (Vocabulary Expansion - 30 New Entries, Session 285)
Added 30 new dictionary entries (IDs 12295-12324) from candidate_words.json:

- **Verbs (3)**: {孕|はら}む (to conceive/be fraught with - godan), {寝|ね}かせる (to lay down/let age - ichidan)
- **Na-adjectives (4)**: {定|さだ}か (definite/certain), {実用的|じつようてき} (practical), {容易|ようい} (easy - formal), {多湿|たしつ} (humid)
- **Nouns - household/family (4)**: {家事|かじ} (housework), {家具|かぐ} (furniture), {家庭|かてい} (home/household), {子持|こも}ち (having children)
- **Nouns - business/work (3)**: {実務|じつむ} (practical work), {多用|たよう} (frequent use/being busy), {多額|たがく} (large sum of money)
- **Nouns - government/legal (3)**: {官邸|かんてい} (official residence), {容疑|ようぎ} (suspicion of crime), {宣誓|せんせい} (oath/pledge)
- **Nouns - abstract/formal (4)**: {安泰|あんたい} (peace/security), {安寧|あんねい} (tranquility), {寄与|きよ} (contribution), {富|とみ} (wealth)
- **Nouns - combat/rivalry (2)**: {実戦|じっせん} (actual combat), {宿敵|しゅくてき} (archenemy)
- **Nouns - culture/food (1)**: {南蛮|なんばん} (nanban-style/Western)
- **Nouns - media (1)**: {密着|みっちゃく} (close contact/behind-the-scenes coverage)
- **Nouns - concepts (4)**: {完璧主義|かんぺきしゅぎ} (perfectionism), {実在|じつざい} (actual existence), {宅|たく} (residence), {多量|たりょう} (large quantity)
- **Nouns - health (2)**: {寝|ね}たきり (bedridden), {察|さっ}し (perception/tact)

Notable features:
- Multi-sense entries: {孕|はら}む (conceive/be fraught with), {子持|こも}ち (parent/containing roe), {多用|たよう} (frequent use/busy), {密着|みっちゃく} (physical contact/media coverage), {寝|ね}かせる (put to bed/let age)
- Cultural context: {南蛮|なんばん} (Portuguese trade history and cuisine), {察|さっ}し (Japanese communication culture), {寝|ね}たきり (aging society)
- Similar word comparisons: {容易|ようい} vs {簡単|かんたん}; {多量|たりょう} vs {大量|たいりょう}; {実戦|じっせん} vs {実践|じっせん}; {寄与|きよ} vs {貢献|こうけん}; {多用|たよう} vs {多様|たよう}
- New kanji: 2,344 → 2,346 ({孕|はら}, {邸|てい})

Total entries: 12,350 → 12,380
Remaining candidates: 491 → 461 (30 removed)

### 2026-02-20 (Vocabulary Expansion - 30 New Entries, Session 284)
Added 30 new dictionary entries (IDs 12265-12294) from candidate_words.json:

- **Nouns - everyday/household (5)**: {定番|ていばん} (standard/staple), {宛先|あてさき} (address/destination), {家計|かけい} (household finances), {家出|いえで} (running away from home), {宝物|たからもの} (treasure)
- **Nouns - medical/health (3)**: {安眠|あんみん} (sound sleep), {安静|あんせい} (rest/quiet repose), {完治|かんち} (complete recovery)
- **Nouns - business/economics (4)**: {大企業|だいきぎょう} (large corporation), {安値|やすね} (low price), {実質|じっしつ} (substance/effectively), {実業家|じつぎょうか} (entrepreneur)
- **Nouns - entertainment/media (4)**: {実写|じっしゃ} (live action), {完結|かんけつ} (completion/conclusion), {実況|じっきょう} (live commentary), {客席|きゃくせき} (audience seating)
- **Nouns - education/academia (2)**: {学園|がくえん} (academy), {学術|がくじゅつ} (scholarship/academic)
- **Nouns - buildings/places (1)**: {宮殿|きゅうでん} (palace)
- **Nouns - nature/harvest (2)**: {実|みの}り (harvest/fruition), {大地震|おおじしん} (major earthquake)
- **Nouns - appearance/emotion (2)**: {容姿|ようし} (appearance/looks), {容赦|ようしゃ} (mercy/forgiveness)
- **Nouns - literary/formal (1)**: {宴|うたげ} (feast/banquet)
- **Na-adjective (1)**: {密接|みっせつ} (close/closely connected)
- **Suru verbs (1)**: {宣言|せんげん} (declaration/proclamation)
- **Godan verb (1)**: {定|さだ}まる (to be settled)
- **Ichidan verb (1)**: {寂|さび}れる (to become deserted)
- **Noun/suru verb (1)**: {寄|よ}り{道|みち} (detour/side trip)
- **Noun (social) (1)**: {孤独死|こどくし} (dying alone)

Notable features:
- Multi-sense entries: {実|みの}り (harvest/fruition), {実質|じっしつ} (substance/effectively), {客席|きゃくせき} (audience seating/passenger seating)
- Cultural context: {孤独死|こどくし} (aging society issue), {大地震|おおじしん} (seismic culture), {定番|ていばん} (retail/cultural staples), {宴|うたげ} (literary/historical banquets)
- Similar word comparisons: {安値|やすね} vs {高値|たかね}; {学園|がくえん} vs {学校|がっこう}; {宴|うたげ} vs {宴会|えんかい}; {定|さだ}まる vs {決|き}まる

Total entries: 12,320 → 12,350
Remaining candidates: 521 → 491 (30 removed)

### 2026-02-20 (Vocabulary Expansion - 30 New Entries, Session 283)
Added 30 new dictionary entries (IDs 12235-12264) from candidate_words.json:

- **Nouns - abstract/formal (6)**: {妨|さまた}げ (hindrance), {喧騒|けんそう}→{威勢|いせい} (vigor), {威信|いしん} (prestige), {大義|たいぎ} (just cause), {字句|じく} (wording), {媒体|ばいたい} (medium/media)
- **Nouns - education (3)**: {学食|がくしょく} (school cafeteria), {学級|がっきゅう} (school class), {学業|がくぎょう} (academics)
- **Nouns - family/people (1)**: {妻子|さいし} (wife and children)
- **Nouns - business/employment (2)**: {子会社|こがいしゃ} (subsidiary), {契約|けいやく}{社員|しゃいん} (contract employee)
- **Nouns - culture/history (5)**: {大和|やまと} (ancient Japan), {大道芸|だいどうげい} (street performance), {守護|しゅご} (guardian/provincial governor), {奉公|ほうこう} (service/apprenticeship), {大判|おおばん} (large format/gold coin)
- **Nouns - general (4)**: {安|やす}らぎ (tranquility), {孤島|ことう} (solitary island), {大台|おおだい} (round-number milestone), {守|まも}り (defense/amulet)
- **Nouns/suru verbs (3)**: {存続|そんぞく} (continuation/survival), {始動|しどう} (starting up/launch), {大別|たいべつ} (broad classification)
- **Na-adjectives (3)**: {安|やす}らか (peaceful), {安価|あんか} (inexpensive), {好|す}き{勝手|かって} (selfish)
- **I-adjectives (1)**: {安|やす}っぽい (cheap-looking, tacky)
- **Nouns - marriage (1)**: {婚姻|こんいん} (marriage - formal/legal)

Notable features:
- Multi-sense entries: {始動|しどう} (engine start/project launch), {守護|しゅご} (protection/provincial governor), {守|まも}り (defense/amulet), {大判|おおばん} (large size/gold coin), {学部|がくぶ} (faculty/undergraduate)
- Cultural context: {大和|やまと} (Yamato civilization/native Japanese vocabulary), {奉公|ほうこう} (feudal service system), {大道芸|だいどうげい} (street performance culture), {学級|がっきゅう}{崩壊|ほうかい} (classroom collapse phenomenon)
- Similar word comparisons: {安価|あんか} vs {安|やす}い; {婚姻|こんいん} vs {結婚|けっこん}; {学業|がくぎょう} vs {勉強|べんきょう}
- New kanji: 2,343 → 2,344 ({姻|いん})

Total entries: 12,290 → 12,320
Remaining candidates: 551 → 521 (30 removed)

### 2026-02-20 (Vocabulary Expansion - 30 New Entries, Session 282)
Added 30 new dictionary entries (IDs 12205-12234) from candidate_words.json:

- **Nouns - preferences/food (3)**: {好|す}き{嫌|きら}い (likes and dislikes), {好物|こうぶつ} (favorite food), {好意|こうい} (goodwill/romantic interest)
- **Nouns - people/family (4)**: {女将|おかみ} (proprietress), {女神|めがみ} (goddess), {女房|にょうぼう} (wife - informal), {姫|ひめ} (princess)
- **Nouns - politics/society (4)**: {大国|たいこく} (major power), {大多数|だいたすう} (vast majority), {外資系|がいしけい} (foreign-affiliated), {委員会|いいんかい} (committee)
- **Nouns - nature/science (2)**: {大麦|おおむぎ} (barley), {太陽系|たいようけい} (solar system)
- **Nouns - culture (1)**: {妖怪|ようかい} (yokai)
- **Nouns - social issues (2)**: {嫌|いや}がらせ (harassment), {子育|こそだ}て (child-rearing)
- **Nouns/suru verbs (5)**: {奨励|しょうれい} (encouragement), {奪取|だっしゅ} (seizure), {妊娠|にんしん} (pregnancy), {孤立|こりつ} (isolation), {始末|しまつ} (management/outcome)
- **Na-adjectives (3)**: {大人気|だいにんき} (very popular), {好調|こうちょう} (going well), {大|おお}がかり (large-scale)
- **Na-adj/adverb (2)**: {存分|ぞんぶん} (to one's heart's content), {如実|にょじつ} (vividly)
- **Verbs (3)**: {妨|さまた}げる (to hinder - ichidan), {威張|いば}る (to swagger - godan), {嫁|とつ}ぐ (to marry into - godan)

Notable features:
- Multi-sense entries: {好意|こうい} (goodwill/romantic interest), {始末|しまつ} (management/sorry outcome), {姫|ひめ} (princess/small prefix)
- Cultural context: {女将|おかみ} (ryokan hospitality), {妖怪|ようかい} (Japanese folklore), {嫁|とつ}ぐ (patrilocal marriage), {子育|こそだ}て (declining birth rate policy)
- Similar word comparisons: {好調|こうちょう} vs {順調|じゅんちょう}; {好意|こうい} vs {親切|しんせつ}; {好機|こうき} vs {機会|きかい}; {妨|さまた}げる vs {邪魔|じゃま}する
- New kanji: 2,339 → 2,343 ({妊|にん}, {妖|よう}, {姫|ひめ}, {娠|しん})

Total entries: 12,260 → 12,290
Remaining candidates: 581 → 551 (30 removed)

### 2026-02-20 (Vocabulary Expansion - 30 New Entries, Session 281)
Added 30 new dictionary entries (IDs 12175-12204) from candidate_words.json:

- **Verbs - ichidan (3)**: {失|う}せる (to vanish/get lost), {奏|かな}でる (to play music), {大人|おとな}びる (to look mature)
- **Na-adjectives (4)**: {大嫌|だいきら}い (to detest), {大々的|だいだいてき} (large-scale), {多様|たよう} (diverse), {多大|ただい} (enormous)
- **Adverbs (3)**: {夜|よ}な{夜|よ}な (night after night), {大概|たいがい} (generally/enough already), {大方|おおかた} (mostly/probably)
- **Nouns - scale/size (3)**: {大規模|だいきぼ} (large-scale), {大都市|だいとし} (major city), {大金|たいきん} (large sum of money)
- **Nouns - time/history (3)**: {大昔|おおむかし} (ancient times), {天下|てんか} (the realm/supremacy), {大河|たいが} (great river)
- **Nouns - language/society (3)**: {失言|しつげん} (verbal gaffe), {失踪|しっそう} (disappearance), {失格|しっかく} (disqualification)
- **Nouns - events/scale (4)**: {大賞|たいしょう} (grand prize), {大作|たいさく} (major work), {大病|たいびょう} (serious illness), {大惨事|だいさんじ} (catastrophe)
- **Nouns - culture/abstract (4)**: {奉納|ほうのう} (shrine offering), {奈落|ならく} (abyss/theater trap), {奥底|おくそこ} (innermost depths), {多岐|たき} (wide-ranging)
- **Nouns - groups (3)**: {多数派|たすうは} (majority faction), {大地|だいち} (earth/ground)

Notable features:
- Multi-sense entries: {失|う}せる (vanish/rude imperative), {大概|たいがい} (generally/moderation), {大方|おおかた} (mostly/probably), {奈落|ならく} (abyss/theater trap), {天下|てんか} (realm/supremacy), {失格|しっかく} (disqualification/unfit)
- Cultural context: {奈落|ならく} (kabuki stage trap), {天下|てんか} (Sengoku period conquest), {奉納|ほうのう} (shrine offerings), {失格|しっかく} ({人間|にんげん}{失格|しっかく} novel)
- Similar word comparisons: {大々的|だいだいてき} vs {大規模|だいきぼ}; {大概|たいがい} vs だいたい vs {大抵|たいてい}; {大作|たいさく} vs {名作|めいさく} vs {傑作|けっさく}
- New kanji: 2,336 → 2,339 ({奈|な}, {奉|ほう}, {踪|そう})

Total entries: 12,230 → 12,260
Remaining candidates: 487 → 457 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
