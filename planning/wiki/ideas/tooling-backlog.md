# Tooling Backlog

**Last updated**: 2026-05-10

Tool improvements and new script ideas surfaced during comprehensive-polish sessions. Each item includes the rationale, suggested approach, and source observation.

## 1. Duplicate top-level JSON key pruner

**Source**: Comprehensive-polish 2026-05-08 session 001

Many verb entries have duplicate `"conjugation":` keys (a legacy stub plus the full table). Python's `json.load` silently collapses duplicates, so runtime is fine but the files contain dead data. Need raw text scanning since `json.load` hides the problem.

**Detection**: `grep -c '"conjugation":' entries/**/*.json | awk -F: '$2 > 1'`

**Suggested implementation**: A one-shot script next to `add_conjugations.py` that:
1. Reads each entry file as raw text
2. Parses for duplicate top-level keys using regex or a streaming JSON parser
3. Removes the first (legacy stub) occurrence, keeping the full table
4. Validates the result with `json.load` before writing

**Scope**: Primarily affects `conjugation` but could generalize to any duplicate key.

## 2. Fix verify_furigana.py false positives on inline links

**Source**: Comprehensive-polish 2026-05-08 session 002 and 2026-05-09 session 001

`build/verify_furigana.py` raises false positives on inline link metadata. After `FURIGANA_PATTERN.sub('', notes)` it still sees kanji in the `→` tail of inline links like `⟦{時間|じかん}→時間：00468_jikan⟧` and reports them as unannotated. The render pipeline doesn't render that tail.

**Suggested fix**: Extend the strip pattern to also consume `→…：…⟧` (and the leading `⟦`) before counting kanji. Small change.

## 3. Suggested cross-references from inline-linked notes

**Source**: Comprehensive-polish 2026-05-08 session 002

When an entry's notes contain inline links (`⟦...→base：entry_id⟧`), the link targets are often good candidates for `cross_references` entries. Currently this connection is manual.

**Suggested implementation**: A scanner that:
1. Extracts `→<id>⟧` link targets from an entry's notes
2. Checks whether each target is already in `cross_references` or `prominent_see_also`
3. Surfaces unlinked targets as suggested cross-references

Could be a standalone script or integrated into `check_consistency.py`.

## 4. Split-compound detector

**Source**: Comprehensive-polish 2026-05-09 session 003

Adjacent `{kanji|reading}` spans sometimes form a known compound (e.g., `{宅配|たくはい}{便|びん}` when 09534_takuhaibin exists). The scanner would:

1. Walk through notes/examples looking for consecutive furigana spans
2. Concatenate adjacent kanji
3. Look up the concatenated form in `word_id_lookup.json` `by_headword`
4. Flag matches as potential split-compound issues

**Scope**: Particularly useful during inline-link polishing — the split prevents proper linking to the compound entry.

## Related pages

- [Cleanup Backlog](cleanup-backlog.md) — patterns these tools would address
- [Entry Follow-ups](entry-followups.md) — specific entry fixes
- [Architecture and Build System](../project/architecture.md) — build script overview
