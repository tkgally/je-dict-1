# Code & Structure — Prompt 12: Add a validate-and-report summary command

**Source:** Agent 1 Report (Code & Structure), Prompt 12
**Priority:** Low
**Effort:** Low

---

In je-dict-1, the validation script (build/validate.py) outputs detailed error
information. Create a new script build/report.py that provides a quick dashboard
summary of the dictionary's health:

Output should include:
- Total entries, broken down by vocabulary tier
- Entry type breakdown (verb, noun, adjective, etc. from tags.pos)
- Cross-reference statistics (total, resolved, pending)
- Example sentence statistics (total examples, average per entry, entries with 0 examples)
- Inline word link coverage (how many entries have linked examples)
- Furigana coverage status
- Recent activity (entries modified in last 7 days)

Run it with: python3 build/report.py
The script should load entries from the entries/ directory and compute all stats.
