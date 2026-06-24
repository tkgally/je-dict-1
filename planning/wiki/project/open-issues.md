# Open Issues

**Last updated**: 2026-06-24 (candidate-pool quality: seen-in-entry lane now drained to 0, both candidate lanes exhausted, curator restock raised in priority; new junk families — place-name misglosses, niche jargon, coinages)

A running list of known problems, design questions, and unresolved edge cases. Items here are candidates for future work sessions or discussion.

## Content issues

### Incomplete transitivity marking
Many verb entries, especially older ones, lack 自動詞/他動詞 labels and paired verb cross-references. The `polish_semantic_labels.md` task addresses this incrementally, but coverage is still incomplete.

### Inconsistent note quality
Entries created before v2 standards often have brief, unstructured notes (single paragraph, no headers, inline lists). The `expand-short-notes.md` task works through these, but thousands remain.

### Missing cross-references
Many semantically related entries aren't linked. The `add_cross-references.md` task and `find_merge_candidates.py` tool help, but systematic coverage would require reviewing all entries.

### Candidate list quality
`candidate_words.json` (~1,232 candidates as of 2026-06-24) contains a high fraction of
low-quality corpus-harvest noise:
- Duplicates of existing entries (variant readings)
- Bare numeral + counter forms (二百, 三歳, 三桁/四桁/五桁) and single-suffix productive
  derivations (〜化, 〜性, 〜率, 〜器) — compositional, not lexical
- Place names, proper nouns, and non-Japanese transcriptions (スポンジボブ); **place-name
  readings mis-glossed as common words** (尾張 おわり glossed "end, finish"; 三重 みえ glossed
  "triple")
- Niche technical jargon (尾椎, 腋窩, 網点, 受水槽)
- Transcription typos / errors and coinages / non-words (怒燥 for 怒涛; アンパッサン glossed
  "ice cream sundae" — actually *en passant*; 権使, 個尊, 些道, 解退, 自紹介)
- Too obscure for intermediate learners; compounds better handled as collocations

**Quantified and recurring (2026-06-17/18 new-entries runs)**: across the oldest ~160
candidates and mid-range samples, **fewer than ~10%** are well-formed standalone learner
vocabulary. The only consistently good candidates are the recent **"seen in entry"**
additions. The practical impact is that `new-entries` Routine runs find few genuinely
useful headwords beyond the seen-in-entry set and are forced to under-produce against
their ~20 target rather than pad from junk.

**Update (2026-06-24): the seen-in-entry safety lane is now empty.** The 2026-06-24
new-entries run reported the selector's `seen_in_entry_count` at **0** — the high-quality
seen-in-entry pool that the last several runs leaned on has been fully drained, while the
2026-06-23 run independently found nearly every common, dictionary-worthy *base* word in the
remaining pool (曖昧, 無難, ぎこちない, 巧み, 速やか, 仲良し, 無邪気…) **already exists as an
entry**. So both lanes are now exhausted: the seen-in-entry inflow is the only reliable
source of quality candidates and it has dried up. Without a curator restock, the next
new-entries run is forced to mine transparent compositional compounds (排水処理, 工業製品,
短距離ミサイル) — explicitly out of scope for a learner headword. This raises the priority of
fix (1) (curator restock) ahead of the next `new-entries`-mode Routine run. **Two complementary fixes**: (1) curator
restock with vetted, common, learner-relevant words (human side); (2) a mechanical
pre-filter in `manage_candidates.py` / corpus harvesting that rejects the predictable
junk families (see [Tooling Backlog](../ideas/tooling-backlog.md) → item 23) so the pool
doesn't re-accumulate noise after a restock. Periodic cleanup
(`clean_up_candidates_list.md`) addresses the existing backlog.

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

### Words with multiple written forms
Many words can be written in different kanji, with different okurigana, or in kanji vs. kana. No systematic policy exists for when variants get separate entries vs. being listed in `alternate_forms`, and the search index doesn't always find entries via variant forms. See [Word Variants](../topics/word-variants.md) for detailed analysis and proposed policies.

### Cross-entry consistency
Entries of the same type (e.g., all transitive verbs, all color terms) present information in different ways — different note structures, different depth, different coverage of standard sections. As the dictionary matures, greater consistency would improve the user experience and make entries easier to maintain. See [Entry Consistency](../topics/entry-consistency.md).

### Compound verb representation
Should compound verbs (V1 + V2, like 食べ始める) get their own entries, or should they be documented as patterns under the component verbs? Current practice is inconsistent.

### Proper names and encyclopedic entries
The dictionary currently excludes proper names (place names, personal names, organization names) and encyclopedic content. Eventually these should be added, but the current entry schema — optimized for vocabulary with example sentences, collocations, and contrastive notes — doesn't fit well. A different entry format with lighter example requirements and encyclopedic notes may be needed. See [Dictionary Growth and Long-Term Vision](../ideas/dictionary-growth.md).

### Expression boundary
Where does "vocabulary" end and "grammar" begin? Entries for expressions like ～ている, ～てしまう, ～ことができる blur the line. Current approach includes common expressions but avoids pure grammar patterns.

### Expository articles
The dictionary could benefit from standalone articles on vocabulary topics too broad for any single entry's notes (e.g., the counter system, keigo, onomatopoeia families). These would serve the goal of making the dictionary more useful for browsing. See [Expository Articles](../ideas/expository-articles.md).

## Technical issues

### Search limitations
Client-side search works but has limits:
- No fuzzy matching for typos
- Limited support for searching by English definition
- No support for searching by kanji component
- Performance may degrade as entry count grows

### Audio coverage
The dictionary currently has no audio files. An earlier experiment with human-recorded audio for ~1,028 entries was discontinued in early 2026. Adding pronunciation audio remains a desirable goal, but requires a scalable generation strategy — likely TTS-based. See [Audio Coverage Expansion](../ideas/audio-expansion.md).

### Mobile experience
The static site works on mobile but wasn't designed mobile-first. Navigation, search, and long entry pages could be improved for small screens.

## Process issues

### Stale tracking files
`PROJECT_CONTEXT_BRIEF.md` counts are manually updated and often lag behind actual counts. The instruction to always run `get_next_id.py` helps, but other counts can mislead.

### Session continuity
Each LLM session starts fresh. While `PROJECT_STATUS.md` and polishing progress files help, complex multi-session tasks can lose context. This knowledge base is partly designed to address this.

### Sequential processing bottleneck
All maintenance tasks run sequentially — one session at a time, one task at a time. This limits throughput to ~30 entries per session for creation, ~20 entries per session for polishing. Parallel execution would multiply throughput but requires solving file conflict problems. See [Parallel Agent Architecture](../ideas/parallel-agent-architecture.md).

### Single-model quality risk
All content has been written and reviewed by Claude. While quality is generally high, systematic verification by other frontier models would catch model-specific blind spots. A cross-model proofreading system is planned. See [Multi-Model Proofreading](../ideas/multi-model-proofreading.md).

## Related pages

- [Quality Standards](quality-standards.md)
- [AI-Assisted Entry Review](../ideas/ai-review.md)
- [Multi-Model Proofreading](../ideas/multi-model-proofreading.md)
- [Parallel Agent Architecture](../ideas/parallel-agent-architecture.md)
- [Entry Consistency](../topics/entry-consistency.md)
- [Word Variants](../topics/word-variants.md)
- [Expository Articles](../ideas/expository-articles.md)
- [Audio Coverage Expansion](../ideas/audio-expansion.md)
- [Word Discovery Strategies](../ideas/word-discovery-strategies.md)
- [Dictionary Growth and Long-Term Vision](../ideas/dictionary-growth.md)
