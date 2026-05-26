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

_(All observations through 2026-05-25 sessions 012 and 021 have been harvested by the wiki maintenance session of 2026-05-26.)_

## 2026-05-26 — comprehensive polish session 004 (entries 03582–03598)
- [pattern] Incorrect semantic tags found in multiple entries this range: "electronics" was applied to 評価, 表面, 不幸 (all general vocabulary); "transportation" applied to 服装; "body-part" applied to 笛; "emotion" applied to 不自由. Suggests the original generation model misassigned tags for some 03500-range entries — worth checking adjacent entries.
- [entry] 03591_fuukei: had a furigana error {描|か}く (wrong reading) — corrected to {描|えが}く → egaku. Worth checking other entries with 描 kanji.


## 2026-05-26 — comprehensive polish session 008 (entries 03662–03676)
- [pattern] Continued finding misassigned "electronics" semantic tags in 03600–03700 range: 喜び (03672) and 理解 (03674) both tagged "electronics" — corrected to "emotion" and "general" respectively. Same systematic error noted in session 004 persists further through this range.
- [pattern] Compound entries (天気予報 01678, 予防接種 11068) should be linked as units when they appear in examples/notes rather than linking individual components. The compound has its own entry so the full compound is the right link target.

## 2026-05-26 — comprehensive polish session 009 (entries 03677–03698)
- [pattern] Multiple entries in the 03686–03698 range had clearly wrong semantic tags (像 03691 tagged "animal-mammal", 班 03697 tagged "food", 進行 03686 tagged "body-part"/"transportation", 操縦 03689 tagged "body-part"/"occupation"/"time-general"/"transportation", 羽根 03696 tagged "transportation"). These appear to be systematic tagging errors from original AI generation, likely from confusion with homophones or unrelated words. A dedicated semantic-tag validation pass over the 03500–03800 range may be warranted.

## 2026-05-26 — comprehensive polish session 010 (entries 03699–03712)
- [entry] 03707 hitei: examples ex2 and ex4 are identical Japanese sentences (both "{否定|ひてい}{形|けい}を{使|つか}って{文|ぶん}を{作|つく}りなさい。") — one should be replaced with a different example
- [entry] 03712 hin: had incorrect "formality": "vulgar" tag — corrected to "neutral" (品 meaning goods/elegance is not vulgar)
