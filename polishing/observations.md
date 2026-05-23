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

_(All observations through 2026-05-21 session 007 have been harvested by the wiki maintenance session of 2026-05-22.)_

## 2026-05-23 Session 003

[pattern] Semantic tag "general" appears frequently across entries 03011–03035 where more specific tags apply (time-general, transportation, work, weather, etc.). This is a systematic quality gap; a targeted pass to replace "general" semantic tags would improve searchability.

[pattern] Katakana words (メール, バス, ネット) are stored with hiragana readings in word_id_lookup.json (めーる, ばす, ねっと). Lookups for katakana headwords must use the `by_headword` key, not `by_reading` with the katakana string.

[pattern] 03032 doukyuusei (同級生): examples 2 and 3 are nearly identical ("I ran into a high school classmate" vs "I met a classmate"). Needs a more diverse example set — one could be replaced with a context showing 同級生 used for reunion or nostalgia.

## 2026-05-23 Session 005

[pattern] Several entries in the 03056–03077 range had structurally corrupt conjugation data: an incomplete object `{type, prefix}` or `{type, ending, stem}` appearing before definitions, followed by a proper full forms table at the end. Python's json.load uses the last occurrence when keys are duplicated, so the full table was operative, but the dead first object is still malformed JSON (duplicate keys). Fixed in 03057, 03064, 03072, 03077. Other verb/suru entries in this range may have the same issue and should be checked.

[pattern] Semantic tag "general" appeared in 7 of 22 entries (03056–03077) and was replaced with more specific tags. This confirms the pattern noted in Session 003 extends well beyond the 03011–03035 range — a systematic sweep of all entries using "general" as the sole semantic tag is warranted.
