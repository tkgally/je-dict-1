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

_(All observations through 2026-05-13 have been harvested by the wiki maintenance session of 2026-05-13.)_

## 2026-05-13 — comprehensive polish session 007 (entries 01014–01038)
- [entry] 01026_hashi ex5: Japanese word order error — `ご飯を箸の中に立てること` should be `ご飯の中に箸を立てること` (箸 and ご飯 are swapped). Needs a human fix to the example sentence.
- [tooling] verify_furigana.py produces false positives for kanji in the base-form part of inline links (text after `→` in `⟦surface→base：id⟧`). Only the surface (user-visible) text requires furigana. Output should skip kanji inside base forms.
- [pattern] Entries in the 01014–01038 range had thorough examples but sparse inline links in notes — especially in VARIETIES, TYPES, and RELATED sections. Many variety/type names (e.g., miso varieties, hot pot types) lacked entries and needed noentry marking + candidates added.
