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

### 2026-10-12 (Routine v3: new-entries — 20 New Entries, IDs 31940–31959)

Twenty internal-closure candidates: 従属節 (主節), 未来永劫 (vs 永遠に, 永久に), 善玉菌 (悪玉菌), 無形文化遺産 (vs 世界遺産, 無形文化財), 問答 (two senses; 問答無用, 禅問答, 押し問答), 論語 (proper noun; sayings still in use), 所狭し (所狭しと), 大物 (two senses: big shot, big item/catch), エンディング, 斉唱 (vs 合唱), 技術力, 生産量, 浮世 (two senses; 憂き世 origin), 一人称 (私/僕/俺/うち), 反逆 (vs 反抗, 謀反), 長者 (億万長者, わらしべ長者), 入館 (vs 入場), 回答者 (WATCH OUT 回答/解答), 片足, 躍る (two senses; WRITING 躍る vs 踊る). Cross-reference harvest wrote 47 references on 35 entries. Self-check skipped (OpenRouter budget spent).

### 2026-10-12 (Routine v3: candidates — 10 Internal-Closure Candidates)

The noentry source is empty, so this restock ran a SudachiPy scan of the unlinked text in all examples for noun, verb and adjective lemmas with no entry, then a duplicate probe on about 95 of them. Most hits were variant spellings (怪我/けが, 引っ越し/引越し, 子ども/子供) or words split out of phrase entries that already exist (思いがけない, 人見知り, 紆余曲折). Ten survived: 技術力, 生産量, 浮世, 一人称, 反逆, 長者, 入館, 回答者, 片足, 躍る, each with "seen in entry". Queue 60 → 70.

### 2026-10-12 (Routine v3: new-entries — 10 New Entries, IDs 31930–31939)

Ten internal-closure candidates, a short last cycle of the run: 黄身 (WATCH OUT 君/気味; 卵黄), 白内障 (WATCH OUT 緑内障), 売主 (vs 買主, 売り手), 隣家 (news word; お隣), 稜線 (vs 尾根), 平均寿命 (健康寿命), 書道家 (vs 書家, 習字), 文人 (文人画, 文人墨客), 頓着 (almost always negative; 無頓着), 波打つ (胸が波打つ, 波打ち際). New kanji 稜 added to the kanji index. Self-check clean.

### 2026-10-11 (Routine v3: new-entries — 20 New Entries, IDs 31910–31929)

Twenty internal-closure candidates in queue order: へたり込む (vs 座り込む), 馬術 (vs 乗馬; 障害馬術, 馬場馬術), 国際社会, 寝入る (vs 寝付く, 眠り込む), 明星 (two senses: 明けの/宵の明星, and a rising star; the 明星 poetry magazine), 過払い (過払い金 claims after the 2006 Supreme Court ruling), 脆弱性, 同社 (news-style back-reference; 同氏, 当社), 色濃い (色濃く残る), 光学 (WATCH OUT 工学, 高額), 集合写真, 保冷 (保冷剤), 病魔, 滅入る (気が滅入る), 交通手段 (vs 交通機関), 吸水性 (vs 撥水), 低金利, 浮世絵師 (絵師, 彫師, 摺師, 版元), 時期尚早, 日付変更線. The linker then linked the new words in the 20 entries that had used them. Self-check skipped (daily OpenRouter cap spent).

### 2026-10-11 (Routine v3: new-entries — 10 New Entries, IDs 31900–31909)

Ten internal-closure candidates in queue order, a short last cycle of the run: 法然 (専修念仏, 知恩院), 菅原道真 (天神, 天満宮, 飛梅), 祇園精舎 (平家物語 opening; WATCH OUT Kyoto's 祇園), 時効 (two senses: legal, and もう時効だから言うけど; 2010 abolition for murder), 忠誠心 (vs 忠誠), 事情聴取 (vs 取り調べ, 聞き込み), 創出 (雇用創出), 船乗り (vs 船員), 新婚旅行 (vs ハネムーン), 上市 (pharma launch; WATCH OUT 上司). New kanji 菅 added to the kanji index. Self-check skipped (daily OpenRouter cap spent).
