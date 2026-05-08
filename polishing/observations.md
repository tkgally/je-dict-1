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

## 2026-05-08 — comprehensive polish session 002 (entries 00006–00025)
- [tooling] `build/verify_furigana.py` raises false positives on inline link metadata. After `FURIGANA_PATTERN.sub('', notes)` it still sees the kanji that follow the `→` in `⟦{時間|じかん}→時間：00468_jikan⟧` and reports them as unannotated. Notes that contain inline links to entries with kanji headwords therefore look broken when they are not. Suggested fix: also strip the `→…：…⟧` link tail (and the leading `⟦`) before counting kanji. The render pipeline doesn't render that tail, so it shouldn't count toward coverage.
- [pattern] The vast majority of older noun entries (in this 00006–00025 stretch, almost all of them) have linked example sentences but **unlinked notes**. Specifically, "COMMON COLLOCATIONS / RELATED WORDS / TYPES OF X / COMPOUNDS" bullet lists in `notes` typically still use bare `{kanji|reading}` without `⟦...⟧` wrappers. This is by far the dominant tier-1 polish task for these entries — far more than missing furigana or example issues. Every single entry 00007–00025 needed this work.
- [pattern] Many older noun entries also lack any `cross_references` to obvious neighbors that they explicitly mention in their notes (e.g., 00010_banchi → 住所/丁目/号; 00014_biyou → 美容院/美容師/健康; 00018_booto → 船/ヨット/カヌー; 00023_bushu → 漢字/画数). When these entries get inline-linked, the cross_references list often deserves to be populated at the same time. A possible tooling helper: scan an entry's notes for `→<id>⟧` link targets that are not already in `cross_references`/`prominent_see_also`, and surface them as suggested cross-refs.
- [entry] 00007_auto: フライ (fly ball, baseball sense) has no entry. The existing 11124_furai is "deep-fried food" only. Recommend expanding 11124_furai with sense 2 (baseball fly ball), since both are written フライ. Currently the example sentence uses a `noentry` marker, which is correct but a placeholder.
- [pattern] 09491_choume was missing the `cross_references` field entirely (not just empty). The schema seems to allow this but the build's symmetry checks may be silently skipping such entries. Worth confirming `check_consistency.py` flags entries that lack the field altogether so that they get back-link audits like everyone else.
