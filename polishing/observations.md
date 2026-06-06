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

_(All observations through 2026-06-05 session 025 have been harvested by the wiki maintenance session of 2026-06-06. The recurring semantic-tag-drift pattern was consolidated into Cleanup Backlog Priority 11 (Update 2026-06-06); the mimetic-adverb spurious-conjugation cluster into Priority 6; the new nested/double-brace furigana sub-pattern into Priority 9; and specific entries — 05318 体力, the 05332–05335 math cluster, 05381 図書室 — into Entry Follow-ups.)_

## 2026-06-06 — comprehensive polish session 029 (entries 05468–05482)
- [pattern] Three entries in this range (05474 分量, 05475 重量, 05476 金槌) had obviously wrong semantic/formality tags: 分量 had ["building","transportation"], 重量 had formality "informal", 金槌 had semantic ["food","tool"]. This continues the tag-drift pattern seen earlier; entries in the 05400–05500 range appear to be a batch generated with tag errors. A targeted scan of semantic and formality tags for this range would be worthwhile.
- [entry] 05478 ドライバー notes mention a "MEANING 4 - COMPUTING" (device driver) but sense 4 is not listed in the definitions array. Either add a definition for the computing sense or remove the note.

## 2026-06-06 — comprehensive polish session 030 (entries 05483–05502)
- [pattern] Continued tag-drift pattern: 05484 体温計 (time-general,tool,weather→health,tool), 05485 体重計 (animal-mammal,tool→health,tool), 05486-05489 plants (general→plant,nature), 05491-05492 office tools (general→tool,office), 05493-05494 ceremonies (general→ritual,social), 05496 ジャングル (general→nature,geography), 05497 高原 (food→geography,nature), 05498 海辺 (general→geography,nature), 05499 群島 (tool→geography,nature), 05500 本土 (general→geography), 05502 秘書 (removed domain:medical).
- [entry] 05501 写真家: notes link ⟦カメラマン→カメラマン：noentry⟧ but 28387_kameraman exists — should be updated to link properly.

## 2026-06-06 — comprehensive polish session 033 (entries 05540–05559)
- [pattern] Incorrect semantic tags continued in 05551–05557 range: 05551 えんちゅう had "body-part", 05556 ないがい had ["electronics","furniture"], 05557 だいしょう had "building" — all fixed to "general". Tag-drift appears to extend beyond the previously identified 05400–05500 range and into 05500+ entries.
- [pattern] Several entries in 05540–05546 had redundant CONJUGATION sections in their notes even though a `conjugation` field already existed in the JSON — removed from 05542, 05543, 05544, 05546. The notes-only CONJUGATION block appears to be a batch artifact; earlier polishing may have added conjugation fields without removing the duplicate notes sections.
