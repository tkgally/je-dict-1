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

### 2026-11-10 (9 new entries, seventh cycle of the 00:15 run)

33275–33283. Closure: 雲水, 改革者, 反則金. Brainstorm (field art): 蒔絵, グラデーション, コラージュ. ezFurigana lookups: 大韓民国, ダイレクト, 乳房. Self-check clean (no flags; 6 kana links confirmed).

### 2026-11-10 (18 new entries, fourth cycle of the 00:15 run)

33257–33274. Closure: 反原発, 菩薩, ガス欠, 内閣改造, 禅問答, 殺気. Brainstorm (field art): 自画像, イーゼル, 墨絵, 木版画, クレヨン, ステンドグラス. ezFurigana lookups: 暖色, 地球儀, 地裁, 血なまぐさい, お茶目 (as 茶目), 力技 (as 力業).
Self-check: 1 flag rejected (イーゼル's source word); 8 kana links confirmed. New kanji 菩 added to the kanji index.

### 2026-11-10 (candidate restock, first cycle of the 00:15 run)

90 candidates added (queue 351 → 441). Closure (36, words used in entries 33150–33256 with no entry): 岩倉具視, 大久保利通, 木戸孝允, 魏志倭人伝, 竜宮城, 玉手箱, 土俵際, 国民主権, 陸上自衛隊, 海上自衛隊, 仮設住宅, 弘法にも筆の誤り, …. Brainstorm, seeds 少し–上がる (17): 山ほど, いささか, 年がら年中, ずる休み, 時は金なり, 金に糸目をつけない, 繰り上がる, …; field body-part (37): 奥歯, 耳たぶ, つむじ, 乳歯, 白目, 口角, 涙袋, 鼻の下, ….

### 2026-11-09 (20 new entries, fourth cycle of the 16:15 run)

33237–33256. Closure: 岩倉使節団, 人間失格, 航空自衛隊, 弘法大師, 浄土真宗, 邪馬台国, 日本書紀. Brainstorm (field art): 現代美術, 静物画, 芸術的, 下絵, 切り絵, 抽象画, 絵筆. ezFurigana lookups: 生 (せい), 側室, タウン, 単線, 端を発する, 抱き寄せる.
Self-check: 3 notes flags applied (人間失格's famous line opens the first notebook; 魏志倭人伝 the main, not only, source for 邪馬台国; タウン誌 not always free); 4 kana links removed (こく in やまとこく, ブルー in ブルーインパルス ×2, ベッド in ベッドタウン), 19 confirmed.

### 2026-11-09 (20 new entries, fourth cycle of the 08:15 run)

33217–33236. Closure: 厚労省, 第一次世界大戦, 暗礁, 汚染水, 誘因, 直毛, 毒々しい. Brainstorm: 姉さん女房, 姉御肌, 兄弟げんか, 頭を冷やす, 頭隠して尻隠さず, キャンバス, パレット. ezFurigana lookups: 造作 (ぞうさ), 絶え絶え, 類 (たぐい), たてつく, 立て膝, 単純化.
Dropped as a spelling duplicate: なで肩 (撫で肩 24257 exists). Self-check: 3 flags applied (姉御 note; two tags); 40 kana links confirmed.

