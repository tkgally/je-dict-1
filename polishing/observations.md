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

_(All observations through 2026-05-29 session 009 have been harvested by the wiki maintenance session of 2026-05-30.)_

---

## 2026-05-30 session 001 (04205–04222)

[pattern] Several entries in this range had incorrect semantic domain tags: "electronics" used for 申請 (administration context), "body-part" for 診断 (medical context), "education" for 実績 (general business). Worth checking nearby entries for similar mismatches.

[pattern] Compound verbs 取り出す/取り入れる/取り除く (04220-04222) follow a consistent note structure: "formed from 取る + X". These patterns make inline linking straightforward but need careful handling of self-reference (entire compound = headword, including conjugated forms).

[wiki] 挙げる (27889) is distinct from 上げる (02443) — separate entries with different meanings (to cite/name vs. to raise/give). Worth documenting in wiki to avoid future confusion during linking.

## 2026-05-30 session 002 (04223–04243)

[pattern] Multiple entries in range 04223–04243 had overly narrow semantic tags: "electronics" (切り替える, should be "action"), "communication" (振り向く, 見送る, should be "action"), "food"/"tool" (振る舞う). The "electronics" tag seems applied when an entry has digital/device examples but the verb itself is neutral.

[entry] 04239 切り替える: furigana error {会社|がいしゃ} in ex5 — should be {会社|かいしゃ}. Corrected.

[entry] 04238 切り取る: スクリーンショット appears in ex9 as noentry — added to candidates.

[pattern] Range 04282–04306: several entries had wrong semantic tags attached. Common errors: "electronics" on transport/work entries, "building" on 乗換 (should be transportation), "clothing" on 歯車 (should be general), "movement" on 蛙 (should be animal-insect), "furniture" on 推定 (should be general), "leisure" on 水産 (should be nature-environment). Pattern: AI model assigns tags based on example topics rather than the headword's semantic domain.

## 2026-05-30 session 005 (04307–04326)

[entry] 04312 発電: semantic tags include "geography" and "time-general" which appear incorrect for a power-generation entry. Should be "action" or similar neutral tag.

[entry] 04316 鮫: semantic tag is "general" but neighboring entries 04319 烏賊 and 04323 蛸 use "animal-fish". Consider updating 04316 to "animal-fish" for consistency.
