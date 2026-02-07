# Agent Team Report 5: Post-Refactoring Audit

## Executive Summary

This report audits the 20 refactoring changes completed from Proposal 1 (Code & Structure), evaluates the robustness of the current codebase, and reviews the 31 remaining prompts from Proposals 2-4 for validity and consistency. The audit was conducted by a team of agents covering: build pipeline testing, code health analysis, remaining prompt validation, and cross-cutting concern analysis.

**Overall Assessment:** The refactoring was highly successful. The core build pipeline is fully functional, all 140 unit tests pass, all 10,303 entries validate, and the full build completes correctly. However, the audit identified several issues that should be addressed before proceeding with the remaining 31 prompts.

**Key findings:**
- **3 real bugs** that should be fixed (entry_renderer.py duplication, inline import, missing template error handling)
- **Pre-commit hook verified working** (the `--entry` flag exists in validate.py as needed)
- **0 prompts invalidated** — all 31 remaining prompts are still valid and executable
- **3 prompt dependency chains** that must be respected during execution
- **Build pipeline is solid** — validate, index, build, and quick-build all work correctly

---

## Part 1: Build Pipeline Verification

### Test Results Summary

| Test | Result | Details |
|------|--------|---------|
| Unit tests (pytest) | **PASS** | 140/140 tests pass in 0.23s |
| Entry validation | **PASS** | 10,303/10,303 entries valid |
| Index update | **PASS** | entries_index.json updated, 183 candidates |
| Full build | **PASS** | 37.09s, 10,303 entries, 12,556 sitemap URLs |
| Quick build (--quick) | **PASS** | 7.71s (~5x faster) |
| Report dashboard | **PASS** | All 7 sections display correctly |
| Makefile targets | **PASS** | `make validate` and `make report` work |
| Pre-commit hook syntax | **PASS** | Valid bash syntax |
| Package-style imports | **FAIL** | See Issue #1 below |

### Validation Warnings (Non-Blocking)

These are informational and do not indicate bugs:
- 80 homonym mismatches (expected — unrelated readings sharing IDs)
- 9 hardenable cross-references (could add target_id; not urgent)
- 2 word link warnings (minor formatting)
- 431 POS consistency warnings (part_of_speech vs tags.pos drift — reported by prompt 13's new check)

### Report Dashboard Output

```
Total entries: 10,303
  Basic:   801 (7.8%)
  Core:    1,998 (19.4%)
  General: 7,504 (72.8%)

Examples: 40,176 total (avg 3.9/entry), 0 entries with 0 examples
Cross-references: 3,313 total
Inline word links: 12,665 total
Furigana coverage: 92.1%
```

---

## Part 2: Code Health Audit

The audit examined all 14 key files modified or created during the first 20 prompts. Issues are organized by severity.

### Issue #1: Package-Style Imports Fail (MEDIUM)

**Files affected:** `entry_renderer.py`, `page_generators.py`, `search_index_builder.py`

These modules use bare imports like `from path_utils import get_directory_range`. This works when the scripts are invoked from the `build/` directory (as `build_flat.py` does via `sys.path` manipulation), but fails when someone tries to import them as Python packages from the project root (`from build.entry_renderer import ...`).

**Impact:** Low in practice — the build system works correctly because `build_flat.py` handles `sys.path`. But it violates Python packaging conventions and will cause issues if anyone adds new scripts that import these modules from a different location.

**Recommendation:** Not urgent, but could be cleaned up by adding `sys.path` setup to each module or using relative imports. This is a pre-existing pattern in the codebase, not a regression from the refactoring.

### Issue #2: Duplicate `is_kanji()` in entry_renderer.py (LOW)

**File:** `build/entry_renderer.py`, line 87

The function `process_headword_with_kanji_links()` defines a local `is_kanji()` function instead of importing it from `japanese_utils.py`, where it was centralized by prompt 3. This is the exact type of duplication that prompt 3 was designed to eliminate.

**Impact:** Low — the local copy works correctly. But it defeats the purpose of the deduplication work.

**Recommendation:** Fix by importing `is_kanji` from `japanese_utils` and removing the local definition.

### Issue #3: Inline Import of build_sitemap (LOW)

**File:** `build/build_flat.py`, line 472

```python
from build_sitemap import build_sitemap
```

This import is inside the `build_flat()` function body rather than at the top of the file. All other imports are at module level.

**Impact:** Very low — it works correctly. This is likely intentional to avoid import-time side effects.

**Recommendation:** Minor style issue. Could be moved to module-level imports, but not urgent.

### Issue #4: Missing Template File Error Handling (LOW)

**Files:** `build_flat.py` (line ~80), `search_index_builder.py` (lines ~121-128)

Template file reads (`styles.css`, `search.js`, `tag-search.js`) use `.read_text()` without try/except. If a template file is accidentally deleted, the build crashes with a raw `FileNotFoundError`.

**Impact:** Low — the files were just created and are checked into git. But a friendlier error message would help debugging.

**Recommendation:** Wrap template reads in try/except with a clear error message pointing to the missing file.

### Issue #5: Pre-commit Hook (VERIFIED OK)

**File:** `.githooks/pre-commit`

The pre-commit hook calls `python3 build/validate.py --entry <file>` to validate individual entry files. The `--entry` flag was confirmed to exist in `validate.py` (line 974, added via argparse). The hook is correctly implemented.

**Impact:** None — this works as intended.

**Status:** No fix needed.

### Issue #6: Silent Failure on Missing kanji_list.json (LOW)

**File:** `build/entry_renderer.py`, lines 32-38

The `KANJI_LIST` is loaded at module import time. If `kanji/kanji_list.json` doesn't exist, it silently creates an empty dict. All kanji links in entry pages would silently fail.

**Impact:** Low — the file exists and is rebuilt by every build. But a warning log would help debugging.

**Recommendation:** Add a warning print if kanji_list.json is missing.

### False Positives from Automated Audit

The automated code health audit flagged several issues that turned out to be incorrect upon manual verification:

1. **"Makefile references non-existent update_indexes.py"** — FALSE. `build/update_indexes.py` exists as a valid wrapper script.
2. **"validate.py counter logic error at lines 102-109"** — FALSE. That code does not exist in validate.py. The auditor fabricated or hallucinated it.
3. **"Timestamp formatting without zero-padding at line 308"** — FALSE. Could not find this pattern in build_flat.py at the referenced line.

---

## Part 3: Remaining Prompts Validation

All 31 remaining prompts were read and cross-checked against the 20 completed changes.

### Overall Status

| Category | Prompts | All Valid? | Issues |
|----------|---------|------------|--------|
| 02 Workflow & Autonomy | 12 prompts | Yes | 1 has pre-completed overlap (build/report.py) |
| 03 Learner Experience | 10 prompts | Yes | None |
| 04 Lexicographic Quality | 10 prompts (5 repeating) | Yes | 3 have forward dependencies |

**No prompts are invalidated.** All file references are correct. All assumptions about the codebase state are accurate. The post-notes on each prompt correctly identify the completed refactoring work.

### File References Verified

Every file referenced by the remaining prompts was checked for existence:

| Referenced File | Status | Created By |
|----------------|--------|------------|
| build/templates/search.js | Exists | Prompt 02 |
| build/templates/styles.css | Exists | Prompt 01 |
| build/entry_renderer.py | Exists | Prompt 09 |
| build/page_generators.py | Exists | Prompt 10 |
| build/search_index_builder.py | Exists | Prompt 11 |
| build/report.py | Exists | Prompt 12 |
| entries_index.json (enriched) | Exists | Prompt 07 |
| Makefile | Exists | Prompt 08 |
| .github/workflows/validate.yml | Exists | Prompt 15 |
| All referenced skills | Exist | Pre-existing |

### Dependency Chains

Three dependency chains must be respected in execution order:

**Chain 1: Workflow Pipeline**
```
02_workflow_prompt_01 (PROJECT_CONTEXT_BRIEF.md)
  --> 02_workflow_prompt_07 (status system references brief)
  --> 02_workflow_prompt_08 (batch prompts reference brief)
```

**Chain 2: Counter Standardization**
```
03_learner_prompt_07 (design counter template, apply to 10 entries)
  --> 04_lexicographic_prompt_06 (apply template to remaining ~40 entries)
```

**Chain 3: Cross-References and Particles**
```
03_learner_prompt_02 (extract cross-refs from 40 basic entries)
  --> 04_lexicographic_prompt_04 (mine similar-word cross-refs)

03_learner_prompt_09 (improve だけ/しか as model pair)
  --> 04_lexicographic_prompt_09 (enhance other secondary particles)
```

### Prompt-Specific Notes

**02_workflow_prompt_07** (Create status update system): The prompt creates `pipeline/update-status.py` for pipeline-specific progress tracking. This is distinct from `build/report.py` (created by prompt 12), which provides a general dictionary health dashboard. The post-note correctly distinguishes the two purposes. No conflict.

**02_workflow_prompt_12** (Integrate with GitHub Actions): Creates `.github/workflows/pipeline.yml` alongside the existing `validate.yml` (created by prompt 15). The post-note correctly identifies the existing workflow. No conflict.

**03_learner_prompt_04** (Improve entry navigation): References `build/entry_renderer.py` and `build/page_generators.py` for modifications. Both exist at the correct paths. The prompt's instructions to modify these files are still valid after the monolith split.

**03_learner_prompt_05** (Add tier badges): References `build/templates/search.js` and `build/search_index_builder.py`. Both exist. The enriched `entries_index.json` already has `vocabulary_tier` data that this prompt needs.

### Recommended Execution Order

The prompts were designed to be run in the numbered order within each category. The recommended cross-category order is:

1. **Phase 1: Workflow infrastructure** (02_workflow_prompt_01 through 12)
2. **Phase 2: Learner experience** (03_learner_prompt_01 through 10)
3. **Phase 3: Lexicographic quality** (04_lexicographic_prompt_01 through 10)

Within Phase 3, ensure:
- 04_lexicographic_prompt_04 runs after 03_learner_prompt_02
- 04_lexicographic_prompt_06 runs after 03_learner_prompt_07
- 04_lexicographic_prompt_09 runs after 03_learner_prompt_09

---

## Part 4: Recommended Pre-Prompt Fixes

Based on the audit findings, we recommend the following fixes be applied BEFORE proceeding with the remaining 31 prompts. These are small, targeted fixes that address the issues found during the audit.

### Fix 1: Remove duplicate is_kanji() from entry_renderer.py

Remove the local `is_kanji()` definition inside `process_headword_with_kanji_links()` in `build/entry_renderer.py` and import it from `japanese_utils` instead. This completes the deduplication work from prompt 3.

**Effort:** 5 minutes
**Risk:** Very low

### Fix 2: Add template file error handling (Optional)

Wrap the template file reads in `build_flat.py` and `search_index_builder.py` with try/except blocks that provide clear error messages if `build/templates/styles.css`, `build/templates/search.js`, or `build/templates/tag-search.js` are missing.

**Effort:** 5 minutes
**Risk:** Very low

### Fix 3: Add kanji_list.json warning (Optional)

Add a warning print in `entry_renderer.py` if `kanji/kanji_list.json` is not found at import time, rather than silently falling back to an empty dict.

**Effort:** 2 minutes
**Risk:** Very low

---

## Part 5: Assessment of Completed Work Quality

### What Went Well

1. **The monolith split was clean.** `build_flat.py` went from 3,664 lines to ~400 lines. The three extracted modules (`entry_renderer.py`, `page_generators.py`, `search_index_builder.py`) are well-structured and the build still works perfectly.

2. **Deduplication was thorough.** Five files were updated to import from `japanese_utils.py` instead of defining their own copies. Only one local copy of `is_kanji()` remains (in `entry_renderer.py`).

3. **Test coverage is solid.** 140 tests cover `japanese_utils.py` and `path_utils.py` comprehensively, including edge cases and boundary conditions. All pass.

4. **The enriched entries_index.json works correctly.** Six new fields were added and all 10,303 entries have correct values. The subsequent prompts that depend on this enrichment will work.

5. **The incremental build (--quick) works as designed.** 5x speedup over full builds when no entries have changed.

6. **The legacy cross-reference cleanup was thorough.** 28 entries were converted, 1 wrong target_id was fixed, and the schema was simplified.

7. **The CI workflow, Makefile, and pre-commit hook provide a solid developer experience foundation.**

### What Could Have Gone Better

1. **The entry_renderer extraction missed one case of is_kanji duplication.** A local function definition was left inside `process_headword_with_kanji_links()` that should have been caught during prompt 3's deduplication pass.

2. **Template file reads lack error handling.** Given that the whole point of extracting templates was to make them editable, adding protection against accidental deletion would have been prudent.

---

## Summary

The first 20 prompts were executed successfully. The build pipeline is fully functional, tests pass, and the codebase is in significantly better shape than before. The 3 recommended fixes are minor and can be completed in under 15 minutes.

All 31 remaining prompts are valid and can proceed as designed. The execution order should follow the numbered sequence within categories, with attention to the 3 cross-category dependency chains documented above.

---

*Report generated by Agent Team 5 (Post-Refactoring Audit) on 2026-02-07*
