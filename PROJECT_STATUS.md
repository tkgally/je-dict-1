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

### 2026-11-14 (36 candidates queued, seventh cycle of the 12:15 UTC run)

Closure 0: no noentry markers remain, and every bare furigana word in the examples turned out to be an existing entry. Brainstorm 36: seeds 220–260 (〜巻, 息を引き取る, 他界, 死に物狂い, 下調べ, 外面 そとづら, 追伸, 体内時計, のど飴, 駄目出し, 晴れ間, 発つ, 一番乗り …) and field business (社内報, 寿退社, 御用納め, 社員旅行); 21 rejected. Queue 306.

### 2026-11-14 (20 new entries, second cycle of the 12:15 UTC run)

33537–33556. Closure: 煮えくり返る, 母屋, 仮病, 商業施設, 支援物資, 江戸幕府, 陸上自衛隊. Brainstorm: 白目, 黒目, 頭皮 (field body-part), 苦学生 (seed 学生), 日本語能力試験 (seed 日本語), 月経, 排卵 (field body-internal). ezFurigana: 昼前, 広間, ビジョン, 一幕, 封, フィンランド. Candidate 日本銀行 dropped (already entry 10141, read にっぽんぎんこう).
Self-check: 1 notes fix applied (33551: 昼前に is "before noon", not "by noon"); kana links clean.

### 2026-11-14 (6 new entries, seventh cycle of the 08:15 UTC run)

33531–33536, a short cycle at the end of the run. Closure: 手漉き, 乙姫, 作業療法士. Brainstorm (field body-internal): 精子, 羊水. ezFurigana: 人気 (ひとけ, "sign of people"; homograph of 人気 にんき).
Self-check: 1 translation fixed (33534); kana links clean.

### 2026-11-14 (43 candidates queued, third cycle of the 08:15 UTC run)

Closure 32 (words used in examples with no entry, found by scanning bare furigana words: 芭蕉, 江戸幕府, 日本銀行, 東証, 関脇, 豊洲, 肉眼, 寄生虫 …). Brainstorm field building 11 (梁, スロープ, 渡り廊下, 間仕切り, 縁の下 …); 5 rejected. Queue 297.

### 2026-11-14 (9 new entries, seventh cycle of the 00:15 UTC run)

33522–33530, a short cycle at the end of the run. Closure: ネットバンキング, 年甲斐もなく, 海上自衛隊. Brainstorm: 股, 上唇, つむじ. ezFurigana lookups: 涅槃, 如来, 羽衣. New kanji 涅, 槃.
Self-check: clean (0 of 10 flagged; 7 kana links judged, 0 flagged).

