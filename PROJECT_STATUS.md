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

### 2026-04-03 (Vocabulary Expansion - 22 New Entries, Session 2)
Added 22 new dictionary entries (IDs 21757-21778) from candidate_words.json. A diverse mix including emotion words, food terms, politics, grammar, and practical vocabulary.

- **Suru verbs (5)**: {失望|しつぼう}する (to be disappointed), がっかりする (to be let down), {奮起|ふんき}する (to rouse oneself), {伝搬|でんぱん} (propagation), {修繕費|しゅうぜんひ} (repair cost - noun only)
- **Godan verbs (2)**: {弔|とむら}う (to mourn), {嘘|うそ}をつく (to tell a lie)
- **I-adjectives (2)**: {根気強|こんきづよ}い (persevering), {飲|の}みやすい (easy to drink)
- **Nouns (11)**: {盛|も}り{合|あ}わせ (assorted platter), {水無月|みなづき} (June/wagashi), {受動態|じゅどうたい} (passive voice), {重油|じゅうゆ} (heavy oil), {舞踊家|ぶようか} (dancer), {地方自治|ちほうじち} (local self-government), {集客力|しゅうきゃくりょく} (drawing power), {��似性|るいじせい} (similarity), {同窓生|どうそうせい} (alumnus), {就労|しゅうろう}ビザ (work visa), {鳥小屋|とりごや} (birdhouse)
- **Politics (2)**: {君主制|くんしゅせい} (monarchy), {独裁制|どくさいせい} (dictatorship)
- 1 new kanji (弔) assigned ID 02644
- Removed 22 candidates that now exist as entries


### 2026-04-02 (Vocabulary Expansion - 30 New Entries, Session 580)
Added 30 new dictionary entries (IDs 21705-21734) from candidate_words.json. A practical mix of vocabulary for intermediate learners including verbs, nouns, adverbs, and food terms.

- **Suru verbs (5)**: {触発|しょくはつ}する (to trigger/inspire), {誘導|ゆうどう}する (to guide/induce), {回想|かいそう}する (to reminisce), {整理|せいり}する (to organize), {改変|かいへん} (alteration)
- **Ichidan verb (1)**: {生|い}き{延|の}びる (to survive)
- **Na-adjectives (2)**: {無敵|むてき} (invincible), {過小|かしょう} (too small)
- **Nouns (16)**: {略語|りゃくご} (abbreviation), {輝|かがや}き (brilliance), {周期|しゅうき} (cycle), {漆黒|しっこく} (jet black), {初春|しょしゅん} (early spring), {料亭|りょうてい} (high-class restaurant), {降雨|こうう} (rainfall), {低気圧|ていきあつ} (low pressure), {文通|ぶんつう} (correspondence), {壇上|だんじょう} (on stage), {並立|へいりつ} (coexistence), {年頭|ねんとう} (start of year), {火照|ほて}り (flushing), {深度|しんど} (depth), {書類選考|しょるいせんこう} (document screening), {音域|おんいき} (vocal range)
- **Adverbs/Other (4)**: たじたじ (flinching), まずまず (fairly), {風雨|ふうう} (wind and rain), {話術|わじゅつ} (speaking skill)
- **Food (1)**: はんぺん (steamed fish cake)
- **Culture (1)**: お{墓|はか} (grave)
- Removed 10 stale duplicate candidates










---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
