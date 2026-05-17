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

## 2026-05-17 — comprehensive polish session 002 (entries 01833–01856)
- [pattern] "するする" typo in TRANSITIVITY → Pattern continues in 01833–01856 range. Affected: 01833, 01835, 01837, 01839, 01841, 01843, 01845, 01847, 01849, 01851, 01852, 01855. All fixed this session.
- [pattern] Incorrect semantic tags continue in this range: 01836 (医療: body-part/education→medical/health), 01838 (祝い: clothing/leisure→celebration/social), 01848 (引退: transportation→work/career), 01849 (入院: education→medical/health), 01855 (輸出: building/transportation→economy/trade). Pattern of wrong tags applied during batch creation.

## 2026-05-17 — comprehensive polish session 009 (entries 01992–02011)
- [pattern] Wrong semantic tags found in entries 02008_ikuratemo ("furniture") and 02011_uragiru ("electronics"). Both corrected. Pattern of batch-creation semantic tag errors continues into the 02000 range.
