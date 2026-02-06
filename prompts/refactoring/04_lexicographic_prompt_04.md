# Lexicographic Quality — Prompt 4: Similar word cross-reference mining

**Source:** Agent 4 Report (Lexicographic Quality), Prompt 4
**Priority:** HIGH
**Effort:** Medium (repeating — session 1 of ~5)

---

**Post-03_learner_prompt_02 note:** Prompt 03_learner_prompt_02 already added
cross-references to 40 basic-tier entries by extracting references from notes fields
(antonyms, pair verbs, similar words, keigo forms). Some basic-tier entries that
previously had empty cross_references arrays may now have entries. Check which entries
still have empty cross_references before processing.

Review all entries whose notes field contains "SIMILAR WORDS" or "SIMILAR EXPRESSIONS"
but whose cross_references array is empty (after accounting for additions made by
03_learner_prompt_02). For each entry:
1. Extract the similar words mentioned in notes
2. Check if those words exist in the dictionary (use entries_index.json, which now
   includes cross_reference_count per entry from 01_code_prompt_07)
3. Add appropriate cross_references (type: "contrast" for confusable words,
   type: "synonym" for near-synonyms)
4. Ensure the referenced entry also gets a reciprocal cross_reference back

This is a mechanical-plus-semantic task: the notes already identify the similar words,
but judgment is needed to set the correct reference type and verify the relationships
are bidirectional.

Process entries in ID order, skipping any already handled by 03_learner_prompt_02.
Run validate.py when done.
