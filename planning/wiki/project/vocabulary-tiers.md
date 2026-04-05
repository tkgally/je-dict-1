# Vocabulary Tier System

**Last updated**: 2026-04-05

## Overview

je-dict-1 uses an original three-tier vocabulary classification instead of JLPT levels. This system was designed to be pedagogically meaningful rather than exam-oriented.

## The three tiers

### Basic (~800 entries, closed)

Foundational survival vocabulary. Words a learner needs from day one: numbers, colors, family terms, basic verbs (する, ある, いく), common greetings. This tier is frozen — no entries are added or removed.

### Core (~2,000 entries, closed)

Essential vocabulary for functioning as an adult in Japanese society. Covers everyday topics: work, shopping, health, transportation, weather, food. A learner who knows all basic + core words can handle most daily situations. This tier is also frozen.

### General (16,000+ entries, growing)

All other vocabulary. Ranges from common words that just missed the core cutoff to specialized terms, literary vocabulary, and technical language. All new entries are added to this tier.

## Design rationale

### Why not JLPT levels?

JLPT (Japanese Language Proficiency Test) levels N5-N1 are the most common vocabulary classification for Japanese learners, but they have significant problems:

- **Exam-oriented**: JLPT levels reflect what's tested, not what's most useful for communication
- **Inconsistent boundaries**: The N3/N2 boundary is particularly arbitrary
- **No official word list**: JLPT doesn't publish an official vocabulary list; available lists are community-reconstructed
- **Poor granularity at high levels**: N1 is a massive, undifferentiated pool
- **Cultural bias**: Favors academic/formal vocabulary over practical spoken language

### Why three tiers instead of five (or more)?

- Simpler to maintain and explain
- The basic/core distinction (survival vs. functioning) is pedagogically clear
- The open "general" tier avoids the problem of arbitrarily ranking advanced vocabulary
- No false precision — it's hard to meaningfully distinguish "N2 vocabulary" from "N1 vocabulary"

## Self-containment principle

Within the basic and core tiers, definitions and examples should be largely self-contained — they shouldn't require vocabulary from higher tiers to understand. General-tier entries have no such restriction.

## Relationship to frequency

The tiers correlate loosely with frequency but are not strictly frequency-based. Some very frequent words (e.g., topic particles, basic conjunctions) are in the basic tier because they're foundational, while some moderately frequent words were placed in general because they serve narrower communicative functions.

## Future considerations

- Should the general tier have sub-bands (e.g., "common general" vs. "specialized")?
- Could frequency data from BCCWJ or other corpora inform tier boundaries retroactively?
- Is there value in a "recognition" tier for words learners should understand but not produce?

## Related pages

- [Project Overview](overview.md)
- [Corpus Linguistics](../research/corpus-linguistics.md)
- [Vocabulary Acquisition](../research/vocabulary-acquisition.md)
- [Corpus-Driven Entry Prioritization](../ideas/corpus-prioritization.md)
