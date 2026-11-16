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

### 2026-11-16 (20 new entries, second cycle of the 00:15 UTC run)

33587–33606. Closure: 停職, 土嚢, 乱獲, 関脇, 心労, 先物, 寄生虫. Brainstorm (field body-part): あばら, 内股, 胸板, 腕っぷし, 腰回り, 膝頭, 赤毛. ezFurigana: 西ドイツ, ヒンドゥー教, フォーカス, 房, フレーバー, 物的.
Self-check: 2 fixes applied (33597: person tag removed; 33604: 乳房 was wrongly given as a "room" reading of 房); kana links clean.

### 2026-11-15 (56 candidates queued, sixth cycle of the 16:17 UTC run)

Closure 10: no noentry markers remain; a scan of unlinked words in today's polished and reviewed examples found 正気, 主格, 合板, 拘束力, 取っ組む, 居合, 隔世の感, 抗原検査, 和洋 (極まる was queued earlier in the run). Brainstorm 46 (field clothing; self 21 proposals, gpt-6.1-sol and gemini-3.8-flash 50 each; 59 new after filtering): 裾上げ, ほつれる, 毛玉, 腹巻き, パンプス, 丸首, 着丈, 着付け, 半纏, 襦袢, 襷, よそ行き, 型崩れ, 脱げる, 袂, 雨合羽, 頭巾 …; 15 rejected (variants of existing entries, kimono-specialist and fashion-jargon items). Queue 332.

### 2026-11-15 (18 new entries, fourth cycle of the 00:15 UTC run)

33569–33586. Closure: 納車, 小選挙区, 漁協, 沐浴, 神保町, アインシュタイン. Brainstorm (field body-part): 利き足, あかぎれ, ささくれ, すね毛, 指の腹, がに股. ezFurigana: 発情期, 備蓄米, 俯瞰的, 復縁, 踏み入れる, 浮遊. New kanji 沐 (02867).
Self-check: 1 clarification applied (33580: O脚 read オーきゃく); 1 kana link removed (33580: ようとして is not として).

### 2026-11-14 (12 new entries, eighth cycle of the 12:15 UTC run)

33557–33568, a short cycle at the end of the run. Closure: 家督, 工務店, 懸賞, 組曲. Brainstorm (field body-part): 口角, 目やに, 力こぶ, 犬歯. ezFurigana: 深掘り, 吹き出し, 不慣れ, 副産物. Candidate 緑化 (りょくか) dropped: entry 32041 has it as りょっか.
Self-check: clean; kana links clean.

### 2026-11-14 (36 candidates queued, seventh cycle of the 12:15 UTC run)

Closure 0: no noentry markers remain, and every bare furigana word in the examples turned out to be an existing entry. Brainstorm 36: seeds 220–260 (〜巻, 息を引き取る, 他界, 死に物狂い, 下調べ, 外面 そとづら, 追伸, 体内時計, のど飴, 駄目出し, 晴れ間, 発つ, 一番乗り …) and field business (社内報, 寿退社, 御用納め, 社員旅行); 21 rejected. Queue 306.

