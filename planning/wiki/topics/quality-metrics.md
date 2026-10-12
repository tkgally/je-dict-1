# Quality Metrics

**Generated**: 2026-10-12 by `pipeline/metrics_report.py` from `pipeline/metrics-history.jsonl` (1136 runs since 2026-06-10) and `reviews/decisions.jsonl` (13246 adjudication lines). Do not edit by hand; rerun the script. The narrative history that used to live on this page is preserved in git (`git log -- planning/wiki/topics/quality-metrics.md`).

## How to read this page

- **Frontier** is the next entry ID of the sequential polish lane. **Review queue** is `reviews/queue.txt`: entries changed since their last external review (each session's `make index` appends the entries it changed, the accuracy sweep drains). **Precision** is the share of reviewer flags that were applied; reject and flag (to curator) are the rest.
- Per-family precision requires the `family` field that `build/review_accuracy.py` (prompt version 4, 2026-09-02) stamps on every issue; older decisions show as `(unlabelled)`.

## Weekly summary (last 16 weeks)

| Week | Runs | Modes | Entries changed | Flags applied / rejected | Frontier | Review queue | Candidates | Entries | OpenRouter $ |
|---|---|---|---|---|---|---|---|---|---|
| 2026-W27 | 53 | pol18 acc13 sys5 new10 wik7 | 482 | 153 / 368 | 6418 | 14242 | 1172 | 29481 | 1.48 |
| 2026-W28 | 40 | pol13 acc9 sys4 new8 wik6 | 449 | 210 / 324 | 6463 | 13758 | 1147 | 29594 | 1.68 |
| 2026-W29 | 55 | pol19 acc13 sys5 new10 wik8 | 752 | 378 / 570 | 6553 | 13024 | 1102 | 29762 | 1.76 |
| 2026-W30 | 55 | pol18 acc14 sys5 new10 wik8 | 1286 | 859 / 771 | 6650 | 12371 | 1042 | 29935 | 3.10 |
| 2026-W31 | 55 | pol19 acc13 sys5 new10 wik8 | 3015 | 2084 / 760 | 6755 | 12948 | 1009 | 30128 | 3.36 |
| 2026-W32 | 56 | pol18 acc13 sys7 new10 wik8 | 3138 | 1405 / 658 | 6850 | 9834 | 989 | 30316 | 3.10 |
| 2026-W33 | 56 | pol19 acc14 sys5 new9 can1 wik8 | 2515 | 1475 / 1187 | 6967 | 10614 | 164 | 30484 | 2.93 |
| 2026-W34 | 11 | pol4 acc2 sys1 new2 wik2 | 270 | 18 / 117 | 7005 | 10801 | 151 | 30524 | 0.20 |
| 2026-W35 | 14 | pol5 acc4 sys2 new2 wik1 | 529 | 96 / 384 | 7059 | 10810 | 152 | 30564 | 1.10 |
| 2026-W36 | 16 | pol5 acc4 sys3 new2 can1 wik1 | 4129 | 254 / 293 | 7116 | 12190 | 199 | 30604 | 2.29 |
| 2026-W37 | 20 | pol6 acc6 sys6 new2 | 511 | 499 / 192 | 7340 | 10321 | 211 | 30683 | 3.52 |
| 2026-W38 | 42 | pol15 acc13 sys10 new4 | 1795 | 977 / 839 | 8076 | 4106 | 178 | 30784 | 6.73 |
| 2026-W39 | 65 | pol19 acc19 sys16 new6 wik1 | 2690 | 581 / 749 | 8652 | 3014 | 113 | 30883 | 25.13 |
| 2026-W40 | 218 | pol65 acc37 sys56 new32 can2 wik1 | 8721 | 349 / 1097 | 9847 | 6063 | 58 | 31370 | 104.98 |
| 2026-W41 | 206 | pol62 acc27 sys56 new25 can7 wik1 | 7210 | 213 / 562 | 10899 | 7607 | 68 | 31706 | 105.02 |
| 2026-W42 | 13 | pol3 acc3 sys2 new1 can1 | 158 | 50 / 65 | 10943 | 7190 | 70 | 31716 | 14.98 |

Latest detector queue depths (2026-10-09): furigana_format 222, artifacts 15, tag_drift 3908

## Reviewer-flag precision, last 30 days

| src/dim | apply | reject | flag | precision |
|---|---|---|---|---|
| None/gloss | 3 | 9 | 0 | 25% |
| None/notes | 3 | 9 | 0 | 25% |
| None/tags | 2 | 8 | 0 | 20% |
| None/translation | 0 | 7 | 0 | 0% |
| accuracy/gloss | 248 | 342 | 5 | 42% |
| accuracy/notes | 489 | 1397 | 17 | 26% |
| accuracy/tags | 864 | 493 | 2 | 64% |
| accuracy/translation | 132 | 188 | 3 | 41% |
| conjugation/conjugation | 0 | 0 | 1 | 0% |
| self-check/gloss | 32 | 79 | 1 | 29% |
| self-check/notes | 94 | 290 | 1 | 24% |
| self-check/tags | 65 | 85 | 1 | 43% |
| self-check/translation | 24 | 44 | 1 | 35% |

| dim:family | apply | reject | flag | precision |
|---|---|---|---|---|
| conjugation:example | 0 | 0 | 1 | 0% |
| gloss:(unlabelled) | 2 | 1 | 0 | 67% |
| gloss:gloss-meaning | 279 | 429 | 6 | 39% |
| gloss:notes-fact | 2 | 0 | 0 | 100% |
| notes:(unlabelled) | 2 | 4 | 0 | 33% |
| notes:crossref-harvest | 1 | 0 | 0 | 100% |
| notes:notes-fact | 582 | 1692 | 18 | 25% |
| notes:register | 1 | 0 | 0 | 100% |
| tags:(unlabelled) | 11 | 2 | 0 | 85% |
| tags:notes-fact | 8 | 1 | 0 | 89% |
| tags:offvocab | 434 | 0 | 2 | 100% |
| tags:register | 212 | 448 | 1 | 32% |
| tags:wrong-category | 266 | 135 | 0 | 66% |
| translation:(unlabelled) | 1 | 1 | 0 | 50% |
| translation:notes-fact | 2 | 0 | 0 | 100% |
| translation:translation-meaning | 153 | 238 | 4 | 39% |

## Reviewer-flag precision, all time

| src/dim | apply | reject | flag | precision |
|---|---|---|---|---|
| None/gloss | 3 | 9 | 0 | 25% |
| None/notes | 3 | 9 | 0 | 25% |
| None/tags | 2 | 8 | 0 | 20% |
| None/translation | 0 | 7 | 0 | 0% |
| accuracy-review/furigana | 1 | 10 | 0 | 9% |
| accuracy-review/gloss | 1 | 19 | 2 | 5% |
| accuracy-review/tags | 32 | 260 | 0 | 11% |
| accuracy-review/translation | 4 | 24 | 0 | 14% |
| accuracy/gloss | 448 | 842 | 21 | 34% |
| accuracy/gloss/translation | 0 | 0 | 1 | 0% |
| accuracy/notes | 527 | 1477 | 19 | 26% |
| accuracy/tags | 8964 | 4756 | 1115 | 60% |
| accuracy/translation | 279 | 532 | 10 | 34% |
| conjugation/conjugation | 0 | 0 | 1 | 0% |
| furigana-screening/furigana | 0 | 1 | 0 | 0% |
| furigana/furigana | 52 | 2281 | 4 | 2% |
| furigana/tags | 1 | 0 | 0 | 100% |
| screening/furigana | 0 | 515 | 0 | 0% |
| self-check/furigana | 3 | 65 | 0 | 4% |
| self-check/gloss | 111 | 204 | 11 | 34% |
| self-check/notes | 109 | 367 | 2 | 23% |
| self-check/tags | 472 | 556 | 96 | 42% |
| self-check/translation | 80 | 174 | 6 | 31% |

