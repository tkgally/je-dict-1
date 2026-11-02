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

### 2026-11-02 (6 new entries, fourteenth cycle)

32654–32659. Closure: 潔癖症, 送り届ける. Brainstorm (animal-insect field): 虫の知らせ, 青虫. ezFurigana lookups: 憂う, 英検.
Self-check: 1 tag flag applied (英検 is a test, not an organization); 1 kana link removed (という in 虫の知らせというのか is と + 言う).

### 2026-11-02 (18 new entries, ninth cycle)

32636–32653. Closure: 単独親権, 国民皆年金, 魔方陣, 急ごしらえ, 前方後円墳, 選び抜く. Brainstorm (animal-insect field): カミキリムシ, ウジ, ミノムシ, 虫取り, 虫食い (two senses), 蝉時雨. ezFurigana lookups: 色味, 迂闊, 内回り, 移ろう, 畝, ウラン.
Self-check: 1 accuracy flag applied (魔方陣 note: 法 means "law, method", not "magic"); 6 kana links confirmed.

### 2026-11-02 (candidate restock, 70 added)

Queue 550 → 620 (C25567–C25636). Closure (49, words named in notes of entries changed since 2026-10-31): e.g. 感謝祭, 直角三角形, 奥の手, 九分九厘, 絵空事, 第一人者, 統合失調症, 鉤括弧. Brainstorm (seeds 遅い…パン, 20 basic headwords; 21 added of 50 new proposals): e.g. 母の日, どこもかしこも, 歩きスマホ, 遊び半分, 家族葬, コッペパン.

### 2026-11-02 (12 new entries, fifth cycle)

32624–32635. Closure: 瀬戸物, 頭数, 証明写真, 個包装. Brainstorm (animal-insect field): モンシロチョウ, アブラゼミ, ミンミンゼミ, ボウフラ. ezFurigana lookups: 致し方ない (as 致し方), いやに, 入れ歯, 後ろ姿.
Self-check: clean (0 accuracy flags); 1 kana link kept (子供のころ → 〜ころ, which lacks the "time when" sense; sent to the curator).

### 2026-11-02 (18 new entries, second cycle)

32606–32623. Closure: 二等辺三角形, 夢物語, 立役者, すり合わせる, 出がらし, おから. Brainstorm (animal-insect field): ダンゴムシ, アメンボ, 蜘蛛の巣, 虫かご, コバエ, ヤゴ. ezFurigana lookups: 異色, 痛手, 一体化, 凍てつく, いとも, 域.
Self-check: clean (0 accuracy flags, 17 kana links confirmed).

