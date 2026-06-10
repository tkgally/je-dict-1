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

## Session 007 (2026-06-09, entries 05970–05989)

[pattern] Systematic semantic tag errors in the medical cluster (05975–05979: 通院, 処方, 感染, 炎症, 健康診断) and aviation cluster (05981–05982: 離陸, 着陸): tags were clearly wrong (body-part/clothing/furniture/leisure/geography) — AI generation artifacts where the model copied tags from an unrelated entry. Fixed in this session. Pattern suggests the range ~05970–05990 may have more such errors worth a targeted audit with check_tag_drift.py.

## accuracy-review session 002 (2026-06-09, entries 00201–00450)

[pattern] Semantic tag errors found by cross-model review in the low-ID core/basic range 00201–00450. Specific confirmed false tags fixed:
- 00281 醜い: food/leisure/slang/colloquial tags → emotion/appearance/literary
- 00299 虫歯: body-part tag → health (虫歯 is a dental condition, not a body part)  
- 00240 小〜: grammatical tag → size (semantic prefix, not grammatical particle)
- 00232 記念: "memory" gloss → "memorial" (記念=commemoration/memorial, not mental faculty)
[pattern] The 'descriptive' semantic tag appears to be applied broadly to many entries in this range where it doesn't fit (謙虚, 懸命, 無限, もしかすると, 自ら). Candidate for systematic review via check_tag_drift.py.
[pattern] 'formal' formality tag over-applied to neutral words (清い, なお, 年月, 日時, 稀). Many of these should be 'neutral'. See Cleanup Backlog.
[pattern] 'body-part' semantic tag misapplied to conditions/diseases in early-ID entries (虫歯 fixed; others may exist).
[wiki] The 'descriptive' tag is problematic — it appears to mean "can describe something" rather than a genuine semantic category. Wiki page on semantic tag standards should address when 'descriptive' is appropriate.

## routine v2 polish session (2026-06-10, priority lane 06485/06749/06852/06858/06662/06735 + frontier 05990–05999)

- [tooling] `build/validate.py` (both `--id` and `--range`) does NOT verify inline-link target resolution. It reported "Entry is valid!" for an entry whose link pointed at `04757_deeta` (a wrong ID — 04757 is クラウド; データ is 03944). The error was caught only by an ad-hoc check that resolves every `⟦…：id⟧` entry_id against the on-disk entry set. A link-resolution gate in validate.py (or a pre-commit/CI hook) would catch this whole class of silent linking errors. High value — hit it this session.
- [pattern] "dup-conjugation" notes artifact in compound-verb entries: 06852_hourikomu, 06858_ukabiagaru, and 06735_sashikakaru each opened their notes with a redundant negative/te-form/past bullet list duplicating the `conjugation` table. Removed this session. The 06xxx godan-compound range likely holds many more; `check_artifacts.py` (P10) is the right detector for a systemic-fix sweep.
- [entry] Duplicate 気持ち entries: 01385_kimochi (basic) and 02485_kimochi (core), both glossed "feeling, mood". Almost certainly a duplicate pair needing consolidation. Inline links this session pointed to 01385 (basic).
- [pattern] Productive compound-verb suffix 〜込む ("into/thoroughly", as in 放り込む) and the 掛かる "to hang over / be about to" sense have no entry (only 込む/かかる "to be crowded / to cost / take" exist), forcing `noentry` in FORMATION glosses. Possible suffix/sense candidates if the project wants compound-verb morphemes linkable.

## routine v2 new-entries session (2026-06-10, IDs 29063–29082)

- [skill] Internal organs / anatomy should use semantic `["body-internal"]`, not `["body-part", "health"]`. Existing organ entries (03262_shinzou 心臓, 01706_i 胃, 13953_jinzou 腎臓) all use `["body-internal"]`. I initially tagged four new anatomy entries (29064 頸動脈, 29065 冠動脈, 29067 胆嚢, 29068 十二指腸) `["body-part", "health"]`; the §4 cross-model review flagged the redundant "health" tag and the fix was to switch to `["body-internal"]`. The `entry-guidelines`/`other-entries` skills don't document this convention — worth a note so anatomy is tagged consistently at creation. ("health" stays correct for diseases/procedures: 29066 膵臓癌, 29063 聴診.)
- [pattern] On freshly-created new entries, the §4 accuracy reviewer (`review_accuracy.py`) had low flag precision: 5 of 33 flags applied (~15%). Most rejected flags were (a) translation style nits ("noisily" vs "with heavy footsteps"), (b) suggestions to inject romaji headwords into example translations (against house style), and (c) terminology the model disliked but that matched established entries (e.g. "blessing" for 吉, consistent with existing 大吉 19336). The high-signal catches were gloss completeness (missing the age sense of 古希/喜寿) and one over-literal example translation. Suggests the `translation` dimension is noisy on new entries while `gloss`/`tags` flags are worth more weight — useful input for the wiki metrics-trend precision-by-dimension table.
