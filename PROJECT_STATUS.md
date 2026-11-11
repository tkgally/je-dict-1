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

### 2026-11-11 (12 new entries, fifth cycle of the 00:15 run)

33357–33368. Closure: 取扱注意, 警戒態勢, 器物損壊, 量子コンピューター. Brainstorm: 芸大, 芸術祭, 雪舟 (field art), 国立国会図書館 (seed 図書館). ezFurigana lookups: でんぐり返し, 通り道, 天王山 (as 天王), 堤.
Self-check clean (no flags); one の inside なので unlinked. New candidates: 前転, 宙返り, 厳戒態勢, 割れ物.

### 2026-11-11 (20 new entries, first cycle of the 00:15 run)

33337–33356. Closure: 着回し, 雄々しい, 男心, 乙女心, 半壊, 足元をすくう, 強制送還. Brainstorm: 絵はがき, 美大, 贋作, 備前焼 (field art), 大学病院, 面白半分, ネット銀行 (seeded from 病院, 面白い, 銀行). ezFurigana lookups: てんで, 問いただす, 当該, 通り魔, 溶き卵, 遠目.
Self-check: 2 flags applied (person tag dropped from 乙女心/男心; 偽造 note reworded in 贋作); 12 kana links confirmed. New kanji 贋 added. New candidates: 着回す, 国外退去, ネットバンキング.

### 2026-11-10 (15 new entries, fifth cycle of the 16:15 run)

33322–33336. Closure: 先負, 名古屋城, 西南戦争, 相対性理論, 加藤清正. Brainstorm (field art): 信楽焼, 九谷焼, 喜多川歌麿, 太陽の塔, 東海道五十三次. ezFurigana lookups: 低賃金, 手いっぱい, 適時, 手放し, 転院.
Self-check clean (no flags; 5 kana links confirmed). New kanji 麿 added. New candidates: 大阪万博, アインシュタイン.

### 2026-11-10 (20 new entries, first cycle of the 16:15 run)

33302–33321. Closure: 定時退社, 直行直帰, 本隊, 実体経済, 旧市街, 市街戦, 先勝. Brainstorm (field art): 戯曲, 影絵, 手描き, 文鎮, 句集, ルネサンス, 伊万里焼. ezFurigana lookups: 題目, 調書, 超然, 手痛い, 手立て, てっぺん.
Self-check clean (no content flags); three として links in 超然 removed (taru-adjective と + する). Candidate 絵巻物 dropped (covered by 絵巻).

### 2026-11-10 (18 new entries, second cycle of the 08:15 run)

33284–33301. Closure: 科料, 携帯食, 犯行予告, 企業統治, 得失点差, 仕掛け花火. Brainstorm (field art): 友禅, 染物, 連作, ゴッホ, ピカソ, モザイク. ezFurigana lookups: 〜っぱなし, チューハイ, 抽象化, 痛恨, 低減, 超党派.
Self-check clean (no flags; 11 kana links confirmed). New candidates: 過料, 無念.

