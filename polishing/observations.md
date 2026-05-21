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

_(All observations through 2026-05-20 session 008 have been harvested by the wiki maintenance session of 2026-05-21.)_

[pattern] 2026-05-21: Entries in the 02559–02583 range had duplicate `conjugation` fields — one old format (`prefix`/`stem`/`ending` keys) followed by a correct `forms`-array block. Found in 02560, 02567, 02568, 02574, 02576, 02582. Worth running a batch check across earlier and later entries for the same pattern.

## 2026-05-21 — comprehensive polish session 004 (entries 02604–02625)
- [entry] 02617 (混んでいる): conjugation table is badly wrong — generated as if いる were a standalone godan verb. E.g. Past shows {混}んでいった instead of {混}んでいた; polite shows {混}んでいります instead of {混}んでいます. Needs repair.

## 2026-05-21 — comprehensive polish session 007 (entries 02670–02696)
- [pattern] Duplicate conjugation blocks (old prefix/stem/ending format + new forms array) found again in 02688 (kyouchou), 02693 (kiru), 02696 (keikoku) — same pattern extends further than the 02559–02583 range noted earlier. A batch script to detect and remove old-style blocks across all entries would be useful.
