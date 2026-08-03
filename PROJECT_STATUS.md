# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-08-03
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

### 2026-08-03 (Routine v2: new-entries — 20 New Entries, IDs 30338–30357)
Created 20 general-tier entries, **draining the "seen in entry" lane down to 3** (25 available; 2 dropped as stale, 20 created). The two stale drops were orthographic/notation variants the candidate capture step cannot see: C22697 {気|き}ぜわしい, the mixed-kana spelling of existing 15598 {気忙|きぜわ}しい, and C22704 ぶり, already covered by 28358 〜ぶり. Three {派|は}-suffix performer types — {正統派|せいとうは}, {演技派|えんぎは}, {個性派|こせいは} — were created together and cross-describe each other and the existing 30319 {本格派|ほんかくは} / 30320 {実力派|じつりょくは}, with {正統派|せいとうは}↔{個性派|こせいは} linked as a `contrast` pair. {総資産|そうしさん} **completes the balance-sheet contrast set** with 30322 {純資産|じゅんしさん} created the day before. The counter/ordinal group is the other cluster: {何回目|なんかいめ}, {二|ふた}つ{目|め}, {二枚|にまい}, {七人|しちにん}, {何曜日|なんようび}, and the two-sense {十一日|じゅういちにち} (date and duration, with the irregular-through-{十日|とおか} reading rule documented). {自身|じしん} is tagged `["noun", "pronoun"]` and its notes spell out both restrictions learners get wrong — it never stands alone as a subject, and inanimate nouns take {自体|じたい} instead. The homophone pair {海草|かいそう} (sea grass, marine seed plants) vs. existing 06750 {海藻|かいそう} (algae) is now explicit in both directions. Rest: あっちこっち (with the "there-and-here" word-order note and the あちこち/{方々|ほうぼう} register ladder), {提唱者|ていしょうしゃ}, めかぶ, {蚊遣|かや}り{豚|ぶた}, {危|あや}うさ, ハイリスク, {打|う}ち{砕|くだ}く, and {別世界|べっせかい}. Conjugation table added to the one godan verb; **no new kanji**. 2 stale candidates removed, 5 added from words the new entries reference; 992 remain. §4 cross-model self-check on all 20 new entries: **2 entries flagged, 1 applied, 2 rejected** — applied the {二|ふた}つ{目|め} example translation ("two stops" → "the second stop", since the entry exists to teach the ordinal 〜{目|め}); rejected both {海草|かいそう} gloss nits, where "marine flowering plant" is precisely the botanical definition that separates it from {海藻|かいそう}. $0.0087.

- **Performer / evaluation types (3)**: {正統派|せいとうは}, {演技派|えんぎは}, {個性派|こせいは}
- **Counters / ordinals / dates (6)**: {何回目|なんかいめ}, {二|ふた}つ{目|め}, {二枚|にまい}, {七人|しちにん}, {何曜日|なんようび}, {十一日|じゅういちにち}
- **Business / risk (2)**: {総資産|そうしさん}, ハイリスク
- **Nature / food (2)**: めかぶ, {海草|かいそう}
- **Abstract / grammar (4)**: {自身|じしん}, あっちこっち, {危|あや}うさ, {別世界|べっせかい}
- **People / objects / verbs (3)**: {提唱者|ていしょうしゃ}, {蚊遣|かや}り{豚|ぶた}, {打|う}ち{砕|くだ}く

### 2026-08-02 (Routine v2: new-entries — 20 New Entries, IDs 30318–30337)
Created 20 general-tier entries, **draining the "seen in entry" lane again** (15 available, 13 created). Two were dropped as stale before creation: C22687 エグい, a katakana orthographic variant of existing 05608 えぐい, and C22691 {白状|はくじょう}, already covered by 21378 {白状|はくじょう}する, whose POS tags are `["noun", "verb-suru"]`. The seen-in thirteen: the three {派|は}-suffix performer types {速球派|そっきゅうは} / {本格派|ほんかくは} / {実力派|じつりょくは}, which now cross-describe each other and 30317 {技巧派|ぎこうは}; the accounting pair {他人資本|たにんしほん} and {純資産|じゅんしさん}, **completing the {自己資本|じこしほん} contrast set** started on 2026-08-01; the mimetic ふにゃふにゃ (distinguished from ぐにゃぐにゃ, ふわふわ, and べちゃべちゃ by loss-of-firmness vs. bending vs. pleasant softness vs. wetness); {飛|と}び{乗|の}る (intransitive, に-marked, paired against {飛|と}び{降|お}りる); {忙|せわ}しい (the same kanji as {忙|いそが}しい read せわしい, linked to existing 06736 {忙|せわ}しない); はしたない, with a REGISTER section on its dated, prescriptive flavor; {何分|なんぷん} (two senses — duration and clock-minute — plus the ふん/ぷん counter alternation, and the {何分|なにぶん} homograph warning); {四時|よじ}, documenting the three irregular hour readings よじ/しちじ/くじ; {最期|さいご}, with the ✗{最後|さいご}を{看取|みと}る kanji-choice mistake called out; and {優良|ゆうりょう}. The other 7 are hand-picked, because the ~990-strong non-seen pool is **still heavily polluted** — filtered scans of the C11000–C20000 blocks returned mostly numeric fragments (三百, 六歳, 四人), transparent compounds (全商品, 追加機能, 調達費), and apparent non-words (個尊, 些道, 怒燥, 老健); the `[pattern]` observation now also notes that `routine_next.py`'s `candidates_low` signal reads raw count and so reports "plentiful" while real supply is ~15/run. The seven: {完了形|かんりょうけい} (grammar term, with the {進行形|しんこうけい}/{受動態|じゅどうたい}/{仮定法|かていほう} series), {避難口|ひなんぐち} (contrasted with the commoner 07045 {非常口|ひじょうぐち}), {国章|こくしょう}, {推進者|すいしんしゃ}, {受取先|うけとりさき} (placed in the 〜{先|さき} series with 12275 {宛先|あてさき} / 23506 {送|おく}り{先|さき} / 11083 {取引先|とりひきさき}), {不許可|ふきょか}, and {内通者|ないつうしゃ}. Conjugation tables added to the godan verb and the 2 i-adjectives; **no new kanji**. 2 stale candidates removed, 5 added from words the new entries reference; 1,004 remain. §4 cross-model self-check on all 20 new entries: **2 flagged, 2 applied, 0 rejected** — both `tags.formality` `formal`→`neutral` on {避難口|ひなんぐち} and {受取先|うけとりさき}, applied because the dictionary's own comparable entries (非常口, 宛先, 送り先) all tag `neutral`. $0.0087.

- **Performer / people types (5)**: {速球派|そっきゅうは}, {本格派|ほんかくは}, {実力派|じつりょくは}, {推進者|すいしんしゃ}, {内通者|ないつうしゃ}
- **Finance / business (3)**: {他人資本|たにんしほん}, {純資産|じゅんしさん}, {受取先|うけとりさき}
- **Time (2)**: {何分|なんぷん}, {四時|よじ}
- **Descriptive (3)**: ふにゃふにゃ, {忙|せわ}しい, はしたない
- **Verbs (1)**: {飛|と}び{乗|の}る
- **Evaluation / life (2)**: {優良|ゆうりょう}, {最期|さいご}
- **Institutional / academic (4)**: {完了形|かんりょうけい}, {避難口|ひなんぐち}, {国章|こくしょう}, {不許可|ふきょか}

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
