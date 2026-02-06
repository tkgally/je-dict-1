# Code & Structure — Prompt 16: Reduce PROJECT_STATUS.md size

**Source:** Agent 1 Report (Code & Structure), Prompt 16
**Priority:** Low
**Effort:** Low

---

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
