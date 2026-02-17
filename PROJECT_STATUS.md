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
| Total entries | ~11,690 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~8,891 (open) |
| Candidate words | ~480 |
| Cross-references | ~3,340 |
| Example sentences | ~43,300 |
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

### 2026-02-17 (Vocabulary Expansion - 30 New Entries, Session 260)
Added 30 new dictionary entries (IDs 11545-11574) from candidate_words.json:

- **Nouns - abstract/formal (12)**: {主題|しゅだい} (theme/subject), {付着|ふちゃく} (adhesion), {代替|だいたい} (substitution), {件名|けんめい} (subject line), {任期|にんき} (term of office), {併用|へいよう} (combined use), {伝達|でんたつ} (transmission), {侵害|しんがい} (infringement), {保全|ほぜん} (conservation), {体罰|たいばつ} (corporal punishment), {保養|ほよう} (recuperation), {不詳|ふしょう} (unknown)
- **Nouns - concrete/people (5)**: {位置|いち} (position/location), {住|す}まい (residence), {体内|たいない} (inside the body), {保護者|ほごしゃ} (guardian/parent), {信者|しんじゃ} (believer/devotee)
- **Nouns - general (5)**: {作|つく}り{話|ばなし} (fabricated story), {使|つか}い{分|わ}け (proper use), {個別|こべつ} (individual/case-by-case), {便箋|びんせん} (letter paper), {人工|じんこう} (artificial)
- **Verbs (3)**: {仕|つか}える (to serve), {供|そな}える (to offer), {作|つく}り{上|あ}げる (to build up/fabricate)
- **Adjective (1)**: {健在|けんざい} (alive and well)
- **Adverb/other (4)**: {今|いま}まで (until now), {他方|たほう} (on the other hand), {仮|かり} (temporary/hypothetical), {例年|れいねん} (normal year)

Notable features:
- Multi-sense entries: {仮|かり} (temporary/hypothetical), {信者|しんじゃ} (religious believer/fan devotee), {作|つく}り{上|あ}げる (build up/fabricate), {健在|けんざい} (alive and well/still going strong)
- Diverse POS: nouns, verbs (ichidan), na-adjective, adverbs, conjunctions, pre-noun adjectivals
- Register variety: formal ({侵害|しんがい}, {伝達|でんたつ}, {不詳|ふしょう}), neutral ({位置|いち}, {個別|こべつ}), informal ({信者|しんじゃ} sense 2)
- Homophone notes: {代替|だいたい} vs {大体|だいたい}, {人工|じんこう} vs {人口|じんこう}, {任期|にんき} vs {人気|にんき}

Total entries: 11,600 → 11,630
Remaining candidates: 570 → 540 (30 removed)

### 2026-02-17 (Vocabulary Expansion - 30 New Entries, Session 259)
Added 30 new dictionary entries (IDs 11515-11544) from candidate_words.json:

- **Verbs (6)**: {伏|ふ}せる (to turn face down/conceal), {傾|かたむ}ける (to tilt/devote), {催|もよお}す (to hold event/feel urge), {使|つか}い{切|き}る (to use up), {付|つ}け{加|くわ}える (to add/append), {使|つか}い{切|き}る (to use up completely)
- **Na-adjectives (4)**: {優雅|ゆうが} (elegant), {健全|けんぜん} (healthy/sound), {偏屈|へんくつ} (eccentric/cranky), {優位|ゆうい} (superior/advantageous)
- **Nouns - abstract/formal (10)**: {兆候|ちょうこう} (sign/symptom), {偽造|ぎぞう} (forgery), {僅差|きんさ} (narrow margin), {働|はたら}きかけ (effort/appeal), {倍増|ばいぞう} (doubling), {値上|ねあ}がり (price increase), {休業|きゅうぎょう} (business closure), {会談|かいだん} (conference/talks), {侵略|しんりゃく} (invasion), {修復|しゅうふく} (restoration)
- **Nouns - concrete/cultural (6)**: {偽物|にせもの} (fake/counterfeit), {仕上|しあ}げ (finishing touches), {先延|さきの}ばし (procrastination), {僧侶|そうりょ} (Buddhist monk), {個室|こしつ} (private room), {個性|こせい} (personality/individuality)
- **Nouns - people/origin (4)**: {働|はたら}き{者|もの} (hard worker), {元凶|げんきょう} (root cause/culprit), {元祖|がんそ} (originator/founder), {儒教|じゅきょう} (Confucianism)

Notable features:
- Multi-sense entries: {伏|ふ}せる (face down/conceal), {傾|かたむ}ける (tilt/devote), {催|もよお}す (hold event/feel urge), {傍|かたわ}ら (beside/while doing)
- Cross-references: {偽物|にせもの} ↔ {本物|ほんもの}, {先延|さきの}ばし ↔ {延期|えんき}, {僧侶|そうりょ} ↔ お{坊|ぼう}さん, {僅差|きんさ} ↔ {大差|たいさ}, {侵略|しんりゃく} ↔ {侵攻|しんこう}, {修復|しゅうふく} ↔ {修理|しゅうり}
- Set expressions: {耳|みみ}を{傾|かたむ}ける (listen attentively), {先延|さきの}ばしにする (to procrastinate)
- Cultural context: {僧侶|そうりょ} (Japanese monks and marriage), {元祖|がんそ} (shop rivalry), {儒教|じゅきょう} (Edo period influence)
- New kanji: 2,306 → 2,310 ({侶|りょ}, {僧|そう}, {儒|じゅ}, {凶|きょう})

Total entries: 11,549 → 11,600 (includes entries from other sessions)
Remaining candidates: 341 → 311 (30 removed)

### 2026-02-16 (Vocabulary Expansion - 30 New Entries, Session 258)
Added 30 new dictionary entries (IDs 11464-11493) from candidate_words.json:

- **Japanese compounds - formal/abstract (8)**: {不愉快|ふゆかい} (unpleasant), {不合理|ふごうり} (unreasonable), {不利益|ふりえき} (disadvantage), {争点|そうてん} (contested point), {事項|じこう} (matter/item), {交錯|こうさく} (intermingling), {事業者|じぎょうしゃ} (business operator), {主体|しゅたい} (subject/main body)
- **Japanese compounds - people/culture (5)**: {亭主|ていしゅ} (husband/host), {仇|かたき} (enemy/target of vengeance), {亡霊|ぼうれい} (ghost/specter), {主治医|しゅじい} (attending physician), {人力車|じんりきしゃ} (rickshaw)
- **Japanese compounds - other (8)**: {主観|しゅかん} (subjectivity), {主題歌|しゅだいか} (theme song), {主力|しゅりょく} (main force), {人差|ひとさ}し{指|ゆび} (index finger), {人里|ひとざと} (inhabited area), {五目|ごもく} (assorted), {云々|うんぬん} (and so on), {事欠|ことか}く (to lack)
- **Loanwords (9)**: ダイナミック (dynamic), ラップ (wrap/rap), リリース (release), プロモーション (promotion), ヘイト (hate), マッチング (matching), バイアス (bias), バーチャル (virtual), テンプレート (template)

Notable features:
- Mixed native Japanese and loanwords: 21 native Japanese words + 9 loanwords for good variety
- Multi-sense entries: ラップ (plastic wrap/rap music), {亭主|ていしゅ} (husband/host), {云々|うんぬん} (et cetera/to comment on), {主体|しゅたい} (main body/philosophical subject)
- Cultural context: {亭主|ていしゅ}{関白|かんぱく} (domineering husband), {仇討|かたきう}ち ({忠臣蔵|ちゅうしんぐら} vendetta), {人力車|じんりきしゃ} (Meiji-era invention), マッチングアプリ (modern dating culture)
- Formal register: {争点|そうてん}, {事項|じこう}, {不利益|ふりえき}, {事業者|じぎょうしゃ}, {交錯|こうさく}
- Modern vocabulary: バイアス, バーチャル (VTuber culture), ヘイト (hate speech law), マッチング, テンプレート
- New kanji: 2,303 → 2,306 ({云|うん}, {亭|てい}, {仇|かたき})

Total entries: 11,519 → 11,549
Remaining candidates: 371 → 341 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
