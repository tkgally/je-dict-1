# Example Sentence Design

**Last updated**: 2026-04-05

## What makes good dictionary examples?

Research on example sentences in learner dictionaries identifies several criteria that determine effectiveness.

## Key criteria (Atkins & Rundell, 2008)

### Typicality
Examples should illustrate common, prototypical uses, not edge cases. A dictionary example for 食べる should show someone eating food, not a metaphorical "eating one's words."

### Informativeness
Each example should add information beyond the definition — showing collocations, syntactic patterns, register, or pragmatic context. An example that merely restates the definition wastes space.

### Intelligibility
Vocabulary and grammar in the example should be accessible to the target user. Laufer (1993) found that unknown words in examples actually hinder learning — learners fixate on the unknown vocabulary rather than learning from context.

### Naturalness
The sentence should sound like something a native speaker would actually say. Textbook-style sentences ("This is a pen") are technically correct but pragmatically odd.

## Authentic vs. constructed examples

### The COBUILD approach
The Collins COBUILD dictionary (1987, led by John Sinclair) pioneered using authentic corpus examples. The argument: real examples show actual collocational patterns that invented examples might miss. "Commit" almost always appears with negative objects (crime, error, sin) — a pattern revealed by corpus analysis but easy to miss when constructing examples.

### The hybrid approach
Most modern learner's dictionaries use corpus-informed but editorially constructed/adapted examples. Raw corpus sentences are often:
- Too long for dictionary use
- Too context-dependent (referring to earlier sentences)
- Full of distracting vocabulary or cultural references

The best practice: study corpus patterns, then construct clean examples that reflect those patterns.

### je-dict-1's approach
Examples are LLM-constructed based on general language knowledge rather than direct corpus extraction. This produces clean, controlled sentences but may miss corpus-revealed patterns. A potential improvement would be to inform example construction with collocational data from BCCWJ.

## Sentence length and complexity

Shorter examples (8-15 words / ~5-30 Japanese characters) are generally more effective for comprehension. Progressive length within each sense — short → medium → longer — serves both quick-lookup users and those wanting deeper context.

je-dict-1 targets:
1. Short (5-15 chars): demonstrates the word clearly
2. Medium (10-20 chars): shows basic context
3. Longer (15-30 chars): natural usage with fuller context

## Vocabulary control

For learner dictionaries with tier systems, example sentences can be controlled:
- Basic-tier examples should use only basic-tier vocabulary
- Core-tier examples should use basic + core vocabulary
- General-tier examples have no restrictions (but should prefer known words)

je-dict-1 implements this principle, though enforcement is by convention rather than automated checking.

## Collocational coverage

Examples should collectively demonstrate the word's major collocates and syntactic frames. For a verb, this means showing:
- Different particle patterns
- Typical subjects/objects
- At least one common collocation per sense

## Quantity

je-dict-1 requires a minimum of 3 examples per sense. This aligns with research suggesting 3-5 examples provides sufficient coverage of typical usage patterns without overwhelming the user.

## Related pages

- [Quality Standards](../project/quality-standards.md)
- [Learner Lexicography](learner-lexicography.md)
- [Corpus Linguistics](corpus-linguistics.md)
- [Vocabulary Acquisition](vocabulary-acquisition.md)
