# Systemic-fix session — 2026-06-15 — dictionary-wide U+FFFD mojibake repair

**Task:** Drive the dictionary-wide U+FFFD (`�`) replacement-character corruption to
zero in a single session and add a CI guard so it cannot recur.

**Branch:** `claude/dictionary-mojibake-repair-fjj9b5`

## Starting state
- `grep -rlP '\xEF\xBF\xBD' entries/` → **234 corrupted entries / 1225 U+FFFD chars**
  (surfaced by routine_2026-06-15_001; tooling-backlog #16).
- Triage: ~97% of corruption sat inside `{kanji|reading}` furigana wrappers, the rest
  standalone kana / particles / sentence-final 。 / em-dash separators. All inline-link
  markers (`⟦ ⟧ → ：`) were intact and balanced (0 corrupted delimiters).
- Git history could not help: the repo is a 50-commit squashed clone and every corrupted
  file was already corrupt in the only commit that touches it. Reconstruction was therefore
  done from Japanese context (the wrapper's kanji fixes its standard reading; the
  headword/compound fixes the kanji), which is well-determined.

## What was done
1. **Detector** — added `build/check_mojibake.py` (read-only; `--json`, `--summary`,
   `--range`, per-entry/-field U+FFFD counts with context windows), mirroring the other
   `build/check_*.py` detectors. Marked tooling-backlog #16 **SHIPPED** and indexed it in
   `backlog-queue.json` as the standing `mojibake-ufffd` item.
2. **Reconstruction** — split the 234 files into 8 disjoint batches and reconstructed every
   `�`-run to its original kanji / kana / particle / punctuation, anchored on the
   headword/reading, the intact kanji compound, or a parallel collocation line. Verified
   residual `�` == 0 per file and updated each `metadata.modified`. Committed in 6 batches.
3. **CI regression guard** — added `find_mojibake_errors()` + a hard check in
   `build/validate.py` (`validate_entry_file`, so the full/single/changed/range paths all
   enforce it). CI (`validate.yml` runs `validate.py`) now **fails** on any entry containing
   U+FFFD. Includes an empty `MOJIBAKE_ALLOWLIST` for future genuinely-unrecoverable
   escalations. Covered by `build/tests/test_validate_mojibake.py` (7 tests, all passing).
   The guard was enabled only after the detector reached zero (correct sequencing).
4. **Build + verify** — `python3 build/validate.py` → exit 0, 29048/29048 entries valid,
   no mojibake/schema errors. `check_mojibake.py` → 0. `make build` regenerated `docs/`,
   `entries_index.json`, the kanji index (many files now correctly link the entries whose
   kanji were restored), `word_id_lookup.json`, and candidate sync.

## Final count
- **U+FFFD remaining: 0** (1225 → 0 across all 234 entries).
- **Escalations to curator: 0.** Every `�` was recoverable; no entry IDs added to
  `reviews/needs_curator.txt`; `MOJIBAKE_ALLOWLIST` left empty. The few non-kanji
  reconstructions (grammatical particles, honorific prefixes, em-dashes, multi-kana runs,
  the 研鑽 idiom in 25579) were high-confidence, context-determined, and noted by the
  reconstructing agents — not guesses.

## Files changed
- 234 entry JSON files (corruption repaired).
- `build/check_mojibake.py` (new detector), `build/validate.py` (guard),
  `build/tests/test_validate_mojibake.py` (new tests).
- `planning/wiki/ideas/tooling-backlog.md` + `backlog-queue.json` (#16 shipped).
- Regenerated build artifacts (`docs/`, indexes, kanji index, word lookup).

## Notes / follow-ups
- None outstanding. The guard prevents reintroduction; the detector remains available for
  ad-hoc scans. If a future corruption is ever genuinely unrecoverable, add its entry ID to
  `MOJIBAKE_ALLOWLIST` in `build/validate.py` and `reviews/needs_curator.txt` rather than
  guessing.
