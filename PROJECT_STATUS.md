# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-24
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
| Total entries | ~13,334 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~10,535 (open) |
| Candidate words | ~667 |
| Cross-references | ~3,400 |
| Example sentences | ~46,390 |
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

### 2026-02-24 (Vocabulary Expansion - 30 New Entries, Session 316)
Added 30 new dictionary entries (IDs 13249-13278) from candidate_words.json:

- **Nouns (18)**: {決着|けっちゃく} (settlement), {決|き}め{手|て} (deciding factor), {気品|きひん} (elegance), {気質|きしつ} (temperament), {民衆|みんしゅう} (the masses), {水害|すいがい} (flood damage), {水田|すいでん} (rice paddy), {水蒸気|すいじょうき} (steam), {水路|すいろ} (waterway), {汚名|おめい} (disgrace), {氷柱|つらら} (icicle), {沿道|えんどう} (roadside), {波乱|はらん} (turbulence), {没後|ぼつご} (after death), {河川|かせん} (river), {戦乱|せんらん} (turmoil of war), {洋食|ようしょく} (Western food), {民間|みんかん} (private sector)
- **Na-adjective (1)**: {活発|かっぱつ} (active, lively)
- **Noun/na-adjective (1)**: {気|き}がかり (worry, concern)
- **Noun/suru verbs (6)**: {沈黙|ちんもく} (silence), {決断|けつだん} (decision), {決戦|けっせん} (decisive battle), {気兼|きが}ね (reserve), {派遣|はけん} (dispatch/temp staffing), {抹殺|まっさつ} (obliteration)
- **Verbs (2)**: {決|き}めつける (to jump to conclusions, ichidan), {気遣|きづか}う (to worry about, godan)
- **Multi-sense entries (2)**: {民間|みんかん} (2 senses), {派遣|はけん} (2 senses)

Notable features:
- 決- cluster: {決断|けつだん}, {決着|けっちゃく}, {決|き}め{手|て}, {決戦|けっせん}, {決|き}めつける
- 気- cluster: {気合|きあ}い, {気品|きひん}, {気質|きしつ}, {気|き}がかり, {気兼|きが}ね, {気遣|きづか}う
- 水- cluster: {水害|すいがい}, {水田|すいでん}, {水蒸気|すいじょうき}, {水路|すいろ}
- 民- pair: {民衆|みんしゅう}, {民間|みんかん}
- Cultural: {洋食|ようしょく} (Meiji-era Western food), {気兼|きが}ね (Japanese social restraint), {水田|すいでん} (rice cultivation)

Total entries: 13,304 → 13,334 (approximate)
Remaining candidates: 697 → 667 (30 removed)

### 2026-02-24 (Vocabulary Expansion - 30 New Entries, Session 315)
Added 30 new dictionary entries (IDs 13219-13248) from candidate_words.json:

- **Nouns (22)**: {歌謡|かよう} (popular song), {武力|ぶりょく} (military power), {武将|ぶしょう} (military commander), {歩兵|ほへい} (infantry), {死因|しいん} (cause of death), {死者|ししゃ} (fatalities), {殺人|さつじん} (murder), {母語|ぼご} (mother tongue), {民族|みんぞく} (ethnic group), {民俗|みんぞく} (folklore), {民法|みんぽう} (civil law), {極限|きょくげん} (limit/extreme), {機微|きび} (subtlety), {歌劇|かげき} (opera), {母乳|ぼにゅう} (breast milk), {武家|ぶけ} (samurai family), {武芸|ぶげい} (martial arts), {武術|ぶじゅつ} (combat techniques), {歌|うた}い{手|て} (singer), {民|たみ} (the people), {楷書|かいしょ} (block script), {死|し} (death)
- **Na-adjective/noun (1)**: {正統|せいとう} (orthodox, legitimate)
- **Noun/suru verbs (5)**: {殺害|さつがい} (killing), {民主化|みんしゅか} (democratization), {樹立|じゅりつ} (establishment), {武装|ぶそう} (armament), {死去|しきょ} (passing away)
- **Noun with 2 senses (2)**: {殿堂|でんどう} (palace/hall of fame), {毀損|きそん} (damage/defamation)

Notable features:
- 武- cluster: {武力|ぶりょく}, {武将|ぶしょう}, {武装|ぶそう}, {武家|ぶけ}, {武芸|ぶげい}, {武術|ぶじゅつ}
- 死- cluster: {死|し}, {死因|しいん}, {死者|ししゃ}, {死去|しきょ}
- 民- cluster: {民|たみ}, {民族|みんぞく}, {民俗|みんぞく}, {民主化|みんしゅか}, {民法|みんぽう}
- 殺- pair: {殺害|さつがい}, {殺人|さつじん} (with cross-references)
- Homophone pair: {民族|みんぞく}↔{民俗|みんぞく} (with cross-references)
- Multi-sense entries: {殿堂|でんどう} (2 senses), {毀損|きそん} (2 senses)
- Cultural: {武家|ぶけ} (feudal class system), {歌謡|かよう} (Showa music), {楷書|かいしょ} (calligraphy)
- New kanji: 2,394 → 2,396 ({楷|かい}, {毀|き})

Total entries: 13,274 → 13,304 (approximate)
Remaining candidates: 727 → 697 (30 removed)

### 2026-02-24 (Vocabulary Expansion - 30 New Entries, Session 314)
Added 30 new dictionary entries (IDs 13189-13218) from candidate_words.json:

- **Nouns (16)**: {正面|しょうめん} (front/facade), {正体|しょうたい} (true identity), {正論|せいろん} (sound argument), {正念場|しょうねんば} (critical moment), {正社員|せいしゃいん} (regular employee), {歳月|さいげつ} (time/years), {死刑|しけい} (death penalty), {毒舌|どくぜつ} (sharp tongue), {母音|ぼいん} (vowel), {母方|ははかた} (maternal side), {母国語|ぼこくご} (mother tongue), {次男|じなん} (second son), {機種|きしゅ} (device model), {歩調|ほちょう} (pace/cadence), {歩み|あゆみ} (step/progress), {民家|みんか} (private house)
- **Na-adjectives (4)**: {正当|せいとう} (legitimate), {残酷|ざんこく} (cruel), {極悪|ごくあく} (heinous), {楽ちん|らくちん} (easy/effortless)
- **Noun/suru verbs (3)**: {欠如|けつじょ} (lack/deficiency), {毛嫌い|けぎらい} (instinctive dislike), {比例|ひれい} (proportion)
- **Verbs (2)**: {歩む|あゆむ} (to walk/tread, godan), {歩み寄る|あゆみよる} (to compromise, godan)
- **Adverbs/other (5)**: {毎回|まいかい} (every time), {次いで|ついで} (next/subsequently), {歴代|れきだい} (successive), {比喩|ひゆ} (metaphor), {機運|きうん} (momentum)

Notable features:
- 正- cluster: {正面|しょうめん}, {正体|しょうたい}, {正当|せいとう}, {正論|せいろん}, {正念場|しょうねんば}, {正社員|せいしゃいん}
- 歩- cluster: {歩み|あゆみ}, {歩む|あゆむ}, {歩み寄る|あゆみよる}, {歩調|ほちょう}
- 母- cluster: {母音|ぼいん}, {母方|ははかた}, {母国語|ぼこくご}
- Multi-sense entries: {正面|しょうめん} (2), {歩み|あゆみ} (2), {歩む|あゆむ} (2), {歩み寄る|あゆみよる} (2), {民家|みんか} (2), {比例|ひれい} (2), {歩調|ほちょう} (2)
- Cultural: {正社員|せいしゃいん} (Japanese employment system), {正念場|しょうねんば} (kabuki origin)
- New kanji: 2,393 → 2,394 ({喩|ゆ})

Total entries: 13,244 → 13,274 (approximate)
Remaining candidates: 757 → 727 (30 removed)

### 2026-02-23 (Vocabulary Expansion - 30 New Entries, Session 313)
Added 30 new dictionary entries (IDs 13159-13188) from candidate_words.json:

- **Nouns (14)**: {楽器|がっき} (musical instrument), {歌詞|かし} (lyrics), {欠片|かけら} (fragment), {次回|じかい} (next time), {標本|ひょうほん} (specimen), {標高|ひょうこう} (altitude), {構図|こうず} (composition), {機器|きき} (equipment), {楽団|がくだん} (orchestra), {楽曲|がっきょく} (musical composition), {欲|よく} (desire), {欧州|おうしゅう} (Europe), {機材|きざい} (equipment/gear), {機密|きみつ} (classified information)
- **Na-adjectives (2)**: {極端|きょくたん} (extreme), {極秘|ごくひ} (top secret)
- **Noun/suru verbs (7)**: {構想|こうそう} (concept/vision), {構築|こうちく} (construction), {機能|きのう} (function), {模索|もさく} (searching/exploring), {歓喜|かんき} (joy/ecstasy), {欲求|よっきゅう} (desire/urge), {歌唱|かしょう} (singing)
- **Nouns (2)**: {次元|じげん} (dimension), {権威|けんい} (authority)
- **Nouns (1)**: {横書|よこが}き (horizontal writing)
- **Verbs (4)**: {欠|か}く (to lack, godan transitive), {欠|か}ける (to chip/be lacking, ichidan intransitive), {欺|あざむ}く (to deceive, godan), {横|よこ}たわる (to lie down/stretch across, godan)

Notable features:
- Transitive/intransitive pair: {欠|か}く↔{欠|か}ける (with cross-references)
- Music cluster: {楽器|がっき}, {歌詞|かし}, {楽団|がくだん}, {楽曲|がっきょく}, {歌唱|かしょう}
- Secrecy cluster: {極秘|ごくひ}, {機密|きみつ} (with cross-references)
- Equipment pair: {機器|きき}↔{機材|きざい} (with cross-references)
- Desire pair: {欲|よく}↔{欲求|よっきゅう} (with cross-references)
- Multi-sense entries: {機能|きのう} (2 senses), {欠|か}く (2 senses), {欠|か}ける (2 senses), {欠片|かけら} (2 senses), {次元|じげん} (2 senses), {権威|けんい} (2 senses), {標本|ひょうほん} (2 senses), {構図|こうず} (2 senses), {欲|よく} (2 senses), {横|よこ}たわる (2 senses)

Total entries: 13,214 → 13,244 (approximate)
Remaining candidates: 463 → 433 (30 removed)

### 2026-02-23 (Vocabulary Expansion - 30 New Entries, Session 312)
Added 30 new dictionary entries (IDs 13129-13158) from candidate_words.json:

- **Nouns (18)**: {業界|ぎょうかい} (industry), {業者|ぎょうしゃ} (vendor/contractor), {根菜|こんさい} (root vegetable), {枚数|まいすう} (number of flat objects), {棟梁|とうりょう} (master carpenter), {格|かく} (status/rank), {業種|ぎょうしゅ} (type of industry), {極|きょく} (pole/extreme), {極|きわ}み (extreme/peak), {極度|きょくど} (extreme/utmost), {桃色|ももいろ} (pink), {梨|なし} (pear), {棘|とげ} (thorn/splinter), {桶|おけ} (bucket/tub), {桜餅|さくらもち} (cherry blossom rice cake), {桜吹雪|さくらふぶき} (cherry petal shower), {本数|ほんすう} (number of long objects), {擬音|ぎおん} (onomatopoeia)
- **Noun/no-adjectives (3)**: {業務用|ぎょうむよう} (for commercial use), {旧来|きゅうらい} (traditional), {枚挙|まいきょ} (enumeration)
- **Noun/suru verbs (5)**: {検定|けんてい} (certification exam), {検出|けんしゅつ} (detection), {林立|りんりつ} (standing in clusters), {撃退|げきたい} (repelling), {撹乱|かくらん} (disruption)
- **Verbs (2)**: {極|きわ}める (to master, ichidan), {案|あん}ずる (to worry, irregular)
- **Cultural (1)**: {文楽|ぶんらく} (Bunraku puppet theater)
- **Time (1)**: {明|あ}け (dawn/end of period)

Notable features:
- 極- cluster: {極|きょく}, {極|きわ}み, {極|きわ}める, {極度|きょくど} (with cross-references)
- 業- cluster: {業界|ぎょうかい}, {業者|ぎょうしゃ}, {業種|ぎょうしゅ}, {業務用|ぎょうむよう}
- Counter-number pair: {枚数|まいすう}↔{本数|ほんすう} (with cross-references)
- 桜- pair: {桜餅|さくらもち}, {桜吹雪|さくらふぶき}
- Multi-sense entries: {棘|とげ} (3 senses), {格|かく} (3 senses), {極|きょく} (2 senses), {検定|けんてい} (2 senses), {本数|ほんすう} (2 senses), {桃色|ももいろ} (2 senses), {案|あん}ずる (2 senses), {極|きわ}める (2 senses), {擬音|ぎおん} (2 senses), {明|あ}け (2 senses), {棟梁|とうりょう} (2 senses)
- Cultural: {文楽|ぶんらく} (UNESCO heritage), {桜餅|さくらもち} (seasonal sweet), {桜吹雪|さくらふぶき} (poetic spring image)
- New kanji: 2,388 → 2,393 ({撹|かく}, {梁|りょう}, {梨|なし}, {棘|とげ}, {棟|とう})

Total entries: 13,184 → 13,214 (approximate)
Remaining candidates: 493 → 463 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
