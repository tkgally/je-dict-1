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

### 2026-11-12 (20 new entries, second cycle of the 00:15 run)

33440–33459. Closure: 八十八箇所, 南無阿弥陀仏, 本願寺, 人物画, 魏志倭人伝, 岩倉具視, 大久保利通. Brainstorm: 網膜, 角膜, 血流, はらわた, アキレス腱, 五臓六腑, 脳みそ (field body-internal). ezFurigana lookups: 生半可, 難産, いつ何時 (as 何時), 肉親, にして, 日本的.
Self-check: 1 flag applied (the Book of Han mentions Wa before the Gishi Wajinden). New kanji 倭, 魏 added. Cycle 1 (polish) retired 16888 振付 as a spelling duplicate of 12880 振り付け.

### 2026-11-11 (candidates: 36 brainstorm candidates, ninth cycle of the 16:15 run)

Field brand-name: 20 own proposals, 50 from gpt-6.1-sol, 50 from gemini-3.8-flash; 10 already entries, 63 vetted, 36 added (Suica, PASMO, ダイソー, ローソン, ファミリーマート, 吉野家, ケンタッキー, マクドナルド, 楽天, メルカリ, ペイペイ, and generic trademarks ウォシュレット, サランラップ, シーチキン, バンドエイド, マジックテープ, プリクラ, …), 27 rejected (foreign brands of little weight, Latin-script duplicates, dated). No unresolved noentry markers; no ezFurigana rows pending. Queue 330.

### 2026-11-11 (14 new entries, sixth cycle of the 16:15 run)

33426–33439. Closure: 具象画, 弘法にも筆の誤り, 二世, 対外的, 美声, 親分肌. Brainstorm: 卵巣, 胎盤, 腱, 卵子 (field body-internal). ezFurigana lookups: とする (as とされる), チープ, 毒見, 慟哭.
Self-check: 4 flags applied (日系二世 is not an emigrant; 腱鞘炎 is tenosynovitis). New kanji 慟, 哭, 腱 added.

### 2026-11-11 (19 new entries, third cycle of the 16:15 run)

33407–33425. Closure: 体感温度, 失敗作, 姉妹校, 弟弟子, 仮設住宅, 天地, 正室. Brainstorm: 胃酸, 大脳, 小脳, 肺活量, 頭蓋骨, 血栓 (field body-internal). ezFurigana lookups: ないといけない, 同額, 同郷, 長丁場, 生々しい, なおざり.
Self-check: 1 flag applied (体感温度 translation); in ないといけない, links from the auxiliary ない to the adjective ない removed and なきゃ retargeted to its own entry.

### 2026-11-11 (18 new entries, sixth cycle of the 08:15 run)

33389–33406. Closure: 対向車, 面倒見, 開祖, 抑留, 美的, 姉御. Brainstorm: 移動図書館 (seed 図書館), 子宮, 小腸, 尿, 膀胱, 気管支 (field body-internal). ezFurigana lookups: 党, 取り巻く, とんと, ドアノブ, 恫喝, トリガー.
Self-check: 1 flag applied (拘留 vs 勾留 in 抑留); 2 kana links removed (やってくる, 困ったことがある). New kanji 恫, 膀, 胱 added.
