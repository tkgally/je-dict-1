# Sense Relations and Semantic Networks

**Last updated**: 2026-06-03

## Overview

Words do not exist in isolation: they form networks of meaning connected by predictable relationships — synonymy, antonymy, hyponymy, meronymy, and others. Understanding these **sense relations** is central to both lexical semantics and practical dictionary design, because dictionaries must decide how to represent, label, and surface the connections between related entries. This page surveys the taxonomy of sense relations, how dictionaries and computational resources organize them, the psycholinguistic evidence on how learners store words in semantic networks, the contested "semantic clustering" question in vocabulary pedagogy, and the implications for je-dict-1's cross-reference and similar-words systems.

## Taxonomy of sense relations

The foundational taxonomy comes from structural semantics, systematized in **Cruse (1986)** *Lexical Semantics* and refined in **Lyons (1977)** *Semantics* and **Murphy (2003)** *Semantic Relations and the Lexicon*. Murphy's central argument is that paradigmatic meaning relations (synonymy, antonymy, hyponymy) constitute **metalinguistic** knowledge — knowledge *about* words — rather than being part of the lexical entry itself. This distinction matters for dictionary design: sense relations are not intrinsic properties of a word but judgments about how words relate to each other.

### Core paradigmatic relations

| Relation | Definition | Example (English) | Example (Japanese) |
|----------|-----------|-------------------|-------------------|
| **Synonymy** | Two words share the same (or nearly the same) denotation | *big* / *large* | {大きい\|おおきい} / {巨大\|きょだい}な |
| **Antonymy** | Two words express opposing meanings | *hot* / *cold* | {暑い\|あつい} / {寒い\|さむい} |
| **Hyponymy** | One word's meaning is included within another's (IS-A) | *dog* IS-A *animal* | {犬\|いぬ} IS-A {動物\|どうぶつ} |
| **Hypernymy** | The converse of hyponymy (superordinate) | *animal* includes *dog* | {動物\|どうぶつ} includes {犬\|いぬ} |
| **Meronymy** | Part-whole relationship (HAS-A) | *finger* PART-OF *hand* | {指\|ゆび} PART-OF {手\|て} |
| **Co-hyponymy** | Two words share the same hypernym | *dog* and *cat* (both *animal*) | {犬\|いぬ} and {猫\|ねこ} |

### Subtypes of antonymy

Cruse (1986) distinguishes several antonym types:

- **Gradable antonyms**: occupy ends of a scale (*hot–cold*, *big–small*). Negating one does not entail the other.
- **Complementary antonyms**: divide a domain exhaustively (*alive–dead*, *true–false*). Negating one entails the other.
- **Converse antonyms**: describe the same relation from opposite perspectives (*buy–sell*, *teacher–student*).
- **Directional antonyms**: opposite directions or movements (*up–down*, *come–go*).

Japanese adds a dimension absent in English: **transitivity pairs** ({開|あ}ける / {開|あ}く, {上|あ}げる / {上|あ}がる) function as a quasi-antonym system where the opposition is not semantic but grammatical — agent-focused vs. change-of-state. These pairs are so central to Japanese that je-dict-1 treats them as a separate cross-reference type (`transitive pair` / `intransitive pair`) rather than classifying them under antonymy.

### Subtypes of synonymy

True (absolute) synonymy is rare — most "synonyms" are **near-synonyms** that differ along one or more dimensions:

- **Denotational overlap with register split**: {食|た}べる (neutral) vs. {召|め}し{上|あ}がる (honorific) vs. いただく (humble)
- **Denotational overlap with connotational split**: {美|うつく}しい (literary beauty) vs. きれい (everyday prettiness)
- **Partial denotational overlap**: {見|み}る (see/watch/look) vs. {眺|なが}める (gaze at leisurely) vs. {観|み}る (watch a performance)
- **Cross-stratal synonyms**: Japanese is especially rich in these because of the wago/kango/gairaigo vocabulary strata — {手紙\|てがみ} (wago) vs. {書簡\|しょかん} (kango) vs. レター (gairaigo) all mean "letter"

Dictionary synonym discrimination — explaining *how* near-synonyms differ — is one of the most valuable services a learner dictionary can provide, and one of the hardest to automate (see [Definition and Gloss Strategies](definition-strategies.md)).

## Sense relations in dictionaries

### Traditional approaches

Dictionaries have used several strategies to present sense relations:

**1. Cross-references**: The oldest approach — noting "see also X" or "compare Y" at the end of an entry. Simple but passive: the learner must follow the link and synthesize the comparison themselves. Most bilingual dictionaries use this approach, including je-dict-1's `cross_references` field.

**2. Synonym discrimination notes**: Entries include a section explicitly contrasting the headword with its near-synonyms, explaining how they differ in meaning, register, collocation, or grammar. The Oxford Advanced Learner's Dictionary (OALD) and je-dict-1's "SIMILAR WORDS" note sections follow this model.

**3. Thesaurus sections**: Some dictionaries embed thesaurus-like groupings within entries. The **Oxford Learner's Thesaurus** (2008) organizes entries around meaning groups, showing near-synonyms clustered with their differences explained.

**4. Production dictionaries**: The **Longman Language Activator** (1993), marketed as "the world's first production dictionary," organizes entries onomasiologically (from meaning to word) rather than alphabetically. A learner who wants to express the concept "angry" finds a cluster of options ({怒|おこ}る, {腹|はら}が{立|た}つ, {憤慨|ふんがい}する, むかつく) with discrimination notes explaining when each is appropriate. This approach foregrounds sense relations as the primary organizing principle.

### Computational approaches: WordNet

**WordNet** (Miller 1995; Fellbaum 1998), developed at Princeton from the mid-1980s, is the most influential computational model of sense relations. It organizes English words into ~117,000 **synsets** (sets of cognitively synonymous words), interlinked by semantic relations: hypernymy/hyponymy (forming a taxonomy tree), meronymy/holonymy, antonymy, and entailment (for verbs). WordNet's design was explicitly informed by psycholinguistic theories of how human semantic memory is organized — as a hierarchical network where more general concepts sit above more specific ones.

The **Japanese WordNet** (日本語ワードネット), developed at NICT from 2006 (Bond et al. 2009), maps Japanese words onto Princeton WordNet's synset structure, inheriting its relational framework. As of version 2.0, it covers a substantial portion of the Japanese lexicon. However, its reliance on the English-derived synset structure means some Japanese-specific semantic distinctions (e.g., the register gradient from wago to kango) are not natively represented.

WordNet's significance for dictionary design is the proof that sense relations can be **formalized and navigated computationally**. A dictionary with typed, bidirectional cross-references is building a small WordNet within its own entry space.

## The mental lexicon and semantic networks

### How words are stored

Psycholinguistic research has established that the mental lexicon is organized as a **network**, not a list. **Aitchison (1987/2012)** *Words in the Mind* demonstrated through word association experiments, speech errors, and tip-of-the-tongue phenomena that words are stored with multiple types of connections:

- **Semantic connections**: words linked by meaning similarity (*doctor* → *nurse*, *hospital*)
- **Phonological connections**: words linked by sound similarity (*cat* → *cap*, *hat*)
- **Collocational connections**: words linked by habitual co-occurrence (*strong* → *coffee*, *tea*)
- **Categorical connections**: words linked by shared superordinate (*red* → *blue*, *green*)

Word association studies consistently show that **paradigmatic responses** (same-word-class associations: *dog* → *cat*) dominate in adult native speakers, while **syntagmatic responses** (different-word-class associations: *dog* → *bark*) are more common in children and L2 learners. This developmental shift suggests that as learners become more proficient, their mental lexicon reorganizes from a syntagmatic (collocational) structure toward a paradigmatic (semantic-relational) structure.

### L2 lexical organization

For L2 learners, the mental lexicon develops differently from L1:

- **Early stages**: L2 words are often connected to their L1 translation equivalents rather than to other L2 words. The L2 lexicon is "parasitic" on the L1 lexicon (Jiang 2000).
- **Intermediate stages**: L2-to-L2 connections develop, but they tend to be syntagmatic (collocational) rather than paradigmatic (semantic). Learners know that *strong* goes with *coffee* before they organize *strong/weak/powerful/mighty* into a paradigmatic set.
- **Advanced stages**: Paradigmatic organization strengthens, approaching (but rarely reaching) L1 patterns.

This developmental trajectory has a dictionary design implication: **collocational information** (syntagmatic connections) may be more immediately useful to intermediate learners than paradigmatic synonym lists, because it matches how their lexicon is currently organized. But paradigmatic information (synonym discrimination, antonym pairs, hypernym links) helps learners *reorganize* their lexicon toward a more mature structure.

## The semantic clustering debate

### Does teaching words in semantic sets help or hurt?

A significant body of research has investigated whether presenting new vocabulary in **semantic clusters** (groups of co-hyponyms like *arm, leg, foot, hand*) helps or hinders learning. The findings are surprisingly mixed.

**Evidence for interference**:

- **Tinkham (1993)** found that learners needed significantly more trials to learn words presented in semantically related clusters than words in unrelated sets. He attributed this to **interference**: similar items compete in memory, making each harder to distinguish and retrieve.
- **Waring (1997)** replicated Tinkham's finding with Japanese learners of English, confirming that the effect holds across L1 backgrounds.
- **Tinkham (1997)** further showed that **thematic clustering** (grouping words by shared context or theme, e.g., *frog, green, hop*) facilitated learning, while semantic clustering (co-hyponyms, e.g., *frog, toad, salamander*) hindered it.

**Evidence for facilitation or null effects**:

- **Hoshino (2010)** found that semantic clustering *facilitated* vocabulary learning in a classroom setting, arguing that the schema activation from organized presentation outweighed interference.
- **Ishii (2015)** argued that impeding effects reported in earlier studies may partly reflect **visual similarity** of word referents rather than semantic connection per se. When physical/visual relatedness was controlled, semantically related sets were neither harder nor easier to learn than unrelated sets.
- A review of 13 empirical studies found six showing interference, two showing limited interference, one showing no effect, and four showing facilitation — suggesting the phenomenon is less robust than early studies implied.

**Resolution**:

The consensus view, following Nation (2000, 2001), is that **presenting new words in semantically related sets is generally inadvisable for initial learning** but that **revisiting learned words through semantic comparison is beneficial for deepening knowledge**. The distinction is between *introduction* (where interference dominates) and *consolidation* (where contrastive comparison strengthens distinctions).

This has a direct implication for dictionaries: the dictionary's **synonym discrimination notes and cross-references** serve the consolidation function. A learner who already knows {暑い\|あつい} and encounters a cross-reference to {熱い\|あつい} benefits from the comparison precisely because both words are already partially known. The dictionary is a consolidation tool, not an introduction tool, and semantic networking in entries supports this role.

## Japanese-specific semantic networks

### Kanji as visual semantic connectors

Japanese kanji create a unique layer of semantic networking that has no parallel in alphabetic languages. Words sharing a kanji character often share a semantic component:

- 教: {教|おし}える (teach), {教育|きょういく} (education), {教師|きょうし} (teacher), {教室|きょうしつ} (classroom), {教科書|きょうかしょ} (textbook)
- 食: {食|た}べる (eat), {食事|しょくじ} (meal), {食品|しょくひん} (food product), {食欲|しょくよく} (appetite), {食堂|しょくどう} (cafeteria)

These kanji-mediated families create a web of semantic associations that a learner can exploit: recognizing that 教 means "teach/instruct" helps predict the meaning of any compound containing it. je-dict-1's **kanji index** feature (`kanji/`) makes this network navigable by listing all entries containing a given kanji.

### Stratal synonymy

The three vocabulary strata (wago, kango, gairaigo) produce systematic near-synonym triplets that are a distinctive feature of the Japanese lexicon (see [Gairaigo: Loanwords in Japanese](gairaigo-loanwords.md)):

| Wago | Kango | Gairaigo | English |
|------|-------|----------|---------|
| {食|た}べ{物|もの} | {食品|しょくひん} | フード | food |
| {買|か}い{物|もの} | {購買|こうばい} | ショッピング | shopping |
| {泊|と}まる | {宿泊|しゅくはく}する | ステイする | stay (overnight) |

These stratal synonyms differ predictably in register (wago = casual/native, kango = formal/written, gairaigo = modern/casual) and in collocational range. Learner dictionaries that make the stratal relationship explicit — "this is the kango equivalent of X" — help learners navigate the register landscape.

### Transitivity pairs as sense relations

As noted in [Verb Transitivity Pairs](../topics/verb-transitivity.md), Japanese has hundreds of transitive/intransitive verb pairs connected by regular morphological patterns. These are a unique type of sense relation — not synonym, not antonym, but a grammatical alternation that preserves core meaning while shifting agency. The dictionary must handle these as a first-class relation type.

## Implications for je-dict-1

### Cross-reference system as a sense relation network

je-dict-1's cross-reference system already implements a basic sense relation network with typed relationships: `synonym`, `antonym`, `related`, `contrast`, `hypernym`, `hyponym`, `transitive pair`, `intransitive pair`, `honorific form`, `humble form`, and others. With 16,275 cross-references across 28,465 entries (0.57 per entry), the network is growing but still sparse compared to what a learner-focused sense relation system could provide.

**Priorities for enrichment**:

1. **Co-hyponym clusters**: Semantic field members (all color terms, all emotion words, all direction words) should be systematically cross-referenced. Currently, some clusters are well-linked while others are not.
2. **Hypernym links**: Few entries link to their superordinate category. Adding `hypernym` links (e.g., {犬\|いぬ} → {動物\|どうぶつ}) would enable top-down browsing.
3. **Stratal synonym links**: Near-synonyms from different vocabulary strata should be systematically cross-referenced with a `synonym` or `contrast` relationship, with notes explaining the register difference.

### Synonym discrimination as a polishing priority

The "SIMILAR WORDS" section in entry notes is the primary vehicle for synonym discrimination. Research shows this is one of the highest-value features a learner dictionary can offer — learners consistently struggle with near-synonyms, and the distinctions (register, collocation, nuance) are not inferable from translation equivalents alone. The current consistency checker could be extended to identify entries with known near-synonyms that lack a SIMILAR WORDS section.

### The clustering lesson for browsing design

The semantic clustering research suggests that the dictionary's browsing and cross-reference features serve **vocabulary consolidation** rather than initial acquisition. Design decisions should optimize for the consolidation use case:

- **Contrastive presentation**: When a learner follows a cross-reference from {暑い\|あつい} to {熱い\|あつい}, the destination entry should make the contrast immediately visible (not buried in notes).
- **Small cluster sizes**: Presenting 3-5 related words at a time is more effective than exhaustive lists of 10+ items.
- **Explicit dimensions of difference**: The note should state *how* the words differ (register, collocation, scope, connotation), not just *that* they're related.

### Kanji-based semantic browsing

The existing kanji index provides a navigable semantic network based on shared characters. This feature could be enhanced to show the semantic relationships between entries sharing a kanji, going beyond a flat list to show how the shared character contributes different meaning facets across compounds.

## References

- Aitchison, J. (1987; 4th ed. 2012). *Words in the Mind: An Introduction to the Mental Lexicon*. Wiley-Blackwell.
- Bond, F., Isahara, H., Fujita, S., Uchimoto, K., Kuribayashi, T. & Kanzaki, K. (2009). Enhancing the Japanese WordNet. *Proceedings of the 7th Workshop on Asian Language Resources (ALR7)*.
- Cruse, D. A. (1986). *Lexical Semantics*. Cambridge University Press.
- Fellbaum, C. (ed.) (1998). *WordNet: An Electronic Lexical Database*. MIT Press.
- Hoshino, Y. (2010). The categorical facilitation effects on L2 vocabulary learning in a classroom setting. *RELC Journal*, 41(3), 301–312.
- Ishii, T. (2015). Semantic connection or visual connection: Investigating the true source of confusion. *Language Teaching Research*, 19(6), 712–722.
- Jiang, N. (2000). Lexical representation and development in a second language. *Applied Linguistics*, 21(1), 47–77.
- Lyons, J. (1977). *Semantics*. Cambridge University Press.
- Miller, G. A. (1995). WordNet: A lexical database for English. *Communications of the ACM*, 38(11), 39–41.
- Murphy, M. L. (2003). *Semantic Relations and the Lexicon: Antonymy, Synonymy, and Other Paradigms*. Cambridge University Press.
- Nation, I. S. P. (2000). Learning vocabulary in lexical sets: Dangers and guidelines. *TESOL Journal*, 9(2), 6–10.
- Nation, I. S. P. (2001). *Learning Vocabulary in Another Language*. Cambridge University Press.
- Read, J. (2004). Plumbing the depths: How should the construct of vocabulary knowledge be defined? In P. Bogaards & B. Laufer (Eds.), *Vocabulary in a Second Language* (pp. 209–227). John Benjamins.
- Tinkham, T. (1993). The effect of semantic clustering on the learning of second language vocabulary. *System*, 21(3), 371–380.
- Tinkham, T. (1997). The effects of semantic and thematic clustering on the learning of second language vocabulary. *Second Language Research*, 13(2), 138–163.
- Waring, R. (1997). The negative effects of learning words in semantic sets: A replication. *System*, 25(2), 261–274.

## Related pages

- [Cross-Reference Design](../topics/cross-references.md) — je-dict-1's cross-reference types, coverage, and improvement plans
- [Vocabulary Acquisition](vocabulary-acquisition.md) — how L2 learners build and organize lexical knowledge
- [Translation Equivalence](translation-equivalence.md) — the bilingual mapping problem and cross-linguistic asymmetry
- [Definition and Gloss Strategies](definition-strategies.md) — synonym discrimination in glosses and notes
- [Polysemy and Sense Discrimination](polysemy-sense-discrimination.md) — sense division within entries
- [Semantic Prosody](semantic-prosody.md) — evaluative colouring that distinguishes near-synonyms
- [Collocations in Learner Dictionaries](collocations.md) — collocational patterns as a dimension of synonym difference
- [Gairaigo: Loanwords in Japanese](gairaigo-loanwords.md) — stratal synonymy and register differences
- [Verb Transitivity Pairs](../topics/verb-transitivity.md) — transitivity pairs as a Japanese-specific sense relation
- [Word Formation and Morphology](word-formation.md) — kanji-based word families and semantic transparency
- [Digital Dictionary UX](digital-dictionary-ux.md) — interface affordances for navigating semantic networks
- [Register and Formality Marking](register-formality-marking.md) — stratal synonymy as a register dimension and cross-reference strategy
- [Vocabulary Learning Strategies](vocabulary-learning-strategies.md) — the semantic clustering debate and its implications for learning vs. consolidation
- [Near-Synonym Discrimination](near-synonym-discrimination.md) — dimensions of near-synonym difference, dictionary presentation strategies, and Japanese stratal register pairs
