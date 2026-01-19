# Phase 1: Semantic Group Inventory - Complete

## Summary

Phase 1 of the vocabulary tier realignment has been completed. This phase created a comprehensive inventory of all semantic groups in the dictionary and their current tier assignments.

## Current Tier Distribution

| Tier | Count | Target |
|------|-------|--------|
| Basic | 1,120 | 600-800 |
| Core | 5,296 | 1,600-2,000 |
| General | 743 | unlimited |
| Unassigned | 200 | 0 |
| **Total** | **7,359** | |

## Semantic Groups Identified

A total of **34 semantic groups** containing **468 entries** have been identified and documented in `semantic_groups.json`.

### Self-Contained Groups (11 groups)

These groups have all entries properly assigned to a single tier:

| Group | Entries | Tier |
|-------|---------|------|
| days_of_week | 7 | basic |
| months | 12 | basic |
| numbers_0_10 | 12 | basic |
| numbers_extended | 14 | basic |
| numbers_large | 3 | basic |
| counter_tsu | 9 | basic |
| seasons | 4 | basic |
| directions_cardinal | 4 | basic |
| family_plain | 20 | basic |
| family_honorific | 8 | basic |
| verbs_existence | 2 | basic |

### Groups Requiring Review (23 groups)

These groups have entries split across tiers, often due to homophone matching (e.g., め matching both 目 "eye" and 芽 "bud"):

- adjectives_i_basic (28 basic, 1 core)
- adjectives_na_basic (9 basic, 7 core)
- adverbs_basic (15 basic, 5 core)
- body_parts (19 basic, 1 core)
- colors (10 basic, 3 core)
- conjunctions (8 basic, 2 core)
- counters_general (18 basic, 8 core)
- demonstratives (21 basic, 3 core)
- directions_relative (11 basic, 1 core)
- nouns_animals (12 basic, 1 core)
- nouns_foods (13 basic, 1 core)
- nouns_nature (14 basic, 2 core)
- nouns_people (14 basic, 4 core)
- nouns_places (12 basic, 4 core)
- nouns_things (13 basic, 4 core)
- particles (17 basic, 4 core)
- pronouns (11 basic, 2 core)
- question_words (12 basic, 1 core)
- time_periods (8 basic, 2 core)
- time_relative (16 basic, 2 core)
- verbs_communication (8 basic, 3 core)
- verbs_daily (10 basic, 1 core)
- verbs_movement (10 basic, 2 core)

## Files Generated

1. `build/tier_analysis/all_entries.json` - Master list of all 7,359 entries with tier info
2. `build/tier_analysis/semantic_groups.json` - Detailed semantic group registry
3. `build/tier_analysis/identify_semantic_groups.py` - Script used for analysis
4. `build/tier_analysis/PHASE1_REPORT.md` - This report

## Notes for Phase 2

When proceeding to Phase 2 (Basic Tier Curation), consider:

1. Many "inconsistencies" in semantic groups are homophone issues, not actual tier misassignments
2. The self-contained groups (days, months, numbers, etc.) are already properly assigned
3. Focus on reviewing and potentially demoting entries from basic to core to reach the 600-800 target
4. Verify semantic group integrity when making tier changes

## Key Findings

1. **Numbers are complete**: All basic numbers (0-10), extended numbers (11-100), and large units (100, 1000, 10000) are in basic tier
2. **Core semantic groups intact**: Days, months, seasons, family terms are properly self-contained in basic
3. **468 entries identified in semantic groups**: These need to be kept together when adjusting tiers
4. **~320-520 basic entries need demotion**: To reach the 600-800 target from current 1,120
