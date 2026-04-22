# Knowledge Base Log

Chronological record of wiki maintenance sessions. Each entry records what was done.

## [2026-04-22] maintenance | Grammar information research, stats sync, cross-reference lint

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **grammar information in learner dictionaries** and created `research/grammar-in-dictionaries.md`. Covers four encoding strategies (opaque codes, semi-transparent codes, natural-language descriptions, grammar-through-examples), the historical trend from Hornby's verb tables to COBUILD's definitions; the consultation gap (Nesi & Haill 2002, Tono 2001, Herbst 1989) showing learners largely ignore coded grammar; Frankenberg-Garcia's (2012–2015) encoding examples concept; Japanese-specific challenges (particle-verb dependencies, transitivity pairs, conjugation complexity, ている aspect polysemy, keigo); the Makino & Tsutsui grammar dictionary model; Herbst's valency dictionary approach; and detailed implications for je-dict-1 including what the dictionary already does well (natural-language notes, conjugation tables, transitivity marking) and five areas for improvement (particle templates, encoding-optimized examples, contrastive grammar notes, structured particle fields, grammar-entry cross-references). Cited Atkins & Rundell 2008, Frankenberg-Garcia 2012/2014/2015, Herbst 1989/2004, Hornby 1942, Makino & Tsutsui 1986/1995, Nesi & Haill 2002, Sinclair 1987, Tono 2001, Wekker 1992.
- [A] Updated entry counts across 15 wiki pages to reflect 2026-04-22 `report.py` output (24,760 entries / 21,977 general / 8,801 cross-references / 99,747 examples / 1,584 candidates / 45.0% symmetry / 4,062 asymmetric refs / 2,847 entries with inline links at 11.5%). Updated pages: `project/overview.md`, `project/vocabulary-tiers.md`, `project/entry-design.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, `topics/enhancement-plan-retrospective.md`, `topics/compound-verbs.md`, `ideas/audio-expansion.md`, `ideas/dictionary-growth.md`, `ideas/multi-model-proofreading.md`, `ideas/parallel-agent-architecture.md`, `ideas/word-discovery-strategies.md`, `research/controlled-defining-vocabulary.md`, `research/digital-dictionary-ux.md`, `research/pitch-accent.md`.
- [E] Ran cross-reference link checker across all wiki pages (359+ internal links checked, 0 broken). Added the new grammar page to `index.md` and as a related page on `learner-lexicography.md`, `example-sentences.md`, `entry-design.md`, `verb-transitivity.md`, `dictionary-lookup-behavior.md`, `definition-strategies.md`, and `collocations.md`. Updated "Last updated" dates on all modified pages.

## [2026-04-17] maintenance | Polysemy research, stats sync, cross-reference lint

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **polysemy and sense discrimination** in learner dictionaries and created `research/polysemy-sense-discrimination.md`. Covers the ontological debate (Kilgarriff 1997), lumping vs. splitting trade-offs (with bilingual dictionary considerations), three sense-ordering approaches (historical, frequency, logical/core-first), Bond et al. (2024) models of polysemy structure (prototype, progenitor, nearest-neighbor chaining, local chaining), cognitive linguistics and prototype theory, Japanese-specific challenges (extreme polysemy in basic verbs, kanji as sense disambiguator, compound verb extensions), Hoshino & Shimizu (2018) on learner mental lexicon organization, and detailed implications for je-dict-1 including quantitative analysis of the current sense distribution (19,005 single-definition entries, 4,504 with 2 definitions, 478 with 3+, none with example-to-sense linking). Recommendations include documenting a sense-ordering convention, adding example-sense linking, reviewing high-polysemy entries, and adding sense relationship markers. Cited Atkins & Rundell 2008, Bond et al. 2024, Geeraerts 2006, Hoshino & Shimizu 2018, Kilgarriff 1997, Lew 2013, Lu & Geng 2024, McCrae et al. 2022, Nesi 1999.
- [A] Updated entry counts across 12 wiki pages to reflect 2026-04-17 `report.py` output (23,987 entries / 21,204 general / 7,787 cross-references / 97,124 examples / 2,366 candidates / 44.9% symmetry / 3,660 asymmetric refs). Updated pages: `project/overview.md`, `project/vocabulary-tiers.md`, `project/open-issues.md`, `research/controlled-defining-vocabulary.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, `topics/enhancement-plan-retrospective.md`, `topics/compound-verbs.md`, `ideas/audio-expansion.md`, `ideas/dictionary-growth.md`, `ideas/multi-model-proofreading.md`, `ideas/parallel-agent-architecture.md`, `ideas/word-discovery-strategies.md`, `research/digital-dictionary-ux.md`, `research/pitch-accent.md`.
- [E] Ran cross-reference link checker across all 40+ wiki pages (350 internal links checked, 0 broken). Added the new polysemy page to `index.md` and as a related page on `definition-strategies.md`, `vocabulary-acquisition.md`, `homographs.md`, and `learner-lexicography.md`. Updated "Last updated" dates on all modified pages.

## [2026-04-15] maintenance | Controlled defining vocabulary research, stats sync, tier-system cross-link

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **controlled defining vocabulary** (CDV) and created `research/controlled-defining-vocabulary.md`. Covers the historical arc from Ogden's Basic English (1930) through West's General Service List (1953) to LDOCE's explicit ~2,000-word defining vocabulary (Procter 1978) and COBUILD's full-sentence definition style (Sinclair 1987); what a CDV accomplishes (non-circularity, reading-level control, stylistic consistency, computational tractability); its criticisms (naturalness trade-offs, intra-CDV circularity, polysemy within defining words, L2-specific pragmatics); treatment in bilingual and Japanese-English dictionaries; and a detailed analysis of how je-dict-1's closed basic+core tiers plus the inline-word-link system function as an analogue of the CDV tradition. Concrete recommendations include keeping the closed-tier policy as a hard constraint, adding an automated self-containment linter, and adopting soft-CDV discipline for the English notes field. Cited Adamska-Sałaciak 2016, Hanks, Herbst 1996, Nation 2001/2013, Ogden 1930, Procter 1978, Rundell 2008, Sinclair 1987, West 1953.
- [C] Expanded `project/vocabulary-tiers.md` self-containment section to explicitly frame the tier system as a CDV analogue and link to the new research page, and added the new page to the vocabulary-tiers related-pages list.
- [A] Refreshed entry counts with end-of-day `report.py` output (23,841 entries / 21,058 general / 7,427 cross-references / 96,585 examples / 2,513 candidates / 45.5% symmetry / 3,463 asymmetric refs) across `project/overview.md`, `project/vocabulary-tiers.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, and the retrospective page. The earlier 2026-04-15 session had used morning snapshot values (23,609 / 20,826 / 2,747); today's second session catches the wiki up to the 24027-24042 and 24013-24026 entry batches merged since then.
- [E] Added the new page to `index.md`. Existing "Last updated" dates on all touched pages were already 2026-04-15 so no date changes were required.

## [2026-04-15] maintenance | Semantic prosody research, stats sync, retrospective refresh

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched **semantic prosody** — the evaluative colouring that attaches to words through habitual collocation — and created `research/semantic-prosody.md`. Covers the Sinclair/Louw/Stubbs/Partington theoretical tradition, distinctions between connotation / semantic preference / semantic prosody, the Hunston/Whitsitt critiques, Japanese examples organised by adverbs (ろくに, なかなか, いちいち, いかにも, わざわざ, せっかく, まさか), verbs and auxiliaries (〜てしまう, benefactives, 〜がる, 〜ぶる), and noun-modifiers (とんでもない, 〜くさい, 〜っぽい). Includes L2 acquisition findings (Xiao & McEnery 2006, Hoey 2005, Wei & Li 2014), five dictionary treatment strategies, and concrete recommendations for how je-dict-1's existing USAGE and SIMILAR WORDS blocks can carry prosody information explicitly. Full reference list: Hoey 2005, Hunston 2007, Louw 1993, Partington 1998/2004, Sinclair 1991/1996, Stubbs 1995/2001, Wei & Li 2014, Whitsitt 2005, Xiao & McEnery 2006.
- [A] Synced entry counts with `report.py` output (23,609 entries / 20,826 general / 7,423 cross-references / 95,784 examples / 2,747 candidates / 45.5% symmetry rate) across `project/overview.md`, `project/vocabulary-tiers.md`, `project/open-issues.md`, `topics/cross-references.md`, `topics/entry-consistency.md`, and the retrospective page.
- [C/E] Refreshed `topics/enhancement-plan-retrospective.md` metrics table to the 2026-04-15 numbers, flagging that **cross-reference symmetry has drifted downward** (3,461 asymmetric refs, up ~500 from two days earlier) as new entries add unreciprocated links faster than the symmetry pass processes them. Noted this as a suggested next sprint target.
- [E] Added cross-references from `research/collocations.md`, `research/definition-strategies.md`, and `research/translation-equivalence.md` into the new semantic prosody page; added the new page to `index.md`. Ran a Python-based link-checker across the whole wiki (0 broken links).
- [E] Updated "Last updated" dates on all pages touched this session.

## [2026-04-13] maintenance | Post-enhancement architecture update, retrospective page, stats sync

**Session type**: Nightly maintenance

**Activities**:
- [C] Substantially rewrote `project/architecture.md` to document the post-Enhancement-Plan infrastructure: task queue, orchestrator, monitor, multi-model review pipeline, entry locking, priority polishing, semantic fields, learner scenarios, expository articles, consistency checker, and the full current build-script inventory. Previous version only described the core build (validate → update_indexes → build_flat).
- [A] Updated `project/content-pipeline.md` to reflect coexisting progress-file and queue-based polishing modes, priority ordering, and the orchestrator/monitor layer. Added verb transitivity, aspect notes, and cross-model review to the polishing task list.
- [D/F] Created `topics/enhancement-plan-retrospective.md` — synthesis of what the 16-phase Enhancement Plan (2026-04-09) built, which wiki hypotheses it validated, which it under-specified, and progress against the plan's targets measured on 2026-04-13. Draws on `enhancement/enhancement-plan-2026-04-09.md`, `enhancement/tracking.md`, and `build/report.py` output.
- [A/E] Added implementation-status banners to `ideas/parallel-agent-architecture.md` and `ideas/multi-model-proofreading.md` linking to the retrospective page and current architecture page — these design docs were written as proposals and the wiki now signals that they've shipped.
- [A] Updated entry counts across core pages: 23,000→23,418 total, 20,200→20,600+ general, 6,000→6,600+ cross-references, 93,500→95,000+ examples, 3,200→2,900 candidates; noted ~48% cross-reference symmetry from the updated `report.py`.
- [E] Updated "Last updated" dates on all pages modified this session; updated `index.md` with the new retrospective page; updated `planning/maintain-knowledge-base.md` to note that the `enhancement/` folder is now a closed project and to point future sessions at the retrospective for catching up.

## [2026-04-08] maintenance | Dictionary lookup behavior research, homographs deepening, stats sync

**Session type**: Nightly maintenance

**Activities**:
- [B] Researched dictionary lookup behavior and skills — Nesi's (1999) lookup process model (5 stages), Lew's (2013) revision for electronic dictionaries, common lookup errors (failure to lemmatize, first-fit sense selection, ignoring context), Atkins & Varantola (1997) monitoring study, Tono (2001) eye-tracking research, Thumb (2004) bilingualised dictionary strategies, Japanese-specific challenges (kanji barrier, homophone density, kun-yomi near-synonyms); created research/dictionary-lookup-behavior.md citing Atkins & Varantola (1997), Lew (2004, 2013), Nesi (1999), Thumb (2004), Tono (2001), Halpern, CJK Dictionary Institute
- [C] Substantially expanded topics/homographs.md from ~250 words to ~1,500 — added concrete data from the dictionary (117 homographic headwords, 1,372 homophone readings), detailed analysis of five homograph types with tables and examples, in-depth treatment of homographic heterophones (角, 追従), dense homophone clusters (けん×7, かく×6), kun-yomi near-synonyms (かえる×5), search result disambiguation strategies, split-vs-merge design principles table
- [A] Updated entry counts across 14 wiki pages: entries 22,700→23,000, general tier 19,900→20,200, cross-references 5,700→6,000, examples 92,500→93,500, candidates 3,470→3,200; updated audio expansion storage estimates, parallel architecture, multi-model proofreading, compound verbs, pitch accent, LLMs-as-corpora, entry consistency, and word discovery pages accordingly
- Added cross-references from vocabulary-acquisition.md, learner-lexicography.md, and digital-dictionary-ux.md to the new dictionary-lookup-behavior page; added dictionary-lookup-behavior.md as a related page on homographs.md
- Updated index.md with 1 new page entry

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
