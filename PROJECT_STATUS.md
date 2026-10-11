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

### 2026-10-11 (Routine v3: new-entries — 20 New Entries, IDs 31910–31929)

Twenty internal-closure candidates in queue order: へたり込む (vs 座り込む), 馬術 (vs 乗馬; 障害馬術, 馬場馬術), 国際社会, 寝入る (vs 寝付く, 眠り込む), 明星 (two senses: 明けの/宵の明星, and a rising star; the 明星 poetry magazine), 過払い (過払い金 claims after the 2006 Supreme Court ruling), 脆弱性, 同社 (news-style back-reference; 同氏, 当社), 色濃い (色濃く残る), 光学 (WATCH OUT 工学, 高額), 集合写真, 保冷 (保冷剤), 病魔, 滅入る (気が滅入る), 交通手段 (vs 交通機関), 吸水性 (vs 撥水), 低金利, 浮世絵師 (絵師, 彫師, 摺師, 版元), 時期尚早, 日付変更線. The linker then linked the new words in the 20 entries that had used them. Self-check skipped (daily OpenRouter cap spent).

### 2026-10-11 (Routine v3: new-entries — 10 New Entries, IDs 31900–31909)

Ten internal-closure candidates in queue order, a short last cycle of the run: 法然 (専修念仏, 知恩院), 菅原道真 (天神, 天満宮, 飛梅), 祇園精舎 (平家物語 opening; WATCH OUT Kyoto's 祇園), 時効 (two senses: legal, and もう時効だから言うけど; 2010 abolition for murder), 忠誠心 (vs 忠誠), 事情聴取 (vs 取り調べ, 聞き込み), 創出 (雇用創出), 船乗り (vs 船員), 新婚旅行 (vs ハネムーン), 上市 (pharma launch; WATCH OUT 上司). New kanji 菅 added to the kanji index. Self-check skipped (daily OpenRouter cap spent).

### 2026-10-11 (Routine v3: new-entries — 20 New Entries, IDs 31880–31899)

Twenty internal-closure candidates that existing entries already use, in queue order: 出廷 (vs 出頭), 殺処分 (official term; 殺処分ゼロ), 横行 (of wrongdoing; vs はびこる/蔓延), 糠床, 土砂災害 (土石流/崖崩れ/地滑り), 明治神宮, 親方 (two senses: master craftsman, sumo stable master; 親方日の丸), 盗塁, 乾季 (also 乾期; WATCH OUT 換気/寒気), 答辞 (vs 送辞), 金沢, 婦人科, 武勇伝, 収入印紙, 御利益 (りやく vs 利益 りえき), 重鎮 (vs 大御所/第一人者), 備長炭, 物産展, 目先 (two senses; 目先の利益, 目先が利く), 宗派. The candidate 福引 was dropped as a duplicate of 福引き (17826). The conjugation generator also filled in tables missing from four する-nouns of an earlier run (大勝, 就労, 変色, 大成). Self-check clean.

### 2026-10-11 (Routine v3: candidates — 39 Candidates Added, C24329–C24367)

No unresolved noentry markers remain, so the source was a scan of example sentences for furigana-marked kanji words with no link that match no headword or candidate. 39 added, each with the entry that uses it: 国際社会, 寝入る, 明星, 過払い, 脆弱性, 同社, 色濃い, 光学, 集合写真, 保冷, 病魔, 滅入る, 交通手段, 吸水性, 低金利, 浮世絵師, 時期尚早, 日付変更線, 従属節, 文人, 未来永劫, 黄身, 善玉菌, 無形文化遺産, 問答, 善光寺, 白内障, 売主, 徳島, 多幸, 論語, 波打つ, 所狭し, 隣家, 稜線, 大物, 平均寿命, 本能寺, 書道家. Queue 79 → 118.

### 2026-10-11 (Routine v3: new-entries — 5 New Entries, IDs 31875–31879)

Five internal-closure candidates in queue order, a short last cycle of the run: 平素 (平素より as a letter opening; vs 普段/日頃), 朝鮮半島 (朝鮮 vs 韓国 as names), 稚魚 (稚魚を放流する), 釈迦 (お釈迦様, 釈迦に説法, お釈迦になる, 花祭り), 蝶番 (also 丁番; butterfly-wing etymology). New kanji 迦 added to the kanji index. Self-check clean.

