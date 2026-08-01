# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-08-01
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
| Total entries | ~19,088 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,289 (open) |
| Candidate words | ~5,472 |
| Cross-references | ~3,400 |
| Example sentences | ~53,200 |
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

### 2026-08-01 (Routine v2: new-entries — 20 New Entries, IDs 30298–30317)
Created 20 general-tier entries, **draining the "seen in entry" lane completely** (all 16 available were created). The seen-in sixteen: the clipped day names {月曜|げつよう} and {水曜|すいよう}; ベーコン; the three mimetics うねうね / にょろにょろ / くにゃくにゃ, which now sit alongside 06717 くねくね and 25196 ぐにゃぐにゃ with SIMILAR WORDS sections spelling out fixed-shape vs. creature-in-motion vs. loss-of-stiffness; the yojijukugo {孤軍奮闘|こぐんふんとう}; {金太郎飴|きんたろうあめ} (two senses — the candy, and the figurative "cookie-cutter", which is now the commoner one); {今週末|こんしゅうまつ} (documenting the bare-adverbial use without に); イクボス, **completing the pair** with 06723 イクメン; the two contrast pairs {動産|どうさん}↔{不動産|ふどうさん} and {自己資本|じこしほん}↔{他人資本|たにんしほん}; {比|ひ} (standalone ratio plus the far commoner {前年比|ぜんねんひ} suffix use); なんとも (two senses keyed entirely to whether the predicate is affirmative or negative); {物|もの}の{哀|あわ}れ; and ノスタルジー, **paired** with 06000 {郷愁|きょうしゅう}. The other 4 are hand-picked, because the ~1,000-strong non-seen pool remains **heavily polluted** — a filter for plain 2-kanji candidates returned 112 items of which a large share are not real words (権使, 些道, 個尊, 怒燥, 発炭, 人義, 印示, 下告, 消痛), with numeric fragments (三百, 八十, 六人) and transparent compounds making up most of the rest; a `[pattern]` observation asks for a `clean_up_candidates_list.md` pass before this pool is used for bulk creation again. The four: {一分|いっぷん} (documenting the whole いっぷん/にふん/さんぷん counter set and the いちぶ reading of the same characters), {冒涜的|ぼうとくてき} (na-adjective off existing 19484 {冒涜|ぼうとく}), {学科長|がっかちょう} (placed in the {学部長|がくぶちょう}/{学長|がくちょう}/{校長|こうちょう} series), and {技巧派|ぎこうは} (the {派|は}-suffix performer-type series). Conjugation added to the one suru-verb; **no new kanji**. 1 stale candidate removed (C19811 {雄蕊|おしべ} → existing 29501 {雄|お}しべ, an orthographic variant that `manage_candidates.py sync` cannot see); 6 added from words the new entries reference; 997 remain. §4 cross-model self-check on all 20 changed entries: **2 flagged, 0 applied, 2 rejected** — both tag-vocabulary nits (`onomatopoeia` asked for in `semantic` when the project keeps it in `pos`; an in-list `grammatical`→`expression` narrowness substitution, rejected by §A policy). $0.0087.

- **Time / calendar (3)**: {月曜|げつよう}, {水曜|すいよう}, {今週末|こんしゅうまつ}
- **Mimetic adverbs (3)**: うねうね, にょろにょろ, くにゃくにゃ
- **Business / law / figures (4)**: {動産|どうさん}, {自己資本|じこしほん}, {比|ひ}, イクボス
- **Culture / aesthetics (3)**: {金太郎飴|きんたろうあめ}, {物|もの}の{哀|あわ}れ, ノスタルジー
- **Function / expression (2)**: なんとも, {孤軍奮闘|こぐんふんとう}
- **Food / everyday (2)**: ベーコン, {一分|いっぷん}
- **People / evaluation (3)**: {学科長|がっかちょう}, {技巧派|ぎこうは}, {冒涜的|ぼうとくてき}

### 2026-07-31 (Routine v2: new-entries — 19 New Entries, IDs 30279–30297)
Created 19 general-tier entries, **draining the usable "seen in entry" lane again** (13 available, 12 created). The 13th, C22661 {激高|げきこう}, was dropped as stale: 09005 {激昂|げきこう} already documents {激高|げきこう} as a kanji variant of the same word, so a separate entry would have duplicated it — a case `check_duplicate.py` surfaced only as a parenthetical homophone note. The seen-in twelve: あんまん (completing the steamed-bun cluster with 28810 {肉|にく}まん / 30274 {中華|ちゅうか}まん), {口|くち}やかましい (linked to 16036 {口|くち}うるさい), {気|き}が{弱|よわ}い (**closing the antonym pair** with 30270 {気|き}が{強|つよ}い), ドラフト (two senses: document draft / sports player draft), {買|か}い{足|た}す (godan-su transitive), とことこ (mimetic adverb), {私見|しけん}, どこまでも (two senses), {断|だん}じて (two senses, negative and affirmative), and the three-word "of its own accord" set ひとりでに / おのずから / {自然|しぜん}と — all three of which 06714 おのずと's own notes had marked `noentry`, and whose SIMILAR WORDS sections now spell out the distinction between absence of an agent, the natural course of things, and everyday effortlessness. The other 7 are hand-picked, since the ~1,000-strong non-seen candidate pool remains **heavily polluted** with inflected forms, compositional phrases, and apparent non-words (a fuller `[pattern]` observation was logged again): のように and ような (the adverbial/attributive comparison pair, cross-referencing each other; ような was the most-referenced real word among the dictionary's own `noentry` links), そうですね (agreement vs. thinking-filler senses), そうやって and ああやって (**completing the demonstrative manner series** with 27245 こうやって and 27496 どうやって), {何|なん}の (including the {何|なん}の…も + negative frame), and {買|か}い{置|お}き (contrasted with 08047 {買|か}いだめ and 30283 {買|か}い{足|た}す). One pre-existing fix: 30270 {気|き}が{強|つよ}い had a furigana typo in its notes ({勝|き}ち{気|き} for {勝|か}ち{気|き}). Conjugation tables added to the godan verb, the suru-verb, and the 2 i-adjectives; **no new kanji**. 3 stale candidates removed (C22661, C16588 のごとく → 20861 ごとく, C19496 関して → 06944 に関して); 996 candidates remain. §4 cross-model self-check on all 20 changed entries: **clean — 20/20, 0 flagged, 0 applied, 0 rejected**. $0.0088.

- **Grammar / function (5)**: のように, ような, {何|なん}の, そうやって, ああやって
- **Adverbs (5)**: とことこ, どこまでも, {断|だん}じて, ひとりでに, おのずから
- **Adverbs, cont. (1)**: {自然|しぜん}と
- **Personality / people (2)**: {口|くち}やかましい, {気|き}が{弱|よわ}い
- **Daily life / shopping (4)**: あんまん, {買|か}い{足|た}す, {買|か}い{置|お}き, ドラフト
- **Communication (2)**: {私見|しけん}, そうですね

### 2026-07-31 (Routine v2: new-entries — 20 New Entries, IDs 30259–30278)
Created 20 general-tier entries, **draining the entire "seen in entry" candidate pool again** (14 available, all 14 created — no stale variants this time; `check_duplicate.py` returned `OK` for all, surfacing only the {開設|かいせつ}する ↔ 17850 {解説|かいせつ}する homophone, which became a `prominent_see_also`). The seen-in fourteen close references made by the 30241–30254 batch and by the comprehensive-polish frontier around 06698–06712. The batch adds **three grammar/function entries** the dictionary had referenced but never defined: どころか (two senses — "far from ~" and "let alone ~", with the connection rules for nouns/verbs/adjectives), そのような (the formal written counterpart of そんな), and {次|つぎ}に (sequencing adverb, two senses). {歓送会|かんそうかい} completes the party cluster alongside 16080 {送別会|そうべつかい}, 15791 {歓迎会|かんげいかい} and 30247 {歓送迎会|かんそうげいかい}; {漫画喫茶|まんがきっさ} and ネットカフェ cross-reference each other and 01079 {喫茶店|きっさてん}/06767 カフェ. The other 6 are hand-picked standalone lexemes, since the ~1,000-strong non-seen candidate pool remains **heavily polluted** with corpus noise, inflected forms of existing entries, and fully compositional compounds — a fuller `[pattern]` observation was logged again this run. Conjugation tables added to the godan verb, the suru-verb, and the 2 i-adjectives; **no new kanji**. 3 referenced-but-missing words added as candidates (C22649–C22651: あんまん, {口|くち}やかましい, {気|き}が{弱|よわ}い). §4 cross-model self-check on all 20 changed entries: **19 clean, 1 flagged — 1 applied, 1 rejected** ("childhood" dropped from {少年時代|しょうねんじだい}'s top-level gloss as too broad; the duplicate flag against the sense gloss was rejected, since that gloss never contained the word). $0.0088.

- **Grammar / function words (3)**: どころか, そのような, {次|つぎ}に
- **Work / social life (3)**: {歓送会|かんそうかい}, {宿泊客|しゅくはくきゃく}, {少年時代|しょうねんじだい}
- **Places / eating out (4)**: {漫画喫茶|まんがきっさ}, ネットカフェ, ファストフード, {中華|ちゅうか}まん
- **Verbs / adjectives (4)**: {飛|と}び{掛|か}かる, やかましい, おしとやか, {気|き}が{強|つよ}い
- **Administration / finance (3)**: {行政機関|ぎょうせいきかん}, {譲渡費用|じょうとひよう}, {開設|かいせつ}する
- **Other (3)**: {平常時|へいじょうじ}, {下痢止|げりど}め, {反対方向|はんたいほうこう}

### 2026-07-30 (Routine v2: new-entries — 18 New Entries, IDs 30241–30258)
Created 18 general-tier entries, **draining the entire "seen in entry" candidate pool again** (21 available; 18 created, 3 removed as stale). The three dropped were {逆転|ぎゃくてん}する (06839 already carries `noun` + `verb-suru`), {心掛|こころが}ける (okurigana variant of 10015 {心|こころ}がける), and {引|ひ}っ{越|こ}し (okurigana variant of 03704 {引越|ひっこ}し) — `check_duplicate.py` returned `OK` for all three and surfaced two of them only as parenthetical homophone notes, the same gap logged as a `[tooling]` observation on 2026-07-29. The batch completes the accounting cluster the last four runs have been building ({仮払金|かりばらいきん} finishing the {仮払|かりばら}い pair from 30222–30240, {取得費|しゅとくひ} joining the 費-expense family) and adds **three grammar entries** the dictionary had referenced but never defined: the general conditional ば (cross-referenced against 09575 なら, with the four-way ば/たら/なら/と contrast) and the feminine sentence-final combinations わよ and のよ, which join the existing ね/よ/ぜ/かしら particle set. {創|つく}る completes the つくる orthography trio alongside 00481 {作|つく}る and 17751 {造|つく}る, with a three-way ORTHOGRAPHY note and reciprocal cross-references. Conjugation table added to the one godan verb; **no new kanji**. 5 referenced-but-missing words added as candidates (C22635–C22639); the other 13 words named in the new notes were already entries or candidates. §4 cross-model self-check on all 18 changed entries: **17 clean, 1 flagged — 1 applied, 0 rejected** (`person` removed from {青春時代|せいしゅんじだい}'s semantic tags; it is a period, not a person). $0.0079.

- **Grammar / particles (3)**: ば, わよ, のよ
- **Accounting / finance (2)**: {仮払金|かりばらいきん}, {取得費|しゅとくひ}
- **Work / school life (4)**: {歓送迎会|かんそうげいかい}, {三学期|さんがっき}, {本試験|ほんしけん}, {時間切|じかんぎ}れ
- **Tools / technical (2)**: {充電式|じゅうでんしき}, {刈|か}り{払|はら}い{機|き}
- **Places / people / nature (4)**: {滞在者|たいざいしゃ}, {本国|ほんごく}, {水遊|みずあそ}び, {細流|さいりゅう}
- **Other (3)**: {非常時|ひじょうじ}, {青春時代|せいしゅんじだい}, {創|つく}る

### 2026-07-29 (Routine v2: new-entries — 19 New Entries, IDs 30222–30240)
Created 19 general-tier entries, **draining the entire "seen in entry" candidate pool** (20 available; 19 created, 1 dropped). The dropped one — {売|う}り{上|あ}げ (うりあげ) — is only an okurigana variant of the existing entry `04102_uriage` ({売上|うりあげ}), so it was removed from `candidate_words.json` instead of becoming a duplicate; `check_duplicate.py` again returned `OK` and surfaced the collision only as a parenthetical homophone note, the same gap logged as a `[tooling]` observation on 2026-07-29. The batch continues the accounting cluster the last three runs have been building out ({前払金|まえばらいきん}, {内金|うちきん}, {償却|しょうきゃく}, {減価償却費|げんかしょうきゃくひ}, {仮払|かりばら}い, {予備費|よびひ}), all of them referenced from the 30203–30221 finance entries, and adds two mimetic adverbs (ちらほら, ぽつりぽつり) that join 06683 ぽつぽつ and 10525 まばら in the sparse-scatter family. Homophone cross-references were added where the duplicate check surfaced real collisions: {償却|しょうきゃく} ↔ 22409 {焼却|しょうきゃく}, {出航|しゅっこう} ↔ 11764 {出港|しゅっこう}. Conjugation tables added to the 4 suru-verbs ({償却|しょうきゃく}, {仮払|かりばら}い, {出航|しゅっこう}, グローバル{化|か}); **no new kanji**. 5 referenced-but-missing words added as candidates (C22614–C22618: {非常時|ひじょうじ}, {充電式|じゅうでんしき}, {仮払金|かりばらいきん}, {取得費|しゅとくひ}, {刈|か}り{払|はら}い{機|き}). §4 cross-model self-check on all 19 changed entries: **clean — 19/19, 0 flagged, 0 applied, 0 rejected**. $0.0083.

- **Accounting / finance (6)**: {前払金|まえばらいきん}, {内金|うちきん}, {償却|しょうきゃく}, {減価償却費|げんかしょうきゃくひ}, {仮払|かりばら}い, {予備費|よびひ}
- **Tools / technical (3)**: インパクトドライバー, {草刈|くさか}り{機|き}, {差|さ}し{込|こ}み{口|ぐち}
- **Transport / weather (3)**: {出航|しゅっこう}, {便数|びんすう}, {雨風|あめかぜ}
- **Adverbs / expressions (3)**: ちらほら, ぽつりぽつり, それなり
- **Other (4)**: {急場|きゅうば}, {前作|ぜんさく}, {暗記力|あんきりょく}, グローバル{化|か}
