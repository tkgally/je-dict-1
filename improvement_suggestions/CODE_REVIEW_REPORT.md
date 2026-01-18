# Code Review Report: je-dict-1

This review covers the `build/` and `scripts/` Python modules and the `docs/` web frontend.

## Critical (must fix)

- **`build/check_duplicate.py` and `build/manage_candidates.py`: Homophone blockage**
  - **Problem**: Both scripts flag a word as a "duplicate" and exit with an error if *only* the reading matches an existing entry.
  - **Impact**: This prevents adding legitimate homophones (e.g., trying to add `合う` when `会う` already exists, as both share the reading `あう`). This is a fundamental issue for a Japanese dictionary.
  - **Suggested Fix**: Update `check_word` and `check_duplicate` to only return `is_duplicate=True` if BOTH the reading and the headword (stripped of furigana) match. Provide a warning instead of an error if only the reading matches.

- **`build/extract_references.py`: Incomplete extraction of compound words**
  - **Problem**: The regex patterns in `extract_word_after_keyword` and `extract_keigo` fail to capture words where furigana groups and plain kana alternate (e.g., `{召|め}し{上|あ}がる`).
  - **Impact**: Cross-references for many common honorifics, humble forms, and compound verbs are either missed entirely or truncated (e.g., extracting only `{召|め}し`).
  - **Suggested Fix**: Update the regex to allow alternating furigana blocks and kana: `(?:(?:\{[^}]+\})|[ぁ-んァ-ヴー])+`.

## High (should fix)

- **Widespread Code Duplication: Dictionary Indexing and Resolution**
  - **Problem**: `build_reading_index`, `resolve_reference`, and entry-loading logic are implemented multiple times with slight variations in `validate.py`, `extract_references.py`, `resolve_links.py`, `harden_references.py`, and `migrate_cross_references.py`.
  - **Impact**: Extremely high maintenance burden. A change in the dictionary structure or resolution priority must be manually synchronized across 5+ files, leading to bugs like the homophone inconsistency between `validate.py` and `check_duplicate.py`.
  - **Suggested Fix**: Create a `build/dictionary_utils.py` (or expand `japanese_utils.py`) to provide a single, optimized `Dictionary` class that handles loading, indexing (ID, reading, headword), and cross-reference resolution.

- **`build/build_flat.py`: Non-fatal duplicate ID check**
  - **Problem**: The main build script identifies duplicate entry IDs but only prints a warning and proceeds with the build.
  - **Impact**: Duplicate IDs in a static site will cause one entry to overwrite another in the output directory, leading to "missing" entries and broken links that are hard to debug.
  - **Suggested Fix**: Change the warning to a fatal error that stops the build, or ensure `validate.py` is always run (and passes) before `build_flat.py`.

## Medium (consider fixing)

- **`build/manage_candidates.py`: Inconsistent Index Usage**
  - **Problem**: The `check` command uses `entries_index.json` (which might be stale), but the `sync` command scans the entire `entries/` directory on disk.
  - **Impact**: `check` might report a word as safe to add even if it was just added to the dictionary, unless the user remembers to run `update_indexes.py` first.
  - **Suggested Fix**: Standardize on a single source of truth. Ideally, all management scripts should use a shared utility that loads the most up-to-date data.

- **`build/update_entries_index.py`: Fragile path handling**
  - **Problem**: Uses `entry_path.relative_to(project_root)` without ensuring both paths are absolute.
  - **Impact**: Can crash with a `ValueError` if the script is invoked from a different directory or if symlinks are involved.
  - **Suggested Fix**: Call `.resolve()` on both `entry_path` and `project_root` before calculating the relative path.

- **`scripts/fix_sense_numbers_format.py` & `update_single_sense.py`: Duplicated Formatting Logic**
  - **Problem**: Both scripts contain identical regex-based logic to compact JSON arrays.
  - **Impact**: Duplication of complex regex logic.
  - **Suggested Fix**: Move the JSON compacting logic to a shared utility function.

## Low (nice to have)

- **`build/japanese_utils.py`: Robustness of `っ` (small tsu) handling**
  - **Problem**: `hiragana_to_romaji` assumes the character following `っ` is always in `HIRAGANA_TO_ROMAJI`.
  - **Impact**: If an entry contains non-standard characters or a trailing `っ`, it might produce unexpected results or skip characters.
  - **Suggested Fix**: Add a check to ensure `next_char` exists in the mapping before attempting to access its first consonant.

- **Atomic Swap in `build_flat.py`**
  - **Problem**: `os.rename` is used to swap the `docs/` directory.
  - **Impact**: While mostly fine, this can fail on Windows if any file inside `docs/` is open in another program, or across different disk partitions.
  - **Suggested Fix**: Use `shutil.move` or provide better error recovery if the rename fails halfway.

## Suggestions (improvements/refactoring)

- **Consolidate `verify_furigana.py` and `find_missing_furigana.py`**
  - These scripts do almost the same thing. `find_missing_furigana.py` is more powerful. You could retire `verify_furigana.py` and add a `--path` filter to `find_missing_furigana.py`.
- **Add CI Configuration**
  - The project would benefit from a `.github/workflows/main.yml` that runs `validate.py` and `check_duplicate.py` on every PR.
- **Unified Entry Loading**
  - Many scripts use `json.load(f)` directly. A unified `load_entry(path)` function could handle common tasks like adding the `_source_file` for debugging or normalizing fields.
- **Schema Enforcement in scripts**
  - Scripts like `add_example_ids.py` and `fix_sense_numbers_format.py` modify JSON. They should ideally run the `jsonschema` validator before saving to ensure they haven't introduced regressions.
