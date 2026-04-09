# Manual Prompts for Claude Code for the Web

Copy-paste any of these prompts to start a task. Each one tells Claude to read the detailed instructions from the corresponding prompt file.

---

## Dictionary Building Tasks

### Create new entries (from candidates)
```
Read prompts/newentries.md and follow the instructions to create 30 new dictionary entries from candidate_words.json.
```

### Find new candidate words
```
Read prompts/newcandidates.md and follow the instructions to add new candidate words to candidate_words.json.
```

### Harvest candidates from corpus
```
Read prompts/corpus_harvesting.md and follow the instructions to process the next batch of words from the corpus extraction file.
```

### Clean up candidate list
```
Read prompts/clean_up_candidates_list.md and follow the instructions to review and clean candidate_words.json.
```

### Create entries for noentry words
```
Read prompts/polish_add_entries_for_noentry_example_words.md and follow the instructions to create entries for words marked noentry in inline links.
```

---

## Polishing Tasks

### Add inline word links
```
Read prompts/polish_add_inline_links.md and follow the instructions to add cross-reference links to example sentences and notes.
```

### Polish example sentences
```
Read prompts/polish_example_sentences.md and follow the instructions to check and improve example sentence quality.
```

### Check furigana completeness
```
Read prompts/polish_furigana_completeness.md and follow the instructions to check for missing furigana on kanji.
```

### Check furigana correctness
```
Read prompts/polish_furigana_correctness.md and follow the instructions to verify that existing furigana readings are correct.
```

### Check semantic labels
```
Read prompts/polish_semantic_labels.md and follow the instructions to verify semantic tags are accurate.
```

### Expand short notes
```
Read prompts/expand-short-notes.md and follow the instructions to expand the notes field for entries with inadequate notes.
```

### Add aspect/ている notes to verbs
```
Read prompts/polish_aspect_notes.md and follow the instructions to add ている documentation to verb entries with non-obvious aspect behavior.
```

---

## Project Health & Planning

### Get task recommendations
```
Run python3 pipeline/recommend-tasks.py and show me the output. This tells us what the dictionary needs most right now.
```

### Run health dashboard
```
Run make report and show me the output. This gives an overview of dictionary statistics and quality metrics.
```

### Validate all entries
```
Run make validate and show me the results.
```

### Full site build
```
Run make build to validate entries, update indexes, and rebuild the static site.
```

### Incremental site build
```
Run make quick to validate entries, update indexes, and rebuild only changed entries.
```

### Check project context
```
Read PROJECT_CONTEXT_BRIEF.md and summarize the current state of the dictionary.
```

### Audit vocabulary tiers
```
Read prompts/audit_vocabulary_tiers.md and follow the instructions to review vocabulary tier assignments and produce a reassessment report.
```

### Consolidate entries (merge duplicates/variants)
```
Read prompts/consolidate_entries.md and follow the instructions to find and merge duplicate or variant entries.
```

### Add cross-references
```
Read prompts/add_cross-references.md and follow the instructions to systematically review and add cross-references to entries.
```

### Fix duplicate numeric IDs
```
Read prompts/fix_duplicate_ids.md and follow the instructions to resolve entries sharing the same 5-digit numeric ID.
```

---

## Knowledge Base

### Maintain project knowledge base
```
Read planning/maintain-knowledge-base.md and follow the instructions to maintain and improve the project knowledge base wiki.
```

---

## Maintenance & Review

### Review a specific entry
```
Read the entry file for [WORD] (use python3 build/check_duplicate.py "WORD" "READING" to find it) and evaluate its quality against the entry-guidelines skill. Suggest improvements if needed.
```

### Check for duplicates
```
Run python3 build/check_duplicate.py "WORD" "READING" to check whether a word already exists in the dictionary or candidate list.
```

### Verify furigana for one entry
```
Run python3 build/verify_furigana.py ENTRY_ID and show me the results.
```

### Update indexes after manual edits
```
Run python3 build/update_indexes.py to sync entries_index.json, candidate_words.json, and the word lookup table.
```

---

## Enhancement Plan

The enhancement plan is a phased, long-term improvement initiative. Each prompt below is a one-time implementation session that builds tooling, creates new polishing prompts, or improves infrastructure. See `enhancement/prompts/README.md` for the full guide, dependency graph, and sequencing.

### Phase 1: Foundation
```
Read enhancement/prompts/01_infrastructure_quick_wins.md and follow the instructions to implement the infrastructure improvements.
```
```
Read enhancement/prompts/02_verb_transitivity_tooling.md and follow the instructions to build the verb transitivity detection script and polishing prompt.
```
```
Read enhancement/prompts/03_aspect_teiru_tooling.md and follow the instructions to create the aspect/ている polishing prompt.
```

### Phase 2: Quality Systems
```
Read enhancement/prompts/04_note_quality_system.md and follow the instructions to define POS note templates and build the note quality scorer.
```
```
Read enhancement/prompts/05_cross_ref_symmetry.md and follow the instructions to build cross-reference symmetry detection and update the polishing prompt for cluster-mode processing.
```
```
Read enhancement/prompts/06_polishing_priority.md and follow the instructions to build the polishing priority system and update polishing prompts to use priority queues.
```

### Phase 3: Content Strategy
```
Read enhancement/prompts/07_semantic_field_audit.md and follow the instructions to define semantic fields and build the coverage audit system.
```
```
Read enhancement/prompts/08_scenario_gap_analysis.md and follow the instructions to define learner scenarios and build gap analysis tools.
```
```
Read enhancement/prompts/09_vocab_tier_reassessment.md and follow the instructions to create the vocabulary tier reassessment prompt and run the initial audit.
```

### Phase 4: Infrastructure & Quality Tools
```
Read enhancement/prompts/10_consistency_and_dashboard.md and follow the instructions to build the consistency checker and enhance the report dashboard.
```
```
Read enhancement/prompts/11_parallel_safe_redesign.md and follow the instructions to redesign prompts for parallel-safe execution.
```

### Phase 5: Advanced Systems
```
Read enhancement/prompts/12_multi_model_review_p1.md and follow the instructions to build the multi-model review runner and run the Phase 1 calibration.
```
```
Read enhancement/prompts/13_task_queue_system.md and follow the instructions to build the claim-based task queue for parallel agent processing.
```
```
Read enhancement/prompts/14_multi_model_review_p2.md and follow the instructions to scale the multi-model review to the full dictionary.
```

### Phase 6: Long-Term Projects
```
Read enhancement/prompts/15_expository_articles.md and follow the instructions to design the article system and create the pilot articles.
```
```
Read enhancement/prompts/16_automated_orchestration.md and follow the instructions to build the automated orchestration system.
```

---

## Notes

- **One task per session** works best for polishing tasks — they use context tracking files to resume across sessions.
- **Entry creation** can be done in batches of 30 per session (the default).
- After any task that modifies entries, always run `make build` or `make quick` before finishing.
- The polishing tasks track progress in `polishing/tasks/{task-name}/progress.txt` — they automatically pick up where the previous session left off.
- **Enhancement prompts** are one-time implementation sessions. After running an enhancement prompt that creates a new polishing prompt, use the new polishing prompt's metaprompt for ongoing work.
