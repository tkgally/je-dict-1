# Dictionary Evaluation and Metalexicography

**Last updated**: 2026-05-15

## Overview

Metalexicography — the study of dictionaries as objects of scholarly inquiry — includes dictionary criticism, evaluation, and user research as its core activities. While lexicography is the practice of making dictionaries, metalexicography asks: how good is this dictionary, for whom, and by what criteria? This page surveys the major evaluation frameworks, user study methodologies, and quality criteria that have been developed, and examines how they relate to je-dict-1's existing automated quality metrics.

## The evaluation problem in lexicography

Dictionary reviews have a long and uneven history. Most published dictionary reviews — in academic journals, newspapers, or online — focus on description rather than evaluation. Reviewers tend to cherry-pick a few entries, assess whether the definitions feel right, and declare the dictionary satisfactory or not. Swanepoel (2008) identified four systematic flaws in most dictionary criticism:

1. **Descriptive bias**: reviews describe design features without evaluating them against explicit criteria
2. **Selective scope**: reviewers narrow attention to one or two subjectively chosen features rather than covering the dictionary systematically
3. **Implicit criteria**: the standards by which the dictionary is judged are never articulated
4. **Unvalidated criteria**: even when criteria are stated, their validity is rarely justified

The gap between everyday reviewing and rigorous evaluation has motivated several attempts to build systematic frameworks.

## Major evaluation frameworks

### Wiegand's general theory of lexicography

Herbert Ernst Wiegand (1984, 1998) laid the groundwork for treating dictionaries as structured texts amenable to formal analysis. His framework decomposes dictionaries into structural layers:

- **Macrostructure**: the selection, ordering, and organization of headwords
- **Microstructure**: the internal organization of each entry (definitions, examples, grammar codes, pronunciation)
- **Mediostructure**: the cross-reference system connecting entries
- **Access structure**: the paths by which users navigate from a search need to the relevant information
- **Outside matter**: front matter, back matter, appendices, and user guides

Each layer can be evaluated independently. A dictionary might have excellent microstructure (rich, accurate entries) but poor access structure (users can't find what they need). Wiegand's structural decomposition remains the standard vocabulary for dictionary analysis.

### Hartmann's metalexicographic checklist

Reinhard Hartmann (2001, 2007) proposed that evaluation should be systematic and comparative. His "metalexicographic checklist" approach suggests that for any new dictionary project, the designer should survey existing comparable dictionaries across a standardized set of dimensions — coverage, treatment quality, accessibility, user fit — and use the comparison to identify gaps and opportunities. Hartmann's *Teaching and Researching Lexicography* (2001) established the field's standard taxonomy of research methods, distinguishing between:

- **Dictionary history**: studying how dictionaries evolved
- **Dictionary typology**: classifying dictionaries by purpose, scope, and structure
- **Dictionary criticism**: evaluating individual dictionaries against standards
- **Dictionary use**: studying how real users interact with dictionaries

### Béjoint's dictionary criticism tradition

Henri Béjoint (2000/2010) treated dictionary criticism as a branch of applied linguistics. In *Modern Lexicography*, he argued that criticism should go beyond surface-level review to examine the linguistic assumptions underlying a dictionary's design choices — how it handles polysemy, what its definition style implies about its model of meaning, whether its examples are authentic or contrived. Béjoint's approach is less checklist-oriented than Hartmann's, emphasizing instead the intellectual coherence of a dictionary's design.

### Jackson's review methodology

Howard Jackson (2002), in *Lexicography: An Introduction*, devoted a chapter to dictionary reviewing as a disciplined activity. He proposed that reviews should address:

- **Authority**: who compiled the dictionary and what expertise they bring
- **Vocabulary coverage**: comprehensiveness relative to the stated purpose
- **Special features**: distinctive elements (pronunciation, etymology, usage notes, illustrations)
- **Treatment of words**: accuracy and completeness of definitions, grammatical information, pronunciation, and usage guidance
- **Continuous revision**: evidence of updating and maintenance
- **Format**: physical or digital presentation quality

Jackson emphasized that the reviewer's criteria should be explicit and that a good review gives equal attention to strengths and weaknesses.

### Tarp's function theory

Sven Tarp (2008) proposed a fundamentally different approach: dictionaries should be evaluated not by their internal properties but by how well they satisfy user needs in specific situations. His "lexicographic function theory" (developed with Henning Bergenholtz) defines a lexicographic function as "the satisfaction of the specific types of lexicographically relevant needs that may arise in a specific type of potential user in a specific type of extra-lexicographical situation."

Functions fall into two categories:

| Function type | Situations | What the user needs |
|---------------|-----------|---------------------|
| **Communication-oriented** | Text reception (reading), text production (writing), translation | Meaning, grammar, collocations, register, equivalents |
| **Cognition-oriented** | Learning about a topic, acquiring general knowledge | Encyclopedic information, cultural context, conceptual relationships |

Under function theory, a dictionary is "good" to the extent that it helps its target users accomplish their actual tasks. A dictionary with perfect definitions but no production guidance fails the text-production function. This reframes evaluation from "does this dictionary have feature X?" to "does this dictionary help user Y do task Z?"

Tono (2009) offered a critical assessment of function theory, noting that while the user-needs framework is theoretically appealing, empirically validating which functions a dictionary actually serves requires the user-study methods described below.

### Swanepoel's meta-framework

Swanepoel (2008) proposed a framework for evaluating the evaluation criteria themselves. He argued that dictionary evaluation criteria should be:

- **Comprehensive**: covering all relevant dimensions of dictionary quality
- **Objective**: applicable by different evaluators with consistent results
- **Valid**: demonstrably connected to actual dictionary quality (not just conventional)
- **Generally accepted**: grounded in the metalexicographic literature
- **Operationalizable**: concrete enough to apply in practice

He distinguished between **internal criteria** (comparing what a dictionary claims about itself against what it actually delivers) and **external criteria** (measuring the dictionary against metalexicographic standards, user needs research, and linguistic adequacy requirements). Most dictionary reviews use only internal criteria, which is why they tend to be descriptive — they summarize features rather than judge quality.

### Lew & Szarowska's online dictionary framework

Lew & Szarowska (2017) developed the most influential recent framework specifically for evaluating digital bilingual dictionaries. Their four-dimension model was applied to six popular free English-Polish dictionaries identified through a user survey:

1. **Coverage**: breadth and depth of the lemma list relative to user needs
2. **Treatment**: quality of equivalents, definitions, grammatical information, examples, and usage labels within entries
3. **Access**: search functionality, auto-complete, navigation, error tolerance
4. **Presentation**: layout, typography, readability, advertising intrusiveness

The framework has since been replicated for English-Chinese dictionaries (2020) and Spanish-Chinese dictionaries (2024), confirming its transferability across language pairs. Its strength is that it balances structural analysis (coverage, treatment) with usability analysis (access, presentation) — the two concerns that most earlier frameworks handled separately.

## User study methods

### Think-aloud protocols

The think-aloud method, adapted from cognitive psychology (Ericsson & Simon 1984/1993), asks dictionary users to verbalize their thoughts while performing lookup tasks. In lexicographic research, Atkins & Varantola (1997) pioneered this approach in their EURALEX monitoring study, recording what users were looking for, which entries they consulted, and whether they found what they needed. Nesi & Haill (2002) adapted the method for studying international students at a British university, documenting common lookup failures — failure to lemmatize correctly, first-fit sense selection (stopping at the first definition that seems plausible), and ignoring grammatical or usage information even when present.

Think-aloud studies are rich in qualitative insight but expensive to conduct and limited in scale (typically 10–30 participants). They also face a reactivity problem: verbalizing one's thoughts may alter the cognitive process being studied.

### Eye-tracking

Eye-tracking technology records where dictionary users look, for how long, and in what sequence. Tono (2001, 2009) pioneered eye-tracking in lexicographic research, revealing that users spend most of their time on definitions and examples, often skip grammatical codes entirely, and process long entries in a scan-then-fixate pattern rather than reading linearly. Research on e-dictionaries using eye-tracking found that interface layout significantly affects attention patterns — but self-reported data often doesn't match actual gaze behavior, suggesting that users are unreliable reporters of their own lookup strategies (Lew & Szarowska 2017).

### Log file analysis

For digital dictionaries, server-side log files offer a passive, large-scale window into user behavior. De Schryver & Joffe (2004) pioneered this approach, arguing that log files provide "free implicit feedback" that can supplement or replace traditional questionnaires. Müller-Spitzer (2014) edited a comprehensive volume on empirical methods for studying online dictionaries, emphasizing the importance of methodological transparency in log file research — how data is collected, cleaned, segmented, and analyzed.

Key findings from log file studies include:

- Users look up frequent, everyday words more often than rare ones — contradicting the assumption that dictionaries are mainly for unfamiliar words (Wolfer, Koplenig, Meyer & Müller-Spitzer 2014)
- Lookup patterns differ significantly by user profile (L1 speakers vs. learners, different proficiency levels)
- Most sessions are short (1–3 lookups) but a minority of "power users" account for a disproportionate share of total lookups
- Search failures (queries that return no results) reveal gaps in coverage and lemmatization

Log file analysis scales to millions of queries but reveals only what users searched for, not why, and not whether the results satisfied their need. It is best used alongside qualitative methods.

### Controlled experiments

Researchers test dictionary effectiveness by comparing user performance on comprehension, translation, or production tasks with and without dictionary access, or comparing performance across different dictionary types. Luppescu & Day (1993) showed that dictionary use during reading significantly improved vocabulary retention; Laufer & Hadar (1997) compared monolingual, bilingual, and bilingualised dictionaries for L2 comprehension and production. Nesi (1999) found that learners often make errors *because* of the dictionary — selecting wrong senses, misinterpreting codes, or applying information incorrectly — suggesting that a dictionary's clarity is as important as its accuracy.

### Questionnaire surveys

Large-sample surveys capture user preferences, habits, and satisfaction at scale. They are cheap to administer but suffer from self-report bias — users describe what they think they do, which often diverges from actual behavior. Surveys are most useful for identifying which dictionaries users prefer and why, and for establishing the user base of a dictionary before conducting deeper studies.

## Evaluation dimensions for digital learner dictionaries

Synthesizing the frameworks above, the following dimensions are most relevant to evaluating a digital bilingual learner dictionary:

### 1. Coverage adequacy

- Does the dictionary include the words its target users need?
- Are word forms that users actually search for present (inflected forms, variant spellings, common misspellings)?
- Is the rate of "lookup disappointment" (queries returning no results) acceptable? Bogaards (1996) identified this as a major determinant of user satisfaction.
- Is the lemma list growing in response to user needs, or static?

### 2. Entry quality

- **Definitions/glosses**: Are translation equivalents accurate, contextually appropriate, and sufficient in number?
- **Examples**: Do they illustrate typical usage, clarify meaning, and model natural phrasing? (See [Example Sentence Design](example-sentences.md) for detailed criteria.)
- **Grammar information**: Is it present, accessible, and usable? (The "consultation gap" documented by Nesi & Haill 2002 and Tono 2001 shows that coded grammar information is largely ignored by users.)
- **Usage guidance**: Register labels, collocations, common errors, pragmatic notes
- **Consistency**: Do similar entries receive similar treatment? (See [Entry Consistency](../topics/entry-consistency.md).)

### 3. Access and navigation

- How quickly can a user get from a search query to the relevant entry?
- Does search handle inflected forms, variant spellings, and partial matches?
- Do cross-references and related-entry links support browsing and serendipitous discovery?
- Is the information architecture predictable — does the user know where to find each type of information within an entry?

### 4. Presentation and usability

- Is the entry layout scannable? Can users find specific information types (definition, example, grammar) without reading the entire entry?
- Is typography clear across devices?
- Do visual hierarchies (headers, indentation, font weight) match information hierarchies?

### 5. Maintenance and currency

- Is the dictionary actively updated?
- Are errors corrected when reported?
- Does new vocabulary get added in a timely way?
- Is there a visible quality trajectory — is the dictionary getting better over time?

### 6. Function satisfaction (Tarp's criterion)

- For text reception: can a user who encounters an unknown word find a clear, correct meaning?
- For text production: can a user who wants to use a word find enough guidance (collocations, register, grammar, examples) to use it correctly?
- For vocabulary learning: does the entry support deeper understanding — semantic relations, usage patterns, cultural context?

## The review–metric gap

Traditional metalexicographic evaluation is labor-intensive: a trained reviewer examines entries, applies criteria, and writes a qualitative assessment. This doesn't scale. Automated metrics — word counts, coverage percentages, cross-reference density, consistency checks — scale easily but may not correlate with what makes a dictionary actually useful.

This gap is visible in the literature. Log file studies tell us *what* users look up but not *whether they were satisfied*. Think-aloud studies tell us *how* users process entries but cover too few entries to characterize a dictionary. Automated metrics tell us about *structural properties* (entry length, cross-reference density, tag consistency) but not about *editorial quality* (whether a definition is clear, whether an example illuminates the right sense).

The most productive approach combines:

1. **Automated structural metrics** for coverage, consistency, and completeness monitoring
2. **Sampled qualitative review** by trained evaluators for editorial quality assessment
3. **User performance testing** on controlled tasks for effectiveness measurement
4. **Log file analysis** (where available) for real-world usage patterns

## Implications for je-dict-1

### What the dictionary already measures

je-dict-1's `report.py` dashboard and `check_consistency.py` produce an unusually rich set of automated structural metrics:

| Metric | Type (Swanepoel) | Dimension (Lew) |
|--------|-------------------|-----------------|
| Entry count by tier | Internal | Coverage |
| Cross-reference count, symmetry rate | Internal | Treatment |
| Examples per entry | Internal | Treatment |
| Note quality score | Internal | Treatment |
| Inline link coverage | Internal | Access |
| Tag consistency checks | Internal | Treatment |
| Missing transitivity, missing aspect docs | Internal | Treatment |
| Furigana completeness | Internal | Treatment |

These are all **internal structural metrics** in Swanepoel's taxonomy — they measure what the dictionary has, not whether it works for users. They correspond primarily to Lew & Szarowska's "coverage" and "treatment" dimensions. Access and presentation are not systematically measured, and there are no user-facing metrics at all.

### What's missing

1. **Coverage adequacy testing**: je-dict-1 has no mechanism to measure "lookup disappointment" — the rate at which a user searches for a word and doesn't find it. The static site currently has no search logging. Even a lightweight analytics integration (recording failed searches) would provide the single most actionable coverage metric. Without this, coverage decisions rely entirely on corpus frequency data and curator judgment.

2. **Function satisfaction assessment**: the automated metrics don't distinguish between text-reception quality (Is the gloss correct?) and text-production quality (Can a learner use this word correctly based on the entry?). A small sampled study — even 50 entries reviewed against Tarp's function criteria — would calibrate whether the structural metrics predict actual usefulness.

3. **Presentation evaluation**: the `docs/` site has never been formally evaluated for usability. Questions like "can users find the SIMILAR WORDS section?", "do users understand what the cross-reference types mean?", and "is the example sentence length progression noticeable?" are unanswered. The wiki's [Digital Dictionary UX](digital-dictionary-ux.md) page documents several improvement opportunities, but none have been user-tested.

4. **Comparative evaluation**: how does je-dict-1 compare to JMdict/Jisho.org, Weblio, Wisdom, or other JE resources on specific lookup tasks? Lew & Szarowska's framework could be adapted for a systematic comparison, which would identify je-dict-1's competitive strengths and weaknesses.

### Recommendations

1. **Adopt a lightweight evaluation framework** based on Lew & Szarowska's four dimensions (coverage, treatment, access, presentation). Map existing automated metrics to these dimensions and identify the gaps — primarily in access and presentation.

2. **Implement failed-search logging** as the single highest-value new metric. Even a static-site-compatible approach (client-side logging to a simple endpoint, or periodic sampling of search terms) would transform coverage planning from guesswork to data-driven.

3. **Conduct a sampled function-satisfaction audit**: take 50 entries stratified by tier and POS, and evaluate each against Tarp's three functions (reception, production, learning). This would validate or calibrate the automated note-quality score.

4. **Frame the existing multi-model review pipeline as evaluation**: the screening/deep review system already performs a form of sampled qualitative review. Expanding its scope beyond furigana correctness to cover definition accuracy, example quality, and usage guidance would align it with metalexicographic best practice.

5. **Document the evaluation methodology**. je-dict-1 is unusual in having a rich health dashboard and systematic quality processes. Documenting these as an explicit evaluation methodology — with reference to the metalexicographic frameworks above — would both improve internal practice and contribute to the field's understanding of how automated dictionary quality management works at scale.

## Key references

- Atkins, B.T.S. & Varantola, K. (1997). "Monitoring dictionary use." *International Journal of Lexicography*, 10(1), 1–45.
- Béjoint, H. (2000/2010). *Modern Lexicography: An Introduction*. Oxford University Press.
- Bergenholtz, H. & Tarp, S. (2003). "Two opposing theories: On H.E. Wiegand's recent discovery of lexicographic functions." *Hermes*, 31, 171–196.
- Bogaards, P. (1996). "Dictionaries for learners of English." *International Journal of Lexicography*, 9(4), 277–320.
- De Schryver, G.-M. & Joffe, D. (2004). "On how electronic dictionaries are really used." In *Proceedings of EURALEX 2004*, 187–196.
- Ericsson, K.A. & Simon, H.A. (1984/1993). *Protocol Analysis: Verbal Reports as Data*. MIT Press.
- Hartmann, R.R.K. (2001). *Teaching and Researching Lexicography*. Longman.
- Jackson, H. (2002). *Lexicography: An Introduction*. Routledge.
- Laufer, B. & Hadar, L. (1997). "Assessing the effectiveness of monolingual, bilingual, and 'bilingualised' dictionaries." *Modern Language Journal*, 81(2), 189–196.
- Lew, R. & Szarowska, A. (2017). "Evaluating online bilingual dictionaries: The case of popular free English-Polish dictionaries." *ReCALL*, 29(2), 138–159.
- Luppescu, S. & Day, R. (1993). "Reading, dictionaries, and vocabulary learning." *Language Learning*, 43(2), 263–287.
- Müller-Spitzer, C. (Ed.) (2014). *Using Online Dictionaries*. De Gruyter.
- Nesi, H. (1999). "The specification of dictionary reference skills in higher education." In R.R.K. Hartmann (Ed.), *Dictionaries in Language Learning*, 53–66. Free University of Berlin.
- Nesi, H. & Haill, R. (2002). "A study of dictionary use by international students at a British university." *International Journal of Lexicography*, 15(4), 277–305.
- Swanepoel, P. (2008). "Towards a framework for the description and evaluation of dictionary evaluation criteria." *Lexikos*, 18, 207–231.
- Tarp, S. (2008). *Lexicography in the Borderland between Knowledge and Non-Knowledge*. Niemeyer.
- Tono, Y. (2001). *Research on Dictionary Use in the Context of Foreign Language Learning*. Niemeyer.
- Tono, Y. (2009). "A critical review of the theory of lexicographical functions." *Lexicon*, 40, 1–26.
- Wiegand, H.E. (1984). "On the structure and contents of a general theory of lexicography." In R.R.K. Hartmann (Ed.), *LEXeter '83 Proceedings*, 13–30. Niemeyer.
- Wolfer, S., Koplenig, A., Meyer, P. & Müller-Spitzer, C. (2014). "Dictionary users do look up frequent and socially relevant words." In *Proceedings of EURALEX 2014*, 281–291.

## Related pages

- [Learner Lexicography](learner-lexicography.md) — the broader field this evaluation tradition serves
- [Digital Dictionary UX](digital-dictionary-ux.md) — interface design and access-structure evaluation
- [Dictionary Lookup Behavior](dictionary-lookup-behavior.md) — the user-side complement to dictionary evaluation
- [Example Sentence Design](example-sentences.md) — evaluation criteria for one specific entry component
- [Entry Consistency](../topics/entry-consistency.md) — internal consistency as an evaluation dimension
- [Enhancement Plan 2026 Retrospective](../topics/enhancement-plan-retrospective.md) — je-dict-1's quality metrics in context
- [Deterministic vs. Semantic Tasks](../topics/deterministic-vs-semantic-tasks.md) — which evaluation activities can be automated
- [Near-Synonym Discrimination](near-synonym-discrimination.md) — evaluation of treatment quality for a specific entry type
