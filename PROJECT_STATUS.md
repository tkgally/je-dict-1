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

### 2026-04-15 (Vocabulary Expansion - 13 New Entries)
Added 13 new dictionary entries (IDs 23915-23927) from candidate_words.json. A mixed set covering everyday objects, medical/social/academic terms, and words frequent in news and formal writing.

- **Everyday objects / food (4)**: {角笛|つのぶえ} (horn — animal-horn musical instrument), {爪楊枝|つまようじ} (toothpick), {鉄鍋|てつなべ} (iron pot/pan), {仕出|しだ}し{弁当|べんとう} (catered bento)
- **Medical / body (1)**: {鼻炎|びえん} (rhinitis — with note on allergic and chronic variants)
- **People / roles (3)**: {仲介者|ちゅうかいしゃ} (mediator; broker), {出場者|しゅつじょうしゃ} (contestant; participant), {声楽家|せいがくか} (classical vocalist)
- **Food-industry noun (1)**: {魚肉|ぎょにく} (fish meat — processed-food category, not everyday cooking speech)
- **News / formal (2)**: {暴発|ぼうはつ} (accidental discharge; sudden eruption — two senses, firearm + metaphorical), {男装|だんそう} (female-to-male cross-dressing — with Takarazuka context)
- **Social / academic (2)**: {階層|かいそう}{社会|しゃかい} (stratified/class society), {序説|じょせつ} (introductory treatise; prolegomena)
- **New kanji**: Added 楊 (kanji ID 02685, 'you/yanagi — willow') to support {爪楊枝|つまようじ}
- All entries follow v2 standards: progressive-length examples (3+ per sense), structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS sections, full furigana coverage, and sense-number annotations

### 2026-04-15 (Vocabulary Expansion - 14 New Entries)
Added 14 new dictionary entries (IDs 23901-23914) from candidate_words.json. A mix of everyday loanwords, social/institutional nouns, and a few more technical terms.

- **Loanword nouns (5)**: スタジアム (stadium — sports venue), ゲレンデ (ski slope — from German), スノーボード (snowboard/snowboarding), ティッシュペーパー (facial tissues), ローマ{字入力|じにゅうりょく} (romaji input method)
- **Social / institutional nouns (4)**: {原住民|げんじゅうみん} (native inhabitants — with usage note on the shift toward {先住民|せんじゅうみん}), {名家|めいか} (distinguished family), {救助隊|きゅうじょたい} (rescue team), {騒乱|そうらん} (civil disturbance; riot)
- **Technical / linguistic / measurement nouns (3)**: {擬声語|ぎせいご} (onomatopoeia — sound-imitating words), {満年齢|まんねんれい} (full age — contrasted with {数|かぞ}え{年|どし}), {機械化|きかいか} (mechanization — also a {する}-verb)
- **Time noun (1)**: {前年|ぜんねん} (previous year — formal; frequent in year-on-year business comparisons)
- **Accessibility noun (1)**: {白杖|はくじょう} (white cane — with note on the legal/SOS signaling function)
- All entries follow v2 standards: progressive-length examples (3+ per sense), structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS sections, full furigana coverage, and sense-number annotations

### 2026-04-15 (Vocabulary Expansion - 8 New Entries)
Added 8 new dictionary entries (IDs 23893-23900) from candidate_words.json, emphasizing quality over quantity. A mixed set covering loanword nouns, linguistics/poetics terminology, and common polite expressions.

- **Loanword noun (1)**: スチュワーデス (stewardess; flight attendant — with note on the shift toward gender-neutral {客室乗務員|きゃくしつじょうむいん})
- **Linguistics / poetics nouns (3)**: {字音|じおん} (Sino-Japanese on-reading of a kanji), {律詩|りっし} (regulated verse, classical Chinese poetic form), {音数|おんすう} (mora count; number of morae, used in haiku/tanka prosody)
- **Art / evaluation noun (1)**: {優品|ゆうひん} (fine piece; superior-quality article, used in auction/antiques contexts)
- **Expressions (3)**: でしょうか (polite softened question ending), {秩序|ちつじょ}を{守|まも}る (to maintain order), お{招|まね}きにあずかる (to be kindly invited — humble/formal)
- Also removed 2 stale candidates (C17377 {上手|じょうず}に — regular adverb of existing entry; C17533 {立替払|たてかえばら}い — orthographic variant of existing 23347)
- All entries follow v2 standards: progressive-length examples (3+ per sense), structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS sections, full furigana coverage, and sense-number annotations

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

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








