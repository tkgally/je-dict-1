# Parallel Agent Architecture for Autonomous Dictionary Improvement

**Last updated**: 2026-04-06

## Overview

The current dictionary maintenance system relies on sequential, manually-triggered sessions: the curator gives Claude a prompt, Claude processes a batch of entries, commits, and stops. This page explores how to evolve toward a system where multiple agents work autonomously and in parallel to improve the dictionary continuously, without the curator needing to intervene for each task.

## Current system and its limitations

### How it works now

1. Curator starts a Claude Code session (web or CLI)
2. Curator provides a prompt (e.g., "Read prompts/newentries.md and follow the instructions")
3. Claude reads the prompt, processes entries, commits, creates a PR, merges
4. Session ends; curator starts a new one for the next task

Some tasks run via `claude --print` (non-interactive batch mode) or the pipeline scheduler, but they still run sequentially and each takes the full repository as its working context.

### Why sequential is a problem

- **Throughput ceiling**: Only one task runs at a time. With ~19,000 entries and many polishing dimensions, sequential processing will take months to cover everything once.
- **Curator bottleneck**: Each session requires the curator to initiate it and (often) review the PR. The curator's time is the scarcest resource.
- **File conflicts**: Multiple sessions cannot safely modify the same files. Polishing tasks read and write `entries_index.json`, `polishing/tasks/*/progress.txt`, and individual entry files. Concurrent runs would create merge conflicts.
- **Context limitations**: A single session can process ~20-30 entries before context fills up. Parallelism would multiply effective throughput.

## Design goals

1. **Multiple agents working simultaneously** on different subsets of entries or different tasks
2. **No file conflicts** — agents must not modify the same files concurrently
3. **Graceful degradation** — if one agent fails, others continue unaffected
4. **Incremental adoption** — the new system should coexist with the current prompting system, not replace it immediately
5. **Auditability** — every change should be traceable to a specific agent, task, and reasoning
6. **Quality preservation** — parallel operation must not reduce quality; if anything, it should enable more thorough review

## Architecture options

### Option A: File-based partitioning

**Concept**: Divide the entry space into non-overlapping partitions (e.g., by ID range). Each agent owns a partition and can only modify entries within it.

**How it works**:
- Agent 1: entries 00000-04999
- Agent 2: entries 05000-09999
- Agent 3: entries 10000-14999
- Agent 4: entries 15000-19999
- Agent 5: entries 20000+

Each agent works on its own git branch, processes entries in its range, and creates a PR. PRs are merged sequentially (or with conflict resolution).

**Pros**: Simple, no coordination needed, clear ownership
**Cons**: Can't handle cross-entry tasks (cross-references span partitions), uneven workload (some ranges may need more work), shared files (`entries_index.json`) still conflict

### Option B: Task-based partitioning

**Concept**: Different agents work on different task types simultaneously, each modifying different fields or aspects of entries.

**How it works**:
- Agent A: furigana correctness (modifies headword and example furigana only)
- Agent B: cross-reference addition (modifies cross_references and prominent_see_also only)
- Agent C: note expansion (modifies notes field only)
- Agent D: example sentence improvement (modifies senses[].examples only)

Each agent touches different JSON fields, so even if they process the same entry file, their changes don't conflict semantically (though they may conflict at the file level in git).

**Pros**: Each agent specializes, enabling deeper expertise; workload distributes naturally
**Cons**: Git still sees file-level conflicts; requires careful field-level merge tooling; some tasks naturally touch multiple fields

### Option C: Claim-based work queue

**Concept**: A central work queue lists tasks (entry IDs + task types). Agents claim tasks before starting, preventing conflicts.

**How it works**:
1. A scheduler populates a queue: `[{entry: 01234, task: "expand-notes"}, {entry: 01235, task: "check-furigana"}, ...]`
2. An agent claims a task by atomically marking it "in progress" (e.g., writing to a lock file or database)
3. The agent processes the entry, commits, and marks the task "done"
4. Another agent can then claim tasks for that entry

**Pros**: No conflicts (claimed tasks are locked), flexible task assignment, natural load balancing
**Cons**: Requires a coordination mechanism (file-based locks, a simple database, or a GitHub issue tracker); more complex infrastructure

### Option D: Branch-per-agent with automated merging

**Concept**: Each agent works on its own long-lived branch. An automated merge process periodically integrates branches into main, resolving conflicts.

**How it works**:
1. Multiple agents run continuously, each on its own branch
2. Each agent pulls from main before starting work, pushes to its branch
3. A merge bot (or the curator) periodically merges branches into main
4. If conflicts arise, the merge bot either resolves them automatically (for simple cases) or flags them for review

**Pros**: Agents are fully independent; familiar git workflow; no shared state beyond git
**Cons**: Merge conflicts accumulate; requires robust auto-merge logic; `entries_index.json` and build artifacts always conflict

### Recommended: Hybrid of B and C

**Task-based partitioning** for broad task assignment (each agent type focuses on one aspect of quality), combined with a **claim-based queue** to prevent multiple agents from modifying the same entry simultaneously.

Implementation sketch:
1. A `task_queue.json` or simple SQLite database tracks: entry_id, task_type, status (pending/claimed/done), agent_id, timestamp
2. Agents are typed: furigana-agent, notes-agent, cross-ref-agent, examples-agent, new-entries-agent
3. Before modifying an entry, an agent claims it in the queue (with a timeout to handle agent failures)
4. Agents work on separate branches and create PRs
5. PRs are reviewed (by the curator initially, potentially by a review agent later) and merged
6. After merge, the queue is updated and the entry is available for the next task type

## Shared file conflict resolution

The biggest technical challenge is files that every agent needs to update:

### `entries_index.json`
**Solution**: Don't modify it in agent branches. Instead, run `update_indexes.py` as a post-merge step on main. The merge bot or a CI action handles this.

### `polishing/tasks/*/progress.txt`
**Solution**: Replace with the claim-based queue. Progress tracking moves from "next entry ID to process" to "which entries have been claimed/completed for this task."

### `docs/` (build output)
**Solution**: Build output is generated only on main, after merging agent PRs. Agents never commit build artifacts.

### `candidate_words.json`
**Solution**: Only the new-entries agent modifies this file. Other agents don't touch it.

## Transition plan

### Phase 1: Parallel-safe prompts (near-term, no infrastructure changes)

Modify existing prompts so they can safely run in parallel:
- Each prompt takes an explicit ID range parameter (e.g., "process entries 10000-10499")
- Prompts don't modify shared files; instead they output a change manifest
- A coordinator script applies manifests sequentially

This requires minimal infrastructure and can be tested immediately.

### Phase 2: Claim-based queue (medium-term)

Build the task queue system:
- Simple JSON file or SQLite database
- A `claim_task.py` script that agents call before starting work
- A `complete_task.py` script that agents call after committing
- Queue populated by a planner script that scans for entries needing work

### Phase 3: Continuous autonomous operation (long-term)

Full autonomous system:
- Agents run continuously (or on a schedule) without curator initiation
- A supervisor agent monitors progress, adjusts priorities, and handles errors
- The curator reviews dashboards and intervenes only for policy decisions
- New entries, polishing, cross-referencing, and proofreading all happen concurrently

## Quality safeguards

Parallel operation introduces new quality risks:

- **Conflicting changes**: Agent A improves a note; Agent B rewrites it differently. Solution: claim-based locking prevents this.
- **Regression**: An agent makes a change that undoes a previous improvement. Solution: agents should read and respect existing content, not blindly overwrite.
- **Cascading errors**: A bug in one agent propagates through many entries before being caught. Solution: small batches, frequent CI, rollback capability.
- **Inconsistent standards**: Different agents might apply different quality standards. Solution: all agents use the same skills and guidelines; cross-agent review as a separate task.

## Cost and resource considerations

- Each parallel agent is a separate Claude Code session (API cost)
- Running 4 agents in parallel costs ~4x a single agent, but completes work ~4x faster
- For autonomous operation, a budget cap per day/week would be prudent
- Cheaper models (Haiku, Sonnet) could handle well-defined tasks (furigana checking), reserving Opus for complex tasks (note writing, cross-reference decisions)

## Open questions

- **How to handle entry creation in parallel?** New entries need unique IDs; `get_next_id.py` scans the filesystem but could race. Solution: allocate ID ranges to each new-entries agent.
- **Should agents communicate?** If Agent A discovers that an entry needs cross-referencing while doing note expansion, should it signal the cross-ref agent? Or just do it?
- **What's the minimum viable system?** Could we start with just 2 parallel agents (one creating entries, one polishing) using separate ID ranges?
- **How does the curator monitor progress?** A dashboard showing agent activity, entries processed, error rates, and queue status would be essential.

## Related pages

- [Content Pipeline](../project/content-pipeline.md) — the current sequential pipeline this would replace
- [AI-Assisted Entry Review](ai-review.md) — review agents could be part of the parallel system
- [Multi-Model Proofreading](multi-model-proofreading.md) — proofreading agents running in parallel
- [Quality Standards](../project/quality-standards.md) — standards all agents must maintain
