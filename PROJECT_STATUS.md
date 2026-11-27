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

### 2026-11-27 (6 new entries, seventh cycle of the 00:15 UTC run)

33985–33990. Brainstorm (fields clothing, cognition, building; no closure or ezFurigana candidates were waiting): 襷, 頭巾, 会得, モデルハウス, 雨合羽, 雪駄. A small batch because the run clock was near its end. New kanji 襷 added to the kanji index (02880). Three closure candidates added (防災頭巾, 住宅展示場, モデルルーム).
Self-check: gpt-6.1-sol reviewed 6, 0 flags; 6 kana links judged, 0 flagged; 3 wrong kana links in my own notes unlinked by hand decision (が, か, モデル in モデルルーム).

### 2026-11-26 (8 new entries, ninth cycle of the 00:15 UTC run)

33977–33984. Closure (all three waiting, queued in the first cycle): 飲み残す, 切れ者, ワッペン. Brainstorm (field clothing, oldest first): ウインドブレーカー, オーバーオール, チノパン, ハーフパンツ, ポンチョ. A small batch because the run clock was near its end.
Self-check: gpt-6.1-sol reviewed 8, 0 flags; 4 kana links judged, 0 flagged.

### 2026-11-26 (20 new entries, first cycle of the 00:15 UTC run)

33957–33976. Closure (all six waiting): 腹が減る, 変声期, 念押し, 話が合う, 飲み残し, 降壇. Brainstorm, everyday words first: ポカリスエット, ポッキー (field brand-name), スカーフ, バッジ, フリース, 型崩れ, 腕まくり, 耳当て, ハイソックス (field clothing), 襲いかかる (compound of かかる), 当月 (register counterpart of 今月), 耳を疑う, 頭が切れる, 思い悩む (field cognition). 九死に一生を得る dropped: 九死に一生 (18016) already covers it. Three closure candidates added (飲み残す, 切れ者, ワッペン).
Self-check: gpt-6.1-sol reviewed 21, 0 flags; 17 kana links judged, 1 flagged (そんなに, kept as in earlier rulings).

### 2026-11-23 (candidates: 12 added, seventh cycle of the 00:15 UTC run)

Brainstorm only (no noentry markers unresolved; the six "seen in entry" candidates were queued earlier today; no ezFurigana rows pending). Seeds 00806–00828: 背中を押す, 背を向ける, すぐさま, 嬉し涙, 溜飲を下げる, 触らぬ神に祟りなし, おばあちゃん子, 多分に, お楽しみ, 楽しげ, 味をしめる, 翌々日. 156 of 179 proposals were already entries; 10 rejected (spellings of existing entries, a transparent phrase, a dated word). Model spend about $0.09.

### 2026-11-23 (22 new entries, first cycle of the 00:15 UTC run)

33935–33956, all brainstorm candidates (no closure or ezFurigana candidates were waiting), chosen for everyday use: お腹が空く, お腹を壊す, 気が変わる, 食べ残し, 食べ残す, 紙コップ, 紙皿, 雨靴, 長椅子, 変わり, 頭に入れる, 物知り, 声変わり, 知ったかぶり, 白っぽい, 赤っぽい, 黒っぽい, 念を押す, 話が弾む, 答え合わせ, 食べかけ, 飲みかけ. お冷 dropped: 冷や (28141) already covers it. Five closure candidates added (腹が減る, 変声期, 念押し, 話が合う, 飲み残し).
Self-check: gpt-6.1-sol reviewed 22, 0 flags; 12 kana links judged, 0 flagged.

