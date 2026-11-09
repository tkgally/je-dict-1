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

### 2026-11-09 (20 new entries, fourth cycle of the 16:15 run)

33237–33256. Closure: 岩倉使節団, 人間失格, 航空自衛隊, 弘法大師, 浄土真宗, 邪馬台国, 日本書紀. Brainstorm (field art): 現代美術, 静物画, 芸術的, 下絵, 切り絵, 抽象画, 絵筆. ezFurigana lookups: 生 (せい), 側室, タウン, 単線, 端を発する, 抱き寄せる.
Self-check: 3 notes flags applied (人間失格's famous line opens the first notebook; 魏志倭人伝 the main, not only, source for 邪馬台国; タウン誌 not always free); 4 kana links removed (こく in やまとこく, ブルー in ブルーインパルス ×2, ベッド in ベッドタウン), 19 confirmed.

### 2026-11-09 (20 new entries, fourth cycle of the 08:15 run)

33217–33236. Closure: 厚労省, 第一次世界大戦, 暗礁, 汚染水, 誘因, 直毛, 毒々しい. Brainstorm: 姉さん女房, 姉御肌, 兄弟げんか, 頭を冷やす, 頭隠して尻隠さず, キャンバス, パレット. ezFurigana lookups: 造作 (ぞうさ), 絶え絶え, 類 (たぐい), たてつく, 立て膝, 単純化.
Dropped as a spelling duplicate: なで肩 (撫で肩 24257 exists). Self-check: 3 flags applied (姉御 note; two tags); 40 kana links confirmed.

### 2026-11-09 (20 new entries, first cycle of the 08:15 run)

33197–33216. Closure: 北朝鮮, 文科省, 基本的人権, 浦島太郎, 喪主, 関東大震災, 北方領土. Brainstorm: 開けっ広げ, 開け閉め, 手分け, 手取り足取り, 兄弟子, 姉妹都市, 頭ごなし. ezFurigana lookups: 宣戦布告, 線量, ソ連, 高嶺の花, たり (the 〜たり〜たりする pattern, which had no entry), 樽.
Self-check: 4 flags applied (文科省 note: the minister is 文科相; two たり contrasts with て-form and し reworded; 樽 food tag removed); 20 kana links confirmed.

### 2026-11-09 (9 new entries, seventh cycle of the 00:15 run)

33188–33196. Closure: つけっぱなし, やましい, 全壊, 真打. Brainstorm (body-internal): 盲腸, 食道, 扁桃腺. ezFurigana lookups: 体感, 対外.
Self-check: 1 notes flag applied (体幹 is the trunk, not the core muscles); 7 kana links confirmed.

### 2026-11-09 (53 candidates queued, third cycle of the 00:15 run)

Candidates mode. Closure: 24 words this run's new and polished entries name without an entry (名古屋城, 加藤清正, 西南戦争, 第三のビール, 相対性理論, 器物損壊, 全壊, 半壊, 真打, 足元をすくう, やましい, 強制送還, …). Brainstorm (field body-internal): 29 of 38 vetted proposals added (子宮, 小腸, 盲腸, 膀胱, 食道, 扁桃腺, 網膜, アキレス腱, 五臓六腑, 脳みそ, …); 9 rejected as specialized anatomy. Queue 364 → 417.

