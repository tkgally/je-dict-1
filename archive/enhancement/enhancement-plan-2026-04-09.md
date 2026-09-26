# je-dict-1 Comprehensive Enhancement Plan

**Prepared**: 2026-04-09
**Based on**: Full analysis of repository (23,000+ entries) and planning wiki (40+ pages)

---

## Executive Summary

je-dict-1 is a remarkably mature LLM-built Japanese-English learner's dictionary—23,000 entries, 93,500+ example sentences, and 6,000+ cross-references, supported by an extensive automated build pipeline. The project has accumulated deep institutional knowledge in its planning wiki and has a clear architectural separation between deterministic scripts and semantic LLM work.

This plan identifies **three strategic fronts**: (1) deepening content quality across the existing 23,000 entries, (2) scaling the production workflow beyond its current sequential bottleneck, and (3) strengthening the feedback loop between content goals and tooling. Recommendations are grounded in specific findings from the wiki's research pages, the open-issues tracker, and the project's own hard-won lessons about what can and cannot be automated.

---

## Part 1: Content Quality Enhancement

### 1.1 Priority Tier: Systemic Quality Gaps (Critical Path)

These are gaps that affect the dictionary's reliability for learners and should be addressed before further expansion.

#### 1.1.1 Verb Transitivity Completion Campaign

**Problem**: Many verb entries—especially older ones—lack 自動詞/他動詞 labels and paired-verb cross-references. This is the #1 item on the v2 quality standards HIGH PRIORITY list and is flagged in `open-issues.md`.

**Why it matters**: Transitivity is the single most frequent source of learner errors in Japanese (wiki: `research/vocabulary-acquisition.md`). A dictionary entry for 開ける that doesn't mention 開く is an incomplete entry.

**Implementation steps**:
1. **Build a deterministic gap detector**: Create `build/find_missing_transitivity.py` that scans all verb entries for those lacking `自動詞`/`他動詞` in notes or missing `pair` cross-references. Output a ranked list.
2. **Prioritize by tier**: Process basic-tier verbs first (these are all high-traffic), then core, then general.
3. **Create a dedicated polishing prompt**: `prompts/polish_verb_transitivity.md` with progress tracking in `polishing/tasks/verb-transitivity/progress.txt`.
4. **Batch processing**: Each session processes ~25 verbs—reading the entry, adding transitivity info to notes, adding `pair` cross-references, and verifying both directions.

**Dependencies**: Requires the gap detector script (deterministic layer) before the polishing prompt (semantic layer) can be efficient. This follows the project's established "automate detection, not decision" principle from `topics/deterministic-vs-semantic-tasks.md`.

**Estimated scope**: Likely 2,000–5,000 verb entries need attention.

#### 1.1.2 Note Quality Standardization

**Problem**: Entries created before v2 standards have brief, unstructured notes. The `expand-short-notes.md` task exists but progress is slow relative to the 23,000-entry corpus.

**Why it matters**: Notes are where the dictionary goes beyond a glossary—they're the pedagogical core (wiki: `research/learner-lexicography.md`). Inconsistent notes erode learner trust (wiki: `topics/entry-consistency.md`).

**Implementation steps**:
1. **Formalize note templates by POS** (as proposed in `entry-consistency.md`):
   - Verbs: transitivity → aspect/ている → collocations → particles → similar verbs → register
   - Na-adjectives: usage → predicate vs. modifier → collocations → similar adjectives → register
   - Nouns: explanation → collocations → compounds → similar words → cultural context
2. **Build a note structure scorer**: `build/score_note_quality.py` that checks each entry's notes against the POS template, outputs a quality score (0–100), and flags the weakest entries.
3. **Create a prioritized work queue**: Sort entries by (tier weight × inverse quality score) so basic/core entries with the worst notes get fixed first.
4. **Accelerate the expand-short-notes task**: Currently tracks progress linearly by ID. Instead, let the scorer prioritize entries—jump to the worst ones first rather than processing sequentially.

**Dependencies**: The note templates must be defined before the scorer can be built. The scorer is a new deterministic tool; the actual note-writing remains semantic.

#### 1.1.3 Cross-Reference Completeness & Symmetry

**Problem**: ~6,000 cross-references across 23,000 entries means most entries have no cross-references. The wiki identifies missing reciprocal links, inconsistent relationship labels, and semantic clusters that should be fully linked.

**Implementation steps**:
1. **Extend `find_merge_candidates.py`** to produce a comprehensive asymmetry report: all cases where A→B exists but B→A doesn't.
2. **Build a semantic cluster linter**: For known tight clusters (transitivity pairs, antonym sets, seasonal words, color terms, family terms, counters), verify that all expected links exist.
3. **Prioritize by learner impact**: Transitivity pairs and antonym pairs first (these are the relationships learners actively seek), then broader semantic fields.
4. **Process in cluster batches**: Instead of the current one-entry-at-a-time polishing for `add_cross-references.md`, modify the prompt to process semantic clusters together—pull 5–10 related entries simultaneously, ensure symmetric linking, and normalize relationship labels.

**Dependencies**: Steps 1–2 are deterministic (extend existing scripts). Step 4 requires modifying the cross-reference polishing prompt for cluster-mode processing.

---

### 1.2 Priority Tier: Enrichment (High Value, Ongoing)

These enhance the dictionary's pedagogical depth without fixing a "broken" state.

#### 1.2.1 Multi-Model Proofreading Implementation

**Problem**: All content written by a single model (Claude) creates systematic blind spots. The wiki has a thorough design in `ideas/multi-model-proofreading.md` but it hasn't been implemented.

**Why now**: This is the single highest-leverage quality intervention remaining. As noted in the wiki, different models have different Japanese-language biases—particularly for furigana readings, which directly mislead learners when wrong.

**Implementation steps (phased)**:

**Phase 1 — Furigana-focused proof of concept**:
1. Write a `build/review_runner.py` script that:
   - Takes a batch of entry IDs
   - Formats each entry into a structured review prompt
   - Sends to OpenRouter (target: GPT-4.1 and Gemini 2.5 Flash)
   - Parses structured JSON responses
   - Stores reports in `reviews/{entry_id}.json`
2. Start with furigana correctness only—this is the highest-risk area and produces the most objectively verifiable results.
3. Run on 100 entries, manually evaluate false-positive rate, calibrate prompts.
4. If >80% of flagged issues are genuine, proceed to Phase 2.

**Phase 2 — Two-pass pipeline**:
1. Pass 1 (screening): Run all 23,000 entries through a cheap model (Gemini Flash / GPT-4.1-mini). Flag entries with any concerns.
2. Pass 2 (deep review): Send flagged entries (~10-20% expected) to multiple strong models. Generate detailed structured reports.
3. Create `prompts/polish_cross_model_review.md` to process flagged entries—Claude reads the multi-model report, evaluates each suggestion, applies or rejects with reasoning.

**Phase 3 — Continuous integration**:
1. Add a post-merge CI step that queues new entries for multi-model review.
2. Track review coverage in `report.py` dashboard.

**Dependencies**: Requires OpenRouter API access. Phase 1 is self-contained. Phase 2 depends on Phase 1 calibration results.

#### 1.2.2 Vocabulary Tier Reassessment

**Problem**: Basic/core tier assignments were made early in the project. As noted in `vocabulary-tiers.md`, some entries may be misclassified. The basic tier (801 entries) and core tier (1,982 entries) are frozen—but that doesn't mean they were correctly classified.

**Implementation steps**:
1. **Audit basic tier**: Review all 801 basic-tier entries to confirm they are genuinely foundational. Flag any that seem too specialized for "survival communication."
2. **Audit core tier**: Review all 1,982 core-tier entries for the same.
3. **Reverse audit**: Scan general-tier entries for words that arguably belong in basic or core but were created after those tiers closed. Document these for curator decision.
4. **Produce a report**, not automatic changes—tier reassignment is a policy decision for the curator.

**Dependencies**: This is a pure semantic task. No new tooling needed, but a dedicated prompt would be useful.

#### 1.2.3 Aspect/ている Documentation

**Problem**: Listed as HIGH PRIORITY in v2 standards. Verbs with non-obvious ている meanings need explicit documentation—this is a common and persistent source of learner confusion.

**Implementation steps**:
1. **Compile a list of verbs with non-obvious ている behavior**: Use LLM knowledge to identify verbs where ている = resultative state (結婚する→married), potential (見える→can see), habitual, etc. Cross-check against existing entries.
2. **Build a polishing prompt**: `prompts/polish_aspect_notes.md` that processes verb entries, checks for ている documentation, and adds it where missing.
3. **Prioritize by frequency and confusion potential**: Basic/core verbs first, then general verbs that have stative ている meanings.

**Dependencies**: No new tooling needed. Can be implemented as a straightforward polishing task.

---

### 1.3 Priority Tier: Content Expansion Strategy

These guide *what* to add next, ensuring growth is strategic rather than random.

#### 1.3.1 Semantic Field Audit System

**Problem**: The brainstorming-based candidate discovery method has a clustering bias—it finds words near existing coverage but can miss entire domains (wiki: `ideas/word-discovery-strategies.md`).

**Implementation steps**:
1. **Define 50–100 essential semantic fields**: colors, body parts, weather, emotions, family, food, transportation, medical, legal, academic, etc.
2. **For each field, create an expected vocabulary list** using LLM reasoning (not external dictionary comparison, per project policy).
3. **Cross-check against existing entries**: `build/audit_semantic_field.py` takes a field definition and reports coverage gaps.
4. **Feed gaps into the candidate pipeline**: Missing words from essential fields get priority candidacy.

**Integration with existing pipeline**: This becomes a new "Stage 0" in the content pipeline, feeding into Stage 1 (candidate discovery).

#### 1.3.2 Scenario-Based Gap Analysis

**Problem**: The dictionary may cover many words but miss the specific vocabulary clusters needed for real-world situations.

**Implementation steps**:
1. Define 100–200 common scenarios a learner encounters (doctor visit, apartment rental, job interview, restaurant ordering, etc.).
2. For each scenario, generate the vocabulary needed.
3. Cross-check against the dictionary.
4. Prioritize gaps by scenario frequency and learner level.

**This complements semantic field audits**: Fields are organized by topic; scenarios are organized by communicative need. Together they provide comprehensive coverage checking.

#### 1.3.3 Expository Articles (Pilot)

**Problem**: The dictionary currently treats every piece of content as an entry note. Some topics—counters, keigo, onomatopoeia families—deserve standalone treatment (wiki: `ideas/expository-articles.md`).

**Implementation steps**:
1. **Pilot with 3 articles**: counters/classifiers, basic keigo system, common onomatopoeia groups.
2. **Define article schema**: Lighter than entry schema—title, body (markdown), related entries, tags.
3. **Build article rendering** into `build_flat.py` and add an "Articles" navigation mode.
4. **Link articles from entries**: Entries for individual counters link to the counters article; keigo entries link to the keigo article.
5. **Evaluate pilot**: Does it improve the browsing experience? Does it reduce duplication in entry notes?

**Dependencies**: Requires schema design, build system changes, and content writing. The build system changes are the gating factor.

---

## Part 2: Implementation Workflow Enhancement

### 2.1 Immediate Wins (No Infrastructure Changes)

#### 2.1.1 Automated PROJECT_CONTEXT_BRIEF.md Refresh

**Problem**: `PROJECT_CONTEXT_BRIEF.md` counts are manually updated and often stale (flagged in `open-issues.md` as "Stale tracking files").

**Implementation**:
1. The `pipeline/update-brief.py` script already exists but isn't always run.
2. **Add a pre-session hook**: Modify `CLAUDE.md` to instruct Claude to run `python3 pipeline/update-brief.py` at session start before reading the file.
3. **Add to GitHub Actions**: Run `update-brief.py` as a post-merge step in the validate workflow, committing the result directly to main.

**Impact**: Eliminates the recurring problem of sessions starting with wrong counts.

#### 2.1.2 Polishing Priority Reordering

**Problem**: All polishing tasks process entries linearly by ID. This means the worst entries (oldest, pre-v2) get reached last—or the polishing pass reaches them only after months of sequential processing.

**Implementation**:
1. **Build `build/prioritize_polishing.py`**: For each polishing task dimension (notes, furigana, examples, cross-refs), score all entries and output a priority-ordered list.
2. **Modify polishing prompts** to accept a priority queue file instead of a simple `next: XXXXX` pointer.
3. **Keep the linear fallback**: If no priority queue exists, revert to sequential processing.

**Impact**: Focuses polishing effort where it matters most, dramatically accelerating quality improvement for the weakest entries.

#### 2.1.3 Session Continuity Improvement

**Problem**: Each LLM session starts fresh. While PROJECT_STATUS.md helps, complex multi-session tasks lose context.

**Implementation**:
1. **Standardize session logs**: Every session writes a structured log to `polishing/sessions/` (this already exists but isn't always done).
2. **Create a session resume prompt**: `prompts/resume-session.md` that reads the last session log for a given task and provides context.
3. **Enhance polishing progress files**: Add a "last session summary" field in addition to the `next: XXXXX` pointer.

**Impact**: Reduces context loss between sessions.

---

### 2.2 Parallel Processing Foundation (Medium-term)

The wiki's `ideas/parallel-agent-architecture.md` provides a thorough analysis. Here's a concrete implementation path.

#### 2.2.1 Phase 1: Parallel-Safe Prompt Redesign

**Goal**: Allow two Claude Code sessions to run simultaneously without file conflicts.

**Implementation steps**:
1. **Separate entry-creation from polishing sessions**: Entry creation modifies `candidate_words.json` and creates new files. Polishing modifies existing files. These can safely run in parallel if they don't touch the same entries.
2. **Add explicit ID range parameters to polishing prompts**: Instead of reading from `progress.txt`, each session receives an ID range (e.g., "process entries 10000-10499").
3. **Defer shared file updates**: Sessions don't modify `entries_index.json` or build artifacts. A post-session coordinator step (run on main) handles `update_indexes.py` and `build_flat.py`.
4. **Create a simple entry-level lock file**: Before modifying an entry, write a `.lock` file in the entry's directory. Check for locks before starting. Delete on completion.

**What this enables**: Two sessions running simultaneously—one creating new entries, one polishing old ones—without conflicts. The curator can start both and review both PRs.

#### 2.2.2 Phase 2: Claim-Based Task Queue

**Goal**: Multiple polishing agents can pick tasks from a shared queue.

**Implementation steps**:
1. **Build `pipeline/task_queue.py`**:
   - Stores tasks in `pipeline/task_queue.json`: `{entry_id, task_type, status, claimed_by, timestamp}`
   - `claim` command: atomically marks a batch of tasks as "in progress"
   - `complete` command: marks tasks as done
   - `populate` command: scans for entries needing work and adds tasks
2. **Create task-typed prompts**: Each prompt type (furigana, notes, cross-refs, examples) claims only its task type.
3. **Add timeout-based reclaim**: If a task is claimed but not completed within 30 minutes, it returns to the queue (handles agent crashes).

**What this enables**: 3–4 parallel agents, each specializing in one quality dimension, processing the dictionary simultaneously.

#### 2.2.3 Phase 3: Automated Orchestration

**Goal**: Agents run on a schedule without curator initiation.

**Implementation steps**:
1. **Extend `pipeline/pipeline-config.json`** to support parallel task slots.
2. **Create an orchestrator script** that launches multiple Claude CLI sessions from `pipeline/run-pipeline.sh`.
3. **Add a monitoring dashboard**: Extend `report.py` to show queue status, agent activity, entries processed per hour, and error rates.
4. **Set daily budget caps**: Limit total API spending per day.

**Dependencies**: Phase 2 must be proven stable first. Requires the curator to set up scheduled runs (cron or GitHub Actions).

---

### 2.3 Build System and CI Improvements

#### 2.3.1 Incremental Validation

**Problem**: `validate.py` validates all entries on every run. With 23,000+ entries, this is slow and wastes CI time.

**Implementation**:
1. **Add `--changed-only` flag to `validate.py`**: Use git diff to find changed entry files and validate only those.
2. **Add `--range` flag**: Validate a specific ID range (useful for parallel sessions).
3. **Keep full validation as a weekly check**: CI uses `--changed-only` for PR checks; a scheduled workflow runs full validation weekly.

#### 2.3.2 Consistency Checker Script

**Problem**: Entry consistency issues identified in `topics/entry-consistency.md` have no automated detection.

**Implementation**:
1. **Build `build/check_consistency.py`** that:
   - Compares entry note structures against POS templates
   - Flags cross-reference asymmetries
   - Identifies note length outliers
   - Checks for verbs missing transitivity labels
   - Reports entries with no collocations
2. **Add to `make report`**: Include consistency metrics in the health dashboard.
3. **Generate a prioritized fix list**: Feed into the claim-based task queue.

#### 2.3.3 Enhanced Report Dashboard

**Problem**: `report.py` tracks basic metrics but doesn't capture quality dimensions.

**Implementation**: Extend `report.py` to include:
- Cross-reference symmetry rate
- Note quality score distribution (requires the scorer from 1.1.2)
- Polishing completion percentages per task
- Multi-model review coverage (once implemented)
- Entries per POS with and without expected sections (transitivity, aspect, collocations)
- Candidate queue health (age, quality distribution)

---

## Part 3: Dependency Map and Priorities

### Critical Path

```
[1.1.1] Verb Transitivity ──→ requires build/find_missing_transitivity.py (new script)
                              ──→ requires prompts/polish_verb_transitivity.md (new prompt)

[1.1.2] Note Standardization ──→ requires POS note templates (design decision)
                               ──→ requires build/score_note_quality.py (new script)
                               ──→ feeds into [2.1.2] Polishing Priority Reordering

[1.1.3] Cross-Ref Symmetry ──→ requires extending find_merge_candidates.py (existing script)
                             ──→ requires cluster-mode prompt revision

[1.2.1] Multi-Model Proof  ──→ requires OpenRouter API access
                             ──→ requires build/review_runner.py (new script)
                             ──→ Phase 2 depends on Phase 1 calibration

[2.1.1] Auto Brief Update  ──→ no dependencies (can start immediately)
[2.1.2] Priority Reorder   ──→ requires build/prioritize_polishing.py (new script)
                             ──→ benefits from [1.1.2] note scorer

[2.2.1] Parallel-Safe       ──→ requires prompt modifications
                              ──→ requires entry-level locking

[2.2.2] Task Queue          ──→ requires pipeline/task_queue.py (new script)
                              ──→ depends on [2.2.1] parallel-safe prompts

[2.3.2] Consistency Checker ──→ requires POS note templates from [1.1.2]
```

### Recommended Execution Order

**Immediate actions** (no blocking dependencies):
1. ✅ `[2.1.1]` Auto-refresh PROJECT_CONTEXT_BRIEF.md — trivial change, immediate value
2. ✅ `[1.1.1]` Build `find_missing_transitivity.py` — extends existing script patterns
3. ✅ `[2.1.3]` Session continuity improvements — modify prompts and add resume template
4. ✅ `[1.2.3]` Aspect/ている documentation — new polishing task, straightforward

**Next batch** (build on the above):
5. `[1.1.2]` Define POS note templates → build note quality scorer
6. `[1.1.3]` Extend cross-reference detection → cluster-mode polishing
7. `[2.1.2]` Priority-based polishing reordering (benefits from scorer)
8. `[1.3.1]` Semantic field audit system (new discovery method)

**Medium-term infrastructure**:
9. `[1.2.1]` Multi-model proofreading Phase 1 (proof of concept)
10. `[2.2.1]` Parallel-safe prompt redesign
11. `[2.3.2]` Consistency checker script
12. `[2.3.3]` Enhanced dashboard

**Longer-term**:
13. `[2.2.2]` Claim-based task queue
14. `[1.2.1]` Multi-model proofreading Phase 2-3
15. `[1.3.3]` Expository articles pilot
16. `[2.2.3]` Automated orchestration

---

## Part 4: New Tooling Summary

| Script | Purpose | Type | Priority |
|--------|---------|------|----------|
| `build/find_missing_transitivity.py` | Find verb entries without transitivity info | Deterministic | Immediate |
| `build/score_note_quality.py` | Score note completeness against POS templates | Deterministic | High |
| `build/prioritize_polishing.py` | Generate priority-ordered work queues | Deterministic | High |
| `build/check_consistency.py` | Flag cross-entry inconsistencies | Deterministic | Medium |
| `build/audit_semantic_field.py` | Check coverage of defined semantic fields | Hybrid | Medium |
| `build/review_runner.py` | Send entries to external models via OpenRouter | Infrastructure | Medium |
| `pipeline/task_queue.py` | Claim-based parallel task management | Infrastructure | Medium-term |
| `prompts/polish_verb_transitivity.md` | Polishing prompt for transitivity completion | Prompt | Immediate |
| `prompts/polish_aspect_notes.md` | Polishing prompt for ている documentation | Prompt | High |
| `prompts/resume-session.md` | Context recovery for multi-session tasks | Prompt | Immediate |

---

## Part 5: Quality Metrics and Success Criteria

### Content Quality Targets

| Metric | Current (est.) | Target | How to Measure |
|--------|---------------|--------|----------------|
| Verbs with transitivity | ~60% | 100% | `find_missing_transitivity.py` |
| Entries with structured notes | ~40% | 80% | `score_note_quality.py` ≥ 60 |
| Cross-reference symmetry | ~70% | 98% | `find_merge_candidates.py` asymmetry report |
| Verbs with ている docs | ~20% | 80% (of those needing it) | New aspect audit script |
| Multi-model review coverage | 0% | 100% (furigana) | `review_runner.py` tracking |
| Average examples per sense | ~4.1 | ≥4 for all entries | `report.py` |
| Cross-references per entry | ~0.26 | ≥0.5 | `report.py` |

### Workflow Efficiency Targets

| Metric | Current | Target | How to Measure |
|--------|---------|--------|----------------|
| Entries polished per day | ~20–30 | 60–120 | Parallel sessions × throughput |
| Stale BRIEF count errors | Frequent | Zero | Auto-refresh verification |
| Polishing coverage rate | Linear by ID | Priority-weighted | Queue depletion metrics |
| Parallel session support | 1 | 2–4 | Task queue utilization |

---

## Part 6: Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Multi-model review generates many false positives | Medium | Medium | Phase 1 calibration on 100 entries before scaling |
| Parallel sessions create merge conflicts despite precautions | Medium | Low | Entry-level locking; defer shared files; small batches |
| Note templates are too rigid, produce cookie-cutter entries | Low | Medium | Templates define expected sections, not required ones; maintain LLM flexibility within structure |
| Semantic field audits miss domain-specific vocabulary | Medium | Low | Complement with scenario-based gap analysis; iterate on field definitions |
| Prioritized polishing skips entries that need mild improvement | Low | Low | Keep periodic full-sweep passes on a longer cycle |
| OpenRouter API costs escalate unexpectedly | Low | Medium | Two-pass architecture; budget caps; use cheapest models for screening |

---

## Appendix: Key Wiki Pages Referenced

This plan draws on the following wiki pages. Their accumulated insights informed every recommendation:

- **Project**: `overview.md`, `content-pipeline.md`, `quality-standards.md`, `open-issues.md`, `entry-design.md`, `vocabulary-tiers.md`, `architecture.md`
- **Research**: `learner-lexicography.md`, `vocabulary-acquisition.md`, `example-sentences.md`, `collocations.md`, `definition-strategies.md`, `dictionary-lookup-behavior.md`
- **Topics**: `deterministic-vs-semantic-tasks.md`, `entry-consistency.md`, `cross-references.md`, `register.md`, `verb-transitivity.md`, `compound-verbs.md`, `word-variants.md`
- **Ideas**: `parallel-agent-architecture.md`, `multi-model-proofreading.md`, `word-discovery-strategies.md`, `expository-articles.md`, `dictionary-growth.md`, `ai-review.md`, `audio-expansion.md`
