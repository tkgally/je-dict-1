# Code & Structure — Prompt 5: Add unit tests for path_utils.py

**Source:** Agent 1 Report (Code & Structure), Prompt 5
**Priority:** Medium
**Effort:** Low

---

Create a test file at build/tests/test_path_utils.py with unit tests for
build/path_utils.py. Test:

- get_numeric_id: various entry ID formats, edge cases
- get_directory_range: boundary cases (00000, 00499, 00500, 00999, 01000)
- get_entry_path: verify correct directory and filename construction

Use the docstring examples as initial test cases. Run with:
cd /home/user/je-dict-1 && python3 -m pytest build/tests/test_path_utils.py -v
