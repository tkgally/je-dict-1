# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-23
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
| Total entries | ~13,214 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~10,415 (open) |
| Candidate words | ~463 |
| Cross-references | ~3,400 |
| Example sentences | ~46,050 |
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

### 2026-02-23 (Vocabulary Expansion - 30 New Entries, Session 311)
Added 30 new dictionary entries (IDs 13099-13128) from candidate_words.json:

- **Adverbs (1)**: {果|は}たして (as expected; really?)
- **Nouns (13)**: {枠|わく} (frame/slot), {柚子|ゆず} (yuzu citrus), {柵|さく} (fence/barrier), {核心|かくしん} (core/crux), {根元|ねもと} (root/base), {根底|こんてい} (foundation/basis), {校門|こうもん} (school gate), {枠組|わくぐ}み (framework), {板前|いたまえ} (Japanese chef), {松茸|まつたけ} (matsutake mushroom), {核兵器|かくへいき} (nuclear weapons), {桜並木|さくらなみき} (row of cherry trees), {桜前線|さくらぜんせん} (cherry blossom front)
- **Na-adjective/nouns (2)**: {柔軟|じゅうなん} (flexible), {格段|かくだん} (remarkably)
- **I-adjective (1)**: {根強|ねづよ}い (deep-rooted)
- **Noun/no-adjective (1)**: {根本|こんぽん} (fundamental)
- **Noun/prefix (1)**: {核|かく} (nucleus/nuclear)
- **Noun/suru verbs (5)**: {栽培|さいばい} (cultivation), {格闘|かくとう} (grappling), {来訪|らいほう} (visit), {格付|かくづ}け (rating), {格上|かくあ}げ (upgrade)
- **Verbs (3)**: {栄|さか}える (to prosper, ichidan), {根付|ねづ}く (to take root, godan), {根|ね}ざす (to be rooted in, godan)

Notable features:
- 根- cluster: {根強|ねづよ}い, {根本|こんぽん}, {根底|こんてい}, {根元|ねもと}, {根付|ねづ}く, {根|ね}ざす
- 格- cluster: {格闘|かくとう}, {格段|かくだん}, {格付|かくづ}け, {格上|かくあ}げ
- 核- cluster: {核|かく}, {核心|かくしん}, {核兵器|かくへいき}
- 桜- pair: {桜並木|さくらなみき}, {桜前線|さくらぜんせん}
- Cultural: {柚子|ゆず} (yuzu bath), {梅干|うめぼ}し (umeboshi), {松茸|まつたけ} (luxury mushroom), {板前|いたまえ} (sushi chef), {桜前線|さくらぜんせん} (spring tracking)
- Cross-references between related entries: {根本|こんぽん}↔{根底|こんてい}, {枠|わく}↔{枠組|わくぐ}み, {格付|かくづ}け↔{格上|かくあ}げ, {根付|ねづ}く↔{根|ね}ざす
- Homophone: {核心|かくしん}↔{革新|かくしん}
- New kanji: 2,385 → 2,388 ({枠|わく}, {柚|ゆず}, {柵|さく})

Total entries: 13,154 → 13,184 (approximate)
Remaining candidates: 523 → 493 (30 removed)

### 2026-02-23 (Vocabulary Expansion - 30 New Entries, Session 310)
Added 30 new dictionary entries (IDs 13069-13098) from candidate_words.json:

- **Nouns (13)**: {文言|もんごん} (wording), {文様|もんよう} (pattern/design), {月間|げっかん} (monthly period), {有事|ゆうじ} (emergency), {朝廷|ちょうてい} (imperial court), {木星|もくせい} (Jupiter), {未遂|みすい} (attempted crime), {晩春|ばんしゅん} (late spring), {晩餐会|ばんさんかい} (banquet), {暖流|だんりゅう} (warm current), {曲目|きょくもく} (musical piece), {明細書|めいさいしょ} (detailed statement), {本殿|ほんでん} (main shrine building)
- **Noun/no-adjective (5)**: {最強|さいきょう} (strongest), {最短|さいたん} (shortest), {最速|さいそく} (fastest), {最長|さいちょう} (longest), {有形|ゆうけい} (tangible), {木製|もくせい} (wooden)
- **Noun/adverb (2)**: {最大限|さいだいげん} (maximum), {最小限|さいしょうげん} (minimum)
- **Na-adjective (1)**: {有用|ゆうよう} (useful)
- **Adverb (1)**: {末永|すえなが}く (for a long time)
- **Noun/prefix (2)**: {日米|にちべい} (Japan-US), {時限|じげん} (time limit/timed)
- **Noun/suru verb (1)**: {本格化|ほんかくか} (getting into full swing)
- **Nouns (3)**: {本家|ほんけ} (main family/originator), {本拠地|ほんきょち} (headquarters), {村長|そんちょう} (village chief), {未然|みぜん} (prevention)

Notable features:
- 最- superlative cluster: {最大限|さいだいげん}, {最小限|さいしょうげん}, {最強|さいきょう}, {最短|さいたん}, {最速|さいそく}, {最長|さいちょう}
- Antonym pairs: {最大限|さいだいげん}↔{最小限|さいしょうげん}, {最短|さいたん}↔{最長|さいちょう}
- Homophone pairs: {木星|もくせい}↔{木製|もくせい}, {最速|さいそく}↔{催促|さいそく}, {村長|そんちょう}↔{尊重|そんちょう}
- Multi-sense entries: {本家|ほんけ} (main family/originator), {時限|じげん} (class period/timed prefix)
- Cultural: {朝廷|ちょうてい} (imperial court), {本殿|ほんでん} (Shinto shrine), {晩餐会|ばんさんかい} (state dinners), {晩春|ばんしゅん} (Ozu film)
- New kanji: 2,384 → 2,385 ({餐|さん})

Total entries: 13,124 → 13,154 (approximate)
Remaining candidates: 553 → 523 (30 removed)

### 2026-02-23 (Vocabulary Expansion - 30 New Entries, Session 309)
Added 30 new dictionary entries (IDs 13039-13068) from candidate_words.json:

- **Nouns/counters (3)**: {台|だい} (stand/counter for machines), {号|ごう} (number/issue), {和|わ} (harmony/Japanese-style)
- **Na-adjective (1)**: {急|きゅう} (sudden/steep/urgent)
- **Nouns (12)**: {恒星|こうせい} (star), {新春|しんしゅん} (New Year), {方位|ほうい} (direction/bearing), {旧正月|きゅうしょうがつ} (Lunar New Year), {書記|しょき} (secretary/clerk), {最低限|さいていげん} (minimum), {最前線|さいぜんせん} (forefront), {最盛期|さいせいき} (peak period), {来客|らいきゃく} (visitor), {村人|むらびと} (villager), {木工|もっこう} (woodworking), {末尾|まつび} (tail end)
- **Noun/suru verbs (6)**: {改訂|かいてい} (revision of text), {明文化|めいぶんか} (codification), {明言|めいげん} (clear statement), {新調|しんちょう} (getting new), {来日|らいにち} (coming to Japan), {来店|らいてん} (visiting a store)
- **Noun/na-adj (1)**: {未完成|みかんせい} (incomplete)
- **Noun (2)**: {本文|ほんぶん} (main text), {書|か}き{方|かた} (way of writing)
- **Verbs (5)**: {映|うつ}し{出|だ}す (to project/reflect, godan), {書|か}き{入|い}れる (to write in, ichidan), {書|か}き{出|だ}す (to begin writing/list out, godan), {束|たば}ねる (to bundle/lead, ichidan), {明|あ}け{暮|く}れる (to be absorbed in, ichidan)

Notable features:
- Multi-sense entries: {台|だい} (stand/counter), {号|ごう} (issue/designation), {和|わ} (harmony/Japanese-style), {急|きゅう} (sudden/steep/urgent), {映|うつ}し{出|だ}す (project/portray), {書|か}き{出|だ}す (begin writing/list out), {束|たば}ねる (bundle/lead)
- Homophone distinction: {改訂|かいてい} (text) vs {改定|かいてい} (standards)
- 最- prefix cluster: {最低限|さいていげん}, {最前線|さいぜんせん}, {最盛期|さいせいき}
- 来- pattern cluster: {来日|らいにち}, {来客|らいきゃく}, {来店|らいてん}
- 書き- compound cluster: {書|か}き{入|い}れる, {書|か}き{出|だ}す, {書|か}き{方|かた}
- Cultural: {和|わ} (Japanese-style prefix), {新春|しんしゅん} (New Year), {旧正月|きゅうしょうがつ} (Lunar New Year)

Total entries: 13,094 → 13,124 (approximate)
Remaining candidates: 583 → 553 (30 removed)

### 2026-02-23 (Vocabulary Expansion - 30 New Entries, Session 308)
Added 30 new dictionary entries (IDs 13009-13038) from candidate_words.json:

- **Na-adjectives (5)**: {最終的|さいしゅうてき} (final/ultimate), {普遍的|ふへんてき} (universal), {晴|は}れやか (bright/radiant), {最適|さいてき} (optimal), {最悪|さいあく} (worst/terrible)
- **Na-adjective/nouns (3)**: {未熟|みじゅく} (immature/unripe), {有意義|ゆういぎ} (meaningful), {慣用|かんよう} (idiomatic)
- **Nouns (13)**: {最先端|さいせんたん} (cutting edge), {最優先|さいゆうせん} (top priority), {未成年|みせいねん} (minor), {木材|もくざい} (timber), {木|き}の{実|み} (nut/berry), {有無|うむ} (presence or absence), {有権者|ゆうけんしゃ} (voter), {有識者|ゆうしきしゃ} (expert), {書面|しょめん} (written document), {書体|しょたい} (typeface), {暴力団|ぼうりょくだん} (crime syndicate), {新芽|しんめ} (new bud), {末期|まっき} (final stage)
- **Noun/no-adjective (1)**: {未知|みち} (unknown)
- **Noun/suru verbs (4)**: {新設|しんせつ} (new establishment), {明記|めいき} (clearly stating), {明示|めいじ} (explicit indication), {改定|かいてい} (revision of standards)
- **Nouns (3)**: {本体|ほんたい} (main body), {本名|ほんみょう} (real name), {放射能|ほうしゃのう} (radioactivity)
- **Noun (1)**: {支|ささ}え (support)

Notable features:
- Multi-sense entries: {最悪|さいあく} (worst/terrible exclamation), {未熟|みじゅく} (inexperienced/unripe), {本体|ほんたい} (main unit/true form)
- 最- prefix cluster: {最悪|さいあく}, {最適|さいてき}, {最先端|さいせんたん}, {最優先|さいゆうせん}, {最終的|さいしゅうてき}
- 未- prefix cluster: {未知|みち}, {未熟|みじゅく}, {未成年|みせいねん}
- Formal/written: {書面|しょめん}, {明記|めいき}, {明示|めいじ}, {有権者|ゆうけんしゃ}, {有識者|ゆうしきしゃ}
- Homophone distinction: {改定|かいてい} (standards/prices) vs {改訂|かいてい} (text)
- New kanji: 2,383 → 2,384 ({遍|へん})

Total entries: 13,064 → 13,094 (approximate)
Remaining candidates: 363 → 333 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
