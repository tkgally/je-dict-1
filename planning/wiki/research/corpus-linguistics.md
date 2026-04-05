# Corpus Linguistics and Frequency Lists

**Last updated**: 2026-04-05

## How corpus data informs dictionary making

Corpus linguistics uses large, systematically collected text databases to study language empirically. Its application to lexicography transformed dictionary-making from an intuition-driven craft to a data-driven discipline.

## Key concepts

### Corpus-informed vs. corpus-driven
- **Corpus-informed**: Use corpus evidence to check and supplement lexicographer intuitions
- **Corpus-driven**: Let corpus patterns determine entry structure, sense divisions, and example selection from the ground up (advocated by Sinclair and the COBUILD project)

Most modern dictionaries, including je-dict-1, take a corpus-informed approach.

### Frequency and range
Raw frequency alone is insufficient for word selection. A word may be frequent overall but concentrated in one genre (e.g., legal terminology). **Range** (the number of different texts/genres a word appears in) is an important complementary measure. Dispersion-adjusted frequency metrics address this.

### Collocational analysis
Corpora reveal statistically significant word combinations that may not be intuitively obvious. Standard measures of collocational strength include mutual information (MI), t-score, and log-likelihood. This data directly informs which collocations to include in dictionary entries.

## Japanese corpora

| Corpus | Size | Description |
|--------|------|-------------|
| **BCCWJ** | ~104M words | Balanced Corpus of Contemporary Written Japanese. Published by NINJAL (2006-2011). Covers books, magazines, newspapers, white papers, web text. Morphologically annotated with UniDic. The gold standard. |
| **NWJC** | ~10B words | NINJAL Web Japanese Corpus. Much larger but less balanced than BCCWJ. |
| **TWC** | Large | Tsukuba Web Corpus. Another large-scale web corpus. |
| **Aozora Bunko** | Varies | Digital library of public-domain Japanese literary works. Useful for historical/literary vocabulary but skewed toward older language. |
| **Subtitle corpora** | Varies | Better representation of spoken/casual language. The "Innocent Corpus" is popular with learners. |

BCCWJ is the most authoritative source for contemporary Japanese frequency data, compiled under the KOTONOHA project at NINJAL led by Maekawa Kikuo.

## Frequency lists for Japanese

- **BCCWJ frequency lists** — published by NINJAL; the most authoritative
- **JLPT vocabulary lists** — not strictly corpus-derived; widely used as a proxy for frequency grading but increasingly superseded by corpus-based approaches
- **Wikipedia/web-derived lists** — various community-generated lists from web and media corpora

## Notable researchers

| Who | Contribution |
|-----|-------------|
| **John Sinclair** | Father of corpus-driven lexicography; led the COBUILD project (1987) |
| **Adam Kilgarriff** | Created Sketch Engine and "word sketches" for corpus-driven lexicography |
| **Maekawa Kikuo** | Led the BCCWJ project at NINJAL |
| **Paul Nation** | BNC/COCA word family lists demonstrating frequency-based pedagogy |

## Implications for je-dict-1

### Word selection
Corpus frequency (preferably BCCWJ) should guide which candidates to prioritize. The `corpus_harvesting.md` task already does this.

### Collocation data
Corpus collocational analysis could systematically identify which collocations to include in entry notes. Currently, collocations are selected by the LLM based on general knowledge rather than corpus evidence.

### Sense ordering
Within multi-sense entries, senses should generally be ordered by frequency of use, not etymology or semantic relatedness. Corpus data can inform this.

### Example authenticity
Corpus examples show real usage patterns but often need editing for learner accessibility. The current approach (LLM-constructed examples) produces clean, controlled sentences but may miss corpus-revealed patterns.

### Gap analysis
Comparing dictionary coverage against BCCWJ frequency ranks would identify the highest-impact missing entries.

## Related pages

- [Vocabulary Tier System](../project/vocabulary-tiers.md)
- [Corpus-Driven Entry Prioritization](../ideas/corpus-prioritization.md)
- [Learner Lexicography](learner-lexicography.md)
