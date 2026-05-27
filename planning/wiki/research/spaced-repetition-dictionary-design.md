# Spaced Repetition, Retrieval Practice, and Dictionary Design

**Last updated**: 2026-05-27

## Overview

Spaced repetition — reviewing material at expanding intervals to combat forgetting — is one of the most robust findings in memory research. Combined with retrieval practice (actively recalling information rather than passively re-reading), it forms the empirical backbone of modern vocabulary learning tools like Anki, SuperMemo, and Memrise. This page reviews the core research, examines how dictionaries interact with spaced repetition workflows, and considers what a dictionary designed with these principles in mind would look like.

## The forgetting curve and spacing effect

### Ebbinghaus (1885)

The foundational work is Hermann Ebbinghaus's *Über das Gedächtnis* (1885), in which he memorized lists of nonsense syllables and tested his retention over time. He discovered that forgetting follows an approximately exponential curve: rapid initial loss, then a gradually slowing decline. Crucially, he also found that each review "resets" the curve to a shallower slope — the same material requires progressively less effort to relearn.

### Cepeda et al. (2006): The definitive meta-analysis

Cepeda, Pashler, Vul, Wixted, and Rohrer (2006) conducted a meta-analysis of 184 articles containing 317 experiments (839 assessments) on distributed practice. Key findings:

- **Spacing consistently outperforms massing.** Across all conditions, distributing practice over time produced better retention than concentrating it in one session.
- **Optimal gap scales with retention interval.** The inter-study interval (ISI) producing maximum retention was roughly 10–20% of the desired retention period for short delays (a few weeks), falling to about 5% for year-long retention. For example, if you want to remember something for 30 days, the optimal gap between study sessions is roughly 3–6 days; for one year, roughly 2–3 weeks.
- **Diminishing returns of very long gaps.** Beyond the optimal ISI, performance declines — there is a genuine cost to spacing items too far apart, especially early in learning.

### Pimsleur (1967): Graduated interval recall

Paul Pimsleur independently arrived at a practical spacing schedule for language learning: 5 seconds, 25 seconds, 2 minutes, 10 minutes, 1 hour, 5 hours, 1 day, 5 days, 25 days, 4 months, 2 years. This "graduated interval recall" schedule was designed for audio-based instruction and remains influential in commercial language courses. The key insight — that early repetitions need to be very closely spaced, with intervals expanding rapidly — anticipated later algorithmic approaches.

### Nakata (2015): Expanding vs. equal spacing for L2 vocabulary

Nakata (2015) directly tested expanding spacing (intervals that increase: e.g., 1–2–4–8) against equal spacing (constant intervals: e.g., 4–4–4–4) for Japanese university students learning English vocabulary. Results showed a limited but statistically significant advantage of expanding spacing — the first L2 study to demonstrate this superiority. However, Nakata also found that initial massed practice followed by spaced review could be beneficial in the earliest stages of acquisition, when the form–meaning link is still fragile.

Nakata and Elgort (2021) extended this work to contextual vocabulary learning, finding that spacing facilitated the acquisition of explicit (form–meaning) vocabulary knowledge but not tacit (contextual usage) knowledge — an important nuance for dictionary design.

## Retrieval practice and the testing effect

### The core finding

The "testing effect" or "retrieval practice effect" refers to the robust finding that actively retrieving information from memory strengthens that memory more than passively re-studying the same information (Roediger & Karpicke 2006). The effect holds across ages, materials, and testing formats.

For L2 vocabulary specifically:
- Nakata (2017) showed retrieval practice facilitated vocabulary learning more than repeated studying across multiple experiments with Japanese EFL learners.
- Nakata and Webb (2016) found that cumulative tests — where previously studied items reappear on later tests — produced strong distributed retrieval practice benefits.
- Maie and Nakata (2025) replicated the cumulative testing advantage across proficiency levels.

### The generation effect

A related phenomenon is the "generation effect" (Slamecka & Graf 1978): generating an answer produces better memory than reading the same answer. For vocabulary learning, this means that tasks requiring the learner to produce a word (e.g., translating L1→L2, filling a gap, writing a sentence) create stronger memories than tasks presenting the word for reading.

### Desirable difficulties

Bjork and Bjork (2011) unified these findings under the framework of "desirable difficulties" — learning conditions that feel harder during practice but produce better long-term retention:

1. **Spacing** (distributing practice over time)
2. **Interleaving** (mixing different types of items rather than blocking by category)
3. **Retrieval practice** (testing rather than re-studying)
4. **Generation** (producing rather than recognizing)

The paradox is that learners consistently prefer massed, blocked, recognition-based study — the conditions that feel most fluent but produce the worst long-term results. Kornell (2009) and Logan et al. (2012) demonstrated this metacognitive illusion: learners give higher "judgments of learning" to massed items (which feel more familiar) even though spaced items are better retained.

## Spaced repetition systems (SRS)

### From Leitner to SM-2 to modern algorithms

The Leitner system (1972) was the first practical spaced repetition method: physical flashcards are sorted into boxes by mastery level, with difficult cards reviewed more frequently. However, the original Leitner system used fixed intervals per box rather than computed optimal gaps.

Piotr Woźniak's SuperMemo (1987) introduced the SM-2 algorithm, which computes per-item review intervals based on an "ease factor" adjusted by the learner's self-reported recall quality. Despite being over three decades old, SM-2 remains the default scheduling algorithm in Anki and most open-source SRS tools.

Modern systems (FSRS in Anki 2023+, SuperMemo's SM-18, Duolingo's half-life regression model) use machine learning to predict forgetting probabilities per item, allowing more precise scheduling. The core principle remains unchanged: items the learner finds difficult get shorter intervals; well-known items get longer intervals.

### Sentence mining as the bridge between SRS and dictionaries

In the Japanese learning community, "sentence mining" has become the dominant SRS practice: learners extract sentences from native content (novels, anime, news) where they encounter unknown words, create Anki cards with the sentence and a dictionary definition, and review them on an SRS schedule. The workflow is:

1. **Encounter** an unknown word in context
2. **Look it up** in a dictionary (Yomichan/Yomitan, Jisho, or a dedicated app)
3. **Create a card** with the sentence, the word, and the dictionary definition
4. **Review** on the SRS schedule

This makes dictionaries a critical upstream component of the SRS pipeline. The quality of the dictionary entry — its definitions, examples, notes on usage, and cross-references — directly determines the quality of what the learner stores in their SRS deck. A poor dictionary entry produces a poor flashcard, and the learner may successfully memorize incorrect or incomplete information.

The "i+1" principle (Krashen 1985, adapted by the sentence-mining community) recommends selecting sentences with exactly one unknown element. This creates a natural difficulty gradient and ensures the card is learnable from context.

## Dictionary consultation and vocabulary retention

### The Involvement Load Hypothesis

Laufer and Hulstijn (2001) proposed that vocabulary retention from a task depends on three factors: **need** (motivation to learn the word), **search** (effort to find the form–meaning connection), and **evaluation** (comparison with other words or contexts). Dictionary consultation involves search — the learner actively looks up the word — which produces better retention than passive glossing where the definition is provided alongside the text.

Hulstijn, Hollander, and Greidanus (1996) confirmed this experimentally: dictionary users retained words better than the control group, and the effect was amplified when combined with contextual guessing (guess first, then verify via dictionary).

### Frequency of consultation

Multiple lookups of the same word — the dictionary equivalent of spaced repetition — produce strong retention. However, learners frequently look up a word only once and never return to verify or deepen their understanding. Nesi and Haill (2002) documented this "single consultation" pattern as a major source of vocabulary learning failure.

This has a direct implication for dictionary design: features that encourage return visits (browsing pathways, cross-references, "related entries" sections) function as informal spaced repetition, exposing the learner to partially known vocabulary in new contexts.

## Implications for je-dict-1

### The dictionary as an SRS content source

je-dict-1 entries are already structured in ways that serve SRS card creation well:

| Entry feature | SRS card element | Quality factor |
|---------------|-----------------|----------------|
| Headword + reading | Front of card | Furigana ensures correct pronunciation |
| Top-level gloss | Back of card (short) | Concise L1 equivalent for quick review |
| Example sentences | Context sentences | Progressive difficulty supports i+1 selection |
| Notes | Extended definition | Deeper understanding for evaluation tasks |
| Cross-references | Related cards | Network building across cards |

The example sentences are particularly valuable: the progressive length design (short → long) means a sentence miner can select the example closest to their level. The vocabulary tier annotations could theoretically be used to filter examples by the learner's approximate level.

### Cross-references as distributed encounters

Research on the spacing effect shows that encountering a word in a new context is more beneficial than encountering it in the same context (Cepeda et al. 2006). je-dict-1's cross-reference system creates exactly this kind of varied encounter: a learner who looks up 教える encounters it again when browsing 教育, 先生, or 習う. Each re-encounter activates different semantic associations, producing the kind of "elaborative retrieval" that strengthens memory traces.

The current cross-reference density (0.58 per entry, 16,140 total) is growing but remains below what would maximize this effect. Higher cross-reference density directly increases the probability of serendipitous re-encounters during browsing.

### The browsing dictionary as "desirable difficulty"

A dictionary designed for browsing — as opposed to one optimized for quick lookup and dismissal — introduces desirable difficulties:

- **Search effort**: navigating related entries requires more processing than a quick definition glance, creating the "search" component of involvement load
- **Evaluation**: encountering a cross-referenced near-synonym (e.g., 見る vs. 観る vs. 眺める) forces the learner to compare and discriminate, the highest-involvement processing component
- **Generation**: notes that describe usage patterns in English prompt the learner to mentally generate Japanese sentences, activating the generation effect
- **Interleaving**: browsing across entries naturally interleaves vocabulary from different semantic domains, unlike the blocking that occurs when studying from a topically organized textbook

### Practical design features that support spaced repetition

Several features, some already present and some potential, would strengthen the dictionary's integration with SRS workflows:

1. **Stable entry URLs** (already present): Each entry has a permanent URL based on its five-digit ID. This allows SRS cards to link back to the source entry for review. Card creators can include the URL on the back of their card for instant access to the full entry during review.

2. **Example sentence selection cues** (partially present): The progressive-length design helps, but explicit vocabulary-tier annotations on example sentences would let card creators select i+1-appropriate sentences more easily.

3. **Collocation fields as SRS prompts** (partially present): Common collocations (e.g., 約束を守る for 約束) are natural SRS card candidates. The collocation field, where present, provides ready-made card content.

4. **"Similar words" as discrimination cards** (partially present): Near-synonym sections directly support the creation of discrimination cards — cards that test whether the learner can distinguish between confusable items, a task that benefits particularly from interleaved practice.

5. **Conjugation tables as reference** (present): Full conjugation tables allow card creators to generate form-focused cards (e.g., "What is the て-form of 走る?") that test morphological knowledge through retrieval practice.

### The metacognitive illusion and dictionary design

Research on metacognitive illusions (Kornell 2009; Logan et al. 2012) has a subtle implication for dictionary design: learners tend to believe they have learned a word after a single successful lookup, when in fact single-exposure retention is poor (Waring & Takaki 2003 found only 4% delayed production from single encounters — see [Incidental Vocabulary Acquisition Through Reading](incidental-vocabulary-reading.md)).

A dictionary can counteract this illusion by:
- Making the richness of word knowledge visible (multiple senses, collocations, register information, aspect behavior) so the learner recognizes how much they don't yet know
- Providing cross-references that naturally lead to re-encounters with partially known words
- Structuring notes to highlight non-obvious dimensions of knowledge (e.g., "ている typically indicates a resultative state, not ongoing action" for 知る) that the learner wouldn't discover from a simple gloss

### What a dictionary cannot do

A dictionary is not an SRS system. It cannot track what the individual learner knows, schedule reviews, or adapt to performance. The dictionary's role is to be the best possible *source* of information that the learner (or their SRS tool) draws from. The quality dimensions that matter most for this role are:

- **Accuracy**: wrong information memorized via SRS is especially hard to correct (the same spaced repetition that aids correct learning entrenches errors)
- **Completeness**: partial entries produce partial knowledge cards
- **Example quality**: sentences used as SRS card contexts must be natural, correctly glossed, and appropriately leveled
- **Navigability**: the easier it is to find related entries, the more the dictionary supports the "varied context" encounters that spaced repetition research shows are most effective

## References

- Barcroft, J. (2015). *Lexical Input Processing and Vocabulary Learning*. John Benjamins.
- Bjork, E. L., & Bjork, R. A. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), *Psychology and the Real World* (pp. 56–64). Worth Publishers.
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3), 354–380.
- Ebbinghaus, H. (1885). *Über das Gedächtnis: Untersuchungen zur experimentellen Psychologie*. Duncker & Humblot.
- Hulstijn, J. H., Hollander, M., & Greidanus, T. (1996). Incidental vocabulary learning by advanced foreign language students: The influence of marginal glosses, dictionary use, and reoccurrence of unknown words. *Modern Language Journal*, 80(3), 327–339.
- Kornell, N. (2009). Optimising learning using flashcards: Spacing is more effective than cramming. *Applied Cognitive Psychology*, 23(9), 1297–1317.
- Krashen, S. D. (1985). *The Input Hypothesis: Issues and Implications*. Longman.
- Laufer, B., & Hulstijn, J. (2001). Incidental vocabulary acquisition in a second language: The construct of task-induced involvement. *Applied Linguistics*, 22(1), 1–26.
- Leitner, S. (1972). *So lernt man lernen*. Herder.
- Logan, J. M., Castel, A. D., Haber, S., & Viehman, E. J. (2012). Metacognition and the spacing effect: The role of repetition, feedback, and instruction on judgments of learning for massed and spaced rehearsal. *Metacognition and Learning*, 7, 175–195.
- Maie, R., & Nakata, T. (2025). Cumulative testing for L2 vocabulary learning: The impact of retrieval practice and proficiency. *TESOL Quarterly*, 59(1).
- Nakata, T. (2015). Effects of expanding and equal spacing on second language vocabulary learning: Does gradually increasing spacing increase vocabulary learning? *Studies in Second Language Acquisition*, 37(4), 677–711.
- Nakata, T., & Elgort, I. (2021). Effects of spacing on contextual vocabulary learning: Spacing facilitates the acquisition of explicit, but not tacit, vocabulary knowledge. *Second Language Research*, 37(2), 233–260.
- Nesi, H., & Haill, R. (2002). A study of dictionary use by international students at a British university. *International Journal of Lexicography*, 15(4), 277–305.
- Pimsleur, P. (1967). A memory schedule. *Modern Language Journal*, 51(2), 73–75.
- Roediger, H. L., III, & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science*, 17(3), 249–255.
- Slamecka, N. J., & Graf, P. (1978). The generation effect: Delineation of a phenomenon. *Journal of Experimental Psychology: Human Learning and Memory*, 4(6), 592–604.
- Waring, R., & Takaki, M. (2003). At what rate do learners learn and retain new vocabulary from reading a graded reader? *Reading in a Foreign Language*, 15(2), 130–163.

## Related pages

- [Vocabulary Acquisition](vocabulary-acquisition.md) — broader L2 vocabulary learning research
- [Vocabulary Learning Strategies](vocabulary-learning-strategies.md) — strategy taxonomies including SRS
- [Incidental Vocabulary Acquisition Through Reading](incidental-vocabulary-reading.md) — single-exposure retention data
- [Depth of Vocabulary Knowledge](depth-of-vocabulary-knowledge.md) — what "knowing a word" means beyond form–meaning mapping
- [Example Sentence Design](example-sentences.md) — quality standards for the sentences that feed SRS cards
- [Cross-Reference Design](../topics/cross-references.md) — how linking creates distributed encounters
- [Sentence Mining Integration](../ideas/sentence-mining.md) — practical integration with Anki workflows
- [Digital Dictionary UX](digital-dictionary-ux.md) — interface design that supports browsing as re-encounter
