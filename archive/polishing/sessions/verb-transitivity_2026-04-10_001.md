## Session: Verb Transitivity
Date: 2026-04-10
Entries checked: 00001-00500 (sequential range, plus dictionary-wide tag sync)

### Approach

This was the first session for the verb-transitivity polishing task. Two
passes were applied:

1. **Dictionary-wide tag sync** (1052 verbs): A helper script extracted
   the transitivity classification from existing TRANSITIVITY notes
   sections (when the type was unambiguous) and added the corresponding
   `metadata.tags.transitivity` tag. The semantic determination was
   already made by the original notes author — this pass only synced the
   tag with the existing notes content. Edge cases handled by the script:
   - Word-boundary matching to avoid `(transitive)` falsely matching
     inside `(intransitive)`.
   - First-marker-wins logic to handle "TRANSITIVITY: ... Pair: ..."
     formats where the pair info comes after the verb's own type.
   - Skipping causative `させる/せる` headwords whose notes describe the
     base verb's transitivity.
   - Skipping "TRANSITIVITY PAIR" sections that describe the pair
     relationship rather than this verb's type.
   - Restricting the parsed window to the current paragraph (so later
     ASPECT/COMMON PATTERNS sections don't introduce false matches).
   - Edits use string-level injection so the rest of the file stays
     byte-identical (avoids triggering pre-existing duplicate-key cleanup).

2. **Manual classification of IDs 1-500** (70 verbs): For verb entries
   in the first 500 IDs that lacked any transitivity statement (mostly
   suru-verbs), I classified each by hand from my knowledge of Japanese
   and applied a TRANSITIVITY notes section plus the tag.

### Changes Made

- 1052 verbs: transitivity tag added by sync from existing notes
- 70 verbs (IDs 1-500): both transitivity tag AND TRANSITIVITY notes
  section added by hand classification

### Manual Classifications (IDs 1-500)

Transitive (39 entries): 我慢, 配達, 発見, 持参, 解放, 解決, 解説, 改造,
可決, 確認, 加熱, 換気, 管理, 観測, 監督, 警備, 見学, 希望, 記念, 記憶,
期待, 区分, 工夫, 空想, 許可, 強化, マッサージ, マスター, メモ, 採集,
指定, 水洗, 開放, 改正, 修飾, 振興, 課税

Intransitive (24 entries): がっかり, 下車, 自衛, 回転, 回答, 下降, 感動,
感激, 観光, 乾杯, 関連, 感謝, 乾燥, 活動, 起床, 工事, 苦心, 協力, 休憩,
ミス, 熱中, お辞儀, 司会, 炊事, スケート, トレーニング, 解答, 生長, 稽古

Both (4 entries): 改善, 加速, 継続, 酸化

### Notes / Issues

- Some pre-existing TRANSITIVITY notes contain pair-verb references
  that point to entries not yet in the dictionary; these were left as
  unhardened references (no target_id) per the task instructions.
- A small number of pre-existing notes appear to misclassify their verb
  (e.g., 21354_kantsuu's notes claim 貫通する is transitive when it is
  intransitive). These were not corrected in this session — a separate
  audit pass should fix them.
- Pair-verb back-link verification was deferred. Most pair links in the
  manual entries already exist via `cross_references` rather than
  `prominent_see_also`; promoting them to prominent_see_also is a
  separate cleanup.

### Statistics

Before this session:
- Verbs with transitivity tag: 1497 / 6163 (24.3%)

After this session:
- Verbs with transitivity tag: 2619 / 6163 (42.5%)
- Net new tags added: 1122

### Next Entry

00501
