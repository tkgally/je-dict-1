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

_(All observations through 2026-06-06 session 033 have been harvested by the wiki maintenance session of 2026-06-07. Tag-drift updates consolidated into Cleanup Backlog Priority 11 (Update 2026-06-07); redundant CONJUGATION notes sections added as a sub-pattern under Priority 4; entry-specific items — 05478 ドライバー sense mismatch, 05501 写真家 stale noentry link — filed to Entry Follow-ups.)_

## 2026-06-07 — comprehensive polish session 037 (entries 05617–05635)
- [pattern] Semantic tag errors: several entries in this range had badly wrong domain tags (懸念→electronics, 端末→building/transportation, 促進→emotion/time/work, 七夕→animal-mammal); a targeted semantic audit of nearby entries may be warranted
- [entry] 05629 shushi: ex2 and ex3 are near-duplicates (both about understanding the shushi of a document); diversify in a future session

## 2026-06-07 — comprehensive polish session 042 (entries 05715–05734)
- [pattern] Several adverb/onomatopoeia entries (e.g., 05715 ぽたぽた, 05716 ぶんぶん, 05719 かちかち, 05720 ばりばり, 05724 じゃぶじゃぶ, 05726 ぼうぼう) have spurious verb conjugation tables in their JSON — they are tagged as adverbs or onomatopoeia but include godan conjugation forms. These should be removed; a targeted cleanup pass for adverb entries with `"conjugation"` fields would be worth adding as a tooling check
- [entry] 05728_mareni: notes refer to めったに as "more common" than まれに — this register note is correct and worth keeping as-is
