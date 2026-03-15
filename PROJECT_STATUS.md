# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-15
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
| Total entries | ~17,069 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~14,270 (open) |
| Candidate words | ~2,710 |
| Cross-references | ~3,400 |
| Example sentences | ~50,000 |
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

### 2026-03-15 (Vocabulary Expansion - 35 New Entries, Session 436)
Added 35 new dictionary entries (IDs 16986-17020) from candidate_words.json:

- **Nouns (16)**: {総合|そうごう} (comprehensive), {箇条書|かじょうが}き (bulleted list), {条件付|じょうけんつ}き (conditional), {助|たす}け{合|あ}い (mutual aid), {読点|とうてん} (comma), {釜飯|かまめし} (pot rice), {粗食|そしょく} (plain food), {襟元|えりもと} (neckline), {語調|ごちょう} (tone of voice), {太鼓判|たいこばん} (seal of approval), ひし{形|がた} (diamond shape), {茶菓子|ちゃがし} (tea cakes), {純金|じゅんきん} (pure gold), {高層|こうそう}ビル (skyscraper), {贅沢品|ぜいたくひん} (luxury item), {同好会|どうこうかい} (hobby club)
- **Nouns/suru (4)**: {漂白|ひょうはく} (bleaching), {占有|せんゆう} (occupancy), {酷使|こくし} (overworking), {繁茂|はんも} (luxuriant growth)
- **Adjectives (3)**: {受動的|じゅどうてき} (passive), {用心深|ようじんぶか}い (cautious), {高機能|こうきのう} (high-performance)
- **Verbs (4)**: {這|は}い{出|だ}す (to crawl out), やって{来|く}る (to come along), {回避|かいひ}する (to avoid), {風車|ふうしゃ} (windmill)
- **Other (8)**: {骨|ほね}を{折|お}る (to take pains), {育|そだ}ちが{良|よ}い (well-bred), {湯桶読|ゆとうよ}み (kun+on reading), {手押|ておし}し{車|ぐるま} (pushcart), {借地|しゃくち} (leased land), {羽音|はおと} (sound of wings), コンタクトレンズ (contact lenses), {変化|へんげ} (shape-shifting)

Notable features:
- Multi-sense: {骨|ほね}を{折|お}る (2: make effort + break bone), {変化|へんげ} (2: transformation + apparition), やって{来|く}る (2: arrive + time/season comes)
- Cross-references: {風車|ふうしゃ} ↔ {風車|かざぐるま}, {変化|へんげ} ↔ {変化|へんか}
- Cultural: {釜飯|かまめし} (station food), {茶菓子|ちゃがし} (tea ceremony), {湯桶読|ゆとうよ}み (kanji reading patterns)
- Linguistics: {読点|とうてん}, {湯桶読|ゆとうよ}み

Total entries: ~17,034 → ~17,069 (approximate)
Remaining candidates: ~2,745 → ~2,710 (35 removed)

### 2026-03-15 (Vocabulary Expansion - 35 New Entries, Session 435)
Added 35 new dictionary entries (IDs 16951-16985) from candidate_words.json:

- **Nouns (16)**: {誘導|ゆうどう} (guidance), {中級|ちゅうきゅう} (intermediate level), {看病|かんびょう} (nursing), {親分|おやぶん} (boss), {抜|ぬ}け{殻|がら} (cast-off skin), {快眠|かいみん} (sound sleep), {派閥|はばつ} (faction), {年頃|としごろ} (marriageable age), {日和|ひより} (weather), {正直者|しょうじきもの} (honest person), {飴玉|あめだま} (hard candy), {愛憎|あいぞう} (love and hate), {平行線|へいこうせん} (parallel lines), {美白|びはく} (skin whitening), {万端|ばんたん} (everything), {一般公開|いっぱんこうかい} (open to public)
- **Nouns/suru (6)**: {軽減|けいげん} (reduction), {補填|ほてん} (compensation), {礼拝|れいはい} (worship), {買|か}い{食|ぐ}い (eating snacks on the go), {完走|かんそう} (finishing a race), {腐心|ふしん} (racking one's brains)
- **Verbs (4)**: {忍|しの}ぶ (to endure/hide), {荒|あ}れ{果|は}てる (to fall into ruin), ぼやける (to become blurry), {上塗|うわぬ}り (topcoat/cover-up)
- **Na-adjectives (2)**: {不吉|ふきつ} (ominous), {簡便|かんべん} (handy)
- **Other (7)**: {更|さら}なる (further), {怠|なま}け{者|もの} (lazy person), {白|しろ}ワイン (white wine), {除夜|じょや}の{鐘|かね} (New Year's Eve bell), {往生際|おうじょうぎわ}が{悪|わる}い (poor loser), {定刻|ていこく} (scheduled time), {重任|じゅうにん} (heavy responsibility)

Notable features:
- Multi-sense: {忍|しの}ぶ (3: endure + conceal + reminisce), {抜|ぬ}け{殻|がら} (2: literal + figurative), {平行線|へいこうせん} (2: geometry + deadlock), {日和|ひより} (2: weather + opportunism), {上塗|うわぬ}り (2: topcoat + cover-up)
- Cultural: {除夜|じょや}の{鐘|かね} (New Year's Eve bell ringing), {抜|ぬ}け{殻|がら} (cicada collecting), {買|か}い{食|ぐ}い (school rules)
- Buddhist: {往生際|おうじょうぎわ}が{悪|わる}い (from Buddhist death concept), {礼拝|れいはい}
- New kanji: 2,550 → 2,551 ({填|てん})

Total entries: ~16,999 → ~17,034 (approximate)
Remaining candidates: ~2,780 → ~2,745 (35 removed)

### 2026-03-15 (Vocabulary Expansion - 35 New Entries, Session 434)
Added 35 new dictionary entries (IDs 16916-16950) from candidate_words.json:

- **Expressions (10)**: {何|なに}が{何|なん}でも (no matter what), {姿|すがた}を{現|あらわ}す (to appear), {顔|かお}を{合|あ}わせる (to meet face-to-face), {気分|きぶん}が{晴|は}れる (to feel refreshed), {先|さき}を{越|こ}す (to beat someone to it), {一抹|いちまつ}の{不安|ふあん} (a touch of anxiety), {汗|あせ}をかく (to sweat), {滅相|めっそう}もない (don't be absurd), {言|い}い{逃|のが}れ (excuse/evasion), {踏|ふ}ん{張|ば}りどころ (crucial moment)
- **Nouns (14)**: {居住者|きょじゅうしゃ} (resident), {情報開示|じょうほうかいじ} (information disclosure), {摩天楼|まてんろう} (skyscraper), {御朱印|ごしゅいん} (shrine/temple seal), ひったくり (purse snatching), {中吊|なかづ}り (train hanging ad), {漂着|ひょうちゃく} (drifting ashore), {焙煎|ばいせん} (roasting), {緊急事態|きんきゅうじたい} (state of emergency), {収拾|しゅうしゅう} (settling), {稼働|かどう} (operation), {規格|きかく} (standard), {収集家|しゅうしゅうか} (collector), {世論調査|よろんちょうさ} (opinion poll)
- **Nouns (5 more)**: {慈善|じぜん} (charity), {幾何学|きかがく} (geometry), {早合点|はやがてん} (jumping to conclusions), {靴擦|くつず}れ (shoe blister), {準備体操|じゅんびたいそう} (warm-up exercises), {無人島|むじんとう} (uninhabited island)
- **Na-adjective (1)**: {不審|ふしん} (suspicious)
- **Adverb (1)**: さほど (not so much)
- **Verbs (3)**: ハラハラする (to be on edge), {光|ひか}り{輝|かがや}く (to shine brilliantly), {指|さ}し{示|しめ}す (to indicate)

Notable features:
- Diverse word types: expressions, nouns, verbs, adverb, na-adjective
- Cultural: {御朱印|ごしゅいん} (temple/shrine seals), {中吊|なかづ}り (train ads), {摩天楼|まてんろう}
- Multi-sense: {汗|あせ}をかく (2: literal sweat + figurative effort), {光|ひか}り{輝|かがや}く (2: literal + figurative), {指|さ}し{示|しめ}す (2: physical pointing + abstract indication)
- Homophone distinctions: {不審|ふしん} vs {不振|ふしん}, {収拾|しゅうしゅう} vs {収集|しゅうしゅう}, {規格|きかく} vs {企画|きかく}, {慈善|じぜん} vs {事前|じぜん}, {稼働|かどう} vs {華道|かどう}
- New kanji: 2,549 → 2,550 ({焙|ばい})

Total entries: ~16,964 → ~16,999 (approximate)
Remaining candidates: ~2,815 → ~2,780 (35 removed)

### 2026-03-15 (Vocabulary Expansion - 45 New Entries, Session 433)
Added 45 new dictionary entries (IDs 16870-16915) from candidate_words.json:

- **Nouns (17)**: {喧騒|けんそう} (tumult), {卸売|おろしう}り (wholesale), {移譲|いじょう} (transfer), {習練|しゅうれん} (training), {振付|ふりつけ} (choreography), {鮪|まぐろ} (tuna), {玉|たま}ねぎ (onion), {隔日|かくじつ} (every other day), {方策|ほうさく} (plan), {二重|にじゅう} (double), ふくらはぎ (calf), {敷布団|しきぶとん} (futon mattress), {小食|しょうしょく} (light eater), {歩留|ぶどま}り (yield rate), {洋紙|ようし} (western paper), {賛助|さんじょ} (sponsorship), {蜜柑|みかん} (mandarin orange)
- **Na-adjectives (7)**: {稀少|きしょう} (rare), しとやか (graceful), {疎|まば}ら (sparse), {日常的|にちじょうてき} (daily), {不急|ふきゅう} (non-urgent), {硬質|こうしつ} (hard), {無恥|むち} (shameless)
- **Verbs (6)**: {憐|あわ}れむ (to pity), {揚|あ}げる (to deep-fry), {怯|ひる}む (to flinch), まどろむ (to slumber), {寛|くつろ}ぐ (to relax), {煎|い}る (to roast)
- **Nouns/suru (4)**: {度忘|どわす}れ (memory lapse), {興隆|こうりゅう} (prosperity), {修業|しゅぎょう} (apprenticeship), {不承知|ふしょうち} (disapproval)
- **Other (11)**: つぼみ (bud), なぞなぞ (riddle), しゃもじ (rice paddle), ウトウト (dozing off), スリ (pickpocket), なんで (why), もしくは (or), {或|ある}いは (or/possibly), {釈然|しゃくぜん}としない (unconvinced), {初等|しょとう} (elementary), {仰|おっしゃ}る{通|とお}り (just as you say)
- **I-adjective (1)**: {見窄|みすぼ}らしい (shabby)

Notable features:
- Food/cooking: {鮪|まぐろ}, {玉|たま}ねぎ, {蜜柑|みかん}, しゃもじ, {煎|い}る, {揚|あ}げる, {小食|しょうしょく}
- Body: ふくらはぎ, ウトウト, まどろむ
- Formal language: もしくは, {或|ある}いは, {仰|おっしゃ}る{通|とお}り, {釈然|しゃくぜん}としない
- Multi-sense: {或|ある}いは (2: or + possibly)
- New kanji: 2,545 → 2,549 ({憐|れん}, {或|わく}, {窄|さく}, {鮪|い})

Total entries: ~16,919 → ~16,964 (approximate)
Remaining candidates: ~2,860 → ~2,815 (45 removed)

### 2026-03-14 (Vocabulary Expansion - 45 New Entries, Session 432)
Added 45 new dictionary entries (IDs 16825-16869) from candidate_words.json:

- **Adjectives (i-adj, 6)**: {子供|こども}っぽい (childish), {胡散臭|うさんくさ}い (shady), {重苦|おもぐる}しい (oppressive), {注意深|ちゅういぶか}い (careful), {湿|しめ}っぽい (damp/gloomy), {流暢|りゅうちょう} (fluent)
- **Adjectives (na-adj, 7)**: {理性的|りせいてき} (rational), {非力|ひりき} (powerless), {意図的|いとてき} (intentional), {好都合|こうつごう} (convenient), {不公平|ふこうへい} (unfair), {内気|うちき} (shy), {優柔不断|ゆうじゅうふだん} (indecisive)
- **Nouns (17)**: {洗脳|せんのう} (brainwashing), {全額|ぜんがく} (full amount), {片思|かたおも}い (unrequited love), {絶景|ぜっけい} (superb view), {万引|まんび}き (shoplifting), {悪影響|あくえいきょう} (bad influence), {古典的|こてんてき} (classical), {鳴|な}き{声|ごえ} (animal cry), {節目|ふしめ} (turning point), {敵意|てきい} (hostility), {駄作|ださく} (poor work), {等身大|とうしんだい} (life-size), {靴紐|くつひも} (shoelace), {運動靴|うんどうぐつ} (sneakers), {朝型|あさがた} (morning person), {見頃|みごろ} (peak viewing season), {梅酒|うめしゅ} (plum wine)
- **Adverbs (4)**: {心|こころ}から (sincerely), いずれも (all/any of them), {不意|ふい}に (unexpectedly), {反射的|はんしゃてき} (reflexively)
- **Suru verbs (4)**: {精進|しょうじん}する (to devote oneself), お{参|まい}り (shrine visit), {勧誘|かんゆう} (solicitation), {挙手|きょしゅ} (show of hands)
- **Other (7)**: おもてなし (hospitality), お{粥|かゆ} (rice porridge), まなざし (gaze), {故意|こい} (intent), {寒|さむ}がり (cold-sensitive person), {暑|あつ}がり (heat-sensitive person), {自撮|じど}り (selfie)

Notable features:
- Multi-sense: {湿|しめ}っぽい (2: damp + gloomy), {古典的|こてんてき} (2: classical + old-fashioned), {等身大|とうしんだい} (2: life-size + authentic)
- Antonym pair: {寒|さむ}がり/{暑|あつ}がり
- Cultural: おもてなし, お{参|まい}り, {梅酒|うめしゅ}, お{粥|かゆ}, {見頃|みごろ}
- Modern: {自撮|じど}り, {洗脳|せんのう}, {朝型|あさがた}
- Four-character compound: {優柔不断|ゆうじゅうふだん}
- New kanji: 2,544 → 2,545 (暢)

Total entries: ~16,874 → ~16,919 (approximate)
Remaining candidates: ~2,905 → ~2,860 (45 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
