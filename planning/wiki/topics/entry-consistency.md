# Consistency in Form and Content Among Similar Entries

**Last updated**: 2026-08-04

## Overview

As the dictionary grows past 27,500 entries, inconsistencies in how similar types of entries present information become increasingly visible. This page analyzes the consistency problem, identifies the most important areas for standardization, and proposes strategies for achieving greater uniformity without losing the flexibility that makes individual entries useful. Since Phase 10 of the Enhancement Plan 2026, `build/check_consistency.py` now operationalizes several of the detection ideas below.

## The consistency problem

### How inconsistencies arise

1. **Temporal drift**: Entries created in January 2026 follow different conventions than entries created in April 2026. Quality standards evolved significantly over this period.
2. **Batch variation**: Even within a single session, Claude's output varies slightly — different phrasing for similar concepts, different organizational choices for notes.
3. **Schema evolution**: The entry schema has grown (adding conjugations, cross-references, inline links), but older entries weren't always back-filled.
4. **Prompt evolution**: The prompts and skills guiding entry creation have been refined over time, meaning newer entries follow stricter guidelines.
5. **Context limitations**: In batch creation sessions of 30 entries, later entries in the batch may receive less attention as context fills up.

### Why consistency matters

- **Learner trust**: If two similar verbs have notes structured differently, learners may wonder if one is missing information or if the difference is meaningful.
- **Comparability**: When a learner looks at 走る and then 歩く, the notes should make it easy to compare their usage patterns.
- **Predictability**: Users who learn the entry structure for one word should know where to find the same type of information in another entry.
- **Maintenance**: Consistent entries are easier to validate, update, and cross-reference programmatically.

## Key areas for consistency improvement

### 1. Notes section structure

**Current state**: Notes vary widely in organization, length, and content categories. Some entries have well-structured notes with headers; others have a single paragraph.

**Target**: Similar entries should have similar note structures. For example, all transitive-intransitive verb pairs should:
- Mention the paired verb prominently
- Explain the usage difference
- Provide collocations for the entry's specific verb
- Note any meaning shifts between the pair

**Proposed standard structures by POS**:

**Verbs**:
1. Core usage explanation (when needed beyond the definitions)
2. Transitivity and paired verb
3. Aspect/ている behavior (if non-obvious)
4. Common collocations
5. Particle patterns
6. Similar verbs / distinctions
7. Register and formality notes
8. Cultural or pragmatic notes (where relevant)

**Na-adjectives**:
1. Core usage explanation
2. Predicate vs. modifier usage patterns
3. Common collocations (noun + な + noun patterns)
4. Similar adjectives / distinctions
5. Degree/intensity patterns
6. Register notes

**Nouns**:
1. Core explanation
2. Common collocations (verb patterns)
3. Compound words and derived forms
4. Similar words / distinctions
5. Cultural context (where relevant)

### 2. Cross-reference consistency

**Current state**: ~13,900 cross-references across ~26,500 entries, but coverage is uneven. Some semantic clusters are well-linked; others have no cross-references at all.

**Target consistency goals**:
- All transitivity pairs linked bidirectionally via `prominent_see_also`
- All antonym pairs linked bidirectionally
- Semantic field neighbors linked (e.g., all season words cross-reference each other)
- Entries mentioned in notes always have a corresponding cross-reference
- Relationship labels used consistently (not "synonym" in one direction and "related" in the other)

**Specific issues to address**:
- Some entries have `prominent_see_also` for relationships that should be regular `cross_references`
- Relationship labels aren't always symmetric (if A→B is "antonym", B→A should also be "antonym")
- Some cross-references point to entries that no longer exist (after merges)

### 3. Gloss and definition style

**Target conventions**:
- First gloss should be the most common, general meaning
- Glosses should use consistent grammatical form (noun glosses for nouns, verb glosses for verbs)
- Definitions that explain rather than just translate should use consistent introductory patterns
- Avoid glosses that are too specific (narrower than the Japanese word) or too broad (wider than the Japanese word)

### 4. Example sentence patterns

**Target conventions** (many already in the example-sentences skill):
- Minimum 3 examples per sense
- Progressive length: short → medium → long
- First example should clearly demonstrate the core meaning
- Avoid examples that could work for a different sense of the same word
- Consistent translation style (natural English, not word-for-word)

### 5. Notes tone and style

**Current variation**: Some notes are list-heavy (bullets of related words with no explanation). Others are discursive and explanatory. The curator has expressed preference for moving toward more discursive, explanatory notes.

**Target**: Notes should:
- Lead with explanation, not lists
- Use lists for collocations and similar words, but introduce them with context
- Explain *why* distinctions matter, not just *that* they exist
- Be written for a learner, not a linguist — accessible prose, not jargon

## Strategies for achieving consistency

### Programmatic detection

Build tools to flag inconsistencies:
- Entries of the same POS missing expected note sections (e.g., verbs without transitivity mention)
- Cross-reference asymmetries (A→B exists but B→A doesn't)
- Note length outliers (much shorter or longer than peers of the same POS)
- Entries with no collocations listed
- Entries with no similar-word distinctions

Some of this is already partially covered by `report.py` and `validate_tags.py`, but more targeted consistency checks could be added.

### Template-driven revision

Create "consistency templates" for each entry type that a polishing prompt can compare against:
- Load template for the entry's POS
- Check which sections are present/missing
- Suggest additions for missing sections
- Flag sections that deviate from the template structure

### Cluster-based review

Instead of reviewing entries one at a time (the current polishing approach), review semantic clusters together:
- Pull all entries in a cross-reference cluster
- Ensure they present information comparably
- Ensure cross-references are complete and symmetric
- Check that contrastive notes are consistent from both sides

This is especially important for:
- Transitivity pairs
- Synonym groups
- Antonym pairs
- Semantic field sets (days of week, colors, family terms, etc.)

### Cross-model consistency checking

The [multi-model proofreading](../ideas/multi-model-proofreading.md) system could include a consistency dimension: show a reviewer model two related entries side by side and ask it to identify inconsistencies in structure, depth, or presentation.

## The entry-internal contradiction: the consistency defect that costs nothing to find

**Added 2026-08-04.** Everything above treats consistency as a *between-entry* property — do
parallel entries present information comparably? That framing is what makes consistency work
expensive: comparing entries means enumerating a cluster, a family, or a whole range before any
defect is visible, and most of the instruments this file proposes are ways of paying that cost.

A year of backlog measurements has surfaced a second class that behaves completely differently.
An **entry-internal contradiction** is a defect where two fields of the *same* entry disagree with
each other. No cluster, no corpus scan, no model: open the file, compare two fields, decide. Every
instance found so far was found this way, and each one is a true positive by construction — the
entry cannot be right both ways.

| Contradiction | Fields that disagree | Measured scope |
|---|---|---|
| Prose says the verb is already a potential form; the conjugation table still generates a potential of it | `notes`/`gloss` vs `conjugation.forms` | 6 exact, ~15 with the known list ([P41](../ideas/cleanup-backlog.md#priority-41-conjugation-tables-generate-the-potential-of-a-verb-that-is-already-potential)) |
| Notes say the word is the everyday form; the tag says `formality: "formal"` | `notes` vs `tags.formality` | 24 katakana entries carry `formal`; several self-refuting ([P37 update](../ideas/cleanup-backlog.md#priority-37-politeness-polite-on-plain-vocabulary--and-the-detector-that-reports-zero)) |
| `explanation` is a verbatim copy of the sense's own `gloss` | `definitions[].explanation` vs `.gloss` | 201 senses / 179 entries ([P39](../ideas/cleanup-backlog.md#priority-39-definitionsexplanation-is-a-verbatim-copy-of-its-own-gloss-201-senses-179-entries)) |
| `tags.verb_class` says `suru`; `tags.pos` says `verb-godan` (or the reverse) | tag vs tag | 5 live, all fixed 2026-08-03 ([Tooling 71](../ideas/tooling-backlog.md)) |
| Free-text `part_of_speech` states transitivity; `tags.transitivity` is absent | display field vs structured tag | 50 ([P22 update](../ideas/cleanup-backlog.md#priority-22-inconsistent-free-text-part_of_speech-display-field)) |
| An inline link's declared base form contradicts its target entry's headword | link label vs target | detector exists, ratchet missing ([Tooling 65](../ideas/tooling-backlog.md)) |

**Why this class deserves its own name.** The project's most expensive quality instrument is the
cross-model accuracy review, and the [deterministic-vs-semantic](deterministic-vs-semantic-tasks.md)
analysis established the rule that you should pay a model for *judgment*, never for *detection*
that has a mechanical signature. Entry-internal contradictions are the extreme case of that rule:
detection is not merely mechanical, it is nearly free — one file open, one comparison — and there
is no false-positive family to calibrate against, because a self-contradicting entry is wrong
whichever way it is resolved.

They are also the class most likely to be *created* rather than inherited. Every instance in the
table above arrived through a generator or a batch: a conjugation script that applies correct
morphology to a verb whose semantics forbid it, a creation template that stamps `formal` on a
whole loanword cohort, a generation run that fills `explanation` by copying `gloss`. That is why
the recurring recommendation in the tooling backlog is a **ratchet rather than a sweep** — the
population is small at any moment and regenerates continuously, so a check that runs forever beats
a queue that is drained once.

**Practical consequence for consistency work**: before designing a cluster-based review (the
expensive instrument this page recommends), scan for the contradictions the entries already
contain. They are cheaper to find, they are unarguable, and — because they come from generators —
fixing the generator retires the defect instead of the batch.

## Relationship to other initiatives

- **Expository articles** ([ideas/expository-articles.md](../ideas/expository-articles.md)): Articles synthesize information across entries, which naturally reveals and motivates fixing inconsistencies
- **Parallel agent architecture** ([ideas/parallel-agent-architecture.md](../ideas/parallel-agent-architecture.md)): Consistency checking could be parallelized — different agents reviewing different semantic clusters
- **Cross-reference rollout**: The ongoing cross-reference work is itself a consistency initiative

## Priority actions

1. **Define note structure templates** for each major POS (verb, na-adj, i-adj, noun, counter, expression)
2. **Build a consistency checker** that compares entry notes against templates and flags gaps
3. **Pilot cluster-based review** on a well-defined semantic group (e.g., color terms, or a set of transitivity pairs)
4. **Establish style guide** for notes prose — consistent tone, consistent depth, consistent use of explanation vs. lists

## Related pages

- [Quality Standards](../project/quality-standards.md) — the target standards entries should meet
- [Cross-Reference Design](cross-references.md) — cross-reference consistency specifically
- [Entry Design](../project/entry-design.md) — the entry schema
- [Multi-Model Proofreading](../ideas/multi-model-proofreading.md) — cross-model consistency checking
- [Expository Articles](../ideas/expository-articles.md) — articles that could drive consistency improvements
- [Dictionary Evaluation and Metalexicography](../research/dictionary-evaluation-metalexicography.md) — consistency as one dimension of systematic dictionary evaluation
- [Deterministic vs Semantic Tasks](deterministic-vs-semantic-tasks.md) — why detection and judgment should be paid for separately; entry-internal contradictions are the extreme case
- [Cleanup Backlog](../ideas/cleanup-backlog.md) / [Tooling Backlog](../ideas/tooling-backlog.md) — where the individual contradiction measurements are filed
