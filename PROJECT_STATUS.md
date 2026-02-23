# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-23
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
| Total entries | ~13,154 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~10,355 (open) |
| Candidate words | ~523 |
| Cross-references | ~3,400 |
| Example sentences | ~45,810 |
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

### 2026-02-23 (Vocabulary Expansion - 30 New Entries, Session 310)
Added 30 new dictionary entries (IDs 13069-13098) from candidate_words.json:

- **Nouns (13)**: {文言|もんごん} (wording), {文様|もんよう} (pattern/design), {月間|げっかん} (monthly period), {有事|ゆうじ} (emergency), {朝廷|ちょうてい} (imperial court), {木星|もくせい} (Jupiter), {未遂|みすい} (attempted crime), {晩春|ばんしゅん} (late spring), {晩餐会|ばんさんかい} (banquet), {暖流|だんりゅう} (warm current), {曲目|きょくもく} (musical piece), {明細書|めいさいしょ} (detailed statement), {本殿|ほんでん} (main shrine building)
- **Noun/no-adjective (5)**: {最強|さいきょう} (strongest), {最短|さいたん} (shortest), {最速|さいそく} (fastest), {最長|さいちょう} (longest), {有形|ゆうけい} (tangible), {木製|もくせい} (wooden)
- **Noun/adverb (2)**: {最大限|さいだいげん} (maximum), {最小限|さいしょうげん} (minimum)
- **Na-adjective (1)**: {有用|ゆうよう} (useful)
- **Adverb (1)**: {末永|すえなが}く (for a long time)
- **Noun/prefix (2)**: {日米|にちべい} (Japan-US), {時限|じげん} (time limit/timed)
- **Noun/suru verb (1)**: {本格化|ほんかくか} (getting into full swing)
- **Nouns (3)**: {本家|ほんけ} (main family/originator), {本拠地|ほんきょち} (headquarters), {村長|そんちょう} (village chief), {未然|みぜん} (prevention)

Notable features:
- 最- superlative cluster: {最大限|さいだいげん}, {最小限|さいしょうげん}, {最強|さいきょう}, {最短|さいたん}, {最速|さいそく}, {最長|さいちょう}
- Antonym pairs: {最大限|さいだいげん}↔{最小限|さいしょうげん}, {最短|さいたん}↔{最長|さいちょう}
- Homophone pairs: {木星|もくせい}↔{木製|もくせい}, {最速|さいそく}↔{催促|さいそく}, {村長|そんちょう}↔{尊重|そんちょう}
- Multi-sense entries: {本家|ほんけ} (main family/originator), {時限|じげん} (class period/timed prefix)
- Cultural: {朝廷|ちょうてい} (imperial court), {本殿|ほんでん} (Shinto shrine), {晩餐会|ばんさんかい} (state dinners), {晩春|ばんしゅん} (Ozu film)
- New kanji: 2,384 → 2,385 ({餐|さん})

Total entries: 13,124 → 13,154 (approximate)
Remaining candidates: 553 → 523 (30 removed)

### 2026-02-23 (Vocabulary Expansion - 30 New Entries, Session 309)
Added 30 new dictionary entries (IDs 13039-13068) from candidate_words.json:

- **Nouns/counters (3)**: {台|だい} (stand/counter for machines), {号|ごう} (number/issue), {和|わ} (harmony/Japanese-style)
- **Na-adjective (1)**: {急|きゅう} (sudden/steep/urgent)
- **Nouns (12)**: {恒星|こうせい} (star), {新春|しんしゅん} (New Year), {方位|ほうい} (direction/bearing), {旧正月|きゅうしょうがつ} (Lunar New Year), {書記|しょき} (secretary/clerk), {最低限|さいていげん} (minimum), {最前線|さいぜんせん} (forefront), {最盛期|さいせいき} (peak period), {来客|らいきゃく} (visitor), {村人|むらびと} (villager), {木工|もっこう} (woodworking), {末尾|まつび} (tail end)
- **Noun/suru verbs (6)**: {改訂|かいてい} (revision of text), {明文化|めいぶんか} (codification), {明言|めいげん} (clear statement), {新調|しんちょう} (getting new), {来日|らいにち} (coming to Japan), {来店|らいてん} (visiting a store)
- **Noun/na-adj (1)**: {未完成|みかんせい} (incomplete)
- **Noun (2)**: {本文|ほんぶん} (main text), {書|か}き{方|かた} (way of writing)
- **Verbs (5)**: {映|うつ}し{出|だ}す (to project/reflect, godan), {書|か}き{入|い}れる (to write in, ichidan), {書|か}き{出|だ}す (to begin writing/list out, godan), {束|たば}ねる (to bundle/lead, ichidan), {明|あ}け{暮|く}れる (to be absorbed in, ichidan)

Notable features:
- Multi-sense entries: {台|だい} (stand/counter), {号|ごう} (issue/designation), {和|わ} (harmony/Japanese-style), {急|きゅう} (sudden/steep/urgent), {映|うつ}し{出|だ}す (project/portray), {書|か}き{出|だ}す (begin writing/list out), {束|たば}ねる (bundle/lead)
- Homophone distinction: {改訂|かいてい} (text) vs {改定|かいてい} (standards)
- 最- prefix cluster: {最低限|さいていげん}, {最前線|さいぜんせん}, {最盛期|さいせいき}
- 来- pattern cluster: {来日|らいにち}, {来客|らいきゃく}, {来店|らいてん}
- 書き- compound cluster: {書|か}き{入|い}れる, {書|か}き{出|だ}す, {書|か}き{方|かた}
- Cultural: {和|わ} (Japanese-style prefix), {新春|しんしゅん} (New Year), {旧正月|きゅうしょうがつ} (Lunar New Year)

Total entries: 13,094 → 13,124 (approximate)
Remaining candidates: 583 → 553 (30 removed)

### 2026-02-23 (Vocabulary Expansion - 30 New Entries, Session 308)
Added 30 new dictionary entries (IDs 13009-13038) from candidate_words.json:

- **Na-adjectives (5)**: {最終的|さいしゅうてき} (final/ultimate), {普遍的|ふへんてき} (universal), {晴|は}れやか (bright/radiant), {最適|さいてき} (optimal), {最悪|さいあく} (worst/terrible)
- **Na-adjective/nouns (3)**: {未熟|みじゅく} (immature/unripe), {有意義|ゆういぎ} (meaningful), {慣用|かんよう} (idiomatic)
- **Nouns (13)**: {最先端|さいせんたん} (cutting edge), {最優先|さいゆうせん} (top priority), {未成年|みせいねん} (minor), {木材|もくざい} (timber), {木|き}の{実|み} (nut/berry), {有無|うむ} (presence or absence), {有権者|ゆうけんしゃ} (voter), {有識者|ゆうしきしゃ} (expert), {書面|しょめん} (written document), {書体|しょたい} (typeface), {暴力団|ぼうりょくだん} (crime syndicate), {新芽|しんめ} (new bud), {末期|まっき} (final stage)
- **Noun/no-adjective (1)**: {未知|みち} (unknown)
- **Noun/suru verbs (4)**: {新設|しんせつ} (new establishment), {明記|めいき} (clearly stating), {明示|めいじ} (explicit indication), {改定|かいてい} (revision of standards)
- **Nouns (3)**: {本体|ほんたい} (main body), {本名|ほんみょう} (real name), {放射能|ほうしゃのう} (radioactivity)
- **Noun (1)**: {支|ささ}え (support)

Notable features:
- Multi-sense entries: {最悪|さいあく} (worst/terrible exclamation), {未熟|みじゅく} (inexperienced/unripe), {本体|ほんたい} (main unit/true form)
- 最- prefix cluster: {最悪|さいあく}, {最適|さいてき}, {最先端|さいせんたん}, {最優先|さいゆうせん}, {最終的|さいしゅうてき}
- 未- prefix cluster: {未知|みち}, {未熟|みじゅく}, {未成年|みせいねん}
- Formal/written: {書面|しょめん}, {明記|めいき}, {明示|めいじ}, {有権者|ゆうけんしゃ}, {有識者|ゆうしきしゃ}
- Homophone distinction: {改定|かいてい} (standards/prices) vs {改訂|かいてい} (text)
- New kanji: 2,383 → 2,384 ({遍|へん})

Total entries: 13,064 → 13,094 (approximate)
Remaining candidates: 363 → 333 (30 removed)

### 2026-02-23 (Vocabulary Expansion - 30 New Entries, Session 307)
Added 30 new dictionary entries (IDs 12979-13008) from candidate_words.json:

- **Noun/suru verbs (4)**: {戦死|せんし} (death in battle), {断絶|だんぜつ} (severance), {暗躍|あんやく} (secret maneuvering), {早寝|はやね} (going to bed early)
- **Nouns (16)**: {戦時|せんじ} (wartime), {新婦|しんぷ} (bride), {新郎|しんろう} (groom), {新曲|しんきょく} (new song), {新着|しんちゃく} (new arrival), {旅立|たびだ}ち (departure), {旅路|たびじ} (journey), {文豪|ぶんごう} (literary master), {文芸|ぶんげい} (literary art), {文語|ぶんご} (literary language), {昼夜|ちゅうや} (day and night), {晴|は}れ{着|ぎ} (formal clothes), {月収|げっしゅう} (monthly income), {月極|つきぎめ} (monthly rental), {月見|つきみ} (moon viewing), {朝市|あさいち} (morning market)
- **Na-adjective/nouns (5)**: {月並|つきな}み (commonplace), {有害|ゆうがい} (harmful), {有罪|ゆうざい} (guilty), {有益|ゆうえき} (beneficial), {有力|ゆうりょく} (influential)
- **Noun/pre-noun adjectival (1)**: {有数|ゆうすう} (prominent)
- **Nouns (2)**: {有志|ゆうし} (volunteers), {暗黒|あんこく} (darkness)
- **Adverb (1)**: {早晩|そうばん} (sooner or later)
- **Verb (1)**: {施|ほどこ}す (to apply/to give charity, godan)

Notable features:
- Multi-sense entries: {施|ほどこ}す (apply/give charity), {暗黒|あんこく} (physical darkness/figurative darkness), {有力|ゆうりょく} (influential/strong candidate), {月見|つきみ} (moon viewing/egg on food)
- Wedding pair: {新郎|しんろう} ↔ {新婦|しんぷ}
- Travel cluster: {旅立|たびだ}ち, {旅路|たびじ} (literary terms)
- Literature cluster: {文豪|ぶんごう}, {文芸|ぶんげい}, {文語|ぶんご}
- 有- prefix cluster: {有害|ゆうがい}, {有罪|ゆうざい}, {有益|ゆうえき}, {有志|ゆうし}, {有数|ゆうすう}, {有力|ゆうりょく}
- Cultural: {月見|つきみ} (autumn tradition + food), {晴|は}れ{着|ぎ} (hare/ke distinction), {朝市|あさいち} (Japanese market tradition)
- New kanji: 2,382 → 2,383 ({郎|ろう})

Total entries: 13,034 → 13,064 (approximate)
Remaining candidates: 393 → 363 (30 removed)

### 2026-02-22 (Vocabulary Expansion - 30 New Entries, Session 306)
Added 30 new dictionary entries (IDs 12949-12978) from candidate_words.json:

- **Nouns (20)**: {旅先|たびさき} (travel destination), {旅客|りょかく} (passenger), {日取|ひど}り (scheduling a date), {日数|にっすう} (number of days), {日本酒|にほんしゅ} (Japanese sake), {日本食|にほんしょく} (Japanese food), {日系|にっけい} (of Japanese descent), {旧姓|きゅうせい} (maiden name), {旧暦|きゅうれき} (lunar calendar), {明|あか}るみ (coming to light), {昨今|さっこん} (nowadays), {昼過|ひるす}ぎ (early afternoon), {時事|じじ} (current affairs), {時代劇|じだいげき} (period drama), {時価|じか} (market price), {時点|じてん} (point in time), {時間帯|じかんたい} (time slot/time zone), {晴天|せいてん} (clear sky), {暑|あつ}さ (heat), {景観|けいかん} (landscape)
- **Verbs (4)**: {旅立|たびだ}つ (to depart on journey, godan), {昇|のぼ}る (to rise, godan), {明|あ}かす (to reveal/stay up all night, godan), {映|うつ}す (to reflect/project, godan)
- **Intransitive verb (1)**: {映|うつ}る (to be reflected/appear, godan)
- **Adverbs (2)**: {早々|そうそう} (promptly/right after), {暗|あん}に (implicitly)
- **Noun (1)**: {暴言|ぼうげん} (abusive language)
- **Expression (1)**: {敬具|けいぐ} (respectfully yours)
- **Noun (1)**: {教義|きょうぎ} (doctrine)

Notable features:
- Multi-sense entries: {旅立|たびだ}つ (journey/euphemism for death), {明|あ}かす (reveal/stay up all night), {映|うつ}す (reflect/project), {映|うつ}る (reflected/appear on screen), {早々|そうそう} (promptly/suffix: right after), {時間帯|じかんたい} (time slot/time zone)
- Transitive-intransitive pair: {映|うつ}す ↔ {映|うつ}る
- Homophone notes: {昇|のぼ}る vs {登|のぼ}る, {暑|あつ}さ vs {厚|あつ}さ vs {熱|あつ}さ, {映|うつ}す vs {写|うつ}す vs {移|うつ}す
- Cultural: {日本酒|にほんしゅ} (brewing terms), {旧暦|きゅうれき} (Meiji calendar reform), {旧姓|きゅうせい} (夫婦別姓 debate), {敬具|けいぐ} (letter writing conventions), {時代劇|じだいげき} (大河ドラマ)
- Time/日-related cluster: many entries built around 日, 時, 旧, 早, 昼, 明, 映, 昨, 晴, 暑, 暗, 暴, 景

Total entries: 13,004 → 13,034 (approximate)
Remaining candidates: 423 → 393 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
