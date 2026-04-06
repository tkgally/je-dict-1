# AI-Assisted Entry Review

**Last updated**: 2026-04-06

## Current state

The dictionary is already LLM-built and maintained. The existing polishing pipeline uses LLMs to systematically review entries for specific quality dimensions (furigana, examples, notes, etc.). This page considers more ambitious uses of AI for quality improvement. For the specific plan to use multiple frontier models for proofreading via OpenRouter, see [Multi-Model Proofreading](multi-model-proofreading.md).

## Review strategies

### Cross-entry consistency checking
Use an LLM to read groups of related entries and check for:
- Inconsistent definitions of the same concept across entries
- Contradictory usage notes
- Missing cross-references between obviously related words
- Inconsistent register labeling for words in the same formality band

See also [Entry Consistency](../topics/entry-consistency.md) for the broader consistency framework including cluster-based review.

### Native speaker simulation
Prompt an LLM to evaluate entries from the perspective of a Japanese native speaker:
- Are the example sentences natural?
- Is the register assessment correct?
- Are there common uses or collocations missing?
- Would a native speaker object to any definition?

This is particularly valuable when done by models other than the one that created the entry (see [Multi-Model Proofreading](multi-model-proofreading.md)), since the creating model is less likely to catch its own errors.

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

## Implementation approaches

### Current: Sequential polishing prompts
Most review currently happens through dedicated polishing prompts (`polish_*.md`) that process entries sequentially, one dimension at a time. This works but is slow.

### Near-term: Multi-model review via OpenRouter
The [Multi-Model Proofreading](multi-model-proofreading.md) page details a two-pass system using OpenRouter to access GPT, Gemini, and other models for systematic review. This is the curator's highest-priority review initiative.

### Medium-term: Parallel review agents
The [Parallel Agent Architecture](parallel-agent-architecture.md) would enable multiple review agents to run simultaneously, each handling different entry ranges or review dimensions. This would multiply review throughput.

### Long-term: Continuous autonomous review
In the full autonomous system, review agents would run continuously, processing new entries shortly after creation and periodically re-reviewing older entries as quality standards and model capabilities evolve.

## Related pages

- [Multi-Model Proofreading](multi-model-proofreading.md) — detailed plan for cross-model proofreading via OpenRouter
- [Parallel Agent Architecture](parallel-agent-architecture.md) — running review agents in parallel
- [Entry Consistency](../topics/entry-consistency.md) — consistency as a specific review dimension
- [Quality Standards](../project/quality-standards.md)
- [Content Pipeline](../project/content-pipeline.md)
- [LLMs as Lexicographic Corpus Replacements](../topics/llms-replacing-corpora.md) — broader context for LLM use in dictionary production
- [Beyond Flat Corpora](../research/beyond-flat-corpora.md) — semantic-pragmatic analysis capabilities
- [Deterministic vs. Semantic Tasks](../topics/deterministic-vs-semantic-tasks.md) — taxonomy of which tasks can be automated and which cannot
