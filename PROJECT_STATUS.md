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
| Total entries | ~16,452 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~13,653 (open) |
| Candidate words | ~3,326 |
| Cross-references | ~3,400 |
| Example sentences | ~49,600 |
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

### 2026-03-11 (Vocabulary Expansion - 30 New Entries, Session 417)
Added 30 new dictionary entries (IDs 16283-16312) from candidate_words.json:

- **Nouns (17)**: {大好物|だいこうぶつ} (favorite food), {不平不満|ふへいふまん} (complaints), {明治維新|めいじいしん} (Meiji Restoration), {年貢|ねんぐ} (land tax), {古物商|こぶつしょう} (second-hand dealer), {質疑応答|しつぎおうとう} (Q&A session), {資産家|しさんか} (wealthy person), {聴診器|ちょうしんき} (stethoscope), {一級品|いっきゅうひん} (first-class goods), {貨物列車|かもつれっしゃ} (freight train), {凡作|ぼんさく} (mediocre work), {大道具|おおどうぐ} (stage set), {電子楽器|でんしがっき} (electronic instrument), ナムル (namul), {群雄|ぐんゆう} (rival warlords), {芸妓|げいぎ} (geisha), {遣唐使|けんとうし} (envoy to Tang China)
- **Nouns/suru verbs (2)**: {中絶|ちゅうぜつ} (discontinuation/abortion), {表面化|ひょうめんか} (becoming apparent)
- **Na-adjectives (2)**: {必要不可欠|ひつようふかけつ} (absolutely essential), {筋肉質|きんにくしつ} (muscular)
- **Nouns/suru verb (1)**: {誹謗中傷|ひぼうちゅうしょう} (slander/defamation)
- **Noun/suru verb (1)**: {真空|しんくう}パック (vacuum pack)
- **Noun (1)**: {吸入器|きゅうにゅうき} (inhaler)
- **Verb (1)**: {褒|ほ}めちぎる (to praise to the skies)
- **Nouns (cultural) (3)**: {白拍子|しらびょうし} (Heian-era dancer), {隈取|くまど}り (kabuki makeup), マーマレード (marmalade)
- **Expressions (2)**: {足|あし}を{延|の}ばす (to make a side trip), {身|み}の{丈|たけ}に{合|あ}う (within one's means)

Notable features:
- History/culture: {明治維新|めいじいしん}, {年貢|ねんぐ}, {遣唐使|けんとうし}, {白拍子|しらびょうし}, {隈取|くまど}り, {芸妓|げいぎ}, {群雄|ぐんゆう}
- Medical: {聴診器|ちょうしんき}, {吸入器|きゅうにゅうき}, {中絶|ちゅうぜつ}
- Modern society: {誹謗中傷|ひぼうちゅうしょう}, {表面化|ひょうめんか}, {古物商|こぶつしょう}
- Food: {大好物|だいこうぶつ}, ナムル, マーマレード, {真空|しんくう}パック
- Multi-sense: {中絶|ちゅうぜつ} (2: discontinuation + abortion)

Total entries: ~16,332 → ~16,362 (approximate)
Remaining candidates: ~3,445 → ~3,415 (30 removed)

### 2026-03-11 (Vocabulary Expansion - 30 New Entries, Session 416)
Added 30 new dictionary entries (IDs 16253-16282) from candidate_words.json:

- **Nouns (14)**: {備品|びひん} (equipment), {起点|きてん} (starting point), {月刊|げっかん} (monthly publication), {交通渋滞|こうつうじゅうたい} (traffic jam), {自動改札機|じどうかいさつき} (automatic ticket gate), {地産地消|ちさんちしょう} (local production/consumption), {自給自足|じきゅうじそく} (self-sufficiency), {拳銃|けんじゅう} (handgun), {生野菜|なまやさい} (raw vegetables), {通話料|つうわりょう} (call charges), {労働力|ろうどうりょく} (labor force), {幸福感|こうふくかん} (sense of happiness), {冷食|れいしょく} (frozen food), {二泊三日|にはくみっか} (3 days 2 nights)
- **Nouns/suru verbs (3)**: {全快|ぜんかい} (complete recovery), {改行|かいぎょう} (line break), {口座開設|こうざかいせつ} (opening a bank account)
- **Nouns/adjective-no (3)**: {生乾|なまがわ}き (half-dried), {中規模|ちゅうきぼ} (medium-scale), {高性能|こうせいのう} (high performance)
- **Expressions (4)**: {嫌気|いやけ}が{差|さ}す (to be fed up), {席|せき}を{譲|ゆず}る (to give up one's seat), お{暇|いとま}する (to take one's leave), {手際|てぎわ}のいい (efficient)
- **Nouns (other) (3)**: {仕切|しき}り{直|なお}し (fresh start), {運任|うんまか}せ (trusting to luck), {三十日|みそか} (last day of month)
- **Verb (1)**: {盛|も}り{立|た}てる (to liven up)
- **Proper noun (1)**: {東南|とうなん}アジア (Southeast Asia)
- **Onomatopoeia (1)**: けらけら (cackling laughter)

Notable features:
- Daily life: {生乾|なまがわ}き, {冷食|れいしょく}, {生野菜|なまやさい}, {交通渋滞|こうつうじゅうたい}
- Travel: {二泊三日|にはくみっか}, {自動改札機|じどうかいさつき}, {東南|とうなん}アジア
- Business/economy: {備品|びひん}, {口座開設|こうざかいせつ}, {労働力|ろうどうりょく}
- Society: {地産地消|ちさんちしょう}, {自給自足|じきゅうじそく}, {幸福感|こうふくかん}
- Multi-sense: {席|せき}を{譲|ゆず}る (2: literal seat + figurative position), {盛|も}り{立|た}てる (2: enliven + support)

Total entries: ~16,302 → ~16,332 (approximate)
Remaining candidates: ~3,475 → ~3,445 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
