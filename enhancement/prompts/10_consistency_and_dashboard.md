# 10 — Consistency Checker & Enhanced Dashboard

**Enhancement plan sections**: [2.3.2] Consistency Checker + [2.3.3] Enhanced Dashboard
**Depends on**: Prompt 04 (note scorer feeds consistency checker; if not yet merged, use note length as fallback)
**Estimated scope**: Medium — new consistency script + report.py enhancements + Makefile/docs updates

## What This Prompt Creates/Modifies

| Action | Path | Description |
|--------|------|-------------|
| Create | `build/check_consistency.py` | Consistency checker script with structured reporting |
| Modify | `build/report.py` | Add quality metrics sections to the health dashboard |
| Modify | `Makefile` | Add `consistency` target |
| Modify | `CLAUDE.md` | Document new commands |

---

## Part A: Build Consistency Checker [2.3.2]

**Goal**: Create `build/check_consistency.py` that detects structural and cross-entry consistency issues. This is a deterministic tool — it flags issues for semantic review, it does not fix them.

### Step A1: Understand existing overlap

Before writing the checker, read `build/find_merge_candidates.py` to understand its cross-reference asymmetry detection. The consistency checker should NOT duplicate that logic. Specifically:

- `find_merge_candidates.py` already detects: noun/する pairs missing cross-refs, homophone pairs missing cross-refs, duplicate numeric IDs, and candidate duplicates.
- The consistency checker should focus on **structural** consistency (note format, tag completeness, section presence) rather than **cross-reference** relationship detection.
- For cross-reference symmetry, the consistency checker should call or import the existing `find_merge_candidates.py` functions and summarize the counts, rather than reimplementing the logic.

### Step A2: Create `build/check_consistency.py`

Create the file at `build/check_consistency.py`. It should:

1. **Parse arguments**:
   ```python
   parser = argparse.ArgumentParser(description='Check entry consistency across the dictionary.')
   parser.add_argument('--json', action='store_true', help='Output as JSON')
   parser.add_argument('--issue', choices=[
       'note-structure', 'crossref-asymmetry', 'note-length',
       'missing-transitivity', 'no-collocations', 'example-count'
   ], help='Filter to a single issue type')
   parser.add_argument('--tier', choices=['basic', 'core', 'general'],
                        help='Filter to a single vocabulary tier')
   parser.add_argument('--fix-list', action='store_true',
                        help='Output entry IDs only (one per line), for piping to other tools')
   ```

2. **Load all entries** from the `entries/` directory (use the same pattern as `report.py` — iterate over `entries/**/*.json`).

3. **Check 1 — Note structure vs POS templates**:
   - If `build/note_templates.json` exists (created by enhancement prompt 04), load it and compare each entry's notes against the expected sections for its POS.
   - If `note_templates.json` does NOT exist, use these reasonable defaults:
     - **Verbs** (`verb-godan`, `verb-ichidan`, `verb-suru`, `verb-kuru`, `verb-irregular`): expect notes to mention at least one of: transitivity (自動詞/他動詞/transitive/intransitive), particles, collocations, aspect, similar verbs
     - **Na-adjectives** (`adjective-na`): expect notes to mention at least one of: usage, collocations, similar adjectives, predicate/modifier
     - **Nouns** (`noun`): expect notes to mention at least one of: collocations, compounds, similar words, usage
     - Other POS: no structural check (skip)
   - Flag entries where the notes contain NONE of the expected keywords for that POS.
   - Issue type: `note-structure`

4. **Check 2 — Cross-reference asymmetry** (summary only):
   - Import `find_merge_candidates` functions or run `find_merge_candidates.py --json` via subprocess and parse the output.
   - Count the total number of asymmetric cross-reference pairs (A→B without B→A).
   - Report the count and list the entry IDs involved.
   - Issue type: `crossref-asymmetry`
   - **Important**: Do NOT reimplement the cross-reference scanning logic. Reuse the existing code.

5. **Check 3 — Note length outliers**:
   - Flag entries with notes shorter than 50 characters (excluding entries with no notes at all — those are a different issue).
   - Flag entries with notes longer than 2000 characters.
   - Issue type: `note-length`
   - Report short and long separately in the output.

6. **Check 4 — Verbs missing transitivity labels**:
   - For every entry with a verb POS tag, check:
     a. Does `metadata.tags.semantic` contain "transitive" or "intransitive"?
     b. Do the notes contain any of: "自動詞", "他動詞", "transitive", "intransitive"?
   - If neither (a) nor (b), flag the entry.
   - Issue type: `missing-transitivity`

7. **Check 5 — Entries with no collocations**:
   - For entries that are verbs, na-adjectives, or nouns: check if the notes contain any of: "COLLOCATION", "collocation", "〜", or common collocation-like patterns (e.g., "Xを", "Xが", "Xに" where X is a Japanese word).
   - Flag entries where none of these patterns appear.
   - Issue type: `no-collocations`
   - This is a soft check — many entries legitimately don't need collocations. The flag helps identify candidates for enrichment.

8. **Check 6 — Example count gaps**:
   - For each entry, check the number of examples against the minimum for its tier:
     - Basic/Core: 5 examples per sense minimum
     - General: 3 examples per sense minimum
   - Count examples per sense using `sense_numbers` fields. If `sense_numbers` is missing, count total examples against `definitions` count.
   - Flag entries that fall short.
   - Issue type: `example-count`

### Step A3: Output formatting

The script should support three output modes:

**Default (human-readable)**:
```
=== CONSISTENCY REPORT ===

Note Structure Issues (N entries)
  Verbs missing expected note sections:
    00123_taberu  食べる
    00456_hashiru  走る
  Na-adjectives missing expected note sections:
    01234_shizukana  静かな

Cross-Reference Asymmetry (N asymmetric pairs)
  (Details available via: python3 build/find_merge_candidates.py --crossref-only)

Note Length Outliers
  Too short (< 50 chars): N entries
    00789_neko  猫  (32 chars)
  Too long (> 2000 chars): M entries
    01567_suru  する  (2341 chars)

Verbs Missing Transitivity (N entries)
    00234_akeru  開ける
    00567_shimeru  閉める

Entries Without Collocations (N entries)
    [list]

Example Count Gaps (N entries)
    00111_hon  本  (basic, 3 examples, needs 5)
    [list]

=== SUMMARY ===
  Note structure:        N issues
  Cross-ref asymmetry:   N pairs
  Note length outliers:  N entries
  Missing transitivity:  N entries
  No collocations:       N entries
  Example count gaps:    N entries
  TOTAL:                 N issues
```

**`--json`**: Output the full results as a JSON object with keys matching the issue types. Each issue entry should include at minimum: `entry_id`, `headword`, `tier`, and issue-specific details.

**`--fix-list`**: Output only entry IDs, one per line, suitable for piping:
```
00123_taberu
00456_hashiru
01234_shizukana
```

When `--issue` is used, only that check runs (and only its results appear). When `--tier` is used, all checks run but only entries matching that tier are reported.

### Step A4: Implementation notes

- Add `sys.path.insert(0, str(Path(__file__).parent))` at the top (same pattern as other build scripts) so imports like `japanese_utils` work.
- Use `strip_furigana` from `japanese_utils` for headword display.
- Make the script executable (`#!/usr/bin/env python3`).
- Keep the code style consistent with `report.py` and `find_merge_candidates.py` — use `pathlib.Path`, `Counter`, `defaultdict`, clear function names.
- The cross-reference asymmetry check should gracefully handle the case where `find_merge_candidates.py` is unavailable (print a warning and skip).

---

## Part B: Enhance Report Dashboard [2.3.3]

**Goal**: Add quality dimension metrics to `build/report.py` so the health dashboard reflects content quality, not just counts.

### Step B1: Read and understand report.py

Read `build/report.py` thoroughly. Note the existing report functions:
- `report_tier_breakdown`
- `report_pos_breakdown`
- `report_cross_references`
- `report_examples`
- `report_inline_links`
- `report_furigana`
- `report_recent_activity`

The new sections should follow the same coding style: standalone functions that take `entries` as a parameter and print formatted output.

### Step B2: Add cross-reference symmetry rate

Add a function `report_crossref_symmetry(entries)` that:

1. Builds a map of entry_id -> set of referenced target_ids (from `cross_references` and `prominent_see_also`).
2. Counts the total number of directed references (A→B).
3. Counts symmetric pairs (where both A→B and B→A exist).
4. Reports:
   ```
   CROSS-REFERENCE SYMMETRY
   ----------------------------------------
     Total directed references:     NNNN
     Symmetric pairs:               NNNN
     Asymmetric references:         NNNN
     Symmetry rate:                 NN.N%
   ```

**Important**: This overlaps with `find_merge_candidates.py`'s asymmetry detection. However, in the dashboard it should be a lightweight count (not a full report), so reimplement the counting logic simply rather than importing/running the other script. The dashboard should be self-contained and fast.

### Step B3: Add note quality summary

Add a function `report_note_quality(entries)` that:

1. First checks if `build/score_note_quality.py` exists (from enhancement prompt 04):
   - If it exists, try to import it and use its scoring function to report score distribution.
   - If it does NOT exist, fall back to note length statistics.

2. **Fallback mode (note length by POS)**:
   - Group entries by primary POS tag.
   - For each POS, compute: entries with notes, average note length, median note length.
   - Report:
     ```
     NOTE QUALITY (by length)
     ----------------------------------------
       POS                  With Notes   Avg Length   Median
       verb-godan              1234         312        280
       verb-ichidan             567         298        265
       noun                    3456         245        220
       adjective-na             234         267        240
       ...
       Entries without notes:    N
     ```

3. **Scorer mode** (if `score_note_quality.py` exists):
   - Import the scorer module and run it on all entries.
   - Report score distribution in buckets (0-20, 21-40, 41-60, 61-80, 81-100).
   - Report average score by POS.

### Step B4: Add polishing completion percentages

Add a function `report_polishing_progress(project_root)` that:

1. Scans `polishing/tasks/*/progress.txt` for all polishing tasks.
2. For each task:
   - Reads the `next:` value from the progress file.
   - Determines the total number of entries (from `len(entries)` or by counting files in `entries/`).
   - Calculates approximate completion percentage: `(next_id / max_id) * 100`.
3. Reports:
   ```
   POLISHING PROGRESS
   ----------------------------------------
     Task                     Progress    Next Entry
     inline-links              45.2%      10500
     example-sentences          32.1%      07500
     furigana-completeness      67.8%      15800
     furigana-correctness       12.3%      02900
     semantic-labels            55.0%      12800
   ```

Note: This function takes `project_root` as a parameter (not `entries`), since it reads from the filesystem.

### Step B5: Add POS section completeness

Add a function `report_pos_completeness(entries)` that:

1. For verb entries, counts:
   - With transitivity info (in tags or notes)
   - With aspect/ている documentation (notes contain "ASPECT" or "ている")
   - With collocations (notes contain collocation patterns)
   - With conjugation data (has `conjugation` field)

2. For na-adjective entries, counts:
   - With collocations
   - With conjugation data

3. Reports:
   ```
   POS SECTION COMPLETENESS
   ----------------------------------------
     Verbs (NNNN total):
       With transitivity:       NNNN (NN.N%)
       With ている docs:        NNNN (NN.N%)
       With collocations:       NNNN (NN.N%)
       With conjugation:        NNNN (NN.N%)
     Na-adjectives (NNN total):
       With collocations:       NNN (NN.N%)
       With conjugation:        NNN (NN.N%)
   ```

### Step B6: Add candidate queue health

Add a function `report_candidate_health(project_root)` that:

1. Loads `candidate_words.json`.
2. Reports:
   - Total candidates in queue.
   - If candidates have a `date_added` or similar timestamp field, report the oldest candidate age. If not, just report the count.
   - Breakdown by any available categorization (POS, source, etc.) — adapt to whatever fields actually exist in the candidate data.
3. Reports:
   ```
   CANDIDATE QUEUE
   ----------------------------------------
     Total candidates:          NNNN
     [Additional breakdowns if data supports it]
   ```

### Step B7: Add consistency summary

Add a function `report_consistency_summary(project_root)` that:

1. Tries to run `python3 build/check_consistency.py --json` via subprocess.
2. If it succeeds, parses the JSON output and reports a one-line summary per issue type.
3. If it fails (script not yet created, or errors), prints a note saying the consistency checker is not available.
4. Reports:
   ```
   CONSISTENCY SUMMARY
   ----------------------------------------
     Note structure issues:     NNN
     Cross-ref asymmetry:       NNN pairs
     Note length outliers:      NNN
     Missing transitivity:      NNN
     No collocations:           NNN
     Example count gaps:        NNN
     (Full report: python3 build/check_consistency.py)
   ```

### Step B8: Integrate new sections into main()

In `report.py`'s `main()` function, add calls to the new report functions AFTER the existing sections but BEFORE `report_recent_activity` (which should remain last as the most time-sensitive section).

The order should be:
1. (existing) Tier breakdown
2. (existing) POS breakdown
3. (existing) Cross-references
4. **NEW** Cross-reference symmetry
5. (existing) Examples
6. (existing) Inline links
7. (existing) Furigana
8. **NEW** Note quality
9. **NEW** POS section completeness
10. **NEW** Polishing progress
11. **NEW** Candidate queue health
12. **NEW** Consistency summary
13. (existing) Recent activity

Pass `project_root` to functions that need filesystem access (polishing progress, candidate health, consistency summary). The others receive `entries`.

---

## Part C: Integration

### Step C1: Add Makefile target

Add the following to the Makefile:

```makefile
consistency:
	python3 build/check_consistency.py
```

Add `consistency` to the `.PHONY` line at the top of the Makefile.

### Step C2: Update CLAUDE.md

In the "Essential commands" section, add:

```bash
python3 build/check_consistency.py            # Check entry consistency across the dictionary
python3 build/check_consistency.py --json      # Machine-readable consistency report
python3 build/check_consistency.py --fix-list  # Entry IDs only (for piping)
make consistency                               # Run consistency checker
```

In the "Essential commands" section, update the `make report` description (if it has one) to note that it now includes quality metrics.

---

## Verification

After all parts are complete, run these checks:

```bash
# Verify check_consistency.py runs without errors
python3 build/check_consistency.py

# Verify JSON output mode works
python3 build/check_consistency.py --json | python3 -c "import sys, json; json.load(sys.stdin); print('JSON output valid')"

# Verify fix-list mode works
python3 build/check_consistency.py --fix-list | head -5

# Verify issue filter works
python3 build/check_consistency.py --issue note-length

# Verify tier filter works
python3 build/check_consistency.py --tier basic

# Verify the enhanced report runs
python3 build/report.py

# Verify Makefile target works
make consistency

# Full validation still passes
make validate
```

Fix any errors found during verification.

---

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow."

1. **Run `make build`** to ensure all build artifacts are up to date
2. **Create a feature branch, stage, and commit all changes**:
   ```bash
   git checkout -b enhancement/10-consistency-dashboard
   git add -A
   git commit -m "Add consistency checker and enhance report dashboard [2.3.2, 2.3.3]

   - Create build/check_consistency.py with 6 issue type checks
   - Extend build/report.py with quality metrics (symmetry, note quality, polishing
     progress, POS completeness, candidate health, consistency summary)
   - Add make consistency target
   - Update CLAUDE.md with new commands"
   ```
3. **Push** to the feature branch:
   ```bash
   git push -u origin enhancement/10-consistency-dashboard
   ```
4. **Create a PR**:
   ```bash
   gh pr create --repo tkgally/je-dict-1 \
     --head enhancement/10-consistency-dashboard \
     --base main \
     --title "Consistency checker + enhanced dashboard [2.3.2, 2.3.3]" \
     --body "$(cat <<'EOF'
   ## Summary
   - New `build/check_consistency.py` script that checks entry consistency across 6 dimensions: note structure vs POS templates, cross-reference asymmetry, note length outliers, verbs missing transitivity, entries without collocations, and example count gaps
   - Enhanced `build/report.py` dashboard with quality metrics: cross-reference symmetry rate, note quality distribution, polishing progress percentages, POS section completeness, candidate queue health, and consistency summary
   - New `make consistency` Makefile target
   - Updated CLAUDE.md documentation

   Implements enhancement plan sections [2.3.2] and [2.3.3].

   ## Test plan
   - [ ] `python3 build/check_consistency.py` runs without errors
   - [ ] `python3 build/check_consistency.py --json` produces valid JSON
   - [ ] `python3 build/check_consistency.py --fix-list` outputs entry IDs only
   - [ ] `python3 build/check_consistency.py --issue note-length` filters correctly
   - [ ] `python3 build/check_consistency.py --tier basic` filters correctly
   - [ ] `python3 build/report.py` runs with all new sections
   - [ ] `make consistency` works
   - [ ] `make validate` passes
   - [ ] `make build` succeeds
   EOF
   )"
   ```
5. **Poll CI status** every 60 seconds: `gh pr checks <number> --repo tkgally/je-dict-1` (allow up to 10 minutes)
6. **Squash-merge** once CI is green: `gh pr merge <number> --repo tkgally/je-dict-1 --squash`
7. **If CI fails**: read logs with `gh run view <run_id> --repo tkgally/je-dict-1 --log-failed`, fix, push, and repeat from step 5
8. **Post-merge cleanup**:
   ```bash
   git checkout main && git pull origin main
   git status  # Should show nothing to commit
   git branch -d enhancement/10-consistency-dashboard
   git push origin --delete enhancement/10-consistency-dashboard
   ```

**CRITICAL**: The PR must include rebuilt `docs/` files from `make build`. If you commit source changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.
