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

### 2026-09-28 (Routine v3: new-entries — 8 New Entries, IDs 31195–31202)

The last six internal-closure candidates: 知床, 鳶が鷹を生む, 大根役者, 笑い皺, 追々 (gradually; distinct from 08812
おいおい 'bawling'), これまで; then two from the vetted proper-noun queue, 湯川秀樹 and 嵐山. 05387's old `noentry`
marker for 嵐山 now links, and 08731's cross-reference to 鳶が鷹を生む is hardened. Stopped at eight because the
run clock was near its end. Self-check skipped (daily review budget spent). Candidate queue stands at 70.

### 2026-09-28 (Routine v3: new-entries — 20 New Entries, IDs 31175–31194)

All twenty are internal-closure words already used by older entries: 縄文, 必殺技, 発泡, マムシ, グローブ, 貧富,
ボンベ, 被写体, 資本金, クリスマスイブ, ゴールイン, レーザー, 直下, コピペ, なめこ, 外堀, and the proper nouns
文部科学省, 大航海時代, ノーベル賞, 大阪城. 33 old `noentry` markers in 21 entries now link to them. Stale candidate
四方山話 removed (duplicate of よもやま話, 26013). Self-check skipped (daily review budget spent). Candidate queue
stands at 77.

### 2026-09-28 (Routine v3: new-entries — 20 New Entries, IDs 31155–31174)

All twenty are internal-closure words already used by older entries: 三唱, レザー, 御礼, ハムスター, スティック,
五角形, カーナビ, ノースリーブ, ピンとくる, 漆塗り, あんパン, ポップス, 螺旋, ワルツ, リクルートスーツ, and the proper
nouns 伊豆, 山梨県, 歌舞伎座, アラビア, 朝鮮. 51 old `noentry` markers in 32 entries now link to them. New kanji 螺
(02809). Self-check skipped (daily review budget spent). Candidate queue stands at 95.

### 2026-09-28 (Routine v3: new-entries — 20 New Entries, IDs 31135–31154)

All twenty are internal-closure words from the restock earlier today, each one already used by older entries:
連体詞, 期する, 厚生, 一次, 二次, 胴, 無機, 借主, 遺志, 対称, 転じる, 与る, 辞する, かしこまる, ケースバイケース,
民主的, 北緯, and the proper nouns 東京都, 姫路城, 東日本大震災. 47 old `noentry` markers in 30 entries now link to
them. Self-check skipped (daily review budget spent). Candidate queue stands at 113.

### 2026-09-28 (Routine v3: candidates — 61 words queued, C23538–C23598)

Internal-closure restock from `check_stale_noentry.py`'s unresolved class: every word is one an existing entry
already uses but the dictionary does not define (期する, 連体詞, 厚生, 一次/二次, 胴, 無機, 借主, 遺志, 対称, 転じる,
与る, 辞する, かしこまる, ピンとくる, ケースバイケース, ゴールイン …), plus places and events those entries name
(東京都, 山梨県, 伊豆, 知床, 姫路城, 大阪城, 歌舞伎座, 東日本大震災, 文部科学省). Affixes, number+counter strings and
variant spellings of existing entries (湯呑み, 箸置き, 売上, 和歌山県 …) were skipped. Queue: 72 → 133.
