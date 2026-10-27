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

### 2026-10-27 (15 new entries, third batch)

32373–32387. Closure: 計画倒れ, 平服, 尾てい骨, 共同親権, 国民皆保険. Brainstorm (bird and fish fields):
ムクドリ, 九官鳥, カンパチ, ドジョウ, トビウオ. ezFurigana lookups: 勝手に, 主たる, 奴隷, 点く, 横殴り.
点く is now the intransitive pair of つける (00562). Self-check: 2 flags, both applied.

### 2026-10-27 (12 new entries, second batch)

32361–32372. Closure: 満ち欠け, 考案者, 厚志, 通じ合う. Brainstorm: 一仕事, 待ち望む, 忘れ去る,
習うより慣れよ. ezFurigana lookups: 術式, 工場 (こうば), 叫び, 狂乱. The 248 existing links on 工場 all
carry the reading こうじょう and stay on 01082. Self-check: 1 flag, applied. 〜型 (がた) was left for a
later batch, because it will need its existing 型 links sorted the way 〜外 was.

### 2026-10-27 (20 new entries, first batch)

32341–32360. Closure: 〜外 (suffix), 暴利, 相当額, 芳名, 座り仕事, を通じて, 計らう. Brainstorm:
までに, お待ちかね, 買い込む, 待ちぼうけ, 忘れっぽい, ても, 人出. ezFurigana lookups: 〜等, には, 大〜, 下 (もと),
願, とは. 45 existing links to 外 that were the suffix (予想外, 圏外, 時間外, …) now point to 〜外 instead of
the prefix 外〜. Self-check: 4 notes flags, all applied. Candidates 頃 and 否応なしに dropped (covered by
〜ころ and 否応なし); 取り計らう queued.

### 2026-10-26 (15 new entries, fourth batch)

32326–32340, five from each stream. Closure: 代替案, 体操服, 最年少, 非公認, 人工的. Brainstorm
(fish and birds): 穴子, ホッケ, メダカ, ヒヨドリ, ナマズ. ezFurigana lookups: 合衆国, 幽閉, 激甚, 説話,
薄明かり. Self-check clean (0 flags on 16 entries). 最年長 queued as a candidate.

### 2026-10-26 (ezFurigana lookup report: 498 new candidates; a third candidate stream)

ezFurigana (https://www.ezfurigana.com/), which adds furigana to its users' texts and links the
words to this dictionary, sent Tom its first report of words users looked up and did not find:
1,384 rows. Each row was vetted against the find-candidates gates. 498 became candidates (幽閉,
奴隷, 過言, いち早く, 点く, 勝手に; homographs read another way such as 生物 なまもの, 人気 ひとけ, 下
もと; grammar patterns the dictionary lacked, such as には, ずに, ないで, ことになる, ことがある,
ことができる, かねない, たり, れる and られる). 276 were other spellings or forms of existing
entries, 7 were already queued, and 601 were rejected (mostly names, bare kanji fragments,
transparent compounds and number + counter strings). Reports now have a home
(`external/ezfurigana/`) and a tool (`build/ezfurigana_lookups.py`: ingest, pending, record,
stats, queue, variants); the `candidates` mode works report rows first, `new-entries` takes about
a third of its words from them (most looked-up first), and the selector no longer counts them
toward the restock threshold, so closure and brainstorming continue as before. The same session
ran one brainstorm batch (field animal-insect: 26 candidates such as ダニ, ヒグラシ, 蝉時雨,
虫の知らせ) and added 8 words the report suggested by association (the dynasties 唐, 明, 清;
させる, せる, かねる; 東部, 西部). Queue: 167 → 699. README and CLAUDE.md now say the data is used
by ezFurigana.

