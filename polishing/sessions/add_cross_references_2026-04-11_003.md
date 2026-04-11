## Session: Add Cross-References (Antonym Asymmetry Cluster)
Date: 2026-04-11

### Mode
Cluster Mode, restricted to `antonym` type asymmetries. Processed all 232
one-way antonym cross-references identified by
`build/find_merge_candidates.py --asymmetry-only`. No tracking file was updated
(asymmetry-driven, not sequential).

### Approach
For each asymmetric pair "source → target (antonym)", the source already had
an antonym cross-reference; the target was missing the reciprocal back-link.
Only the target entries were modified (per the `add_cross-references.md`
instruction: "When visiting target entries, ONLY add the reciprocal back-link
to the starting entry"). No other cross-references on the target entries were
audited, modified, or migrated.

Pairs were grouped by unique target entry (232 pairs → 221 unique targets,
with 11 targets receiving two incoming back-links). Each target was loaded,
the new back-link appended to its `cross_references` array, and its
`metadata.modified` timestamp refreshed. Edits were applied via standard JSON
re-serialization; no surgical text edits were necessary.

### Label Convention
All new labels describe the TARGET of the new back-link (i.e., the source
entry of the original one-way link). Labels are taken from the first
comma/semicolon segment of the source entry's `gloss` field. This matches the
convention used in session 002 and is consistent with the style used on the
source side of the original one-way links.

### Statistics
- Back-links added: 232
- Target entries modified: 221
- Targets receiving two back-links: 11 (see "Multi-source targets" below)
- References fixed/migrated: 0

### Multi-source targets (11)
These targets had two distinct source entries with one-way antonym links:

- 00517_muzukashii ← 00765_yasashii, 02640_yasashii
- 01125_kibishii ← 00430_yurui, 02640_yasashii
- 01320_inaka ← 01477_toshi, 03115_daitokai
- 01614_juubun ← 03598_fusoku, 05616_fujuubun
- 01985_heru ← 01183_fueru, 02422_masu
- 02526_touchaku ← 01832_shuppatsusuru, 03694_hassha
- 03595_fukou ← 01420_shiawase, 02774_saiwai
- 04133_yakan ← 01713_hiruma, 03519_nicchuu
- 09378_kakkoii ← 04752_dasai, 10759_kakkowarui
- 12890_shudou ← 03339_jidou, 06412_dendou
- 14806_shakuhou ← 02803_kousoku, 03397_taiho

### Flagged for curator review
Asymmetry cleanup was the goal of this session; questionable pre-existing
antonym links on source entries were added to the target as back-links
anyway (per task scope), but curators may want to revisit:

1. **11717_kaeru (代える "to substitute") → 00508_kaeru (帰る "to return home")**
   — These are NOT direct antonyms; they are homophones with unrelated
   meanings. The source's `cross_references` antonym link is almost certainly
   a miscategorization (likely meant as `homophone`). A curator should review
   and likely retype or remove both sides of this link.

2. **06412_dendou (電動 "electric-powered") → 12890_shudou (手動 "manual")**
   — Not a direct antonym in the lexical sense. The proper antonym pair for
   手動 is 自動 ("automatic"), which is already linked separately. 電動 is a
   power-source descriptor, not the lexical opposite of 手動. This link could
   be retyped as `contrast` or `related` on both sides.

3. **00761_tsukeru (付ける "to attach, to turn on") → 00528_kesu (消す
   "to turn off, to erase")** — The antonym relationship is valid for the
   "turn on/off" sense, but the new back-link label "to attach" derives from
   the first gloss segment of 00761_tsukeru and is contextually awkward here
   (the relevant sense is "to turn on"). A curator may want to refine the
   label on 00528_kesu to "to turn on" or similar.

4. **02774_saiwai (幸い "fortunately, luckily; happiness") → 03595_fukou
   (不幸 "unhappiness, misfortune")** — The back-link label "fortunately"
   (first gloss segment, adverbial sense) is awkward as an antonym of
   "unhappiness." The "happiness" sense of 幸い is the one that pairs with
   不幸. A curator may want to adjust the label to "happiness."

All four cases above result from either (a) a questionable pre-existing
source-side antonym classification (#1, #2) or (b) a label that is
mechanically correct but contextually suboptimal due to the source's
multi-sense gloss (#3, #4). None introduce validator errors, and the
asymmetry is now resolved in all cases.

### Verification
- `build/validate.py`: 23021/23021 entries valid (no new cross-reference,
  homonym, POS, or hardenable-ref warnings on modified entries; pre-existing
  counts unchanged)
- `build/find_merge_candidates.py --asymmetry-only`:
  - Before: 2998 asymmetric pairs (antonym: 232)
  - After: 2766 asymmetric pairs (antonym: 0)
  - Exact drop of 232 matches back-links added
- `make build`: clean rebuild of the static site

### Notes
- Remaining asymmetry types after this session: related (~1840), synonym
  (~496), contrast (~279), see_also (~90), prominent_see_also (~40), pair
  (~21). (Counts approximate; see the report for exact numbers.)
- `check_semantic_clusters.py --type antonym` may still report additional
  gaps within semantic groups (e.g., suggesting multi-way antonym clusters).
  Those are broader cluster completeness issues, not asymmetries, and were
  intentionally out of scope for this session.

### Next Entry
N/A — this was an asymmetry-driven session, not sequential.
