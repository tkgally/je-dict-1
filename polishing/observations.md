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

_(All observations through 2026-05-14 session 007 have been harvested by the wiki maintenance session of 2026-05-15.)_

## 2026-05-15 — comprehensive polish sessions 001–007 (entries 01489–01511)
- [tooling] verify_furigana.py and find_missing_furigana.py were producing false positives on base forms in inline links (e.g., `→縫う：00326_nuu` triggers unmatched kanji). Fixed by stripping `→[^⟧]*⟧` before furigana scan in both scripts.
- [pattern] Several entries in the 01490–01511 range had wrong semantic tags: `furniture` applied to non-furniture items (話, 引き出し has `emotion`). Worth noting that emotion/furniture confusions may indicate a systematic labeling issue.
- [entry] 01495_hatsumei had a Unicode replacement character (U+FFFD) in a cross-reference headword — likely introduced during a bulk edit. Check if other entries in similar ranges have corrupt cross-reference data.
