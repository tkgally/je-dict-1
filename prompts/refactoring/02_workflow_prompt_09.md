# Workflow & Autonomy — Prompt 9: Generate a word-ID lookup table

**Source:** Agent 2 Report (Workflow & Autonomy), Phase 3, Prompt 9
**Priority:** Medium (Phase 3: Optimize Task Prompts)
**Effort:** Medium

---

Create `build/generate_word_lookup.py` that scans all entries and generates
`build/word_id_lookup.json` mapping readings to entry IDs (with headword and gloss
for disambiguation). This lookup table should be loaded by Claude during inline
linking sessions instead of running Python search snippets for every word. Include
it in the inline-links batch prompt instructions. Also add this to the build pipeline
so it stays current.
