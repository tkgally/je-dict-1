# Corpus-Driven Entry Prioritization

**Last updated**: 2026-06-08

## Concept

Use frequency data from Japanese language corpora to inform which candidate words
to create next — on the principle that the words learners are most likely to
encounter should generally be covered first. This was je-dict-1's *initial*
expansion strategy. It has since been **largely superseded by LLM brainstorming**
as the primary discovery method (see [Word Discovery
Strategies](word-discovery-strategies.md) and [Content
Pipeline](../project/content-pipeline.md)), so this page is best read as
documenting one lever among several — and the reasons the project does **not**
make raw frequency its master sort key.

## Available corpora and frequency lists

### BCCWJ (Balanced Corpus of Contemporary Written Japanese)
- ~100 million words, balanced across genres (newspapers, books, web, etc.)
- Published by NINJAL (National Institute for Japanese Language and Linguistics)
- The most authoritative source for modern *written* Japanese frequency; derived
  frequency lists are available. For the grading detail, see [Japanese Vocabulary
  Grading](../research/japanese-vocabulary-grading.md).

### Other sources
- **Subtitle corpora** — better representation of spoken/casual language
- **Wikipedia / web corpora** — large but biased toward encyclopedic/technical
  vocabulary and noisy
- **Textbook vocabulary** — curated for learners but limited in scope

## Where frequency fits among discovery methods

The project tried frequency-first expansion and moved away from it. The honest
positioning today:

- **Corpus harvesting** (`prompts/corpus_harvesting.md`, progress in
  `corpus_harvesting_next_entry_number.txt`) still exists and is frequency-ordered,
  but it is an *earlier* approach now mostly replaced. Its weaknesses in practice:
  proper nouns, inflected forms, and function words dominate the top of raw lists,
  producing many false positives that need manual curation.
- **LLM brainstorming** (primary) radiates from existing entries across seven
  relation types. Its known blind spot is precisely the one frequency data
  covers: it carries **no frequency signal**, so a rare literary word and an
  everyday word are suggested with equal weight. This is the strongest remaining
  argument for keeping a frequency lever in the mix — as a *re-ranking* and
  *sanity-check* layer over brainstormed candidates rather than as the generator.
- **"Seen in entry" internal-completeness candidates** — words already referenced
  inside existing entries but lacking their own entry — are, as of mid-2026, one
  of the most productive sources of new entries. This is a frequency-independent
  signal (a word's importance is inferred from its use *within the dictionary*),
  and it is what most recent creation batches actually draw from.

## Frequency-independent gap analysis

The "gap analysis" idea — find high-value missing words — does not require a
frequency list at all. The project's actual systematic gap-finding tools are
coverage audits against curated targets:

- **Semantic-field coverage** (`audit_semantic_field.py`, `make audit-fields`)
  checks the dictionary against per-category word lists and can add missing words
  as candidates.
- **Scenario gap analysis** (`analyze_scenarios.py`, `make audit-scenarios`)
  starts from learner *situations* (visiting a doctor, renting an apartment,
  attending a wedding) and surfaces the highest-impact missing vocabulary.

These give a frequency-like "cover the important things first" effect while
sidestepping the genre-bias and proper-noun problems of raw corpus counts.

## Where frequency still earns its keep

- **Tier validation.** Check whether the (closed) basic/core tiers actually
  contain the most frequent words; a very common word stuck in *general* while a
  rarer word sits in *core* is worth investigating — though the tiers are
  deliberately **not** purely frequency-based (see [Vocabulary Tier
  System](../project/vocabulary-tiers.md)).
- **Candidate re-ranking.** Scoring an existing candidate queue by corpus
  frequency is a cheap way to push everyday words ahead of rare ones without
  changing how candidates are *discovered*.

## Challenges (why frequency is a lever, not the master)

- Frequency varies dramatically by genre (newspaper vs. fiction vs. web).
- Many of the most frequent items are function words already well covered.
- Compound words and inflected forms complicate counting (the word-family unit
  problem — see [Japanese Vocabulary
  Grading](../research/japanese-vocabulary-grading.md)).
- Proper nouns dominate the top of some lists.

## Related pages

- [Word Discovery Strategies](word-discovery-strategies.md) — the full comparison of discovery methods; frequency harvesting in context
- [Corpus Linguistics](../research/corpus-linguistics.md) — frequency data, corpora, and word selection
- [Japanese Vocabulary Grading](../research/japanese-vocabulary-grading.md) — BCCWJ frequency data and the word-counting-unit problem
- [Vocabulary Size and Text Coverage](../research/vocabulary-size-coverage.md) — the coverage thresholds that motivate prioritization
- [Vocabulary Tier System](../project/vocabulary-tiers.md) · [Content Pipeline](../project/content-pipeline.md)
