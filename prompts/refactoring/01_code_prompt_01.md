# Code & Structure — Prompt 1: Extract CSS from build_flat.py

**Source:** Agent 1 Report (Code & Structure), Prompt 1
**Priority:** High
**Effort:** Medium

---

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
