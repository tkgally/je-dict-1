# je-dict-1 Knowledge Base

A persistent, LLM-maintained knowledge base for the je-dict-1 Japanese-English learner's dictionary project. This wiki is written and maintained by Claude; the human curator directs research, asks questions, and guides priorities.

**Last updated**: 2026-04-05

## How this wiki is organized

| Directory | Purpose |
|-----------|---------|
| `project/` | About this dictionary — its purpose, architecture, content policies, and operational details |
| `research/` | Summaries of external knowledge — lexicography, SLA, corpus linguistics, Japanese grammar |
| `topics/` | Deep dives on specific dictionary-making decisions and design questions |
| `ideas/` | Future directions, feature proposals, and experimental concepts |

## Project

- [Project Overview](project/overview.md) — What je-dict-1 is, who it's for, and what makes it distinctive
- [Architecture and Build System](project/architecture.md) — Technical structure, build pipeline, deployment
- [Entry Design](project/entry-design.md) — Entry schema, required fields, quality standards
- [Vocabulary Tier System](project/vocabulary-tiers.md) — The three-tier classification (basic/core/general)
- [Content Pipeline](project/content-pipeline.md) — How entries are created, polished, and maintained
- [Quality Standards](project/quality-standards.md) — v2 quality standards and priority enhancements
- [Open Issues](project/open-issues.md) — Known problems, edge cases, and unresolved design questions

## Research

- [Learner Lexicography](research/learner-lexicography.md) — Principles of pedagogical dictionary design
- [Vocabulary Acquisition](research/vocabulary-acquisition.md) — How L2 learners acquire vocabulary
- [Japanese Lexicography](research/japanese-lexicography.md) — Challenges specific to Japanese dictionaries
- [Corpus Linguistics](research/corpus-linguistics.md) — Frequency data, corpora, and word selection
- [Digital Dictionary UX](research/digital-dictionary-ux.md) — Interface design and user behavior research
- [Translation Equivalence](research/translation-equivalence.md) — The bilingual mapping problem
- [Example Sentence Design](research/example-sentences.md) — What makes effective dictionary examples
- [Pitch Accent](research/pitch-accent.md) — Pitch accent systems, notation, and learner dictionary implications
- [Collocations in Learner Dictionaries](research/collocations.md) — Collocation types, L1 transfer effects, and dictionary presentation

## Topics

- [Furigana Strategy](topics/furigana-strategy.md) — When and how to annotate kanji with readings
- [Cross-Reference Design](topics/cross-references.md) — Linking related entries effectively
- [Handling Homographs](topics/homographs.md) — Disambiguation strategies for words with identical writing
- [Verb Transitivity Pairs](topics/verb-transitivity.md) — Presenting 自動詞/他動詞 pairs
- [Register and Formality](topics/register.md) — Marking casual/neutral/formal/honorific usage
- [Compound Verb Representation](topics/compound-verbs.md) — Entry-vs-pattern decisions for V1+V2 compound verbs

## Ideas

- [Audio Coverage Expansion](ideas/audio-expansion.md) — Strategies for increasing audio coverage beyond 1,028 entries
- [Sentence Mining Integration](ideas/sentence-mining.md) — Connecting the dictionary to SRS/Anki workflows
- [AI-Assisted Entry Review](ideas/ai-review.md) — Using LLMs for systematic quality improvement
- [Corpus-Driven Entry Prioritization](ideas/corpus-prioritization.md) — Using frequency data to guide expansion

## Log

See [log.md](log.md) for a chronological record of wiki sessions.
