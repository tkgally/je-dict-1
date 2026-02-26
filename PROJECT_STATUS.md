# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-26
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
| Total entries | ~13,814 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~11,015 (open) |
| Candidate words | ~5,955 |
| Cross-references | ~3,400 |
| Example sentences | ~47,500 |
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

### 2026-02-26 (Vocabulary Expansion - 30 New Entries, Session 332)
Added 30 new dictionary entries (IDs 13729-13758) from candidate_words.json:

- **Nouns (14)**: {礎|いしずえ} (foundation), {社会人|しゃかいじん} (working adult), {社内|しゃない} (within company), {祈|いの}り (prayer), {祭壇|さいだん} (altar), {神棚|かみだな} (kami shelf), {礼節|れいせつ} (courtesy), {禁物|きんもつ} (taboo), {社畜|しゃちく} (corporate slave), {直売所|ちょくばいじょ} (farm stand), {秘訣|ひけつ} (secret/key), {空間|くうかん} (space), {秋刀魚|さんま} (Pacific saury), {福祉|ふくし} (welfare)
- **Noun/suru verbs (4)**: {祝福|しゅくふく} (blessing), {祈願|きがん} (supplication), {移住|いじゅう} (migration), {突破|とっぱ} (breakthrough)
- **Noun/na-adjectives (3)**: {神秘|しんぴ} (mystery/mystique), {究極|きゅうきょく} (ultimate), {確立|かくりつ} (establishment)
- **Na-adjective (1)**: {神聖|しんせい} (sacred)
- **Ichidan verbs (3)**: {禁|きん}じる (to prohibit), {秀|ひい}でる (to excel), {称|たた}える (to praise)
- **I-adjective (1)**: {禍々|まがまが}しい (ominous/sinister)
- **Noun/suru verb (1)**: {目礼|もくれい} (silent nod)
- **Adverb (1)**: {目|ま}の{当|あ}たり (before one's eyes)
- **Cultural noun (1)**: {神隠|かみかく}し (spiriting away)

Notable features:
- Multi-sense entries: {禁|きん}じる (2: prohibit + suppress emotion), {突破|とっぱ} (2: break through + surpass number)
- Cultural: {神隠|かみかく}し (folklore, Studio Ghibli), {神棚|かみだな} (household worship), {秋刀魚|さんま} (autumn cuisine icon), {社会人|しゃかいじん} (life stage concept)
- Modern/colloquial: {社畜|しゃちく} (internet slang for overworked employees)
- Religion cluster: {祈|いの}り, {祝福|しゅくふく}, {神秘|しんぴ}, {神聖|しんせい}, {祈願|きがん}, {祭壇|さいだん}, {神棚|かみだな}
- Business cluster: {社会人|しゃかいじん}, {社内|しゃない}, {社畜|しゃちく}, {社交|しゃこう} (indirectly)
- Homophone notes: {確立|かくりつ}↔{確率|かくりつ}, {福祉|ふくし}↔{副詞|ふくし}, {秘訣|ひけつ}↔{否決|ひけつ}
- New kanji: 2,423 → 2,427 ({祉|し}, {禍|か}, {聖|せい}, {訣|けつ})

Total entries: 13,784 → 13,814 (approximate)
Remaining candidates: 5,985 → 5,955 (30 removed)

### 2026-02-26 (Vocabulary Expansion - 30 New Entries, Session 331)
Added 30 new dictionary entries (IDs 13699-13728) from candidate_words.json:

- **Nouns (12)**: {真意|しんい} (true intention), {省庁|しょうちょう} (government ministries), {着想|ちゃくそう} (idea/inspiration), {異物|いぶつ} (foreign body), {画集|がしゅう} (art book), {白玉|しらたま} (rice flour dumpling), {砂粒|すなつぶ} (grain of sand), {番茶|ばんちゃ} (coarse green tea), {石碑|せきひ} (stone monument), {矜持|きょうじ} (pride/dignity), {碁盤|ごばん} (go board), {異国|いこく} (foreign land)
- **Na-adjectives (2)**: {知的|ちてき} (intellectual), {盲目|もうもく} (blind)
- **Noun/no-adjective (3)**: {直近|ちょっきん} (most recent), {略式|りゃくしき} (informal), {異形|いぎょう} (monstrous form)
- **Noun/suru verbs (6)**: {直結|ちょっけつ} (direct connection), {発汗|はっかん} (sweating), {確定|かくてい} (finalization), {着色|ちゃくしょく} (coloring), {直撃|ちょくげき} (direct hit), {直談判|じかだんぱん} (direct negotiation)
- **Taru-adjective (1)**: {確固|かっこ} (firm/unwavering)
- **Godan verbs (2)**: {白|しら}む (to grow light at dawn), {着古|きふる}す (to wear out clothing)
- **Ichidan verb (1)**: {登|のぼ}り{詰|つ}める (to climb to the top)
- **Noun/na-adjective (3)**: {相対|そうたい} (relative), {相応|そうおう} (suitable), {硬化|こうか} (hardening)

Notable features:
- Multi-sense entries: {知的|ちてき} (2: intellectual + intelligent-looking), {直近|ちょっきん} (2: temporal + spatial), {白|しら}む (2: dawn + pallor), {登|のぼ}り{詰|つ}める (2: physical + figurative), {盲目|もうもく} (2: literal + figurative blindness)
- Cultural: {碁盤|ごばん}の{目|め} (Kyoto grid pattern), {番茶|ばんちゃ} (everyday tea culture, proverb), {白玉|しらたま} (wagashi ingredient)
- Literary: {白|しら}む (poetic dawn), {矜持|きょうじ} (elevated pride), {異国|いこく} (evocative foreign land), {確固|かっこ}たる (formal resolve)
- Practical: {確定|かくてい}{申告|しんこく} (tax returns), {省庁|しょうちょう} (Japanese government structure), {直撃|ちょくげき}インタビュー (journalism)
- New kanji: 2,421 → 2,423 ({矜|きん}, {碑|ひ})

Total entries: 13,754 → 13,784 (approximate)
Remaining candidates: 6,015 → 5,985 (30 removed)

### 2026-02-26 (Vocabulary Expansion - 30 New Entries, Session 330)
Added 30 new dictionary entries (IDs 13669-13698) from candidate_words.json:

- **Nouns (13)**: {矢印|やじるし} (arrow sign), {眠|ねむ}り (sleep), {短冊|たんざく} (tanzaku strip), {白湯|さゆ} (plain hot water), {盃|さかずき} (sake cup), {硫黄|いおう} (sulfur), {白書|はくしょ} (white paper), {白身|しろみ} (white meat/egg white), {直球|ちょっきゅう} (fastball/directness), {知性|ちせい} (intelligence), {盛|も}り (food serving), {盛|も}り{上|あ}がり (excitement), {知見|ちけん} (knowledge/findings)
- **Na-adjective (1)**: {真摯|しんし} (sincere)
- **I-adjectives (1)**: {真新|まあたら}しい (brand new)
- **Noun/suru verbs (7)**: {破壊|はかい} (destruction), {破損|はそん} (damage), {確保|かくほ} (securing), {確信|かくしん} (conviction), {着用|ちゃくよう} (wearing), {登壇|とうだん} (taking the stage), {直視|ちょくし} (looking squarely), {発声|はっせい} (vocalization)
- **Ichidan verbs (3)**: {睨|にら}みつける (to glare at), {着|き}せる (to dress someone), {痛|いた}めつける (to torment)
- **Godan verb (1)**: {研|と}ぎ{澄|す}ます (to hone/sharpen)
- **Multi-sense noun (3)**: {目覚|めざ}め (2: waking + figurative awakening), {目前|もくぜん} (2: before eyes + imminent), {真髄|しんずい} (1: essence)

Notable features:
- Multi-sense entries: {破壊|はかい} (2: physical + figurative destruction), {着|き}せる (2: dress someone + place blame), {直球|ちょっきゅう} (2: fastball + being direct), {白身|しろみ} (2: white fish + egg white), {目覚|めざ}め (2: waking + awakening), {目前|もくぜん} (2: before eyes + imminent), {盛|も}り{上|あ}がり (2: excitement + physical swell)
- Cultural: {短冊|たんざく} (Tanabata strips), {盃|さかずき} (ceremonial sake cups, {三々九度|さんさんくど}), {白湯|さゆ} (health trend)
- Homophone cross-refs: {確信|かくしん}↔{核心|かくしん}↔{革新|かくしん}, {発声|はっせい}↔{発生|はっせい}, {破損|はそん}↔{破壊|はかい} (contrast)
- New kanji: 2,418 → 2,421 ({摯|し}, {盃|はい}, {硫|りゅう})

Total entries: 13,724 → 13,754 (approximate)
Remaining candidates: 6,045 → 6,015 (30 removed)

### 2026-02-26 (Vocabulary Expansion - 30 New Entries, Session 329)
Added 30 new dictionary entries (IDs 13639-13668) from candidate_words.json:

- **発- cluster (3)**: {発|はっ}する (to emit/issue), {発効|はっこう} (taking effect), {発足|ほっそく} (inauguration)
- **直- cluster (3)**: {直前|ちょくぜん} (just before), {直面|ちょくめん} (confronting), {直通|ちょくつう} (direct connection)
- **目- cluster (3)**: {目当|めあ}て (aim/attraction), {目玉|めだま} (eyeball/highlight), {目線|めせん} (gaze/perspective)
- **盛- cluster (2)**: {盛大|せいだい} (grand), {盛況|せいきょう} (great turnout)
- **監- cluster (2)**: {監修|かんしゅう} (editorial supervision), {監禁|かんきん} (confinement)
- **相- cluster (2)**: {相性|あいしょう} (compatibility), {相殺|そうさい} (offset)
- **真- cluster (3)**: {真|ま}っ{最中|さいちゅう} (right in the middle of), {真心|まごころ} (sincerity), {真顔|まがお} (straight face)
- **Ichidan verb (1)**: {省|かえり}みる (to reflect on)
- **Suru verbs (4)**: {瞑想|めいそう} (meditation), {着目|ちゃくもく} (attention), {短縮|たんしゅく} (shortening), {疾走|しっそう} (sprint)
- **Time nouns (2)**: {瞬時|しゅんじ} (instant), {矢先|やさき} (just when)
- **Other nouns (3)**: {白黒|しろくろ} (black and white), {皮切|かわき}り (starting with), {知名度|ちめいど} (name recognition)
- **Household (1)**: {皿洗|さらあら}い (dishwashing)
- **Medical (1)**: {看護|かんご} (nursing)

Notable features:
- Multi-sense entries: {白黒|しろくろ} (2: monochrome + right/wrong), {目当|めあ}て (2: aim + attraction), {目玉|めだま} (2: eyeball + highlight), {目線|めせん} (2: gaze + perspective), {発|はっ}する (2: emit + issue)
- Thematic clusters: 直- (3 entries), 目- (3 entries), 真- (3 entries)
- Homophone cross-refs: {発効|はっこう}↔{発行|はっこう}↔{発酵|はっこう}, {監修|かんしゅう}↔{慣習|かんしゅう}, {相性|あいしょう}↔{愛称|あいしょう}, {瞑想|めいそう}↔{迷走|めいそう}, {疾走|しっそう}↔{失踪|しっそう}, {看護|かんご}↔{漢語|かんご}
- Etymology: {皮切|かわき}り (from moxibustion), {矢先|やさき} (from arrowhead)
- New kanji: 2,416 → 2,418 ({疾|しつ}, {瞑|めい})

Total entries: 13,694 → 13,724 (approximate)
Remaining candidates: 6,075 → 6,045 (30 removed)

### 2026-02-26 (Vocabulary Expansion - 30 New Entries, Session 328)
Added 30 new dictionary entries (IDs 13609-13638) from candidate_words.json:

- **Health/illness cluster (7)**: {疫病|えきびょう} (epidemic), {病|やまい} (illness), {病|や}む (to be ill), {病弱|びょうじゃく} (sickly), {痛|いた}める (to hurt), {痛感|つうかん} (keenly feeling), {療法|りょうほう} (therapy)
- **Healing (1)**: {癒|いや}す (to heal)
- **四字熟語 (1)**: {疲労困憊|ひろうこんぱい} (total exhaustion)
- **Cognition/language (3)**: {目撃|もくげき} (witnessing), {直訳|ちょくやく} (literal translation), {疑似|ぎじ} (pseudo/simulated)
- **Descriptive (2)**: {目覚|めざま}ましい (remarkable), {盛大|せいだい} → replaced by {発祥|はっしょう} (origin/birthplace)
- **Food (2)**: {田楽|でんがく} (dengaku), ラード (lard)
- **People (3)**: {猛者|もさ} (tough guy), {痴漢|ちかん} (groper), {王妃|おうひ} (queen consort)
- **General nouns (4)**: {物販|ぶっぱん} (merchandise sales), {法|ほう} (law/method), {渡|わた}り (crossing), {白紙|はくし} (blank paper/clean slate)
- **Scene/stage (1)**: {登場|とうじょう} (appearance/entrance)
- **Loanwords (5)**: ライト (light), リストアップ (listing), レーベル (music label), リニア (maglev), ファクス (fax)
- **Person (1)**: レディ (lady)

Notable features:
- Health/illness cluster: 7 related entries covering epidemic, illness, constitution, pain, therapy
- Multi-sense entries: {病|やまい} (2: illness + bad habit), {病|や}む (2: physical + mental), {痛|いた}める (2: physical + emotional), {癒|いや}す (2: heal + soothe), ライト (2: light device + casual), {白紙|はくし} (2: blank paper + clean slate), {法|ほう} (2: law + method), {渡|わた}り (2: crossing + opportunity), レーベル (2: music label + product label), リニア (2: maglev + linear)
- Cultural: {痴漢|ちかん} (women-only train cars), ファクス (Japan's fax culture), {田楽|でんがく} (traditional cuisine), ラード (ramen culture)
- Wasei-eigo: リストアップ (list up — not standard English)
- Modern slang: {病|や}んでる (mentally unwell, youth language)
- New kanji: 2,413 → 2,416 ({妃|ひ}, {憊|はい}, {祥|しょう})

Total entries: 13,664 → 13,694 (approximate)
Remaining candidates: 6,105 → 6,075 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
