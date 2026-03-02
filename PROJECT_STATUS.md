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
| Total entries | ~14,624 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~11,825 (open) |
| Candidate words | ~5,145 |
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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
