# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-25
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
| Total entries | ~19,058 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,259 (open) |
| Candidate words | ~5,099 |
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

### 2026-03-26 (Vocabulary Expansion - 24 New Entries)
Added 24 new dictionary entries (IDs 19462-19485) from candidate_words.json. A diverse mix of nouns, adjectives, and verbs covering food, culture, language, and society.

- **Nouns (15)**: {会食|かいしょく} (dining together), {逸品|いっぴん} (masterpiece), {遠方|えんぽう} (distant place), {含意|がんい} (implication), {鏡餅|かがみもち} (New Year rice cake), {資材|しざい} (materials), {余波|よは} (aftereffects), {便所|べんじょ} (toilet), {存命|そんめい} (alive), {天罰|てんばつ} (divine punishment), {穀類|こくるい} (grains), {名品|めいひん} (fine article), {小刀|こがたな} (small knife), {労務|ろうむ} (labor affairs), {亡命者|ぼうめいしゃ} (exile)
- **Nouns/Suru verbs (4)**: {投降|とうこう} (surrender), {模写|もしゃ} (copying), {空想|くうそう} (fantasy), {冒涜|ぼうとく} (blasphemy)
- **Adjective-na/Nouns (3)**: {激辛|げきから} (extremely spicy), {貧乏|びんぼう} (poor), {不敬|ふけい} (disrespectful)
- **Verb (1)**: {編|あ}み{込|こ}む (to braid in)
- **Food/culture (1)**: {柏餅|かしわもち} (oak-leaf rice cake)
- 2 new kanji added: 柏, 涜
- 1 stale candidate removed (会釈する, already exists)

### 2026-03-25 (Noentry Link Polish - 26 New Entries + All Remaining Links Resolved)
Created 26 new dictionary entries (IDs 19436-19461) for words marked `noentry` in inline links, and resolved all remaining ~305 noentry links across ~190 files.

- **New noun entries (21)**: {光栄|こうえい}, {迷|まよ}い, {重荷|おもに}, {闘志|とうし}, {路上|ろじょう}, {間柄|あいだがら}, {銅|どう}, {鉄分|てつぶん}, {高所|こうしょ}, {上体|じょうたい}, {人違|ひとちが}い, {例文|れいぶん}, {凍土|とうど}, {不良品|ふりょうひん}, {下半身|かはんしん}, {入場券|にゅうじょうけん}, {両腕|りょううで}, {貝殻|かいがら}, {沖合|おきあい}, {均等|きんとう}, {是非|ぜひ}, {土地勘|とちかん}
- **New noun/suru entry (1)**: {転換|てんかん}
- **New verb entries (2)**: {静|しず}める, {買|か}い{替|か}える
- **New adverb entry (1)**: {青々|あおあお}
- **Link-only updates (26 links)**: Updated noentry links to newly created entries
- **Link removals (~280 links)**: Stripped noentry wrappers for number+counter combinations (百年, 十時, etc.), proper nouns (兵庫, 奈良, etc.), place names, specialized compounds, single-kanji words, and grammatical patterns
- **All noentry links now resolved**: 0 remaining (down from ~305)

### 2026-03-25 (Noentry Link Polish - 44 New Entries + 132 Link Fixes)
Created 44 new dictionary entries (IDs 19392-19435) for words marked `noentry` in inline links, and updated 132 existing-entry link-only fixes plus 56 links for newly created entries.

- **Link-only fixes (95 words)**: Updated noentry links to existing entries including うち, つく, でも, 月, 方, 後, 空, やる, よろしく, アルバム, ジャケット, プロジェクト, 億, 千, 政策, 節分, 給食, 音色, 鳴き声, and 75 more
- **New noun entries (36)**: {本番|ほんばん}, {子犬|こいぬ}, {歯科医|しかい}, {解決策|かいけつさく}, {料理人|りょうりにん}, {窓側|まどがわ}, {白旗|しらはた}, チャンピオン, マニキュア, セメント, {肉料理|にくりょうり}, {小枝|こえだ}, {白馬|はくば}, {名古屋|なごや}, レンガ, {堤防|ていぼう}, {救急箱|きゅうきゅうばこ}, {新型|しんがた}, {火山灰|かざんばい}, ピアニスト, カップル, パン{屋|や}, デモ, {韓国|かんこく}, フランス, カンニング, コルク, イタリア, {生活費|せいかつひ}, {日本料理|にほんりょうり}, {航空券|こうくうけん}, {水|みず}たまり, {裏道|うらみち}, {病歴|びょうれき}, {批評家|ひひょうか}, {街頭|がいとう}, {褒|ほ}め{言葉|ことば}, {山火事|やまかじ}, {子守歌|こもりうた}, {粘土|ねんど}
- **New adverb entries (3)**: くっきり, すくすく, なだらか (na-adj)
- **New verb/suffix entries (1)**: まくる (to roll up / ~まくる suffix)
- **New multi-sense entries**: マニキュア (2), デモ (2), {裏道|うらみち} (2), まくる (2)
- 2 new kanji added: 堤, 韓
- Total noentry links resolved: ~188 links across ~165 files; ~290 unique noentry words remaining

### 2026-03-25 (Noentry Link Polish - 25 New Entries + 18 Link Fixes)
Created 25 new dictionary entries (IDs 19367-19391) for words marked `noentry` in inline links, and updated 18 existing-entry links.

- **Link-only fixes (18 words)**: Updated noentry links to existing entries for かかる, 白, 風呂, 咲く, 宝くじ, 赤ちゃん, パソコン, トマト, おにぎり, 家族, 見つかる, 国旗, 犠牲者, 物腰, 王, 罰金, バラ, ひまわり
- **New verb entries (6)**: {受|う}かる (to pass exam), {治|なお}す (to cure), {離|はな}す (to separate), {交|か}わす (to exchange), {冒|おか}す (to brave/risk), {剥|む}ける (to peel off)
- **New adjective entries (2)**: {思|おも}いがけない (unexpected), {真|ま}ん{丸|まる} (perfectly round)
- **New noun entries (17)**: {説明書|せつめいしょ}, {江戸|えど}, {餌食|えじき}, {経済学|けいざいがく}, {第一|だいいち}, {科学者|かがくしゃ}, {人前|ひとまえ}, {営業部|えいぎょうぶ}, {今日中|きょうじゅう}, {飛行士|ひこうし}, {安全性|あんぜんせい}, {委員長|いいんちょう}, {危害|きがい}, {日|ひ}の{丸|まる}, {木刀|ぼくとう}, {雀蜂|すずめばち}, {松竹梅|しょうちくばい}
- Total noentry links resolved: ~60 links across ~55 entry files

### 2026-03-25 (Vocabulary Expansion - 30 New Entries, Session 500)
Added 30 new dictionary entries (IDs 19337-19366) from candidate_words.json. A diverse mix of single-kanji words, common nouns, verbs, and expressions.

- **Single-kanji nouns (18)**: {鮭|さけ} (salmon), {串|くし} (skewer), {芝|しば} (turf), {刃|やいば} (blade), {芸|げい} (art/trick), {吉|きち} (good fortune), {凶|きょう} (bad luck), {乳|ちち} (milk/breast), {腸|ちょう} (intestine), {雫|しずく} (droplet), {虜|とりこ} (captive/devotee), {某|ぼう} (a certain), {黄|き} (yellow), {王|おう} (king), {的|まと} (target), {要|かなめ} (linchpin), {魔|ま} (demon), {栓|せん} (stopper)
- **Multi-sense nouns (3)**: {錠|じょう} (lock/tablet, 2 senses), {節|せつ} (section/season/moderation, 3 senses), {表|ひょう} (table/chart)
- **Verbs (2)**: {難航|なんこう}する (to run into difficulties), {始動|しどう}する (to start up)
- **Other (7)**: {旧|きゅう} (old/former, prefix), {暦|こよみ} (calendar), {際|きわ} (edge/verge), {空模様|そらもよう} (weather conditions), {目|め}を{閉|と}じる (to close one's eyes), {抵抗感|ていこうかん} (reluctance), {主|あるじ} (master/host)
- **Multi-sense entries**: {刃|やいば} (2: blade/sword), {芸|げい} (2: art/trick), {乳|ちち} (2: milk/breast), {虜|とりこ} (2: captive/devotee), {王|おう} (2: king/champion), {際|きわ} (2: edge/critical moment), {魔|ま} (2: demon/magic), {錠|じょう} (2: lock/tablet), {節|せつ} (3: section/season/moderation)

4 new kanji added to kanji index: 某, 虜, 雫, 鮭
Topics covered: food, culture, nature, body, tool, emotion, language, society, time, religion
Total entries: ~19,141 → ~19,171 (approximate)
Remaining candidates: ~5,015 → ~4,985 (30 entries created)


Topics covered: emotion, daily life, culture, time, food-drink, nature, education, language
Total entries: ~19,122 → ~19,141 (approximate)
Remaining candidates: ~5,035 → ~5,015 (19 entries created + 1 duplicate removed)




---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
