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
| Total entries | ~14,684 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~11,885 (open) |
| Candidate words | ~5,085 |
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

### 2026-03-02 (Vocabulary Expansion - 30 New Entries, Session 358)
Added 30 new dictionary entries (IDs 14509-14538) from candidate_words.json:

- **I-adjective (1)**: {重|おも}たい (heavy — colloquial)
- **Na-adjectives (2)**: {閑静|かんせい} (quiet/peaceful), {間近|まぢか} (close/imminent)
- **Godan verbs (2)**: {閉|と}じこもる (to shut oneself in), {阻|はば}む (to block)
- **Godan verb (1)**: {陥|おちい}る (to fall into)
- **Noun/suru verbs (10)**: {通説|つうせつ} (accepted theory), {進言|しんげん} (advice to a superior), {鎖国|さこく} (national isolation), {鑑賞|かんしょう} (appreciation), {長居|ながい} (overstaying), {長続|ながつづ}き (lasting), {閉鎖|へいさ} (closure), {開花|かいか} (flowering), {隔離|かくり} (quarantine), {隠居|いんきょ} (retirement)
- **Nouns (14)**: {農作業|のうさぎょう} (farm work), {錦鯉|にしきごい} (koi), {鎮痛|ちんつう} (pain relief), {長女|ちょうじょ} (eldest daughter), {長男|ちょうなん} (eldest son), {長雨|ながあめ} (prolonged rain), {門松|かどまつ} (New Year's pine decoration), {闇|やみ} (darkness/black market), {降雪|こうせつ} (snowfall), {陶器|とうき} (pottery), {随一|ずいいち} (foremost), {際限|さいげん} (limit), {障壁|しょうへき} (barrier), {閃光|せんこう} (flash)

Notable features:
- Multi-sense entries: {開花|かいか} (2: blooming + bearing fruit), {闇|やみ} (2: darkness + black market), {間近|まぢか} (2: nearby + imminent), {隠居|いんきょ} (2: retirement + retired person)
- Culture: {門松|かどまつ}, {錦鯉|にしきごい}, {鎖国|さこく}, {陶器|とうき}
- Family: {長女|ちょうじょ}, {長男|ちょうなん}
- Weather: {長雨|ながあめ}, {降雪|こうせつ}
- Medical: {鎮痛|ちんつう}, {隔離|かくり}
- New kanji: 2,478 → 2,481 ({錦|きん}, {鎮|ちん}, {閃|せん})

Total entries: 14,564 → 14,594 (approximate)
Remaining candidates: 5,205 → 5,175 (30 removed)

### 2026-03-01 (Vocabulary Expansion - 30 New Entries, Session 357)
Added 30 new dictionary entries (IDs 14479-14508) from candidate_words.json:

- **Nouns (20)**: {背脂|せあぶら} (back fat/ramen topping), {行司|ぎょうじ} (sumo referee), {良書|りょうしょ} (good book), {署員|しょいん} (station staff), {追|お}っ{手|て} (pursuer), {送|おく}り{火|び} (Obon farewell fire), {通商|つうしょう} (trade/commerce), {通年|つうねん} (year-round), {連峰|れんぽう} (mountain range), {選抜|せんばつ} (selection), {配分|はいぶん} (allocation), {重曹|じゅうそう} (baking soda), {野鳥|やちょう} (wild bird), {金平糖|こんぺいとう} (konpeito candy), {鉢合|はちあ}わせ (running into someone), {金物|かなもの} (hardware/ironware), {鉄壁|てっぺき} (iron wall), {銭|ぜに} (money/coin), {野草|やそう} (wild plant), {配下|はいか} (subordinate)
- **Multi-sense noun (2)**: {銘柄|めいがら} (brand + stock issue), {重|おも}み (weight + significance)
- **Na-adjective (1)**: {鋭敏|えいびん} (keen/acute)
- **Expressions (1)**: {諸行無常|しょぎょうむじょう} (all things are impermanent)
- **Nouns (other) (6)**: {謀略|ぼうりゃく} (stratagem), {襟首|えりくび} (scruff of neck), {輪廻|りんね} (cycle of rebirth), {連立|れんりつ} (coalition), {進撃|しんげき} (advance/charge), {都道府県|とどうふけん} (prefectures)

Notable features:
- Multi-sense entries: {銘柄|めいがら} (2: brand + stock), {重|おも}み (2: physical weight + significance)
- Food/culture: {背脂|せあぶら}, {金平糖|こんぺいとう}, {重曹|じゅうそう}, {送|おく}り{火|び}, {行司|ぎょうじ}
- Nature: {野鳥|やちょう}, {野草|やそう}, {連峰|れんぽう}
- Politics/economics: {連立|れんりつ}, {通商|つうしょう}, {配分|はいぶん}, {銘柄|めいがら}, {選抜|せんばつ}
- Philosophy/religion: {諸行無常|しょぎょうむじょう}, {輪廻|りんね}
- New kanji: 2,475 → 2,478 ({峰|ほう}, {廻|かい}, {曹|そう})

Total entries: 14,534 → 14,564 (approximate)
Remaining candidates: 5,235 → 5,205 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
