# Continue Dictionary Polishing

Continue the systematic polishing of dictionary entries. Review approximately 100 entries in this session, following the full-review task.

## Quick Context

```bash
# Check current progress
python3 -c "import json; p=json.load(open('polishing/progress.json')); print(f\"Reviewed: {p['statistics']['reviewed']}/{p['statistics']['total_entries']}\")"

# Find next entry to review
python3 -c "import json; p=json.load(open('polishing/progress.json')); print('Next entry:', p.get('entries', {}).get('last_reviewed_entry', 'Check session logs'))"
```

Read the most recent session log in `polishing/sessions/` to get the exact continuation point.

## Workflow

1. **Load the polish-entries skill** for detailed review guidelines

2. **Read the latest session file** in `polishing/sessions/` to find:
   - The next entry number to start from
   - Context and patterns from the previous session
   - Any pending tasks

3. **Review entries** following the full-review task in `polishing/tasks/full-review.md`:
   - Check all fields against quality standards
   - Fix minor issues directly (furigana, formatting, tag errors)
   - Flag major issues in `polishing/issues.json`
   - Update `modified` timestamp on any changed entries

4. **After reviewing all entries**:
   ```bash
   python3 build/validate.py              # Verify no errors introduced
   python3 build/validate_tags.py         # Check tag consistency
   python3 build/update_indexes.py        # Sync indexes
   python3 build/build_flat.py            # Build static site
   ```

5. **Update tracking files**:
   - `polishing/progress.json`: Add reviewed entries to the entries object, update statistics
   - `polishing/sessions/`: Create new session log with changes summary
   - Update `review_history` array in progress.json

6. **Commit and push** with a descriptive message

## Key Reminders

- **Target: ~100 entries** per session (adjustable based on issue density)
- **Update timestamps**: Use `python3 build/get_timestamp.py` when modifying entries
- **Track all changes**: Record every modification in your session log
- **Cross-reference targets**: If a reference target doesn't exist, add to candidates:
  ```bash
  python3 build/manage_candidates.py add "headword" "reading" "brief note"
  ```
- **Focus areas from previous sessions**:
  - Politeness/formality accuracy (word's inherent register vs usage context)
  - Semantic tag appropriateness
  - Suffix entries should have 'grammatical' semantic tag

## Output

At session end, provide:
1. Entry range reviewed (e.g., "00631-00830")
2. Number of entries modified
3. Summary of change types
4. Any patterns or issues discovered
5. Continuation notes for the next session
