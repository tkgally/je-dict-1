# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-02
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
| Total entries | ~14,744 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~11,945 (open) |
| Candidate words | ~5,025 |
| Cross-references | ~3,400 |
| Example sentences | ~49,000 |
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

### 2026-03-02 (Vocabulary Expansion - 30 New Entries, Session 363)
Added 30 new dictionary entries (IDs 14659-14688) from candidate_words.json:

- **Nouns (14)**: {防具|ぼうぐ} (protective gear), {陣営|じんえい} (camp/faction), {雪景色|ゆきげしき} (snowy scenery), {霊|れい} (spirit/ghost), {露天|ろてん} (open air), {顔|かお}ぶれ (lineup), {風紀|ふうき} (public morals), {風貌|ふうぼう} (appearance), {食塩|しょくえん} (table salt), {餅|もち}つき (rice cake pounding), {首位|しゅい} (first place), {香料|こうりょう} (spices/fragrance), {高台|たかだい} (elevated ground), {顔立|かおだ}ち (facial features)
- **Noun/suru verbs (7)**: {開国|かいこく} (opening of a country), {陳情|ちんじょう} (petition), {集約|しゅうやく} (consolidation), {集結|しゅうけつ} (gathering), {頻発|ひんぱつ} (frequent occurrence), {駆使|くし} (full command), {魅了|みりょう} (fascination)
- **Noun/suru verb (1)**: {高望|たかのぞ}み (aiming too high)
- **Noun/adjective-no (1)**: {非日常|ひにちじょう} (extraordinary)
- **Godan verbs (2)**: {霞|かす}む (to become hazy), {駆|か}け{寄|よ}る (to rush over to)
- **Na-adjective (1)**: {鮮明|せんめい} (vivid/clear)
- **Noun (time) (1)**: {頃合|ころあ}い (suitable time)
- **Noun (cultural) (3)**: {金魚|きんぎょ}すくい (goldfish scooping), {開国|かいこく} (opening of country), {餅|もち}つき (mochi pounding)

Notable features:
- Multi-sense entries: {防具|ぼうぐ} (2: sports gear + armor), {霊|れい} (2: spirit + ghost), {香料|こうりょう} (2: spice + fragrance), {霞|かす}む (2: become hazy + be overshadowed), {頃合|ころあ}い (2: suitable time + moderate degree), {陣営|じんえい} (2: faction + military camp), {集約|しゅうやく} (2: consolidation + intensive)
- Culture: {金魚|きんぎょ}すくい, {餅|もち}つき, {露天|ろてん}, {開国|かいこく}
- Daily life: {食塩|しょくえん}, {高台|たかだい}, {顔立|かおだ}ち, {顔|かお}ぶれ
- Formal/written: {類似|るいじ}, {鮮明|せんめい}, {風貌|ふうぼう}, {陳情|ちんじょう}, {駆使|くし}
- New kanji: 2,487 → 2,488 ({陣|じん})

Total entries: 14,714 → 14,744 (approximate)
Remaining candidates: 5,055 → 5,025 (30 removed)

### 2026-03-02 (Vocabulary Expansion - 30 New Entries, Session 362)
Added 30 new dictionary entries (IDs 14629-14658) from candidate_words.json:

- **Verbs (4)**: {面|めん}する (to face), {静|しず}まり{返|かえ}る (to fall completely silent), {馴染|なじ}む (to become familiar), {駆|か}けつける (to rush to)
- **Nouns (17)**: {風呂|ふろ} (bath), {食|しょく}パン (sliced bread), {首輪|くびわ} (collar), {馬車|ばしゃ} (carriage), {魂|たましい} (soul), {魔法|まほう} (magic), {魔女|まじょ} (witch), {魚屋|さかなや} (fish shop), {鮮度|せんど} (freshness), {麺|めん} (noodles), {黄金|おうごん} (gold), {髪型|かみがた} (hairstyle), {高熱|こうねつ} (high fever), {駄々|だだ} (tantrum), {馬力|ばりき} (horsepower), {騒動|そうどう} (commotion), {驚異|きょうい} (wonder)
- **Noun/suru verbs (4)**: {高騰|こうとう} (soaring prices), {集会|しゅうかい} (assembly), {養成|ようせい} (training), {高揚|こうよう} (elation)
- **Nouns (other) (2)**: {頼|たよ}り (reliance), {高齢|こうれい} (old age)
- **I-adjectives (2)**: {頼|たよ}りない (unreliable), {青白|あおじろ}い (pale)
- **Noun (weather) (1)**: {風向|かざむ}き (wind direction)

Notable features:
- Multi-sense entries: {馴染|なじ}む (2: get used to + fit in), {黄金|おうごん} (2: gold + golden/prime), {魂|たましい} (2: soul + spirit/passion), {風向|かざむ}き (2: wind direction + trend), {青白|あおじろ}い (2: pale + bluish-white), {馬力|ばりき} (2: horsepower + vigor)
- Daily life: {風呂|ふろ}, {食|しょく}パン, {首輪|くびわ}, {髪型|かみがた}, {麺|めん}, {魚屋|さかなや}
- Culture/pop culture: {魔法|まほう}, {魔女|まじょ}, {黄金|おうごん}, {魂|たましい}
- Economy/society: {高騰|こうとう}, {高齢|こうれい}, {集会|しゅうかい}, {養成|ようせい}
- New kanji: 2,486 → 2,487 ({魂|こん})

Total entries: 14,684 → 14,714 (approximate)
Remaining candidates: 5,085 → 5,055 (30 removed)

### 2026-03-02 (Vocabulary Expansion - 30 New Entries, Session 361)
Added 30 new dictionary entries (IDs 14599-14628) from candidate_words.json:

- **Nouns (17)**: {随所|ずいしょ} (everywhere), {集|つど}い (gathering), {雑念|ざつねん} (distracting thoughts), {門|もん} (gate), {難所|なんしょ} (difficult spot), {雨水|あまみず} (rainwater), {雪国|ゆきぐに} (snow country), {電力|でんりょく} (electric power), {露天風呂|ろてんぶろ} (open-air bath), {青春|せいしゅん} (youth), {静|しず}けさ (quietness), {面子|めんつ} (face/dignity), {頻度|ひんど} (frequency), {願|ねが}い{事|ごと} (wish), {風船|ふうせん} (balloon), {養子|ようし} (adopted child), {風土|ふうど} (climate and culture)
- **Noun/suru verbs (2)**: {離散|りさん} (dispersal), {非難|ひなん} (criticism)
- **Noun/na-adjective (2)**: {非常識|ひじょうしき} (lack of common sense), {難病|なんびょう} (intractable disease)
- **Ichidan verbs (2)**: {青|あお}ざめる (to turn pale), {飢|う}える (to starve)
- **Godan verbs (3)**: {頬張|ほおば}る (to stuff one's cheeks), {頼|たの}み{込|こ}む (to beg), {食|く}いしばる (to clench teeth)
- **Na-adjective (1)**: {頑|かたく}な (stubborn)
- **Noun (food) (1)**: {風味|ふうみ} (flavor)
- **Noun (geography) (1)**: {陰影|いんえい} (shadow/nuance)
- **Noun (time) (1)**: {震災|しんさい} (earthquake disaster)

Notable features:
- Multi-sense entries: {陰影|いんえい} (2: shading + nuance), {飢|う}える (2: starve + hunger for), {風土|ふうど} (2: climate + cultural character)
- Culture/nature: {露天風呂|ろてんぶろ}, {雪国|ゆきぐに}, {雨水|あまみず}, {震災|しんさい}, {青春|せいしゅん}, {願|ねが}い{事|ごと}
- Body/emotion: {頬張|ほおば}る, {青|あお}ざめる, {食|く}いしばる, {飢|う}える
- Social/abstract: {面子|めんつ}, {非常識|ひじょうしき}, {非難|ひなん}, {養子|ようし}, {離散|りさん}
- Diverse POS mix: nouns, suru verbs, godan verbs, ichidan verbs, na-adjectives

Total entries: 14,654 → 14,684 (approximate)
Remaining candidates: 5,115 → 5,085 (30 removed)

### 2026-03-02 (Vocabulary Expansion - 30 New Entries, Session 360)
Added 30 new dictionary entries (IDs 14569-14598) from candidate_words.json:

- **Noun/suru verbs (12)**: {開店|かいてん} (opening a store), {開業|かいぎょう} (starting a business), {防止|ぼうし} (prevention), {闘争|とうそう} (struggle/conflict), {防御|ぼうぎょ} (defense), {阻害|そがい} (obstruction), {隣接|りんせつ} (adjacent), {離脱|りだつ} (withdrawal), {難航|なんこう} (rough going), {開設|かいせつ} (establishment), {集計|しゅうけい} (tabulation), {陥落|かんらく} (fall/capture)
- **Nouns (7)**: {関門|かんもん} (barrier/hurdle), {階層|かいそう} (class/layer), {集大成|しゅうたいせい} (culmination), {雑煮|ぞうに} (New Year's soup), {難色|なんしょく} (reluctance), {雨上|あめあ}がり (after rain), {雨音|あまおと} (sound of rain), {詰|つ}め{襟|えり} (stand-up collar), {離島|りとう} (remote island)
- **Noun/na-adjective (3)**: {間抜|まぬ}け (fool), {雄弁|ゆうべん} (eloquent), {雑|ざつ} (sloppy)
- **Godan verbs (2)**: {見知|みし}る (to know by sight), {集|つど}う (to gather)
- **Noun (time) (1)**: {除夜|じょや} (New Year's Eve)
- **Adverbs (2)**: {長|なが}らく (for a long time), {難|なん}なく (without difficulty)

Notable features:
- Multi-sense entries: {開店|かいてん} (2: first opening + daily opening), {関門|かんもん} (2: checkpoint + hurdle), {階層|かいそう} (2: social class + layer/tier), {陰|かげ} (2: shade + behind the scenes)
- Culture/seasons: {雑煮|ぞうに}, {除夜|じょや}, {雨上|あめあ}がり, {雨音|あまおと}, {詰|つ}め{襟|えり}
- Business/formal: {開店|かいてん}, {開業|かいぎょう}, {開設|かいせつ}, {集計|しゅうけい}, {難航|なんこう}, {難色|なんしょく}
- Diverse POS mix: nouns, suru verbs, godan verbs, na-adjectives, adverbs

Total entries: 14,624 → 14,654 (approximate)
Remaining candidates: 5,145 → 5,115 (30 removed)

### 2026-03-02 (Vocabulary Expansion - 30 New Entries, Session 359)
Added 30 new dictionary entries (IDs 14539-14568) from candidate_words.json:

- **Ichidan verbs (2)**: {長|た}ける (to be skilled at), {閉|と}じ{込|こ}める (to lock up/confine)
- **Godan verbs (2)**: {謳|うた}う (to extol/stipulate), {諮|はか}る (to consult)
- **Noun/suru verbs (7)**: {鎮圧|ちんあつ} (suppression), {進入|しんにゅう} (entry/approach), {白濁|はくだく} (cloudiness), {配車|はいしゃ} (vehicle dispatch), {閉塞|へいそく} (blockage/stagnation), {開示|かいじ} (disclosure), {除去|じょきょ} (removal)
- **Nouns (14)**: {部活動|ぶかつどう} (club activities), {鎧|よろい} (armor), {遺物|いぶつ} (relic), {部類|ぶるい} (category), {酒宴|しゅえん} (drinking party), {都市部|としぶ} (urban area), {銀髪|ぎんぱつ} (silver hair), {酒浸|さけびた}り (heavy drinking), {見殺|みごろ}し (abandoning), {自失|じしつ} (daze/stupor), {長身|ちょうしん} (tall stature), {門外漢|もんがいかん} (outsider/layman), {防音|ぼうおん} (soundproofing), {陛下|へいか} (Your Majesty)
- **Na-adjectives (2)**: {長|なが}め (somewhat long), {閑散|かんさん} (deserted/slack)
- **Adverb (1)**: {道|みち}すがら (along the way)
- **Noun (time) (1)**: {間際|まぎわ} (just before/verge)
- **Noun (formal) (1)**: {隆盛|りゅうせい} (prosperity/flourishing)

Notable features:
- Multi-sense entries: {謳|うた}う (2: extol + stipulate), {閉塞|へいそく} (2: blockage + stagnation), {閑散|かんさん} (2: deserted + slack)
- Culture/society: {部活動|ぶかつどう}, {鎧|よろい}, {陛下|へいか}, {酒宴|しゅえん}, {門外漢|もんがいかん}
- Daily life: {防音|ぼうおん}, {配車|はいしゃ}, {都市部|としぶ}, {長身|ちょうしん}, {銀髪|ぎんぱつ}
- Formal/literary: {諮|はか}る, {隆盛|りゅうせい}, {道|みち}すがら, {開示|かいじ}
- New kanji: 2,481 → 2,486 ({諮|し}, {謳|おう}, {鎧|がい}, {陛|へい}, {隆|りゅう})

Total entries: 14,594 → 14,624 (approximate)
Remaining candidates: 5,175 → 5,145 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
