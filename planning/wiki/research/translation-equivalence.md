# Translation Equivalence

**Last updated**: 2026-04-05

## The core problem

Bilingual dictionaries face an inherent tension: they must provide translation equivalents, but true semantic equivalence across languages is rare. Zgusta (1971) established that most word pairs are only partial equivalents — they overlap in some senses, collocations, or registers but diverge in others.

This problem is especially acute for Japanese-English dictionaries because the languages are structurally and culturally distant.

## Types of non-equivalence

### Lexical gaps
One language lexicalizes a concept the other doesn't:
- 木漏れ日 (こもれび) — "sunlight filtering through leaves" has no single English word
- 積ん読 (つんどく) — buying books and leaving them unread
- "Privacy" has no direct Japanese equivalent; プライバシー is a loanword with different connotations

### Semantic asymmetry
Japanese words may encode distinctions English doesn't (and vice versa):
- **Giving verbs**: あげる/くれる/もらう all involve giving/receiving but encode direction relative to the speaker's in-group. English "give" and "receive" don't make this distinction.
- **Existence**: ある/いる split along an animate/inanimate axis that English "be/exist/have" doesn't encode grammatically.
- **Wearing**: 着る/履く/被る/かける divide by body region; English uses "wear" for all.

### Grammatical category mismatches
- は and が are particles with no English equivalent — they must be described functionally
- ～てしまう expresses completion + regret in a single construction
- Sentence-final particles (ね, よ, な) encode pragmatic meaning English handles through intonation

### Cultural embedding
Words carrying cultural assumptions absent in the target language:
- 先輩/後輩 — more than "senior/junior"; encodes a web of social obligations
- お疲れ様 — a greeting/acknowledgment with no English equivalent
- 空気を読む — "reading the air" encompasses a cultural concept

## Approaches to handling non-equivalence

### Meaning-based definitions alongside translations
Don't rely solely on a gloss. Provide an explanation of what the word means in its own cultural/linguistic context, then give the best available English equivalent with caveats.

### Contrastive usage notes
Explain where the equivalence breaks down. For あげる: "Unlike English 'give,' あげる cannot be used when the recipient is the speaker or the speaker's in-group."

### Cross-references between related terms
Link あげる ↔ くれる ↔ もらう so learners see the system, not isolated words.

### Example sentences showing boundaries
Examples should demonstrate contexts where the English translation does and doesn't apply. Show the edge cases, not just the prototypical center.

### Semantic labels for sense disambiguation
When different senses require different English translations, label clearly and provide examples for each.

## Implications for je-dict-1

The notes field is where je-dict-1 addresses translation equivalence problems. Good notes explain the conceptual space a word occupies, contrast it with related Japanese words, and flag where the English gloss is misleading.

The "similar words" sections (a v2 quality standard) are particularly valuable for words in semantic fields where English and Japanese carve up meaning differently.

Cross-references are also essential — they expose the system of related words rather than treating each entry in isolation.

## Related pages

- [Definition Strategies](definition-strategies.md) — practical techniques for writing effective glosses (complementary to this page)
- [Learner Lexicography](learner-lexicography.md) — broader principles of pedagogical dictionary design
- [Cross-Reference Design](../topics/cross-references.md)
- [Register and Formality](../topics/register.md)
- [Onomatopoeia and Mimetic Words](onomatopoeia-mimetics.md) — acute translation equivalence challenges for mimetics
