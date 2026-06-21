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

_(2026-06-18 wiki (Routine v2) harvest: processed all observations from the 2026-06-17 routine polish / new-entries / accuracy-review / systemic-fix runs and the 2026-06-18 new-entries run. Filed:
- **Cleanup Backlog P11 update 2026-06-18**: the wrong-category tag residue quantified above the 5700–6340 block — 6341–6540 (~50 single-sole-wrong tags, 50 applied) and 6541–6840 (104/300 wrong-category tags applied); recommends a proactive accuracy-review `tags` sweep of 6157–~7500 ahead of the polish frontier.
- **Cleanup Backlog P13 update 2026-06-18**: the recurring `general`→clearly-correct-specific suggestions (~51+28 across the two sweeps) recorded as a **curator policy question** (lazy-default `general` on single-domain nouns vs. the current reject-all-narrowness policy); no Routine action until policy is set.
- **Cleanup Backlog P17 update 2026-06-18**: slang/colloquial neologisms (陰キャ/陽キャ/リア充/コミュ障) mis-tagged `formality: formal` — the inverse of the early-entry over-tag; mechanically detectable as gloss-slang-marker vs `formal`.
- **Cleanup Backlog P21 update 2026-06-18**: 06154–06160 zero-inline-link frontier (examples linked per-entry, notes glossaries still pending; 06156 modified 2026-06-16 yet unlinked).
- **Tooling Backlog item 17 update 2026-06-18**: the `tags` signal/noise flips on un-polished ranges (51.2% apply runs 61–77) — fix still worth shipping to keep a proactive sweep high-precision.
- **Tooling Backlog item 20 update 2026-06-18**: third/fourth confirmation of the particle/function no-op recurrence (7/8 and 3/4 clean); recommends excluding the closed particle set from the notes ranking.
- **Tooling Backlog item 21 update 2026-06-18**: third screener truncation, now hitting the §4 self-check (24/51); batch into ~25-ID sub-ranges.
- **Tooling Backlog new item 22**: particle structured-field furigana-completeness sweep (00484_も had unwrapped 数量/一 in `fixed_patterns`/`notes`).
- **Tooling Backlog new item 23**: candidate-pool pre-filter rejecting numeral+counter / single-suffix / proper-noun junk.
- **Open Issues → Candidate list quality**: rewritten with the quantified <10%-signal finding and the new-entries throughput impact.
- **Already filed (no new action)**: the `by_reading` homophone-false-match caveat is already documented in Cleanup P2 update 2026-06-17; the 28 lazy-default `general` observation folded into the P13 policy question above.
- **Activity H (metrics trend)**: refreshed `topics/quality-metrics.md` to 77 runs / 3,863 flags (tags apply 51.2% runs 61–77, queue −3,980 from peak).
All observations cleared.)_

_(2026-06-18 wiki (Routine v2, second run) harvest: processed the 4 observations from the 2026-06-18 routine accuracy-review / polish / new-entries runs. Filed:
- **Cleanup Backlog P11 update 2026-06-18 (second)**: tag contamination extends to 6925 (concrete-topic tags on unrelated words; 30 fixes applied 6840–6925) — confirmed dense band 6157–6925.
- **Cleanup Backlog P17 update 2026-06-18 (second)**: casual sentence-final particles/fillers/idioms (ぞ/なんて/やっぱ/よね/かしら/っていう/えーと) mis-tagged `formality: formal` — same gloss/notes-slang-marker-vs-`formal` detector slice as the slang-neologism sub-family.
- **Cleanup Backlog P21 update 2026-06-18 (second)**: the 06169–06176 〜的 cluster created Jan-2026 with zero inline links (examples + notes); working hypothesis that most 06000–07000 entries need full tier-1 inline linking as the frontier climbs the Jan-2026 band.
- **Tooling Backlog item 20 update 2026-06-18 (scorer-bug root cause)**: `score_note_quality.py` `has_bare_kanji` counts inline-link baseforms as un-furiganaed kanji (entries with links in notes score furigana=0) and the `required_sections` matcher misses valid headers — systematically depressing fully-polished entries' scores. The concrete bug behind the recurring notes-priority no-ops; strip ⟦…⟧ link baseforms before the bare-kanji check.
- **Tooling Backlog item 23 update 2026-06-18**: two more candidate-junk families (non-lexical compound fragments 倍率差/機成り/些道; decomposable/ad-hoc phrases 給水槽/排水処理/あらかじめ準備する/用につき) — reconfirms <10% signal and the new-entries throughput hit (13 curated rather than padded). The candidate-quality finding itself was already filed (item 23 + Open Issues, 2026-06-18); this is reinforcement only.
All 4 observations cleared.)_

_(2026-06-19 wiki (Routine v2) harvest: processed all observations from the 2026-06-18 accuracy-review session 007 and the three 2026-06-19 routine polish / systemic-fix runs. Filed:
- **Cleanup Backlog P21 update 2026-06-19**: 06177–06189 frontier blocks (onomatopoeia adverbs + tech loanwords + Jan-2026 batch) have zero inline-link coverage in examples *and* notes despite some recent `modified` timestamps — gap not self-healing through ordinary polishing; dedicated ~06150–07000 inline-link sweep recommendation restated (still gated on Tooling item 15 detector).
- **Tooling Backlog item 13 update 2026-06-19**: `review_runner.py --pass deep` aborted after the first entry (06930) with exit 0, no result files, no error — silent-drop failure escalated to an aborted pass; per-entry try/except hardening would fix it.
- **Tooling Backlog item 21 update 2026-06-19**: measured screening rate ~10 entries/min (gemini-2.5-flash) ⇒ size furigana-screening ranges to ~200 IDs/run.
- **Tooling Backlog new item 24**: non-hiragana-reading lint (deterministic catch for the screener's one true-positive class — Latin "uu" in 06952) + the screener's pair-extraction reading-truncation false-positive family (39/40 FP this range, ~2.5% precision; truncation is a `review_runner.py` extraction bug, not a model error).
- **Tooling Backlog new item 25**: cross-reference target-id resolution cluster — (a) `check_artifacts.py --issue missing-target-id` over-counts intentional target-less refs (homophone/contrast display labels for entry-less words; ~96 permanent re-flags); (b) build-time by-reading fallback resolves to the wrong homophone sense (04026 〜着→27655 着 counter), should require a surface match; (c) vestigial `id`-instead-of-`target_id` field (26 promoted this run, 4 stale pre-renumber) + entry-creation may still emit `id`.
- **[skill] recommendation (session log only)**: check the entry-creation skill/templates for emitting `id` instead of `target_id` on cross-references (knowledge-base session does not modify skills).
- **Tooling Backlog item 20 update 2026-06-19**: a fresh (post-regeneration) priority file still produced all-no-ops on line 57's basic/core content words (01092 億, 02350 良い, 00642 金曜日, 01003 隣, 01006 腕, 02006 ばかり, 02007 まま, 00765 優しい) — reinforces that the `score_note_quality.py` scorer-bug fix, not the ranking filters, is the binding fix.
- **Activity H (metrics trend)**: refreshed `topics/quality-metrics.md` (12 new metrics lines, 77→89 runs).
All observations cleared.)_

_(2026-06-20 wiki (Routine v2) harvest: processed all observations from the 2026-06-19 routine polish session 006 and the two 2026-06-20 routine polish / systemic-fix runs. Filed:
- **Cleanup Backlog P21 update 2026-06-20**: the zero-inline-link frontier band is now confirmed **unbroken from ~06150 (idiom cohort) through 06209** — 06190–06196 (nouns/proverbs) and 06204–06209 (general nouns 車掌/序文/付録/栄養素/炭水化物/太陽光) both had zero `⟦...⟧` links in examples *and* notes despite being schema-valid + furigana-complete; both runs hand-linked their frontier entries. The same session's priority/notes lane ran 6/6 no-op, so the notes ranking is pointing away from the real frontier deficit (inline-link coverage). Dedicated ~06150–07000 inline-link-sweep recommendation restated.
- **Cleanup Backlog P9 update 2026-06-20**: the 06xxx Jan-2026 creation batch carries cosmetic o-prefix-inside + pure-kana wrappers (detector dict-wide: o-go-prefix=228, pure-kana=888) plus a previously-unlisted **empty-reading `{X|}` degenerate** (kanji left, nothing after the pipe). The o-prefix/pure-kana sub-patterns are detector-caught, so a scoped 06000–06400 mechanical sweep (validated vs. word_id_lookup.json) is a ready systemic-fix candidate; flagged an open tooling question on whether `check_furigana_format.py` catches the empty-reading form (else extend Tooling item 8).
- **Tooling Backlog item 20 update 2026-06-20**: seventh consecutive priority-lane 6/6 no-op (00025/00533/00304/01092/00642/01003), now juxtaposed against the same run's zero-link 06190s/06204–06209 frontier — clearest single-session evidence the notes scorer is anti-correlated with real need; the `score_note_quality.py` scorer-bug fix remains binding.
- **Tooling Backlog item 25 update 2026-06-20**: missing-target-id trajectory quantified across four runs (190→136→96→82); queue hovering near 80, not converging, because the residual ~80 are intentional permanent homophone/contrast pointers — exactly what fix (1) (exclude type=homophone/contrast/labeled no-entry refs) addresses. Already filed; quantitative reinforcement only.
- **Already filed (no new action)**: the [entry] 気持ち duplicate (01385/02485) is already in [Entry Follow-ups](../planning/wiki/ideas/entry-followups.md) (§ "01385_kimochi & 02485_kimochi"); the [tooling] missing-target-id detector-exclusion request is already Tooling item 25(1) + Cleanup P2 update 2026-06-20.
- **Activity A (light sync)**: refreshed the General-tier count on `project/overview.md` (~26,370 of 29,155 total). Activity H (metrics trend) not due — only 8 new metrics lines since the page's 89-run refresh (threshold ≥10).
All observations cleared.)_

_(2026-06-21 wiki (Routine v2) harvest: processed all observations from the 2026-06-20 routine(polish) session and the 2026-06-21 accuracy-review / polish (routine_002) / new-entries (routine_003) runs. Filed:
- **Cleanup Backlog P20 update 2026-06-21**: the headline finding — a **new 7815–8037 creation cohort with 73% (163/223) out-of-taxonomy semantic tags**, a denser and different cohort from the 01490–06925 P11 batch. The 2026-06-21 accuracy-review migrated the 43 error-severity flags; **120 entries still carry invalid tags**. Enumerated the large 1:1-mappable drift families (free-form domain words `career`/`lifestyle`/`place`/`document`/`accommodation`/`commerce`/`accounting`/`employment`/`logistics`/`personnel`; `daily_life`/`daily life`→`daily-life`; `Japanese_cuisine`→drop; `body`→`body-part`, `sleep`/`injury`→`health`). Recommended a systemic-fix sweep over 7815–8037 + the adjacent ~7000–8500 cohort after expanding the migration map.
- **Tooling Backlog item 6 update 2026-06-21**: the migration-map expansion that makes the P20 7000–8500 sweep deterministic (the scalable instrument vs. the per-pass accuracy reviewer).
- **Tooling Backlog new item 26**: embed the valid `formality` enum (formal/neutral/informal/vulgar) + `politeness` enum in `review_accuracy.py`'s tags/register prompt — the formality analogue of the resolved item-14 `VALID_SEMANTIC` gap (reviewer suggested out-of-enum "colloquial" for a formality flag = guaranteed false positive).
- **Cleanup Backlog P21 update 2026-06-21**: the zero-inline-link frontier band now confirmed unbroken ~06150→06214+ (06210–06213 compound verbs + the 06214+ proverb/yojijukugo block, again with recent-but-unlinked `modified` timestamps); 06200–06250 backfill-as-a-block recommendation.
- **Tooling Backlog item 20 update 2026-06-21**: eighth consecutive 6/6 priority-lane no-op (two runs), again juxtaposed against genuine zero-link frontier gaps; scorer-bug fix remains binding, plus a recency/coverage guard in `prioritize_polishing.py`.
- **Tooling Backlog item 23 update 2026-06-21**: two consecutive new-entries runs (2026-06-20, 2026-06-21) skipped the oldest-first junk fallback lane entirely and stayed under target; recommends running `clean_up_candidates_list.md` to purge the pre-March junk (curator side) alongside the pre-filter.
- **Entry Follow-ups**: 00304_nandemo sense 3 ("by all means / at any cost") rests on 何でも alone carrying an adverbial meaning that is dubious standard usage (natural forms are 何が何でも / どうしても) — flagged for a sense-level editorial decision.
- **Reinforcement only (no new action)**: the 2026-06-21 furigana-screener ~0% precision over the structured 7815–8037 range is the documented known-noise family (calibration_report + Tooling item 24); the candidate-backlog-junk `[pattern]` is the already-filed <10%-signal finding (item 23 + Open Issues).
- **Activity H (metrics trend)**: seventh refresh of `topics/quality-metrics.md` (14 new metrics lines, 89→103 runs / 4,431 adjudicated flags) — range-state thesis held a fourth period (`tags` 49.4% on the densest contamination yet), review queue reached its structural floor (range-bound 15,298–15,436). No metric judged to be moving the wrong way, so no new `[pattern]` observation logged.
All observations cleared.)_
