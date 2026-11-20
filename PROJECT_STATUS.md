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

### 2026-11-20 (16 candidates added, eighth cycle of the 12:15 UTC run)

Brainstorm, seeds 300–320 (撮る … 階段; 177 proposals: 60 own, 107 gpt-6.1-sol, 91 gemini-3.8-flash after merging; 164 already entries; 13 new, 9 added, 4 rejected): 危なっかしい, 授業参観, 記念撮影, 百発百中, 隠し撮り, 危ぶむ, 猛勉強, 病み上がり, ご飯粒. Closure (words used in today's entries): 烙印, 袖の下, 御霊, 枢軸, 頭字語, 点鼻薬, 榴弾. Queue: 208.

### 2026-11-20 (12 new entries, sixth cycle of the 12:15 UTC run)

33830–33841. Brainstorm: プリクラ, マジックテープ, バンドエイド, エクセル (field brand-name), 秋分の日 (same category as 九月), 関西国際空港 (related to 空港). ezFurigana: レイアウト, レッテル, 連呼, 連名, 沸き返る, 訳あり (shows 訳アリ). No closure candidates queued.
Self-check: clean (0 flags from gpt-6.1-sol; 8 kana links judged, 0 flagged).

### 2026-11-20 (10 new entries, eighth cycle of the 00:15 UTC run)

33820–33829. Brainstorm (field brand-name): プレイステーション, PASMO, カルピス, ヤクルト, グーグル. ezFurigana: 皇室典範 (shows 典範), 両刃, 臨海, 倫理的, 塁. No closure candidates were queued.
Self-check: clean (0 flags from gpt-6.1-sol; 5 kana links judged, 0 flagged).

### 2026-11-20 (20 new entries, second cycle of the 00:15 UTC run)

33800–33819. Closure: 鍔 (brim; sword guard, seen in 33789), アンインストール (seen in 04762). Brainstorm (field brand-name and art): 尾形光琳, パナソニック, ホンダ, 楽天, イオン (ion; Aeon), カップヌードル, ドン・キホーテ, ニトリ, 日産. ezFurigana: 悶絶, 友愛, 遊説, 夢見心地, リテラシー, 留置, 両思い (shows 両想い), ミュージック, ラグ (rug; lag). New kanji 琳 (02875), 鍔 (02876).
Self-check: 2 fixed (イオン came via German Ion; 日産 "daily output" stands alone too); 15 kana links judged, 0 flagged.

### 2026-11-19 (47 candidates added, seventh cycle of the 12:15 UTC run)

Brainstorm, field color (96 proposals: 47 own, 50 each from gpt-6.1-sol and gemini-3.8-flash; 44 already entries; 51 new, 47 added, 5 rejected as rare traditional or technical color names): ベージュ, ねずみ色, 黄土色, 白っぽい / 赤っぽい / 黒っぽい, 黄ばむ, くすむ, 色むら, 色移り, 三原色, 蛍光色, モノトーン, 乳白色, 浅黒い, 紅一点, 黄色い声, 白黒をつける, 迷彩, … Closure: no unresolved noentry markers remain. Queue 233 (205 closure and brainstorm).

