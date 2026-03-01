# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-01
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
| Total entries | ~14,564 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~11,765 (open) |
| Candidate words | ~5,205 |
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

### 2026-03-01 (Vocabulary Expansion - 30 New Entries, Session 356)
Added 30 new dictionary entries (IDs 14449-14478) from candidate_words.json:

- **Godan verbs (5)**: {連|つら}なる (to stretch in a row), {釣|つ}り{合|あ}う (to be balanced), {鈍|にぶ}る (to become dull), {長引|ながび}く (to drag on), {酔|よ}い{潰|つぶ}れる (to pass out drunk — ichidan)
- **Ichidan verb (1)**: {鑑|かんが}みる (to consider, in light of)
- **Noun/suru verbs (5)**: {連合|れんごう} (union/alliance), {選定|せんてい} (selection/designation), {進級|しんきゅう} (grade promotion), {長持|ながも}ち (long-lasting), {配役|はいやく} (casting)
- **Nouns (13)**: {道化|どうけ} (clown/buffoon), {謀反|むほん} (rebellion), {邦楽|ほうがく} (Japanese music), {部位|ぶい} (body part/site), {酢飯|すめし} (sushi rice), {醜聞|しゅうぶん} (scandal), {里芋|さといも} (taro), {野良犬|のらいぬ} (stray dog), {野郎|やろう} (guy/bastard), {金貨|きんか} (gold coin), {釘付|くぎづ}け (riveted/captivated), {鉄板|てっぱん} (iron plate/sure thing), {銅像|どうぞう} (bronze statue)
- **Nouns (other) (3)**: {鉢巻|はちまき} (headband), {長編|ちょうへん} (full-length work), {長寿|ちょうじゅ} (longevity)
- **Na-adjectives (2)**: {足早|あしばや} (brisk pace), {邪険|じゃけん} (harsh treatment)
- **Na-adjective (1)**: {重厚|じゅうこう} (stately/dignified)

Notable features:
- Multi-sense entries: {鈍|にぶ}る (2: dull blade + weakened skills), {道化|どうけ} (2: person + act), {釘付|くぎづ}け (2: captivated + nailed down), {鉄板|てっぱん} (2: iron plate + sure thing), {野郎|やろう} (2: guy + bastard), {連|つら}なる (2: lined up + attend)
- Food/culture: {酢飯|すめし}, {里芋|さといも}, {邦楽|ほうがく}, {鉢巻|はちまき}, {長寿|ちょうじゅ}
- Daily life: {長引|ながび}く, {長持|ながも}ち, {足早|あしばや}, {野良犬|のらいぬ}, {野郎|やろう}
- Formal/literary: {鑑|かんが}みる, {醜聞|しゅうぶん}, {選定|せんてい}, {謀反|むほん}
- New kanji: 2,474 → 2,475 ({邦|ほう})

Total entries: 14,504 → 14,534 (approximate)
Remaining candidates: 5,265 → 5,235 (30 removed)

### 2026-03-01 (Vocabulary Expansion - 30 New Entries, Session 355)
Added 30 new dictionary entries (IDs 14419-14448) from candidate_words.json:

- **Noun/suru verbs (11)**: {逃避|とうひ} (escape/evasion), {連動|れんどう} (linkage), {連帯|れんたい} (solidarity), {遠出|とおで} (excursion), {遠吠|とおぼ}え (howling), {醸造|じょうぞう} (brewing), {量産|りょうさん} (mass production), {配列|はいれつ} (arrangement/array), {選出|せんしゅつ} (selection/election), {遊|あそ}び{心|ごころ} (playfulness — noun only), {金欠|きんけつ} (being broke — noun only)
- **Na-adjective (1)**: {過密|かみつ} (overcrowding)
- **Verbs (5)**: {通|とお}り{抜|ぬ}ける (to pass through — ichidan), {透|す}かす (to hold up to light — godan), {遠|とお}のく (to recede — godan), {酔|よ}う (to get drunk — godan), {重|おも}んじる (to value — ichidan)
- **Nouns (13)**: {過渡期|かとき} (transitional period), {途上国|とじょうこく} (developing country), {道中|どうちゅう} (during a journey), {道程|みちのり} (distance/journey), {選手権|せんしゅけん} (championship), {遺体|いたい} (corpse/remains), {邸宅|ていたく} (mansion), {部族|ぶぞく} (tribe), {酒屋|さかや} (liquor store), {野生|やせい} (wild/wildlife), {野良猫|のらねこ} (stray cat), {金髪|きんぱつ} (blonde hair), {重|おも}さ (weight/heaviness)

Notable features:
- Multi-sense entries: {透|す}かす (2: hold to light + thin out), {酔|よ}う (3: drunk + motion sick + entranced), {連帯|れんたい} (2: solidarity + joint liability), {道程|みちのり} (2: distance + figurative path), {重|おも}さ (2: physical weight + significance), {配列|はいれつ} (2: arrangement + array), {遠吠|とおぼ}え (2: howling + empty threats)
- Daily life: {酒屋|さかや}, {野良猫|のらねこ}, {金欠|きんけつ}, {金髪|きんぱつ}, {遠出|とおで}
- Society/politics: {途上国|とじょうこく}, {連帯|れんたい}, {選出|せんしゅつ}, {過渡期|かとき}
- Business/tech: {量産|りょうさん}, {連動|れんどう}, {配列|はいれつ}

Total entries: 14,474 → 14,504 (approximate)
Remaining candidates: 5,295 → 5,265 (30 removed)

### 2026-03-01 (Vocabulary Expansion - 30 New Entries, Session 354)
Added 30 new dictionary entries (IDs 14389-14418) from candidate_words.json:

- **Noun/suru verbs (10)**: {転用|てんよう} (repurposing), {転移|てんい} (metastasis/transference), {転身|てんしん} (career change), {輩出|はいしゅつ} (producing talent), {起用|きよう} (appointment), {返上|へんじょう} (forfeiture), {追求|ついきゅう} (pursuit), {配置|はいち} (placement), {配布|はいふ} (distribution), {逃走|とうそう} (escape)
- **Nouns (11)**: {語|かた}り (narration), {軍事|ぐんじ} (military affairs), {軍艦|ぐんかん} (warship), {近世|きんせい} (early modern period), {通称|つうしょう} (common name), {部門|ぶもん} (department), {郷土|きょうど} (homeland), {都度|つど} (each time), {酵素|こうそ} (enzyme), {重点|じゅうてん} (emphasis), {選択肢|せんたくし} (option)
- **Na-adjective (1)**: {辺鄙|へんぴ} (remote)
- **Nouns (other) (4)**: {醍醐味|だいごみ} (true delight), {重傷|じゅうしょう} (serious injury), {野原|のはら} (field/meadow), {遺産|いさん} (heritage/inheritance)
- **Godan verb (1)**: {醸|かも}し{出|だ}す (to create atmosphere)
- **Noun/na-adj/suru verb (1)**: {重宝|ちょうほう} (useful/handy)
- **Godan verb (1)**: {見合|みあ}う (to be proportionate)
- **Noun/suru verb (1)**: {退散|たいさん} (dispersal)

Notable features:
- Multi-sense entries: {見合|みあ}う (2: proportionate + look at each other), {転移|てんい} (2: metastasis + transference), {遺産|いさん} (2: inheritance + heritage), {重宝|ちょうほう} (2: useful + treasure)
- Military/history: {軍事|ぐんじ}, {軍艦|ぐんかん}, {近世|きんせい}, {返上|へんじょう}
- Business/work: {起用|きよう}, {転身|てんしん}, {部門|ぶもん}, {配置|はいち}, {配布|はいふ}
- Science/medicine: {酵素|こうそ}, {転移|てんい}, {重傷|じゅうしょう}
- Culture: {醍醐味|だいごみ} (Buddhist origin), {醸|かも}し{出|だ}す (brewing metaphor), {郷土|きょうど}
- New kanji: 2,470 → 2,474 ({肢|し}, {鄙|ひ}, {醍|だい}, {醐|ご})

Total entries: 14,444 → 14,474 (approximate)
Remaining candidates: 5,325 → 5,295 (30 removed)

### 2026-02-28 (Vocabulary Expansion - 30 New Entries, Session 353)
Added 30 new dictionary entries (IDs 14359-14388) from candidate_words.json:

- **Noun/suru verbs (13)**: {転載|てんさい} (reposting), {送|おく}り{迎|むか}え (picking up and dropping off), {通話|つうわ} (telephone call), {逝去|せいきょ} (passing away), {造形|ぞうけい} (modeling/plastic arts), {進展|しんてん} (progress), {運行|うんこう} (train/bus operation), {遠回|とおまわ}り (detour), {適応|てきおう} (adaptation), {遭遇|そうぐう} (encounter), {進出|しんしゅつ} (expansion/advance), {連結|れんけつ} (connection/coupling), {逃亡|とうぼう} (flight/escape)
- **Nouns (11)**: {農産物|のうさんぶつ} (agricultural products), {近隣|きんりん} (neighborhood), {詰|つ}め{物|もの} (filling/stuffing), {買取|かいとり} (trade-in), {連中|れんちゅう} (bunch/group), {週刊|しゅうかん} (weekly publication), {達人|たつじん} (master/expert), {遠隔|えんかく} (remote), {適量|てきりょう} (proper amount), {道標|みちしるべ} (signpost), {道筋|みちすじ} (route/course)
- **Godan verbs (2)**: {請|う}け{負|お}う (to contract), {遠|とお}ざかる (to recede)
- **Ichidan verb (1)**: {諌|いさ}める (to admonish)
- **Na-adjective (1)**: {過度|かど} (excessive)
- **I-adjective (1)**: {逆風|ぎゃくふう} (headwind/adversity)
- **Noun (1)**: {過|あやま}ち (mistake/wrongdoing)

Notable features:
- Multi-sense entries: {逆風|ぎゃくふう} (2: headwind + adversity), {造形|ぞうけい} (2: modeling + plastic arts), {道標|みちしるべ} (2: signpost + guide), {道筋|みちすじ} (2: route + course of action)
- Transportation: {運行|うんこう}, {遠回|とおまわ}り, {送|おく}り{迎|むか}え, {連結|れんけつ}
- Business/formal: {転載|てんさい}, {進出|しんしゅつ}, {連結|れんけつ}, {請|う}け{負|お}う, {買取|かいとり}
- Daily life: {通話|つうわ}, {詰|つ}め{物|もの}, {適量|てきりょう}, {週刊|しゅうかん}
- New kanji: 2,468 → 2,470 ({諌|かん}, {逝|せい})

Total entries: 14,414 → 14,444 (approximate)
Remaining candidates: 5,355 → 5,325 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
