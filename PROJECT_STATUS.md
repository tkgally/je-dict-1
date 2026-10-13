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

### 2026-10-13 (Routine v3: new-entries — 19 New Entries, IDs 31971–31989)

No internal-closure candidates were left, so all nineteen came from the queue: 既約分数 (約分, 最大公約数), じゃなければ (two senses; vs でなければ, じゃないと), and seventeen proper nouns — 読売新聞, 表参道 (two senses: the Tokyo avenue and a shrine's main approach), 下北沢, 有馬温泉, 道後温泉, 卑弥呼, 平清盛, 正岡子規, 小林一茶, 与謝野晶子, 森鴎外 (new kanji 鴎, ID 02828), 古今和歌集, 羅生門, 吾輩は猫である, 走れメロス, 銀河鉄道の夜, 七人の侍. Self-check: accuracy reviewer clean; three kana-link flags (two kept, やれ in Issa's haiku unlinked and added as a candidate). Two wrong harvested cross-references (Soseki titles resolved to 心 and 坊っちゃん "young boy") reverted. Queue 40 → 22.

### 2026-10-12 (Routine v3: new-entries — 11 New Entries, IDs 31960–31970)

Five internal-closure candidates (善光寺 with 牛に引かれて善光寺参り, 徳島, 多幸 as in ご多幸をお祈りします, 本能寺 with 本能寺の変 and 敵は本能寺にあり, 遊撃手 vs ショート) and six from the queue: 信州, the proverb 案ずるより産むが易し, だとしたら, でなければ (two senses; vs でないと, さもなければ), 最小公倍数, 迷信深い. そうでないと was skipped as already covered by the でないと entry. Cross-reference harvest wrote 16 references on 14 entries. Self-check skipped (OpenRouter budget spent). Queue 51 → 40.

### 2026-10-12 (Routine v3: new-entries — 20 New Entries, IDs 31940–31959)

Twenty internal-closure candidates: 従属節 (主節), 未来永劫 (vs 永遠に, 永久に), 善玉菌 (悪玉菌), 無形文化遺産 (vs 世界遺産, 無形文化財), 問答 (two senses; 問答無用, 禅問答, 押し問答), 論語 (proper noun; sayings still in use), 所狭し (所狭しと), 大物 (two senses: big shot, big item/catch), エンディング, 斉唱 (vs 合唱), 技術力, 生産量, 浮世 (two senses; 憂き世 origin), 一人称 (私/僕/俺/うち), 反逆 (vs 反抗, 謀反), 長者 (億万長者, わらしべ長者), 入館 (vs 入場), 回答者 (WATCH OUT 回答/解答), 片足, 躍る (two senses; WRITING 躍る vs 踊る). Cross-reference harvest wrote 47 references on 35 entries. Self-check skipped (OpenRouter budget spent).

### 2026-10-12 (Routine v3: candidates — 10 Internal-Closure Candidates)

The noentry source is empty, so this restock ran a SudachiPy scan of the unlinked text in all examples for noun, verb and adjective lemmas with no entry, then a duplicate probe on about 95 of them. Most hits were variant spellings (怪我/けが, 引っ越し/引越し, 子ども/子供) or words split out of phrase entries that already exist (思いがけない, 人見知り, 紆余曲折). Ten survived: 技術力, 生産量, 浮世, 一人称, 反逆, 長者, 入館, 回答者, 片足, 躍る, each with "seen in entry". Queue 60 → 70.

### 2026-10-12 (Routine v3: new-entries — 10 New Entries, IDs 31930–31939)

Ten internal-closure candidates, a short last cycle of the run: 黄身 (WATCH OUT 君/気味; 卵黄), 白内障 (WATCH OUT 緑内障), 売主 (vs 買主, 売り手), 隣家 (news word; お隣), 稜線 (vs 尾根), 平均寿命 (健康寿命), 書道家 (vs 書家, 習字), 文人 (文人画, 文人墨客), 頓着 (almost always negative; 無頓着), 波打つ (胸が波打つ, 波打ち際). New kanji 稜 added to the kanji index. Self-check clean.
