#!/bin/bash
# run_corpus_harvesting.sh — Process corpus words into candidates in batches
# Each run processes ~150 words from corpus_extracted_words.json.
# Default: 10 runs. Change TOTAL_RUNS below to adjust.

set -euo pipefail

TOTAL_RUNS=10
PROJECT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$PROJECT_DIR"

PROMPT="Read prompts/corpus_harvesting.md and follow the instructions."
LOG_FILE="prompts/batch/logs/corpus_harvesting_$(date +%Y%m%d_%H%M%S).log"

mkdir -p prompts/batch/logs

echo "=== Corpus Harvesting Batch — $TOTAL_RUNS runs ===" | tee "$LOG_FILE"
echo "Started: $(date)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

completed=0
failed=0

for i in $(seq 1 "$TOTAL_RUNS"); do
    echo "--- Run $i of $TOTAL_RUNS ---" | tee -a "$LOG_FILE"
    echo "Started: $(date)" | tee -a "$LOG_FILE"

    RUN_LOG="prompts/batch/logs/corpus_harvesting_run${i}_$(date +%Y%m%d_%H%M%S).log"
    if claude -p "$PROMPT" --verbose 2>&1 | tee "$RUN_LOG"; then
        cat "$RUN_LOG" >> "$LOG_FILE"
        if ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git ls-files --others --exclude-standard)" ]; then
            git add -A
            git commit -m "Corpus harvesting — batch run $i of $TOTAL_RUNS ($(date +%Y-%m-%d))"
            echo "Committed changes from run $i." | tee -a "$LOG_FILE"
            completed=$((completed + 1))
        else
            echo "No changes in run $i — skipping commit." | tee -a "$LOG_FILE"
            completed=$((completed + 1))
        fi
    else
        cat "$RUN_LOG" >> "$LOG_FILE"
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
