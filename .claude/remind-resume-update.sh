#!/bin/bash
# Hook to remind about updating RESUME_semantic_assignment.md before context compaction

echo ""
echo "=== REMINDER: SEMANTIC ASSIGNMENT TASK ==="
echo "Before ending work on a directory (ka/, sa/, ta/, etc.):"
echo "1. Commit all changes"
echo "2. Update RESUME_semantic_assignment.md with:"
echo "   - Current multi-sense entry count for completed directory"
echo "   - Next directory to process"
echo "   - Any entries flagged for review"
echo ""
echo "Current multi-sense counts:"
for dir in ka sa ta na ha ma ya ra wa; do
    count=$(grep -l '"sense_numbers": \[\]' /home/user/je-dict-1/entries/$dir/*/*.json 2>/dev/null | wc -l)
    echo "  $dir/: $count remaining"
done
echo "============================================"
