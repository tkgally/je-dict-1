# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-07-19
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

### 2026-07-21 (Routine v2: new-entries — 20 New Entries, IDs 29993–30012)
Created 20 general-tier entries, **all 20 from the "seen in entry" priority queue** (candidates C22448–C22467, cited from entries 06559–06566) — internal-completeness gaps the dictionary already referenced. Three clusters: nature/animals — {逃|に}げ{水|みず} (road mirage), ボノボ (bonobo), アシカ (sea lion), オットセイ (fur seal), {鰭|ひれ} (fin), ゴマフアザラシ (spotted seal), {鍬形|くわがた} (helmet crest), オオクワガタ (giant stag beetle), ノコギリクワガタ (sawtooth stag beetle), ミヤマクワガタ (deep-mountain stag beetle); baseball — {中継|なかつ}ぎ (middle reliever, 2 senses), {抑|おさ}え (closer/restraint, 2 senses), クローザー (closer), {奪三振|だつさんしん} (strikeouts), {好打者|こうだしゃ} (good hitter), {打|う}ち{取|と}る (to retire a batter; verb-godan), {四番|よんばん} (cleanup hitter, 2 senses); music — {聴|き}く (to listen attentively; verb-godan), コンダクター (conductor), マエストロ (maestro). Conjugation tables added to the 2 new godan verbs ({打|う}ち{取|と}る, {聴|き}く). One new kanji: {鰭|ひれ} → `02786_ki_hire_fin`. §4 cross-model self-check on all 20 changed entries: **18 clean, 2 flagged — 1 applied, 1 rejected** — applied dropping a stretch `business` tag on {中継|なかつ}ぎ (replaced with `abstract`); rejected an in-list narrowness swap `history`→`military` on {鍬形|くわがた} (`history` is defensible for a samurai-era artifact). $0.0087. Added {打線|だせん} (batting lineup), {登板|とうばん} (taking the mound), {仕留|しと}める (to bring down), {凡打|ぼんだ} (easy out) as referenced-but-missing candidates. The seen-in-entry queue drops to 8 remaining.

- **Nature / animals (10)**: {逃|に}げ{水|みず} (road mirage), ボノボ (bonobo), アシカ (sea lion), オットセイ (fur seal), {鰭|ひれ} (fin), ゴマフアザラシ (spotted seal), {鍬形|くわがた} (helmet crest), オオクワガタ (giant stag beetle), ノコギリクワガタ (sawtooth stag beetle), ミヤマクワガタ (deep-mountain stag beetle)
- **Baseball (7)**: {中継|なかつ}ぎ (middle reliever), {抑|おさ}え (closer; restraint), クローザー (closer), {奪三振|だつさんしん} (strikeouts), {好打者|こうだしゃ} (good hitter), {打|う}ち{取|と}る (to retire a batter; verb), {四番|よんばん} (cleanup hitter)
- **Music (3)**: {聴|き}く (to listen attentively; verb), コンダクター (conductor), マエストロ (maestro)

### 2026-07-20 (Routine v2: new-entries — 21 New Entries, IDs 29972–29992)
Created 21 general-tier entries, **all 21 from the "seen in entry" priority queue** (candidates C22427–C22447, cited from entries 06543–06556, 29954–29962) — internal-completeness gaps the dictionary already referenced. This **cleared the seen-in-entry queue**. Clusters: sports — バタ{足|あし} (flutter kick), ノーヒットノーラン (no-hitter), イエローカード (yellow card), コーナーキック (corner kick), ペナルティキック (penalty kick); tools — {槌|つち} (mallet), {木槌|きづち} (wooden mallet), グラインダー (grinder); vehicle — {方向指示器|ほうこうしじき} (turn signal, formal), ギア (gear), エンスト (engine stall), オートマ (automatic car), {発進|はっしん} (moving off), {放|はな}す (to let go; verb-godan); school/lottery — {席替|せきが}え (changing seats), {二等|にとう} (second prize/class), {参加賞|さんかしょう} (participation prize), スクラッチ (scratch card); plant/traditional — {数珠玉|じゅずだま} (Job's tears), {俵|たわら} (straw bale); plus {新装開店|しんそうかいてん} (grand reopening). Conjugation tables added to the 4 new suru-verbs ({新装開店|しんそうかいてん}, エンスト, {発進|はっしん}, {席替|せきが}え) and 1 godan verb ({放|はな}す); no new kanji. §4 cross-model self-check on all 21 changed entries: **20 clean, 1 flagged — 0 applied, 1 rejected** — on ペナルティキック, where the model's suggested translation was identical to the existing one (misread its own concern; ペナルティキック{戦|せん} = "penalty shootout" is correct). $0.0091. The seen-in-entry queue is empty again and awaits curator/polish restock.

- **Sports (5)**: バタ{足|あし} (flutter kick), ノーヒットノーラン (no-hitter), イエローカード (yellow card), コーナーキック (corner kick), ペナルティキック (penalty kick)
- **Tools (3)**: {槌|つち} (mallet), {木槌|きづち} (wooden mallet), グラインダー (grinder)
- **Vehicle (6)**: {方向指示器|ほうこうしじき} (turn signal), ギア (gear), エンスト (engine stall), オートマ (automatic car), {発進|はっしん} (moving off), {放|はな}す (to let go; verb)
- **School / lottery (4)**: {席替|せきが}え (changing seats), {二等|にとう} (second prize), {参加賞|さんかしょう} (participation prize), スクラッチ (scratch card)
- **Plant / traditional / business (3)**: {数珠玉|じゅずだま} (Job's tears), {俵|たわら} (straw bale), {新装開店|しんそうかいてん} (grand reopening)

### 2026-07-19 (Routine v2: new-entries — 20 New Entries, IDs 29952–29971)
Created 20 general-tier entries, **all 20 from the "seen in entry" priority queue** (candidates C22407–C22426, cited from entries 06537–06545) — internal-completeness gaps the dictionary already referenced. A largely sports cluster: baseball — サヨナラ{勝|が}ち (walk-off win), {打数|だすう} (at-bats), {継投|けいとう} (relay pitching), {完全試合|かんぜんじあい} (perfect game); soccer — フリーキック (free kick), レッドカード (red card), ペナルティ (penalty); swimming — ドルフィンキック (dolphin kick), ストローク (stroke), {入水|にゅうすい} (entry into the water); plus {素振|すぶ}り (practice swing), {禁|きん}じ{手|て} (prohibited move), サドンデス (sudden death), もつれ{込|こ}む (to drag on into — verb-godan). Also a business set — {商売繁盛|しょうばいはんじょう} (prosperous business), {千客万来|せんきゃくばんらい} (roaring trade), やきもきする (to fret — verb-suru); anatomy pair — {左|ひだり}{目|め} (left eye), {右|みぎ}{目|め} (right eye); and traditional toy だるま{落|お}とし (daruma otoshi). Conjugation tables added to the 1 new suru-verb (やきもきする) and 1 new godan-verb (もつれ{込|こ}む); no new kanji. This **cleared all but 2 of the seen-in-entry queue** (バタ足, ノーヒットノーラン left). §4 cross-model self-check on all 20 changed entries: **19 clean, 1 flagged — 0 applied, 2 rejected** — both on {入水|にゅうすい}, where the model conflated the じゅすい (suicide-by-drowning) reading with this entry's にゅうすい (entering water) reading; the entry already disambiguates the homograph in its notes. $0.0087. Added イエローカード, コーナーキック, ペナルティキック, 新装開店 as referenced-but-missing candidates.

- **Baseball (5)**: サヨナラ{勝|が}ち (walk-off win), {打数|だすう} (at-bats), {継投|けいとう} (relay pitching), {完全試合|かんぜんじあい} (perfect game), もつれ{込|こ}む (to drag into overtime; verb)
- **Soccer / other sport (5)**: フリーキック (free kick), レッドカード (red card), ペナルティ (penalty), {禁|きん}じ{手|て} (prohibited move), サドンデス (sudden death)
- **Swimming (3)**: ドルフィンキック (dolphin kick), ストローク (stroke), {入水|にゅうすい} (entry into the water)
- **Business / feeling (3)**: {商売繁盛|しょうばいはんじょう} (prosperous business), {千客万来|せんきゃくばんらい} (roaring trade), やきもきする (to fret; verb-suru)
- **Everyday (4)**: {素振|すぶ}り (practice swing), {左|ひだり}{目|め} (left eye), {右|みぎ}{目|め} (right eye), だるま{落|お}とし (daruma otoshi)

### 2026-07-19 (Routine v2: new-entries — 16 New Entries, IDs 29936–29951)
Created 16 general-tier entries. The **5 "seen in entry" candidates** (C22402–C22406, cited from entries 06533 and 06536) were created first — internal-completeness gaps: ホルモン (hormone; grilled offal — 2 senses), {腹八分|はらはちぶ} (eating to 80% full), {元|もと}カレ (ex-boyfriend), {元|もと}カノ (ex-girlfriend), ぎくしゃく (awkward/strained; mimetic adverb). This **cleared the seen-in-entry queue**. The other 11 are hand-picked standalone lexemes, since the general candidate pool remains **heavily polluted with corpus-harvesting noise** (bare numbers/counters, compositional phrases, mis-glossed/coined items). The 11 salvaged: {日雇|ひやと}い{労働者|ろうどうしゃ} (day laborer), {二要素認証|にようそにんしょう} (two-factor authentication), {日照時間|にっしょうじかん} (hours of sunshine), ぐい{呑|の}み (sake cup), {駆動装置|くどうそうち} (drive mechanism), {喫煙車|きつえんしゃ} (smoking car), {圧縮率|あっしゅくりつ} (compression ratio), {士族階級|しぞくかいきゅう} (samurai class), {発酵菌|はっこうきん} (fermentation microbe), {防除剤|ぼうじょざい} (pest-control agent), {集客効果|しゅうきゃくこうか} (customer-drawing effect). All plain nouns except one mimetic adverb — no new verbs, i-adjectives, or kanji. 換気扇 and 農閑期 skipped as existing entries. §4 cross-model self-check on all 16 changed entries: **clean — 16/16, 0 flagged, 0 applied, 0 rejected**. $0.0069. The seen-in-entry queue is empty again and awaits curator/polish restock.

- **Seen-in-entry priority (5)**: ホルモン (hormone; offal), {腹八分|はらはちぶ} (eating to 80% full), {元|もと}カレ (ex-boyfriend), {元|もと}カノ (ex-girlfriend), ぎくしゃく (awkward; strained)
- **Everyday / social (3)**: {日雇|ひやと}い{労働者|ろうどうしゃ} (day laborer), ぐい{呑|の}み (sake cup), {喫煙車|きつえんしゃ} (smoking car)
- **Technical / science (4)**: {二要素認証|にようそにんしょう} (two-factor authentication), {駆動装置|くどうそうち} (drive mechanism), {圧縮率|あっしゅくりつ} (compression ratio), {発酵菌|はっこうきん} (fermentation microbe)
- **Nature / history / business (4)**: {日照時間|にっしょうじかん} (hours of sunshine), {士族階級|しぞくかいきゅう} (samurai class), {防除剤|ぼうじょざい} (pest-control agent), {集客効果|しゅうきゃくこうか} (customer-drawing effect)

### 2026-07-18 (Routine v2: new-entries — 12 New Entries, IDs 29924–29935)
Created 12 general-tier noun entries. The **3 remaining "seen in entry" candidates** (C22399–C22401, cited from entry 06526 平泳ぎ) were created first — a swimming set: メドレー (medley), {蛙足|かえるあし} (frog kick), プル (swimming arm pull). This **cleared the seen-in-entry queue**. The other 9 are hand-picked standalone lexemes, because the general candidate pool is now **heavily polluted with corpus-harvesting noise** — a ~600-candidate sample across the full added-date range was mostly bare numbers/counters, compositional phrases, mis-glossed place names, coined compounds, and wrong-kanji/wrong-gloss items. The 9 salvaged: {曳航|えいこう}{船|せん} (tugboat); a baseball cluster — {中堅|ちゅうけん}{手|しゅ} (center fielder), {右翼|うよく}{手|しゅ} (right fielder), {左翼|さよく}{手|しゅ} (left fielder), {出塁|しゅつるい}{率|りつ} (on-base percentage), {打点|だてん}{王|おう} (RBI leader); plus {章末|しょうまつ} (end of a chapter), {手|て}{牌|はい} (mahjong hand tiles), {持|じ}{碁|ご} (drawn game in go). All plain nouns — no new verbs, i-adjectives, or kanji. No duplicates created. Removed 1 stale candidate (C18953 剥れる/はぐれる — wrong kanji+gloss for the existing entry 28244 はぐれる). §4 cross-model self-check on all 12 changed entries: **clean — 12/12, 0 flagged, 0 applied, 0 rejected**. $0.0052. Logged a `[tooling]` observation recommending a curator prune of the corpus-harvested junk and a restock of useful mid-frequency vocabulary — the pool can no longer feed a full 20-entry run at quality.

- **Swimming — seen-in-entry (3)**: メドレー (medley), {蛙足|かえるあし} (frog kick), プル (arm pull)
- **Baseball (5)**: {中堅|ちゅうけん}{手|しゅ} (center fielder), {右翼|うよく}{手|しゅ} (right fielder), {左翼|さよく}{手|しゅ} (left fielder), {出塁|しゅつるい}{率|りつ} (on-base percentage), {打点|だてん}{王|おう} (RBI leader)
- **Other (4)**: {曳航|えいこう}{船|せん} (tugboat), {章末|しょうまつ} (end of a chapter), {手|て}{牌|はい} (mahjong hand tiles), {持|じ}{碁|ご} (drawn game in go)

