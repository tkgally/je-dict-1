## 1. Duplicated `get_entry_prefix()` Function

**Location**: `validate.py:81`, `build_flat.py:1861`, `migrate_entries.py:24`, `merge_audio.py:52`, `migrate_audio.py:15`

**Issue**: This trivial function (extracting first 2 characters of entry ID) is defined **five times**:

```python
def get_entry_prefix(entry_id: str) -> str:
    return entry_id[:2].lower()
```

Some are named `get_entry_prefix()`, others `get_audio_prefix()`, but they do the same thing.

**Impact**: If the prefix logic ever needs to change, it must be updated in 5 places.

**Recommendation**: Move to shared module and import everywhere.

## 2 Fix the entry metadata file path shown on entry pages. `build/build_flat.py` writes `metadata-file` as `folder/id`, but the real path is `folder/prefix/id`. This is misleading for debugging and navigation.

## 3 Make cross-reference resolution deterministic and unambiguous. `readings_to_ids` maps a reading to a single ID, which breaks when multiple entries share a reading. Use a `reading -> [ids]` index and either match by headword or allow an explicit `id` field in `cross_references`.

## 4 Duplicated Hiragana-Romaji Conversion Functions

**Location**: `validate.py`, `build_flat.py`, `resolve_links.py`

**Issue**: The conversion between hiragana and romaji is implemented **three separate times**:
- `validate.py`: `HIRAGANA_TO_ROMAJI` dict + `COMBO_MAPPINGS` dict + `hiragana_to_romaji()` function (lines 24-134)
- `build_flat.py`: `hiragana_to_romaji()` function with inline dict (lines 154-211)
- `resolve_links.py`: `romaji_to_hiragana()` function for reverse conversion (lines 86-133)

Each implementation is slightly different:
- `validate.py` handles っ (gemination) and ー (long vowel) specially
- `build_flat.py` handles っ differently (looks ahead for next consonant)
- `resolve_links.py` has bugs (e.g., `'kk': 'っk'` leaves a trailing 'k')

**Impact**: Bugs may occur when one implementation is fixed but others aren't. Maintenance is multiplied. Different behaviors in different contexts.

**Recommendation**: Create a shared module `build/japanese_utils.py` containing:
- A single `hiragana_to_romaji()` function
- A single `romaji_to_hiragana()` function (with proper consonant handling)
- Common constants like KANA_ROWS, KANA_TO_FOLDER mappings

## 5 Guard recent-entry sorting against invalid or missing timestamps. `build_recent_entries` returns a naive datetime for bad values, which can raise when sorting against aware datetimes. Use a timezone-aware fallback or skip invalid entries with a warning.

## 6 Inconsistent Cross-Reference Format in Data

**Location**: `entries/ta/ta/taberu_00001.json` (and likely others)

**Issue**: The same entry contains both legacy string format and new structured format:
```json
"cross_references": [
    "nomu_00001",                          // Legacy string (deprecated)
    {
        "type": "antonym",                 // New structured format
        "reading": "のむ",
        "headword": "{飲|の}む",
        "label": "to drink"
    },
    ...
]
```

The schema allows both formats, but mixing them in the same entry causes confusion and requires the build system to handle both cases everywhere.

**Impact**: Build scripts have conditional logic for both formats. Legacy references may not resolve correctly.

**Recommendation**:
1. Run a migration script to convert all legacy string references to structured format
2. Remove legacy format support from schema after migration
3. Update `extract_references.py` to only produce structured format

## 7 Add an audio integrity check (either in `build/validate.py` or a new script) to verify that `has_audio: true` examples have corresponding MP3 files and that orphaned audio files are reported.

## 8 Clean output deterministically. The build deletes a fixed list of files in `docs/` but leaves any stale artifacts not in that list. Consider wiping `docs/` (except `docs/flat/`) or writing to a temp dir then swapping.

## 9 Python Version Compatibility Issue

**Location**: `merge_audio.py:24`, `build_flat.py` (various)

**Issue**: Type hints use Python 3.10+ syntax:
```python
def parse_audio_filename(filename: str) -> tuple[str, int] | None:  # 3.10+ only
```

But README states Python 3.8+ is supported.

**Impact**: Users on Python 3.8/3.9 will get syntax errors.

**Recommendation**: Either:
- Update requirements to Python 3.10+, OR
- Change to compatible syntax: `from typing import Tuple, Optional` and `Optional[Tuple[str, int]]`

## 10 Duplicated Kana-to-Folder Mapping

**Location**: `validate.py` (KANA_TO_DIRECTORY), `build_flat.py` (KANA_ROWS/KANA_TO_FOLDER)

**Issue**: Two different approaches to the same mapping:
- `validate.py`: Hardcoded `KANA_TO_DIRECTORY` dict listing every kana character
- `build_flat.py`: Generated from `KANA_ROWS` list dynamically

**Impact**: If new kana need to be added, two places must be updated. Risk of inconsistency.

**Recommendation**: Single source of truth in shared module.

## 11 Inefficient Double-Loading of Entries During Validation

**Location**: `validate.py:317-366`

**Issue**: `validate_all_entries()` loads each entry file **twice**:
1. First pass: For schema validation (line 338)
2. Second pass: For duplicate checking (lines 343-349, re-loading the same file)

With 2,074 entries, this doubles the I/O operations unnecessarily.

**Impact**: Slower validation, especially as dictionary grows.

**Recommendation**: Load each entry once and reuse the data for both validation and duplicate checking.

## 12 No Test Suite

**Location**: N/A (none exists)

**Issue**: The project has 14 Python scripts in `build/` with no automated tests. Critical functions like validation, cross-reference resolution, and HTML generation are untested.

**Impact**: Refactoring is risky. Bugs may go unnoticed. Code quality degrades over time.

**Recommendation**: Add pytest-based test suite covering:
- Hiragana-romaji conversion (edge cases: っ, ー, combinations)
- Entry validation (valid and invalid cases)
- Cross-reference resolution
- HTML generation output

## 13 Error Handling Gaps in Subprocess Calls

**Location**: `update_indexes.py:41-66`

**Issue**: The script calls subprocesses without checking if the scripts exist or if Python is available:
```python
result = subprocess.run(
    [sys.executable, 'build/update_entries_index.py'],
    ...
)
```

If the script is missing, the error message is unclear.

**Impact**: Confusing errors for users.

**Recommendation**: Add existence checks before subprocess calls:
```python
script_path = Path('build/update_entries_index.py')
if not script_path.exists():
    print(f"Error: {script_path} not found")
    return 1
```

## 14 Inconsistent Datetime Handling

**Location**: Various scripts

**Issue**: Different approaches to UTC datetime:
- `datetime.now(timezone.utc)` (correct, timezone-aware)
- `datetime.utcnow()` (deprecated in Python 3.12)
- Some places use `.isoformat()`, others use `.strftime()`

**Impact**: Inconsistent timestamp formats, potential timezone bugs.

**Recommendation**: Standardize on `datetime.now(timezone.utc).isoformat()` everywhere.

## 15 Unused/Orphan Script: `migrate_audio.py`

**Location**: `build/migrate_audio.py`

**Issue**: This migration script exists but isn't called from anywhere (not in `build.py`, not documented in PROJECT_STATUS.md).

**Impact**: Dead code clutters the repository.

**Recommendation**: Either document its usage or remove if no longer needed.

## 16 Minimal `requirements.txt`

**Location**: `build/requirements.txt` (contains only `jsonschema>=4.0.0`)

**Issue**: Only one dependency is listed, but the code may rely on implicit stdlib dependencies that could change.

**Impact**: Dependency versions aren't pinned; builds may break with future Python/jsonschema updates.

**Recommendation**: Consider:
- Pin exact versions for reproducibility
- Add a development requirements file for testing tools

## 17 Schema Still Allows Deprecated Legacy Format

**Location**: `build/schema.json` lines 86-118

**Issue**: The schema explicitly allows both legacy string references and new structured references via `oneOf`. The legacy format is marked as deprecated but still valid.

**Impact**: New entries could be created with deprecated format.

**Recommendation**: After migrating existing entries, remove legacy format from schema to enforce new format.

### Proposed Module Structure

Create a shared utilities module to eliminate duplication:

```
build/
├── __init__.py
├── japanese_utils.py    # NEW: Shared hiragana/romaji conversion
├── path_utils.py        # NEW: Shared path/prefix functions
├── build.py
├── build_flat.py
├── validate.py
├── ...
```

**japanese_utils.py would contain:**
- `hiragana_to_romaji(reading: str) -> str`
- `romaji_to_hiragana(romaji: str) -> str`
- `KANA_ROWS` list
- `KANA_TO_FOLDER` mapping
- `get_kana_folder(reading: str) -> str`

**path_utils.py would contain:**
- `get_entry_prefix(entry_id: str) -> str`
- `get_expected_path(entry_id: str, reading: str) -> Path`
