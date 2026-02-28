# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-28
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
| Total entries | ~14,324 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~11,525 (open) |
| Candidate words | ~5,445 |
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

### 2026-02-28 (Vocabulary Expansion - 30 New Entries, Session 349)
Added 30 new dictionary entries (IDs 14239-14268) from candidate_words.json:

- **Noun/suru verbs (6)**: {解毒|げどく} (detoxification), {誘発|ゆうはつ} (inducement), {誹謗|ひぼう} (slander), {調停|ちょうてい} (mediation), {調印|ちょういん} (signing), {賛同|さんどう} (agreement)
- **Godan verbs (7)**: {見出|みいだ}す (to discover), {語|かた}らう (to converse), {説|と}く (to preach), {読|よ}み{解|と}く (to interpret), {読|よ}み{込|こ}む (to load), {覆|おお}い{隠|かく}す (to conceal), {赴|おもむ}く (to proceed)
- **Ichidan verb (1)**: {見|み}せつける (to show off)
- **Nouns (14)**: {荷車|にぐるま} (cart), {語尾|ごび} (word ending), {諜報|ちょうほう} (espionage), {諸々|もろもろ} (various), {負|ま}け{犬|いぬ} (loser), {賃上|ちんあ}げ (wage increase), {賢者|けんじゃ} (sage), {赤子|あかご} (baby), {走行|そうこう} (vehicle running), {起業家|きぎょうか} (entrepreneur), {起因|きいん} (cause), {谷底|たにそこ} (valley bottom), {蒸|む}し (steaming), {訪|おとず}れ (visit/advent)
- **Noun/suffix (1)**: {術|じゅつ} (technique/art)
- **Noun (1)**: {言|い}い{合|あ}い (argument)

Notable features:
- Multi-sense entries: {見出|みいだ}す (2: discover + find meaning), {説|と}く (2: expound + advocate), {読|よ}み{込|こ}む (2: load data + read thoroughly), {負|ま}け{犬|いぬ} (2: loser + underdog), {術|じゅつ} (2: technique + means), {訪|おとず}れ (2: visit + arrival)
- Communication: {語|かた}らう, {語尾|ごび}, {説|と}く, {誹謗|ひぼう}, {賛同|さんどう}, {言|い}い{合|あ}い
- Legal/formal: {調停|ちょうてい}, {調印|ちょういん}, {起因|きいん}, {誹謗|ひぼう}
- Business/work: {賃上|ちんあ}げ, {起業家|きぎょうか}, {走行|そうこう}
- New kanji: 2,458 → 2,461 ({誹|ひ}, {諜|ちょう}, {謗|ぼう})

Total entries: 14,294 → 14,324 (approximate)
Remaining candidates: 5,475 → 5,445 (30 removed)

### 2026-02-28 (Vocabulary Expansion - 30 New Entries, Session 348)
Added 30 new dictionary entries (IDs 14209-14238) from candidate_words.json:

- **Noun/suru verbs (8)**: {誘惑|ゆうわく} (temptation), {誘拐|ゆうかい} (kidnapping), {説教|せっきょう} (sermon/lecture), {説得|せっとく} (persuasion), {談笑|だんしょう} (chatting and laughing), {警戒|けいかい} (vigilance), {護衛|ごえい} (escort/bodyguard), {負荷|ふか} (load/burden)
- **Godan verbs (6)**: {誤魔化|ごまか}す (to deceive/gloss over), {見返|みかえ}す (to look back/get even), {解|と}き{放|はな}つ (to set free), {諭|さと}す (to admonish), {賑|にぎ}わう (to be bustling), {記|しる}す (to write down)
- **Ichidan verb (1)**: {設|もう}ける (to establish/set up)
- **Na-adjectives (2)**: {誠実|せいじつ} (sincere), {豪快|ごうかい} (bold/hearty)
- **Nouns (13)**: {語彙|ごい} (vocabulary), {語源|ごげん} (etymology), {読|よ}み{物|もの} (reading material), {試|こころ}み (attempt/trial), {豆乳|とうにゅう} (soy milk), {豊作|ほうさく} (bountiful harvest), {豚汁|とんじる} (pork miso soup), {負|お}い{目|め} (sense of guilt), {財閥|ざいばつ} (zaibatsu), {賛否|さんぴ} (pros and cons), {賞金|しょうきん} (prize money), {複数|ふくすう} (plural/multiple), {要件|ようけん} (requirement)

Notable features:
- Multi-sense entries: {誘惑|ゆうわく} (2: temptation + seduction), {誤魔化|ごまか}す (2: deceive + gloss over), {説教|せっきょう} (2: sermon + scolding), {見返|みかえ}す (2: look back + get even), {解|と}き{放|はな}つ (2: physical + figurative release), {要件|ようけん} (2: requirement + business matter)
- Communication: {説教|せっきょう}, {説得|せっとく}, {諭|さと}す, {談笑|だんしょう}, {記|しる}す
- Language/education: {語彙|ごい}, {語源|ごげん}, {読|よ}み{物|もの}, {複数|ふくすう}
- Food: {豆乳|とうにゅう}, {豚汁|とんじる}, {豊作|ほうさく}
- Society/business: {財閥|ざいばつ}, {賛否|さんぴ}, {賞金|しょうきん}, {要件|ようけん}
- New kanji: 2,455 → 2,458 ({拐|かい}, {諭|ゆ}, {閥|ばつ})

Total entries: 14,264 → 14,294 (approximate)
Remaining candidates: 5,505 → 5,475 (30 removed)

### 2026-02-28 (Vocabulary Expansion - 30 New Entries, Session 347)
Added 30 new dictionary entries (IDs 14179-14208) from candidate_words.json:

- **Godan verbs (3)**: {言|い}い{争|あらそ}う (to argue), {誇|ほこ}る (to be proud of), {詠|よ}む (to compose a poem)
- **Ichidan verb (1)**: {詰|つ}めかける (to crowd into)
- **I-adjective (1)**: {誇|ほこ}らしい (proud)
- **Na-adjective/noun (2)**: {親愛|しんあい} (dear/beloved), {血|ち}まみれ (blood-soaked)
- **Noun/suru verbs (7)**: {認知|にんち} (cognition), {診療|しんりょう} (medical treatment), {解読|かいどく} (deciphering), {計測|けいそく} (measurement), {解剖|かいぼう} (dissection), {訪日|ほうにち} (visit to Japan), {討伐|とうばつ} (subjugation)
- **Nouns (16)**: {規約|きやく} (terms/agreement), {訴|うった}え (appeal/lawsuit), {言論|げんろん} (speech/discourse), {直伝|じきでん} (direct transmission), {親交|しんこう} (friendship), {計略|けいりゃく} (strategy/ruse), {観賞|かんしょう} (viewing for enjoyment), {言霊|ことだま} (power of words), {親族|しんぞく} (relatives), {誘|さそ}い (invitation), {茶髪|ちゃぱつ} (brown-dyed hair), {美肌|びはだ} (beautiful skin), {診療所|しんりょうじょ} (clinic), {老害|ろうがい} (harmful elderly), {脱法|だっぽう} (circumventing law), {言質|げんち} (verbal commitment)

Notable features:
- Multi-sense entries: {誇|ほこ}る (2: pride + boasting), {訴|うった}え (2: appeal + lawsuit), {認知|にんち} (2: cognition + acknowledgment), {解剖|かいぼう} (2: dissection + analysis), {誘|さそ}い (2: invitation + enticement), {老害|ろうがい} (2: systemic + individual), {詠|よ}む (2: compose + recite)
- Communication/language: {言|い}い{争|あらそ}う, {言論|げんろん}, {言霊|ことだま}, {言質|げんち}
- Medical: {診療|しんりょう}, {診療所|しんりょうじょ}, {解剖|かいぼう}
- Culture: {言霊|ことだま} (kotodama belief), {茶髪|ちゃぱつ} (hair culture)
- New kanji: 2,453 → 2,455 ({剖|ぼう}, {詠|えい})

Total entries: 14,234 → 14,264 (approximate)
Remaining candidates: 5,535 → 5,505 (30 removed)

### 2026-02-28 (Vocabulary Expansion - 30 New Entries, Session 346)
Added 30 new dictionary entries (IDs 14149-14178) from candidate_words.json:

- **Nouns (14)**: {芸者|げいしゃ} (geisha), {街|まち}づくり (community development), {英国|えいこく} (Britain), {衆議院|しゅうぎいん} (House of Representatives), {痴話喧嘩|ちわげんか} (lovers' quarrel), {留飲|りゅういん} (vindication), {要塞|ようさい} (fortress), {見世物|みせもの} (spectacle), {規範|きはん} (norm), {観光地|かんこうち} (tourist spot), {試練|しれん} (trial/ordeal), {詰|つ}め{合|あ}わせ (assortment), {話|はな}し{合|あ}い (discussion), {誓|ちか}い (vow/oath)
- **Noun/suru verbs (7)**: {襲来|しゅうらい} (invasion), {見合|みあ}い (matchmaking), {解明|かいめい} (elucidation), {記載|きさい} (listing), {設立|せつりつ} (establishment), {許容|きょよう} (tolerance), {該当|がいとう} (applicable)
- **Noun (multi-sense) (1)**: {衣|ころも} (robe + batter)
- **Noun (1)**: {記者|きしゃ} (reporter), {親権|しんけん} (parental rights), {言|い}い{方|かた} (way of saying), {言葉|ことば}づかい (language use)
- **Ichidan verbs (3)**: {薄汚|うすよご}れる (to become grimy), {言|い}い{聞|き}かせる (to admonish), {詫|わ}びる (to apologize)
- **Godan verb (1)**: {託|たく}す (to entrust)

Notable features:
- Multi-sense entry: {衣|ころも} (2: robe/garment + batter/coating)
- Politics/law: {衆議院|しゅうぎいん}, {親権|しんけん}, {規範|きはん}, {該当|がいとう}
- Communication: {言|い}い{方|かた}, {言葉|ことば}づかい, {言|い}い{聞|き}かせる, {話|はな}し{合|あ}い, {詫|わ}びる, {誓|ちか}い
- Culture: {芸者|げいしゃ}, {見世物|みせもの}, {見合|みあ}い, {観光地|かんこうち}
- New kanji: 2,452 → 2,453 ({該|がい})

Total entries: 14,204 → 14,234 (approximate)
Remaining candidates: 5,565 → 5,535 (30 removed)

### 2026-02-28 (Vocabulary Expansion - 30 New Entries, Session 345)
Added 30 new dictionary entries (IDs 14119-14148) from candidate_words.json:

- **Nouns (10)**: {茎|くき} (stem/stalk), {苦|くる}しみ (suffering), {行|おこな}い (behavior/deed), {荷台|にだい} (truck bed), {見覚|みおぼ}え (recognition), {親心|おやごころ} (parental love), {視界|しかい} (field of vision), {視線|しせん} (gaze), {若年|じゃくねん} (youth), {製造業|せいぞうぎょう} (manufacturing industry)
- **Noun/suru verbs (7)**: {行政|ぎょうせい} (administration), {表記|ひょうき} (notation), {襲撃|しゅうげき} (attack/raid), {要約|ようやく} (summary), {規定|きてい} (regulation), {観戦|かんせん} (spectating), {解消|かいしょう} (elimination/resolution), {解禁|かいきん} (lifting a ban)
- **Na-adjective (1)**: {親密|しんみつ} (intimate/close)
- **Godan verbs (5)**: {見失|みうしな}う (to lose sight of), {見積|みつ}もる (to estimate), {見舞|みま}う (to visit sick/to strike), {見開|みひら}く (to open eyes wide), {親|した}しむ (to become familiar with)
- **Ichidan verbs (2)**: {見捨|みす}てる (to abandon), {見据|みす}える (to stare at/keep in sight)
- **Nouns (other) (3)**: {藩|はん} (feudal domain), {言|い}い{伝|つた}え (legend), {言|い}い{回|まわ}し (phrasing)
- **Noun (1)**: {言動|げんどう} (words and actions)

Notable features:
- Multi-sense entries: {見舞|みま}う (2: visit sick + befall), {見据|みす}える (2: stare at + keep in sight)
- 見- compound verbs: {見失|みうしな}う, {見捨|みす}てる, {見据|みす}える, {見積|みつ}もる, {見舞|みま}う, {見開|みひら}く, {見覚|みおぼ}え
- Language/expression: {表記|ひょうき}, {言|い}い{伝|つた}え, {言|い}い{回|まわ}し, {言動|げんどう}, {要約|ようやく}
- Society/law: {行政|ぎょうせい}, {規定|きてい}, {解消|かいしょう}, {解禁|かいきん}, {襲撃|しゅうげき}
- Family/relationships: {親心|おやごころ}, {親密|しんみつ}, {親|した}しむ
- History: {藩|はん} (feudal domain)
- New kanji: 2,451 → 2,452 ({藩|はん})

Total entries: 14,174 → 14,204 (approximate)
Remaining candidates: 5,595 → 5,565 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
