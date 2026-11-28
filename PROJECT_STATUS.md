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

### 2026-11-28 (17 candidates queued, fourth cycle of the 07:12 UTC run)

Candidates mode. Brainstorm, seeds 380–400 (眠い, おかしい, 怒る, おととい, お釣り, レジ, 最近, 最初, 皿, 砂糖, 島, 塩, 質問, 正しい, 助ける, 店員, 手伝う, 生まれる, 売る, 悪い): 330 proposals (124 mine, 111 from gpt-6.1-sol, 95 from gemini-3.8-flash), of which 166 were already entries and 11 were other spellings of entries (眠たい, 売上, 欠伸, 寝惚ける, ムカつく, 頭に来る …); 17 queued (目が冴える, 眠気覚まし, おかしな, お釣りが来る, レジ係, レジ打ち, このところ, 受け皿, 粉砂糖, 岩塩, 塩対応, 質問攻め, 助け舟, 生まれ故郷, 喧嘩を売る, 売り物, 売り込む), 5 rejected as free phrases or transparent compounds (塩を振る, 砂糖水, 質問票, お釣りを渡す, キャッシュレジスター). Closure: nothing new. Queue 111 → 128. Model spend $0.09.

### 2026-11-28 (16 new entries, third cycle of the 07:12 UTC run)

34061–34076. Closure (queued from the previous new-entries cycle's notes): 悔し涙, 感涙, 日増しに, 触れ回る. Brainstorm (fields brand-name, color): ヤフー, サントリー, シーチキン, ホワイト, レッド, シルバー (with its "for the elderly" sense: シルバー人材センター, シルバーシート), カーキ, モノトーン (a false friend: not English "monotone"), 真っ黄色, 乳白色, 色むら, 色移り. The harvester added reciprocal cross-references in ツナ缶 and ベージュ.
Self-check: gpt-6.1-sol reviewed 18 (16 new + 2 neighbours), 2 applied: 日増しに also describes a deepening decline; モノトーン's rare "monotonous" sense is now acknowledged. 8 kana links judged, 0 flagged.

### 2026-11-28 (20 new entries, second cycle of the 01:16 UTC run)

34041–34060. Closure (from cycle 1's notes on 知的財産): 知財, 意匠権. Brainstorm (seeds 背中, すぐ, 嬉しい, だんだん, 楽しい, 悲しい, 困る, 味, 場所, 出かける; fields color, cooking, communication): 背中を押す, すぐさま, 嬉し涙, 日に日に, お楽しみ, 悲しげ, 楽しげ, 困り果てる, 味をしめる, くすむ, 色分け, 火が通る, 火を通す (paired in prominent see-also), ひとつまみ, 粗熱, お出かけ, 置き場所, 言いふらす. The harvester added reciprocal cross-references in 14 existing entries. Candidates queued from the new notes: 悔し涙, 感涙, 日増しに, 触れ回る.
Self-check: gpt-6.1-sol reviewed the 20 new entries, clean. 19 kana links judged, 1 removed (として in 意匠権 is quotative とする, "on the grounds that").

### 2026-11-27 (14 new entries, sixth cycle of the 10:44 UTC run)

34027–34040. Closure (from the notes of this run's first cycle): 加味, 破竹の勢い, 日の出の勢い, からし色. Brainstorm (seeds 危ない, 授業, 撮る, 百, 勉強, 病気, ご飯; field communication): 危なっかしい, 授業参観, 記念撮影, 百発百中, 危ぶむ, 猛勉強, 病み上がり, ご飯粒, 手話, 釘を刺す. The harvester added reciprocal cross-references in 6 existing entries.
Self-check: gpt-6.1-sol reviewed 20 (14 new + 6 neighbours), clean. 9 kana links judged, 0 flagged.

### 2026-11-27 (11 candidates queued, fifth cycle of the 10:44 UTC run)

Candidates mode. Brainstorm, field creation (147 member entries): 110 proposals (45 mine, 50 each from gpt-6.1-sol and gemini-3.8-flash), of which 94 were already entries; 11 queued (合作, 遺作, プロデュース, プロトタイプ, リメイク, 生みの親, 縫い合わせる, 縫製, 匠, 練り直す, 習作), 5 rejected (ろくろ is a spelling of 轆轤; 著作者, 鍛造, 製図 too specialized; 手先が器用 a free phrase). Closure: nothing new (no unresolved noentry markers; four closure words were queued by this run's first cycle). Queue 144 → 155. Model spend $0.06.

