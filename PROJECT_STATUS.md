# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-17
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
| Total entries | ~11,780 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~8,981 (open) |
| Candidate words | ~390 |
| Cross-references | ~3,350 |
| Example sentences | ~43,400 |
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

### 2026-02-17 (Vocabulary Expansion - 30 New Entries, Session 265)
Added 30 new dictionary entries (IDs 11695-11724) from candidate_words.json:

- **Loanwords - nouns (10)**: チュートリアル (tutorial), ファンタジー (fantasy), フィットネス (fitness), フェスティバル (festival), プレート (plate), レーダー (radar), ロール (roll/role), パッケージ (package), リアリティ (reality), ピックアップ (pickup/selection)
- **Loanwords - na-adjective (1)**: ポピュラー (popular)
- **Loanwords - noun/suru verb (3)**: スカウト (scouting/recruiting), トライ (try/attempt), リベラル (liberal)
- **Japanese nouns - formal/historical (6)**: {主君|しゅくん} (feudal lord), {伯爵|はくしゃく} (count/earl), {俗称|ぞくしょう} (colloquial name), {亡骸|なきがら} (remains/corpse), {不死|ふし} (immortality), {下位|かい} (lower rank)
- **Japanese nouns - general (5)**: {今日|こんにち} (today/nowadays), {交友|こうゆう} (friendship), {人力|じんりき} (manpower), {人工衛星|じんこうえいせい} (artificial satellite), {付加価値|ふかかち} (added value)
- **Japanese nouns - counter (1)**: {件|けん} (matter/case; counter for cases)
- **Japanese nouns - cultural (1)**: {仲居|なかい} (ryokan attendant)
- **Nouns - warfare (1)**: {交戦|こうせん} (battle/engagement)
- **Verbs (2)**: {代|か}える (to substitute), {代|か}わる (to take the place of)

Notable features:
- Good mix of katakana loanwords (14) and native Japanese words (16)
- Multi-sense entries: トライ (attempt/rugby try), パッケージ (packaging/package deal), プレート (dish/metal plate), ファンタジー (genre/daydream), ロール (roll/role), リアリティ (realism/reality TV), ピックアップ (selection/pickup), {件|けん} (matter/counter), {今日|こんにち} (today/nowadays)
- Transitive/intransitive pair: {代|か}える ↔ {代|か}わる
- Homophone cross-references: {今日|こんにち} ↔ {今日|きょう}, {不死|ふし} ↔ {節|ふし}, {交戦|こうせん} ↔ {光線|こうせん}
- Cultural context: {仲居|なかい} (ryokan hospitality), {伯爵|はくしゃく} (Meiji peerage system)
- New kanji: 2,314 → 2,318 ({伯|はく}, {俗|ぞく}, {爵|しゃく}, {称|しょう})

Total entries: 11,750 → 11,780
Remaining candidates: 420 → 390 (30 removed)

### 2026-02-17 (Vocabulary Expansion - 30 New Entries, Session 264)
Added 30 new dictionary entries (IDs 11665-11694) from candidate_words.json:

- **Nouns/suru verbs - joining/membership (4)**: {入会|にゅうかい} (enrollment), {入部|にゅうぶ} (joining school club), {入賞|にゅうしょう} (winning a prize), {入選|にゅうせん} (being selected for exhibition)
- **Nouns/suru verbs - society/diplomacy (5)**: {公開|こうかい} (release to public), {共有|きょうゆう} (sharing), {共存|きょうぞん} (coexistence), {共生|きょうせい} (symbiosis), {共演|きょうえん} (co-starring)
- **Nouns/suru verbs - technical/formal (3)**: {作動|さどう} (operation of machinery), {併設|へいせつ} (attached facility), {伝来|でんらい} (introduction from abroad)
- **Nouns - formal (6)**: {公文書|こうぶんしょ} (official document), {公用語|こうようご} (official language), {兵器|へいき} (weapon), {兵士|へいし} (soldier), {使節|しせつ} (envoy), {共犯|きょうはん} (accomplice)
- **Nouns - general (5)**: {全文|ぜんぶん} (full text), {全米|ぜんべい} (all of America), {円形|えんけい} (circular shape), {付|つ}け{根|ね} (base/root), {先住民|せんじゅうみん} (indigenous people)
- **Nouns - abstract (3)**: {内心|ないしん} (inwardly), {内面|ないめん} (inner feelings), {何者|なにもの} (who/what kind of person)
- **Verb (1)**: {兼|か}ねる (to serve as both / unable to)
- **Adverb (1)**: {再度|さいど} (once more, again)
- **Cultural (1)**: {侘|わ}び{寂|さ}び (wabi-sabi aesthetic)
- **Noun/suru verb (1)**: {再会|さいかい} (reunion)

Notable features:
- Multi-sense entries: {兼|か}ねる (serve as both / Vますかねる unable to), {内面|ないめん} (inner self / inner surface), {伝来|でんらい} (introduction from abroad / handed down through generations)
- Homophone notes: {公開|こうかい} vs {後悔|こうかい}/{航海|こうかい}, {再会|さいかい} vs {再開|さいかい}, {兵器|へいき} vs {平気|へいき}, {作動|さどう} vs {茶道|さどう}, {使節|しせつ} vs {施設|しせつ}
- Distinction pairs: {共存|きょうぞん} vs {共生|きょうせい}, {入賞|にゅうしょう} vs {入選|にゅうせん}, {内心|ないしん} vs {内面|ないめん}
- Cultural context: {侘|わ}び{寂|さ}び (tea ceremony, haiku, Zen aesthetics), {入部|にゅうぶ} (school club culture), {伝来|でんらい} (historical cultural exchange)
- New kanji: 2,313 → 2,314 ({兵|へい})

Total entries: 11,720 → 11,750
Remaining candidates: 450 → 420 (30 removed)

### 2026-02-17 (Vocabulary Expansion - 30 New Entries, Session 263)
Added 30 new dictionary entries (IDs 11635-11664) from candidate_words.json:

- **Nouns - formal/abstract (10)**: {事象|じしょう} (phenomenon), {全力|ぜんりょく} (full effort), {全盛期|ぜんせいき} (heyday), {全容|ぜんよう} (full picture), {個人差|こじんさ} (individual differences), {保安|ほあん} (security), {公衆|こうしゅう} (the public), {代名詞|だいめいし} (pronoun/byword), {元年|がんねん} (first year of era), {仕立|した}て (tailoring)
- **Nouns/suru verbs (10)**: {入手|にゅうしゅ} (obtaining), {全滅|ぜんめつ} (annihilation), {公演|こうえん} (public performance), {公表|こうひょう} (disclosure), {公認|こうにん} (official recognition), {入浴|にゅうよく} (bathing), {入門|にゅうもん} (introduction/becoming disciple), {先取|さきど}り (getting ahead), {修了|しゅうりょう} (course completion), {公約|こうやく} (campaign promise)
- **Na-adjectives (3)**: {人為的|じんいてき} (artificial), {人道的|じんどうてき} (humanitarian), {全体的|ぜんたいてき} (overall)
- **Nouns - social/political (3)**: {公共|こうきょう} (public), {信任|しんにん} (confidence/mandate), {付|つ}き{添|そ}い (attendant)
- **Verbs (4)**: {入|い}り{込|こ}む (to slip into/get absorbed), {全|まっと}うする (to accomplish), {介|かい}する (to mediate/not care about)

Notable features:
- Multi-sense entries: {入門|にゅうもん} (intro book/becoming disciple), {代名詞|だいめいし} (pronoun/byword), {入|い}り{込|こ}む (enter deeply/get absorbed), {元年|がんねん} (era year/inaugural year), {仕立|した}て (tailoring/style format), {介|かい}する (go through/mind)
- Homophone notes: {公演|こうえん} vs {公園|こうえん}, {修了|しゅうりょう} vs {終了|しゅうりょう}, {公共|こうきょう} vs {好況|こうきょう}
- Cross-references: {入|い}り{込|こ}む ↔ {入|はい}り{込|こ}む, {公演|こうえん} ↔ {公園|こうえん}
- Set phrases: {全力|ぜんりょく}を{尽|つ}くす, {意|い}に{介|かい}さない, {天寿|てんじゅ}を{全|まっと}うする
- Formal register variety: {公表|こうひょう}, {信任|しんにん}, {人道的|じんどうてき} alongside neutral {全力|ぜんりょく}, {個人差|こじんさ}

Total entries: 11,690 → 11,720
Remaining candidates: 480 → 450 (30 removed)

### 2026-02-17 (Vocabulary Expansion - 30 Mixed Entries, Session 262)
Added 30 new dictionary entries (IDs 11605-11634) from candidate_words.json:

- **Nouns - formal/abstract (9)**: {他者|たしゃ} (others), {住居|じゅうきょ} (dwelling), {侵攻|しんこう} (invasion), {保有|ほゆう} (possession), {保健|ほけん} (healthcare), {保湿|ほしつ} (moisturizing), {信憑性|しんぴょうせい} (credibility), {個々|ここ} (individual), {体現|たいげん} (embodiment)
- **Nouns - people/places (5)**: {仙人|せんにん} (hermit/sage), {令嬢|れいじょう} (young lady), {会長|かいちょう} (chairman), {住人|じゅうにん} (resident), {先進国|せんしんこく} (developed country)
- **Nouns - concrete/cultural (4)**: {代物|しろもの} (thing/article), {兜|かぶと} (samurai helmet), {備|そな}え (preparation), {作画|さくが} (artwork/animation)
- **Verbs (4)**: {入|い}り{混|ま}じる (to intermingle), {入|い}り{組|く}む (to be intricate), {入|い}れ{替|か}わる (to switch places), {作|つく}り{出|だ}す (to create)
- **Adjectives (2)**: {優美|ゆうび} (graceful), ストレート (straight/direct)
- **Adverbs (2)**: {今頃|いまごろ} (about now), {元来|がんらい} (originally)
- **Nouns - informal/loanwords (4)**: {兄貴|あにき} (big brother), {不動|ふどう} (immovable), スローガン (slogan), リアクション (reaction)

Notable features:
- Diverse POS mix: 20 nouns, 4 verbs, 2 adjectives, 2 adverbs, 2 loanwords
- Multi-sense entries: {今頃|いまごろ} (present time/too late), {作画|さくが} (artwork/animation quality), ストレート (straight/direct), {兄貴|あにき} (brother/respected figure), {入|い}れ{替|か}わる (switch places/be replaced), {作|つく}り{出|だ}す (create/generate atmosphere)
- Cultural context: {兜|かぶと} (Boys' Day display), {仙人|せんにん} (Taoist mythology), {令嬢|れいじょう} ({悪役令嬢|あくやくれいじょう} light novel genre), {作画|さくが} (anime criticism), リアクション (variety show comedy)
- Homophone notes: {保健|ほけん} vs {保険|ほけん}, {個々|ここ} vs ここ (here)
- New kanji: 2,310 → 2,313 ({仙|せん}, {兜|かぶと}, {憑|ひょう})

Total entries: 11,660 → 11,690
Remaining candidates: 510 → 480 (30 removed)

### 2026-02-17 (Vocabulary Expansion - 30 Loanword Entries, Session 261)
Added 30 new katakana loanword entries (IDs 11575-11604) from candidate_words.json:

- **Communication/tech (6)**: スルー (ignore/let pass), スペック (specs/personal attributes), スタンプ (stamp/LINE sticker), ステータス (status/prestige), リアルタイム (real-time), プラットフォーム (platform)
- **Places/structures (4)**: スポット (spot/location), スタジオ (studio), ハブ (hub), フレーム (frame)
- **Process/method (3)**: ステップ (step/phase), スライド (slide/presentation), モード (mode/fashion)
- **Sports/leisure (4)**: バット (bat), リーグ (league), リード (lead/leash), トレード (trade/exchange)
- **Business/work (4)**: スポンサー (sponsor), ポジション (position/role), ライセンス (license), ロジック (logic)
- **Objects/tools (3)**: ストック (stock/reserve), スプレー (spray), チューブ (tube), ポンプ (pump)
- **Media/appearance (3)**: ビジュアル (visual/appearance), メジャー (major/tape measure), ユニット (unit/group)
- **Other (3)**: テクノロジー (technology)

Notable features:
- All katakana loanwords, filling gaps in the dictionary's loanword coverage
- Multi-sense entries: スペック (tech specs/personal attributes), スタンプ (rubber stamp/LINE sticker), スポット (location/spotlight), ステータス (prestige/process status), スライド (presentation/sliding), メジャー (mainstream/tape measure), モード (English mode/French fashion), リード (lead advantage/leash), ユニット (module/performer group), プラットフォーム (station platform/digital platform), チューブ (squeeze tube/inner tube), ビジュアル (visual element/appearance)
- Wasei-eigo notes: スルー (through ≠ ignore in English), マナーモード (manner mode), {既読|きどく}スルー
- Cultural context: LINEスタンプ (mobile culture), スタンプラリー (stamp rallies), ユニットバス (Japanese housing), ビジュアル{系|けい} (visual kei music)
- Etymology notes: ポンプ (Dutch/Portuguese origin), モード (dual English/French etymology)

Total entries: 11,630 → 11,660
Remaining candidates: 540 → 510 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
