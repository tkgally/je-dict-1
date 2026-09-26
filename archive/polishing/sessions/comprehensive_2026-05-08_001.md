## Session: Comprehensive Polish
Date: 2026-05-08
Entries processed: 00001, 00002, 00003, 00004, 00005

### Per-entry changes
- 00001 (余る/amaru): removed duplicate `conjugation` stub key (the file had both the legacy stub and the full conjugation table, with the second silently overriding the first); added back-link cross-reference on neighbor 17255_amari (noun 余り) pointing to this verb form; updated modified timestamps on both.
- 00002 (編む/amu): removed duplicate `conjugation` stub key; added back-link cross-references on neighbor 04373_oru (織る "to weave") to 00002_amu and to 00326_nuu (織る's cross_references was empty).
- 00003 (あんまり/anmari): tier 1 clean — schema, furigana, inline links, prominent_see_also pair with 00604_amari all valid. No changes.
- 00004 (扇ぐ/aogu): removed duplicate `conjugation` stub key; added cross-reference to 07924_aoru (煽る) since sense 2 examples ({不安}を{扇}る etc.) really belong to 煽る not 扇ぐ — these are two distinct lemmata with different stems and conjugations. Also added back-link from 07924_aoru. Logged as [entry] for future restructuring.
- 00005 (アップ/appu): tier 1 clean — schema, furigana, inline links, antonym pairing with 00035_daun all valid. No changes.

### Candidates added
- 余す (あます): "to leave over (transitive); seen in entry 00001" — transitivity pair of 余る referenced in 00001's prominent_see_also but had no entry yet.

### Observations logged
- [pattern] Many verb entries (and at least one i-adjective category likely too) contain TWO `"conjugation":` keys: a legacy stub `{"type":"godan","ending":"る","stem":"…"}` plus a full conjugation table appended later. JSON parsers take the second key, so the data is correct, but the stub is dead text. Detected on 00001, 00002, 00004, 07924; not present on 00006_aru. Worth a one-pass cleanup script.
- [tooling] A small script could scan `entries/**/*.json` for duplicate `"conjugation":` keys (or any duplicate top-level key) and either auto-prune the legacy stub or report. `jq -e 'has("conjugation")'` won't catch this because Python parsing collapses duplicates. Use raw text grep `grep -c '"conjugation":'` per file.
- [entry] 00004_aogu (扇ぐ) conflates two distinct verbs: 扇ぐ (godan-gu, to fan) for sense 1 and 煽る/扇る (godan-ru, to incite) for sense 2. Sense 2 examples (00004_aogu_ex3, ex5, ex6) all use the form 扇る (る okurigana — wrong conjugation class for the headword). 07924_aoru already covers all three senses comprehensively (fan, incite, tailgate). Recommend: drop sense 2 from 00004_aogu (and its three examples) and let 07924_aoru carry that meaning. Cross-reference between the two has been added in this session.

### Next entry
00006
