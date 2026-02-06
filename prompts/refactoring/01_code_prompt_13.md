# Code & Structure — Prompt 13: Validate part_of_speech consistency with tags.pos

**Source:** Agent 1 Report (Code & Structure), Prompt 13
**Priority:** Low
**Effort:** Low

---

In je-dict-1, entries have both a free-text part_of_speech field (e.g., "godan verb",
"verb (ichidan)") and a structured tags.pos array (e.g., ["verb-godan"]). These can
drift apart. Add a validation check to build/validate.py that cross-checks the
free-text part_of_speech against metadata.tags.pos for consistency.

For example:
- part_of_speech "godan verb" should have tags.pos containing "verb-godan"
- part_of_speech "adjective (i-adjective)" should have tags.pos containing "adjective-i"

Add this as a new warning category (not an error, since it's a soft check).
Run: python3 build/validate.py
Report any mismatches found.
