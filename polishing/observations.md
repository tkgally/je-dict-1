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

_(All observations through 2026-05-15 sessions 001–007 have been harvested by the wiki maintenance session of 2026-05-16.)_

## 2026-05-16 — comprehensive polish session 001 (entries 01603–01627)
- [pattern] Several entries in the 01600s had a stub conjugation field `{"type": "suru", "prefix": "..."}` alongside a full conjugation table — a clear artifact from early entry creation. Entries 01624 (維持) and 01626 (意地悪) both had this. The add_conjugations.py script likely created the full table without checking for an existing stub. Worth checking if earlier entries have the same issue.
- [pattern] Some adverb entries in this range incorrectly had verb conjugation tables added (01604 ますます had a full godan table with verb_class tag). The add_conjugations.py script may be matching on POS string too broadly (e.g., picking up "adverb, suru verb" entries that aren't really verbs). Worth auditing.
- [pattern] Many examples in this range had missing inline links for sentence-final です・か・ます — suggesting earlier polish passes didn't catch these terminals consistently.
