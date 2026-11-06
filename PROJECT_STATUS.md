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

### 2026-11-06 (21 new entries, fourth cycle of the 12:15 run)

32982–33002. Closure: はみ出し者, 借り物競走, 女友達, よじ登る, ユーカリ, 蘭学, 出島, 負け組. Brainstorm (appearance field): 分け目, 切れ長, 刈り上げ, 団子鼻, 垂れ目, 枝毛, 短髪. ezFurigana lookups: 主眼, 主軸, 所感, 所長, 周遊, 職人技.
Self-check: clean (0 flags on 21 entries); 14 kana links confirmed.

### 2026-11-06 (80 candidates added, first cycle of the 12:15 run)

Closure (34, from words used in entries 31000+ without an entry): 鎌倉幕府, 室町幕府, 日本書紀, 関東大震災, 第一次世界大戦, 北方領土, 基本的人権, 教育委員会, 文科省, 厚労省, 被爆者, 喪主, 暗礁 and others. Brainstorm (art field, 46): キャンバス, パレット, 静物画, 自画像, 下絵, 蒔絵, 九谷焼, 備前焼, 雪舟, 尾形光琳, ゴッホ, ピカソ, 美大, 贋作 and others; 7 rejected. Queue 451 → 531.

### 2026-11-06 (8 new entries, sixth cycle of the 08:50 run)

32974–32981. Closure: 岩手山, 起立採決, はみ出す, ガリ勉, 読書家. Brainstorm (appearance field): チーク, ムキムキ. ezFurigana lookup: 清水 (with a warning that 清水寺 and 清水の舞台 read きよみず). A short cycle at the end of the run.
Self-check: 1 flag applied (大の読書家 reads だいの); 7 kana links confirmed.

### 2026-11-06 (20 new entries, third cycle of the 08:50 run)

32954–32973. Closure: ありあり, のしかかる, わんこそば, 南部鉄器, 中尊寺 (all three from 岩手), 無記名投票, 第一声. Brainstorm (appearance field): ルックス, 若作り, 隈, おかっぱ, ぱっちり, 二重あご, つり目. ezFurigana lookups: 至近, 私大, 使途, 酌, 謝辞, 車中泊.
Self-check: 1 flag applied (中尊寺 was founded in 850, not the 12th century); 2 kana links removed (として in a quotative, わら in 座敷わらし).

### 2026-11-06 (8 new entries, seventh cycle of the 00:15 run)

32946–32953. Closure: 代表取締役, 極夜 (antonym of 白夜), 腰巾着. Brainstorm (appearance field): アイライン, 童顔, 坊主頭. ezFurigana lookups: 四股, 柘榴. A short cycle near the end of the run; 至近 left in the queue (至近距離 already has an entry). New kanji 柘 added to the kanji index.
Self-check: clean (0 flags on 8 entries); 1 kana link removed (について in 上司について回る is ついて回る).

