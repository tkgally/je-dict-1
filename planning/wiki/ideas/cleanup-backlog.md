# Cleanup Backlog

**Last updated**: 2026-05-10

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

## Informational: Pre-polished cohort around 00083–00090

Four entries in the 00074–00096 range (00083 俳句, 00086 発揮, 00087 花火, 00088 判事) were already fully linked — suggesting a prior polish pass touched that range. Subsequent sessions entering this area should expect occasional entries needing no work.

## Related pages

- [Tooling Backlog](tooling-backlog.md) — tool improvements surfaced alongside these patterns
- [Entry Follow-ups](entry-followups.md) — specific entry fixes
- [Content Pipeline](../project/content-pipeline.md) — how polishing tasks work
- [Entry Consistency](../topics/entry-consistency.md) — consistency standards
