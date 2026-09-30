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

### 2026-09-30 (Routine v3: new-entries — 20 New Entries, IDs 31349–31368)

Twenty more words that older entries already used: スクール, ピンからキリまで, そっくりさん, 交じり, 仕事着, the affixes 〜権 and 脱〜,
クロワッサン, フランスパン, チャリンコ, 二つ折り, 開き戸, ベレー帽, 忌み数, シャトルバス, 低脂肪, 正答, 盛り塩, 流砂, ティースプーン.
No new kanji. Self-check skipped: the day's OpenRouter budget was spent.

### 2026-09-30 (Routine v3: new-entries — 20 New Entries, IDs 31329–31348)

Twenty words that older entries already used but never defined: デスクワーク, スポーツカー, 南緯, ホーロー, マシン,
the six Kanto prefectures around Tokyo 千葉, 神奈川, 埼玉, 栃木, 群馬, 茨城, plus 滋賀 and 湘南, ソファベッド, フィーリング, ヘアピン,
王政, パイプライン, 居宅, ニス. New kanji 埼, 栃, 湘, 茨 (02814–02817). Self-check skipped: the day's OpenRouter budget was spent.

### 2026-09-30 (Routine v3: new-entries — 20 New Entries, IDs 31309–31328)

Twenty words that older entries already used but never defined: 創出する, 保養所, 大草原, ブロガー, 赤蜻蛉, エコカー,
ライブハウス, ジグソーパズル, 控訴審, 独裁的, オリオン座, 競艇, 情報化, マスカラ, ハンドクリーム, サワークリーム,
ホイップクリーム, フレグランス, アロマ, スポーツマン. Three older "no entry" markers now link to them (in 控訴, 独裁 and 星座).
New kanji 艇 (02813). Self-check skipped: the day's OpenRouter budget was spent.

### 2026-09-30 (Routine v3: new-entries — 9 New Entries, IDs 31300–31308)

Nine words that older entries used inside stripped `noentry` markers (block 04000–04499, cycle 2 of this run):
総選挙, 年輪, 樹皮, 超音波, 太字, 触角, 編集長, 人体, 家庭科. 触角 carries a WATCH OUT against its homophone 触覚 and
a see-also to it. Stale candidate 狸寝入り removed (exists as タヌキ寝入り 24457). No new kanji. Kept to nine because
the run clock was near its end. Self-check clean.

### 2026-09-29 (Routine v3: new-entries — 10 New Entries, IDs 31290–31299)

Ten words that older entries used inside stripped `noentry` markers: お古, どっちつかず, 大損, 出し合う, 勤め人, 印紙,
司法試験, 形容動詞, 語幹, 空豆. Reciprocal cross-references added on eleven neighbours (活用, 会社員, 弁護士, 中古, 損失,
サラリーマン, 曖昧, 中途半端, 語尾, 自営業, 枝豆). No new kanji. Kept to ten because the run clock was near its end.
Self-check skipped: the day's OpenRouter budget was spent.

