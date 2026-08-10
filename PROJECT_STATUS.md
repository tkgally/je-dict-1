# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-08-10
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

### 2026-08-07 (Routine v2: new-entries — 20 New Entries, IDs 30474–30493)
Created 20 general-tier entries, **all 20 from the "seen in entry" lane** (22 available), which now leaves that lane holding only two proper-noun candidates. The batch **finishes the thousands series** that yesterday's run left half-done: {四千|よんせん}, {六千|ろくせん}, {七千|ななせん}, and {九千|きゅうせん} join the existing {一千|いっせん}/{三千|さんぜん}/{五千|ごせん}/{八千|はっせん}, each carrying the same three-item sound-change table (only {一千|いっせん}, {三千|さんぜん}, {八千|はっせん} change) plus its own reading warning — よん-not-し (avoiding the {死|し} homophone), なな-not-しち, きゅう-not-く, and the {六百|ろっぴゃく}-changes-but-{六千|ろくせん}-doesn't contrast. {三時間|さんじかん} completes the hours set with 00941 {一時間|いちじかん} and 27637 {二時間|にじかん}, repeating their duration-vs-time-point split ({三時間|さんじかん} / {三時|さんじ}). The other 15 close inline-link `noentry` gaps across the dictionary: {亡|な}くす — entered as the **death sense of なくす**, transitive, `contrast`-linked to 01110 {無|な}くす with a KANJI CHOICE section and its {亡|な}くなる intransitive partner; {連|つ}れ{合|あ}う, the dated verb behind 06810 {連|つ}れ{合|あ}い; とともに, two-sense (accompaniment / parallel change), marked as the formal counterpart of と{一緒|いっしょ}に; {膨|ふく}らませる, two-sense (inflate / build up hopes), linked to both 05342 {膨|ふく}らむ and 09646 {膨|ふく}らます with the shorter-form distinction spelled out; {意|い}, two-sense and flagged as a **bound formal noun** learners meet only inside {遺憾|いかん}の{意|い}-type phrases; the suffix 〜{勢|ぜい} (with the established {上位|じょうい}{勢|ぜい}/{若手|わかて}{勢|ぜい} uses separated from freshly coined ガチ{勢|ぜい}/エンジョイ{勢|ぜい}); {冷|ひ}やかし, two-sense (browsing without buying / teasing), with the {冷|ひ}やかしお{断|ことわ}り shop sign; {閉校|へいこう} (distinguished three ways from {廃校|はいこう} and {休校|きゅうこう}); {副店長|ふくてんちょう} (with the {副|ふく}〜 title family); {胃癌|いがん}; ラスト (with a COMMON MISTAKE section — 'last week' is {先週|せんしゅう}, not ラスト{週|しゅう}); {牡丹肉|ぼたんにく} (with the もみじ/さくら game-meat euphemism set); {蕨|わらび} and {米|こめ}ぬか, both from 06818 {灰汁|あく}{抜|ぬ}き and cross-linked back to it; and {百十番|ひゃくとおばん}, created under the kanji headword because 01393 {警察|けいさつ}'s inline link expects that form, with a note that 110{番|ばん} is the standard orthography. Conjugation tables added to 5 entries (2 godan, 1 ichidan, 2 suru). **One new kanji**: {蕨|けつ} assigned `02790_ketsu_warabi_bracken`. 6 candidates added from words the new entries reference ({連|つ}れ{添|そ}う, ぜんまい, ふきのとう, ぬか{漬|づ}け, ラストスパート, {牡丹|ぼたん}{鍋|なべ}); 980 remain. §4 cross-model self-check on all 20: **3 flagged, 1 applied, 2 rejected** — applied ラスト's `informal`→`neutral` register fix; rejected the {意|い} and {連|つ}れ{合|あ}う formality flags (the first contradicted by the entry's own REGISTER note, the second suggesting `literary`, which is not in the schema's formality enum). $0.0088.

- **Numbers / time (5)**: {四千|よんせん}, {六千|ろくせん}, {七千|ななせん}, {九千|きゅうせん}, {三時間|さんじかん}
- **Verbs (3)**: {亡|な}くす, {連|つ}れ{合|あ}う, {膨|ふく}らませる
- **Grammar / bound forms (3)**: とともに, {意|い}, 〜{勢|ぜい}
- **Work / education / society (4)**: {閉校|へいこう}, {副店長|ふくてんちょう}, {冷|ひ}やかし, {百十番|ひゃくとおばん}
- **Food / health (5)**: {牡丹肉|ぼたんにく}, {蕨|わらび}, {米|こめ}ぬか, {胃癌|いがん}, ラスト

### 2026-08-07 (Routine v2: new-entries — 20 New Entries, IDs 30454–30473)
Created 20 general-tier entries, all from the **"seen in entry" lane** (26 available). The batch **drains the number backlog the last three runs kept deferring**: {三万|さんまん}, {五万|ごまん}, {十万|じゅうまん}, {五千|ごせん}, {八千|はっせん}, {一千|いっせん}, and {三十人|さんじゅうにん}, referenced from 00794 {三十|さんじゅう}, 00795 {万|まん}, and 00809 {千|せん}. The set is built around **where the readings are actually irregular**: {八千|はっせん} and {一千|いっせん} each carry the three-item thousands table ({一千|いっせん}/{三千|さんぜん}/{八千|はっせん} change; the rest are regular), {十万|じゅうまん} is framed as the digit-grouping trap (Japanese counts in fours, English in threes, so 100,000 is "ten {万|まん}"), and {一千|いっせん} documents the one genuinely non-obvious fact — that its {一|いち} is *optional* where {一万|いちまん}'s is obligatory, so plain {千円|せんえん} but {一千万|いっせんまん}{円|えん}. {五万|ごまん} adds the ごまんとある idiom. **{三十人|さんじゅうにん} reverses yesterday's skip** ("purely compositional"): 10978 {三人|さんにん}, 28475 {十人|じゅうにん}, and 10985 {百人|ひゃくにん} are all existing entries, so leaving it out was the inconsistency. The other 13 are ordinary vocabulary: {桜肉|さくらにく} (euphemism for 30430 {馬肉|ばにく}, its source entry, with the {牡丹|ぼたん}{肉|にく}/{紅葉|もみじ} parallel), {拘置所|こうちしょ} (completing the {留置場|りゅうちじょう}/{拘置所|こうちしょ}/{刑務所|けいむしょ} three-way that 30444 already described from the other side), the {本校|ほんこう}/{分校|ぶんこう} pair (each defined against the other; {本校|ほんこう} is two-sense — institutional self-reference vs. main campus — with 6 examples), {儲|もう}け{話|ばなし} (with a USAGE section on why the word reads as fraud), {傍線|ぼうせん} (the vertical-writing counterpart to 00190 {下線|かせん}), {自撮|じど}り{棒|ぼう}, {店長|てんちょう} (with the bare-title address pattern), レジスター (marked as the written full form of everyday レジ), ウィンドウショッピング, オンラインショッピング ({通販|つうはん} flagged as what speakers actually say), {肖像権|しょうぞうけん}, and プライバシーポリシー. Conjugation tables added to the two suru-nouns; **no new kanji**. 4 candidates added ({閉校|へいこう}, {冷|ひ}やかし, {牡丹肉|ぼたんにく}, {副店長|ふくてんちょう}); 981 remain. §4 cross-model self-check on all 20: **1 entry flagged, 2 applied, 0 rejected** — {傍線|ぼうせん}'s gloss now qualifies "underline" as the horizontal-writing case, since bare "underline" would send a learner to {傍線|ぼうせん} where {下線|かせん} is wanted. $0.0087.

**CI note**: GitHub Actions has dispatched no workflow run repo-wide since 2026-08-06 15:50 UTC, which stranded PRs #3130 and #3131. Neither was rescuable (no green to rescue) and neither is superseded, so this run **absorbed #3131's branch** (which already carried #3130) rather than opening a third parallel strand.

- **Numbers / counters (7)**: {三万|さんまん}, {五万|ごまん}, {十万|じゅうまん}, {五千|ごせん}, {八千|はっせん}, {一千|いっせん}, {三十人|さんじゅうにん}
- **Education (3)**: {本校|ほんこう}, {分校|ぶんこう}, {傍線|ぼうせん}
- **Law (3)**: {拘置所|こうちしょ}, {肖像権|しょうぞうけん}, プライバシーポリシー
- **Shopping / business (4)**: {店長|てんちょう}, レジスター, ウィンドウショッピング, オンラインショッピング
- **Food / objects (3)**: {桜肉|さくらにく}, {自撮|じど}り{棒|ぼう}, {儲|もう}け{話|ばなし}
