# Tooling Backlog

**Last updated**: 2026-06-23 (harvest: item 20 — tenth/eleventh no-op confirmation, regeneration proven not to help; item 21 — fifth screening truncation [174/500 over 8459–8632]; item 24 — 22/174 screen flags all FP except one お-prefix case [08474]; **new item 27** — promote unknown-semantic to a CI error/gate [8,698 dict-wide flags, accuracy-review can't outpace inflow]; **new item 28** — systemic-fix selector should skip scope-0 standing checks. Prior 2026-06-22: item 20 ninth confirmation, items 21/24/25)

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

**Update 2026-06-17 (proverb/yojijukugo signal)**: The 2026-06-16 accuracy-review run over 6140–6340 (which fixed 61 garbage-tagged entries; Cleanup P11 update 2026-06-17) suggested a cheap, high-precision addition to the `semantic-mismatch` heuristic: **proverbs and yojijukugo headwords that lack a `proverb`/`idiom` tag are almost always mis-tagged** (the run found idioms tagged `clothing`/`animal-insect`/`time-general`/`leisure`). A headword detectable as a four-character compound (kanji-only length 4) or marked as a saying, carrying a concrete-object semantic tag instead of `proverb`/`idiom`/`expression`, is a strong drift signal worth flagging deterministically — and complements the noisy keyword-map check rather than relying on it.

**SHIPPED (2026-06-17)** — two high-precision checks added to `build/check_tag_drift.py`, both read-only (`--json`/`--summary`/`--check`/`--range`/`--cohort`) and registered in `backlog-queue.json`:
- **`proverb-idiom-mismatch`** implements exactly the signal above (yojijukugo / POS `expression` / gloss idiom-marker, carrying a physical-object/creature domain with no keyword support, lacking `proverb`/`idiom`). **~93% measured precision.** Deliberately excludes tool/geography/weather/building/transportation/body-part from the flagged domain set — those legitimately apply to compositional 4-kanji compounds (懐中電灯, 都道府県, 直射日光), and including them dropped early drafts below the noise floor.
- **`concrete-noun-domain-mismatch`** flags a non-verb headword carrying ≥2 mutually-distant hard physical-object domains (横断歩道 → animal-mammal+clothing+transportation; 油絵 → body-part+tool). It is *structural* (counts incompatible domain clusters) rather than keyword-based, so it beats the `semantic-mismatch` noise floor: the broad keyword cross-domain variant measured ~5% precision (516 flags, mostly correct bench→furniture/school→building) and was rejected; the shipped structural version measured **~77% clear precision**.

The two checks are the batch-ready slices of P11; the keyword `semantic-mismatch` stays experimental, and the in-list-but-wrong-category long tail (朱肉→animal-mammal *sole* tag) remains accuracy-review territory. Remediation prompt: `prompts/fix_semantic_tag_drift.md`. Unit tests in `build/tests/test_detectors.py`. First batch fixed 35 entries (Cleanup P11 update 2026-06-17).

**Update 2026-06-21 (expand the `unknown-semantic` migration map for the 7000–8500 cohort)**: A 2026-06-21 accuracy-review run measured **73% out-of-taxonomy semantic tags (163/223 entries) across 7815–8037** — a different, denser creation cohort than the 2026-04-14 P11 batch, and the highest migration yield seen to date (Cleanup P20 update 2026-06-21). The drift families are large and mostly **1:1-mappable**, so the scalable fix is to extend `check_tag_drift.py`'s `TAG_MIGRATION` map (the `--check unknown-semantic` source) rather than drain it one accuracy-review pass at a time:
- **Free-form domain words** needing new 1:1 targets: `career`/`employment`/`personnel`→`work`(or `business`); `lifestyle`→`daily-life`; `place`→`geography`(context-dependent); `document`→`communication`; `accommodation`→`building`; `commerce`→`business`; `accounting`→`economics`; `logistics`→`transportation`. (Verify per entry — several are context-dependent.)
- **Underscore/space variants** (pure normalisation, mechanically safe): `daily_life`/`daily life`→`daily-life`; `Japanese_cuisine`/`Japanese cuisine`→drop (entries already carry `food`).
- **Body/health splits**: `body`→`body-part`; `sleep`→`health`; `injury`→`health`.

Once the map covers these, a deterministic+spot-checked systemic-fix sweep over 7815–8037 and the adjacent ~7000–8500 cohort would clear the bulk; per-entry verification on the context-dependent free-form mappings (`place`, `document`, `logistics`). Queued under the existing `unknown-semantic-tags` backlog item.

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

**Enhancement 2026-06-17 (no-pipe / unbalanced-brace detection)**: The shipped detector keys on `\{([^|}{]+)\|([^}{]+)\}` — a regex that **requires a pipe**, so it cannot see degenerate wrappers that contain no `|` at all (`{やけになる}`) or fields with an unbalanced/stray closing brace (`{投|な}げやりになる}`). Both were found in 06147_jiboujiki (a 2026-06 routine polish observation, now Cleanup P9 update 2026-06-17) and render as literal braces on the live site while passing furigana-*coverage* checks. Add two rules: (a) flag any `{` … `}` span whose interior contains no `|`; (b) flag any field whose `{` and `}` counts are unequal. Likely present across the same early-2026 yojijukugo batch (06140s).

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

**Update 2026-06-19 (deep furigana pass aborts after the first entry, exit 0)**: A
2026-06-18 accuracy-review furigana phase over 06926–07139 (session 007) hit a third,
worse variant: `review_runner.py --pass deep` queried both `openai/gpt-4.1` **and**
`google/gemini-2.5-pro` for the first flagged entry (06930), then **exited 0 with no
result files written and nothing logged** — the whole deep pass produced zero output and
gave no error. The screening pass (gemini-2.5-flash) ran fine for ~214 entries. This is
the silent-drop failure mode (#2 above) escalated to an *aborted pass*: a single
bad/slow gemini-2.5-pro response on entry one appears to be swallowed and to take the
loop down with it. The per-entry try/except hardening proposed above would fix this too
(skip 06930, continue the pass) — and the abort should at minimum be logged rather than
exiting 0. **Cross-reference**: the same session is the throughput observation under
item 21 (screening is ~10 entries/min, so a 518-entry furigana range cannot finish a
25-min wrapper regardless).

## 14. accuracy-review prompt: include valid-tag list and semantically-plausible guidance

**RESOLVED (2026-06-11)** — with a factual correction to this item's premise.
The reviewer prompt **already embedded** the full `VALID_SEMANTIC` list
(`review_accuracy.py` prompt v2); the "invalid tag" flags were the reviewer
correctly enforcing it against a dictionary whose de-facto tag vocabulary had
drifted (17,762 out-of-taxonomy instances — `schema.json` has no semantic-tag
enum, so "defined in schema.json" below was wrong). The fixes shipped: (1)
curator tag-policy decision — 30 established tags blessed into
`VALID_SEMANTIC`, near-duplicate migration map in `check_tag_drift.py --check
unknown-semantic`, long tail tracked as Cleanup Backlog P20; (2)
`review_accuracy.py` prompt v3 — flags out-of-list tags as migration
candidates, forbids "too narrow/too broad" substitutions between in-list tags,
restricts formality flags to unambiguous register contradictions; (3) the
standing adjudication rule in `prompts/routine2.md` §A (a not-in-list flag is
correct by definition — apply the migration). See
[Schema Tag Reliability](../topics/schema-tag-reliability.md) → "The
tag-vocabulary contradiction and its resolution."

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

## 15. Lint rule: unlinked 自動詞/他動詞 labels in notes fields

**Source**: 2026-06-11 comprehensive-polish session (entries 06038–06047)

Compound-verb notes from the 2026-04-10 creation cohort use `{自動詞|じどうし}` and
`{他動詞|たどうし}` in TRANSITIVITY lines without enclosing `⟦...⟧` inline-link wrappers.
The full scope of this pattern is unknown, but the observation estimates hundreds of
entries in the 06000–09000 range.

**Detection approach**: Scan all `*.json` entry files for the pattern
`{自動詞|` or `{他動詞|` (i.e. a furigana-wrapped form) that is *not* preceded by `⟦`.
A regex like `(?<!⟦)\{(?:自動詞|他動詞)\|` should identify all occurrences.

**Suggested implementation**: Either:
1. A new check in `build/check_artifacts.py --issue unlinked-transitivity-label`
   (consistent with the existing artifact-detection pattern), or
2. A standalone script `build/check_inline_link_gaps.py` that can also detect
   unlinked particles in Pattern lines and content words in COMMON PATTERNS bullets
   (the full three-sub-pattern problem documented in Cleanup Backlog P21).

The detector should emit JSON with entry ID, field name, and the unlinked string,
so the systemic-fix mode can work through the queue per-entry.

**Impact**: Would quantify the scope of Cleanup Backlog P21 and convert it from
`batch_ready:false` to `batch_ready:true` once the detector exists.

## 16. UTF-8 replacement-character repair script for corrupted furigana wrappers

**SHIPPED (2026-06-15)** — `build/check_mojibake.py` is built (read-only; `--json`,
`--summary`, `--range`, per-entry/-field U+FFFD counts with context windows) and indexed
in `backlog-queue.json` as `mojibake-ufffd`. A dedicated sweep reconstructed all 234
corrupted entries (1225 U+FFFD chars) to zero, and `build/validate.py` now carries a hard
U+FFFD guard (covered by `build/tests/test_validate_mojibake.py`) so CI rejects any future
entry that reintroduces the corruption. The notes below are retained for historical context.

**Source**: 2026-06-12 systemic-fix run (surfaced via `check_example_headword.py` output)

Approximately 246 entry files in the 20000–29000+ range (and possibly some earlier)
have UTF-8 replacement characters (U+FFFD, `�`) embedded in furigana wrappers —
either in the kanji component or the reading component of `{漢字|よみ}` markup.
Root cause is unknown but likely a batch-creation episode where UTF-8 multi-byte
sequences were corrupted (mojibake at write time). The `check_example_headword.py`
detector correctly flags these entries because the expected headword kanji can't be
found in the corrupted text.

**Detection**: Run `python3 build/check_example_headword.py --json` and filter for
entries where the issue is a FFFD character in a furigana wrapper (not a genuine
headword-absent example). Alternatively, grep: `grep -rl $'�' entries/`.

**Suggested repair approach**: For each affected file, identify the corrupted
character by context — the surrounding intact kanji characters plus the furigana
reading in the wrapper make the missing character unambiguous in most cases. Apply
manually or with a semi-automated script that proposes a fix for curator confirmation.
Scope: ~246 files, estimated 1–3 corrupted characters per file.

**Impact**: Fixes a silent data-quality problem that makes headword-search fail for
affected entries and causes `check_example_headword.py` to produce false positives,
obscuring genuine headword-absent examples.

## 17. accuracy-review prompt: suppress `general`-tag-noise false positives

**Source**: 2026-06-12 accuracy-review run (entries 03301–03800), 54.6% flag rate

The reviewer flagged 273 of 500 entries, far above the 20% noise threshold. The
primary noise family: the model flags any entry carrying the `general` semantic tag
as needing a more specific replacement, even though `general` is a valid `VALID_SEMANTIC`
tag and the standing adjudication rule in `routine2.md §A` says to reject "too
narrow/too broad" substitutions between in-list tags. One run's bulk-reject tally was
180 flags from this family alone (`"family: too-broad/too-narrow in-list tag
substitutions (general→specific, descriptive→evaluation, etc.)"`).

A secondary noise family: `formal` tags on words whose notes don't explicitly
contradict the label — many of these are genuine applies, but there are false positives
when the model assumes a word is neutral without reading the notes.

**Root cause**: Prompt v3 (2026-06-11) added "do not flag too-narrow/too-broad
substitutions between in-list tags", but the reviewer still treats `general` as a
sign of under-tagging rather than a legitimate editorial choice. The standing
instruction is not strong enough to suppress the pattern.

**Suggested fix**: Add to the `review_accuracy.py` tags-dimension prompt:
- Explicit exception: "Do not flag entries tagged `general`, `descriptive`, `action`,
  or `expression` as needing a more specific tag. These are valid fallback tags.
  Flag only when the tag's domain is factually wrong for the headword."
- For `formal` tags: "Flag `formal` only when the entry's own notes or example
  sentences contradict the formal-register label; do not infer formality from word
  frequency or perceived neutrality alone."

**Impact**: Reduces per-run adjudication cost by ~180 bulk rejections (removing noise
that currently dominates the review queue). Precision on the `tags` dimension would
increase from ~30% to potentially >60% once the `general`-noise family is suppressed.

**Update 2026-06-13**: The same `general`-tag noise pattern persists in the 03801–04300
accuracy-review run: 246/492 entries (50%) flagged, with 252 tag flags of which 222
(88%) were `general` flagged as "too broad." The broader 285-flag run was bulk-rejected
(`reviews/decisions.jsonl`). Two genuine furigana fixes were found via screening (0%
false-positive rate for screening vs. ~88% for the tags dimension on this range). The
proposed prompt fix remains unimplemented; the noise family is now confirmed across the
03301–04300 range (two consecutive 500-entry runs, consistent ~50% flag rates).

**Update 2026-06-14**: The 4801–4982 accuracy-review run shows the noise now appears at
**error severity**, not just warn: 73 error-severity tag flags across 182 entries (42%
of entries), but only 13 were genuine wrong-category AI-artifact mis-tags (`body-part`
on 手当, `geography` on 容量/発信, `animal-mammal` on 焼き物/まな板, `leisure` on 反応/合唱)
plus 1 not-in-list (`economy`→`finance`). The other ~60 were the same "`general` is too
broad, use plant-tree/finance/food/society" in-list narrowness nits — but emitted as
`error`, which defeats the existing "work every error-severity flag individually" triage
rule (it forces full per-item adjudication on what is known noise). This sharpens the
fix: the prompt needs not only the fallback-tag exception already proposed, but an
explicit **severity rule** — "a more-specific in-list tag existing is never an `error`;
reserve `error` for tags whose domain is factually wrong for the headword." Estimated to
cut tag-flag volume ~80% and, more importantly, restore the error/warn severity split as
a usable triage signal. Furigana screening over this already-polished range was again 0%
precision (all 9 screening + deep flags were rendaku/compound-onyomi false positives),
consistent with the documented note.

**Update 2026-06-15**: Two more accuracy-review runs confirm the `general`-noise family
is now the steady-state dominant cost on already-polished mid-ID ranges:
- **4301–4800**: 44% flag rate (221/500). Breakdown: "`general` too broad" (71, all
  in-list nits), formality tags (27), misc narrowness (95). Genuine errors were
  animal-taxonomy mismatches (`animal-fish` for squid/octopus/crab, `animal-insect`
  for frog and 〜長), wrong-category (`geography`/`time-general` for 発電; `economy` for
  損得), and factual gloss errors (recyclable for 再生可能, leotards for タイツ,
  rolling-vs-lying for 寝転ぶ). Applied 18, rejected 211.
- **4983–5482**: ~120/496 entries flagged on the same `general`-too-broad family with
  in-list substitution suggestions.
Across both runs the genuine-error rate sits at ~4–8% of flags while the `general`/
narrowness noise dominates adjudication, exactly the profile the proposed prompt fix
(fallback-tag exception + severity rule) targets. The fix remains unimplemented; the
noise is now confirmed continuous across the 03301–05482 band.

**Update 2026-06-16**: A 2026-06-15 accuracy-review observation extends the band
upward into **05521–05703**: 39% of entries flagged (72/183), but most were
`general`/`descriptive`-too-broad narrowness substitutions between in-list tags
(rejected per the semantic-tag policy). The genuine-error fraction stays in the same
~4–8% range. The contributing run also recorded its bulk rejections as one aggregated
§C line (`family: in-list narrowness/defensible substitutions`, n=38). The noise family
is now confirmed continuous from 03301 to ~05700 — five consecutive ~500-entry sweeps
with the same ~40–55% flag rate driven by in-list narrowness nits. This is the
fifth independent confirmation; the fallback-tag exception + severity rule remains the
single highest-leverage unshipped reviewer-prompt fix.

**Update 2026-06-17**: A 2026-06-16 accuracy-review run over **5704–6139** flagged
137/436 entries (31%) — above the 20% noise threshold but lower than the 40–55% of the
03301–05700 band, because this higher range carries more genuine wrong-category tags
(see Cleanup P11 update 2026-06-17). The dominant noise family was again "in-list
semantic tag too broad/narrow" (general→specific domain), ~60 flags rejected per policy.
The run reiterated that the `tags` prompt should suppress in-list narrowness
substitutions and flag only out-of-taxonomy or genuinely-wrong-domain tags — the precise
slice where this run's precision was high. Sixth consecutive confirmation; fix still
unshipped.

**Update 2026-06-18 (signal/noise flips on *un-polished* ranges — fix is still worth shipping)**: Two 2026-06-17 accuracy-review sweeps over **6341–6540** (50 applied) and **6541–6840** (104 applied of 300) show the opposite profile from the 03301–05700 band: these *un-polished* ranges carry genuine wrong-category tags at error severity, so the `tags` apply rate jumped to **51.2%** across runs 61–77 (285 applied of 557 — see [Quality Metrics Trend](../topics/quality-metrics.md)). This is **not** evidence the noise family is gone — it is range-state dependence (genuine catches above the polish frontier; `general`/narrowness noise on already-polished ranges). The prompt fix (fallback-tag exception + severity rule) is still the right change: it would suppress the noise on polished ranges *without* touching the genuine wrong-domain catches on un-polished ones (those are out-of-domain, not in-list narrowness). Shipping it would let a proactive `tags` sweep of 6157–~7500 (Cleanup P11 update 2026-06-18) run at high precision instead of dragging the `general`-noise tail.

## 18. check_example_headword.py false-positive reduction

**Source**: 2026-06-14/15 routine runs (example-headword-missing systemic-fix lane)

Once the clean-entry frontier is exhausted (P19 `batch_ready: false`), the
`build/check_example_headword.py` queue is dominated by detector false positives rather
than genuine cases. Two families:

1. **U+FFFD-corrupted entries** — the kanji headword was mojibake, so it could never
   match its examples. **Now moot**: tooling-backlog item 16 shipped (`check_mojibake.py`
   + a one-time repair to zero U+FFFD), so these no longer pollute the queue, but the
   detector should still defensively skip any entry containing U+FFFD.
2. **Legitimate orthographic false positives** — kana/katakana orthography of the
   headword (ごちそう for ご馳走, ヤギ, シミ, カツオ, カキ, しわ寄せ), documented compound
   forms (退職届/婚姻届 in 届け), the radical sense (うかんむり in 冠), and ～-prefix
   headwords (〜時) whose plain-kanji examples the matcher can't bind.

**Suggested fix**: Teach the detector to (a) skip entries containing U+FFFD, (b) strip a
leading ～/〜 from the headword before matching, and (c) treat katakana of the reading as
a headword match for animal/seafood/loanword nouns. Estimated to cut the residual queue
from ~31 entries to near zero, which would let the P19 lane re-open to find genuine
verb-form-misparse cases (the 00472 仕様 / 22875 出回り class) without manual de-noising.

## 19. Stale-`noentry` inline-link detector

**Source**: 2026-06-14/15 routine runs (multiple stale-`noentry` sightings)

Inline links written as `⟦surface→base：noentry⟧` are correct at creation time when no
entry exists, but they become stale once an entry is later created for that word — the
link silently stays `noentry` instead of pointing at the now-existing ID. Confirmed
stale cases this week:
- 00012_batsu notes mark バツニ as `noentry`, but 27329_batsuni now exists.
- 05528/05530 had `⟦潰える…：noentry⟧` / `⟦大志…：noentry⟧`, but 28923_tsuieru and
  28925_taishi now exist.
- (Earlier: 05501_shashinka カメラマン→`noentry`, now 28387_kameraman — Entry Follow-ups.)

**Detection approach**: For every `⟦…：noentry⟧` span, extract the base form and look it
up in `build/word_id_lookup.json` (`by_headword` and `by_reading`). If a unique entry
exists, the marker is stale and should be re-resolved to that ID. This is a cheap,
fully-mechanical, self-healing scan — a strong systemic-fix candidate because the fix
(swap `noentry` for the resolved ID) is deterministic and low-risk where the lookup is
unambiguous.

**Suggested implementation**: A new `build/check_noentry_links.py` (read-only `--json`
review queue) sibling to `check_inline_links.py` (proposed in item 11), emitting
`{entry_id, field, surface, base, resolved_id}` for each stale marker. Ambiguous lookups
(multiple candidate IDs for one reading) go to the queue for per-entry judgment rather
than auto-resolution.

## 20. Notes-priority ranking excludes recently-polished / structurally-passing entries

**Source**: 2026-06-14 routine polish session 004 (priority "notes" lane)

The `prioritize_polishing.py` "notes" ranking surfaced high-frequency basic/core
adjectives (00469_matsu, 00039_erai, 01112_tsurai, 01133_kusai, 00585_akai) that came
back **already fully polished** — complete inline links, valid in-list tags,
well-structured notes. 5 of 7 priority entries needed no changes, which forced a
mid-run priority regeneration + cursor reset. The notes-quality ranking appears to go
stale for long-settled entries: a once-thin note that has since been expanded still
ranks high because the score isn't recomputed against the current text, or the score
threshold admits notes that are already adequate.

**Suggested fix**: Exclude from the notes priority ranking any entry whose `modified`
date is recent (e.g. within 30 days) **or** whose note already passes a structural
adequacy threshold (has the expected sections / minimum length / link density), so the
lane targets genuinely thin notes instead of re-surfacing settled ones. The Routine's
polish mode already regenerates + resets when >half the priority-lane entries need no
changes (routine2.md §2), but that is a reactive backstop; filtering at ranking time
would stop wasting the priority lane's budget on no-op entries in the first place.

**Update 2026-06-17 (structured-field blind spot)**: A 2026-06-16 routine polish run
exposed a second, sharper cause of the same no-op problem: `score_note_quality.py` /
`prioritize_polishing.py` rank **structured particle/function-word entries** at the very
top of `priority/notes.txt` — が (00051, score 30), は (00079, score 35), ぐらい (02900,
score 50) — even though those entries are *comprehensive*. Their content lives in
dedicated structured fields (`predicates_requiring`, `particle_contrasts`,
`information_structure`, `fixed_patterns`, `common_mistakes`) that the scorer ignores
while measuring only the `notes` string. Result: the priority lane keeps surfacing
already-excellent function-word entries as "worst notes" (4 of 7 priority entries needed
no changes for this reason in the originating run). **Fix**: have the scorer credit
those structured fields toward the note-quality score, or skip particle/function entries
that populate them. This is complementary to the recency/adequacy filter above — both
should land together so the notes lane stops re-surfacing settled and structurally-rich
entries.

**Update 2026-06-18 (third and fourth confirmations — same particle set keeps recurring)**: Two more 2026-06-17 routine polish runs hit the identical no-op pattern: one checked 8 priority-lane entries (00051_が, 00079_は, 00733_まずい, 02900_ぐらい, 00740_おいしい, 00484_も, 00864_こわい, 00025_ちいさい) and found **7 of 8 needed no changes**; the other found **3 of 4** clean (が 00051, は 00079, まずい 00733 again). Both runs were forced into the reactive regenerate-priorities + cursor-reset backstop. The same handful of closed-tier particle/adjective entries (が, は, まずい, ぐらい) keep re-surfacing at the top of `priority/notes.txt` across runs, wasting ~40% of the priority lane's budget each time. This strengthens the case to **exclude the closed basic/core particle+function set from the notes ranking entirely** (the cleanest fix, since those tiers are closed and their structured fields are already comprehensive) in addition to crediting structured fields toward the score.

**Update 2026-06-18 (a concrete scorer bug behind the no-ops, not just staleness)**: A
2026-06-18 routine polish run traced the recurring top-of-list no-ops (00025_chiisai,
00530_chikai, 00533_osoi, etc. — all already clean) to **two false signals inside
`score_note_quality.py` itself**, distinct from the staleness/structured-field causes
above:
1. **`has_bare_kanji` counts inline-link baseforms as un-furiganaed kanji.** The baseform
   inside an inline link — e.g. the `小さな` in `⟦{小|ちい}さな→小さな：02913_chiisana⟧` — is
   matched as bare kanji, so **any entry with inline links in its notes scores
   furigana=0**, the exact opposite of reality (links are the polished state). The scorer
   should strip `⟦…⟧` link baseforms (the `→base：id` segment) before the bare-kanji check.
2. **The `required_sections` matcher misses valid section headers**, giving required=0 to
   notes that *do* carry the expected sections — penalising well-structured notes for a
   matcher gap.
Together these systematically depress the scores of fully-polished entries, so the top
~30 notes-priority entries are exactly the ones that need no work. This is the **root
cause** the recency/structured-field filters above only paper over: fixing the two scorer
bugs would clean the ranking at the source. Smallest high-value fix in this item.

**Update 2026-06-19 (fresh priority file, still all no-ops — now on basic/core content
words)**: A 2026-06-19 routine polish run worked priority-lane line 57 and found **all 8
eligible entries already fully polished** (01092 億, 02350 良い, 00642 金曜日, 01003 隣,
01006 腕, 02006 ばかり, 02007 まま, 00765 優しい) — complete inline links, good notes,
examples — needing **zero** changes. This was *not* a stale-file artifact in the usual
sense (the run regenerated priorities + reset the cursor as the §2 >half-no-op backstop
requires), and the entries are ordinary basic/core content words, not the
structured-particle blind spot of the 2026-06-17 update. The observing run's diagnosis
matches scorer-bug #1/#2 above: these are settled basic/core entries the scorer still
ranks as "worst notes" on note *length* while the notes are actually complete. Net: the
notes-priority ranking remains low-yield even *immediately after regeneration* until the
two `score_note_quality.py` scorer bugs are fixed — the recency/structured-field/closed-set
filters do not help here because these are open-tier content words that genuinely look
thin to the length heuristic but are not. Reinforces that the scorer-bug fix (strip
inline-link baseforms before the bare-kanji check; fix the `required_sections` matcher) is
the binding fix, not just the ranking filters.

**Update 2026-06-20 (seventh confirmation — 6/6 no-op, now juxtaposed against the real frontier gap)**: A
2026-06-20 routine polish run worked **6 priority-lane entries (00025 ちいさい, 00533 おそい, 00304 なんでも,
01092 億, 00642 金曜日, 01003 隣) and found all 6 already complete** (full inline links, example sets, notes,
cross-refs) — zero changes, the seventh consecutive run to hit this. What sharpens the case this time: the
*same* run's frontier lane found 06190–06196 and 06204–06209 with **zero** inline links (see
[Cleanup Backlog](cleanup-backlog.md) → P21 update 2026-06-20). So the priority lane spent ~40% of its budget
re-confirming settled basic/core entries while the genuine tier-1 deficit — inline-link coverage on the
general-tier frontier — sat untouched in the frontier lane, invisible to the notes ranking. Clearest
single-session evidence that the notes-quality scorer is anti-correlated with real need; the scorer-bug fix
remains the binding fix.

**Update 2026-06-21 (eighth confirmation — two more 6/6 no-op runs on the same closed-tier set)**: Two
2026-06-21 routine polish runs each ran their priority/notes lane 6/6 no-op on the same already-polished
basic-tier words (へ, 小さい, 遅い, 何でも, 隣, 腕) — full inline links, cross-refs, conjugation tables, needing
zero changes — while both runs' frontier lanes found genuine zero-link gaps (06210–06213 compound verbs and
the 06214+ proverb/yojijukugo block; [Cleanup Backlog](cleanup-backlog.md) → P21 update 2026-06-21). This is
the eighth consecutive priority-lane no-op session and again juxtaposes the wasted ~40% priority budget against
the untouched real frontier deficit. No new diagnosis — pure reinforcement that the two `score_note_quality.py`
scorer bugs (strip inline-link baseforms before the bare-kanji check; fix the `required_sections` matcher), not
the ranking filters, are the binding fix. The observing runs additionally suggest a recency/coverage guard in
`prioritize_polishing.py` so heavily-polished basic entries stop dominating the lane — the same closed-set
exclusion recommended in the 2026-06-18 update.

**Update 2026-06-22 (ninth confirmation — concrete header names behind scorer-bug #2)**: Two more 2026-06-21
routine polish runs ran their notes lanes effectively all-no-op — one found **all 12 eligible priority entries**
(一緒, 小さい, 遅い, 何でも, 金曜日, 隣, 腕, ばかり, まま, 優しい, 好き, 青) already fully linked, furigana-complete,
and well-structured, needing zero changes. The sharper new detail is on **scorer-bug #2 (the `required_sections`
matcher gap)**: `score_note_quality.py` only credits the literal `usage`/`functions` keyword its POS template
expects, so well-formed adjective/particle/noun notes that use **descriptive section headers** — `TWO MEANINGS`,
`FORMS`, `DEGREES OF LIKING`, `PATTERN 1/2/3` — score **50–58 despite being complete and correctly formatted**
(00025 ちいさい, 00533 おそい, 02355 すき, 00765 やさしい, 02006 ばかり, 02007 まま). The concrete fix is to broaden
`find_sections` variant matching — treat any header followed by a bulleted pattern/meaning list as satisfying the
`usage`/`functions` requirement — so the priority ranking stops penalising descriptive-but-complete notes. This is
the same scorer-bug #2 as the 2026-06-18 update, now with the exact header strings that trip the matcher.

**Update 2026-06-23 (tenth/eleventh confirmation — regeneration is now proven not to help)**:
Two more routine polish runs ran their priority/notes lanes effectively all-no-op: a
2026-06-22 run found **6/6 eligible** clean (02848 一緒, 02947 低い, 00025 小さい, 00533 遅い,
00304 何でも, 00642 金曜日) and a 2026-06-23 run found **all 8 eligible** clean (03095 など,
02947 低い, 00025 小さい, 00533 遅い, 00304 何でも, 03093 だけ, 00642 金曜日, 01003 隣) — full
inline links, furigana-complete, well-structured, needing zero changes. The 2026-06-23 run
followed the §2 >half-no-op rule and regenerated priorities + reset the cursor, but noted
this is now a **near-no-op corrective**: the file had *already* been regenerated the day
before (2026-06-22), and the same unchanged basic/function entries re-top the ranking each
time because the scorer re-derives the same low scores from unchanged text. This is the
direct confirmation of the 2026-06-19 update's point — regeneration does not break the loop
because the binding defect is the `score_note_quality.py` scorer (strip inline-link
baseforms before the bare-kanji check; broaden the `required_sections` matcher), not the
ranking freshness. Eleventh consecutive priority-lane no-op session; the scorer-bug fix
remains the only thing that will break it.

## 21. Chunk the review/screening runners to fit the session timeout

**Source**: 2026-06-16 routine runs (systemic-fix self-check + furigana accuracy-review)

`review_runner.py --pass screening` is killed by the session's `timeout` wrapper on
large ID sets, because gemini-2.5-flash runs ~9 s/entry and the runner processes one
entry at a time with no internal checkpoint against the wall clock. Two confirmed
truncations this week:
- A systemic-fix self-check over **118 IDs** was killed at ~59/118 by the 540 s wrapper.
- A furigana screen over **6140–6650** was killed at 580 s having covered only
  6140–6223 (84 entries).

In both cases the partial results that *were* written are usable (the runner is
incremental), and all flags from the truncated portions were the documented furigana
false-positive families (rendaku-in-compound, okurigana/partial-reading "correct by
design", screener input-truncation artifacts), so no coverage was lost in practice — but
the abnormal exit is noise in the logs and risks a half-finished pass being mistaken for
a complete one.

**Suggested fix (any of):** (a) have callers (routine2.md §4 self-check, §A furigana
pass) **batch into ~50–100-ID sub-ranges** and loop, so each invocation finishes well
inside the timeout; (b) add a `--max-seconds` / batch-size guard inside `review_runner.py`
that stops cleanly and prints how far it got, instead of being SIGKILLed; (c) raise the
wrapper timeout for screening-only passes. Option (a) is the smallest change and is
already the documented workaround in `polishing/observations.md`.

**Update 2026-06-18 (third truncation — §4 self-check now also affected)**: A 2026-06-17
systemic-fix run's §4 furigana self-check screened only **24 of 51** changed entries
before the 500 s background timeout (a 2026-06-16 run similarly got 59/118). The serial
per-entry calls to gemini-2.5-flash dominate. This is the third confirmed truncation in a
week and the second hitting the §4 self-check specifically — the self-check is the
highest-value review pass (49.6% all-time precision) and should not be the one silently
cut short. Option (a) — have §4 batch its changed-ID list into ~25-ID sub-ranges and loop
— is the smallest fix and would make a typical systemic-fix batch's furigana self-check
complete. Partial results are still written per-entry, so coverage is incomplete but not
lost.

**Update 2026-06-19 (measured screening rate ⇒ size furigana ranges to ~200/run)**: The
2026-06-18 accuracy-review furigana phase (session 007) puts a number on the screening
throughput: gemini-2.5-flash screened ~214 entries before the wrapper limit at **~10
entries/min**, so a single furigana screening invocation should be sized to **~200 IDs**
to finish inside a ~25-min wrapper. This is the §A-furigana-pass counterpart to the §4
self-check ~25-ID batching above (option (a)): the binding rate is the same serial
per-entry gemini-2.5-flash latency. Concretely, the selector / §A range sizing for the
furigana screen should cap at ~200 IDs/run rather than the ~400–600 used for the
combined screening+accuracy budget math, because the furigana screen alone is the
throughput-bound part.

**Update 2026-06-22 (fourth truncation — measured ~6 s/entry, cursor stranded mid-range)**: A 2026-06-22
accuracy-review furigana phase sized its screening range to **8238–8838 (601 IDs)** and was **SIGKILLed by the
25-min wrapper after completing only 221/601 entries** (~6 s/entry against google/gemini-2.5-flash in this
environment — faster than the 2026-06-19 ~10 entries/min figure but still far short of 601 IDs in 25 min).
Per-entry results for the 221 covered IDs were kept and used, and the **cursor advanced only to 8459** (the
covered frontier), so no work was lost — but the run had to leave ~380 IDs of the intended range unscreened. This
is the fourth confirmed truncation and reconfirms the 2026-06-19 prescription exactly: **size a single furigana
screening invocation to ~200 IDs** (option (a)), which at ~6 s/entry finishes in ~20 min, comfortably inside the
ceiling. The selector / §A range sizing for the furigana pass should cap at ~200 IDs rather than the ~400–600 used
for the combined screening+accuracy budget math.

**Update 2026-06-23 (fifth truncation — same ~6–7 s/entry profile)**: A 2026-06-22
accuracy-review furigana phase over **8459–8632** was **killed at 174/500 by the 20-min
wrapper** (~7 s/entry against gemini-2.5-flash), the fifth confirmed truncation in two
weeks. Per-entry results for the 174 covered IDs were kept and used. Reconfirms the
~200-IDs-per-furigana-screen sizing prescription exactly — no new diagnosis, pure
reinforcement that the §A furigana range should cap at ~200 IDs rather than 500.

## 22. Particle structured-field furigana-completeness sweep

**Source**: 2026-06-17 routine polish session (priority lane, 00484_も)

`verify_furigana.py` correctly catches unwrapped kanji inside particle **structured
fields** — 00484_も had 数量 / 一 unwrapped in both `fixed_patterns` and `notes` — but
these slip past casual human review because the example/notes *prose* looks complete, so
the gap is only found when the verifier is run on the specific entry. The structured
fields particle entries carry (`fixed_patterns`, `particle_behavior`,
`question_word_patterns`, `predicates_requiring`, `particle_contrasts`,
`common_mistakes`) contain many short Japanese phrase fragments that were never furigana-
checked at creation time.

**Suggested implementation**: A targeted sweep that runs the furigana-completeness check
over *every* string value inside the structured fields of all particle/function-word
entries (not just `examples`/`notes`), and emits a JSON queue of `{entry_id, field, path,
unwrapped_kanji}`. This is a scoped extension of `verify_furigana.py` /
`find_missing_furigana.py` to recurse into the structured-field subtree rather than only
the top-level prose fields. Low entry count (the closed particle set is ~30 entries) but
high per-entry value, since these are the most-consulted entries in the dictionary. The
fix per hit is mechanical (wrap the bare kanji), so once the queue exists it is a clean
systemic-fix or one-shot batch.

## 23. Candidate-pool pre-filter for corpus harvesting / manage_candidates

**Source**: 2026-06-17 + 2026-06-18 routine new-entries sessions (recurring)

`candidate_words.json` is dominated by low-quality corpus-harvest noise: across the
oldest ~160 candidates and mid-range samples, **fewer than ~10%** are well-formed
standalone learner vocabulary. The junk families are predictable and mechanically
recognisable:

- **Bare numeral + counter** forms (二百, 三歳) — compositional, not lexical.
- **Single-suffix productive derivations** (〜化, 〜性, 〜率, 〜器 compounds) — productive
  morphology, inferable from the base.
- **Place names and proper nouns** (incl. transcriptions like スポンジボブ).
- **Transcription typos / errors** (怒燥 for 怒涛, アンパッサン glossed "ice cream sundae").

The only consistently good candidates are the recent **"seen in entry"** additions. The
practical effect is that new-entries runs find few genuinely useful headwords beyond the
seen-in-entry set (5 useful candidates in one 2026-06-17 run; only the seen-in-entry ones
in another), forcing them to either pad from junk or under-produce against the ~20 target.

**Suggested implementation**: A pre-filter in `manage_candidates.py add` (and any corpus-
harvesting path) that **rejects or quarantines** (a) bare numeral+counter forms, (b)
single productive-suffix derivations where the base is itself a likely entry, and (c)
obvious proper nouns / non-Japanese transcriptions. Combined with a one-time cleanup pass
over the existing Feb–May 2026 corpus/brainstorm batches, this would raise the candidate-
pool signal substantially and let new-entries runs hit their target without padding. **Note**:
the curator restock is the complementary human-side fix (see Open Issues → candidate-pool
quality); the pre-filter keeps the pool from re-accumulating noise after a restock.

**Update 2026-06-18 (two more junk families to add to the filter)**: A 2026-06-18 routine
new-entries run (which curated 13 quality words rather than padding from the oldest-first
junk) named two families not yet in the reject list above: **non-lexical compound
fragments** (倍率差, 機成り, 些道, 多角的一面) and **transparent decomposable compounds /
ad-hoc phrases** (給水槽, 排水処理, あらかじめ準備する, 用につき) — both inferable from their parts
and not standalone learner headwords. The pre-filter's productive-suffix rule should be
widened to a general "decomposable compound" / "ad-hoc phrase" heuristic. Reconfirms the
<10%-genuine signal rate and the throughput hit (a strict oldest-first run would have
produced low-value entries).

**Update 2026-06-21 (two consecutive runs skipped the fallback lane entirely)**: The
2026-06-20 and 2026-06-21 new-entries runs **both abandoned the oldest-unprocessed
fallback lane** and stayed under the ~20 target because the pre-March candidate vintage
(Feb-2026, e.g. C06045 権使, C08195 些道, C09223 個尊, C10277 怒燥, plus 火虫/黒手) is
dominated by typos, dialect fragments, proper nouns, and OCR artifacts — the same
<10%-signal families as above. The "seen in entry" pool was uniformly high quality in
both runs. This is the throughput cost made concrete: with the fallback lane unusable,
new-entries production is now effectively capped at the seen-in-entry inflow. Both the
**pre-filter** (this item) and a **one-time curator triage/restock** of the pre-March
batches (Open Issues → candidate-pool quality) are needed; the observing runs explicitly
recommend running `clean_up_candidates_list.md` to purge the pre-March junk so the
fallback lane becomes usable again.

## 26. accuracy-review prompt: embed the valid `formality` enum (formal/neutral/informal/vulgar)

**Source**: 2026-06-20 routine new-entries self-check (gemini-2.5-flash, `tags` dimension)

A §4 self-check flagged 炭水 with `formality: "informal"` as an error and suggested
**`"colloquial"`** as the replacement — but `colloquial` is not a valid `formality` value
(schema enum: `formal` / `neutral` / `informal` / `vulgar`); it reads more like a domain
label. This is the **formality-field analogue of the now-resolved item 14 `VALID_SEMANTIC`
gap**: the reviewer's `tags`-dimension prompt embeds the valid *semantic* vocabulary (item
14, prompt v3) but does **not** embed the valid *formality* enum, so the model invents
out-of-enum formality suggestions that can never be applied. Each such flag is a guaranteed
false positive that still costs adjudication time.

**Suggested implementation**: Embed the four-value `formality` enum (and likewise the
`politeness` enum) in `review_accuracy.py`'s tags/register prompt, with an instruction to
suggest only in-enum values — exactly as `VALID_SEMANTIC` is embedded for semantic tags.
Cheap, high-leverage, and symmetric with the item-14 fix that already suppressed the
out-of-list *semantic*-tag false positives.

## 24. Non-hiragana-reading lint (cheap replacement for the furigana screener's true-positive class)

**Source**: 2026-06-18 accuracy-review furigana phase (entries 06926–07139), session 007

The expensive multi-model furigana **screener** earns its keep on already-polished ranges
at roughly **0–5% precision** (documented in `reviews/calibration_report.md`), and session
007 measured **39/40 false positives** (~2.5%) over 06926–07139. The false positives this
range were dominated by the runner's own **pair-extraction truncating long compound
readings** before showing them to the model: 入場料→「にゅうじ」, 電話→「でん」, 電気技師→「でんき」,
観客席→「かんきゃ」 were all flagged as "incomplete reading," but the actual entries hold the
correct full readings (`{入場料|にゅうじょうりょう}` etc.). So a large slice of screener noise is
an **extraction bug in `review_runner.py`**, not a model error — worth fixing on its own
(stop truncating the reading passed to the screener), and it would lift measured screener
precision without any model change.

The lone **true positive** in the range (06952) was a genuine non-furigana signal — Latin
letters ("uu") leaked into a reading. That class — *a reading field containing any
non-hiragana character* — is exactly what a **deterministic lint** would catch for free,
far more cheaply and reliably than paying gemini-2.5-flash per entry. 

**Suggested implementation**: A read-only `build/check_reading_charset.py` (or a rule in an
existing furigana checker) that flags any furigana **reading** component (the `…` in
`{kanji|…}`) containing a character outside hiragana + the small allowed set
(ー長音 where appropriate, ・ in some compounds) — i.e. stray katakana, Latin letters, digits,
or U+FFFD. This converts the screener's one real value-add on polished ranges into a
deterministic check, leaving the (expensive, low-precision) multi-model screener for ranges
that have never been reviewed. Pairs naturally with item 16's U+FFFD guard (same "reading
contains an illegal character" family) and the item-13/item-21 hardening (which addresses
the *abort* and *throughput* of the screener, while this addresses its *low precision*).

**Update 2026-06-22 (truncation artifact reconfirmed at 100% FP; plus a new grouping-error class the screener
*misses*)**: Two 2026-06-21/22 accuracy-review furigana phases over the 8038–8458 structured cohort give the
sharpest evidence yet for both halves of this item.
- **The extraction-truncation false positives reached 100%.** Over **8238–8458, ALL 30 screening flags were false
  positives**, dominated by the same `review_runner.py` pair-extraction truncation documented above: the screening
  model is shown example text cut off mid-word and flags the truncated reading as "incomplete" — 昇格→「しょ」,
  最高→「さい」, 視聴率→「しちょうり」, 永久凍土→「えいき」, 復号→「ふく」 — while the actual entries hold the correct
  full readings. A telling new detail: several truncated concerns even show a stray `)` where the entry has `}`,
  i.e. the extractor is mangling the wrapper delimiter, not just the reading length. The fix is unchanged and
  reinforced: **send the example/reading fields to the screener untruncated (or truncate only at furigana-pair
  boundaries)**, which would erase this dominant noise family without any model change. (The 8038–8237 phase
  similarly logged all 16 of its flags as documented FP families.) Both runs bulk-rejected the family as one
  aggregated `decisions.jsonl` line.
- **A genuine true-positive class the LLM screener does NOT flag: furigana *grouping* errors.** The 8038–8237
  deep pass surfaced **two real malformed-grouping errors** — `{全部食|ぜんぶた}` (should split to
  `{全部|ぜんぶ}{食|た}`) and `{メガ盛|も}` (should be `メガ{盛|も}`, katakana orphan pulled under the wrapper).
  These are *grouping* defects (multiple tokens, or a leading katakana/okurigana orphan, crammed under one
  furigana span), not reading errors, and the screener flags none of them. A cheap deterministic detector — flag
  any `{kanji…|reading}` span where the left side contains **more than one kanji token with intervening
  okurigana**, or a **leading katakana/kana character pulled inside the wrapper** — would catch this whole class
  for free, exactly the inverse trade-off of the truncation FPs above (the screener wastes money flagging
  non-errors while missing these real ones). This extends item 24's thesis: convert the furigana-correctness
  classes the screener handles badly — both its low-precision noise and its blind spots — into deterministic
  checks, and reserve the multi-model screener for never-reviewed ranges only.

**Update 2026-06-23 (the one screener true-positive class is exactly the deterministic lint's target)**: A
2026-06-22 accuracy-review screen over **8459–8632** flagged **22 of 174** entries; on adjudication **all were
truncation/display false positives (stray `)` for `}`, latin-char artifacts like "まちga", "じ)") except one** —
**08474**, a genuine **お-prefix-inside-wrapper** case. So on an already-polished structured range the screener's
entire net value was a single hit that a deterministic furigana-format/charset check (`check_furigana_format.py`
o-go-prefix class, or the proposed `check_reading_charset.py`) would have caught for free, while the model cost
174 paid calls to surface 21 FPs. This is the cleanest single-range demonstration of item 24's core trade — retire
the screener's furigana-correctness role on reviewed ranges to deterministic checks and reserve the multi-model
screener for never-reviewed ranges.

## 25. Cross-reference target-id resolution: detector over-count, build-time reading fallback, and `id`-vs-`target_id` drift

**Source**: 2026-06-19 routine systemic-fix run (missing-target-id lane)

A 2026-06-19 systemic-fix run draining `check_artifacts.py --issue missing-target-id`
surfaced three related defects in how cross-reference targets are detected, resolved, and
stored. They share a root concern — *which entry a cross-reference actually points at* —
and are best fixed together.

1. **`check_artifacts.py --issue missing-target-id` over-counts intentional target-less
   refs.** Of 136 flagged refs, only **40 were genuinely resolvable** (fixed this run →
   96 remain), and the residual ~96 are mostly **legitimate, permanent** target-less
   pointers: homophone / contrast / antonym **display labels** for words that have no
   entry and never will (e.g. 00250 工夫/こうふ "laborer (homophone)", 17797 侯爵 "marquis
   (homophone)", 00296 有限 "finite"). Because they can never resolve, they re-flag every
   run and the queue never converges. **Fix**: teach the detector to **exclude** a ref whose
   `type` is `homophone`/`contrast` (or that carries an explanatory `label`/`note`) **and**
   whose reading has no entry — those are intentional and should not be in the fix queue.

2. **Build-time by-reading fallback can resolve to the wrong sense.** 04026_hatsu's antonym
   `〜着` (arrival sense, ちゃく) has no entry; the build's by-reading fallback would resolve
   it to **27655_chaku (着 = counter for suits of clothing)** — a homophone of the wrong
   sense. (`target_id` was left unset this run to avoid the mis-link.) This is the same
   homophone-false-match hazard documented in Cleanup Backlog P2 (2026-06-17). **Fix**: the
   reading-fallback resolver should require a **headword-surface match**, not reading-only,
   before binding a `target_id` — reading alone is not enough to pick the right homophone.

3. **Vestigial non-schema `id` field instead of `target_id`.** 26 of the 136 dangling refs
   carried a legacy `id` field (the renderer reads `target_id` only, so these rendered as
   dead refs); 4 of those `id`s were **stale pre-renumber values** (01040_shinjin,
   02032_tenkin, 00373_ondo, 00213_gaikokujin). All 26 were promoted/repointed to
   `target_id` this run. The forward-looking concern: **newer entry-creation may still emit
   `id` instead of `target_id`** — worth a deterministic check (`check_artifacts.py` or
   `validate.py`: flag any cross-reference/see-also object carrying an `id` key) so the drift
   self-heals, and a look at the **entry-creation skill/templates** to stop emitting `id` at
   the source (flagged as a `[skill]` recommendation in the 2026-06-19 wiki session log; not
   actioned from the knowledge-base session).

**Impact**: (1) makes the missing-target-id queue converge instead of permanently
re-flagging ~96 intentional pointers; (2) closes a silent wrong-sense mis-link class at
build time; (3) stops dead `id`-only refs from being created and provides a self-healing
detector for the existing ones.

**Update 2026-06-20 (the convergence-failure quantified across four runs)**: A 2026-06-20
systemic-fix observation gave the detector's run-over-run trajectory: **190 → 136 → 96 → 82**.
Each run only drains the handful of refs whose referenced word gained an entry since the last
run (this run filled 13 whose targets were created as 29338–29351 — see Cleanup Backlog P2
update 2026-06-20); the residual ~80 are the **intentional, permanent** target-less
homophone/contrast/antonym display labels that re-flag every run. The queue is therefore
**hovering near 80 instead of converging to 0** — exactly the behaviour fix (1) above
(exclude `type=homophone`/`contrast`/`label`-bearing refs whose reading has no entry)
exists to correct. Already filed; this is quantitative reinforcement, no new action.

**Update 2026-06-21 (fix (1) IMPLEMENTED — the detector now converges)**: A 2026-06-21
systemic-fix run shipped fix (1). `check_artifacts.py --issue missing-target-id` now flags
**only refs whose referenced word actually has an entry** (resolvable = some entry shares
the ref's reading *and* furigana-stripped surface); the intentional, permanent target-less
pointers — homophone notes, antonym/contrast display labels, transitivity-pair pointers to
words with no entry — are **no longer re-surfaced every run**. `--include-intentional`
restores the full audit list (**77** such pointers as of that run). With the last 5
resolvable refs also filled (curator restock 29368–29383), the detector reports **0**
resolvable refs dictionary-wide and the queue has converged; the `artifact-missing-target-id`
backlog item is marked `resolved` in `backlog-queue.json` (and Cleanup Backlog P2 is marked
RESOLVED). It will only re-open automatically if a future ref's referenced word gains an
entry. **Fixes (2) (build-time by-reading fallback should require a surface match) and (3)
(deterministic `id`-vs-`target_id` drift check + entry-creation skill audit) remain open.**

## 27. Promote unknown-semantic tags from a `validate_tags.py` warning to a CI error

**Source**: 2026-06-22 + 2026-06-23 routine runs (recurring, two independent observations)

`validate_tags.py` treats out-of-`VALID_SEMANTIC` semantic tags as **warnings, not
errors**, so unknown-semantic drift accumulates silently as new entries are created:
`check_tag_drift.py --check unknown-semantic` reports **8,698 flags dictionary-wide** as
of 2026-06-22, and fresh creation cohorts keep adding to it (the free-form 7815–9239 band
runs 55–88% out-of-taxonomy; see [Cleanup Backlog](cleanup-backlog.md) → P20). Routine
accuracy-review (tags dimension) is currently the **only** thing draining the backlog, and
its per-run budget cannot keep pace with the inflow — much of the long tail has no 1:1
migration target and must be escalated to the curator (394 escalated in one 2026-06-23 run
alone). Draining a backlog that new-entry creation keeps refilling is a losing race.

**Suggested implementation**: promote unknown-semantic to a **CI error** (or a pre-commit
gate) so a new entry cannot introduce an off-list semantic tag — exactly parallel to the
U+FFFD guard shipped with item 16 and the inline-link target-id gate proposed in item 11.
The valid vocabulary is already centralised in `build/validate_tags.VALID_SEMANTIC`
(`schema.json` deliberately has no semantic-tag enum), so the gate is a small addition:
fail validation if any `metadata.tags.semantic` value is not in `VALID_SEMANTIC`, with the
existing `check_tag_drift.py` migration map surfaced as the suggested fix. **Sequencing
note**: a hard gate should land *with or after* the curated-migration systemic-fix pass
(Cleanup P20), or it would block legitimate work on the 8,698 existing entries; the cleanest
order is (1) curated migration sweep to drain the backlog, then (2) flip the gate to error so
it can't re-accumulate. Until then, keep it a warning but watch the dict-wide count.

## 28. systemic-fix selector should skip scope-0 standing checks

**Source**: 2026-06-22 routine systemic-fix run (selector landed on a no-op item)

The `routine_next.py` selector handed a 2026-06-22 systemic-fix run the backlog item
`tag-conjugation-no-verb-pos` (priority 6) as its top pick, but that detector returns **0**
— it is a deliberately-kept **scope-0 standing check** (the P6 cleanup is RESOLVED; the
check stays only to catch regressions). The run was therefore a no-op for its assigned item
and had to **cascade manually** to the next actionable item (`tag-politeness-unsupported`,
priority 7, 2 flags, resolved). Two scope-0 standing checks —
`tag-conjugation-no-verb-pos` and `proverb-idiom-mismatch` — currently sit at the top of
the open / `batch_ready` queue **ahead of genuinely-actionable items**, so a systemic-fix
run can be handed a guaranteed no-op and must hand-cascade to find real work.

**Suggested fix (either)**: (a) give standing checks a distinct `status` (e.g.
`standing`/`monitoring`) that the selector skips when their current `scope_estimate == 0`,
reverting to `open` automatically if the detector ever flags again; or (b) have the selector
**sort open `batch_ready` items by `scope_estimate > 0` before priority**, so it always
lands on an item with actual work and never burns a run on a scope-0 check. Option (b) is
the smaller change (a sort key in the selector) and needs no schema change to
`backlog-queue.json`. Either prevents the manual-cascade waste and keeps systemic-fix runs
landing on real work.

## Related pages

- [Cleanup Backlog](cleanup-backlog.md) — patterns these tools would address
- [Entry Follow-ups](entry-followups.md) — specific entry fixes
- [Architecture and Build System](../project/architecture.md) — build script overview
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis of the tag-drift patterns that items 5 and 6 address
- [Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) — analysis of the wrapper-format patterns that items 8 and 9 address
