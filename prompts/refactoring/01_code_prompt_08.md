# Code & Structure — Prompt 8: Add a Makefile or build runner script

**Source:** Agent 1 Report (Code & Structure), Prompt 8
**Priority:** Medium
**Effort:** Low

---

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
