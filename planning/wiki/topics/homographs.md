# Handling Homographs

**Last updated**: 2026-04-05

## The problem

Japanese has many words that share identical written forms but differ in reading and/or meaning:

- **Different readings, different meanings**: 生 → なま (raw), いきる (to live), うまれる (to be born), etc.
- **Same reading, different kanji**: かける → 掛ける, 欠ける, 架ける, 駆ける
- **Same everything, different senses**: Often handled as multiple senses within one entry

## Current approach

### Separate entries for different readings
Words with the same kanji but different readings get separate entries, each with its own ID. They are linked via cross-references.

Example: 下 has entries for した (below), もと (under/basis), くだる (to go down), さがる (to fall), etc.

### Multi-sense for same reading
When a word has one reading but multiple distinct meanings, these are handled as separate senses within a single entry. The threshold for "separate entry" vs. "separate sense" is:
- **Same entry**: meanings are etymologically related or the connection is clear to learners
- **Separate entries**: meanings are unrelated enough that combining them would confuse learners

### Search and disambiguation
The search index includes all readings and glosses, so searching for a kanji will surface all entries that use it. The kanji index (`kanji/`) maps individual kanji to all entries containing them.

## Edge cases

### Verbs that are homophones but different conjugation classes
Example: きる — 切る (godan, "to cut") vs. 着る (ichidan, "to wear"). These must be separate entries because they conjugate differently.

### Katakana homographs
Rare but exist: バス (bus) vs. バス (bass). Separate entries with disambiguation in the definition.

### Words written in kana only
When a word is typically written in kana, homography is less of a problem for the reader but more of a problem for the dictionary — the search must distinguish between, e.g., かける as an independent search vs. part of a longer word.

## Future improvements

- Better disambiguation in search results (showing reading + brief gloss)
- Visual grouping of related homographs on search result pages
- Kanji component search to help learners find "that word with 生 in it"

## Related pages

- [Entry Design](../project/entry-design.md)
- [Cross-Reference Design](cross-references.md)
- [Japanese Lexicography](../research/japanese-lexicography.md)
