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

### 2026-10-01 (Routine v3: new-entries — 8 New Entries, IDs 31369–31376)

Eight words that older entries already used, a short batch at the end of a six-cycle run: 魚釣り, 金曜, マスカット,
統計学, カシミヤ, 絵日記, 国際空港, 社会福祉. Self-check clean.

### 2026-09-30 (Interactive: homepage, audio buttons, conjugation fixes and a conjugation-check mode)

Homepage: the Browse/Kanji/Lists/Articles/Recent/Advanced link row is gone (the header has the same links),
the intro gives the number of examples with recorded audio (counted at each build), and advanced.html now
redirects to lists/index.html. Browser-speech listen buttons are removed: only examples with a recording show
the boxed 🔊 button. Conjugation tables: 乞う and 問う (乞うた, 問うた), the 行く compounds ついていく, 連れていく,
持っていく, くれる (imperative くれ), ふける, 読みふける and 見返る (godan, were ichidan), あざとかわいい, ございます,
the ずる verbs, passive headwords, and 27 stative one-kanji する verbs fixed; 恐る has no table. New
`build/check_conjugations.py` and a trigger-only `conjugation-check` Routine mode (about once a day, §D).

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

