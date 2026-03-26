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

### 2026-03-26 (Vocabulary Expansion - 30 New Entries, Session 503)
Added 30 new dictionary entries (IDs 19516-19545) from candidate_words.json. Focused on practical, high-utility words for intermediate learners — emotions, social behavior, common expressions, and everyday verbs.

- **Expressions (7)**: {機嫌|きげん}が{悪|わる}い (in a bad mood), {納得|なっとく}がいかない (can't accept), {気|き}が{気|き}でない (anxious), {気|き}が{楽|らく} (at ease), {愛想|あいそ}を{尽|つ}かす (fed up with), {後|うし}ろ{髪|がみ}を{引|ひ}かれる (reluctant to leave), {丁重|ていちょう}に{断|ことわ}る (politely decline)
- **Verbs (7)**: {面白|おもしろ}がる (find amusing), {遠慮|えんりょ}する (refrain), {謝罪|しゃざい}する (apologize formally), {拒絶|きょぜつ}する (reject), {変色|へんしょく}する (discolor), {波及|はきゅう}する (spread/ripple out), {絞|しぼ}り{出|だ}す (squeeze out)
- **Nouns (5)**: {侵入者|しんにゅうしゃ} (intruder), {積極性|せっきょくせい} (proactiveness), {利害関係|りがいかんけい} (interests/stakes), {感想文|かんそうぶん} (book report), {習慣化|しゅうかんか} (habituation)
- **Adjectives (2)**: {心細|こころぼそ}い (anxious/helpless), {心|こころ}もとない (uncertain/uneasy)
- **Na-adjectives/Nouns (3)**: {高慢|こうまん} (arrogant), {独|ひと}りぼっち (all alone), ハイテンション (excited/hyper)
- **Other (4)**: でございます (polite copula), お{天気屋|てんきや} (moody person), {入会|にゅうかい}する (join/enroll), {侵|おか}す (invade/violate)
- **Verbs with cross-refs**: {積|つ}み{重|かさ}なる (pile up, with transitive pair), {移|うつ}り{変|か}わる (change gradually), {侵|おか}す (with homophone cross-refs to {犯|おか}す and {冒|おか}す)

### 2026-03-26 (Vocabulary Expansion - 30 New Entries, Session 502)
Added 30 new dictionary entries (IDs 19486-19515) from candidate_words.json. A diverse mix of expressions, nouns, and adverbs covering daily life, culture, health, nature, and abstract concepts.

- **Expressions (10)**: {折|おり}に{触|ふ}れて (on occasion), {元気|げんき}がない (listless), {落|お}ち{着|つ}かない (restless), {口火|くちび}を{切|き}る (to start things off), {心|こころ}ここにあらず (absentminded), {期限|きげん}が{切|き}れる (to expire), {言葉|ことば}を{交|か}わす (to exchange words), {役割|やくわり}を{果|は}たす (to fulfill a role)
- **Nouns (15)**: {勝手口|かってぐち} (kitchen door), {因果関係|いんがかんけい} (causal relationship), {血糖値|けっとうち} (blood sugar level), {炭酸飲料|たんさんいんりょう} (carbonated beverage), {徳利|とっくり} (sake bottle), {豆類|まめるい} (legumes), {虚空|こくう} (void), {音漏|おとも}れ (sound leakage), {通信簿|つうしんぼ} (report card), {夕映|ゆうば}え (sunset glow), {青菜|あおな} (leafy greens), {後頭部|こうとうぶ} (back of the head), {生|は}え{際|ぎわ} (hairline), ご{祝儀袋|しゅうぎぶくろ} (gift money envelope), {適者生存|てきしゃせいぞん} (survival of the fittest)
- **Noun/Suru verbs (3)**: {沈静化|ちんせいか} (calming down), バトンタッチ (handover), {品種改良|ひんしゅかいりょう} (selective breeding)
- **Adverbs (2)**: {急|いそ}いで (hurriedly), {皆目|かいもく} (not at all)
- **Na-adjective (1)**: {自分勝手|じぶんかって} (selfish)
- **Other (1)**: {一切合切|いっさいがっさい} (absolutely everything)

### 2026-03-26 (Vocabulary Expansion - 23 New Entries)
Added 23 new dictionary entries (IDs 19462-19485) from candidate_words.json. A diverse mix of nouns, adjectives, and verbs covering food, culture, language, and society.

- **Nouns (15)**: {会食|かいしょく} (dining together), {逸品|いっぴん} (masterpiece), {遠方|えんぽう} (distant place), {含意|がんい} (implication), {鏡餅|かがみもち} (New Year rice cake), {資材|しざい} (materials), {余波|よは} (aftereffects), {便所|べんじょ} (toilet), {存命|そんめい} (alive), {天罰|てんばつ} (divine punishment), {穀類|こくるい} (grains), {名品|めいひん} (fine article), {小刀|こがたな} (small knife), {労務|ろうむ} (labor affairs), {亡命者|ぼうめいしゃ} (exile)
- **Nouns/Suru verbs (3)**: {投降|とうこう} (surrender), {模写|もしゃ} (copying), {冒涜|ぼうとく} (blasphemy)
- **Adjective-na/Nouns (3)**: {激辛|げきから} (extremely spicy), {貧乏|びんぼう} (poor), {不敬|ふけい} (disrespectful)
- **Verb (1)**: {編|あ}み{込|こ}む (to braid in)
- **Food/culture (1)**: {柏餅|かしわもち} (oak-leaf rice cake)
- 2 new kanji added: 柏, 涜
- 1 stale candidate removed (会釈する, already exists)
- 1 duplicate removed (空想, already exists as entry 00256)

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



---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
