#!/bin/bash
# General-purpose pre-compact reminder
# Runs before context compaction to ensure work is saved

echo ""
echo "=== PRE-COMPACT REMINDER ==="
echo "Before context compacts, make sure you have:"
echo ""
echo "1. Updated progress tracking:"
echo "   - prompts/refactoring/progress.json (if doing refactoring tasks)"
echo "   - PROJECT_STATUS.md (if significant changes were made)"
echo ""
echo "2. Written a session log if one is expected"
echo ""
echo "3. Committed all changes:"
echo "   - git add the files you changed"
echo "   - git commit with a descriptive message"
echo "   - git push if on a feature branch"
echo "==============================="
echo ""
