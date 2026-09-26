# Lexicographic Quality — Prompt 5: Homophone cross-reference pass

**Source:** Agent 4 Report (Lexicographic Quality), Prompt 5
**Priority:** HIGH
**Effort:** Medium

---

Using entries_index.json, identify all groups of entries that share the same reading
but have different headwords (homophones). For each homophone group:
1. Add "homophone" type cross_references between all members of the group
2. In the notes of each entry, add a brief disambiguation note if not already present

Focus on the most common/confusable homophones first (e.g., readings with 3+ entries
sharing the same reading). Currently only 5 homophone references exist in the entire
dictionary.

Process the top 50 homophone groups (by frequency). Run validate.py when done.
