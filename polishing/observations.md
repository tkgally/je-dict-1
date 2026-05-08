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

## 2026-05-08 — comprehensive polish session 001 (entries 00001–00005)
- [pattern] Many verb entries have two `"conjugation":` top-level keys: a legacy stub (e.g., `{"type":"godan","ending":"る","stem":"…"}`) plus a full conjugation table appended later. JSON parsers silently take the last value, so the parsed data is correct, but the stub is dead text in the file. Confirmed on 00001_amaru, 00002_amu, 00004_aogu, 07924_aoru. Not present on 00006_aru. Likely affects most or all verb entries that pre-date the conjugation-table retrofit. Cleanup pass would be safe (drops are idempotent and the surviving data is already what tools use).
- [tooling] Add a one-shot pruning script that scans entries for duplicate top-level keys (especially `conjugation`) and removes the legacy stub form. Use raw text scanning rather than `json.load`, since Python silently collapses duplicates. A simple check: `grep -c '"conjugation":' entries/**/*.json | awk -F: '$2 > 1'`. Could live next to `add_conjugations.py`.
- [entry] 00004_aogu (扇ぐ) conflates two distinct verbs. Sense 1 is 扇ぐ (godan-gu, "to fan"). Sense 2 is 煽る/扇る (godan-ru, "to incite") — examples ex3, ex5, ex6 all use the form 扇る with okurigana る, which is the wrong conjugation class for the godan-gu headword. 07924_aoru already covers fan/incite/tailgate comprehensively. Recommended fix: remove sense 2 + the three sense-2 examples from 00004_aogu and let 07924_aoru carry the incite meaning. A cross-reference between the two has been added.
