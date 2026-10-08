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

### 2026-10-08 (Routine v3: new-entries — 20 New Entries, IDs 31718–31737)

Twenty internal-closure candidates that existing entries already use: 賠償金, 振りまく (two senses), 計り知れない (i-adjective), 合否, 無作為, 釣り糸, 立ち込める, 絡み合う (two senses), 育て上げる, 切り立つ, 木目, 街中, 駄菓子屋, 奪い返す, 問題視 (noun + する), 危機感, 吹きこぼれる, 健康的, 断り (two senses), 科する (contrasted with 課する, now a candidate). Conjugation tables added for the nine verbs and the adjective. The source entries were relinked (23 new inline links). The cross-reference harvester wrongly tied 科する to 課 (lesson); reverted. Self-check clean on the new entries.

### 2026-10-07 (Routine v3: new-entries — 20 New Entries, IDs 31698–31717)

Twenty internal-closure candidates that existing entries already use: 投資信託, 術 (すべ, as in 為す術がない), こどもの日 (proper noun, event), 策定 and 加担 (noun + する), 人通り, 審議会, 驚異的 (na-adjective), 糧 (two senses), 南部, 象牙, 民間人, 第一線, 厚み (two senses), 猛攻, 解脱 (noun + する); the verbs 覗き込む, 切り込む and 滅ぶ (conjugation tables added; 滅ぶ paired with 滅ぼす and 滅びる); 手早い (i-adjective, table added). 蜉蝣 was dropped from the queue as a variant spelling of the existing 蜻蛉 (かげろう). The source entries were relinked (25 new inline links). No new kanji; no stale markers or newcomer link ambiguities. Self-check skipped: the day's OpenRouter cap was spent.

### 2026-10-07 (Routine v3: candidates — 60 Internal-Closure Candidates, C24092–C24175)

The same SudachiPy scan of the examples' unlinked text for kanji words with no entry (the stale-noentry source is still empty). 110 proposed; the duplicate probe dropped 読み聞かせ and 17 variant spellings of existing entries (歯ごたえ, 寄りかかる, 肩こり, 折りたたむ, 生ごみ, 改ざん, 子猫 …); transparent compounds (合格者, 手術室, 緊急時 …) and 24 lower-value words were left out. 60 added, each with the entry it was seen in (策定, 人通り, 危機感, 覗き込む, 浪士, 志士, 被爆, 陽性 …). Queue 50 → 110.

### 2026-10-07 (Routine v3: new-entries — 20 New Entries, IDs 31678–31697)

Twenty internal-closure candidates that existing entries already use: 面持ち, 大仏, 選手団, 遺品, 文末, 黙秘権, 海峡, 流れ着く and 度重なる (godan verbs, conjugation tables added), 北上 and 飛来 (noun + する), 昨年度, 登山家, 冬山, 家族連れ, 作曲家, 耐性菌, 表書き, 仕打ち, 頭部. No new kanji; no stale markers or newcomer link ambiguities. Self-check skipped: the day's OpenRouter cap was spent. Four internal-closure candidates remain (投資信託, 術 (すべ), 蜉蝣, こどもの日).

### 2026-10-07 (Routine v3: new-entries — 20 New Entries, IDs 31658–31677)

Twenty internal-closure candidates that existing entries already use: 落札 (noun + する), 悪霊, 少子高齢化, 海岸線, 専門医, 最高裁 (proper noun), 受刑者, 通学路, 与野党, 雑貨屋, 客先, 三塁, 南国, 肖像, 戦車; the verbs 酔っぱらう, 立ち尽くす, 吹きかける, 手向ける, 持ち越す (conjugation tables added). The twenty entries that mentioned these words were relinked (27 new inline links). No new kanji, stale markers or newcomer link ambiguities. Self-check: no issues. 23 internal-closure candidates remain.

