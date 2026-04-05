# Vocabulary Acquisition

**Last updated**: 2026-04-05 (deepened)

## How L2 learners acquire vocabulary

Second-language vocabulary acquisition research investigates how learners build, retain, and deploy lexical knowledge. The findings have direct implications for dictionary design.

## Key concepts

### Incremental acquisition
Knowing a word is not binary. Nation (2001) identifies multiple dimensions of word knowledge:
- **Form**: spoken, written, word parts
- **Meaning**: form-meaning connection, concepts, associations
- **Use**: grammatical functions, collocations, constraints on use

Learners acquire these dimensions gradually across many encounters. A dictionary that provides all these dimensions for each entry supports the full arc of acquisition.

### Frequency and coverage
Nation's research demonstrates that the most frequent 2,000-3,000 word families cover approximately 80-85% of running text in most genres. The next 7,000 families add roughly 8-10% more. This underpins the rationale for frequency-based vocabulary tiers — a small core vocabulary provides disproportionate text coverage.

### Incidental vs. intentional learning
- **Incidental learning**: occurs as a by-product of reading or listening (extensive reading research by Krashen, Waring, Nation)
- **Intentional learning**: deliberate study via flashcards, word lists, dictionary lookup

Both are necessary. Intentional learning is more efficient per unit of time, but incidental learning provides richer contextual knowledge. Learners typically need 12+ encounters with a word in context for incidental acquisition.

### Spaced repetition
Based on Ebbinghaus's forgetting curve, spaced repetition systems (SRS) schedule reviews at increasing intervals. Modern implementations (Anki) demonstrate that spaced practice consistently outperforms massed practice for long-term retention.

### Depth of processing
Craik & Lockhart's (1972) levels-of-processing framework predicts that deeper engagement with a word leads to better retention. The **involvement load hypothesis** (Laufer & Hulstijn, 2001) quantifies this: tasks with higher need, search, and evaluation demands produce better retention.

### The lexical threshold
Laufer (1989) proposed that learners need ~95% text coverage for adequate reading comprehension; Hu & Nation (2000) revised this to 98%. This has direct implications for which vocabulary learners need first.

### Receptive vs. productive vocabulary knowledge

Learners' vocabulary knowledge exists on a continuum from receptive (recognition) to productive (use):

- **Receptive knowledge**: recognizing a word's form and recalling at least one meaning when encountered in context. This is the easier and earlier-acquired dimension.
- **Productive knowledge**: retrieving a word's form from memory and using it correctly in original output, including appropriate collocations, register, and grammatical context. This is harder and develops later.

The gap between receptive and productive vocabulary size is substantial — Laufer (1998) found that learners' productive vocabularies were typically only 50-80% the size of their receptive vocabularies. Melka (1997) argued the relationship is not a simple dichotomy but a continuum of mastery, with partial productive knowledge as an intermediate stage.

For dictionary design, this means entries must serve both lookup modes: quick definition retrieval (receptive) and detailed usage guidance for output (productive). Collocations, particle patterns, and register labels primarily serve productive needs.

### Formulaic sequences and multiword units

Wray (2002) and Schmitt (2004) demonstrated that much of fluent language use consists of **formulaic sequences** — prefabricated chunks that are stored and retrieved as wholes rather than constructed word-by-word. Examples in Japanese include ～ことができる, お世話になっています, ～ているところ.

Research suggests formulaic sequences account for a large proportion of fluent speech and writing. Pawley & Syder (1983) posed the "puzzle of nativelike fluency" — how speakers choose, from all grammatically possible combinations, the ones that sound natural. The answer is largely collocational knowledge: knowing which words habitually co-occur.

For L2 learners, acquiring formulaic knowledge is one of the biggest challenges. Martinez & Schmitt (2012) compiled a Phrasal Expressions List (PHRASE List) of high-frequency multiword items that deserve dedicated teaching attention.

### Dictionary lookup and vocabulary retention

Research on dictionary use and retention shows mixed but instructive results:

- **Luppescu & Day (1993)** found that L2 readers with dictionary access learned more vocabulary from reading than those without, but read more slowly.
- **Knight (1994)** showed that dictionary use during reading led to better vocabulary retention than contextual guessing alone.
- **Hulstijn, Hollander, & Greidanus (1996)** found that dictionary consultation led to better retention than marginal glosses, likely because the search effort itself deepened processing (consistent with the involvement load hypothesis).
- **Laufer & Hill (2000)** found that learners who used multiple dictionary features (definitions, examples, collocations) retained more than those who only checked the basic gloss.

These findings support providing rich entry content — learners who engage with examples, notes, and collocations during a lookup are more likely to retain the word than those who just grab a translation.

## Notable researchers

| Who | Key contribution |
|-----|-----------------|
| **Paul Nation** | *Learning Vocabulary in Another Language* (2001/2013); Vocabulary Size Test; BNC/COCA word family lists |
| **Batia Laufer** | Lexical thresholds; involvement load hypothesis; productive vs. receptive vocabulary |
| **Norbert Schmitt** | *Vocabulary in Language Teaching* (2000); vocabulary assessment; formulaic sequences |
| **Rob Waring** | Extensive reading and graded readers for incidental acquisition |

## Implications for je-dict-1

### Tier system alignment
The basic/core/general tiers align with acquisition research: prioritize the most frequent, most useful words. The ~2,800 basic+core entries likely cover the vocabulary needed for ~85-90% text coverage.

### Rich entries support deep processing
By providing definitions, examples, collocations, usage notes, and cross-references, each entry offers multiple dimensions of word knowledge — exactly what research says learners need.

### Example sentences as encounters
Each example sentence is a contextual encounter with the target word. Multiple examples per sense, with progressive complexity, simulate the natural acquisition process of meeting a word in varied contexts.

### SRS compatibility
The dictionary's structured data (clear senses, example sentences with translations) is well-suited for extraction into Anki or other SRS tools, supporting intentional learning workflows.

### Serving receptive and productive needs
The entry structure already supports both vocabulary knowledge dimensions: quick glosses for receptive lookup, plus collocations, usage notes, and example sentences for productive use. The v2 quality improvements (register labels, similar-word distinctions, particle patterns) primarily strengthen the productive side.

### Dictionary engagement and retention
Research shows that learners who engage with multiple entry features retain more vocabulary. This argues against minimalist entries and in favor of the rich entry structure used here — but also for progressive disclosure in the UX, so that the richness doesn't overwhelm quick-lookup users.

### Formulaic knowledge
The dictionary's expression entries, collocation sections, and inline links to related patterns help learners build formulaic competence. The compound verb analysis (see [Compound Verb Representation](../topics/compound-verbs.md)) and collocation patterns in notes directly address the challenge of acquiring natural-sounding word combinations.

## Related pages

- [Vocabulary Tier System](../project/vocabulary-tiers.md)
- [Example Sentence Design](example-sentences.md)
- [Sentence Mining Integration](../ideas/sentence-mining.md)
- [Collocations in Learner Dictionaries](collocations.md)
- [Digital Dictionary UX](digital-dictionary-ux.md)
