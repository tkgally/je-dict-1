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

### 2026-10-13 (Routine v3: new-entries — 20 New Entries, IDs 31990–32009)

All twenty are internal-closure candidates (words already used in other entries): ビート板, 酔い (two senses: drunkenness, motion sickness), 傷み (vs 痛み), 法師, 弱小, 新鋭, 収蔵 (vs 所蔵), 構内 (vs 校内), 集積回路, 集積 (vs 蓄積), 原子核, 生体, 二塁, 一級 (two senses; downward grade numbering explained), 両用 (vs 兼用), 刷る, 切らす (two senses; pair 切れる), 陰り, 火気, 両軍. 企む was dropped from the queue as a duplicate of たくらむ (07676). The new ビート板 entry fixes 09261's link, which had pointed ビート at "beat (music)". Self-check skipped: daily OpenRouter budget spent.

### 2026-10-13 (Routine v3: candidates — 22 Internal-Closure Candidates)

Every one is a word used in some entry's example but not defined anywhere: 酔い, 傷み, 法師, 弱小, 新鋭, 収蔵, 構内, 集積, 集積回路, 原子核, 生体, 二塁, 一級, 両用, 刷る, 両軍, 言行, 切らす, 陰り, 初志貫徹, 大口, 火気. About 130 words were proposed from a scan of the examples' unlinked text. Most were dropped as idioms, proper nouns or compounds that already have entries (the scan sees them inside their own entry's examples), as kanji spellings of kana headwords, or as free compounds. Queue 23 → 45.

### 2026-10-13 (Routine v3: new-entries — 19 New Entries, IDs 31971–31989)

No internal-closure candidates were left, so all nineteen came from the queue: 既約分数 (約分, 最大公約数), じゃなければ (two senses; vs でなければ, じゃないと), and seventeen proper nouns — 読売新聞, 表参道 (two senses: the Tokyo avenue and a shrine's main approach), 下北沢, 有馬温泉, 道後温泉, 卑弥呼, 平清盛, 正岡子規, 小林一茶, 与謝野晶子, 森鴎外 (new kanji 鴎, ID 02828), 古今和歌集, 羅生門, 吾輩は猫である, 走れメロス, 銀河鉄道の夜, 七人の侍. Self-check: accuracy reviewer clean; three kana-link flags (two kept, やれ in Issa's haiku unlinked and added as a candidate). Two wrong harvested cross-references (Soseki titles resolved to 心 and 坊っちゃん "young boy") reverted. Queue 40 → 22.

### 2026-10-12 (Routine v3: new-entries — 11 New Entries, IDs 31960–31970)

Five internal-closure candidates (善光寺 with 牛に引かれて善光寺参り, 徳島, 多幸 as in ご多幸をお祈りします, 本能寺 with 本能寺の変 and 敵は本能寺にあり, 遊撃手 vs ショート) and six from the queue: 信州, the proverb 案ずるより産むが易し, だとしたら, でなければ (two senses; vs でないと, さもなければ), 最小公倍数, 迷信深い. そうでないと was skipped as already covered by the でないと entry. Cross-reference harvest wrote 16 references on 14 entries. Self-check skipped (OpenRouter budget spent). Queue 51 → 40.

### 2026-10-12 (Routine v3: new-entries — 20 New Entries, IDs 31940–31959)

Twenty internal-closure candidates: 従属節 (主節), 未来永劫 (vs 永遠に, 永久に), 善玉菌 (悪玉菌), 無形文化遺産 (vs 世界遺産, 無形文化財), 問答 (two senses; 問答無用, 禅問答, 押し問答), 論語 (proper noun; sayings still in use), 所狭し (所狭しと), 大物 (two senses: big shot, big item/catch), エンディング, 斉唱 (vs 合唱), 技術力, 生産量, 浮世 (two senses; 憂き世 origin), 一人称 (私/僕/俺/うち), 反逆 (vs 反抗, 謀反), 長者 (億万長者, わらしべ長者), 入館 (vs 入場), 回答者 (WATCH OUT 回答/解答), 片足, 躍る (two senses; WRITING 躍る vs 踊る). Cross-reference harvest wrote 47 references on 35 entries. Self-check skipped (OpenRouter budget spent).

