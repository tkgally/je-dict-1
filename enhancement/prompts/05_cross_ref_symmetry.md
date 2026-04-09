# Cross-Reference Completeness & Symmetry

**Enhancement plan section**: [1.1.3] Cross-Reference Completeness & Symmetry

Extend cross-reference tooling to detect asymmetric references, lint semantic clusters, and update the polishing prompt for cluster-mode processing.

## What This Prompt Creates/Modifies

| File | Action | Purpose |
|------|--------|---------|
| `build/find_merge_candidates.py` | **Modify** | Add asymmetric cross-reference detection and `--asymmetry-only` flag |
| `build/check_semantic_clusters.py` | **Create** | Lint transitivity pairs, antonym pairs, and keigo groups for missing internal links |
| `prompts/add_cross-references.md` | **Modify** | Add "Cluster Mode" section for batch processing of related entries |
| `.claude/skills/cross-reference-entry/SKILL.md` | **Modify** | Add symmetry requirements and cluster processing guidance |
| `CLAUDE.md` | **Modify** | Document `check_semantic_clusters.py` in essential commands |
| `Makefile` | **Modify** | Add `check-symmetry` and `check-clusters` targets |

---

## Part A: Extend find_merge_candidates.py [1.1.3]

**Goal**: Add a dedicated asymmetric cross-reference report to the existing merge candidate script.

### Step A1: Read the current script

```bash
cat build/find_merge_candidates.py
```

Understand the existing structure: `find_potential_merges()`, `find_missing_crossrefs()`, `find_duplicate_numeric_ids()`, `_load_entry_refs()`, and the `main()` CLI with `--merge-only`, `--crossref-only`, `--dupid-only`, `--json` flags.

### Step A2: Add a `find_asymmetric_references()` function

Add a new function after the existing `find_missing_crossrefs()` function. This function specifically checks for directional asymmetry in existing references (A references B but B does not reference A back).

The function should:

1. Load all entry files (reuse the `_load_entry_refs()` pattern but also collect the full reference details, not just IDs/readings).
2. For each entry, iterate over its `prominent_see_also` and `cross_references`:
   - For each reference that has a `target_id`, check whether the target entry has any reference (in `prominent_see_also` or `cross_references`) pointing back to the source entry.
   - A "back-reference" is any reference in the target entry whose `target_id` matches the source entry's ID, OR whose reading matches the source entry's reading (for entries without hardened target_id).
3. Collect all cases where A->B exists but B->A does not.
4. Return a list of asymmetric reference dicts:

```python
{
    'source_id': 'XXXXX_word',
    'source_headword': '...',
    'target_id': 'YYYYY_word',
    'target_headword': '...',
    'ref_type': 'prominent_see_also' or 'cross_references',
    'ref_detail': 'antonym' or 'synonym' or null (for prominent_see_also)
}
```

5. Also compute summary stats:
   - Total references with target_id (across all entries)
   - Number of symmetric pairs (both directions exist)
   - Number of asymmetric references (one direction only)

### Step A3: Add `--asymmetry-only` flag

In the `main()` function:

1. Add `--asymmetry-only` to the argparse options:
   ```python
   parser.add_argument('--asymmetry-only', action='store_true',
                       help='Only show asymmetric cross-reference report')
   ```
2. Update the `show_all` logic to include the new flag
3. Call `find_asymmetric_references()` when appropriate
4. Add human-readable output for the asymmetry report:

```
=== ASYMMETRIC CROSS-REFERENCES (N found) ===
References where A→B exists but B→A does not.

  00123_ageru → 00456_agaru  (prominent_see_also)
    Source has link to target, but target has no link back.

  01234_ookii → 01235_chiisai  (cross_references: antonym)
    Source has link to target, but target has no link back.

Summary:
  Total references with target_id: XXXX
  Symmetric pairs: XXXX
  Asymmetric (one-way): XXXX
```

5. Add JSON support for the new report section.

### Step A4: Test the new functionality

```bash
# Full report (now includes asymmetry section)
python3 build/find_merge_candidates.py | tail -40

# Asymmetry-only report
python3 build/find_merge_candidates.py --asymmetry-only

# JSON output with asymmetry
python3 build/find_merge_candidates.py --asymmetry-only --json | python3 -m json.tool | head -40
```

Verify the output is correct by spot-checking a few reported asymmetric pairs: read both entries and confirm that one direction of the reference is indeed missing.

---

## Part B: Build Semantic Cluster Linter [1.1.3]

**Goal**: Create a script that checks known tight semantic clusters (transitivity pairs, antonym pairs, keigo groups) for missing internal links.

### Step B1: Create `build/check_semantic_clusters.py`

Create the script at `build/check_semantic_clusters.py` with this structure:

```
usage: check_semantic_clusters.py [-h] [--type TYPE] [--json] [--summary]

Check semantic clusters for missing internal cross-references.

Options:
  --type TYPE    Check only one cluster type: transitivity, antonym, keigo (default: all)
  --json         Output as JSON
  --summary      Show counts only, not individual entries
```

The script should implement three cluster checks:

#### Check 1: Transitivity pairs

1. Load all entry files.
2. For each verb entry, check the `notes` field for transitivity information:
   - Look for patterns like `{自動詞|じどうし}` / `{他動詞|たどうし}` / `intransitive` / `transitive`
   - Look for patterns like "Pair:" followed by a word
3. For entries that mention a transitive/intransitive label:
   - Check if they have a `prominent_see_also` link to their pair verb
   - If the pair verb is mentioned in notes but not linked via `prominent_see_also`, flag it
4. For entries with `prominent_see_also` where the note mentions "transitive" or "intransitive":
   - Verify the target entry exists
   - Verify the target has a reciprocal `prominent_see_also` back

Output format:
```
TRANSITIVITY PAIR GAPS (N found)

  00123_ageru (transitive, {上|あ}げる)
    Notes mention transitivity but no prominent_see_also link to pair verb
    Pair mentioned in notes: {上|あ}がる

  00456_agaru → 00123_ageru (prominent_see_also)
    Target 00123_ageru has no reciprocal link back
```

#### Check 2: Antonym pairs

1. For each entry with a `cross_references` of type `antonym`:
   - Check if the target entry has a reciprocal `antonym` cross-reference back
   - Flag asymmetric antonym pairs

Output format:
```
ANTONYM PAIR GAPS (N found)

  01234_ookii → 01235_chiisai (antonym)
    Target has no reciprocal antonym link back
```

#### Check 3: Keigo groups

1. For each entry with a `cross_references` of type `keigo`:
   - Collect the keigo group (source + all keigo targets)
   - Check that every member of the group links to every other member
   - Flag incomplete keigo groups

Output format:
```
KEIGO GROUP GAPS (N found)

  Group: {食|た}べる / {召|め}し{上|あ}がる / いただく
    00396_taberu → 00789_meshiagaru (keigo: honorific) ✓
    00396_taberu → 00654_itadaku (keigo: humble) ✓
    00789_meshiagaru → 00396_taberu (keigo) MISSING
    00654_itadaku → 00396_taberu (keigo) MISSING
```

#### Summary output

```
SEMANTIC CLUSTER SUMMARY
========================
Transitivity pairs checked: XX
  Complete pairs: XX
  Incomplete (missing link): XX
  Mentioned in notes but unlinked: XX

Antonym pairs checked: XX
  Symmetric: XX
  Asymmetric: XX

Keigo groups checked: XX
  Fully linked: XX
  Partially linked: XX
```

### Step B2: Test the cluster linter

```bash
python3 build/check_semantic_clusters.py
python3 build/check_semantic_clusters.py --type transitivity
python3 build/check_semantic_clusters.py --type antonym
python3 build/check_semantic_clusters.py --type keigo
python3 build/check_semantic_clusters.py --summary
python3 build/check_semantic_clusters.py --json | python3 -m json.tool | head -40
```

Spot-check the output by reading a few flagged entries to confirm the reports are accurate.

---

## Part C: Update Cross-Reference Polishing Prompt [1.1.3]

**Goal**: Add a "Cluster Mode" section to the cross-reference polishing prompt so that related entries can be processed together for guaranteed symmetry.

### Step C1: Read the current prompt

```bash
cat prompts/add_cross-references.md
```

### Step C2: Add a Cluster Mode section

After the existing "Workflow for Each Entry" section and before the "Batch Commits" section, add a new section:

```markdown
## Cluster Mode (Alternative Workflow)

Instead of processing entries one at a time by sequential ID, you can process **semantic clusters together**. This is more efficient for ensuring symmetric linking because you handle both sides of a relationship in the same batch.

### When to use Cluster Mode

Use cluster mode when:
- The asymmetry report shows many one-way references: `python3 build/find_merge_candidates.py --asymmetry-only`
- The cluster linter flags incomplete groups: `python3 build/check_semantic_clusters.py`
- You want to focus on a specific relationship type (transitivity, antonyms, keigo)

### Cluster Mode Workflow

1. **Generate a cluster report**:
   ```bash
   python3 build/check_semantic_clusters.py --type transitivity
   # or: --type antonym, --type keigo
   ```

2. **Pick a cluster** from the report (e.g., a transitivity pair with a missing link).

3. **Load all entries in the cluster** simultaneously (typically 2-5 entries):
   - Read each entry's full JSON
   - Map out all existing cross-references between cluster members

4. **Fix all links within the cluster**:
   - Add missing `prominent_see_also` links (transitivity pairs, homophones)
   - Add missing `cross_references` links (antonyms, keigo)
   - Ensure every link is bidirectional where required
   - Normalize relationship labels across the cluster (e.g., both sides of an antonym pair should use the same label format)

5. **Update timestamps** on all modified entries.

6. **Move to the next cluster** from the report.

### Cluster size guidelines

- **Transitivity pairs**: 2 entries per cluster
- **Antonym pairs**: 2 entries per cluster
- **Keigo groups**: 2-5 entries per cluster (plain + honorific + humble + any variants)
- **Homophone groups**: 2-4 entries per cluster

Process 5-10 clusters per commit batch (roughly 10-20 entries total).
```

### Step C3: Update the session end output

In the "Output at Session End" section, add a line about cluster-mode reporting:

```
8. If using cluster mode: number of clusters processed, cluster types
```

---

## Part D: Update Cross-Reference-Entry Skill [1.1.3]

**Goal**: Add symmetry requirements and cluster processing guidance to the skill file.

### Step D1: Read the current skill

```bash
cat .claude/skills/cross-reference-entry/SKILL.md
```

### Step D2: Add a symmetry section

At the end of the skill file (before any closing checklist if one exists, or at the very bottom), add:

```markdown
## Symmetry Requirements

Cross-references should be **bidirectional** for most relationship types. The table below summarizes when back-links are required vs. optional:

| Relationship | Back-link Required? | Via |
|-------------|--------------------|----|
| Transitive/intransitive pair | **Always** | `prominent_see_also` both ways |
| N/Nする pair | **Always** | `prominent_see_also` both ways |
| Homophones (confusable) | **Always** | `prominent_see_also` both ways |
| Antonym | **Usually** | `cross_references` (antonym) both ways |
| Keigo | **Usually** | `cross_references` (keigo) both ways within group |
| Synonym | Case-by-case | `cross_references` (synonym) — add back-link if genuinely helpful |
| Contrast | Case-by-case | `cross_references` (contrast) |
| Related | Optional | `cross_references` (related) |
| See also | Optional | `cross_references` (see_also) |

### Checking symmetry

Use the asymmetry report to find one-way references:
```bash
python3 build/find_merge_candidates.py --asymmetry-only
```

Use the cluster linter to find incomplete semantic groups:
```bash
python3 build/check_semantic_clusters.py
```

### Cluster processing

When fixing symmetry issues, process related entries together as a cluster rather than one at a time. This ensures both sides of a relationship are updated in the same session. See the "Cluster Mode" section in `prompts/add_cross-references.md` for the detailed workflow.
```

**Important**: Do not restructure the existing content of the skill file. Only append the new section.

---

## Part E: Update CLAUDE.md and Makefile [1.1.3]

### Step E1: Update CLAUDE.md essential commands

In the "Essential commands" section, in the "Entry consolidation" sub-area (near `python3 build/find_merge_candidates.py`), add:

```bash
python3 build/find_merge_candidates.py --asymmetry-only  # Asymmetric cross-reference report
python3 build/check_semantic_clusters.py                  # Lint transitivity/antonym/keigo clusters
python3 build/check_semantic_clusters.py --summary        # Cluster completeness summary
```

### Step E2: Update the Makefile

Add new targets to the Makefile:

```makefile
check-symmetry:
	python3 build/find_merge_candidates.py --asymmetry-only

check-clusters:
	python3 build/check_semantic_clusters.py --summary
```

Add `check-symmetry` and `check-clusters` to the `.PHONY` line at the top.

### Step E3: Update CLAUDE.md Makefile shortcuts

In the "Essential commands" section where Makefile shortcuts are listed, add:

```bash
make check-symmetry                       # asymmetric cross-reference report
make check-clusters                       # semantic cluster completeness summary
```

---

## Verification

After all parts are complete, run these checks:

```bash
# Part A: verify the asymmetry report runs
python3 build/find_merge_candidates.py --asymmetry-only
python3 build/find_merge_candidates.py --asymmetry-only --json | python3 -m json.tool | head -20

# Full report still works (now includes asymmetry section)
python3 build/find_merge_candidates.py | tail -20

# Part B: verify the cluster linter runs
python3 build/check_semantic_clusters.py
python3 build/check_semantic_clusters.py --summary
python3 build/check_semantic_clusters.py --type transitivity
python3 build/check_semantic_clusters.py --json | python3 -m json.tool | head -20

# Part C: verify the prompt is valid markdown
head -10 prompts/add_cross-references.md

# Part D: verify the skill file is intact
head -5 .claude/skills/cross-reference-entry/SKILL.md

# Full validation still passes
make validate
```

Fix any issues found during verification.

---

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md under "End-of-session PR and merge workflow."

1. **Run `make build`** to ensure all build artifacts are up to date
2. **Stage and commit all changes**:
   ```bash
   git add -A
   git commit -m "Add cross-reference symmetry detection and cluster linting [1.1.3]

   - Extend find_merge_candidates.py with asymmetric reference report and --asymmetry-only flag
   - Create build/check_semantic_clusters.py for transitivity/antonym/keigo cluster linting
   - Add Cluster Mode section to prompts/add_cross-references.md
   - Update cross-reference-entry skill with symmetry requirements
   - Add make check-symmetry and make check-clusters targets"
   ```
3. **Push** to the feature branch
4. **Create a PR**: `gh pr create --repo tkgally/je-dict-1 --head <branch> --base main --title "Cross-reference symmetry detection and cluster linting [1.1.3]" --body "..."`
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
