# How to Use the Enhancement Infrastructure

This guide explains how to operate the je-dict-1 dictionary project now that all 16 enhancement phases are complete. It covers the day-to-day prompts you give Claude, the tools available to you, and the recommended workflows.

## Quick Summary

The enhancement project built three categories of things:

1. **Quality measurement tools** -- scripts that analyze the dictionary and tell you what needs work
2. **Polishing prompts** -- self-contained task prompts that Claude follows to fix specific quality issues
3. **Scalability infrastructure** -- parallel execution, task queues, and orchestration for running multiple sessions

You don't need to re-run any of the enhancement prompts (01-16). Those were one-time implementation sessions. What you use going forward are the tools and prompts they created.

---

## Starting a Session

Every Claude Code session should begin the same way. Copy-paste this:

```
Run python3 pipeline/update-brief.py, then read PROJECT_CONTEXT_BRIEF.md and give me a quick status summary.
```

This refreshes the counts and gives Claude (and you) an accurate picture of the dictionary's current state.

---

## The Core Loop: Building the Dictionary

The dictionary grows through two activities: **adding new entries** and **polishing existing entries**. Here's how to do each.

### Adding New Entries

**Step 1: Find candidate words** (if the candidate list is running low)
```
Read prompts/newcandidates.md and follow the instructions to add new candidate words to candidate_words.json.
```

**Step 2: Create entries from candidates** (the main entry-creation prompt)
```
Read prompts/newentries.md and follow the instructions to create 30 new dictionary entries from candidate_words.json.
```

Each session creates ~30 entries, validates them, builds the site, and merges to main.

### Polishing Existing Entries

Polishing prompts improve entries that already exist. Each one tracks its progress automatically -- it picks up where the last session left off. Just give the prompt and Claude handles the rest.

**The polishing prompts, roughly in order of impact:**

| Prompt | What it does |
|--------|-------------|
| `prompts/expand-short-notes.md` | Expands entries with thin or missing notes |
| `prompts/polish_example_sentences.md` | Fixes example count, quality, vocabulary tier |
| `prompts/polish_furigana_completeness.md` | Adds missing furigana to kanji |
| `prompts/polish_furigana_correctness.md` | Verifies existing furigana readings |
| `prompts/polish_add_inline_links.md` | Adds cross-reference links in examples/notes |
| `prompts/add_cross-references.md` | Adds `prominent_see_also` and `cross_references` |
| `prompts/polish_verb_transitivity.md` | Adds transitivity info to verb entries |
| `prompts/polish_aspect_notes.md` | Documents non-obvious aspect behavior |
| `prompts/polish_semantic_labels.md` | Verifies semantic tags match meanings |
| `prompts/polish_cross_model_review.md` | Processes multi-model review results (requires reviews to exist) |

**How to run any polishing task:**
```
Read prompts/polish_furigana_completeness.md and follow the instructions.
```

Replace the filename with whichever task you want. That's it -- the prompt contains all the instructions Claude needs.

### Consolidation

Over time, duplicate or near-duplicate entries accumulate. Run this periodically:
```
Read prompts/consolidate_entries.md and follow the instructions to find and merge duplicate or variant entries.
```

---

## Figuring Out What to Work On

The enhancement project built several analysis tools to help you decide what needs attention. You don't need to memorize flags -- just ask Claude to run them.

### Health Dashboard
```
Run make report and summarize the results.
```
Shows entry counts, quality metrics, polishing progress, consistency issues.

### Note Quality Scores
```
Run python3 build/score_note_quality.py --summary and show me the results.
```
Shows the distribution of note quality scores. Use `--below 30` to see the worst entries.

### Consistency Checker
```
Run make consistency and summarize the results.
```
Finds structural issues: missing collocations, asymmetric cross-references, note problems.

### Semantic Field Coverage
```
Run make audit-fields and summarize which fields have the worst coverage.
```
Shows which semantic domains (body parts, colors, daily life, etc.) have vocabulary gaps.

### Scenario Coverage
```
Run python3 build/analyze_scenarios.py --top-gaps 20 and show me the highest-impact missing words.
```
Shows which words learners would need most but the dictionary doesn't have yet.

### Vocabulary Tier Audit
```
Run make audit-tiers and show me any outliers.
```
Flags potential tier misclassifications (e.g., specialized words in the basic tier).

### Polishing Priority Lists
```
Run make priorities and show me a summary.
```
Regenerates priority-ordered lists so polishing tasks process the worst entries first.

---

## Running Parallel Sessions

The enhancement project added infrastructure for running 2+ Claude sessions simultaneously on non-overlapping entry ranges.

### Manual Parallel Sessions

This is the simplest approach. Open two Claude Code sessions (two browser tabs, two terminal windows, etc.) and give each one a range:

**Session 1:**
```
Read prompts/polish_furigana_completeness.md and follow the instructions. Process entries 00000-10999 only.
```

**Session 2:**
```
Read prompts/polish_furigana_completeness.md and follow the instructions. Process entries 11000-22999 only.
```

Each session creates its own branch. After both finish, merge them:
```
Run python3 build/parallel_coordinator.py branch1 branch2 to merge the parallel session results.
```

### Task Queue (for more sessions)

For 3+ parallel sessions, the task queue prevents conflicts automatically:

**Step 1: Populate the queue**
```
Run python3 pipeline/task_queue.py populate --all to scan all entries and create tasks.
```

**Step 2: Give each session the queue-based prompt**
```
Read prompts/queue_polishing_template.md and follow the instructions for the "furigana" task type.
```

Each session claims tasks from the queue, processes them, and marks them complete. No overlap possible.

### Automated Orchestration

The orchestrator can launch and monitor parallel sessions automatically:

```
Run python3 pipeline/orchestrator.py start --dry-run to see what it would do.
```

If the dry run looks good:
```
Run python3 pipeline/orchestrator.py start to begin orchestration.
```

Monitor with:
```
Run python3 pipeline/monitor.py to see real-time status.
```

Budget caps in `pipeline/budget.json` prevent runaway spending. The circuit breaker pauses after 3 consecutive failures.

**Note:** The orchestrator requires `claude` CLI to be available in PATH and uses git worktrees for isolation. Each session runs in its own worktree so multiple sessions can operate concurrently without git conflicts.

---

## Multi-Model Review (Furigana Verification)

This uses external AI models via OpenRouter to cross-check furigana correctness. Requires an `OPENROUTER_API_KEY` environment variable.

**Screening pass** (cheap, catches obvious issues):
```
Run python3 build/review_runner.py --pass screening --range 1 1000 and show me the results.
```

**Deep review** (thorough, on flagged entries only):
```
Run python3 build/review_runner.py --pass deep and show me the results.
```

**Process the results:**
```
Read prompts/polish_cross_model_review.md and follow the instructions.
```

---

## Expository Articles

Three pilot articles exist in `articles/`: counters, keigo, and onomatopoeia. These are built automatically by `make build` and appear at `/articles/` on the live site.

To add a new article, create a JSON file in `articles/` following the schema in `build/article_schema.json`. The build system picks it up automatically.

---

## Maintenance Checklist

Run these periodically (weekly or after large batches of changes):

| Task | Command |
|------|---------|
| Rebuild priority lists | `make priorities` |
| Check consistency | `make consistency` |
| Check cross-ref symmetry | `make check-symmetry` |
| Check semantic clusters | `make check-clusters` |
| Reassemble semantic fields | `make assemble-fields` (after editing category files) |
| Reassemble scenarios | `make assemble-scenarios` (after editing category files) |
| Refresh project brief | `python3 pipeline/update-brief.py` |

---

## Reference: What Each Enhancement Phase Built

| Phase | What it created | How you use it now |
|-------|----------------|-------------------|
| 01 | `--changed-only`/`--range` validation, auto-brief refresh, session resume template | Automatic (CI runs brief refresh; `make validate-changed` for fast checks) |
| 02 | `find_missing_transitivity.py`, `polish_verb_transitivity.md` | Run the polishing prompt to add transitivity to verbs |
| 03 | `polish_aspect_notes.md` | Run the polishing prompt to document aspect behavior |
| 04 | `score_note_quality.py`, `note_templates.json` | Run `make note-scores` to see quality distribution |
| 05 | `check_semantic_clusters.py`, asymmetry detection | Run `make check-clusters` or `make check-symmetry` |
| 06 | `prioritize_polishing.py`, priority files | Run `make priorities` to regenerate priority lists |
| 07 | Semantic field definitions, `audit_semantic_field.py` | Run `make audit-fields` to find vocabulary gaps |
| 08 | Learner scenario definitions, `analyze_scenarios.py` | Run `make audit-scenarios` to find scenario gaps |
| 09 | `audit_tiers.py`, `audit_vocabulary_tiers.md` | Run `make audit-tiers` for tier analysis |
| 10 | `check_consistency.py`, enhanced `report.py` | Run `make consistency` or `make report` |
| 11 | `entry_lock.py`, `parallel_coordinator.py` | Use for manual parallel sessions |
| 12 | `review_runner.py`, calibration report | Run multi-model reviews (requires OpenRouter key) |
| 13 | `task_queue.py` | Use for queue-based parallel polishing |
| 14 | Two-pass review system, `polish_cross_model_review.md` | Run screening + deep review passes |
| 15 | Article system, 3 pilot articles | Articles build automatically with `make build` |
| 16 | `orchestrator.py`, `monitor.py` | Automated parallel session management |

---

## Tips

- **One task per session** works best for polishing. The prompts are designed for focused work with automatic progress tracking.
- **Run `make build` at the end** of any session that modifies entries. The polishing prompts do this automatically.
- **The priority system is optional.** Polishing prompts work with or without priority files. With priority files, they process the worst entries first. Without them, they go sequentially by ID.
- **Semantic field and scenario data** live in per-category files under `build/data/semantic_fields/` and `build/data/learner_scenarios/`. Edit those files, then run `make assemble-fields` or `make assemble-scenarios` to rebuild the combined JSON.
- **The knowledge base** at `planning/wiki/` has background research and design decisions. Read `planning/wiki/index.md` for the catalog.
- **All prompts are listed** in `prompts/metaprompt_list.md` with copy-paste-ready text.
