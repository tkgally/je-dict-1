# Dictionary Growth and Long-Term Vision

**Last updated**: 2026-05-30

## Overview

There is no maximum size for this dictionary. Even after core learner needs are comprehensively met, the dictionary can continue growing by adding rarer vocabulary, specialized terms, and eventually new entry types. This page discusses the long-term growth trajectory and the major expansion directions under consideration.

## Current state and near-term priorities

As of late May 2026, the dictionary has over 28,200 entries covering basic, core, and general vocabulary for intermediate Japanese learners. The immediate priority is:

1. **Fill remaining gaps in common vocabulary** — ensure no everyday word is missing (see [Word Discovery Strategies](word-discovery-strategies.md))
2. **Polish existing entries** — bring all entries up to v2 quality standards
3. **Grow the candidate pipeline** — maintain a healthy queue of words ready for entry creation

## Growth phases

### Phase 1: Learner completeness (current)

Goal: A learner at the intermediate level should be able to look up virtually any word they encounter in everyday reading, media, and conversation.

- Focus on high-frequency, high-utility vocabulary
- Target: probably 25,000-30,000 entries to feel "complete" for typical learner needs
- Polishing is as important as new entry creation

### Phase 2: Specialized and literary vocabulary

Goal: Extend coverage to words a learner encounters in specific domains — technical fields, literary texts, formal/legal contexts.

- Academic vocabulary (論文 language, scientific terms)
- Business Japanese (beyond basic 敬語)
- Literary and archaic words encountered in novels and essays
- Medical, legal, and bureaucratic terms
- Internet slang and contemporary casual language

These words are lower frequency but high value when encountered, as they're harder to look up in general-purpose resources.

### Phase 3: Rare and historical vocabulary

Goal: Become a comprehensive reference, not just a learner's tool.

- Classical Japanese words that appear in proverbs or set phrases
- Regional dialect vocabulary
- Obsolete words needed for reading older texts
- Highly specialized technical terminology

This phase has no natural endpoint — the dictionary can keep growing indefinitely.

## Proper names and encyclopedia-type entries

A major intentional gap in the current dictionary is proper names and encyclopedic content. This includes:

- **Place names**: 東京, 京都, 北海道, 富士山, etc.
- **Personal names**: Historical figures, literary characters
- **Cultural terms**: 七五三, お盆, 節分 (some already exist as vocabulary)
- **Organization names**: NHK, 自民党, etc.
- **Brand/product names** that have entered common usage

### Why they're currently excluded

The existing entry schema is optimized for vocabulary: senses, example sentences showing usage in context, collocations, similar-word distinctions. Proper names don't fit this model well:

- Example sentences for 東京 wouldn't teach collocational patterns the way examples for a verb do
- The "notes" section would need to function more like an encyclopedia article
- Cross-references would work differently (geographical groupings, historical relationships)

### Proposed approach for proper names

**DECIDED 2026-08-11 (curator).** Proper nouns are in scope and the answer to almost every
question below turned out to be "no new format." What shipped:

| Question this section asked | What was decided |
|---|---|
| Lighter example requirements? | **No.** Proper nouns take the ordinary example and collocation requirements. The names worth entering are the ones with collocational behaviour to demonstrate, so the requirement selects the right headwords rather than obstructing them. |
| Encyclopedic notes? | **No.** Notes describe *language use* as in every other entry; referent facts belong in [expository articles](expository-articles.md). Non-obvious readings and register are in scope because they are language facts. |
| A new tag category? | **Yes, as ordinary tags** — `proper-noun` plus one of `place-name`, `person-name`, `organization-name`, `work-name`, `event-name`, `brand-name`. Filtering and browsing work through the existing tag machinery, not a parallel one. |
| Schema changes (relaxed validation / separate schema / `entry_type`)? | **None of the three.** `build/schema.json` is unchanged; proper nouns validate as ordinary entries. |
| Which names first? | **Collocationally and semantically rich ones** — names that carry usage beyond their referent. This supersedes the "when the time comes" ordering below, which stays as useful heuristics within that filter. |

The one problem the decision did **not** dissolve is a collision, not a format issue: a proper
noun whose surface *and* reading exactly match an existing common-noun entry is rejected by
`check_duplicate.py`'s exact word+reading rule (03515 {日光|にっこう} "sunlight" blocks the place
Nikko). The resolution is to add the proper-noun sense to the existing entry during polish, not
to create a second entry — the same shape as any other polysemy case.

The **priority** verdict below ("low for now") is also superseded: discovery runs actively
solicit proper nouns as of 2026-08-11 rather than deferring them behind comprehensive
vocabulary coverage.

Original 2026 analysis, kept for the reasoning:

A different entry format may be needed. Considerations:

**Lighter example requirements**: Proper names don't need 3+ progressive examples per sense. One or two examples showing typical usage patterns (e.g., how 東京 appears in sentences with particles) may suffice. The emphasis should shift from demonstrating collocational behavior to showing the word in natural context.

**Encyclopedic notes**: Instead of contrastive linguistics notes, proper name entries would need:
- What the name refers to (brief factual description)
- Reading(s), especially when non-obvious (e.g., place names with unusual readings)
- Cultural significance for learners
- Related vocabulary (e.g., 京都 → 舞妓, 抹茶, 寺)

**Categorization**: A new semantic tag category (e.g., `proper-noun-place`, `proper-noun-person`, `proper-noun-organization`) would allow filtering and browsing proper nouns separately.

**Schema changes**: Options include:
1. **Relaxed validation** for proper-noun entries (fewer required examples)
2. **Separate schema** for encyclopedic entries
3. **New entry type field** (`"entry_type": "encyclopedic"`) that triggers different validation and rendering

**Priority**: Low for now. The dictionary should first achieve comprehensive vocabulary coverage. Proper names can be looked up in many existing resources, while vocabulary entries with usage notes and examples are harder to find.

### Which proper names to include first

When the time comes:
1. Places that appear frequently in texts and conversation (major cities, regions, landmarks)
2. Historical and cultural terms that blur the line between proper noun and vocabulary (already partially covered — e.g., 正月, 花見)
3. Names needed to understand common expressions (e.g., 江戸 for 江戸時代)

## Long-term dictionary identity

As the dictionary grows beyond learner essentials, its identity may shift from "learner's dictionary" to "learner-friendly comprehensive dictionary." The key design principle should remain: **every entry is written with the learner in mind**, regardless of how rare the word is. Even a specialized term should have clear English explanations, furigana, and at least basic example sentences.

This distinguishes je-dict-1 from reference dictionaries (which assume native-speaker knowledge) and from pure learner dictionaries (which cap their vocabulary). The goal is to be both comprehensive and accessible.

## Related pages

- [Word Discovery Strategies](word-discovery-strategies.md) — how new words are found
- [Vocabulary Tier System](../project/vocabulary-tiers.md) — the three-tier classification
- [Corpus-Driven Entry Prioritization](corpus-prioritization.md) — frequency-based expansion
- [Content Pipeline](../project/content-pipeline.md) — how entries flow from discovery to publication
- [Vocabulary Size and Text Coverage](../research/vocabulary-size-coverage.md) — research on how many words learners need and dictionary sizing
- [Project Overview](../project/overview.md) — what the dictionary is and who it's for
- [Multilingual Dictionary](multilingual-dictionary.md) — the other major expansion axis: more target languages rather than more entries
