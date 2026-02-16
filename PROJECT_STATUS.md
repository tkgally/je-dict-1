# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-16
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
| Total entries | ~11,549 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~8,750 (open) |
| Candidate words | ~341 |
| Cross-references | ~3,340 |
| Example sentences | ~42,900 |
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

### 2026-02-16 (Vocabulary Expansion - 30 New Entries, Session 257)
Added 30 new dictionary entries (IDs 11434-11463) from candidate_words.json:

- **Expressions/adjectives (2)**: {仕方|しかた}ない (it can't be helped), {仲良|なかよ}し (close friend)
- **Verbs (6)**: {仕組|しく}む (to devise/plot), {仰|あお}ぐ (to look up at/revere), {佇|たたず}む (to stand still), {伸|の}び{悩|なや}む (to plateau), {乗|の}っかる (to get on/jump on board)
- **Nouns - society/people (5)**: {人手不足|ひとでぶそく} (labor shortage), {人情|にんじょう} (human feelings), {人間関係|にんげんかんけい} (interpersonal relations), {仲良|なかよ}し, {何事|なにごと} (what/everything)
- **Nouns - abstract/general (8)**: {使命|しめい} (mission), {伝説|でんせつ} (legend), {伝承|でんしょう} (tradition/folklore), {侮辱|ぶじょく} (insult), {主導権|しゅどうけん} (initiative), {争奪戦|そうだつせん} (contest/scramble), {乱入|らんにゅう} (barging in), {作風|さくふう} (artistic style)
- **Nouns - practical (7)**: {代謝|たいしゃ} (metabolism), {仮面|かめん} (mask), {侵入|しんにゅう} (intrusion), {依存|いぞん} (dependence/addiction), {保管|ほかん} (storage), {体験|たいけん} (firsthand experience), {休養|きゅうよう} (rest/recuperation)
- **Nouns - specialized (2)**: {保育|ほいく} (childcare), {供養|くよう} (memorial service), {似顔絵|にがおえ} (portrait/caricature)

Notable features:
- Multi-sense entries: {仰|あお}ぐ (look up/revere/seek guidance), {仮面|かめん} (physical mask/figurative), {依存|いぞん} (dependence/addiction), {伝説|でんせつ} (legend/legendary), {何事|なにごと} (what/everything), {乗|の}っかる (physical/figurative)
- Cultural context: {人情|にんじょう} ({義理|ぎり}{人情|にんじょう} cultural concept), {供養|くよう} (Buddhist memorial for objects), {保育|ほいく} ({待機|たいき}{児童|じどう} social issue), {仮面|かめん}ライダー
- Social vocabulary: {人手不足|ひとでぶそく} (aging society), {人間関係|にんげんかんけい} (workplace stress), {依存|いぞん}{症|しょう} (modern addiction issues)
- Verb variety: godan-mu ({仕組|しく}む, {佇|たたず}む, {伸|の}び{悩|なや}む), godan-gu ({仰|あお}ぐ), godan-ru ({乗|の}っかる)

Total entries: 11,489 → 11,519
Remaining candidates: 353 → 323 (30 removed)

### 2026-02-16 (Vocabulary Expansion - 30 New Entries, Session 256)
Added 30 new dictionary entries (IDs 11404-11433) from candidate_words.json:

- **主- compounds (5)**: {主人公|しゅじんこう} (protagonist), {主催|しゅさい} (hosting an event), {主導|しゅどう} (leadership), {主流|しゅりゅう} (mainstream), {主食|しゅしょく} (staple food)
- **乗- compounds (3)**: {乗|の}っ{取|と}る (to take over/hijack), {乗|の}り{切|き}る (to get through/overcome), {乗用車|じょうようしゃ} (passenger car)
- **乱- words (2)**: {乱|みだ}す (to disturb), {乱|みだ}れ (disorder)
- **事- compounds (5)**: {事例|じれい} (case/example), {事務|じむ} (office work), {事実上|じじつじょう} (de facto), {事柄|ことがら} (matter/affair), {事業|じぎょう} (business/enterprise)
- **人- compounds (2)**: {人材|じんざい} (talent/human resources), {人格|じんかく} (personality/character)
- **仕- words (3)**: {仕上|しあ}がる (to be completed), {仕入|しい}れる (to stock/purchase), {仕切|しき}り (partition/management)
- **代- compounds (2)**: {代償|だいしょう} (compensation/price to pay), {代行|だいこう} (proxy service)
- **Other (8)**: {乳児|にゅうじ} (infant), {了承|りょうしょう} (consent), {予感|よかん} (premonition), {二次元|にじげん} (2D/anime world), {五輪|ごりん} (Olympics), {亡命|ぼうめい} (exile/defection), {交付|こうふ} (issuance), {仏教|ぶっきょう} (Buddhism)

Notable features:
- Systematic kanji compound clusters: 主-, 乗-, 乱-, 事-, 仕-, 代- prefix/radical families
- Multi-sense entries: {乗|の}っ{取|と}る (takeover/hijack), {仕切|しき}り (partition/management), {事業|じぎょう} (business/project), {二次元|にじげん} (math 2D/otaku culture), {代償|だいしょう} (figurative price/legal compensation)
- Transitive/intransitive pair: {乱|みだ}す (transitive) ↔ {乱|みだ}れ (noun from intransitive)
- Cultural context: {二次元|にじげん} (otaku 2D vs 3D culture), {五輪|ごりん} (Olympics shorthand), {代行|だいこう} ({運転|うんてん}{代行|だいこう} designated driver service), {仏教|ぶっきょう} (Japanese Buddhist customs)
- Register variety: formal ({了承|りょうしょう}, {交付|こうふ}, {事実上|じじつじょう}) to neutral ({主流|しゅりゅう}, {予感|よかん})

Total entries: 11,459 → 11,489
Remaining candidates: 222 → 290 (30 removed, new candidates may have been added)

### 2026-02-16 (Vocabulary Expansion - 30 New Entries, Session 255)
Added 30 new dictionary entries (IDs 11374-11403) from candidate_words.json:

- **Japanese compounds - positional (5)**: {上記|じょうき} (above-mentioned), {下記|かき} (below-mentioned), {上部|じょうぶ} (upper part), {下部|かぶ} (lower part), {下限|かげん} (lower limit)
- **Japanese compounds - 不- prefix (5)**: {不快|ふかい} (unpleasant), {不揃|ふぞろ}い (uneven/mismatched), {不向|ふむ}き (unsuited), {不人気|ふにんき} (unpopular), {不定期|ふていき} (irregular)
- **Japanese compounds - other (5)**: {並|なみ} (ordinary/medium), {中頃|なかごろ} (around the middle), {中卒|ちゅうそつ} (middle school graduate), {一揆|いっき} (uprising), {一堂|いちどう} (in one place)
- **Japanese compounds - time/quantity (2)**: {丸々|まるまる} (completely/plump), {一端|いったん} (one end/a part)
- **Loanwords (13)**: ハイブリッド (hybrid), マジック (magic/marker), ユニーク (unique/quirky), リゾート (resort), リーズナブル (reasonable in price), レギュラー (regular/starter), ローカル (local), バラエティ (variety/variety show), ブレンド (blend), パンデミック (pandemic), プラチナ (platinum), ロマンス (romance), ワイド (wide)

Notable features:
- Antonym pairs: {上記|じょうき} ↔ {下記|かき}, {上部|じょうぶ} ↔ {下部|かぶ}
- Homophone warnings: {上部|じょうぶ} vs {丈夫|じょうぶ}, {下限|かげん} vs {加減|かげん}, {不快|ふかい} vs {深|ふか}い, {一端|いったん} vs {一旦|いったん}
- False friend notes: ユニーク (quirky, not just "unique"), リーズナブル (price only, not general "reasonable")
- Multi-sense entries: {丸々|まるまる} (completely/plump), マジック (magic/marker), レギュラー (starter/standard), バラエティ (variety/TV show), {一端|いったん} (physical end/glimpse)
- Cultural context: {並|なみ} (restaurant sizing), ブレンド (coffee shop culture), ワイドショー (Japanese TV genre), プラチナチケット (hard-to-get tickets)
- New kanji: 2,302 → 2,303 ({揆|き})

Total entries: 11,429 → 11,459
Remaining candidates: 252 → 222

### 2026-02-16 (Vocabulary Expansion - 30 New Entries, Session 254)
Added 30 new dictionary entries (IDs 11344-11373) from candidate_words.json:

- **下- compounds (4)**: {下剋上|げこくじょう} (overthrowing superiors), {下手|へた}くそ (terrible at), {下敷|したじ}き (desk pad/pinned underneath), {下級|かきゅう} (lower grade), {下座|げざ} (lower seat), {下層|かそう} (lower stratum)
- **不- compounds (13)**: {不倫|ふりん} (adultery), {不審者|ふしんしゃ} (suspicious person), {不死身|ふじみ} (invulnerable), {不自然|ふしぜん} (unnatural), {不意|ふい} (unexpected), {不明|ふめい} (unknown), {不適切|ふてきせつ} (inappropriate), {不平等|ふびょうどう} (inequality), {不法|ふほう} (illegal), {不確|ふたし}か (uncertain), {不本意|ふほんい} (reluctant), {不完全|ふかんぜん} (incomplete), {不透明|ふとうめい} (opaque/unclear)
- **中- compounds (5)**: {中華街|ちゅうかがい} (Chinatown), {中退|ちゅうたい} (dropping out), {中部|ちゅうぶ} (central region), {中流|ちゅうりゅう} (middle class/midstream), {中核|ちゅうかく} (nucleus/core), {中枢|ちゅうすう} (nerve center)
- **両- compounds (3)**: {両端|りょうたん} (both ends), {両者|りょうしゃ} (both parties), {両面|りょうめん} (both sides)
- **Other (2)**: {串|くし}カツ (deep-fried skewers), {世紀末|せいきまつ} (end of century)

Notable features:
- Systematic 不- prefix cluster covering negation patterns: from everyday ({不自然|ふしぜん}, {不明|ふめい}) to formal/legal ({不法|ふほう}, {不適切|ふてきせつ})
- Multi-sense entries: {下敷|したじ}き (stationery/disaster), {不透明|ふとうめい} (physical/figurative), {中流|ちゅうりゅう} (social class/river)
- Cultural context: {下剋上|げこくじょう} (Sengoku history/sports upsets), {下座|げざ} (seating etiquette), {中華街|ちゅうかがい} (Yokohama/Kobe/Nagasaki), {串|くし}カツ (Osaka food culture), {世紀末|せいきまつ} (North Star/fin de siecle)
- Antonym cross-references: {不自然|ふしぜん} ↔ {自然|しぜん}, {不平等|ふびょうどう} ↔ {平等|びょうどう}, {不完全|ふかんぜん} ↔ {完全|かんぜん}, {下級|かきゅう} ↔ {上級|じょうきゅう}, {下座|げざ} ↔ {上座|かみざ}
- New kanji: 2,299 → 2,302 ({剋|こく}, {枢|すう}, {核|かく})

Total entries: 11,399 → 11,429
Remaining candidates: 282 → 252

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
