# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-17
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
| Total entries | ~19,088 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,289 (open) |
| Candidate words | ~5,472 |
| Cross-references | ~3,400 |
| Example sentences | ~53,200 |
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

### 2026-04-18 (Vocabulary Expansion - 22 New Entries)
Added 22 new dictionary entries (IDs 24382-24403) from candidate_words.json. A varied batch emphasizing formal/literary vocabulary, practical expressions, and useful concepts.

- **Abstract concepts (4)**: {客観|きゃっかん} (objectivity), {隔絶|かくぜつ} (isolation), {残余|ざんよ} (remainder), {劣位|れつい} (inferiority)
- **Expressions (5)**: {話|はなし}を{盛|も}る (to exaggerate), {先延|さきの}ばしにする (to postpone), {先送|さきおく}りにする (to defer), {論|ろん}をまたない (goes without saying), {役|やく}を{演|えん}じる (to play a role)
- **Society / politics (2)**: {人口|じんこう}{減少|げんしょう} (population decline), {共存|きょうそん}{共栄|きょうえい} (coexistence and co-prosperity)
- **Business / finance (2)**: {預金|よきん}{口座|こうざ} (bank account), {契約者|けいやくしゃ} (subscriber)
- **Culture / arts (3)**: {銘|めい} (inscription), {楚々|そそ} (graceful), {無類|むるい} (peerless)
- **Knowledge / description (3)**: {通暁|つうぎょう} (thorough knowledge), {緩徐|かんじょ} (slow/gradual), いかん (depending on)
- **Military / sports (2)**: {堅守|けんしゅ} (firm defense), {起工|きこう} (commencement of construction)
- Also removed 1 stale candidate (取立て, duplicate of existing 取り立て)
- All entries follow v2 standards with structured notes, collocations, similar words, and full furigana

Total entries: 24,180 → 24,202.

### 2026-04-18 (Vocabulary Expansion - 30 New Entries)
Added 30 new dictionary entries (IDs 24352-24381) from candidate_words.json. A varied batch covering language, culture, food, science, transportation, politics, architecture, history, and everyday vocabulary.

- **Language / culture (5)**: {京都弁|きょうとべん} (Kyoto dialect), {大阪弁|おおさかべん} (Osaka dialect), {反意語|はんいご} (antonym), {熟字訓|じゅくじくん} (special kanji reading), {俗|ぞく} (secular/colloquial)
- **Food / cooking (3)**: {食道楽|しょくどうらく} (gourmet), {生乳|せいにゅう} (raw milk), {牛脂|ぎゅうし} (beef tallow)
- **Politics / society (4)**: {閥|ばつ} (faction), {官界|かんかい} (bureaucratic world), {同質化|どうしつか} (homogenization), {皇女|こうじょ} (imperial princess)
- **Transportation (3)**: {航空便|こうくうびん} (airmail), {支線|しせん} (branch line), {接岸|せつがん} (docking)
- **Science (2)**: {電荷|でんか} (electric charge), {外力|がいりょく} (external force)
- **Arts / literature (2)**: {筆致|ひっち} (writing style), {格子窓|こうしまど} (lattice window)
- **Everyday / general (8)**: {不明確|ふめいかく} (unclear), {布切|ぬのき}れ (piece of cloth), {局員|きょくいん} (office staff), {全席|ぜんせき} (all seats), {河岸|かがん} (riverbank), {県人|けんじん} (person from prefecture), {諸所|しょしょ} (various places), {学習書|がくしゅうしょ} (study book)
- **Expressions (3)**: {術中|じゅっちゅう} (trap/scheme), {猛特訓|もうとっくん} (rigorous training), {大奮発|だいふんぱつ} (big splurge)
- Conjugation tables auto-generated for suru-verbs ({同質化|どうしつか}, {接岸|せつがん}, {猛特訓|もうとっくん}, {大奮発|だいふんぱつ})
- All entries follow v2 standards with structured notes, collocations, similar words, and full furigana

Total entries: 24,150 → 24,180.

### 2026-04-18 (Vocabulary Expansion - 30 New Entries)
Added 30 new dictionary entries (IDs 24322-24351) from candidate_words.json. A diverse batch covering politics, business, food culture, society, nature, education, and everyday vocabulary.

- **Business / commerce (5)**: {販売元|はんばいもと} (seller/distributor), {契約先|けいやくさき} (contract partner), {上場企業|じょうじょうきぎょう} (listed company), {転売屋|てんばいや} (scalper), ブランド{化|か} (branding)
- **Society / politics (4)**: {共和国|きょうわこく} (republic), {報道|ほうどう}の{自由|じゆう} (press freedom), {対人恐怖|たいじんきょうふ} (social anxiety), {肉食系|にくしょくけい} (assertive type)
- **Nature / animals (3)**: {蜂|はち}の{巣|す} (beehive), {鳥|とり}の{巣|す} (bird's nest), {巣穴|すあな} (burrow/den)
- **Food / culture (2)**: {黒蜜|くろみつ} (black sugar syrup), {香草|こうそう} (herb)
- **Education (2)**: {法学部|ほうがくぶ} (faculty of law), {補習授業|ほしゅうじゅぎょう} (supplementary lessons)
- **Work / life (2)**: {深夜勤務|しんやきんむ} (night shift), {休|やす}みなし (no days off)
- **Emotion / abstract (3)**: {金銭欲|きんせんよく} (greed for money), {無自覚|むじかく} (lack of self-awareness), {情事|じょうじ} (love affair)
- **General vocabulary (7)**: {最後尾|さいごび} (tail end), {爪痕|つめあと} (scratch mark/aftermath), {再送|さいそう} (resending), {特別版|とくべつばん} (special edition), {逆順|ぎゃくじゅん} (reverse order), {一|ひと}つずつ (one by one), {遥|はる}か{彼方|かなた} (far away)
- **Expression (2)**: {抜|ぬ}け{出|だ}せない (unable to escape), {野|の}いちご (wild strawberry)
- Conjugation tables auto-generated for suru-verbs ({再送|さいそう}, ブランド{化|か})
- All entries follow v2 standards with structured notes, collocations, similar words, and full furigana

Total entries: 24,120 → 24,150.

### 2026-04-18 (Vocabulary Expansion - 30 New Entries)
Added 30 new dictionary entries (IDs 24292-24321) from candidate_words.json. A diverse batch covering general vocabulary, loanwords, body parts, nature, business, medicine, geography, and cultural terms.

- **Business / society (4)**: {管理者|かんりしゃ} (administrator), {協力者|きょうりょくしゃ} (collaborator), {経済界|けいざいかい} (business world), {再調整|さいちょうせい} (readjustment)
- **Nature / plants (2)**: {茂|しげ}み (thicket), {草木|そうもく} (vegetation)
- **Medicine / health (2)**: {鎮静剤|ちんせいざい} (sedative), {粘液|ねんえき} (mucus)
- **Body / appearance (2)**: {首元|くびもと} (neckline), {足指|あしゆび} (toe)
- **Language / writing (2)**: {疑問符|ぎもんふ} (question mark), {言葉遊|ことばあそ}び (wordplay)
- **Fashion / accessories (2)**: {宝飾|ほうしょく} (jewelry), {耳飾|みみかざ}り (earring)
- **Technology / IT (2)**: フォーマット (format), リーダー (leader/reader)
- **Travel / geography (3)**: {遊覧船|ゆうらんせん} (sightseeing boat), {東|ひがし}アジア (East Asia), {海外旅行|かいがいりょこう} (overseas travel)
- **Construction / materials (3)**: {建造物|けんぞうぶつ} (structure), {石材|せきざい} (stone material), {鋳型|いがた} (mold/cast)
- **Household (1)**: {防虫剤|ぼうちゅうざい} (mothball)
- **Abstract / concepts (5)**: {上機嫌|じょうきげん} (good mood), {不確定|ふかくてい} (uncertain), {等身|とうしん} (life-size), {最上位|さいじょうい} (highest rank), {参加型|さんかがた} (participatory)
- **Other (2)**: {端切|はぎ}れ (fabric scrap), {実証実験|じっしょうじっけん} (field trial)
- Conjugation tables auto-generated for suru-verbs (フォーマット, {再調整|さいちょうせい}, {海外旅行|かいがいりょこう})
- All entries follow v2 standards with structured notes, collocations, similar words, and full furigana

Total entries: 24,090 → 24,120.

### 2026-04-18 (Vocabulary Expansion - 30 New Entries)
Added 30 new dictionary entries (IDs 24262-24291) from candidate_words.json. A diverse batch spanning business, culture, nature, education, medicine, arts, and idiomatic expressions.

- **Business / economics (4)**: {金融緩和|きんゆうかんわ} (monetary easing), {商界|しょうかい} (business world), {小社|しょうしゃ} (our company, humble), {営業車|えいぎょうしゃ} (company car)
- **Ceremonies / awards (3)**: {祝典|しゅくてん} (celebration ceremony), {受賞式|じゅしょうしき} (award ceremony), {最優秀賞|さいゆうしゅうしょう} (grand prize)
- **Medicine / health (3)**: {点眼薬|てんがんやく} (eye drops), {外用薬|がいようやく} (external medicine), {軽労働|けいろうどう} (light work)
- **Nature / birds (3)**: {夏鳥|なつどり} (summer bird), {冬鳥|ふゆどり} (winter bird), {山峡|さんきょう} (mountain gorge)
- **Culture / religion (2)**: {春彼岸|はるひがん} (spring equinox period), {秋彼岸|あきひがん} (autumn equinox period)
- **Education (3)**: {副担任|ふくたんにん} (assistant homeroom teacher), {塾長|じゅくちょう} (cram school director), {漢学|かんがく} (Chinese classical studies)
- **Arts / music (2)**: {古典派|こてんは} (classical school), {音響効果|おんきょうこうか} (sound effects)
- **Science / writing (3)**: {有機物|ゆうきぶつ} (organic matter), {字形|じけい} (character shape), {解説書|かいせつしょ} (explanatory book)
- **Society / politics (3)**: {派閥争|はばつあらそ}い (factional strife), ヘイトスピーチ (hate speech), {接触事故|せっしょくじこ} (fender bender)
- **Expressions / idioms (2)**: {会話|かいわ}を{交|か}わす (to exchange conversation), へそを{曲|ま}げる (to sulk)
- **Other (2)**: {淫|みだ}ら (lewd), {一輪|いちりん} (single flower / one wheel)
- 1 new kanji added to index: 淫 (lewd)
- All entries follow v2 standards with structured notes, collocations, similar words, and full furigana

Total entries: 24,060 → 24,090.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








