# Vocabulary Tier System

**Last updated**: 2026-08-07 (added the two open headword-scope questions — person names, and number+counter compounds)

## Overview

je-dict-1 uses an original three-tier vocabulary classification instead of JLPT levels. This system was designed to be pedagogically meaningful rather than exam-oriented.

## The three tiers

### Basic (~800 entries, closed)

Foundational survival vocabulary. Words a learner needs from day one: numbers, colors, family terms, basic verbs (する, ある, いく), common greetings. This tier is frozen — no entries are added or removed.

### Core (~2,000 entries, closed)

Essential vocabulary for functioning as an adult in Japanese society. Covers everyday topics: work, shopping, health, transportation, weather, food. A learner who knows all basic + core words can handle most daily situations. This tier is also frozen.

### General (27,461 entries, growing)

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

This principle is the functional analogue of the **controlled defining vocabulary** tradition in monolingual English learner dictionaries like LDOCE and COBUILD — see [Controlled Defining Vocabulary](../research/controlled-defining-vocabulary.md). Where LDOCE enforces a ~2,000-word English defining vocabulary across all definitions, je-dict-1 enforces a roughly 2,800-word Japanese vocabulary (basic + core) for examples and notes in those tiers. The **inline word link system** (`⟦…⟧`) extends this discipline into the general tier by hyperlinking non-basic vocabulary in examples, giving readers an explicit escape hatch instead of forcing paraphrase.

## Relationship to frequency

The tiers correlate loosely with frequency but are not strictly frequency-based. Some very frequent words (e.g., topic particles, basic conjunctions) are in the basic tier because they're foundational, while some moderately frequent words were placed in general because they serve narrower communicative functions.

## Tier reassessment needed

The basic and core tiers were assigned early in the project, when the dictionary was much smaller. Since then, thousands of general-tier entries have been added, and it is likely that some of these should be in the basic or core tiers. For example, a common everyday word added later in the project may have been placed in general simply because the basic/core tiers were already marked as "closed."

A systematic reassessment is planned:
- **Review general-tier entries** for words that are clearly basic or core level (survival vocabulary, essential adult communication)
- **Review basic/core entries** for any that might be less fundamental than newer general entries
- **Keep total counts approximately the same** — basic should stay around ~800, core around ~2,000. This means any promotions should be balanced by demotions or the thresholds should be explicitly expanded
- **Criteria**: Use communicative need as the primary criterion (not raw frequency). A word belongs in basic if a learner needs it from day one; in core if an adult needs it for daily life
- **Process**: This should be done in a dedicated session with careful review, not as a side effect of other work

Until reassessment is complete, the tiers remain closed to new additions — all new entries continue to go in the general tier.

## Two open headword-scope questions (2026-08-07)

Neither of these is a tier question — both are prior to tiering, because they ask whether a
string is a headword at all. Both surfaced because consecutive `new-entries` runs made
*different* decisions about the same class, which is the signal that the rule is missing rather
than merely unwritten. Both are routed to the curator.

**1. Are person names in scope?** `candidate_words.json` contains proper-noun person names —
C22806 夏目漱石, harvested from entry 06801. The dictionary already has place names (東京,
富士山), so proper nouns as a category are not excluded; but there are no biographical
headwords, and a biographical entry needs a different shape (dates, significance, works) than
the entry schema currently expresses. The 2026-08-06 `new-entries` run skipped the candidate
rather than guess. Until the curator answers, such candidates will accumulate and be skipped
individually by every run that meets them.

**2. When is a number+counter compound entry-worthy?** Two consecutive runs disagreed. The
2026-08-06 run skipped C22795 三十人 as "purely compositional"; the 2026-08-07 run created it,
on the evidence that 10978 三人, 28475 十人 and 10985 百人 are all existing entries — i.e. the
dictionary's own practice already contradicted the "compositional" reasoning. The 08-07
decision is the consistent one, but consistency reached by inspecting neighbours is expensive
and will not survive the next run that does not think to look.

The rule that would settle it, and that both runs would have applied the same way:
**a number+counter combination is entry-worthy when the counter's reading changes in that
combination (三人 さんにん, 十人 じゅうにん, 一杯 いっぱい) or when the combination is a common
round figure.** Purely regular combinations (三十人 さんじゅうにん) are compositional by that
test — which would have meant *skipping* C22795, the opposite of what was decided, so writing
the rule down is a real decision and not a rationalisation of current practice.

**[skill] recommendation** (wiki sessions do not modify skills): the rule belongs in
`find-candidates` or `vocabulary-tiers`, whichever the curator prefers as the gate.

## Future considerations

- Should the general tier have sub-bands (e.g., "common general" vs. "specialized")?
- Could frequency data from BCCWJ or other corpora inform tier boundaries retroactively?
- Is there value in a "recognition" tier for words learners should understand but not produce?

## Related pages

- [Project Overview](overview.md)
- [Corpus Linguistics](../research/corpus-linguistics.md)
- [Dictionary Growth](../ideas/dictionary-growth.md)
- [Vocabulary Acquisition](../research/vocabulary-acquisition.md)
- [Controlled Defining Vocabulary](../research/controlled-defining-vocabulary.md) — the monolingual-dictionary tradition that the tier system parallels
- [Vocabulary Size and Text Coverage](../research/vocabulary-size-coverage.md) — how the tier system maps to research on lexical thresholds
- [Corpus-Driven Entry Prioritization](../ideas/corpus-prioritization.md)
- [Japanese Vocabulary Grading](../research/japanese-vocabulary-grading.md) — BCCWJ frequency data, JLPT limitations, and why je-dict-1 uses a pedagogical rather than exam-based system
