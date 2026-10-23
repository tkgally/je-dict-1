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

### 2026-10-23 (Routine v3: candidates — 60 words queued, C24610–C24669)

Restocked the candidate queue with 60 words the dictionary already uses in example sentences but does not define, each noted with the entry it was seen in. They came from a fresh SudachiPy scan of unlinked example text, read by hand: everyday words (前歯, 春先, 長旅, 体操服, 酔い止め, 立ち仕事, 新生児), verbs (生え変わる, 見計らう, 追いやる, 負け越す, 勝ち上がる, 垣間見える), set phrases and idioms (我を張る, 難攻不落, 異国情緒, 粒揃い), and Labor Thanksgiving Day (勤労感謝の日). Most scan hits were other spellings of existing entries (子ども, 気づく, 怪我, 可愛い …) that the linker does not link; that is logged as a tooling observation. Queue 32 → 92.

### 2026-10-22 (Routine v3: new-entries — 20 New Entries, IDs 32185–32204)

All twenty are internal-closure candidates: 一理, 便宜上, 隊員 (vs 退院), 参上, 貫徹, 発現 (vs 発言), 選り好み, 低価格, 一塁, 内覧会, 離職率, 浄水場, 縦走, 成形 (vs 整形), 管弦楽, 四重奏, 弦楽四重奏, 素因数分解, 略字, 戯画. 参上, 貫徹, 発現 and 選り好み already had separate する-verb entries; each pair now cross-references the other. Self-check: one flag on a neighbour, rejected. 32 candidates remain, 11 of them internal-closure.

### 2026-10-21 (Routine v3: new-entries — 20 New Entries, IDs 32165–32184)

All twenty are internal-closure candidates: 経口, 時候 (時候の挨拶), 色白, 黄泉, 屋形船, 長月, 松葉杖, 関白 (亭主関白), 熱情 (vs 情熱), 植わる (intransitive pair of 植える), 傍流 (vs 主流), 有期 (有期拘禁刑 since the 2025 penal reform), 傾注, 嘲弄, 各論 (総論賛成、各論反対), 干菓子, 予診, 招集 (vs 召集), 抵当権, 五穀豊穣. The harvester added reciprocal cross-references in 25 existing entries. Self-check: 1 applied, 1 rejected.

### 2026-10-21 (Routine v3: candidates — 40 words queued, C24570–C24609)

Restocked the candidate queue with 40 words the dictionary already uses in examples or notes but does not define, each noted with the entry it was seen in: 26 held back from the 2026-10-18 restock (傾注, 嘲弄, 各論, 干菓子, 予診, 招集 vs 召集, 抵当権, 五穀豊穣, 送辞, 立憲君主制, 戯画, 略字, 縦走, 成形, 管弦楽, 醸造所, 年俸制, 尺貫法, 濃口醤油, 刀鍛冶, 町奉行, 金目鯛, 四重奏, 弦楽四重奏, 素因数分解, 有期) and 14 from a fresh scan of unlinked example text (発現, 貫徹, 参上, 隊員, 芳名帳, 選り好み, 低価格, 級数, 便宜上, 一塁, 内覧会, 離職率, 浄水場, 一理). Most scan hits were spelling variants or fragments of compound entries that already exist. Queue 32 → 72.

### 2026-10-20 (Routine v3: new-entries — 20 New Entries, IDs 32145–32164)

All twenty are internal-closure candidates: 注力, 私情 (vs 市場/史上/至上), 突進, 教官, 登園, 前面 (vs 全面), 第一子, 気位, 内申書 (officially 調査書), 不測 (vs 不足), 催事, 盗掘, 霊前 (御霊前 vs 御仏前), 受験者 (vs 受験生), 手水, 薄茶, 悪玉菌, 財源, 国営 (NHK is not state broadcasting), 民営. The candidate しわ寄せ was dropped as a duplicate of 皺寄せ. Self-check: one flag on a neighbour, applied (資金 tagged formal); one kana link kept. 32 candidates remain.

