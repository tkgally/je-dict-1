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

### 2026-11-07 (12 new entries, fourth cycle of the 12:15 run)

33075–33086. Closure: カツオのたたき, 色打掛, 核分裂, 本塁. Brainstorm: 絵になる, 見違える (appearance field), 父の日, 姉貴. ezFurigana lookups: 重症化, 常備薬, 助産師 (looked up as 助産婦), 尋常.
Self-check: 1 flag applied (異常 is not always negative); 8 kana links confirmed.

### 2026-11-07 (20 new entries, first cycle of the 12:15 run)

33055–33074. Closure: ダッシュ, 健勝, 番頭, 濃茶, 今場所, 写経, 親鸞. Brainstorm (appearance field): ヘアスタイル, 小綺麗, 彫りが深い, 恰幅, 様になる, 無精ひげ, 目鼻立ち. ezFurigana lookups: ショット, シンガポール, 実験的, 邪念, ジャーナリスト, 重軽傷.
Self-check: 3 flags applied (初日 read しょにち; 健勝 claim softened; 恰幅 not a body part); 25 kana links confirmed.

### 2026-11-07 (20 new entries, fourth cycle of the 00:15 run)

33035–33054. Closure: 来季, 修行僧, 革命家, 陸の孤島, 高裁, 家裁, 不信任案. Brainstorm (appearance field): エステ, スキンヘッド, 丸刈り, 出っ歯, 口ひげ, 小顔, 天然パーマ (入れ墨 dropped: covered by 刺青 09639). ezFurigana lookups: 心技体, 親身, 時空, 辞書形, 地蔵, 実地.
Self-check: clean (0 flags on 20 entries); 22 kana links confirmed.

### 2026-11-07 (22 new entries, second cycle of the 00:15 run)

33013–33034. Closure: 役満, 天皇陛下, 両論併記, 腸内細菌, 素因, 立憲主義, 待ち焦がれる, 脱原発, 子々孫々. Brainstorm (appearance field): いかり肩, おめかし, けばけばしい, こざっぱり, つけまつげ, もみあげ, イメチェン. ezFurigana lookups: クレイジー, シック, 初老, 調べ, 新歓, 処理水.
Self-check: 2 flags applied (つけまつげ is not a body part; 漏電 is electrical leakage); 22 kana links confirmed; 1 wrong kanji link removed (付け in 付けまつげ).

### 2026-11-06 (10 new entries, eighth cycle of the 12:15 run)

33003–33012. Closure: 連帯債務, 器楽, 製造者, 武器商人. Brainstorm (appearance field): 美少年, 色黒, 長髪. ezFurigana lookups: 市議, 主席 (contrasted with 首席), 集合体. A short cycle at the end of the run.
Self-check: clean (0 flags on 10 entries); 7 kana links confirmed.

