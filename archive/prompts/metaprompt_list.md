# Manual Prompts for Claude Code for the Web

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

Copy-paste any of these prompts to start a task. Each one tells Claude to read the detailed instructions from the corresponding prompt file.

---

## Scheduled Routine (default unattended task)

### Unified improvement Routine v2 — schedule THIS
```
Read prompts/routine2.md and follow it end to end as an unattended run: complete the pre-flight, execute the mode the selector picks, then finish the full §7 wrap-up — build if needed, commit, push, create the PR, wait for CI, squash-merge it yourself, and release the lock. If the pre-flight lock is held by another active run, stop quietly.
```

This is the single task to schedule as a Routine (and the default for unattended runs). Each run a deterministic selector picks ONE focus — `polish` (priority lane + frontier), `new-entries`, `accuracy-review`, `wiki`, or `systemic-fix` — by tunable weights with health nudges, follows that mode's prompt, captures candidates/observations, **self-verifies its own entry changes with an independent model**, appends a quality-metrics line, and merges its own PR. It replaces scheduling comprehensive polish, new-entries, and wiki maintenance separately. (It is the only Routine prompt — the superseded v1 `routine.md` was removed 2026-06-11.) Tune the mix in `pipeline/routine-config.json`. Useful checks:

```
python3 pipeline/routine_next.py --explain      # why the next run would pick a given mode
python3 pipeline/routine_next.py --simulate 60  # mode distribution over 60 runs
python3 pipeline/routine_next.py --force-mode polish   # force one mode for manual testing
python3 pipeline/metrics_snapshot.py --mode polish --changed 0 --dry-run  # preview a metrics row
```

The prompts below remain runnable manually for targeted work.

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

### Comprehensive polish (DEFAULT — use this)
```
Read prompts/comprehensive_polish.md and follow the instructions.
```

This is the default ongoing-improvement task. Each session walks through up to 5 entries and applies a tiered checklist that unifies furigana, examples, inline links, cross-references, semantic labels, transitivity, aspect, and notes work. Designed to run repeatedly on a schedule.

### Targeted polish prompts (special-purpose)

The prompts below are kept for occasional focused sweeps. Most ongoing polishing should use `comprehensive_polish.md` instead.

#### Add inline word links
```
Read prompts/polish_add_inline_links.md and follow the instructions to add cross-reference links to example sentences and notes.
```

#### Polish example sentences
```
Read prompts/polish_example_sentences.md and follow the instructions to check and improve example sentence quality.
```

#### Check furigana completeness
```
Read prompts/polish_furigana_completeness.md and follow the instructions to check for missing furigana on kanji.
```

#### Check furigana correctness
```
Read prompts/polish_furigana_correctness.md and follow the instructions to verify that existing furigana readings are correct.
```

#### Check semantic labels
```
Read prompts/polish_semantic_labels.md and follow the instructions to verify semantic tags are accurate.
```

#### Fix semantic tag drift (P11 — detector-driven)
```
Read prompts/fix_semantic_tag_drift.md and follow the instructions to drain the high-precision semantic-tag-drift detectors and the accuracy-review tags pass.
```
Pairs two high-precision `check_tag_drift.py` checks (`proverb-idiom-mismatch`, `concrete-noun-domain-mismatch`) with the cross-model `tags` pass for the cases detectors can't catch. Slots into the Routine as a `systemic-fix` lane (per backlog item) or an `accuracy-review` lane (cursor-driven over the 5700–6340 block). Cursor: `polishing/tasks/semantic-tag-drift/progress.txt`.

#### Expand short notes
```
Read prompts/expand-short-notes.md and follow the instructions to expand the notes field for entries with inadequate notes.
```

#### Add aspect/ている notes to verbs
```
Read prompts/polish_aspect_notes.md and follow the instructions to add ている documentation to verb entries with non-obvious aspect behavior.
```

#### Process multi-model review results
```
Read prompts/polish_cross_model_review.md and follow the instructions to process review results and apply corrections.
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

- **Comprehensive polish** is the default scheduled task. It processes up to 5 entries per session, applying all polish dimensions, and is intended to be run repeatedly on a schedule.
- **One task per session** still applies to the targeted polish prompts — they use context tracking files to resume across sessions.
- **Entry creation** can be done in batches of 30 per session (the default). Candidates with "seen in entry XXXXX" notes are highest priority for new entry sessions, since they fill internal-completeness gaps surfaced during comprehensive polish.
- After any task that modifies entries, always run `make build` or `make quick` before finishing.
- All polishing tasks track progress in `polishing/tasks/{task-name}/progress.txt` — they automatically pick up where the previous session left off.
- **Enhancement prompts** are one-time implementation sessions. After running an enhancement prompt that creates a new polishing prompt, use the new polishing prompt's metaprompt for ongoing work.
