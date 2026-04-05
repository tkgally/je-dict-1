# Corpus-Driven Entry Prioritization

**Last updated**: 2026-04-05

## Concept

Use frequency data from Japanese language corpora to prioritize which candidate words to create entries for next. The most frequently used words should generally be added first, ensuring the dictionary covers the vocabulary learners are most likely to encounter.

## Available corpora and frequency lists

### BCCWJ (Balanced Corpus of Contemporary Written Japanese)
- ~100 million words, balanced across genres (newspapers, books, web, etc.)
- Published by NINJAL (National Institute for Japanese Language and Linguistics)
- Frequency lists derived from BCCWJ are available
- Most authoritative source for modern written Japanese frequency

### Other sources
- **Wikipedia frequency lists** — biased toward encyclopedic/technical vocabulary
- **Subtitle corpora** — better representation of spoken/casual language
- **Web corpora** — large but noisy
- **Textbook vocabulary** — curated for learners but limited scope

## How to use frequency data

### Gap analysis
Compare the top N most frequent Japanese words against existing entries:
- Which frequent words are missing?
- Are any very frequent words still only candidates?
- This identifies the highest-impact additions

### Candidate prioritization
Score candidates by corpus frequency and sort the creation queue accordingly. Higher-frequency candidates should be created first.

### Tier validation
Check whether the basic/core tiers actually contain the most frequent words. If a very common word is in general but a rarer word is in core, that's worth investigating (though the tiers aren't purely frequency-based).

## Current implementation

The `prompts/corpus_harvesting.md` task processes corpus words into candidates, with progress tracked in `corpus_harvesting_next_entry_number.txt`. This is the primary mechanism for frequency-informed expansion.

## Challenges

- Frequency varies dramatically by genre (newspaper vs. fiction vs. web)
- Some very frequent words are function words already well-covered
- Compound words and inflected forms complicate counting
- Proper nouns dominate the top of some frequency lists

## Related pages

- [Corpus Linguistics](../research/corpus-linguistics.md)
- [Vocabulary Tier System](../project/vocabulary-tiers.md)
- [Content Pipeline](../project/content-pipeline.md)
