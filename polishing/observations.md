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

_(All observations through 2026-05-31 session 006 have been harvested by the wiki maintenance session of 2026-06-01.)_

## 2026-06-01 — comprehensive polish session 001 (entries 04533–04553)
- [pattern] Several entries had clearly wrong semantic tags from initial creation: 04547_dekoboko (`furniture, tool`→`general`), 04549_densen (`body-part`→`general`), 04550_taikin (`time-general, tool`→`work`), 04535_sangurasu (`general`→`clothing`), 04540_teppou (`general`→`weapon`), 04544_uchiwa (`electronics`→`tool`). The tool that creates initial entries appears to select tags without adequate category review.
- [pattern] Compound suru-verbs in the 04540–04553 range (勤務、退勤、出勤、昇進) all had good conjugation tables already in place from add_conjugations.py.
- [entry] 上皇 (じょうこう, Emperor Emeritus) needs an entry — appears in notes for 04546_tennou and in the news; core vocabulary for understanding modern Japanese imperial system.

## 2026-06-01 — comprehensive polish session 003 (entries 04574–04594)
- [pattern] Several entries in this range had wrong semantic tags from initial creation: 04583_kikitoru (`geography,work`→`communication,action`), 04585_hayamaru (`electronics,time-general`→`action`), 04589_kareru (`furniture`→`nature,action`), 04590_omoikiru (`communication`→`action`). The pattern of incorrect initial tags continues in this range.
- [pattern] ASPECT section template artifact `{ている}` (uses furigana braces on a hiragana-only word) found in 04584, 04585, 04587, 04592, 04594. Should be plain `(ている)` with no braces.
- [pattern] `[Register: Neutral]` legacy artifact at end of notes found in 04583, 04586, 04588, 04590, 04591, 04593. These were removed.
