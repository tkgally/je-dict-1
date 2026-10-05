# Quality Metrics

**Generated**: 2026-10-05 by `pipeline/metrics_report.py` from `pipeline/metrics-history.jsonl` (926 runs since 2026-06-10) and `reviews/decisions.jsonl` (12474 adjudication lines). Do not edit by hand; rerun the script. The narrative history that used to live on this page is preserved in git (`git log -- planning/wiki/topics/quality-metrics.md`).

## How to read this page

- **Frontier** is the next entry ID of the sequential polish lane. **Review queue** is `reviews/queue.txt`: entries changed since their last external review (each session's `make index` appends the entries it changed, the accuracy sweep drains). **Precision** is the share of reviewer flags that were applied; reject and flag (to curator) are the rest.
- Per-family precision requires the `family` field that `build/review_accuracy.py` (prompt version 4, 2026-09-02) stamps on every issue; older decisions show as `(unlabelled)`.

## Weekly summary (last 16 weeks)

| Week | Runs | Modes | Entries changed | Flags applied / rejected | Frontier | Review queue | Candidates | Entries | OpenRouter $ |
|---|---|---|---|---|---|---|---|---|---|
| 2026-W26 | 53 | pol17 acc13 sys5 new10 wik8 | 884 | 604 / 410 | 6320 | 14620 | 1215 | 29342 | 2.49 |
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
| 2026-W41 | 9 | pol2 acc2 sys2 new1 | 308 | 18 / 70 | 9894 | 5623 | 53 | 31382 | 11.92 |

Latest detector queue depths (2026-10-02): furigana_format 233, artifacts 15, tag_drift 4235

## Reviewer-flag precision, last 30 days

| src/dim | apply | reject | flag | precision |
|---|---|---|---|---|
| None/gloss | 3 | 9 | 0 | 25% |
| None/notes | 3 | 9 | 0 | 25% |
| None/tags | 2 | 8 | 0 | 20% |
| None/translation | 0 | 7 | 0 | 0% |
| accuracy/gloss | 225 | 264 | 5 | 46% |
| accuracy/notes | 431 | 1262 | 19 | 25% |
| accuracy/tags | 1190 | 429 | 2 | 73% |
| accuracy/translation | 115 | 158 | 3 | 42% |
| conjugation/conjugation | 0 | 0 | 1 | 0% |
| self-check/gloss | 26 | 55 | 2 | 31% |
| self-check/notes | 60 | 214 | 1 | 22% |
| self-check/tags | 60 | 65 | 1 | 48% |
| self-check/translation | 15 | 22 | 0 | 41% |

| dim:family | apply | reject | flag | precision |
|---|---|---|---|---|
| conjugation:example | 0 | 0 | 1 | 0% |
| gloss:(unlabelled) | 2 | 1 | 0 | 67% |
| gloss:gloss-meaning | 249 | 327 | 7 | 43% |
| gloss:notes-fact | 3 | 0 | 0 | 100% |
| notes:(unlabelled) | 2 | 4 | 0 | 33% |
| notes:notes-fact | 491 | 1481 | 20 | 25% |
| notes:register | 1 | 0 | 0 | 100% |
| tags:(unlabelled) | 11 | 2 | 0 | 85% |
| tags:notes-fact | 12 | 1 | 0 | 92% |
| tags:offvocab | 748 | 0 | 2 | 100% |
| tags:register | 215 | 400 | 1 | 35% |
| tags:wrong-category | 266 | 99 | 0 | 73% |
| translation:(unlabelled) | 1 | 1 | 0 | 50% |
| translation:notes-fact | 1 | 0 | 0 | 100% |
| translation:translation-meaning | 128 | 186 | 3 | 40% |

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
| accuracy/gloss | 409 | 761 | 21 | 34% |
| accuracy/gloss/translation | 0 | 0 | 1 | 0% |
| accuracy/notes | 449 | 1289 | 19 | 26% |
| accuracy/tags | 8932 | 4664 | 1115 | 61% |
| accuracy/translation | 251 | 494 | 10 | 33% |
| conjugation/conjugation | 0 | 0 | 1 | 0% |
| furigana-screening/furigana | 0 | 1 | 0 | 0% |
| furigana/furigana | 52 | 2281 | 4 | 2% |
| furigana/tags | 1 | 0 | 0 | 100% |
| screening/furigana | 0 | 515 | 0 | 0% |
| self-check/furigana | 3 | 65 | 0 | 4% |
| self-check/gloss | 102 | 177 | 11 | 35% |
| self-check/notes | 73 | 282 | 2 | 20% |
| self-check/tags | 464 | 536 | 96 | 42% |
| self-check/translation | 71 | 151 | 5 | 31% |

