# Code & Structure — Prompt 14: Investigate and document build performance

**Source:** Agent 1 Report (Code & Structure), Prompt 14
**Priority:** Low
**Effort:** Low

---

In je-dict-1, the build (python3 build/build_flat.py) regenerates all 10,306 entry
pages every time. Profile the build to understand where time is spent:

1. Add timing instrumentation to build_flat.py's build_flat() function -- measure
   time for each of the 6 steps plus the kanji rebuild and sitemap generation.
2. Run the build and report the timing breakdown.
3. Based on the results, add a comment block at the top of build_flat.py documenting
   the build time breakdown and potential optimization strategies.

Do NOT implement optimizations yet -- just measure and document.
Run: python3 build/build_flat.py
