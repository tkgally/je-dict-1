# Code & Structure — Prompt 18: Clean up legacy cross-reference string format

**Source:** Agent 1 Report (Code & Structure), Prompt 18
**Priority:** Low
**Effort:** Very low

---

In je-dict-1, the cross_references field in schema.json allows both string format
(legacy) and object format (current). Check whether any entries still use the legacy
string format:

1. Search all entry files in entries/ for cross_references arrays containing plain
   strings (not objects)
2. If any are found, convert them to the structured object format
3. If none are found, consider removing the string option from the schema's oneOf
   (but leave a comment noting it was removed)
4. Run python3 build/validate.py to verify everything still passes
