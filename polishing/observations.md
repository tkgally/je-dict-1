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

_(2026-06-12 wiki (Routine v2, run 2) harvest: processed 2 observations from the 2026-06-12 systemic-fix and accuracy-review runs. `[tooling]` UTF-8 replacement characters (U+FFFD) in 246 furigana wrappers → Tooling Backlog item 16. `[tooling]` 54.6% flag rate on 03301–03800 accuracy-review driven by `general`-tag false positives → Tooling Backlog item 17 + documented in topics/quality-metrics.md Finding §8. Both items cleared.)_

_(2026-06-13 wiki harvest: processed 4 observations from the 2026-06-13 accuracy-review and polish sessions. `[tooling]` accuracy-review 03801–04300 `general`-tag noise (50% flag rate, 88% of tag flags = `general` flagged as "too broad") → Tooling Backlog item 17 update + schema-tag-reliability.md new subsection on reverse-direction noise. `[pattern]` `transportation` tag on 06107_junshu → Cleanup Backlog P11 update 2026-06-13. `[pattern]` `general`-instead-of-specific on 06101_hakumai/06106_katsuo → same P11 update. `[entry]` 06109_karorii needs inline links → Entry Follow-ups. All four observations cleared.)_

[tooling] accuracy-review 4301-4800: 44% flagged rate (221/500 entries) well above 20% noise threshold. Dominant families: "general tag too broad" (71, all in-list nits), formality tags (27), misc narrowness (95). Genuine errors were animal-taxonomy mismatches (animal-fish for squid/octopus/crab, animal-insect for frog and 〜長), wrong-category tags (geography/time-general for 発電; economy for 損得), factual gloss errors (recyclable for 再生可能, leotards for タイツ), and rolling-vs-lying translations for 寝転ぶ. Applied 18, rejected 211. Reviewer prompt may over-flag in-list tag substitutions.

## 2026-06-14 — Routine v2 polish session (priority lines 83–112; frontier 06121–06128)

- [pattern] Frontier entries in the 06121–06128 range (hibachi, kakejiku, tenugui, suzuri, ochuugen, oseibo, kouden, souryou) all had zero inline word links in both examples and notes — a systematic gap for entries created in early 2026 before inline-link polishing was established. All 8 were polished this session.
- [pattern] Semantic tag errors cluster in same 06121–06128 cohort: hibachi had `clothing` instead of `daily-life`; kouden had `time-general` instead of `culture`; souryou had `communication` instead of `shopping`. Suggests entries from this period should be audited for semantic tag accuracy.
- [pattern] Priority lane entries (00391 sunao, 00717 kirei, 01312 ichido, 00908 warui, 00478 motsu, 00964 kyoudai) showed recurring issues: furigana inside link base forms (e.g. `→{花|はな}：` instead of `→花：`), missing particle links, and missing function-word links (こと, ので, じゃない). These patterns are consistent with the early-entry cohort.
- [entry] 06127_kouden notes reference 不祝儀袋 (ふしゅうぎぶくろ) — the special envelope for condolence money — as noentry; good candidate to add if coverage of funeral customs is desired.

## 2026-06-14 — routine accuracy-review (entries 4801–4982)
- [tooling] `review_accuracy.py` tag dimension over-flags: 73 error-severity tag flags across 182 entries (42% of entries), but only 13 were genuine wrong-category AI-artifact mis-tags (body-part on 手当, geography on 容量/発信, animal-mammal on 焼き物/まな板, leisure on 反応/合唱, etc.) + 1 not-in-list (economy→finance). The other ~60 were "'general' is too broad, use plant-tree/finance/food/society" in-list narrowness nits that the §A semantic-tag policy says to reject. The reviewer prompt should distinguish "tag is factually wrong for the headword" (worth flagging) from "a more specific in-list tag exists" (not an error) — e.g. instruct it not to flag 'general'/'descriptive' merely for being broad. Would cut tag-flag volume ~80% and make adjudication tractable.
- [pattern] Furigana screening over this already-polished range was 0% precision: all 9 screening flags + all deep-pass flags (がらがら声→ごえ, 穴熊囲い→がこい, 端攻め→ぜめ, 合炊き→だき, 麻婆/木綿/絹ごし豆腐→どうふ) were rendaku-in-compound or standard-onyomi false positives. Consistent with the documented 0–5% precision note.
