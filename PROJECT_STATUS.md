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
| Total entries | ~17,454 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~14,655 (open) |
| Candidate words | ~2,325 |
| Cross-references | ~3,400 |
| Example sentences | ~50,600 |
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

### 2026-03-17 (Vocabulary Expansion - 35 New Entries, Session 447)
Added 35 new dictionary entries (IDs 17374-17408) from candidate_words.json:

- **Nouns (19)**: {塗|ぬ}り{薬|ぐすり} (ointment), {鉛筆削|えんぴつけず}り (pencil sharpener), {看板|かんばん}メニュー (signature dish), {鈍痛|どんつう} (dull pain), {事務職|じむしょく} (office job), {魔法瓶|まほうびん} (thermos), {防寒|ぼうかん} (cold protection), {買|か}い{替|か}え (replacement purchase), {健診|けんしん} (health checkup), {限定版|げんていばん} (limited edition), {宝庫|ほうこ} (treasure house), {土下座|どげざ} (prostration), {起源|きげん} (origin), {無駄足|むだあし} (wasted trip), {宅急便|たっきゅうびん} (courier service), {背骨|せぼね} (backbone), {綱引|つなひ}き (tug-of-war), {汚職|おしょく} (corruption), {武者震|むしゃぶる}い (excited trembling)
- **Na-adjectives (4)**: {赤裸々|せきらら} (frank, candid), {不鮮明|ふせんめい} (unclear, blurred), {甚大|じんだい} (enormous, severe), {節々|ふしぶし} (joints / various points)
- **Nouns/suru verbs (2)**: {表彰|ひょうしょう} (commendation), {黙祷|もくとう} (silent prayer)
- **Noun (humble) (1)**: {弊社|へいしゃ} (our company)
- **Noun (clothing) (1)**: {半|はん}ズボン (shorts)
- **Noun (emotion) (1)**: {至福|しふく} (bliss)
- **Verbs (2)**: {干上|ひあ}がる (to dry up), {鉢合|はちあ}わせる (to bump into)
- **Noun (animal/culture) (1)**: {雛|ひな} (chick / hina doll)
- **Noun (name painting/film) (1)**: {名画|めいが} (famous painting / classic film)
- **Expressions (3)**: {真|ま}っ{赤|か}な{嘘|うそ} (blatant lie), {我|われ}に{返|かえ}る (to come to one's senses), {必着|ひっちゃく} (must arrive by)

Notable features:
- Health/body: {塗|ぬ}り{薬|ぐすり}, {鈍痛|どんつう}, {健診|けんしん}, {背骨|せぼね}, {節々|ふしぶし}
- Business: {弊社|へいしゃ}, {事務職|じむしょく}, {表彰|ひょうしょう}, {汚職|おしょく}
- Culture: {土下座|どげざ}, {黙祷|もくとう}, {雛|ひな}, {綱引|つなひ}き
- Daily life: {宅急便|たっきゅうびん}, {魔法瓶|まほうびん}, {買|か}い{替|か}え, {防寒|ぼうかん}
- New kanji: 2,563 → 2,565 ({彰|しょう}, {祷|とう})

Total entries: ~17,419 → ~17,454 (approximate)
Remaining candidates: ~2,360 → ~2,325 (35 removed)

### 2026-03-17 (Vocabulary Expansion - 35 New Entries, Session 446)
Added 35 new dictionary entries (IDs 17339-17373) from candidate_words.json:

- **Suru verbs (9)**: {前進|ぜんしん}する (to advance), {後退|こうたい}する (to retreat), {予防|よぼう}する (to prevent), {防止|ぼうし}する (to stop), {侵入|しんにゅう}する (to invade), {対抗|たいこう}する (to oppose), {選出|せんしゅつ}する (to elect), {継承|けいしょう}する (to inherit), {記述|きじゅつ}する (to describe)
- **Nouns (15)**: {告知|こくち} (notice), {男女|だんじょ}{平等|びょうどう} (gender equality), {排斥|はいせき} (exclusion), {高評価|こうひょうか} (positive rating), {自己|じこ}{評価|ひょうか} (self-evaluation), {文化|ぶんか}{遺産|いさん} (cultural heritage), {温室|おんしつ}{効果|こうか} (greenhouse effect), {健康|けんこう}{食品|しょくひん} (health food), {早番|はやばん} (early shift), {模範|もはん}{解答|かいとう} (model answer), {個別|こべつ}{指導|しどう} (individual tutoring), {車線|しゃせん}{変更|へんこう} (lane change), {着信|ちゃくしん}{履歴|りれき} (call history), {栄養|えいよう}{剤|ざい} (supplement), {変化球|へんかきゅう} (breaking ball)
- **Informal nouns (2)**: {朝飯|あさめし} (breakfast), {昼飯|ひるめし} (lunch)
- **Adjective (1)**: {写実的|しゃじつてき} (realistic)
- **Verb (1)**: {切|き}り{揃|そろ}える (to trim evenly)
- **Expressions (2)**: {口|くち}を{利|き}く (to speak/put in a word), {相手|あいて}にする (to deal with)
- **Other nouns (5)**: {運転|うんてん}{代行|だいこう} (designated driver), {鉄鋼|てっこう} (iron and steel), {世捨|よす}て{人|びと} (hermit), {指導力|しどうりょく} (leadership), {大技|おおわざ} (major technique)

Notable features:
- Prevention/defense: {予防|よぼう}する, {防止|ぼうし}する, {侵入|しんにゅう}する, {対抗|たいこう}する
- Society/culture: {男女|だんじょ}{平等|びょうどう}, {排斥|はいせき}, {文化|ぶんか}{遺産|いさん}, {世捨|よす}て{人|びと}
- Modern life: {高評価|こうひょうか}, {着信|ちゃくしん}{履歴|りれき}, {運転|うんてん}{代行|だいこう}
- Education: {模範|もはん}{解答|かいとう}, {個別|こべつ}{指導|しどう}, {自己|じこ}{評価|ひょうか}
- New kanji: 2,562 → 2,563 ({斥|せき})

Total entries: ~17,384 → ~17,419 (approximate)
Remaining candidates: ~2,395 → ~2,360 (35 removed)

### 2026-03-17 (Vocabulary Expansion - 35 New Entries, Session 445)
Added 35 new dictionary entries (IDs 17304-17338) from candidate_words.json:

- **Verbs (4)**: {闘|たたか}う (to fight/struggle), あがる (to get nervous), {追|お}い{詰|つ}められる (to be cornered), {維持|いじ}する (to maintain)
- **Nouns (8)**: {闘|たたか}い (fight/struggle), {街|まち} (commercial district), {香|こう} (incense), {最少|さいしょう} (minimum), {茶碗蒸|ちゃわんむ}し (egg custard), {実写化|じっしゃか} (live-action adaptation), {四|よ}つ{角|かど} (crossroads), {水掛|みずか}け{論|ろん} (futile argument)
- **Expressions (15)**: {問答無用|もんどうむよう} (no arguing), {締|し}まりがない (slovenly), {合点|がてん}が{行|い}く (to be convinced), {可能|かのう}な{限|かぎ}り (as much as possible), {陰|かげ}りが{見|み}える (signs of decline), {余裕|よゆう}がない (no room/leeway), {見|み}るに{忍|しの}びない (unbearable to watch), {未然|みぜん}に{防|ふせ}ぐ (prevent beforehand), {事|こと}の{次第|しだい} (circumstances), {空気|くうき}を{壊|こわ}す (ruin the mood), {意識|いしき}が{遠|とお}のく (lose consciousness), {愛想|あいそ}を{振|ふ}りまく (try to please everyone), {幕|まく}を{閉|と}じる (come to an end), {耳|みみ}を{塞|ふさ}ぐ (cover one's ears), {髪|かみ}を{梳|と}かす (comb one's hair)
- **Adjective (1)**: {容姿端麗|ようしたんれい} (strikingly beautiful)
- **Adverb (1)**: {必然的|ひつぜんてき}に (inevitably)
- **Suffix (1)**: {館|かん} (hall/building)
- **Compounds (3)**: {現状打破|げんじょうだは} (breaking status quo), {読書三昧|どくしょざんまい} (absorbed in reading), {無断駐車|むだんちゅうしゃ} (unauthorized parking)
- **Conjunction (1)**: そういうわけで (for that reason)
- **Other (1)**: {型|かた}にはまる (to be conventional)

Notable features:
- Communication/social: {愛想|あいそ}を{振|ふ}りまく, {空気|くうき}を{壊|こわ}す, {耳|みみ}を{塞|ふさ}ぐ, {問答無用|もんどうむよう}, {水掛|みずか}け{論|ろん}
- Cognition: {合点|がてん}が{行|い}く, {意識|いしき}が{遠|とお}のく, あがる
- Culture/food: {茶碗蒸|ちゃわんむ}し, {香|こう}, {読書三昧|どくしょざんまい}, {実写化|じっしゃか}
- Figurative language: {陰|かげ}りが{見|み}える, {幕|まく}を{閉|と}じる, {型|かた}にはまる
- New kanji: 2,561 → 2,562 ({梳|そ})

Total entries: ~17,314 → ~17,349 (approximate)
Remaining candidates: ~2,430 → ~2,395 (35 removed)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
