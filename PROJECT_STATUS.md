# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-21
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
| Total entries | ~12,485 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~9,686 (open) |
| Candidate words | ~483 |
| Cross-references | ~3,380 |
| Example sentences | ~44,350 |
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

### 2026-02-21 (Vocabulary Expansion - 30 New Entries, Session 288)
Added 30 new dictionary entries (IDs 12400-12429) from candidate_words.json:

- **Nouns - abstract/formal (4)**: {差異|さい} (difference/discrepancy), {山積|さんせき} (accumulation of problems), {対比|たいひ} (contrast/comparison), {巨額|きょがく} (enormous sum)
- **Nouns - culture/religion (4)**: {山車|だし} (festival float), {巫女|みこ} (shrine maiden), {師匠|ししょう} (master/teacher), {帝国|ていこく} (empire)
- **Nouns - food (3)**: {山菜|さんさい} (wild mountain vegetables), {山椒|さんしょう} (Japanese pepper), {干物|ひもの} (dried fish)
- **Nouns - geography/places (2)**: {山道|やまみち} (mountain path), {工房|こうぼう} (workshop/studio)
- **Nouns - daily life/society (5)**: {巷|ちまた} (the streets/the public), {巻|ま}き{寿司|ずし} (sushi roll), {工程|こうてい} (process/procedure), {庶民|しょみん} (common people), {市販|しはん} (commercially available)
- **Nouns - travel/lifestyle (2)**: {帰省|きせい} (returning to hometown), {幼馴染|おさななじみ} (childhood friend)
- **Nouns - other (3)**: {対話|たいわ} (dialogue), {展示|てんじ} (exhibition), {巡回|じゅんかい} (patrol/tour)
- **Na-adjective (1)**: {平凡|へいぼん} (ordinary/commonplace)
- **I-adjective (1)**: {小高|こだか}い (slightly elevated)
- **Ichidan verbs (2)**: {廃|すた}れる (to fall into disuse), {帯|お}びる (to wear/be tinged with)
- **Godan verb (1)**: {巡|めぐ}らす (to encircle/to ponder)
- **Suru verb (1)**: {属|ぞく}する (to belong to)
- **Noun/suru verbs (1)**: {幻|まぼろし} (illusion/phantom/legendary)

Notable features:
- Multi-sense entries: {巡|めぐ}らす (encircle/ponder), {帯|お}びる (wear/be tinged with), {幻|まぼろし} (illusion/legendary rarity)
- Cultural context: {山車|だし} (festival floats at Gion and Takayama), {巫女|みこ} (shrine maiden traditions), {帰省|きせい} (homecoming rush), {山椒|さんしょう} (proverb about small but pungent)
- Similar word comparisons: {差異|さい} vs {違|ちが}い; {対比|たいひ} vs {比較|ひかく}; {巷|ちまた} journalistic usage; {工房|こうぼう} vs {工場|こうじょう}
- New kanji: 2,350 → 2,355 ({匠|しょう}, {巫|ふ}, {巷|こう}, {帝|てい}, {庶|しょ})

Total entries: 12,455 → 12,485
Remaining candidates: 513 → 483 (30 removed)

### 2026-02-21 (Vocabulary Expansion - 30 New Entries, Session 287)
Added 30 new dictionary entries (IDs 12370-12399) from candidate_words.json:

- **Godan verbs (2)**: {寝返|ねがえ}る (to turn over/to defect), {宿|やど}す (to harbor/to conceive)
- **Ichidan verb (1)**: {居合|いあ}わせる (to happen to be present)
- **I-adjective (1)**: {尊|とうと}い (precious/noble/sacred)
- **Nouns - history/culture (6)**: {土偶|どぐう} (clay figurine), {将軍|しょうぐん} (shogun), {宣教師|せんきょうし} (missionary), {家来|けらい} (retainer), {寄席|よせ} (variety theater), {屋敷|やしき} (mansion)
- **Nouns - business/economics (3)**: {売上高|うりあげだか} (total sales), {富裕層|ふゆうそう} (wealthy class), {委譲|いじょう} (delegation of authority)
- **Nouns - abstract/formal (5)**: {始祖|しそ} (founder), {尊厳|そんげん} (dignity), {対決|たいけつ} (confrontation), {対抗|たいこう} (opposition), {展望|てんぼう} (prospect/panoramic view)
- **Nouns - daily life (4)**: {専用|せんよう} (exclusive use), {寝具|しんぐ} (bedding), メイド (maid), バック (back/reversing)
- **Nouns - food/preservation (1)**: {塩蔵|えんぞう} (salt preservation)
- **Nouns - concepts (4)**: {助動詞|じょどうし} (auxiliary verb), {不老不死|ふろうふし} (eternal youth), {多幸感|たこうかん} (euphoria), {女子高生|じょしこうせい} (high school girl)
- **Nouns - medical (1)**: {大動脈|だいどうみゃく} (aorta)
- **Nouns - people (2)**: {小僧|こぞう} (youngster/temple boy), {封印|ふういん} (seal/sealing away)

Notable features:
- Multi-sense entries: {寝返|ねがえ}る (turn in bed/defect), {宿|やど}す (harbor/conceive/reflect light), {将軍|しょうぐん} (shogun/general), {大動脈|だいどうみゃく} (aorta/main artery), バック (background/reversing), メイド (maid/maid cafe worker), {封印|ふういん} (physical seal/sealing away), {尊|とうと}い (precious/sacred), {展望|てんぼう} (outlook/panoramic view), {小僧|こぞう} (brat/temple boy)
- Cultural context: {土偶|どぐう} (Jomon archaeology), {将軍|しょうぐん} (feudal governance), {寄席|よせ} (rakugo tradition), {家来|けらい} (Momotaro folk tale), メイド (Akihabara subculture), {不老不死|ふろうふし} (East Asian mythology)
- Similar word comparisons: {始祖|しそ} vs {創始者|そうししゃ}; {売上高|うりあげだか} vs {売|う}り{上|あ}げ; {対決|たいけつ} vs {対立|たいりつ}; {富裕層|ふゆうそう} vs {金持|かねも}ち; {尊|とうと}い (slang usage in otaku culture)

Total entries: 12,425 → 12,455
Remaining candidates: 543 → 513 (30 removed)

### 2026-02-21 (Vocabulary Expansion - 30 New Entries, Session 286)
Added 30 new dictionary entries (IDs 12340-12369) from candidate_words.json:

- **Godan verbs (3)**: {寝転|ねころ}がる (to sprawl out), {富|と}む (to be rich in), {導|みちび}く (to guide/derive)
- **Ichidan verbs (2)**: {封|ふう}じる (to seal/block), {尽|つ}きる (to run out/be exhausted)
- **Na-adjectives (4)**: {安穏|あんのん} (peaceful), {寡黙|かもく} (taciturn), {対等|たいとう} (equal), {対照的|たいしょうてき} (contrastive)
- **Na-adj/noun (1)**: {小柄|こがら} (petite)
- **Nouns - work/society (3)**: {定職|ていしょく} (steady job), {家業|かぎょう} (family business), {就任|しゅうにん} (taking office)
- **Nouns - abstract/formal (5)**: {容認|ようにん} (acceptance), {実証|じっしょう} (verification), {尺度|しゃくど} (yardstick), {屈指|くっし} (leading/foremost), {対峙|たいじ} (confrontation)
- **Nouns - daily life (5)**: {寝起|ねお}き (waking up), {寝床|ねどこ} (sleeping place), {小遣|こづか}い (pocket money), {居場所|いばしょ} (one's place), {寿命|じゅみょう} (lifespan)
- **Nouns - food (1)**: {完食|かんしょく} (eating everything)
- **Nouns - pattern/form (1)**: {定型|ていけい} (fixed form)
- **Nouns - nature (1)**: {寒波|かんぱ} (cold wave)
- **Noun/suru verbs (4)**: {密集|みっしゅう} (crowding), {寄贈|きぞう} (donation), {対峙|たいじ} (confrontation), {就任|しゅうにん} (inauguration)

Notable features:
- Multi-sense entries: {寝起|ねお}き (waking up/living somewhere), {宿|やど}る (to lodge/to inhabit), {封|ふう}じる (to seal/to suppress), {導|みちび}く (to guide/to derive), {寿命|じゅみょう} (lifespan/service life), {居場所|いばしょ} (location/belonging)
- Cultural context: {家業|かぎょう} (traditional family businesses), {居場所|いばしょ} (social isolation discussions), {完食|かんしょく} (food waste culture), {小遣|こづか}い (salaryman allowance)
- Similar word comparisons: {安穏|あんのん} vs {平穏|へいおん}; {寡黙|かもく} vs {無口|むくち}; {寸前|すんぜん} vs {直前|ちょくぜん}; {尺度|しゃくど} vs {基準|きじゅん}; {富|と}む vs {豊|ゆた}かな
- New kanji: 2,348 → 2,350 ({寡|か}, {峙|じ})

Total entries: 12,380 → 12,410 (actually 12,395 → 12,425 per validator)
Remaining candidates: 573 → 543 (30 removed)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
