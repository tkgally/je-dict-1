# Japanese Vocabulary Grading: Frequency Data and Learner Word Lists

**Last updated**: 2026-05-16

## Overview

How should Japanese vocabulary be ranked for learners? This question sits at the intersection of corpus linguistics, SLA research, and pedagogical tradition. Unlike English — where large-scale frequency lists (BNC, COCA) and well-established word family frameworks provide clear grading criteria — Japanese presents unique challenges: multiple productive morphological processes, a logographic writing system that provides partial compositional access to compound meaning, and a dominant exam-based grading tradition (JLPT) that was never empirically grounded. This page surveys the available frequency data, published word lists, and modern corpus-based alternatives, with specific attention to how they inform je-dict-1's tier system.

## Japanese corpora for frequency research

### BCCWJ: The gold standard

The Balanced Corpus of Contemporary Written Japanese (BCCWJ), compiled by NINJAL under the KOTONOHA project (2006–2011, Version 1.1 released 2012), is the most authoritative source for Japanese frequency data. Key characteristics:

| Feature | Detail |
|---------|--------|
| Size | ~104.3 million tokens |
| Period | Primarily 2001–2005 |
| Subcorpora | Publication (books, magazines, newspapers), Library (Tokyo public library holdings 1986–2005), Special-purpose (white papers, Diet proceedings, textbooks, Yahoo! Answers, Yahoo! Blogs, web pages) |
| Annotation | Morphologically tagged with UniDic; Short Unit Words (短単位) as the base counting unit |
| Access | Chunagon concordance system; derived frequency data available through NINJAL |
| Director | Maekawa Kikuo |

BCCWJ's balanced design across registers and genres makes it far more representative than newspaper-only corpora. Its genre tagging also enables dispersion analysis — measuring not just how often a word appears, but how evenly it is distributed across text types.

### Other Japanese corpora

| Corpus | Size | Strengths | Limitations |
|--------|------|-----------|-------------|
| **NWJC** (NINJAL Web Japanese Corpus) | ~25.8 billion tokens | Captures rare words, internet-era vocabulary, scale | Unbalanced; web-heavy; no genre control |
| **CSJ** (Corpus of Spontaneous Japanese) | ~7.5 million words | Spoken language frequency; academic/everyday | Small; genre-limited (lectures, conversations) |
| **Mainichi/Yomiuri** newspaper corpora | 10+ years each | Long time-series; clean text | Heavily formal register; over-represents politics/economics |
| **Aozora Bunko** | Varies | Literary/historical vocabulary | Skewed toward pre-1950s language |
| **Subtitle corpora** | Varies | Casual/spoken register | Uncontrolled; genre-limited; some noise from OCR |

For learner dictionary work, BCCWJ is the primary reference. NWJC supplements it for rare vocabulary and neologisms. CSJ would be relevant for a spoken-oriented dictionary but is too small to serve as a primary frequency source.

## Published Japanese frequency and word lists

### BCCWJ-derived vocabulary lists

**Matsushita Toshiko** (松下達彦, University of Tokyo) created the VDRJ (Vocabulary Database for Reading Japanese) using BCCWJ data with adjusted frequency accounting for dispersion. The VDRJ provides graduated difficulty levels and is one of the most rigorous corpus-based rankings available for Japanese.

**Sunakawa Yuriko et al.** (砂川有里子, University of Tsukuba) led development of the 日本語教育語彙表 (Japanese Language Education Vocabulary List, 2012), drawing on BCCWJ frequency and dispersion data combined with pedagogical criteria. This list assigns vocabulary to six levels based on cumulative coverage contribution and represents the most carefully constructed corpus-based alternative to JLPT lists.

### The JLPT word lists

The JLPT (Japanese Language Proficiency Test) has **never published an official vocabulary list** since the 2010 test reform. The pre-2010 examination guideline (出題基準, 2002) listed approximate vocabulary targets:

| Old level | Approximate vocabulary | Post-2010 equivalent |
|-----------|----------------------|---------------------|
| Level 4 | ~800 words | N5 |
| Level 3 | ~1,500 words | N4 |
| Level 2 | ~6,000 words | N3–N2 |
| Level 1 | ~10,000 words | N2–N1 |

Currently circulating "JLPT word lists" are community-reconstructed from test preparation materials, textbooks, and the now-withdrawn 2002 guideline. No list has official JLPT endorsement.

**Problems with JLPT word lists for dictionary grading:**

1. **Not corpus-based**: Selected by committee intuition rather than empirical frequency data
2. **Outdated**: Reflect 1990s vocabulary; no technology terms, internet-era words, or contemporary social vocabulary
3. **Exam-focused**: Prioritize testability (reading comprehension items) over communicative utility
4. **No dispersion weighting**: A word frequent only in newspapers gets the same level as one frequent across all genres
5. **Arbitrary boundaries**: The N3/N2 boundary is particularly poorly motivated
6. **N1 is undifferentiated**: Encompasses everything from "frequently useful in daily life" to "literary archaisms"
7. **No official list exists post-2010**: Everything in circulation is unofficial reconstruction

### Other approaches

**CEFR-J Wordlist** (Tono et al.): Maps Japanese vocabulary to Common European Framework levels using corpus evidence. Still developing but represents an attempt at international standardization.

**Chikamatsu et al. (2000)**: Published a **kanji character** frequency list based on the Asahi Shimbun corpus — useful for character-level analysis but not directly a word-level frequency ranking. (Chikamatsu, N., Yokoyama, S., Nozaki, H., Long, E., & Fukuda, S. "A Japanese logographic character frequency list for cognitive science research." *Behavior Research Methods, Instruments, & Computers*, 32(3), 482–500.)

## The word-family unit problem for Japanese

The most significant methodological challenge in Japanese vocabulary grading is the **counting unit**. English vocabulary research uses the "word family" (Nation, 2001): a base word plus its transparent inflections and derivations (e.g., *economy, economies, economic, economical, economize* = 1 family). This unit doesn't translate cleanly to Japanese.

### Why word families don't work for Japanese

1. **Sino-Japanese compound productivity**: Is 経済 (economy) + 経済学 (economics) + 経済学者 (economist) + 経済的 (economic) one family? If yes, knowing 経済 means "knowing" four entries. If no, the coverage numbers inflate relative to English.

2. **Verb derivation opacity**: Do 食べる (eat), 食べ物 (food), 食品 (food products), 食事 (meal), 食堂 (cafeteria) form one family? The character 食 unites them, but the phonological forms and readings differ completely (たべる, たべもの, しょくひん, しょくじ, しょくどう).

3. **Multiple readings**: Japanese kanji have multiple readings, and the same character in different compounds is effectively a different morpheme for production purposes. 生: なま (raw), い(きる) (to live), う(まれる) (to be born), せい (life/student) — these are historically related but functionally separate for a learner.

4. **suru-verb compounds**: Is a noun + する construction (勉強する) one item or two? BCCWJ's Short Unit Words split them; traditional pedagogy treats them as one vocabulary item.

### Counting units compared

| Unit | Definition | Effect on Japanese counts |
|------|-----------|--------------------------|
| **Short Unit Word** (短単位, BCCWJ default) | Minimal morphological unit | Inflates counts; splits suru-compounds |
| **Long Unit Word** (長単位) | Bunsetsu-like phrases | Deflates counts; may group too aggressively |
| **Lexical item** (語, traditional) | Pedagogical word unit | Middle ground; what textbooks and JLPT use |
| **Word family** (Nation-style) | Base + transparent derivatives | Unclear application to Japanese morphology |

Matsushita (2012) addresses this by using BCCWJ short unit words as the base but providing lemmatized groupings. Sunakawa's vocabulary list uses a pedagogically motivated "word" unit closer to what textbooks count.

### The kanji compound transparency advantage

Unlike English derivational morphology, many Japanese kanji compounds are semantically transparent at the character level. A learner who knows 食 (eat/food) and 品 (goods/items) can often infer 食品 (food products). This means:

- The "known vocabulary" for *comprehension* purposes is larger than the number of items explicitly studied
- Coverage curves are steeper for Japanese than for English once a critical mass of kanji is known
- But for *production*, each compound must still be learned individually (correct reading, collocations, register)

This asymmetry between receptive and productive vocabulary is sharper in Japanese than in English, and directly relevant to dictionary design: a dictionary aimed at productive use must treat kanji compounds individually even when a reader could infer their meaning.

## Japanese-specific coverage curve findings

Research applying the coverage model to Japanese (Matsushita 2012, building on Nation 2006):

| Coverage level | Approximate items needed (written Japanese) |
|---------------|---------------------------------------------|
| 90% | ~3,000–4,000 lemmas |
| 95% | ~5,000–6,000 lemmas |
| 98% | ~9,000–11,000 lemmas |

These numbers are approximate because they depend heavily on the counting unit and text type. Key findings:

1. **Fewer distinct items needed than English** for equivalent coverage, due to kanji compound transparency and productive Sino-Japanese morphology
2. **But total learning burden is similar or higher** because each item requires learning kanji forms, multiple readings, pitch accent, and appropriate contexts
3. **Proper nouns contribute heavily** in news/web text (3–6% of running tokens), providing "free" coverage
4. **Genre variation is extreme**: Casual blog text vs. academic writing can differ by 3,000+ items at the 98% threshold

## The JLPT–corpus divide in practice

The Japanese language teaching field currently operates with two parallel systems:

| Dimension | JLPT tradition | Corpus-based approach |
|-----------|---------------|----------------------|
| Basis | Expert/committee judgment | Empirical frequency + dispersion |
| Unit | Pedagogical "word" | Varies (lemma, short unit word) |
| Update cycle | Frozen since 2010 | Can be refreshed with new data |
| Strengths | Widely known; motivates learners; textbook ecosystem | Empirically grounded; updatable; genre-sensitive |
| Weaknesses | Outdated; exam-focused; unofficial | No single dominant list; methodological debates; less institutional backing |
| Adoption | Dominant in practice | Growing in research; limited classroom penetration |

The most promising developments are hybrid approaches (Sunakawa's vocabulary list, CEFR-J) that use corpus frequency as the primary criterion but apply pedagogical judgment as a secondary filter — exactly the approach je-dict-1's tier system takes, albeit at a coarser granularity.

## Implications for je-dict-1

### Tier system validation

je-dict-1's three-tier system (basic 801, core ~1,982, general 24,700+) maps roughly to frequency-based expectations:

- **Basic + core** (~2,800 items) corresponds to the first ~90% coverage band in Matsushita's estimates — foundational vocabulary for daily communication
- **General tier at 24,700+** extends well past the 98% threshold for written text — the dictionary already covers vocabulary deep enough for unassisted reading comprehension
- The tier boundaries were set by pedagogical judgment (survival vs. functioning vs. everything else), which aligns with the hybrid approach recommended by current research

### What frequency data could add

1. **Candidate prioritization**: Ranking candidate words by BCCWJ frequency × dispersion would ensure the highest-impact gaps are filled first. The `corpus_harvesting.md` task partially does this.
2. **Coverage gap analysis**: Comparing je-dict-1's headword list against BCCWJ's top-N frequency ranks would identify high-frequency words still missing.
3. **Tier boundary audit**: Cross-checking the basic/core tier contents against BCCWJ frequency would reveal any tier assignment anomalies (high-frequency words in general, low-frequency words in basic/core).
4. **Example vocabulary control**: Frequency data could inform which words are "safe" to use in examples for basic/core entries without exceeding the tier's self-containment budget.

### Why je-dict-1 doesn't use JLPT levels

The project's decision to avoid JLPT levels (documented in [Vocabulary Tier System](../project/vocabulary-tiers.md)) aligns with the research consensus:

- JLPT lists are not empirically grounded
- They haven't been updated to reflect modern vocabulary
- The five-level granularity is false precision for a non-exam dictionary
- je-dict-1's open "general" tier avoids the problem of arbitrarily ranking advanced vocabulary — consistent with the finding that beyond ~6,000 items, frequency-based ranking becomes unreliable (too much genre dependence)

### Production-oriented implications

The kanji compound transparency finding reinforces that je-dict-1's rich entry structure (collocations, register labels, usage notes, example sentences) serves a critical function: even when a learner can *read* a compound by inferring from kanji, they cannot *produce* it correctly without knowing the reading, register, collocations, and common patterns. A frequency-ranked word list alone cannot replace the deep entry treatment that supports productive use.

## References

- Chikamatsu, N., Yokoyama, S., Nozaki, H., Long, E., & Fukuda, S. (2000). A Japanese logographic character frequency list for cognitive science research. *Behavior Research Methods, Instruments, & Computers*, 32(3), 482–500.
- Matsushita, T. (2012). In what order should learners learn Japanese vocabulary: A corpus-based approach. University of Tokyo research papers.
- Nation, I.S.P. (2001). *Learning Vocabulary in Another Language*. Cambridge University Press.
- Nation, I.S.P. (2006). How large a vocabulary is needed for reading and listening? *Canadian Modern Language Review*, 63(1), 59–82.
- NINJAL (2012). *Balanced Corpus of Contemporary Written Japanese (BCCWJ)*. Version 1.1.
- Sunakawa, Y., Lee, J., & Takahara, M. (2012). 日本語教育語彙表 [Japanese Language Education Vocabulary List]. Tsukuba University research reports.
- Tono, Y. (2001). *Research on Dictionary Use in the Context of Foreign Language Learning*. Tübingen: Max Niemeyer Verlag.

## Related pages

- [Corpus Linguistics and Frequency Lists](corpus-linguistics.md) — general corpus linguistics principles and their application to lexicography
- [Vocabulary Size and Text Coverage](vocabulary-size-coverage.md) — the 95%/98% coverage threshold research (primarily English-language studies)
- [Vocabulary Tier System](../project/vocabulary-tiers.md) — je-dict-1's three-tier classification and its rationale
- [Controlled Defining Vocabulary](controlled-defining-vocabulary.md) — the CDV tradition and its relationship to je-dict-1's tier system
- [Lemmatization and Headword Selection](lemmatization-headword-selection.md) — entry scope and counting-unit decisions
- [Word Formation and Morphology](word-formation.md) — Japanese compounding and derivation patterns
- [Corpus-Driven Entry Prioritization](../ideas/corpus-prioritization.md) — using frequency data to guide dictionary expansion
- [Vocabulary Testing and Assessment](vocabulary-testing-assessment.md) — frequency-based vocabulary tests (VLT, VST) and the word-family counting problem for Japanese
