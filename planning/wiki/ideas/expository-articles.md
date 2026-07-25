# Expository Articles on Japanese Vocabulary

**Last updated**: 2026-04-06

## Overview

A proposal to add a new category of content to the dictionary: standalone expository articles that explore aspects of Japanese vocabulary too broad or complex for any single entry's notes section. These articles would serve the dictionary's evolving role as a resource for vocabulary-building through browsing and serendipitous discovery, rather than purely as a lookup tool.

## Motivation

### The changing role of the dictionary

As the curator has observed, the "look up an unknown word to find its meaning" function is increasingly well-served by search engines and LLMs. A static dictionary's comparative advantage lies elsewhere:
- **Curated depth**: Carefully organized information about word relationships, usage patterns, and cultural context that a quick LLM query won't provide
- **Browsability**: Structured content that rewards exploration and leads to unexpected discoveries
- **Persistence**: Stable, citable content that doesn't change with each query

Expository articles would strengthen all three of these advantages.

### Precedent in print dictionaries

Many well-regarded print dictionaries include essay-length articles:
- **Oxford English Dictionary**: "Usage notes" on contentious or complex topics (e.g., the singular "they")
- **Kenkyusha's New Japanese-English Dictionary (新和英大辞典)**: Extensive supplementary articles on Japanese culture and usage
- **Longman Dictionary of Contemporary English**: "Language notes" on grammar, usage, and vocabulary groups
- **Robert (French)**: Encyclopedic articles integrated with the dictionary
- **Kodansha's Furigana Japanese Dictionary**: Cultural and usage notes scattered through entries

These articles add significant value beyond what individual entries can provide.

## Proposed article types

### 1. Semantic field surveys

Deep explorations of vocabulary clusters that span many entries:
- **Counting and classifiers**: How the counter system works, which counters overlap, common mistakes — synthesizing information spread across dozens of counter entries
- **Keigo (honorific language)**: The three-way system (尊敬語/謙譲語/丁寧語), how it maps onto the dictionary's entries, common patterns
- **Color terms**: How Japanese color vocabulary differs from English (青 covering blue and green, etc.), cultural associations, metaphorical extensions
- **Body-part idioms**: Systematic survey of expressions using 手, 目, 口, 足, etc.
- **Onomatopoeia families**: How sound-symbolic words cluster by initial consonant (ぱ- words vs. ば- words vs. ぴ- words)
- **Time expressions**: The complex system of relative time words, calendar vocabulary, duration vs. point-in-time

### 2. Grammatical-lexical boundary topics

Areas where vocabulary and grammar intertwine:
- **Auxiliary verbs and their lexical origins**: How ～てしまう, ～ておく, ～てくる trace back to literal meanings
- **The する verb family**: How する combines with nouns, and how this differs from English verb formation
- **Adjective-noun boundaries**: When -的 turns a noun into an adjective, and when it doesn't
- **Particles as vocabulary**: Why particles deserve dictionary entries and how to use them

### 3. Usage and register essays

Extended discussions of pragmatic topics:
- **Masculine and feminine speech**: How gendered language works in modern Japanese, what's changing
- **Written vs. spoken registers**: How vocabulary choice differs between modes
- **Formality in everyday life**: Practical guide to register choices in common situations
- **Loanword adaptation**: How English words change meaning and usage when borrowed into Japanese

### 4. Orthographic topics

Discussions of writing-related vocabulary issues:
- **Kanji vs. kana writing conventions**: When to write in kanji, when kana is preferred, and why
- **Okurigana variation**: Words with multiple accepted okurigana patterns and how to choose
- **Katakana conventions**: Beyond loanwords — emphasis, scientific names, stylistic choices
- **Old vs. new kanji forms**: 旧字体 awareness for learners encountering older texts

### 5. Cultural-lexical topics

Where vocabulary reflects culture:
- **Seasonal words (季語)**: The rich vocabulary of seasons in Japanese and its poetic tradition
- **Food vocabulary**: How Japanese food terminology reflects culinary culture
- **Academic and testing vocabulary**: Words learners encounter in institutional contexts
- **Business Japanese vocabulary**: The specialized vocabulary of the workplace

## Implementation considerations

### Entry format

Articles would need a new entry type or a separate content system:

**Option A: New entry type** — Add a `"type": "article"` to the schema, with a different required-fields set (no senses/examples, but structured prose sections). Articles would appear in the dictionary alongside entries and be searchable.

**Option B: Separate article directory** — A new `articles/` directory with markdown or JSON files, rendered into dedicated pages. Articles link to entries; entries link back to relevant articles.

**Option C: Special entries** — Use existing entry format but with a dedicated POS tag like `article` and modified rendering. Minimal schema changes.

**Recommended**: Option B. Articles are fundamentally different from dictionary entries and should have their own format, but they should be deeply integrated with the entry pages through bidirectional links.

### Integration with entries

- Entries in a semantic field covered by an article should link to the article (e.g., every counter entry links to the "Counting and classifiers" article)
- Articles should contain inline links (⟦...⟧) to dictionary entries throughout
- The search index should include article content
- Articles should appear in browse/navigation alongside entries

### Authoring and maintenance

- Articles could be written by Claude during dedicated sessions (a new prompt type)
- Cross-model review (see [Multi-Model Proofreading](multi-model-proofreading.md)) would be especially valuable for articles, which make broader claims than individual entries
- Articles should be versioned and dated
- As individual entries are updated, articles referencing them may need updates too

### Browsability enhancements

Articles would support the goal of making the dictionary more useful for browsing:
- A dedicated "Articles" index page, browsable by topic
- "Related article" links on entry pages
- Random article feature (alongside existing random entry)
- Featured article on the homepage

## Prioritization

Which articles to write first, based on likely user interest and available entry depth:

| Priority | Topic | Entry coverage | Complexity |
|----------|-------|---------------|------------|
| High | Counting and classifiers | Good (~100+ counter entries) | Medium |
| High | Keigo and politeness | Good (many register-marked entries) | High |
| High | Onomatopoeia families | Good (many entries) | Medium |
| Medium | Color terms | Moderate | Low |
| Medium | Auxiliary verb origins | Good (verb entries exist) | Medium |
| Medium | Kanji vs. kana conventions | Relevant to all entries | Medium |
| Lower | Seasonal words | Some coverage | Medium |
| Lower | Business vocabulary | Growing coverage | Low |

### Added 2026-07-25: `ている` and the te-form auxiliaries — an article as the cheapest answer to a real gap

A 2026-07-25 routine polish run observed that **`ている` has no entry** and is marked `noentry` in the
ASPECT notes of **37 entries** (count verified this run). It is plainly a core form for the dictionary's
intermediate-learner audience, but it is also a **grammatical form rather than a vocabulary item**, and
adding entries for auxiliaries would be a genuine change in what this dictionary *is* (see the
[Cleanup Backlog informational note](cleanup-backlog.md) on the same observation, which frames the
curator's three options).

An **article** is the option that serves the learner without that scope change: one piece covering
ている's progressive vs. resultative-state split — the distinction the ASPECT notes in those 37 entries
keep gesturing at individually — extended to its te-form siblings ておく, てしまう, てみる, ていく/てくる.
Entry coverage is unusually strong: the ASPECT notes already written across verb entries are effectively
the article's source material, and each of the 37 `noentry` markers is a natural inbound link once the
article exists.

| Priority | Topic | Entry coverage | Complexity |
|----------|-------|---------------|------------|
| High | `ている` and the te-form auxiliaries (aspect) | Strong (37 entries' ASPECT notes + all verb entries) | Medium |

Note the adjacent open question this would also settle in practice: whether an article can be an
inline-link target. If it can, the 37 stale `noentry` markers resolve to the article; if not, they stay
as they are and the article is discoverable only by browsing — worth deciding before writing, and
related to the "landing pages for thematic search" question below.

## Open questions

- How long should articles be? Print dictionary essays range from 500 to 5,000 words.
- Should articles be written all at once or grown incrementally as entry coverage improves?
- How to handle overlapping scope between articles and entry notes? (Articles should add synthesis and breadth; notes should stay entry-specific.)
- Should articles have a separate visual style on the website to distinguish them from entries?
- Could articles serve as landing pages for thematic search (e.g., searching "counters" leads to the article)?

## Related pages

- [Digital Dictionary UX](../research/digital-dictionary-ux.md) — browsing behavior and interface design
- [Project Overview](../project/overview.md) — the dictionary's evolving purpose
- [Cross-Reference Design](../topics/cross-references.md) — how articles would link to entries
- [Example Sentence Design](../research/example-sentences.md) — quality standards that would apply to article examples too
- [Onomatopoeia and Mimetic Words](../research/onomatopoeia-mimetics.md) — research backing an onomatopoeia overview article
