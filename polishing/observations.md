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

_(All observations through 2026-05-12 have been harvested by the wiki maintenance session of 2026-05-12.)_

## 2026-05-12 — comprehensive polish session 009 (entries 00776–00799)
- [tooling] `verify_furigana.py` incorrectly flags kanji in inline link baseforms (the part after `→`) as missing furigana. These are not displayed to users and do not need furigana. The script should strip the baseform portion before checking. Affects any entry with inline links containing kanji in the target form (e.g., `→炊く：02127_taku` triggers a false positive on `炊`).
