# Dictionary Microstructure and Information Architecture

**Last updated**: 2026-05-31

## Overview

The microstructure of a dictionary is the systematic internal organization of individual entries — the types of information included, their ordering, their typographic presentation, and the relationships between them. If the macrostructure determines *which* words a dictionary contains and how they are accessed, the microstructure determines *what the user sees* once they arrive at an entry. Microstructure design directly affects lookup success, reading time, and the depth of knowledge a user extracts from a consultation.

The term was established by Wiegand (1989) as part of a comprehensive structural theory of dictionaries, alongside macrostructure (headword list), mediostructure (cross-referencing system), and access structure (the paths a user follows to reach information). The field has evolved significantly with the shift from print to digital, but the core questions remain: what information belongs in an entry, in what order, and how should it be presented?

## Wiegand's structural framework

Herbert Ernst Wiegand developed the most influential theoretical account of dictionary article structure over three decades of work (1984–2009). His framework treats dictionary entries as structured texts whose components can be formally analyzed.

### Two-part division

Wiegand divides each dictionary article into two main components:

1. **Form comment** (*Formkommentar*): information about the word's form — spelling, pronunciation, morphological properties, inflectional paradigm
2. **Semantic comment** (*semantischer Kommentar*): information about the word's meaning — definitions, translations, examples, usage labels, semantic relations

This binary division is present in virtually every dictionary tradition, though the balance between the two varies by dictionary type.

### Item types and addressing

Wiegand distinguishes between different types of lexicographic items:

- **Items giving form** (*Formangaben*): headword spelling, pronunciation transcription, inflection tables
- **Items giving meaning** (*Bedeutungsangaben*): definitions, translation equivalents, glosses
- **Items giving pragmatics** (*pragmatische Angaben*): usage labels, register markers, domain labels
- **Items giving syntagmatics** (*syntagmatische Angaben*): collocations, example sentences, grammatical patterns

Each item has an **address** — the element it provides information about. In *lemmatic addressing*, items relate back to the headword. In *sublemmatic addressing*, items relate to a subentry or run-on. In *non-lemmatic addressing*, items relate to other items within the entry (e.g., a usage label that applies to a specific sense rather than to the whole entry).

### Integrated vs. non-integrated microstructures

Wiegand (1996) distinguishes:

- **Integrated microstructure**: all information about a sense (definition, examples, collocations, labels) is grouped together under that sense number, then repeated for each subsequent sense
- **Non-integrated microstructure**: some information categories are presented in blocks separate from sense divisions (e.g., all pronunciation information at the top, all collocations at the bottom, regardless of sense)

Most modern learner dictionaries use integrated microstructures, since users consulting a polysemous entry need to match the right example and the right collocation to the right sense.

## Information categories

### Core categories (present in virtually all dictionaries)

| Category | Content | Print conventions |
|----------|---------|-------------------|
| **Headword** | Citation form, orthography | Bold, larger font |
| **Pronunciation** | Phonetic/phonemic transcription | IPA in slashes or brackets |
| **Part of speech** | Grammatical category | Abbreviated italic label |
| **Inflection** | Irregular forms, paradigm information | Abbreviated or tabular |
| **Definition/gloss** | Meaning explanation or translation equivalent | Roman text |
| **Examples** | Illustrative sentences or phrases | Italic or indented |

### Extended categories (common in learner dictionaries)

| Category | Content | Function |
|----------|---------|----------|
| **Frequency indicators** | Band markers, frequency labels | Guide vocabulary priority |
| **Register/usage labels** | Formal, informal, slang, technical | Constrain appropriate contexts |
| **Collocations** | Common word combinations | Support production |
| **Grammatical patterns** | Valency frames, complementation | Encode syntactic behavior |
| **Semantic relations** | Synonyms, antonyms, hypernyms | Build vocabulary networks |
| **Cross-references** | Links to related entries | Enable exploration |
| **Cultural notes** | Encyclopedic or pragmatic information | Contextualize usage |
| **Pictures/illustrations** | Visual referents | Disambiguate concrete nouns |

### Lehmann's comprehensive model

Lehmann (2024) proposes a maximum microstructure model with seven information domains: (A) entry identity (lemma, homonym number, sense number), (B) expression (phonology, sound, orthographic variants), (C) language variety (dialect, sociolect, style, historical stage), (D) structure (syntax, morphology, word formation, valency, phraseology), (E) meaning (definitions, glosses, semantic classes, semantic relations, encyclopedic information), (F) genetic-historical information (etymology, cognates), and (G) methodology (sources, comments, timestamps). This maximal model is designed so that "not every field will be needed in every case" — blank fields are preferable to structural expansion later.

## Sense ordering

For polysemous entries, how senses are ordered is one of the most consequential microstructural decisions. Three main approaches exist:

### Frequency-based ordering

Senses are arranged by decreasing frequency of use, so the most common meaning appears first. This is the approach COBUILD pioneered and that most modern learner dictionaries have adopted. The rationale: the sense the learner most likely needs should be the one they encounter first.

**Advantages**: matches the probability of what the user is looking for; reduces scanning time for common lookups.

**Disadvantages**: requires reliable corpus frequency data per sense (not just per lemma); the most frequent sense is sometimes the most obvious and least in need of a dictionary.

### Historical ordering

Senses are arranged chronologically, with the earliest attested meaning first and later developments following. This was the traditional approach in comprehensive dictionaries (OED, Kenkyusha) and persists in some scholarly dictionaries.

**Advantages**: reveals semantic development; provides etymological context.

**Disadvantages**: the historical sense may be archaic or obscure, putting the information the learner least needs in the most prominent position.

### Logical/semantic ordering

Senses are arranged from core/literal to peripheral/figurative, with related subsenses grouped together. This approach often uses a hierarchical scheme where major senses are numbered and subsenses are lettered.

**Advantages**: reveals semantic relationships; groups related meanings.

**Disadvantages**: "core" meaning is often a theoretical construct that doesn't match any actual use; hierarchy can be difficult to maintain consistently.

### The lumping-splitting spectrum

Orthogonal to ordering is the question of **granularity**: how many distinct senses to recognize. *Lumpers* group related uses under a single sense with a broad definition; *splitters* create fine-grained sense distinctions. Svensén (2009) notes that splitting "imposes a problem of knowing when to stop eliciting distinctions." Modern learner dictionaries tend toward moderate splitting — enough to prevent confusion, but not so much that the entry becomes unwieldy.

Wiegand's framework uses **hierarchical punctuation** to signal sense granularity: period (.) separates major senses, semicolon (;) separates subsenses, comma (,) separates near-synonymous paraphrases. This convention remains widespread in bilingual dictionaries.

## Sense navigation devices

Bogaards (1998) demonstrated that dictionary users dislike long entries and that the first definition in a polysemous entry "catches the user's eye" — alternative senses lower in the entry are often ignored. This finding motivated the development of sense navigation devices:

### Signposts (shortcuts)

Short labels placed before each sense that summarize the meaning in a word or two. LDOCE pioneered these (e.g., under *run*: **MOVE QUICKLY** | **MANAGE** | **MACHINE** | **FLOW**). Research by Lew (2010) found that entries with signposts produced significantly more accurate sense selection than entries without.

### Menus

A numbered overview of all senses placed at the top of the entry, before the detailed treatment begins. OALD's online edition uses this approach for highly polysemous entries. Nesi and Tan (2011) compared menus and signposts experimentally: both improved accuracy over unguided entries, with menus being slightly faster but signposts slightly more accurate.

### Digital collapsibility

Online dictionaries can show/hide senses interactively. Users first see the headword plus the sense menu, then expand only the sense they need. This progressive disclosure approach eliminates the scanning problem entirely, though it requires the user to make a selection decision before seeing the full definitions.

## The Big Four: microstructure comparison

The four major English learner dictionaries (OALD, LDOCE, COBUILD, CALD) illustrate different microstructural philosophies:

| Feature | OALD | LDOCE | COBUILD | CALD |
|---------|------|-------|---------|------|
| Sense ordering | Frequency/core | Frequency | Strict frequency | Frequency/core |
| Definition style | Analytical | Analytical | Full-sentence | Analytical |
| Signposting | Menus (online) | Signpost labels | — | Guided words |
| Frequency marking | Symbol scale | Frequency bands | ◆ diamonds | — |
| Collocation treatment | Integrated | Integrated | Word Partnership box | Integrated |
| Example source | Corpus-informed | Corpus-informed | Authentic corpus | Corpus-informed |
| Synonym discrimination | "Which Word?" boxes | "Word Choice" boxes | — | "Thesaurus" boxes |

COBUILD's full-sentence definitions (e.g., "If you *run*, you move more quickly than when you walk") represent a distinctive microstructural choice: the definition itself models the word's grammar, eliminating the need for separate grammatical codes. This approach is more readable but requires more space.

## Digital-era transformations

The shift from print to digital has transformed microstructure in several ways:

### Space constraints removed

Print dictionaries encoded information densely through abbreviations, symbols, and compressed typography because each page was costly. Digital dictionaries can use full words, expand abbreviations on hover, and allocate unlimited space per entry. This changes the calculus of what to include.

### Layered presentation

Information can be organized in layers of increasing detail:

1. **Summary layer**: headword, primary pronunciation, core definition(s)
2. **Standard layer**: all senses, examples, grammatical information, basic labels
3. **Extended layer**: collocations, semantic relations, cultural notes, etymology
4. **Expert layer**: corpus concordances, frequency data, usage notes

Users access deeper layers only when they need them. This is Tarp's (2008) **function-based** approach applied to microstructure: different user situations require different information, so the entry should adapt.

### Hyperlinked mediostructure

Print cross-references ("See also: X") required the user to close the current entry, find the referenced entry, and navigate to it. Digital cross-references are instantaneous links, making the mediostructure effectively part of the microstructure — semantic relations become navigable pathways rather than static labels.

### Multimedia integration

Audio pronunciation, video examples, interactive conjugation tables, and illustrated definitions are all microstructural elements that have no print equivalent. They don't replace textual information but add channels that serve different learning styles.

## Japanese-specific considerations

Japanese dictionaries face microstructural challenges that European-language dictionaries do not:

### Multiple representation layers

A single entry may need to present: the kanji form, one or more kana readings, romanization, and the mapping between kanji and readings (furigana). In European dictionaries, headword and pronunciation are two items; in Japanese dictionaries, the relationship between orthography and pronunciation is itself a complex information category.

### Conjugation as microstructural content

Japanese verb and adjective entries must present inflectional paradigms that are far richer than European equivalents. A single verb may have dozens of conjugated forms across formality levels and auxiliary combinations. Whether this information belongs in the microstructure of each entry (as a conjugation table) or in the macrostructure (as a separate grammar section with cross-references) is a design decision with significant usability implications.

### Transitivity pairs

Many Japanese verbs come in intransitive/transitive pairs (e.g., 開く/開ける, 閉まる/閉める) that share kanji but differ in conjugation class and meaning. The microstructure must make this pairing relationship prominent without conflating the two entries, since learners frequently confuse which form to use.

### Register stratification

Japanese vocabulary draws from three etymological strata (wago, kango, gairaigo) that correlate with register. The microstructure should surface this register information not just as a label but through contrastive examples and notes, since the stratal register system has no direct parallel in English.

### Script choice as information

Whether a word is conventionally written in kanji, hiragana, or katakana is itself meaningful information that European dictionaries don't need to address. The microstructure should indicate standard orthographic practice (e.g., "usually written in kana") as part of the form comment.

## Implications for je-dict-1

je-dict-1's JSON-based entry schema is itself a microstructure specification. The current structure maps onto Wiegand's framework as follows:

| Wiegand concept | je-dict-1 implementation |
|----------------|--------------------------|
| Form comment | `headword`, `reading`, `headword_alternatives`, `conjugation` |
| Semantic comment | `definitions[].meaning`, `definitions[].examples`, `notes` |
| Pragmatic items | `metadata.tags` (register, formality, semantic domain) |
| Syntagmatic items | `definitions[].collocations`, `definitions[].patterns` |
| Mediostructure | `cross_references`, `prominent_see_also`, inline `⟦...⟧` links |

### Current strengths

1. **Integrated microstructure**: examples and collocations are grouped under their respective definitions, matching modern learner dictionary best practice
2. **Rich mediostructure**: the cross-reference system (prominent_see_also, cross_references, inline links) provides multiple levels of semantic connection
3. **Conjugation tables**: presenting the full paradigm inline gives production support that most bilingual JE dictionaries omit
4. **Notes field**: the unstructured notes field allows entry-specific information (cultural context, aspect behavior, usage warnings) that rigid schema slots would not accommodate

### Areas for consideration

1. **Sense navigation for polysemous entries**: entries with multiple definitions currently have no signposting or menu system. For highly polysemous basic-tier entries (取る, 出る, 掛ける), the flat numbered list may make sense selection difficult. The static site could benefit from expandable sense summaries.
2. **Information layering**: all information in an entry is presented at the same level. A layered approach (core definition visible by default, notes/collocations/cross-references expandable) could reduce cognitive load for simple lookups while preserving depth for deeper consultation.
3. **Form comment completeness**: pitch accent information is absent from the microstructure (see [Pitch Accent](pitch-accent.md) for the research context). Adding it would enrich the form comment but requires a reliable data source.
4. **Register marking consistency**: the `formality` and `politeness` tags provide register information, but the tag vocabulary is coarse (see [Schema Tag Reliability](../topics/schema-tag-reliability.md)). Richer register information currently lives in the notes prose, where it is harder to search or filter.
5. **Example ordering**: the project guidelines specify "progressive length" for examples (short → long), but research suggests frequency-based sense ordering should also influence example ordering — the most prototypical use should appear first within each sense.

## Related pages

- [Entry Design](../project/entry-design.md) — je-dict-1's entry schema and required fields
- [Quality Standards](../project/quality-standards.md) — v2 quality standards
- [Polysemy and Sense Discrimination](polysemy-sense-discrimination.md) — sense division and ordering
- [Definition and Gloss Strategies](definition-strategies.md) — equivalence types and gloss writing
- [Dictionary Lookup Behavior](dictionary-lookup-behavior.md) — how users navigate entries
- [Dictionary Skills and Reference Skills Training](dictionary-skills-training.md) — sense selection as a skill
- [Digital Dictionary UX](digital-dictionary-ux.md) — interface design research
- [Grammar Information in Learner Dictionaries](grammar-in-dictionaries.md) — grammatical codes and patterns
- [Dictionary Evaluation and Metalexicography](dictionary-evaluation-metalexicography.md) — Wiegand's broader framework
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — tag quality issues in je-dict-1's metadata
- [Example Sentence Design](example-sentences.md) — example placement and sequencing within entry structure

## References

- Atkins, B. T. S. & Rundell, M. (2008). *The Oxford Guide to Practical Lexicography*. Oxford University Press.
- Bogaards, P. (1998). Scanning long entries in learner's dictionaries. In *Proceedings of the 8th EURALEX International Congress*, Liège.
- Hausmann, F. J. & Wiegand, H. E. (1989). Component parts and structures of general monolingual dictionaries. In F. J. Hausmann et al. (Eds.), *Wörterbücher/Dictionaries/Dictionnaires* (Vol. 1, pp. 328–360). De Gruyter.
- Lehmann, C. (2024). Microstructure: Structure of a lexical entry. University of Erfurt.
- Lew, R. (2010). Users take shortcuts: Navigating dictionary entries. In A. Dykstra & T. Schoonheim (Eds.), *Proceedings of the XIV EURALEX International Congress* (pp. 1121–1132).
- Lew, R. (2013). Identifying, ordering and defining senses. In H. Jackson (Ed.), *The Bloomsbury Companion to Lexicography* (pp. 284–302). Bloomsbury.
- Nesi, H. & Tan, K. H. (2011). The effect of menus and signposting on the speed and accuracy of sense selection. *International Journal of Lexicography*, 24(1), 79–96.
- Svensén, B. (2009). *A Handbook of Lexicography: The Theory and Practice of Dictionary-Making*. Cambridge University Press.
- Tarp, S. (2008). *Lexicography in the Borderland between Knowledge and Non-Knowledge*. Niemeyer.
- Tono, Y. (2001). *Research on Dictionary Use in the Context of Foreign Language Learning*. Niemeyer.
- Wiegand, H. E. (1989). Der Begriff der Mikrostruktur: Geschichte, Probleme, Perspektiven. In F. J. Hausmann et al. (Eds.), *Wörterbücher/Dictionaries/Dictionnaires* (Vol. 1, pp. 409–462). De Gruyter.
- Wiegand, H. E. (1996). Über die Mediostrukturen bei gedruckten Wörterbüchern. In A. H. Ibrahim (Ed.), *Lexiques-grammaires comparés et traitements automatiques* (pp. 11–43).
