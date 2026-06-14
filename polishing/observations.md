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

_(2026-06-14 wiki (Routine v2) harvest: processed 6 observations from the two 2026-06-14 Routine runs (polish 06121–06128 + priority lanes; accuracy-review 4801–4982). Filed: Cleanup Backlog P11 update 2026-06-14 (semantic tag errors in the 06121–06128 cultural-vocabulary cohort — hibachi clothing→daily-life, kouden time-general→culture, souryou communication→shopping); Cleanup Backlog P21 update 2026-06-14 (general inline-link absence reaches the 06120s noun cohort + new furigana-in-link-base-form malformation sub-pattern from low-ID priority lane, `⟦花→{花|はな}：⟧` should be `⟦花→花：⟧`, with proposed detector); Tooling Backlog item 17 update 2026-06-14 (the `general`-too-broad tag noise now emitted at **error** severity in the 4801–4982 run — 73 error-tag flags, only 13 genuine — defeating the error/warn triage split; proposed severity rule for the prompt). The [entry] 06127_kouden→不祝儀袋 item was added as candidate C21925 (always-on capture). The furigana-screening 0%-precision [pattern] is consistent with the documented calibration note — no new wiki page needed. All six observations cleared.)_

## 2026-06-14 — Routine v2 polish session 004 (priority lines 113–131 + frontier 06129–06132)
- [pattern] Priority "notes" lane high-frequency basic/core entries (00469_matsu, 00039_erai, 01112_tsurai, 01133_kusai, 00585_akai) came back already fully polished — complete inline links, valid in-list tags, well-structured notes. 5 of 7 priority entries needed no changes, so priorities were regenerated and the cursor reset to line 1. The notes-quality ranking appears stale for these long-settled adjectives; consider excluding entries whose `modified` is recent OR whose note already passes a structural threshold from the notes priority ranking so the lane targets genuinely thin notes.
- [pattern] Frontier 06129–06132 (consumer/business suru-noun cohort) all had ZERO inline links plus template-default semantic tags: 06129_kaiyaku had `geography,work` (→ business), 06130_henkin had `action` (→ money). Same zero-link + template-tag signature seen in the 06121–06128 cohort — the 06100s–06130s general-vocabulary band needs a sweep.
- [entry] 06131_toiawase: noun headword 問い合わせ, but ex1/ex2 demonstrate the compound verb 問い合わせる (separate entry 17737_toiawaseru) and the conjugation table lists the unnatural 問い合わせする (suru) paradigm. Linked the verb forms to 17737 this run, but the entry would benefit from restructuring to separate the noun headword from the verb lemma (or pointing the verb examples cleanly at 17737).
- [pattern] バツニ "divorced twice" already exists as entry 27329_batsuni, but 00012_batsu's notes still marked it `noentry`; a `noentry` marker pointing at a word that has since gained an entry is a self-healing target for a detector (scan `：noentry⟧` against word_id_lookup.json).

- [tooling] accuracy reviewer over-flags `general` semantic tag as "too broad" (~120/496 entries in 4983-5482) and suggests in-list substitutions; `general` is a valid VALID_SEMANTIC tag, so these are noise per the semantic-tag policy. Prompt could be told `general` is an accepted fallback and not to flag narrowness between in-list tags. (Routine 2026-06-14)
- [pattern] Entries ~5000-5300 carry many genuine clearly-wrong semantic tags (body-part/communication on 柱, emotion on 箪笥, time-general on ベランダ/わさび, food on コック/ウェイター, body-part on mimetic adverbs). 26 fixed this run. Also widespread formality/politeness data errors in this range (e.g. 茶漬け politeness=honorific, 羊羹 formality=formal) left for a dedicated register-tag pass. (Routine 2026-06-14)
