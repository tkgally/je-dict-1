# Knowledge Base Log

Chronological record of wiki maintenance sessions. Each entry records what was done.

## [2026-04-05] maintenance | Counters research, audio expansion deepening, stats sync

**Session type**: Nightly maintenance

**Activities**:
- [A] Updated project/overview.md with current stats (22,200+ entries, 90,800+ examples, 5,200+ cross-refs, 19,400+ general tier)
- [B] Researched Japanese counters and classifiers in learner dictionaries — semantic categories, sound changes, acquisition challenges, dictionary treatment approaches; created research/counters-classifiers.md citing Downing (1996), Yamamoto & Keil, and Tofugu's tiered classification
- [C] Substantially expanded ideas/audio-expansion.md — added 2026 TTS landscape comparison (cloud and open-source), detailed implementation plan in 3 phases, storage/format considerations, cost estimates, quality assurance notes; updated entry count and audio coverage percentage
- Added cross-references from japanese-lexicography.md and vocabulary-acquisition.md to the new counters page

## [2026-04-05] maintenance | LLMs beyond flat corpora, LLMs as corpus replacements

**Session type**: Manual session (curator-directed)

**Activities**:
- [B] Researched LLM applications in lexicography — Rundell (2024), eLex 2025 proceedings, pragmatics surveys, Sydney Corpus Lab synthesis
- [D] Created research/beyond-flat-corpora.md — how LLMs enable semantic-pragmatic analysis that flat corpora cannot provide, covering word sense disambiguation in context, pragmatic function identification, register assessment, and discourse-level analysis
- [D] Created topics/llms-replacing-corpora.md — whether LLMs can replace traditional corpora in dictionary production, synthesizing Rundell's skepticism, the "trend toward the mean" argument, eLex 2025 consensus, a comparative strengths table, and implications for je-dict-1's LLM-primary workflow
- Both pages written in response to curator observations about LLM capabilities in this project

## [2026-04-05] maintenance | Collocations research, vocabulary acquisition deepening, stats update

**Session type**: Nightly maintenance

**Activities**:
- [A] Updated project/overview.md with current stats (nearly 22,000 entries, 90,000+ examples, 5,200+ cross-references)
- [A] Updated project/open-issues.md with corrected audio coverage percentage
- [B] Researched collocations in learner dictionaries — L1 transfer effects, Japanese-specific patterns, statistical measures, dictionary presentation approaches; created research/collocations.md
- [C] Substantially deepened research/vocabulary-acquisition.md — added sections on receptive vs. productive knowledge, formulaic sequences, dictionary lookup and retention research, and expanded implications
- [E] Checked all 107 cross-references across 27 wiki pages — no broken links found
- Added cross-references from corpus-linguistics.md, quality-standards.md, and vocabulary-acquisition.md to the new collocations page

## [2026-04-05] maintenance | Pitch accent research, register deepening, compound verbs

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched pitch accent in Japanese learner dictionaries; created research/pitch-accent.md covering accent patterns, notation systems, intelligibility research, existing resources (OJAD, NHK dictionary), and implications for je-dict-1
- [C] Substantially expanded topics/register.md — added sections on the two-axis register system (formality vs. politeness), schema field documentation, gendered language, keigo handling patterns, register in example sentences, register challenges for learner dictionaries, and an implementation roadmap
- [D] Created topics/compound-verbs.md — new page covering lexical vs. syntactic compound verbs, V2 auxiliary patterns, the entry-vs-pattern design decision, current je-dict-1 practice, the NINJAL Compound Verb Lexicon, and recommended approach

## [2026-04-05] initial | Knowledge Base Creation

**Session type**: Initial setup

Created the knowledge base structure:
- Directory layout: `project/`, `research/`, `topics/`, `ideas/`
- Index file with page catalog
- 7 project pages covering overview, architecture, entry design, tiers, pipeline, quality, and open issues
- 7 research pages synthesizing external knowledge on lexicography, SLA, corpus linguistics, etc.
- 5 topic pages on specific design decisions (furigana, cross-refs, homographs, transitivity, register)
- 4 idea pages for future directions
- Maintenance session prompt at `planning/maintain-knowledge-base.md`
