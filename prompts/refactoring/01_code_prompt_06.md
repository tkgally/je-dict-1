# Code & Structure — Prompt 6: Archive one-time migration scripts

**Source:** Agent 1 Report (Code & Structure), Prompt 6
**Priority:** Low
**Effort:** Very low

---

In je-dict-1, the build/ directory contains several one-time migration scripts that
were used during development but are no longer needed for regular operation. Move them
to a new build/archive/ directory to reduce clutter:

Scripts to archive:
- build/migrate_cross_references.py
- build/migrate_entries.py
- build/migrate_pos.py
- build/renumber_entries.py
- build/fix_katakana_readings.py
- build/fix_round_timestamps.py
- build/add_example_ids.py
- build/pos_mapping.json (used only by migrate_pos.py)

Also move the scripts/ directory's contents (fix_sense_numbers_format.py,
update_single_sense.py) to build/archive/ since they are ad-hoc fix scripts.

After moving, verify the build still works: python3 build/validate.py
