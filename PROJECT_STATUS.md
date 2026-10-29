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

### 2026-10-29 (20 new entries)

32436–32455. Closure: 調子に乗る, 出品者, 美術展, 冷やっこい, 早春, 日長, 告知書. Brainstorm: 待ち受ける, 巡り会う,
聞き捨てならない, までもない, 長々と, 人任せ, 肉球. ezFurigana lookups: 〜型 (がた), 環境省, ごまかし, 就業, 宿舎, 衆院.
Self-check: 3 notes overstatements fixed.

### 2026-10-29 (12 new entries)

32424–32435. Closure: 北極線, 同性婚, 冷やかし客, 訪問診療. Brainstorm: 待ち構える, 待ったなし (seed 待つ), 仕事始め,
力仕事 (seed 仕事). ezFurigana lookups: 一途をたどる, 疑義, ことになる, 小太り. Self-check clean.

### 2026-10-29 (candidates: 92 added)

Closure 40 (words that recent entries name in their notes without an entry: 連れ戻す, 結果論, 立役者, 周知徹底,
有効求人倍率, 前方後円墳, マイナンバー …). Brainstorm (mammal field): 96 proposals, 29 already entries; 52 added
(コアラ, シャチ, ラッコ, チーター, モグラ, ロバ, 介助犬, 牧羊犬, 張り子の虎, 猫の額, 虎の子 …), 10 rejected. Queue 715.

### 2026-10-28 (9 new entries, third batch)

32415–32423. Closure: 対句, 警棒, 税務調査. Brainstorm (fish field): 川魚, 小骨, 魚群. ezFurigana lookups: 舵取り,
かのように, 管内. 版 (03698) compound readings fixed (改訂版, 最新版 … are ばん). Self-check: 1 applied, 1 link fixed.

### 2026-10-28 (6 new entries, second batch)

32409–32414. Closure: 歴史作家, 平面図形. Brainstorm (fish field): トロ, 海水魚. ezFurigana lookups: 宋, 永眠.
Self-check clean.

