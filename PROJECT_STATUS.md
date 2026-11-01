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

### 2026-11-01 (11 new entries, fourth cycle)

32595–32605. Closure: プレゼンター, 周知徹底, 大トロ, 有効求人倍率. Brainstorm: 蟻地獄 (animal-insect field), 唐, 明, 清 (seed 宋). ezFurigana lookups: アドベンチャー, あいうえお, 太郎. Candidate かねる dropped (covered by 兼ねる sense 2).
Self-check: 2 flags applied (明 has other readings such as みょう; 日清食品's 清 is not the dynasty).

### 2026-11-01 (20 new entries, third cycle)

32575–32594. Closure: 高級車, 勝ち進む, 勝ち越す, エキゾチック, 時代小説, 願掛け, 啓蒙. Brainstorm: たら, とか (seed と), 東部, 西部 (seed 南部), ダニ, ヒグラシ, カメムシ (animal-insect field). ezFurigana lookups: 証, アスリート, 雨脚, あらかた, 在り処, あらあら.
Self-check: clean (0 accuracy flags); 1 kana link removed (について in カメムシ was に + 付く). ば's cross-reference to たら pointed at タラ (cod); now points at the new たら entry. New kanji 蒙 added to the kanji index.

### 2026-11-01 (11 new entries, second cycle)

32564–32574. Closure: 耕作放棄地, 指し棒, ポチ袋, 動体視力. Brainstorm: 赤身魚 (animal-fish field), 動物愛護 (animal-general field), 人捜し (seed 探す). ezFurigana lookups: 枡席, 約束事, 瑠璃, リサーチ.
Self-check: clean (0 flags). New kanji 枡 added to the kanji index.

### 2026-11-01 (16 new entries)

32548–32563. Closure: 焼きプリン, 先読み, 高速鉄道, 若旦那, 気象予報士, 結果論. Brainstorm: 恒温動物, 珍獣, 血統書 (animal-general field), 果物屋 (seed 果物), 店構え (seed 店). ezFurigana lookups: パルプ, 墓標, 魔術師, 約款, 悠久.
Self-check: clean (0 flags); 9 kana links checked, none flagged.

### 2026-10-31 (10 new entries, fourth cycle)

32538–32547. Closure: 親告罪, ご機嫌よう, 庭先, 出世頭. Brainstorm: からには (seed から), 帰り際 (seed 帰る), 働き口 (seed 働く). ezFurigana lookups: もがく, まがい, 旨.
Self-check: clean; 1 link removed (旨としている read as the particle として).

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

### 2026-11-01 (11 new entries, fourth cycle)

32595–32605. Closure: プレゼンター, 周知徹底, 大トロ, 有効求人倍率. Brainstorm: 蟻地獄 (animal-insect field), 唐, 明, 清 (seed 宋). ezFurigana lookups: アドベンチャー, あいうえお, 太郎. Candidate かねる dropped (covered by 兼ねる sense 2).
Self-check: 2 flags applied (明 has other readings such as みょう; 日清食品's 清 is not the dynasty).

### 2026-11-01 (20 new entries, third cycle)

32575–32594. Closure: 高級車, 勝ち進む, 勝ち越す, エキゾチック, 時代小説, 願掛け, 啓蒙. Brainstorm: たら, とか (seed と), 東部, 西部 (seed 南部), ダニ, ヒグラシ, カメムシ (animal-insect field). ezFurigana lookups: 証, アスリート, 雨脚, あらかた, 在り処, あらあら.
Self-check: clean (0 accuracy flags); 1 kana link removed (について in カメムシ was に + 付く). ば's cross-reference to たら pointed at タラ (cod); now points at the new たら entry. New kanji 蒙 added to the kanji index.

### 2026-11-01 (11 new entries, second cycle)

32564–32574. Closure: 耕作放棄地, 指し棒, ポチ袋, 動体視力. Brainstorm: 赤身魚 (animal-fish field), 動物愛護 (animal-general field), 人捜し (seed 探す). ezFurigana lookups: 枡席, 約束事, 瑠璃, リサーチ.
Self-check: clean (0 flags). New kanji 枡 added to the kanji index.

### 2026-11-01 (16 new entries)

32548–32563. Closure: 焼きプリン, 先読み, 高速鉄道, 若旦那, 気象予報士, 結果論. Brainstorm: 恒温動物, 珍獣, 血統書 (animal-general field), 果物屋 (seed 果物), 店構え (seed 店). ezFurigana lookups: パルプ, 墓標, 魔術師, 約款, 悠久.
Self-check: clean (0 flags); 9 kana links checked, none flagged.

### 2026-10-31 (10 new entries, fourth cycle)

32538–32547. Closure: 親告罪, ご機嫌よう, 庭先, 出世頭. Brainstorm: からには (seed から), 帰り際 (seed 帰る), 働き口 (seed 働く). ezFurigana lookups: もがく, まがい, 旨.
Self-check: clean; 1 link removed (旨としている read as the particle として).

### 2026-10-31 (19 new entries, third cycle)

32519–32537. Closure: 異存, 連れ戻す, ソースコード, コードレス, 替え刃, 基調講演. Brainstorm: 探し回る, 探し出す (seed 探す), 入室 (seed 入る), 夜店, 店番 (seed 店), 働きかける (seed 働く), ペットショップ. ezFurigana lookups: 短刀, 生物 (なまもの), 付加, 膨らみ, 崩落, 孫の手. Candidate 授賞式 was the standard spelling of 24267 受賞式, so that entry now has the headword 授賞式 (same ID) and a WRITING note.
Self-check: clean; 1 link removed (孫の手でかく read as でかい).

