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

### 2026-10-26 (8 new entries, third batch)

Eight entries added (32318–32325). Four define words the dictionary already used: 度外視,
年老いる, 生まれ育つ, 手術室. Four come from the brainstorm on basic words: 探し物, 店じまい,
明くる日 (the next day, in narrative, contrasted with 翌日 and 明日), 乗り気. An independent check
found two overstatements in the new notes, both fixed.

### 2026-10-26 (30 new candidates)

The candidate queue was restocked from 145 to 175 words. Twelve are closure words that entries
written or fixed today use without an entry (調子に乗る, 早春, 日長, 歯列, 八重歯, 目白押し, 托卵,
閑古鳥, 授賞式, 板書, 使節団, 親告罪). Eighteen come from brainstorming the basic seeds 探す–と
(探し物, 探し出す, 店じまい, 店番, 明くる日, 働きかける, からには, 乗り気, …), including two
grammar words the dictionary turned out to lack entirely: the conditional たら and the listing
particle とか.

### 2026-10-26 (20 new entries, second batch)

Twenty entries added (32298–32317), bringing the dictionary to about 32,090. Ten define words the
dictionary already used without an entry: 自然体, 異国情緒, 小細工, 思い上がる, 雪下ろし, 春先, 夜長,
歯並び, 長旅, 活断層. Ten come from brainstorming the fish and bird vocabulary: ハマチ, カレイ, タラ,
フグ, ニシン, シシャモ, メジロ, ホトトギス, セキセイインコ, ハチドリ. An independent check found two
factual slips in the notes (ヒラメ called halibut; why 鸚鵡貝 is so named), both fixed.

