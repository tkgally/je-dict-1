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

### 2026-10-18 (Routine v3: candidates — 60 Internal-Closure Candidates)

Source 1 (noentry markers) is empty. Added the 29 probe-clean words the 2026-10-15 run held back (不信任, 舞踏会, 管制, 貸主, 共犯者, 簡易裁判所, 杜氏, 養子縁組, 合同会社, 文語体, …) and 31 more from a fresh scan of unlinked example and notes text (感服, 注力, 私情, しわ寄せ, 登園, 気位, 内申書, 不測, 催事, 手水, 悪玉菌, 財源, 国営, 民営, 経口, 時候, 色白, 黄泉, 屋形船, 松葉杖, 関白, …), all "seen in entry NNNNN". Most high-frequency scan hits are fragments of compounds that already have entries (交感 in 交感神経, 机上 in 机上の空論). C24508–C24567.

### 2026-10-17 (Routine v3: new-entries — 20 New Entries, IDs 32064–32083)

All twenty are internal-closure candidates: 不通 (vs 普通), 心肺, 攪拌, 同質, 道楽 (two senses: hobby; dissipation), 常用 (常用漢字), 心筋, 既得権, 縁故, 表出, 因数, 増補, 首長 (also said くびちょう), 必携, 全権, 反戦, 電化, 弦楽, 均質 (vs 同質), 不相応. 同質 and 均質 point at each other. Self-check skipped: the day's OpenRouter budget was spent by earlier cycles. 50 candidates remain.

### 2026-10-16 (Routine v3: new-entries — 12 New Entries, IDs 32052–32063)

All twelve are internal-closure candidates: 同族, 野性 (vs 野生), 過大, 接着, 優待 (株主優待), 養護, 理容 (vs 床屋, 美容), 格子, 悪性 (vs 良性, 悪質), 適格 (vs 的確), 先々 (two senses: the future; 行く先々で), 果て. A smaller batch than usual because this was the run's fourth cycle. Homophone cross-references were added for 野性/野生 and 適格/的確. Self-check: 0 accuracy flags on 12 entries, 0 kana-link flags. 70 candidates remain.

### 2026-10-16 (Routine v3: new-entries — 22 New Entries, IDs 32030–32051)

All twenty-two are internal-closure candidates (words already used in other entries): やれ (two senses: "hey!"; やれ X だ、やれ Y だ), 不燃, 雌雄 (incl. 雌雄を決する), 総長, 在外, 引き揚げる (withdraw; be repatriated; salvage — distinguished from 引き上げる), 合皮, 手指, 恥じらい, 弾道, 出生届, 緑化, 歌劇団, 菜種油, 婿養子, 半濁点, 追究 (vs 追及, 追求), 盲目的, 縁取る, 先駆ける, 詰め替える, 人称. Self-check: 0 accuracy flags on 33 entries; one kana-link flag rejected (ながら). 81 candidates remain.

### 2026-10-15 (Routine v3: candidates — 60 Internal-Closure Candidates)

The noentry list is still empty, so this run scanned the unlinked text of every entry's notes and examples (SudachiPy lemmas with kanji that match no headword or candidate), ranks 1–750. Sixty words the dictionary uses but never defined, for example 人称, 野性 (vs 野生), 過大, 優待, 養護, 格子, 不通, 悪性, 心肺, 適格, 道楽, 先々, 果て, 心筋, 既得権, 縁故, 因数, 首長, 立法, 家庭裁判所, 原子力発電所, 御用達, 胃もたれ, 川下, 戒名, 満期, 拒否権, 感嘆符, 受信料, 土石流, 殿下, 規制緩和, 震源地, 液状化, むき出し, 模擬店, 自惚れる, 決する, 子爵, 真っ向. About 300 hits were dropped: exact duplicates, spelling variants (売り上げ/売上, 名字/苗字, 手がかり/手掛かり …), and fragments of set phrases that already have entries (否応なく, 物心つく, 余儀なく, 肩身が狭い …). Queue 42 → 102.

