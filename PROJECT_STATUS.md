# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-27
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
| Total entries | ~13,874 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~11,075 (open) |
| Candidate words | ~5,895 |
| Cross-references | ~3,400 |
| Example sentences | ~47,700 |
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

### 2026-02-27 (Vocabulary Expansion - 30 New Entries, Session 334)
Added 30 new dictionary entries (IDs 13789-13818) from candidate_words.json:

- **Na-adjectives (4)**: {細|こま}やか (attentive/detailed), {簡易|かんい} (simple/simplified), {絶妙|ぜつみょう} (exquisite/superb), {緩|ゆる}やか (gentle/gradual)
- **Nouns (15)**: {細工|さいく} (craftsmanship), {細菌|さいきん} (bacteria), {紺色|こんいろ} (navy blue), {終盤|しゅうばん} (final stage), {組|く}み{合|あ}わせ (combination), {経歴|けいれき} (career history), {経路|けいろ} (route/path), {結晶|けっしょう} (crystal), {結束|けっそく} (unity), {給食|きゅうしょく} (school lunch), {素顔|すがお} (bare face), {立地|りっち} (location), {紅白|こうはく} (red and white), {納税|のうぜい} (tax payment), {素手|すで} (bare hands)
- **Noun/suru verbs (5)**: {絶叫|ぜっきょう} (scream), {結成|けっせい} (formation), {目視|もくし} (visual inspection), plus above entries that also function as suru verbs
- **Nouns (other) (3)**: {絶品|ぜっぴん} (superb item), {罠|わな} (trap), {続編|ぞくへん} (sequel)
- **Noun/adverb (1)**: {終日|しゅうじつ} (all day)
- **Godan verbs (2)**: {結|むす}びつく (to be connected), {紡|つむ}ぐ (to spin thread)
- **Ichidan verb (1)**: {絶|た}える (to cease/die out)

Notable features:
- Multi-sense entries: {細工|さいく} (2: craftsmanship + trickery), {経路|けいろ} (2: physical route + abstract channel), {結晶|けっしょう} (2: crystal + fruit of effort), {紅白|こうはく} (2: colors + team competition), {素顔|すがお} (2: bare face + true character), {罠|わな} (2: animal trap + scheme), {絶|た}える (2: cease + die out), {緩|ゆる}やか (2: gentle + loose), {細|こま}やか (2: attentive + warm/rich)
- Cultural: {紅白|こうはく} (NHK紅白歌合戦), {給食|きゅうしょく} (Japanese school lunch system), {縁起|えんぎ} (luck/omens in Japanese culture), {紺色|こんいろ} (traditional indigo dyeing)
- Literary: {紡|つむ}ぐ (modern metaphorical usage for weaving stories/bonds)
- Practical: {経歴|けいれき} (job applications), {納税|のうぜい} (ふるさと納税), {立地|りっち} (real estate), {目視|もくし} (workplace safety)
- New kanji: 2,428 → 2,430 ({紡|ぼう}, {罠|わな})

Total entries: 13,844 → 13,874 (approximate)
Remaining candidates: 5,925 → 5,895 (30 removed)

### 2026-02-27 (Vocabulary Expansion - 30 New Entries, Session 333)
Added 30 new dictionary entries (IDs 13759-13788) from candidate_words.json:

- **Ichidan verbs (2)**: {秘|ひ}める (to keep secret), {築|きず}き{上|あ}げる (to build up)
- **Godan verb (1)**: {競|きそ}う (to compete)
- **Noun/suru verbs (6)**: {移植|いしょく} (transplant), {移行|いこう} (transition), {突入|とつにゅう} (rushing in), {立候補|りっこうほ} (candidacy), {移籍|いせき} (transfer), {精進|しょうじん} (devotion)
- **Nouns (11)**: {移|うつ}り{変|か}わり (change over time), {空耳|そらみみ} (mishearing), {窯|かま} (kiln), {竜|りゅう} (dragon), {笑|え}み (smile), {節度|せつど} (moderation), {米粉|こめこ} (rice flour), {粉末|ふんまつ} (powder), {秘伝|ひでん} (secret tradition), {税務署|ぜいむしょ} (tax office), {策略|さくりゃく} (stratagem)
- **Na-adjectives (4)**: {粋|いき} (stylish/chic), {精密|せいみつ} (precise), {突飛|とっぴ} (outlandish), {端的|たんてき} (straightforward), {稀有|けう} (rare)
- **Nouns (3)**: {精度|せいど} (precision), {簿記|ぼき} (bookkeeping), {精一杯|せいいっぱい} (to the fullest)
- **Adverbs (2)**: {突如|とつじょ} (suddenly), {立|た}て{続|つづ}け (in succession)

Notable features:
- Multi-sense entries: {移植|いしょく} (2: organ transplant + plant/software porting), {突入|とつにゅう} (2: physical charge + entering a phase), {粋|いき} (2: stylish + considerate), {精進|しょうじん} (2: devotion + vegetarian cuisine)
- Cultural: {粋|いき} (Edo aesthetic), {竜|りゅう} (East Asian dragon mythology), {精進|しょうじん} (Buddhist practice), {窯|かま} (pottery culture), {空耳|そらみみ} (Soramimi Hour TV segment)
- Practical: {税務署|ぜいむしょ} (tax filing), {簿記|ぼき} (Nissho certification), {精度|せいど} (AI/tech accuracy), {移行|いこう} (system migration)
- Literary: {秘|ひ}める, {笑|え}み, {稀有|けう}, {突如|とつじょ}
- New kanji: 2,427 → 2,428 ({窯|かま})

Total entries: 13,814 → 13,844 (approximate)
Remaining candidates: 5,955 → 5,925 (30 removed)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
