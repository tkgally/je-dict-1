# Knowledge Base Log

Chronological record of wiki maintenance sessions. Each entry records what was done.

## [2026-04-07] maintenance | Definition strategies research, learner lexicography deepening, stats sync

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched definition and gloss writing strategies for bilingual learner dictionaries — Adamska-Sałaciak's equivalence typology (translational, cognitive, explanatory, functional), Zgusta's degrees of equivalence, sense ordering approaches, Japanese-English specific challenges; created research/definition-strategies.md citing Adamska-Sałaciak (2010), Atkins & Rundell (2008), Zgusta (1971), Lew (2004)
- [C] Substantially expanded research/learner-lexicography.md — added sections on the monolingual vs. bilingual debate (Laufer & Hadar 1997, Laufer & Kimmel 1997, Lew 2004), bilingualised dictionaries, dictionary structure terminology (macrostructure/microstructure/mediostructure/access structure), frame semantics and prototype theory foundations, production vs. reception comparison table; expanded references and related pages
- [A] Updated entry counts across 14 wiki pages: entries 22,400→22,700, general tier 19,600→19,900, cross-references 5,400→5,700, candidates 3,750→3,470; updated audio expansion estimates, parallel architecture, multi-model proofreading, compound verbs, pitch accent, LLMs-as-corpora, and word discovery pages accordingly
- Added cross-references from translation-equivalence.md and learner-lexicography.md to the new definition-strategies page
- Updated index.md with 1 new page entry

## [2026-04-06] maintenance | Word formation research, stats sync, lint check

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched Japanese word formation and morphology for learner dictionaries — vocabulary strata (wago/kango/gairaigo), compounding patterns, productive affixes, derivation, abbreviation, morphological awareness research (Kondo-Brown 2006, Mori & Nagy 1999); created research/word-formation.md citing Kageyama (2016), Halpern, CJK Dictionary Institute, Ito & Mester (2015)
- [A] Updated entry counts across 7 wiki pages: entries 22,200→22,400, general tier 19,400→19,600, candidates 4,000→3,750, cross-references 5,300→5,400, examples 90,800→91,700; updated audio expansion estimates accordingly
- [E] Audited all cross-references across 40 wiki pages — no broken links, no orphan pages, all "Last updated" dates current (2026-04-04 or later)
- Added cross-references from japanese-lexicography.md, vocabulary-acquisition.md, and compound-verbs.md to the new word-formation page
- Updated index.md with 1 new page entry

## [2026-04-06] maintenance | Deterministic vs. semantic task analysis

**Session type**: Manual session (curator-directed)

**Activities**:
- [D] Created topics/deterministic-vs-semantic-tasks.md — comprehensive analysis of which editorial tasks can be automated deterministically and which require LLM semantic judgment. Covers: historical context (early project experience with Claude writing scripts), the two-layer architecture, complete taxonomy of all 22+ deterministic scripts and 12+ semantic tasks, detailed analysis of hybrid tasks, deep dives into why specific tasks (furigana, cross-references, examples, semantic labels) resist automation, the "trend toward the mean" advantage for lexicographic work, automatable components within semantic tasks, design principles distilled from project experience, and implications for future development
- [F] Synthesized information across prompts, skills, and build scripts to document the project's hard-won lessons about the boundary between programmatic and editorial work
- Updated index.md with 1 new page entry

## [2026-04-06] maintenance | Onomatopoeia research, UX deepening, cross-ref additions

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched Japanese onomatopoeia and mimetic words — classification system, morphological patterns, phonosemantics (Hamano 1998), L2 acquisition challenges, dictionary treatment approaches; created research/onomatopoeia-mimetics.md citing Hamano, Iwasaki & Yoshioka, Feng, and Inose
- [C] Substantially expanded research/digital-dictionary-ux.md — added detailed analysis of je-dict-1's current search architecture (three parallel indexes, match strategies, tag-based browsing), documented 8 specific improvement opportunities with implementation notes, added inflected form search as a high-value opportunity using existing conjugation data, added entry page UX section
- [E] Added cross-references from japanese-lexicography.md, translation-equivalence.md, and expository-articles.md to the new onomatopoeia page; checked all wiki cross-references for broken links
- Updated index.md with 1 new page entry

## [2026-04-06] maintenance | Cross-check accuracy, word discovery strategies, growth vision, cross-ref expansion

**Session type**: Manual session (curator-directed)

**Activities**:
- [E] Fixed outdated audio references in open-issues.md and audio-expansion.md — audio files were removed in early 2026 but wiki still referenced ~1,028 entries with audio
- [E] Updated outdated counts: cross-references (3,400→5,300+), candidates (5,400→4,000), general tier (16,000→19,400+) across multiple pages
- [A] Updated content-pipeline.md to reflect LLM brainstorming as the primary candidate discovery method
- [D] Created ideas/word-discovery-strategies.md — comprehensive analysis of brainstorming pros/cons, 7 proposed alternative discovery methods (scenario-based, textbook mining, user simulation, reverse cross-ref mining, kanji productivity, semantic field audits, learner error analysis), safeguards against missing basic vocabulary
- [D] Created ideas/dictionary-growth.md — no maximum size policy, three growth phases, proper names/encyclopedia entry design discussion, long-term dictionary identity
- [C] Substantially expanded topics/cross-references.md — added sections on why cross-refs matter for browsing (vocabulary networks, serendipitous learning, disambiguation), improvement ideas (higher coverage targets, automated suggestions, quality review, navigational improvements, typed browsing paths, completeness metrics)
- [C] Added tier reassessment section to project/vocabulary-tiers.md — noting that basic/core assignments need rechecking since they were made early in the project
- [C] Added proper names design question to project/open-issues.md
- Updated index.md with 2 new page entries

## [2026-04-06] maintenance | Major expansion — proofreading, articles, consistency, parallelism, word variants

**Session type**: Manual session (curator-directed)

**Activities**:
- [D] Created ideas/multi-model-proofreading.md — comprehensive plan for systematic cross-model entry verification via OpenRouter, covering furigana, glosses, examples, notes; two-pass review architecture; implementation roadmap in three phases; cost estimates
- [D] Created ideas/expository-articles.md — proposal for standalone articles on vocabulary topics (counters, keigo, onomatopoeia families, etc.) to support browsing and serendipitous discovery; article types, format options, implementation plan, prioritization
- [D] Created topics/entry-consistency.md — analysis of consistency problems in note structure, cross-references, glosses, and examples across similar entries; proposed standard note structures by POS; strategies including template-driven revision and cluster-based review
- [D] Created ideas/parallel-agent-architecture.md — design for autonomous parallel agent system; four architecture options analyzed (file-based, task-based, claim-based, branch-per-agent) with hybrid recommendation; three-phase transition plan; quality safeguards
- [D] Created topics/word-variants.md — policy framework for handling words with multiple written forms (kanji variants, okurigana, kanji vs. kana, reading variants); when to create separate entries vs. consolidate; search index implications; data model considerations
- [C] Expanded ideas/ai-review.md — added links to new multi-model proofreading and parallel architecture pages; reorganized into review strategies and implementation approaches sections
- [C] Updated project/open-issues.md — added new design questions (word variants, entry consistency, expository articles) and process issues (sequential bottleneck, single-model risk); expanded related pages
- [E] Updated index.md with 5 new page entries (2 topics, 3 ideas)
- All new pages incorporate insights from the curator's about.html blog entries and respond to specific curator priorities communicated in this session

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
