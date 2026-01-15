# Semantic Assignment Progress Checkpoint

## Task Status: IN PROGRESS

**Last Updated**: 2026-01-15
**Total Entries**: ~4,857
**Single-sense Entries (auto-completed)**: 2,579
**Multi-sense Entries (need manual review)**: ~1,479
**Multi-sense Entries Completed**: ~308 (in ka/) + a/ complete

---

## Current Approach

A two-phase workflow is now in use:

1. **Automated Phase**: Run `scripts/update_single_sense.py` on each directory to automatically assign `sense_numbers: [1]` to all examples in single-sense entries.

2. **Manual Phase**: Semantically analyze each multi-sense entry individually, assigning appropriate sense_numbers based on which definition(s) each example illustrates.

---

## Resume Prompt

Copy and paste the following prompt to continue this task:

```
RESUME SEMANTIC ASSIGNMENT TASK

Read the file RESUME_semantic_assignment.md for the current progress checkpoint.

TASK: Continue semantically assigning example sentences to their corresponding
sense definitions in je-dict-1 dictionary entries.

CURRENT PROGRESS:
- Single-sense entries: COMPLETED for all directories (auto-processed)
- Multi-sense entries:
  - a/: COMPLETE
  - ka/: 15 remaining (all in ka/ki/), 6 files edited but NOT committed
  - Other directories: pending

IMMEDIATE NEXT STEPS:
1. First, commit the 6 pending ka/ki/ files:
   git add entries/ka/ki/kinko_00502.json entries/ka/ki/kinodoku_01688.json \
     entries/ka/ki/kire_01793.json entries/ka/ki/kirei_00093.json \
     entries/ka/ki/kireru_00615.json entries/ka/ki/kiri_01025.json
   git commit -m "Assign sense_numbers to multi-sense entries in ka/ki/ (6 more files)"

2. Process remaining 9 files in ka/ki/ (listed in RESUME file)

3. After ka/ complete, continue with sa/, ta/, etc.

WORKFLOW FOR EACH ENTRY:
1. Read the file to see definitions array (each sense with sense_number)
2. Analyze each example sentence against the definitions
3. Assign sense_numbers: [1], [2], [1, 2], etc.
4. Edit the file using the Edit tool
5. Commit in batches of 6-12 files

ASSIGNMENT RULES:
- Single sense entries: All examples get sense_numbers: [1] (handled by script)
- Multi-sense entries: Analyze each example to determine which sense(s) it illustrates
- Examples can illustrate multiple senses: use [1, 2] format when applicable
- Every example must link to at least one sense

ENTRY FILE LOCATIONS:
Entries are in /home/user/je-dict-1/entries/{kana_row}/{prefix}/*.json
Example: entries/ka/ki/kireru_00615.json

FINDING REMAINING MULTI-SENSE ENTRIES:
grep -l '"sense_numbers": \[\]' entries/{dir}/*/*.json
```

---

## Progress by Kana Row

| Row | Directory | Single-sense | Multi-sense Remaining | Status |
|-----|-----------|--------------|----------------------|--------|
| あ | entries/a/ | 651 (100%) | 0 | COMPLETE |
| か | entries/ka/ | 649 | 15 | IN PROGRESS (ka/ki/) |
| さ | entries/sa/ | 664 | 304 | SCRIPT DONE |
| た | entries/ta/ | 422 | 267 | SCRIPT DONE |
| な | entries/na/ | 123 | 111 | SCRIPT DONE |
| は | entries/ha/ | 377 | 206 | SCRIPT DONE |
| ま | entries/ma/ | 140 | 152 | SCRIPT DONE |
| や | entries/ya/ | 112 | 69 | SCRIPT DONE |
| ら | entries/ra/ | 64 | 23 | SCRIPT DONE |
| わ | entries/wa/ | 28 | 24 | SCRIPT DONE |

**Total Single-sense Completed**: 2,579 entries
**Total Multi-sense Remaining**: 1,171 entries (15 in ka/ + 1,156 in remaining directories)

---

## Detailed Progress Log

### Initial Sessions (2026-01-15)
- Completed all 651 entries in a/ directory manually
- Created `scripts/update_single_sense.py` to automate single-sense entries
- Began work on ka/ directory

### Script Automation Session (2026-01-15)
- Ran script on ka/: 649 single-sense entries updated
- Manually processed 24 multi-sense entries in ka/ including:
  - ga (が): subject/object marker/conjunction (3 senses)
  - ganbaru (頑張る): try hard/persevere (2 senses)
  - genzai (現在): present time/currently (2 senses)
  - goshujin (ご主人): husband/proprietor (2 senses)
  - kakkou (格好): appearance/suitable (2 senses)
- Ran script on all remaining directories (sa/, ta/, na/, ha/, ma/, ya/, ra/, wa/)
- Total 1,930 single-sense entries auto-processed in remaining directories

### ka/ Directory Processing (2026-01-15 continued)
- Completed ka/ka/, ka/ke/, ka/ko/, ka/ku/, ka/ky/ subdirectories
- Completed ka/ga/, ka/ge/, ka/gi/, ka/go/, ka/gu/ subdirectories
- ka/ki/ IN PROGRESS: processed through kiri_01025
- **6 files edited but NOT YET COMMITTED:**
  - kinko_00502.json (金庫: safe/vault)
  - kinodoku_01688.json (気の毒: pitiful/sorry)
  - kire_01793.json (切れ: piece/cloth/counter)
  - kirei_00093.json (きれい: beautiful/clean)
  - kireru_00615.json (切れる: be cut/run out/snap)
  - kiri_01025.json (霧: fog/mist)
- **15 files remaining in ka/ki/** (see list below)

---

## Entries Flagged for Human Review

| Entry ID | Reason |
|----------|--------|
| (none yet) | |

---

## Next Steps

1. **IMMEDIATE**: Commit the 6 pending ka/ki/ files listed above
2. Complete remaining 9 files in ka/ki/:
   - kirin_05126.json, kiro_00161.json, kiroku_01593.json
   - kiru_01819.json, kitanai_00094.json, kitsui_01259.json
   - kiyoi_00001.json, kiyou_01781.json, kizamu_03519.json
   - kizu_01027.json, kizuku_00609.json, kizuku_00817.json
   - kizutsukeru_00611.json, kizutsuku_00610.json, kyougen_04794.json
3. After ka/ complete, process sa/ (304 entries)
4. Continue with ta/, na/, ha/, ma/, ya/, ra/, wa/
5. Update this file after completing each directory

---

## Multi-sense Entry Counts by Directory

To get current count of unprocessed multi-sense entries:
```bash
grep -l '"sense_numbers": \[\]' entries/{dir}/*/*.json 2>/dev/null | wc -l
```

Current counts (as of last update):
- ka/: 15 (all in ka/ki/, 6 edited but uncommitted)
- sa/: 304
- ta/: 267
- na/: 111
- ha/: 206
- ma/: 152
- ya/: 69
- ra/: 23
- wa/: 24

## Remaining Files in ka/ki/ (15 total)

Files with empty sense_numbers:
```
kirin_05126.json
kiro_00161.json
kiroku_01593.json
kiru_01819.json
kitanai_00094.json
kitsui_01259.json
kiyoi_00001.json
kiyou_01781.json
kizamu_03519.json
kizu_01027.json
kizuku_00609.json
kizuku_00817.json
kizutsukeru_00611.json
kizutsuku_00610.json
kyougen_04794.json
```
