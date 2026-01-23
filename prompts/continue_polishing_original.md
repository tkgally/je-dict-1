# Continue Dictionary Polishing

Continue the systematic polishing of dictionary entries. Review approximately 10 entries per batch, following the full-review task. This workflow loops automatically—after each batch, check your remaining context and either process another batch or create a PR.

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
   - **Verify semantic tags** match the word's actual meaning (watch for template artifacts like "building", "transportation" on unrelated words)
   - **Check and fix example sentences** (see Example Sentence Requirements below)
   - Flag major issues in `polishing/issues.json`
   - **CRITICAL: Update `modified` timestamp for EACH modified entry individually**:
     ```bash
     # Run this IMMEDIATELY BEFORE saving each entry you modify
     python3 build/get_timestamp.py
     ```
     Every modified entry must have its own unique timestamp. Do NOT reuse a single timestamp for multiple entries.

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
   - **If less than 30% context remains**: Proceed to step 8 to create PR

8. **Create PR** (only when context < 30%):
   - Push all commits from this session: `git push -u origin <branch-name>`
   - Create a PR summarizing all batches processed in this session
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
- **Context loop**: Keep processing batches until context drops below 30%
- **TIMESTAMPS ARE PER-ENTRY**: Run `python3 build/get_timestamp.py` immediately before saving EACH modified entry. Never batch timestamps—each modified entry needs its own unique timestamp.
- **Track all changes**: Record every modification in your session log
- **Verify ALL fields, not just examples**: Check semantic tags, formality, politeness for accuracy
- **Cross-reference targets**: If a reference target doesn't exist, add to candidates:
  ```bash
  python3 build/manage_candidates.py add "headword" "reading" "brief note"
  ```
- **Focus areas for polishing**:
  - Politeness/formality accuracy (word's inherent register vs usage context)
  - Semantic tag appropriateness (must match word meaning, not copied from templates)
  - Suffix entries should have 'grammatical' semantic tag
  - **Example sentence compliance** (counts, vocabulary tiers, length progression)

## Output

At session end (when creating PR), provide:
1. Total entry range reviewed across all batches (e.g., "00631-01230")
2. Number of batches processed in this session
3. Total number of entries modified
4. Summary of change types across all batches
5. Any patterns or issues discovered
6. Continuation notes for the next session
