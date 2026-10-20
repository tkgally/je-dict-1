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

### 2026-10-20 (Routine v3: new-entries — 20 New Entries, IDs 32145–32164)

All twenty are internal-closure candidates: 注力, 私情 (vs 市場/史上/至上), 突進, 教官, 登園, 前面 (vs 全面), 第一子, 気位, 内申書 (officially 調査書), 不測 (vs 不足), 催事, 盗掘, 霊前 (御霊前 vs 御仏前), 受験者 (vs 受験生), 手水, 薄茶, 悪玉菌, 財源, 国営 (NHK is not state broadcasting), 民営. The candidate しわ寄せ was dropped as a duplicate of 皺寄せ. Self-check: one flag on a neighbour, applied (資金 tagged formal); one kana link kept. 32 candidates remain.

### 2026-10-19 (Routine v3: new-entries — 20 New Entries, IDs 32125–32144)

All twenty are internal-closure candidates: 固定資産税, 浄水 (vs 上水), 杜氏, 培養, 模造品, 廃刊 (vs 休刊), 丁稚, 求刑, 能動態, 養子縁組, 醸造酒 (vs 蒸留酒), 自助, 公助 (the 自助・共助・公助 slogan), 無双 (literary and slang uses), 法定 (vs 法廷), 合同会社, 社名, 打掛, 文語体, 感服. Self-check: 0 accuracy flags; one kana link (なさい) retargeted from なさる to the なさい entry. 52 candidates remain.

### 2026-10-19 (Routine v3: new-entries — 20 New Entries, IDs 32105–32124)

All twenty are internal-closure candidates: 規制緩和, 震源地 (two senses: epicenter; source of a rumor or trend; notes give 震源 vs 震央), 液状化, むき出し (two senses: bare; undisguised), 模擬店, 乳酸菌, 日本三景 (proper noun, place), 春闘, 丸め込む, 黒歴史, 不信任, 舞踏会, 管制, 貸主, 共犯者, 簡易裁判所, 低所得, 不凍液, 製糸, 鉄器. Self-check: one flag, rejected (the model misread the 震源地 note); the note was reworded anyway to name 震央.

### 2026-10-18 (Routine v3: new-entries — 21 New Entries, IDs 32084–32104)

All twenty-one are internal-closure candidates: 西陣織 (proper noun, brand), 概括, 壁掛け, 自惚れる, 決する (notes separate 意を決して from the adverb 決して), 子爵 (with the five peerage ranks), 真っ向, 攻勢 (vs 守勢), 立法, 家庭裁判所, 原子力発電所 (short form 原発), 御用達, 胃もたれ, 川下, 戒名, 満期 (vs 満了), 拒否権, 感嘆符, 受信料, 土石流, 殿下 (vs 陛下). Self-check: 0 accuracy flags on 42 entries (the new ones plus the 21 that gained reciprocal cross-references), 0 kana-link flags. 91 candidates remain.

### 2026-10-18 (Routine v3: candidates — 60 Internal-Closure Candidates)

Source 1 (noentry markers) is empty. Added the 29 probe-clean words the 2026-10-15 run held back (不信任, 舞踏会, 管制, 貸主, 共犯者, 簡易裁判所, 杜氏, 養子縁組, 合同会社, 文語体, …) and 31 more from a fresh scan of unlinked example and notes text (感服, 注力, 私情, しわ寄せ, 登園, 気位, 内申書, 不測, 催事, 手水, 悪玉菌, 財源, 国営, 民営, 経口, 時候, 色白, 黄泉, 屋形船, 松葉杖, 関白, …), all "seen in entry NNNNN". Most high-frequency scan hits are fragments of compounds that already have entries (交感 in 交感神経, 机上 in 机上の空論). C24508–C24567.

