# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-17
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
| Total entries | ~17,314 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~14,515 (open) |
| Candidate words | ~2,465 |
| Cross-references | ~3,400 |
| Example sentences | ~50,200 |
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

### 2026-03-17 (Vocabulary Expansion - 35 New Entries, Session 444)
Added 35 new dictionary entries (IDs 17267-17303) from candidate_words.json:

- **Suru verbs (9)**: {発揮|はっき}する (to demonstrate), {主催|しゅさい}する (to host), {反論|はんろん}する (to refute), {推進|すいしん}する (to promote), {無視|むし}する (to ignore), {起動|きどう}する (to start up), {包装|ほうそう}する (to wrap), {操縦|そうじゅう}する (to pilot), {閉口|へいこう}する (to be stumped)
- **Godan verbs (3)**: {黒|くろ}ずむ (to darken), {身籠|みごも}る (to become pregnant), {見|み}つけ{出|だ}す (to discover)
- **Nouns (7)**: {慌|あわ}て{者|もの} (hasty person), {横向|よこむ}き (sideways), {特撮|とくさつ} (tokusatsu), {小動物|しょうどうぶつ} (small animal), {言|い}い{争|あらそ}い (quarrel), {錠剤|じょうざい} (tablet), {読書感想文|どくしょかんそうぶん} (book report)
- **Noun/adjective (3)**: {未解決|みかいけつ} (unresolved), {純白|じゅんぱく} (pure white), {悪|わる}ふざけ (prank)
- **Nouns (culture) (3)**: {炊|た}き{出|だ}し (soup kitchen), {確執|かくしつ} (feud), {謹賀新年|きんがしんねん} (Happy New Year)
- **Expressions (4)**: お{見|み}えになる (to come, honorific), {相槌|あいづち}を{打|う}つ (back-channel), {口|くち}が{減|へ}らない (always has comeback), {身|み}の{毛|け}もよだつ (hair-raising)
- **Adverbs (2)**: {足早|あしばや}に (briskly), {交互|こうご}に (alternately)
- **Conjunction (1)**: それゆえ (therefore)
- **Other (3)**: おっちょこちょい (scatterbrain), きちんとした (neat/proper), {落葉|らくよう} (falling leaves)

Notable features:
- Body/emotions: {閉口|へいこう}する, {身|み}の{毛|け}もよだつ, {確執|かくしつ}
- Technology: {起動|きどう}する, {操縦|そうじゅう}する, {特撮|とくさつ}
- Communication: {相槌|あいづち}を{打|う}つ, {反論|はんろん}する, {口|くち}が{減|へ}らない, {言|い}い{争|あらそ}い
- Culture: {謹賀新年|きんがしんねん}, {炊|た}き{出|だ}し, {読書感想文|どくしょかんそうぶん}
- New kanji: 2,560 → 2,561 ({錠|じょう})

Total entries: ~17,314 → ~17,349 (approximate)
Remaining candidates: ~2,465 → ~2,430 (35 removed)

### 2026-03-17 (Vocabulary Expansion - 35 New Entries, Session 443)
Added 35 new dictionary entries (IDs 17231-17266) from candidate_words.json:

- **Verbs (8)**: {甦|よみがえ}る (to revive), {彷徨|さまよ}う (to wander), {可愛|かわい}がる (to dote on), ボケる (to play the fool), {解|ほぐ}れる (to come loose), {擦|す}り{減|へ}る (to wear down), {結|むす}び{付|つ}く (to be connected)
- **Na-adjectives (4)**: {逆|さか}さま (upside down), {控|ひか}えめ (moderate), {露|あらわ} (exposed), おろそか (negligent)
- **Nouns (17)**: {縦|たて} (vertical), しつけ (discipline), {道|みち}しるべ (guidepost), ひき{肉|にく} (ground meat), {炭坑|たんこう} (coal mine), {物置|ものおき} (storage shed), {甘|あま}み (sweetness), {目途|めど} (prospect), {肩書|かたがき} (title), {街並|まちな}み (townscape), {落葉|おちば} (fallen leaves), {顔|かお}なじみ (familiar face), {測位|そくい} (positioning), {余|あま}り (remainder), {左記|さき} (mentioned below), {控室|ひかえしつ} (waiting room), {従兄弟|いとこ} (cousin)
- **Adverbs (2)**: {度々|たびたび} (often), はるばる (from afar)
- **Onomatopoeia (3)**: ガラガラ (empty/rattling), ボロボロ (worn out), ベタベタ (sticky/clingy)
- **Other (1)**: {一押|いちお}し (top recommendation), {日次|にちじ} (daily), {足|あし}かせ (shackle/hindrance)

Notable features:
- Daily life/food: ひき{肉|にく}, {甘|あま}み, {物置|ものおき}, {控室|ひかえしつ}
- Onomatopoeia: ガラガラ, ボロボロ, ベタベタ
- Business: {目途|めど}, {肩書|かたがき}, {日次|にちじ}, {左記|さき}
- Family/people: {従兄弟|いとこ}, {顔|かお}なじみ
- Nature: {落葉|おちば}, {街並|まちな}み
- New kanji: 2,557 → 2,560 ({坑|こう}, {徨|ほう}, {甦|そ})

Total entries: ~17,279 → ~17,314 (approximate)
Remaining candidates: ~2,500 → ~2,465 (35 removed)

### 2026-03-17 (Vocabulary Expansion - 35 New Entries, Session 442)
Added 35 new dictionary entries (IDs 17196-17230) from candidate_words.json:

- **Particles/expressions (3)**: につき (regarding/per), といっても (although one might say), {難|がた}い (difficult to do, suffix)
- **Verbs (9)**: おられる (to be, honorific), {場馴|ばな}れる (to get used to), ませる (to be precocious), {結|むす}び{付|つ}ける (to tie/connect), {埋|う}め{尽|つ}くす (to fill completely), {流|なが}される (to be swept away), {分岐|ぶんき}する (to branch off), {書|か}き{崩|くず}す (to write in cursive), {埋|う}め{尽|つ}くす (to fill up)
- **Nouns (19)**: {生返事|なまへんじ} (vague reply), {一学期|いちがっき} (first semester), {零時|れいじ} (midnight), {国内外|こくないがい} (domestic and foreign), {体得|たいとく} (mastery through experience), {実力差|じつりょくさ} (skill gap), {進学校|しんがくこう} (prep school), {車体|しゃたい} (car body), {揉|も}み{返|かえ}し (post-massage soreness), {丸洗|まるあら}い (full wash), {納入|のうにゅう} (delivery/payment), {検品|けんぴん} (goods inspection), {不義理|ふぎり} (ingratitude), {適齢期|てきれいき} (marriageable age), {徒競走|ときょうそう} (footrace), {古美術|こびじゅつ} (antique art), {備考欄|びこうらん} (remarks column), {取引所|とりひきじょ} (exchange market), {花街|かがい} (geisha district)
- **Other nouns (2)**: {送電|そうでん} (power transmission), {人類学|じんるいがく} (anthropology)
- **Noun (1)**: {投|な}げ{技|わざ} (throwing technique)
- **Adjective (1)**: {面映|おもは}ゆい (bashful/self-conscious)

Notable features:
- Grammar/language: につき, といっても, {難|がた}い, おられる
- Culture: {花街|かがい}, お{座敷|ざしき}, {古美術|こびじゅつ}, {不義理|ふぎり}
- Daily life: {生返事|なまへんじ}, {揉|も}み{返|かえ}し, {丸洗|まるあら}い, {備考欄|びこうらん}
- Education/sports: {一学期|いちがっき}, {進学校|しんがくこう}, {徒競走|ときょうそう}
- Business: {納入|のうにゅう}, {検品|けんぴん}, {取引所|とりひきじょ}

Total entries: ~17,244 → ~17,279 (approximate)
Remaining candidates: ~2,535 → ~2,500 (35 removed)

### 2026-03-16 (Vocabulary Expansion - 35 New Entries, Session 441)
Added 35 new dictionary entries (IDs 17161-17195) from candidate_words.json:

- **Nouns (14)**: {夜食|やしょく} (late-night snack), {吉兆|きっちょう} (good omen), {廃屋|はいおく} (abandoned house), {激痛|げきつう} (intense pain), {成果物|せいかぶつ} (deliverable), {死語|しご} (dead word), {広範囲|こうはんい} (wide range), {古文|こぶん} (classical Japanese), {短期間|たんきかん} (short period), {御社|おんしゃ} (your company), {料理酒|りょうりしゅ} (cooking sake), {暗殺者|あんさつしゃ} (assassin), {美男子|びだんし} (handsome man), {石像|せきぞう} (stone statue)
- **Nouns with figurative senses (3)**: {古傷|ふるきず} (old wound/past disgrace), {裸足|はだし} (barefoot), {巨木|きょぼく} (giant tree)
- **Na-adjective (1)**: {大柄|おおがら} (large-framed/bold-patterned)
- **Noun/suru verbs (10)**: {優遇|ゆうぐう} (favorable treatment), {解任|かいにん} (dismissal), {素揚|すあ}げ (deep-frying without batter), {存在|そんざい}する (to exist), {反映|はんえい}する (to reflect), {露呈|ろてい}する (to be exposed), {妥協|だきょう}する (to compromise), {交渉|こうしょう}する (to negotiate), {移住|いじゅう}する (to relocate), {解決|かいけつ}する (to solve)
- **Verbs (3)**: {教壇|きょうだん} (teacher's platform), {商|あきな}い (trade/business), {責任者|せきにんしゃ} (person in charge)
- **Ichidan verbs (3)**: {報|ほう}じる (to report), {仕損|しそん}じる (to fail), {逸|そ}れる (to stray)
- **Noun (1)**: {困惑|こんわく}する (to be bewildered)

Notable features:
- Food/cooking: {夜食|やしょく}, {料理酒|りょうりしゅ}, {素揚|すあ}げ
- Business: {御社|おんしゃ}, {成果物|せいかぶつ}, {解任|かいにん}, {交渉|こうしょう}する, {責任者|せきにんしゃ}
- Body/health: {激痛|げきつう}, {古傷|ふるきず}, {裸足|はだし}, {大柄|おおがら}
- Education/language: {古文|こぶん}, {死語|しご}, {教壇|きょうだん}
- Nature/culture: {巨木|きょぼく}, {石像|せきぞう}, {吉兆|きっちょう}

Total entries: ~17,209 → ~17,244 (approximate)
Remaining candidates: ~2,570 → ~2,535 (35 removed)

### 2026-03-16 (Vocabulary Expansion - 35 New Entries, Session 440)
Added 35 new dictionary entries (IDs 17126-17160) from candidate_words.json:

- **Nouns (22)**: {前書|まえが}き (preface), {敷物|しきもの} (rug), {留|と}め{具|ぐ} (fastener), {形跡|けいせき} (traces), {種子|しゅし} (seed), {諸君|しょくん} (everyone), {合金|ごうきん} (alloy), {貴金属|ききんぞく} (precious metal), {茶筒|ちゃづつ} (tea caddy), {同世代|どうせだい} (same generation), {大文字|おおもじ} (uppercase), {甘味処|かんみどころ} (sweets shop), {全盛|ぜんせい} (heyday), {別冊|べっさつ} (supplement), {祝賀会|しゅくがかい} (celebration), {野外|やがい} (outdoors), {副食|ふくしょく} (side dish), {飴細工|あめざいく} (candy sculpture), {同調圧力|どうちょうあつりょく} (peer pressure), {知識人|ちしきじん} (intellectual), {客観性|きゃっかんせい} (objectivity), {無断欠勤|むだんけっきん} (unauthorized absence)
- **Na-adjectives (2)**: {不健康|ふけんこう} (unhealthy), {自主的|じしゅてき} (voluntary)
- **Noun/suru verbs (10)**: {楽観|らっかん} (optimism), {追記|ついき} (postscript), {失効|しっこう} (expiration), {提言|ていげん} (proposal), {潜伏|せんぷく} (hiding/latency), {登用|とうよう} (appointment), {嘱託|しょくたく} (contract worker), {合理化|ごうりか} (rationalization), {餓死|がし} (starvation), {過熱|かねつ} (overheating)
- **Expression (1)**: {早寝早起|はやねはやお}き (early to bed, early to rise)

Notable features:
- Society/culture: {同調圧力|どうちょうあつりょく}, {知識人|ちしきじん}, {甘味処|かんみどころ}, {飴細工|あめざいく}
- Business/work: {登用|とうよう}, {嘱託|しょくたく}, {合理化|ごうりか}, {無断欠勤|むだんけっきん}, {提言|ていげん}
- Materials: {合金|ごうきん}, {貴金属|ききんぞく}
- Daily life: {敷物|しきもの}, {留|と}め{具|ぐ}, {茶筒|ちゃづつ}, {包装|ほうそう}
- New kanji: 2,555 → 2,557 ({嘱|しょく}, {餓|が})

Total entries: ~17,174 → ~17,209 (approximate)
Remaining candidates: ~2,605 → ~2,570 (35 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
