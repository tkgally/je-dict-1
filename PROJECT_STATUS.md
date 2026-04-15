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

### 2026-04-15 (Vocabulary Expansion - 15 New Entries)
Added 15 new dictionary entries (IDs 23878-23892) from candidate_words.json. A themed mix covering language/linguistics, transportation, environment, education, engineering, and architecture.

- **Language / grammar (2)**: {話|はな}し{言葉|ことば} (spoken/colloquial language), {過去形|かこけい} (past tense)
- **Transportation / urban (2)**: {終着駅|しゅうちゃくえき} (terminal station; last stop — with figurative usage), {分譲住宅|ぶんじょうじゅうたく} (housing for sale, contrasting with rentals)
- **Environment / weather (2)**: {焼却炉|しょうきゃくろ} (incinerator), {集中豪雨|しゅうちゅうごうう} (torrential localized downpour)
- **Business / industry (1)**: {印刷所|いんさつじょ} (print shop)
- **Engineering / technology (4)**: {側面図|そくめんず} (side view / elevation drawing), {絶縁体|ぜつえんたい} (electrical insulator), {増幅器|ぞうふくき} (amplifier), {計量器|けいりょうき} (measuring instrument)
- **Architecture (1)**: {高層建築|こうそうけんちく} (high-rise building)
- **Healthcare (1)**: {在宅医療|ざいたくいりょう} (home healthcare)
- **Ideas / school life (2)**: {妙案|みょうあん} (clever idea), {二学期|にがっき} (second school term)
- All entries follow v2 standards: progressive-length examples (3+ per sense), structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS sections, full furigana coverage, and sense-number annotations

### 2026-04-15 (Vocabulary Expansion - 10 New Entries)
Added 10 new dictionary entries (IDs 23868-23877) from candidate_words.json. A mixed set covering everyday nouns, loanwords, a grammatical expression, and question-word vocabulary.

- **Nouns (7)**: {舟|ふね} (small boat — distinguished from {船|ふね}), {仏教徒|ぶっきょうと} (Buddhist), {拳法|けんぽう} (Chinese-style martial arts — homophone-linked to {憲法|けんぽう}), {野球帽|やきゅうぼう} (baseball cap), {限界点|げんかいてん} (limit point; threshold), {何日|なんにち} (how many days / what day — two senses)
- **Loanwords (3)**: パウダー (powder — cosmetic), ワークブック (workbook), スカッシュ (squash sport / squash drink — two senses)
- **Expression (1)**: {次第|しだい}で (depending on; subject to — grammatical pattern)
- All entries follow v2 standards: progressive-length examples (3 per sense), structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS sections, full furigana coverage, and sense-number annotations
- Cross-references added: {舟|ふね}↔{船|ふね}, {拳法|けんぽう}↔{憲法|けんぽう} (homophone)

### 2026-04-15 (Vocabulary Expansion - 10 New Entries)
Added 10 new dictionary entries (IDs 23858-23867) from candidate_words.json. A mixed set covering clothing, medical/biology, industrial, commerce, education, and informal everyday vocabulary.

- **Clothing (2)**: {袖口|そでぐち} (cuff; sleeve opening), {袖|そで}なし (sleeveless — garment type)
- **Medical / body (2)**: {甲状腺|こうじょうせん} (thyroid gland), {汗腺|かんせん} (sweat gland)
- **Industrial / abstract (1)**: {潤滑|じゅんかつ} (lubrication; smoothness — with figurative usage)
- **Education (1)**: {受講料|じゅこうりょう} (course fee; tuition for a class)
- **Geography (1)**: {岩山|いわやま} (rocky mountain; rocky hill)
- **Transportation / commerce (2)**: {輸入車|ゆにゅうしゃ} (imported car), {国産車|こくさんしゃ} (domestic car) — cross-contrastive pair
- **Informal everyday (1)**: うんこ (poop; poo — casual/childlike)
- All entries follow v2 standards: progressive-length examples (3 per sense), structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS / RELATED TERMS sections, full furigana coverage, and sense-number annotations

### 2026-04-15 (Vocabulary Expansion - 15 New Entries)
Added 15 new dictionary entries (IDs 23843-23857) from candidate_words.json. A themed mix of academic, music, technology, and everyday nouns plus one {する}-verb.

- **Academic / language / education (4)**: {社会学|しゃかいがく} (sociology), {派生語|はせいご} (derived word; linguistic derivative), {体験学習|たいけんがくしゅう} (experiential/hands-on learning), {助演男優|じょえんだんゆう} (supporting actor)
- **Music (2)**: {二重奏|にじゅうそう} (instrumental duet), {三重奏|さんじゅうそう} (instrumental trio) — cross-linked to each other
- **Transport / places (2)**: {寝台車|しんだいしゃ} (sleeping car on a train), マリーナ (marina)
- **Technology / leisure (2)**: ヘッドセット (headset with microphone), {攻略本|こうりゃくぼん} (strategy guide book for video games)
- **Everyday / infrastructure (4)**: {電気工事|でんきこうじ} (electrical work), {使用法|しようほう} (directions for use), {誘導灯|ゆうどうとう} (illuminated exit/evacuation sign), {有酸素|ゆうさんそ} (aerobic; prefix-like noun)
- **Noun + {する}-verb (1)**: {立証|りっしょう} (proof; substantiation — legal/academic register)
- All entries follow v2 standards: progressive-length examples (3 per sense), structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR or RELATED WORDS sections, full furigana coverage, and sense-number annotations

### 2026-04-15 (Vocabulary Expansion - 10 New Entries)
Added 10 new dictionary entries (IDs 23833-23842) from candidate_words.json. A mixed set covering everyday nouns, technical vocabulary, a na-adjective loanword, and a multi-sense general noun.

- **Nouns (8)**: アスピリン (aspirin), ウェブページ (web page), イタチ (weasel), {花輪|はなわ} (floral wreath; garland), {電磁石|でんじしゃく} (electromagnet), {投稿者|とうこうしゃ} (poster; contributor), {広報活動|こうほうかつどう} (public relations activities), {通知書|つうちしょ} (official notice/notification letter)
- **Na-adjective (1)**: チャーミング (charming; endearing — loanword)
- **Multi-sense noun (1)**: {小口|こぐち} (small-lot; cut end of a log; edge of a book — three senses, 9 examples)
- All entries include progressive-length examples, structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS sections, and full furigana coverage

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








