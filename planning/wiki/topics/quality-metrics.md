# Quality Metrics

**Generated**: 2026-09-28 by `pipeline/metrics_report.py` from `pipeline/metrics-history.jsonl` (702 runs since 2026-06-10) and `reviews/decisions.jsonl` (11265 adjudication lines). Do not edit by hand; rerun the script. The narrative history that used to live on this page is preserved in git (`git log -- planning/wiki/topics/quality-metrics.md`).

## How to read this page

- **Frontier** is the next entry ID of the sequential polish lane. **Review queue** is `reviews/queue.txt`: entries changed since their last external review (each session's `make index` appends the entries it changed, the accuracy sweep drains). **Precision** is the share of reviewer flags that were applied; reject and flag (to curator) are the rest.
- Per-family precision requires the `family` field that `build/review_accuracy.py` (prompt version 4, 2026-09-02) stamps on every issue; older decisions show as `(unlabelled)`.

## Weekly summary (last 16 weeks)

| Week | Runs | Modes | Entries changed | Flags applied / rejected | Frontier | Review queue | Candidates | Entries | OpenRouter $ |
|---|---|---|---|---|---|---|---|---|---|
| 2026-W25 | 56 | pol19 acc13 sys6 new10 wik8 | 1073 | 575 / 867 | 6231 | 15255 | 1287 | 29180 | 1.86 |
| 2026-W26 | 53 | pol17 acc13 sys5 new10 wik8 | 884 | 604 / 410 | 6320 | 14620 | 1215 | 29342 | 2.49 |
| 2026-W27 | 53 | pol18 acc13 sys5 new10 wik7 | 482 | 153 / 368 | 6418 | 14242 | 1172 | 29481 | 1.48 |
| 2026-W28 | 40 | pol13 acc9 sys4 new8 wik6 | 449 | 210 / 324 | 6463 | 13758 | 1147 | 29594 | 1.68 |
| 2026-W29 | 55 | pol19 acc13 sys5 new10 wik8 | 752 | 378 / 570 | 6553 | 13024 | 1102 | 29762 | 1.76 |
| 2026-W30 | 55 | pol18 acc14 sys5 new10 wik8 | 1286 | 859 / 771 | 6650 | 12371 | 1042 | 29935 | 3.10 |
| 2026-W31 | 55 | pol19 acc13 sys5 new10 wik8 | 3015 | 2084 / 760 | 6755 | 12948 | 1009 | 30128 | 3.36 |
| 2026-W32 | 56 | pol18 acc13 sys7 new10 wik8 | 3138 | 1405 / 658 | 6850 | 9834 | 989 | 30316 | 3.10 |
| 2026-W33 | 56 | pol19 acc14 sys5 new9 can1 wik8 | 2515 | 1475 / 1187 | 6967 | 10614 | 164 | 30484 | 2.93 |
| 2026-W34 | 11 | pol4 acc2 sys1 new2 wik2 | 270 | 18 / 117 | 7005 | 10801 | 151 | 30524 | 0.20 |
| 2026-W35 | 14 | pol5 acc4 sys2 new2 wik1 | 529 | 96 / 418 | 7059 | 10810 | 152 | 30564 | 1.10 |
| 2026-W36 | 16 | pol5 acc4 sys3 new2 can1 wik1 | 4129 | 254 / 293 | 7116 | 12190 | 199 | 30604 | 2.29 |
| 2026-W37 | 20 | pol6 acc6 sys6 new2 | 511 | 499 / 192 | 7340 | 10321 | 211 | 30683 | 3.52 |
| 2026-W38 | 42 | pol15 acc13 sys10 new4 | 1795 | 977 / 839 | 8076 | 4106 | 178 | 30784 | 6.73 |
| 2026-W39 | 65 | pol19 acc19 sys16 new6 wik1 | 2690 | 581 / 749 | 8652 | 3014 | 113 | 30883 | 25.13 |
| 2026-W40 | 3 | acc1 new1 | 28 | 9 / 18 | 8652 | 3052 | 91 | 30905 | 5.73 |

Latest detector queue depths (2026-09-25): furigana_format 240, artifacts 45, tag_drift 4479

## Reviewer-flag precision, last 30 days

| src/dim | apply | reject | flag | precision |
|---|---|---|---|---|
| None/gloss | 3 | 9 | 0 | 25% |
| None/notes | 3 | 9 | 0 | 25% |
| None/tags | 2 | 8 | 0 | 20% |
| None/translation | 0 | 7 | 0 | 0% |
| accuracy/gloss | 201 | 164 | 4 | 54% |
| accuracy/notes | 346 | 821 | 16 | 29% |
| accuracy/tags | 1258 | 471 | 2 | 73% |
| accuracy/translation | 88 | 104 | 3 | 45% |
| furigana/furigana | 0 | 2 | 0 | 0% |
| self-check/gloss | 24 | 39 | 5 | 35% |
| self-check/notes | 48 | 176 | 2 | 21% |
| self-check/tags | 77 | 67 | 1 | 53% |
| self-check/translation | 19 | 32 | 5 | 34% |

| dim:family | apply | reject | flag | precision |
|---|---|---|---|---|
| furigana:(unlabelled) | 0 | 2 | 0 | 0% |
| gloss:(unlabelled) | 5 | 12 | 0 | 29% |
| gloss:gloss-meaning | 220 | 200 | 9 | 51% |
| gloss:notes-fact | 3 | 0 | 0 | 100% |
| notes:notes-fact | 396 | 1006 | 18 | 28% |
| notes:register | 1 | 0 | 0 | 100% |
| tags:(unlabelled) | 31 | 169 | 0 | 16% |
| tags:notes-fact | 17 | 1 | 0 | 94% |
| tags:offvocab | 867 | 0 | 2 | 100% |
| tags:register | 192 | 312 | 1 | 38% |
| tags:wrong-category | 230 | 64 | 0 | 78% |
| translation:(unlabelled) | 7 | 8 | 0 | 47% |
| translation:notes-fact | 1 | 0 | 0 | 100% |
| translation:translation-meaning | 99 | 135 | 8 | 41% |

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
| accuracy/gloss | 376 | 650 | 20 | 36% |
| accuracy/gloss/translation | 0 | 0 | 1 | 0% |
| accuracy/notes | 346 | 821 | 16 | 29% |
| accuracy/tags | 8861 | 4544 | 1115 | 61% |
| accuracy/translation | 222 | 434 | 10 | 33% |
| furigana-screening/furigana | 0 | 1 | 0 | 0% |
| furigana/furigana | 52 | 2322 | 4 | 2% |
| furigana/tags | 1 | 0 | 0 | 100% |
| screening/furigana | 0 | 515 | 0 | 0% |
| self-check/furigana | 3 | 65 | 0 | 4% |
| self-check/gloss | 93 | 142 | 11 | 38% |
| self-check/notes | 48 | 176 | 2 | 21% |
| self-check/tags | 448 | 509 | 96 | 43% |
| self-check/translation | 63 | 140 | 5 | 30% |

