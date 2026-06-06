# Translation Equivalence

**Last updated**: 2026-06-06

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

## Implications for multilingual versions

Every category of non-equivalence on this page is **target-language-specific**: it is defined
against English, and it changes when the target language is not English. The
[Multilingual Dictionary](../ideas/multilingual-dictionary.md) plan is, in one sense, this page
multiplied across languages. Concretely:

- **Lexical gaps move.** 先輩/後輩 is a hard *English* gap, but Korean lexicalizes it directly
  (선배/후배) and Chinese has close matches (前辈/学长/学姐). お疲れ様 and 空気を読む are gaps for
  some target languages and near-matches for others. A note that says "no English equivalent"
  is **English-specific content** and must be re-evaluated, not translated, for each language —
  exactly the boundary the
  [Japanese→Chinese Adaptation Brief](japanese-chinese-adaptation-brief.md) draws.
- **Semantic asymmetries differ.** The giving verbs (あげる/くれる/もらう) and the 着る/履く/被る
  "wear" split are genuine asymmetries against English; against a different L1 the contrast may be
  sharper or already present, so the *amount* of explanation needed varies by audience.
- **The asymmetry can flip to a false friend.** For a Chinese learner, the dominant
  equivalence hazard is not the lexical gap but the **同形異義語** — a shared kanji compound that
  *looks* like a perfect equivalent and is not (手紙 ≠ "letter" for a Chinese reader who reads it
  as 手纸 "toilet paper"). English has no analogue of this class because English shares no
  characters with Japanese. This is the single biggest structural difference between an
  English-target and a Chinese-target version of the same entry.

The practical rule for the translation pipeline: the **explanation of what the Japanese word
means in its own context** (the meaning-based definition) is largely universal and translates
cleanly; the **contrastive usage notes** ("unlike English X…") are the part this page is really
about, and they are the part that must be adapted per target language.

## Related pages

- [Definition Strategies](definition-strategies.md) — practical techniques for writing effective glosses (complementary to this page)
- [Learner Lexicography](learner-lexicography.md) — broader principles of pedagogical dictionary design
- [Cross-Reference Design](../topics/cross-references.md)
- [Register and Formality](../topics/register.md)
- [Onomatopoeia and Mimetic Words](onomatopoeia-mimetics.md) — acute translation equivalence challenges for mimetics
- [Semantic Prosody](semantic-prosody.md) — the evaluative dimension that monolingual glosses routinely strip
- [Gairaigo: Loanwords in Japanese](gairaigo-loanwords.md) — semantic shift in loanwords as a translation equivalence challenge
- [Pragmatics and Speech Acts](pragmatics-speech-acts.md) — when translation fails because the pragmatic function has no English equivalent
- [Sense Relations and Semantic Networks](sense-relations-semantic-networks.md) — cross-linguistic asymmetry in near-synonym sets and stratal synonymy
- [Near-Synonym Discrimination](near-synonym-discrimination.md) — why overlapping bilingual glosses obscure near-synonym distinctions
- [Register and Formality Marking](register-formality-marking.md) — register asymmetry in translation equivalents and diasystematic labels
- [Cultural Content in Bilingual Dictionaries](cultural-content-dictionaries.md) — culture-bound terms where translation equivalence breaks down entirely
- [Bilingual vs. Monolingual Dictionary Debate](bilingual-monolingual-debate.md) — why false equivalence risk does not make bilingual dictionaries inferior
- [Multilingual Dictionary](../ideas/multilingual-dictionary.md) — non-equivalence multiplied across target languages; what is invariant vs. adapted
- [Japanese→Chinese Adaptation Brief](japanese-chinese-adaptation-brief.md) — the first per-language working-out of which equivalence notes adapt and which translate
