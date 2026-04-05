# AI-Assisted Entry Review

**Last updated**: 2026-04-05

## Current state

The dictionary is already LLM-built and maintained. The existing polishing pipeline uses LLMs to systematically review entries for specific quality dimensions (furigana, examples, notes, etc.). This page considers more ambitious uses of AI for quality improvement.

## Ideas

### Cross-entry consistency checking
Use an LLM to read groups of related entries and check for:
- Inconsistent definitions of the same concept across entries
- Contradictory usage notes
- Missing cross-references between obviously related words
- Inconsistent register labeling for words in the same formality band

### Native speaker simulation
Prompt an LLM to evaluate entries from the perspective of a Japanese native speaker:
- Are the example sentences natural?
- Is the register assessment correct?
- Are there common uses or collocations missing?
- Would a native speaker object to any definition?

### Learner simulation
Prompt an LLM to evaluate entries from the perspective of an intermediate learner:
- Is the definition clear without prior knowledge?
- Are the examples at the right difficulty level?
- Do the notes explain things the learner would actually be confused about?
- Is anything unnecessarily complex?

### Automated comparison with existing dictionaries
Compare je-dict-1 entries against data from:
- JMdict/EDICT (freely available Japanese-English dictionary data)
- Sense coverage comparison
- Missing common definitions
- Identify entries with fewer senses than JMdict

### Batch quality scoring
Run all entries through a quality rubric and rank by score:
- Which entries most need improvement?
- Where are the biggest gaps between current and target quality?
- Prioritize polishing effort on lowest-scoring entries

## Implementation

Most of these could be implemented as batch prompts run via `claude --print`, similar to existing pipeline tasks. Results would be stored as reports or fed into polishing task queues.

## Related pages

- [Quality Standards](../project/quality-standards.md)
- [Content Pipeline](../project/content-pipeline.md)
