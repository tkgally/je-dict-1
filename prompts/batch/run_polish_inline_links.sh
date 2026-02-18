#!/bin/bash
# run_polish_inline_links.sh — Add inline word links to entries in batches
# Each run processes entries from where the last left off (progress-tracked).
# Default: 10 runs. Change TOTAL_RUNS below to adjust.

set -euo pipefail

TOTAL_RUNS=10
PROJECT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$PROJECT_DIR"

PROMPT="Read prompts/polish_add_inline_links.md and follow the instructions."
LOG_FILE="prompts/batch/logs/polish_inline_links_$(date +%Y%m%d_%H%M%S).log"

mkdir -p prompts/batch/logs

echo "=== Polish Inline Links Batch — $TOTAL_RUNS runs ===" | tee "$LOG_FILE"
echo "Started: $(date)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

completed=0
failed=0

for i in $(seq 1 "$TOTAL_RUNS"); do
    echo "--- Run $i of $TOTAL_RUNS ---" | tee -a "$LOG_FILE"
    echo "Started: $(date)" | tee -a "$LOG_FILE"

    RUN_LOG="prompts/batch/logs/polish_inline_links_run${i}_$(date +%Y%m%d_%H%M%S).log"
    if script -q "$RUN_LOG" claude -p "$PROMPT"; then
        cat "$RUN_LOG" >> "$LOG_FILE"
        if ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git ls-files --others --exclude-standard)" ]; then
            git add -A
            git commit -m "Polish inline links — batch run $i of $TOTAL_RUNS ($(date +%Y-%m-%d))"
            echo "Committed changes from run $i." | tee -a "$LOG_FILE"
            completed=$((completed + 1))
        else
            echo "No changes in run $i — skipping commit." | tee -a "$LOG_FILE"
            completed=$((completed + 1))
        fi
    else
        cat "$RUN_LOG" >> "$LOG_FILE" 2>/dev/null
        failed=$((failed + 1))
        echo "ERROR: Run $i failed (exit code $?)." | tee -a "$LOG_FILE"
        echo "Stopping batch to avoid cascading errors." | tee -a "$LOG_FILE"
        break
    fi

    echo "Completed: $(date)" | tee -a "$LOG_FILE"
    echo "" | tee -a "$LOG_FILE"
done

echo "=== Batch complete ===" | tee -a "$LOG_FILE"
echo "Completed: $completed / $TOTAL_RUNS runs" | tee -a "$LOG_FILE"
echo "Failed: $failed" | tee -a "$LOG_FILE"
echo "Finished: $(date)" | tee -a "$LOG_FILE"
echo "Log: $LOG_FILE"
