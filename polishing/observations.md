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

_(All observations through 2026-05-18 sessions 003 and 010 have been harvested by the wiki maintenance session of 2026-05-19.)_

## 2026-05-20 — comprehensive polish session 008 (entries 02487–02514)
- [pattern] Adverbs with spurious conjugation tables: 02491 (間もなく) and 02492 (おそらく) both had full godan conjugation tables with verb_class tags incorrectly added. The add_conjugations.py script may have treated adverbs ending in -く as godan verbs. Recommend auditing all adverb POS entries for erroneous conjugation fields.
