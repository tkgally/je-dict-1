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

### 2026-11-08 (6 new entries, eighth cycle of the 00:15 run)

33119–33124. Closure: 鳥獣戯画, 北原白秋, 〜周忌. Brainstorm (appearance field): 老け顔, マッチョ. ezFurigana lookups: 〜場 (looked up as 場).
Self-check: clean (0 flags); kana links confirmed.

### 2026-11-08 (12 new entries, sixth cycle of the 00:15 run)

33107–33118. Closure: 下関, 琵琶法師, 鹿鳴館, やれやれ. Brainstorm: 父子, 子供心, 妹分, 猫っ毛. ezFurigana lookups: 薩摩, 殉教, 色即是空, スロー. New kanji 殉, 薩 added to the kanji index.
Self-check: 3 flags applied (関門 joins 下関's 関 and 門司's 門, also fixed in 14573; Dan-no-ura is the Heike's climax; 子供心 not a person); 19 kana links confirmed.

### 2026-11-08 (20 new entries, third cycle of the 00:15 run)

33087–33106. Closure: 鉄格子, 心躍る, 手水舎, 落雁, 八宝菜, 三人称, 百害あって一利なし (子猫 dropped: 仔猫 24479 already covers it). Brainstorm: 手に取る, 口を出す, 開け放す, 子供扱い, 子供騙し, 海の家, 白髪交じり. ezFurigana lookups: 素通り, すり減らす, ずんぐり, ステッカー, 実弾, 従者.
Self-check: clean (0 flags); 11 kana links confirmed.

### 2026-11-07 (12 new entries, fourth cycle of the 12:15 run)

33075–33086. Closure: カツオのたたき, 色打掛, 核分裂, 本塁. Brainstorm: 絵になる, 見違える (appearance field), 父の日, 姉貴. ezFurigana lookups: 重症化, 常備薬, 助産師 (looked up as 助産婦), 尋常.
Self-check: 1 flag applied (異常 is not always negative); 8 kana links confirmed.

### 2026-11-07 (20 new entries, first cycle of the 12:15 run)

33055–33074. Closure: ダッシュ, 健勝, 番頭, 濃茶, 今場所, 写経, 親鸞. Brainstorm (appearance field): ヘアスタイル, 小綺麗, 彫りが深い, 恰幅, 様になる, 無精ひげ, 目鼻立ち. ezFurigana lookups: ショット, シンガポール, 実験的, 邪念, ジャーナリスト, 重軽傷.
Self-check: 3 flags applied (初日 read しょにち; 健勝 claim softened; 恰幅 not a body part); 25 kana links confirmed.

