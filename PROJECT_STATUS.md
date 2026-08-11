# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-08-11
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

### 2026-08-11 (Workflow: `clear-reports` skill — plain-language reports to the curator)
On Tom's instruction (given for all three of his Claude-run projects), added `.claude/skills/clear-reports/SKILL.md`: PR descriptions, end-of-run summaries, and `reviews/needs_curator.txt` flags are now written as self-contained plain English for a reader who does not follow the project run by run — what the run did stated in the project's context, internal machinery terms (mode names, P-numbers, cursors, queues, sweeps) glossed or reworded at first use, counts given against the whole dictionary, and an explicit closing line saying what needs the curator or that nothing does. Lexicographic detail stays; it is the machinery shorthand that must be translated. Referenced from `CLAUDE.md` (Skills list and the PR/merge workflow) and `prompts/routine2.md` §7 (PR body, plus a new final-report step). Entry content conventions are unchanged, and internal session logs may stay technical. No entries touched; no build needed.

### 2026-08-10 (Routine v2: new-entries — 15 New Entries, IDs 30540–30554)
Created 15 general-tier entries, **all from the "seen in entry" lane**, which this run empties again (20 available). Four of the 20 were stale duplicates that `check_duplicate.py` surfaced only as parenthetical homophone notes, and were removed: にかけて (already 30530 〜にかけて), しかない (already 30533 〜しかない), {焼印|やきいん} (already 27135 {焼|や}き{印|いん}), and {一人|ひとり}ぼっち (already 19525 {独|ひと}りぼっち). C22806 {夏目漱石|なつめそうせき} was skipped for the fifth consecutive run and stays in the list — the personal-name policy call is still the curator's. **Nine of the 15 close gaps opened by the previous run's own batch.** The three 〜{陣|じん} and 〜{派|は} entries are built as a set against 30531/30532: {報道陣|ほうどうじん} and {首脳陣|しゅのうじん} document the collective suffix that makes the word inherently plural (so {首脳陣|しゅのうじん} cannot name one executive — {幹部|かんぶ} can), and {賛成派|さんせいは}/{推進派|すいしんは} are `antonym`-linked to {反対派|はんたいは} and split on **whether the camp merely approves or actively campaigns**. {背水|はいすい}の{陣|じん} carries its {韓信|かんしん} origin and a USAGE note that it describes a deliberate commitment, so it fits poorly where someone is simply cornered by bad luck. **The five osechi entries** — {黒豆|くろまめ}, {田作|たづく}り, {祝|いわ}い{肴|ざかな}, plus the yakitori pair {砂肝|すなぎも} and ねぎま — are cross-linked into a cluster around 26981 おせち{料理|りょうり} and 30539 {数|かず}の{子|こ}, with {祝|いわ}い{肴|ざかな} carrying the Kanto/Kansai {三種|さんしゅ} split and {砂肝|すなぎも} noting that despite "sand liver" it is not レバー. {注意事項|ちゅういじこう} and {長文|ちょうぶん} come from 06850; {長文|ちょうぶん} documents the set courtesy {長文|ちょうぶん}{失礼|しつれい}しました alongside the exam sense. Rest: {運|はこ}び{込|こ}む (transitive, with the {病院|びょういん}に{運|はこ}び{込|こ}まれる passive that is how learners meet it), {言|い}い{足|た}す (against {付|つ}け{加|くわ}える, which also covers writing), and {損害額|そんがいがく} (against {被害額|ひがいがく} — payer's side vs. victim's side). Conjugation tables added to 2 godan verbs; **no new kanji**. 6 candidates added from words the new entries reference; 978 remain. §4 cross-model self-check on all 15: **2 flagged, 1 applied, 1 rejected**. $0.0065. Applied: {祝|いわ}い{肴|ざかな}'s top-level gloss read "the celebratory dishes of an osechi box", which frames the word as a subset of the box rather than as the dishes themselves; corrected to match the sense gloss. Rejected: a flag that {注意事項|ちゅういじこう}'s `formality: "formal"` should be `neutral` — the dictionary tags every 〜{事項|じこう} compound formal ({事項|じこう} 11469, {懸念事項|けねんじこう} 17071, {決議事項|けつぎじこう} 24690, {決定事項|けっていじこう} 18093), so the flag argues against a consistent internal convention rather than against an error.

- **Groups / factions (4)**: {賛成派|さんせいは}, {推進派|すいしんは}, {報道陣|ほうどうじん}, {首脳陣|しゅのうじん}
- **Food (5)**: {砂肝|すなぎも}, ねぎま, {黒豆|くろまめ}, {田作|たづく}り, {祝|いわ}い{肴|ざかな}
- **Verbs (2)**: {運|はこ}び{込|こ}む, {言|い}い{足|た}す
- **Text / money / idiom (4)**: {注意事項|ちゅういじこう}, {長文|ちょうぶん}, {損害額|そんがいがく}, {背水|はいすい}の{陣|じん}

**Escalation**: the candidate-pool contamination is now in its **fifth consecutive report** and again capped the count below the ~20 target — the "seen in entry" lane held only 20 words, four of which were duplicates, and the 971 remaining general candidates are non-words ({権使|けんし}, {些道|さどう}, {個尊|こそん}, {怒燥|どとう}), free phrases ({推薦状|すいせんじょう}を{書|か}く, {首|くび}を{上|あ}げる), and corpus noise ({火虫|ひむし}, {次元上昇|じげんじょうしょう}). A `clean_up_candidates_list.md` pass is now the binding constraint on every `new-entries` run. Second, related: three of the four stale duplicates would never have entered the list if the comprehensive-polish capture step ran `check_duplicate.py` **without** `--skip-candidates` before adding a "seen in entry" candidate — a one-line change worth making.

### 2026-08-10 (Routine v2: new-entries — 14 New Entries, IDs 30526–30539)
Created 14 general-tier entries, **all from the "seen in entry" lane** (18 available). The lane refilled since 2026-08-09 and is now empty again. Three of the 18 were stale duplicates surfaced only as parenthetical homophone notes by `check_duplicate.py` and were removed: {蕗|ふき}の{薹|とう} (already 30496 ふきのとう, kana headword), {払|はら}い{戻|もど}し (already 07343 {払戻|はらいもど}し), and {寝|ね}ぐせ (already 10626 {寝癖|ねぐせ}). C22806 {夏目漱石|なつめそうせき} was skipped for the fourth consecutive run and stays in the list — a personal-name policy call the curator has to make. **Eight of the 14 close gaps opened by the previous two runs' own batches**: {萼片|がくへん} from 30519 {萼|がく} (cross-linked, the individual segment vs. the whole calyx), {付|つ}け{値|ね} from 30525 {言|い}い{値|ね} (entered as its reciprocal — buyer's offer against seller's ask, with {定価|ていか} as the non-negotiable third term), and {残骸|ざんがい} from 30524 {瓦礫|がれき}, `related`-linked and split on **whether the original shape survives**: {残骸|ざんがい} keeps a recognizable wreck in view, {瓦礫|がれき} is formless. **{毛並|けな}み** is two-sense (6 examples) and carries a USAGE warning that sense 2 works only in the {毛並|けな}みがいい frame and keeps a racehorse smell, so it is not a neutral way to describe someone's family. **〜にかけて and 〜しかない** are the two grammar entries, each two-sense with 6 examples: にかけて splits the から〜にかけて span use (approximate endpoints — {九時|くじ}から{五時|ごじ}まで must take まで) from the boast frame 〜にかけては, and しかない documents that しか replaces は/が/を but follows other particles, with 〜だけ contrasted as the neutral counting word that carries no sense of shortage. {狂|くる}わせる is entered as the transitive pair of 02052 {狂|くる}う with the note that its subject is usually a disruptive force rather than an agent ("threw off", not "made"). {陣|じん} is two-sense with the productive suffix use ({報道|ほうどう}{陣|じん}, {首脳|しゅのう}{陣|じん}) marked as the one learners actually meet. Rest: {運|はこ}び{出|だ}す (against {運|はこ}び{込|こ}む and {持|も}ち{出|だ}す), {反対派|はんたいは} (the 〜{派|は} suffix family, and {野党|やとう} as a party rather than a stance), べとべと (three-way against ねばねば and ぬるぬる), and the three food entries {鳥皮|とりかわ}, とびこ, {数|かず}の{子|こ}. Conjugation tables added to 2 entries (1 godan, 1 ichidan); **no new kanji**. 11 candidates added from words the new entries reference; 997 remain. §4 cross-model self-check on all 14: **clean — 0 flagged, 0 applied, 0 rejected**. $0.0062. Three slips were caught locally before the self-check: ten entries written with `cross_references: null` where the schema requires an array, `formality: "casual"` (not in the enum) on べとべと, and an unannotated 塩 in {鳥皮|とりかわ}'s cultural note.

- **Food (3)**: {鳥皮|とりかわ}, とびこ, {数|かず}の{子|こ}
- **Grammar (2)**: 〜にかけて, 〜しかない
- **Money / society (3)**: {付|つ}け{値|ね}, {反対派|はんたいは}, {陣|じん}
- **Verbs (2)**: {運|はこ}び{出|だ}す, {狂|くる}わせる
- **Nature / description (4)**: {萼片|がくへん}, {残骸|ざんがい}, {毛並|けな}み, べとべと

**Escalations**: (1) A scan found **259 entries whose kanji headwords have no furigana**, including 11 of the 26 created on 2026-08-09 — `find_missing_furigana.py` does not cover the `headword` field, so these validate and ship with bare kanji in the field learners read first. Good `systemic-fix` batch plus a validator check. (2) The candidate-pool contamination is now blocking the count: only 14 of the ~20 target could be built, because outside the 18-word "seen in entry" lane the 968 remaining candidates are inflected forms ({与|あた}えられる, {知|し}らない), free phrases ({静|しず}かに{歩|ある}く, {推薦状|すいせんじょう}を{書|か}く), and non-words ({権使|けんし}, {些道|さどう}, {個尊|こそん}). This is the fourth consecutive run to report it; a `clean_up_candidates_list.md` pass should run before the selector next picks `new-entries`.

### 2026-08-09 (Routine v2: new-entries — 14 New Entries, IDs 30512–30525)
Created 14 general-tier entries, **all from the "seen in entry" lane, which this run empties** (16 available). The two it did not build are the ones the 2026-08-08 run deferred: C22806 {夏目漱石|なつめそうせき} stays in the list as a genuine scope question (the dictionary has no proper-noun precedent — no {東京|とうきょう}, {日本|にほん}, or {富士山|ふじさん} entry), while C22851 {画期|かっき} was **removed as stale** — it is a bound morpheme whose only host, {画期的|かっきてき}, is already 06826, so nothing about it needs a curator ruling. The 14 close inline gaps across seven source ranges, and **eight of them come from the previous run's own batch**: {添|そ}い{遂|と}げる, {追熟|ついじゅく}, {机上|きじょう}の{空論|くうろん}, {蕗|ふき}, {悲観論|ひかんろん}, {楽観論|らっかんろん}, {追|お}い{込|こ}み, and {萼|がく}. **{悲観論|ひかんろん} and {楽観論|らっかんろん}** are entered as a reciprocal `antonym` pair and defined against their 〜{的|てき} adjectives (06090/06091): the 〜{論|ろん} ending makes each a *position that can be argued*, not a temperament, so both take {唱|とな}える and {広|ひろ}がる. {机上|きじょう}の{空論|くうろん} carries a USAGE warning that it is a blunt criticism — aimed at a superior it reads as rude, and {現実的|げんじつてき}ではない is the polite substitute. {添|そ}い{遂|と}げる is marked as covering the whole span of a marriage rather than a moment, which is why it barely occurs in the plain present outside vows, and is split from {連|つ}れ{添|そ}う (ongoing state, no "until death"). {言|い}い{値|ね} is defined against its counterpart {付|つ}け{値|ね} and against {定価|ていか}, with an explicit caution not to read it as the social-media いいね. **{蕗|ふき} and {萼|がく}** both note that their kanji are rare enough that kana is the normal orthography, and {萼|がく} is separated from the kitchen word ヘタ for the same object. ボックス is the one two-sense entry (6 examples): the container sense, contrasted with {箱|はこ} as sounding like a product or fixture, and the booth sense, which barely stands alone outside ボックス{席|せき} / カラオケボックス. Rest: {追熟|ついじゅく} (produce term, {常温|じょうおん}で{追熟|ついじゅく}させる), {追|お}い{込|こ}み (noun of {追|お}い{込|こ}む, but "drive the task to the finish", not "corner someone"), マイコン (the 1980s home-computer sense marked dated), {早炊|はやだ}き, ワード (confined to search/media/IT — {単語|たんご} and {言葉|ことば} for words as language), and {瓦礫|がれき}. Conjugation tables added to 2 entries (1 ichidan, 1 suru). **Three new kanji**: {礫|れき} `02791_reki_tsubute_pebble`, {萼|がく} `02792_gaku_utena_calyx`, {蕗|ろ} `02793_ro_fuki_butterbur`. 4 candidates added from words the new entries reference ({蕗|ふき}の{薹|とう}, {萼片|がくへん}, {付|つ}け{値|ね}, {残骸|ざんがい}); 990 remain. §4 cross-model self-check on all 14: **1 flagged, 1 applied, 0 rejected** — マイコン's top-level gloss read "microcontroller; built-in computer control", where the second element names a function rather than a synonym; corrected to "microcontroller; microcomputer" to match the sense gloss. $0.0061.

- **Nature / food (3)**: {蕗|ふき}, {萼|がく}, {追熟|ついじゅく}
- **Opinion nouns (3)**: {悲観論|ひかんろん}, {楽観論|らっかんろん}, {机上|きじょう}の{空論|くうろん}
- **Loanwords (3)**: マイコン, ボックス, ワード
- **Work / money (3)**: {追|お}い{込|こ}み, {言|い}い{値|ね}, {早炊|はやだ}き
- **Verbs / society (2)**: {添|そ}い{遂|と}げる, {瓦礫|がれき}

**Escalation**: the `seen in entry` lane is now empty and the ~970 remaining corpus-harvested candidates are the polluted 2026-03/04/05 batches (non-words like {権使|けんし}, {些道|さどう}, {個尊|こそん}; transparent compounds like {片面印刷|かためんいんさつ}, {若|わか}い{女性|じょせい}). This is the third consecutive run to report it. A `clean_up_candidates_list.md` pass should run before the selector next picks `new-entries`.

### 2026-08-08 (Routine v2: new-entries — 18 New Entries, IDs 30494–30511)
Created 18 general-tier entries, **all from the "seen in entry" lane, which this run drains** (23 available). Three of the 23 turned out to be duplicates of existing entries and were removed as stale — ぬか{漬|づ}け (orthographic variant of 17712 {糠漬|ぬかづ}け), {勢|ぜい} (already 30490 〜{勢|ぜい}), and {食|く}らう (variant of 10022 {喰|く}らう) — each surfaced by `check_duplicate.py` only as a parenthetical homophone note. Two were left unbuilt for a curator ruling: C22806 {夏目漱石|なつめそうせき} (a personal name; the dictionary carries place names but no people) and C22851 {画期|かっき} (a bound morpheme whose only host, {画期的|かっきてき}, is already 06826). The 18 close inline gaps across six source ranges. **Yesterday's own batch supplied five**: {連|つ}れ{添|そ}う, the modern verb 30484 {連|つ}れ{合|あ}う names as its everyday replacement, entered as intransitive-with-と and marked literary because it appears almost only in retrospect ({長年|ながねん}{連|つ}れ{添|そ}った{妻|つま}); ぜんまい and ふきのとう, the two {山菜|さんさい} 30491 {蕨|わらび} referenced, cross-linked to each other and split on **how the bitterness is handled** (ぜんまい is boiled and simmered, ふきのとう is fried or made into miso precisely to keep it); ラストスパート, flagged as a **Japanese-made compound** since スパート does not stand alone; and {牡丹鍋|ぼたんなべ}, carrying the {牡丹|ぼたん}/もみじ/さくら game-meat euphemism table that 30481 {牡丹肉|ぼたんにく} introduced. **{半数|はんすう} and {二分|にぶん}** both come from 02938 {半分|はんぶん} and are defined against it and each other: {半数|はんすう} counts members of a set (so people and votes, never water or money) and carries the {過半数|かはんすう} voting threshold; {二分|にぶん} is two-sense (splitting in two / the fraction {二分|にぶん}の{一|いち}) with 6 examples and a **reading caution** — the same characters read にふん mean "two minutes". 〜てみる completes the て-form auxiliary set with 30376 ている, 30377 〜てある, 30378 〜ておく and 03102 〜てしまう, documenting both its softening use ({考|かんが}えてみます over {考|かんが}えます) and the trap that it does **not** mean "attempt but fail" — that is 〜ようとする. {熟|う}れる is entered with an explicit ASPECT section, because {熟|う}れている is the resulting state ("is ripe"), not an action in progress. Rest: {理想論|りそうろん} (with the built-in criticism spelled out — never used of one's own proposal), へた (a kitchen word, contrasted with the botanical {萼|がく}), {駅名|えきめい}, {科学史|かがくし}, {確定的|かくていてき} (the journalist's word for *before* the result is official, against {確定|かくてい}した after), {逆転勝利|ぎゃくてんしょうり}, ドラマチック (with a COMMON MISTAKE note: unlike English "dramatic" it is not used of large moves in figures — that is {劇的|げきてき}に or {大幅|おおはば}に), {総支給額|そうしきゅうがく} (with the full pay-slip vocabulary set against 06833 {手取|てど}り), and {成田|なりた} (noting that in travel talk the bare name means the airport). Conjugation tables added to 3 entries (1 godan, 1 ichidan, 1 suru); **no new kanji**. 8 candidates added from words the new entries reference ({添|そ}い{遂|と}げる, {追熟|ついじゅく}, {机上|きじょう}の{空論|くうろん}, {蕗|ふき}, {悲観論|ひかんろん}, {楽観論|らっかんろん}, {追|お}い{込|こ}み, {萼|がく}); 981 remain. §4 cross-model self-check on all 18: **clean — 0 flagged, 0 applied, 0 rejected**. $0.0079. One slip caught before the build without the reviewer's help: {二分|にぶん}'s notes had `{〜を二分|にぶん}する`, non-kanji inside a furigana wrapper, rewritten as `〜を{二分|にぶん}する`.

- **Food / plants (4)**: ぜんまい, ふきのとう, {牡丹鍋|ぼたんなべ}, へた
- **Numbers / quantity (2)**: {半数|はんすう}, {二分|にぶん}
- **Verbs / grammar (3)**: {連|つ}れ{添|そ}う, {熟|う}れる, 〜てみる
- **Work / money (2)**: {総支給額|そうしきゅうがく}, {確定的|かくていてき}
- **Sports / media (2)**: {逆転勝利|ぎゃくてんしょうり}, ドラマチック
- **Places / reference (5)**: {成田|なりた}, {駅名|えきめい}, {科学史|かがくし}, {理想論|りそうろん}, ラストスパート
