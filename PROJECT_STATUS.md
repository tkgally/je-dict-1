# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-08-05
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

### 2026-08-05 (Routine v2: new-entries — 18 New Entries, IDs 30397–30414)
Created 18 general-tier entries, **draining the "seen in entry" lane** (16 available, 15 created). The 16th, C22754 {部|ぶ}, was dropped as stale: existing entry 00440 〜{部|ぶ} already carries "club" as its sense 2, so the candidate — added from a バスケ{部|ぶ}/バレー{部|ぶ} sighting — would have duplicated it; `check_duplicate.py` surfaced it only as a parenthetical homophone note. The seen-in fifteen cluster tightly around three source ranges. **Food and drink (7)**, from the 06769–06770 café/restaurant entries: ナポリタン (documented as {洋食|ようしょく} invented in Yokohama, not Italian), ピッツァ (**a register variant, not a different food** — the SIMILAR WORDS section spells out that everyday speech uses ピザ and ピッツァ belongs to Italian menus and food writing), マルゲリータ, シーフード (contrasted with the native {魚介|ぎょかい}{類|るい} and {海鮮|かいせん}), ティー (flagged as **compound-only** — アイスティー, ミルクティー — since standalone tea is {紅茶|こうちゃ} or お{茶|ちゃ}), ジェラート, and マカロン (with an explicit warning off the マカロニ confusion, mirroring the one 30379 マカロニ already carries). **Winter sports and school PE (3)**, from 06773/06775: ドッジボール (with the Japanese-specific {外野|がいや} rule), スノーボーダー, and リフト — two-sense (chairlift / hoist), 6 examples, with a note that it **does not** mean "elevator". **Everyday nouns (5)**: {使|つか}いにくい (i-adjective, **completing the antonym pair** with 30388 {使|つか}いやすい created yesterday), {腰椎|ようつい} (**pairing with 30395 {頚椎|けいつい}**, its source entry, which already pointed at it in SIMILAR WORDS), {水垢|みずあか}, キャンセル{待|ま}ち, and セルフ (marked as near-exclusively compound-forming: セルフレジ, セルフサービス). The other 3 are hand-picked, because the non-seen candidate pool remains **heavily polluted** — a fresh sample of roughly 200 candidates across the whole list turned up almost nothing entry-worthy, dominated by transparent compounds ({参加者数|さんかしゃすう}, {全商品|ぜんしょうひん}, {三千円|さんぜんえん}), inflected forms filed as words ({潔|いさぎよ}くない, {戦|たたか}わない, {動|うご}かない), and apparent non-words ({権使|けんし}, {些道|さどう}, {個尊|こそん}, {怒燥|どとう}, {多角的一面|たかくてきいちめん}); the `[pattern]` observation asking for a `clean_up_candidates_list.md` pass was logged again, now noting that the 989-candidate headline **materially overstates usable supply**. The three: {視覚|しかく}{障害者|しょうがいしゃ} (with the note that the older {盲人|もうじん} is now avoided in public writing), {殺人|さつじん}{事件|じけん} (documenting the news-style {事件|じけん}-vs-{事故|じこ} split), and {直接|ちょくせつ}{交渉|こうしょう}. Conjugation table added to the one i-adjective; **no new kanji**. 1 stale candidate removed (C22754); 2 added from words the new entries reference (ミートソース, {湯垢|ゆあか}) — three others encountered (ゲレンデ, {点字|てんじ}ブロック, セルフレジ) were rejected by `manage_candidates.py` as already present. §4 cross-model self-check on all 18 new entries: **clean — 18/18, 0 flagged, 0 applied, 0 rejected**. $0.0078.

- **Food / drink (7)**: ナポリタン, マカロン, ピッツァ, マルゲリータ, シーフード, ティー, ジェラート
- **Sports / leisure (3)**: ドッジボール, スノーボーダー, リフト
- **Daily life (3)**: {水垢|みずあか}, キャンセル{待|ま}ち, セルフ
- **Evaluation / body (2)**: {使|つか}いにくい, {腰椎|ようつい}
- **Society / law / business (3)**: {視覚|しかく}{障害者|しょうがいしゃ}, {殺人|さつじん}{事件|じけん}, {直接|ちょくせつ}{交渉|こうしょう}


### 2026-08-04 (Routine v2: new-entries — 20 New Entries, IDs 30377–30396)
Created 20 general-tier entries, **draining the "seen in entry" lane completely** (10 available, all 10 created; `check_duplicate.py` returned `OK` for every one). The batch **finishes the 〜て-auxiliary cluster** that 30376 ている opened yesterday: 〜てある (transitive-only, with the を→が object shift), 〜ておく (two senses — preparation and leaving-as-is — plus the 〜とく/〜どく contractions), and 〜たがる (the third-person desire form, with the "never about yourself" restriction and the 〜たいとおっしゃっています workaround for superiors); all three link back to 30376, which had already pointed at them by reading. {使|つか}いやすい **completes the pair** with 30369 {使|つか}いやすさ, created a day earlier, and carries an antonym link to {使|つか}いにくい. The pasta trio スパゲッティ / ペンネ / マカロニ all cross-reference 06768 パスタ and each other, and each SIMILAR WORDS section distinguishes them by shape; スパゲッティ additionally documents the スパゲッティ-means-ナポリタン vs. パスタ-means-Italian-menu split, and マカロニ warns off the マカロン confusion. {間|ま}に{合|あ}わせる is entered as the **transitive partner of 01142 {間|ま}に{合|あ}う**, with a `pair` cross-reference and a TRANSITIVITY section, and is two-sense (meet a deadline / make do with a stopgap). Rest of the seen-in lane: {油|あぶら}{汚|よご}れ and {一曲|いっきょく} (with the {曲|きょく} counter's いっ/ろっ sound changes). The other 10 are hand-picked, because the ~980-strong non-seen pool remains **heavily polluted** — a fresh scan of the whole list turned up mostly compositional phrases ({裸足|はだし}で{歩|ある}く, {速|すみ}やかに{処理|しょり}する), numeric fragments ({四十五|よんじゅうご}, {三千円|さんぜんえん}), and apparent non-words ({権使|けんし}, {些道|さどう}, {個尊|こそん}, {怒燥|どとう}), with the genuinely good base words usually buried inside a longer compound candidate ({換気扇|かんきせん}{掃除|そうじ}, {五月病|ごがつびょう}{患者|かんじゃ}, {皆無|かいむ}である). The ten: {好奇心旺盛|こうきしんおうせい}, {期待|きたい}の{星|ほし}, {速度違反|そくどいはん} (linked to 26875 {制限速度|せいげんそくど}), {勝|か}ち{点|てん} (distinguished from {得点|とくてん} and {勝|か}ち{星|ぼし}), {一昨晩|いっさくばん}, the two-sense {敵前逃亡|てきぜんとうぼう} (military offense / backing out at the decisive moment), {表外漢字|ひょうがいかんじ}, {過労運転|かろううんてん}, {頚椎|けいつい}, and {産学協同|さんがくきょうどう} (with the note that {産学連携|さんがくれんけい} is now the preferred official term). Conjugation tables added to the ichidan verb and the i-adjective. **One new kanji**: {頚|けい} was assigned `02789_kei_kubi_neck` (kei / kubi / neck), the simplified variant of the existing 02770 {頸|けい}. 1 stale candidate removed (C19146 {脂性肌|しせいはだ}, already 23960); {制限速度|せいげんそくど} was also dropped from the pick list as a duplicate of 26875. 5 candidates added from words the new entries reference ({使|つか}いにくい, {腰椎|ようつい}, {水垢|みずあか}, ナポリタン, マカロン); 979 remain. §4 cross-model self-check on all 20 new entries: **1 flagged, 0 applied, 1 rejected** — rejected the {一昨晩|いっさくばん} `formal`→`neutral` flag, since the entry's own REGISTER section documents it as a written word whose spoken equivalent is おとといの{晩|ばん}. $0.0088.

- **Grammar / auxiliaries (3)**: 〜てある, 〜ておく, 〜たがる
- **Food / pasta (3)**: スパゲッティ, ペンネ, マカロニ
- **Traffic / law (2)**: {速度違反|そくどいはん}, {過労運転|かろううんてん}
- **Time / music / sports (3)**: {一昨晩|いっさくばん}, {一曲|いっきょく}, {勝|か}ち{点|てん}
- **People / evaluation (3)**: {好奇心旺盛|こうきしんおうせい}, {期待|きたい}の{星|ほし}, {使|つか}いやすい
- **Body / language / society (4)**: {頚椎|けいつい}, {表外漢字|ひょうがいかんじ}, {産学協同|さんがくきょうどう}, {敵前逃亡|てきぜんとうぼう}
- **Daily life / verbs (2)**: {油|あぶら}{汚|よご}れ, {間|ま}に{合|あ}わせる


### 2026-08-03 (Routine v2: new-entries — 19 New Entries, IDs 30358–30376)
Created 19 general-tier entries, **draining the "seen in entry" lane completely** (all 19 available were created; `check_duplicate.py` returned `OK` for every one, with only homophone notes). The batch is unusually **grammar-heavy**: three of the dictionary's most-referenced but never-defined function items now have entries — the auxiliary ている (three senses keyed to verb type: progressive with activity verbs, resulting-state with change-of-state verbs, habitual with a time expression, plus the {死|し}んでいる/{知|し}っている "is dead / know, not is dying / am knowing" mistake called out), the auxiliary たい (with the third-person restriction and the 〜たがる / 〜たいそうだ escapes), and {自体|じたい} (the inanimate counterpart to 30345 {自身|じしん}, created two days ago, which its own notes already pointed at). Two suffix entries join the existing 〜{地|ち} / 〜{個|こ} series: 〜{上|じょう} (viewpoint marker — {法律上|ほうりつじょう}, {性質上|せいしつじょう}) and 〜{帯|たい} (band/zone — {温帯|おんたい}, {時間帯|じかんたい}, {価格帯|かかくたい}). ローリスク **completes the antonym pair** with 30355 ハイリスク created the day before, and {別天地|べってんち} is linked as a synonym of 30357 {別世界|べっせかい}. {何時間|なんじかん} is two-sense (the duration question, and the 〜も "for hours on end" use) and contrasts explicitly with 00973 {何時|なんじ}, the clock-time question learners confuse it with. Rest: the {幻想|げんそう} pair {幻想曲|げんそうきょく} / {幻想文学|げんそうぶんがく}, {藻場|もば} (marine-conservation term), {症候群|しょうこうぐん}, {使|つか}いやすさ, グラフィックデザイン, ディベート (distinguished from {討論|とうろん} / {議論|ぎろん} / {口論|こうろん} by rules-and-a-winner), {二番目|にばんめ}, {七個|ななこ}, and the standalone noun {地|ち} (two senses, separated from the existing 09852 〜{地|ち} suffix). Conjugation tables added to the ichidan verb and the suru-verb; **no new kanji**. One fix-up during validation: 30361's romaji had to be `roorisuku`, not `rourisuku` (ろー is a long o). 4 candidates added from words the new entries reference (〜てある, 〜ておく, 〜たがる, {使|つか}いやすい); 984 remain. §4 cross-model self-check on all 19 new entries: **4 flagged, 2 applied, 2 rejected** — applied the {待|ま}ちきれる glosses (reworded around the negative {待|ま}ちきれない, which is how the word is actually met) and dropped {七個|ななこ}'s over-narrow "small objects" wording; rejected the {自体|じたい} `grammatical`→`expression` in-list substitution per §A policy, and the {地|ち} `formal`→`neutral` flag, since the entry's own notes describe the word as literary. $0.0085.

- **Grammar / function (5)**: ている, たい, {自体|じたい}, 〜{上|じょう}, 〜{帯|たい}
- **Arts / media (3)**: {幻想曲|げんそうきょく}, {幻想文学|げんそうぶんがく}, グラフィックデザイン
- **Counters / ordinals / time (3)**: {二番目|にばんめ}, {七個|ななこ}, {何時間|なんじかん}
- **Place / nature (3)**: {別天地|べってんち}, {藻場|もば}, {地|ち}
- **Business / health (3)**: ローリスク, {症候群|しょうこうぐん}, {使|つか}いやすさ
- **Communication / evaluation (2)**: ディベート, {待|ま}ちきれる

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
