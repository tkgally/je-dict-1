# Comprehensive Polish Session — 2026-05-24 (001)

**Date:** 2026-05-24  
**Branch:** claude/elegant-dirac-nmhit  
**Entry range processed:** 03231–03252  
**Entries processed:** 22  
**Next entry:** 03253

## Summary

Added full inline word links (⟦...⟧) to all Japanese text in examples and notes for entries 03231–03252. Also fixed several tier-1 issues found along the way.

## Entries processed

| ID | Headword | Reading | Notes |
|----|----------|---------|-------|
| 03231 | 正午 | しょうご | Links added; removed invalid antonym cross-ref (正夜 has no entry) |
| 03232 | 少々 | しょうしょう | Links added |
| 03233 | 少女 | しょうじょ | Links added; added candidate 女児 |
| 03234 | 症状 | しょうじょう | Links added; fixed semantic tag "body-part" → "general" |
| 03235 | 衝突 | しょうとつ | Links added; added missing headword to 摩擦 cross-ref; added new contrast cross-ref to 対立 |
| 03236 | 商人 | しょうにん | Links added; added candidate 商売人 |
| 03237 | 承認 | しょうにん | Links added; fixed semantic tag "electronics" → "general" |
| 03238 | 少年 | しょうねん | Links added; added candidates 男児, 新薬 |
| 03239 | 商売 | しょうばい | Links added; added candidate 水物 |
| 03240 | 消費 | しょうひ | Links added |
| 03241 | 消防 | しょうぼう | Links added; used compound entries (消防士, 消防署, 消防車, 消化器) |
| 03242 | 証明 | しょうめい | Links added; linked 身分証明書 as compound |
| 03243 | 照明 | しょうめい | Links added; fixed semantic tag "geography" → "general"; fixed spurious furigana つける |
| 03244 | 省略 | しょうりゃく | Links added |
| 03245 | 職業 | しょくぎょう | Links added; used 保障(03719) not 保証(03718) |
| 03246 | 食卓 | しょくたく | Links added |
| 03247 | 食品 | しょくひん | Links added; linked 冷凍食品, 加工食品, 健康食品, 食品添加物 as compounds |
| 03248 | 植物 | しょくぶつ | Links added; linked 植物園, 観葉植物 as compounds |
| 03249 | 食欲 | しょくよく | Links added; fixed semantic tag "electronics" → removed (kept "emotion") |
| 03250 | 食料 | しょくりょう | Links added; linked 食料品, 自給率 as compounds |
| 03251 | 処理 | しょり | Links added; fixed semantic tag "body-part" → "general"; linked 粗大ゴミ compound |
| 03252 | 知らせ | しらせ | Links added |

## Candidates added

- C21062 商売人 (しょうばいにん) — merchant, trader; seen in 03236
- C21063 女児 (じょじ) — girl (medical/formal); seen in 03233
- C21064 男児 (だんじ) — boy (formal/literary); seen in 03238
- C21065 新薬 (しんやく) — new drug, new medicine; seen in 03238
- C21066 水物 (みずもの) — uncertain thing, risky venture; seen in 03239

## Issues found

- Note: PR #2449 on another branch covers 03211–03230; started from 03231 to avoid conflicts.
- Several entries had wrong semantic tags ("electronics", "body-part", "geography") — all corrected to "general".
- 03231: removed antonym cross-ref for 正夜 (no entry in dictionary).
- 03243: spurious furigana `{つける|つける}` on plain hiragana word — removed.
