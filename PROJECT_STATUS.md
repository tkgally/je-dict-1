# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-07
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
| Total entries | ~15,554 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~12,755 (open) |
| Candidate words | ~4,217 |
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

### 2026-03-07 (Vocabulary Expansion - 30 New Entries, Session 390)
Added 30 new dictionary entries (IDs 15469-15498) from candidate_words.json:

- **Nouns (11)**: {道草|みちくさ} (dawdling on the way), {各駅停車|かくえきていしゃ} (local train), {平熱|へいねつ} (normal body temperature), {黒幕|くろまく} (mastermind), {蔵書|ぞうしょ} (book collection), {競泳|きょうえい} (competitive swimming), {靴底|くつぞこ} (shoe sole), {満車|まんしゃ} (parking lot full), {頭髪|とうはつ} (head hair), {五十音|ごじゅうおん} (Japanese syllabary), {出版物|しゅっぱんぶつ} (publication)
- **Noun/verb-suru (3)**: {日焼|ひや}け (sunburn/suntan), {積|つ}ん{読|どく} (buying books and not reading them), {研鑽|けんさん} (diligent study)
- **Expressions (4)**: {宝|たから}の{持|も}ち{腐|ぐさ}れ (wasted talent), {万事休|ばんじきゅう}す (all is lost), {重箱|じゅうばこ}の{隅|すみ}をつつく (to nitpick), {否|いな}めない (undeniable)
- **Na-adjectives (3)**: {罰当|ばちあ}たり (sacrilegious), {盛|も}りだくさん (packed with content), {恩知|おんし}らず (ungrateful)
- **I-adjective (1)**: {思慮深|しりょぶか}い (thoughtful, prudent)
- **Nouns (other) (5)**: {神頼|かみだの}み (praying as last resort), {打開策|だかいさく} (breakthrough measure), {立|た}ち{居振|いふ}る{舞|ま}い (deportment), {音律|おんりつ} (melody/tuning), {異聞|いぶん} (strange tale)
- **Adverb/noun (1)**: {数多|あまた} (many, numerous)
- **Noun (1)**: {洗|あら}い{場|ば} (washing area)
- **Time noun (1)**: {一昨年|いっさくねん} (year before last)

Notable features:
- Mix of practical daily vocabulary ({日焼|ひや}け, {各駅停車|かくえきていしゃ}, {満車|まんしゃ}, {靴底|くつぞこ}) and literary/cultural words ({数多|あまた}, {異聞|いぶん}, {万事休|ばんじきゅう}す)
- Multiple proverbs and set expressions: {宝|たから}の{持|も}ち{腐|ぐさ}れ, {重箱|じゅうばこ}の{隅|すみ}をつつく
- Book/reading theme: {積|つ}ん{読|どく}, {蔵書|ぞうしょ}, {出版物|しゅっぱんぶつ}
- Multi-sense entries: {日焼|ひや}け (2: skin + materials), {音律|おんりつ} (2: melody + tuning system), {異聞|いぶん} (2: strange tale + variant account)
- New kanji: 2,511 → 2,512 ({鑽|さん})

Total entries: ~15,524 → ~15,554 (approximate)
Remaining candidates: ~4,247 → ~4,217 (30 removed)

### 2026-03-07 (Vocabulary Expansion - 30 New Entries, Session 389)
Added 30 new dictionary entries (IDs 15439-15468) from candidate_words.json:

- **Expressions (9)**: {意地|いじ}を{張|は}る (to be stubborn), {腰|こし}を{下|お}ろす (to sit down), {手|て}に{負|お}えない (unmanageable), {目|め}を{輝|かがや}かせる (eyes light up), {腰|こし}を{抜|ぬ}かす (frozen with shock), {満員御礼|まんいんおんれい} (full house), {火|ひ}の{用心|ようじん} (beware of fire), {命|いのち}に{関|かか}わる (life-threatening), {首|くび}を{縦|たて}に{振|ふ}る (to nod yes)
- **Nouns (7)**: {非対面|ひたいめん} (non-face-to-face), {発送済|はっそうず}み (shipped), {永住権|えいじゅうけん} (permanent residency), {鎮痛剤|ちんつうざい} (painkiller), {老夫婦|ろうふうふ} (elderly couple), {名著|めいちょ} (masterpiece book), {新年度|しんねんど} (new fiscal year)
- **Noun/verb-suru (3)**: {精通|せいつう} (being well-versed), {熟達|じゅくたつ} (proficiency), {抑止力|よくしりょく} (deterrent force)
- **Verbs (3)**: {引|ひ}き{連|つ}れる (to take along), {奪|うば}い{合|あ}う (to scramble for), {踏|ふ}みにじる (to trample)
- **Na-adjective (1)**: {全般的|ぜんぱんてき} (overall)
- **Adverb (1)**: {従来通|じゅうらいどお}り (as before)
- **Other nouns (4)**: {下|した}の{名前|なまえ} (given name), {開発者|かいはつしゃ} (developer), {免状|めんじょう} (diploma), {雨乞|あまご}い (praying for rain)
- **Verb-ichidan (1)**: {取|と}り{留|と}める (to save a life)
- **Multi-sense verb (1)**: {踏|ふ}みにじる (2: literal trampling + figurative violation)

Notable features:
- Strong emphasis on expressions and idioms (9 entries)
- Practical daily life: {発送済|はっそうず}み, {非対面|ひたいめん}, {鎮痛剤|ちんつうざい}, {開発者|かいはつしゃ}
- Culture: {満員御礼|まんいんおんれい}, {火|ひ}の{用心|ようじん}, {雨乞|あまご}い
- Immigration/legal: {永住権|えいじゅうけん}
- New kanji: 2,510 → 2,511 ({乞|こ})

Total entries: ~15,494 → ~15,524 (approximate)
Remaining candidates: ~4,277 → ~4,247 (30 removed)

### 2026-03-06 (Vocabulary Expansion - 30 New Entries, Session 388)
Added 30 new dictionary entries (IDs 15409-15438) from candidate_words.json:

- **Nouns (17)**: {所在地|しょざいち} (location/address), {街路樹|がいろじゅ} (roadside trees), {原産地|げんさんち} (place of origin), {製造元|せいぞうもと} (manufacturer), {愛読書|あいどくしょ} (favorite book), {縮尺|しゅくしゃく} (map scale), {年中行事|ねんじゅうぎょうじ} (annual event), {美容師|びようし} (beautician), {執念|しゅうねん} (tenacity), {鉄橋|てっきょう} (railway bridge), {薄味|うすあじ} (mild flavor), {革靴|かわぐつ} (leather shoes), {円筒|えんとう} (cylinder), {立|た}て{札|ふだ} (notice board), {初舞台|はつぶたい} (debut performance), {口|くち}ぶり (way of talking), {霊魂|れいこん} (soul/spirit)
- **Verbs (4)**: {慌|あわ}てふためく (to panic), {企|くわだ}てる (to plot), {発覚|はっかく}する (to be revealed), {的中|てきちゅう}する (to hit the mark)
- **Na-adjectives (3)**: {断続的|だんぞくてき} (intermittent), {口達者|くちだっしゃ} (silver-tongued), {共学|きょうがく} (coeducation)
- **Adverb (1)**: {相次|あいつ}いで (one after another)
- **Multi-sense nouns (3)**: {墓穴|ぼけつ} (grave + own undoing), {空白|くうはく} (blank space + void), {研磨|けんま} (polishing + skill refinement)
- **Multi-sense verb (1)**: {的中|てきちゅう}する (hitting target + prediction coming true)

Notable features:
- Diverse domains: business ({所在地|しょざいち}, {製造元|せいぞうもと}, {原産地|げんさんち}), food ({薄味|うすあじ}), culture ({年中行事|ねんじゅうぎょうじ}, {初舞台|はつぶたい}), daily life ({美容師|びようし}, {革靴|かわぐつ}, {愛読書|あいどくしょ})
- News/formal vocabulary: {発覚|はっかく}する, {相次|あいつ}いで, {断続的|だんぞくてき}

Total entries: ~15,464 → ~15,494 (approximate)
Remaining candidates: ~4,307 → ~4,277 (30 removed)

### 2026-03-06 (Vocabulary Expansion - 30 New Entries, Session 387)
Added 30 new dictionary entries (IDs 15379-15408) from candidate_words.json:

- **Nouns (17)**: {鼻緒|はなお} (thong strap), {和傘|わがさ} (Japanese umbrella), {木管|もっかん} (woodwind), {金管|きんかん} (brass instrument), しゃり (sushi rice), {雨林|うりん} (rainforest), {魚卵|ぎょらん} (fish roe), {少額|しょうがく} (small sum), {形状|けいじょう} (shape/form), {姓|せい} (surname), {年|とし}の{瀬|せ} (year-end), {命綱|いのちづな} (lifeline), {専業|せんぎょう} (sole occupation), {出身地|しゅっしんち} (birthplace), {水不足|みずぶそく} (water shortage), {塗|ぬ}り{物|もの} (lacquerware), {寒暖計|かんだんけい} (thermometer)
- **Noun/verb-suru (3)**: {浮上|ふじょう} (surfacing), {復職|ふくしょく} (returning to work), {養蜂|ようほう} (beekeeping)
- **Na-adjectives (4)**: まともな (proper/decent), {残虐|ざんぎゃく} (cruel/brutal), {絶望的|ぜつぼうてき} (hopeless), {純朴|じゅんぼく} (simple and honest)
- **Other nouns (3)**: ピエロ (clown), {直喩|ちょくゆ} (simile), {隠喩|いんゆ} (metaphor)
- **Noun (building) (1)**: {石造|いしづく}り (stone construction)
- **Verb (1)**: {切|き}り{裂|さ}く (to slash/rip apart)
- **Person noun (1)**: {独裁者|どくさいしゃ} (dictator)

Notable features:
- Paired entries: {木管|もっかん}/{金管|きんかん}, {直喩|ちょくゆ}/{隠喩|いんゆ}
- Multi-sense entries: まともな (2: proper + direct), {命綱|いのちづな} (2: safety rope + figurative lifeline), {浮上|ふじょう} (2: surfacing + emergence)
- Culture/tradition: {和傘|わがさ}, {鼻緒|はなお}, {塗|ぬ}り{物|もの}, しゃり, {年|とし}の{瀬|せ}
- Academic: {直喩|ちょくゆ}, {隠喩|いんゆ}, {形状|けいじょう}
- Daily life: {出身地|しゅっしんち}, {復職|ふくしょく}, {専業|せんぎょう}, {少額|しょうがく}

Total entries: 15,434 → 15,464 (approximate)
Remaining candidates: 4,337 → 4,307 (30 removed)

### 2026-03-06 (Vocabulary Expansion - 30 New Entries, Session 386)
Added 30 new dictionary entries (IDs 15349-15378) from candidate_words.json:

- **Noun/verb-suru (9)**: {判別|はんべつ} (distinction), {算出|さんしゅつ} (calculation), {服従|ふくじゅう} (obedience), {創立|そうりつ} (founding), {順延|じゅんえん} (postponement), {自死|じし} (suicide/euphemistic), {苦闘|くとう} (bitter struggle), {自害|じがい} (suicide/historical), {夕涼|ゆうすず}み (enjoying evening cool)
- **Nouns (13)**: {及第点|きゅうだいてん} (passing grade), {図案|ずあん} (design/pattern), {短歌|たんか} (tanka poetry), {白和|しらあ}え (tofu-dressed vegetables), {共著|きょうちょ} (co-authorship), {礼状|れいじょう} (thank-you letter), {家紋|かもん} (family crest), {工芸品|こうげいひん} (handicraft), {甲冑|かっちゅう} (armor), {錦絵|にしきえ} (color woodblock print), {画題|がだい} (painting subject), {遊郭|ゆうかく} (pleasure quarter), {蒸気機関車|じょうききかんしゃ} (steam locomotive)
- **Na-adjective (1)**: {明快|めいかい} (clear/lucid)
- **Noun/adjective-na (1)**: {無気力|むきりょく} (apathy/lethargy)
- **Person nouns (2)**: {道化師|どうけし} (clown), {老婆|ろうば} (old woman), {花魁|おいらん} (oiran)
- **Verbs (2)**: {究|きわ}める (to master/investigate), {仕|し}でかす (to make a blunder)
- **Intransitive verb (1)**: {野垂|のた}れ{死|じ}ぬ (to die in the gutter)

Notable features:
- Cultural: {家紋|かもん}, {錦絵|にしきえ}, {短歌|たんか}, {遊郭|ゆうかく}, {花魁|おいらん}, {甲冑|かっちゅう}, {夕涼|ゆうすず}み
- Academic/formal: {算出|さんしゅつ}, {創立|そうりつ}, {共著|きょうちょ}, {判別|はんべつ}, {明快|めいかい}
- Daily life: {礼状|れいじょう}, {白和|しらあ}え, {蒸気機関車|じょうききかんしゃ}, {工芸品|こうげいひん}
- New kanji: 2,507 → 2,510 ({冑|かぶと}, {婆|ばば}, {魁|さきがけ})

Total entries: 15,404 → 15,434 (approximate)
Remaining candidates: 4,367 → 4,337 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
