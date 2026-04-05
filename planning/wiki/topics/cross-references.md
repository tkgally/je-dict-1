# Cross-Reference Design

**Last updated**: 2026-04-05

## Overview

Cross-references connect related entries, helping learners discover vocabulary networks. je-dict-1 has two cross-reference mechanisms plus inline links.

## Reference types

### `prominent_see_also`

High-priority links displayed prominently on the entry page. Used for:
- **Transitivity pairs**: 開ける (transitive) ↔ 開く (intransitive)
- **Antonyms**: 大きい ↔ 小さい
- **Honorific/humble pairs**: 食べる → 召し上がる / いただく
- **Closely related words** that learners should know together

### `cross_references`

Standard related-entry links in a "See also" section. Used for:
- **Synonyms and near-synonyms**: 美しい → きれい, 見事
- **Same-family words**: 教える → 教育, 教師, 教室
- **Semantic field neighbors**: 春 → 夏, 秋, 冬
- **Words mentioned in notes**: if the notes contrast with another word, link to it

### Inline word links (`⟦...⟧`)

Within example sentences and notes, specific words can link to their dictionary entries:
- Format: `⟦surface→base：entry_id⟧`
- Added during polishing (never during initial entry creation)
- Enables direct navigation from any mention of a word to its entry

## Relationship labels

Each cross-reference includes a `relationship` field:
- `synonym`, `antonym`, `hypernym`, `hyponym`
- `transitive pair`, `intransitive pair`
- `honorific form`, `humble form`
- `related`, `variant`, `compound`

## Current coverage

~3,400 cross-references exist across ~19,000 entries. Coverage is growing through:
- Systematic review (`prompts/add_cross-references.md`)
- Entry creation (new entries include initial cross-refs)
- Polishing passes

## Design principles

1. **Bidirectional**: If A references B, B should reference A
2. **Specific relationships**: Use the most specific label available (not just "related")
3. **Don't over-link**: Focus on pedagogically useful connections, not encyclopedic completeness
4. **Prominent for must-know pairs**: Use `prominent_see_also` sparingly for the most important connections

## Related pages

- [Entry Design](../project/entry-design.md)
- [Verb Transitivity Pairs](verb-transitivity.md)
