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

### 2026-11-03 (12 new entries, fifth cycle of the 05:50 run)

32705–32716. Closure: 効能書き, サブタイトル, 落札者, 天下無双. Brainstorm (animal-mammal field): カワウソ (cross-referenced to ラッコ), セイウチ, チーター, ナマケモノ (contrasted with 怠け者). ezFurigana lookups: 思える (seem; can believe), 過言, 関わり, 勝ち組.
Self-check: 2 flags applied (サブタイトル can also mean film subtitles; 関わり is not a person tag).

### 2026-11-03 (15 new entries, third cycle of the 05:50 run)

32690–32704. Closure: 後述, 先述 (both from 11911 前述), フェンシング, 写真展, 販売者. Brainstorm: 前借り (from 借りる), コアラ, ラッコ, シャチ, 虫取り網 (animal fields). ezFurigana lookups: おめでたい (happy; naive), 思いの丈, 買い戻す, 返り討ち, オランダ.
Self-check: clean (0 accuracy flags, 13 kana links confirmed).

### 2026-11-03 (6 new entries, fifth cycle of the 02:49 run)

32684–32689. Closure: 仏頂面, しかめっ面 (both from 02231, contrasted with each other). Brainstorm: もらい物 (from もらう), 勉強家 (from 勉強する). ezFurigana lookups: 男友達, お膝元. Candidates added: ガリ勉, 読書家, 女友達.
Self-check: 1 notes flag applied (plain 膝元 can also mean a ruler's seat).

### 2026-11-03 (6 new entries, sixth cycle)

32678–32683. Closure: 台布巾, 記名投票. Brainstorm: 借り物 (from 借りる), はみ出る (from 出る). ezFurigana lookups: 開口一番, 影武者. Also fixed the reading of 遅れて in 32673 出遅れる ex2 (おく, not おそ).
Self-check: 2 translation flags applied (台布巾 is a table-wiping cloth, not a tablecloth).

### 2026-11-03 (18 new entries, third cycle)

32660–32677. Closure: マイナンバー, スピンオフ, 白夜, 巾着, 人相, 謀る. Brainstorm: シラミ, ノミ (animal-insect field), 脱ぎ捨てる, 手始め, 目に入る, 出遅れる (seeded from 脱ぐ, 始める, 目, 出る). ezFurigana lookups: 英単語, 覆いかぶさる, お子様, 雄叫び, 落ち度, 岩手. Candidate 嗜む dropped (spelling of existing たしなむ).
Self-check: clean (0 accuracy flags, 15 kana links confirmed).

