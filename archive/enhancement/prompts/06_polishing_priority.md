# Polishing Priority Reordering

**Enhancement plan section**: [2.1.2] Polishing Priority Reordering

Build a priority scoring system so polishing tasks process the worst entries first instead of sequentially by ID. Update all polishing prompts to use priority files when available.

## What This Prompt Creates/Modifies

| File | Action | Purpose |
|------|--------|---------|
| `build/prioritize_polishing.py` | **Create** | Score entries and generate per-task priority-ordered lists |
| `polishing/priority/` | **Create** (directory + files) | Priority-ordered entry ID lists per task |
| `prompts/polish_add_inline_links.md` | **Modify** | Add priority file support |
| `prompts/polish_example_sentences.md` | **Modify** | Add priority file support |
| `prompts/polish_furigana_completeness.md` | **Modify** | Add priority file support |
| `prompts/polish_furigana_correctness.md` | **Modify** | Add priority file support |
| `prompts/polish_semantic_labels.md` | **Modify** | Add priority file support |
| `Makefile` | **Modify** | Add `priorities` target |
| `CLAUDE.md` | **Modify** | Document the priority system and new commands |

**Depends on**: Prompt 04 (note quality scorer). If `build/score_note_quality.py` does not exist when this prompt runs, the note quality dimension will use a simple length-based heuristic instead. This is a graceful fallback, not a hard dependency.

---

## Part A: Build prioritize_polishing.py [2.1.2]

**Goal**: Create a script that scores every entry across multiple quality dimensions and generates priority-ordered lists for each polishing task.

### Step A1: Read existing scoring/reporting infrastructure

```bash
# Understand what utilities are available
cat build/report.py | head -50
cat build/japanese_utils.py | head -50
ls build/score_note_quality.py 2>/dev/null && echo "Note scorer exists" || echo "Note scorer NOT found (will use fallback)"
```

### Step A2: Create `build/prioritize_polishing.py`

Create the script at `build/prioritize_polishing.py`. It should:

1. **Load all entries** from entry files in the `entries/` directory (load the actual JSON, not just the index).

2. **Score each entry across five quality dimensions** (each dimension scores 0.0 to 1.0, where 0.0 = worst quality / highest priority for work):

#### Dimension 1: Note quality

- If `build/score_note_quality.py` exists, import and use its scoring function to get a 0-100 score, then normalize to 0.0-1.0.
- **Fallback** (if scorer not available): Use a simple length heuristic:
  - `notes` is null or empty: 0.0
  - `notes` length < 50 chars: 0.1
  - `notes` length < 100 chars: 0.3
  - `notes` length < 200 chars: 0.5
  - `notes` length < 400 chars: 0.7
  - `notes` length >= 400 chars: 0.9

#### Dimension 2: Furigana coverage

Check the `notes` field for bare kanji (kanji characters not inside `{...|...}` markup):
- Use the `is_kanji` and `FURIGANA_PATTERN` utilities from `build/japanese_utils.py`
- Strip all furigana-marked text, then check if any kanji remain
- Also check example sentences the same way
- Score:
  - No notes and no examples: 0.5 (neutral)
  - All kanji covered in all fields: 1.0
  - Any bare kanji found: 0.0

#### Dimension 3: Example count

Compare the number of examples to the minimum requirement:
- Determine the minimum per the entry's tier: basic/core = 5 per sense, general = 3 per sense
- Count senses from the `senses` array length (or default to 1)
- Count examples from the `examples` array length
- Score = min(1.0, example_count / (min_per_sense * sense_count))
- If no examples at all: 0.0

#### Dimension 4: Cross-reference count

- Count `prominent_see_also` + `cross_references` entries
- Score:
  - 0 references: 0.0
  - 1 reference: 0.3
  - 2 references: 0.6
  - 3+ references: 1.0

#### Dimension 5: Verb-specific: transitivity info

Only for entries where `part_of_speech` contains "verb":
- Check if `notes` contains any of: `transitive`, `intransitive`, `自動詞`, `他動詞`, `TRANSITIVITY`
- Score: 1.0 if present, 0.0 if absent
- For non-verb entries: score = 1.0 (not applicable, no penalty)

3. **Combine dimensions into task-specific priority scores**.

Each polishing task cares about different dimensions. The priority score is:

```
priority = tier_weight * (1.0 - relevant_quality_score)
```

Where `tier_weight` is:
- basic: 3.0
- core: 2.0
- general: 1.0

And the relevant quality score depends on the task:

| Task | Primary dimension | Weight | Secondary dimension | Weight |
|------|-------------------|--------|---------------------|--------|
| notes | note_quality | 0.8 | cross_refs | 0.2 |
| furigana | furigana_coverage | 1.0 | (none) | - |
| examples | example_count | 0.9 | note_quality | 0.1 |
| cross_refs | cross_ref_count | 0.7 | transitivity_info | 0.3 |

The quality score for each task = weighted sum of its dimensions (0.0 to 1.0).
Then: `priority = tier_weight * (1.0 - quality_score)`.
Higher priority number = more urgent to fix.

4. **Generate priority files**.

For each task, sort entries by priority score descending (highest priority first) and write the entry IDs to a file, one per line:

```
polishing/priority/notes.txt
polishing/priority/furigana.txt
polishing/priority/examples.txt
polishing/priority/cross_refs.txt
```

Each file format:
```
# Generated by prioritize_polishing.py on YYYY-MM-DD
# Task: notes
# Total entries: XXXXX
# Entries with priority > 0: XXXXX
XXXXX_word
XXXXX_word
XXXXX_word
...
```

Only include entries with priority > 0 (i.e., entries that actually need work). Entries scoring 1.0 on all relevant dimensions have priority = 0 and are omitted.

5. **Command-line interface**:

```
usage: prioritize_polishing.py [-h] [--task TASK] [--limit N] [--dry-run] [--summary]

Generate polishing priority lists.

Options:
  --task TASK    Generate priority list for one task only: notes, furigana, examples, cross_refs
  --limit N      Limit output to top N entries per task (default: all)
  --dry-run      Print priorities to stdout instead of writing files
  --summary      Show priority statistics without writing files
```

6. **Summary output** (`--summary` or printed at the end of a normal run):

```
POLISHING PRIORITIES
====================

Task: notes
  Total entries: 23,456
  Entries needing work (priority > 0): 18,234
  Top priority: 00234_ageru (score: 3.00, tier: basic, note_quality: 0.00)
  Written to: polishing/priority/notes.txt

Task: furigana
  Total entries: 23,456
  Entries needing work (priority > 0): 1,456
  Top priority: 01234_sanpo (score: 3.00, tier: basic, furigana: 0.00)
  Written to: polishing/priority/furigana.txt

Task: examples
  Total entries: 23,456
  Entries needing work (priority > 0): 5,678
  Top priority: 00567_iku (score: 3.00, tier: basic, examples: 0.00)
  Written to: polishing/priority/examples.txt

Task: cross_refs
  Total entries: 23,456
  Entries needing work (priority > 0): 15,890
  Top priority: 00123_au (score: 3.00, tier: basic, cross_refs: 0.00)
  Written to: polishing/priority/cross_refs.txt
```

### Step A3: Create the priority directory

```bash
mkdir -p polishing/priority
```

### Step A4: Test the priority script

```bash
# Generate all priorities
python3 build/prioritize_polishing.py

# Check output files
head -20 polishing/priority/notes.txt
head -20 polishing/priority/furigana.txt
head -20 polishing/priority/examples.txt
head -20 polishing/priority/cross_refs.txt

# Summary only
python3 build/prioritize_polishing.py --summary

# Single task
python3 build/prioritize_polishing.py --task notes --limit 50 --dry-run

# Verify entries at the top of each list are genuinely low-quality
# Pick the top entry from notes.txt and check it
head -5 polishing/priority/notes.txt | tail -1 | xargs -I{} find entries/ -name "{}*"
```

Spot-check a few top-priority entries to confirm they genuinely need the most work. If the priorities seem wrong, adjust the dimension weights.

---

## Part B: Modify Polishing Prompts [2.1.2]

**Goal**: Update all five polishing prompts to check for a priority file before falling back to sequential processing. This must be a non-breaking change -- prompts work with or without priority files.

### Step B1: Define the priority mode section

Add the following section to each polishing prompt, immediately after the "Starting Point" section. The exact wording should be adapted slightly per prompt, but the logic is the same:

```markdown
## Priority Mode (Optional)

If a priority file exists, process entries in priority order instead of sequentially by ID:

```bash
ls polishing/priority/{TASK_FILE}.txt 2>/dev/null
```

**If the file exists**:
1. Read the priority file to get the ordered list of entry IDs
2. Find your current position: check `polishing/tasks/{TASK}/progress.txt` for the last processed entry
3. Skip any entries in the priority list that come before your last processed entry
4. Process entries in priority file order (highest priority first)
5. Update `polishing/tasks/{TASK}/progress.txt` with the ID of the last entry processed (NOT the next sequential ID, but the next entry in the priority list)

**If the file does not exist**: Fall back to sequential processing by ID (the standard behavior described in "Starting Point" above).

**Regenerating priorities**: Run `python3 build/prioritize_polishing.py --task {TASK_KEY}` to refresh the priority list. This is useful after many entries have been polished and priorities have shifted.
```

### Step B2: Apply to each prompt

For each prompt, adapt the section above using the correct task file name and task key:

| Prompt file | Task file (`{TASK_FILE}`) | Task key (`{TASK_KEY}`) | Progress dir (`{TASK}`) |
|-------------|---------------------------|-------------------------|--------------------------|
| `prompts/polish_add_inline_links.md` | `cross_refs` | `cross_refs` | `inline-links` |
| `prompts/polish_example_sentences.md` | `examples` | `examples` | `example-sentences` |
| `prompts/polish_furigana_completeness.md` | `furigana` | `furigana` | `furigana-completeness` |
| `prompts/polish_furigana_correctness.md` | `furigana` | `furigana` | `furigana-correctness` |
| `prompts/polish_semantic_labels.md` | `notes` | `notes` | `semantic-labels` |

**For `polish_add_inline_links.md`**: Insert the priority mode section after the existing "Starting Point" section (which reads `polishing/tasks/inline-links/progress.txt`). Use `cross_refs` as the priority file because entries with no cross-references also tend to lack inline links.

**For `polish_example_sentences.md`**: Insert after the "Starting Point" section. Use `examples` as the priority file.

**For `polish_furigana_completeness.md`**: Insert after the "Starting Point" section. Use `furigana` as the priority file.

**For `polish_furigana_correctness.md`**: Insert after the "Starting Point" section. Use `furigana` as the priority file. Note: furigana correctness benefits from the same priority ordering as furigana completeness since entries with bare kanji are more likely to also have incorrect readings.

**For `polish_semantic_labels.md`**: Insert after the "Starting Point" section. Use `notes` as the priority file since semantic label quality correlates with overall note quality.

### Step B3: Verify the modifications are non-breaking

Check that each modified prompt still works in the standard sequential mode by verifying:
1. The "Starting Point" section is unchanged
2. The priority mode section is clearly marked as optional
3. The fallback behavior is explicitly documented
4. No existing sections were removed or restructured

---

## Part C: Add Makefile Target [2.1.2]

### Step C1: Update the Makefile

Add a new target:

```makefile
priorities:
	python3 build/prioritize_polishing.py
```

Add `priorities` to the `.PHONY` line at the top.

---

## Part D: Update CLAUDE.md [2.1.2]

### Step D1: Document the priority system

In CLAUDE.md, find the section about polishing tasks (near "Polishing (progress-tracked)" in the "Task prompts" area). Add a brief note about the priority system:

```
**Polishing priority**: Polishing tasks can optionally process entries in priority order (worst first) instead of sequentially by ID. Run `make priorities` to generate priority files in `polishing/priority/`. Polishing prompts automatically detect and use these files when present. Without priority files, prompts fall back to sequential processing.
```

### Step D2: Add to essential commands

In the "Essential commands" section of CLAUDE.md, add near the reports area:

```bash
python3 build/prioritize_polishing.py             # Generate polishing priority lists
python3 build/prioritize_polishing.py --summary    # Priority statistics without writing files
python3 build/prioritize_polishing.py --task notes # Generate priority for one task only
```

### Step D3: Add to Makefile shortcuts

In the Makefile shortcuts section of CLAUDE.md, add:

```bash
make priorities                           # generate polishing priority lists
```

### Step D4: Update project structure

In the project structure section of CLAUDE.md, add the `polishing/priority/` directory:

```
  polishing/priority/                  # Priority-ordered entry ID lists per polishing task
```

---

## Verification

After all parts are complete, run these checks:

```bash
# Verify the priority script runs and generates files
python3 build/prioritize_polishing.py
ls -la polishing/priority/

# Check file contents
wc -l polishing/priority/*.txt
head -15 polishing/priority/notes.txt
head -15 polishing/priority/furigana.txt
head -15 polishing/priority/examples.txt
head -15 polishing/priority/cross_refs.txt

# Verify summary mode
python3 build/prioritize_polishing.py --summary

# Verify single-task mode
python3 build/prioritize_polishing.py --task notes --limit 10 --dry-run

# Verify Makefile target
make priorities

# Verify polishing prompts haven't broken (just check they parse as valid markdown)
head -5 prompts/polish_add_inline_links.md
head -5 prompts/polish_example_sentences.md
head -5 prompts/polish_furigana_completeness.md
head -5 prompts/polish_furigana_correctness.md
head -5 prompts/polish_semantic_labels.md

# Full validation still passes
make validate
```

Fix any issues found during verification. Pay special attention to:
- The priority script handling entries with missing fields gracefully
- The generated files containing valid entry IDs
- The top-priority entries actually being low-quality when spot-checked

---

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow."

1. **Run `make build`** to ensure all build artifacts are up to date
2. **Stage and commit all changes**:
   ```bash
   git add -A
   git commit -m "Add polishing priority system [2.1.2]

   - Create build/prioritize_polishing.py to score entries across quality dimensions
   - Generate priority-ordered lists in polishing/priority/ (notes, furigana, examples, cross_refs)
   - Update all 5 polishing prompts to use priority files when available (non-breaking)
   - Add make priorities target and CLAUDE.md documentation
   - Priority scoring: tier_weight * inverse_quality per task-specific dimensions"
   ```
3. **Push** to the feature branch
4. **Create a PR**: `gh pr create --repo tkgally/je-dict-1 --head <branch> --base main --title "Polishing priority system [2.1.2]" --body "..."`
5. **Poll CI status** every 60 seconds: `gh pr checks <number> --repo tkgally/je-dict-1` (allow up to 10 minutes)
6. **Squash-merge** once CI is green: `gh pr merge <number> --repo tkgally/je-dict-1 --squash`
7. **If CI fails**: read the error with `gh run view <run_id> --repo tkgally/je-dict-1 --log-failed`, fix, push, and repeat
8. **Post-merge cleanup**:
   ```bash
   git checkout main && git pull origin main
   git status  # Should show nothing to commit
   git branch -d <branch-name>
   git push origin --delete <branch-name>
   ```

**CRITICAL**: The PR must include rebuilt `docs/` files from `make build`. If you commit source changes but not the build output, the live site won't update and the repo will be left in a dirty state for the next session.
