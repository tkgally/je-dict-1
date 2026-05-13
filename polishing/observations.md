# Long-Term Observations

Append-only log of observations from comprehensive-polish sessions that go beyond the entry currently being polished. The daily wiki-maintenance session harvests this file: it files actionable items into `planning/wiki/`, schedules concrete work, and prunes entries that have been acted on.

## Format

Each session appends a section. Within each section, prefix observations with a tag:

- `[pattern]` — systemic issue across multiple entries (e.g., "many 〜的 entries lack notes on adjective vs adverbial use")
- `[wiki]` or `[wiki:page-name]` — content that belongs in the knowledge base
- `[article]` — possible expository article topic
- `[tooling]` — possible script or tool improvement
- `[skill]` — possible skill update needed
- `[entry]` — a specific entry that needs work beyond what fits a single session

## Template

```
## YYYY-MM-DD — comprehensive polish session NNN (entries XXXXX–YYYYY)
- [pattern] ...
- [wiki:topic-name] ...
- [article] ...
- [tooling] ...
```

---

## 2026-05-08 — comprehensive polish session 001 (entries 00001–00005)
- [pattern] Many verb entries have two `"conjugation":` top-level keys: a legacy stub (e.g., `{"type":"godan","ending":"る","stem":"…"}`) plus a full conjugation table appended later. JSON parsers silently take the last value, so the parsed data is correct, but the stub is dead text in the file. Confirmed on 00001_amaru, 00002_amu, 00004_aogu, 07924_aoru. Not present on 00006_aru. Likely affects most or all verb entries that pre-date the conjugation-table retrofit. Cleanup pass would be safe (drops are idempotent and the surviving data is already what tools use).
- [tooling] Add a one-shot pruning script that scans entries for duplicate top-level keys (especially `conjugation`) and removes the legacy stub form. Use raw text scanning rather than `json.load`, since Python silently collapses duplicates. A simple check: `grep -c '"conjugation":' entries/**/*.json | awk -F: '$2 > 1'`. Could live next to `add_conjugations.py`.
- [entry] 00004_aogu (扇ぐ) conflates two distinct verbs. Sense 1 is 扇ぐ (godan-gu, "to fan"). Sense 2 is 煽る/扇る (godan-ru, "to incite") — examples ex3, ex5, ex6 all use the form 扇る with okurigana る, which is the wrong conjugation class for the godan-gu headword. 07924_aoru already covers fan/incite/tailgate comprehensively. Recommended fix: remove sense 2 + the three sense-2 examples from 00004_aogu and let 07924_aoru carry the incite meaning. A cross-reference between the two has been added.

## 2026-05-08 — comprehensive polish session 002 (entries 00006–00025)
- [tooling] `build/verify_furigana.py` raises false positives on inline link metadata. After `FURIGANA_PATTERN.sub('', notes)` it still sees the kanji that follow the `→` in `⟦{時間|じかん}→時間：00468_jikan⟧` and reports them as unannotated. Notes that contain inline links to entries with kanji headwords therefore look broken when they are not. Suggested fix: also strip the `→…：…⟧` link tail (and the leading `⟦`) before counting kanji. The render pipeline doesn't render that tail, so it shouldn't count toward coverage.
- [pattern] The vast majority of older noun entries (in this 00006–00025 stretch, almost all of them) have linked example sentences but **unlinked notes**. Specifically, "COMMON COLLOCATIONS / RELATED WORDS / TYPES OF X / COMPOUNDS" bullet lists in `notes` typically still use bare `{kanji|reading}` without `⟦...⟧` wrappers. This is by far the dominant tier-1 polish task for these entries — far more than missing furigana or example issues. Every single entry 00007–00025 needed this work.
- [pattern] Many older noun entries also lack any `cross_references` to obvious neighbors that they explicitly mention in their notes (e.g., 00010_banchi → 住所/丁目/号; 00014_biyou → 美容院/美容師/健康; 00018_booto → 船/ヨット/カヌー; 00023_bushu → 漢字/画数). When these entries get inline-linked, the cross_references list often deserves to be populated at the same time. A possible tooling helper: scan an entry's notes for `→<id>⟧` link targets that are not already in `cross_references`/`prominent_see_also`, and surface them as suggested cross-refs.
- [entry] 00007_auto: フライ (fly ball, baseball sense) has no entry. The existing 11124_furai is "deep-fried food" only. Recommend expanding 11124_furai with sense 2 (baseball fly ball), since both are written フライ. Currently the example sentence uses a `noentry` marker, which is correct but a placeholder.
- [pattern] 09491_choume was missing the `cross_references` field entirely (not just empty). The schema seems to allow this but the build's symmetry checks may be silently skipping such entries. Worth confirming `check_consistency.py` flags entries that lack the field altogether so that they get back-link audits like everyone else.

## 2026-05-09 — comprehensive polish session 001 (entries 00026–00043)
- [pattern] The "older noun entries have unlinked notes" pattern from 0006–0025 continues unchanged through 0026–0043. Every single entry in this 18-entry run needed inline-link work in its notes (TYPES OF X, COMMON COLLOCATIONS, SIMILAR WORDS, RELATED TERMS, REGISTER lists). This is now confirmed dictionary-wide for at minimum the entire January–February 2026 creation cohort.
- [pattern] Many of these older entries also have under-populated `cross_references` even when notes mention obvious neighbors. Sometimes (00041_fudan referencing 通常) the cross-reference is structurally invalid — a `headword`/`reading` with no `target_id` field — and `validate.py` only emits a "Note", not an error. Suggested: a `validate.py --strict` mode that promotes "missing target_id" notes to errors, or a separate pre-merge check.
- [tooling] `verify_furigana.py` false-positive on inline link metadata after `→` continues. Same finding as 2026-05-08; not addressed yet. Fix is small (extend the strip pattern to consume `→…：…⟧`).
- [skill] `inline-word-links` skill could note that compound terms like チーズケーキ (25894_chiizukeeki), ダイヤモンド (11038_daiyamondo), 桜吹雪 (13137_sakurafubuki) often have dedicated entries even when their morphological components do not — and the polisher should prefer linking the whole compound when a single entry exists, rather than piecewise linking each kanji.
- [skill] `cross-reference-entry` skill should explicitly note that `"transitivity_pair"` is NOT a valid cross-reference type — schema accepts only `pair, synonym, antonym, keigo, related, see_also, contrast, homophone`. Verb transitivity pairs use `"type": "pair"`. Discovered this via validation failure on 00027_chijimu and could be saved by a one-line note in the skill.
- [entry] 00040_fubuki ex3 references しかける (04243_shikakeru) for the auxiliary "almost did" sense (`{遭難|そうなん}しかけた`). 04243 is glossed only as "to set up; to start; to challenge" — the suffix-verb sense ("almost ~", "be on the verge of ~ing") is a distinct grammatical use. The link still resolves to the right lemma but the gloss is misleading; 04243 may deserve a sense expansion or a separate grammar-pattern entry.

## 2026-05-09 — comprehensive polish session 002 (entries 00044–00073)
- [pattern] Same continuing pattern: older general/core/basic-tier entries from January 2026 routinely have unlinked notes. Confirmed across yet another 24-entry run — virtually every entry in this stretch needed tier-1 link coverage in notes (Common collocations, Similar words, Related terms, FORMS, etc.). The fix per entry takes 2-5 minutes once the lookup grep is open.
- [pattern] Two more broken cross_references (missing target_id) discovered in this run: 00065_genni → {実際|じっさい}に and 00069_gesui → {上水|じょうすい}. This pattern is not localized — it appears in entries created throughout January 2026. Confirms the urgency of a `validate.py --strict` flag (already noted on 2026-05-08 and 2026-05-09 session 001) or a one-shot scanner that lists every cross_references entry without target_id.
- [skill] `cross-reference-entry` skill (and CLAUDE.md project description) need correcting: the type `"formality_variant"` is mentioned but is NOT in the schema (`build/schema.json`). Schema-allowed values: `pair, synonym, antonym, keigo, related, see_also, contrast, homophone`. Hit this directly on 00072_gomen — used `related` as a fallback. Either the schema should add `formality_variant` (looks like an intended type) or the skill/CLAUDE.md should drop the reference.
- [pattern] Particle entries with extensive structured fields (00051_ga has `predicates_requiring`, `particle_contrasts`, `fixed_patterns`, `common_mistakes`) contain dozens of small Japanese phrase fragments embedded in template text that lack inline link coverage. These are not addressable by ordinary tier-1 work — they need a dedicated particle-polish session that treats each structured field as a mini example. Same likely applies to は (00079), を (00422), に (00314), で (00502), etc.
- [entry] 00051_ga: tier-1 partial only (notes section linked). Structured fields untouched. Worth a follow-up session targeted at the basic particles 00051, 00079, 00422, 00314, 00502, 00504, 00512.
- [pattern] Cross-reference back-link symmetry on thematic clusters is poor. School-types cluster (00055_gakkou ↔ 01055_shougakkou, 01083_koukou) had no back-links until this session. Likely true for family-terms, time-expressions, sibling/relative compounds, ceremony types. Could be a high-leverage one-shot batch-pass: pick a cluster, ensure every member references at least its main parent term.

## 2026-05-09 — comprehensive polish session 003 (entries 00074–00096)
- [pattern] Four entries in this run (00083 俳句, 00086 発揮, 00087 花火, 00088 判事) were already fully linked — the first time in five sessions that any entries needed zero changes. Suggests the cohort from around 00083–00090 received a prior polish pass. Subsequent sessions entering this range should expect occasional entries that need no work.
- [pattern] Particle entry 00079 (は) mirrors 00051 (が): it has `particle_contrasts`, `fixed_patterns`, `common_mistakes`, and `information_structure` fields containing dozens of bare Japanese phrase fragments that ordinary tier-1 polishing cannot address. This is now confirmed for both は and が. A dedicated particle-polish task is needed — one that iterates through each structured-field element and adds inline links to the phrase fragments.
- [entry] 00084_haitatsu had a split-compound bug: `{宅配|たくはい}{便|びん}` appeared as two adjacent furigana spans with no link, while 09534_takuhaibin (宅配便) exists as an entry. Fixed to use the compound as a single link target. Worth checking if other entries with 宅配便 have the same split.
- [tooling] A scanner that detects adjacent `{kanji|reading}` spans forming a known compound (i.e., concatenated they match a headword in the index) could catch split-compound issues like the 宅配便 case above. The word_id_lookup.json `by_headword` map is already the right data structure; the scanner just needs to test whether consecutive kanji spans resolve to a single compound entry.

## 2026-05-13 — comprehensive polish session 001 (entries 00115–00144)
- [entry] 00140_kaiteki ex5: `{替|か}えた` is incorrectly linked to `01089_kaeru` (変える - to change/alter) but should target `13399_kaeru` (替える - to replace/substitute). Pillow-replacement context requires 替える.
