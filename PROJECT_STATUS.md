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

### 2026-03-20 (Vocabulary Expansion - 35 New Entries, Session 462)
Added 35 new dictionary entries (IDs 18052-18086) from candidate_words.json.

- **Verbs (8)**: {注|そそ}ぎ{込|こ}む (to pour into), {途切|とぎ}れる (to be interrupted), {和|なご}む (to be soothed), {尊|とうと}ぶ (to value), つぼむ (to close up), {損|そこ}なう (to harm), {被|こうむ}る (to sustain damage), {際立|きわだ}たせる (to make stand out)
- **Nouns/Suru verbs (8)**: {内示|ないじ} (unofficial notice), {更生|こうせい} (rehabilitation), {就航|しゅうこう} (entering service), {発給|はっきゅう} (issuance), {混和|こんわ} (mixing), リバウンド (rebound), {倍返|ばいがえ}し (returning double), {顕在|けんざい} (becoming manifest)
- **Nouns (13)**: {満杯|まんぱい} (full to capacity), {対応力|たいおうりょく} (adaptability), {参政権|さんせいけん} (suffrage), {茶店|さてん} (teahouse), {丙|へい} (third/C grade), {卓|たく} (table), {吉凶|きっきょう} (fortune), {理容室|りようしつ} (barbershop), {電子機器|でんしきき} (electronic device), {生活苦|せいかつく} (hardship), {防腐剤|ぼうふざい} (preservative), {中性|ちゅうせい} (neutral), {砲兵|ほうへい} (artillery), {無機物|むきぶつ} (inorganic matter)
- **Counters (2)**: {頭|とう} (large animals), {尾|び} (fish)
- **Expressions (2)**: {目|め}につく (to catch one's eye), {気|き}にかける (to worry about)
- **Adverb (1)**: これほど (this much)
- **Na-adjective (1)**: {満杯|まんぱい} (full to capacity)

Notable features:
- Verbs with nuance: {和|なご}む (online culture), {損|そこ}なう (verb suffix usage), つぼむ (flower terminology)
- Workplace: {内示|ないじ}, {更生|こうせい}, {対応力|たいおうりょく}
- Daily life: {理容室|りようしつ}, {茶店|さてん}, {防腐剤|ぼうふざい}, {電子機器|でんしきき}
- Culture: {倍返|ばいがえ}し (半沢直樹 catchphrase), {吉凶|きっきょう}, {丙|へい} (Heavenly Stems)
- Counters: {頭|とう}, {尾|び} — animal counting
- New kanji: 2,573 → 2,574 ({丙|へい})
- Removed 11 stale duplicate candidates

Total entries: ~17,863 → ~17,898 (approximate)
Remaining candidates: ~6,317 → ~6,272 (45 removed: 34 created + 11 stale duplicates)

### 2026-03-19 (Vocabulary Expansion - 35 New Entries, Session 461)
Added 35 new dictionary entries (IDs 18017-18051) from candidate_words.json.

- **Nouns (14)**: {鼻歌|はなうた} (humming), {真昼|まひる} (midday), {紳士|しんし} (gentleman), {淑女|しゅくじょ} (lady), {交響曲|こうきょうきょく} (symphony), {演奏会|えんそうかい} (concert), {質感|しつかん} (texture), {郵便物|ゆうびんぶつ} (mail), {木炭|もくたん} (charcoal), {切|き}り{札|ふだ} (trump card), {囲碁|いご} (Go), {救|すく}いの{手|て} (helping hand), {指折|ゆびお}り (leading), {一回|いっかい}きり (once only)
- **Noun/Suru verbs (10)**: {日向|ひなた}ぼっこ (sunbathing), {厳禁|げんきん} (strictly prohibited), {懺悔|ざんげ} (confession), {未払|みばら}い (unpaid), {出題|しゅつだい} (setting questions), {根負|こんま}け (giving in), {密告|みっこく} (informing), {盗作|とうさく} (plagiarism), {殴|なぐ}り{書|が}き (scribbling), {集客|しゅうきゃく} (attracting customers)
- **Noun/Suru verbs (formal) (3)**: {快諾|かいだく} (ready consent), {疎通|そつう} (communication), {贈答|ぞうとう} (gift exchange)
- **Noun/Na-adjectives (3)**: {引|ひ}っ{込|こ}み{思案|じあん} (shy), {崇高|すうこう} (sublime), {高品質|こうひんしつ} (high quality)
- **Na-adjective (1)**: {華|はな}やかな (gorgeous)
- **I-adjectives (2)**: {若々|わかわか}しい (youthful), {汚|けが}らわしい (disgusting)
- **Noun/Verb-suru (1)**: {同情|どうじょう}する (to sympathize)
- **Counter/Noun (1)**: {難問|なんもん} (difficult problem)

Notable features:
- Culture: {囲碁|いご}, {贈答|ぞうとう}, {懺悔|ざんげ}, {紳士|しんし}/{淑女|しゅくじょ} pair
- Music: {交響曲|こうきょうきょく}, {演奏会|えんそうかい}
- Personality: {引|ひ}っ{込|こ}み{思案|じあん}, {若々|わかわか}しい
- Business: {集客|しゅうきゅく}, {未払|みばら}い, {快諾|かいだく}
- Figurative: {切|き}り{札|ふだ}, {救|すく}いの{手|て}, {指折|ゆびお}り
- New kanji: 2,571 → 2,573 ({懺|ざん}, {紳|しん})

Total entries: ~17,828 → ~17,863 (approximate)
Remaining candidates: ~6,352 → ~6,317 (35 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
