## Session: Add Verb Conjugation Data
Date: 2026-03-29
Entries processed: 00001-20350 (full scan of all entries)

### Summary
Added conjugation field and verb_class tag to all verb entries in the dictionary that were missing them. Used a batch processing script (`build/add_conjugations.py`) with linguistic knowledge for verb classification.

### Verb Types Updated
- Godan verbs: ~1200 (including -u, -ku, -gu, -su, -tsu, -nu, -bu, -mu, -ru endings)
- Ichidan verbs: ~600
- Suru verbs: ~3500 (noun + する compounds)
- Kuru verbs: 1 (来る)
- Aru (special): 1 (ある)
- Auxiliary verbs: 1 (～続ける)
- Verb phrase expressions: 4 (頭を抱える, 息を潜める, 手を染める, 目を奪われる)

### Irregular Verbs Handled
- 行く: overrides for irregular て/た forms (行って/行った instead of 行いて/行いた)
- ある: type "aru" for special negative (ない) and limited conjugation

### Entries Skipped
- Non-verb entries: ~14,674
- Proverb/expression entries (no conjugation needed): ~12
- Noun forms of verbs (e.g., 申し送り): 1 (correctly excluded)

### Statistics
- Verb entries updated this session: 5,478
- Next entry ID: 20351

### Notes
- Created `build/add_conjugations.py` helper script for batch processing
- POS field has many inconsistent formats; script handles: "godan verb", "verb (godan)", "noun, suru verb", "noun (verbal)", "noun; noun (する)", "noun" with verb-suru pos tag, "expression, verb phrase", etc.
- Fixed edge case where noun forms ending in り (e.g., 申し送り) were incorrectly classified as godan verbs
- All 20,152 entries pass validation after changes
