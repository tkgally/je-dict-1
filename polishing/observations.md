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

_(All observations through 2026-06-04 session 017 have been harvested by the wiki maintenance session of 2026-06-05.)_

[pattern] Several entries in the 05291–05312 range had completely wrong semantic tags (e.g., "transportation" for だるい/面倒くさい, "animal-mammal" for 浴室, "animal-insect" for だるい, "furniture/tool" for 叶う). This suggests a systematic tagging error in a batch of entries around this range. Worth a tooling audit for semantic tags that are obviously mismatched with the POS or gloss. (2026-06-05)

---

## Session 022 — 2026-06-05

[entry] 05318_tairyoku (体力, physical strength): semantic tags include "leisure" which is clearly wrong for physical stamina. Should be something like "health" or "body". Check similar entries (気力, 精力, 忍耐力) for similar tagging errors.

## 2026-06-05 Session 023

[pattern] Entries 05332-05335 (足し算, 引き算, 掛け算, 割り算) all had wrong semantic tags: tags like "body-part", "furniture", "time-general" instead of "mathematics". These were created by claude-opus-4-5 with modified date 2026-04-14. Suggests a batch creation run had cross-contamination of semantic tag data. Watch for similar wrong tags in nearby ID ranges (05300-05400).

[pattern] Entry 05344_kogeru (焦げる) had semantic tag "body-part" instead of "action" — same model/date as above (claude-opus-4-5, 2026-04-14). Likely same batch run.
