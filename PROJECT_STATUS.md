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
| Total entries | ~14,384 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~11,585 (open) |
| Candidate words | ~5,385 |
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

### 2026-02-28 (Vocabulary Expansion - 30 New Entries, Session 351)
Added 30 new dictionary entries (IDs 14299-14328) from candidate_words.json:

- **Nouns (14)**: {跡継|あとつ}ぎ (successor), {身|み}なり (appearance), {身代金|みのしろきん} (ransom), {軸|じく} (axis/core/scroll), {轟音|ごうおん} (thunderous roar), {迫力|はくりょく} (force/impact), {逆効果|ぎゃくこうか} (counterproductive), {逸話|いつわ} (anecdote), {道場|どうじょう} (dojo), {近況|きんきょう} (recent situation), {連日|れんじつ} (day after day), {進路|しんろ} (course/career path)
- **Noun/suru verbs (7)**: {転倒|てんとう} (falling over/reversal), {軽視|けいし} (disregard), {購買|こうばい} (purchasing), {追悼|ついとう} (mourning), {追放|ついほう} (banishment), {退治|たいじ} (extermination), {通報|つうほう} (report/notification), {速報|そくほう} (breaking news), {連載|れんさい} (serialization), {過労死|かろうし} (death from overwork)
- **Godan verbs (3)**: {貸|か}し{出|だ}す (to lend out), {透|す}き{通|とお}る (to be transparent)
- **Ichidan verbs (3)**: {貶|おとし}める (to disparage), {追|お}い{詰|つ}める (to corner), {途絶|とだ}える (to cease), {遂|と}げる (to accomplish)
- **Na-adjective (1)**: {過激|かげき} (radical/extreme)
- **Multi-sense entries (2)**: {身内|みうち} (2: family + inner circle), {転倒|てんとう} (2: toppling + reversal), {軸|じく} (3: axis + core + scroll), {進路|しんろ} (2: route + career path)

Notable features:
- Multi-sense entries: {身内|みうち}, {転倒|てんとう}, {軸|じく} (3 senses), {進路|しんろ}
- Culture: {道場|どうじょう} (martial arts), {退治|たいじ} (Momotaro folklore), {過労死|かろうし} (social issue)
- Media: {連載|れんさい} (manga culture), {速報|そくほう} (news), {通報|つうほう}
- Society: {過労死|かろうし}, {追放|ついほう}, {軽視|けいし}, {過激|かげき}
- New kanji: 2,465 → 2,467 ({貶|おとし}, {轟|とどろき})

Total entries: 14,354 → 14,384 (approximate)
Remaining candidates: 5,415 → 5,385 (30 removed)

### 2026-02-28 (Vocabulary Expansion - 30 New Entries, Session 350)
Added 30 new dictionary entries (IDs 14269-14298) from candidate_words.json:

- **Nouns (18)**: {読|よ}み{方|かた} (way of reading), {詰|つ}め{込|こ}み (cramming), {語|かた}り{手|て} (narrator), {覆|おお}い (cover), {見落|みお}とし (oversight), {豆|まめ}まき (bean-throwing), {語順|ごじゅん} (word order), {跡取|あとと}り (heir), {跡地|あとち} (former site), {路面電車|ろめんでんしゃ} (streetcar), {身代|みが}わり (substitute), {身|み}だしなみ (grooming), {身|み}の{丈|たけ} (stature/means), {転機|てんき} (turning point), {辛味|からみ} (spiciness), {辻褄|つじつま} (consistency), {輪郭|りんかく} (outline), {足湯|あしゆ} (foot bath), {軽自動車|けいじどうしゃ} (kei car)
- **Noun/suru verbs (3)**: {賞賛|しょうさん} (praise), {踏襲|とうしゅう} (following precedent), {身震|みぶる}い (shudder), {転嫁|てんか} (shifting blame)
- **Godan verbs (2)**: {解|と}き{明|あ}かす (to elucidate), {踏|ふ}み{出|だ}す (to step forward)
- **Ichidan verb (1)**: {表|あらわ}れる (to manifest)
- **Na-adjectives (2)**: {迅速|じんそく} (swift), {軽|かる}やか (light/nimble)
- **Noun (multi-sense) (4)**: {走馬灯|そうまとう} (2: lantern + flashback), {軒並|のきな}み (2: row of houses + across the board), {身|み}の{丈|たけ} (2: height + means), {輪郭|りんかく} (2: outline + framework)

Notable features:
- Multi-sense entries: {読|よ}み{方|かた} (2: reading + interpretation), {踏|ふ}み{出|だ}す (2: physical + figurative), {転嫁|てんか} (2: blame + costs), {走馬灯|そうまとう} (2: lantern + flashback)
- 身- compounds: {身代|みが}わり, {身|み}だしなみ, {身|み}の{丈|たけ}, {身震|みぶる}い
- Culture: {豆|まめ}まき (Setsubun), {足湯|あしゆ} (hot spring foot bath), {軽自動車|けいじどうしゃ} (kei car), {走馬灯|そうまとう}
- Language/education: {読|よ}み{方|かた}, {語順|ごじゅん}, {語|かた}り{手|て}
- Food: {辛味|からみ}
- New kanji: 2,461 → 2,465 ({褄|つま}, {辻|つじ}, {迅|じん}, {郭|かく})

Total entries: 14,324 → 14,354 (approximate)
Remaining candidates: 5,445 → 5,415 (30 removed)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
