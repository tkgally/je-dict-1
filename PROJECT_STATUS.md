# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-16
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
| Total entries | ~17,174 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~14,375 (open) |
| Candidate words | ~2,605 |
| Cross-references | ~3,400 |
| Example sentences | ~50,000 |
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

### 2026-03-16 (Vocabulary Expansion - 35 New Entries, Session 439)
Added 35 new dictionary entries (IDs 17091-17125) from candidate_words.json:

- **Nouns (22)**: {責務|せきむ} (duty), {清算|せいさん} (settlement), {全焼|ぜんしょう} (total fire), {証券|しょうけん} (securities), {北米|ほくべい} (North America), {面接官|めんせつかん} (interviewer), {対岸|たいがん} (opposite shore), {片面|かためん} (one side), {蓮華|れんげ} (soup spoon/lotus), {燃|も}えるゴミ (burnable garbage), {尊敬語|そんけいご} (honorific language), {頻出|ひんしゅつ} (frequent occurrence), {危篤|きとく} (critical condition), {販促|はんそく} (sales promotion), {健忘|けんぼう} (forgetfulness), {酒造|しゅぞう} (sake brewing), {私学|しがく} (private school), {救援物資|きゅうえんぶっし} (relief supplies), {許容量|きょようりょう} (tolerance), {絶世|ぜっせい} (peerless), {義理|ぎり}の{父|ちち} (father-in-law), {仕事|しごと}{中毒|ちゅうどく} (workaholic)
- **Adjective (1)**: {素早|すばや}い (quick)
- **Verbs (5)**: {泡立|あわだ}つ (to foam), {連|つ}れ{出|だ}す (to take out), {抑制|よくせい}する (to suppress), {圧倒|あっとう}する (to overwhelm), {乗馬|じょうば} (horse riding)
- **Adverb (1)**: {一年中|いちねんじゅう} (all year round)
- **Nouns (4)**: {成人病|せいじんびょう} (lifestyle disease), {官公庁|かんこうちょう} (government offices), {婚約者|こんやくしゃ} (fiancé), {自問自答|じもんじとう} (self-questioning)
- **Expression (1)**: {耳|みみ}にする (to hear)
- **Compound noun (1)**: {売|う}り{出|だ}し (bargain sale/debut)

Notable features:
- Daily life: {燃|も}えるゴミ, {蓮華|れんげ}, {片面|かためん}, {売|う}り{出|だ}し
- Business/finance: {証券|しょうけん}, {販促|はんそく}, {清算|せいさん}, {面接官|めんせつかん}
- Language/education: {尊敬語|そんけいご}, {頻出|ひんしゅつ}, {私学|しがく}
- Medical: {危篤|きとく}, {健忘|けんぼう}, {成人病|せいじんびょう}
- Family: {義理|ぎり}の{父|ちち}, {婚約者|こんやくしゃ}

Total entries: ~17,139 → ~17,174 (approximate)
Remaining candidates: ~2,640 → ~2,605 (35 removed)

### 2026-03-15 (Vocabulary Expansion - 35 New Entries, Session 438)
Added 35 new dictionary entries (IDs 17056-17090) from candidate_words.json:

- **Nouns (23)**: {事務局|じむきょく} (secretariat), お{酌|しゃく} (serving alcohol), {体|からだ}つき (body build), {僻地|へきち} (remote area), {引数|ひきすう} (argument/parameter), {近畿|きんき} (Kinki region), {資金調達|しきんちょうたつ} (fundraising), {再開発|さいかいはつ} (redevelopment), {給与明細|きゅうよめいさい} (pay stub), {定例会|ていれいかい} (regular meeting), {団体客|だんたいきゃく} (group tourists), {道路工事|どうろこうじ} (road work), {懸念事項|けねんじこう} (matters of concern), {歩数計|ほすうけい} (pedometer), {全巻|ぜんかん} (complete set), {判断材料|はんだんざいりょう} (basis for judgment), {寄稿|きこう} (article contribution), {来襲|らいしゅう} (raid), {凶行|きょうこう} (violent act), {代入|だいにゅう} (assignment), {休止|きゅうし} (suspension), {所有権|しょゆうけん} (ownership), {市街地|しがいち} (urban area), {最新鋭|さいしんえい} (state-of-the-art), {支持率|しじりつ} (approval rating), {不測|ふそく}の{事態|じたい} (unforeseen circumstances)
- **Adjective (2)**: {無情|むじょう} (heartless), {説教臭|せっきょうくさ}い (preachy)
- **Verbs (2)**: {酌|く}み{交|か}わす (to exchange cups), {遅|おく}らす (to delay)
- **Adverb (1)**: {追|お}って (later, in due course)
- **Suffix (1)**: {御中|おんちゅう} (addressed to organization)
- **Other (4)**: {荷下|にお}ろし (unloading), {割増|わりまし} (surcharge), {農具|のうぐ} (farming tool)

Notable features:
- Business/work: {事務局|じむきょく}, {資金調達|しきんちょうたつ}, {給与明細|きゅうよめいさい}, {定例会|ていれいかい}, {懸念事項|けねんじこう}, {割増|わりまし}
- Politics/news: {支持率|しじりつ}, {凶行|きょうこう}, {来襲|らいしゅう}, {不測|ふそく}の{事態|じたい}
- Technical: {引数|ひきすう}, {代入|だいにゅう}, {最新鋭|さいしんえい}
- Culture: お{酌|しゃく}, {酌|く}み{交|か}わす, {近畿|きんき}, {御中|おんちゅう}
- New kanji: 2,553 → 2,555 ({僻|へき}, {畿|き})

Total entries: ~17,104 → ~17,139 (approximate)
Remaining candidates: ~2,675 → ~2,640 (35 removed)

### 2026-03-15 (Vocabulary Expansion - 35 New Entries, Session 437)
Added 35 new dictionary entries (IDs 17021-17055) from candidate_words.json:

- **Nouns (30)**: {権力者|けんりょくしゃ} (powerful person), {完全予約制|かんぜんよやくせい} (by appointment only), {発車|はっしゃ}メロディ (departure melody), {点字|てんじ}ブロック (tactile paving), リボ{払|ばら}い (revolving payment), {一括購入|いっかつこうにゅう} (bulk purchase), {急勾配|きゅうこうばい} (steep slope), {芝刈|しばか}り{機|き} (lawn mower), {防犯登録|ぼうはんとうろく} (bicycle registration), {清涼飲料水|せいりょういんりょうすい} (soft drink), {不快指数|ふかいしすう} (discomfort index), {脂肪燃焼|しぼうねんしょう} (fat burning), {股関節|こかんせつ} (hip joint), {対面授業|たいめんじゅぎょう} (in-person class), {校友会|こうゆうかい} (alumni association), {注文票|ちゅうもんひょう} (order slip), {有形文化財|ゆうけいぶんかざい} (tangible cultural property), {内容量|ないようりょう} (net content), クレーンゲーム (claw machine), {臨時休業|りんじきゅうぎょう} (temporary closure), {冷凍保存|れいとうほぞん} (frozen storage), {軽作業|けいさぎょう} (light work), {新規参入|しんきさんにゅう} (new market entry), {三角定規|さんかくじょうぎ} (set square), {自給率|じきゅうりつ} (self-sufficiency rate), {言論|げんろん}の{自由|じゆう} (freedom of speech), {技術者|ぎじゅつしゃ} (engineer), {定額制|ていがくせい} (subscription), {取|と}り{皿|ざら} (small plate), {追突|ついとつ} (rear-end collision)
- **Na-adjective (1)**: {流動的|りゅうどうてき} (fluid/unstable)
- **Expression (1)**: せっかくですが (thank you, but...)
- **Noun/suru (1)**: {充満|じゅうまん} (being filled with)
- **Noun with cross-ref (1)**: {責任転嫁|せきにんてんか} (shifting blame)
- **Noun (1)**: {右利|みぎき}き (right-handed)

Notable features:
- Japan-specific: {防犯登録|ぼうはんとうろく}, {発車|はっしゃ}メロディ, {点字|てんじ}ブロック, クレーンゲーム, {完全予約制|かんぜんよやくせい}
- Business/finance: リボ{払|ばら}い, {一括購入|いっかつこうにゅう}, {定額制|ていがくせい}, {新規参入|しんきさんにゅう}
- Daily life: {取|と}り{皿|ざら}, {内容量|ないようりょう}, {臨時休業|りんじきゅうぎょう}, {冷凍保存|れいとうほぞん}
- Politics/society: {権力者|けんりょくしゃ}, {言論|げんろん}の{自由|じゆう}, {自給率|じきゅうりつ}
- New kanji: 2,551 → 2,553 ({勾|こう}, {股|こ})

Total entries: ~17,069 → ~17,104 (approximate)
Remaining candidates: ~2,710 → ~2,675 (35 removed)

### 2026-03-15 (Vocabulary Expansion - 35 New Entries, Session 436)
Added 35 new dictionary entries (IDs 16986-17020) from candidate_words.json:

- **Nouns (16)**: {総合|そうごう} (comprehensive), {箇条書|かじょうが}き (bulleted list), {条件付|じょうけんつ}き (conditional), {助|たす}け{合|あ}い (mutual aid), {読点|とうてん} (comma), {釜飯|かまめし} (pot rice), {粗食|そしょく} (plain food), {襟元|えりもと} (neckline), {語調|ごちょう} (tone of voice), {太鼓判|たいこばん} (seal of approval), ひし{形|がた} (diamond shape), {茶菓子|ちゃがし} (tea cakes), {純金|じゅんきん} (pure gold), {高層|こうそう}ビル (skyscraper), {贅沢品|ぜいたくひん} (luxury item), {同好会|どうこうかい} (hobby club)
- **Nouns/suru (4)**: {漂白|ひょうはく} (bleaching), {占有|せんゆう} (occupancy), {酷使|こくし} (overworking), {繁茂|はんも} (luxuriant growth)
- **Adjectives (3)**: {受動的|じゅどうてき} (passive), {用心深|ようじんぶか}い (cautious), {高機能|こうきのう} (high-performance)
- **Verbs (4)**: {這|は}い{出|だ}す (to crawl out), やって{来|く}る (to come along), {回避|かいひ}する (to avoid), {風車|ふうしゃ} (windmill)
- **Other (8)**: {骨|ほね}を{折|お}る (to take pains), {育|そだ}ちが{良|よ}い (well-bred), {湯桶読|ゆとうよ}み (kun+on reading), {手押|ておし}し{車|ぐるま} (pushcart), {借地|しゃくち} (leased land), {羽音|はおと} (sound of wings), コンタクトレンズ (contact lenses), {変化|へんげ} (shape-shifting)

Notable features:
- Multi-sense: {骨|ほね}を{折|お}る (2: make effort + break bone), {変化|へんげ} (2: transformation + apparition), やって{来|く}る (2: arrive + time/season comes)
- Cross-references: {風車|ふうしゃ} ↔ {風車|かざぐるま}, {変化|へんげ} ↔ {変化|へんか}
- Cultural: {釜飯|かまめし} (station food), {茶菓子|ちゃがし} (tea ceremony), {湯桶読|ゆとうよ}み (kanji reading patterns)
- Linguistics: {読点|とうてん}, {湯桶読|ゆとうよ}み

Total entries: ~17,034 → ~17,069 (approximate)
Remaining candidates: ~2,745 → ~2,710 (35 removed)

### 2026-03-15 (Vocabulary Expansion - 35 New Entries, Session 435)
Added 35 new dictionary entries (IDs 16951-16985) from candidate_words.json:

- **Nouns (16)**: {誘導|ゆうどう} (guidance), {中級|ちゅうきゅう} (intermediate level), {看病|かんびょう} (nursing), {親分|おやぶん} (boss), {抜|ぬ}け{殻|がら} (cast-off skin), {快眠|かいみん} (sound sleep), {派閥|はばつ} (faction), {年頃|としごろ} (marriageable age), {日和|ひより} (weather), {正直者|しょうじきもの} (honest person), {飴玉|あめだま} (hard candy), {愛憎|あいぞう} (love and hate), {平行線|へいこうせん} (parallel lines), {美白|びはく} (skin whitening), {万端|ばんたん} (everything), {一般公開|いっぱんこうかい} (open to public)
- **Nouns/suru (6)**: {軽減|けいげん} (reduction), {補填|ほてん} (compensation), {礼拝|れいはい} (worship), {買|か}い{食|ぐ}い (eating snacks on the go), {完走|かんそう} (finishing a race), {腐心|ふしん} (racking one's brains)
- **Verbs (4)**: {忍|しの}ぶ (to endure/hide), {荒|あ}れ{果|は}てる (to fall into ruin), ぼやける (to become blurry), {上塗|うわぬ}り (topcoat/cover-up)
- **Na-adjectives (2)**: {不吉|ふきつ} (ominous), {簡便|かんべん} (handy)
- **Other (7)**: {更|さら}なる (further), {怠|なま}け{者|もの} (lazy person), {白|しろ}ワイン (white wine), {除夜|じょや}の{鐘|かね} (New Year's Eve bell), {往生際|おうじょうぎわ}が{悪|わる}い (poor loser), {定刻|ていこく} (scheduled time), {重任|じゅうにん} (heavy responsibility)

Notable features:
- Multi-sense: {忍|しの}ぶ (3: endure + conceal + reminisce), {抜|ぬ}け{殻|がら} (2: literal + figurative), {平行線|へいこうせん} (2: geometry + deadlock), {日和|ひより} (2: weather + opportunism), {上塗|うわぬ}り (2: topcoat + cover-up)
- Cultural: {除夜|じょや}の{鐘|かね} (New Year's Eve bell ringing), {抜|ぬ}け{殻|がら} (cicada collecting), {買|か}い{食|ぐ}い (school rules)
- Buddhist: {往生際|おうじょうぎわ}が{悪|わる}い (from Buddhist death concept), {礼拝|れいはい}
- New kanji: 2,550 → 2,551 ({填|てん})

Total entries: ~16,999 → ~17,034 (approximate)
Remaining candidates: ~2,780 → ~2,745 (35 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
