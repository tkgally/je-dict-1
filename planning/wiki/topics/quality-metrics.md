# Quality Metrics

**Generated**: 2026-09-23 by `pipeline/metrics_report.py` from `pipeline/metrics-history.jsonl` (646 runs since 2026-06-10) and `reviews/decisions.jsonl` (10639 adjudication lines). Do not edit by hand; rerun the script. The narrative history that used to live on this page is preserved in git (`git log -- planning/wiki/topics/quality-metrics.md`).

## How to read this page

- **Frontier** is the next entry ID of the sequential polish lane. **Review queue** is `reviews/queue.txt`: entries changed since their last external review (CI appends, the accuracy sweep drains). **Precision** is the share of reviewer flags that were applied; reject and flag (to curator) are the rest.
- Per-family precision requires the `family` field that `build/review_accuracy.py` (prompt version 4, 2026-09-02) stamps on every issue; older decisions show as `(unlabelled)`.

## Weekly summary (last 16 weeks)

| Week | Runs | Modes | Entries changed | Flags applied / rejected | Frontier | Review queue | Candidates | Entries | OpenRouter $ |
|---|---|---|---|---|---|---|---|---|---|
| 2026-W24 | 52 | pol17 acc11 sys6 new10 wik8 | 1228 | 648 / 2356 | 6137 | 15985 | 1321 | 29048 | 3.95 |
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
| 2026-W39 | 12 | pol4 acc4 sys3 new1 | 728 | 388 / 207 | 8142 | 3285 | 164 | 30804 | 2.07 |

Latest detector queue depths (2026-09-18): furigana_format 239, artifacts 45, tag_drift 4937

## Reviewer-flag precision, last 30 days

| src/dim | apply | reject | flag | precision |
|---|---|---|---|---|
| None/gloss | 3 | 9 | 0 | 25% |
| None/notes | 3 | 9 | 0 | 25% |
| None/tags | 2 | 8 | 0 | 20% |
| None/translation | 0 | 7 | 0 | 0% |
| accuracy/gloss | 189 | 129 | 3 | 59% |
| accuracy/notes | 289 | 618 | 14 | 31% |
| accuracy/tags | 1272 | 559 | 2 | 69% |
| accuracy/translation | 79 | 85 | 3 | 47% |
| furigana/furigana | 0 | 122 | 0 | 0% |
| self-check/furigana | 0 | 3 | 0 | 0% |
| self-check/gloss | 25 | 34 | 4 | 40% |
| self-check/notes | 33 | 119 | 1 | 22% |
| self-check/tags | 74 | 49 | 1 | 60% |
| self-check/translation | 16 | 27 | 5 | 33% |

| dim:family | apply | reject | flag | precision |
|---|---|---|---|---|
| furigana:(unlabelled) | 0 | 125 | 0 | 0% |
| gloss:(unlabelled) | 17 | 24 | 0 | 41% |
| gloss:gloss-meaning | 197 | 148 | 7 | 56% |
| gloss:notes-fact | 3 | 0 | 0 | 100% |
| notes:notes-fact | 324 | 746 | 15 | 30% |
| notes:register | 1 | 0 | 0 | 100% |
| tags:(unlabelled) | 95 | 379 | 0 | 20% |
| tags:notes-fact | 17 | 0 | 0 | 100% |
| tags:offvocab | 848 | 0 | 2 | 100% |
| tags:register | 180 | 205 | 1 | 47% |
| tags:wrong-category | 208 | 32 | 0 | 87% |
| translation:(unlabelled) | 12 | 11 | 0 | 52% |
| translation:translation-meaning | 83 | 108 | 8 | 42% |

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
| accuracy/gloss | 359 | 605 | 19 | 37% |
| accuracy/gloss/translation | 0 | 0 | 1 | 0% |
| accuracy/notes | 289 | 618 | 14 | 31% |
| accuracy/tags | 8812 | 4424 | 1115 | 61% |
| accuracy/translation | 209 | 412 | 10 | 33% |
| furigana-screening/furigana | 0 | 1 | 0 | 0% |
| furigana/furigana | 52 | 2322 | 4 | 2% |
| furigana/tags | 1 | 0 | 0 | 100% |
| screening/furigana | 0 | 515 | 0 | 0% |
| self-check/furigana | 3 | 65 | 0 | 4% |
| self-check/gloss | 87 | 135 | 10 | 38% |
| self-check/notes | 33 | 119 | 1 | 22% |
| self-check/tags | 444 | 489 | 96 | 43% |
| self-check/translation | 59 | 135 | 5 | 30% |

