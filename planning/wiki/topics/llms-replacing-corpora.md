# LLMs as Lexicographic Corpus Replacements

**Last updated**: 2026-04-08

## The question

Traditional dictionary-making relies on text corpora as empirical evidence for how words are used. Large language models are trained on enormous text collections and appear to internalize the distributional patterns that corpus analysis extracts. Can LLMs serve as a replacement for — or at least a radical supplement to — traditional corpora in dictionary production?

This is not merely a theoretical question. je-dict-1 is already being built primarily through LLM-generated content, with the LLM drawing on its training-derived knowledge of Japanese rather than consulting external corpora during entry creation. The results have been consistently good, raising the question of whether the corpus step can be largely bypassed.

## The case for LLMs as corpus replacements

### LLMs encode distributional knowledge

An LLM trained on hundreds of billions of tokens has, in effect, "read" far more text than any individual lexicographer could consult, and more than most purpose-built corpora contain. The BCCWJ (the gold-standard Japanese corpus) contains ~104 million words. Claude's training data is orders of magnitude larger. The statistical patterns that corpus linguists extract with concordancers and association measures — collocational preferences, frequency rankings, register distributions — are implicitly encoded in the model's parameters.

### The "trend toward the mean" is a feature, not a bug

One of the widely noted characteristics of LLM output is its tendency toward the average — toward the most typical, consensus-level language use. In creative writing or personal communication, this is a weakness (producing what critics call "AI slop" — bland, personality-free prose). But for lexicography, this is precisely what is wanted. Dictionaries represent conventional, mainstream usage. They document not how any individual uses language, but how the language community as a whole uses it. The LLM's gravitational pull toward the center of the distribution aligns perfectly with the lexicographer's goal of describing typical usage.

When Claude writes example sentences for a dictionary entry, they are:
- Grammatically standard (not dialectal or idiosyncratic)
- Stylistically neutral unless a specific register is called for
- Representative of common usage patterns
- Natural-sounding to native speakers

These are exactly the properties that corpus-derived examples are selected and edited to achieve — but the LLM produces them directly.

### LLMs provide what corpora cannot

As discussed in [Beyond Flat Corpora](../research/beyond-flat-corpora.md), LLMs go beyond distributional statistics to provide semantic, pragmatic, and discourse-level analysis. A corpus can show that 電話を切る is a frequent collocation; an LLM can explain *why* 切る is used (the metaphor of severing a connection), that it carries no negative connotation in this context, and how it differs from 電話を止める. This analytical capability is something corpora fundamentally lack.

### Practical advantages

- **No corpus construction cost**: Building a balanced, representative corpus is expensive and time-consuming. BCCWJ took years and significant institutional resources.
- **No licensing restrictions**: Many corpora have access limitations. LLM knowledge is immediately available.
- **No tools required**: No need for concordancers, statistical software, or annotation pipelines.
- **Instant multilingual access**: The same LLM can provide insights about Japanese, English, and the translation relationships between them.
- **Dynamic updates**: While corpora are static snapshots, LLMs trained on more recent data can reflect evolving usage (though with a training cutoff).

## The case for caution

### Rundell's critique (2024)

Michael Rundell, one of the most respected figures in learner lexicography (editor of Macmillan English Dictionary, co-author of *The Oxford Guide to Practical Lexicography*), addressed this question directly in "Automating the creation of dictionaries: are we nearly there?" (February 2024). His assessment of ChatGPT for dictionary production was skeptical:

- **Non-deterministic output**: Different queries produce different results, undermining reproducibility.
- **Hallucinated senses**: For polysemous words, LLMs sometimes invent meanings or miss common ones. Rundell demonstrated this with words like *party* and *overwhelm*.
- **Unverifiable claims**: LLM output cannot be traced back to source data. A corpus entry can be verified against the original text; an LLM assertion cannot.
- **Formulaic examples**: LLM-generated example sentences, while grammatically correct, can feel artificial compared to carefully selected corpus examples.

Rundell concluded that "corpus-linked post-editing methods remain superior because they maintain traceable connections to source data."

### Specific risks

1. **Frequency blindness**: LLMs don't have reliable access to their own frequency data. Asked "Is X more common than Y?", they may give plausible but incorrect answers. Corpus frequency counts are precise; LLM frequency intuitions are approximate.

2. **Training data bias**: LLMs overrepresent internet text, English-language content, and certain genres. Their "sense" of typical Japanese usage may be skewed by which Japanese text was included in training data. BCCWJ, by contrast, was deliberately balanced across genres.

3. **Temporal blindness**: LLMs have a training cutoff and cannot distinguish between current and obsolete usage. A corpus with publication dates allows diachronic analysis.

4. **Minority patterns vanish**: LLMs trend toward the mean, which means rare but legitimate usage patterns (dialectal forms, domain-specific terminology, archaic-but-still-used expressions) may be underrepresented or absent from LLM knowledge. Corpora preserve the long tail.

5. **Circularity risk**: As more AI-generated text enters the internet, future LLMs may be trained partly on AI output, potentially amplifying the trend toward the mean and losing contact with authentic human language use.

6. **Opacity**: When an LLM says "this collocation is common," there is no way to verify the claim against specific texts. Corpus evidence is transparent and auditable.

### The eLex 2025 consensus

The eLex 2025 conference (Electronic Lexicography in the 21st Century, Bled, November 2025) reflected a field-wide consensus that LLMs are best used as **tools within a structured lexicographic pipeline**, not as autonomous dictionary generators. Widmann (2025) presented "A Pipeline for Automated Dictionary Creation with Optional Human Intervention" — the emphasis on pipeline and intervention is telling. The emerging best practice treats LLMs as "trainees working under strict supervision," with each step validated against formal schemas and, where possible, traceable to corpus data.

## A synthesis: complementary strengths

Rather than asking "Can LLMs replace corpora?", a more productive framing is: **What does each tool do best, and how should they be combined?**

| Capability | Traditional corpus | LLM |
|-----------|-------------------|-----|
| Precise frequency data | Excellent | Approximate at best |
| Collocational statistics | Excellent (MI, t-score, etc.) | Good intuitions, not quantifiable |
| Balanced genre representation | Excellent (if well-designed) | Uneven, opaque |
| Diachronic analysis | Excellent (dated texts) | Poor (training cutoff) |
| Verifiability/auditability | Excellent | Poor |
| Semantic analysis | Poor without annotation | Excellent |
| Pragmatic analysis | Very poor | Good and improving |
| Register/connotation judgment | Limited | Excellent |
| Example sentence generation | Good (with selection/editing) | Excellent |
| Usage explanation and metalanguage | N/A | Excellent |
| Cost and accessibility | High | Low |
| Scalability | Limited by corpus size | Virtually unlimited |

## Implications for je-dict-1

### The current model works

je-dict-1's LLM-primary workflow has produced nearly 23,000 entries with consistent quality. The LLM's implicit distributional knowledge, combined with structured prompts, schema validation, and human oversight, has proven effective for:
- Selecting appropriate senses and ordering them by frequency
- Generating natural collocations and example sentences
- Writing nuanced usage notes that explain semantic and pragmatic distinctions
- Assessing register and formality
- Identifying related words and cross-references

This is strong empirical evidence that LLMs can carry the bulk of dictionary production work, at least for a language as well-represented in training data as Japanese.

### Where corpus data would add value

Despite the success of the LLM-primary approach, corpus data could strengthen the dictionary in specific ways:

1. **Frequency validation**: Cross-checking vocabulary tier assignments and sense ordering against BCCWJ frequency data would catch cases where the LLM's frequency intuitions are wrong.

2. **Coverage gap analysis**: Comparing the dictionary's headword list against corpus-derived frequency lists would identify missing high-frequency words more reliably than LLM-based candidate generation alone.

3. **Collocation verification**: For the high-priority collocation patterns initiative, corpus association measures could validate LLM-generated collocation lists and identify patterns the LLM might miss.

4. **Rare usage documentation**: For entries covering words with domain-specific or archaic uses, corpus examples provide evidence that the LLM might not surface.

### A hybrid approach

The most robust approach for je-dict-1 going forward would be:

- **LLM as primary creator**: Continue using LLMs for entry drafting, sense analysis, example generation, and usage notes — the tasks where LLMs excel.
- **Corpus as validator**: Use BCCWJ and other corpora for frequency checks, coverage analysis, and collocation verification — the tasks where corpora provide irreplaceable empirical grounding.
- **Schema as guardrail**: The existing JSON schema, validation pipeline, and quality standards provide the structured framework that prevents LLM errors from propagating.
- **Human as curator**: Editorial oversight on priorities, quality standards, and edge cases.

This is essentially what je-dict-1 already does, though the corpus validation step is currently informal (the LLM draws on training data that includes corpus-derived knowledge) rather than systematic.

### The broader significance

je-dict-1 may be an early example of a broader shift in lexicographic methodology. The traditional workflow (corpus → analysis → draft → edit → publish) is being replaced or supplemented by a workflow where LLMs handle multiple steps simultaneously. The question is not whether this shift is happening — it clearly is — but how to preserve the empirical rigor that corpus-based methods brought to lexicography while gaining the semantic-pragmatic depth that LLMs offer.

The dictionary's existence as a large-scale, LLM-built reference work with automated quality controls and human curation is itself a data point in this evolving discussion.

## References

- Rundell, M. (2024). "Automating the creation of dictionaries: are we nearly there?" *Humanising Language Teaching*, February 2024.
- Widmann, L. (2025). "A Pipeline for Automated Dictionary Creation with Optional Human Intervention." *eLex 2025 Proceedings*.
- Rundell, M., Jakubíček, M., Kovar, V. & Matuska, O. (2025). "Lexicom at 25: reflections on the changing world of lexicography and language technology." *eLex 2025*.
- Vranjek Ošlak, U. (2025). "How Effective is AI as a Language Consultant?" *eLex 2025*.
- Frankenberg-Garcia, A. (2025). "Contrasting a new AI-powered dictionary designed for on-[the-fly use]." *eLex 2025*.

## Related pages

- [Beyond Flat Corpora](../research/beyond-flat-corpora.md) — the semantic-pragmatic analysis that LLMs enable
- [Corpus Linguistics](../research/corpus-linguistics.md) — the traditional corpus methods
- [Collocations in Learner Dictionaries](../research/collocations.md) — a domain where both corpus and LLM approaches apply
- [AI-Assisted Entry Review](../ideas/ai-review.md) — other uses of LLMs in dictionary quality improvement
- [Corpus-Driven Entry Prioritization](../ideas/corpus-prioritization.md) — where corpus data remains most valuable
- [Content Pipeline](../project/content-pipeline.md) — the current LLM-primary workflow
- [Deterministic vs. Semantic Tasks](deterministic-vs-semantic-tasks.md) — which dictionary tasks can be automated and which require semantic judgment
