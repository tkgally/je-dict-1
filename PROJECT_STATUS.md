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

### 2026-10-28 (9 new entries, third batch)

32415–32423. Closure: 対句, 警棒, 税務調査. Brainstorm (fish field): 川魚, 小骨, 魚群. ezFurigana lookups: 舵取り,
かのように, 管内. 版 (03698) compound readings fixed (改訂版, 最新版 … are ばん). Self-check: 1 applied, 1 link fixed.

### 2026-10-28 (6 new entries, second batch)

32409–32414. Closure: 歴史作家, 平面図形. Brainstorm (fish field): トロ, 海水魚. ezFurigana lookups: 宋, 永眠.
Self-check clean.

### 2026-10-28 (21 new entries)

32388–32408. Closure: 一点鎖線, 理解し合う, 撥音便, インクパッド, 粗悪品, 方法論, 溝鼠. Brainstorm (bird and
fish fields): コンドル, スズキ, サワラ, ニジマス, エイ, タツノオトシゴ, シラス. ezFurigana lookups: 〜ずに,
〜ないで, 〜としても, 〜であれ, 紫色, 罵詈雑言, いち早く. Self-check: 1 applied, 1 link fixed.

### 2026-10-27 (candidates: 21 added)

Closure 12 (words today's accuracy review and new entries named in notes: 単独親権, 国民皆年金, 魔方陣, 計画停電,
吹き降り, 結び切り, 波括弧, 焼きプリン, 耕作放棄地, 替え刃, 指し棒, 基調講演). Brainstorm seeds 80–99 (出る … 借りる):
222 proposals, 198 already entries; 9 added (脱ぎ捨てる, 手始め, 借り物, 目に入る, はみ出る, 出遅れる, もらい物,
勉強家, 前借り), 14 rejected. Queue 660.

### 2026-10-27 (15 new entries, third batch)

32373–32387. Closure: 計画倒れ, 平服, 尾てい骨, 共同親権, 国民皆保険. Brainstorm (bird and fish fields):
ムクドリ, 九官鳥, カンパチ, ドジョウ, トビウオ. ezFurigana lookups: 勝手に, 主たる, 奴隷, 点く, 横殴り.
点く is now the intransitive pair of つける (00562). Self-check: 2 flags, both applied.

