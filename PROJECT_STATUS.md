# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-05
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
| Total entries | ~15,284 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~12,485 (open) |
| Candidate words | ~4,487 |
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

### 2026-03-05 (Vocabulary Expansion - 30 New Entries, Session 381)
Added 30 new dictionary entries (IDs 15199-15228) from candidate_words.json:

- **Nouns (15)**: {関取|せきとり} (ranked sumo wrestler), {飾|かざ}り{気|け} (affectation), {総理大臣|そうりだいじん} (Prime Minister), {総意|そうい} (consensus), {人肌|ひとはだ} (body warmth), {私物|しぶつ} (personal belongings), {領事|りょうじ} (consul), {提案書|ていあんしょ} (written proposal), {装飾品|そうしょくひん} (ornaments), {軍艦巻|ぐんかんま}き (battleship roll sushi), お{造|つく}り (sashimi), {炙|あぶ}り (seared food), {低空|ていくう} (low altitude), 校長室 (principal's office), すりこぎ (wooden pestle)
- **Na-adjectives (3)**: {国民的|こくみんてき} (nationally popular), {粗暴|そぼう} (rough/violent), {痛切|つうせつ} (keen/acute)
- **Godan verbs (2)**: {引|ひ}き{締|し}まる (to tighten), {着崩|きくず}す (to wear casually)
- **Suru verb (1)**: {失礼|しつれい}する (to excuse oneself)
- **Nouns (more) (6)**: {刑法|けいほう} (criminal law), {閑職|かんしょく} (dead-end position), {議決|ぎけつ} (resolution/vote), {対抗策|たいこうさく} (countermeasure), {強国|きょうこく} (powerful nation), {持|も}ち{株|かぶ} (shareholdings)
- **Nouns (abstract) (1)**: {具現化|ぐげんか} (embodiment)
- **Expressions (1)**: {口|くち}を{滑|すべ}らす (to let something slip)
- **Nouns (construction) (1)**: {架橋|かきょう} (bridge building)

Notable features:
- Multi-sense entries: {引|ひ}き{締|し}まる (2: physical + mental), {失礼|しつれい}する (2: leave-taking + being rude), {架橋|かきょう} (2: literal + figurative), {低空|ていくう} (figurative usage: barely scraping by)
- Food/culture: {軍艦巻|ぐんかんま}き, お{造|つく}り, {炙|あぶ}り, すりこぎ, {関取|せきとり}
- Business/politics: {総理大臣|そうりだいじん}, {議決|ぎけつ}, {持|も}ち{株|かぶ}, {対抗策|たいこうさく}, {提案書|ていあんしょ}
- Daily life: {私物|しぶつ}, {校長室|こうちょうしつ}, {口|くち}を{滑|すべ}らす, {着崩|きくず}す

Total entries: 15,254 → 15,284 (approximate)
Remaining candidates: 4,517 → 4,487 (30 removed)

### 2026-03-05 (Vocabulary Expansion - 30 New Entries, Session 380)
Added 30 new dictionary entries (IDs 15169-15198) from candidate_words.json:

- **Nouns (18)**: {香味野菜|こうみやさい} (aromatic vegetables), {霧吹|きりふ}き (spray bottle), {惚気話|のろけばなし} (love-boasting), {独占欲|どくせんよく} (possessiveness), {志望者|しぼうしゃ} (applicant), {教職員|きょうしょくいん} (teaching staff), {議席|ぎせき} (parliamentary seat), {洗濯洗剤|せんたくせんざい} (laundry detergent), {蕁麻疹|じんましん} (hives), {数倍|すうばい} (several times), {一輪車|いちりんしゃ} (unicycle/wheelbarrow), {番付|ばんづけ} (rankings), {面倒|めんどう}くさがり (lazy person), {常識外|じょうしきはず}れ (lacking common sense), {余暇|よか} (leisure time), {推薦状|すいせんじょう} (recommendation letter), {政界|せいかい} (political world), {対抗心|たいこうしん} (competitive spirit)
- **Noun/verb-suru (3)**: {路駐|ろちゅう} (street parking), {懐柔|かいじゅう} (winning over), {付随|ふずい} (accompanying)
- **Na-adjective (1)**: {過敏|かびん} (hypersensitive)
- **Nouns (medical) (1)**: {拒絶反応|きょぜつはんのう} (rejection reaction)
- **Expressions (2)**: {度|ど}を{越|こ}す (to go too far), {予期|よき}せぬ (unexpected)
- **Godan verbs (2)**: {潜|もぐ}り{込|こ}む (to slip into), {上|あ}がり{込|こ}む (to enter someone's house)
- **Adverbs (2)**: {頻繁|ひんぱん}に (frequently), オタク (otaku/geek)

Notable features:
- Multi-sense entries: {拒絶反応|きょぜつはんのう} (2: medical + figurative), {一輪車|いちりんしゃ} (2: unicycle + wheelbarrow), {潜|もぐ}り{込|こ}む (2: physical + figurative), {番付|ばんづけ} (2: sumo + general)
- Medical: {蕁麻疹|じんましん}, {過敏|かびん}, {拒絶反応|きょぜつはんのう}
- Daily life: {洗濯洗剤|せんたくせんざい}, {霧吹|きりふ}き, {路駐|ろちゅう}, {一輪車|いちりんしゃ}
- Culture/society: オタク, {番付|ばんづけ}, {政界|せいかい}, {議席|ぎせき}
- Relationships: {独占欲|どくせんよく}, {惚気話|のろけばなし}
- New kanji: 2,501 → 2,502 ({蕁|じん})

Total entries: 15,224 → 15,254 (approximate)
Remaining candidates: 4,546 → 4,517 (29 removed)

### 2026-03-05 (Vocabulary Expansion - 30 New Entries, Session 379)
Added 30 new dictionary entries (IDs 15139-15168) from candidate_words.json:

- **Expressions (4)**: ひょっとすると (perhaps), なんていうか (how should I put it), {恐縮|きょうしゅく}ですが (excuse me but), {知|し}らん (don't know — casual)
- **Nouns (14)**: {本人|ほんにん}{確認|かくにん} (identity verification), {月|つき}{初|はじ}め (start of month), {貸借|たいしゃく} (lending/borrowing), {昇降|しょうこう} (ascending/descending), {一文|いちぶん} (single sentence), {破|やぶ}れ{目|め} (tear/rip), {現品|げんぴん} (actual item), {進行形|しんこうけい} (progressive form), ご{機嫌|きげん}{取|と}り (flattery), {三度|さんど} (three times), {諸経費|しょけいひ} (miscellaneous expenses), {米飯|べいはん} (cooked rice), {参議院|さんぎいん} (House of Councillors), {既卒|きそつ} (previous graduate)
- **Nouns (more) (7)**: {上|のぼ}り{下|くだ}り (ups and downs), {遠泳|えんえい} (long-distance swimming), {芸風|げいふう} (artistic style), {月頭|げっとう} (beginning of month), {不純物|ふじゅんぶつ} (impurities), {皆殺|みなごろ}し (massacre), {雑居|ざっきょ} (mixed tenancy)
- **Nouns (science) (1)**: ろ{過|か} (filtration)
- **Adverbs/time (2)**: {目標|もくひょう}{達成|たっせい} (goal achievement), {毎夕|まいゆう} (every evening)
- **Verbs (2)**: きょろつく (to look around — godan), {眠|ねむ}れる (to be able to sleep — ichidan)

Notable features:
- Multi-sense entries: {上|のぼ}り{下|くだ}り (2: physical + figurative), {現品|げんぴん} (2: actual item + display stock), {進行形|しんこうけい} (2: grammar + ongoing), {知|し}らん (2: don't know + don't care), {眠|ねむ}れる (2: potential + attributive), {三度|さんど} (2: three times + three degrees)
- Business: {本人|ほんにん}{確認|かくにん}, {貸借|たいしゃく}, {諸経費|しょけいひ}, {月頭|げっとう}, {既卒|きそつ}, {目標|もくひょう}{達成|たっせい}
- Polite expressions: {恐縮|きょうしゅく}ですが, ひょっとすると
- Science: {不純物|ふじゅんぶつ}, ろ{過|か}

Total entries: 15,194 → 15,224 (approximate)
Remaining candidates: 4,576 → 4,546 (30 removed)

### 2026-03-05 (Vocabulary Expansion - 30 New Entries, Session 378)
Added 30 new dictionary entries (IDs 15109-15138) from candidate_words.json:

- **Na-adjectives (4)**: {強烈|きょうれつ} (intense), {不注意|ふちゅうい} (careless), {格安|かくやす} (bargain), {身軽|みがる} (agile/unburdened)
- **Nouns (15)**: {竹林|ちくりん} (bamboo grove), {私生活|しせいかつ} (private life), {法廷|ほうてい} (courtroom), {食物繊維|しょくもつせんい} (dietary fiber), {遊戯|ゆうぎ} (game), {溶液|ようえき} (solution), {荘園|しょうえん} (manor), {偉人|いじん} (great person), {失態|しったい} (blunder), {余談|よだん} (digression), {郷土料理|きょうどりょうり} (local cuisine), {老後|ろうご} (old age), {末|すえ}っ{子|こ} (youngest child), {一軒家|いっけんや} (detached house), {密度|みつど} (density)
- **Noun/verb-suru (4)**: {欠乏|けつぼう} (deficiency), {降参|こうさん} (surrender), {食|た}べ{歩|ある}き (food tour), {粗探|あらさが}し (fault-finding)
- **Na-adj/noun (1)**: {小刻|こきざ}み (in small increments)
- **Noun/suffix (1)**: {類|るい} (kind/type)
- **Verbs (2)**: {忍|しの}び{寄|よ}る (to creep up — godan), {見惚|みと}れる (to gaze admiringly — ichidan)
- **Noun (go/strategy) (1)**: {布石|ふせき} (preparatory step)
- **Expression (1)**: {一理|いちり}ある (to have a point)
- **Noun (immigration) (1)**: {永住|えいじゅう} (permanent residence)

Notable features:
- Multi-sense entries: {食|た}べ{歩|ある}き (2), {身軽|みがる} (2), {密度|みつど} (2), {布石|ふせき} (2)
- Daily life: {格安|かくやす}, {私生活|しせいかつ}, {老後|ろうご}, {末|すえ}っ{子|こ}, {一軒家|いっけんや}
- Culture/food: {郷土料理|きょうどりょうり}, {食物繊維|しょくもつせんい}, {竹林|ちくりん}, {食|た}べ{歩|ある}き
- Academic: {溶液|ようえき}, {密度|みつど}, {荘園|しょうえん}

Total entries: 15,164 → 15,194 (approximate)
Remaining candidates: 4,606 → 4,576 (30 removed)

### 2026-03-05 (Vocabulary Expansion - 30 New Entries, Session 377)
Added 30 new dictionary entries (IDs 15079-15108) from candidate_words.json:

- **Nouns (16)**: シアター (theater), スタンダード (standard), コレステロール (cholesterol), プレイヤー (player), ミーム (meme), {結末|けつまつ} (ending), {唸|うな}り{声|ごえ} (groan/growl), {飲食店|いんしょくてん} (restaurant), {芸能界|げいのうかい} (show business), {衣食住|いしょくじゅう} (basic necessities), {講演会|こうえんかい} (lecture meeting), {選挙区|せんきょく} (electoral district), {子宝|こだから} (gift of children), {食通|しょくつう} (gourmet), {駐輪|ちゅうりん} (bicycle parking), {小麦色|こむぎいろ} (golden-brown/tanned)
- **Nouns (other) (5)**: モラトリアム (moratorium), フェミニスト (feminist), {世辞|せじ} (flattery), {舞妓|まいこ} (apprentice geisha), {現行犯|げんこうはん} (caught in the act)
- **Na-adjectives (3)**: {冷酷|れいこく} (cruel), {丹念|たんねん} (painstaking), {伝統芸能|でんとうげいのう} (traditional performing arts)
- **Expressions/compounds (3)**: {厄介払|やっかいばら}い (good riddance), {手持|ても}ち{無沙汰|ぶさた} (having nothing to do), {右肩上|みぎかたあ}がり (steadily rising)
- **Verb (1)**: {勇気|ゆうき}づける (to encourage)
- **Adjective-i (1)**: {礼儀正|れいぎただ}しい (polite/well-mannered)
- **Adjective-taru (1)**: {微々|びび}たる (slight/insignificant)

Notable features:
- Multi-sense entries: プレイヤー (2: person + device), モラトリアム (2: suspension + identity exploration), フェミニスト (2: rights advocate + chivalrous man)
- Katakana loanwords: シアター, スタンダード, コレステロール, プレイヤー, モラトリアム, ミーム, フェミニスト
- Culture: {舞妓|まいこ}, {伝統芸能|でんとうげいのう}, {芸能界|げいのうかい}
- Daily life: {飲食店|いんしょくてん}, {駐輪|ちゅうりん}, {衣食住|いしょくじゅう}, {小麦色|こむぎいろ}
- New kanji: 2,500 → 2,501 ({妓|ぎ})

Total entries: 15,134 → 15,164 (approximate)
Remaining candidates: 4,636 → 4,606 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
