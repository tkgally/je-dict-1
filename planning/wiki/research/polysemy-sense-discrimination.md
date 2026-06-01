# Polysemy and Sense Discrimination

**Last updated**: 2026-06-31

## Overview

Polysemy — the phenomenon of a single word having multiple related meanings — is one of the central challenges in lexicography. Every dictionary must decide how many senses a word has, how to order them, how to signal the relationships between them, and how finely to draw the distinctions. These decisions affect whether a learner can quickly find the right meaning, understand how meanings relate, and build a rich mental model of the word. This page surveys the theoretical landscape, practical approaches, and Japanese-specific challenges.

## The ontological question: do word senses exist?

Before discussing how to divide and order senses, it is worth acknowledging a foundational debate. Kilgarriff (1997), in his influential paper "I don't believe in word senses," argued that discrete word senses are not natural objects but abstractions created by lexicographers for practical purposes. In his view, the basic objects are corpus citations — actual occurrences of a word in context — and "senses" are clusters imposed on these occurrences according to whoever does the clustering and why.

This position does not invalidate dictionary-making, but it reframes it: sense division is a design decision, not a discovery. Different dictionaries legitimately arrive at different sense inventories for the same word, depending on their audience, purpose, and granularity preferences. For a learner's dictionary, the right question is not "what are the true senses?" but "what division of meaning best helps this learner understand and use the word?"

## Lumping vs. splitting

The fundamental tension in sense discrimination is between **lumping** (grouping related meanings under fewer, broader senses) and **splitting** (establishing more, finer distinctions). Neither approach is inherently correct; each serves different dictionary types and user needs.

### Arguments for lumping (fewer senses)

- Avoids overwhelming learners with a long list of subtly different meanings
- Reveals the underlying semantic unity of the word
- Reduces the "first-fit" problem (Nesi 1999), where users pick the first plausible-looking sense and stop reading
- More natural for reception-oriented use (reading comprehension)

### Arguments for splitting (more senses)

- Helps production-oriented users find the exact nuance they need
- Essential in bilingual dictionaries where the target language has distinct translations for senses that feel unified in the source language (e.g., English "fish" → Spanish *pez* [animal] / *pescado* [food])
- Makes example sentences more targeted — each example can illustrate one specific sense
- Facilitates computational processing and cross-referencing

### Bilingual dictionaries and cross-linguistic polysemy

The splitting-lumping trade-off is sharpened in bilingual dictionaries because the target language may cut the semantic space differently. As McCrae et al. (2022) note, sense divisions in a bilingual dictionary are partly driven by translation equivalence: if two senses of a source word require different target-language translations, they must be distinguished regardless of how closely related they feel in the source language.

This means that a Japanese-English dictionary may need to split senses that a monolingual Japanese dictionary would lump, and vice versa. The entry for {掛|か}ける illustrates this acutely: its dozens of Japanese senses map onto many different English verbs (hang, put on, sit down, spend, multiply, lock, pour over, etc.), forcing extensive splitting despite the cognitive unity of the word for Japanese speakers.

## Sense ordering

Once senses are established, they must be ordered. Three principal approaches exist in the literature (Lew 2013):

### Historical order

Senses are arranged by earliest attested usage. The Oxford English Dictionary and Merriam-Webster use this approach. It serves scholarly and etymological purposes but is poorly suited to learners, who must wade through archaic or rare senses to find common ones.

### Frequency order

Senses are arranged by corpus frequency, most common first. LDOCE and COBUILD pioneered this approach. It optimizes for the most likely lookup scenario: a learner encountering a word in context will usually need the most frequent sense. However, frequency depends on corpus composition, and the most frequent sense may not be the "core" meaning that illuminates the others.

### Logical (core-first) order

Senses are arranged to reveal semantic structure, typically with the core or prototypical meaning first and extensions (metaphorical, metonymic, specialized) radiating outward. OALD uses a version of this approach. It helps learners build a mental model of the word's semantic range and understand how different senses relate.

In practice, most modern learner dictionaries blend frequency and logical ordering — placing the most common core sense first, then arranging extended senses in a way that makes semantic relationships visible. Pure frequency ordering can produce puzzling results when a metaphorical sense happens to be more frequent than the literal one it derives from.

## Models of polysemy structure

Bond et al. (2024), studying polysemy representation in the New Oxford Dictionary of English and Merriam-Webster, formalized four computational models of how senses relate:

| Model | Structure | Key property |
|-------|-----------|-------------|
| **Prototype** | Central sense attracts peripheral meanings; center can shift | Captures radial category structure |
| **Progenitor** | First sense is a fixed hub; all others radiate outward | Star pattern, simple but rigid |
| **Nearest-neighbor chaining** | Each new sense links to the most semantically similar existing sense | Best matches actual dictionary structure |
| **Local chaining** | Each new sense links only to the immediately preceding one | Simple chains, poor semantic coherence |

Their key finding was that **nearest-neighbor chaining** most accurately describes how dictionaries actually structure polysemous entries, validating the cognitive linguistics view (Geeraerts 2006) that dictionaries implicitly build radial semantic networks rather than flat lists.

## Cognitive linguistics and prototype theory

Cognitive linguistics offers a theoretical framework that many modern learner dictionaries draw on, even when not explicitly stated. The key concepts:

- **Core (prototypical) meaning**: The most basic, concrete, or salient sense of a word, from which other senses derive. For {立|た}つ, the core meaning is physical standing; "to be established" and "to elapse (of time)" are extensions.
- **Radial categories**: Senses radiate outward from the core through regular cognitive mechanisms — metaphor, metonymy, generalization, specialization, image-schema transformations.
- **Family resemblance**: Peripheral senses may be more closely related to each other than to the core, creating chains where sense A relates to B, B to C, but A and C seem unrelated.

For learner dictionaries, prototype theory suggests a practical approach: lead with the core meaning, then arrange extended senses to make the derivation path visible. This helps learners internalize the word as a structured network rather than a list of unrelated translations.

## Japanese-specific challenges

### Extreme polysemy in basic vocabulary

Japanese has several words with exceptionally high polysemy. Verbs like {掛|か}ける (dozens of senses), {付|つ}く/{付|つ}ける, {取|と}る, {出|だ}す, and {上|あ}げる/{上|あ}がる present particular challenges. These are basic-tier words that learners encounter early but whose full semantic range takes years to master.

### Kanji as sense disambiguator

Japanese orthography sometimes disambiguates polysemy in ways that English cannot. Different kanji can signal different senses of the same reading:
- あつい → {暑|あつ}い (hot weather) / {熱|あつ}い (hot object) / {厚|あつ}い (thick)
- かえる → {変|か}える (change) / {替|か}える (replace) / {換|か}える (exchange) / {代|か}える (substitute)

This creates a dictionary design question: are these polysemes (related senses of one word) or homonyms (unrelated words with the same pronunciation)? The answer depends on whether one takes etymology or synchronic usage as primary. je-dict-1 treats distinct-kanji words as separate entries, which is the right approach for learners.

### Compound verbs and sense extension

Japanese compound verbs (V1+V2) create productive sense extensions. When {掛|か}ける serves as V2 in compounds like {話|はな}しかける (address someone), {呼|よ}びかける (call out to), {働|はたら}きかける (work on/lobby), the "direction toward" sense of かける generates a family of related but distinct meanings. These sit at the boundary between compositional compounds and polysemous extensions.

### Learner mental lexicon studies

Hoshino and Shimizu (2018), studying Japanese EFL learners' organization of polysemous English words, found that learners with larger vocabularies (5,500+ words) categorized senses more consistently with dictionary classifications, while lower-proficiency learners created idiosyncratic categories. This suggests that sense organization in dictionaries is not just descriptive but pedagogically formative — how a dictionary presents senses shapes how learners store them.

## Implications for je-dict-1

### Current approach

je-dict-1 uses a `definitions` array where each element has a `sense_number`, `gloss`, and optional `explanation`. As of April 2026:

| Definition count | Entries |
|-----------------|---------|
| 1 definition | 19,005 |
| 2 definitions | 4,504 |
| 3 definitions | 457 |
| 4+ definitions | 21 |

The distribution is heavily skewed toward single-definition entries (79%), which reflects both the genuine semantic simplicity of many two-kanji compounds and the project's tendency to create separate entries for words with distinct kanji rather than lumping them as polysemes.

### Sense ordering practice

je-dict-1 does not follow a rigid ordering rule. In practice, entries tend to use a blend of frequency and logical ordering:
- Particle entries (に, で, と) use a logical ordering that groups related functions
- Concrete-to-abstract progression is common for words with both literal and figurative uses
- The most common or basic sense generally comes first

### Example-sense linking

Currently, examples in multi-definition entries are not linked to specific senses via `sense_number` in the example object. The schema supports this field but it is not used. For entries with 2+ definitions (4,982 entries), examples appear as a flat list. Readers must infer which examples illustrate which senses.

This is a significant gap for highly polysemous entries. Adding sense-number links to examples would allow the UI to group examples under their relevant senses, dramatically improving navigation for entries like {筋|すじ} (4 senses: line/muscle/plot/logic) or particles.

### Recommendations

1. **Document a sense-ordering convention**: Adopt "core meaning first, then extensions by semantic proximity" as the default, with an explicit note that frequency should break ties. This aligns with both prototype theory and learner needs.

2. **Add example-sense linking**: Extend the example schema to require `sense_number` for entries with 2+ definitions. This is a deterministic, scriptable enhancement — existing examples can often be assigned to senses based on vocabulary overlap with sense glosses.

3. **Review high-polysemy entries**: The 478 entries with 3+ definitions deserve targeted review to ensure senses are well-ordered, sufficiently split (but not over-split), and accompanied by sense-specific examples.

4. **Consider sense relationship markers**: For highly polysemous entries, adding a brief marker indicating the derivation path (metaphorical, metonymic, specialized, figurative) would help learners understand why a word has the senses it does. This is lightweight — a single tag per sense — and pedagogically valuable.

5. **Leverage kanji disambiguation**: Continue the current practice of separate entries for distinct-kanji homophone senses. This is well-aligned with learner needs and avoids the confusion of overloaded entries.

## References

- Atkins, B. T. S. & Rundell, M. (2008). *The Oxford Guide to Practical Lexicography*. Oxford University Press.
- Bond, F., Maziarz, M., Piotrowski, T. & Rudnicka, E. (2024). Models of polysemy in two English dictionaries. *International Journal of Lexicography*, 37(2), 196–.
- Geeraerts, D. (2006). Prototype theory: Prospects and problems. In D. Geeraerts (Ed.), *Cognitive Linguistics: Basic Readings*. Mouton de Gruyter.
- Hoshino, Y. & Shimizu, H. (2018). The organization of the senses of polysemy in Japanese EFL learners' mental lexicon. *Creative Education*, 9(6).
- Kilgarriff, A. (1997). I don't believe in word senses. *Computers and the Humanities*, 31(2), 91–113.
- Lew, R. (2013). Identifying, ordering and defining senses. In H. Jackson (Ed.), *The Bloomsbury Companion to Lexicography* (pp. 284–302). Bloomsbury.
- Lu, Z. & Geng, Q. (2024). Bridging across polysemic senses in bilingual specialized dictionaries for ESP learners. *Lexikos*, 34(1).
- McCrae, J., Rademaker, A., Bond, F. et al. (2022). Toward an integrative approach for making sense distinctions. *Frontiers in Artificial Intelligence*, 5.
- Nesi, H. (1999). The specification of dictionary reference skills in higher education. In R. R. K. Hartmann (Ed.), *Dictionaries in Language Learning*. Freie Universität Berlin.

## Related pages

- [Definition and Gloss Strategies](definition-strategies.md) — equivalence types and gloss writing techniques
- [Translation Equivalence](translation-equivalence.md) — the bilingual mapping problem
- [Handling Homographs](../topics/homographs.md) — disambiguation for identical-writing words (related but distinct from polysemy)
- [Entry Design](../project/entry-design.md) — schema including sense/definition structure
- [Dictionary Lookup Behavior](dictionary-lookup-behavior.md) — how learners navigate multi-sense entries
- [Compound Verb Representation](../topics/compound-verbs.md) — entry-vs-pattern decisions for V1+V2 compounds
- [Word Variants](../topics/word-variants.md) — handling multiple written forms
- [Vocabulary Acquisition](vocabulary-acquisition.md) — how learners acquire multi-sense knowledge
- [Sense Relations and Semantic Networks](sense-relations-semantic-networks.md) — paradigmatic sense relations (synonymy, antonymy, hyponymy) and their dictionary treatment
- [Japanese Aspect and ている](japanese-aspect-teiru.md) — ている as a case study in constructional polysemy driven by lexical aspect
- [Dictionary Skills and Reference Skills Training](dictionary-skills-training.md) — sense selection as the most common dictionary-use failure point
- [Figurative Language and Idiom Processing in L2](figurative-language-idiom-processing.md) — literal-to-figurative sense extension and metaphorical polysemy
- [Dictionary Microstructure and Information Architecture](dictionary-microstructure.md) — sense ordering principles, navigation devices, and entry-internal organization
- [Japanese Particles in L2 Acquisition](japanese-particles-l2.md) — particles as a paradigm case of polysemy in function words; cognitive-linguistic prototype approaches
