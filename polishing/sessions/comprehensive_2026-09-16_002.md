# Comprehensive polish — 2026-09-16 (002)

Mode: `polish` (selector reason: "polish: highest scheduler debt among eligible modes").

## Priority lane (`polishing/priority/notes.txt`, cursor line 8914 → 21494)

Most of the scanned range had already been touched by recent bulk passes
(systemic-fix, accuracy-review) within the last 30 days, so very few
unmodified candidates turned up — 15 found after scanning ~12,580 lines; 5
of those needed real fixes:

- `02991_ashioto` (足音) — semantic tag was a sole `general`; changed to `movement`.
- `04517_burausu` (ブラウス) — two hand-written `noentry` markers (シフォン,
  フリル) replaced with plain text; both added as candidates.
- `04932_mimizu` (蚯蚓) — three `noentry` markers (蝦蟇, イモリ, 地竜) fixed;
  一つ (おたまじゃくし) and からし〈of 04979 below〉 actually already have
  entries, so those were relinked instead of left as noentry; also added
  furigana to a bare `{蚯蚓}` the validator flagged in the notes.
- `04924_ryouseirui` (両生類) — four `noentry` markers: 両生 and 蝦蟇 and イモリ
  added as candidates; おたまじゃくし relinked to its existing entry (28707).
- `04979_aemono` (和え物) — からし relinked to its existing entry (28711)
  instead of `noentry`.
- 10 other priority-lane entries (00109_hobo, 04731_gorufu, 05262_zukizuki,
  05325_tansa, 05375_meramera, 06920_teiuka, 00077_guusuu, 02208_koi,
  04855_shousou, 05168_urouro) were read and found already solid — no
  change made.

## Frontier lane (`polishing/tasks/comprehensive/progress.txt`, 07421 → 07446)

Read entries 07421–07445 (25 entries). Found a cluster of verb-suru entries
missing the required `transitivity` tag — apparently dropped when these
entries were bulk-touched on 2026-09-02:

- Added `transitivity`: 07424_boukan (transitive), 07425_kainyuu
  (intransitive), 07426_douchou (intransitive), 07428_suitai (intransitive),
  07429_yakushin (intransitive), 07440_shunjun (intransitive),
  07445_torishimari (transitive).
- Fixed sole-`general` semantic tags: 07432_shiagari → `evaluation`,
  07433_temochi → `action`.
- Removed two more hand-written `noentry` markers: 07441_meisou (しがち,
  added as candidate).
- The rest of the range (07430, 07431, 07434–07439, 07442–07444) was read
  and found already solid.

This transitivity gap is a known systemic issue (backlog item
`pos-freetext-transitivity-backfill`); a spot check found 7 more instances
just before this range (07068–07178) that are out of scope for this run —
left for the next `systemic-fix` pass.

## Candidates added

シフォン, フリル, 地竜, 両生, 蝦蟇, イモリ, しがち — 7 new candidates
(`build/manage_candidates.py add`).

## Mechanical pass

`normalize_notes.py`, `auto_link.py`, `harvest_crossrefs.py` run on all 15
changed entries. `auto_link.py` added 6 new unambiguous links (07424,
07433, 07445). `validate.py` clean on all 15 after one furigana fix
(04932).

## Self-check

`review_accuracy.py --ids <15 ids> --budget 0.40`: 3 flagged, all rejected
as reviewer misreadings (register-range note vs. single formality tag; a
note that actually matches its tags; two note sections concatenated by the
reviewer's text extraction). Logged in `reviews/decisions.jsonl`.

`review_links.py`: 1 flag (04932_mimizu, かけると/かける) — verified correct
(と is just the conditional suffix in the surface span); logged as `keep`
in `reviews/link_decisions.jsonl`.

## Cursors

- `polishing/tasks/comprehensive/progress.txt`: `next: 07446`
- `polishing/tasks/comprehensive/priority-cursor.txt`: `line: 21494`
