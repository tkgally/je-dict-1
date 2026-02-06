# Learner Experience — Prompt 1: Audit under-example'd basic/core entries

**Source:** Agent 3 Report (Learner Experience), Proposal 1
**Priority:** High
**Effort:** Low (script creation)

---

Read the example-sentences skill. Then check which basic and core tier entries
have fewer than the required number of examples (5 per sense for basic/core).
Write a Python script that scans all entries and outputs a report: entry_id,
tier, number_of_senses, total_examples, examples_per_sense, and a compliance
flag (PASS/FAIL). Sort by tier (basic first), then by examples_per_sense
ascending. Save the report to build/reports/example_compliance.txt.

**Follow-up session prompt (run separately after the report is generated):**

Read build/reports/example_compliance.txt. Pick the 10 basic-tier entries with
the fewest examples relative to their required minimum. For each one, read
the existing entry, then add examples following the example-sentences skill
guidelines (progressive length, vocabulary restrictions). Update the modified
timestamp. Validate with python3 build/validate.py after each entry.
