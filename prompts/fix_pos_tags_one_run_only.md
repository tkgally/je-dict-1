# Fix POS Tag Consistency (One-Time Task)

Fix mismatches between the free-text `part_of_speech` field and the structured `metadata.tags.pos` array across ~544 entries. This is a one-time cleanup task — do not use for ongoing polishing.

## Background

Each entry has two POS fields:
- **`part_of_speech`** — free-text string (e.g., `"noun"`, `"godan verb"`, `"noun, suru verb"`)
- **`metadata.tags.pos`** — structured array of canonical enum values (e.g., `["noun", "verb-suru"]`)

The validator infers what `tags.pos` should contain from the `part_of_speech` string. When they disagree, it warns. In nearly all cases (528/544), `tags.pos` is correct and `part_of_speech` is too narrow — it needs to be updated to match.

**The fix direction is: update `part_of_speech` to match `tags.pos`** (not the other way around). The `tags.pos` values were set with full knowledge of the word's grammar; the `part_of_speech` string was often written too narrowly.

## Warnings Breakdown

### Category A: "Extra" warnings (528) — `tags.pos` has values `part_of_speech` doesn't imply

These need `part_of_speech` updated. The major patterns:

| Count | Current `part_of_speech` | `tags.pos` has extra | Fix `part_of_speech` to |
|-------|--------------------------|----------------------|-------------------------|
| 256 | `"noun"` | `verb-suru` | `"noun, suru verb"` |
| 81 | `"verb"` | `verb-godan` | `"godan verb"` |
| 29 | `"verb"` | `verb-ichidan` | `"ichidan verb"` |
| 23 | `"adverb"` | `onomatopoeia` | `"adverb, onomatopoeia"` |
| 18 | `"noun"` | `adjective-na` | `"noun, na-adjective"` |
| 9 | `"noun"` | `adverb` | `"noun, adverb"` |
| 9 | `"verb (intransitive)"` | `verb-godan` | `"godan verb (intransitive)"` |
| 8 | `"verb (transitive)"` | `verb-godan` | `"godan verb (transitive)"` |
| 7 | `"noun"` | `adjective-no` | `"noun, no-adjective"` |
| 7 | `"verb (transitive)"` | `verb-ichidan` | `"ichidan verb (transitive)"` |
| 6 | `"verb"` | `verb-suru` | `"suru verb"` |
| 6 | `"noun"` | `counter` | `"noun, counter"` |
| 5 | `"noun"` | `prefix` | `"noun, prefix"` |
| 5 | `"verb (suru)"` | `noun` | `"noun, suru verb"` |
| 4 | `"adjective-na"` | `noun` | `"na-adjective, noun"` |
| 4 | `"verb-suru"` | `noun` | `"noun, suru verb"` |
| 4 | `"verb"` | `noun`, `verb-suru` | `"noun, suru verb"` |
| 3 | `"noun"` | `suffix` | `"noun, suffix"` |
| 3 | `"na-adjective"` | `noun` | `"na-adjective, noun"` |
| 3 | `"adjective (い)"` | `adjective-i` | `"i-adjective"` |
| 2 | `"adjective"` | `adjective-i` | `"i-adjective"` |
| 2 | `"adjective (な)"` | `adjective-na` | `"na-adjective"` |
| 2 | `"adverb"` | `noun` | `"adverb, noun"` |
| 2 | `"suffix"` | `noun` | `"suffix, noun"` |
| 2 | `"noun"` | `verb-ichidan` | `"noun, ichidan verb"` |
| 2+ | `"adverb, adjective (na/no)"` | `onomatopoeia` | `"adverb, na-adjective, no-adjective, onomatopoeia"` |
| misc | (various other small groups) | | (see fix procedure) |

### Category B: "Missing" warnings (16) — `tags.pos` is missing values implied by `part_of_speech`

These need `tags.pos` updated. The specific entries:

| Entry | Issue | Fix |
|-------|-------|-----|
| 7 four-character idiom entries (06145–06249, 07462) | `part_of_speech` says "four-character idiom" but `tags.pos` lacks `expression` | Add `"expression"` to `tags.pos` |
| 02992_ironna | `part_of_speech` "adjectival noun" implies `noun` but `tags.pos` only has `adjective-na` | Add `"noun"` to `tags.pos` |
| 09236_zatsuzen | `part_of_speech` "taru-adjective, to-adverb" implies `adverb` but `tags.pos` only has `adjective-taru` | Add `"adverb"` to `tags.pos` |
| 04582_oiru | `part_of_speech` says "ichidan, irregular" but `tags.pos` has `verb-godan` | **Verify the correct verb class**, then fix whichever field is wrong |
| 04916_chekkusuru | `part_of_speech` says "verb (する)" but `tags.pos` has `verb-godan` | **Verify**: this is a suru-verb; fix `tags.pos` to `["verb-suru"]` and `part_of_speech` to `"suru verb"` |
| 10835_gatagoto | `part_of_speech` "adverb / noun" implies `noun` but missing | Add `"noun"` to `tags.pos` |
| 02004_tsuzukeru | `part_of_speech` "auxiliary verb (ichidan)" implies `verb-ichidan` | Add `"verb-ichidan"` to `tags.pos` |

## Fix Procedure

### Automated fix for Category A (bulk `part_of_speech` updates)

Write a Python script to handle the bulk fixes. The script should:

1. Load each entry
2. Read `tags.pos`
3. Generate the correct `part_of_speech` string from `tags.pos` plus any transitivity info
4. Update `part_of_speech` if it changed
5. Update the `modified` timestamp
6. Save the entry

Use these `part_of_speech` conventions (matching existing entries in the dictionary):

```
Verb patterns:
  ["verb-godan"]                     → "godan verb"
  ["verb-ichidan"]                   → "ichidan verb"
  ["verb-suru"]                      → "suru verb"
  ["verb-godan"] + transitive        → "godan verb (transitive)"
  ["verb-godan"] + intransitive      → "godan verb (intransitive)"
  ["verb-ichidan"] + transitive      → "ichidan verb (transitive)"
  ["verb-ichidan"] + intransitive    → "ichidan verb (intransitive)"

Noun patterns:
  ["noun", "verb-suru"]              → "noun, suru verb"
  ["noun", "adjective-na"]           → "noun, na-adjective"
  ["noun", "adjective-no"]           → "noun, no-adjective"
  ["noun", "adverb"]                 → "noun, adverb"
  ["noun", "counter"]               → "noun, counter"
  ["noun", "prefix"]                → "noun, prefix"
  ["noun", "suffix"]                → "noun, suffix"
  ["noun", "verb-suru"] + na-adj    → "noun, na-adjective, suru verb"

Adjective patterns:
  ["adjective-i"]                    → "i-adjective"
  ["adjective-na"]                   → "na-adjective"
  ["adjective-na", "noun"]           → "na-adjective, noun"

Adverb patterns:
  ["adverb", "onomatopoeia"]         → "adverb, onomatopoeia"
  ["adverb", "noun"]                 → "adverb, noun"

Other:
  ["suffix", "noun"]                 → "suffix, noun"
```

**Important**: Preserve transitivity info. If the current `part_of_speech` contains "(transitive)" or "(intransitive)", carry that forward. Also check `tags.transitivity` for entries where the current `part_of_speech` just says "verb".

### Manual fix for Category B (16 entries needing `tags.pos` updates)

Handle these individually:
1. Read each entry
2. Add the missing value to the `tags.pos` array
3. For 04582_oiru and 04916_chekkusuru, verify the correct verb class first
4. Update the `modified` timestamp
5. Save

### Validation

After all fixes:

```bash
python3 build/validate.py 2>&1 | grep "POS consistency"
```

This should report 0 POS consistency warnings. If warnings remain, investigate and fix.

Then do a full build:

```bash
make build
```

### Commit

```bash
git add entries/
git commit -m "Fix part_of_speech / tags.pos consistency across ~544 entries

Category A: update part_of_speech to match tags.pos (528 entries)
Category B: add missing values to tags.pos (16 entries)"
```

## Quality Checklist

Before committing:
- [ ] 0 POS consistency warnings from `validate.py`
- [ ] No new validation errors introduced
- [ ] Transitivity info preserved in `part_of_speech` for all verbs
- [ ] Entries 04582_oiru and 04916_chekkusuru manually verified
- [ ] `modified` timestamp updated on every changed entry
- [ ] `make build` completes successfully

## Important Notes

- **Do NOT change `tags.pos`** except for the 16 Category B entries. The `tags.pos` values are correct in Category A — only `part_of_speech` needs updating.
- **Do NOT change any other fields** (examples, notes, definitions, etc.).
- The script approach is recommended for Category A due to the volume (528 entries). Manual fixes are fine for Category B (16 entries).
- This prompt is single-use. Once the fixes are committed, this task is complete.
