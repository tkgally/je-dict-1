# Agent 1 Report: Code & Structure Assessment

## Executive Summary

The je-dict-1 project is a well-organized static-site Japanese-English learner's dictionary with 10,306 entries. The architecture follows a clear pattern: JSON source files are validated and compiled into a static HTML website via Python scripts. The project leverages Claude Code skills for consistent entry authoring and a prompt-based workflow for polishing tasks.

**Key strengths:**
- Clean separation of data (JSON entries) from presentation (HTML generation)
- Atomic build process that prevents broken states
- Comprehensive validation with schema enforcement
- Well-documented skill system for Claude-driven workflows
- Scalable directory structure (500-entry buckets)

**Key improvement areas:**
- `build_flat.py` is a 3,664-line monolith containing HTML templates, CSS, JavaScript, and Python logic all in one file
- Significant code duplication: `strip_furigana` is defined 6 times, `is_kanji` 5 times, `FURIGANA_PATTERN` 5 times across the codebase
- No automated test suite exists anywhere in the project
- No CI/CD pipeline (GitHub Actions or similar)
- The generated `search-index.js` (5.7 MB), `browse.html` (3.7 MB), and `random.html` (1.5 MB) are very large and are checked into git
- The `docs/` output directory (140 MB total) is version-controlled alongside source
- `entries_index.json` (2.4 MB) stores only basic metadata but could include tag data for richer offline queries
- Several scripts in `build/` are one-time migration scripts that could be archived

---

## 1. Architecture Assessment

### Project Layout

```
je-dict-1/
  entries/          # 10,306 JSON files in 500-entry subdirectories
  kanji/            # 2,249 kanji JSON index files + kanji_list.json
  build/            # 42 Python scripts (build, validate, utilities, migrations)
  docs/             # Generated static site (140 MB, version-controlled)
  scripts/          # 2 ad-hoc fix scripts
  prompts/          # Prompt templates for Claude-driven workflows
  polishing/        # Task-based polishing framework with progress tracking
  .claude/skills/   # 16 Claude Code skill definitions
  entries_index.json    # Master index (2.4 MB)
  candidate_words.json  # 153 pending candidate words
  PROJECT_STATUS.md     # Session continuity file (154 KB, growing)
```

### What Works Well

1. **Data-first architecture**: Raw JSON entries are the single source of truth. The build system is purely generative -- nothing in `docs/` needs to be hand-edited (except `about.html`).

2. **Scalable directory structure**: The 500-entry bucket system (`entries/00000/`, `entries/00500/`, etc.) stays within GitHub's 1,000-file-per-directory limit and is computed deterministically from entry IDs.

3. **Atomic build pattern**: `build_flat.py` builds to a temp directory and swaps atomically, preventing broken states on build failure. Preserved files (`about.html`, `CNAME`) survive the swap.

4. **Shared utility modules**: `path_utils.py`, `japanese_utils.py`, `constants.py`, and `html_utils.py` centralize common logic (though not all scripts use them yet).

5. **Skill-based workflow**: The 16 Claude Code skills in `.claude/skills/` provide consistent guidelines for entry creation, revision, and polishing tasks. Each skill is auto-loaded based on context.

### What Could Improve

1. **The `build_flat.py` monolith**: At 3,664 lines and 123 KB, this single file contains:
   - HTML template generation for 8+ page types
   - Complete CSS stylesheet (~700 lines)
   - JavaScript for search, furigana toggle, examples toggle, word links
   - Search index generation
   - Entry HTML rendering with complex furigana/kanji-link processing
   - Build orchestration (load, generate, swap, verify)

2. **Code duplication across kanji-related scripts**: Five separate files define their own `strip_furigana`, `is_kanji`, and `FURIGANA_PATTERN` instead of importing from `japanese_utils.py`.

3. **No test infrastructure**: Zero test files exist. The validation script (`validate.py`) checks entry data but there are no unit tests for the build scripts, utility functions, or HTML generation.

4. **Generated output in version control**: The `docs/` directory (140 MB) is committed to git because GitHub Pages serves from it. This makes commits large and git history bloated.

5. **PROJECT_STATUS.md growth**: At 154 KB (with a 364 KB archive file), this session continuity file grows with every session. It duplicates information that could be derived from git history or computed from entry data.

---

## 2. Build System Analysis

### Build Pipeline

The full build chain runs in this order:

1. `python3 build/validate.py` -- Schema validation + consistency checks
2. `python3 build/update_indexes.py` -- Updates `entries_index.json`, syncs candidates, checks for new kanji
3. `python3 build/build_flat.py` -- Generates the full static site:
   - Verifies kanji index integrity
   - Loads all 10,306 entry JSON files
   - Generates individual HTML pages for each entry
   - Generates navigation pages (index, browse, recent, random, pending, advanced)
   - Generates `search-index.js` (5.7 MB JavaScript file)
   - Generates `styles.css` and `search.js`
   - Atomically swaps the build output into `docs/`
   - Rebuilds kanji JSON and HTML via subprocess calls to `build_kanji_json.py` and `build_kanji_html.py`
   - Generates sitemaps via `build_sitemap.py`

### Pain Points

1. **Full rebuild every time**: There is no incremental build. Every run regenerates all 10,306 entry HTML files plus all navigation pages. As the dictionary grows, build time will increase linearly.

2. **CSS and JS embedded in Python**: The entire stylesheet and all JavaScript code live as Python string literals inside `build_flat.py`. This makes them hard to edit, lint, or test independently.

3. **Subprocess chaining in build**: `build_flat.py` calls `build_kanji_json.py`, `build_kanji_html.py`, and `build_sitemap.py` as subprocesses rather than importing them as modules.

4. **No build caching or checksums**: If an entry JSON file hasn't changed since the last build, its HTML page is still regenerated.

5. **Large generated files checked into git**: `search-index.js` (5.7 MB), `browse.html` (3.7 MB), `entries_index.json` (2.4 MB), and `sitemap-entries.xml` (1.9 MB) change with every build.

### What Works Well

- The atomic build pattern (temp dir + swap) is robust
- Duplicate entry ID detection during build prevents data corruption
- CNAME and `about.html` preservation logic handles edge cases
- Cross-reference resolution happens at build time, keeping source data clean

---

## 3. Data Model Review

### Entry JSON Schema

The schema (`build/schema.json`, Draft-07) defines a rich entry format with:
- **Required fields**: `id`, `headword`, `reading`, `part_of_speech`, `gloss`, `metadata`
- **Optional structured fields**: `definitions[]`, `examples[]`, `notes`, `cross_references[]`
- **Particle-specific fields**: `predicates_requiring`, `particle_contrasts`, `fixed_patterns`, `common_mistakes`
- **Tag system**: `metadata.tags` with `pos[]`, `transitivity`, `verb_class`, `formality`, `politeness`, `style[]`, `domain[]`, `semantic[]`

### Strengths

- The furigana notation `{kanji|reading}` is elegant and round-trips cleanly between JSON and HTML
- Cross-references use a dual resolution system: hard-coded `target_id` for direct links, with fallback to reading-based resolution
- The `sense_numbers` field on examples creates a structured link between examples and definitions
- The inline word link format `[surface->baseform:entry_id]` (using Unicode delimiters) enables rich sentence navigation

### Issues and Gaps

1. **Schema allows loose data**: `part_of_speech` is a free-text string ("godan verb", "verb (ichidan)", "adjective (i-adjective)") with no enum constraint. The `tags.pos` field has a proper enum but the free-text `part_of_speech` can drift.

2. **`entries_index.json` is minimal**: It stores only `id`, `headword`, `reading`, `gloss`, `filename`, `path` -- no tags, no vocabulary tier, no cross-reference count. Richer index data would enable more powerful search and filtering without loading all entry files.

3. **No schema versioning**: There is no `schema_version` field in entries. If the schema evolves, there is no way to distinguish old-format entries from new ones.

4. **Inconsistent cross-reference format**: The schema still allows legacy string references alongside structured objects (the `oneOf` in `cross_references.items`). This legacy support adds complexity.

5. **Tag taxonomy is separate from schema**: `build/tag_taxonomy.json` defines the semantic tag hierarchy but the schema only validates `pos`, `transitivity`, `verb_class`, etc. with inline enums. Semantic tags have no schema validation.

---

## 4. Code Quality Observations

### Function Duplication

The most significant code quality issue is function duplication. The following functions are redefined instead of imported:

| Function | Defined In | Should Import From |
|----------|-----------|-------------------|
| `strip_furigana` | 6 files | `japanese_utils.py` |
| `is_kanji` | 5 files | Should be added to `japanese_utils.py` |
| `FURIGANA_PATTERN` | 5 files | `japanese_utils.py` |
| `hiragana_sort_key` | `build_kanji_json.py` | Could be in `japanese_utils.py` |

### Script Categories

The 42 files in `build/` fall into distinct categories:

**Core build system** (actively used every session):
- `build_flat.py`, `validate.py`, `update_entries_index.py`, `update_indexes.py`, `build_kanji_json.py`, `build_kanji_html.py`, `build_sitemap.py`

**Utilities** (imported by other scripts):
- `path_utils.py`, `japanese_utils.py`, `constants.py`, `html_utils.py`, `duplicate_utils.py`

**Entry management tools** (used during authoring):
- `check_duplicate.py`, `get_entry_path.py`, `get_timestamp.py`, `manage_candidates.py`, `verify_furigana.py`, `harden_references.py`, `extract_references.py`, `resolve_links.py`

**Validation extensions**:
- `validate_tags.py`, `check_tag_consistency.py`, `tag_statistics.py`, `verify_kanji_index.py`

**One-time migration scripts** (could be archived):
- `migrate_cross_references.py`, `migrate_entries.py`, `migrate_pos.py`, `renumber_entries.py`, `fix_katakana_readings.py`, `fix_round_timestamps.py`, `add_example_ids.py`

**Data files** (not scripts):
- `schema.json`, `tag_taxonomy.json`, `pos_mapping.json`, `requirements.txt`

### Monolith Concern

`build_flat.py` at 3,664 lines is the project's most critical file and its biggest technical debt. It generates:
- 8 complete HTML page templates (index, advanced, browse, recent, random, pending, entry, search)
- A full CSS stylesheet (~700 lines of CSS as a Python string)
- Multiple JavaScript modules (search, furigana toggle, examples toggle, word links toggle, header search)
- The search index data structure

This makes it:
- Hard to review changes to CSS or JS without wading through Python
- Impossible to use standard CSS/JS tooling (linters, formatters, minifiers)
- Risky to modify -- a small Python syntax error in a large string literal can break the entire build

### Dependency Management

The project has minimal external dependencies -- just `jsonschema` (pinned to `>=4.0.0,<5.0.0`). The `validate.py` script even has an auto-install fallback for `jsonschema`, though the project's settings wisely deny unrestricted bash access.

### No Testing

There are zero test files in the project. Functions like `hiragana_to_romaji`, `strip_furigana`, `get_directory_range`, and `process_furigana` have docstring examples that could be turned into doctests, but no test runner is configured.

---

## 5. Proposed Improvements

The following prompts are designed for individual Claude Code sessions (~10-15 minutes each). Each is self-contained and does not require context from previous sessions.

---

### Prompt 1: Extract CSS from build_flat.py into a standalone file

```
In the je-dict-1 project, the file build/build_flat.py contains a function called
generate_stylesheet() that returns a large CSS string (~700 lines). Extract this CSS
into a standalone file at build/templates/styles.css. Then modify generate_stylesheet()
to read from that file instead of containing the CSS inline. Make sure the build still
works by running: python3 build/build_flat.py

Steps:
1. Read build/build_flat.py and find the generate_stylesheet() function
2. Create build/templates/styles.css with the CSS content
3. Replace the function body to read from the file
4. Test with: python3 build/build_flat.py
```

---

### Prompt 2: Extract JavaScript from build_flat.py into standalone files

```
In je-dict-1, build/build_flat.py contains several functions that return JavaScript
as Python strings: generate_search_js(), generate_tag_search_js(), and any inline
<script> blocks. Extract these into standalone .js files under build/templates/:

1. build/templates/search.js (from generate_search_js())
2. build/templates/tag-search.js (from generate_tag_search_js())

Modify the generator functions to read from these files instead. Test with:
python3 build/build_flat.py

Note: The small inline scripts in html_utils.py (furigana toggle, examples toggle,
word links toggle, header search) can stay inline for now since they're short.
```

---

### Prompt 3: Eliminate strip_furigana and is_kanji duplication

```
In je-dict-1, the functions strip_furigana() and is_kanji() are duplicated across
multiple files instead of being imported from the shared utility module. Fix this:

1. Ensure japanese_utils.py exports strip_furigana (it already does) and add
   is_kanji() to japanese_utils.py (it's currently not there)
2. Update these files to import from japanese_utils instead of defining their own:
   - build/build_kanji_json.py (has its own strip_furigana, is_kanji, FURIGANA_PATTERN)
   - build/extract_kanji_from_entries.py (has its own strip_furigana, is_kanji, FURIGANA_PATTERN)
   - build/update_kanji_index.py (has its own strip_furigana, is_kanji, FURIGANA_PATTERN)
   - build/verify_kanji_index.py (has its own strip_furigana, is_kanji, FURIGANA_PATTERN)
   - build/check_tag_consistency.py (has its own strip_furigana)
3. Verify the build still works: python3 build/validate.py && python3 build/build_flat.py
```

---

### Prompt 4: Add unit tests for japanese_utils.py

```
Create a test file at build/tests/test_japanese_utils.py with unit tests for the
functions in build/japanese_utils.py. Test at minimum:

- hiragana_to_romaji: basic cases, combo characters, gemination (っ), long vowels (ー)
- romaji_to_hiragana: basic cases, double consonants
- strip_furigana: simple and nested cases, empty input
- is_valid_hiragana: valid hiragana, katakana (should fail), romaji (should fail)
- normalize_reading: katakana to hiragana conversion
- contains_katakana: with and without katakana, long vowel mark edge case
- get_kana_folder: various starting characters

Use the docstring examples as initial test cases. Run with:
cd /home/user/je-dict-1 && python3 -m pytest build/tests/test_japanese_utils.py -v

If pytest is not installed, install it first: pip install pytest
```

---

### Prompt 5: Add unit tests for path_utils.py

```
Create a test file at build/tests/test_path_utils.py with unit tests for
build/path_utils.py. Test:

- get_numeric_id: various entry ID formats, edge cases
- get_directory_range: boundary cases (00000, 00499, 00500, 00999, 01000)
- get_entry_path: verify correct directory and filename construction

Use the docstring examples as initial test cases. Run with:
cd /home/user/je-dict-1 && python3 -m pytest build/tests/test_path_utils.py -v
```

---

### Prompt 6: Archive one-time migration scripts

```
In je-dict-1, the build/ directory contains several one-time migration scripts that
were used during development but are no longer needed for regular operation. Move them
to a new build/archive/ directory to reduce clutter:

Scripts to archive:
- build/migrate_cross_references.py
- build/migrate_entries.py
- build/migrate_pos.py
- build/renumber_entries.py
- build/fix_katakana_readings.py
- build/fix_round_timestamps.py
- build/add_example_ids.py
- build/pos_mapping.json (used only by migrate_pos.py)

Also move the scripts/ directory's contents (fix_sense_numbers_format.py,
update_single_sense.py) to build/archive/ since they are ad-hoc fix scripts.

After moving, verify the build still works: python3 build/validate.py
```

---

### Prompt 7: Enrich entries_index.json with tag and tier data

```
In je-dict-1, the entries_index.json file stores only basic metadata (id, headword,
reading, gloss, filename, path) for each of the 10,306 entries. Enrich it by adding:

1. vocabulary_tier (from metadata.vocabulary_tier)
2. part_of_speech (from part_of_speech field)
3. pos_tags (from metadata.tags.pos array)
4. cross_reference_count (length of cross_references array)
5. example_count (length of examples array)
6. has_inline_links (boolean: whether any example contains the link delimiter character)

Edit build/update_entries_index.py to extract these additional fields. Then run:
python3 build/update_entries_index.py

Verify the output looks correct by checking the first few entries in entries_index.json.
```

---

### Prompt 8: Add a Makefile or build runner script

```
In je-dict-1, the build process requires running multiple Python scripts in sequence.
Create a simple Makefile (or a build.sh shell script if you prefer) at the project root
that defines these common targets:

- validate: runs python3 build/validate.py
- index: runs python3 build/update_indexes.py
- build: runs validate, index, then python3 build/build_flat.py
- check-furigana: runs python3 build/find_missing_furigana.py
- check-kanji: runs python3 build/verify_kanji_index.py
- stats: runs python3 build/tag_statistics.py
- clean: removes docs_build_temp/ and docs_backup/ if they exist
- full: runs clean, then build

The Makefile should use the project root as the working directory. Test it with:
make validate
make build
```

---

### Prompt 9: Split build_flat.py entry HTML generation into a separate module

```
In je-dict-1, build/build_flat.py is 3,664 lines long. Extract the entry page HTML
generation into a separate module. Specifically, move these functions to a new file
build/entry_renderer.py:

- generate_entry_html()
- process_headword_with_kanji_links()
- process_notes_text()
- render_examples() (the inner function)
- Any helper functions used only by the above

The new module should import from the existing shared utilities (japanese_utils,
constants, html_utils, path_utils). Update build_flat.py to import from entry_renderer.

Test with: python3 build/build_flat.py
```

---

### Prompt 10: Split build_flat.py page generators into a separate module

```
In je-dict-1, build/build_flat.py contains generator functions for navigation pages.
Extract these into a new file build/page_generators.py:

- generate_index_page()
- generate_advanced_page()
- generate_browse_page()
- generate_recent_page()
- generate_random_page()
- generate_pending_page()
- generate_html_head() (if not already in html_utils.py)
- generate_header_search_redirect_script()
- build_recent_entries()
- format_jst_datetime()

Update build_flat.py to import from page_generators. After this extraction,
build_flat.py should mainly contain the build_flat() orchestration function
and the main() entry point.

Test with: python3 build/build_flat.py
```

---

### Prompt 11: Split build_flat.py search index generation into a separate module

```
In je-dict-1, build/build_flat.py contains the search index generation logic.
Extract these into a new file build/search_index_builder.py:

- generate_search_index() (the function that creates search-index.js content)
- Any helper functions used exclusively by search index generation

The search-index.js file is currently 5.7 MB. While extracting, consider whether
the index could be optimized (e.g., shorter field names, excluding fields not needed
for search).

Update build_flat.py to import from search_index_builder. Test with:
python3 build/build_flat.py
```

---

### Prompt 12: Add a validate-and-report summary command

```
In je-dict-1, the validation script (build/validate.py) outputs detailed error
information. Create a new script build/report.py that provides a quick dashboard
summary of the dictionary's health:

Output should include:
- Total entries, broken down by vocabulary tier
- Entry type breakdown (verb, noun, adjective, etc. from tags.pos)
- Cross-reference statistics (total, resolved, pending)
- Example sentence statistics (total examples, average per entry, entries with 0 examples)
- Inline word link coverage (how many entries have linked examples)
- Furigana coverage status
- Recent activity (entries modified in last 7 days)

Run it with: python3 build/report.py
The script should load entries from the entries/ directory and compute all stats.
```

---

### Prompt 13: Validate part_of_speech consistency with tags.pos

```
In je-dict-1, entries have both a free-text part_of_speech field (e.g., "godan verb",
"verb (ichidan)") and a structured tags.pos array (e.g., ["verb-godan"]). These can
drift apart. Add a validation check to build/validate.py that cross-checks the
free-text part_of_speech against metadata.tags.pos for consistency.

For example:
- part_of_speech "godan verb" should have tags.pos containing "verb-godan"
- part_of_speech "adjective (i-adjective)" should have tags.pos containing "adjective-i"

Add this as a new warning category (not an error, since it's a soft check).
Run: python3 build/validate.py
Report any mismatches found.
```

---

### Prompt 14: Investigate and document build performance

```
In je-dict-1, the build (python3 build/build_flat.py) regenerates all 10,306 entry
pages every time. Profile the build to understand where time is spent:

1. Add timing instrumentation to build_flat.py's build_flat() function -- measure
   time for each of the 6 steps plus the kanji rebuild and sitemap generation.
2. Run the build and report the timing breakdown.
3. Based on the results, add a comment block at the top of build_flat.py documenting
   the build time breakdown and potential optimization strategies.

Do NOT implement optimizations yet -- just measure and document.
Run: python3 build/build_flat.py
```

---

### Prompt 15: Create a GitHub Actions CI workflow

```
In je-dict-1, there is no CI/CD pipeline. Create a GitHub Actions workflow at
.github/workflows/validate.yml that runs on every push and pull request:

1. Checkout the repository
2. Set up Python 3.10+
3. Install dependencies from build/requirements.txt
4. Run python3 build/validate.py
5. Report success/failure

This should be a minimal validation workflow -- it does NOT need to build the site
(that's too expensive for CI). Just validate entry data integrity.

Keep the workflow simple and fast.
```

---

### Prompt 16: Reduce PROJECT_STATUS.md size with automated sections

```
In je-dict-1, PROJECT_STATUS.md is 154 KB and growing because every session appends
a "Recent Changes" section. The file serves as a session continuity mechanism for Claude.

Improve this by:
1. Keep only the last 5 "Recent Changes" sections in PROJECT_STATUS.md
2. Move older sections to PROJECT_STATUS-archive.md (which already exists at 364 KB)
3. Add a comment at the top of PROJECT_STATUS.md noting that older history is in
   the archive file
4. Update the "Current State" / "Content Status" section with current counts derived
   from running: python3 build/update_entries_index.py (to get accurate numbers)

This is a one-time cleanup. The session workflow in the entry-guidelines skill should
be updated to mention rotating old entries to the archive.
```

---

### Prompt 17: Add schema version field to entry schema

```
In je-dict-1, the entry schema (build/schema.json) has no version field. Add a
schema_version field to support future schema evolution:

1. Add "schema_version" as an optional string field to build/schema.json with
   description "Schema version this entry conforms to"
2. Set the current version to "2.0" (since the project already went through a v2
   quality standards revision)
3. Update the entry-guidelines skill (.claude/skills/entry-guidelines/SKILL.md) to
   mention that new entries should include schema_version: "2.0" in their metadata
4. Do NOT backfill existing entries (that would touch 10,306 files)

This is a forward-looking change that makes future migrations easier.
```

---

### Prompt 18: Clean up legacy cross-reference string format support

```
In je-dict-1, the cross_references field in schema.json allows both string format
(legacy) and object format (current). Check whether any entries still use the legacy
string format:

1. Search all entry files in entries/ for cross_references arrays containing plain
   strings (not objects)
2. If any are found, convert them to the structured object format
3. If none are found, consider removing the string option from the schema's oneOf
   (but leave a comment noting it was removed)
4. Run python3 build/validate.py to verify everything still passes
```

---

### Prompt 19: Add incremental build capability for entry pages

```
In je-dict-1, build/build_flat.py regenerates all 10,306 entry HTML pages on every
build. Add a --quick flag that only regenerates entry pages whose source JSON file
has been modified more recently than the corresponding HTML file:

1. Add argument parsing to build_flat.py's main() function
2. When --quick is passed, compare mtime of each entries/{range}/{id}.json against
   docs/entries/{range}/{id}.html
3. Only regenerate HTML for entries where JSON is newer
4. Still regenerate all navigation pages (index, browse, recent, random) since they
   depend on all entries
5. Print how many entries were skipped vs regenerated

Test with:
python3 build/build_flat.py --quick

Note: The full build (without --quick) should continue to work exactly as before.
```

---

### Prompt 20: Create a pre-commit hook for entry validation

```
In je-dict-1, there is an install_hooks.py script in build/ but it's unclear if any
hooks are active. Create a lightweight git pre-commit hook that:

1. Checks if any files in entries/ are staged for commit
2. If so, runs python3 build/validate.py on just those files (not the full validation)
3. Blocks the commit if validation fails
4. If no entry files are staged, skips validation (fast path)

Create the hook at .githooks/pre-commit and update the README or a setup script to
explain how to install it (git config core.hooksPath .githooks).

Keep it fast -- it should validate only changed entry files, not all 10,306.
```

---

## Summary of Priorities

| Priority | Prompt | Impact | Effort |
|----------|--------|--------|--------|
| High | 3 (Eliminate duplication) | Reduces bugs from divergent copies | Low |
| High | 1, 2 (Extract CSS/JS) | Makes templates editable/lintable | Medium |
| High | 9, 10, 11 (Split monolith) | Makes build_flat.py maintainable | Medium each |
| Medium | 4, 5 (Add tests) | Prevents regressions | Low |
| Medium | 8 (Makefile) | Simplifies developer workflow | Low |
| Medium | 15 (CI/CD) | Catches errors automatically | Low |
| Medium | 7 (Enrich index) | Enables richer search/filtering | Low |
| Low | 6 (Archive migrations) | Reduces directory clutter | Very low |
| Low | 12 (Report script) | Provides health dashboard | Low |
| Low | 13 (POS consistency) | Catches data drift | Low |
| Low | 14 (Build profiling) | Informs optimization work | Low |
| Low | 16 (STATUS.md cleanup) | Reduces file size, keeps context | Low |
| Low | 17 (Schema version) | Future-proofs schema changes | Very low |
| Low | 18 (Legacy cleanup) | Simplifies schema | Very low |
| Low | 19 (Incremental build) | Speeds up development cycle | Medium |
| Low | 20 (Pre-commit hook) | Catches errors at commit time | Low |

---

*Report generated by Agent 1 (Code & Structure) on 2026-02-06*
