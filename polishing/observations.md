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

_(2026-06-10 wiki (Routine v2) harvest: processed all observations from the four 2026-06-10 Routine runs — polish session 007, accuracy-review session 002, and the routine v2 polish/new-entries/systemic-fix sessions. Filed: Cleanup Backlog P11 update (05970–05990 medical/aviation clusters + 00201–00450 low-ID fixes), P17 update (formality to 00450), new P18 ('descriptive' catch-all), P4 notes-level sub-pattern (06xxx compound verbs + detector gap); Tooling Backlog items 11 (validate.py inline-link gate), 12 (review_runner deep-range scoping), 13 (review_runner response-parsing robustness); Entry Follow-ups (01385/02485 気持ち duplicate, 〜込む/掛かる morpheme gaps); deepened topics/schema-tag-reliability.md (undefined-tag-semantics: `descriptive` + `body-internal`; empirical flag precision); created topics/quality-metrics.md. The review-queue-convergence `[pattern]` is fully reflected in topics/quality-metrics.md (finding #5 + implications) and in topics/content-pipeline.md (review-queue section); no additional wiki page needed.)_

_(2026-06-11 wiki (Routine v2) harvest: processed all observations from the 2026-06-10/11 accuracy-review sessions. Filed: Tooling Backlog item 14 (accuracy-review prompt: valid-tag list + semantically-plausible guidance — addresses `[pattern]` gemini false "invalid tag" claims + `[tooling]` 27.5% false-positive rate + `[tooling]` "too narrow/broad" flagging from sessions 002–003); Entry Follow-ups 06917_zo (wrong formality/semantic tags on sentence-final particle ぞ). All four observations cleared.)_

_(2026-06-11 curator session harvest: acted on the `[tooling]` 37%-flag-rate observation from the 1651–2100 accuracy-review pass. Root cause was the tag-vocabulary drift (17,762 out-of-taxonomy instances), not reviewer noise alone. Fixes: curator tag-policy decision (VALID_SEMANTIC expanded with 30 established tags), review_accuracy.py prompt v3 (no "too narrow/broad" nits, formality flags only on unambiguous contradictions), standing adjudication rule in routine2.md §A, Cleanup Backlog P20 migration item with `check_tag_drift.py --check unknown-semantic` detector. See topics/schema-tag-reliability.md → "The tag-vocabulary contradiction and its resolution".)_

_(2026-06-11 wiki (Routine v2, run 2) harvest: processed 2 observations from the 2026-06-11 routine v2 polish session (entries 06038–06047). `[pattern]` compound verb inline-link gaps → Cleanup Backlog P21 (unlinked 自動詞/他動詞 labels and particles in compound-verb notes). `[tooling]` lint rule for unlinked 自動詞/他動詞 → Tooling Backlog item 15. Both items cleared.)_

_(2026-06-12 wiki (Routine v2) harvest: processed 2 observations from the 2026-06-11 routine v2 polish session (entries 06048–06067). `[pattern]` compound/suru-verb object-category semantic tag errors → Cleanup Backlog P11 update 2026-06-12. `[pattern]` general inline-link absence across 06000 cohort → Cleanup Backlog P21 update + compound-verbs.md polishing-findings section. Both items cleared.)_

- [tooling] 246 entry files in the 20000-29000+ range (and some earlier) have UTF-8 replacement characters (U+FFFD) embedded in furigana wrappers — either in the kanji or reading components of {漢字|よみ} markup. Root cause unknown (likely a batch creation episode where UTF-8 multi-byte sequences were corrupted). The `check_example_headword.py` detector correctly flags these because the headword kanji can't be found in the corrupted text. Needs a dedicated systemic-fix run: detect all affected files, identify the corrupted character by context (the surrounding intact kanji + the furigana reading usually make the missing character unambiguous), and repair the replacement chars. Scope: 246 files, estimated 1-3 corrupted chars per file. See the full list in build/check_example_headword.py output for the 2026-06-12 systemic-fix run.
