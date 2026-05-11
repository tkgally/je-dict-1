# Cleanup Backlog

**Last updated**: 2026-05-11

Concrete cleanup work items surfaced during comprehensive-polish sessions. Each item describes a systemic pattern that affects multiple entries and could be addressed by a dedicated batch pass.

## Priority 1: Unlinked notes in older entries

**Source**: Comprehensive-polish sessions 2026-05-08 through 2026-05-09 (entries 00006–00096)
**Scope**: Virtually every entry in the January–February 2026 creation cohort

Older noun entries have linked example sentences but **unlinked notes**. Structured lists in `notes` (Common Collocations, Related Words, Types of X, Compounds, Similar Words) use bare `{kanji|reading}` without `⟦...⟧` wrappers. This is confirmed as the single most common tier-1 polish deficit for entries below ~00100, and likely extends through most pre-March 2026 entries.

The inline-links polishing task (`polishing/tasks/inline-links/progress.txt`) at entry 02730 is the primary mechanism addressing this, but comprehensive-polish sessions are also fixing entries as they encounter them starting from entry 00001.

## Priority 2: Missing or broken cross-references

**Source**: Comprehensive-polish sessions 2026-05-08 through 2026-05-09

Two related sub-issues:

1. **Under-populated cross_references**: Entries mention obvious neighbors in notes but have no `cross_references` entries for them. Examples: 00010_banchi → 住所/丁目/号; 00014_biyou → 美容院/美容師/健康; 00018_booto → 船/ヨット/カヌー.

2. **Structurally invalid cross_references**: Some entries have cross-reference objects with `headword`/`reading` but no `target_id` field (e.g., 00041_fudan → 通常, 00065_genni → 実際に, 00069_gesui → 上水). `validate.py` emits a "Note" rather than an error for these, so they persist silently.

3. **Missing field entirely**: 09491_choume was missing the `cross_references` field altogether, not just having it empty. The symmetry checker may silently skip such entries.

**Suggested actions**:
- One-shot scanner listing every cross_references entry without `target_id`
- Consider `validate.py --strict` mode promoting "missing target_id" notes to errors
- Confirm `check_consistency.py` flags entries lacking the `cross_references` field

## Priority 3: Cross-reference symmetry on thematic clusters

**Source**: Comprehensive-polish 2026-05-09 session 002

Back-link symmetry on thematic clusters (school types, family terms, time expressions, ceremony types) is poor. Example: 00055_gakkou ↔ 01055_shougakkou/01083_koukou had no back-links until manually fixed.

**Suggested action**: High-leverage one-shot batch — pick a cluster, ensure every member references its main parent term. `check_semantic_clusters.py` partially addresses this but focuses on transitivity/antonym/keigo clusters rather than thematic groupings.

## Priority 4: Duplicate conjugation keys in verb JSON

**Source**: Comprehensive-polish 2026-05-08 session 001

Many verb entries have two `"conjugation":` top-level keys: a legacy stub (e.g., `{"type":"godan","ending":"る","stem":"…"}`) plus the full conjugation table appended later by `add_conjugations.py`. JSON parsers silently take the last value, so runtime behavior is correct, but the dead stub wastes space and is confusing. Confirmed on 00001_amaru, 00002_amu, 00004_aogu, 07924_aoru; not present on 00006_aru. Likely affects most verb entries predating the conjugation-table retrofit.

**Suggested action**: See tooling-backlog for the pruning script proposal.

## Priority 5: Particle entry polish

**Source**: Comprehensive-polish 2026-05-09 sessions 002 and 003

Particle entries with extensive structured fields (e.g., 00051_ga and 00079_ha with `predicates_requiring`, `particle_contrasts`, `fixed_patterns`, `common_mistakes`, `information_structure`) contain dozens of small Japanese phrase fragments that lack inline link coverage. These are not addressable by ordinary tier-1 polishing — they need a dedicated particle-polish session.

**Affected entries**: At minimum 00051 (が), 00079 (は), and likely 00422 (を), 00314 (に), 00502 (で), 00504 (と), 00512 (から).

## Priority 6: Spurious onomatopoeia conjugation tables

**Source**: Wiki maintenance 2026-05-11 entry exploration

Twelve adverbial onomatopoeia entries currently carry full godan conjugation blocks with nonsense forms (e.g., ぐつぐつ → ぐつぐたない, こつこつ → こつこたない). They have `pos: ["adverb", "onomatopoeia"]` (no verb POS), but a stale `verb_class: "godan-tsu"` tag triggered `add_conjugations.py` at some point in the past.

**Affected entries (12):**
05646_gyuugyuu, 05723_pakupaku, 05724_jabujabu, 05726_boubou, 06683_potsupotsu, 08432_gotsugotsu, 18531_gutsugutsu, 21888_mukumuku, 22356_gougou, 26081_pukupuku, 26864_buruburu, 27085_kotsukotsu.

**Suggested actions**:
1. One-shot pass: remove the `conjugation` field and the stray `verb_class` tag from each of the 12 entries.
2. Defensive guard in `add_conjugations.py`: refuse to write a conjugation block unless the entry has at least one `verb-*` POS tag. Filed in [Tooling Backlog](tooling-backlog.md).
3. See [Schema Tag Reliability](../topics/schema-tag-reliability.md) for the broader pattern.

## Priority 7: Politeness tag conflation (uchi/soto, bikago, familiar suffixes)

**Source**: Wiki maintenance 2026-05-11 entry exploration

The `politeness` tag's four buckets (plain/polite/humble/honorific) are being applied too loosely. Three sub-issues:

1. **Uchi/soto kinship terms mis-tagged as humble**: 母 (はは), 父 (ちち), 兄 (あに), 姉 (あね), 息子 (むすこ) and several similar entries are tagged `politeness: humble`. They are the plain in-group reference forms, not humble forms in the technical sense. The contrast お母さん/お父さん/お兄さん etc. (out-group reference and address forms) is uchi/soto, not the speech-level politeness scale.

2. **Bikago mis-tagged as honorific**: Words where the お〜/ご〜 prefix has fused into the lexical form (ご飯, お釣り, etc.) are tagged `honorific`. They are 美化語 (bikago, beautifying language) — a separate category in the 2007 五分類 (five-category) reclassification — not productive sonkeigo.

3. **Familiar suffixes mis-tagged as honorific**: 〜ちゃん, 〜くん are tagged `politeness: honorific`. They are diminutive/familiar suffixes marking intimacy or subordinate-status address, not deference.

**Total affected**: ~58 entries with non-verb POS and `politeness: humble`; ~49 entries with non-verb POS and `politeness: honorific`. Not all are wrong, but a meaningful fraction is.

**Suggested actions**:
- These cases need semantic review, not a deterministic pass. They are a natural target for a polish-politeness-labels task (parallel to `polish_semantic_labels.md`).
- In the interim, ensure the notes prose carries the correct nuance even if the tag is coarse. Most well-polished entries (e.g., 00549_haha) already do this.
- Longer term: see [Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Implications for the schema" for the structured-politeness proposal vs. its costs.

## Priority 8: Unconsolidated duplicate-expression entries

**Source**: Wiki maintenance 2026-05-11 entry exploration

Some entries are duplicates of each other that were linked via `prominent_see_also` instead of being merged. Confirmed example: 02008_ikuratemo and 02461_ikuratemo both cover the expression いくら〜ても. The two entries have overlapping examples and similar (but not identical) notes. The link makes the relationship discoverable but two parallel sources of truth keep diverging on every polishing pass.

**Suggested action**: Run `python3 build/find_merge_candidates.py --merge-only` and review the output. Merge candidates where the two entries are functionally identical. The `consolidate-entries` skill describes the process; the [Resolve Duplicates](../../.claude/skills/resolve-duplicates/SKILL.md) skill (path may differ) is the operational guide.

Also: 02008_ikuratemo carries `semantic: ["furniture"]` — an obviously stale auto-label. This is a representative case for [Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Stale auto-labels."

## Informational: Pre-polished cohort around 00083–00090

Four entries in the 00074–00096 range (00083 俳句, 00086 発揮, 00087 花火, 00088 判事) were already fully linked — suggesting a prior polish pass touched that range. Subsequent sessions entering this area should expect occasional entries needing no work.

## Related pages

- [Tooling Backlog](tooling-backlog.md) — tool improvements surfaced alongside these patterns
- [Entry Follow-ups](entry-followups.md) — specific entry fixes
- [Content Pipeline](../project/content-pipeline.md) — how polishing tasks work
- [Entry Consistency](../topics/entry-consistency.md) — consistency standards
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis of recurring tag-drift patterns (covers P6–P8 above)
