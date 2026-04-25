# Grammar Information in Learner Dictionaries

**Last updated**: 2026-04-25

## Overview

How should a dictionary present grammatical information? This question has occupied lexicographers since A.S. Hornby's pioneering verb-pattern tables in the 1940s. For bilingual learner dictionaries like je-dict-1, grammar information is especially critical: learners need not just definitions but syntactic guidance to produce correct output. This page surveys the grammar-encoding traditions of English-language learner dictionaries, reviews what research says about how learners actually use grammatical information, examines Japanese-specific challenges, and draws implications for je-dict-1's entry design.

## Types of grammatical information in dictionaries

Grammatical information in dictionaries can be categorized by what it tells the user and how it is encoded.

### What grammar information covers

| Category | What it tells the user | Examples |
|----------|----------------------|----------|
| **Part of speech** | Word class | noun, verb, adjective, adverb |
| **Inflectional morphology** | How the word changes form | conjugation tables, irregular forms |
| **Syntactic patterns** | What structures the word takes | verb complementation, adjective predication |
| **Valency / argument structure** | What arguments a verb requires | transitive/intransitive, case frames |
| **Selectional restrictions** | What kinds of words fill each slot | animate subjects, concrete objects |
| **Collocational patterns** | What words habitually co-occur | noun + verb, adjective + noun pairings |
| **Register constraints** | Where the word is appropriate | formal writing, casual speech, technical contexts |

### How grammar information is encoded

Dictionaries have used at least four distinct encoding strategies, each with different usability profiles.

**1. Opaque codes (OALD 1st–3rd ed.)**
Hornby's original system used algebraic labels like `[VP6A]` and `[VP19B]` for verb patterns. Users had to consult a reference table to decode them. Wekker (1992) criticized these as virtually inaccessible to all but the most dedicated users.

**2. Semi-transparent codes (OALD 4th ed., LDOCE)**
The OALD 4th edition (1989) replaced opaque codes with more readable labels like `[Tn]` (transitive + noun object), `[Tf]` (transitive + that-clause), and `[Ipr]` (intransitive + prepositional phrase). Wekker (1992) evaluated these against six user-friendliness criteria — unambiguity, self-explanatory coding, interpretability without a reference table, example-code alignment, indication of transformational possibilities, and completeness — and found the OALD 4th edition system superior to its competitors.

**3. Natural-language pattern descriptions (OALD 10th ed., COBUILD)**
Modern learner dictionaries have moved toward spelling out patterns in plain language: "acknowledge sb/sth", "decide to do sth", "interested in sth/doing sth". The COBUILD dictionary (Sinclair 1987) went further with full-sentence definitions that embed syntactic information in the definition itself ("If you *decide to* do something, you choose to do it"). The OALD 10th edition uses spelled-out patterns with "sb" and "sth" placeholders, a significant shift from the code-based traditions.

**4. Grammar-through-examples (implicit encoding)**
Rather than providing explicit codes, some dictionaries rely on carefully designed example sentences to demonstrate syntactic patterns. Frankenberg-Garcia (2015) found that learners prefer to extract grammatical information from examples rather than from codes or labels. This approach works best when examples are specifically designed for encoding (production support) rather than purely for meaning illustration.

### The historical trend

The progression from opaque codes → semi-transparent codes → natural-language descriptions → grammar-through-examples reflects a broader principle: **grammatical information is most useful when it is most transparent**. Research consistently shows that learners underuse or ignore coded grammar information but engage with examples and plain-language explanations.

## Do learners actually use grammar information?

### The consultation gap

Multiple studies reveal a troubling gap between the grammar information dictionaries provide and what users actually consult.

**Nesi & Haill (2002)** studied 89 EFL/ESL students using paper dictionaries for reading assignments and found that students frequently fail to identify parts of speech, which hinders their dictionary searches. Many looked only at the first definition that seemed plausible, ignoring grammatical codes entirely.

**Tono (2001)** documented through eye-tracking research that dictionary users spend most of their time on definitions and examples, with grammar codes receiving minimal attention. In a five-stage lookup process — locating the entry, scanning sub-entries, selecting a sense, extracting relevant information, and integrating it — grammar information is typically bypassed unless the learner has been explicitly trained to use it.

**Herbst (1989)** argued that grammar codes in dictionaries are used mainly by teachers and linguists rather than by the learners they were designed for. His subsequent work on valency dictionaries (Herbst et al. 2004) sought to make argument-structure information more accessible through pattern-based presentation.

### What learners do use

The evidence suggests learners extract grammatical knowledge primarily through:

1. **Example sentences** — by far the most-used entry component after the definition (see [Example Sentence Design](example-sentences.md)). Well-designed examples implicitly teach syntax, collocation, and register.
2. **Natural-language usage notes** — explanations like "usually used with negative verbs" or "followed by a noun phrase" are read and understood, unlike coded grammar labels.
3. **Pattern illustrations** — "decide to do sth", "prevent sb from doing sth" — readable shorthand that doubles as a template for production.

### Implications for dictionary design

These findings suggest that dictionary grammar information should be:
- **Integrated into examples** rather than isolated in codes
- **Written in natural language** rather than using abbreviations or symbols
- **Targeted at known difficulty points** rather than comprehensively systematic
- **Redundant** — the same grammatical point conveyed through multiple channels (label, example, note)

## The grammar-example nexus

Frankenberg-Garcia (2012, 2014, 2015) developed the concept of **encoding examples** — examples specifically designed to support language production, as opposed to decoding examples that merely illustrate meaning.

| Property | Decoding example | Encoding example |
|----------|-----------------|------------------|
| **Purpose** | Clarify meaning | Model correct usage |
| **Shows** | Typical context | Syntactic pattern + collocation |
| **Vocabulary** | Controlled for comprehension | Controlled for pattern visibility |
| **Quantity** | 1-2 per sense sufficient | Multiple needed to show pattern range |

The distinction matters because a single example can serve both purposes if designed carefully. An example like "彼女は毎日ジョギングすることに決めた" (She decided to jog every day) simultaneously illustrates the meaning of 決める and models the ～ことに決める pattern.

## Japanese-specific challenges

Japanese grammar presents several challenges that go beyond what English-centric learner lexicography has addressed.

### Particle-verb dependencies

Japanese verbs select specific particles for their arguments, and the particle choice often changes meaning:

- 学校**に**行く (go **to** school — destination)
- 学校**で**遊ぶ (play **at** school — location of action)
- 学校**を**出る (leave school — departure point)

Unlike English prepositions, which are partly predictable from spatial metaphors, Japanese particle-verb pairings must often be learned as fixed combinations. This makes particle information in verb entries essential for production — a point reflected in je-dict-1's v2 quality standards, which list particle predicate lists as a high priority.

### Transitivity pairs

Japanese has a highly productive system of transitive/intransitive verb pairs that has no parallel in English (see [Verb Transitivity Pairs](../topics/verb-transitivity.md)). A dictionary must:
- Clearly label each verb as 自動詞 or 他動詞
- Link paired verbs bidirectionally
- Illustrate the semantic difference in examples (agent-focused vs. change-of-state)
- Explain which form to use in production contexts

Learner resources consistently identify transitivity pairs as one of the most persistent L2 acquisition challenges for English-speaking learners of Japanese.

### Verb conjugation complexity

Japanese verbs conjugate across multiple dimensions — tense, aspect, mood, politeness, voice — producing dozens of forms from a single lemma. The five verb classes (godan, ichidan, suru, kuru, irregular) follow different conjugation patterns. Learner dictionaries must decide how much conjugation information to include.

The Makino & Tsutsui *Dictionary of Japanese Grammar* series (basic, intermediate, advanced; ~200 entries each) took a radical approach: organize the entire dictionary around grammatical patterns rather than individual words, providing extensive examples and contrastive notes for each pattern. This works well as a grammar reference but doesn't replace a vocabulary dictionary — learners need both.

### Aspect and ている

The Japanese progressive/resultative marker ている has well-known polysemy that trips up learners:
- 食べている = is eating (ongoing action)
- 結婚している = is married (resultative state)
- 角が丸くなっている = has become rounded (resultant state)
- 毎日走っている = runs every day (habitual action)

The aspect behavior of ている with a given verb is partly predictable from the verb's lexical aspect (Kindaichi's four-way classification) but has many exceptions. This is exactly the kind of grammatical information that is not inferrable from a translation equivalent and must be stated explicitly in the dictionary entry.

### Keigo (honorific system)

Japanese grammatical politeness is not just a register label but a morphological system with its own verb conjugations (尊敬語, 謙譲語, 丁寧語). Learners need to know not just that a word is "formal" but which specific honorific forms exist and when each is used.

## Grammar information in the Makino & Tsutsui model

The *Dictionary of Japanese Grammar* series (Makino & Tsutsui 1986/1995/2008) set a standard for how Japanese grammatical patterns can be explained to English-speaking learners. Each entry follows a consistent structure:

1. **Pattern name** — the grammatical form being explained
2. **Brief English equivalent** — a one-line translation/explanation
3. **Formation rules** — how the pattern is constructed morphologically
4. **Detailed notes** — numbered paragraphs explaining nuances, restrictions, and common errors
5. **Example sentences** — multiple graded examples (simple → complex) with translations
6. **Related expressions** — contrastive analysis with similar patterns

This structure — combining explicit rule statement with abundant examples and contrastive notes — aligns well with the research finding that learners benefit most from natural-language explanations reinforced by examples.

## Valency dictionaries

Herbst et al. (2004) created *A Valency Dictionary of English* that foregrounds argument structure. Each verb entry specifies its valency frames — what arguments it takes, whether they are obligatory or optional, and what form they take.

The valency approach is particularly relevant to Japanese because:
- Japanese verbs have relatively fixed particle-argument structures
- Particle choice is not predictable from English translations
- Verbs with the same English equivalent may take different particles (e.g., 乗る takes に, 乗せる takes を)
- Compound verbs inherit or modify the valency of their components

je-dict-1's particle pattern documentation in entry notes functions as an informal valency description, though without the systematic notation of a formal valency dictionary.

## Implications for je-dict-1

### What je-dict-1 already does well

1. **Natural-language notes**: Grammar information lives in the prose notes field with labeled sections (USAGE, TRANSITIVITY, etc.) rather than in opaque codes. This aligns with research showing natural-language descriptions are more effective than coded systems.

2. **Conjugation tables**: Full hard-coded conjugation data for all verbs and i-adjectives, generated by `add_conjugations.py` / `add_adjective_conjugations.py`. This goes beyond what most online Japanese dictionaries offer.

3. **Transitivity marking and pair linking**: The v2 quality standards mandate transitivity labels and `prominent_see_also` links between pairs — addressing one of the most important Japanese-specific grammar needs.

4. **Aspect documentation**: The polish_aspect_notes task adds ている behavior notes to verbs with non-obvious aspect, directly addressing the aspect polysemy challenge.

5. **Example-based grammar teaching**: With over 101,800 examples averaging 4.0 per entry, the dictionary provides substantial implicit grammar input through examples.

### Areas for potential improvement

1. **Particle-verb patterns in verb entries**: The v2 quality standards flag particle predicate lists as high priority. Beyond listing particles in notes, verb entries could include pattern templates (e.g., "X**を**食べる", "X**に**住む") in a standardized format.

2. **Encoding-optimized examples**: Some examples primarily illustrate meaning (decoding). Deliberately designing at least one example per sense to showcase the syntactic pattern would improve production support.

3. **Contrastive grammar notes**: Where two words differ grammatically but have similar translations (e.g., ～ている vs. ～てある, ～ようにする vs. ～ことにする), notes could explain the grammatical contrast explicitly.

4. **Systematizing particle information**: Rather than free-form particle notes, a structured field listing particle-argument frames would enable both human reading and computational use (e.g., search by particle pattern).

5. **Grammar-entry cross-references**: Entries for grammatically complex words could link to external grammar resources or to the dictionary's own particle entries, creating a navigable grammar network alongside the vocabulary network.

## References

- Atkins, B. T. S. & Rundell, M. (2008). *The Oxford Guide to Practical Lexicography*. Oxford University Press.
- Frankenberg-Garcia, A. (2012). Learners' use of corpus examples. *International Journal of Lexicography*, 25(3), 273–296.
- Frankenberg-Garcia, A. (2014). The use of corpus examples for language comprehension and production. *ReCALL*, 26(2), 128–146.
- Frankenberg-Garcia, A. (2015). Dictionaries and encoding examples to support language production. *International Journal of Lexicography*, 28(4), 490–512.
- Herbst, T. (1989). Grammar in dictionaries. In M. L. Tickoo (Ed.), *Learner's Dictionaries: State of the Art*. SEAMEO RELC.
- Herbst, T., Heath, D., Roe, I. F., & Götz, D. (2004). *A Valency Dictionary of English*. Mouton de Gruyter.
- Hornby, A. S. (1942). *Idiomatic and Syntactic English Dictionary*. Kaitakusha.
- Makino, S. & Tsutsui, M. (1986). *A Dictionary of Basic Japanese Grammar*. The Japan Times.
- Makino, S. & Tsutsui, M. (1995). *A Dictionary of Intermediate Japanese Grammar*. The Japan Times.
- Nesi, H. & Haill, R. (2002). A study of dictionary use by international students at a British university. *International Journal of Lexicography*, 15(4), 277–305.
- Sinclair, J. (1987). *Collins COBUILD English Language Dictionary*. Collins.
- Tono, Y. (2001). *Research on Dictionary Use in the Context of Foreign Language Learning*. Max Niemeyer.
- Wekker, H. (1992). Grammar coding in the Oxford Advanced Learner's Dictionary of Current English. *International Journal of Applied Linguistics*, 2(1), 88–99.

## Related pages

- [Learner Lexicography](learner-lexicography.md) — broader context of pedagogical dictionary design
- [Example Sentence Design](example-sentences.md) — how examples carry implicit grammar information
- [Collocations in Learner Dictionaries](collocations.md) — overlap between collocational and grammatical patterns
- [Entry Design](../project/entry-design.md) — je-dict-1's schema and field structure
- [Quality Standards](../project/quality-standards.md) — v2 grammar-related priorities
- [Verb Transitivity Pairs](../topics/verb-transitivity.md) — transitivity pair presentation
- [Definition and Gloss Strategies](definition-strategies.md) — COBUILD's grammar-in-definitions approach
- [Dictionary Lookup Behavior](dictionary-lookup-behavior.md) — how users navigate entries
- [Multiword Expressions](multiword-expressions.md) — grammar patterns (〜について, 〜てしまう) as a category of MWE
- [Error Analysis and Learner Corpora](error-analysis-japanese-l2.md) — structural and particle errors that grammar encoding should preempt
