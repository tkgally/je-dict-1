# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-09-21
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

### 2026-10-06 (Routine v3: new-entries — 20 New Entries, IDs 31638–31657)

Twenty internal-closure candidates that existing entries already use: the sayings 弱り目に祟り目, 踏んだり蹴ったり and 腕が上がる; the verbs 乗り上げる (including 暗礁に乗り上げる), 先立つ, 絶つ, 通ずる and 儲かる (conjugation tables added); the nouns 活字離れ, 忠臣, 党内, 取り返し, 相手方, 我が社, 保健所, 蔵元, 寸断 (noun + する), 広がり; 慢性的 (na-adjective); and 外務省 (proper noun). No new kanji, stale markers or newcomer link ambiguities. Self-check skipped: the day's OpenRouter budget was spent. 43 internal-closure candidates remain.

### 2026-10-06 (Routine v3: new-entries — 12 New Entries, IDs 31626–31637)

Twelve internal-closure candidates that existing entries already use: the proverbs 後悔先に立たず and 石橋を叩いて渡る, 航行 and 拡充 (noun + する, conjugation tables added), 細める, 飛び交う and 浴びせる (verbs, tables added), 両家, 理系, 定評, 見分け, 色使い. A short cycle (started at 95 min). No new kanji; no stale markers or newcomer link ambiguities. Self-check skipped (the day's OpenRouter allowance was spent). 63 internal-closure candidates remain.

### 2026-10-06 (Routine v3: candidates — 56 Internal-Closure Candidates, C24033–C24088)

A SudachiPy scan of the examples' unlinked text for kanji words with no entry (the stale-noentry source is empty). 72 proposed; 11 variant spellings of existing entries dropped (活かす, うかがう, 見惚れる, 辿り着く, 取り掛かる …) and a few transparent compounds; 56 added, each with the entry it was seen in (保健所, 少子高齢化, 黙秘権, 遺品, 持ち越す, 面持ち …). Queue 63 → 119.

### 2026-10-06 (Routine v3: new-entries — 6 New Entries, IDs 31620–31625)

A short last cycle (started at 108 min): six internal-closure nouns that existing examples and notes already use,
物価高, 株主総会, 選挙戦, 定食屋, 満塁, 通気性. No new kanji; no stale markers or newcomer link ambiguities. Self-check
clean (0 flags). 17 internal-closure candidates remain.

### 2026-10-05 (Routine v3: new-entries — 10 New Entries, IDs 31610–31619)

Ten internal-closure nouns that existing examples and notes already use: 賛否両論, 取り調べ, 講習, 臭み, 尋問 (noun +
する, conjugation table added), 国際法, 損害賠償, 和平, 水性, 雪道. No new kanji; no stale markers or newcomer link
ambiguities. Self-check skipped (the day's OpenRouter allowance was spent). 23 internal-closure candidates remain.
