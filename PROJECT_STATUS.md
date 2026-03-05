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
| Total entries | ~15,224 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~12,425 (open) |
| Candidate words | ~4,546 |
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

### 2026-03-05 (Vocabulary Expansion - 30 New Entries, Session 376)
Added 30 new dictionary entries (IDs 15049-15078) from candidate_words.json:

- **Nouns (14)**: {綴|つづ}り (spelling), {用件|ようけん} (business/matter), {鉢植|はちう}え (potted plant), {下地|したじ} (groundwork/base coat), {幹線|かんせん} (main line), {爆音|ばくおん} (roar/blast), {原色|げんしょく} (primary color), {来歴|らいれき} (history/provenance), {振替休日|ふりかえきゅうじつ} (substitute holiday), {救急|きゅうきゅう} (emergency), {首飾|くびかざ}り (necklace), {腕輪|うでわ} (bracelet), {倍率|ばいりつ} (magnification/competitive ratio), {個展|こてん} (solo exhibition)
- **Noun/verb-suru (7)**: {没入|ぼつにゅう} (immersion), {燃焼|ねんしょう} (combustion), {補修|ほしゅう} (repair), {近代化|きんだいか} (modernization), {読解|どっかい} (reading comprehension), {聴解|ちょうかい} (listening comprehension), {粘着|ねんちゃく} (adhesion)
- **Na-adjectives (3)**: {綿密|めんみつ} (meticulous), {不遜|ふそん} (arrogant), {具|ぐ}だくさん (full of ingredients)
- **No-adjective (1)**: {泥|どろ}だらけ (covered in mud)
- **Noun/verb-suru (art) (1)**: {彩色|さいしき} (coloring/painting)
- **Godan verbs (3)**: {立|た}ち{直|なお}る (to recover), {響|ひび}き{渡|わた}る (to echo), {摘|つ}み{取|と}る (to pluck)
- **Ichidan verb (1)**: {追|お}い{上|あ}げる (to gain on)

Notable features:
- Multi-sense entries: {綴|つづ}り (2: spelling + bound pages), {燃焼|ねんしょう} (2: combustion + energy burning), {下地|したじ} (2: groundwork + base coat), {原色|げんしょく} (2: primary color + vivid color), {粘着|ねんちゃく} (2: adhesion + obsessive clinging), {倍率|ばいりつ} (2: magnification + competitive ratio), {摘|つ}み{取|と}る (2: pluck + nip in the bud)
- Education pair: {読解|どっかい}/{聴解|ちょうかい} (reading/listening comprehension)
- Accessories: {首飾|くびかざ}り, {腕輪|うでわ}
- Daily life: {鉢植|はちう}え, {具|ぐ}だくさん, {泥|どろ}だらけ, {救急|きゅうきゅう}, {振替休日|ふりかえきゅうじつ}
- Compound verbs: {立|た}ち{直|なお}る, {響|ひび}き{渡|わた}る, {追|お}い{上|あ}げる, {摘|つ}み{取|と}る

Total entries: 15,104 → 15,134 (approximate)
Remaining candidates: 4,666 → 4,636 (30 removed)

### 2026-03-05 (Vocabulary Expansion - 30 New Entries, Session 375)
Added 30 new dictionary entries (IDs 15019-15048) from candidate_words.json:

- **Nouns (16)**: {雑学|ざつがく} (trivia), {目頭|めがしら} (inner corner of eye), {発作|ほっさ} (attack/fit), {堪忍袋|かんにんぶくろ} (patience), {反動|はんどう} (recoil/backlash), {上流|じょうりゅう} (upstream/upper class), {下流|かりゅう} (downstream/lower class), {段位|だんい} (dan rank), {裏方|うらかた} (behind-the-scenes), {口数|くちかず} (talkativeness), {帳消|ちょうけ}し (cancellation), {沿線|えんせん} (along a railway line), {容疑者|ようぎしゃ} (suspect), {裏声|うらごえ} (falsetto), {直射日光|ちょくしゃにっこう} (direct sunlight), まつ{毛|げ} (eyelash)
- **Noun/verb-suru (5)**: {激励|げきれい} (encouragement), {合法|ごうほう} (legal), {独|ひと}り{占|じ}め (monopolizing), {殺到|さっとう} (rush/flood), {噴射|ふんしゃ} (jet/spray)
- **Noun/na-adj (1)**: {無礼|ぶれい} (rude)
- **Godan verbs (3)**: {呻|うめ}く (to groan), {着飾|きかざ}る (to dress up), {断|た}ち{切|き}る (to sever)
- **Adverbs (2)**: {当分|とうぶん} (for the time being), {一挙|いっきょ}に (all at once)
- **Noun (linguistics) (2)**: {送|おく}り{仮名|がな} (okurigana), {号泣|ごうきゅう} (wailing)
- **Noun (water) (1)**: {給水|きゅうすい} (water supply)

Notable features:
- Multi-sense entries: {呻|うめ}く (2: pain + frustration), {発作|ほっさ} (2: medical + emotional), {上流|じょうりゅう} (2: river + social class), {下流|かりゅう} (2: river + social class), {反動|はんどう} (2: rebound + political), {断|た}ち{切|き}る (2: physical + figurative)
- Paired entries: {上流|じょうりゅう}/{下流|かりゅう} (upstream/downstream, upper/lower class)
- Body/emotion: {目頭|めがしら}, まつ{毛|げ}, {号泣|ごうきゅう}, {堪忍袋|かんにんぶくろ}
- Daily life: {裏方|うらかた}, {沿線|えんせん}, {直射日光|ちょくしゃにっこう}, {給水|きゅうすい}
- Legal/news: {容疑者|ようぎしゃ}, {合法|ごうほう}, {殺到|さっとう}
- Culture: {段位|だんい}, {送|おく}り{仮名|がな}
- New kanji: 2,499 → 2,500 ({呻|うめ}く)

Total entries: 15,074 → 15,104 (approximate)
Remaining candidates: 4,696 → 4,666 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
