# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-07-31
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

### 2026-07-29 (Routine v2: new-entries — 19 New Entries, IDs 30203–30221)
Created 19 general-tier entries. **12 of the 14 "seen in entry" candidates were created**, draining that lane; the other two were dropped as stale orthographic variants of existing entries (のこぎり → 05477 {鋸|のこぎり}, {折|お}りたたみ{傘|がさ} → 20390 {折|お}り{畳|たた}み{傘|がさ}) — `check_duplicate.py` returned `OK` for both and flagged the collision only in a parenthetical homophone note, which is logged as a `[tooling]` observation. The seen-in twelve: {売掛金|うりかけきん} (accounts receivable), {販売促進費|はんばいそくしんひ} (sales promotion expenses, full form of {販促費|はんそくひ}), {試食会|ししょくかい} (food tasting event), チェーンソー (chainsaw), {損|そん}をする (to lose out), {端子|たんし} (terminal / port), {十四日|じゅうよっか} and {二十四日|にじゅうよっか} (the two irregular よっか dates, both marked `noentry` in 02985 {四日|よっか}'s own notes), {抜|ぬ}かす (to skip; to overtake — two senses, godan-su transitive), {話|はな}し{出|だ}す and {歩|ある}き{出|だ}す (godan-su intransitive, joining the 〜{出|だ}す onset family with 06678/06679/06343/03004), {内履|うちば}き (indoor shoes). The other 7 are hand-picked standalone lexemes, since the ~1,000-strong non-seen candidate pool remains **heavily polluted** with non-words and free syntax — a fuller `[pattern]` observation was logged this run: {買掛金|かいかけきん} (accounts payable), {未払金|みばらいきん} (accrued payable), {前受金|まえうけきん} (advance received), {減価償却|げんかしょうきゃく} (depreciation; noun + verb-suru), {経費精算|けいひせいさん} (expense reimbursement; noun + verb-suru), {電動|でんどう}ドリル (electric drill), {電動|でんどう}ドライバー (power screwdriver). The run closes several mirror pairs: {売掛金|うりかけきん} ↔ {買掛金|かいかけきん}, {未払金|みばらいきん} ↔ {未収金|みしゅうきん} (30183), {損|そん}をする ↔ {得|とく}をする (30190), {内履|うちば}き ↔ {外履|そとば}き (27460), and {試食会|ししょくかい} ↔ {試飲会|しいんかい} (30193). Conjugation tables added to the 3 godan verbs and the 2 suru-verbs; **no new kanji**. 8 referenced-but-missing words added as candidates (C22594–C22601); 2 stale candidates removed. §4 cross-model self-check on all 19 changed entries: **clean — 19/19, 0 flagged, 0 applied, 0 rejected**. $0.0084.

- **Accounting / finance (6)**: {売掛金|うりかけきん}, {買掛金|かいかけきん}, {未払金|みばらいきん}, {前受金|まえうけきん}, {減価償却|げんかしょうきゃく}, {経費精算|けいひせいさん}
- **Business / events (2)**: {販売促進費|はんばいそくしんひ}, {試食会|ししょくかい}
- **Tools / technical (4)**: チェーンソー, {電動|でんどう}ドリル, {電動|でんどう}ドライバー, {端子|たんし}
- **Verbs / expressions (4)**: {抜|ぬ}かす, {話|はな}し{出|だ}す, {歩|ある}き{出|だ}す, {損|そん}をする
- **Dates / daily life (3)**: {十四日|じゅうよっか}, {二十四日|にじゅうよっか}, {内履|うちば}き
