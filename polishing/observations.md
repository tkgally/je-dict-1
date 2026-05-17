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

_(All observations through 2026-05-16 sessions 001–004 have been harvested by the wiki maintenance session of 2026-05-17.)_

## 2026-05-17 — comprehensive polish session 001 (entries 01808–01832)
- [pattern] Multiple entries in the 01800–01832 range have the typo `するする` instead of `する` in the TRANSITIVITY → Pattern line. Affected: 01811, 01823, 01826, 01828, 01830, 01832. Likely a template copy-paste error during batch creation. Worth scanning remaining batches for this.
- [pattern] Multiple entries in this range have incorrect semantic tags (`transportation` for words unrelated to transport). Affected: 01815 (飽きる), 01822 (居眠り), 01825 (衣服). Suggests a validation gap — the `transportation` tag may be applied as a default in some batch creation contexts.
- [tooling] `validate_tags.py` could be extended to flag semantic tags that conflict with the POS or gloss (e.g., `transportation` + verb meaning "to get bored").
