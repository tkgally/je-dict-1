# Collocations in Learner Dictionaries

**Last updated**: 2026-07-28

## What collocations are and why they matter

Collocations are habitual word combinations that native speakers use naturally but that are not predictable from the meanings of their component words. Knowing the word "take" and the word "bath" does not predict that English uses "take a bath" rather than "do a bath" or "make a bath." Similarly, in Japanese, 風呂に入る (get into a bath) is the natural combination — 風呂をする would sound wrong to native speakers.

Collocations are distinct from:
- **Free combinations** — any words that can grammatically combine (read a book, read a sign)
- **Idioms** — fixed expressions whose meaning is not derivable from components (kick the bucket)
- **Collocations** occupy the middle ground — semantically transparent but conventionally restricted

### Why collocations matter for L2 learners

1. **Naturalness**: Collocation errors are one of the strongest markers of non-native speech. A learner who says "strong rain" instead of "heavy rain" is understood but immediately identified as non-native.

2. **Volume**: Estimates vary, but a substantial portion of fluent language use consists of semi-fixed combinations. Pawley & Syder (1983) showed that the "puzzle of nativelike selection" — choosing the natural combination from among many grammatically possible ones — is largely a collocation problem.

3. **Acquisition difficulty**: Yamashita & Jiang (2010) studied Japanese ESL and EFL learners and found that **L1-congruent collocations** (where the Japanese equivalent uses a similar combination) are significantly easier to acquire than **L1-incongruent collocations**. Even advanced ESL users with extensive L2 exposure still showed L1 influence on collocation processing. This suggests that explicit collocation instruction — and collocation information in dictionaries — is essential.

4. **Production vs. reception gap**: Learners may understand collocations in context (receptive knowledge) but fail to produce them correctly (productive knowledge). Dictionaries that list collocations help bridge this gap.

## Types of collocations

### By grammatical pattern

| Pattern | English example | Japanese example |
|---------|----------------|-----------------|
| Verb + noun | make a decision | 決断を下す |
| Adjective + noun | heavy rain | 激しい雨 |
| Noun + verb | prices rise | 物価が上がる |
| Adverb + adjective | deeply concerned | 非常に心配 |
| Verb + adverb | apologize profusely | 深くお詫びする |
| Noun + noun | a round of applause | 拍手の嵐 |

### By strength

- **Strong collocations**: highly restricted combinations where one component strongly predicts the other (e.g., 足を組む "cross one's legs" — 組む is the default verb for this action)
- **Medium collocations**: preferred but not exclusive combinations (e.g., 電話をかける "make a phone call" — other verbs like する are possible but less natural)
- **Weak collocations**: tendencies that guide native word choice but allow broader substitution

## Japanese-specific collocation challenges

### Particle-mediated collocations

Japanese collocations typically involve a particle linking the components: noun + particle + verb. The particle is part of the collocation and varies by pattern:

- 電話**を**かける (make a phone call)
- 風呂**に**入る (take a bath)
- 席**を**立つ (leave one's seat)
- 夢**を**見る (have a dream)
- 気**に**なる (be concerned about)

For learners, both the verb choice and the particle choice must be learned together. This is why je-dict-1's collocation notes and particle pattern documentation are closely linked.

### Verb choice unpredictability

Japanese often uses a different "light verb" than English would predict:

- 薬を**飲む** (drink medicine — English "take")
- 傘を**さす** (point an umbrella — English "hold/use/open")
- 年を**取る** (take years — English "get old/age")
- 写真を**撮る** (take a photograph — same as English, but the Japanese verb is "capture")

These are the collocations that cause the most production errors for English-speaking learners.

### Onomatopoeia collocations

Japanese onomatopoeia (擬態語/擬音語) frequently collocate with specific verbs:

- じろじろ**見る** (stare)
- にこにこ**笑う** (smile happily)
- ぐっすり**眠る** (sleep soundly)
- ぺらぺら**話す** (speak fluently)

These are a distinct and characteristically Japanese collocation type.

## How major dictionaries handle collocations

### Dedicated collocation dictionaries

- **Oxford Collocations Dictionary** (OCD): Groups collocations by headword, organized by grammatical type (verb + noun, adj + noun, etc.) with brief examples. Sense-disambiguated. The standard reference for English collocations.
- **Macmillan Collocations Dictionary** (Rundell, 2010): Over 121,000 collocational phrases for advanced learners, organized by semantic meaning, allowing learners to see related options with different connotations.
- **Shoji, Kakuko (2010). *Common Japanese Collocations: A Learner's Guide to Frequent Word Pairings***: The first dedicated Japanese collocation resource for learners, focusing on noun + verb and noun + adjective patterns. Published by Kodansha.

### General learner dictionaries

The "Big Five" EFL dictionaries (OALD, LDOCE, COBUILD, CALD, MALD) all include collocation information, but their approaches vary:

- **COBUILD** integrates collocations into its full-sentence definitions and corpus-derived examples
- **LDOCE** marks frequent collocations in example sentences and includes a separate collocation box for selected entries
- **OALD** provides collocation boxes and links to the Oxford Collocations Dictionary online

Research has found that collocation treatment in general dictionaries tends to be "inconsistent and incomplete" — collocations appear in examples but are not always explicitly labeled or systematically covered.

### Digital integration approaches

The **ColloCaid** project explored integrating collocation information directly into text editors, bypassing the dictionary lookup step entirely. This represents a newer approach: rather than requiring learners to consult a separate resource, collocation suggestions appear in context during writing.

## Identifying collocations: statistical measures

Corpus linguists use statistical association measures to identify collocations from large corpora:

| Measure | What it captures | Strengths | Weaknesses |
|---------|-----------------|-----------|------------|
| **MI (Mutual Information)** | How much more often two words co-occur than expected by chance | Good at finding strong, exclusive collocations | Overweights rare words; unreliable for low-frequency pairs |
| **t-score** | Statistical significance of co-occurrence above chance | Good at finding frequent, reliable collocations | Biased toward very high-frequency words |
| **Log-likelihood** | Significance of the observed vs. expected co-occurrence pattern | Handles varying corpus sizes well | Still requires frequency thresholds |
| **Dice coefficient** | Symmetric measure of association | Less frequency-biased than t-score | Less commonly used in lexicography |

In practice, lexicographers often combine measures: MI to find strong/exclusive collocations, t-score to find frequent/typical ones. The BCCWJ and NINJAL Web Japanese Corpus both support collocational analysis for Japanese.

## Implications for je-dict-1

### Current collocation coverage

je-dict-1 includes collocations in the `notes` field of entries, typically under a "Collocations" or "Common patterns" header. This is one of the v2 quality standards (high priority: "Add common noun-verb pairings"). The dictionary also captures collocations implicitly through example sentences.

### Recommendations based on research

1. **Systematic noun + particle + verb patterns**: For noun entries, list the verbs that commonly take that noun as an object or complement, including the particle. For verb entries, list the nouns they commonly govern. This bidirectional coverage helps both receptive and productive use.

2. **Flag L1-incongruent collocations**: Given Yamashita & Jiang's (2010) finding that L1-incongruent collocations are hardest to acquire, entries should explicitly note when the Japanese collocation uses a different verb/pattern than the English equivalent would predict. For example, 薬を飲む should note that English uses "take" not "drink."

3. **Include collocations in examples**: Every collocation listed should appear in at least one example sentence showing it in natural context. This aligns with the involvement load hypothesis — deeper processing from seeing the collocation in use leads to better retention.

4. **Distinguish collocation types**: Mark whether a collocation is essential (the standard way to express something) vs. common (a frequent but not exclusive combination). This helps learners prioritize.

5. **Cross-reference collocation partners**: When entry A lists "A + B" as a collocation, entry B should also reference the combination. The existing cross-reference system can support this.

6. **Onomatopoeia + verb patterns**: For onomatopoeia entries (89 currently), systematically list the verbs they collocate with. This is a high-value, distinctively Japanese collocation type that general dictionaries often neglect.

### Finding from polishing: the lexicalized compound that blocks the phrase (2026-07-28)

A 2026-07-27 polish run surfaced a failure mode this page's framework predicts but the entry
guidelines do not currently guard against. Several colour and temperature adjective entries
illustrate the adjective with an **attributive phrase** in a slot where Japanese uses an
**established N+N compound**: ×青い信号 for 青信号, ×赤い信号 for 赤信号.

This is the *blocking* case of Yamashita & Jiang's L1-incongruence problem rather than the
substitution case. The usual incongruent collocation (薬を飲む vs. "take medicine") gives the
learner a wrong-but-existing partner to unlearn. Here the compound **pre-empts the productive
rule entirely**: the adjective's ordinary attributive form is grammatical, semantically
transparent, and simply not used, because a lexicalized item already occupies the meaning. An
English speaker producing 青い信号 has made no grammatical error and will get no feedback.

Three points worth carrying into practice:

1. **It is invisible to every automated check the project has.** The phrase is well-formed JSON,
   grammatical Japanese, and faithfully translated — so schema validation, the note scorer, and
   the cross-model accuracy reviewer all pass it. Only a reader who knows the compound notices.
   This is the clearest instance yet of the general point in
   [dictionary-evaluation-metalexicography](dictionary-evaluation-metalexicography.md): idiomaticity
   is not measurable by any instrument that checks correctness.
2. **Model-written examples are structurally prone to it.** An example generated from a headword
   plus a target sense composes productively by default; the lexicalized alternative has to be
   *recalled*, and nothing in the generation prompt asks for it. Expect the class wherever an
   entry's examples were written without a frequency check.
3. **The affected population is enumerable.** The trigger is a specific structural collision —
   a lexicalized N+N compound competing with the adjective's own attributive form — which
   confines it to small clusters (colour + 信号/字/板/紙, temperature + 湯/水/蔵, 高/低, 大/小).
   That makes it a bounded review queue rather than an open-ended quality concern.

Filed as [Cleanup Backlog P29](../ideas/cleanup-backlog.md#priority-29-adjective-examples-that-teach-a-phrase-where-the-language-uses-a-set-compound).
It also argues for a small addition to recommendation 2 above: entries for adjectives with a
competing set compound should state the compound *and* mark the phrase as not idiomatic —
knowing 青信号 exists does not tell a learner that ×青い信号 is unavailable.

### Future possibilities

- **Corpus-validated collocations**: Using BCCWJ collocational data to verify and supplement LLM-generated collocation lists
- **Collocation search**: Extending the site's search to find entries by collocation pattern (e.g., search "電話" and see "電話をかける" highlighted)
- **Collocation-based entry linking**: Automated detection of collocation relationships between entries for cross-reference suggestions

## References

- Yamashita, J. & Jiang, N. (2010). "L1 Influence on the Acquisition of L2 Collocations: Japanese ESL Users and EFL Learners Acquiring English Collocations." *TESOL Quarterly*, 44(4).
- Shoji, K. (2010). *Common Japanese Collocations: A Learner's Guide to Frequent Word Pairings*. Kodansha International.
- Rundell, M. (2010). *Macmillan Collocations Dictionary for Learners of English*. Macmillan Education.
- Pawley, A. & Syder, F.H. (1983). "Two puzzles for linguistic theory: Nativelike selection and nativelike fluency." In Richards, J.C. & Schmidt, R.W. (eds.), *Language and Communication*.
- Wray, A. (2002). *Formulaic Language and the Lexicon*. Cambridge University Press.
- Laufer, B. & Waldman, T. (2011). "Verb-Noun Collocations in Second Language Writing." *Language Learning*, 61(2).

## Related pages

- [Corpus Linguistics](corpus-linguistics.md) — statistical measures and Japanese corpora
- [Vocabulary Acquisition](vocabulary-acquisition.md) — formulaic sequences and depth of processing
- [Learner Lexicography](learner-lexicography.md) — production vs. reception in dictionary design
- [Quality Standards](../project/quality-standards.md) — collocation patterns as a v2 priority
- [Compound Verb Representation](../topics/compound-verbs.md) — a related category of multi-word units
- [Semantic Prosody](semantic-prosody.md) — the evaluative colouring that extends beyond simple collocation
- [Grammar Information in Learner Dictionaries](grammar-in-dictionaries.md) — overlap between collocational and grammatical patterns
- [Multiword Expressions](multiword-expressions.md) — broader taxonomy of MWEs including idioms, formulaic routines, and grammar patterns
- [Error Analysis and Learner Corpora](error-analysis-japanese-l2.md) — collocational violations as a major error category
- [Sense Relations and Semantic Networks](sense-relations-semantic-networks.md) — how collocation patterns distinguish near-synonyms
- [Near-Synonym Discrimination](near-synonym-discrimination.md) — collocation as the primary discriminating dimension between near-synonyms
- [Vocabulary Learning Strategies](vocabulary-learning-strategies.md) — collocational knowledge as productive vocabulary and its role in consolidation strategies
- [Depth of Vocabulary Knowledge](depth-of-vocabulary-knowledge.md) — collocation as the hardest dimension to acquire (Nesselhauf 2005, Laufer & Waldman 2011)
- [Productive Vocabulary and Encoding Support](productive-vocabulary-encoding.md) — collocation as a critical encoding-dictionary information category
- [Formulaic Language and Phraseological Competence](formulaic-language-phraseological-competence.md) — the broader psycholinguistic context: processing advantages, fluency benefits, and L2 acquisition of prefabricated sequences
- [The Lexical Approach and Vocabulary-Centered Teaching](lexical-approach-vocabulary-teaching.md) — the pedagogical methodology that puts collocations at the centre of language instruction
- [L2 Writing and Dictionary Consultation](l2-writing-dictionary-consultation.md) — collocation as the primary productive challenge in L2 writing, and collocation dictionary consultation behavior
- [Example Sentence Design](example-sentences.md) — collocational typicality as a core criterion for example quality
