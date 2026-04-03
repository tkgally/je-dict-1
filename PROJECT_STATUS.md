# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-03
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

### 2026-04-03 (Vocabulary Expansion - 30 New Entries, Session 8)
Added 30 new dictionary entries (IDs 21924-21953) from candidate_words.json. A diverse mix of nouns, verbs, and expressions covering architecture, nature, food, sports, culture, and everyday life.

- **Nouns (22)**: {低層|ていそう} (low-rise), {留|と}め{金|がね} (clasp/fastener), {本拠|ほんきょ} (headquarters), {苦労話|くろうばなし} (hardship story), {率直|そっちょく}さ (frankness), {鎮痛薬|ちんつうやく} (painkiller), {洗浄液|せんじょうえき} (cleaning solution), {実寸|じっすん} (actual size), {海港|かいこう} (seaport), {勢力圏|せいりょくけん} (sphere of influence), {防衛線|ぼうえいせん} (defensive line), {薬味皿|やくみざら} (condiment plate), {暖房器具|だんぼうきぐ} (heating appliance), リズム{感|かん} (sense of rhythm), {休刊日|きゅうかんび} (newspaper holiday), {求肥|ぎゅうひ} (gyuhi mochi), {投|な}げ (throw), {巻雲|けんうん} (cirrus cloud), {書風|しょふう} (calligraphic style), {光影|こうえい} (light and shadow), {高校野球|こうこうやきゅう} (high school baseball), {趣味三昧|しゅみざんまい} (immersed in hobbies)
- **Suru verbs (3)**: {密生|みっせい}する (dense growth), {群生|ぐんせい}する (growing in clusters), {再発行|さいはっこう}する (to reissue)
- **Verbs (3)**: {叩|たた}き{伏|ふ}せる (to knock down), {仕立|した}て{直|なお}す (to alter clothing), {動|うご}き{始|はじ}める (to begin moving)
- **Expressions (1)**: {名|な}もなき (nameless), {追|お}いはぎ (highway robber)
- Removed 30 candidates that now exist as entries

### 2026-04-03 (Vocabulary Expansion - 30 New Entries, Session 7)
Added 30 new dictionary entries (IDs 21894-21923) from candidate_words.json. A diverse mix of na-adjectives, suru verbs, nouns, and expressions useful for intermediate learners.

- **Na-adjectives (8)**: {神秘的|しんぴてき} (mysterious/mystical), {平均的|へいきんてき} (average/typical), {飛躍的|ひやくてき} (dramatic/remarkable), {金銭的|きんせんてき} (financial/monetary), {恣意的|しいてき} (arbitrary/capricious), {原始的|げんしてき} (primitive/primeval), {熱狂的|ねっきょうてき} (fanatical/fervent), {英雄的|えいゆうてき} (heroic/valiant), {独善的|どくぜんてき} (self-righteous/dogmatic)
- **Suru verbs (7)**: {秘匿|ひとく}する (to conceal), {集中|しゅうちゅう}する (to concentrate), {中止|ちゅうし}する (to cancel), {管理|かんり}する (to manage), {妄想|もうそう}する (to fantasize), {注力|ちゅうりょく}する (to focus efforts), {離反|りはん}する (to defect), {推量|すいりょう}する (to conjecture)
- **Nouns (7)**: {協議会|きょうぎかい} (council), {無給|むきゅう} (unpaid), {目尻|めじり} (outer corner of eye), {締切日|しめきりび} (deadline date), {流言|りゅうげん} (rumor), {立体感|りったいかん} (three-dimensionality), {注目度|ちゅうもくど} (degree of attention), {扱|あつか}い{方|かた} (how to handle), {老婦人|ろうふじん} (elderly woman), {林道|りんどう} (forest road), {料金表|りょうきんひょう} (price list)
- **Expressions (2)**: {失礼|しつれい}します (excuse me), {恐|おそ}れ{入|い}ります (I'm sorry to trouble you — removed as duplicate of existing entry 17552)
- 1 new kanji (恣) assigned ID 02647
- Removed 1 stale candidate (恐れ入りますが — already exists as entry)

### 2026-04-03 (Vocabulary Expansion - 30 New Entries, Session 6)
Added 30 new dictionary entries (IDs 21864-21893) from candidate_words.json. A diverse mix of practical vocabulary for intermediate learners including verbs, nouns, expressions, adjectives, and adverbs.

- **Verbs (8)**: {考|かんが}え{込|こ}む (to ponder deeply), たしなむ (to enjoy as a pastime), {敢行|かんこう}する (to carry out boldly), {撃退|げきたい}する (to repel), {助成|じょせい}する (to subsidize), {見聞|みき}きする (to see and hear), {降|ふ}り{続|つづ}く (to keep falling), {見返|みかえ}る (to look back; to prove oneself)
- **Nouns (10)**: {続行|ぞっこう} (continuation), {歩行|ほこう} (walking), {展示会|てんじかい} (exhibition), {年中無休|ねんじゅうむきゅう} (open year-round), {博識|はくしき} (erudition), {勝|か}ち{越|こ}し (winning record), {師弟|してい} (master and disciple), {私事|しじ} (personal matter), {音質|おんしつ} (sound quality), {事典|じてん} (encyclopedia)
- **Expressions (3)**: {腕|うで}を{組|く}む (to fold one's arms), {息|いき}をつく (to catch one's breath), {小分|こわ}けする (to divide into smaller portions)
- **Adjectives (2)**: {将来的|しょうらいてき} (future/prospective), {栗色|くりいろ} (chestnut color)
- **Adverbs (3)**: {先立|さきだ}って (prior to; the other day), むくむく (swelling/fluffy), {夜毎|よごと} (every night)
- **Other nouns (4)**: {県立|けんりつ} (prefectural), {同業|どうぎょう} (same trade), {酒席|しゅせき} (drinking party), {初陣|ういじん} (debut/first battle)
- Removed 30 candidates that now exist as entries

### 2026-04-03 (Vocabulary Expansion - 30 New Entries, Session 5)
Added 30 new dictionary entries (IDs 21834-21863) from candidate_words.json. A diverse mix of vocabulary across business, culture, history, food, health, law, and everyday life.

- **Na-adjectives (3)**: {辛辣|しんらつ} (harsh/scathing), {激烈|げきれつ} (fierce/intense), {怪異|かいい} (mysterious/supernatural)
- **Na-adj/noun combos (2)**: {自由自在|じゆうじざい} (freely/at will), {阿呆|あほう} (fool/idiot)
- **Nouns - Business/Law (4)**: {管理職|かんりしょく} (management position), {許認可|きょにんか} (permits and licenses), {専売|せんばい} (monopoly sale), {実力者|じつりょくしゃ} (person of influence)
- **Nouns - History/Military (3)**: {統制|とうせい} (control/regulation), {平定|へいてい} (pacification), {征伐|せいばつ} (subjugation)
- **Nouns - Culture/Society (5)**: {悲願|ひがん} (long-cherished wish), {直筆|じきひつ} (one's own handwriting), {名士|めいし} (notable person), {後援者|こうえんしゃ} (supporter/patron), {検視|けんし} (coroner's inquest)
- **Nouns - Everyday/Science (6)**: {空中|くうちゅう} (midair), {減塩|げんえん} (salt reduction), {進行中|しんこうちゅう} (in progress), {古紙|こし} (waste paper), {脱色|だっしょく} (bleaching), {縦横|じゅうおう} (vertical and horizontal)
- **Nouns - Other (4)**: {甲羅|こうら} (shell/carapace), {海難|かいなん} (maritime disaster), {内服|ないふく} (oral medicine), {午睡|ごすい} (afternoon nap)
- **Loanwords (1)**: フィルター (filter)
- **Expressions (1)**: お{世話様|せわさま} (thank you for your help)
- **Other (1)**: {探訪|たんぼう} (visit/exploration)
- 1 new kanji (辣) assigned ID 02646
- Removed 1 stale candidate (配役 with incorrect reading)

### 2026-04-03 (Vocabulary Expansion - 30 New Entries, Session 4)
Added 30 new dictionary entries (IDs 21804-21833) from candidate_words.json. A diverse mix of vocabulary across nature, culture, food, law, and everyday life.

- **Adverbs (2)**: あからさまに (bluntly/blatantly), いかほど (how much - formal)
- **Nouns - Nature (5)**: {雨空|あまぞら} (rainy sky), {草地|くさち} (grassland), {黄葉|こうよう} (yellow autumn leaves), {山茶花|さざんか} (sasanqua), {花木|かぼく} (flowering tree)
- **Nouns - Food (3)**: {中華麺|ちゅうかめん} (Chinese noodles), すだち (sudachi citrus), {白子|しらこ} (milt)
- **Nouns - Culture/Society (6)**: {死生観|しせいかん} (view of life and death), {徒弟|とてい} (apprentice), {騎手|きしゅ} (jockey), {優勝者|ゆうしょうしゃ} (champion), {戦火|せんか} (flames of war), {夭折|ようせつ} (dying young)
- **Nouns - Everyday (6)**: {基礎知識|きそちしき} (basic knowledge), {別日|べつじつ} (another day), {運動場|うんどうじょう} (sports ground), マット (mat), マーカー (marker pen), {談話室|だんわしつ} (lounge)
- **Nouns - Formal/Technical (4)**: {推量|すいりょう} (conjecture), {適法|てきほう} (lawful), {権益|けんえき} (vested interests), {薬効|やっこう} (medicinal effect)
- **Other (4)**: {小技|こわざ} (trick/technique), {彩色|さいしょく} (coloring), {燃|も}え{殻|がら} (cinders), {無欠|むけつ} (flawless)
- 1 new kanji (夭) assigned ID 02645
- Removed 30 candidates that now exist as entries

### 2026-04-03 (Vocabulary Expansion - 25 New Entries, Session 3)
Added 25 new dictionary entries (IDs 21779-21803) from candidate_words.json. Focused on practical grammar, expressions, and common vocabulary useful for intermediate learners.

- **Conjunctions (3)**: おまけに (on top of that), {加|くわ}えて (in addition), もっとも (however/though)
- **Pre-noun adjectivals (2)**: こうした (such/this kind of), そうした (such/that kind of)
- **Expressions (5)**: {目|め}を{見張|みは}る (to be amazed), {上手|うま}くいく (to go well), {白紙|はくし}に{戻|もど}る (to go back to square one), {気|き}がつく (to notice), {顔|かお}を{上|あ}げる (to raise one's head), 〜における (in/at - formal)
- **Verbs (3)**: {名乗|なの}り{出|で}る (to come forward), {帰国|きこく}する (to return to one's country), {注|つ}ぎ{足|た}す (to top up)
- **Nouns (2)**: {現役|げんえき} (active service), {得意先|とくいさき} (customer/client), バイキング (buffet), {予約済|よやくず}み (reserved)
- **Adjectives (3)**: {小|ちい}さめ (rather small), {太|ふと}り{気味|ぎみ} (somewhat overweight), {食|た}べやすい (easy to eat), {平明|へいめい} (plain/clear)
- **Particles (2)**: 〜つつ (while/although), 〜にて (at/in - formal)
- **Adverb (1)**: いくらか (somewhat/some)
