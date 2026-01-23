# Continue Dictionary Polishing

Continue the systematic polishing of dictionary entries. Review approximately 10 entries per batch, following the full-review task. This workflow loops continuously—after each batch, check your remaining context and either process another batch directly or perform a context reset to continue working.

**Important**: Continue working until either:
1. The user tells you to stop, OR
2. You reach the target number of entries specified by the user at session start

Do NOT stop just because context is running low—use the context reset procedure instead.

## Quick Context

```bash
# Check current progress
python3 -c "import json; p=json.load(open('polishing/progress.json')); print(f\"Reviewed: {p['statistics']['reviewed']}/{p['statistics']['total_entries']}\")"

# Find next entry to review
python3 -c "import json; p=json.load(open('polishing/progress.json')); print('Next entry:', p.get('entries', {}).get('last_reviewed_entry', 'Check session logs'))"
```

Read the most recent session log in `polishing/sessions/` to get the exact continuation point.

## Workflow

1. **Load skills** for detailed guidelines:
   - **polish-entries**: General review guidelines
   - **example-sentences**: Example sentence requirements (counts, vocabulary tiers, length progression)

2. **Read the latest session file** in `polishing/sessions/` to find:
   - The next entry number to start from
   - Context and patterns from the previous session
   - Any pending tasks

3. **Review entries** following the full-review task in `polishing/tasks/full-review.md`:
   - Check all fields against quality standards
   - Fix minor issues directly (furigana, formatting, tag errors)
   - **Check and fix example sentences** (see Example Sentence Requirements below)
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

6. **Commit changes** with a descriptive message (do NOT push yet)

7. **Check remaining context** using `/context` command:
   - **If 30% or more context remains**: Return to step 2 and process another batch of ~10 entries
   - **If less than 30% context remains**: Proceed to step 8 for context reset

8. **Context Reset Procedure** (when context < 30%):

   a. **Update session log** in `polishing/sessions/` with:
      - Entry range processed in this context window
      - Summary of all modifications made
      - Any patterns or issues discovered
      - The exact next entry number to continue from

   b. **Create a context summary** by writing a brief note at the end of the session log:
      ```
      ## Context Continuation Note
      - Last entry reviewed: [entry_id]
      - Next entry to process: [entry_id]
      - Target remaining: [X entries until goal / or "until user stops"]
      - Key patterns to remember: [brief notes]
      ```

   c. **Commit all pending changes**:
      ```bash
      git add -A && git commit -m "Polish entries XXXXX-XXXXX (batch N)"
      ```

   d. **Clear context and continue** using the `/compact` command to summarize and clear context

   e. **Reread this prompt** to restore your working instructions:
      - Read `prompts/continue_polishing.md`
      - Read the latest session log in `polishing/sessions/`
      - Load the skills: `polish-entries` and `example-sentences`

   f. **Resume from step 2** and continue processing entries

9. **Final PR** (only when target is reached OR user requests stop):
   - Push all commits: `git push -u origin <branch-name>`
   - Create a PR summarizing all batches processed
   - Include total entry range, total modifications, and key patterns discovered

## Example Sentence Requirements

During polishing, check and fix example sentences according to the `example-sentences` skill guidelines.

### Minimum Counts by Tier

| Tier | Min Examples per Sense |
|------|------------------------|
| Basic | 5 |
| Core | 5 |
| General | 3 |

If an entry doesn't meet the minimum, **write new examples** to reach the requirement.

### Vocabulary Restrictions

| Tier | Examples 1-2 | Examples 3+ |
|------|-------------|-------------|
| **Basic** | Basic vocab only | Basic + Core only |
| **Core** | Basic + Core only | No restriction |
| **General** | No restriction | No restriction |

**Critical**: In basic-tier entries, examples 1-2 cannot contain general-tier or unlisted vocabulary. Use `python3 build/check_duplicate.py "word" "reading"` to verify vocabulary tiers.

### Progressive Length

Examples should progress from shorter to longer within each sense:
1. Short (5-15 chars)
2. Short-medium (10-20 chars)
3. Medium (15-30 chars)
4. Medium-long (25-45 chars)
5. Long or multi-sentence (35-70 chars)

Reorder or revise examples if length progression is missing.

### Quality Checklist

- [ ] All kanji have furigana: `{kanji|reading}`
- [ ] `sense_numbers` correctly reference definitions
- [ ] IDs follow format: `{entry_id}_ex{N}`
- [ ] IDs are sequential (ex1, ex2, ex3...)
- [ ] At least one example shows a common collocation per sense
- [ ] Translations are natural (not overly literal)

### Common Fixes

- **Insufficient examples**: Add new examples following vocabulary restrictions and length progression
- **Vocabulary violation**: Replace non-compliant words (e.g., {購入|こうにゅう}する → {買|か}う)
- **No length progression**: Reorder or revise examples
- **Missing furigana**: Add `{kanji|reading}` markup

## Key Reminders

- **Target: ~10 entries per batch** (adjustable based on issue density)
- **Never stop for context**: Use context reset procedure to continue indefinitely
- **Stop conditions**: Only stop when user requests OR target entry count is reached
- **Update timestamps**: Use `python3 build/get_timestamp.py` when modifying entries
- **Track all changes**: Record every modification in your session log
- **Session logs are critical**: They preserve your progress across context resets
- **Cross-reference targets**: If a reference target doesn't exist, add to candidates:
  ```bash
  python3 build/manage_candidates.py add "headword" "reading" "brief note"
  ```
- **Focus areas for polishing**:
  - Politeness/formality accuracy (word's inherent register vs usage context)
  - Semantic tag appropriateness
  - Suffix entries should have 'grammatical' semantic tag
  - **Example sentence compliance** (counts, vocabulary tiers, length progression)

## Output

At session end (when target reached or user stops), provide:
1. Total entry range reviewed across all batches (e.g., "00631-01230")
2. Number of batches processed and context resets performed
3. Total number of entries modified
4. Summary of change types across all batches
5. Any patterns or issues discovered
6. Continuation notes for the next session (if not complete)
