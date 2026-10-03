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

### 2026-10-03 (Routine v3: new-entries — 20 New Entries, IDs 31487–31506)

Twenty words that older entries already used: 排出量, 追随, 内出血, 歯石, 肝硬変, 国家試験, 添乗員, 偽造品, 雄鶏,
雌鶏, 研修生, 巻き毛, 資本家, 二乗, 勾配, 元値, 考え事, 名優, 発言権, 本命. No new kanji. The linker connected them in
the entries where they were first seen. Candidate 浸食 dropped (variant spelling of 侵食 10927). Self-check: clean;
one kana link retargeted (なさい).

### 2026-10-03 (Routine v3: new-entries — 20 New Entries, IDs 31467–31486)

Twenty words that older entries already used: 冷や水, 違える, 吾輩, 呼び起こす, 再三再四, 取らぬ狸の皮算用,
爪弾く, 托鉢, 更ける, 身につく, 括り付ける, 無用, 受給, 信託, 非現実的, 最大化, 法人税, 敵地, 言い訳がましい,
深海魚. One new kanji (吾, 02819). Self-check: 1 applied (所得税 tag), 1 rejected.

### 2026-10-02 (Routine v3: new-entries — 20 New Entries, IDs 31447–31466)

Twenty words that older entries already used: 護憲, 狩人, サンタクロース, ばば抜き, 地下足袋, エイプリルフール,
カルチャーショック, 高官, 最古, 建国, カーソル, 屑籠, 長官, 駅長, 保育所, 朝ドラ, 脳梗塞, 社宅, 生活保護, 握り飯.
No new kanji. The linker connected 12 of them in the entries where they were first seen.
Self-check skipped (daily OpenRouter cap spent).

### 2026-10-02 (Routine v3: new-entries — 10 New Entries, IDs 31437–31446)

Ten words that older entries already used: 降り積もる, プレーヤー, レモンティー, 重金属, アンパイア, 抜け目ない,
誇り高い, 禅寺, 表面張力, 訪問販売. No new kanji. Self-check skipped (daily OpenRouter cap spent).

### 2026-10-02 (Routine v3: new-entries — 8 New Entries, IDs 31429–31436)

Eight words that older entries already used: アイスティー, レフェリー, 筏, 開場, 際どい, 弟子入り, 連邦, 紛らす.
One new kanji (筏, ID 02818). Self-check: clean.

