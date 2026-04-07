# Learner Lexicography

**Last updated**: 2026-04-07

## What is learner lexicography?

Learner lexicography (pedagogical lexicography) is the branch of dictionary-making concerned with producing reference works tailored to language learners rather than native speakers. The field emerged from the recognition that general-purpose dictionaries fail learners in specific, predictable ways.

## Key principles

### Controlled defining vocabulary
Learner's dictionaries restrict definitions to a limited set of high-frequency words (typically 2,000-3,000). The Longman Defining Vocabulary (~2,000 words) pioneered this approach, ensuring definitions don't contain words harder than the headword itself.

**Relevance to je-dict-1**: The three-tier system serves a similar function. Definitions are in English (the learner's L1), so vocabulary control in definitions is less critical, but example sentences and notes should be accessible.

### Extensive example sentences
While native-speaker dictionaries give brief illustrative phrases, learner dictionaries provide full, natural sentences showing collocations, grammatical patterns, and register. Examples are often corpus-derived but edited for clarity. Research shows that example sentences are the most-consulted part of learner dictionary entries after the definition itself.

### Explicit grammatical coding
Learner dictionaries encode syntactic behavior: transitivity, countability, complementation patterns. This information is implicit knowledge for native speakers but must be made explicit for learners.

**Relevance to je-dict-1**: The v2 quality standards emphasize exactly this — verb transitivity, particle patterns, aspect behavior.

### Production vs. reception
A key design axis. Decoding (reception) dictionaries help learners understand text; encoding (production) dictionaries help learners generate correct output. Good learner dictionaries serve both, but design trade-offs exist.

| Feature | Receptive (decoding) | Productive (encoding) |
|---------|---------------------|----------------------|
| **Primary need** | "What does this word mean?" | "How do I say this?" |
| **Key information** | Definitions, glosses | Collocations, syntax, register |
| **Example function** | Illustrate meaning | Model correct usage |
| **Sense ordering** | Frequency-based | By communicative function |
| **Cross-references** | Less critical | Essential (synonyms, contrasts) |

**Relevance to je-dict-1**: The dictionary primarily serves receptive use (looking up unfamiliar words while reading) but also supports production through collocations, example sentences, and usage notes. The notes field is where productive information lives — collocations, similar-word distinctions, and register guidance.

### Graded entry complexity
Entries for high-frequency polysemous words require careful sense ordering, typically by frequency or cognitive salience rather than historical etymology. See [Definition Strategies](definition-strategies.md) for detailed discussion of sense ordering approaches.

## The monolingual vs. bilingual debate

A long-standing debate in language pedagogy concerns whether learners should use monolingual (L2-L2) or bilingual (L1-L2) dictionaries. Research has increasingly challenged the traditional teaching orthodoxy that monolingual dictionaries are inherently superior.

### Key findings

- **Laufer & Hadar (1997)**: Tested 123 learners using monolingual, bilingual, and "bilingualised" dictionaries. Bilingual and bilingualised entries produced better comprehension scores than monolingual entries.
- **Laufer & Kimmel (1997)**: Studied how learners actually use bilingualised dictionaries. Found that the format accommodates all individual preferences — learners can use the L1 translation, the L2 definition, or both.
- **Lew (2004)**: Found that Polish learners of English performed better with bilingual dictionaries across multiple tasks, challenging the assumption that monolingual dictionaries build deeper L2 competence.

### Bilingualised dictionaries

A bilingualised (or semi-bilingual) dictionary provides both: a monolingual definition in the target language plus an L1 translation. Major examples include the *Password* series and the *Kernerman Semi-Bilingual Dictionaries*. Research consistently shows this format outperforms pure monolingual or pure bilingual dictionaries for most learners at most proficiency levels.

**Relevance to je-dict-1**: je-dict-1 is a bilingual JE dictionary with English definitions and Japanese examples. The entry structure effectively functions as a bilingualised dictionary in reverse: English explanations (L1 for the target user) combined with Japanese example sentences and collocations (L2 in context). This hybrid approach aligns with research showing the superiority of combined L1/L2 information.

## Dictionary structure

Modern lexicographic theory divides dictionary structure into four components:

| Component | What it covers | je-dict-1 implementation |
|-----------|---------------|-------------------------|
| **Macrostructure** | The ordered list of headwords; what's in the dictionary and how it's organized | Entries in JSON files, browsable alphabetically and by tags; three-tier vocabulary system |
| **Microstructure** | The internal structure of each entry: definitions, examples, notes, cross-references | Defined by `build/schema.json`; senses, examples, notes, collocations, conjugations |
| **Mediostructure** | Cross-referencing system linking entries to each other | `cross_references` and `prominent_see_also` fields; inline word links (⟦...⟧) |
| **Access structure** | How users find what they need: search, browse, index | Three parallel search indexes (romaji, kana, English); tag-based browsing; kanji index |

The access structure is especially important for digital dictionaries, where users arrive via search rather than browsing alphabetically. See [Digital Dictionary UX](digital-dictionary-ux.md) for je-dict-1's search architecture.

## Theoretical foundations

### Frame semantics

Atkins and Fillmore's work on frame semantics (2009) fundamentally influenced modern learner lexicography. The core insight is that words are understood relative to conceptual frames — background knowledge structures that organize experience. A word like "buy" invokes a commercial transaction frame with roles (buyer, seller, goods, money) that the dictionary should make explicit.

For learner dictionaries, this means definitions should evoke the conceptual frame, not just provide synonyms. This is particularly relevant for Japanese words that invoke cultural frames unfamiliar to English speakers (e.g., 恩 evokes a debt/obligation frame distinct from English "favor").

### Prototype theory

Rosch's prototype theory (1975) informs sense ordering and definition writing. Word meanings cluster around prototypical instances rather than having sharp boundaries. Learner dictionaries benefit from defining the prototype first, then extending to peripheral senses — a strategy je-dict-1 uses when ordering numbered senses.

## Notable researchers and works

| Who | Contribution |
|-----|-------------|
| **A.S. Hornby** | Created the Oxford Advanced Learner's Dictionary (1948), the prototype for all modern EFL learner dictionaries |
| **Michael Rundell** | Editor of Macmillan English Dictionary; co-author of *Oxford Guide to Practical Lexicography* (with Atkins, 2008) |
| **B.T.S. Atkins (Sue Atkins)** | Pioneer in computational and pedagogical lexicography; co-developed the "word sketch" concept with Kilgarriff |
| **John Sinclair** | Led the COBUILD project (1987), the first dictionary built primarily from corpus evidence |
| **Robert Ilson, Reinhard Hartmann** | Key metalexicographers; shaped the theoretical foundations of the field |

### The "Big Five" EFL dictionaries
OALD (Oxford), LDOCE (Longman), COBUILD (Collins), CALD (Cambridge), MALD (Macmillan) represent decades of competing approaches to learner lexicography. Each makes different trade-offs on the principles above.

## Practical implications for je-dict-1

- Use frequency data to determine headword selection and sense ordering
- Prioritize collocational and syntactic information — learners need to know how a word combines, not just what it means
- Provide graduated example sentences (simple to complex) within each entry
- Make explicit what native speakers know implicitly: register, formality, aspect behavior
- The notes field is where je-dict-1 bridges the gap between a simple bilingual glossary and a true learner's dictionary

## Further reading

- Atkins, B.T.S. & Rundell, M. (2008). *The Oxford Guide to Practical Lexicography*. Oxford University Press.
- Laufer, B. & Hadar, L. (1997). "Assessing the effectiveness of monolingual, bilingual, and 'bilingualised' dictionaries." *Modern Language Journal*, 81(2), 189-196.
- Laufer, B. & Kimmel, M. (1997). "Bilingualised dictionaries: How learners really use them." *System*, 25(3), 361-369.
- Lew, R. (2004). *Which Dictionary for Whom? Receptive Use of Bilingual, Monolingual and Semi-bilingual Dictionaries by Polish Learners of English*. Motivex.
- Nation, I.S.P. (2001). *Learning Vocabulary in Another Language*. Cambridge University Press.
- Hartmann, R.R.K. (2001). *Teaching and Researching Lexicography*. Longman.
- Fillmore, C.J. & Atkins, B.T.S. (2009). "Describing polysemy: the case of 'crawl'." In *Polysemy in Cognitive Linguistics*, Cuyckens, H. & Zawada, B. (eds.), John Benjamins.

## Related pages

- [Definition Strategies](definition-strategies.md) — practical techniques for writing effective glosses
- [Example Sentence Design](example-sentences.md) — what makes effective dictionary examples
- [Translation Equivalence](translation-equivalence.md) — the bilingual mapping problem
- [Digital Dictionary UX](digital-dictionary-ux.md) — search and access structure design
- [Japanese Lexicography](japanese-lexicography.md) — challenges specific to Japanese dictionaries
- [Vocabulary Acquisition](vocabulary-acquisition.md) — how L2 learners acquire vocabulary
- [Quality Standards](../project/quality-standards.md) — je-dict-1's entry quality standards
- [Entry Design](../project/entry-design.md) — je-dict-1's microstructure
