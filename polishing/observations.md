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

_(2026-06-15 wiki (Routine v2) harvest: processed the orphaned 4301-4800 accuracy-review `[tooling]` note plus all observations from the 2026-06-14 routine polish session 004 and the two 2026-06-15 routine polish runs — 15 observations total. Filed:
- **Cleanup Backlog P11 update 2026-06-15**: frontier tag errors (06129 geography/work→business, 06130 action→money; 06139 body-part→movement, 06140 occupation→proverb, 06142 communication/furniture→proverb) + the 05000–05300 pocket of genuine wrong tags (26 fixed: 柱, 箪笥, ベランダ/わさび, コック/ウェイター, mimetic adverbs).
- **Cleanup Backlog P17 update 2026-06-15**: `formal` over-applied to everyday 06xxx compound action verbs (06135 突き飛ばす, 06136 投げ捨てる contradicting their own "Neutral" REGISTER notes) + the 05000–05300 register pocket (茶漬け honorific, 羊羹 formal); mechanically-detectable slice = tag contradicts REGISTER note.
- **Cleanup Backlog P21 update 2026-06-15**: zero inline links across the 06129–06149 frontier cohorts + new **hiragana-base-form** orthography sub-pattern (claude-opus-4-6 entries use `→さかな` instead of `→魚`; cosmetic, links resolve).
- **Tooling Backlog item 17 update 2026-06-15**: `general`-noise confirmed continuous across 03301–05482 (4301-4800 44% / 4983-5482 ~120 flags); genuine-error rate ~4–8%.
- **Tooling Backlog new item 18**: check_example_headword.py false-positive reduction (skip U+FFFD, strip ～/〜 prefix, accept katakana-of-reading).
- **Tooling Backlog new item 19**: stale-`noentry` inline-link detector (00012_batsu→27329, 05528/05530→28923/28925 are stale; deterministic self-healing scan against word_id_lookup.json).
- **Tooling Backlog new item 20**: notes-priority ranking staleness filter (exclude recently-modified / structurally-adequate notes; 5 of 7 priority-lane entries were no-ops).
- **Entry Follow-ups**: 06131_toiawase noun-headword-vs-verb-lemma restructure.
- **Cleared as already RESOLVED**: the two U+FFFD mojibake `[tooling]`/`[entry]` observations (05528/05530 + the dictionary-wide 244-entry note) — Tooling Backlog item 16 shipped 2026-06-15 (`build/check_mojibake.py` + a sweep to zero U+FFFD + a validate.py guard); confirmed 0 remaining this session.
All 15 observations cleared.)_

_(2026-06-16 wiki (Routine v2) harvest: processed the 3 observations from the 2026-06-15 routine polish/accuracy-review runs. Filed: **Cleanup Backlog P11 update 2026-06-16** (in-list-but-wrong-category tag drift across 0552x–0570x: yojijukugo→furniture/leisure, 〜的/〜性→time-general/education, concrete nouns 天秤/苦楽/頷く mis-tagged — needs accuracy-review `tags` pass, not the P20 unknown-semantic detector, since the tags are in-list); **Cleanup Backlog P21 update 2026-06-16** (06143–06149 yojijukugo cohort, e.g. 06143_oninikanabou, zero inline links — same pre-inline-link creation batch as the 06137–06149 cohort already noted); **Tooling Backlog item 17 update 2026-06-16** (accuracy-review tags noise confirmed continuous up to 05703: 5521–5703 ran 39% flagged, mostly in-list narrowness nits — fifth consecutive sweep with the same profile). All 3 observations cleared.)_

- [tooling] accuracy-review (2026-06-16, range 5704-6139): 31% entry flag rate (137/436), above the 20% noise threshold. Dominant noise family = "in-list semantic tag too broad/narrow" (general→specific domain), ~60 flags rejected per policy. The `tags` reviewer prompt could be tuned to suppress in-list narrowness substitutions and flag only out-of-taxonomy or genuinely-wrong-domain tags, which is where precision was high this run.
- [pattern] Heavy semantic tag-drift (Cleanup P11) concentrated in the 5700-6100 ID block: 50 entries carried genuinely-wrong or invalid concrete-domain semantic tags (electronics/furniture/weather/body-part/geography/leisure misapplied; `onomatopoeia` missing on clear mimetic words; invalid `payment`/`body`/`death`). This batch-creation era likely warrants a dedicated tag sweep beyond what accuracy-review reaches incrementally.
- [entry] Stale `noentry` inline links found during review: 05803 `創業者→noentry` (now entry 29027_sougyousha) and 05720 `ぼりぼり→noentry` (now entry 28996_boribori). An inline-link refresh pass should resolve these.

- [pattern] Malformed furigana wrappers in notes: 06147_jiboujiki had `{やけになる}` and `{投|な}げやりになる}` — the `{...}` (kanji|reading) syntax wrongly applied to whole kana phrases / with a stray trailing `}`. These render as literal braces on the site and slip past furigana-coverage checks. Likely present across the same early-2026 yojijukugo batch; `build/check_furigana_format.py` could be extended to flag `{...}` spans lacking a `|` separator.
- [entry] Partial progress on Cleanup P21 (zero-inline-link yojijukugo cohort): added full inline-link coverage to 06147, 06148, 06149 (idioms) and 06150 (コーディング) this run. 06151+ in the same batch still pending.

- [tooling] review_runner.py --pass screening on 118 IDs was killed by the 540s `timeout` wrapper at ~59/118 entries (~9s/entry via gemini-2.5-flash). For systemic-fix self-checks over 100+ IDs, either raise the timeout, batch the screener into ~50-ID chunks, or accept partial coverage. All 11 flags from the 59 screened were false positives (rendaku-in-compound, okurigana/partial-reading "correct by design", and screener input-truncation artifacts like `そうが)` / `しんりょ`). [systemic-fix routine 2026-06-16]

- [tooling] The notes-quality prioritizer (score_note_quality.py / prioritize_polishing.py) ranks structured particle/function entries (が 00051 score 30, は 00079 score 35, ぐらい 02900 score 50) at the very top of `priority/notes.txt`, but these entries are actually comprehensive — their content lives in dedicated structured fields (predicates_requiring, particle_contrasts, information_structure, fixed_patterns, common_mistakes) that the scorer ignores while only measuring the `notes` string. Result: the priority lane keeps surfacing already-excellent entries as "worst notes." Suggest the scorer credit structured fields (or skip particle entries that have them). Observed in routine polish 2026-06-16: 4 of 7 priority-lane entries needed no changes for this reason. [routine polish 2026-06-16]
- [tooling] furigana screener timed out (580s) mid-range over 6140-6650, covering only 6140-6223 (84 entries); all 11 flags were partial-idiom/okurigana-split false positives. Consider chunking screening into ~100-entry sub-ranges to fit the timeout. (2026-06-16T21:28:05Z)
- [pattern] Systemic garbage-semantic-tag bug in the 6140-6340 range: ~30% of entries had categorically-wrong auto-assigned semantic tags (朱肉=animal-mammal, proverbs tagged clothing/animal-insect, idioms tagged time-general/leisure). Fixed 61 in this accuracy-review run. A dedicated systemic-fix detector (semantic-tag-vs-headword sanity; proverbs/yojijukugo should carry proverb/idiom) would clear the rest faster. (2026-06-16T21:34:53Z)
