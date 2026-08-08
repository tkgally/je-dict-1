# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-08-08
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

### 2026-08-06 (Routine v2: new-entries — 20 New Entries, IDs 30434–30453)
Created 20 general-tier entries, all drawn from the **"seen in entry" lane** (33 available). Six of the ten source entries were yesterday's own batch, so this run largely closes the dictionary back over itself: {増益|ぞうえき} and {減収|げんしゅう} were referenced by 30424 {増収|ぞうしゅう}, {馬刺|ばさ}し by 30430 {馬肉|ばにく}, {傍線部|ぼうせんぶ} by 30432 {下線部|かせんぶ} (now linked as `synonym`), and {楽|たの}しさ by 30422. {増益|ぞうえき}/{減収|げんしゅう} complete the four-way earnings-report set with existing 13511 {減益|げんえき} and 30424 {増収|ぞうしゅう}, each carrying the {増収|ぞうしゅう}{増益|ぞうえき}-style set phrases and an explicit revenue-vs-profit distinction; {減収|げんしゅう} is two-sense (revenue drop / smaller harvest) with 6 examples. {楽|たの}しさ documents the さ-nominalization pattern and is `contrast`-linked to 01651 {楽|たの}しみ — the distinction learners actually get wrong. {堪|こた}える is entered as **the third こたえる kanji**: intransitive ichidan, marked formal/written, with the note that learners meet it mainly inside 06796 {持|も}ち{堪|こた}える (whose inline link had it as `noentry`), plus disambiguation from 08995 {堪|こら}える, 12087 {耐|た}える, and a `homophone` link to 09893 {応|こた}える. The **hundreds series** was completed from 00780 {百|ひゃく}'s references: {四百|よんひゃく}, {六百|ろっぴゃく}, {七百|ななひゃく}, {八百|はっぴゃく}, {九百|きゅうひゃく}, each carrying the same three-item sound-change table (only {三百|さんびゃく}/{六百|ろっぴゃく}/{八百|はっぴゃく} change) and a per-entry reading note — しひゃく as an archaism, なな-over-しち for clarity, {八百|やお} for the "a great many" sense, きゅう-not-く. Rest: ジンギスカン (Genghis Khan link documented as marketing legend), セルフィー (flagged as media-register; everyday Japanese is 16863 {自撮|じど}り), {半円|はんえん}, らせん{階段|かいだん}, {鍵穴|かぎあな}, {留置場|りゅうちじょう} (with the {留置場|りゅうちじょう}/{拘置所|こうちしょ}/{刑務所|けいむしょ} three-way legal distinction), {投資話|とうしばなし} (rendaku plus a REGISTER note on why the word smells of fraud), {当校|とうこう} (the {当|とう}〜 self-reference family), and {三回|さんかい}. Conjugation table added to the one ichidan verb; **no new kanji**. 1 stale candidate removed (C22792 {化|か}, duplicating 28335 〜{化|か}); C22806 {夏目漱石|なつめそうせき} skipped as a person name with no precedent in the dictionary (logged for curator decision) and C22795 {三十人|さんじゅうにん} as purely compositional; the 千/万 compounds remain queued. 7 candidates added from words the new entries reference; 990 remain. §4 cross-model self-check on all 20 new entries: **2 flagged, 0 applied, 2 rejected** — rejected the {減収|げんしゅう} request for an `agriculture` semantic tag (not in `VALID_SEMANTIC`, and no in-list tag covers the yield sense) and the {堪|こた}える `formal`→`neutral` flag, since the entry's own USAGE section documents it as formal/written. $0.0087.

- **Business / finance (3)**: {増益|ぞうえき}, {減収|げんしゅう}, {投資話|とうしばなし}
- **Numbers / counters (6)**: {四百|よんひゃく}, {六百|ろっぴゃく}, {七百|ななひゃく}, {八百|はっぴゃく}, {九百|きゅうひゃく}, {三回|さんかい}
- **Food (2)**: {馬刺|ばさ}し, ジンギスカン
- **Objects / buildings (3)**: {半円|はんえん}, らせん{階段|かいだん}, {鍵穴|かぎあな}
- **Education / law (3)**: {傍線部|ぼうせんぶ}, {当校|とうこう}, {留置場|りゅうちじょう}
- **Abstract / verbs / loanwords (3)**: {楽|たの}しさ, {堪|こた}える, セルフィー

### 2026-08-05 (Routine v2: new-entries — 19 New Entries, IDs 30415–30433)
Created 19 general-tier entries. The **"seen in entry" lane** offered 14 candidates; 10 became entries and 4 were removed as stale — {軟|やわ}らかい (C22762) is a kanji variant already documented inside 01096 {柔|やわ}らかい, while {二羽|にわ} (C22765), {三羽|さんば} (C22766), and {一足|いっそく} (C22768) are number+counter combinations covered by the counter entries 01007 {羽|わ} and 00992 {足|そく}. The ten: ミートソース (noted as usually meaning the whole dish, not just the sauce), {湯垢|ゆあか} (paired against 30399 {水垢|みずあか}, its source entry), {空|あ}き{部屋|べや}, the suffix {月|がつ} (**with the {月|つき}/がつ/か{月|げつ} three-way split spelled out**, plus the し/しち/く irregular readings, cross-referenced to 02230 {月|つき}), the counter {脚|きゃく} for chairs and legged furniture (with the note that {三脚|さんきゃく} is separately a tripod), {行|い}き{届|とど}く (**ASPECT section**: the plain present is rare; the live forms are {行|い}き{届|とど}いている and the negative {行|い}き{届|とど}かない), {悲|かな}しさ and {嬉|うれ}しさ (both distinguished from the -み/{喜|よろこ}び emotion nouns and linked to their base adjectives), {熱性|ねっせい} (medical, bound form, with the ねっせい-not-ねつせい reading warning), and the two-sense {増収|ぞうしゅう} (revenue / harvest yield, with the {増収|ぞうしゅう}{増益|ぞうえき} set phrase).

Because the non-seen candidate pool remains **heavily polluted** (a fresh scan again returned transparent compounds, number+counter fragments, and apparent non-words like {権使|けんし}, {些道|さどう}, {個尊|こそん}, {怒燥|どとう}), the other 9 were drawn from a **different internal-completeness signal**: words the dictionary itself links as `：noentry⟧` inside existing examples and notes. A sweep of those links found most had **quietly become resolvable** — {湯呑|ゆの}み, {箸置|はしお}き, {銀杏|ぎんなん}, {語学力|ごがくりょく}, メロンパン, {売|う}り{上|あ}げ, and {長|なが}ねぎ all have entries now while the links still say `noentry` (logged as a `[pattern]` observation proposing a detector). The genuinely missing nine became entries: {千羽鶴|せんばづる} (with the Sadako/peace-movement context), {羊肉|ようにく} (distinguished from ラム/マトン/ジンギスカン), {手数|てすう} (**built around お{手数|てすう}ですが as a business-email cushion**), {最上階|さいじょうかい}, {大|おお}けが, {馬肉|ばにく}, the suffix {年生|ねんせい} (with the note that Japanese counts school years from one within each school), {下線部|かせんぶ}, and {挙|あ}がる — entered as **the third あがる kanji**, two-sense, with a CHOOSING THE KANJI section and `see_also` links to 00615 {上|あ}がる and 28726 {揚|あ}がる. Conjugation tables added to both godan verbs; **no new kanji**. 6 candidates added from words the new entries reference ({増益|ぞうえき}, {減収|げんしゅう}, {馬刺|ばさ}し, {傍線部|ぼうせんぶ}, {楽|たの}しさ, ジンギスカン). §4 cross-model self-check on all 19 new entries: **3 flagged, 0 applied, 3 rejected** — rejected two {月|がつ} gloss flags claiming がつ also counts months (duration is か{月|げつ}, which the entry documents) and one {下線部|かせんぶ} tag flag wanting `education`→`general`, an in-list narrowness nit the §A policy excludes. $0.0083.

- **Food (3)**: ミートソース, {羊肉|ようにく}, {馬肉|ばにく}
- **Suffixes / counters (3)**: {月|がつ}, {脚|きゃく}, {年生|ねんせい}
- **Emotion nouns (2)**: {悲|かな}しさ, {嬉|うれ}しさ
- **Daily life / buildings (3)**: {湯垢|ゆあか}, {空|あ}き{部屋|べや}, {最上階|さいじょうかい}
- **Verbs (2)**: {行|い}き{届|とど}く, {挙|あ}がる
- **Health / business / education (4)**: {熱性|ねっせい}, {大|おお}けが, {増収|ぞうしゅう}, {下線部|かせんぶ}
- **Culture / social (2)**: {千羽鶴|せんばづる}, {手数|てすう}
