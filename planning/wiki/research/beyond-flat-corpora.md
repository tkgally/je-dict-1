# Beyond Flat Corpora: LLMs and Semantic-Pragmatic Analysis

**Last updated**: 2026-04-05

## The limitation of traditional corpora

The rise of collocations as a central concern in lexicography and language pedagogy (see [Collocations in Learner Dictionaries](collocations.md)) was made possible by the availability of large-scale text corpora from the 1980s onward. Tools like Sketch Engine, KWIC concordancers, and statistical association measures (MI, t-score, log-likelihood) enabled lexicographers to move from intuition to evidence.

But these corpora are fundamentally **flat**. They represent language as sequences of tokens — words in linear order. Even when annotated with part-of-speech tags, lemmatization, or syntactic parsing, the analysis operates at the level of form and structure. What corpora capture well:

- **Distributional patterns**: which words co-occur and how often
- **Collocational statistics**: which combinations are statistically significant
- **Frequency data**: how common a word or pattern is across genres
- **Grammatical behavior**: what syntactic frames a word appears in

What corpora capture poorly or not at all:

- **Semantic roles**: whether a noun is an agent, patient, instrument, or beneficiary in a given sentence
- **Pragmatic function**: whether an utterance is a request, a complaint, an apology, or a hedge
- **Discourse context**: how a word's use shifts depending on the topic, register, or communicative purpose of the surrounding text
- **Connotation and affect**: whether a word carries positive, negative, or neutral emotional valence in a specific context
- **Implicature**: what a speaker means beyond what is literally said
- **World knowledge integration**: understanding that "the bank was steep" refers to a riverbank, not a financial institution, based on discourse context

Traditional corpus annotation can address some of these (e.g., semantic role labeling, sentiment annotation), but manual annotation is extremely expensive and doesn't scale, and automated annotation has historically been too unreliable for nuanced semantic or pragmatic phenomena.

## What LLMs change

Large language models represent a qualitative shift. Because they are trained on vast amounts of text (hundreds of billions to trillions of tokens), they develop internal representations that go beyond linear co-occurrence patterns. When prompted appropriately, LLMs can:

1. **Disambiguate word senses in context** — not by looking up a sense inventory, but by understanding the discourse. A corpus can tell you that "bank" co-occurs with "river" and "money"; an LLM can tell you which sense is active in a specific passage and explain why.

2. **Identify pragmatic functions** — recognize that "Could you pass the salt?" is a request, not a question about ability, and that "Nice weather we're having" said during a rainstorm is sarcastic. Recent surveys (Ma et al., 2025, "Pragmatics in the Era of Large Language Models") document growing LLM capability across pragmatic phenomena including implicature, presupposition, speech acts, and figurative language.

3. **Assess register and formality at discourse level** — not just flagging individual words as "formal" or "casual" but evaluating the overall communicative context and how a word's register interacts with it.

4. **Explain semantic relationships** — articulate why two near-synonyms differ, what connotations a word carries, how its usage shifts between spoken and written registers, or why a particular collocation "sounds natural" while a semantically equivalent alternative doesn't.

5. **Integrate world knowledge** — bring extralinguistic context to bear on linguistic analysis. Understanding that 年賀状 involves specific cultural practices around New Year, or that お疲れ様 functions differently depending on the relative status of speaker and listener.

## From co-occurrence to understanding

The key insight is that traditional corpus analysis answers **"what patterns exist?"** while LLM-assisted analysis can additionally address **"what do these patterns mean and why do they exist?"**

Consider the Japanese verb 切る (to cut). A corpus analysis reveals:
- High-frequency collocations: 髪を切る, 電話を切る, 縁を切る, カードを切る
- Statistical co-occurrence data across genres
- Syntactic patterns (transitive, を-marked object)

An LLM can additionally explain:
- The semantic extension from physical cutting (髪) to termination (電話, 縁) to shuffling (カード)
- That 電話を切る carries no negative connotation despite the "cutting" metaphor, while 縁を切る is strongly negative
- That each collocation inhabits a different register (髪を切る is neutral; 縁を切る is emotionally charged)
- That a learner who says 電話を止める instead of 電話を切る would be understood but sounds unnatural, and *why* — because 切る encodes the abruptness of disconnection

This is precisely the kind of semantic-pragmatic analysis that dictionaries need but that flat corpora cannot provide.

## Current state of research

The application of LLMs to semantic and pragmatic analysis beyond flat corpus methods is an emerging field. Key developments:

- **LLM-assisted annotation**: Yu et al. (2025) explored LLM-assisted annotation for corpus-based pragmatics and discourse analysis, finding that GPT-4 approaches human-coder accuracy for some pragma-discursive phenomena (e.g., apology strategies), though complex pragmatic features still require human oversight.

- **Pragmatic competence surveys**: Ma et al. (2025) provide a comprehensive survey of LLM pragmatic capabilities across implicature, presupposition, speech acts, reference resolution, and figurative language. Performance is uneven but improving rapidly.

- **LLMs as linguistic consultants**: Vranjek Ošlak (2025, eLex 2025) investigated "How Effective is AI as a Language Consultant?" — directly relevant to using LLMs for the kind of semantic-pragmatic judgments that dictionaries require.

- **Sociolinguistic foundations**: Nguyen et al. (2024) explored "The Sociolinguistic Foundations of Language Modeling," arguing that research on language use in pragmatics, discourse analysis, and cognitive linguistics will become central to advancing language modeling.

This is still early-stage work. Most existing corpus linguistics infrastructure was built for flat analysis. The tools and methodologies for systematic LLM-assisted semantic-pragmatic analysis are still being developed.

## Implications for je-dict-1

### What this dictionary already does

je-dict-1 is arguably already operating in this beyond-flat-corpus paradigm. When Claude creates dictionary entries, it draws on:
- **Semantic knowledge**: explaining why near-synonyms differ in connotation, not just listing them
- **Pragmatic awareness**: noting when expressions are used for hedging, politeness, or emotional effect
- **Register sensitivity**: assessing formality based on communicative context, not just word-level labels
- **Cultural integration**: explaining social practices that shape word usage

This goes well beyond what a concordancer could provide. The notes fields in entries routinely contain the kind of semantic-pragmatic analysis that would require extensive manual annotation in a corpus-based workflow.

### Future opportunities

1. **Systematic semantic role documentation**: For verbs, document not just what particles they take but what semantic roles their arguments fill. 教える takes に for the recipient (indirect object/beneficiary) and を for the content (theme) — this is semantic role information, not just syntactic pattern.

2. **Pragmatic usage notes**: Document the speech acts and discourse functions that expressions serve. いいですよ can be permission, agreement, refusal (with falling intonation), or reassurance — pragmatic information that flat corpora cannot distinguish.

3. **Connotation and affect mapping**: Systematically note the emotional valence and connotative associations of words in different contexts. A corpus shows that 太い co-occurs with both positive (太い腕 "strong arms") and negative (太い声 "gruff voice") contexts; an LLM can articulate the evaluative dimension.

4. **Discourse-level collocation analysis**: Go beyond word-level collocations to document discourse-level patterns — how words function differently in narrative vs. argumentative vs. conversational contexts.

### Methodological caution

LLM-generated semantic-pragmatic analysis should be treated as **expert hypothesis** rather than **empirical evidence**. Unlike corpus data (which is grounded in attested usage), LLM judgments reflect training data patterns filtered through model architecture. They can be wrong, biased, or overly confident. The ideal approach combines:
- LLM analysis for generating hypotheses and articulating distinctions
- Corpus evidence for grounding claims in attested usage
- Human review for catching errors and ensuring accuracy

## Related pages

- [Collocations in Learner Dictionaries](collocations.md) — the collocation research tradition that LLMs can extend
- [Corpus Linguistics](corpus-linguistics.md) — the flat-corpus methods that LLMs complement
- [LLMs as Lexicographic Corpus Replacements](../topics/llms-replacing-corpora.md) — the related question of whether LLMs can replace corpora entirely
- [Translation Equivalence](translation-equivalence.md) — semantic-pragmatic analysis is essential for explaining non-equivalence
- [Register and Formality](../topics/register.md) — a domain where LLM analysis already goes beyond corpus methods
