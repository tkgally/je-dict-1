# Cross-Reference Design

**Last updated**: 2026-04-06

## Overview

Cross-references connect related entries, helping learners discover vocabulary networks. In a browsing-oriented dictionary like je-dict-1, cross-references are arguably **the single most important navigational feature** — they transform a collection of isolated entries into an interconnected web that rewards exploration.

## Why cross-references matter especially in a browsing dictionary

Traditional dictionaries are lookup tools: the user has a word, finds the entry, gets the answer. But je-dict-1 is designed to also support **browsing** — a learner exploring related vocabulary to deepen their understanding. Cross-references serve this browsing use case in several ways:

### Vocabulary network discovery

When a learner looks up 教える (to teach), cross-references to 教育 (education), 教師 (teacher), 教室 (classroom), and 習う (to learn) reveal an entire semantic network. This is how vocabulary is actually organized in the mental lexicon — as interconnected webs, not isolated items. Research on vocabulary acquisition (see [Vocabulary Acquisition](../research/vocabulary-acquisition.md)) consistently shows that learning words in semantic clusters improves retention.

### Serendipitous learning

A learner looking up 暑い (hot/weather) who discovers a prominent link to 熱い (hot/objects) learns a distinction they didn't know they needed. This serendipitous discovery is one of the great advantages of a browsable dictionary over a search-only interface.

### Disambiguation

For near-synonyms that learners commonly confuse (見る vs. 観る vs. 眺める), cross-references ensure the learner finds all the relevant entries and can compare them. The notes in each entry may contrast these words, but without links, a learner might never discover the other entries exist.

### Completeness signals

When a learner sees that a verb entry links to its transitivity pair, its honorific form, and several common compounds, they gain confidence that the dictionary covers the topic thoroughly. Missing cross-references create the opposite impression — the dictionary feels incomplete even if the entries exist.

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

Over 5,400 cross-references exist across 22,400+ entries (roughly 0.24 cross-references per entry on average). Coverage is growing through:
- Systematic review (`prompts/add_cross-references.md`)
- Entry creation (new entries include initial cross-refs)
- Polishing passes
- The `find_merge_candidates.py` tool, which also detects missing cross-references

## Design principles

1. **Bidirectional**: If A references B, B should reference A
2. **Specific relationships**: Use the most specific label available (not just "related")
3. **Don't over-link**: Focus on pedagogically useful connections, not encyclopedic completeness
4. **Prominent for must-know pairs**: Use `prominent_see_also` sparingly for the most important connections

## Ideas for improving the cross-reference system

### Higher coverage targets

The current ratio of ~0.24 cross-references per entry is low. Most entries have zero or one cross-reference. A reasonable target might be an average of 1-2 cross-references per entry, which would mean 22,400-44,800 total. Priority should go to:
- **Verbs without transitivity pair links** — these are the most pedagogically critical
- **Near-synonyms** — words that learners commonly confuse
- **Semantic field clusters** — groups of related words (colors, emotions, family terms) that should all link to each other

### Automated cross-reference suggestions

The `find_merge_candidates.py` tool already detects some missing cross-references. This could be extended:
- **Shared-kanji detection**: Entries sharing a kanji character are often related (教える, 教育, 教室). Automatically suggest cross-references between entries that share kanji
- **Note text mining**: When entry notes mention another word by name, suggest a cross-reference. Many notes already contrast or compare words without linking to them
- **Semantic embedding clustering**: Use LLM embeddings to find entries with similar meanings and suggest cross-references between them

### Cross-reference quality review

Not all cross-references are equally useful. A periodic review could:
- Verify bidirectionality (if A→B exists, does B→A?)
- Check that relationship labels are accurate and specific
- Remove low-value "related" links that don't help learners
- Upgrade generic "related" labels to more specific ones where possible

### Navigational improvements on the website

The static site could better leverage cross-references for browsing:
- **"Related words" sidebar**: Show cross-references in a sidebar panel rather than buried at the bottom of the entry
- **Semantic field pages**: Auto-generated pages that cluster entries by semantic field (all color terms, all emotion words, etc.) based on cross-reference networks
- **"Explore related" mode**: A browsing interface that shows a word and its immediate cross-reference network, letting the learner click through related words
- **Graph visualization**: A visual map of cross-reference connections for a given entry or semantic field — useful for understanding vocabulary networks at a glance

### Typed browsing paths

Beyond individual cross-references, curated "learning paths" could guide learners through related vocabulary in a meaningful order:
- "Verbs of motion" path: 行く → 来る → 歩く → 走る → 飛ぶ → ...
- "Keigo progression" path: 食べる → 召し上がる → いただく
- "Counter words" path: grouped by semantic category

These would be built on top of the cross-reference data but add an editorial layer of ordering and narrative.

### Cross-reference completeness metrics

The `build/report.py` dashboard could track:
- Percentage of entries with at least one cross-reference
- Percentage of verbs with transitivity pair links
- Bidirectionality compliance rate
- Distribution of relationship types
- Entries with the most cross-references (hub words)
- Orphan entries (no cross-references and no inline links to/from)

## Implications for je-dict-1

Cross-references are not just metadata — they are a core part of the user experience for a browsing dictionary. Investing in cross-reference coverage and quality has a multiplier effect: each new cross-reference makes two entries more useful. The automated pipeline (`add_cross-references.md`) should remain a high-priority polishing task, and new tools for suggesting and validating cross-references would have high ROI.

## Related pages

- [Entry Design](../project/entry-design.md)
- [Verb Transitivity Pairs](verb-transitivity.md)
- [Content Pipeline](../project/content-pipeline.md) — cross-references are added during creation and polishing
- [Vocabulary Acquisition](../research/vocabulary-acquisition.md) — research on learning words in semantic clusters
- [Digital Dictionary UX](../research/digital-dictionary-ux.md) — interface design for browsing
- [Quality Standards](../project/quality-standards.md) — cross-reference coverage as a quality metric
