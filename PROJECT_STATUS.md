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

### 2026-10-04 (Routine v3: new-entries — 20 New Entries, IDs 31533–31552)

Twenty words that older entries already used: 抑うつ, 財務省, 院内感染, 機能障害, 動脈瘤, 静脈瘤, 四角四面, フレイル,
闇バイト, うな重, うな丼, ひつまぶし, 白焼き, 戻りガツオ, 表装, 文房四宝, されど, 追い抜き, 共同浴場, 新快速. No new
kanji. The harvester added back-links in 15 neighbours. Two stale candidates removed (許しがたい and そうはいっても
duplicate 許し難い and そうは言っても). Self-check skipped (daily OpenRouter budget spent); ひつまぶし awaits kana screening.

### 2026-10-04 (Routine v3: new-entries — 14 New Entries, IDs 31519–31532)

Fourteen words that older entries already used: 軍勢, 疼痛, 着水, 巡航, 配当金, 提供者, 銃弾, 論理学, 無礼者, 前年比,
使用済み, スペアタイヤ, 地方裁判所, 精白米. One new kanji (疼, kanji ID 02821). The linker connected them where they
were first seen, and the harvester added back-links in 18 neighbours. Self-check: clean (no issues on 32 entries); one
kana link checked and kept.

### 2026-10-03 (Routine v3: new-entries — 8 New Entries, IDs 31511–31518)

Eight words that older entries already used: 何より, 叙述, 呵責, 押し返す, 理路整然, 改善策, 労災, 走り抜ける. One new
kanji (呵, kanji ID 02820). A short cycle at the end of the run. Self-check skipped (daily OpenRouter budget spent), so
these eight have had no independent review yet. 22 links of ふける (耽る) checked against the newer 更ける entry: all stay.

### 2026-10-03 (Routine v3: new-entries — 4 New Entries, IDs 31507–31510)

Four words that older entries already used: ガイドブック, 不時着, 精鋭, 北枕. A short cycle at the end of the run. No new
kanji. Self-check skipped (daily OpenRouter budget spent), so these four have had no independent review yet.

### 2026-10-03 (Routine v3: new-entries — 20 New Entries, IDs 31487–31506)

Twenty words that older entries already used: 排出量, 追随, 内出血, 歯石, 肝硬変, 国家試験, 添乗員, 偽造品, 雄鶏,
雌鶏, 研修生, 巻き毛, 資本家, 二乗, 勾配, 元値, 考え事, 名優, 発言権, 本命. No new kanji. The linker connected them in
the entries where they were first seen. Candidate 浸食 dropped (variant spelling of 侵食 10927). Self-check: clean;
one kana link retargeted (なさい).

