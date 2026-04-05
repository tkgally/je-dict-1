# Japanese Counters and Classifiers

**Last updated**: 2026-04-05

## Overview

Japanese numeral classifiers (助数詞, josūshi — literally "helping number words") are obligatory morphemes that categorize and quantify nouns. Unlike English, where numbers directly modify nouns ("three apples"), Japanese requires a classifier between the number and the noun, selected based on semantic properties of the referent — shape, size, animacy, or function. The system has roughly 500 identified classifiers, though only about 30 see frequent daily use (Downing, 1996).

## The classifier system

### Semantic categories

Classifiers organize the noun world along several dimensions:

| Dimension | Examples | Classifiers |
|-----------|----------|------------|
| **Animacy** | People, small animals, large animals, birds | 人, 匹, 頭, 羽 |
| **Shape** | Flat/thin, long/cylindrical, small/compact | 枚, 本, 個 |
| **Function** | Vehicles, buildings, cups/glasses | 台, 軒, 杯 |
| **Abstraction** | Times/occurrences, points/scores | 回, 点 |
| **Time** | Hours, minutes, seconds, days, months, years | 時, 分, 秒, 日, ヶ月, 年 |
| **Units** | Currency, weight, volume | 円, グラム, リットル |

### The generality hierarchy

Not all classifiers are equally specific. There is a hierarchy from general to specific:

1. **つ** (native Japanese counting) — the most general classifier, usable for almost anything including abstract concepts and ages (up to 9)
2. **個** (Sino-Japanese) — general-purpose for bounded, concrete objects; the default fallback when a specific counter is unknown
3. **Specific classifiers** — 枚 for flat things, 本 for long things, 匹 for small animals, etc.

Tofugu's analysis of 350 classifiers groups them into usefulness tiers: 2 "absolutely must-know" (つ and 個), 17 "must-know," 47 "common," and roughly 280 less common or specialized ones. This maps closely to the finding that ~30 classifiers cover daily usage.

### Sound changes (音便)

When Sino-Japanese numbers combine with classifiers beginning with certain consonants, systematic sound changes occur. These are a major source of difficulty for learners:

**Classifiers beginning with h- (は行):**
- Numbers 1, 6, 8, 10 → h changes to **p** (with gemination): 一本 → いっ**ぽ**ん, 六匹 → ろっ**ぴ**き
- Number 3 → h changes to **b**: 三本 → さん**ぼ**ん, 三匹 → さん**び**き
- Numbers 2, 4, 5, 7, 9 → no change: 二本 → に**ほ**ん, 五匹 → ご**ひ**き

**Classifiers beginning with k-, s-, t-:**
- Numbers 1, 6, 8, 10 → gemination: 一個 → い**っこ**, 六歳 → ろ**っさ**い

These changes are phonologically motivated (ease of articulation) but must be memorized as patterns, since learners cannot reliably predict them from general rules alone.

### Native vs. Sino-Japanese counting

Japanese has two parallel counting systems:

- **Wago (和語)**: ひとつ, ふたつ, みっつ... とお (1-10 only). Used with the general classifier つ. Flexible and informal.
- **Kango (漢語)**: いち, に, さん... Uses Sino-Japanese numbers. Required for all specific classifiers.

The wago system is limited to 1-10 and cannot combine with specific classifiers, but it serves as a universal fallback — a learner who says "りんごを三つ" instead of "三個" is always understood.

## Acquisition challenges for L2 learners

### Why counters are difficult

1. **No L1 equivalent**: English speakers have limited experience with classifier systems (pieces, sheets, heads of cattle are rare exceptions)
2. **Large inventory**: Even the "essential" set of ~20 classifiers requires memorizing which semantic category each noun belongs to
3. **Sound changes**: Phonological alternations add a memorization burden on top of classifier selection
4. **Category boundaries**: Why is a rabbit counted with 羽 (birds) rather than 匹 (small animals)? Category assignments contain historical and cultural quirks
5. **Register sensitivity**: Using a generic classifier where a specific one is expected can sound childish or uneducated in formal contexts

### Research findings

Yamamoto and Keil's research on classifier acquisition found that even Japanese children don't fully master the system until around age 6, and the semantic basis of classifier selection (shape, animacy, etc.) is acquired gradually. For L2 learners, research using eye-tracking (De Gruyter, 2019) showed that advanced L2 speakers can use classifier information for real-time sentence processing and prediction comparably to native speakers, but proficiency level affects processing speed.

Downing (1996) found that in actual usage, classifiers rarely carry information unavailable from context — the noun itself usually makes the referent's category clear. This suggests classifiers serve primarily a grammatical rather than semantic function in discourse, which has implications for how dictionaries should treat them.

### Pedagogical priorities

Based on frequency and learner needs, counters can be prioritized:

**Tier 1 — Essential (survival):** つ, 個, 人/名, 枚, 本, 匹, 台, 冊, 杯, 回 + time counters (時, 分, 秒, 日, ヶ月, 年, 週間)

**Tier 2 — Common (intermediate):** 階, 歳, 足, 軒, 頭, 羽, 点, 通, 着, 問, 番, 曲, 発

**Tier 3 — Specialized (advanced):** 滴, 尾, 両, 合, 棟, domain-specific counters

## Dictionary treatment of counters

### Challenges for bilingual dictionaries

1. **Headword format**: Should the counter be listed as "〜個" (with tilde prefix to show it's a suffix) or "個" alone? Japanese-English dictionaries vary.
2. **Sound change documentation**: Full counting tables (1-10 + "how many?") are essential but space-intensive.
3. **Semantic scope**: Defining exactly which nouns a counter applies to requires listing typical objects — too few examples and learners can't generalize, too many and the entry bloats.
4. **Cross-referencing**: Counters need links to related counters (個 vs. つ, 匹 vs. 頭 vs. 羽) and to nouns they commonly count.
5. **Grammatical patterns**: The basic pattern "number + counter + の + noun" vs. "noun + を + number + counter + verb" needs illustration.

### What effective counter entries include

Drawing from pedagogical research and existing dictionary practice:

- **Clear semantic scope** with concrete examples of countable objects
- **Full counting table** (1-10 + なん〜) with all sound changes marked
- **Example sentences** showing the counter in natural syntactic positions
- **Notes on register** (e.g., 名 is formal, 人 is neutral)
- **Contrast with related counters** (when to use 匹 vs. 頭)
- **Fallback guidance** — when is it acceptable to use 個 or つ instead?

## Implications for je-dict-1

### Current coverage

je-dict-1 has 36 counter entries spanning the most essential counters (個, 枚, 本, 匹, 人, 冊, 杯, 台, 羽, 頭, etc.) plus time-related counters. This covers most of Tier 1 and some of Tier 2.

### What's working well

The existing counter entries (e.g., 個) already include counting tables with sound changes marked, example sentences with natural usage, and notes on semantic scope. This is a strong foundation.

### Potential improvements

1. **Gap filling**: Some common Tier 2 counters may still be missing (着 for clothing, 曲 for songs, 番 for ordinal numbers). A systematic check against frequency-ranked counter lists would identify gaps.
2. **Cross-references between counters**: Entries like 匹, 頭, and 羽 should prominently cross-reference each other, since learners frequently confuse which to use for which animals.
3. **Counter-noun pairing data**: The notes could more systematically list which common nouns each counter is used with, functioning as a mini-collocation dictionary for counters.
4. **Sound change patterns**: A general note or wiki page explaining the h→p/b pattern once, with individual entries referencing it, could reduce redundancy and help learners see the system.
5. **Fallback guidance**: Explicit notes on when 個 or つ is acceptable as a substitute would help intermediate learners navigate uncertainty.

## Sources

- Downing, Pamela A. (1996). *Numeral Classifier Systems: The Case of Japanese*. John Benjamins.
- Yamamoto, Kasumi & Keil, Frank C. "The Acquisition of Japanese Numeral Classifiers." Yale Cognitive Development Lab.
- Kanero, Junko et al. (2024). "The acquisition of the semantics of Japanese numeral classifiers: The methodological value of nonsense." *Journal of Child Language*, Cambridge University Press.
- "Generating predictions based on semantic categories in a second language: A case of numeral classifiers in Japanese." (2019). *IRAL - International Review of Applied Linguistics*, De Gruyter.
- Tofugu. "350 Japanese Counters Grouped by How Useful They Are." https://www.tofugu.com/japanese/japanese-counters-list/

## Related pages

- [Japanese Lexicography](japanese-lexicography.md) — broader challenges of Japanese dictionaries
- [Vocabulary Acquisition](vocabulary-acquisition.md) — how L2 learners acquire vocabulary
- [Vocabulary Tier System](../project/vocabulary-tiers.md) — the three-tier classification system
- [Entry Design](../project/entry-design.md) — entry schema and field structure
- [Collocations in Learner Dictionaries](collocations.md) — related topic of word pairing data
