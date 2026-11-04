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

### 2026-11-04 (9 new entries, sixth cycle of the 12:15 run)

32825–32833. Closure: 幹細胞, 遺伝子組み換え, 回顧録. Brainstorm (animal-mammal field): ヤマアラシ (contrasted with ハリネズミ), ポニー, スカンク. ezFurigana lookups: 食い物 (also 〜を食い物にする), くびれ, 串刺し.
Self-check: clean (0 flags on 9 entries, 3 kana links confirmed).

### 2026-11-04 (18 new entries, fourth cycle of the 12:15 run)

32807–32824. Closure: お供, 造船所, 脳出血, 費用対効果, 奥の手, 逃げ場. Brainstorm (animal-mammal field): ホッキョクグマ (linked to シロクマ), 介助犬, 牧羊犬, 闘牛 (Spanish and Japanese bull contests), アリクイ, マングース. ezFurigana lookups: 〜業, 〜切れ, 苦 (苦にする, 苦もなく), 禁忌, 供与, 近海.
Self-check: clean (0 flags on 18 entries, 9 kana links confirmed).

### 2026-11-04 (candidate restock, first cycle of the 12:15 run)

70 candidates queued (C25668–C25737), queue 479 → 549. Closure (13, from a tokenizer scan of example sentences for words with no entry): 天皇陛下, 両論併記, 腸内細菌, 素因, 立憲主義, 〜周忌, カツオのたたき, 子々孫々, 待ち焦がれる, 脱原発, 来季, 修行僧, 革命家. Brainstorm (appearance field, 57): えくぼ, 丸顔, 面長, 童顔, 垂れ目, 切れ長, くせ毛, 枝毛, 坊主頭, 二重あご, 無精ひげ, アイシャドウ, つけまつげ, イメチェン, 様になる, 見違える and others.

### 2026-11-04 (6 new entries, seventh cycle of the 00:15 run)

32801–32806. Closure: 直角三角形, 東側 (also the Cold War East), 火口湖. Brainstorm: シロナガスクジラ. ezFurigana lookups: 教皇 (with the 2019 switch from 法王), 教祖.
Self-check: clean (0 flags on 12 entries, 4 kana links confirmed).

### 2026-11-04 (20 new entries, fourth cycle of the 00:15 run)

32781–32800. Closure: ヒキガエル, 文化系 and 体育会系 (paired as antonyms), ガチャ, 湯取り法, 苦言, 思考回路, 感謝祭. Brainstorm (animal-mammal field): ロバ, アルマジロ, バイソン, シロクマ, カピバラ, シマリス. ezFurigana lookups: 甲 (party A; shell; back of the hand), 主 (main; the Lord), イエス, 関連付け, 貴公子, 肝いり.
Self-check: clean (0 flags on the 20 new entries and 10 neighbours that gained cross-references).

