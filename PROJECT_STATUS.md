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

### 2026-11-06 (8 new entries, seventh cycle of the 00:15 run)

32946–32953. Closure: 代表取締役, 極夜 (antonym of 白夜), 腰巾着. Brainstorm (appearance field): アイライン, 童顔, 坊主頭. ezFurigana lookups: 四股, 柘榴. A short cycle near the end of the run; 至近 left in the queue (至近距離 already has an entry). New kanji 柘 added to the kanji index.
Self-check: clean (0 flags on 8 entries); 1 kana link removed (について in 上司について回る is ついて回る).

### 2026-11-06 (20 new entries, first cycle of the 00:15 run)

32926–32945. Closure: 統合失調症, 大儲け, 蒸留所, 座礁, 一元化, 人工呼吸器, 人間臭い. Brainstorm: マナティー, ハクビシン, ヘラジカ (animal-mammal field), 乳母 (from 母), 遊び人 (from 遊ぶ), 総菜パン (from パン), アイシャドウ (appearance field). ezFurigana lookups: 空自, 黒人, 祭祀, 三位一体 (two senses), 材質, 四肢. Candidate 照れくさい dropped: 07134 てれくさい already covers it. New kanji 祀 added to the kanji index.
Self-check: clean (0 flags on 20 entries); 12 kana links confirmed.

### 2026-11-05 (12 new entries, sixth cycle of the 15:30 run)

32914–32925. Closure: 自衛権, 若女将, 歴史小説 (contrasted with 時代小説), 煮崩れ. Brainstorm: 丸顔, 面長 (appearance field), コッペパン (from パン), 猫可愛がり. ezFurigana lookups: グリーン (color; golf), 豪奢, ごまんと, 佐賀 (shown as 佐賀県). A short cycle near the end of the run.
Self-check: 1 flag on 17 entries, applied to the existing 長崎 entry (Dejima was the only window onto Europe, not onto all foreign countries); 15 kana links confirmed.

### 2026-11-05 (candidates restock, fourth cycle of the 15:30 run)

71 candidates added. Closure (27, words used in entries but not defined): 高裁, 家裁, 不信任案, 健勝, 番頭, 色打掛, 濃茶, 鳥獣戯画, 今場所, 写経, 親鸞, 琵琶法師, 核分裂, 本塁, 三人称, 鉄格子, 鹿鳴館, 手水舎, 落雁, 八宝菜, 下関, 北原白秋, 子猫, 百害あって一利なし, 心躍る, 熊本城, 岩倉使節団. Brainstorm (44, seeds 子供 … 頭): 父の日, 姉貴, 子供騙し, 海の幸, 山の幸, 海開き, 出来損ない, 顔負け, 女々しい, 口約束, 男勝り, 開けっ放し, 手取り足取り, 姉妹都市, 頭ごなし, 頭隠して尻隠さず and others; 7 proposals rejected (6 spelling variants of existing entries, 味付ける).

### 2026-11-05 (21 new entries, first cycle of the 15:30 run)

32893–32913. Closure: 防衛省, 負け越し, 寒中見舞い, 後ろ足, 鉤括弧, 功労者, 変幻自在. Brainstorm: 猫かぶり, 張り子の虎 (animal idioms), 家族葬 (from 家族), パンの耳 (from パン), えくぼ, やつれる, くせ毛 (appearance field). ezFurigana lookups: 教委, クラスター, 公安, 拷問, 権化, 斎場, コントローラー. New kanji 拷 and 鉤 added to the kanji index.
Self-check: 3 flags on 26 entries, all applied (a 負け越し translation, 家族葬 and 権化 notes softened); 28 kana links judged, 1 unlinked (として after a clause in 外務省).
