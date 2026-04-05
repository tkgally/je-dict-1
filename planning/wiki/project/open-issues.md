# Open Issues

**Last updated**: 2026-04-05

A running list of known problems, design questions, and unresolved edge cases. Items here are candidates for future work sessions or discussion.

## Content issues

### Incomplete transitivity marking
Many verb entries, especially older ones, lack 自動詞/他動詞 labels and paired verb cross-references. The `polish_semantic_labels.md` task addresses this incrementally, but coverage is still incomplete.

### Inconsistent note quality
Entries created before v2 standards often have brief, unstructured notes (single paragraph, no headers, inline lists). The `expand-short-notes.md` task works through these, but thousands remain.

### Missing cross-references
Many semantically related entries aren't linked. The `add_cross-references.md` task and `find_merge_candidates.py` tool help, but systematic coverage would require reviewing all entries.

### Candidate list quality
`candidate_words.json` contains ~5,400 candidates, but some are:
- Duplicates of existing entries (variant readings)
- Too obscure for intermediate learners
- Compound words better handled as collocations in existing entries
Periodic cleanup (`clean_up_candidates_list.md`) addresses this.

## Design questions

### Should the general tier have sub-bands?
The general tier spans from common everyday words to rare specialized terms. Sub-bands (e.g., "common general" vs. "specialized general") could help users and guide expansion priorities. But it adds complexity.

### How to handle loanwords consistently?
Katakana loanwords raise questions:
- When to include the English origin word?
- How to handle words with both katakana and kanji forms?
- Should very common English words (like "computer") get cultural notes about Japanese usage differences?

### Homograph disambiguation
Some words share identical writing but have different readings and meanings (e.g., 生 with multiple readings). Current approach is separate entries with cross-references, but the search/display experience could be improved.

### Compound verb representation
Should compound verbs (V1 + V2, like 食べ始める) get their own entries, or should they be documented as patterns under the component verbs? Current practice is inconsistent.

### Expression boundary
Where does "vocabulary" end and "grammar" begin? Entries for expressions like ～ている, ～てしまう, ～ことができる blur the line. Current approach includes common expressions but avoids pure grammar patterns.

## Technical issues

### Search limitations
Client-side search works but has limits:
- No fuzzy matching for typos
- Limited support for searching by English definition
- No support for searching by kanji component
- Performance may degrade as entry count grows

### Audio coverage
Only ~1,028 entries have audio files (~5% of total). Expanding this would significantly improve the user experience but requires a scalable audio generation strategy.

### Mobile experience
The static site works on mobile but wasn't designed mobile-first. Navigation, search, and long entry pages could be improved for small screens.

## Process issues

### Stale tracking files
`PROJECT_CONTEXT_BRIEF.md` counts are manually updated and often lag behind actual counts. The instruction to always run `get_next_id.py` helps, but other counts can mislead.

### Session continuity
Each LLM session starts fresh. While `PROJECT_STATUS.md` and polishing progress files help, complex multi-session tasks can lose context. This knowledge base is partly designed to address this.

## Related pages

- [Quality Standards](quality-standards.md)
- [AI-Assisted Entry Review](../ideas/ai-review.md)
- [Audio Coverage Expansion](../ideas/audio-expansion.md)
