# Quality Metrics

**Generated**: 2026-09-02 by `pipeline/metrics_report.py` from `pipeline/metrics-history.jsonl` (561 runs since 2026-06-10) and `reviews/decisions.jsonl` (7948 adjudication lines). Do not edit by hand; rerun the script. The narrative history that used to live on this page is preserved in git (`git log -- planning/wiki/topics/quality-metrics.md`).

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
| 2026-W36 | 5 | pol1 acc1 new1 can1 wik1 | 55 | 15 / 112 | 7065 | 10777 | 195 | 30584 | 0.29 |

Latest detector queue depths (2026-08-27): furigana_format 765, artifacts 44, tag_drift 5582

## Reviewer-flag precision, last 30 days

| src/dim | apply | reject | flag | precision |
|---|---|---|---|---|
| accuracy/gloss | 62 | 137 | 6 | 30% |
| accuracy/tags | 2697 | 1480 | 75 | 63% |
| accuracy/translation | 45 | 71 | 0 | 39% |
| furigana/furigana | 9 | 548 | 1 | 2% |
| self-check/furigana | 0 | 7 | 0 | 0% |
| self-check/gloss | 33 | 43 | 4 | 41% |
| self-check/tags | 133 | 197 | 92 | 32% |
| self-check/translation | 29 | 31 | 0 | 48% |

| dim:family | apply | reject | flag | precision |
|---|---|---|---|---|
| furigana:(unlabelled) | 9 | 555 | 1 | 2% |
| gloss:(unlabelled) | 95 | 180 | 10 | 33% |
| tags:(unlabelled) | 2830 | 1677 | 167 | 61% |
| translation:(unlabelled) | 74 | 102 | 0 | 42% |

## Reviewer-flag precision, all time

| src/dim | apply | reject | flag | precision |
|---|---|---|---|---|
| accuracy-review/furigana | 1 | 10 | 0 | 9% |
| accuracy-review/gloss | 1 | 19 | 2 | 5% |
| accuracy-review/tags | 32 | 260 | 0 | 11% |
| accuracy-review/translation | 4 | 24 | 0 | 14% |
| accuracy/gloss | 177 | 496 | 16 | 26% |
| accuracy/gloss/translation | 0 | 0 | 1 | 0% |
| accuracy/tags | 7612 | 4223 | 1113 | 59% |
| accuracy/translation | 136 | 335 | 7 | 28% |
| furigana-screening/furigana | 0 | 1 | 0 | 0% |
| furigana/furigana | 52 | 2322 | 4 | 2% |
| furigana/tags | 1 | 0 | 0 | 100% |
| screening/furigana | 0 | 515 | 0 | 0% |
| self-check/furigana | 3 | 65 | 0 | 4% |
| self-check/gloss | 71 | 105 | 6 | 39% |
| self-check/tags | 382 | 460 | 95 | 41% |
| self-check/translation | 48 | 110 | 0 | 30% |

