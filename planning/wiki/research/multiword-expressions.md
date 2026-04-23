# Multiword Expressions in Learner Dictionaries

**Last updated**: 2026-04-23

## What multiword expressions are

Multiword expressions (MWEs) are sequences of two or more words that behave as a single lexical unit — stored, retrieved, and used as wholes rather than assembled compositionally each time. Wray (2002) defines a formulaic sequence as "a sequence, continuous or discontinuous, of words or other elements, which is, or appears to be, prefabricated: that is, stored and retrieved whole from memory at the time of use, rather than being subject to generation or analysis by the language grammar."

The term "multiword expression" is an umbrella covering a wide range of phenomena that the literature has named separately: collocations, idioms, fixed expressions, formulaic sequences, lexical bundles, phrasal verbs, set phrases, proverbs, greetings, light-verb constructions, and compound verbs. What unites them is that they occupy territory between the single word and the freely composed sentence — they are too fixed or too conventionalized to be treated as free syntax, but too large to be a single word.

## Taxonomy of MWE types

The lexicographic literature generally recognizes a continuum from fully compositional to fully opaque, though the categories are not sharply bounded.

### By compositionality

| Type | Compositionality | Examples (English) | Examples (Japanese) |
|------|-----------------|-------------------|-------------------|
| **Free combinations** | Fully compositional | read a book | 本を読む |
| **Collocations** | Semantically transparent but conventionally restricted | heavy rain (not *strong rain) | 電話をかける (not *電話をする) |
| **Light-verb constructions** | Verb is semantically bleached | take a walk, make a decision | 決断を下す, 影響を与える |
| **Figurative idioms** | Metaphorically motivated | spill the beans, break the ice | 腹を割る, 顔が広い |
| **Pure idioms** | Fully opaque | kick the bucket, by and large | 油を売る, さじを投げる |

This compositionality continuum (following Cowie 1998, building on Vinogradov's tripartite classification) is the central challenge for dictionary-makers: fully compositional combinations don't need entries, fully opaque idioms clearly do, and everything in between requires judgment.

### By grammatical structure (Japanese-focused)

| Category | Japanese term | Structure | Example |
|----------|-------------|-----------|---------|
| Compound verbs | 複合動詞 | V1連用形 + V2 | 飛び込む, 考え込む |
| Verb-object idioms | 慣用句 | N + particle + V | 気をつける, 顔を出す |
| Four-character compounds | 四字熟語 | 4 kanji (often from Chinese) | 一石二鳥, 七転八起 |
| Proverbs | ことわざ | Full clause | 猿も木から落ちる |
| Greetings/routines | 挨拶表現 | Fixed phrases | いただきます, お疲れ様 |
| Grammar patterns | 文型 | Slot + fixed frame | 〜について, 〜によると |
| Adverbial set phrases | 連語 | N/Adj + particle | 久しぶりに, 初めて |
| Light-verb constructions | 機能動詞結合 | N + をする/になる | 勉強をする, 問題になる |

## The dictionary placement problem

The most persistent practical problem in MWE lexicography is where to put multiword entries in the dictionary's macrostructure. Five main strategies exist (surveyed in Atkins & Rundell 2008):

1. **Under the first content word**: place "spill the beans" at *spill*
2. **Under the least frequent word**: place it at *beans* (expecting a shorter entry with less competition)
3. **Under the first noun**: a common convention in many dictionaries
4. **Under the first verb**: used by some verb-focused dictionaries
5. **As a headword in its own right**: treat the MWE as an independent entry

For print dictionaries, strategies 1–4 were necessary because entries were anchored to single headwords. Digital dictionaries can and should use strategy 5 — giving the MWE its own entry — because search eliminates the findability problem that drove alphabetical placement decisions.

### Subentry vs. independent entry

Even in digital dictionaries, the question persists in a different form: should an MWE be a subentry (documented within a component word's entry) or an independent entry?

**Arguments for independent entries:**
- Findability via search — users type the full phrase
- MWEs often have their own usage patterns, register, collocations, and examples that don't fit naturally into a component word's entry
- Cleaner data model — each entry has one headword and one set of definitions

**Arguments for subentry treatment:**
- Avoids entry count bloat for transparent combinations
- Groups related information (a verb's collocations belong with the verb)
- Teaches patterns rather than individual instances

The emerging consensus (Granger & Meunier 2008, Siepmann 2005) favors giving MWEs independent entries when they are idiomatic or when the combination has specific nuances, while documenting productive patterns within the base word's entry.

## MWE types and acquisition challenges

### Collocations

Collocations are the most numerous MWE type and arguably the most important for learners. Nesselhauf (2005) showed that even advanced L2 learners produce systematic collocation errors, and that L1-incongruent collocations (where the L1 uses a different combination) are the most error-prone. Yamashita & Jiang (2010) confirmed persistent L1 influence on collocation processing even among highly proficient Japanese learners of English.

For a Japanese-English dictionary, this means that collocations where Japanese and English diverge in verb or adjective choice are especially worth documenting: 薬を飲む (drink medicine, not *eat medicine), 傘をさす (put up an umbrella, using さす not *開く), 写真を撮る (take a photo, using 撮る not *取る).

### Idioms (慣用句)

Japanese idioms typically follow a Noun + Particle + Verb pattern, with the meaning extending beyond the literal: 顔が広い (face is wide → well-connected), 腹を割る (split the belly → speak frankly), 気が利く (attention works → be attentive/considerate). The body-part idioms (目, 手, 口, 腹, 顔, 気, etc.) are especially productive and form semantic clusters.

Learner acquisition research shows that idioms with transparent metaphorical motivation (顔が広い is visualizable) are easier to learn than fully opaque ones (油を売る, literally "sell oil" → to slack off), and that dictionaries can aid acquisition by noting the metaphorical logic when it exists.

### Compound verbs (複合動詞)

Japanese compound verbs (V1 stem + V2) are a particularly complex MWE category because they span a continuum from fully lexical (打ち明ける, to confess) through semi-transparent (考え込む, to become absorbed in thought) to fully productive-aspectual (食べ始める, to begin eating). The NINJAL Compound Verb Lexicon catalogs over 2,700 entries. See the [Compound Verb Representation](../topics/compound-verbs.md) topic page for detailed treatment.

### Formulaic routines

Greetings (いただきます, ごちそうさま, お疲れ様), conversational formulas (よろしくお願いします), and social routines are MWEs with high pragmatic importance but relatively simple semantics. They are essential for communicative competence and their cultural loading makes them high-priority dictionary entries. Their meaning is often more about social function than lexical content.

### Grammar patterns

Expressions like 〜について (concerning), 〜によると (according to), and 〜てしまう (V-te shimau, expressing completion or regret) sit at the boundary between lexis and grammar. Some dictionaries treat these as entries; others leave them to grammar references. For a learner's dictionary, including the most common patterns as entries aids lookup when learners encounter them in text.

## Frequency and coverage

Research consistently shows that formulaic language constitutes a substantial fraction of natural text:

- Erman & Warren (2000) found that about 55% of spoken and written English text consists of "prefabricated" combinations
- Biber et al. (1999) found that certain lexical bundles (e.g., "on the other hand," "as a result of") are so frequent that omitting them leaves gaps in any learner dictionary

For Japanese, the situation is comparable. The 慣用句 corpus contains over 4,000 expressions in common use; the NINJAL compound verb lexicon has 2,700+; and productive patterns (〜ている, 〜てしまう, 〜ことにする, etc.) pervade everyday text. A learner dictionary that covers only single words misses a large portion of the phrases learners need to decode text.

## Dictionary treatment strategies

### Dedicated MWE entries (the je-dict-1 approach)

je-dict-1 uses a flat entry model where MWEs get their own independent entries with the POS tag "expression." As of April 2026, the dictionary contains approximately 745 entries tagged as expressions, including:

| Subtype | Count | Examples |
|---------|-------|---------|
| Verb-object phrases (を) | ~233 | 気をつける, 顔を出す, 手を打つ |
| Subject-predicate phrases (が) | ~113 | 気が利く, 気が重い, 目が覚める |
| Location/goal phrases (に) | ~100 | 気に入る, 身につける, 手に入れる |
| Greetings/routines | ~50+ | いただきます, ごちそうさま, お疲れ様 |
| Proverbs | ~15 | 猿も木から落ちる, 灯台下暗し |
| Grammar patterns | ~7 | 〜について, 〜によると, 〜てしまう |
| Other fixed phrases | ~227 | かもしれない, 後で, 本当は |

This approach makes every MWE independently searchable and gives each one space for its own examples, notes, and cross-references. The trade-off is that it can obscure the relationship between an MWE and its component words — a learner looking up 気 won't automatically see that 気をつける, 気に入る, 気が利く, 気が重い, etc. exist unless cross-references are comprehensive.

### Collocation fields within entries

Many learner dictionaries (Oxford Collocations Dictionary, Kenkyusha's) embed collocation information within the base word's entry rather than creating separate entries. This groups related combinations together and teaches patterns. je-dict-1 supports this through its notes field, where entries can list typical collocations (e.g., listing 激しい, 強い, 大きい as typical modifiers for 雨).

### Dual approach (recommended)

The strongest approach combines both strategies:

1. **Independent entries** for MWEs that are idiomatic, pragmatically loaded, or have specific nuances (idioms, greetings, proverbs, metaphorical expressions)
2. **Collocation documentation** within base-word entries for transparent but conventionally restricted combinations
3. **Cross-references** linking independent MWE entries back to their component words and linking component words forward to their MWE entries

## Inclusion criteria for MWE entries

When should an MWE get its own dictionary entry? Drawing from the literature and je-dict-1's practice, these criteria emerge:

| Criterion | Give it an entry | Document in base word |
|-----------|-----------------|----------------------|
| **Compositionality** | Meaning is not predictable from parts | Meaning is sum of parts |
| **Fixedness** | Substitution breaks the expression | Components can be varied |
| **Frequency** | High frequency in natural text | Low frequency or fully productive |
| **Cultural loading** | Carries pragmatic/cultural meaning | Purely referential |
| **Lookup likelihood** | Learner will search for the whole phrase | Learner can decompose |
| **Nuance** | Specific connotations beyond components | Meaning is straightforward |

The decision criterion from the compound verbs discussion applies broadly: **if a learner who knows the component words separately would still need help understanding the combination, it deserves its own entry.**

## Japanese-specific considerations

### The 気 cluster problem

Some base words are extraordinarily productive in MWE formation. 気 (spirit, mind, feeling) participates in dozens of idiomatic expressions: 気をつける, 気に入る, 気が利く, 気が重い, 気が短い, 気になる, 気にする, 気を使う, etc. Each has distinct meaning and usage. A dictionary faces a choice:

- List all of these in the 気 entry → the entry becomes enormous and hard to navigate
- Give each its own entry → the relationship to 気 is fragmented
- Both: independent entries with comprehensive cross-references from 気 → best for learners but requires systematic cross-referencing

### Particle as part of the expression

Japanese MWEs typically include a particle (を, に, が, で, と) that is integral to the meaning. 気**に**なる (become concerned) and 気**を**つける (be careful) have different particles and completely different meanings. The particle is part of the stored unit and must be included in the headword. This is why je-dict-1's expression entries include particles in their headwords.

### Honorific/register variants

Many MWEs have register variants that may or may not merit separate entries: お疲れ様 vs. お疲れ様です vs. お疲れ様でした; よろしく vs. よろしくお願いします vs. よろしくお願いいたします. The dictionary must decide whether to create entries for each variant or document the range within a single entry.

## Related research

### Siepmann (2005) on compositional routine formulae

Siepmann analyzed major learner dictionaries and found that they "still tend to focus on traditional non-compositional idioms whilst disregarding compositional routine formulae that have been shown to be much more frequent in both writing and speech." This finding suggests that dictionaries should expand coverage beyond opaque idioms to include frequent collocations and semi-fixed phrases. je-dict-1's inclusion of greetings, adverbial phrases, and grammar patterns as expression entries aligns with Siepmann's recommendation.

### Palmer and Hornby's early Japanese MWE work

Cowie (1998) documents that modern phraseological research originated in Japan through the work of Harold E. Palmer and A. S. Hornby in the 1930s, who developed elaborate syntactic categorizations of multiword units (verbal, nominal, adjectival, etc.) while working at the Institute for Research in English Teaching in Tokyo. This historical connection between Japanese language teaching and MWE lexicography is notable — the dictionary tradition's first systematic approach to MWEs grew from the challenges of teaching English to Japanese learners.

## Implications for je-dict-1

### Current strengths

1. **Independent entry model**: The flat-entry approach with "expression" as a POS tag gives each MWE full entry treatment (examples, notes, cross-references), which is the modern best practice for digital dictionaries.
2. **Particle inclusion**: Headwords include particles (気をつける, not 気つける), correctly representing the stored unit.
3. **Diverse coverage**: The 745 expression entries span idioms, greetings, grammar patterns, proverbs, and set phrases — not just opaque idioms.

### Areas for improvement

1. **Cross-reference density**: MWE entries should systematically cross-reference their component words, and component-word entries should list their productive MWEs. A learner looking up 気 should find all 気-based expressions; a learner looking up 気をつける should see 気 and つける as related entries.

2. **Metaphorical motivation notes**: For figurative idioms, noting the metaphorical logic (when transparent) aids acquisition. 顔が広い → "wide face" → knowing many people → well-connected. This kind of etymological note helps learners remember and correctly deploy the expression.

3. **Collocation fields in non-expression entries**: Verb and noun entries could benefit from structured collocation information (typical objects for transitive verbs, typical modifiers for nouns) beyond what the current notes field provides.

4. **Grammar pattern coverage**: Only 7 grammar-pattern expressions exist. Common patterns like 〜ことにする, 〜ようにする, 〜わけにはいかない, and 〜ざるを得ない are highly lookup-worthy and could be added as expression entries.

5. **MWE search**: The search system could be enhanced to handle partial MWE matches — if a user searches for 気をつける but the entry headword uses furigana markup, the search should still find it. Similarly, searching for a component word could surface related MWE entries.

6. **Body-part idiom clusters**: Systematically auditing and expanding body-part MWEs (気, 手, 目, 口, 顔, 腹, etc.) would fill a high-value gap, as these are among the most frequent and most opaque MWEs learners encounter.

## References

- Atkins, B. T. S. & Rundell, M. (2008). *The Oxford Guide to Practical Lexicography*. Oxford University Press.
- Biber, D., Johansson, S., Leech, G., Conrad, S. & Finegan, E. (1999). *Longman Grammar of Spoken and Written English*. Longman.
- Cowie, A. P. (Ed.) (1998). *Phraseology: Theory, Analysis, and Applications*. Oxford University Press.
- Erman, B. & Warren, B. (2000). The idiom principle and the open choice principle. *Text*, 20(1), 29–62.
- Granger, S. & Meunier, F. (Eds.) (2008). *Phraseology in Foreign Language Learning and Teaching*. John Benjamins.
- Moon, R. (1998). *Fixed Expressions and Idioms in English: A Corpus-Based Approach*. Oxford University Press.
- Nesselhauf, N. (2005). *Collocations in a Learner Corpus*. John Benjamins.
- Pawley, A. & Syder, F. H. (1983). Two puzzles for linguistic theory: Nativelike selection and nativelike fluency. In J. C. Richards & R. W. Schmidt (Eds.), *Language and Communication* (pp. 191–226). Longman.
- Siepmann, D. (2005). Collocation, colligation and encoding dictionaries. *International Journal of Lexicography*, 18(4), 409–443.
- Wray, A. (2002). *Formulaic Language and the Lexicon*. Cambridge University Press.
- Yamashita, J. & Jiang, N. (2010). L1 influence on the acquisition of L2 collocations. *TESOL Quarterly*, 44(4), 647–668.

## Related pages

- [Collocations in Learner Dictionaries](collocations.md) — detailed treatment of collocations specifically
- [Compound Verb Representation](../topics/compound-verbs.md) — the V1+V2 compound verb design question
- [Example Sentence Design](example-sentences.md) — MWEs in example contexts
- [Entry Design](../project/entry-design.md) — schema structure including expression POS
- [Cross-Reference Design](../topics/cross-references.md) — linking MWE entries to components
- [Word Formation and Morphology](word-formation.md) — compounding and derivation context
- [Definition and Gloss Strategies](definition-strategies.md) — how to define phrasal meanings
- [Grammar Information in Learner Dictionaries](grammar-in-dictionaries.md) — grammar patterns as MWEs
- [Semantic Prosody](semantic-prosody.md) — evaluative colouring in collocations and expressions
- [Register and Formality](../topics/register.md) — register variation in formulaic routines
