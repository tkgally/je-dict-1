# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-03
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
| Total entries | ~14,774 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~11,975 (open) |
| Candidate words | ~4,996 |
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

### 2026-03-03 (Vocabulary Expansion - 30 New Entries, Session 364)
Added 30 new dictionary entries (IDs 14689-14718) from candidate_words.json:

- **Nouns (16)**: {重要文化財|じゅうようぶんかざい} (Important Cultural Property), {陸地|りくち} (land), {顔面|がんめん} (face), {食育|しょくいく} (food education), {音源|おんげん} (sound source/audio track), {高まり|たかまり} (rise/heightening), {高値|たかね} (high price), {高額|こうがく} (large sum), {高温|こうおん} (high temperature), {魚介|ぎょかい} (seafood), {鯛|たい} (sea bream), {黒船|くろふね} (black ships), {黎明期|れいめいき} (dawn of an era), {騎士|きし} (knight), {風当|かぜあ}たり (wind exposure/criticism), {食|く}い{倒|だお}れ (eating oneself into ruin)
- **Noun/suru verb (1)**: {鼓舞|こぶ} (encouragement)
- **Godan verbs (2)**: {陣取|じんど}る (to take up position), {駆|か}る (to drive/compel)
- **Ichidan verbs (2)**: {駆|か}ける (to run/dash), {魅|み}せる (to fascinate)
- **Na-adjectives (4)**: {風流|ふうりゅう} (elegant), {鬱|うつ} (depression), {高らか|たからか} (resounding), {露|あらわ} (exposed/undisguised)
- **Adverb (1)**: {黙々|もくもく} (silently/diligently)
- **Multi-POS (4)**: {風俗|ふうぞく} (customs/entertainment), {雛形|ひながた} (model/template), {鞘|さや} (sheath/pod), {風水|ふうすい} (feng shui)

Notable features:
- Multi-sense entries: {風俗|ふうぞく} (2: customs + adult entertainment), {雛形|ひながた} (2: model + template), {鞘|さや} (2: sheath + pod), {鬱|うつ} (2: depression + gloom), {黒船|くろふね} (2: historical + figurative disruptor), {音源|おんげん} (2: sound source + audio track), {風当|かぜあ}たり (2: wind exposure + criticism), {駆|か}る (2: drive/spur + compel), {駆|か}ける (2: run + gallop), {露|あらわ} (2: exposed + undisguised), {食|く}い{倒|だお}れ (2: spending ruin + Osaka culture)
- Culture: {重要文化財|じゅうようぶんかざい}, {黒船|くろふね}, {風水|ふうすい}, {風流|ふうりゅう}, {鯛|たい}, {食|く}い{倒|だお}れ
- Daily life: {高温|こうおん}, {魚介|ぎょかい}, {顔面|がんめん}, {食育|しょくいく}, {音源|おんげん}
- Finance: {高値|たかね}, {高額|こうがく}
- New kanji: 2,488 → 2,490 ({雛|すい}, {鞘|しょう})

Total entries: 14,744 → 14,774 (approximate)
Remaining candidates: 5,025 → 4,996 (29 removed)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
