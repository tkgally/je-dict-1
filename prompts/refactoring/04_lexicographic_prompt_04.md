# Lexicographic Quality — Prompt 4: Similar word cross-reference mining

**Source:** Agent 4 Report (Lexicographic Quality), Prompt 4
**Priority:** HIGH
**Effort:** Medium (repeating — session 1 of ~5)

---

Review all entries whose notes field contains "SIMILAR WORDS" or "SIMILAR EXPRESSIONS"
but whose cross_references array is empty. For each entry:
1. Extract the similar words mentioned in notes
2. Check if those words exist in the dictionary (use entries_index.json)
3. Add appropriate cross_references (type: "contrast" for confusable words,
   type: "synonym" for near-synonyms)
4. Ensure the referenced entry also gets a reciprocal cross_reference back

This is a mechanical-plus-semantic task: the notes already identify the similar words,
but judgment is needed to set the correct reference type and verify the relationships
are bidirectional.

Process entries in ID order. Run validate.py when done.
