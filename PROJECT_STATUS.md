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

### 2026-11-28 (20 new entries, second cycle of the 01:16 UTC run)

34041–34060. Closure (from cycle 1's notes on 知的財産): 知財, 意匠権. Brainstorm (seeds 背中, すぐ, 嬉しい, だんだん, 楽しい, 悲しい, 困る, 味, 場所, 出かける; fields color, cooking, communication): 背中を押す, すぐさま, 嬉し涙, 日に日に, お楽しみ, 悲しげ, 楽しげ, 困り果てる, 味をしめる, くすむ, 色分け, 火が通る, 火を通す (paired in prominent see-also), ひとつまみ, 粗熱, お出かけ, 置き場所, 言いふらす. The harvester added reciprocal cross-references in 14 existing entries. Candidates queued from the new notes: 悔し涙, 感涙, 日増しに, 触れ回る.
Self-check: gpt-6.1-sol reviewed the 20 new entries, clean. 19 kana links judged, 1 removed (として in 意匠権 is quotative とする, "on the grounds that").

### 2026-11-27 (14 new entries, sixth cycle of the 10:44 UTC run)

34027–34040. Closure (from the notes of this run's first cycle): 加味, 破竹の勢い, 日の出の勢い, からし色. Brainstorm (seeds 危ない, 授業, 撮る, 百, 勉強, 病気, ご飯; field communication): 危なっかしい, 授業参観, 記念撮影, 百発百中, 危ぶむ, 猛勉強, 病み上がり, ご飯粒, 手話, 釘を刺す. The harvester added reciprocal cross-references in 6 existing entries.
Self-check: gpt-6.1-sol reviewed 20 (14 new + 6 neighbours), clean. 9 kana links judged, 0 flagged.

### 2026-11-27 (11 candidates queued, fifth cycle of the 10:44 UTC run)

Candidates mode. Brainstorm, field creation (147 member entries): 110 proposals (45 mine, 50 each from gpt-6.1-sol and gemini-3.8-flash), of which 94 were already entries; 11 queued (合作, 遺作, プロデュース, プロトタイプ, リメイク, 生みの親, 縫い合わせる, 縫製, 匠, 練り直す, 習作), 5 rejected (ろくろ is a spelling of 轆轤; 著作者, 鍛造, 製図 too specialized; 手先が器用 a free phrase). Closure: nothing new (no unresolved noentry markers; four closure words were queued by this run's first cycle). Queue 144 → 155. Model spend $0.06.

### 2026-11-27 (20 new entries, first cycle of the 10:44 UTC run)

34007–34026. Closure: 防災頭巾, 住宅展示場, モデルルーム. Brainstorm (clothing, cognition and color fields, and seeds 先週, 飛ぶ, 七): ショーツ, ボーダー, 襦袢, よそ行き, 袂, 内省, 勘案, 探究, 前週, 飛ぶ鳥を落とす勢い, 七不思議, パステルカラー, 三原色, 蛍光色, 黄土色, クリーム色, ゴールド. New kanji 袂, 襦, 袢 added to the kanji index. Candidates queued from the new notes: 加味, 破竹の勢い, 日の出の勢い, からし色.
Self-check: gpt-6.1-sol reviewed 20, 1 flag, applied (a gold card is a premium tier, not the top one). 17 kana links judged, 1 removed (というのは in 七不思議 is a topicalizer, not the "the reason is" entry).

### 2026-11-27 (16 new entries, fifth cycle of the 06:15 UTC run)

33991–34006. Closure: 腸内環境. Brainstorm (cognition and color fields, and seeds 七, 二, 三, 美味しい, 写真): 感づく, 物心がつく, 思い詰める, 頭をひねる, 七味唐辛子, ほっぺたが落ちる, 三流, 二の次, 二の舞, 三度目の正直, 写真写り, ベージュ, 黄ばむ, ねずみ色, 既視感. The first entries in directory entries/34000/. The harvester added reciprocal cross-references in 6 existing entries.
Self-check: gpt-6.1-sol reviewed 22 (16 new + 6 neighbours), 3 flags, all applied (思い詰める is transitive; a grammar slip in ほっぺたが落ちる's notes; 黄ばむ is also used of leaves). 13 kana links judged, 0 flagged.

