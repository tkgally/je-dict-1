# Code & Structure — Prompt 7: Enrich entries_index.json with tag and tier data

**Source:** Agent 1 Report (Code & Structure), Prompt 7
**Priority:** Medium
**Effort:** Low

---

In je-dict-1, the entries_index.json file stores only basic metadata (id, headword,
reading, gloss, filename, path) for each of the 10,306 entries. Enrich it by adding:

1. vocabulary_tier (from metadata.vocabulary_tier)
2. part_of_speech (from part_of_speech field)
3. pos_tags (from metadata.tags.pos array)
4. cross_reference_count (length of cross_references array)
5. example_count (length of examples array)
6. has_inline_links (boolean: whether any example contains the link delimiter character)

Edit build/update_entries_index.py to extract these additional fields. Then run:
python3 build/update_entries_index.py

Verify the output looks correct by checking the first few entries in entries_index.json.
