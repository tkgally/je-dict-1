# Enhancement: Automated Orchestration

**Enhancement plan section**: [2.2.3] Automated Orchestration

**Depends on**: Prompt 13 (Claim-Based Task Queue must be operational)

## What This Prompt Creates/Modifies

| Artifact | Action |
|----------|--------|
| `pipeline/orchestrator.py` | **Create** — launches and monitors parallel Claude sessions |
| `pipeline/pipeline-config.json` | **Modify** — add parallel task slot configuration |
| `pipeline/monitor.py` | **Create** — real-time monitoring dashboard |
| `pipeline/budget.json` | **Create** — daily budget cap configuration |
| `build/report.py` | **Modify** — add queue status and agent activity metrics |
| `CLAUDE.md` | **Modify** — document orchestration system |

## Overview

Build an orchestrator that launches multiple Claude CLI sessions on a schedule without curator initiation. Sessions draw from the task queue (prompt 13), process entries, and commit results. A monitoring dashboard tracks throughput and costs.

## Prerequisites

Before starting, verify:
```bash
# Task queue must exist and be functional
python3 pipeline/task_queue.py status
```

If the task queue is not operational, stop and report that prompt 13 must be completed first.

## Implementation Steps

### Part A: Extend Pipeline Configuration

Read `pipeline/pipeline-config.json` and add parallel task slot support:

```json
{
  "parallel_slots": [
    {
      "id": "slot-1",
      "task_type": "furigana",
      "prompt": "prompts/polish_furigana_completeness.md",
      "batch_size": 50,
      "enabled": true
    },
    {
      "id": "slot-2",
      "task_type": "notes",
      "prompt": "prompts/expand-short-notes.md",
      "batch_size": 25,
      "enabled": true
    },
    {
      "id": "slot-3",
      "task_type": "cross_refs",
      "prompt": "prompts/add_cross-references.md",
      "batch_size": 15,
      "enabled": false
    },
    {
      "id": "slot-4",
      "task_type": "examples",
      "prompt": "prompts/polish_example_sentences.md",
      "batch_size": 20,
      "enabled": false
    }
  ],
  "schedule": {
    "max_concurrent": 2,
    "daily_budget_usd": 50.0,
    "cooldown_minutes": 5,
    "max_runs_per_day": 10
  },
  "coordinator": {
    "post_session_build": true,
    "auto_merge": false,
    "notify_on_failure": true
  }
}
```

### Part B: Build Orchestrator Script

Create `pipeline/orchestrator.py` that:

1. **Reads configuration** from `pipeline/pipeline-config.json`
2. **Checks budget** against `pipeline/budget.json`:
   ```json
   {
     "daily_limit_usd": 50.0,
     "spent_today_usd": 0.0,
     "last_reset": "2026-04-09",
     "session_log": []
   }
   ```
   - Resets daily spend at midnight UTC
   - Refuses to launch if daily limit would be exceeded (estimate cost per session)
3. **Claims tasks** from the task queue for each enabled slot:
   ```bash
   python3 pipeline/task_queue.py claim --task-type TYPE --count BATCH_SIZE --session-id SLOT_ID
   ```
4. **Launches Claude CLI sessions** for each slot:
   ```bash
   claude -p "Read PROMPT_FILE and process entries: ID1, ID2, ..." --verbose
   ```
   - Each session runs on its own branch (e.g., `auto/slot-1-20260409-001`)
   - Captures output to `pipeline/logs/slot-{id}_{timestamp}.log`
5. **Monitors running sessions**:
   - Tracks which slots are active
   - Detects completion or failure
   - Enforces max_concurrent limit
6. **Post-session coordination** (when a session completes):
   - Validates the branch: `python3 build/validate.py --changed-only`
   - If valid and auto_merge enabled: merge to main
   - If valid and auto_merge disabled: create PR for curator review
   - If invalid: log error, release claimed tasks back to queue
   - Run `make build` on main after merge
7. **Supports commands**:
   - `start`: Begin orchestration loop
   - `stop`: Gracefully stop (finish current sessions, don't start new ones)
   - `status`: Show running sessions, queue status, budget
   - `--dry-run`: Show what would happen without launching sessions

### Part C: Build Monitoring Dashboard

Create `pipeline/monitor.py` that provides real-time status:

1. **Queue status**: pending/in-progress/completed per task type
2. **Active sessions**: which slots are running, entry IDs being processed
3. **Throughput**: entries processed per hour (rolling average)
4. **Budget**: spent today vs. daily limit
5. **Error rate**: failed sessions / total sessions
6. **Recent activity**: last 10 completed sessions with entry counts

Output as formatted terminal report. Support `--json` for machine-readable output.

### Part D: Extend Report Dashboard

Add to `build/report.py`:
- Queue status section (from task_queue.py status)
- Agent activity metrics (from pipeline logs)
- Entries processed per day trend
- Error rates

### Part E: Create Budget Configuration

Create `pipeline/budget.json` with sensible defaults:
```json
{
  "daily_limit_usd": 50.0,
  "spent_today_usd": 0.0,
  "last_reset": "2026-04-09",
  "session_log": [],
  "estimated_cost_per_session_usd": 2.0
}
```

### Part F: Add Makefile Targets

```makefile
orchestrate:
	python3 pipeline/orchestrator.py start

orchestrate-status:
	python3 pipeline/orchestrator.py status

orchestrate-stop:
	python3 pipeline/orchestrator.py stop

monitor:
	python3 pipeline/monitor.py
```

### Part G: Safety Measures

The orchestrator must include these safeguards:
1. **Budget enforcement**: Hard stop when daily limit reached
2. **Error circuit breaker**: If 3 consecutive sessions fail, pause and notify
3. **Lock file**: `pipeline/orchestrator.lock` prevents multiple orchestrator instances
4. **Graceful shutdown**: SIGINT/SIGTERM handler finishes current sessions
5. **Audit trail**: All actions logged to `pipeline/logs/orchestrator_{date}.log`

### Part H: Documentation

Update CLAUDE.md:
- Add orchestrator to project structure
- Document orchestrator commands
- Add to essential commands section
- Note that auto_merge defaults to false (curator review required)

## Testing

```bash
# Verify configuration is valid
python3 pipeline/orchestrator.py --dry-run

# Check queue has tasks to process
python3 pipeline/task_queue.py status

# Run monitor
python3 pipeline/monitor.py

# Verify report includes new metrics
make report
```

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md:

1. **Run `make build`** to regenerate all build artifacts
2. **Commit ALL changes**:
   ```bash
   git add -A && git commit -m "Add automated orchestration system

   Creates orchestrator for parallel Claude sessions with budget caps,
   monitoring dashboard, and safety measures. Extends pipeline config
   for multi-slot parallel execution. Enhancement plan [2.2.3]."
   ```
3. **Push** to the feature branch
4. **Create PR** with description of the orchestration system
5. **Poll CI** every 60 seconds (up to 10 minutes)
6. **Squash-merge** once CI is green
7. **If CI fails**: read logs, fix, push, repeat
8. **Post-merge cleanup**: switch to main, pull, verify clean, delete feature branch locally and remotely
