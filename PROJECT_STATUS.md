# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-15
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

### 2026-04-15 (Vocabulary Expansion - 16 New Entries)
Added 16 new dictionary entries (IDs 23988-24003) from candidate_words.json. A balanced mix of nature, medicine, formal technical vocabulary, food-related loanwords, and one formal suru verb.

- **Nature / biology (3)**: {桑|くわ} (mulberry — historically central to sericulture; introduces new kanji 桑), {白魚|しらうお} (icefish; whitebait — spring seasonal delicacy), {群落|ぐんらく} (plant community; stand — botanical/ecological term)
- **Medical / body (2)**: {神経痛|しんけいつう} (neuralgia; nerve pain), {診療科|しんりょうか} (medical department; clinical specialty)
- **Institution / titles (2)**: {副部長|ふくぶちょう} (deputy department head / vice-captain of a club), {副校長|ふくこうちょう} (vice-principal — formally established in 2007 school law reform)
- **Social / family (2)**: {同性愛|どうせいあい} (same-sex love; homosexuality — neutral reference term), {姻戚|いんせき} (relative by marriage; in-law — formal/legal register)
- **Verb (1)**: {議|ぎ}する (to deliberate formally — verb-suru; full conjugation table)
- **Food / loanwords (3)**: グラニュー{糖|とう} (granulated sugar), クランプ (clamp; general fixture tool), チョコチップ (chocolate chips)
- **Math / technical (3)**: {垂線|すいせん} (perpendicular line — geometry), {冗長性|じょうちょうせい} (redundancy — engineering/IT and writing), {経文|きょうもん} (sutra text — Buddhist ritual and literary)
- **New kanji**: Added 桑 (kanji ID 02686, 'sou/kuwa — mulberry') to support the 桑 entry
- All entries follow v2 standards: progressive-length examples (3+ per sense), structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS sections, full furigana coverage, and sense-number annotations

### 2026-04-15 (Vocabulary Expansion - 12 New Entries)
Added 12 new dictionary entries (IDs 23976-23987) from candidate_words.json. A balanced mix of sports, business/finance, medical/abstract, astronomy, and everyday product vocabulary.

- **Sports / martial arts (3)**: {強打者|きょうだしゃ} (slugger; heavy hitter), {指名打者|しめいだしゃ} (designated hitter), {関節技|かんせつわざ} (joint lock technique)
- **Counter (1)**: {一羽|いちわ} (one bird — counter for birds and, traditionally, rabbits; includes full counting table)
- **Formal / abstract (3)**: {様態|ようたい} (state; condition — two senses: medical and grammatical 'mode'), {顕在的|けんざいてき} (manifest; overt — na-adjective, contrasts with 潜在的), {発足式|ほっそくしき} (inauguration ceremony)
- **Business / finance (1)**: {上場廃止|じょうじょうはいし} (delisting from a stock exchange — also takes する)
- **Everyday product / concrete (2)**: {電動|でんどう}のこぎり (power saw), {乾燥果実|かんそうかじつ} (dried fruit — formal counterpart of ドライフルーツ)
- **Astronomy (1)**: {一等星|いっとうせい} (first-magnitude star)
- **Loanword (1)**: タクト (conductor's baton / leadership — two senses, literal and figurative)
- All entries follow v2 standards: progressive-length examples (3+ per sense), structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS sections, full furigana coverage, and sense-number annotations

### 2026-04-15 (Vocabulary Expansion - 14 New Entries)
Added 14 new dictionary entries (IDs 23962-23975) from candidate_words.json. A mixed set of formal/technical nouns, everyday food and real-estate vocabulary, and one theatrical idiom with literal and figurative senses.

- **Formal / institutional (3)**: {閉会|へいかい} (closing of a meeting; adjournment), {入国|にゅうこく}{管理|かんり} (immigration control), {労働者|ろうどうしゃ} (worker; laborer)
- **Technical / medical (3)**: {吸気|きゅうき} (inhalation; intake air — two senses), {老年期|ろうねんき} (old age; senescence period), {航空母艦|こうくうぼかん} (aircraft carrier)
- **Business / publishing (3)**: {試用|しよう} (trial use), {自費|じひ}{出版|しゅっぱん} (self-publishing), {周辺|しゅうへん}{環境|かんきょう} (surrounding environment)
- **Everyday / food / hobby (3)**: {歯触|はざわ}り (mouthfeel; texture of food), {艶出|つやだ}し (polishing; glossing), {棋譜|きふ} (shogi/go game record)
- **Literature / criticism (1)**: {人物|じんぶつ}{描写|びょうしゃ} (characterization; portrayal of a person)
- **Expression (1)**: {幕|まく}が{上|あ}がる (the curtain rises; to get underway — two senses, literal and figurative)
- All entries follow v2 standards: progressive-length examples (3+ per sense), structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS sections, full furigana coverage, and sense-number annotations

### 2026-04-15 (Vocabulary Expansion - 16 New Entries)
Added 16 new dictionary entries (IDs 23946-23961) from candidate_words.json. A mix of everyday nouns, cosmetics/skincare vocabulary, formal na-adjectives, and a multi-sense grammar expression.

- **General nouns (8)**: {大喝采|だいかっさい} (thunderous applause), {廃材|はいざい} (scrap material), {命名者|めいめいしゃ} (namer), {月替|つきが}わり (monthly rotation), {期間中|きかんちゅう} (during the period), {二重国籍|にじゅうこくせき} (dual citizenship), {外国製|がいこくせい} (foreign-made), ページ{数|すう} (page count)
- **Business / product (1)**: {従来品|じゅうらいひん} (previous model; existing product)
- **Cosmetics / skincare (3)**: グロス (lip gloss / glossy finish — two senses), {脂性肌|しせいはだ} (oily skin), {混合肌|こんごうはだ} (combination skin)
- **Loanword / marking (1)**: マーキング (marking / territorial scent marking — two senses, noun and verb-suru)
- **Na-adjectives (2)**: {防衛的|ぼうえいてき} (defensive), {観念的|かんねんてき} (notional; theoretical — with nuance of being out of touch)
- **Grammar expression (1)**: に{限|かぎ}って (three senses: limiting 'only', unexpected-timing 'of all times', and confident-denial 'of all people')
- All entries follow v2 standards: progressive-length examples (3+ per sense), structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS sections, full furigana coverage, and sense-number annotations

### 2026-04-15 (Vocabulary Expansion - 18 New Entries)
Added 18 new dictionary entries (IDs 23928-23945) from candidate_words.json. A balanced mix spanning politics, chemistry, finance, pop culture, geography, and general vocabulary.

- **Politics / society (4)**: {極右|きょくう} (far right), {極左|きょくさ} (far left), {売人|ばいにん} (drug dealer), {全方位|ぜんほうい} (all directions; omnidirectional)
- **Pop culture / people (3)**: {握手会|あくしゅかい} (handshake event), {女子力|じょしりょく} (\"girl power\"), {女子大生|じょしだいせい} (female college student)
- **Science / tech (4)**: {酸化物|さんかぶつ} (oxide), {受信機|じゅしんき} (receiver), {亜熱帯|あねったい} (subtropics), {燃料補給|ねんりょうほきゅう} (refueling)
- **Business / academic (3)**: {時価総額|じかそうがく} (market capitalization), {言語能力|げんごのうりょく} (language ability), {哲学者|てつがくしゃ} (philosopher)
- **Descriptive (2)**: {熱情的|ねつじょうてき} (passionate — na-adjective), {無比|むひ} (matchless; peerless)
- **Adverb (1)**: {過剰|かじょう}に (excessively; overly)
- **Family / education (1)**: {保育園児|ほいくえんじ} (daycare child)

All entries include full notes with COMMON COLLOCATIONS and SIMILAR WORDS / RELATED TERMS sections, appropriate semantic tags, and progressive-length examples.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








