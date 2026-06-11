# Tooling Backlog

**Last updated**: 2026-06-11 (added item 14 accuracy-review prompt: valid-tag list and semantically-plausible guidance)

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

**Update 2026-05-22**: Comprehensive-polish sessions 2026-05-21 (entries 02559–02583 and 02670–02696) confirmed the pattern extends throughout the entry range — 9 more entries identified (02560, 02567, 02568, 02574, 02576, 02582, 02688, 02693, 02696) all have the old-format stub followed by the full forms-array block. The pattern is likely pervasive across all verb entries created before the conjugation-table retrofit. A batch run of the proposed pruner would be a high-impact one-shot fix.

**Update 2026-05-23**: Session 005 (entries 03056–03077) confirmed 4 more entries (03057, 03064, 03072, 03077) with the same malformed duplicate-key pattern.

**Update 2026-05-25**: Session 011 (entries 03211–03230) confirmed 5 more suru-verb entries (03214, 03216, 03218, 03220, 03222) with lightweight stub + full table duplicates.

## 2. Fix verify_furigana.py false positives on inline links

**Source**: Comprehensive-polish 2026-05-08 session 002 and 2026-05-09 session 001

`build/verify_furigana.py` raises false positives on inline link metadata. After `FURIGANA_PATTERN.sub('', notes)` it still sees kanji in the `→` tail of inline links like `⟦{時間|じかん}→時間：00468_jikan⟧` and reports them as unannotated. The render pipeline doesn't render that tail.

**Suggested fix**: Extend the strip pattern to also consume `→…：…⟧` (and the leading `⟦`) before counting kanji. Small change.

**Resurfaced**: Comprehensive-polish 2026-05-12 session 009 (entries 00776–00799) confirmed the same false-positive pattern — kanji in inline link baseforms (after `→`) are not rendered to users and should not require furigana. Continues to generate noise for entries with many inline links.

**Resurfaced again**: Comprehensive-polish 2026-05-13 session 007 (entries 01014–01038) reports the same issue. Third independent confirmation across different entry ranges.

**Resurfaced (4th)**: Comprehensive-polish 2026-05-14 session 004 (entries 01181–01204) reports the same false-positive pattern after adding inline links with kanji base forms (e.g., `⟦{踏|ふ}む→踏む：01197_fumu⟧`). Fourth independent confirmation. The `→baseform：` portion is clearly the primary noise source.

**RESOLVED (2026-05-15)**: Comprehensive-polish sessions 001–007 (entries 01489–01511) fixed the issue by stripping `→[^⟧]*⟧` before the furigana scan in both `verify_furigana.py` and `find_missing_furigana.py`. Committed in PR #2346. No further action needed on this item.

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

## 5. Non-verb conjugation pruner + defensive guard in add_conjugations.py

**RESOLVED (2026-06-08).** Both parts of the fix shipped in the one-time non-verb conjugation sweep:

1. **Pruner built and committed** as `build/prune_nonverb_conjugations.py` (kept in the repo as a reusable audit tool). It dry-runs by default, skips `expression`-tagged entries for manual review unless `--include-expressions` is passed, and on `--apply` removes the `conjugation` field + stray `verb_class` tag and bumps `modified`. It cleaned **133 entries** (101 non-expression non-verbs + 32 reviewed expressions). All 32 expressions turned out to be multi-word idioms/proverbs/adverbial phrases or compound-ている forms — none was a single mis-tagged verb needing re-tagging — so all were stripped; the lone borderline keigo case (お会いする, 22190) was stripped and logged for curator review.

2. **Defensive guard added** to `build/add_conjugations.py`. **Root cause (sharper than "stale tag"):** the old guard was `if not any('verb' in p for p in ([pos] + pos_tags))` — the substring test `'verb' in p` is **true for `"adverb"`** (the string "adverb" contains "verb"), so adverbs passed the guard and a stray `verb_class: "godan-*"` then drove godan generation. The new guard is an exact-enum membership test against `{verb-godan, verb-ichidan, verb-suru, verb-kuru, verb-irregular}` over `metadata.tags.pos` only. Proven safe: `add_conjugations.py --force --dry-run --stats` would (re)generate tables for ~7,056 legitimate verbs and **zero** non-verbs, and re-running the retrofit after the sweep re-adds nothing.

`build/add_adjective_conjugations.py` was **already** correctly guarded (`if 'adjective-i' not in pos_tags: return None, None`) and had **zero** spurious i-adjective tables, so it needed no change.

**Source**: Wiki maintenance 2026-05-11 + 2026-05-12 entry exploration

The 2026-05-11 audit identified 12 adverbial onomatopoeia entries with spurious godan conjugation blocks. The 2026-05-12 follow-up widened the affected set to **130 entries** — 91 adverbs (mostly く-ending adverbial forms like 著しく, すごく, ますます), 31 expressions (反応を見る, 場を和ませる, …), 5 noun-adverbs (真っ二つ, 多く), 2 auxiliaries, 1 na-adjective+adverb. All 130 have a stray `verb_class` tag that triggered `add_conjugations.py` even though their `pos` contains no `verb-*` value.

**Two-part fix:**

1. **One-shot pruner** that finds every entry where `metadata.tags.pos` contains no `verb-*` value but the entry has a `conjugation` field, prints them for review, and on confirmation removes the `conjugation` field and the stray `verb_class` tag. 130 entries currently match. For the 31 expression cases the script should pause and ask: some idioms may legitimately want a conjugation block if their final verb is correctly classified, but most should not.

2. **Defensive guard** in `build/add_conjugations.py`: at the top of the per-entry generation, refuse to write if `metadata.tags.pos` doesn't contain `verb-godan`, `verb-ichidan`, `verb-suru`, `verb-irregular`, or `verb-kuru`. Emit a warning naming the entry. This prevents the same drift from regenerating if `verb_class` tags get rewritten in the future.

The same pattern applies to `build/add_adjective_conjugations.py`, which should require `adjective-i` POS.

**Connection**: see [Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Runaway automation" for the broader analysis. See [Cleanup Backlog](cleanup-backlog.md) → Priority 6 for the entry-level list.

## 6. Tag-drift detector

**SHIPPED (2026-06-09, partial)** — `build/check_tag_drift.py` is built (read-only). The deterministic checks are batch-ready and indexed in `backlog-queue.json`: `conjugation-no-verb-pos` (P6 standing guard), `politeness-unsupported` (P7), `sole-general` (P13). The `semantic-mismatch` heuristic (P11) runs but is **experimental / not batch_ready** — its keyword map is noisy (flags boat=transportation, school=building). Tightening that heuristic (richer maps or an LLM-judged pass) is the top systemic-fix follow-up. `check_artifacts.py` (P16/P15/P10/P4/P2) was also shipped the same day.

**Source**: Wiki maintenance 2026-05-11 entry exploration

A simple heuristic detector that flags entries whose tags don't match their content:

- `politeness` tag is `humble` or `honorific` but the notes contain none of the words "humble", "honorific", "polite", "keigo", "respectful" → tag likely misapplied or notes need expansion
- `semantic` tag list contains a value with no keyword overlap against the gloss or example translations (e.g., 02008_ikuratemo tagged `["furniture"]` for a grammatical pattern about quantity)
- POS tag list contains no `verb-*` but a `conjugation` field exists (the onomatopoeia case)
- POS tag list contains no `adjective-i` but the entry has i-adjective conjugation forms

Each check is cheap. A combined `check_tag_drift.py` script could emit a JSON report consumable by polish prompts. False positives are acceptable — the output is a manual-review queue, not an autofix.

**Scope**: Implement as a new build script (`build/check_tag_drift.py`) sibling to `check_consistency.py`. Possibly fold into `report.py` as a "TAG DRIFT" section.

**Related suggestion (2026-05-17 comprehensive-polish sessions 001–002)**: `validate_tags.py` could also be extended to flag semantic tags that conflict with the POS or gloss — e.g., `transportation` on a verb meaning "to get bored." This is simpler than a full tag-drift detector: a keyword-overlap heuristic between the semantic tag and the English gloss would catch the most egregious cases (the `furniture` / `transportation` / `electronics` / `clothing` mis-labels that keep surfacing). Could be a first-pass filter before the full item 6.

**Connection**: [Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Detection sketches" lists the specific check rules.

## 7. Polysemic kanji-variant overlap detector

**Source**: Wiki maintenance 2026-05-11 entry exploration

Some polysemic entries have a sense that is largely covered by a separate entry with a kanji-variant headword. Example: 00565_toru (取る) sense 2 ("to take a photo") duplicates the entirety of 00760_toru (撮る). The `prominent_see_also` link makes the relationship navigable, but the duplicated content drifts.

A detector would:
1. Walk through each polysemic entry's sense list
2. For each sense, check whether any cross-referenced or `prominent_see_also` target has the same reading and gloss family
3. Flag the overlap so a curator can decide: keep duplicated for browsing convenience, prune the sense, or convert the sense into a pointer

**Scope**: Lower priority than the tag-drift items above, but a useful long-term audit tool. See [Word Variants](../topics/word-variants.md) and [Handling Homographs](../topics/homographs.md) for the design context.

## 8. Furigana format validator (`check_furigana_format.py`)

**SHIPPED (2026-06-09)** — `build/check_furigana_format.py` is built as a read-only review queue (`--json`/`--summary`/`--severity`/`--range`). It classifies wrappers into `reading-truncated` (74 visible-bug truncations), `slash-reading` (130, Cleanup P12), `pure-kana`, `o-go-prefix`, `over-wrapped`, and `nested`, skipping kanji+katakana mixes (ヶ月, 筋トレ) to avoid false positives. Indexed in `planning/wiki/ideas/backlog-queue.json`; the Routine's systemic-fix mode drains it with per-entry verification.

**Source**: Wiki maintenance 2026-05-12 entry exploration

A companion to the existing `verify_furigana.py` (which checks only for *missing* furigana — i.e., kanji without a wrapper). The new validator checks whether wrappers are well-formed.

**Detection rules:**

For each `\{([^|}{]+)\|([^}{]+)\}` match in headword / examples / notes:

1. **Pure-kana wrapper**: kanji portion contains no kanji at all. Flag as either reversed (`{ところ|所}`), redundant (`{どんどん|どんどん}`), or content error (`{ある|ない}`).
2. **o/go-prefix inside wrapper**: kanji portion starts with `お` or `ご`. Suggest moving the prefix outside: `{お酒|おさけ}` → `お{酒|さけ}`.
3. **Okurigana inside wrapper, reading truncated**: length of reading portion is shorter than length of kanji portion (or reading does not phonetically span the surface). Highest-severity bucket — these display visibly wrong furigana on the live site.
4. **Okurigana inside wrapper, reading covers full word**: over-wrapped but renders correctly. Suggest canonical split.

**Output**: JSON list of `{entry_id, field, location, original, suggested_replacement, severity}` records for downstream polish prompts.

**Current state**: 859 instances across 624 unique entries detected by the heuristic. 68 of those are the high-severity truncated-reading case.

**Scope**: New script `build/check_furigana_format.py`, sibling to `verify_furigana.py` and `check_consistency.py`. Possibly fold a summary into `report.py`.

**Connection**: see [Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) for the full analysis and [Cleanup Backlog](cleanup-backlog.md) → Priority 9 for the planned remediation.

## 9. Headword furigana format fix script

**Source**: Wiki maintenance 2026-05-12 entry exploration

A subset of item 8 with stricter scope: just headwords. The malformed-headword set is small (22 entries) but high-impact because:

- `add_adjective_conjugations.py` skipped 01525_wakai (`{若い|わかい}`) — the basic-tier i-adjective 若い is currently on the live site **without conjugations** because of this.
- Similar entries may be silently absent from other generated indices.

**Scope**: A small script that loads each of the 22 entries, fixes the headword to the canonical form (move okurigana outside, split honorific prefix, etc.), validates the result with `validate.py`, and writes back. Then re-runs `add_conjugations.py` / `add_adjective_conjugations.py` on the modified entries to backfill the missing conjugation data.

**Affected entries** (full list from the audit): 17611_dowasure, 17879_uonome, 22070_hashiritsuzukeru, 22079_imamadedoori, 22061_jidouhikiotoshi, 22078_izendoori, 22058_ichidokiri, 22069_mizubukure, 22059_nomisugi, 22080_chakusouwoeru, 01514_mukae, 01525_wakai, 01516_mukou, 16520_makunouchibentou, 01420_shiawase, 01498_hikidashi, 01475_toori, 01462_chikaku, 01385_kimochi, 24896_kirimochi, 24593_kegare, 10668_konoha.

## 10. add_conjugations.py false-positive suru detection on godan verbs ending in する

**Source**: Comprehensive-polish 2026-06-04 session 013 (entries 05121–05141)

`add_conjugations.py` falsely detects godan verbs whose reading ends in する (e.g., すする 05127_susuru, "to slurp/sip") as suru compounds, generating malformed forms like `{啜|すす}るする`. The script checks for する at the end of the reading but doesn't verify whether the verb_class is explicitly `verb-suru` before applying suru-compound logic.

**Suggested fix**: Before applying suru-compound detection, check whether the entry's `verb_class` tag is explicitly `"godan-*"`. If so, skip the suru detection entirely — godan verbs ending in する (すする, くすくすする if it existed) are not suru compounds. This is a one-line guard near the top of the conjugation-generation function.

**Workaround**: Manual conjugation was required for 05127_susuru. Other godan verbs whose readings happen to end in する may also be affected.

## 11. Inline-link target-id resolution gate in validate.py (or pre-commit/CI)

**Source**: Routine v2 polish session, 2026-06-10 (high value — hit live this session)

`build/validate.py` (both `--id` and `--range`) validates an entry against the
schema but does **not** verify that the `entry_id` inside each inline link
`⟦surface→base：entry_id⟧` actually resolves to an existing entry. An entry whose
note linked to `04757_deeta` reported "Entry is valid!" even though 04757 is
クラウド (cloud) and the intended target was データ (03944). The wrong-ID link
renders as a dead/incorrect cross-reference on the live site, and nothing in the
normal validate → build pipeline catches it. The error was found only by an
ad-hoc script that resolves every `⟦…：id⟧` against the on-disk entry set.

**Suggested implementation**: A check that, for every inline link in
`headword`/`definitions`/`examples`/`notes`, extracts the trailing `：<entry_id>`
and confirms the file `entries/<range>/<entry_id>_*.json` exists (and, ideally,
that its reading/headword matches the link's base form). `noentry` is a valid
sentinel and must be skipped. Wire it into `validate.py` as a non-schema check
(so `make validate` and CI catch it), or add a dedicated
`build/check_inline_links.py` sibling and a pre-commit/CI gate. This closes a
whole class of silent linking errors that inline-link polishing can introduce.

**Scope**: A full-corpus scan would also surface how many such broken links
already exist; worth running once the gate is built.

## 12. review_runner.py `--pass deep --range` deep-reviews the whole range, not just flagged

**Source**: Routine v2 new-entries / accuracy-review sessions, 2026-06-10

In `build/review_runner.py`, `--pass deep --range A B` deep-reviews **every**
entry in `[A, B]` rather than only the entries the screening pass flagged.
`resolve_entry_ids()` returns the full range and bypasses
`get_flagged_entry_ids()`, so the deep (expensive) pass blows past its intended
scope: a 2026-06-10 accuracy-review run over 451–650 deep-reviewed 199 entries
instead of the ~45 the screen had flagged — a ~4× cost/time overrun.

**Routine §A already documents the workaround** ("deep covers only flagged"):
pass `--ids <flagged-list>` to the deep pass instead of `--range`. But the
`--pass deep --range` combination is a footgun that contradicts the screening →
deep funnel design.

**Suggested fix**: When `--pass deep` is combined with `--range`, intersect the
range with `get_flagged_entry_ids()` (or require `--ids`/`--all-in-range` to opt
into reviewing every entry). Emit a one-line notice of how many of the range were
flagged vs. skipped.

## 13. review_runner.py response-parsing robustness

**Source**: accuracy-review §A note (routine2) + Routine v2 sessions, 2026-06-10

Two distinct failure modes when an OpenRouter model returns something unexpected:

1. **Null-response crash (known, 2026-06-09)**: the runner can exit abnormally
   mid-pass on a null API response. Routine §A's documented resilience is to keep
   the per-entry results already written and continue — but the crash itself
   should be caught per-entry so one bad response doesn't abort the pass.
2. **Bare-array parse failure (2026-06-10)**: in the deep pass,
   `google/gemini-2.5-pro` intermittently returns a bare JSON **array** instead of
   the expected object, producing "Failed to parse response" for that entry.
   `gpt-4.1` still returns valid data, so the entry is reviewed single-model and
   the pass exits 0 — reduced redundancy, not a crash, but it silently drops one
   model's vote on those entries.

**Suggested fix**: Wrap per-entry response handling so any single
unparseable/null response is logged and skipped (entry reviewed by whatever
models did parse) rather than crashing or silently dropping. For the bare-array
case, accept a top-level array and coerce it to the expected shape (or take the
first element) before parsing. Both are small, localized hardening changes that
make multi-model review more reliable under the daily budget.

## 14. accuracy-review prompt: include valid-tag list and semantically-plausible guidance

**Source**: accuracy-review session 003 (entries 01151–01650), 2026-06-11; corroborated by accuracy-review sessions 001–002

Two related failure modes have accumulated across accuracy-review sessions, both producing high false-positive rates on the `tags` dimension:

1. **False "invalid tag" claims.** `google/gemini-2.5-flash` consistently flags valid semantic tags — `culture`, `religion`, `entertainment`, `business`, `nature`, and others — as "not in the schema" or "invalid." These tags each have 100+ uses in the dictionary and are defined in `build/schema.json`. The model asserts they don't exist rather than judging whether they are well-chosen for the entry in question. Accuracy-review session 003 observed this pattern on entries 01151–01650 and bulk-rejected ~120 such flags.

2. **Subjective "too narrow/too broad" flagging.** The reviewer also flags tags like `education`, `communication`, `work` as "too narrow for the headword," suggesting replacements like `cognition`, `general`, `action`. These suggestions are matters of editorial preference, not factual error — the current project convention explicitly accepts `general`, `descriptive`, `action`, and `expression` as legitimate fallback tags; replacing a more specific tag with `general` is usually a regression. Accuracy-review session 003 bulk-rejected ~10 of these per run.

Both patterns inflate the flags-per-applied ratio for the `tags` dimension, diluting the signal from the genuinely applicable catches (batch tag-drift, wrong-domain tags on anatomy entries, etc.).

**Suggested prompt improvements** for `build/review_accuracy.py` (tags dimension prompt):
- Provide a sample of the ~80 valid semantic tags (or the top ~30 most common), so the model cannot claim that widely-used tags are invalid.
- Add an explicit instruction: "Do not flag a tag as wrong merely because a different tag would also be defensible. Flag only clear factual mismatches between the tag's semantic domain and the headword's primary meaning. `general`, `descriptive`, `action`, and `expression` are valid fallback tags — do not flag entries for using them."
- For tags that appear valid but borderline, suggest "REJECT unless the tag is clearly wrong for the headword's primary meaning."

**Impact**: The `tags` dimension has the highest apply rate of any review dimension (~7–9%), but only ~9% of flags in session 003 were genuinely applicable (11 of 121). Better prompt scoping would reduce the bulk-rejection workload by roughly 10× while preserving the real catches.

## Related pages

- [Cleanup Backlog](cleanup-backlog.md) — patterns these tools would address
- [Entry Follow-ups](entry-followups.md) — specific entry fixes
- [Architecture and Build System](../project/architecture.md) — build script overview
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis of the tag-drift patterns that items 5 and 6 address
- [Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) — analysis of the wrapper-format patterns that items 8 and 9 address
