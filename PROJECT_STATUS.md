# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-08-07
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
