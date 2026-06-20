# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-06-16
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

### 2026-06-20 (Routine v2: new-entries — 14 New Entries, IDs 29365–29378)
Created all 14 priority "seen in entry" candidates — internal-completeness gaps the dictionary already referenced but had not defined (several are antonym/counterpart partners of existing entries: 悪徳↔美徳, 急減↔急増, 軟質↔硬質, 一神教↔多神教, 降機↔搭乗). The fallback "oldest unprocessed" lane was skipped: those Feb-2026 candidates are largely typos/non-words (権使, 些道, 個尊, 怒燥), so the run stayed focused on the 14 high-quality gaps rather than padding to ~20. Added ぼたもち and 管理栄養士 as new candidates from the new entries' notes; logged a [pattern] observation requesting a candidate-list cleanup and a [tooling] note on a reviewer false positive.

- **Foods/objects**: おはぎ (ohagi), {芋類|いもるい} (tubers/starches), {炭水|たんすい} (carbs, casual abbrev.), シルバーシート (silver/priority seat)
- **Abstract/society**: {悪徳|あくとく} (vice/corruption), {急減|きゅうげん} (sharp decrease; verb-suru), {軟質|なんしつ} (soft quality; adj-no), {一神教|いっしんきょう} (monotheism)
- **Travel/work/text**: {降機|こうき} (disembarking; verb-suru), {栄養士|えいようし} (nutritionist), {緒言|しょげん} (preface, academic), はじめに (to begin with / Introduction), {三大|さんだい} (the three major ~; prefix), {摂|と}る (to ingest/consume; verb-godan)

§4 self-check: 13 CLEAN; 1 flagged (29378 炭水 — model wanted formality "colloquial", but that is a domain value, not a valid formality; "informal" upheld and domain colloquial already set; rejected). $0.0061.

### 2026-06-20 (Routine v2: new-entries — 13 New Entries, IDs 29352–29364)
Added all 7 remaining priority seen-in-entry candidates (a coherent Japanese seasonal-customs/foods cluster tied to entries 06185–06196 and 29348) plus 6 hand-curated standalone words. The candidate pool outside the seen-in-entry set remains overwhelmingly corpus-harvest noise (bare numerals/counters, transparent 〜化/〜性/〜槽 compounds, conjugated fragments, dubious coinages), so standalone picks were curated for genuine dictionary-worthiness rather than padding to ~20. Added おはぎ (autumn counterpart of 牡丹餅) as a candidate from 29357's notes.

- **Seen-in-entry (7)**: {大食漢|たいしょくかん} (big eater/glutton), {千歳飴|ちとせあめ} (Shichi-Go-San candy), なので (so/therefore; because-it-is connective), お{焚|た}き{上|あ}げ (ritual burning of charms), {乾物屋|かんぶつや} (dried-goods store), {牡丹餅|ぼたもち} (botamochi), {棚|たな}ぼた (windfall; abbrev. of 棚から牡丹餅)
- **Standalone (6)**: {味|あじ}わい{深|ぶか}い (deeply flavorful; profound — i-adj), あしらい (handling/treatment; garnish), {塩入|しおい}れ (salt container), {戸襖|とぶすま} (fusuma-style sliding door), {売春婦|ばいしゅんふ} (prostitute), つり{輪|わ} (the rings, gymnastics)

§4 self-check: 12 CLEAN; 1 flagged (なので, 2 gloss issues, both rejected — sense 2 deliberately documents the copula-な + ので bundle, so "because (it) is" is accurate; model misread an intentional design). $0.0057.

### 2026-06-19 (Routine v2: new-entries — 15 New Entries, IDs 29337–29351)
Added all 15 remaining priority seen-in-entry candidates — a coherent batch of internal-completeness gaps, most of them antonym/counterpart pairs whose partner already had an entry, so each new entry adds a back-reference (target_id) to its existing partner. All are general-tier nouns (two also verb-suru). Added 大食漢 (たいしょくかん, big eater) as a candidate from 29348's notes.

- **Antonym pairs (8)**: {有限|ゆうげん} (finite ↔ {無限|むげん}), {低温|ていおん} (low temperature ↔ {高温|こうおん}), {高地|こうち} (highland ↔ {低地|ていち}), {能動|のうどう} (active ↔ {受動|じゅどう}), {好天|こうてん} (fine weather ↔ {悪天候|あくてんこう}), {大食|たいしょく} (big appetite ↔ {小食|しょうしょく}), {実名|じつめい} (real name ↔ {匿名|とくめい}), {車外|しゃがい} (outside the vehicle ↔ {車内|しゃない})
- **Counterpart/related (7)**: {軸|じく}{受|う}け (mechanical bearing; native term for ベアリング), {父性|ふせい} (fatherhood; cf {母性|ぼせい}), {答申|とうしん} (formal report/reply; cf {諮問|しもん}; verb-suru), {近刊|きんかん} (forthcoming publication), {避寒|ひかん} (escaping the winter cold; cf {避暑|ひしょ}; verb-suru), {独創|どくそう} (originality), {小学|しょうがく} (elementary-school level; cf {中学|ちゅうがく})

§4 self-check: 0 applied, 2 rejected (29339 `weather` upheld for 低温 — keeps the 高温 pair consistent, in-list narrowness nit; 29345 `general` upheld for 能動 — 能動的 is behavioral, not purely grammatical). $0.0065.

### 2026-06-18 (Routine v2: new-entries — 13 New Entries, IDs 29324–29336)
Added 13 curated standalone entries plus the 2 priority seen-in-entry gaps. The candidate pool outside the seen-in-entry set remains overwhelmingly corpus-harvest noise (bare numbers/counters, non-lexical fragments, transparent 〜率/〜化/〜性 compounds, ad-hoc phrases), so standalone picks were hand-selected for genuine dictionary-worthiness rather than padding to ~20. Dropped 段ボール箱 (transparent compound already covered by 18885 段ボール). Added 軸受け (じくうけ) as a candidate from 29330's similar-words note. Logged a [pattern] observation requesting a curator cleanup/restock of candidate_words.json.

- **Seen-in-entry (2)**: {捨|す}て{猫|ねこ} (abandoned/stray cat), {寝顔|ねがお} (sleeping face)
- **Standalone (11)**: メモ{用紙|ようし} (memo paper), {駐車|ちゅうしゃ}スペース (parking space), {似顔絵|にがおえ}{師|し} (portrait artist/caricaturist), {三角錐|さんかくすい} (triangular pyramid), ベアリング (mechanical bearing), {乳搾|ちちしぼ}り (milking), {麻雀|まーじゃん}{牌|ぱい} (mahjong tile), プリンアラモード (pudding à la mode), {南|みなみ}アジア (South Asia), アフリカ{大陸|たいりく} (African continent), {害獣|がいじゅう}{駆除|くじょ} (pest/vermin control)

§4 self-check: 1 applied (29333 gloss — opaque "pudding à la mode" clarified to descriptive form), 4 rejected (29329 `science` upheld — suggested "mathematics" not in taxonomy; 29333 ×3 translation — model wanted romaji "purin" in English, less clear). $0.0056.

### 2026-06-18 (Routine v2: new-entries — 12 New Entries, IDs 29312–29323)
Added 12 new entries: all 4 remaining priority seen-in-entry gaps plus 8 curated standalone words. The candidate pool outside the seen-in-entry set remains overwhelmingly corpus-harvest noise, so standalone picks were hand-selected for genuine dictionary-worthiness. Removed stale candidate ネジ (orthographic katakana variant of existing 00307_neji ねじ "screw"). Logged a [pattern] observation requesting curator restock of higher-quality candidates.

- **Seen-in-entry (4)**: {人災|じんさい} (man-made disaster; contrast 天災), {辞職願|じしょくねがい} (letter of resignation), {配属先|はいぞくさき} (place of assignment/posting), コロナ{禍|か} (the COVID-19 pandemic)
- **Standalone (8)**: {核|かく}ミサイル (nuclear missile), {距離計|きょりけい} (rangefinder), {昆虫類|こんちゅうるい} (insects/the insect class), {神在月|かみありづき} (tenth lunar month, Izumo name), {限界速度|げんかいそくど} (critical/limiting speed), {主要部|しゅようぶ} (main part), {重要語|じゅうようご} (key word/term), {厨房機器|ちゅうぼうきき} (commercial kitchen equipment)

§4 self-check: CLEAN — 0 issues across all 12 entries (independent accuracy review, $0.0052).

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
