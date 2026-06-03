# Long-Term Observations

Append-only log of observations from comprehensive-polish sessions that go beyond the entry currently being polished. The daily wiki-maintenance session harvests this file: it files actionable items into `planning/wiki/`, schedules concrete work, and prunes entries that have been acted on.

## Format

Each session appends a section. Within each section, prefix observations with a tag:

- `[pattern]` — systemic issue across multiple entries (e.g., "many 〜的 entries lack notes on adjective vs adverbial use")
- `[wiki]` or `[wiki:page-name]` — content that belongs in the knowledge base
- `[article]` — possible expository article topic
- `[tooling]` — possible script or tool improvement
- `[skill]` — possible skill update needed
- `[entry]` — a specific entry that needs work beyond what fits a single session

## Template

```
## YYYY-MM-DD — comprehensive polish session NNN (entries XXXXX–YYYYY)
- [pattern] ...
- [wiki:topic-name] ...
- [article] ...
- [tooling] ...
```

---

_(All observations through 2026-06-02 session 004 have been harvested by the wiki maintenance session of 2026-06-03.)_

[pattern] 2026-06-03 session 006: Wrong semantic tags found on household/food entries — 04985 浴槽 had "animal-mammal", 04988 洗面台 had "animal-mammal" and "transportation", 04992 前菜 had "electronics". These appear to be bulk-assignment errors from initial entry creation. When polishing entries in the 04800-05200 range, check semantic tags in addition to inline links. Running `python3 build/validate_tags.py` after polishing batches would help catch these.
