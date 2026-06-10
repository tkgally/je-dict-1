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

_(All observations through 2026-06-09 session 050 and accuracy-review session 001 have been harvested by the wiki maintenance session of 2026-06-09. Session 045: semantic tag drift in 05784–05804 range; 05747_kirisuteru body-part tag filed to Entry Follow-ups. Session 049: tag drift in 05891–05915; 08116_rokku missing lock sense filed to Entry Follow-ups. Session 050: tag drift in 05936–05953; 空前絶後/史上初/悪事 filed to Entry Follow-ups and added as candidates C21844/C21845/C21846. Accuracy-review session 001: formality over-tagging in early entries added as Cleanup Backlog P17; semantic over-application patterns noted in P11 update.)_

_(2026-06-10 wiki (Routine v2) harvest: processed all observations from the four 2026-06-10 Routine runs — polish session 007, accuracy-review session 002, and the routine v2 polish/new-entries/systemic-fix sessions. Filed: Cleanup Backlog P11 update (05970–05990 medical/aviation clusters + 00201–00450 low-ID fixes), P17 update (formality to 00450), new P18 ('descriptive' catch-all), P4 notes-level sub-pattern (06xxx compound verbs + detector gap); Tooling Backlog items 11 (validate.py inline-link gate), 12 (review_runner deep-range scoping), 13 (review_runner response-parsing robustness); Entry Follow-ups (01385/02485 気持ち duplicate, 〜込む/掛かる morpheme gaps); deepened topics/schema-tag-reliability.md (undefined-tag-semantics: `descriptive` + `body-internal`; empirical flag precision); created topics/quality-metrics.md. The `[skill]` body-internal recommendation is recorded in the session log. Only the metrics `[pattern]` below remains for the next harvest.)_

## 2026-06-10 — wiki (Routine v2) metrics-trend review

- [pattern] **Review queue not converging.** The first `topics/quality-metrics.md` snapshot shows `reviews/queue.txt` sitting at ~19,450 entries — about two-thirds of the dictionary — and barely moving across the four 2026-06-10 Routine runs (19,602 → 19,607 → 19,444 → 19,450; net −152 over the whole day). Only `accuracy-review` drains it (−163 on its run), while `new-entries` (+5) and `systemic-fix` (+6) re-add their own changed entries by design and CI re-adds anything that later changes. At ~150/run net and roughly one run in five being accuracy-review, the queue behaves as a permanent surveillance backlog, not something that reaches zero. This is the metric most clearly trending the wrong way (or rather: not trending toward convergence at all). Options for the curator: accept the queue as surveillance-only (rename/reframe it so its size isn't read as "debt"), fund a cheaper bulk screening tier, or have accuracy-review take a larger range per run. Revisit once `metrics-history.jsonl` has ≥10 lines so the slope is real rather than a one-day reading. (Captured here for the next wiki harvest; full analysis in `planning/wiki/topics/quality-metrics.md`.)
