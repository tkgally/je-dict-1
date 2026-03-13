# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-12
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
| Total entries | ~16,512 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~13,713 (open) |
| Candidate words | ~3,266 |
| Cross-references | ~3,400 |
| Example sentences | ~49,700 |
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

### 2026-03-12 (Vocabulary Expansion - 30 New Entries, Session 422)
Added 30 new dictionary entries (IDs 16433-16462) from candidate_words.json:

- **Na-adjectives (3)**: {柔軟|じゅうなん}な (flexible), {無責任|むせきにん}な (irresponsible), {肥沃|ひよく}な (fertile)
- **Nouns (20)**: {電子書籍|でんししょせき} (e-book), {金網|かなあみ} (wire mesh), {薄化粧|うすげしょう} (light makeup), {病床|びょうしょう} (sickbed), {協調性|きょうちょうせい} (cooperativeness), {関係者|かんけいしゃ} (person concerned), {怨恨|えんこん} (grudge), {全体像|ぜんたいぞう} (big picture), {撥水|はっすい} (water repellent), {行楽地|こうらくち} (tourist spot), {最新版|さいしんばん} (latest version), {山腹|さんぷく} (mountainside), {詳報|しょうほう} (detailed report), {健康維持|けんこういじ} (health maintenance), {中道|ちゅうどう} (centrism), {群舞|ぐんぶ} (group dance), {個体差|こたいさ} (individual variation), {逆転劇|ぎゃくてんげき} (dramatic comeback), {一網打尽|いちもうだじん} (wholesale roundup), {逆転負|ぎゃくてんま}け (come-from-behind loss)
- **Nouns/suru verbs (5)**: {代用|だいよう} (substitution), {再確認|さいかくにん} (reconfirmation), {数値化|すうちか} (quantification), {再雇用|さいこよう} (re-employment), {定年退職|ていねんたいしょく} (mandatory retirement)
- **Nouns (multi-sense) (2)**: {無風|むふう} (2: windless + uncontested), {一般道|いっぱんどう} (public road)

Notable features:
- Work/society: {協調性|きょうちょうせい}, {定年退職|ていねんたいしょく}, {再雇用|さいこよう}, {関係者|かんけいしゃ}, {無責任|むせきにん}な
- Technology/modern: {電子書籍|でんししょせき}, {最新版|さいしんばん}, {数値化|すうちか}, {撥水|はっすい}
- Sports/politics: {逆転劇|ぎゃくてんげき}, {逆転負|ぎゃくてんま}け, {中道|ちゅうどう}, {無風|むふう}
- Nature/geography: {山腹|さんぷく}, {肥沃|ひよく}な
- Four-character idiom: {一網打尽|いちもうだじん}
- New kanji: 2,534 → 2,536 (撥, 沃)

Total entries: ~16,482 → ~16,512 (approximate)
Remaining candidates: ~3,296 → ~3,266 (30 removed)

### 2026-03-12 (Vocabulary Expansion - 30 New Entries, Session 421)
Added 30 new dictionary entries (IDs 16403-16432) from candidate_words.json:

- **Nouns (18)**: {野次馬|やじうま} (onlooker), {評論家|ひょうろんか} (critic), {新書|しんしょ} (pocket-sized book), {山積|やまづ}み (huge pile), {物腰|ものごし} (demeanor), {幼虫|ようちゅう} (larva), {絶壁|ぜっぺき} (precipice), {厚化粧|あつげしょう} (heavy makeup), {無駄話|むだばなし} (idle talk), {帰宅部|きたくぶ} (go-home club), {月謝|げっしゃ} (monthly tuition), {爪先|つまさき} (tiptoe), {天袋|てんぶくろ} (overhead cupboard), {鏡台|きょうだい} (dressing table), {画廊|がろう} (art gallery), {好感|こうかん} (good impression), {荒天|こうてん} (stormy weather), {焼香|しょうこう} (burning incense)
- **Nouns/suru verbs (3)**: {減点|げんてん} (deducting points), {戦慄|せんりつ} (shudder), {大歓迎|だいかんげい} (warm welcome)
- **Nouns (multi-sense) (3)**: {担任|たんにん} (homeroom teacher/person in charge), {修羅|しゅら} (carnage/Asura), {不意打|ふいう}ち (surprise attack)
- **Noun/na-adjective (2)**: {不条理|ふじょうり} (absurdity), {謙譲|けんじょう} (humility)
- **Adjective-i (2)**: {物珍|ものめずら}しい (novel/curious), {計算高|けいさんだか}い (calculating)
- **Adverb (1)**: さながら (just like)
- **Verb (1)**: {言|い}い{返|かえ}す (to talk back)

Notable features:
- School/education: {担任|たんにん}, {帰宅部|きたくぶ}, {月謝|げっしゃ}, {減点|げんてん}
- Culture: {焼香|しょうこう} (Buddhist funerals), {新書|しんしょ} (publishing format), {鏡台|きょうだい} (traditional furniture)
- Literary/formal: さながら, {戦慄|せんりつ}, {修羅|しゅら}, {謙譲|けんじょう}, {荒天|こうてん}
- Daily life: {爪先|つまさき}, {厚化粧|あつげしょう}, {無駄話|むだばなし}, {野次馬|やじうま}
- Multi-sense: {担任|たんにん} (2), {修羅|しゅら} (2), {大歓迎|だいかんげい} (2)
- New kanji: 2,533 → 2,534 (慄)

Total entries: ~16,452 → ~16,482 (approximate)
Remaining candidates: ~3,326 → ~3,296 (30 removed)

### 2026-03-12 (Vocabulary Expansion - 30 New Entries, Session 420)
Added 30 new dictionary entries (IDs 16373-16402) from candidate_words.json:

- **Nouns (17)**: {薬指|くすりゆび} (ring finger), {教頭|きょうとう} (vice-principal), {朝礼|ちょうれい} (morning assembly), {朝刊|ちょうかん} (morning newspaper), {凶器|きょうき} (weapon), {液晶|えきしょう} (LCD), {急流|きゅうりゅう} (rapid stream), {圏内|けんない} (within range), {筋力|きんりょく} (muscle strength), {冥福|めいふく} (rest in peace), {悪巧|わるだく}み (evil scheme), {平静|へいせい} (calm), {照|て}り (shine/glaze), {鎌|かま} (sickle), {隠|かく}れ{家|が} (hideaway), {生前|せいぜん} (during one's lifetime), {風評|ふうひょう} (rumor)
- **Nouns/suru verbs (5)**: {駆除|くじょ} (extermination), {除外|じょがい} (exclusion), {離職|りしょく} (leaving one's job), {注視|ちゅうし} (close observation), {憶測|おくそく} (speculation)
- **Nouns (multi-sense) (3)**: {上|のぼ}り{坂|ざか} (uphill/upward trend), {下|くだ}り{坂|ざか} (downhill/decline), {曲折|きょくせつ} (twists/complications)
- **Noun/na-adjective (1)**: {平静|へいせい} (calm)
- **Noun (person) (1)**: {幹事|かんじ} (organizer)
- **Adverb (1)**: {気長|きなが}に (patiently)
- **Expression (1)**: {凛|りん}とした (dignified/crisp)
- **Noun (food/weather) (1)**: {照|て}り (shine/glaze)

Notable features:
- Multi-sense: {上|のぼ}り{坂|ざか} (2: physical + figurative), {下|くだ}り{坂|ざか} (2: physical + figurative), {隠|かく}れ{家|が} (2: hideout + hidden-gem restaurant), {凛|りん}とした (2: dignified + crisp air), {曲折|きょくせつ} (2: physical bends + complications), {照|て}り (2: sunshine + food glaze)
- Work/school culture: {幹事|かんじ}, {朝礼|ちょうれい}, {教頭|きょうとう}, {離職|りしょく}
- Formal/news: {注視|ちゅうし}, {風評|ふうひょう}, {憶測|おくそく}, {除外|じょがい}
- Daily life: {薬指|くすりゆび}, {朝刊|ちょうかん}, {液晶|えきしょう}, {下取|したど}り, {筋力|きんりょく}
- Cultural: {冥福|めいふく} (Buddhist condolence), {生前|せいぜん} (end-of-life culture), {鎌|かま} (traditional farming)
- New kanji: 2,531 → 2,533 (冥, 鎌)

Total entries: ~16,422 → ~16,452 (approximate)
Remaining candidates: ~3,356 → ~3,326 (30 removed)

### 2026-03-12 (Vocabulary Expansion - 30 New Entries, Session 419)
Added 30 new dictionary entries (IDs 16343-16372) from candidate_words.json:

- **Nouns (14)**: {崖|がけ}っぷち (cliff edge/critical moment), {仕送|しおく}り (allowance), {大西洋|たいせいよう} (Atlantic Ocean), {絶好調|ぜっこうちょう} (peak condition), {博士号|はくしごう} (doctorate), {歓待|かんたい} (hospitality), {一人前|ひとりまえ} (one serving/full-fledged), お{手伝|てつだ}いさん (housekeeper), {皇后|こうごう} (empress), {生中継|なまちゅうけい} (live broadcast), {長話|ながばなし} (long chat), {耳|みみ}かき (ear pick), {空洞|くうどう} (hollow/cavity), {多数決|たすうけつ} (majority vote)
- **Verbs (4)**: でっち{上|あ}げる (to fabricate), {見受|みう}ける (to observe), {勘繰|かんぐ}る (to be suspicious), {吹|ふ}き{抜|ぬ}ける (to blow through)
- **Adjective (1)**: {面倒臭|めんどうくさ}い (bothersome)
- **Adverbs (2)**: {依然|いぜん}として (still/as before), カサカサ (dry/rustling)
- **Nouns (other) (6)**: {坊|ぼ}っちゃん (young boy/pampered boy), {造詣|ぞうけい} (deep knowledge), {隅|すみ}っこ (corner), {短絡|たんらく} (short circuit/hasty reasoning), {同封|どうふう} (enclosure), {疾患|しっかん} (disease)
- **Expression (1)**: {筋|すじ}が{通|とお}る (to make sense)
- **Noun (literary) (1)**: {最果|さいは}て (farthest reaches)
- **Noun (formal) (1)**: {造詣|ぞうけい} (deep knowledge)

Notable features:
- Good POS variety: nouns, verbs, adjective, adverbs, expression, onomatopoeia
- Multi-sense: {崖|がけ}っぷち (2: physical + figurative), {一人前|ひとりまえ} (2: serving + full-fledged), {坊|ぼ}っちゃん (2: polite + spoiled), {空洞|くうどう} (2: physical + figurative), {短絡|たんらく} (2: electrical + reasoning), カサカサ (2: dry + rustling), {耳|みみ}かき (2: tool + act)
- Formal/literary: {依然|いぜん}として, {見受|みう}ける, {造詣|ぞうけい}, {同封|どうふう}, {歓待|かんたい}, {疾患|しっかん}
- Daily life: {面倒臭|めんどうくさ}い, {隅|すみ}っこ, {耳|みみ}かき, カサカサ, {仕送|しおく}り
- New kanji: 2,530 → 2,531 (后)

Total entries: ~16,392 → ~16,422 (approximate)
Remaining candidates: ~3,385 → ~3,356 (29 removed)

### 2026-03-12 (Vocabulary Expansion - 30 New Entries, Session 418)
Added 30 new dictionary entries (IDs 16313-16342) from candidate_words.json:

- **Nouns (12)**: {標的|ひょうてき} (target), {音響|おんきょう} (sound/acoustics), {元号|げんごう} (era name), {核家族|かくかぞく} (nuclear family), {古本屋|ふるほんや} (secondhand bookshop), {向|む}かい{風|かぜ} (headwind), {着|き}せ{替|か}え (dress-up), {割|わ}り{当|あ}て (allocation), {洋間|ようま} (Western-style room), {染料|せんりょう} (dye), {形勢|けいせい} (situation), {自虐|じぎゃく} (self-deprecation)
- **Nouns/suru verbs (6)**: {挽回|ばんかい} (recovery), {英訳|えいやく} (English translation), {失念|しつねん} (forgetting), {合奏|がっそう} (ensemble), {伸縮|しんしゅく} (expansion/contraction), {放射|ほうしゃ} (radiation)
- **Nouns/na-adj (2)**: {優勢|ゆうせい} (superiority), {捨|す}て{鉢|ばち} (desperate/reckless)
- **Noun/na-adj/suru (1)**: {親孝行|おやこうこう} (filial piety)
- **Noun/suru (1)**: {上書|うわが}き (overwriting)
- **Adverbs (4)**: はきはき (briskly), {堂々|どうどう}と (confidently), {是非|ぜひ}とも (by all means), {一段|いちだん}と (even more)
- **I-adjective (1)**: {心強|こころづよ}い (reassuring)
- **Verbs (2)**: {食|く}い{違|ちが}う (to differ), {締|し}め{括|くく}る (to conclude)
- **Noun/suru (1)**: {養育|よういく} (upbringing)

Notable features:
- Cultural: {元号|げんごう} (Japanese era system), {親孝行|おやこうこう} (filial piety), {古本屋|ふるほんや} (bookshop culture)
- Business/formal: {失念|しつねん}, {形勢|けいせい}, {是非|ぜひ}とも, {挽回|ばんかい}
- Daily life: {核家族|かくかぞく}, {洋間|ようま}, {着|き}せ{替|か}え, {上書|うわが}き
- Multi-sense: {上書|うわが}き (2: computing overwrite + envelope address)
- New kanji: 2,529 → 2,530 (孝)

Total entries: ~16,362 → ~16,392 (approximate)
Remaining candidates: ~3,415 → ~3,385 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
