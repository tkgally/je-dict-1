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

_(2026-06-17 wiki (Routine v2) harvest: processed all 9 observations from the 2026-06-16 routine polish / accuracy-review / systemic-fix runs. Filed:
- **Cleanup Backlog P11 update 2026-06-17**: the heavy semantic tag-drift across the 5700–6340 block — ~50 wrong/out-of-taxonomy concrete-domain tags in 5700–6100 (incl. missing `onomatopoeia` and invalid `payment`/`body`/`death`) and ~30% garbage tags in 6140–6340 (61 fixed in one accuracy-review run; 朱肉→animal-mammal, proverbs→clothing/animal-insect). Recommends a semantic-tag-vs-headword detector.
- **Cleanup Backlog P9 update 2026-06-17**: new no-pipe brace-span + stray-trailing-brace sub-pattern (06147_jiboujiki `{やけになる}`, `{投|な}げやりになる}`), likely across the 06140s yojijukugo batch.
- **Cleanup Backlog P21 update 2026-06-17**: partial backfill progress — 06147–06150 inline-linked, 06151+ pending.
- **Tooling Backlog item 6 update**: proverb/yojijukugo-lacking-`proverb`/`idiom` as a high-precision drift signal for `check_tag_drift.py`'s semantic-mismatch heuristic.
- **Tooling Backlog item 8 enhancement**: extend `check_furigana_format.py` to flag no-pipe `{...}` spans and unbalanced braces (the shipped regex requires a pipe and misses them).
- **Tooling Backlog item 17 update 2026-06-17**: sixth confirmation of the in-list-narrowness `tags` noise family (5704–6139, 31% flagged).
- **Tooling Backlog item 20 update 2026-06-17 (structured-field blind spot)**: notes-quality scorer ranks comprehensive particle/function entries (が/は/ぐらい) as "worst notes" because it only measures the `notes` string and ignores structured fields.
- **Tooling Backlog new item 21**: chunk review_runner/screening into ~50–100-ID sub-ranges (two timeout truncations this week: 118-ID self-check and 6140–6650 screen).
- **Entry Follow-ups**: stale `noentry` links 05803 創業者→29027 and 05720 ぼりぼり→28996.
All 9 observations cleared.)_

## 2026-06-17 — routine polish session (priority lane 00xxx; frontier 06154–06156)
- [pattern] Priority lane (notes ranking) again surfaced already-clean basic particle/adjective entries: of 8 checked (00051_ga, 00079_ha, 00733_mazui, 02900_gurai, 00740_oishii, 00484_mo, 00864_kowai, 00025_chiisai), 7 needed no changes — confirms structured-field blind spot (existing item 20). Regenerated priorities + reset cursor this run.
- [tooling] verify_furigana correctly catches unwrapped kanji in particle structured fields (00484_mo had 数量/一 unwrapped in both `fixed_patterns` and `notes`), but these slip past casual review since the example/notes prose looked complete. Worth a targeted sweep of `fixed_patterns`/`particle_behavior`/`question_word_patterns` pattern strings across all particle entries for furigana completeness.
- [pattern] Frontier 06154–06156 (loanword + 出社/退社 cluster) had ZERO inline-link coverage in examples and notes despite being created entries — recent-vintage general entries are systematically missing inline links. 06156 was modified 2026-06-16 yet still had no links, so a prior touch did not add them.

## 2026-06-17 — routine new-entries (29302–29311)
- [pattern] candidate_words.json is dominated by low-quality corpus-harvest noise (compositional numerals/counters like 二百/三歳, productive 〜化/〜性/〜率/〜器 compounds, place names, transcription typos, and proper nouns such as スポンジボブ). Across the oldest ~160 candidates and a mid-range sample, fewer than ~10% are well-formed standalone learner vocabulary. The only consistently good candidates are the recent "seen in entry" additions. Curator restock with vetted words and/or a cleanup pass would let new-entries runs hit their ~20 target without padding from junk.
- [tooling] A pre-filter for manage_candidates / corpus harvesting that rejects bare numeral+counter forms, single-suffix derivations, and obvious proper nouns would raise candidate-pool signal substantially.

## 2026-06-17 — routine accuracy-review (06341–06540)
- [pattern] The pre-frontier general-tier block 6341–6540 carries heavy AI-artifact semantic-tag drift: ~50 entries had a flatly-wrong single semantic tag (e.g. 取捨選択→body-part, どうせ→furniture, 乱視→furniture, 家畜→work, 憤慨→geography, アンチ→electronics, 健気→clothing). These are category errors, not narrowness — applied 50 fixes this run. The whole pre-polish-frontier range likely has similar density; an accuracy-review tags sweep across 6157–~7000 would catch most.
- [pattern] Cross-model accuracy review also surfaced ~51 "general → more-specific in-list tag" suggestions in this range (e.g. 害虫→animal-insect, 蜜蜂→animal-insect, 踝→body-part, 経理→business). Current semantic-tag policy (2026-06-11) rejects in-list narrowness substitutions, so all were rejected — but many of these `general` tags are genuinely uninformative where an obviously-correct specific tag exists. Curator may wish to reconsider whether `general`→clearly-correct-specific should be an APPLY case (distinct from leisure-vs-daily-life churn).
- [pattern] Slang/colloquial entries in this range were systematically mis-tagged formality=formal (陰キャ, 陽キャ, リア充, コミュ障) despite their own glosses labeling them slang — a recurring artifact where the formality default landed on "formal" for casual neologisms.

## 2026-06-17 — routine (polish) session (frontier 06157–06160, priority lane が/は/まずい/ぐらい)
- [pattern] Entries from the 2026-01-17 creation batch (IDs ~6157+) systematically lack inline links in BOTH examples and notes. This run added full inline-link coverage to the examples of 06157–06160, but their dense glossary-style notes (COMPONENTS / CONTRAST WITH RELATED TERMS / COMMON COLLOCATIONS sections, plus loanword synonym lists) still have no links. A dedicated inline-link sweep over the 6157+ range — focused on notes — would close this; the example linking is tractable per-entry but the notes glossaries are heavy and partly noentry (loanwords).
- [tooling] The notes-priority list (polishing/priority/notes.txt) currently top-ranks already-complete basic particle/grammar entries (が 00051, は 00079, まずい 00733) that need no changes — 3 of 4 priority-lane entries this run were clean. The note-quality scorer appears to over-weight these structurally-rich particle entries (long structured fields like predicates_requiring/particle_contrasts) even when their notes/examples are fully polished. Consider down-weighting entries whose structured grammar fields already exist, or excluding the closed basic/core particle set from the notes-priority ranking.

- [tooling] (routine systemic-fix 2026-06-17) `build/review_runner.py --pass screening` is too slow for §4 self-checks: it screened only 24/51 entries before the 500s background timeout (a 2026-06-16 run similarly got 59/118). Per-entry serial API calls to gemini-2.5-flash dominate. Consider concurrent requests or a smaller default per-run cap so §4 furigana screening of a typical systemic-fix batch completes. Partial results are still written per-entry, so the run can continue, but coverage is incomplete.
- [pattern] (routine systemic-fix 2026-06-17) When resolving missing `target_id` on cross_references, the `by_reading` lookup fallback produces homophone false matches (有限/ゆうげん→幽玄, 小学/しょうがく→少額, 工夫/こうふ→工夫くふう). Only resolve on an exact headword+reading unique match. If a `resolve_cross_ref_targets.py` helper is ever built for this backlog item, it must require both fields to agree and must skip deliberately-labeled no-entry homophone/contrast pointers.

- [pattern] accuracy-review 06541–06840: heavy P11 concrete-domain semantic-tag contamination persists ABOVE the documented 5700–6340 block — 104/300 entries had clearly-wrong category tags (animal-mammal on ダッシュボード/打者, building+transportation on soccer-position loanwords, electronics/furniture/food on abstract nouns and adjectives). The reviewer's tags dimension caught these cleanly (error-severity). Suggests the P11 residue extends well past 6340; a targeted tags-only accuracy sweep of 6500–7500 would likely keep yielding ~30% apply rates.
- [pattern] accuracy-review 06541–06840: 28 entries with clearly domain-specific headwords (chisel→tool, stag beetle→animal-insect, cosmos→plant-flower, USB drive→electronics, carbon→science) sit at semantic ['general']. Policy rejects general→specific as noise, but in this range many are lazy-default 'general', not deliberate fallback. Curator may want a one-off general-retag pass for unambiguously single-domain nouns.
