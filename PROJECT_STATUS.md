# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-08
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
| Total entries | ~15,764 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~12,965 (open) |
| Candidate words | ~4,008 |
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

### 2026-03-08 (Vocabulary Expansion - 30 New Entries, Session 397)
Added 30 new dictionary entries (IDs 15679-15708) from candidate_words.json:

- **Nouns (19)**: {苗木|なえぎ} (sapling), {感染症|かんせんしょう} (infectious disease), {平屋|ひらや} (one-story house), {備考|びこう} (remarks), {退職届|たいしょくとどけ} (resignation letter), {原本|げんぽん} (original document), {陶磁器|とうじき} (ceramics), {曲芸|きょくげい} (acrobatics), {密猟|みつりょう} (poaching), {潜水艦|せんすいかん} (submarine), {空母|くうぼ} (aircraft carrier), {異文化|いぶんか} (different culture), {茶托|ちゃたく} (teacup saucer), {定款|ていかん} (articles of incorporation), {被害届|ひがいとどけ} (damage report), {操縦席|そうじゅうせき} (cockpit), {箱推|はこお}し (supporting entire group), {四捨五入|ししゃごにゅう} (rounding), {踏|ふ}み{倒|たお}し (defaulting on debt)
- **Noun with two senses (2)**: {報|むく}い (reward/retribution), {死角|しかく} (blind spot)
- **Noun/na-adjective (1)**: {太|ふと}っ{腹|ぱら} (generous)
- **Adjective-i (1)**: {輝|かがや}かしい (brilliant)
- **Adjective-taru (1)**: {騒然|そうぜん} (tumultuous)
- **Pre-noun adjectival (1)**: ありふれた (commonplace)
- **Noun/verb-suru (3)**: {思索|しさく} (contemplation), {追憶|ついおく} (reminiscence), {一段落|いちだんらく} (reaching a stopping point)
- **Noun (family) (1)**: {母性|ぼせい} (motherhood)
- **Adverb (1)**: {存分|ぞんぶん}に (to one's heart's content)

Notable features:
- Business/legal cluster: {備考|びこう}, {退職届|たいしょくとどけ}, {原本|げんぽん}, {定款|ていかん}, {被害届|ひがいとどけ}, {踏|ふ}み{倒|たお}し
- Military: {潜水艦|せんすいかん}, {空母|くうぼ}
- Culture: {陶磁器|とうじき}, {茶托|ちゃたく}, {箱推|はこお}し, {異文化|いぶんか}
- Multi-sense entries: {報|むく}い (2: reward + retribution), {死角|しかく} (2: physical + figurative)
- New kanji: 2,520 → 2,522 ({托|たく}, {款|かん})

Total entries: ~15,734 → ~15,764 (approximate)
Remaining candidates: ~4,037 → ~4,008 (29 removed)

### 2026-03-08 (Vocabulary Expansion - 30 New Entries, Session 396)
Added 30 new dictionary entries (IDs 15649-15678) from candidate_words.json:

- **Nouns (18)**: {高齢者|こうれいしゃ} (elderly person), {焼|や}き{芋|いも} (roasted sweet potato), {遺失物|いしつぶつ} (lost property), {保険金|ほけんきん} (insurance money), {資産|しさん} (assets), {無力感|むりょくかん} (helplessness), {手|て}ほどき (basic instruction), {苦労人|くろうにん} (person of hardship), {半月|はんつき} (half a month), {四字熟語|よじじゅくご} (four-character idiom), {貴社|きしゃ} (your company), {装丁|そうてい} (book design), {診察室|しんさつしつ} (examination room), {窓枠|まどわく} (window frame), {小論文|しょうろんぶん} (short essay), {城塞|じょうさい} (fortress), {背表紙|せびょうし} (book spine), {情報源|じょうほうげん} (information source)
- **Noun/na-adjective (1)**: {不規則|ふきそく} (irregular)
- **Noun/verb-suru (6)**: {完敗|かんぱい} (complete defeat), {突発|とっぱつ} (sudden outbreak), {道案内|みちあんない} (giving directions), {遮断|しゃだん} (cutoff/blocking), {中休|なかやす}み (mid-break), {定期検診|ていきけんしん} (periodic checkup)
- **Noun (work) (3)**: {年次|ねんじ} (annual), {試用期間|しようきかん} (probation period), {不採用|ふさいよう} (rejection)
- **Verb-godan (1)**: {打|う}ち{負|ま}かす (to defeat)
- **Adverb (1)**: けろりと (nonchalantly; completely recovering)

Notable features:
- Business/work cluster: {年次|ねんじ}, {貴社|きしゃ}, {試用期間|しようきかん}, {不採用|ふさいよう}, {資産|しさん}, {保険金|ほけんきん}
- Medical: {診察室|しんさつしつ}, {定期検診|ていきけんしん}, {高齢者|こうれいしゃ}
- Books/publishing: {装丁|そうてい}, {背表紙|せびょうし}, {小論文|しょうろんぶん}
- Culture/food: {焼|や}き{芋|いも}, {四字熟語|よじじゅくご}
- Multi-sense entries: けろりと (2: nonchalant + complete recovery), {年次|ねんじ} (2: annual + year of service)

Total entries: ~15,704 → ~15,734 (approximate)
Remaining candidates: ~4,067 → ~4,037 (30 removed)

### 2026-03-07 (Vocabulary Expansion - 30 New Entries, Session 395)
Added 30 new dictionary entries (IDs 15619-15648) from candidate_words.json:

- **Nouns (11)**: {柑橘類|かんきつるい} (citrus fruits), {日系人|にっけいじん} (person of Japanese descent), {嫡男|ちゃくなん} (legitimate heir), {手渡|てわた}し (hand delivery), {勝者|しょうしゃ} (winner), {首脳|しゅのう} (head/leader), {調律師|ちょうりつし} (piano tuner), {土蔵|どぞう} (earthen storehouse), {債券|さいけん} (bond), {動物|どうぶつ}{病院|びょういん} (vet hospital), {競走|きょうそう} (race)
- **Noun/verb-suru (5)**: {譲渡|じょうと} (transfer), {安堵|あんど}する (to be relieved), {参拝|さんぱい}する (to visit a shrine), {具現|ぐげん} (embodiment), {完走|かんそう}する (to finish a race)
- **Na-adjectives (3)**: {専門的|せんもんてき} (specialized), {不正確|ふせいかく} (inaccurate), {凄絶|せいぜつ} (ghastly/fierce)
- **Verbs (3)**: {投|な}げつける (to hurl at), {軽|かろ}んじる (to belittle), {洒落|しゃれ}た (stylish)
- **Nouns (other) (5)**: いきさつ (circumstances), {戸建|こだて} (detached house), {術後|じゅつご} (post-operative), {羞恥心|しゅうちしん} (sense of shame), {右肩下|みぎかたさ}がり (downward trend)
- **Adverb (1)**: {何故|なぜ}か (for some reason)
- **Expression (1)**: {甘|あま}く{見|み}る (to underestimate)
- **Place name (1)**: {九州|きゅうしゅう} (Kyushu)

Notable features:
- Good variety: financial ({債券|さいけん}, {譲渡|じょうと}), medical ({術後|じゅつご}, {動物|どうぶつ}{病院|びょういん}), cultural ({土蔵|どぞう}, {参拝|さんぱい}する, {嫡男|ちゃくなん})
- Practical daily life: {戸建|こだて}, {手渡|てわた}し, {完走|かんそう}する, {甘|あま}く{見|み}る
- Multi-sense entries: いきさつ (2: circumstances + complications), {凄絶|せいぜつ} (2: ghastly + fierce), {洒落|しゃれ}た (2: stylish + witty)
- New kanji: 2,517 → 2,520 ({嫡|ちゃく}, {柑|かん}, {橘|きつ})

Total entries: ~15,674 → ~15,704 (approximate)
Remaining candidates: ~4,097 → ~4,067 (30 removed)

### 2026-03-07 (Vocabulary Expansion - 30 New Entries, Session 394)
Added 30 new dictionary entries (IDs 15589-15618) from candidate_words.json:

- **Noun/verb-suru (8)**: {提唱|ていしょう} (advocacy), {付与|ふよ} (granting), {結実|けつじつ} (bearing fruit), {立案|りつあん} (planning), {力走|りきそう} (powerful run), {奪還|だっかん} (recapture), {方向転換|ほうこうてんかん} (change of direction), {断行|だんこう} (decisive action)
- **Nouns (7)**: {名案|めいあん} (brilliant idea), {帰省|きせい}ラッシュ (homecoming rush), {部外者|ぶがいしゃ} (outsider), {桜色|さくらいろ} (cherry blossom pink), {野暮用|やぼよう} (trifling errand), {濃紺|のうこん} (dark navy), {障害物|しょうがいぶつ} (obstacle)
- **Na-adjectives (3)**: {地道|じみち} (steady), {独占的|どくせんてき} (monopolistic), {種別|しゅべつ} (classification)
- **I-adjectives (2)**: {忍耐強|にんたいづよ}い (patient), {気忙|きぜわ}しい (restless)
- **Noun/na-adjective (2)**: {非凡|ひぼん} (extraordinary), {腹|はら}ぺこ (starving)
- **Pre-noun adjectival (1)**: {古|ふる}びた (old-looking)
- **Noun (1)**: ろくでなし (good-for-nothing)
- **Noun/expression (2)**: {三者三様|さんしゃさんよう} (each to their own), {繰|く}り{越|こ}し (carryover)
- **Verb-godan (1)**: {駆|か}け{出|だ}す (to dash off)
- **Verb-ichidan (1)**: {強|し}いる (to force)
- **Expression (1)**: {気|き}を{紛|まぎ}らす (to distract oneself)
- **Color (1)**: {黄緑|きみどり} (yellow-green)

Notable features:
- Good variety of parts of speech across adjectives, verbs, nouns, and expressions
- Practical daily life: {帰省|きせい}ラッシュ, {野暮用|やぼよう}, {腹|はら}ぺこ, {繰|く}り{越|こ}し
- Business/formal: {付与|ふよ}, {立案|りつあん}, {断行|だんこう}, {独占的|どくせんてき}, {種別|しゅべつ}
- Color pair: {桜色|さくらいろ}, {黄緑|きみどり}, {濃紺|のうこん}
- Multi-sense entries: {駆|か}け{出|だ}す (2: start running + run out), {結実|けつじつ} (2: literal + figurative), {方向転換|ほうこうてんかん} (2: physical + strategic)

Total entries: ~15,644 → ~15,674 (approximate)
Remaining candidates: ~4,127 → ~4,097 (30 removed)

### 2026-03-07 (Vocabulary Expansion - 30 New Entries, Session 393)
Added 30 new dictionary entries (IDs 15559-15588) from candidate_words.json:

- **Nouns (20)**: {芥川賞|あくたがわしょう} (Akutagawa Prize), {直木賞|なおきしょう} (Naoki Prize), {処女作|しょじょさく} (debut work), {占星術|せんせいじゅつ} (astrology), {久遠|くおん} (eternity), {血圧計|けつあつけい} (blood pressure monitor), {酷寒|こっかん} (severe cold), {美人画|びじんが} (bijin-ga), {五線譜|ごせんふ} (musical staff), {毛織物|けおりもの} (woolen fabric), {静止画|せいしが} (still image), {接近戦|せっきんせん} (close-quarters combat), {病熱|びょうねつ} (fever from illness), {貯水槽|ちょすいそう} (water tank), {汚泥|おでい} (sludge), {補正予算|ほせいよさん} (supplementary budget), {高山植物|こうざんしょくぶつ} (alpine plants), {不在連絡票|ふざいれんらくひょう} (missed delivery notice), {百聞|ひゃくぶん} (hearing a hundred times), {瞬間接着剤|しゅんかんせっちゃくざい} (super glue)
- **Noun/verb-suru (3)**: {誤嚥|ごえん} (aspiration), {起案|きあん} (drafting), {急接近|きゅうせっきん} (rapid approach)
- **Noun/na-adjective (3)**: {至高|しこう} (supreme), {超一流|ちょういちりゅう} (world-class), {電気自動車|でんきじどうしゃ} (electric vehicle)
- **Noun (2)**: {公使|こうし} (diplomatic minister), {少数民族|しょうすうみんぞく} (ethnic minority)
- **Noun (1)**: {真|ま}っ{向|こう}{勝負|しょうぶ} (head-on contest)
- **Expression (1)**: {機嫌|きげん}をとる (to humor someone)

Notable features:
- Literary prizes pair: {芥川賞|あくたがわしょう}/{直木賞|なおきしょう}
- Daily life vocabulary: {不在連絡票|ふざいれんらくひょう}, {瞬間接着剤|しゅんかんせっちゃくざい}, {血圧計|けつあつけい}
- Technical/modern: {電気自動車|でんきじどうしゃ}, {静止画|せいしが}, {補正予算|ほせいよさん}
- Cultural: {美人画|びじんが}, {占星術|せんせいじゅつ}, {久遠|くおん}
- Multi-sense entry: {急接近|きゅうせっきん} (2: physical approach + relationship)
- New kanji: 2,516 → 2,517 ({芥|かい})

Total entries: ~15,614 → ~15,644 (approximate)
Remaining candidates: ~4,157 → ~4,127 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
