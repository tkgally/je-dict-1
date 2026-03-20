# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-20
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

### 2026-03-20 (Vocabulary Expansion - 35 New Entries, Session 464)
Added 35 new dictionary entries (IDs 18122-18156) from candidate_words.json.

- **Nouns (16)**: {中華料理|ちゅうかりょうり} (Chinese cuisine), {公共交通|こうきょうこうつう} (public transportation), {肉食動物|にくしょくどうぶつ} (carnivore), {著作物|ちょさくぶつ} (copyrighted work), {整骨院|せいこついん} (osteopathic clinic), {立|た}ち{見席|みせき} (standing room), {持|も}ち{歌|うた} (signature song), フライ{返|がえ}し (spatula), カトラリー (cutlery), {台所用品|だいどころようひん} (kitchenware), ダイヤ{乱|みだ}れ (schedule disruption), {出張手当|しゅっちょうてあて} (travel allowance), {記載漏|きさいも}れ (omission), {葉物野菜|はものやさい} (leafy vegetables), {波浪|はろう} (ocean waves), {歌唱力|かしょうりょく} (singing ability)
- **Na-adjectives (4)**: {多目的|たもくてき} (multipurpose), {自己中心的|じこちゅうしんてき} (self-centered), {利他的|りたてき} (altruistic), {官能的|かんのうてき} (sensual)
- **Expressions (5)**: {目頭|めがしら}が{熱|あつ}くなる (moved to tears), {肩|かた}を{並|なら}べる (to rival), {視野|しや}を{広|ひろ}げる (to broaden horizons), {百獣|ひゃくじゅう}の{王|おう} (king of beasts), {海外向|かいがいむ}け (for overseas)
- **Noun/Suru verbs (6)**: {拭|ふ}き{掃除|そうじ} (wiping clean), {同時進行|どうじしんこう} (proceeding simultaneously), {現地集合|げんちしゅうごう} (meeting at venue), {給仕|きゅうじ} (waiting tables), {正月遊|しょうがつあそ}び (New Year games), {最先端技術|さいせんたんぎじゅつ} (cutting-edge technology)
- **Other (4)**: {被害妄想|ひがいもうそう} (paranoia), {帰属意識|きぞくいしき} (sense of belonging), {蓋然性|がいぜんせい} (probability), {羽子板|はごいた} (battledore)

Notable features:
- Daily life: {中華料理|ちゅうかりょうり}, カトラリー, フライ{返|がえ}し, {台所用品|だいどころようひん}, {拭|ふ}き{掃除|そうじ}
- Transportation: {公共交通|こうきょうこうつう}, ダイヤ{乱|みだ}れ
- Workplace: {出張手当|しゅっちょうてあて}, {記載漏|きさいも}れ, {同時進行|どうじしんこう}
- Culture: {正月遊|しょうがつあそ}び, {羽子板|はごいた}, {持|も}ち{歌|うた}, {給仕|きゅうじ}
- Personality: {自己中心的|じこちゅうしんてき}, {利他的|りたてき}
- Expressions: {目頭|めがしら}が{熱|あつ}くなる, {肩|かた}を{並|なら}べる, {視野|しや}を{広|ひろ}げる

Total entries: ~17,933 → ~17,968 (approximate)
Remaining candidates: ~6,237 → ~6,202 (35 removed)

### 2026-03-20 (Vocabulary Expansion - 35 New Entries, Session 463)
Added 35 new dictionary entries (IDs 18087-18121) from candidate_words.json.

- **Expressions (7)**: {申|もう}し{訳|わけ}ございません (deeply sorry), {失礼|しつれい}いたします (excuse me - formal), {知恵|ちえ}を{絞|しぼ}る (to rack one's brains), {皮|かわ}をむく (to peel), {食卓|しょくたく}を{囲|かこ}む (gather around the table), {焦点|しょうてん}を{絞|しぼ}る (to focus/narrow down), というのも (the reason is)
- **Nouns (17)**: {負|ふ}の{連鎖|れんさ} (vicious cycle), {時短|じたん}{勤務|きんむ} (reduced working hours), {潜在|せんざい}{意識|いしき} (subconscious), {雑居|ざっきょ}ビル (multi-tenant building), {決定|けってい}{事項|じこう} (decided matters), {客室|きゃくしつ}{乗務員|じょうむいん} (flight attendant), {車内|しゃない}{販売|はんばい} (trolley service), {金融|きんゆう}{政策|せいさく} (monetary policy), {助演|じょえん} (supporting role), {資産|しさん}{運用|うんよう} (asset management), {赤十字|せきじゅうじ} (Red Cross), {配布物|はいふぶつ} (handouts), {公共|こうきょう}{交通|こうつう}{機関|きかん} (public transportation), {国際|こくさい}{連合|れんごう} (United Nations), {安保理|あんぽり} (UN Security Council), {寒冷|かんれい}{前線|ぜんせん} (cold front), {新規|しんき}{開拓|かいたく} (new business development)
- **Na-adjectives (4)**: {能弁|のうべん} (eloquent), {不純|ふじゅん} (impure), {男性的|だんせいてき} (masculine), {精選|せいせん} (careful selection)
- **Other (7)**: {泣|な}き{落|お}とし (tearful persuasion), {幾多|いくた}の (many - literary), {贔屓目|ひいきめ} (biased view), {生薬|しょうやく} (herbal medicine), {毒草|どくそう} (poisonous plant), {禁令|きんれい} (prohibition), {自由形|じゆうがた} (freestyle swimming)

Notable features:
- Formal expressions: {申|もう}し{訳|わけ}ございません, {失礼|しつれい}いたします — business Japanese essentials
- Idiomatic: {知恵|ちえ}を{絞|しぼ}る, {泣|な}き{落|お}とし, {贔屓目|ひいきめ}
- International affairs: {国際|こくさい}{連合|れんごう}, {安保理|あんぽり}, {赤十字|せきじゅうじ}
- Workplace: {時短|じたん}{勤務|きんむ}, {決定|けってい}{事項|じこう}, {新規|しんき}{開拓|かいたく}
- Daily life: {公共|こうきょう}{交通|こうつう}{機関|きかん}, {車内|しゃない}{販売|はんばい}, {皮|かわ}をむく

Total entries: ~17,898 → ~17,933 (approximate)
Remaining candidates: ~6,272 → ~6,237 (35 removed)

### 2026-03-20 (Vocabulary Expansion - 35 New Entries, Session 466)
Added 35 new dictionary entries (IDs 18192-18226) from candidate_words.json.

- **Nouns (17)**: {甘味料|かんみりょう} (sweetener), {滞在先|たいざいさき} (place of stay), {難聴|なんちょう} (hearing loss), {自己犠牲|じこぎせい} (self-sacrifice), {仏様|ほとけさま} (Buddha/the deceased), {焦|こ}げ{茶|ちゃ} (dark brown), {往路|おうろ} (outward journey), {一人旅|ひとりたび} (solo trip), {学割|がくわり} (student discount), {模擬試験|もぎしけん} (mock exam), {継母|ままはは} (stepmother), {雲海|うんかい} (sea of clouds), {日本画|にほんが} (Japanese painting), {春分|しゅんぶん}の{日|ひ} (Vernal Equinox Day), {襟巻|えりま}き (scarf), {冷|ひ}え{性|しょう} (cold sensitivity), {悠々自適|ゆうゆうじてき} (life of leisure)
- **Noun/Suru verbs (3)**: {除雪|じょせつ} (snow removal), {終業|しゅうぎょう} (end of work), {暴露|ばくろ}する (to expose)
- **Verbs (3)**: {分|わ}かち{合|あ}う (to share), {舞|ま}い{落|お}ちる (to flutter down), {見張|みは}る (to keep watch)
- **I-adjectives (2)**: {愛|あい}くるしい (adorable), {回|まわ}りくどい (roundabout)
- **Na-adjectives (4)**: {甘口|あまくち} (sweet/mild), {遠慮|えんりょ}がち (reserved), {温厚|おんこう} (gentle), {不格好|ぶかっこう} (awkward-looking), {縦長|たてなが} (tall and narrow)
- **Adverbs (3)**: {漠然|ばくぜん}と (vaguely), {未然|みぜん}に (before it happens), どことなく (somehow)

Notable features:
- Food/drink: {甘味料|かんみりょう}, {甘口|あまくち}
- Nature/weather: {雲海|うんかい}, {除雪|じょせつ}, {舞|ま}い{落|お}ちる
- Culture: {春分|しゅんぶん}の{日|ひ}, {日本画|にほんが}, {仏様|ほとけさま}, {継母|ままはは}
- Student life: {学割|がくわり}, {模擬試験|もぎしけん}
- Travel: {滞在先|たいざいさき}, {往路|おうろ}, {一人旅|ひとりたび}
- Personality: {温厚|おんこう}, {遠慮|えんりょ}がち, {不格好|ぶかっこう}

Total entries: ~18,003 → ~18,038 (approximate)
Remaining candidates: ~6,167 → ~6,132 (35 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
