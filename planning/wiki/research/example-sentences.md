# Example Sentence Design

**Last updated**: 2026-06-08

## Overview

Example sentences are among the most consulted features in learner dictionaries. Empirical studies consistently show that learners look at examples more often than definitions (Lew 2004; Thumb 2004), and that examples significantly improve both comprehension and production when combined with definitions (Laufer 1993). Yet constructing effective examples is not straightforward: a "good" dictionary example must simultaneously serve multiple functions — illustrating meaning, showing syntactic behavior, revealing collocational patterns, and modeling register — without overwhelming the learner with unfamiliar vocabulary. This page surveys the research on what makes dictionary examples effective and how those findings inform je-dict-1's approach.

## Criteria for good dictionary examples

### The Atkins–Rundell framework

Atkins & Rundell (2008, *The Oxford Guide to Practical Lexicography*) identify four criteria that a dictionary example must satisfy:

**Typicality.** The example should illustrate a common, prototypical use of the word, not an edge case or literary flourish. A dictionary example for 食べる should show someone eating food in a recognizable context, not a metaphorical extension. Typicality is the criterion most directly served by corpus evidence: frequency data reveals what the "normal" use of a word looks like.

**Informativeness.** Each example should add information beyond what the definition already states — a collocation, a syntactic frame, a register context, a pragmatic implication. An example that merely restates the definition in sentence form wastes the learner's time. The highest-value examples show the learner something they could not have inferred from the definition alone.

**Intelligibility.** The vocabulary and grammar in the example should be accessible to the target user. Laufer (1993) found that unknown words in examples actually hinder learning — learners fixate on the unfamiliar vocabulary rather than learning from the context. This is the criterion most directly in tension with authenticity: real corpus sentences are often full of low-frequency words and complex syntax.

**Naturalness.** The sentence should sound like something a native speaker would actually produce in a plausible context. Textbook-style sentences ("This is a pen") are grammatically correct but pragmatically odd. Naturalness also means avoiding sentence fragments that only make sense in the context of a surrounding paragraph.

### The GDEX criteria

Kilgarriff et al. (2008) formalized these intuitions into the GDEX (Good Dictionary EXample) system, a software module integrated into the Sketch Engine corpus tool that automatically ranks candidate sentences. GDEX scores sentences on a 0–1 scale based on:

1. **Sentence length**: 10–25 words (the most heavily weighted criterion). Too short loses context; too long overwhelms.
2. **Word frequency**: constituent words should fall within the top ~17,000 most frequent, ensuring intelligibility.
3. **Main-clause position**: the target word or collocation should appear in the main clause, not buried in a subordinate clause or parenthetical.
4. **Pronoun and anaphor avoidance**: sentences that rely on *he*, *it*, or *this* for reference are less self-contained; GDEX penalizes them.
5. **Topic safety**: avoidance of controversial content (politics, religion, violence) that could distract from the lexicographic purpose.

GDEX has been adapted for multiple languages and dictionaries. Its significance for lexicographic theory is the demonstration that "good example" is a measurable, decomposable property — not just an editorial intuition. Kosem et al. (2019) extended the GDEX framework with language-specific configurations and showed that automated scoring aligns reasonably well with lexicographer judgments across several European languages, though human editorial selection still outperforms fully automated extraction.

## Authentic, constructed, and LLM-generated examples

### The COBUILD revolution: authentic corpus examples

The Collins COBUILD dictionary (1987), directed by John Sinclair, broke with centuries of lexicographic practice by using only authentic corpus examples — real sentences drawn from the Bank of English corpus. The argument was powerful: real examples reveal actual collocational patterns that invented examples might miss. The verb *commit* almost always appears with negative objects (*crime*, *error*, *sin*, *murder*) — a pattern revealed by corpus analysis but easy to overlook when constructing examples from introspection.

Sinclair's innovation fundamentally changed the field. All subsequent major English learner dictionaries (LDOCE, OALD, CALD, MED) adopted some form of corpus-informed example policy, and the idea that examples should reflect attested usage rather than editorial imagination became the professional standard.

### The hybrid approach: corpus-informed construction

In practice, raw corpus sentences rarely satisfy all four Atkins–Rundell criteria simultaneously. Authentic sentences tend to be:
- **Too long** for dictionary use (newspaper sentences average 20–30 words)
- **Too context-dependent** (referring to entities introduced in prior sentences)
- **Full of low-frequency vocabulary** (violating intelligibility)
- **Topically distracting** (a real sentence about 走る might involve a specific marathon in a specific year)

The resolution adopted by most modern learner dictionaries is a **hybrid approach**: lexicographers study corpus evidence (concordances, collocations, frequency data) and then construct clean examples that reflect attested patterns while satisfying intelligibility and self-containment requirements. The Macmillan English Dictionary (MED) and current editions of LDOCE and OALD all follow this model. The examples read like natural sentences but are editorially crafted to serve pedagogical purposes.

### LLM-generated examples: a new paradigm

Recent research has begun evaluating large language models as example sentence generators for dictionaries. This work is directly relevant to je-dict-1, which uses LLM-constructed examples as its primary method.

Patel et al. (2024, NAACL) developed the **OxfordEval** metric to compare LLM-generated examples against Oxford Dictionary examples, finding that GPT-4-generated examples achieved over 80% win rate against human-written examples on quality criteria — a striking result suggesting that LLMs can produce examples rated as natural, informative, and intelligible. However, the evaluation was English-only.

Haider et al. (2024) tested LLM-generated bilingual example sentences across language pairs of varying resource levels. French (high-resource) examples achieved 4.68/5 quality ratings, but quality degraded for lower-resource languages. Of the GDEX criteria, **informativeness** proved the hardest for LLMs to satisfy: 95% of French examples were rated "typical" but only 56% of Tetun examples met the informativeness standard. The study also found low inter-annotator agreement on what constitutes a "good" example, confirming that example quality assessment involves substantial subjectivity.

Takahashi et al. (2025) addressed example diversity for L2 Japanese learners specifically, developing a system that retrieves candidate sentences from corpora (Tatoeba, Japanese Wikipedia) and uses BERT-based models to rank them for diversity, difficulty (mapped to JLPT levels), and contextual appropriateness. Their key finding was that **diversity across examples** — showing the target word in varied syntactic and semantic contexts — is as important as the quality of any individual example.

### je-dict-1's approach

je-dict-1 uses LLM-constructed examples informed by general language knowledge rather than direct corpus extraction. This approach produces clean, vocabulary-controlled sentences but carries two known risks: (1) missing corpus-revealed collocational patterns (the *commit*-with-negative-objects problem), and (2) generating plausible-sounding but non-typical usage. The multi-model review pipeline (`review_runner.py`) provides a partial check on the second risk by flagging examples that multiple models judge as unnatural.

## Encoding vs. decoding examples

Frankenberg-Garcia (2012, 2015) introduced a crucial distinction that the field had largely overlooked: the difference between **decoding examples** (which help a learner understand a word's meaning) and **encoding examples** (which help a learner produce the word correctly).

**Decoding examples** are sorted by sense — each example illustrates a different meaning of the word. This is the traditional approach: one example per sense, showing what the word means in context.

**Encoding examples** serve a different purpose: they show the word's lexico-grammatical behavior — its syntactic frames, collocational partners, and register constraints. For encoding, examples should be sorted by **pattern of use**, not by meaning. A learner trying to use 決める in a sentence needs to see that it takes を for direct objects, that it collocates with 日程, 方針, and ルール, and that 決まる is its intransitive pair — information that a single decoding example won't provide.

Frankenberg-Garcia's (2015) experimental findings were strong: when learners were given **multiple examples sorted by lexico-grammatical pattern**, their production accuracy improved significantly compared to a single example or to multiple examples sorted by meaning. The implication is that dictionaries should provide examples that collectively demonstrate the word's behavioral repertoire, not just its semantic range.

This encoding–decoding distinction maps directly onto je-dict-1's design: the **first example per sense** serves a decoding function (illustrate this meaning clearly), while **subsequent examples** serve encoding functions (show collocations, particle patterns, register variation, longer natural contexts).

## Sentence length and progressive complexity

### Optimal length

The GDEX research established 10–25 words as the effective range for English dictionary examples. For Japanese, character counts are a better metric than word counts (since Japanese lacks word-boundary spaces), but the principle holds: very short examples (under 10 characters) lack context, while very long examples (over 40 characters) impose a parsing burden that interferes with learning.

### Progressive sequencing

je-dict-1 implements a **progressive length model** within each sense:

1. **Short** (~5–15 characters): demonstrates the word clearly with minimal surrounding context. Serves the quick-lookup user and the decoding function.
2. **Medium** (~10–25 characters): shows the word in a basic syntactic frame with one or two collocates. Begins to serve the encoding function.
3. **Longer** (~15–35 characters): a more natural, contextualized usage. Serves advanced encoding — register, pragmatics, discourse context.

This progressive model has theoretical support from the **Involvement Load Hypothesis** (Laufer & Hulstijn 2001): each successive example demands slightly more processing effort (longer context, more inference required), which promotes deeper encoding of the target word. It also matches the **Levels of Processing** framework (Craik & Lockhart 1972): the first example requires shallow processing (match word to meaning), while later examples require deeper semantic and syntactic processing. See [Input Processing, Noticing, and Depth of Processing](input-processing-noticing-vocabulary.md) for the theoretical foundations.

## Vocabulary control in examples

### Tier-aligned vocabulary restriction

For learner dictionaries with vocabulary tier systems, example sentences can be controlled to avoid creating a comprehension barrier:

- **Basic-tier examples** should use only basic-tier vocabulary (and high-frequency general words)
- **Core-tier examples** should draw from basic + core vocabulary
- **General-tier examples** have no restrictions, but should prefer known words where possible

je-dict-1 implements this principle by convention rather than automated enforcement. The `example-sentences` skill specifies the restriction, and LLM entry-creation sessions follow it. Automated checking (flagging examples that use vocabulary from higher tiers than the entry) is a potential enhancement that would catch violations systematically.

### The intelligibility–naturalness trade-off

Strict vocabulary control can conflict with naturalness. An example for a general-tier cooking verb that avoids all general-tier ingredient names will sound stilted. The practical resolution: control vocabulary in the sentence structure and grammar, but allow domain-appropriate nouns — a reader looking up a cooking verb expects to encounter cooking vocabulary. The furigana system provides an escape hatch: even if a kanji compound in an example is above the learner's level, the reading annotation keeps it accessible.

## Number of examples per sense

je-dict-1 requires a minimum of **3 examples per sense**. This aligns with both theoretical and empirical findings:

- **Frankenberg-Garcia (2015)** found that multiple examples significantly improved production accuracy compared to a single example, with the benefit coming specifically from showing different lexico-grammatical patterns.
- **Nation (2001)** recommends 3–5 encounters with a word for initial learning, with more needed for productive knowledge. Dictionary examples provide concentrated encounters in a controlled context.
- **The Involvement Load Hypothesis** predicts that each additional example adds processing opportunity, but with diminishing returns — the third and fourth examples add less than the first and second.
- **Practical constraints**: Too many examples (7+) overwhelm the entry and slow down lookup. The 3–4 range provides sufficient coverage of typical patterns without cluttering the page.

je-dict-1's current average is 3.9 examples per entry across 113,326 total examples, with multi-sense entries receiving 3+ per sense (yielding 6–9 total for two- or three-sense entries).

## Collocational coverage

Examples should collectively demonstrate the word's major collocates and syntactic frames. For a verb, this means showing:
- Different particle patterns (に向かう, を向く, に向ける)
- Typical subjects and objects (the "who does what to whom" of the word)
- At least one common collocation per sense
- Both literal and figurative uses if both are common

For adjectives, examples should show both predicative (この本は面白い) and attributive (面白い本) uses, and for na-adjectives, the adverbial form (静かに) if common.

Corpus collocation data (from tools like Sketch Engine's Word Sketch or NINJAL's BCCWJ online search) can identify the highest-frequency collocates that examples should cover. je-dict-1's LLM-generated examples draw on the model's implicit frequency knowledge, but a systematic comparison against BCCWJ collocation data has not been performed.

## Japanese-specific considerations

### Script complexity and example design

Japanese examples carry an information layer absent in alphabetic languages: the script choice itself conveys register and formality. An example written in hiragana-heavy style reads differently from one with dense kanji. je-dict-1's furigana system (`{漢字|かんじ}`) resolves the reading barrier but not the register signal — an example using the kanji form 美味しい versus the hiragana おいしい implicitly models different writing registers.

### Sentence-final expressions

Japanese sentence-final particles and expressions (よ, ね, わ, のだ, んです) carry pragmatic force that English punctuation cannot convey. Dictionary examples that end with plain dictionary form (食べる) sound unnaturally truncated; examples ending with です/ます sound formal; examples with sentence-final particles sound conversational. The choice of sentence ending is itself a register-encoding decision that every example must make.

### Particle patterns as example targets

For verbs and adjectives, the particle frame is often as important as the word itself. A learner who knows the meaning of 決める but doesn't know its particle pattern (〜を決める, 〜に決める, 〜と決める — each with different meanings) will produce errors. Examples that systematically vary the particle frame across the 3+ required examples per sense serve a critical encoding function specific to Japanese.

### Topic–comment structure

Japanese topic–comment structure (〜は...が...) often requires longer examples to demonstrate naturally than English SVO patterns. The topic-marking は and the subject-marking が frequently co-occur in the same sentence, producing structures that resist compression into 5-character examples. je-dict-1's progressive length model accommodates this: the shortest example may use a simple が-subject sentence, while the medium example shows a は-topic structure.

## References

- Atkins, B. T. S. & Rundell, M. (2008). *The Oxford Guide to Practical Lexicography*. Oxford University Press.
- Craik, F. I. M. & Lockhart, R. S. (1972). Levels of processing: A framework for memory research. *Journal of Verbal Learning and Verbal Behavior*, 11(6), 671–684.
- Frankenberg-Garcia, A. (2012). Learners' use of corpus examples. *International Journal of Lexicography*, 25(3), 273–296.
- Frankenberg-Garcia, A. (2015). Dictionaries and encoding examples to support language production. *International Journal of Lexicography*, 28(4), 490–512.
- Haider, T. et al. (2024). Generating bilingual example sentences with large language models as lexicography assistants. arXiv:2410.03182.
- Kilgarriff, A., Husák, M., McAdam, K., Rundell, M. & Rychlý, P. (2008). GDEX: Automatically finding good dictionary examples in a corpus. In E. Bernal & J. DeCesaris (Eds.), *Proceedings of the 13th EURALEX International Congress* (pp. 425–432).
- Kosem, I., Krek, S., Gantar, P., Arhar Holdt, Š., Čibej, J. & Laskowski, C. (2019). Identification and automatic extraction of good dictionary examples: The case(s) of GDEX. *International Journal of Lexicography*, 32(2), 119–137.
- Laufer, B. (1993). The effect of dictionary definitions and examples on the use and comprehension of new L2 words. *Cahiers de Lexicologie*, 63, 131–142.
- Laufer, B. & Hulstijn, J. H. (2001). Incidental vocabulary acquisition in a second language: The construct of task-induced involvement. *Applied Linguistics*, 22(1), 1–26.
- Lew, R. (2004). *Which Dictionary for Whom? Receptive Use of Bilingual, Monolingual and Semi-Bilingual Dictionaries by Polish Learners of English*. Motivex.
- Nation, I. S. P. (2001). *Learning Vocabulary in Another Language*. Cambridge University Press.
- Patel, A. et al. (2024). Low-cost generation and evaluation of dictionary example sentences. In *Proceedings of NAACL 2024* (pp. 3489–3505).
- Sinclair, J. (Ed.) (1987). *Collins COBUILD English Language Dictionary*. Collins.
- Takahashi, R. et al. (2025). Automatically suggesting diverse example sentences for L2 Japanese learners using pre-trained language models. arXiv:2506.03580.
- Thumb, J. (2004). *Dictionary Look-up Strategies and the Bilingualised Learner's Dictionary*. Max Niemeyer Verlag.

## Implications for je-dict-1

1. **The encoding–decoding distinction should inform example review.** During polishing, reviewers should check that examples collectively demonstrate the word's behavioral repertoire (particle frames, collocations, register contexts), not just its meanings. The first example per sense is a decoding example; subsequent examples should be encoding examples sorted by lexico-grammatical pattern.

2. **BCCWJ collocation data could improve coverage.** A systematic comparison of je-dict-1's examples against BCCWJ collocation lists for high-frequency words would reveal missed collocational patterns — the equivalent of the COBUILD *commit*-with-negative-objects discovery.

3. **Vocabulary control could be automated.** A script that checks whether examples in basic/core-tier entries use only tier-appropriate vocabulary would catch violations that manual review misses.

4. **Progressive complexity is already well-implemented** but could be more explicitly enforced — a validator that flags entries where example 3 is shorter than example 1 would catch ordering inconsistencies.

5. **LLM-generated examples carry specific risks** — plausible but atypical usage, missed high-frequency collocations, and potential repetitiveness across entries. The multi-model review pipeline is the right mitigation; expanding it to specifically check collocational typicality would address the most concerning gap.

6. **Japanese particle-pattern coverage deserves dedicated attention.** For verb entries, the polishing checklist should verify that the example set collectively demonstrates the verb's major particle frames, not just its senses.

## Related pages

- [Quality Standards](../project/quality-standards.md)
- [Learner Lexicography](learner-lexicography.md)
- [Corpus Linguistics](corpus-linguistics.md)
- [Vocabulary Acquisition](vocabulary-acquisition.md)
- [Grammar Information in Learner Dictionaries](grammar-in-dictionaries.md) — encoding examples and grammar-through-examples
- [Error Analysis and Learner Corpora](error-analysis-japanese-l2.md) — designing examples that preempt common errors
- [Pragmatics and Speech Acts](pragmatics-speech-acts.md) — designing examples that make pragmatic context salient
- [Japanese Aspect and ている](japanese-aspect-teiru.md) — ている examples as aspect-encoding vehicles for verbs with non-obvious readings
- [Register and Formality Marking](register-formality-marking.md) — register-appropriate examples as an alternative to metalinguistic labels
- [Keigo: Honorific Language](keigo-honorifics.md) — keigo forms in example sentences as a vehicle for modeling social context
- [Vocabulary Learning Strategies](vocabulary-learning-strategies.md) — how example design supports deep processing and the involvement load hypothesis
- [Input Processing, Noticing, and Depth of Processing](input-processing-noticing-vocabulary.md) — progressive examples as staged involvement load
- [Spaced Repetition and Dictionary Design](spaced-repetition-dictionary-design.md) — how examples serve as SRS card content via sentence mining
- [Near-Synonym Discrimination](near-synonym-discrimination.md) — contrastive encoding examples as the most effective format for teaching synonym distinctions
- [Depth of Vocabulary Knowledge](depth-of-vocabulary-knowledge.md) — progressive examples serve learners at different stages of incremental acquisition
- [The Lexical Approach and Vocabulary-Centered Teaching](lexical-approach-vocabulary-teaching.md) — examples as chunk exposure opportunities in a vocabulary-centred methodology
- [Incidental Vocabulary Acquisition Through Reading](incidental-vocabulary-reading.md) — how example sentences create incidental learning opportunities and re-encounter contexts
- [Productive Vocabulary and Encoding Support](productive-vocabulary-encoding.md) — encoding examples vs. decoding examples (Frankenberg-Garcia 2015)
- [L2 Writing and Dictionary Consultation](l2-writing-dictionary-consultation.md) — multiple examples as significantly more helpful for production than single examples (Frankenberg-Garcia 2015)
- [Collocations in Learner Dictionaries](collocations.md) — collocational typicality as a core criterion for example quality
- [Dictionary Microstructure and Information Architecture](dictionary-microstructure.md) — example placement and sequencing within entry structure
- [Dictionary Use in the Age of Machine Translation](dictionary-and-machine-translation.md) — examples as depth-of-processing assets that MT cannot replicate
