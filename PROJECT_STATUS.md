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

### 2026-05-07 (Vocabulary Expansion - 22 New Entries, Batch 104)
Added 22 new dictionary entries (IDs 27141-27162) from candidate_words.json. Diverse vocabulary covering geography, law, arts, nature, linguistics, and abstract concepts.

- **Geography/Nature (2)**: {祖国|そこく} (homeland), {湖面|こめん} (lake surface)
- **Animals (2)**: {雄鹿|おじか} (stag), {雌鹿|めじか} (doe)
- **Law/Politics (2)**: {罰則|ばっそく} (penal provisions), {非暴力|ひぼうりょく} (nonviolence)
- **Arts (1)**: {油彩|ゆさい} (oil painting)
- **Linguistics/Education (2)**: {旧字体|きゅうじたい} (old-form kanji), {新字体|しんじたい} (new-form kanji)
- **Abstract/Formal (5)**: {錯誤|さくご} (error), {贈与|ぞうよ} (gift/donation), {取捨|しゅしゃ} (selection), {困苦|こんく} (hardship), {無策|むさく} (lack of policy)
- **Culture/Sports (2)**: {構|かま}え (stance/posture), {稽古場|けいこば} (practice hall)
- **Science/Technical (2)**: {気泡|きほう} (air bubble), {波形|はけい} (waveform)
- **Description (2)**: まだら (mottled/spotted), {無毒|むどく} (nontoxic)
- **Plants (1)**: {果樹|かじゅ} (fruit tree)
- **Honorific (1)**: {閣下|かっか} (Your Excellency)
- 22 candidates synced

Total entries: 26,932 → 26,954.

### 2026-05-07 (Vocabulary Expansion - 17 New Entries, Batch 105)
Added 17 new dictionary entries (IDs 27163-27180) from candidate_words.json. Mix of useful vocabulary spanning adverbs, na-adjectives, cultural terms, and formal/academic nouns.

- **Adverb (1)**: {一|ひと}つ{一|ひと}つ (one by one)
- **Na-adjectives (5)**: {通俗的|つうぞくてき} (popular/lowbrow), {組織的|そしきてき} (organized), {実際的|じっさいてき} (practical), {習慣的|しゅうかんてき} (habitual), {非効率的|ひこうりつてき} (inefficient), {地域的|ちいきてき} (regional)
- **Cultural/Food (2)**: {大判焼|おおばんや}き (filled cake), {粋人|すいじん} (sophisticate)
- **Language/Linguistics (2)**: {定型句|ていけいく} (set phrase), {美化語|びかご} (beautifying language)
- **Emotion/Social (2)**: {敵対心|てきたいしん} (hostility), {障害者|しょうがいしゃ} (person with disability)
- **Formal/News (2)**: {負傷者|ふしょうしゃ} (injured person), {諸条件|しょじょうけん} (various conditions)
- **Other (2)**: せどり (retail arbitrage), {突破力|とっぱりょく} (breakthrough ability), {可動式|かどうしき} (movable type)
- 1 stale candidate removed (均一化する — already existed)
- 18 candidates synced

Total entries: 26,954 → 26,972.

### 2026-05-07 (Vocabulary Expansion - 30 New Entries, Batch 103)
Added 30 new dictionary entries (IDs 27111-27140) from candidate_words.json. Diverse vocabulary covering cultural terms, daily life, food, travel, and workplace vocabulary.

- **Verbs (2)**: {華|はな}やぐ (to brighten/become festive), {掘|ほ}り{出|だ}す (to dig out/discover)
- **Food/Cooking (4)**: {焼|や}き{方|かた} (way of grilling), {魚市場|うおいちば} (fish market), {厚焼|あつや}き (thick omelette), {和食屋|わしょくや} (Japanese restaurant)
- **Culture/Religion (4)**: {戦国|せんごく} (warring states), {口伝|くでん} (oral tradition), {慰霊祭|いれいさい} (memorial service), {作務|さむ} (temple work)
- **People/Society (3)**: {学友|がくゆう} (school friend), {文筆家|ぶんぴつか} (writer), {草食系|そうしょくけい} (passive/herbivore type)
- **Work/Business (4)**: {係員|かかりいん} (attendant), {経歴書|けいれきしょ} (CV/resume), {配達先|はいたつさき} (delivery destination), {文章化|ぶんしょうか} (putting into writing)
- **Travel/Places (3)**: {途中下車|とちゅうげしゃ} (stopover), {展望所|てんぼうじょ} (viewing platform), {再入国|さいにゅうこく} (re-entry)
- **Daily life (3)**: {常備|じょうび} (keeping on hand), {遅寝|おそね} (going to bed late), {閲覧室|えつらんしつ} (reading room)
- **Communication/Language (2)**: {発話|はつわ} (speech/utterance), {対比的|たいひてき} (contrasting)
- **Description (3)**: {局地的|きょくちてき} (localized), {美文字|びもじ} (beautiful handwriting), {普及率|ふきゅうりつ} (adoption rate)
- **Other (2)**: {似顔|にがお} (likeness/portrait), {焼|や}き{印|いん} (branding mark)
- 29 candidates synced

Total entries: 26,902 → 26,932.

### 2026-05-07 (Vocabulary Expansion - 26 New Entries, Batch 102)
Added 26 new dictionary entries (IDs 27085-27110) from candidate_words.json. Focus on broadly useful vocabulary for intermediate learners: everyday expressions, cultural terms, and workplace vocabulary.

- **Adverb/Onomatopoeia (1)**: こつこつ (steadily; with tapping sound)
- **Expressions (3)**: {昔々|むかしむかし} (once upon a time), {上|うえ}から{目線|めせん} (condescending attitude), {取|と}るに{足|た}らない (insignificant)
- **Workplace/Business (3)**: {辞表|じひょう} (resignation letter), {勤務形態|きんむけいたい} (work arrangement), {準備不足|じゅんびぶそく} (lack of preparation)
- **Pronoun (1)**: {自分自身|じぶんじしん} (oneself)
- **Texture/Sensory (1)**: ざらつく (to feel rough)
- **Health/Body (1)**: {血色|けっしょく} (complexion)
- **Geography/Nature (2)**: {沼地|ぬまち} (swamp), {村落|そんらく} (village)
- **Military/News (2)**: {銃撃|じゅうげき} (shooting), {隊列|たいれつ} (formation)
- **Education (1)**: {短期大学|たんきだいがく} (junior college)
- **Life/Society (2)**: {身辺整理|しんぺんせいり} (putting affairs in order), {福音|ふくいん} (gospel/good news)
- **Culture (3)**: {五月人形|ごがつにんぎょう} (Boys' Day doll), ゲームセンター (arcade), {無法|むほう} (lawless)
- **Abstract (2)**: {才覚|さいかく} (resourcefulness), {潔|いさぎよ}さ (integrity)
- **Technology (1)**: インストールする (to install)
- **Psychology (1)**: {心的外傷|しんてきがいしょう} (psychological trauma)
- 20 stale duplicate candidates removed; 26 candidates synced

Total entries: 26,876 → 26,902.

### 2026-05-06 (Vocabulary Expansion - 22 New Entries, Batch 101)
Added 22 new dictionary entries (IDs 27063-27084) from candidate_words.json. Mix of abstract nouns, practical loanwords, and culturally interesting vocabulary.

- **Abstract nouns (心/力 compounds) (4)**: {競争心|きょうそうしん} (competitive spirit), {勝負心|しょうぶしん} (fighting spirit), {協調心|きょうちょうしん} (spirit of cooperation), {競争力|きょうそうりょく} (competitiveness)
- **Loanwords (8)**: ピンポン (ping-pong/doorbell), クレーン (crane), ペダル (pedal), タキシード (tuxedo), フルネーム (full name), ラック (rack), ギャング (gang), ブルーレイ (Blu-ray)
- **Business/Finance (3)**: {増資|ぞうし} (capital increase), {販売促進|はんばいそくしん} (sales promotion), リース (lease/wreath)
- **Appearance/Fashion (2)**: {髪色|かみいろ} (hair color), ヘアカラー (hair dye)
- **Daily life/Culture (3)**: {磯風|いそかぜ} (sea breeze), {竿竹|さおだけ} (bamboo pole), モーニング (morning set/morning coat)
- **Technology (2)**: ツイートする (to tweet), {受取証|うけとりしょう} (receipt)
- 22 candidates synced

Total entries: 26,854 → 26,876.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
