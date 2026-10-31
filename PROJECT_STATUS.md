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

### 2026-10-31 (19 new entries, third cycle)

32519–32537. Closure: 異存, 連れ戻す, ソースコード, コードレス, 替え刃, 基調講演. Brainstorm: 探し回る, 探し出す (seed 探す), 入室 (seed 入る), 夜店, 店番 (seed 店), 働きかける (seed 働く), ペットショップ. ezFurigana lookups: 短刀, 生物 (なまもの), 付加, 膨らみ, 崩落, 孫の手. Candidate 授賞式 was the standard spelling of 24267 受賞式, so that entry now has the headword 授賞式 (same ID) and a WRITING note.
Self-check: clean; 1 link removed (孫の手でかく read as でかい).

### 2026-10-31 (12 new entries, second cycle)

32507–32518. Closure: 動線, 吹き降り, 結び切り, 波括弧. Brainstorm (animal-general field): ナマコ, ヤモリ, 保護犬, カメレオン. ezFurigana lookups: 嘆き, 晴れ姿, 運び (three senses, incl. 〜の運びとなる), 戯れ.
Self-check: 1 tag fix (戯れ emotion → leisure).

### 2026-10-31 (15 new entries)

32492–32506. Closure: 托卵, 閑古鳥, ぶり返す, 計画停電, 取り計らう. Brainstorm (animal-general field): クラゲ, ヒトデ, ムカデ, 触手, サソリ. ezFurigana lookups: にわたる (as にわたって), ばかりか, 抱き合う, 白衣, 鼻息.
Self-check: 2 fixes (触手が動く is a slip for 食指が動く; どころか contrast softened).

### 2026-10-30 (8 new entries, second run)

32484–32491. Closure: 板書, 最年長, 使節団. Brainstorm (animal-general field): 蹄, 猟犬, 固有種. ezFurigana lookups: 胎動, 壁ドン.
Self-check: 1 doubtful claim (蹄 not Jōyō) removed.

### 2026-10-30 (8 new entries)

32476–32483. Closure: 歯列, 八重歯, 目白押し. Brainstorm: 三枚おろし, 胸びれ, 在来種. ezFurigana lookups: 上海, 除染.
Self-check: 1 pre-existing overstatement fixed in 盛りだくさん.
