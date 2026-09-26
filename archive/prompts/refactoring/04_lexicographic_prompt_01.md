# Lexicographic Quality — Prompt 1: Verb transitivity batch

**Source:** Agent 4 Report (Lexicographic Quality), Prompt 1
**Priority:** HIGH
**Effort:** Medium (repeating — session 1 of ~10)

---

Review the next 100 verb entries (by ID order) that lack "TRANSITIVITY" in their notes
field. For each verb:
1. Add TRANSITIVITY section with Type (自動詞/他動詞), Pair verb (if exists), and
   Pattern (Xが/Xを)
2. Add transitivity tag to metadata.tags if missing
3. If a pair verb exists in the dictionary, add a "pair" type cross_reference

Start from the first verb missing transitivity after ID 00001. Track which verb you
stopped at so the next session can continue.

Use the verb-entry skill for formatting. Do NOT add inline links.
Run validate.py when done.

**Note:** This prompt is designed to be repeated ~10 times to cover all ~1,900 verbs
missing transitivity information.
