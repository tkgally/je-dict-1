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

### 2026-10-30 (8 new entries, second run)

32484–32491. Closure: 板書, 最年長, 使節団. Brainstorm (animal-general field): 蹄, 猟犬, 固有種. ezFurigana lookups: 胎動, 壁ドン.
Self-check: 1 doubtful claim (蹄 not Jōyō) removed.

### 2026-10-30 (8 new entries)

32476–32483. Closure: 歯列, 八重歯, 目白押し. Brainstorm: 三枚おろし, 胸びれ, 在来種. ezFurigana lookups: 上海, 除染.
Self-check: 1 pre-existing overstatement fixed in 盛りだくさん.

### 2026-10-30 (20 new entries)

32456–32475. Closure: カバー力, 投影図, 熊鼠, 据え置き機, 素魚, 軽空母, 交戦権. Brainstorm: 待ちわびる (seed 待つ),
古道具 (seed 古い), 仕事人間 (seed 仕事), 放し飼い, 雑種, 狂犬病, 浮き袋. ezFurigana lookups: 〜期, 〜沿い, 〜省,
神出鬼没, 推計, 専門性. Self-check: 2 pre-existing errors fixed in 護衛艦 (JMSDF unit names).

### 2026-10-29 (20 new entries)

32436–32455. Closure: 調子に乗る, 出品者, 美術展, 冷やっこい, 早春, 日長, 告知書. Brainstorm: 待ち受ける, 巡り会う,
聞き捨てならない, までもない, 長々と, 人任せ, 肉球. ezFurigana lookups: 〜型 (がた), 環境省, ごまかし, 就業, 宿舎, 衆院.
Self-check: 3 notes overstatements fixed.

### 2026-10-29 (12 new entries)

32424–32435. Closure: 北極線, 同性婚, 冷やかし客, 訪問診療. Brainstorm: 待ち構える, 待ったなし (seed 待つ), 仕事始め,
力仕事 (seed 仕事). ezFurigana lookups: 一途をたどる, 疑義, ことになる, 小太り. Self-check clean.

