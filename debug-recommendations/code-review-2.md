# Code Review: je-dict-1

**Reviewed:** 2026-01-16
**Reviewer:** Claude Opus 4.5
**Scope:** Python build scripts, JavaScript frontend, JSON schema, configuration files

---

## Critical (must fix)

### 1. `validate.py:24-34` - Auto-installing packages at import time is a security and reliability risk

**Problem:** The `ensure_package()` function auto-installs `jsonschema` using `pip install` at import time, which:
- Can fail silently (errors go to DEVNULL)
- Is a security risk in production environments
- Breaks deterministic builds
- May cause permission issues

```python
def ensure_package(package_name: str) -> None:
    try:
        __import__(package_name)
    except ImportError:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package_name, "--quiet"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL  # Errors hidden!
        )
```

**Impact:** Build failures, security vulnerabilities, unpredictable behavior

**Suggested fix:** Remove auto-install; require packages via `requirements.txt` and document in setup instructions. A simple import check with a clear error message is better:
```python
try:
    import jsonschema
except ImportError:
    sys.exit("Error: jsonschema required. Run: pip install -r build/requirements.txt")
```

---

### 2. `docs/search.js:74-82` - XSS vulnerability in search results

**Problem:** The `displayResults` function directly interpolates `entry.headword`, `entry.reading`, and `entry.gloss` into HTML without escaping:
```javascript
resultsList.innerHTML = results.map(function(entry) {
    return '<a href="entries/' + folder + '/' + prefix + '/' + entry.id + '.html" class="result-item">' +
        '<div class="result-headword">' + entry.headword + '</div>' + // No escaping!
        '<div class="result-reading">' + entry.reading + '</div>' +
        '<div class="result-gloss">' + entry.gloss + '</div>' +
    '</a>';
}).join('');
```

While the data comes from a generated index file, if the index ever contains malicious content (e.g., `<script>` tags), it would execute.

**Impact:** Potential XSS if dictionary content is compromised

**Suggested fix:** Use `textContent` instead of `innerHTML`, or create elements programmatically:
```javascript
const link = document.createElement('a');
link.href = `entries/${folder}/${prefix}/${entry.id}.html`;
link.className = 'result-item';

const headword = document.createElement('div');
headword.className = 'result-headword';
headword.textContent = entry.headword; // Safe

// ... etc
link.appendChild(headword);
```

---

## High (should fix)

### 3. `build_flat.py:1896-1905` - Import inside function causes repeated import overhead

**Problem:** `from collections import defaultdict` is inside `build_flat()` function at line 1899, causing repeated import evaluation:
```python
def build_flat(project_root: Path) -> int:
    ...
    from collections import defaultdict  # Line 1899
```

**Impact:** Minor performance penalty, non-standard import pattern

**Suggested fix:** Move all imports to the top of the file.

---

### 4. `cleanup_candidates.py:33-34` - Missing error handling for file operations

**Problem:** Lines 33-34 load JSON files without try/except:
```python
candidates_data = load_json('candidate_words.json')
entries_data = load_json('entries_index.json')
```

If either file is malformed or missing, the script crashes with an unhelpful error.

**Impact:** Poor user experience, no graceful degradation

**Suggested fix:** Add try/except with clear error messages:
```python
try:
    candidates_data = load_json('candidate_words.json')
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading candidate_words.json: {e}")
    sys.exit(1)
```

---

### 5. `manage_candidates.py:27` - Hardcoded relative path

**Problem:** `CANDIDATES_FILE = Path('candidate_words.json')` uses a relative path at module level, which will fail if the script is run from a different directory.

**Impact:** Script fails when run from non-project-root directory

**Suggested fix:** Calculate path relative to script location:
```python
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
CANDIDATES_FILE = PROJECT_ROOT / 'candidate_words.json'
```

---

### 6. `add_example_ids.py:91-94` - Double file read in loop

**Problem:** The main loop reads each file twice - once to check example count, then again in `process_entry`:
```python
for filepath in sorted(files):
    with open(filepath, 'r', encoding='utf-8') as f:  # First read
        data = json.load(f)
    examples_before = len(data.get('examples', []))
    if process_entry(filepath):  # Reads file again inside
```

**Impact:** Performance penalty (I/O doubled for ~6000 files)

**Suggested fix:** Pass loaded data to `process_entry` or refactor to load once.

---

## Medium (consider fixing)

### 7. `build_flat.py:1910-1919` - Deleting files outside transaction

**Problem:** The build process deletes `docs/` content before generating new content. If the build fails mid-process, the site is left in a broken state:
```python
if docs_dir.exists():
    for item in docs_dir.iterdir():
        if item.name not in preserved_dirs:
            if item.is_dir():
                shutil.rmtree(item)  # Destructive
```

**Impact:** Build failures leave site broken with no rollback

**Suggested fix:** Build to a temp directory, then atomically swap:
```python
temp_dir = docs_dir.parent / 'docs_temp'
# ... build to temp_dir ...
shutil.rmtree(docs_dir)
temp_dir.rename(docs_dir)
```

---

### 8. `validate.py:350` - Function with 7 return values

**Problem:** `validate_all_entries()` returns a 7-tuple which is hard to use correctly:
```python
def validate_all_entries(...) -> tuple[int, int, list[...], list[...], list[...], list[...], list[...]]:
```

**Impact:** Hard to maintain, easy to mix up return values

**Suggested fix:** Return a dataclass or typed dictionary:
```python
@dataclass
class ValidationResult:
    total_count: int
    valid_count: int
    invalid_files: list
    cross_ref_errors: list
    semantic_warnings: list
    timestamp_warnings: list
    sense_number_errors: list
```

---

### 9. `japanese_utils.py:215` - Import inside function

**Problem:** `import re` is inside `romaji_to_hiragana()`:
```python
def romaji_to_hiragana(romaji: str) -> str:
    ...
    import re  # Line 215
    result = re.sub(...)
```

**Impact:** Minor performance penalty, inconsistent with rest of codebase

**Suggested fix:** Move `import re` to module top.

---

### 10. `build_flat.py:883-891` - Inefficient search index creation

**Problem:** The English word index loop has O(n) appends with uniqueness checks:
```python
if entry_id not in index['english'][word]:
    index['english'][word].append(entry_id)
```

**Impact:** Quadratic time complexity for duplicate detection

**Suggested fix:** Use sets instead of lists, convert to lists at the end:
```python
index['english'][word] = set()
index['english'][word].add(entry_id)
# At end:
index['english'] = {k: list(v) for k, v in index['english'].items()}
```

---

### 11. `schema.json:21-23` - Reading pattern is too strict

**Problem:** The reading pattern `"^[ぁ-んー]+$"` doesn't include the voiced iteration mark (ゝ, ゞ) or some rare kana:
```json
"reading": {
    "pattern": "^[ぁ-んー]+$"
}
```

**Impact:** May reject valid entries with unusual readings

**Suggested fix:** Expand the pattern or validate programmatically.

---

## Low (nice to have)

### 12. `build_flat.py` - CSS embedded in Python file (~930 lines)

**Problem:** The `generate_stylesheet()` function returns a massive CSS string embedded in Python. This is hard to maintain and edit.

**Impact:** Difficult to maintain, no CSS syntax highlighting

**Suggested fix:** Move CSS to a separate file (e.g., `build/templates/styles.css`) and read it:
```python
def generate_stylesheet() -> str:
    template_path = Path(__file__).parent / 'templates' / 'styles.css'
    return template_path.read_text()
```

---

### 13. `resolve_links.py:31-32` - Import inside function

**Problem:** `from collections import defaultdict` inside `build_reading_index()`.

**Suggested fix:** Move to module top.

---

### 14. `extract_references.py` - Local import pattern

**Problem:** Uses `from datetime import datetime, timezone` at top but the import pattern could be cleaner throughout the file.

---

### 15. `validate.py:247` - Local import inside function

**Problem:** `from datetime import datetime, timezone` inside `check_timestamps()`:
```python
def check_timestamps(...):
    from datetime import datetime, timezone
```

**Suggested fix:** Move to module top with other imports.

---

### 16. `update_entries_index.py:96` - No return value from main

**Problem:** `update_entries_index()` returns a boolean but the return value is ignored in the `if __name__ == '__main__'` block.

**Suggested fix:** Use the return value for exit code:
```python
if __name__ == '__main__':
    import sys
    sys.exit(0 if update_entries_index() else 1)
```

---

## Suggestions (improvements/refactoring)

### 17. Code Duplication: Furigana pattern appears in multiple files

The pattern `re.compile(r'\{([^|]+)\|([^}]+)\}')` or similar appears in:
- `build_flat.py:25`
- `extract_references.py:24`
- `find_missing_furigana.py:23`
- `verify_furigana.py:19`
- `update_entries_index.py:26`

**Suggestion:** Move to `japanese_utils.py`:
```python
# japanese_utils.py
import re

FURIGANA_PATTERN = re.compile(r'\{([^|]+)\|([^}]+)\}')

def strip_furigana(text: str) -> str:
    """Strip furigana notation from text, keeping only the base text."""
    return FURIGANA_PATTERN.sub(r'\1', text)

def extract_furigana_pairs(text: str) -> list[tuple[str, str]]:
    """Extract all (base, reading) pairs from furigana notation."""
    return FURIGANA_PATTERN.findall(text)
```

---

### 18. Add type hints throughout

Files like `add_example_ids.py`, `cleanup_candidates.py` lack type hints. Adding them would improve IDE support and catch bugs.

---

### 19. Consider using `pathlib` consistently

Some scripts use `os.path` while others use `pathlib.Path`. Standardizing on `pathlib` would improve consistency.

---

### 20. Add `__all__` exports to utility modules

`japanese_utils.py` and `path_utils.py` could benefit from explicit `__all__` declarations to clarify public API:

```python
__all__ = [
    'hiragana_to_romaji',
    'romaji_to_hiragana',
    'get_kana_folder',
    'KANA_ROWS',
    'KANA_TO_FOLDER',
]
```

---

### 21. Test coverage

There are no unit tests visible in the codebase. Adding tests for:
- `hiragana_to_romaji()` / `romaji_to_hiragana()` conversions
- `process_furigana()` HTML generation
- Schema validation edge cases
- Cross-reference resolution logic

would improve reliability and make refactoring safer.

---

## Summary

| Severity | Count |
|----------|-------|
| Critical | 2 |
| High | 4 |
| Medium | 5 |
| Low | 5 |
| Suggestions | 5 |

### Key Findings

The codebase is generally well-structured and readable. The main concerns are:

1. **Security**: XSS vulnerability in search.js and auto-install pattern in validate.py
2. **Robustness**: Lack of error handling in several utility scripts
3. **Maintainability**: Large embedded CSS, duplicated patterns across files
4. **Performance**: Double file reads and quadratic search index building

### Positive Observations

- Good separation of concerns between build scripts and utilities
- Consistent use of JSON schema for validation
- Well-documented functions with docstrings
- Sensible directory structure for scaling (prefix-based subdirectories)
- Good handling of Japanese text (furigana, kana conversion)
