# Code & Structure — Prompt 17: Add schema version field to entry schema

**Source:** Agent 1 Report (Code & Structure), Prompt 17
**Priority:** Low
**Effort:** Very low

---

In je-dict-1, the entry schema (build/schema.json) has no version field. Add a
schema_version field to support future schema evolution:

1. Add "schema_version" as an optional string field to build/schema.json with
   description "Schema version this entry conforms to"
2. Set the current version to "2.0" (since the project already went through a v2
   quality standards revision)
3. Update the entry-guidelines skill (.claude/skills/entry-guidelines/SKILL.md) to
   mention that new entries should include schema_version: "2.0" in their metadata
4. Do NOT backfill existing entries (that would touch 10,306 files)

This is a forward-looking change that makes future migrations easier.
