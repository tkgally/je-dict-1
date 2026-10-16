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

### 2026-10-16 (Routine v3: new-entries — 12 New Entries, IDs 32052–32063)

All twelve are internal-closure candidates: 同族, 野性 (vs 野生), 過大, 接着, 優待 (株主優待), 養護, 理容 (vs 床屋, 美容), 格子, 悪性 (vs 良性, 悪質), 適格 (vs 的確), 先々 (two senses: the future; 行く先々で), 果て. A smaller batch than usual because this was the run's fourth cycle. Homophone cross-references were added for 野性/野生 and 適格/的確. Self-check: 0 accuracy flags on 12 entries, 0 kana-link flags. 70 candidates remain.

### 2026-10-16 (Routine v3: new-entries — 22 New Entries, IDs 32030–32051)

All twenty-two are internal-closure candidates (words already used in other entries): やれ (two senses: "hey!"; やれ X だ、やれ Y だ), 不燃, 雌雄 (incl. 雌雄を決する), 総長, 在外, 引き揚げる (withdraw; be repatriated; salvage — distinguished from 引き上げる), 合皮, 手指, 恥じらい, 弾道, 出生届, 緑化, 歌劇団, 菜種油, 婿養子, 半濁点, 追究 (vs 追及, 追求), 盲目的, 縁取る, 先駆ける, 詰め替える, 人称. Self-check: 0 accuracy flags on 33 entries; one kana-link flag rejected (ながら). 81 candidates remain.

### 2026-10-15 (Routine v3: candidates — 60 Internal-Closure Candidates)

The noentry list is still empty, so this run scanned the unlinked text of every entry's notes and examples (SudachiPy lemmas with kanji that match no headword or candidate), ranks 1–750. Sixty words the dictionary uses but never defined, for example 人称, 野性 (vs 野生), 過大, 優待, 養護, 格子, 不通, 悪性, 心肺, 適格, 道楽, 先々, 果て, 心筋, 既得権, 縁故, 因数, 首長, 立法, 家庭裁判所, 原子力発電所, 御用達, 胃もたれ, 川下, 戒名, 満期, 拒否権, 感嘆符, 受信料, 土石流, 殿下, 規制緩和, 震源地, 液状化, むき出し, 模擬店, 自惚れる, 決する, 子爵, 真っ向. About 300 hits were dropped: exact duplicates, spelling variants (売り上げ/売上, 名字/苗字, 手がかり/手掛かり …), and fragments of set phrases that already have entries (否応なく, 物心つく, 余儀なく, 肩身が狭い …). Queue 42 → 102.

### 2026-10-14 (Routine v3: new-entries — 20 New Entries, IDs 32010–32029)

All twenty are internal-closure candidates: 言行 (vs 言動), 初志貫徹, 大口 (two senses: big talk; large-lot orders), 連濁, 入管, 前略, 草々, 発砲, 統率力, 学界 (vs 学会), 邦人, 高等裁判所, 有人 (vs 無人), 侯爵 (new kanji 侯, ID 02829), 中層 (three senses), 起立, 修了証, 場内, 破裂音 (two senses), 感知器. Two wrong harvested cross-references (パン "bread" and バン "van" from a "pop, bang" bullet) were reverted. Self-check: two reviewer flags on neighbours, both rejected; one kana link (なさい) retargeted. Queue 62 → 42.

### 2026-10-13 (Routine v3: candidates — 37 Internal-Closure Candidates)

The noentry list is empty and the example scan is exhausted, so this run scanned the unlinked text of every entry's notes (SudachiPy lemmas with kanji that match no headword). Thirty-seven words the notes use but the dictionary never defined: 連濁, 半濁点, 破裂音, 前略, 草々, 起立, 入管, 邦人, 在外, 高等裁判所, 発砲, 弾道, 学界 (vs 学会), 追究 (vs 追及, 追求), 引き揚げる (vs 引き上げる), 有人, 侯爵, 総長, 婿養子, 出生届, 修了証, 場内, 感知器, 不燃, 雌雄, 中層, 統率力, 合皮, 手指, 恥じらい, 緑化, 歌劇団, 菜種油, 盲目的, 縁取る, 先駆ける, 詰め替える. Dropped as variants: 税込み, 税抜き, 挽き肉, 雛祭り, 寝巻き, 人混み, 空っぽ, 折りたたむ, 引き落とし, 純米酒. Found on the way: ひき肉 (17241) and 挽肉 (14783) are duplicate entries (flagged for the curator).
