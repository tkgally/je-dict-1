#!/bin/bash

LOG_FILE="inline-links-batch-$(date +%Y%m%d-%H%M%S).log"

for i in {1..10}; do
  echo "=== Starting iteration $i of 10 at $(date) ===" | tee -a "$LOG_FILE"
  claude --print "$(cat prompts/polish_add_inline_links.md)" 2>&1 | tee -a "$LOG_FILE"
  
  if [ $? -ne 0 ]; then
    echo "Error in iteration $i, stopping" | tee -a "$LOG_FILE"
    exit 1
  fi
  
  echo "=== Completed iteration $i ===" | tee -a "$LOG_FILE"
done

echo "=== All 10 iterations complete ===" | tee -a "$LOG_FILE"
