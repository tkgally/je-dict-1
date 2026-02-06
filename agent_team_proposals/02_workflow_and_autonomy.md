# Agent 2 Report: Workflow & Autonomy

## Executive Summary

The je-dict-1 project has developed a remarkably sophisticated workflow for AI-assisted dictionary construction, with 10,306 entries built through hundreds of individual Claude sessions. The current approach -- one prompt per session, 10-15 minutes each, manual merge to main -- provides excellent quality control but creates a bottleneck where the user's available attention is the limiting factor on throughput.

The project already contains the architectural seeds of a more autonomous system: task-specific prompts with progress tracking, context reset procedures, session logging, and a batch script (`run-inline-links-batch.sh`) that chains multiple `claude --print` invocations. What is needed is not a radical redesign but a careful evolution of these existing patterns into a structured pipeline that can run longer with less manual intervention while preserving the semantic quality that defines this dictionary.

Key findings:
1. **The context window is the fundamental constraint.** When Claude works too long continuously, it loses semantic grounding and falls back to scripting. The current 10-15 minute session window is an empirical response to this problem.
2. **The existing prompt/skill architecture is well-designed for autonomy.** Each task type already has a self-contained prompt with clear start/stop procedures and progress persistence.
3. **The biggest throughput gains come from reducing inter-session overhead**, not from making individual sessions longer. The time spent manually launching, reviewing, merging, and launching the next task is where efficiency is lost.
4. **Different task types have fundamentally different autonomy profiles.** New entry creation requires deep semantic engagement (low autonomy). Inline link addition is semi-mechanical (medium autonomy). Corpus harvesting is evaluative (high autonomy). A one-size-fits-all approach will not work.

---

## Current Workflow Analysis

### How Work Currently Flows

The dictionary expansion pipeline has four main activity types, each handled as separate sessions:

| Activity | Prompt | Batch Size | Frequency | Autonomy Level |
|----------|--------|-----------|-----------|----------------|
| Candidate discovery | `newcandidates.md`, `corpus_harvesting.md` | 50-150 words evaluated | Every few days | Medium-High |
| New entry creation | `newentries.md` | 30 entries | Daily (often 3-5 sessions/day) | Low |
| Inline link polishing | `polish_add_inline_links.md` | 20-30 entries | Every few days | Medium |
| Quality polishing | `polish_*.md` (4 types) | 20-50 entries | Periodic | Medium |

Each session follows this lifecycle:
1. User pastes a prompt (or gives a brief instruction referencing a prompt file)
2. Claude reads progress state, performs work, writes results
3. Claude runs validation, build, commits, and pushes
4. User reviews the PR on GitHub, merges to main
5. User initiates the next session

### Strengths of the Current Approach

1. **Atomic units of work.** Each session produces a clean, reviewable PR. If something goes wrong, it is easy to revert a single session's work.
2. **Semantic quality is preserved.** Because each session starts fresh, Claude approaches each task with full context window capacity and does not suffer from accumulated drift.
3. **Progress persistence is robust.** Every task type tracks its progress in a simple `progress.txt` or tracking file, making it trivial to resume across sessions.
4. **Skill architecture provides guardrails.** The `.claude/skills/` directory ensures Claude loads the right quality standards for each task type automatically.
5. **Validation is integrated.** Every session ends with `validate.py`, `update_indexes.py`, and `build_flat.py`, catching errors before they reach main.

### Pain Points

1. **User is the bottleneck.** Every 10-15 minutes, work stops until the user initiates the next session. If the user is unavailable for 8 hours, no work happens.
2. **Inter-session overhead is high.** Each session requires the user to: check the previous PR, merge it, decide the next task, paste the prompt, and wait for Claude to read context files and begin. This overhead is 3-5 minutes per session.
3. **Task switching is manual.** The user must decide when to switch between activity types (e.g., "we have enough candidates, time to create entries" or "entries need inline links now"). This scheduling requires mental model maintenance.
4. **No parallelism.** Only one task type runs at a time. Candidate harvesting, entry creation, polishing, and linking could conceptually overlap, but the serial workflow prevents this.
5. **Context window waste on repeated bootstrapping.** Each session spends significant context reading PROJECT_STATUS.md (which is very large at 56,000+ tokens), skill files, and progress state. This is repeated work that consumes precious context capacity.

### Work Cadence (from git history analysis)

Looking at recent commits (2026-02-01 through 2026-02-06):

- **Feb 1**: 7 sessions (candidates x2, entries x5) -- high-intensity day
- **Feb 2**: 3 sessions (candidates, entries, inline links)
- **Feb 3**: 6 sessions (candidates x2, entries x4)
- **Feb 4**: 5 sessions (entries x4, candidates)
- **Feb 5**: 6 sessions (entries x4, inline links x2)
- **Feb 6**: 2 sessions (entries x1, corpus harvesting x1)

Average: ~5 sessions per day, predominantly entry creation. The user is clearly investing substantial time managing these sessions.

---

## Context Window Challenges

### The Fundamental Problem

Claude's context window creates a hard limit on how much semantic work can be done in a single continuous session. Based on the evidence in this project:

- **Entry creation**: ~30 entries per session before context becomes strained. Each entry requires reading the candidate, checking for duplicates, writing JSON with examples and notes, and running furigana checks. At roughly 3-4 tool calls per entry, 30 entries consumes most of a context window.
- **Inline linking**: ~20-30 entries per session. Each entry requires reading the full JSON, identifying every word in every example, looking up IDs, and rewriting the Japanese strings with link markup. This is context-intensive.
- **Polishing tasks**: ~50 entries per session for lighter tasks (semantic labels, furigana), ~20 entries for heavier tasks (example sentences, notes expansion).
- **Corpus harvesting**: ~150 entries evaluated per session. This is lighter per-item work (evaluate, skip/add).

### How the Project Currently Handles It

The project has already developed a "context reset" pattern that appears in every polishing prompt:

1. Monitor context usage (via `/context` command)
2. At <30% remaining: save progress, write session log, commit
3. Use `/compact` to reset context
4. Re-read the prompt and continue

This pattern works within a single interactive session but requires user presence to trigger and monitor.

### Where It Fails

1. **PROJECT_STATUS.md has grown enormous** (56,000+ tokens). Reading it consumes a large fraction of the context window at session start. Most of this content is historical session logs that are irrelevant to the current task.
2. **The PreCompact hook** (`remind-resume-update.sh`) is designed for a specific old task (semantic assignment) and provides stale guidance.
3. **Context reset in batch mode** (`run-inline-links-batch.sh`) works by starting entirely new Claude processes. This is the correct architecture but is only implemented for one task type.
4. **No mechanism to detect quality degradation.** When context gets low, Claude may start cutting corners (shorter notes, fewer examples, less careful furigana) before explicitly running out. There is no automated quality gate.

---

## Proposed Autonomous Workflow

### Design Principles

1. **Fresh context for every atomic unit of work.** Never try to fight the context window -- embrace it. Each `claude --print` invocation should do one well-scoped batch and exit cleanly.
2. **Orchestration through shell scripts, semantics through Claude.** Scripts handle scheduling, sequencing, and validation; Claude handles the semantic work that requires language knowledge.
3. **User reviews at natural boundaries, not at every step.** Accumulate work into larger reviewable chunks (e.g., a day's worth of entries) rather than one PR per session.
4. **Quality gates are automated checks, not manual inspection.** Use validation scripts as go/no-go gates between batches. Reserve human review for periodic spot-checks.
5. **Progress state is the source of truth.** Everything needed to continue work is in the filesystem (progress.txt files, candidate_words.json, tracking files). No session-to-session memory is needed.

### Architecture: The Task Runner

The core proposal is a **task runner script** that orchestrates multiple Claude sessions automatically, with the user configuring what to run and reviewing results afterward.

```
je-dict-pipeline.sh
  |
  +-- Reads pipeline-config.json (user-configured task queue)
  |
  +-- For each task in queue:
  |     |
  |     +-- Runs pre-flight checks (git clean, validation passes)
  |     +-- Invokes: claude --print "<task prompt>"
  |     +-- Runs post-flight validation
  |     +-- If validation passes: commits to feature branch
  |     +-- If validation fails: logs error, skips to next task
  |     +-- Updates pipeline-status.json with results
  |
  +-- At end: generates summary report
  +-- Optionally: creates PR for user review
```

### Pipeline Configuration

The user controls the pipeline through a simple config file:

```json
{
  "branch": "pipeline/2026-02-07",
  "tasks": [
    {"type": "corpus-harvesting", "count": 1},
    {"type": "new-entries", "count": 3},
    {"type": "inline-links", "count": 2},
    {"type": "example-sentences", "count": 1}
  ],
  "options": {
    "stop_on_validation_failure": true,
    "auto_create_pr": true,
    "max_total_runtime_minutes": 120
  }
}
```

This says: "Run 1 corpus harvesting session, then 3 entry creation sessions, then 2 inline link sessions, then 1 example sentence polishing session. Stop if validation fails. Create a PR at the end."

The user can launch this before going to bed or leaving for work, and return to a single PR containing all the work for review.

### Task-Specific Designs

#### 1. New Entry Creation (Low Autonomy -- 30 entries per invocation)

This is the most semantically demanding task. Each entry requires genuine linguistic knowledge for:
- Choosing appropriate definitions
- Writing natural example sentences
- Crafting learner-focused notes
- Assigning correct tags

**Recommended approach**: Keep the current 30-entry batch size. The task runner invokes `claude --print` with the newentries prompt. The key improvement is removing the user from the loop between batches.

**Quality gate**: After each batch, run `validate.py` and `find_missing_furigana.py`. If either reports errors, stop the pipeline (do not proceed to more entry creation on top of broken entries).

**Context optimization**: Create a `PROJECT_CONTEXT_BRIEF.md` file (under 2,000 tokens) containing only what Claude needs for entry creation: current entry count, next available ID, tier policy, and critical rules. Do not load the full PROJECT_STATUS.md.

#### 2. Inline Link Polishing (Medium Autonomy -- 30 entries per invocation)

This task is semi-mechanical: read each example, identify words, look up IDs, add markup. It requires semantic knowledge (understanding word boundaries, choosing correct homograph entries) but follows a repetitive pattern.

**Recommended approach**: The existing `run-inline-links-batch.sh` is the right model. Extend it with validation gates between iterations and progress tracking.

**Quality gate**: After each batch, run `validate.py` with word-link checks. Count validation errors; if new errors appear, stop.

**Context optimization**: The inline-links skill file already contains a common-words reference table. Consider generating an expanded lookup table (`build/word_id_lookup.json`) that maps readings to entry IDs, reducing the number of search tool calls Claude must make.

#### 3. Corpus Harvesting (High Autonomy -- 150 entries per invocation)

This task evaluates words from `corpus_extracted_words.json` and decides whether to add them as candidates. It is evaluative rather than generative -- Claude is filtering, not creating content.

**Recommended approach**: This can run with the highest autonomy. Multiple invocations can process the entire corpus list without user intervention.

**Quality gate**: After each batch, verify that `candidate_words.json` is valid JSON and that no duplicate candidates were added. Since this task only adds candidates (not entries), the risk of quality problems is low.

#### 4. Quality Polishing Tasks (Medium Autonomy -- variable batch sizes)

The four polishing tasks (furigana completeness, furigana correctness, example sentences, semantic labels) all follow the same pattern: iterate through entries sequentially, check one aspect, fix if needed.

**Recommended approach**: These are natural candidates for the batch runner. Each invocation processes its batch, updates progress.txt, and exits. The next invocation picks up where the previous left off.

**Quality gate**: Run `validate.py` and the task-specific validator (e.g., `validate_tags.py` for semantic labels). For example sentence polishing, also run a count check to ensure minimum example requirements are met for modified entries.

#### 5. Noentry Resolution (Medium-Low Autonomy -- special task)

This task (`polish_add_entries_for_noentry_example_words.md`) creates entries for words marked `noentry` during inline linking, then updates the links. It combines entry creation (low autonomy) with link updating (medium autonomy).

**Recommended approach**: Run as a dedicated pipeline step after inline linking sessions accumulate enough noentry words. Prioritize high-frequency noentry words.

### Keeping the User in the Loop

The user should not need to babysit the pipeline but should have full visibility and control.

#### 1. Pipeline Status Dashboard

Create `pipeline-status.json` that is updated after each task:

```json
{
  "started": "2026-02-07T22:00:00Z",
  "tasks_completed": 4,
  "tasks_remaining": 3,
  "entries_created": 90,
  "entries_polished": 60,
  "candidates_added": 25,
  "validation_errors": 0,
  "last_task": {
    "type": "new-entries",
    "duration_seconds": 540,
    "entries": 30,
    "status": "success"
  }
}
```

#### 2. Summary Reports

At pipeline completion, generate a human-readable summary:

```
=== Pipeline Summary: 2026-02-07 ===
Duration: 1h 42m
Tasks completed: 7/7

Corpus Harvesting:
  - Evaluated 150 words, added 28 candidates

New Entries (3 sessions):
  - Created 90 entries (10307-10396)
  - 4 new kanji added
  - All validation passed

Inline Links (2 sessions):
  - Linked entries 00471-00530
  - 23 words marked noentry

Example Sentences (1 session):
  - Checked entries 01059-01108
  - Modified 12 entries (added examples)

No validation errors. PR ready for review.
```

#### 3. Stop Conditions

The pipeline should stop automatically when:
- Validation fails (entry creation errors, broken links)
- A task produces no output (Claude error or context issue)
- The total runtime exceeds the configured maximum
- A task's progress file has not advanced (stuck loop detection)

#### 4. Periodic User Review

Instead of reviewing every PR, the user reviews at these checkpoints:
- **Daily review**: One PR per day containing all pipeline work
- **Spot-check cadence**: Every 3-5 days, manually inspect 10-20 entries from recent sessions
- **Milestone review**: At every 500 new entries, do a thorough quality audit

### Reducing PROJECT_STATUS.md Bloat

PROJECT_STATUS.md is currently 56,000+ tokens because it accumulates detailed session logs. This wastes context window capacity on every session start. The proposal:

1. **Create `PROJECT_CONTEXT_BRIEF.md`** (~1,500 tokens): Contains only current state needed for work:
   - Current entry count, candidate count, next available ID
   - Tier policy, critical rules
   - Active polishing task progress pointers
   - No historical session logs

2. **Archive session logs**: Move the "Recent Changes" section of PROJECT_STATUS.md to a separate `CHANGELOG.md`. Keep only the last 5 sessions in PROJECT_STATUS.md.

3. **Auto-update brief file**: The pipeline script updates PROJECT_CONTEXT_BRIEF.md after each task completion, so it is always current.

### Respecting the Semantic/Scripting Boundary

The core insight from this project is that certain tasks require Claude's semantic capabilities (understanding Japanese, judging naturalness, identifying learner challenges) while others can be scripted. The pipeline must never cross this boundary by trying to automate semantic work.

**Tasks that MUST remain semantic (Claude does the work):**
- Writing dictionary entries (definitions, examples, notes)
- Adding inline word links (word boundary identification, homograph disambiguation)
- Evaluating candidate words (determining relevance and appropriateness)
- Checking furigana correctness (determining the right reading in context)
- Writing and evaluating example sentences

**Tasks that CAN be scripted (shell/Python does the work):**
- Running validation
- Building the website
- Updating indexes
- Committing and pushing
- Creating PRs
- Tracking progress
- Generating reports
- Detecting stuck states

The pipeline script handles the second category, freeing Claude to focus entirely on the first.

---

## Implementation Plan

The following steps are designed to be executed as individual prompts the user gives to Claude, each as a self-contained session. They are ordered by dependency and priority.

### Phase 1: Reduce Context Overhead (2-3 sessions)

**Prompt 1: Create PROJECT_CONTEXT_BRIEF.md**

> Create a new file `PROJECT_CONTEXT_BRIEF.md` that contains only the information Claude needs at the start of a work session: current entry count, candidate count, next available entry ID, vocabulary tier policy, polishing task progress pointers, and critical rules. Target under 1,500 tokens. Do NOT include historical session logs. Then update all prompts in `prompts/` to reference `PROJECT_CONTEXT_BRIEF.md` instead of `PROJECT_STATUS.md` for session startup. Keep PROJECT_STATUS.md as-is for historical reference.

**Prompt 2: Archive old session logs from PROJECT_STATUS.md**

> Move all "Recent Changes" entries older than 7 days from PROJECT_STATUS.md into a new file `CHANGELOG.md`. Keep only the 5 most recent session logs in PROJECT_STATUS.md. Update the PROJECT_STATUS.md header to reference CHANGELOG.md for full history.

**Prompt 3: Update the PreCompact hook**

> Update `.claude/remind-resume-update.sh` to be a general-purpose pre-compact reminder. Instead of the old semantic assignment task, it should remind Claude to: (1) update the relevant progress.txt file, (2) write a session log if one is expected, and (3) commit all changes. Remove the outdated multi-sense entry counting loop.

### Phase 2: Build the Task Runner (3-4 sessions)

**Prompt 4: Create the pipeline configuration schema**

> Create `pipeline/pipeline-config.json` with a schema that defines a task queue. Each task should specify: type (one of: corpus-harvesting, new-entries, inline-links, example-sentences, furigana-completeness, furigana-correctness, semantic-labels, noentry-resolution, expand-short-notes), count (number of invocations), and optional parameters. Also create `pipeline/pipeline-config.example.json` with a sample configuration. Store the schema documentation in `pipeline/README.md`.

**Prompt 5: Create the pipeline runner script**

> Create `pipeline/run-pipeline.sh`, a bash script that reads `pipeline/pipeline-config.json` and executes each task in sequence. For each task: (1) check that git working tree is clean, (2) invoke `claude --print` with the appropriate prompt from `prompts/`, (3) run `python3 build/validate.py` as a quality gate, (4) if validation passes, commit to the configured branch, (5) if validation fails, log the error and either stop or skip based on config, (6) update `pipeline/pipeline-status.json` with results. At the end, generate a summary report to `pipeline/pipeline-report.txt` and optionally create a PR. Use the existing `run-inline-links-batch.sh` as reference for the `claude --print` invocation pattern.

**Prompt 6: Create post-task validation gates**

> Create `pipeline/validate-task.sh` that takes a task type as argument and runs the appropriate validation suite. For new-entries: validate.py + find_missing_furigana.py. For inline-links: validate.py with word-link grep. For example-sentences: validate.py + example count check. For semantic-labels: validate_tags.py + validate.py. For corpus-harvesting: JSON syntax check on candidate_words.json. For all tasks: verify that the progress file has advanced (detect stuck loops). Return exit code 0 for pass, 1 for fail.

**Prompt 7: Create the status update and reporting system**

> Create `pipeline/update-status.py` that: (1) reads the current pipeline-status.json, (2) accepts task results as arguments (type, duration, items processed, status), (3) updates the status file, (4) when called with --report flag, generates a human-readable summary of the pipeline run. Also create `pipeline/update-brief.py` that reads the current state of the project (entry count from entries_index.json, candidate count from candidate_words.json, polishing progress from progress.txt files) and regenerates PROJECT_CONTEXT_BRIEF.md automatically.

### Phase 3: Optimize Individual Task Prompts (2-3 sessions)

**Prompt 8: Create --print-optimized versions of key prompts**

> The existing prompts in `prompts/` are designed for interactive sessions. Create `prompts/batch/` versions optimized for `claude --print` (non-interactive) execution. Key differences: (1) read PROJECT_CONTEXT_BRIEF.md instead of PROJECT_STATUS.md, (2) do not include context reset procedures (each invocation is a fresh context), (3) always commit at end, (4) do not push (the pipeline handles pushing), (5) include explicit "exit cleanly" instructions. Create batch versions for: newentries.md, polish_add_inline_links.md, corpus_harvesting.md, polish_example_sentences.md.

**Prompt 9: Generate a word-ID lookup table for inline linking**

> Create `build/generate_word_lookup.py` that scans all entries and generates `build/word_id_lookup.json` mapping readings to entry IDs (with headword and gloss for disambiguation). This lookup table should be loaded by Claude during inline linking sessions instead of running Python search snippets for every word. Include it in the inline-links batch prompt instructions. Also add this to the build pipeline so it stays current.

**Prompt 10: Create a task scheduler recommendation script**

> Create `pipeline/recommend-tasks.py` that examines the current project state and recommends what the next pipeline run should contain. Logic: (1) if candidate_words.json has fewer than 100 candidates, recommend corpus harvesting, (2) if candidate count is over 100, recommend entry creation sessions (count = candidates / 30, capped at 5), (3) if inline links progress is more than 500 entries behind the latest entry, recommend inline link sessions, (4) recommend one polishing session for whichever polishing task has the most entries remaining. Output a suggested pipeline-config.json.

### Phase 4: User Workflow Integration (1-2 sessions)

**Prompt 11: Create the daily workflow documentation**

> Create `pipeline/DAILY_WORKFLOW.md` documenting the new workflow for the user. Cover: (1) how to configure and launch a pipeline run, (2) how to review the summary report and PR, (3) how to do periodic spot-check reviews, (4) how to handle validation failures, (5) how to add new task types. Include example daily routines: "morning launch" (configure pipeline, start it, go to work), "evening review" (check PR, merge, adjust config for next day), "weekend audit" (thorough quality review of week's work).

**Prompt 12: Integrate with GitHub Actions (optional, advanced)**

> Create a GitHub Actions workflow that can be manually triggered to run the pipeline. The workflow would: (1) check out the repo, (2) read pipeline-config.json, (3) run pipeline/run-pipeline.sh, (4) create a PR with the results. This allows the user to trigger a pipeline run from their phone or any browser without needing a terminal. Note: this requires the Claude CLI to be available in the CI environment, which may require a custom runner or API-based approach.

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Quality degradation in autonomous mode | Medium | High | Validation gates, periodic user audits, spot-check protocol |
| Stuck loops (Claude fails silently) | Medium | Low | Progress advancement detection, timeout limits |
| Merge conflicts from parallel work | Low | Medium | Pipeline works on a single branch sequentially |
| Context window issues in batch mode | Low | Medium | Each invocation is a fresh context; batch prompts are minimal |
| Candidate pipeline runs dry | Low | Low | Scheduler recommends harvesting when candidates < 100 |

## Expected Impact

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Sessions per day (user-attended) | 5 | 1-2 (review only) | 60-80% less user time |
| Entries created per day | 30-150 | 90-150 (pipeline) | Consistent throughput |
| User time per session | 13-18 min (10-15 work + 3-5 overhead) | 15-20 min (review) | Time spent on review, not launching |
| Pipeline tasks per day | 5 (manual) | 7-10 (automated) | 40-100% more tasks |
| Context wasted on PROJECT_STATUS.md | ~20% of window | <2% of window | Major efficiency gain |

## Conclusion

The je-dict-1 project is already well-architected for autonomous operation. The prompt/skill system, progress tracking, validation suite, and session logging all support a pipeline-based workflow. The main gaps are: (1) a task runner to orchestrate multiple sessions, (2) context-optimized prompts for batch execution, (3) automated quality gates between sessions, and (4) a reduced-size project context file. These can be built incrementally through the 12-prompt implementation plan above, with each step producing immediate value. The user transitions from "session operator" to "pipeline manager" -- configuring work, reviewing results, and performing quality audits rather than manually launching and monitoring every session.
