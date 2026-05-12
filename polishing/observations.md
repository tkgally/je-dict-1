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

## 2026-05-11 — comprehensive polish session 003 (entries 00451–00461)
- [entry] 03537_nou: semantic tag is "clothing" but should be "body" — pre-existing misclassification

## 2026-05-11 — comprehensive polish session 006 (entries 00513–00537)
- [entry] 00536_itsu: has incorrect conjugation field (godan-tsu forms applied to an adverb — forms are nonsensical like いちます, いたない) and wrong tag verb_class: "godan-tsu"; the conjugation block and that tag should be removed entirely
- [entry] 00517_muzukashii: had incorrect antonym cross-ref to 02640_yasashii (優しい = kind/gentle, not the antonym of difficult); also had duplicate 00475_yasashii; both removed in this session, keeping only 00765_yasashii (易しい) and 00713_kantan

## 2026-05-12 — comprehensive polish backfill (entries 00436–00450)
- [pattern] 2026-05-12: session 003 (PR #2285) skipped entries 00436-00450 by hallucinating prior session coverage instead of reading progress.txt. Consider adding a hard "echo current next: value back to me before processing the first entry" guard to comprehensive_polish.md's Entry selection section.

## 2026-05-12 — comprehensive polish session 001 (entries 00584–00606)
- [pattern] Bogus godan-conjugation-on-adverb keeps surfacing: 00536_itsu (session 006), 00601_yoku and 00602_mou (this session) all carried `conjugation` blocks with fabricated godan forms (e.g., よかない/もわない) and a matching `verb_class: godan-*` tag, despite `part_of_speech == "adverb"`. Worth a one-shot scan + cleanup across the whole dictionary for `non-verb POS + conjugation field` rather than catching them one entry at a time.
- [tooling] A `build/find_bogus_conjugations.py` (or extension to `check_consistency.py`) that flags any entry where `part_of_speech` is not in {verb-godan, verb-ichidan, verb-suru, verb-irregular, adjective-i} but a `conjugation` field exists, would let us batch-clean these in one pass. Same check should also flag a `verb_class` tag on a non-verb POS.
