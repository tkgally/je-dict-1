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

### 2026-11-08 (15 new entries, sixth cycle of the 16:15 run)

33153–33167. Closure: 教育委員会, 参院選, 教鞭, 国歌斉唱, 法定速度. Brainstorm: 出来損ない, 女手一つ, 口約束, 男泣き, 備え付け. ezFurigana lookups: 身上, 生理学, 征服者, セクション, セレクション.
Self-check: clean (0 flags); 9 kana links confirmed. 24 cross-references harvested (12 reciprocal).

### 2026-11-08 (20 new entries, third cycle of the 16:15 run)

33133–33152. Closure: 万歳三唱, 二世帯住宅, 激甚災害, 鎌倉幕府, 室町幕府, 宝塚歌劇団, 平泉. Brainstorm: 子沢山, 止まり木, 海原, 海開き, 海鳴り, 荒海, 顔負け. ezFurigana lookups: 籍, 精, 刹那的, 責め, セラピスト, 星条旗.
Dropped as spelling duplicates: たれ目 (垂れ目 32994 exists), 座敷わらし (座敷童 06558). Self-check: 1 notes flag applied (セラピスト: カウンセラー is not a licensed title); 10 kana links confirmed.

### 2026-11-08 (8 new entries, fifth cycle of the 12:15 run)

33125–33132. Closure: 対称的, 冥利, 定形. Brainstorm: とめどない, 海の幸, 山の幸. ezFurigana lookups: 精悍, ご清聴.
Self-check: clean; 9 kana links confirmed. New kanji 悍 added to the kanji index.

### 2026-11-08 (33 candidates queued, fourth cycle of the 12:15 run)

Candidates mode. Closure: 20 words that entries use without an entry of their own (ガス欠, 反則金, 内閣改造, 企業統治, 得失点差, 直行直帰, 先勝, 先負, …). Brainstorm (seeds 00575–00595, 足 to ちょっと): 13 of 32 vetted proposals added (大学病院, 面白半分, 国立国会図書館, 上野公園, 足が棒になる, 雪合戦, 暇人, …). Queue 396 → 429.

### 2026-11-08 (6 new entries, eighth cycle of the 00:15 run)

33119–33124. Closure: 鳥獣戯画, 北原白秋, 〜周忌. Brainstorm (appearance field): 老け顔, マッチョ. ezFurigana lookups: 〜場 (looked up as 場).
Self-check: clean (0 flags); kana links confirmed.
