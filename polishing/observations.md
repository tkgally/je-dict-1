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

_(All observations through 2026-05-13 session 007 have been harvested by the wiki maintenance session of 2026-05-14.)_

## 2026-05-14 — comprehensive polish session 004 (entries 01181–01204)
- [tooling] `verify_furigana.py` false-positive: after adding inline links with kanji base forms (e.g. `⟦{踏|ふ}む→踏む：01197_fumu⟧`) to notes, the checker flags kanji in the `→baseform：` portion as "missing furigana." The script strips `{漢字|かんじ}` notation but not `⟦...→...：...⟧` inline link syntax. Fix: strip inline link brackets before furigana checking.
