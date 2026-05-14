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


## 2026-05-14 — comprehensive polish session 006 (entries 01255–01282)
- [pattern] Two adverb entries (01267 しばらく, 01281 なるべく) had bogus godan conjugation tables with nonsensical forms (e.g., しばらかない, なるべかない) and `verb_class: "godan-ku"` in tags. This was likely generated incorrectly by the AI model. Other adverb entries in the same ID range should be audited for the same issue.


## 2026-05-14 — comprehensive polish session 007 (entries 01283–01304)
- [entry] 01300 ございます: conjugation table uses wrong template (regular godan/ichidan verb forms instead of polite-verb forms); needs manual correction or a new conjugation template for polite-only verbs
- [entry] 01293 汚れる: was misclassified as verb-godan in POS tag and verb_class; corrected to verb-ichidan with regenerated conjugations this session. Other entries near this range may have similar misclassifications worth a spot-check.
