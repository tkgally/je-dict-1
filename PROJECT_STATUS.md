# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-22
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
| Total entries | ~18,318 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~15,519 (open) |
| Candidate words | ~5,848 |
| Cross-references | ~3,400 |
| Example sentences | ~52,000 |
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

### 2026-03-22 (Vocabulary Expansion - 35 New Entries, Session 474)
Added 35 new dictionary entries (IDs 18472-18508) from candidate_words.json.

- **Nouns (17)**: {抱負|ほうふ} (aspiration), {台車|だいしゃ} (hand cart), {健康保険|けんこうほけん} (health insurance), {営業時間|えいぎょうじかん} (business hours), お{猪口|ちょこ} (sake cup), {暖炉|だんろ} (fireplace), {財宝|ざいほう} (treasure), {予防策|よぼうさく} (preventive measure), {取|と}り{換|か}え (replacement), {飼|か}い{猫|ねこ} (pet cat), {商社|しょうしゃ} (trading company), {首都圏|しゅとけん} (Tokyo metro area), {潮干狩|しおひが}り (clamming), {出張所|しゅっちょうじょ} (branch office), {代理人|だいりにん} (agent/proxy), {中辛|ちゅうから} (medium-spicy), {水揚|みずあ}げ (fish landing/sales)
- **Nouns/Suru verbs (7)**: {着席|ちゃくせき} (taking a seat), {飲酒運転|いんしゅうんてん} (drunk driving), {命中|めいちゅう} (direct hit), {即決|そっけつ} (snap decision), {模造|もぞう} (imitation), {放流|ほうりゅう} (release/discharge), {二転三転|にてんさんてん} (changing repeatedly)
- **Na-adjectives (3)**: {悲痛|ひつう} (grief-stricken), {必然的|ひつぜんてき} (inevitable), {誇|ほこ}らしげ (proud-looking)
- **Verbs (2)**: まぶす (to coat), {群|む}れる (to flock)
- **Adjective (1)**: {得難|えがた}い (hard to come by)
- **Expression (1)**: {気|き}が{進|すす}まない (reluctant)
- **Noun/Adj (2)**: {最良|さいりょう} (the best), {失策|しっさく} (blunder/error)
- **Four-character idiom (2)**: {一攫千金|いっかくせんきん} (striking it rich), {他力本願|たりきほんがん} (relying on others)
- **Noun/Suru verb (1)**: {推奨|すいしょう} (recommendation)

Notable features:
- Daily life: {営業時間|えいぎょうじかん}, {健康保険|けんこうほけん}, {台車|だいしゃ}, {暖炉|だんろ}, {飼|か}い{猫|ねこ}, {中辛|ちゅうから}
- Culture: お{猪口|ちょこ}, {潮干狩|しおひが}り, {他力本願|たりきほんがん}
- Business: {商社|しょうしゃ}, {代理人|だいりにん}, {出張所|しゅっちょうじょ}
- Four-character idioms: {一攫千金|いっかくせんきん}, {他力本願|たりきほんがん}, {二転三転|にてんさんてん}
- Removed 2 duplicate candidates ({推奨|すいしょう}, {雑|ざつ} — already existed as entries)

Total entries: ~18,283 → ~18,318 (approximate)
Remaining candidates: ~5,883 → ~5,848 (35 removed)

### 2026-03-22 (Vocabulary Expansion - 35 New Entries, Session 473)
Added 35 new dictionary entries (IDs 18437-18471) from candidate_words.json.

- **Nouns (24)**: {文庫|ぶんこ} (paperback), {異世界|いせかい} (another world), {三|み}つ{編|あ}み (braid), {礼服|れいふく} (formal wear), {精神疾患|せいしんしっかん} (mental illness), {論評|ろんぴょう} (criticism), {役|やく}どころ (role), {引|ひ}き{立|た}て{役|やく} (foil), {長期保存|ちょうきほぞん} (long-term storage), {念珠|ねんじゅ} (prayer beads), {司令部|しれいぶ} (headquarters), {歳時記|さいじき} (saijiki), {万雷|ばんらい} (thunderous), {類人猿|るいじんえん} (great ape), {霊長類|れいちょうるい} (primates), {若造|わかぞう} (youngster), {水洗|すいせん}トイレ (flush toilet), {車夫|しゃふ} (rickshaw puller), {股下|またした} (inseam), {言|い}い{付|つ}け (order/tattling), {取|と}り{消|け}し{線|せん} (strikethrough), {鍵盤楽器|けんばんがっき} (keyboard instrument), {円座|えんざ} (round cushion), {英才教育|えいさいきょういく} (gifted education)
- **Nouns/Other (5)**: {未開|みかい} (undeveloped), {不実|ふじつ} (faithlessness), {目出|めだ}し{帽|ぼう} (balaclava), {喚声|かんせい} (shout), {頓服|とんぷく} (as-needed medicine)
- **Adverb (1)**: {判然|はんぜん} (clearly)
- **Pronoun (1)**: {貴様|きさま} (you, rude)
- **Interjection (1)**: ちくしょう (damn it)
- **Expression (1)**: {熱|ねつ}を{帯|お}びる (to get heated)
- **Traditional month name (1)**: {文月|ふづき} (July)
- **Suru verb (1)**: {妥結|だけつ} (settlement)

Notable features:
- Culture: {歳時記|さいじき}, {文月|ふづき}, {念珠|ねんじゅ}, {車夫|しゃふ}, {円座|えんざ}
- Modern culture: {異世界|いせかい}, {文庫|ぶんこ}
- Medical: {精神疾患|せいしんしっかん}, {頓服|とんぷく}
- Biology: {類人猿|るいじんえん}, {霊長類|れいちょうるい}
- Expressive vocabulary: ちくしょう, {貴様|きさま}, {若造|わかぞう}
- Removed 1 stale candidate ({蛞蝓|なめくじ} — kanji variant of existing なめくじ entry)

Total entries: ~18,248 → ~18,283 (approximate)
Remaining candidates: ~5,919 → ~5,883 (35 removed as entries + 1 stale removed)

### 2026-03-22 (Vocabulary Expansion - 35 New Entries, Session 472)
Added 35 new dictionary entries (IDs 18402-18436) from candidate_words.json.

- **Nouns (22)**: {山小屋|やまごや} (mountain hut), {手提|てさ}げ (handbag), {子音|しいん} (consonant), {採光|さいこう} (natural lighting), {弦|げん} (string), {労苦|ろうく} (hardship), {滋養|じよう} (nourishment), {用量|ようりょう} (dosage), {処理能力|しょりのうりょく} (processing power), {汚染物質|おせんぶっしつ} (pollutant), {日除|ひよ}け (sunshade), {地表|ちひょう} (earth's surface), なめくじ (slug), {当|あ}てこすり (insinuation), {秒刻|びょうきざ}み (second by second), {野兎|のうさぎ} (hare), どんちゃん{騒|さわ}ぎ (revelry), スラックス (slacks), {執行猶予|しっこうゆうよ} (suspended sentence), {貧困層|ひんこんそう} (the poor), {発信源|はっしんげん} (source of information), {学|がく}ラン (school uniform)
- **Nouns/Suru verbs (3)**: {残留|ざんりゅう} (remaining), {初公開|はつこうかい} (first showing), {接吻|せっぷん} (kiss)
- **Na-adjectives/Nouns (3)**: {別個|べっこ} (separate), {未発達|みはったつ} (undeveloped), {不協和|ふきょうわ} (dissonance)
- **Adjective (1)**: {珍奇|ちんき} (rare and curious)
- **Adverbs/Other (2)**: {何|なん}らか (some kind of), {腹一杯|はらいっぱい} (bellyful)
- **Expressions (4)**: {耳|みみ}に{付|つ}く (to stick in one's ears), {義妹|ぎまい} (sister-in-law), {濡|ぬ}れ{衣|ぎぬ}を{着|き}せる (to frame someone)

Notable features:
- Daily life: {山小屋|やまごや}, {手提|てさ}げ, {日除|ひよ}け, スラックス, {学|がく}ラン
- Medical/Science: {用量|ようりょう}, {汚染物質|おせんぶっしつ}, {子音|しいん}, {地表|ちひょう}
- Legal/News: {執行猶予|しっこうゆうよ}, {貧困層|ひんこんそう}, {残留|ざんりゅう}
- Expressions/Idioms: {濡|ぬ}れ{衣|ぎぬ}を{着|き}せる, {耳|みみ}に{付|つ}く, {当|あ}てこすり
- New kanji added: 吻 (ID 02578), 滋 (ID 02579)
- Removed 2 stale candidates (duplicates: {客観的|きゃっかんてき}, {個人的|こじんてき})

Total entries: ~18,213 → ~18,248 (approximate)
Remaining candidates: ~5,955 → ~5,919 (34 removed as entries + 2 stale removed)

### 2026-03-21 (Vocabulary Expansion - 35 New Entries, Session 471)
Added 35 new dictionary entries (IDs 18367-18401) from candidate_words.json.

- **Grammar suffixes (6)**: ～やすい (easy to), ～づらい (hard to), ～{終|お}わる (to finish doing), ～{始|はじ}める (to start doing), ～{直|なお}す (to do over), ～だらけ (covered in)
- **Expressions/idioms (10)**: ～だけでなく (not only), {後手|ごて}に{回|まわ}る (to fall behind), {先手|せんて}を{打|う}つ (to take the initiative), {群|ぐん}を{抜|ぬ}く (to stand out), {注意|ちゅうい}を{払|はら}う (to pay attention), {念頭|ねんとう}に{置|お}く (to keep in mind), {罠|わな}にはまる (to fall into a trap), ご{苦労様|くろうさま} (thank you for your efforts), {俗|ぞく}に{言|い}う (commonly called), などなど (etcetera)
- **Verbs (14)**: {寝過|ねす}ごす (to oversleep), {没頭|ぼっとう}する (to be absorbed in), {号泣|ごうきゅう}する (to wail), {誘発|ゆうはつ}する (to trigger), {交|まじ}わる (to cross), {噛|か}み{砕|くだ}く (to crunch/simplify), {立|た}てこもる (to barricade), {放|ほう}っておく (to leave alone), {据|す}え{置|お}く (to keep unchanged), {熟|じゅく}す (to ripen), じゃれ{合|あ}う (to frolic), {乗|じょう}ずる (to take advantage), がっつく (to devour), {勝|か}ち{誇|ほこ}る (to gloat)
- **Nouns (5)**: {難読|なんどく} (hard to read), {登頂|とうちょう} (summiting), {口頭|こうとう}で (orally), {回答|かいとう}する (to reply), {雇|やと}い{止|ど}め (non-renewal of contract)

Notable features:
- Grammar focus: 6 productive verb suffixes (～やすい, ～づらい, ～{終|お}わる, ～{始|はじ}める, ～{直|なお}す, ～だらけ)
- Idiomatic expressions: shogi-derived ({先手|せんて}を{打|う}つ, {後手|ごて}に{回|まわ}る), set phrases ({群|ぐん}を{抜|ぬ}く, {罠|わな}にはまる)
- Colloquial vocabulary: がっつく, などなど, {放|ほう}っておく

Total entries: ~18,178 → ~18,213 (approximate)
Remaining candidates: ~5,988 → ~5,955 (33 removed as entries)

### 2026-03-21 (Vocabulary Expansion - 35 New Entries, Session 470)
Added 35 new dictionary entries (IDs 18332-18366) from candidate_words.json.

- **Nouns (28)**: {護衛艦|ごえいかん} (escort ship), {豪速球|ごうそっきゅう} (blazing fastball), {爵位|しゃくい} (peerage), {胸骨|きょうこつ} (sternum), {深奥|しんおう} (profound depths), {佳人|かじん} (beautiful woman), {阿吽|あうん} (a-un), {指向性|しこうせい} (directivity), {移調|いちょう} (transposition), {副読本|ふくどくほん} (supplementary reader), {基板|きばん} (circuit board), {導体|どうたい} (conductor), {国体|こくたい} (national polity), {発赤|ほっせき} (erythema), {泳力|えいりょく} (swimming ability), {絶対量|ぜったいりょう} (absolute amount), {所有欲|しょゆうよく} (possessiveness), {悪口雑言|あっこうぞうごん} (torrent of insults), {一家離散|いっかりさん} (family breakup), {匍匐前進|ほふくぜんしん} (belly crawl), {徒手空拳|としゅくうけん} (bare-handed), {鱗粉|りんぷん} (wing scales), {開襟|かいきん} (open collar), {銅色|あかがねいろ} (copper color), {床面|ゆかめん} (floor surface), {少佐|しょうさ} (major), {中佐|ちゅうさ} (lieutenant colonel), {加速器|かそくき} (accelerator)
- **Other (7)**: {一個|いっこ}ずつ (one by one), {牌|ぱい} (mahjong tile), {給紙|きゅうし} (paper feed), {排気量|はいきりょう} (engine displacement), {困窮者|こんきゅうしゃ} (the needy), {陣中見舞|じんちゅうみま}い (morale visit), {板|いた}ガム (stick gum)

Notable features:
- Military: {護衛艦|ごえいかん}, {少佐|しょうさ}, {中佐|ちゅうさ}, {匍匐前進|ほふくぜんしん}
- Four-character compounds: {悪口雑言|あっこうぞうごん}, {一家離散|いっかりさん}, {匍匐前進|ほふくぜんしん}, {徒手空拳|としゅくうけん}
- Technical: {基板|きばん}, {導体|どうたい}, {指向性|しこうせい}, {加速器|かそくき}, {排気量|はいきりょう}
- Medical: {胸骨|きょうこつ}, {発赤|ほっせき}
- Literary: {佳人|かじん}, {深奥|しんおう}, {銅色|あかがねいろ}
- New kanji added: 匍 (ID 02576), 匐 (ID 02577)
- Removed 4 stale candidates (duplicates: {太っ腹|ふとっぱら}, {憎|にく}しみ, {小刻|こきざ}みに, {倍返|ばいがえ}し)

Total entries: ~18,143 → ~18,178 (approximate)
Remaining candidates: ~6,026 → ~5,988 (35 removed as entries + 4 stale removed)

Remaining candidates: ~6,062 → ~6,026 (35 removed + 1 stale)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
