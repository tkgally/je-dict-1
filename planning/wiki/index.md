# je-dict-1 Knowledge Base

A persistent, LLM-maintained knowledge base for the TKG Japanese-English Learner’s Dictionary project (je-dict-1). This wiki is written and maintained by Claude; the human curator (Tom Gally) directs research, asks questions, and guides priorities.

**Last updated**: 2026-06-18 (wiki, second run: harvest 4 later-2026-06-18 observations → Cleanup Backlog P11 [residue extends to 6925, 30 applied], P17 [casual particles/fillers tagged `formal`], P21 [06169–06176 〜的 cluster + Jan-2026-band hypothesis] updates; Tooling Backlog item 20 update [concrete score_note_quality.py scorer bugs], item 23 update [two more candidate-junk families])


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
- [Semantic Prosody](research/semantic-prosody.md) — How evaluative colouring attaches to near-synonyms, and how dictionaries can surface it
- [Controlled Defining Vocabulary](research/controlled-defining-vocabulary.md) — The CDV tradition (Ogden, West, LDOCE, COBUILD) and its relationship to je-dict-1's tier system
- [Polysemy and Sense Discrimination](research/polysemy-sense-discrimination.md) — Sense division, ordering, and structure in learner dictionaries; models of polysemy; Japanese-specific challenges
- [Grammar Information in Learner Dictionaries](research/grammar-in-dictionaries.md) — Grammar codes, natural-language patterns, valency, conjugation, and Japanese-specific grammatical challenges
- [Multiword Expressions](research/multiword-expressions.md) — Taxonomy, dictionary placement, inclusion criteria, and Japanese-specific MWE challenges
- [Error Analysis and Learner Corpora](research/error-analysis-japanese-l2.md) — Learner corpora (I-JAS, KY), common error types by category and L1, and dictionary design implications
- [Vocabulary Size and Text Coverage](research/vocabulary-size-coverage.md) — Lexical thresholds (95%/98%), word-family counts for comprehension, dictionary sizing, and Japanese-specific considerations
- [Gairaigo: Loanwords in Japanese](research/gairaigo-loanwords.md) — Phonological adaptation, semantic shift, false friends, wasei-eigo, cognate advantage, and dictionary treatment
- [Pragmatics and Speech Acts](research/pragmatics-speech-acts.md) — Speech act theory, Japanese indirectness, sentence-final particles, pragmatic competence gap, and dictionary treatment
- [Sense Relations and Semantic Networks](research/sense-relations-semantic-networks.md) — Synonymy, antonymy, hyponymy, mental lexicon organization, semantic clustering debate, and dictionary treatment
- [Kanji Learning and Dictionary Treatment](research/kanji-learning-dictionaries.md) — Kanji acquisition, L1 transfer, radical/component awareness, compound inferencing, lookup methods, and furigana scaffolding
- [Japanese Aspect and ている](research/japanese-aspect-teiru.md) — Kindaichi's verb classification, progressive/resultative/habitual/experiential readings, L2 acquisition, and dictionary treatment of aspect
- [Register and Formality Marking](research/register-formality-marking.md) — Diasystematic labels, the consultation gap, Japanese stratal register, keigo marking, and encoding strategies
- [Keigo: Honorific Language](research/keigo-honorifics.md) — The keigo system's structure, 2007 five-category reclassification, L2 acquisition challenges, uchi/soto dynamics, and dictionary treatment
- [Vocabulary Learning Strategies](research/vocabulary-learning-strategies.md) — Strategy taxonomies (Oxford, Schmitt, Gu & Johnson), keyword method, word cards, morphological analysis, self-regulation, and dictionary design implications
- [Near-Synonym Discrimination](research/near-synonym-discrimination.md) — Dimensions of near-synonym difference, learner difficulty, dictionary presentation strategies, and Japanese stratal register pairs
- [History of Japanese-English Dictionaries](research/je-dictionary-history.md) — From the 1603 Nippo Jisho through Hepburn, Kenkyusha, and JMdict to the modern digital landscape
- [Cultural Content in Bilingual Dictionaries](research/cultural-content-dictionaries.md) — Culture-bound terms, the encyclopedic–linguistic boundary, Japanese cultural vocabulary dimensions, and dictionary treatment strategies
- [Lemmatization and Headword Selection](research/lemmatization-headword-selection.md) — Citation forms, entry scope criteria, non-inferability, word-counting units, and Japanese-specific headword challenges
- [Dictionary Evaluation and Metalexicography](research/dictionary-evaluation-metalexicography.md) — Evaluation frameworks (Wiegand, Hartmann, Tarp, Lew & Szarowska), user study methods, quality metrics, and the review–metric gap
- [Japanese Vocabulary Grading](research/japanese-vocabulary-grading.md) — BCCWJ frequency data, JLPT vs. corpus-based word lists, the word-family unit problem for Japanese, and coverage curve findings
- [Depth of Vocabulary Knowledge](research/depth-of-vocabulary-knowledge.md) — Nation's knowledge dimensions, breadth vs. depth, incremental acquisition, collocational difficulty, and implications for dictionary content
- [L1 Transfer in Japanese L2 Vocabulary](research/l1-transfer-japanese-vocabulary.md) — Jiang's three-stage model, script-based transfer effects (Chinese/Korean/English), cognate advantage, false friends, and dictionary design implications
- [Japanese→Chinese Adaptation Brief](research/japanese-chinese-adaptation-brief.md) — the per-language brief for the multilingual plan's first additional language: 文化庁 S/O/D/N triage, sourced 同形異義語 false-friend tables, calque/POS production hazards, L1-specific common mistakes, and what to drop from the English notes
- [Japanese-Learner Demand by L1](research/japanese-learner-demand-by-l1.md) — Japan Foundation 2021 learner-population data re-read by L1/target language, supplying the demand half of the language-priority ranking (confirms Chinese first, Korean second)
- [LLM Translation Quality for Japanese Language Pairs](research/llm-translation-quality-japanese-pairs.md) — the feasibility half of the multilingual demand × feasibility gate: published MT-eval evidence that ja/zh/ko are high-resource (junior-translator-quality first drafts) but that LLMs are weakest on the false-friend items the dictionary cares about most
- [Dictionary Skills and Reference Skills Training](research/dictionary-skills-training.md) — Lookup process models (Scholfield, Nesi, Lew), skills taxonomy, training effectiveness, sense selection failures, and compensatory dictionary design
- [Incidental Vocabulary Acquisition Through Reading](research/incidental-vocabulary-reading.md) — Acquisition rates from unassisted reading, dictionary consultation effects, the Involvement Load Hypothesis, contextual guessing vs. lookup, and implications for dictionary design
- [Bilingual vs. Monolingual Dictionary Debate](research/bilingual-monolingual-debate.md) — Teacher orthodoxy vs. empirical evidence, bilingualized dictionaries, the Revised Hierarchical Model, proficiency effects, and je-dict-1's hybrid position
- [Productive Vocabulary and Encoding Support](research/productive-vocabulary-encoding.md) — Receptive–productive gap, encoding vs. decoding dictionaries, production-oriented features, and Japanese-specific encoding challenges
- [Formulaic Language and Phraseological Competence](research/formulaic-language-phraseological-competence.md) — Prefabricated sequences, processing advantages, formulaic competence and L2 fluency, Japanese formulaic categories, and dictionary treatment
- [The Lexical Approach and Vocabulary-Centered Teaching](research/lexical-approach-vocabulary-teaching.md) — Lewis's chunk taxonomy, Sinclair's idiom principle, Willis's frequency-based syllabus, empirical evidence, criticisms, and dictionary design implications
- [Spaced Repetition and Dictionary Design](research/spaced-repetition-dictionary-design.md) — Forgetting curve, spacing effect, retrieval practice, SRS systems, sentence mining, and dictionary features that support spaced learning
- [Figurative Language and Idiom Processing in L2](research/figurative-language-idiom-processing.md) — Processing models (literal salience, graded salience, dual representation), metaphorical competence, Japanese figurative categories, and dictionary treatment
- [Dictionary Use in the Age of Machine Translation](research/dictionary-and-machine-translation.md) — MT prevalence, depth-of-processing costs, what dictionaries provide that MT cannot, complementary-tools framework, and Japanese-specific considerations
- [Dictionary Microstructure and Information Architecture](research/dictionary-microstructure.md) — Entry-internal organization, Wiegand's structural framework, information categories, sense ordering, navigation devices, and digital-era transformations
- [Japanese Particles in L2 Acquisition](research/japanese-particles-l2.md) — Particle classification, は/が interface problem, acquisition order, L1 transfer effects, error patterns, cognitive-linguistic pedagogy, and dictionary treatment
- [L2 Writing and Dictionary Consultation](research/l2-writing-dictionary-consultation.md) — How L2 writers use dictionaries, dictionary-induced errors, encoding challenges, collocation support, and Japanese-specific production problems
- [Vocabulary Testing and Assessment](research/vocabulary-testing-assessment.md) — Major vocabulary tests (VLT, VST, VKS, PVLT, WAT), knowledge dimension frameworks, Japanese-specific challenges, and dictionary design implications
- [Lexical Inferencing and Guessing from Context](research/lexical-inferencing.md) — Knowledge source taxonomies, success rates, morphological vs. contextual strategies, Japanese kanji compound inferencing, and dictionary design implications
- [Input Processing, Noticing, and Depth of Processing](research/input-processing-noticing-vocabulary.md) — Schmidt's Noticing Hypothesis, Levels of Processing, Involvement Load Hypothesis, Barcroft's TOPRA model, input enhancement, and dictionary design implications

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
- [Enhancement Plan 2026 Retrospective](topics/enhancement-plan-retrospective.md) — What the 16-phase enhancement plan built, which targets were met, and what remains
- [Schema Tag Reliability](topics/schema-tag-reliability.md) — Recurring cases where metadata tags drift from entry content (runaway automation, categorical compression, stale auto-labels)
- [Quality Metrics Trend](topics/quality-metrics.md) — Time series from the Routine v2 metrics and decision ledgers: per-run snapshots, flag precision by review dimension and source, and what each instrument is worth
- [Furigana Wrapper Anomalies](topics/furigana-wrapper-anomalies.md) — Malformed furigana wrapper patterns: honorific-prefix-inside-wrapper, pure-kana wrappers, truncated readings, and over-wrapped okurigana (859 instances across 624 entries)
- [Chinese Simplified/Traditional Handling](topics/chinese-simplified-traditional.md) — Worked design for the multilingual plan's (now-resolved) simplified-first decision: `zh-Hans`/`zh-Hant` BCP-47 code space, why simplified→traditional conversion is lossy (one-to-many merges + vocabulary norms), the OpenCC-seed-plus-human-review path for adding traditional later, and font/search/UI consequences
- [Multilingual Rendering and Delivery Architecture](topics/multilingual-rendering-architecture.md) — Worked design for the multilingual plan's §6 delivery layer (the previously-only-sketched static-vs-client-side question): Google's separate-URL/`hreflang` guidance, the measured GitHub Pages 1 GB ceiling (hit at the *first* additional language), and the recommended size-controlled hybrid with the hosting decision it forces before language #3

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
- [Multilingual Dictionary](ideas/multilingual-dictionary.md) — Adding target languages beyond English (Chinese first): schema, AI translation pipeline, note adaptation, UI toggle, build changes
- [Translation Sidecar Design](ideas/translation-sidecar-design.md) — Worked design for the multilingual plan's recommended storage option and staleness mechanism: concrete sidecar JSON shape, referential-integrity rules, per-field source hashing, re-translation queue, and field-level fallback contract
- [Cleanup Backlog](ideas/cleanup-backlog.md) — Systemic cleanup work surfaced during comprehensive-polish sessions
- [Tooling Backlog](ideas/tooling-backlog.md) — Tool improvements and new script ideas from polishing observations
- [Entry Follow-ups](ideas/entry-followups.md) — Specific entries needing work beyond a single polishing pass

## Log

See [log.md](log.md) for a chronological record of wiki sessions.
