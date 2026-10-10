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

### 2026-10-10 (Routine v3: new-entries — 5 New Entries, IDs 31870–31874)

Five internal-closure candidates in queue order, a short last cycle of the run: 大成 (two senses: 〜として大成する, and bringing a field to completion as in 集大成), 競走馬 (WATCH OUT 競走/競争), 博多 (博多駅, 博多ラーメン, Fukuoka vs Hakata), 新任 (vs 新人; WATCH OUT 信任), 紙面 (紙面を割く, 紙面の都合で). Self-check skipped (daily OpenRouter cap spent).

### 2026-10-10 (Routine v3: new-entries — 15 New Entries, IDs 31855–31869)

Fifteen internal-closure candidates that existing entries already use, in queue order: 買主 (WATCH OUT 飼い主), 熊本 (熊本城, 2016 earthquakes), 平家 (平家物語, 驕る平家は久しからず), 大勝 (vs 圧勝/完勝; homophones), 就労 (就労ビザ, 28-hour student limit), 讃岐 (讃岐うどん), 鬼ヶ島, 青森 (apples, ねぶた), 神々 (WATCH OUT 神々しい こうごうしい), 長野 (信州, 1998 Olympics), 清栄 (letter openings), 印象派, 名工 (現代の名工), 米軍 (在日米軍), 変色 (WATCH OUT 偏食). New kanji 讃 added to the kanji index. Self-check skipped (daily OpenRouter cap spent).

### 2026-10-10 (Routine v3: new-entries — 10 New Entries, IDs 31845–31854)

Ten internal-closure candidates that existing entries already use: 結婚観 (〜観 compounds), 拘禁刑 (the unified prison sentence since June 2025; WATCH OUT 懲役/禁錮), 山中 (WATCH OUT surname やまなか), 鹿児島 (薩摩, さつまいも), 浄土宗 (WATCH OUT 浄土真宗), 天照大神 (天岩戸, Ise), 赤穂浪士 (忠臣蔵, 泉岳寺), 手短 (手短に言うと), 時下 (business-letter opening), 輪島塗 (2024 Noto earthquake). A short last cycle of the run; self-check skipped (daily OpenRouter cap spent).

### 2026-10-10 (Routine v3: new-entries — 20 New Entries, IDs 31825–31844)

Twenty internal-closure candidates that existing entries already use, in queue order: 大軍 (WATCH OUT 大群), 華族 (five peerage ranks; WATCH OUT 家族), 商家, 来航 (ペリー来航), 汁粉 (Kansai vs Kanto ぜんざい), 遍路 (お接待), 私腹を肥やす (godan, conjugation table), 白物家電, 知的財産権, 最大公約数 (two senses; WATCH OUT "lowest common denominator"), 日経平均, 不要不急, 首脳会談, 日本列島, 第二次世界大戦 (太平洋戦争), 国会議事堂, 屋久島, 日本国憲法, 本能寺の変 (敵は本能寺にあり), カレーパン. Self-check skipped (daily OpenRouter cap spent).

### 2026-10-10 (Routine v3: candidates — 63 internal-closure candidates, C24263–C24325)

No noentry markers remain, so every candidate comes from a scan of example sentences for furigana-marked words that have no entry; each names the entry that uses it. Okurigana stems of existing verbs (苛立つ, 見張る, 名乗る …) and free compounds (〜後, 〜中, 〜者) were dropped after the duplicate probe. Added: everyday and news words (手短, 変色, 横行, 時効, 事情聴取, 殺処分, 土砂災害, 蝶番, 福引, 婦人科, 新婚旅行, 大勝, 大成 …), formal-letter words (時下, 清栄, 平素), and culturally weighty proper nouns (天照大神, 赤穂浪士, 平家, 法然, 菅原道真, 祇園精舎, 明治神宮, 鹿児島, 熊本, 青森, 長野, 金沢, 博多, 讃岐, 輪島塗, 備長炭). Queue 68 → 131.
