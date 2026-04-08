# je-dict-1 Knowledge Base

A persistent, LLM-maintained knowledge base for the je-dict-1 Japanese-English learner's dictionary project. This wiki is written and maintained by Claude; the human curator directs research, asks questions, and guides priorities.

**Last updated**: 2026-04-08

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
- [Beyond Flat Corpora](research/beyond-flat-corpora.md) — LLMs and semantic-pragmatic analysis beyond distributional patterns
- [Japanese Counters and Classifiers](research/counters-classifiers.md) — The numeral classifier system, acquisition challenges, and dictionary treatment
- [Onomatopoeia and Mimetic Words](research/onomatopoeia-mimetics.md) — Sound symbolism, morphological patterns, L2 acquisition, and dictionary treatment
- [Word Formation and Morphology](research/word-formation.md) — Compounding, derivation, vocabulary strata, and implications for entry scope
- [Definition and Gloss Strategies](research/definition-strategies.md) — Equivalence types, gloss writing techniques, and sense ordering for bilingual learner dictionaries
- [Dictionary Lookup Behavior](research/dictionary-lookup-behavior.md) — Lookup process models, common errors, and implications for dictionary design

## Topics

- [Furigana Strategy](topics/furigana-strategy.md) — When and how to annotate kanji with readings
- [Cross-Reference Design](topics/cross-references.md) — Linking related entries effectively
- [Handling Homographs](topics/homographs.md) — Disambiguation strategies for words with identical writing
- [Verb Transitivity Pairs](topics/verb-transitivity.md) — Presenting 自動詞/他動詞 pairs
- [Register and Formality](topics/register.md) — Marking casual/neutral/formal/honorific usage
- [Compound Verb Representation](topics/compound-verbs.md) — Entry-vs-pattern decisions for V1+V2 compound verbs
- [LLMs as Lexicographic Corpus Replacements](topics/llms-replacing-corpora.md) — Whether and how LLMs can supplement or replace traditional corpora
- [Entry Consistency](topics/entry-consistency.md) — Achieving uniformity in form and content among similar entries
- [Word Variants](topics/word-variants.md) — Handling words with multiple written forms (kanji variants, okurigana, kanji vs. kana)
- [Deterministic vs. Semantic Tasks](topics/deterministic-vs-semantic-tasks.md) — Which editorial tasks can be automated and which require LLM judgment

## Ideas

- [Audio Coverage Expansion](ideas/audio-expansion.md) — Strategies for adding TTS-based pronunciation audio
- [Sentence Mining Integration](ideas/sentence-mining.md) — Connecting the dictionary to SRS/Anki workflows
- [AI-Assisted Entry Review](ideas/ai-review.md) — Using LLMs for systematic quality improvement
- [Corpus-Driven Entry Prioritization](ideas/corpus-prioritization.md) — Using frequency data to guide expansion
- [Multi-Model Proofreading](ideas/multi-model-proofreading.md) — Systematic cross-model verification via OpenRouter
- [Expository Articles](ideas/expository-articles.md) — Standalone articles on vocabulary topics for browsing
- [Parallel Agent Architecture](ideas/parallel-agent-architecture.md) — Autonomous parallel revision and improvement system
- [Word Discovery Strategies](ideas/word-discovery-strategies.md) — LLM brainstorming, scenario-based gaps, and other approaches for finding missing words
- [Dictionary Growth and Long-Term Vision](ideas/dictionary-growth.md) — No maximum size, proper names, long-term expansion phases

## Log

See [log.md](log.md) for a chronological record of wiki sessions.
