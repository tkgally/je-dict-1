# Enhancement Plan Implementation Prompts

This directory contains step-by-step implementation prompts for the [Comprehensive Enhancement Plan](../enhancement-plan-2026-04-09.md). Each prompt is designed to be given to Claude Code for autonomous execution through to merge.

## How to Use

1. Give Claude Code the **metaprompt** for the next item in sequence
2. Claude reads the detailed prompt file and executes it autonomously
3. Each prompt ends with validation, commit, push, PR, CI, squash-merge, and cleanup
4. Move to the next prompt in the sequence

**Important**: Follow the sequence below. Some prompts depend on artifacts created by earlier ones. Dependencies are noted for each prompt.

---

## Phase 1: Foundation (No Dependencies)

These prompts have no prerequisites and can be run in any order within the phase.

### 01 — Infrastructure Quick Wins
**Plan sections**: [2.1.1] Auto-refresh BRIEF + [2.1.3] Session continuity + [2.3.1] Incremental validation
**Creates**: CI workflow update, session resume prompt, `--changed-only` flag for validate.py
**Estimated scope**: Small — config and script modifications

```
Read enhancement/prompts/01_infrastructure_quick_wins.md and follow the instructions to implement the infrastructure improvements.
```

### 02 — Verb Transitivity Tooling
**Plan section**: [1.1.1] Verb Transitivity Completion Campaign
**Creates**: `build/find_missing_transitivity.py`, `prompts/polish_verb_transitivity.md`, progress tracking
**Estimated scope**: Medium — new script + new polishing prompt

```
Read enhancement/prompts/02_verb_transitivity_tooling.md and follow the instructions to build the verb transitivity detection script and polishing prompt.
```

### 03 — Aspect/ている Documentation Tooling
**Plan section**: [1.2.3] Aspect/ている Documentation
**Creates**: `prompts/polish_aspect_notes.md`, progress tracking, verb-entry skill update
**Estimated scope**: Small — new polishing prompt

```
Read enhancement/prompts/03_aspect_teiru_tooling.md and follow the instructions to create the aspect/ている polishing prompt.
```

---

## Phase 2: Quality Measurement Systems (Builds on Phase 1)

### 04 — Note Quality System
**Plan section**: [1.1.2] Note Quality Standardization
**Creates**: POS note templates, `build/score_note_quality.py`, vocabulary-notes skill update
**Depends on**: None (but benefits Phase 2 prompt 06)
**Estimated scope**: Medium — template design + new scoring script

```
Read enhancement/prompts/04_note_quality_system.md and follow the instructions to define POS note templates and build the note quality scorer.
```

### 05 — Cross-Reference Symmetry
**Plan section**: [1.1.3] Cross-Reference Completeness & Symmetry
**Creates**: Extended `find_merge_candidates.py`, cluster-mode cross-reference prompt update
**Depends on**: None
**Estimated scope**: Medium — extend existing script + modify polishing prompt

```
Read enhancement/prompts/05_cross_ref_symmetry.md and follow the instructions to build cross-reference symmetry detection and update the polishing prompt for cluster-mode processing.
```

### 06 — Polishing Priority System
**Plan section**: [2.1.2] Polishing Priority Reordering
**Creates**: `build/prioritize_polishing.py`, modified polishing prompts
**Depends on**: Prompt 04 (note scorer provides one input dimension)
**Estimated scope**: Medium — new script + prompt modifications

```
Read enhancement/prompts/06_polishing_priority.md and follow the instructions to build the polishing priority system and update polishing prompts to use priority queues.
```

---

## Phase 3: Content Strategy

### 07 — Semantic Field Audit
**Plan section**: [1.3.1] Semantic Field Audit System
**Creates**: Semantic field definitions, `build/audit_semantic_field.py`, candidate pipeline integration
**Depends on**: None
**Estimated scope**: Medium — field definitions + new audit script

```
Read enhancement/prompts/07_semantic_field_audit.md and follow the instructions to define semantic fields and build the coverage audit system.
```

### 08 — Scenario-Based Gap Analysis
**Plan section**: [1.3.2] Scenario-Based Gap Analysis
**Creates**: Scenario definitions, gap analysis tooling
**Depends on**: Prompt 07 (complementary system, shares infrastructure patterns)
**Estimated scope**: Medium — scenario definitions + analysis tools

```
Read enhancement/prompts/08_scenario_gap_analysis.md and follow the instructions to define learner scenarios and build gap analysis tools.
```

### 09 — Vocabulary Tier Reassessment
**Plan section**: [1.2.2] Vocabulary Tier Reassessment
**Creates**: Tier audit prompt, reassessment report
**Depends on**: None
**Estimated scope**: Small — audit prompt (produces report, not automatic changes)

```
Read enhancement/prompts/09_vocab_tier_reassessment.md and follow the instructions to create the vocabulary tier reassessment prompt and run the initial audit.
```

---

## Phase 4: Infrastructure & Quality Tools

### 10 — Consistency Checker & Enhanced Dashboard
**Plan sections**: [2.3.2] Consistency Checker + [2.3.3] Enhanced Dashboard
**Creates**: `build/check_consistency.py`, extended `report.py`
**Depends on**: Prompt 04 (note scorer feeds consistency checker)
**Estimated scope**: Medium — two script enhancements

```
Read enhancement/prompts/10_consistency_and_dashboard.md and follow the instructions to build the consistency checker and enhance the report dashboard.
```

### 11 — Parallel-Safe Prompt Redesign
**Plan section**: [2.2.1] Parallel-Safe Prompt Redesign
**Creates**: Modified prompts with ID range parameters, entry-level locking, deferred shared file updates
**Depends on**: None (but benefits from all earlier prompt work)
**Estimated scope**: Medium — prompt modifications + locking mechanism

```
Read enhancement/prompts/11_parallel_safe_redesign.md and follow the instructions to redesign prompts for parallel-safe execution.
```

---

## Phase 5: Advanced Systems

### 12 — Multi-Model Review Phase 1
**Plan section**: [1.2.1] Multi-Model Proofreading, Phase 1
**Creates**: `build/review_runner.py`, review prompt format, calibration results
**Depends on**: None (but requires OpenRouter API access)
**Estimated scope**: Large — API integration + calibration
**Prerequisites**: OpenRouter API key must be available

```
Read enhancement/prompts/12_multi_model_review_p1.md and follow the instructions to build the multi-model review runner and run the Phase 1 calibration.
```

### 13 — Claim-Based Task Queue
**Plan section**: [2.2.2] Claim-Based Task Queue
**Creates**: `pipeline/task_queue.py`, task-typed prompt modifications
**Depends on**: Prompt 11 (parallel-safe prompts)
**Estimated scope**: Medium — new queue system + prompt modifications

```
Read enhancement/prompts/13_task_queue_system.md and follow the instructions to build the claim-based task queue for parallel agent processing.
```

### 14 — Multi-Model Review Phase 2-3
**Plan section**: [1.2.1] Multi-Model Proofreading, Phases 2-3
**Creates**: Two-pass pipeline, `prompts/polish_cross_model_review.md`, CI integration
**Depends on**: Prompt 12 (Phase 1 calibration must be complete and successful)
**Estimated scope**: Large — scaling pipeline + new polishing prompt

```
Read enhancement/prompts/14_multi_model_review_p2.md and follow the instructions to scale the multi-model review to the full dictionary.
```

---

## Phase 6: Long-Term Projects

### 15 — Expository Articles Pilot
**Plan section**: [1.3.3] Expository Articles
**Creates**: Article schema, build system integration, 3 pilot articles
**Depends on**: None (standalone feature)
**Estimated scope**: Large — schema + build changes + content

```
Read enhancement/prompts/15_expository_articles.md and follow the instructions to design the article system and create the pilot articles.
```

### 16 — Automated Orchestration
**Plan section**: [2.2.3] Automated Orchestration
**Creates**: Extended pipeline config, orchestrator script, monitoring dashboard
**Depends on**: Prompt 13 (task queue must be operational)
**Estimated scope**: Large — orchestrator + monitoring

```
Read enhancement/prompts/16_automated_orchestration.md and follow the instructions to build the automated orchestration system.
```

---

## Repeatable Polishing Prompts

These prompts are **created** by the implementation prompts above. After the corresponding implementation prompt has been merged, use these metaprompts to run the polishing task repeatedly:

### Verb Transitivity Polishing (created by Prompt 02)
```
Read prompts/polish_verb_transitivity.md and follow the instructions to add transitivity information to verb entries.
```

### Aspect/ている Polishing (created by Prompt 03)
```
Read prompts/polish_aspect_notes.md and follow the instructions to add ている documentation to verb entries.
```

### Cross-Model Review Polishing (created by Prompt 14)
```
Read prompts/polish_cross_model_review.md and follow the instructions to process multi-model review results.
```

---

## Dependency Graph

```
Phase 1 (no deps)          Phase 2                Phase 3         Phase 4         Phase 5/6
                                                                                  
01 Infrastructure ────────────────────────────────────────────────────────────────────────────
02 Verb Transit. ──→ (polish_verb_transitivity.md available)                                  
03 Aspect/ている ──→ (polish_aspect_notes.md available)                                      
                        04 Note Quality ──→ 06 Priority ──→ 10 Consistency                    
                        05 Cross-Ref Sym ────────────────────────────────────────              
                                            07 Semantic ──→ 08 Scenarios                      
                                            09 Vocab Tiers                                    
                                                             11 Parallel ──→ 13 Task Queue ──→ 16 Orchestration
                                                             12 Multi-Model P1 ──→ 14 Multi-Model P2-3
                                                                                  15 Articles  
```

## Notes

- **Session length**: Each implementation prompt is designed for a single Claude Code session
- **Build artifacts**: Every prompt includes `make build` and commits `docs/` — the live site updates with each merge
- **Polishing prompts**: Created by implementation prompts, these are run repeatedly over many sessions
- **Flexibility**: Prompts within the same phase can generally be reordered. Cross-phase dependencies are noted above.
- **Pausing**: You can pause between any two prompts. The enhancement plan is additive — each prompt leaves the project in a fully working state.
