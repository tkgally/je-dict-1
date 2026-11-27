# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-10-26
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
| Total entries | ~30,764 |
| Basic tier | 801 (closed) |
| Core tier | ~1,982 (closed) |
| General tier | ~27,981 (open) |
| Candidate words | ~188 (all vetted; queue cleaned 2026-08-11) |
| Cross-references | ~19,000 |
| Example sentences | ~119,000 |

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

### 2026-11-27 (20 new entries, first cycle of the 10:44 UTC run)

34007–34026. Closure: 防災頭巾, 住宅展示場, モデルルーム. Brainstorm (clothing, cognition and color fields, and seeds 先週, 飛ぶ, 七): ショーツ, ボーダー, 襦袢, よそ行き, 袂, 内省, 勘案, 探究, 前週, 飛ぶ鳥を落とす勢い, 七不思議, パステルカラー, 三原色, 蛍光色, 黄土色, クリーム色, ゴールド. New kanji 袂, 襦, 袢 added to the kanji index. Candidates queued from the new notes: 加味, 破竹の勢い, 日の出の勢い, からし色.
Self-check: gpt-6.1-sol reviewed 20, 1 flag, applied (a gold card is a premium tier, not the top one). 17 kana links judged, 1 removed (というのは in 七不思議 is a topicalizer, not the "the reason is" entry).

### 2026-11-27 (16 new entries, fifth cycle of the 06:15 UTC run)

33991–34006. Closure: 腸内環境. Brainstorm (cognition and color fields, and seeds 七, 二, 三, 美味しい, 写真): 感づく, 物心がつく, 思い詰める, 頭をひねる, 七味唐辛子, ほっぺたが落ちる, 三流, 二の次, 二の舞, 三度目の正直, 写真写り, ベージュ, 黄ばむ, ねずみ色, 既視感. The first entries in directory entries/34000/. The harvester added reciprocal cross-references in 6 existing entries.
Self-check: gpt-6.1-sol reviewed 22 (16 new + 6 neighbours), 3 flags, all applied (思い詰める is transitive; a grammar slip in ほっぺたが落ちる's notes; 黄ばむ is also used of leaves). 13 kana links judged, 0 flagged.

### 2026-11-27 (43 candidates queued, second cycle of the 06:15 UTC run)

Candidates mode. Brainstorm, field cooking: 22 queued (ピーラー, 粗熱, 塩もみ, ひと煮立ち, 火が通る, 火を通す, 目分量, 焼き色, …), 10 rejected (5 spellings of existing entries, 5 too specialized). Brainstorm, seeds 場所 to 値段 (basic tier): 20 queued (場所取り, 困り果てる, 昨日今日, 一枚岩, 客足, よりどりみどり, …), 5 rejected as spellings of existing entries. Closure: 1 (腸内環境); the noentry list is empty and the unlinked words in examples are almost all other spellings of existing entries. Queue 133 → 176. Model spend $0.15.

### 2026-11-27 (6 new entries, seventh cycle of the 00:15 UTC run)

33985–33990. Brainstorm (fields clothing, cognition, building; no closure or ezFurigana candidates were waiting): 襷, 頭巾, 会得, モデルハウス, 雨合羽, 雪駄. A small batch because the run clock was near its end. New kanji 襷 added to the kanji index (02880). Three closure candidates added (防災頭巾, 住宅展示場, モデルルーム).
Self-check: gpt-6.1-sol reviewed 6, 0 flags; 6 kana links judged, 0 flagged; 3 wrong kana links in my own notes unlinked by hand decision (が, か, モデル in モデルルーム).

### 2026-11-26 (8 new entries, ninth cycle of the 00:15 UTC run)

33977–33984. Closure (all three waiting, queued in the first cycle): 飲み残す, 切れ者, ワッペン. Brainstorm (field clothing, oldest first): ウインドブレーカー, オーバーオール, チノパン, ハーフパンツ, ポンチョ. A small batch because the run clock was near its end.
Self-check: gpt-6.1-sol reviewed 8, 0 flags; 4 kana links judged, 0 flagged.

