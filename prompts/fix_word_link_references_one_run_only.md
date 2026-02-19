# Fix Broken Word Link References (One-Time Task)

Fix inline word links in 13 specific entries that reference non-existent entry IDs. This is a one-time cleanup task — do not use for ongoing polishing.

## Background

These entries have `⟦...⟧` inline links pointing to entry IDs that don't exist. There are two distinct problems:

1. **Entries 00740–00751** (12 entries): Links use **bare numeric IDs** (e.g., `00498`) instead of full entry IDs (e.g., `00498_nani`). Every link in these entries needs the ID portion fixed.

2. **Entry 00761_tsukeru** (1 entry): A single link in the notes references `00792_ki` which doesn't exist (that file is `00792_kubi`). The correct entry for 気 is `02199_ki`.

## Affected Entries

```
entries/00500/00740_oishii.json      (35 broken links)
entries/00500/00741_okureru.json      (23 broken links)
entries/00500/00742_okuru.json        (58 broken links)
entries/00500/00743_oto.json          (50 broken links)
entries/00500/00744_raigetsu.json     (45 broken links)
entries/00500/00745_rainen.json       (47 broken links)
entries/00500/00746_raishuu.json      (40 broken links)
entries/00500/00747_roku.json         (33 broken links)
entries/00500/00748_ryokou.json       (38 broken links)
entries/00500/00749_san.json          (37 broken links)
entries/00500/00750_semai.json        (50 broken links)
entries/00500/00751_sengetsu.json     (42 broken links)
entries/00500/00761_tsukeru.json      (1 broken link)
```

## Prerequisites

Load the inline word links skill for format reference and the common words table:

```
.claude/skills/inline-word-links/SKILL.md
```

## Fix Procedure

### Step 1: Fix entries 00740–00751 (bare numeric IDs)

These entries have links like:
```
⟦{何|なん}→なに：00498⟧⟦の→の：09472⟧
```

The format is correct except the entry ID is bare (e.g., `00498` instead of `00498_nani`). For each entry:

1. Read the entry file
2. Find every `⟦...⟧` link block in examples and notes
3. For each link, extract the bare numeric ID
4. Look up the correct full entry ID. Use this approach:
   ```bash
   # Find the actual entry file for a bare ID
   ls entries/*/<ID>_*.json
   ```
   For example, `ls entries/*/00498_*.json` will show `entries/00000/00498_nani.json`, confirming the full ID is `00498_nani`.
5. Replace the bare ID with the full ID in the link
6. **Semantically verify** each link — confirm the linked entry matches the word's meaning in context. Use the common words reference table in the skill file for quick checks.
7. Update the `modified` timestamp:
   ```bash
   python3 build/get_timestamp.py
   ```
8. Save the entry

**Batch lookup approach** — to speed things up, extract all unique bare IDs first:

```bash
python3 -c "
import json, re, glob
bare_ids = set()
for path in glob.glob('entries/00500/007[4-5][0-9]_*.json'):
    with open(path) as f:
        text = f.read()
    for m in re.finditer(r'：(\d{5})⟧', text):
        bare_ids.add(m.group(1))
for bid in sorted(bare_ids):
    print(bid)
" | while read id; do echo -n "$id -> "; ls entries/*/${id}_*.json 2>/dev/null || echo "NOT FOUND"; done
```

This gives you a mapping of bare ID to full ID. Then apply the replacements.

### Step 2: Fix entry 00761_tsukeru

This entry has one broken link in the notes field:
```
⟦{気|き}→気：00792_ki⟧
```

The entry `00792_ki` does not exist. The correct entry for 気 is `02199_ki`. Change it to:
```
⟦{気|き}→気：02199_ki⟧
```

### Step 3: Validate and build

```bash
python3 build/validate.py 2>&1 | grep -E "Word link warnings"
```

This should report 0 word link warnings (or at least none for these 13 entries). If warnings remain, fix them before proceeding.

Then do a full build:

```bash
make build
```

### Step 4: Commit

```bash
git add entries/00500/00740_oishii.json entries/00500/00741_okureru.json entries/00500/00742_okuru.json entries/00500/00743_oto.json entries/00500/00744_raigetsu.json entries/00500/00745_rainen.json entries/00500/00746_raishuu.json entries/00500/00747_roku.json entries/00500/00748_ryokou.json entries/00500/00749_san.json entries/00500/00750_semai.json entries/00500/00751_sengetsu.json entries/00500/00761_tsukeru.json
git commit -m "Fix broken word link references in 13 entries

Entries 00740-00751: replace bare numeric IDs with full entry IDs
Entry 00761: fix incorrect 00792_ki reference to 02199_ki"
```

## Quality Checklist

Before committing:
- [ ] All 499 word link warnings are resolved
- [ ] Every replaced ID points to a real entry file
- [ ] Each link was semantically verified (correct meaning in context)
- [ ] No new validation errors introduced
- [ ] `make build` completes successfully
- [ ] The `modified` timestamp was updated on every changed entry

## Important Notes

- **Do NOT rewrite the links from scratch.** The existing link markup (surface forms, arrows, baseforms) is correct — only the entry ID portion needs fixing.
- **Do NOT change entries outside the 13 listed above.**
- **Do NOT update polishing progress files** — this is a standalone fix, not part of the inline-links polishing task.
- This prompt is single-use. Once the fixes are committed, this task is complete.
