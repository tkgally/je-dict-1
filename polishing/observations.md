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

_(All observations through 2026-06-03 session 008 have been harvested by the wiki maintenance session of 2026-06-04.)_

## 2026-06-04 session 012 (entries 05095–05120)

[pattern] Many entries in the 05095–05120 range had clearly wrong semantic tags — cosmetics tagged "electronics," sunscreen tagged "electronics," ガイド tagged "tool," 姑 tagged "animal-insect." These appear to be systematic AI generation errors in original batches. A targeted audit of semantic tags in the general tier (05000–06000) would likely surface many more.

[pattern] Entries for culturally specific Japanese concepts (アイドル, 役者, 歌舞伎役者) often have notes that reference related concepts without inline links. These were added in this session, but the pattern suggests that post-creation inline-link passes are particularly valuable for culturally rich entries.

## 2026-06-04 — comprehensive polish session 013 (entries 05121–05141)

[tooling] `add_conjugations.py` falsely detects godan verbs whose reading ends in する (e.g., すする 05127) as suru compounds, generating malformed forms like {啜|すす}るする. The fix is to check whether the verb_class is explicitly "godan-*" before applying the suru detection. Manual conjugation was required for 05127_susuru.

[entry] 05124_shiwa notes contain `{笑|え}い{皺|じわ}` — the reading え for 笑 looks wrong (should be わら for 笑い皺). Flagged for furigana-correctness review.

[pattern] Business/logistics cluster (05132–05138: 受注, 発注, 納品, 出荷, 関税, 物流, 流通) has dense internal cross-references; the inline-link pass revealed these entries are well interconnected. Semantic tag "communication" on 05134_nouhin seems wrong — delivery of goods is not communication; suggest "action" or a logistics tag.

[pattern] 05137_butsuryuu had furigana error: {会社|がいしゃ} in both an example and the notes — corrected to {会社|かいしゃ} in this session. Systematic furigana errors in AI-generated entries may be more common in compound words inside notes fields (less frequently checked than headword furigana).
