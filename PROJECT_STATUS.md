# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-21
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
| Total entries | ~17,898 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~15,099 (open) |
| Candidate words | ~6,272 |
| Cross-references | ~3,400 |
| Example sentences | ~51,830 |
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

### 2026-03-21 (Vocabulary Expansion - 35 New Entries, Session 470)
Added 35 new dictionary entries (IDs 18332-18366) from candidate_words.json.

- **Nouns (28)**: {護衛艦|ごえいかん} (escort ship), {豪速球|ごうそっきゅう} (blazing fastball), {爵位|しゃくい} (peerage), {胸骨|きょうこつ} (sternum), {深奥|しんおう} (profound depths), {佳人|かじん} (beautiful woman), {阿吽|あうん} (a-un), {指向性|しこうせい} (directivity), {移調|いちょう} (transposition), {副読本|ふくどくほん} (supplementary reader), {基板|きばん} (circuit board), {導体|どうたい} (conductor), {国体|こくたい} (national polity), {発赤|ほっせき} (erythema), {泳力|えいりょく} (swimming ability), {絶対量|ぜったいりょう} (absolute amount), {所有欲|しょゆうよく} (possessiveness), {悪口雑言|あっこうぞうごん} (torrent of insults), {一家離散|いっかりさん} (family breakup), {匍匐前進|ほふくぜんしん} (belly crawl), {徒手空拳|としゅくうけん} (bare-handed), {鱗粉|りんぷん} (wing scales), {開襟|かいきん} (open collar), {銅色|あかがねいろ} (copper color), {床面|ゆかめん} (floor surface), {少佐|しょうさ} (major), {中佐|ちゅうさ} (lieutenant colonel), {加速器|かそくき} (accelerator)
- **Other (7)**: {一個|いっこ}ずつ (one by one), {牌|ぱい} (mahjong tile), {給紙|きゅうし} (paper feed), {排気量|はいきりょう} (engine displacement), {困窮者|こんきゅうしゃ} (the needy), {陣中見舞|じんちゅうみま}い (morale visit), {板|いた}ガム (stick gum)

Notable features:
- Military: {護衛艦|ごえいかん}, {少佐|しょうさ}, {中佐|ちゅうさ}, {匍匐前進|ほふくぜんしん}
- Four-character compounds: {悪口雑言|あっこうぞうごん}, {一家離散|いっかりさん}, {匍匐前進|ほふくぜんしん}, {徒手空拳|としゅくうけん}
- Technical: {基板|きばん}, {導体|どうたい}, {指向性|しこうせい}, {加速器|かそくき}, {排気量|はいきりょう}
- Medical: {胸骨|きょうこつ}, {発赤|ほっせき}
- Literary: {佳人|かじん}, {深奥|しんおう}, {銅色|あかがねいろ}
- New kanji added: 匍 (ID 02576), 匐 (ID 02577)
- Removed 4 stale candidates (duplicates: {太っ腹|ふとっぱら}, {憎|にく}しみ, {小刻|こきざ}みに, {倍返|ばいがえ}し)

Total entries: ~18,143 → ~18,178 (approximate)
Remaining candidates: ~6,026 → ~5,988 (35 removed as entries + 4 stale removed)

### 2026-03-21 (Vocabulary Expansion - 35 New Entries, Session 469)
Added 35 new dictionary entries (IDs 18297-18331) from candidate_words.json.

- **Nouns (20)**: {秀才|しゅうさい} (prodigy), {凡人|ぼんじん} (ordinary person), {造花|ぞうか} (artificial flower), {愛国心|あいこくしん} (patriotism), {骸骨|がいこつ} (skeleton), {点線|てんせん} (dotted line), {生垣|いけがき} (hedge), {至近距離|しきんきょり} (point-blank range), {小山|こやま} (hill), {半紙|はんし} (calligraphy paper), {競歩|きょうほ} (race walking), {胃痛|いつう} (stomachache), {波線|なみせん} (wavy line), {護身術|ごしんじゅつ} (self-defense), {新境地|しんきょうち} (new ground), {座卓|ざたく} (low table), {症例|しょうれい} (clinical case), セルフサービス (self-service), {三次元|さんじげん} (three-dimensional), {強者|きょうしゃ} (the strong)
- **Nouns with suru (5)**: {大騒|おおさわ}ぎ (uproar), {出願|しゅつがん} (application), {休職|きゅうしょく} (leave of absence), {即断|そくだん} (snap decision), {治験|ちけん} (clinical trial)
- **Nouns/Na-adjectives (3)**: {不評|ふひょう} (unpopularity), {不信|ふしん} (distrust), {非課税|ひかぜい} (tax-exempt)
- **Other nouns (4)**: {残|のこ}り{物|もの} (leftovers), {引|ひ}け{目|め} (feeling of inferiority), {細切|こまぎ}れ (small pieces), {同性|どうせい} (same sex), {憐|あわ}れみ (pity)
- **Expressions (2)**: {阿吽|あうん}の{呼吸|こきゅう} (perfect synchronization), {羽目|はめ}を{外|はず}す (to go overboard)

Notable features:
- People/personality: {秀才|しゅうさい}, {凡人|ぼんじん}, {強者|きょうしゃ}
- Medical: {治験|ちけん}, {症例|しょうれい}, {胃痛|いつう}
- Expressions/idioms: {阿吽|あうん}の{呼吸|こきゅう}, {羽目|はめ}を{外|はず}す
- Daily life: {残|のこ}り{物|もの}, {造花|ぞうか}, セルフサービス, {座卓|ざたく}, {半紙|はんし}
- New kanji added: 吽 (ID 02575)

Total entries: ~18,108 → ~18,143 (approximate)
Remaining candidates: ~6,062 → ~6,026 (35 removed + 1 stale)

### 2026-03-21 (Vocabulary Expansion - 35 New Entries, Session 468)
Added 35 new dictionary entries (IDs 18262-18296) from candidate_words.json.

- **Nouns (15)**: {起動|きどう} (startup), {開催地|かいさいち} (host city), {前売|まえう}り{券|けん} (advance ticket), {残量|ざんりょう} (remaining amount), {一団|いちだん} (a group), {億万長者|おくまんちょうじゃ} (billionaire), {相部屋|あいべや} (shared room), {三連休|さんれんきゅう} (three-day holiday), {旧型|きゅうがた} (old model), {展望台|てんぼうだい} (observation deck), {低音|ていおん} (bass), {卓球|たっきゅう} (table tennis), {船長|せんちょう} (ship captain), {黒砂糖|くろざとう} (brown sugar), {角砂糖|かくざとう} (sugar cube)
- **Noun/Suru verbs (5)**: {手直|てなお}し (correction), {閲覧|えつらん}する (to browse), {寄生|きせい} (parasitism), {退出|たいしゅつ} (leaving), {噴出|ふんしゅつ} (eruption)
- **Na-adjectives (4)**: {活動的|かつどうてき} (active), {高圧的|こうあつてき} (overbearing), {表情豊|ひょうじょうゆた}か (expressive), {平易|へいい} (plain)
- **Verbs (3)**: {見回|みまわ}る (to patrol), {黙|だま}り{込|こ}む (to fall silent), うずくまる (to crouch down)
- **Expressions (3)**: {面倒|めんどう}を{見|み}る (to look after), {目|め}を{逸|そ}らす (to look away), {裏|うら}をかく (to outwit)
- **Nouns (5)**: {丸|まる}み (roundness), {短時間|たんじかん} (short time), {雲行|くもゆ}き (way things are going), {身|み}の{程|ほど} (one's place), {主権|しゅけん} (sovereignty)

Notable features:
- Technology: {起動|きどう}, {閲覧|えつらん}する, {旧型|きゅうがた}
- Daily life: {前売|まえう}り{券|けん}, {相部屋|あいべや}, {三連休|さんれんきゅう}, {角砂糖|かくざとう}, {黒砂糖|くろざとう}
- Expressions/idioms: {裏|うら}をかく, {身|み}の{程|ほど}, {雲行|くもゆ}き
- Cross-references added for 3 homophones: {起動|きどう}/{軌道|きどう}, {一団|いちだん}/{一段|いちだん}, {寄生|きせい}/{帰省|きせい}/{規制|きせい}

Total entries: ~18,073 → ~18,108 (approximate)
Remaining candidates: ~6,097 → ~6,062 (35 removed)

### 2026-03-20 (Vocabulary Expansion - 35 New Entries, Session 467)
Added 35 new dictionary entries (IDs 18227-18261) from candidate_words.json.

- **Nouns (14)**: {守衛|しゅえい} (security guard), ござ (rush mat), {牧師|ぼくし} (pastor), {図解|ずかい} (diagram), スパイ (spy), {善|よ}し{悪|あ}し (good or bad), {正夢|まさゆめ} (prophetic dream), {裏面|りめん} (back side), {豪雪|ごうせつ} (heavy snowfall), {自制心|じせいしん} (self-control), {人脈|じんみゃく} (personal connections), {偽名|ぎめい} (false name), {共稼|ともかせ}ぎ (dual income), {主催者|しゅさいしゃ} (organizer)
- **Noun/Suru verbs (7)**: {誓約|せいやく} (oath), {著作|ちょさく} (literary work), {同感|どうかん} (agreement), {根絶|こんぜつ} (eradication), {進呈|しんてい} (presentation), {死別|しべつ} (bereavement), {感知|かんち} (detection)
- **Na-adjectives (5)**: {無邪気|むじゃき} (innocent), {一途|いちず} (wholehearted), {強情|ごうじょう} (stubborn), {不謹慎|ふきんしん} (imprudent), {純真|じゅんしん} (pure)
- **Noun/Suru verb (1)**: {密封|みっぷう} (airtight seal)
- **Verbs (5)**: {見損|みそこ}なう (to misjudge), {枯|か}らす (to let wither), {恥|は}じる (to feel ashamed), {聞|き}き{返|かえ}す (to ask again), しなる (to bend)
- **Noun (4)**: {所帯|しょたい} (household), {筋道|すじみち} (logic), {聖地|せいち} (sacred place)

Notable features:
- Character/personality: {無邪気|むじゃき}, {純真|じゅんしん}, {一途|いちず}, {強情|ごうじょう}, {自制心|じせいしん}
- Social/professional: {人脈|じんみゃく}, {主催者|しゅさいしゃ}, {共稼|ともかせ}ぎ, {守衛|しゅえい}
- Communication: {同感|どうかん}, {聞|き}き{返|かえ}す, {誓約|せいやく}, {進呈|しんてい}
- Pop culture: {聖地|せいち} (anime pilgrimage), {正夢|まさゆめ}
- Daily life: ござ, {密封|みっぷう}, {裏面|りめん}, {図解|ずかい}

Total entries: ~18,038 → ~18,073 (approximate)
Remaining candidates: ~6,132 → ~6,097 (35 removed)

### 2026-03-20 (Vocabulary Expansion - 35 New Entries, Session 465)
Added 35 new dictionary entries (IDs 18157-18191) from candidate_words.json.

- **Nouns (20)**: {園児|えんじ} (kindergarten child), {豪邸|ごうてい} (mansion), {通算|つうさん} (cumulative total), {供|そな}え{物|もの} (offering), {嗜好品|しこうひん} (indulgence item), {土星|どせい} (Saturn), {水星|すいせい} (Mercury), {膝掛|ひざか}け (lap blanket), {抱|だ}き{枕|まくら} (body pillow), パプリカ (bell pepper), {手札|てふだ} (hand of cards), {貯水池|ちょすいち} (reservoir), {湧|わ}き{水|みず} (spring water), {安楽死|あんらくし} (euthanasia), {走行距離|そうこうきょり} (mileage), {五分咲|ごぶざ}き (half-bloom), {水上|すいじょう} (on the water), {肘掛|ひじか}け (armrest), {公民館|こうみんかん} (community center), {町民|ちょうみん} (townspeople)
- **Noun/Suru verbs (7)**: {脚色|きゃくしょく} (dramatization), {再認識|さいにんしき} (renewed recognition), {駐在|ちゅうざい} (stationing), {丸写|まるうつ}し (copying verbatim), {殴打|おうだ} (striking), {防疫|ぼうえき} (epidemic prevention), {並走|へいそう} (running parallel)
- **Verb (1)**: {捻|ひね}り{出|だ}す (to squeeze out / to devise)
- **Na-adjectives (2)**: {粗悪|そあく} (inferior), {真|ま}っ{正直|しょうじき} (dead honest)
- **Nouns with special context (3)**: お{点前|てまえ} (tea ceremony technique), {口|くち}づけ (kiss - literary), {正当防衛|せいとうぼうえい} (self-defense - legal)
- **Noun/Verb-suru (2)**: {急死|きゅうし} (sudden death), {慈愛|じあい} (benevolent love)

Notable features:
- Daily life: パプリカ, {膝掛|ひざか}け, {抱|だ}き{枕|まくら}, {肘掛|ひじか}け, {公民館|こうみんかん}
- Astronomy: {土星|どせい}, {水星|すいせい}
- Culture: {五分咲|ごぶざ}き (cherry blossom scale), お{点前|てまえ} (tea ceremony), {供|そな}え{物|もの}
- Legal/medical: {正当防衛|せいとうぼうえい}, {安楽死|あんらくし}, {防疫|ぼうえき}, {殴打|おうだ}
- Cross-references added for 3 homophones: {水星|すいせい}/{彗星|すいせい}, {防疫|ぼうえき}/{貿易|ぼうえき}, {急死|きゅうし}/{休止|きゅうし}

Total entries: ~17,968 → ~18,003 (approximate)
Remaining candidates: ~6,202 → ~6,167 (35 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
