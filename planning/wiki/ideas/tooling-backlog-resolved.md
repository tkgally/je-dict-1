# Tooling Backlog — resolved and closed items

Items moved here from [tooling-backlog.md](tooling-backlog.md) on 2026-09-26 because they are resolved, shipped, retired or refuted (by their `backlog-queue.json` status where they have one, otherwise by the status the item itself records). Kept for the record and for their measurements. If an item here turns out to be open, move it back.

## 2. Fix verify_furigana.py false positives on inline links

**Source**: Comprehensive-polish 2026-05-08 session 002 and 2026-05-09 session 001

`build/verify_furigana.py` raises false positives on inline link metadata. After `FURIGANA_PATTERN.sub('', notes)` it still sees kanji in the `→` tail of inline links like `⟦{時間|じかん}→時間：00468_jikan⟧` and reports them as unannotated. The render pipeline doesn't render that tail.

**Suggested fix**: Extend the strip pattern to also consume `→…：…⟧` (and the leading `⟦`) before counting kanji. Small change.

**Resurfaced**: Comprehensive-polish 2026-05-12 session 009 (entries 00776–00799) confirmed the same false-positive pattern — kanji in inline link baseforms (after `→`) are not rendered to users and should not require furigana. Continues to generate noise for entries with many inline links.

**Resurfaced again**: Comprehensive-polish 2026-05-13 session 007 (entries 01014–01038) reports the same issue. Third independent confirmation across different entry ranges.

**Resurfaced (4th)**: Comprehensive-polish 2026-05-14 session 004 (entries 01181–01204) reports the same false-positive pattern after adding inline links with kanji base forms (e.g., `⟦{踏|ふ}む→踏む：01197_fumu⟧`). Fourth independent confirmation. The `→baseform：` portion is clearly the primary noise source.

**RESOLVED (2026-05-15)**: Comprehensive-polish sessions 001–007 (entries 01489–01511) fixed the issue by stripping `→[^⟧]*⟧` before the furigana scan in both `verify_furigana.py` and `find_missing_furigana.py`. Committed in PR #2346. No further action needed on this item.

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

**Update 2026-07-01 (a new high-precision signal: physical-object semantic tag on a function-word POS)**: A 2026-07-01 routine polish run found **06355 どうせ** (adverb) tagged `furniture` (Cleanup [P11](cleanup-backlog.md) update 2026-07-01). This is a cleaner deterministic signal than the shipped `concrete-noun-domain-mismatch` check (which requires ≥2 mutually-distant hard domains and only fires on non-verb *content* headwords): **a physical-object/creature domain tag (`furniture`, `clothing`, `electronics`, `food`, `animal-*`, `tool`, `body-part`, …) on an entry whose `tags.pos` is an adverb, particle, conjunction, or interjection is a template/copy error by construction** — function words have no concrete semantic domain. Add it to `check_tag_drift.py` as a `function-word-concrete-domain` check: single-domain-tag is sufficient (no cluster count needed), keyed on the closed POS set, so precision should be very high. Complements the existing proverb-idiom / concrete-noun checks by covering the function-word slice they exclude.

**Update 2026-07-09 (six more 1:1 mappings for the `TAG_MIGRATION` map — the 13200–13299 death/crime/martial-arts cohort)**: A 2026-07-09 accuracy-review over **13200–13299** (a death/crime/martial-arts vocab cluster) migrated recurring off-taxonomy semantic tags that are **not yet in `check_tag_drift.py`'s `TAG_MIGRATION`** — `death`→`existence`, `crime`→`law`, `martial-arts`→`sports`, `writing`→`language`, `sport`→`sports` (singular/plural normalisation), plus `body`→`body-part` (already listed in the 2026-06-21 map update above). These are clean, context-independent 1:1 mappings that recurred across ~11 entries in the range (13224/13225/13226/13236/13237/13240/13241/13243/13244/13247/13248), so folding them into the migration map would let `--check unknown-semantic` auto-detect and the systemic-fix mode auto-migrate them dictionary-wide rather than draining them one accuracy-review pass at a time — the same scalable-instrument argument as the 2026-06-21 update. Queued under the existing `unknown-semantic-tags` backlog item; mirrored in the Cleanup Backlog [P20](cleanup-backlog.md) update 2026-07-09.

**Update 2026-07-14 (a 14387–14899 migration confirms the families are 1:1-mappable well into the 14000s)**: A 2026-07-13 systemic-fix run migrated **19 legacy off-vocab semantic tags** across **14387–14899** — `place`, `conflict`, `relation`, `time`, `medicine`, `transport`, `household`, `philosophy`, `interpersonal`, `quality` — all 1:1-mappable to in-list tags. Most are already covered by the 2026-06-21 / 2026-07-09 map expansions above (`place`→`geography`, `transport`→`transportation`, `household`→`daily-life`/`building`, `quality`→`descriptive`), reconfirming that the free-form/off-vocab cohort stays overwhelmingly deterministic-migratable this far up the ID range. With the dict-wide residue at ~**6,235 entries** ([Cleanup P20](cleanup-backlog.md) update 2026-07-14), the standing argument holds: a single `--check unknown-semantic` systemic-fix sweep with the accumulated `TAG_MIGRATION` map would drain them far faster than the accuracy reviewer surfacing ~19–20 per range at ~4× adjudication cost through the in-list-narrowness noise ([item 17](#17-accuracy-review-prompt-suppress-general-tag-noise-false-positives)). Same `unknown-semantic-tags` backlog item.

**Update 2026-07-15 (a cheap high-precision formality-drift cut — `adjective-i` POS carrying `formality: formal`)**: A 2026-07-15 routine polish §4 self-check caught **06498 しつこい** tagged `formality: formal` (corrected to `neutral`) — an everyday colloquial i-adjective given the creation-template formal default. Because the overwhelming majority of common i-adjectives are register-neutral, an **`adjective-i` POS + `formality: formal`** pair is a high-precision, cluster-free drift signal (single-tag test, no context count needed — cleaner than the register-note-contradiction slice, which requires parsing the notes). Worth adding to `check_tag_drift.py` as a standing formality check alongside the semantic-mismatch heuristics; pairs with [Cleanup P17](cleanup-backlog.md#priority-17-formal-formality-tag-over-applied-in-early-entries) (formality over-tagging in early entries), which this would surface deterministically for the i-adjective class.

**Update 2026-07-23 (more clean 1:1 mappings for the `TAG_MIGRATION` map — the 17086–17202 batch cohort)**: A 2026-07-22 accuracy-review over **17086–17202** migrated **53 off-vocab semantic tags** ([Cleanup P20](cleanup-backlog.md#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration) update 2026-07-23), the great majority of them **clean, context-independent 1:1 mappings** the observing run enumerated for the migration map — several already listed above (`motion`→`movement`, `body`→`body-part`, `place`→`building`/`geography`, `industry`→`business`), plus new ones to fold in: `grammar`→`grammatical`, `literature`→`media`, `environment`→`daily-life`, `hobby`→`leisure`, `house`→`furniture`, `object`→`tool`, `sensation`→`health` (context: `person` for a build/physique sense, `health` for pain). These recur across the 16000–18000 pre-enforcement creation band, so folding them into `check_tag_drift.py`'s `TAG_MIGRATION` would let `--check unknown-semantic` auto-detect and the systemic-fix mode auto-migrate them dictionary-wide — the same scalable-instrument argument as the 2026-06-21 / 2026-07-09 / 2026-07-14 map expansions. Queued under the existing `unknown-semantic-tags` backlog item.

**Update 2026-07-27 (two free deterministic cuts that the 19701–19950 accuracy sweep paid a model to find)**:

1. **Extend `TAG_MIGRATION` with the ~50 safe renames the sweeps keep re-deriving.** The 2026-07-27 accuracy-review over 19701–19950 hit 143 off-vocab tag occurrences across 83 distinct tags, dominated by 1:1 synonym renames (`time`→`time-general`, `body`→`body-part`, `thought`→`cognition`, `social`→`society`, `medical`/`medicine`→`health`, `people`→`person`, `description`→`descriptive`, `transport`→`transportation`, `grammar`→`grammatical`, `food-drink`/`food-and-drink`→`food`). The shipped map covers **nine**. Every run that re-derives the same renames by model call is paying for a lookup table. See [Cleanup P20](cleanup-backlog.md#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration) update 2026-07-27 for the measured family list and the judgment-dependent residue that must stay out of the map.
2. **"Semantic tag is a valid *domain* tag" is a set-membership test, not a review dimension.** `validate_tags.py` accepts `medical`, `legal`, `academic`, `business`, `technical` in `VALID_DOMAIN` but not in `VALID_SEMANTIC`, and the same sweep found five entries with them sitting in the semantic slot (19769, 19782, 19798, 19814, 19847). This whole misfiled-slot family is decidable with zero model calls, and the resolution is per-value and fixed: move the value to `tags.domain`, or migrate it (`medical`→`health`, `legal`→`law`, `academic`→`education`). Worth its own `--check domain-in-semantic-slot` sub-check.

Both reinforce the 2026-07-26 sequencing note: run `check_tag_drift.py --check unknown-semantic` **before** spending OpenRouter budget on a range, and let the model see only what set membership cannot decide.

**Update 2026-07-30 (the map is worth extending, but this range shows the tail is genuinely long — a table alone will not close `unknown-semantic`)**: The 2026-07-30 accuracy-review over **21301–21900** found **275 off-vocabulary semantic tags** spanning **~100 distinct tag strings** (`industry`, `human-relations`, `personal-qualities`, `stationery`, `maritime`, …). The shipped `TAG_MIGRATION` covers a handful; the ~19-pair table drafted on 2026-07-29 covers more.

This is the first measurement that separates the two things this item has been arguing for. The **head** of the distribution is a lookup table and should be one — the same dozen renames recur in every sweep and paying a model to re-derive them is waste. The **tail** is not: ~100 distinct strings over 275 occurrences means most strings appear once or twice, each needing a genuine judgment about the best in-list destination, and no table written today will contain the next range's inventions. So the honest framing of the map's value is *throughput on the recurring head*, not closure of the class. Closure has to come from the inflow gate (item 27's CI ratchet, already shipped as a baseline) plus a residual judgment queue that never goes to zero while entries are still being created against no enum.

The practical consequence for sequencing: extending the map raises the fraction a systemic-fix pass can auto-migrate, but the accuracy-review's `tags` dimension stays necessary for the tail — which is consistent with that dimension's high and rising apply rate (73.9% at the twenty-seventh metrics refresh). Map the head, review the tail, gate the inflow; none of the three substitutes for the others.

**Update 2026-07-30 (the reviewer is a source of *destinations*, not just detections — and it halves the curator queue)**: the 2026-07-30 accuracy-review over **22501–22766** measured what the tail costs with and without the model's help. For **34 off-vocabulary tags the deterministic 1:1 map could not resolve**, the `tags` dimension supplied a concrete in-list destination — craft/literature→`art`, facility/housing/place→`building`, perception/reading/mental-state→`cognition`, welfare→`society`. That cut the block's curator escalation **from 87 entries to 46**.

This reframes the "review the tail" leg above. The reviewer's value on off-vocab tags is not detection — set membership is free, and item 46 already argues for pre-scanning it deterministically — it is *proposing where the tag should go*. And that is exactly the work `reviews/needs_curator.txt` currently queues for a human, one entry at a time.

**Concrete recommendation**: run a `review_accuracy.py --dimensions tags` sweep **over the existing `needs_curator.txt` backlog** before asking the curator to decide each item by hand. The backlog is the accumulated residue of ranges where no destination was found; on this window's evidence, roughly half of it has a destination the reviewer will name for pennies. Whatever survives that pass is the genuine taxonomy question — and the twenty-eighth metrics refresh shows why this matters now: 337 escalations in four days, against a human loop that closed three items in the same period.

**The counter-caveat, from the same run**: roughly a **quarter** of the reviewer's tag suggestions were "replace the off-vocab tag with `general`" (`location`, `place`, `position`, `object`, `space`, `status`, `document` — all spatial or metadata concepts the taxonomy has no slot for). Those were rejected as a family: they trade a descriptive tag for the catch-all and would inflate the `tag-sole-general` queue (Cleanup P13). So the sweep proposed above needs a standing rejection rule for `→ general` suggestions, and the residue is a **taxonomy** question for the curator — does `VALID_SEMANTIC` want a spatial-position slot? — rather than 100 per-entry questions.

**Update 2026-08-02 (the map that already shipped has 660 unapplied hits — the extension debate has been running ahead of the sweep)**: This item has argued about *which* mappings to add since 2026-06-21. The 2026-08-02 wiki harvest measured what the **nine already in `TAG_MIGRATION`** are worth against the live corpus, and the answer reorders the work:

| | Labels | Live instances | Share of the 4,900 |
|---|---|---|---|
| `TAG_MIGRATION` as shipped | 9 | **660** | **13.5%** |
| + the 22 mappings proposed across the 2026-08-01 observations | 31 | 1,365 | 27.9% |
| A curated top-50-label map | 50 | 2,370 | 48.4% |

`time`→`time-general` alone has **204 live instances**; `people`→`person` 129; `medical`/`medicine`→`health` 95. **None of the nine has ever been swept dictionary-wide.** Successive accuracy-review runs have migrated 35–104 tags apiece by paid LLM review while a free, judgment-free instrument covering 13.5% of the population sat unrun in the repo. Extending the map is worth doing; running it is worth more, and should come first.

Two further measurements sharpen the item's own "map the head, review the tail" framing. The head is **flatter than assumed** — 818 distinct off-vocab labels, 345 of them singletons, only 199 occurring five or more times — so a curated top-50 map caps out near 48% and each label added past that buys steadily less. And the tail is **not concentrated ahead of the review frontier**: 46.7% of the residue sits inside 6739–23607, which accuracy-review has already swept, against 51.7% above 23608. The "review the tail" leg therefore cannot be scheduled as a frontier march; the deterministic sweep has to run over the whole corpus, including ranges already reviewed. Full numbers and the recommended three-step sequencing in [Cleanup P20](cleanup-backlog.md#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration), update 2026-08-02.

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

**Enhancement 2026-06-26 (an `--fix` mode for the `{お{…|…}}` nested-honorific shape)**: The detector currently emits a read-only review queue only; every fix is hand-applied. A 2026-06-26 routine polish run (frontier 06288–06300) found 06295/06296 carrying the nested-honorific wrapper `{お{香|こう}}` / `{お{土産|みやげ}}` (the `nested` + `o-go-prefix` classes together) and observed that this specific shape has a **single deterministic, provably-safe rewrite** — `{お{KANJI|reading}}` → `お{KANJI|reading}` (and the `{ご{…|…}}` analogue) — which alters only wrapper boundaries, never the surface text or reading. Add an opt-in `--fix` mode scoped to *this* transform (and the other provably-safe sub-patterns: bare-kana de-wrap, o/go-prefix lift), validated against `word_id_lookup.json` so inline-link surfaces still resolve, so the recurring 06200s–06300s honorific-batch instances (Cleanup P9 update 2026-06-26) can be cleaned mechanically instead of one entry at a time. Keep the default read-only; `--fix` writes only the sub-patterns whitelisted as never-error.

**Enhancement 2026-06-28 (two more degenerate right-side / no-pipe sub-patterns from the 06xxx frontier)**: Two 2026-06-27 routine observations surfaced wrapper shapes the current classifier folds into `pure-kana` instead of naming as their own degenerate class:
1. **English/Latin-text-after-pipe** — `{ゴマフアザラシ|spotted seal}` (found at 06561; the same shape as the ゴマフアザラシ bug fixed in [Cleanup P9 update 2026-06-27](cleanup-backlog.md)): the right side is an English gloss, not a reading, so the live site renders "spotted seal" as ruby. The detector classifies this as `pure-kana` because the left side has no kanji, masking a real content bug. Add a rule: a wrapper whose right (reading) side contains Latin letters / an English phrase is its own `english-after-pipe` class (severity = error — it renders a gloss as furigana).
2. **Katakana-only, no pipe** — `{ビル}`, `{モード}` (found at 06308): a `{...}` span wrapping katakana with no `|` at all. Katakana never needs furigana, so these render as literal braces and break inline-link/furigana expectations. This is a special case of the 2026-06-17 *no-pipe-span* rule (enhancement above) but worth surfacing distinctly because the fix is unambiguous — drop the braces entirely (`{ビル}` → `ビル`), a provably-safe `--fix` candidate alongside the `{お{…|…}}` transform.

Both cluster in the same early-2026 06xxx creation batch and are detector-cheap (right-side character-class test; no-pipe-span test already specified).

**Enhancement 2026-06-28 (the `o-go-prefix` *suggestion* assumes お/ご is honorific — verify it forms a real word first)**: A 2026-06-28 routine systemic-fix run (06650–07300 slice) caught the detector emitting a **wrong suggested rewrite**: `{おむつ替|か}` at 07140 was flagged `o-go-prefix` with suggestion `お{むつ替|か}`, but おむつ (diaper) is a *fixed kana word*, not honorific お + むつ — the only kanji is 替, so the correct rewrap is `おむつ{替|か}`. The detector's `o-go-prefix` class blindly assumes a leading お/ご is a separable honorific prefix and lifts it outside the wrapper; when the kana after お/ご is part of the lexical stem (おむつ, おやつ, おしぼり, …) the suggestion is wrong and must be hand-corrected. The flag itself is still useful (the wrapper *is* malformed — kana inside the kanji group), but the **suggested_replacement** is unreliable for this sub-family. A fix would check whether the kana run starting at お/ご forms a real word (e.g. against a kana-word list or `word_id_lookup.json`) before proposing the honorific lift, and otherwise fall back to "lift only the leading kana that are not part of a known word." Until then this remains a per-entry-verify case (and an argument against an unguarded `o-go-prefix` `--fix` mode — the `{お{…|…}}` nested-honorific transform of the 2026-06-26 enhancement is provably safe; the bare `o-go-prefix` lift is not).

**Update 2026-07-26 (a fourth degenerate sub-pattern with a clean mechanical test: Latin script on the *left* of the pipe)**: A 2026-07-26 systemic-fix sweep of 21000–21999 found the wrapper being used as a **gloss/reading separator** inside SIMILAR WORDS lists: `{furigana|ふりがな}` (21516) and `{downtown|ダウンタウン}` (21534) — matching the earlier `{old girl|オールドガール}` / `{old boy|オールドボーイ}` (07715/07716) and the inverse `{ゴマフアザラシ|spotted seal}` (06561, recorded 2026-06-28).

The test is trivially precise: **Latin script on either side of the pipe is never valid furigana** (the left side must be Japanese, the right side must be kana). Worth adding to `check_furigana_format.py` as its own sub-check rather than letting these fall through as `pure-kana`.

The **fix is not uniform**, so this sub-check should emit a review queue rather than auto-repair: the correct output depends on what the list item is meant to be — plain English when the item is the English term, plain katakana when it is the Japanese loanword. `{furigana|ふりがな}` → `ふりがな`; `{downtown|ダウンタウン}` → `ダウンタウン`; `{ゴマフアザラシ|spotted seal}` → `ゴマフアザラシ` with the gloss moved out of the braces. One glance per instance, and the population is small.

**Update 2026-07-27 (the no-pipe family finally measured dictionary-wide: 887 instances / 616 entries — comparable to the entire remaining P9 backlog)**: The 2026-06-17 enhancement above specified the no-pipe rule; the 2026-07-27 systemic-fix sweep (22000–23499) put a number on it. Because `FURIGANA_PATTERN` in `build/japanese_utils.py` is `\{([^|]+)\|([^}]+)\}` — pipe **required** — a brace span with no reading is never matched, never stripped, and reaches the rendered page as visible curly braces; and because all five shipped subpatterns assume a pipe, the family is absent from every scope estimate on this page and in `backlog-queue.json`. Measured across the string values of all entries: **887 instances across 616 entries**.

Two sub-shapes, with different fixes: (a) kana/loanword spans to simply de-brace (`{コンビニ}`, `{ゴミ}`, `{スカート}`, `{おひたし}`); (b) **bare kanji with no reading at all** (`{稀}`, `{続}`, `{匂}`, `{漸}`) — worse, because those render with braces *and* leave the kanji unglossed, so they are a furigana-*coverage* bug that `verify_furigana.py` also cannot see (the brace makes it look wrapped).

**Documented reject family** (this is why the sub-check must emit a review queue, not a `--fix`): a minority of no-pipe spans are intentional notation that must keep its braces — `{1, 2, 3, ...}` set notation (23397 自然数), `{X}` pattern placeholders, `{emotion}`-style category labels. Ship the sub-check with those as named exclusions. Full analysis in [Cleanup P9](cleanup-backlog.md#priority-9-malformed-furigana-wrappers) update 2026-07-27.

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

**Update 2026-07-25 (the strongest evidence yet: a single polish run silently introduced NINE dead links, all of which passed `validate.py` clean — and the documented check is the one that fails)**: A 2026-07-25 routine polish run wrote **nine inline links with plausible-but-nonexistent target IDs** (`00478_tomodachi`, `09048_koukyuu`, `09502_noni`, …). Every one of them **validated clean**. They were caught only by an **ad-hoc scan against the set of entry filenames** that the run happened to write for itself; without that improvisation they would have shipped.

The sharp point this adds to the item is that **the documented check is the broken one**. Both `CLAUDE.md` and `prompts/comprehensive_polish.md` advise `python3 build/validate.py --id X | grep -i "word link"` as *the* way to verify inline links — so a polishing session that follows the documented procedure exactly, and sees a clean result, has verified nothing about target-ID existence. The failure is silent, it is introduced by the very sessions whose job is to *improve* linking, and it accumulates invisibly between the rare occasions someone writes an ad-hoc scan.

This makes the item's priority materially higher than "worth running once the gate is built":

- **Minimum viable fix**: have `validate.py` resolve every `⟦…：entry_id⟧` target against the set of existing entry IDs (or `build/word_id_lookup.json`) and report unresolvable targets as an error. The set is already loaded by other build steps, so the cost is negligible.
- **Then run it once dictionary-wide** to size the existing dead-link population — nine were created in a *single* run, so the standing total is unlikely to be small.
- **Related**: [Cleanup P24](cleanup-backlog-resolved.md#priority-24-inline-link-base-forms-written-with-furigana-braces) (39 entries whose link *base form* carries furigana braces) is the same blind spot seen from the other side — malformed link internals that no check looks at.

**Update 2026-07-26 — the dictionary-wide scan this item asked for was finally run: 292 dead links / 160 entries, and 74% of them are mechanically repairable.** Two more polish runs hit the bug first (a 2026-07-26 run wrote **10** bad IDs — `01522_bangumi`, `05602_netto`, `00394_dekiru` … — all validating clean; a second wrote **2** more, `01188_nokosu` and `00939_made`, again caught only by a hand-rolled filesystem check). The wiki run then executed the scan the item had been requesting since 2026-06-10. Results over all 29,935 entries:

| Measure | Count |
|---|---|
| Inline links total | 262,189 |
| `noentry` sentinels (valid, skipped) | 7,301 |
| **Dead target IDs (occurrences)** | **292** |
| Distinct bad IDs | 144 |
| **Entries affected** | **160** |
| Dead-link rate | 0.11% of links |

Three findings make this **the single most batch-ready item in the backlog**:

1. **74% auto-repairable.** Resolving each dead link's *base form* against `build/word_id_lookup.json` gives **217 occurrences with exactly one candidate entry** — an unambiguous 1:1 repair (`見る` linked to `00433_miru` → `00283_miru`; `する` → `00392_suru`; `勉強` → `00770_benkyou`). **74** are ambiguous homographs needing judgment (`こと` → 3 candidates, `いる` → 4, `から` → 3, `後` → 2), and exactly **1** has no entry at all (`逆転する` — a candidate-creation or `noentry` case).
2. **The failure mode is number invention, not word confusion.** In nearly every case the *romaji* in the dead ID is right and only the digits are wrong (`00433_miru` vs `00283_miru`). The polisher recalled the reading correctly and guessed the five digits. That is precisely the error class a resolution gate catches for free, and it explains why the bug is invisible to every semantic check: the link *reads* correct.
3. **Dead links are created by polishing, not by entry creation.** All 292 fall in **00000–07999**, and nothing above:

   | Band | Dead links |
   |---|---|
   | 00000–00999 | 18 |
   | 01000–01999 | 10 |
   | 02000–02999 | 28 |
   | 03000–03999 | 64 |
   | 04000–04999 | 49 |
   | **05000–05999** | **112** |
   | 06000–06999 | 10 |
   | 07000–07999 | 1 |

   That is the inline-link-polished band exactly (the comprehensive frontier sits at 06650; entry creation never adds links per `CLAUDE.md`). The distribution is not a coincidence — **the population is entirely iatrogenic**, produced by the sessions whose purpose is to improve linking, which is the strongest possible argument for gating at write time rather than sweeping periodically.

**Detect command** (read-only, ~20 s dictionary-wide — regenerate rather than trusting these counts later):

```python
import json, re, pathlib
files = sorted(pathlib.Path("entries").rglob("*.json"))
ids = {f.stem for f in files}
L = json.load(open("build/word_id_lookup.json", encoding="utf-8"))
LINK = re.compile(r'⟦([^⟧]*?)→([^⟧：]*)：([^⟧]+)⟧')
for f in files:
    for m in LINK.finditer(f.read_text(encoding="utf-8")):
        base, tid = m.group(2).strip(), m.group(3).strip()
        if tid == "noentry" or tid in ids:
            continue
        cand = L["by_headword"].get(base) or L["by_reading"].get(base) or []
        print(f.stem, base, tid, [c["id"] for c in cand])
```

**Recommended sequencing** (unchanged in kind, now sized): ship the gate in `validate.py` first so the population stops growing, then work the 217 unambiguous repairs as a systemic-fix batch (filed as [Cleanup P27](cleanup-backlog.md#priority-27-dead-inline-link-target-ids)) and route the 74 ambiguous ones through per-entry judgment. Fixing the corpus before the gate exists would simply refill.

**Update 2026-07-27 (second consecutive cycle in which a polish run improvised its own link checker and found real dead links)**: The 2026-07-27 polish run reports that `python3 build/validate.py --id <id>` still prints "Entry is valid!" for entries whose inline links point at **nonexistent target IDs**, and caught `00494_aru` plus six wrong IDs only by writing an ad-hoc checker for the session. That is the same failure mode as the nine dead links of 2026-07-25 (recorded in [quality-metrics](../topics/quality-metrics.md) twenty-fifth refresh) — and the same workaround, re-invented. Two cycles running, the sessions whose job is to *improve* linking are the ones introducing dead links, and the only thing catching them is a throwaway script.

Nothing about the diagnosis has changed since this item was filed; what has changed is the evidence that the gap is **actively producing defects at a measurable rate**, not merely theoretically open. This remains the cheapest high-value gate outstanding: resolve every `⟦surface→base：entry_id⟧` target against `entries_index.json` / `word_id_lookup.json` in `validate.py`, and fail the entry. (Cleanup [P27](cleanup-backlog.md#priority-27-dead-inline-link-target-ids) tracks the existing population; this item is the inflow gate that stops it refilling.)

**Update 2026-07-28 (third consecutive cycle — and the two new dead links show *why* a wrong-but-existing ID is the dangerous shape)**: The 2026-07-28 polish run again wrote links that `validate.py --id` passed clean, and again caught them only with a throwaway scan of `entries/*/*.json` basenames. The two links are worth recording individually because both point at **real entries for the wrong word**:

- `何` linked to **`00294_motomoto`** (もともと "originally")
- `でも` linked to **`09528_tanaka`** (田中, a surname)

Neither is a dead *reference* — both IDs resolve, both render as working links on the live site, and both take the reader somewhere unrelated. This is a strictly worse failure than P27's 292 nonexistent-ID links, which at least fail visibly. It also means the gate this item proposes is necessary but **not sufficient**: existence-checking the target ID would not have caught either of these. The complete check is **base-form agreement** — resolve the link's own `base` segment through `word_id_lookup.json` and warn when the declared `entry_id` is not among the candidates. That is the same lookup the item's existing detect snippet already performs to *suggest* repairs; it just needs to run as an assertion rather than as a hint.

Three cycles running, three separate sessions have each written their own link checker because the documented gate (`validate.py --id X | grep "word link"`, per `CLAUDE.md`) is a no-op. The recurrence is the argument: this is not a latent risk, it is an active one, and the sessions exposed to it are precisely the ones whose job is to add links.

**Update 2026-07-29 (fifth and sixth consecutive cycles — and the corpus has now been swept, so this item has a number)**: The 2026-07-28 second polish run and the 2026-07-29 polish run both hit it live again. The second wrote `する：00003_suru` (00003 is `anmari`) and `見える：00284_mieru` (00284 is not `mieru`); both passed `validate.py --id` cleanly and were caught only by an ad-hoc comparison against the set of entry filenames.

The 2026-07-29 run then did what every prior cycle recommended and **swept the whole dictionary**:

> **292 dead inline links across 160 entries, pointing at 144 distinct non-existent entry IDs.**

Top offenders look like pre-renumbering stragglers rather than fresh mistakes: `00347_de` ×47, `00421_de` ×12, `00511_mo` ×10, `00368_to` ×9, `01286_toru` ×8 (`01286` is now `kanojo`). The rendering consequence is documented in the source: `html_utils.process_word_links` silently degrades an unresolvable target to plain text, so the word simply loses its link on the live site with **no error anywhere** — not in `validate.py`, not in the build, not in CI.

**The gate should be a ratchet, not a hard fail.** Baseline the existing 292 (as `build/validate_tags.py --check-no-new-unknown` already does for off-vocab tags) so CI does not go red on legacy entries, and fail only on a *new* dead link. That is what makes this shippable today rather than blocked behind a 160-entry cleanup — and it is the difference between this item and the `link-target-dead` queue entry, which is `blocked` precisely because it was framed as clean-first.

**And the existence check alone is still not sufficient** (carried forward from the 2026-07-28 update, unchanged by the sweep): the two links that run wrote pointed at *real entries for the wrong word* (何→`00294_motomoto`, でも→`09528_tanaka`), which render as working links to unrelated pages — strictly worse than a dead ID, which at least fails visibly. The complete check is **base-form agreement**: resolve the link's own declared base through `word_id_lookup.json` and warn when the declared ID is not among the candidates. Existence is the cheap half; agreement is the half that catches what a careful run actually gets wrong.

Recommended shape, in order: (1) ratcheted existence check in `validate.py` — ~15 lines, ships now; (2) base-form-agreement warning alongside it; (3) a systemic-fix pass that re-resolves each of the 292 by its own baseform/reading via `word_id_lookup.json`, which is mechanical for the `_de`/`_mo`/`_to` particle bulk.

**RESOLVED 2026-07-29 (routine systemic-fix) — and the diagnosis was wrong in one instructive way: the check already existed.**

All three recommended steps shipped in one run, but step 1 turned out not to need writing. `check_word_links()` in `validate.py` has been resolving link targets against the entry-ID set all along, and a full `make validate` was reporting **308 word-link warnings** (291 dead targets + 17 malformed) the whole time. The reason six consecutive polish runs saw "Entry is valid!" is narrower and worse than "the check is missing":

> `validate_single_entry()` — the function behind **both** `--entry` and `--id` — **never called `check_word_links` at all.** Neither did `validate_changed_only()` or `validate_range()`. The check ran only in the full-corpus path that a polishing session never invokes, and the pre-commit hook (`validate.py --entry`) was blind for the same reason.

So every cycle of this item read the *symptom* correctly ("the documented check is a no-op") and inferred the *wrong cause* ("no check exists"), and each cycle's proposed fix — write a resolution check — would have added a second implementation next to a working one that simply wasn't wired into three of four entry points. **The durable lesson: when a documented check reports nothing, verify which code path the documented invocation actually takes before concluding the check is absent.** A single `grep -n check_word_links build/validate.py` would have closed six cycles' worth of speculation, and the ad-hoc scanners three sessions wrote were re-implementing code already in the file they were running.

What shipped:

- **Corpus swept to zero.** All **291** dead links / **159** entries / **143** distinct dead IDs repaired. 289 re-targeted by resolving each link's own baseform through `word_id_lookup.json`; **2** set to `noentry` because no entry exists to link to (`逆転する`, and the conditional particle `ば`), both queued as candidates. Every one of the 143 distinct `(dead_id, baseform)` mappings was verified individually before application, and the three where a *kana* baseform matched a *kanji*-headword entry were checked in situ — which caught the one false resolution the lookup produced on its own: `ば` → `03699_ba` (場, "place"), a reading homophone of the conditional particle, not the word. A run that had trusted the lookup's single-candidate answer would have shipped a working link to the wrong entry.
- **The gate, made real rather than added.** Dead targets are now **errors** instead of warnings (they fail `make validate` and CI), and `check_word_links` is wired into `--entry`/`--id`, `--changed-only`, and `--range`, each checking against the whole dictionary's ID set rather than the subset under validation. **No baseline/ratchet was needed** — the corpus is at 0, so the check is absolute, which is stronger than the ratchet this item asked for and was only possible because the sweep and the gate shipped together.
- **New detector**: `build/check_link_targets.py` (read-only; `--summary`, `--json`, `--by-target`, `--resolvable`, `--ambiguous`, `--count`), which also proposes a replacement per dead link. This is the sibling proposed as `check_inline_links.py` in the item text.
- Note for future items: `build/tests/` still could not be run (no `pytest` in the image — Tooling 42), so the `validate.py` changes were verified by injecting a synthetic dead link and confirming exit 1 in all four modes, then confirming exit 0 and 30,031/30,031 valid after removal.

**The base-form-agreement half is now measured, and it is not a warning you can just switch on** — filed separately as `link-target-baseform-disagreement` in [backlog-queue.json](backlog-queue.json). Over all **264,132** links: 7,296 `noentry`, **255,070 agree**, 871 with no lookup hit, and **895 disagree**. But a naive check would be mostly noise, in two normalizable families:

| Family | Count | Verdict |
|---|---|---|
| Affix headword written with `〜`/`～` (`的`→`〜的` 09839, `者`→`〜者` 04662, `中`→`〜中` 09840) | 210 | benign — normalize the tilde |
| する-verb base pointing at its noun entry (`確認する`→`00158_kakunin`) | 267 | benign by convention — but note a separate `25332_kakuninsuru` exists, so which is *preferred* is a policy call |
| **Survivors after both normalizations** | **418** | the real queue |

The survivors contain exactly the failure shape the 2026-07-28 update predicted, now with confirmed instances: **`立てる` → `01189_tateru`, which is 建てる** (to build, not to stand up), ×11, and **`治る` → `00735_naoru`, which is 直る** (to be fixed, not to heal), ×7. Both render as working links to a different word. They also contain a benign orthographic-variant family (`頃`→`03091_koro` 〜ころ; `街`→`00613_machi` 町) that needs a policy decision rather than a repair. So: agreement is worth shipping, but only behind the two normalizations, and its output is a review queue, not an auto-fix.

**Shipped 2026-07-31 (routine systemic-fix): `build/check_link_baseform.py`** — read-only, same CLI shape as its sibling (`--summary`, `--json`, `--count`, `--by-base`, `--resolvable`, `--ambiguous`, `--range`). Three findings from building it:

- **A third normalization was needed, and it subsumes the first.** Comparing the base form against the *declared entry's own headword* — including alternatives in a `優しい／易しい` headword, and with `〜`/`～` stripped — accepts **227** links, and takes the affix family's count to **0**: normalizing `〜ころ`→`ころ` catches everything the tilde-prefixed lookup key was meant to catch. The affix path is retained as a lookup-key fallback but never fires. The `する`-noun rule stands on its own at **267**.
- **Re-measured on the current corpus: 405 disagree** (265,173 links; 256,094 agree; 870 no lookup hit; 0 dead targets). The item's 418 estimate held.
- **The queue is two families, and only one is a defect** — which is the durable finding. (a) *Wrong word*: base and declared headword are different words sharing a reading. (b) *Benign orthographic indexing*: the declared entry **is** the same word under a kana headword or variant spelling (`頃`→`〜ころ` ×24, `上げる`→`あげる` ×18, `通り`→`どおり`, `焼きたて`→`焼き立て`). Sweeping (b) would be a regression, so the detector reports and never repairs.

**First batch swept the same run**: the compound-homophone slice — base *and* declared headword both all-kanji, 2+ characters — is entirely family (a) and entirely unambiguous. **87 occurrences / 64 entries**, each verified against its own sentence before applying, each repair 1:1: `機能`→`昨日`, `状況`→`上京`, `電気`→`伝記`, `性格`→`正確`, `福祉`→`副詞`, `会社`→`外車`, `結婚式`→`結婚`. **318 remain**, and they are harder per link rather than easier — family (b) interleaved with genuine kanji-variant verb errors (`立てる`→`建てる`, `治る`→`直る`, `合う`→`会う`, `越える`→`超える`, `量る`→`測る`) that need sense judgment against the example. 12 are ambiguous (>1 lookup candidate) and belong to the curator.

**Ratchet candidate once the queue is worked down.** This class is invisible to every semantic instrument the project owns: the run's §4 accuracy self-check over the same 64 entries returned **zero** findings on the dimension that was actually broken (and 25 unrelated tag opinions instead). Deterministic base-form resolution is the only thing that can see it, so `check_link_baseform.py --count` deserves the same absolute gate the dead-target check got — but only after the 318 are triaged, since a gate over a non-zero benign population would fail CI on correct links.

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

**Update 2026-06-24 (twelfth/thirteenth confirmation — closed-tier function words again top the list)**:
Two 2026-06-23 routine polish runs ran their priority/notes lanes effectively all-no-op:
one found **0 of 8** sampled entries needing any change (already-polished basic-tier function
words — particles, basic i-adjectives 小さい/遅い/低い, など/だけ), and a frontier-lane run
corroborated with **0 of 4** (03095 など, 02947 低い, 00025 小さい, 00533 遅い — all with full
links, structured notes, conjugation, cross-refs). Both runs reiterate the same two
complementary fixes already filed: (a) the binding `score_note_quality.py` scorer-bug fix
(strip inline-link baseforms before the bare-kanji check; broaden the `required_sections`
matcher), and (b) a `prioritize_polishing.py` ranking-time **pre-filter that excludes entries
modified within the last ~30 days** so recently-polished entries stop re-surfacing in the
priority lane. No new diagnosis — twelfth/thirteenth consecutive no-op, pure reinforcement
that the scorer is anti-correlated with real need on the closed basic/core tiers.

**Update 2026-06-25 (fourteenth/fifteenth confirmation — the recency filter and the scorer bug now stack against the lane)**:
Two more routine polish runs (2026-06-24, 2026-06-25) hit the same no-op wall, and the 2026-06-25 run added a
sharper diagnosis of **how the recency skip and the scorer bug interact to defeat the lane**: the
2026-06-24-generated `priority/notes.txt` is dominated at the top by already-fully-polished **basic-tier
adjectives/particles** (03095 など, 02947 低い, 00025 小さい, 00533 遅い, だって, etc.) scoring ~50–57 purely from
POS-template conformance, and **most of that top band was modified within the last 30 days**, so routine2.md §2's
30-day skip rule *skips most of them* — and the few that survive the skip (だって, 低い, 遅い, 隣) come back needing
zero changes anyway. The two filters are thus stacked against the lane: the scorer keeps thoroughly-polished basic
entries perennially at the top (scorer-bugs #1/#2), and the 30-day skip then thins the eligible set down to a
handful that are *also* no-ops. The fix ordering is unchanged and reinforced — the binding fix is still the
`score_note_quality.py` scorer-bug pair (strip inline-link baseforms before the bare-kanji check; broaden the
`required_sections` matcher), and a **generation-time recency/coverage down-weight in `prioritize_polishing.py`**
(rank by staleness, not just length) would surface genuinely-stale entries instead of recently-polished basic ones.
Fifteenth consecutive priority-lane no-op session.

**Update 2026-06-26 (sixteenth confirmation — and the first non-no-op is itself diagnostic)**: A 2026-06-26 routine
polish run processed **6 eligible priority-lane entries** (だって / 低い / 小さい / 遅い / 何でも / だけ — all basic-tier
particles and adjectives, from a `notes.txt` regenerated that same day) and found **5 needing zero changes**; only
00304 何でも got real work (でも-series cross-refs 誰でも/いつでも/どこでも + back-links — a cross-reference gap, *not*
the note-quality deficit the scorer claims to rank). Per routine2.md §2's >half-no-op rule the run regenerated
priorities and reset the cursor — but, exactly as the 2026-06-23/25 updates predicted, regeneration re-surfaces the
same closed-tier function words because the scorer re-derives the same low scores from unchanged text. The single
non-no-op being a *cross-reference* fix (which the notes scorer does not measure at all) sharpens the point: the
ranking is not just noisy, it is measuring the wrong axis. Binding fix unchanged — the `score_note_quality.py`
scorer-bug pair plus the generation-time recency/coverage down-weight in `prioritize_polishing.py`. Sixteenth
consecutive effectively-no-op priority-lane session.

**Update 2026-06-26 (seventeenth/eighteenth confirmation — two all-no-op runs back-to-back)**: Two more
2026-06-26 routine polish runs ran their priority/notes lanes **5/5** (00642 金曜日, 01003 隣, 01006 腕, 02006 ばかり,
02007 まま) and **8/8** (だって, 低い, 小さい, 遅い, だけ, 金曜日, 隣, 腕) no-op — all basic/core function words and
adjectives already fully inline-linked and tier-1 clean, needing zero changes. The 8/8 run hit the §2 >half-no-op
rule and regenerated priorities + reset the cursor, and the observing run confirmed (as on 2026-06-23/25) that
**regeneration produces an identical ordering** because the scorer re-derives the same low scores from the same
unchanged text. One run added a concrete framing of the binding constraint as a generation-time filter: *"skip if
note already at structural floor for POS"* — i.e. a basic-tier function word whose note is already as short-and-clean
as its POS template allows should not be surfaced as "worst notes" at all. This is the closed-set/structural-adequacy
exclusion already filed (2026-06-18 update), restated from the frontier. Seventeenth/eighteenth consecutive
effectively-no-op priority-lane session; the `score_note_quality.py` scorer-bug pair plus a generation-time
recency/coverage (or structural-floor) down-weight in `prioritize_polishing.py` remain the binding fix.

**Update 2026-06-28 (nineteenth/twentieth confirmation — the regenerate+reset loop now demonstrably repeats *within a single day*)**: Two 2026-06-27 routine polish runs ran their priority/notes lanes **6/6** (03423 だって, 03728 まあ, 02947 低い, 00025 小さい, 00533 遅い, 03877 曜日) and **5/5** (03423 だって, 03728 まあ, 02947 低い, 00025 小さい, 00533 遅い) no-op on already-polished basic/core function words and adjectives — all eligible (modified >30d) but in good shape, needing zero changes. The sharper new detail: the 5/5 run's set is **identical to the set an earlier same-day routine polish run already processed**, so the §2 regenerate-priorities + reset-to-line-1 backstop now demonstrably **loops within a single day**, not just across days — because the `score_note_quality.py` scorer re-derives the same low scores from the same unchanged text, regeneration reproduces the same top ordering immediately. Nineteenth/twentieth consecutive effectively-no-op priority-lane session; the binding fix is unchanged — the `score_note_quality.py` scorer-bug pair (strip inline-link baseforms before the bare-kanji check; broaden the `required_sections` matcher) plus a generation-time recency/structural-floor down-weight in `prioritize_polishing.py` for closed-set or short-by-nature POS. **Twenty-first confirmation (later 2026-06-28, routine polish session 003)**: a third same-day run hit the *identical* 5/5 set (だって/まあ/低い/小さい/遅い) no-op; this run did **not** regenerate (the loop is documented to reproduce the same set within a day) and instead advanced the priority cursor past the examined lines — a sensible local workaround that further confirms regeneration is futile until the scorer bug is fixed.

**Update 2026-06-29 (twenty-second/twenty-third confirmation — and a clean statement of scorer-bug #1's mechanism from the frontier)**: Two 2026-06-29 routine polish runs ran their priority/notes lanes effectively all-no-op on the same closed-tier set: one examined 6 eligible entries (01118 ない, 03095 など, 00025 小さい, 03423 だって, 03728 まあ, 02947 低い + 00533 遅い / 01003 隣 in the same band) and found **5 of 6 needed zero changes**; the other found **all 6 eligible** (03423 だって, 03728 まあ, 02947 低い, 00025 小さい, 00533 遅い, 03877 曜日) already fully polished — valid, furigana-complete, fully inline-linked, adequate examples. Both runs restated **scorer-bug #1's mechanism** in concrete terms: the note-quality scorer *penalizes entries whose notes are dense with inline-link markup* (`⟦…⟧`) and structured glossary lists, ranking the most-polished entries at the bottom — because `has_bare_kanji` counts inline-link baseforms as un-furiganaed kanji (an entry with links in its notes scores furigana=0, the opposite of reality). This is the same root cause filed in the 2026-06-18 update, now reported from the frontier as "teach the scorer to strip/score inline-link markup before the length/quality heuristics." One observing run also juxtaposed its no-op priority lane against the genuine zero-link gap on the 06323–06328 frontier ([Cleanup Backlog](cleanup-backlog.md) → P21 update 2026-06-29) — the same anti-correlation between the notes ranking and real need documented since 2026-06-20. Twenty-second/twenty-third consecutive effectively-no-op priority-lane session; binding fix unchanged (the `score_note_quality.py` scorer-bug pair — strip inline-link baseforms before the bare-kanji check; broaden the `required_sections` matcher — plus a generation-time recency/structural-floor down-weight in `prioritize_polishing.py`).

**Update 2026-06-30 (twenty-fourth/twenty-fifth confirmation — and a sharper recency-stacking framing)**: Two more routine polish runs (2026-06-29, 2026-06-30) ran their priority/notes lanes effectively all-no-op on the same closed-tier set: one found **3 of 4** eligible entries needed no changes (top of `priority/notes.txt` dominated by basic/core entries 痛い / 同じ / まで / 兄弟 / 高い, all modified within the last 30 days), and a second found the **entire eligible priority lane already clean** (だって / ひくい / ちいさい … — 6/6 no-op). The 2026-06-30 observation adds the same recency-stacking diagnosis as the 2026-06-25 update: the note-quality ranker keeps high-frequency basic/core entries near the top on length-based heuristics *even though they are already polished*, and most of that top band is modified <30 days ago, so routine2.md §2's 30-day skip thins the eligible set to a handful that are *also* no-ops. Both runs restate the two complementary fixes already filed: the binding `score_note_quality.py` scorer-bug pair (strip inline-link baseforms before the bare-kanji check; broaden the `required_sections` matcher) **and** a generation-time recency/structural-floor down-weight in `prioritize_polishing.py` so recently-polished entries stop re-surfacing. Twenty-fourth/twenty-fifth consecutive effectively-no-op priority-lane session; no new diagnosis, pure reinforcement.

**Update 2026-07-01 (twenty-sixth confirmation — recency-stacking again yields 0/6)**: A 2026-06-30 routine polish run (routine_008) ran its priority `notes.txt` lane **0/6** — every eligible entry already well-polished — and triggered the §2 regenerate-priorities backstop. The observing run gave the same recency-stacking diagnosis as the 2026-06-25/30 updates: the notes ranking keeps high-frequency basic/core entries near the top on length-based heuristics even though they are already polished, and most of that top band is modified within the last 30 days, so routine2.md §2's 30-day skip thins the eligible set to a handful that are *also* no-ops. Restates the `prioritize_polishing.py` recency down-weight as (half of) the binding fix. Twenty-sixth consecutive effectively-no-op priority-lane session; pure reinforcement, no new diagnosis.

**Update 2026-07-02 (twenty-seventh/twenty-eighth confirmation — and the sharpest evidence yet that the scorer, not recency, is the binding defect)**: Two 2026-07-01 routine polish runs again ran their priority `notes.txt` lanes effectively all-no-op, but one of them isolated the failure from the recency-stacking confound. Routine polish session 006 processed the **first 6 *eligible* entries past §2's 30-day skip** (03423 だって, 03728 まあ, 02947 低い, 00025 小さい, 00533 遅い, 03877 曜日) and found **all 6 already fully polished** — complete inline links in examples and notes, good cross-references, conjugation tables — yet `score_note_quality.py` scores them **30–70**, keeping them at the top of "worst-first." So even after the 30-day recency skip removes the freshly-touched band, the entries that remain are *still* well-structured-but-low-scoring: the heuristic yields **false positives on well-structured basic/core notes independent of recency**, because it scores structured `FORMS` / `COLLOCATIONS` / `CONTRAST` blocks and inline-link-dense notes low (the two scorer bugs already filed). The observing run recommends the item-20 fix add an explicit **"structured-note credit"** — recognize ・-bulleted collocation/forms blocks and inline links as *quality* signal — rather than only length/section heuristics, otherwise the priority lane will keep surfacing already-clean basics. That run chose **not** to regenerate (a deterministic scorer over unchanged text reproduces the identical ordering, and reset-to-1 would re-examine the same clean entries) and advanced the priority cursor past the examined lines; the other run hit stale rankings at cursor line 42+ (top eligible >30d entries scoring 40–70 despite structured notes + inline links + cross-refs) and did regenerate + reset. Both restate the same underlying scorer defect. Twenty-seventh/twenty-eighth consecutive effectively-no-op priority-lane session; the binding fix is unchanged in kind but now more precisely specified — the `score_note_quality.py` scorer-bug pair (strip inline-link baseforms before the bare-kanji check; broaden the `required_sections` matcher) **plus** the new structured-note-credit signal, and the `prioritize_polishing.py` recency/structural-floor down-weight.

**Update 2026-07-03 (twenty-ninth/thirtieth/thirty-first confirmation — the advance-the-cursor workaround adopted as standing practice)**: Three routine polish runs across 2026-07-02/03 ran their priority `notes.txt` lanes effectively all-no-op on the same closed-tier set. (1) Session 004 (2026-07-02) surfaced **7/7** top *eligible* entries already fully polished (basic/core adjectives & particles: だって, まあ, 低い, 小さい, 遅い, 曜日, 転職), with 74/86 top-ranked entries modified within the last 30 days; it regenerated priorities + reset the cursor per the >half-no-op rule. (2) Session 007 (2026-07-02) then found the **top 5 eligible** (だって, まあ, 低い, 小さい, 遅い) fully polished again — and, noting that regeneration is deterministic and same-day reproduces the identical ranking (the idle loop documented in the 2026-06-28 update), **advanced the priority cursor to line 35** instead of resetting, to make forward progress down the ranked list. (3) Session 008 (2026-07-03), of the first 41 ranked IDs from line 35, skipped **36 as modified <30 days**, and of the 5 genuinely-eligible (小さい, 遅い, 曜日, 隣, 転職) found **4 already at full furigana + inline-link coverage**; only 転職 had a real defect (sense-1 explanation duplicated the gloss verbatim). It followed session 007's precedent and **advanced the cursor 35→71** rather than reset. The new operational datum: **advancing the cursor past the examined lines is now the de-facto workaround** (three runs, two of them explicitly choosing it over the futile regenerate+reset), which keeps the lane making forward progress but does not address the root defect. Binding fix unchanged and now well-specified — the `score_note_quality.py` scorer-bug pair (strip inline-link baseforms before the bare-kanji check; broaden the `required_sections` matcher) **plus** the structured-note-credit signal (2026-07-02 update) **plus** a generation-time recency/structural-floor down-weight in `prioritize_polishing.py`. Twenty-ninth/thirtieth/thirty-first consecutive effectively-no-op priority-lane session.

**Update 2026-07-04 (thirty-second/thirty-third confirmation — and a POS-misclassification detail that pins scorer-bug #2)**: Two 2026-07-03 routine polish runs again ran their priority `notes.txt` lanes effectively all-no-op. (1) One found **4 of its top 6 eligible entries** (02007 まま, 04376, 04767, 02355 すき, 00765 やさしい) already fully polished — complete inline links, thorough notes, cross-refs — and reiterated the scorer-bug #1 hypothesis directly ("the note-quality scorer appears to rank heavily inline-linked entries at the bottom even when their notes are complete; the ⟦…⟧ markup may be inflating apparent length or not being discounted — check whether `score_note_quality.py` strips inline-link markup before scoring"). (2) The other run traced the first ~34 ranked lines as mostly recently-modified (skipped) or fully-polished, checked the 5 eligible ones (03423 だって, 03728 まあ, 02947 低い, 00025 小さい, 00533 遅い), found all clean, and surfaced a **new concrete mechanism behind scorer-bug #2**: `score_note_quality.py` **misclassifies POS** — まあ (an interjection/adverb) was scored as `verb-godan` — so it applies the *wrong POS template* and penalizes correctly-formatted interjection/adverb/particle notes against verb/noun section expectations. This is a sharper, separately-fixable facet of the `required_sections`-matcher bug: the scorer must derive POS from `tags.pos` (not infer it) before choosing the section template. Binding fix unchanged in kind and now more precisely specified — the `score_note_quality.py` scorer-bug pair (strip inline-link baseforms before the bare-kanji check; fix POS derivation + broaden the `required_sections` matcher), the structured-note-credit signal, and the `prioritize_polishing.py` recency/structural-floor down-weight. Thirty-second/thirty-third consecutive effectively-no-op priority-lane session.

**Update 2026-07-04 (second) (thirty-fourth/thirty-fifth confirmation — the same closed-tier set, scores 33–57)**: Two 2026-07-04 routine polish loose observations reconfirm the pattern. (1) A priority-lane run found the top `notes.txt` set again dominated by already-polished basic/core function words, yielded **5/6 clean**, and regenerated + reset the cursor per the >half-no-op rule. (2) A second, more detailed observation named the exact top-ranked entries — 01118_nai (ない), 03423_datte (だって), 02947_hikui (低い), 00025_chiisai (小さい), 00533_osoi (遅い), 03877_youbi (曜日), 03728_maa (まあ) — all scored **33–57** by `score_note_quality.py` yet, on inspection, **content-complete with full inline links and good notes**, and restated the root cause precisely: the scorer measures against rigid POS templates, so template-nonconforming-but-complete entries stay top-ranked regardless of recent polishing, and because eligibility also skips <30-day-modified entries, each run's lane keeps landing on the same handful of eligible-but-clean entries — "a potential cross-run loop after regenerate+reset". Same binding fix (`score_note_quality.py` scorer-bug pair + structured-note credit + `prioritize_polishing.py` recency/structural-floor down-weight). Thirty-fourth/thirty-fifth consecutive effectively-no-op priority-lane session.

**Update 2026-07-08 (thirty-eighth–fortieth confirmation — but now with a small, informative non-no-op rate)**: Two more routine polish runs. (1) A 2026-07-06 run processed **5** priority-lane entries and found only **05432 じゃん** a genuine gap (a note-link fix); the other 4 (じゃん-neighbours in the じゃん/だって/まあ/ひくい/ちいさい band) were content-complete no-ops. (2) A 2026-07-07 run processed **8** priority-lane entries: **6 no-op** (00025 ちいさい, 00533 おそい, 03877 曜日, 01003 となり, 00765 やさしい, 02841 青) and **2 fixable** — 04376 洗面 (a stale `noentry`→now-resolved inline link) and 02355 好き (naked です in three examples). Because the priority file had been regenerated same-day (2026-07-06), the 2026-07-07 run correctly **advanced the cursor** per §2 rather than regenerate+reset (rankings current, not stale). The datum this window adds is that the lane is not *pure* noise — ~2 of 13 processed entries had real (if small) gaps, both of a kind the notes scorer does **not** measure (a stale-link fix and naked-copula examples), which is itself further evidence that the scorer is ranking on the wrong axis: it surfaces content-complete grammatical words while the genuine gaps it does catch are incidental to the ranking. Binding fix unchanged (`score_note_quality.py` scorer-bug pair + structured-note credit + `prioritize_polishing.py` recency/structural-floor down-weight). Thirty-eighth–fortieth consecutive effectively-no-op priority-lane session (36th/37th were the 2026-07-05 runs recorded in the top-of-page summary).

**Update 2026-07-09 (forty-first confirmation — richly-structured core adjectives surfaced as "worst notes")**: A 2026-07-09 routine polish run's notes-priority lane (`priority/notes.txt`, gen 2026-07-06) examined 5 eligible entries at lines 100–107 — 05337 映える, 00039 偉い, 01112 辛い, 01133 臭い, 03805 飯 — and found **3 of 5** (映える / 偉い / 臭い) already carrying complete, richly-structured notes needing no change; >half clean forced the §2 regenerate-priorities + cursor-reset backstop. Same diagnosis as the whole item-20 chain: `score_note_quality.py` under-ranks entries whose notes are *already thorough* (structured blocks + inline-link density read as low quality), so the ranking drifts stale relative to actual polishing state. Pure reinforcement — no new mechanism — but notable that the no-op set has moved off the closed basic/core function-word band (が/は/だって/まあ) onto **content adjectives** (偉い/辛い/臭い/映える), showing the scorer defect is not confined to the particle/function template mismatch (scorer-bug #2) but also hits ordinary well-structured adjective notes (scorer-bug #1, the inline-link-baseform bare-kanji miscount). Binding fix unchanged (`score_note_quality.py` scorer-bug pair + structured-note credit + `prioritize_polishing.py` recency/structural-floor down-weight). Forty-first consecutive effectively-no-op priority-lane session.

**Update 2026-07-10 (forty-second confirmation — same no-op set, same-day regeneration proven futile once more, and the genuine gaps are again off-axis)**: A 2026-07-10 routine polish priority lane (`priority/notes.txt` lines 36–83) examined 6 notes-priority entries and found **4 no-op** — 00533 遅い, 00674 涼しい, 03877 曜日, 01003 隣 — all richly-structured, fully-linked basic/core entries the scorer keeps ranking as "worst"; **00533 and 00674 are the identical no-ops the 2026-07-09 run flagged**, directly confirming the 2026-07-09 prediction that regeneration re-ranks these to the top identically (deterministic scorer). The 2 genuine fixes were again **off the axis the notes scorer measures** — both stale-`noentry` markers in mimetic entries (05766 にやにや → 29117, 05775 もぐもぐ → a new candidate), the same "incidental to the ranking" signal as the 2026-07-08 update. The observing run reiterated that regenerate+reset per §2 is a **no-op holding action** and that the durable fix is the `prioritize_polishing.py` down-weight of full-inline-link-coverage + recently-modified entries, not ranking freshness. Forty-second consecutive effectively-no-op priority-lane session; binding fix unchanged (scorer-bug pair + structured-note credit + `prioritize_polishing.py` recency/structural-floor down-weight). The recurring stale-`noentry` hits are filed as reinforcement under [item 19](#19-stale-noentry-inline-link-detector).

**Update 2026-07-12 (forty-fifth/forty-sixth confirmation — the real defects are structural, off the scorer's axis)**: Two routine polish priority lanes reconfirm the pattern and sharpen the "wrong axis" diagnosis. (1) The 2026-07-11 lane examined **7** entries (ない, 速い, 軽い, まあ, 執筆, 一切, 視聴) and found **only 2 real fixes**, *both* of a kind `score_note_quality.py` does not measure: 00514 速い's frozen **conjugation table** (the slash-variant bug now filed as [item 32](#32-add_adjective_conjugationspy-mishandles-slash-variant-i-adjective-headwords)) and 執筆's stale `者：noentry` (者 = 04662_sha — an [item 19](#19-stale-noentry-inline-link-detector) hit); the other 5 were closed-tier/complete no-ops, and the run advanced the cursor past the examined lines rather than regenerate. (2) The 2026-07-12 lane ran **7/7 clean** — 4 needing no change and 3 only incidental stale-`noentry` fixes — which crossed the >half-no-op threshold, so it regenerated priorities + reset the cursor per §2. The through-line both runs draw explicitly: the notes-quality scorer keeps surfacing content-complete basic/core entries as "worst notes," while the genuine defects it does *not* rank are **structural** (a broken conjugation table, stale inline links), not note-length or section-shape — the clearest statement yet that the ranking axis is mismatched to real need. Binding fix unchanged (the `score_note_quality.py` scorer-bug pair + structured-note credit + a `prioritize_polishing.py` recency/structural-floor down-weight). Forty-fifth/forty-sixth consecutive effectively-no-op priority-lane session.

**Update 2026-07-13 (scorer-bug #1 reproduced with three fresh entry IDs)**: A 2026-07-13 routine polish
run polishing basic i-adjectives named **00335, 00464, 00617** as concrete instances where the
`priority/notes.txt` ranking surfaced **already-clean** entries: `score_note_quality.py`'s `has_bare_kanji`
strips furigana `{漢|かん}` but **not** inline-link base forms `⟦{犬|いぬ}→犬：id⟧`, so the base-form kanji
after the `→` is counted as "bare kanji," costing any note that contains inline links the 5-point furigana
credit (a false positive) and inflating its worst-first rank. This is the exact scorer-bug #1 filed in the
2026-06-18 / 2026-07-04 updates, now with three more reproductions on ordinary basic-adjective notes. The
minimal fix is unchanged and precise: **strip `⟦…⟧` link markup (or test only the pre-`→` surface segment)
before the bare-kanji test.** No new mechanism — pure reinforcement that scorer-bug #1, not recency, keeps
inline-link-dense notes at the top of the ranking. Binding fix unchanged (the `score_note_quality.py`
scorer-bug pair + structured-note credit + the `prioritize_polishing.py` recency/structural-floor
down-weight). See also the item-15 update 2026-07-13: a dedicated "notes contain furigana outside `⟦…⟧`"
detector would replace this mis-firing ranking for the frontier-link backlog it is meant to surface.

**Update 2026-07-14 (forty-seventh/forty-eighth confirmation — and the sharpest single-run consolidation of both scorer bugs to date)**: Two 2026-07-13/14 routine polish priority lanes ran effectively all-no-op again — a 2026-07-13 lane examined **8** eligible low-ID basic/core adjectives + particles (00617 甘い, 00647 暗い, 00785 軽い, 03728 まあ, 00788 汚い, 00922 茶色い, 02947 低い, 00512 と) with **0** needing changes, and the 2026-07-14 lane ran **7/7** clean on the same closed-tier band (暗い/軽い/汚い/茶色い/低い, particle と, interjection まあ); both regenerated priorities + reset the cursor per the §2 >half-no-op rule. The value this window adds is a **consolidated root-cause statement** the observing run wrote out in full, pinning the permanent ~53 score on the two scorer bugs already filed, now with the concrete header strings and IDs in one place:
1. **`has_bare_kanji()` counts inline-link base-forms as bare kanji.** It strips only `{漢字|かな}` furigana markup, so kanji inside `⟦…→base：id⟧` link base-forms are counted as un-furiganaed → **every fully inline-linked entry scores `furigana: 0`**, the opposite of its polished state. Fix: strip `⟦…⟧` link syntax (or test only the pre-`→` surface segment) before the bare-kanji check.
2. **`find_sections()` credits `usage` only via literal `USAGE:` / "how to use" headers**, so notes that describe usage in an opening paragraph or under descriptive headers — `FORMS:`, `COMMON PATTERNS:`, `TWO MEANINGS`, `DEGREES OF LIKING` — score `required: 0`. Fix: credit an opening usage paragraph and broaden the header variant matching (and, per the 2026-07-04 update, derive POS from `tags.pos` before choosing the section template).
Net: because the metric is deterministic over unchanged text, **regeneration re-ranks the identical fully-polished basic/core adjectives to the top every time** — the regenerate+reset backstop is a no-op holding action, and the binding fix remains the `score_note_quality.py` scorer-bug pair + the structured-note-credit signal + a `prioritize_polishing.py` recency/structural-floor down-weight. Forty-seventh/forty-eighth consecutive effectively-no-op priority-lane session.

**Update 2026-07-15 (forty-ninth/fiftieth confirmation — the same two scorer bugs, two more no-op lanes)**: Two 2026-07-14 routine polish priority lanes again ran effectively all-no-op on already-well-polished closed-tier entries. (1) A lane surfaced basic-tier function words scoring **~50 despite comprehensive, well-structured notes with full inline links** — 03095 など, 02352 いろいろ, 02900 ぐらい, 02870 黄色, 05432 じゃん — and the observing run again pinned it on the scorer **under-crediting ALL-CAPS section headers and treating heavy `⟦…⟧` inline-link markup as length-inflating / plain-text-density-reducing**; their genuine gap when one existed was missing `cross_references`, *not* note quality — the ranking is measuring the wrong axis. (2) A separate lane examined the **8 top notes-priority entries** (00335 大きい, 00464 安い, 00647 暗い, 00785 軽い, 03728 まあ, 00788 汚い, 00922 茶色い, 02947 低い) and found **all 8 already fully polished** (valid, complete furigana + inline links, well-sectioned notes) needing no change; priorities regenerated at wrap-up. Forty-ninth/fiftieth consecutive effectively-no-op priority-lane session; no new mechanism — pure reinforcement of scorer-bug #1 (inline-link base-forms counted as bare kanji) and #2 (descriptive/ALL-CAPS headers uncredited). Binding fix unchanged (`score_note_quality.py` scorer-bug pair + structured-note credit + `prioritize_polishing.py` recency/structural-floor down-weight).

**Update 2026-07-15 (fifty-first/fifty-second confirmation — two more no-op lanes; the scorer floats already-polished basics again)**: Two 2026-07-15 routine polish priority lanes ran effectively all-no-op on already-fully-polished closed-tier entries. (1) A lane surfaced the older-than-30-day i-adjectives **00335 大きい / 00464 安い / 00647 暗い** at the top of `notes.txt`, all fully polished no-ops with symmetric back-links already in place (ookii↔chiisai, yasui↔takai); priorities regenerated + cursor reset. (2) The 06495–06499 frontier run's paired priority lane examined **7** entries (黄色 kiiro, 大きい ookii, 安い yasui, 暗い kurai, 軽い karui, 黄色い kiiroi, まあ maa — closed-tier, polished May–June) and found **all 7** needing zero changes (cross-refs symmetric, tags fine, notes well-formed); regenerated priorities + reset the cursor per the §2 >half-no-op rule. Both runs restate that `score_note_quality.py` keeps floating content-complete closed-tier basics to the top (the inline-link-base-form bare-kanji miscount + uncredited descriptive headers), and one run reframed the durable fix as a **"recently-polished / has-full-notes" damping term** in the scorer/ranking — the same structural-floor down-weight already filed. Fifty-first/fifty-second consecutive effectively-no-op priority-lane session; binding fix unchanged.

**Update 2026-07-16 (fifty-third confirmation — and a new escalation: the notes priority lane is now *exhausted*, not just noisy)**: A 2026-07-16 routine polish priority lane ran **7 of 8 no-op** on the same closed-tier basic i-adjective set (黄色 kiiro, 大きい ookii, 安い yasui, 暗い kurai, 軽い karui, 弱い yowai, 黄色い kiiroi — all already fully polished, scoring ~50–57), the lone real fix being **off the notes-scorer's axis** again (00763 うるさい carried a なあ `⟦…：noentry⟧` marker that now resolves to 29262_naa — an item-19 stale-`noentry` fix, not a note-quality gap). No new mechanism: the same 03728_maa was again POS-misdetected by the scorer as `verb-godan` (scoring 30), and the same inline-link-base-form bare-kanji miscount (scorer-bug #1) + literal-header `usage` matcher (scorer-bug #2) drive the false-low scores on 02870_kiiro / 00335_ookii / 00464_yasui / 00647_kurai / 00785_karui / 00825_yowai / 00959_kiiroi / 01136_sukunai / 03728_maa.

The genuinely-new datum is that the lane has now hit its **floor**: the same run reported (and this wiki session independently confirmed) that **`score_note_quality.py --below 30` now returns *nothing* dictionary-wide** — the notes-priority list's own top IDs (03095_nado, 02870_kiiro, 00335_ookii, 00464_yasui, 00510_mijikai, 00514_hayai) all score ~50–53 and need no work. So the lane is no longer merely re-surfacing settled entries; there are **no genuinely-thin notes left for it to find** at the current threshold, and every remaining "worst note" is a scorer false-positive. This escalates the fix priority two ways:
1. **The scorer-bug pair is now the *only* thing standing between the lane and correctly reporting "done"** — with the bugs fixed, the exhaustion would be visible as a clean empty ranking instead of a loop on false-positive basics.
2. **Consider retiring or repurposing the notes priority lane itself** (routine2.md §2's priority lane), or **reweighting it toward dimensions where real gaps remain** — the polish observations consistently show the genuine frontier deficits are **inline-link coverage** (Cleanup P21) and **stale `noentry` markers** (item 19), neither of which `score_note_quality.py` measures. A `cross_refs`/`links`-oriented priority ranking would point the lane at the work that actually exists. Fifty-third consecutive effectively-no-op priority-lane session; the binding scorer-bug fix is unchanged, but its urgency is now backed by lane exhaustion, not just recurring noise.

 **Update 2026-07-18 (fifty-fourth confirmation + a precise restatement of scorer-bug #2 on adjective-i)**: A 2026-07-17 routine polish priority lane ran **5 of 6 no-op** on the same closed-tier basics (00825 弱い, 00959 黄色い, 01136 少ない, 03728 まあ, 00504 から, 01253 大事); the lone fix (00959) was **off the notes-scorer's axis** — a kana-in-furigana wrapper `{きれい|きれい}`→`きれい`, not a note-quality issue — so priorities were regenerated + cursor reset to line 1 per the §2 >half-no-op rule. A **second 2026-07-17 observation pinned scorer-bug #2 exactly** for the adjective-i case: `prioritize_polishing.py --task notes` floats well-polished basic-tier i-adjectives (02870 kiiro, 00335 ookii, 00464 yasui, 00616 akarui, 00647 kurai, 00785 karui, 00825 yowai) at the very top with score ~53, all passing tier-1 cleanly (valid, full furigana, complete inline links, good cross-refs); the ~30-point penalty is `score_note_quality.py`'s `required_sections=['usage']` for `adjective-i` scoring the entry as if the header were absent when the usage is conveyed in an **unheadered opening sentence** rather than a literal `USAGE:`-matchable header. The concrete two-option fix (unchanged from the standing recommendation, now stated per-POS): **(a)** make `find_sections` treat an unheadered opening usage paragraph as satisfying `'usage'`, or **(b)** drop `'usage'` from `adjective-i`'s `required_sections`. Fifty-fourth consecutive effectively-no-op priority-lane session; binding scorer-bug-pair fix unchanged, urgency reinforced by the ongoing exhaustion (item's escalation above).

**Update 2026-07-18 (second) (fifty-fifth/fifty-sixth confirmation — two independent runs name inline-link completeness as the un-credited axis)**: Two 2026-07-18 runs — a routine accuracy-review and routine polish session 006 — each independently restated the same root cause without prompting. (1) The **accuracy-review** run's priority lane processed **4 entries, all no-op** (01136 少ない, 03728 まあ, 00504 から, 01253 大事, all already fully inline-linked and structured, 0 changes), and concluded plainly: "the notes-quality score doesn't credit inline-link completeness, so recently link-polished basic/core entries still rank at the top"; it regenerated priorities and recommended `prioritize_polishing.py` down-weight entries already carrying full `⟦…⟧` coverage. (2) The **polish session 006** lane examined the identical closed-tier basic-adjective band (kiiro / ookii / yasui / akarui / kurai / karui / yowai / sukunai) and drew the same conclusion — the top of `priority/notes.txt` is filled with already-link-polished basic adjectives whose real gap was only a `USAGE:`/`COLLOCATIONS` header rename, not content — and offered the same two-option fix stated at the whole-scorer level: **(a)** fold a small link-coverage term into `score_note_quality.py`, or **(b)** down-weight entries already carrying full `⟦…⟧` coverage in `prioritize_polishing.py` so genuinely thin notes surface first. This is the first window where **two separate modes** (accuracy-review + polish) each surfaced and diagnosed the no-op loop in the same run-day, both landing on inline-link-coverage as the missing signal — pure reinforcement of scorer-bug #1 (inline-link base-forms counted as bare kanji), now framed as a positive "link-coverage credit / down-weight" term rather than only a bug to remove. Binding fix unchanged (the `score_note_quality.py` scorer-bug pair + structured-note credit + the `prioritize_polishing.py` recency/structural-floor/full-link-coverage down-weight); fifty-fifth/fifty-sixth consecutive effectively-no-op priority-lane confirmation.

**Update 2026-07-18 (third) (fifty-seventh confirmation — a clean 8/8 no-op on a mixed particle+adjective band)**: A 2026-07-18 routine polish session 009 priority notes-lane ran **8 of 8 no-op** across the 00484–01253 band — 03728 まあ, 00504 から, 01253 大事, 00788 汚い, 00922 茶色い, 02947 低い, 00484 も, 00512 と — all fully-linked / well-noted closed-tier basic/core **particles and adjectives** scoring low only on the known `score_note_quality.py` false positives (the inline-link-base-form bare-kanji miscount + uncredited descriptive headers + the まあ POS-misdetection). The lane's mix of particles (も / と / から) alongside adjectives reconfirms the scorer floats *any* content-complete closed-tier entry, not just i-adjectives. Priorities were regenerated + cursor reset to line 1 per the §2 >half-no-op rule. Fifty-seventh consecutive effectively-no-op priority-lane session; pure reinforcement, continuing to argue for the notes-lane retirement / inline-link-coverage credit (the escalation recorded in the 2026-07-16 update above) over the deterministically-futile regenerate+reset backstop.

**Update 2026-07-20 (fifty-eighth/fifty-ninth confirmation — the no-op set moves onto basic-tier content adjectives/adverbs, one run advances the cursor rather than regenerate)**: Two routine polish runs reconfirmed the loop. The 2026-07-19 session (frontier 06546–06552) examined the top-8 priority-lane entries and found **all 8 clean** (00510 短い, 00512 と, 00504 から, 03728 まあ, 01253 大事, 00484 も, …) — fully-linked, comprehensive-noted closed-tier particles/function words scoring low only on the known `score_note_quality.py` false positives. The 2026-07-20 session examined priority ordinals 16–21 (**00025 小さい, 00530 近い, 00533 遅い, 00674 涼しい** — now basic-tier **content adjectives/adverbs**, not the closed function-word band) and again found them **all clean** (complete inline links, furigana, correct example counts, good notes), and **advanced the priority cursor to line 22 instead of regenerating** (deterministic scorer → regeneration re-surfaces the same entries, proven futile many times). The move of the no-op set off particles onto ordinary well-structured basic adjectives reconfirms scorer-bug #1 (inline-link base-forms miscounted as bare kanji depresses link-dense notes) hits *any* concise-but-complete entry regardless of POS. Binding fix unchanged (the `score_note_quality.py` scorer-bug pair + structured-note credit + the `prioritize_polishing.py` recency/structural-floor/full-link-coverage down-weight); reinforces the standing notes-lane-retirement / inline-link-coverage-credit escalation (2026-07-16 update).

**Update 2026-07-21 (sixtieth/sixty-first confirmation — and the concrete scorer-bug mechanism for kana headwords: POS is inferred from the romaji shape, not `tags.pos`)**: Two 2026-07-20 routine polish priority notes-lanes ran effectively all-no-op again — the top entries (03728 まあ, 00504 から, 01253 大事, 00922 茶色い, 02947 低い, 00484 も, 00512 と, 00846 必要) all examined, all needing zero changes; because the earlier run had already regenerated+reset the same day, the later run **advanced the cursor past the examined no-ops instead of regenerating again** (the deterministic scorer re-surfaces the identical set). The genuinely-new datum is a **precise mechanism for the long-noted 03728_maa mis-score**: `score_note_quality.py` scores まあ (an interjection/adverb, `tags.pos=["interjection","adverb"]`) as **`verb-godan`** and gives it **30 — the lowest score in the whole priority file** — despite full inline links, 15 examples across 3 senses, and cleanly-sectioned notes. The scorer is **inferring POS from the romaji/headword shape** (まあ→"maa"→godan-looking `-u`-final) rather than reading `tags.pos`, so kana interjections/adverbs/particles are judged against the verb-note template and float to the top. This sharpens scorer-bug #2's fix into a concrete first step: **derive the section template from `tags.pos` before choosing `required_sections`** (noted parenthetically in the 2026-07-04 update, now with a reproducing entry and the exact wrong POS/score). Sixtieth/sixty-first consecutive effectively-no-op priority-lane session; binding scorer-bug-pair fix unchanged, urgency reinforced by the ongoing lane exhaustion.

**Update 2026-07-22 (sixty-second/sixty-third confirmation — two more all-no-op lanes, the second explicitly recommending an inline-link-coverage / already-polished damper)**: Two routine polish priority notes-lanes reconfirmed the loop. (1) A 2026-07-21 lane examined **all 8 notes-priority entries at cursor lines 27–38** (00783, 03877, 00490, 00964, 00592, 00755, 06662, 00118) and found **every one already fully polished** — complete inline links, rich structured notes, correct tags, genuine `noentry` markers — needing zero changes; priorities were regenerated + cursor reset per the §2 >half-clean rule. (2) A 2026-07-22 lane again found `priority/notes.txt` topped by already-polished low-ID basic/core entries (00510 短い, 01253 大事, 02947 低い, 00922 茶色い, 03728 まあ, …) and ran **all 4 eligible entries no-op**, concluding the note-quality scorer **under-credits these compact, complete basic-tier notes** and recommending a concrete damper — "cap the penalty when inline-link coverage is already full, or add a recency/already-polished dampener so the priority lane surfaces genuinely thin notes, not short-but-complete ones." Sixty-second/sixty-third consecutive effectively-no-op priority-lane session; no new mechanism — pure reinforcement of scorer-bug #1 (inline-link base-forms counted as bare kanji) and #2 (descriptive/ALL-CAPS-header + kana-headword POS misdetection), and of the standing notes-lane-retirement / inline-link-coverage-credit escalation (2026-07-16 update). Binding fix unchanged.

**Update 2026-07-23 (sixty-fourth/sixty-fifth confirmation — and a concrete demonstration that "regenerate + reset to line 1" *loops within a single day*)**: Two 2026-07-22 routine polish priority notes-lanes ran all-no-op again on the same closed-tier basic/core band — one examined **6** eligible entries (02947 低い, 00922 茶色い, 00025 小さい, 03728 まあ, 01253 大事, 00846 必要) with **0** changes and regenerated priorities + reset the cursor per the §2 >half-no-op rule; the *next* run then **started at line 1 and hit the identical already-polished adjectives+particles** (03728 まあ, 00504 から, 01253 大事, 00922 茶色い, 02947 低い, 00484 も), again **6/6 no-op**. The genuinely-new datum is that the §2 regenerate-and-reset-to-1 backstop is not merely a no-op holding action but an **active loop**: because the scorer is deterministic over unchanged text, `make priorities` reproduces the identical ranking, so reset-to-1 sends the next run straight back to the same no-ops. That run therefore **deliberately advanced the priority cursor to line 13** (past the 12 lines examined) rather than reset — the advance-past-examined-lines workaround (now de-facto standing practice since 2026-07-03) is the only way to make forward progress and escape the loop. It also restated the precise mechanism for the 03728 まあ mis-score (scorer infers POS from the romaji shape — まあ→"maa"→godan — and scores the interjection/adverb as `verb-godan`=30, floating it to the top; derive the section template from `tags.pos` first). Sixty-fourth/sixty-fifth consecutive effectively-no-op priority-lane session; binding scorer-bug-pair fix unchanged, and the "reset-to-1 loops" demonstration further strengthens the notes-lane-retirement / inline-link-coverage-credit escalation (2026-07-16 update) over the regenerate+reset backstop.

**Update 2026-07-24 (sixty-sixth–sixty-eighth no-op confirmation — three consecutive routine polish runs)**: Three 2026-07-23/24 routine polish priority `notes.txt` lanes again ran effectively all-no-op on the same closed-tier basic particles/adjectives (00504 から / 01253 大事 / 00922 茶色い / 02947 低い / 00484 も / 00512 と / 00846 必要 / 00025 小さい, scored ~50 yet content-complete with structured fields + full inline links) — the 2026-07-24 run's 6/6 the third same-day recurrence of the identical head-of-list set. Two runs regenerated priorities + reset the cursor per §2, again reproducing the same ordering (deterministic scorer). Pure reinforcement of the two `score_note_quality.py` scorer bugs (inline-link-baseform bare-kanji miscount + POS-from-romaji mis-template) and the standing **notes-lane-retirement / inline-link-coverage-credit** escalation — the genuine frontier gaps this window (the zero-linked 06599–06613 band, [Cleanup P21](../ideas/cleanup-backlog.md#priority-21-unlinked-自動詞他動詞-labels-and-particles-in-compound-verb-notes)) are exactly what the notes scorer does not measure. Binding fix unchanged.

**Update 2026-07-25 (an important counter-datum — two priority notes-lanes were NOT no-op; the low scores were *partly* a real structural gap, not purely scorer noise)**: Two 2026-07-24/25 routine polish priority notes-lanes broke the long "deterministically-futile no-op" streak on the *same* head-of-list basic set (から / 大事 / 茶色い / 低い / も / と, and further basic adjectives/particles). All the processed entries had a **real, fixable gap**: the `notes` field lacked the **template-required FUNCTIONS/USAGE overview section** (an at-a-glance function/usage summary that is house standard for particles and adjectives), and one (大事) used mixed-case headers instead of the house-style UPPERCASE. Adding a concise, inline-linked FUNCTIONS/USAGE section + normalizing headers raised scores **40–57 → 80–92** — genuine learner-facing improvements, not metric-gaming. This **refines the scorer-retirement debate rather than overturning it**: the recurring low scores on these basics are **not purely scorer noise** — a subset reflected a real missing overview section the scorer legitimately penalized — even though the scorer *also* still under-credits the rich structured fields these entries do have (`particle_contrasts` / `fixed_patterns`) via scorer-bugs #1/#2. Takeaway: before retiring the notes lane, **separate the two signals** — the lane surfaces both (a) genuine missing-section gaps worth fixing and (b) false positives from the scorer bugs; the fix is still the scorer-bug pair + structured-note credit, but the lane is **not** pure noise, so the retirement escalation should become "fix the scorer and add a structured-note/section-presence credit" rather than "remove the lane." (Contrast the sixty-fourth–sixty-eighth all-no-op confirmations above, which examined bands that already *had* the overview section.)

**Update 2026-07-26 (scorer-bug #1 is now *measured*, not merely diagnosed — it mis-scores 6,351 entries, and the lane ran 5/5 productive for a second run)**: Two things this harvest, one of which finally sizes the bug that has driven ~68 of the confirmations above.

**(1) Scorer-bug #1, quantified dictionary-wide.** Two 2026-07-26 polish runs reported it again from the entry side ("all five entries in this run's priority lane scored exactly 50 before polishing, and the missing 5 points were this bug in every case"). The wiki run measured it directly against `build/score_note_quality.py`:

| Entries whose `notes` contain `⟦…⟧` inline links | 6,555 |
|---|---|
| **Flagged `has_bare_kanji` *solely* because of link markup** | **6,351 (96.9%)** |
| Flagged with genuine bare kanji as well | 70 |
| Clean | 134 |

Reproduced minimally — `has_bare_kanji('⟦{漢字|かんじ}→漢字：01234_x⟧ is a word.')` returns `True`, the same text without the link returns `False`. The mechanism is `score_note_quality.py:123`: `FURIGANA_PATTERN.sub('', text)` deletes the `{漢字|かんじ}` wrapper but leaves the link's **base form** `漢字` standing in the residue `⟦→漢字：01234_x⟧`, which then trips the kanji test.

So **21% of the dictionary silently forfeits the 5-point furigana credit, and the penalty lands precisely on the entries that are *most* polished** — completing tier-1 inline-link coverage lowers an entry's note score. `polishing/priority/notes.txt` is ranked by that score, so the priority lane's ordering is not merely noisy but **inverted with respect to link coverage**: the more thoroughly an entry has been linked, the higher it ranks for "needs work." That is the mechanical explanation for the whole no-op streak, and it makes the one-line fix (strip `⟦…⟧` markup before the bare-kanji test — or apply the test only to the link's *surface* portion) the highest-leverage item on this page after [item 11](#11-inline-link-target-id-resolution-gate-in-validatepy-or-pre-commitci).

**(2) The lane ran 5/5 productive again.** A 2026-07-26 lane (priority lines 67–78) found real work in **all five** entries — missing USAGE / COMMON PATTERNS sections, stale `noentry` markers that now resolve, empty `cross_references` on entries whose notes already named the neighbors. Together with the 2026-07-25 counter-datum above, that is **two consecutive productive lanes** now that the cursor has moved past the closed-tier basics at the head of the list. This settles the retirement debate in the direction the 2026-07-25 update pointed: **the lane is not the problem, the scorer and the head of the list were.** Recommended disposition — fix scorer-bug #1 (one line), keep the lane, and keep advancing the cursor past examined no-ops rather than resetting to line 1.

**Update 2026-07-27 (the section-name mismatch, with the exact strings — and a cheaper alternative to widening the matcher)**: The 2026-07-27 priority-lane run pinned down more of scorer bug #2. `find_sections` in `build/score_note_quality.py` is **name-driven**, so notes with fully adequate content under differently-worded headings score as if the section were missing: a **"SIMILAR WORDS:"** block in an i-adjective entry does not satisfy the template's *similar adjectives* slot, and **"REGIONAL USE:"** does not satisfy *usage*. Several priority-lane entries therefore rank low for wording, not content — which is the mechanism behind this item's long run of no-op priority lanes.

Two ways out, and the second is cheaper than it looks:
1. **Widen the variant lists** — `similar words` → any heading containing `similar`; `use`/`used for`/`regional use` → `usage`. Fixes the scorer but leaves the heading vocabulary open-ended, so the next descriptive heading re-opens the gap.
2. **Document the exact expected headings in the `vocabulary-notes` skill** so polishing and creation sessions write to them. This converts an unbounded matching problem into a bounded authoring convention, and it is the only one of the two that makes the score comparable across entries written months apart.

Doing (2) without (1) would misscore the existing corpus; doing (1) without (2) leaves the scorer chasing synonyms forever. Recommend both, in that order — and note that a skill change is a **curator action** (a `wiki` run may not modify skills).

**Update 2026-07-28 (scorer bug #2's root cause found, and it is a one-character substring match: `"adverb"` contains `"verb"`)**: The POS-misclassification half of this item has been reported since 2026-07-04 (まあ scored as `verb-godan`) without a mechanism. The 2026-07-28 priority-lane run found it. `normalize_pos()` in `build/score_note_quality.py` reaches a generic branch that tests

```python
'verb' in pos.split(',')[0]
```

— a **substring** test against the first comma-separated POS field. `"adverb"` contains `"verb"`, so every entry whose `part_of_speech` begins with `adverb` is classified `verb-godan` and scored against the verb template: it is required to have TRANSITIVITY, ASPECT, and COMMON PATTERNS sections that an adverb cannot sensibly have. The worked case is **00266_maido** (`part_of_speech: "adverb, noun"`), whose score stayed at **54 after a complete notes rewrite** — the missing points were structurally unreachable.

The fix is one line: a word-boundary test (`re.search(r'\bverb', ...)`) or an explicit `adverb` check ahead of the generic verb branch.

**This completes the diagnosis of the no-op streak, and both halves are now one-line fixes in the same file.** Bug #1 (inline-link base forms counted as bare kanji, measured at 6,351 entries) systematically *lowers* the score of the most-polished entries; bug #2 makes an entire POS class permanently unscoreable. Together they explain both directions of the ranking's inversion: the lane was fed entries that were already good and entries that could never be improved. Note the interaction with the section-name mismatch documented in the 2026-07-27 update above — an adverb entry misrouted to the verb template is *also* being matched against the wrong section-name list, so the two bugs compound rather than merely coexist.

Recommended disposition is unchanged in kind and now fully specified: **fix both one-liners, regenerate `polishing/priority/notes.txt`, reset the priority cursor to line 1** (the current cursor position indexes a ranking produced by the buggy scorer and is meaningless afterward), and keep the lane. All three are **curator actions** — a `wiki` run may not modify build scripts.

**RESOLVED 2026-07-29 — both one-liners shipped, priorities regenerated, cursor reset.** The 2026-07-28 polish run applied both fixes and this harvest verified them in the source:

| Bug | Fix in `build/score_note_quality.py` | Verified |
|---|---|---|
| #2 POS substring match | `normalize_pos()` line 62 now reads `if pos.startswith('verb') or re.search(r'\bverb\b', pos.split(',')[0].strip())`, with an explicit `'adverb' in pos` branch downstream | ✅ |
| #1 inline-link tail counted as bare kanji | `has_bare_kanji()` now strips `INLINE_LINK_TAIL_PATTERN` **before** `FURIGANA_PATTERN` | ✅ |

Measured blast radius of the two bugs together: **6,529 of 29,993 entries (22%) were mis-scored**, so every `polishing/priority/*.txt` ranking produced since the priority lane was introduced was ranking partly the wrong entries. 1,039 entries carried an adverb-first POS string and 334 changed template after the word-boundary fix (02921 どうも: 54 as a "verb" → 83 as an adverb); 6,195 entries were affected by bug #1. Priorities were regenerated in the same run and the priority cursor reset to line 1 (now at `line: 57`).

**Standing caveat for future harvests**: any conclusion drawn from a *pre-2026-07-28* priority-lane session — in particular the long no-op streak this item was opened to explain, and the staleness hypothesis in the original text above — was drawn against the buggy ranking and should not be treated as evidence about the lane's design. The lane's real hit rate is only measurable from 2026-07-28 forward. Two data points so far: the 2026-07-29 06:27 run's priority lane still reported no-ops on some entries, so **the staleness question is re-opened, not answered** — it simply cannot be attributed to the scorer any more.

This item took **25 days** from first symptom (2026-07-04, まあ scored as `verb-godan`) to fix, and the fix was two lines. The gating factor was mechanism, not effort: it moved the day a run traced the symptom to `'verb' in "adverb"` rather than re-reporting it.

### Update 2026-08-03 — what the post-fix lane is actually finding (and it is not missing notes)

The first substantive report from a post-fix priority lane, from the 2026-08-02 polish run: **all
six entries it worked had structured notes with sections.** They did not score low for absence.
They scored low because the notes are **inventories** — a list of similar words, a list of
patterns — with no statement of what distinguishes the headword from its neighbours. The run's
high-value edit on every one was converting a SIMILAR WORDS *list* into *contrasts* that say when
each alternative is wrong.

Two consequences:

- **The lane is now finding real work**, which is the first evidence since the scorer fix that its
  design is sound. The long no-op streak really was the scorer.
- **The scorer appears to reward the right thing by accident.** It measures structure and length,
  and a contrast paragraph is longer than a list — so the score improves for a reason adjacent to
  the actual improvement. That is fine as a *ranking* signal and unreliable as a *quality* signal;
  nobody should treat a rising note score as evidence that notes got more useful.

If this item ever gains a follow-on, it is the one this report suggests: a signal for
**inventory-shaped notes** (a SIMILAR WORDS section whose body is a bare list with no "use X when
…" clause), which is both mechanically detectable and closer to what a learner needs than length.

### Update 2026-08-04 — three more entries that top the list and are never worked

Two polish runs reported the same shape from opposite ends of the priority file: `00755_shizuka`
sits at the top of `polishing/priority/notes.txt` but was polished 2026-07-25, and `06481_kikinaosu`
and `00118_ii` likewise rank high but fall inside the 30-day recency skip. Both runs drew the same
conclusion independently — *if an entry still ranks near the top after `make priorities`
regenerates, the scorer is probably penalising something the polishing passes do not actually fix.*

That is a testable claim and the test is cheap: after the next regeneration, take the entries that
rank top-20 in **both** the old and the new file despite having been polished in between, and read
what the scorer is docking them for. The 2026-08-03 harvest already found one such mechanism — the
scorer rewards length, so an inventory-shaped SIMILAR WORDS list scores well while a short,
contrastive note scores badly — and a second confirmed instance would turn this item from "the
ranking excludes recently-polished entries" into a concrete scoring-function bug. Until then the
practical cost is small but real: the priority lane spends its first minutes skipping the same
three entries every run.

## 30. `sweep-stranded-prs.py` fails with HTTP 403 against api.github.com under the agent proxy — RESOLVED 2026-06-26

**Status (resolved 2026-06-25 tooling-fix session, harvested 2026-06-26)**: Fixed via **option (b) + (c)
combined** — the strand-sweep and CI-gate are now done through the GitHub **MCP** server, and the legacy direct-REST
scripts exit cleanly instead of crashing. The session diagnosed the 403 precisely: it is **not** a token/network/egress
problem (unauthenticated reads return 200, the CONNECT tunnel succeeds, only *authenticated* REST is refused — a
platform policy 403 "GitHub access is not enabled for this session"), so "fix the auth" was the wrong framing; the real
fix was to **stop depending on direct REST**. The Routine now sweeps strands via `list_pull_requests` + `get_files` +
`update_pull_request`(close) and gates CI via `pull_request_read method=get_check_runs`, and both
`pipeline/sweep-stranded-prs.py` and `pipeline/wait-for-pr-checks.sh` now detect the 403 and exit cleanly with a
pointer (sweep = no-op exit 0, wait = exit 3) rather than a bare traceback. CLAUDE.md, routine2.md,
comprehensive_polish.md, newentries.md, fix_spurious_conjugations.md, and fix_semantic_tag_drift.md were updated to make
the MCP path authoritative. **A latent rescue bug was fixed in the same session**: §0a's rescue gate and several prompts
used `pull_request_read method=get_status`, but the legacy combined-status API is blind to GitHub Actions check-runs
(it returns `state:"pending", total_count:0` for a PR whose `validate` check actually succeeded — verified on PR 2808),
so a `get_status`-based rescue could never confirm green; all CI-status checks were switched to `method=get_check_runs`
(green = `total_count≥1` AND every run completed with conclusion `success`/`neutral`/`skipped`). The original bug report
is retained below for context.

**Source**: 2026-06-25 routine pre-flight (wiki run)

The Routine's §0b pre-flight step `python3 pipeline/sweep-stranded-prs.py` **fails with HTTP 403** in the
agent-proxy execution environment. The traceback is in `get_progress_next_from_main()` →
`gh_api("/contents/{PROGRESS_PATH}?ref=main")`: the script makes a **direct `urllib` request to
`api.github.com`**, which the agent proxy blocks (the proxy only permits the routed MCP/`HTTPS_PROXY` paths).
`GITHUB_TOKEN` is present (len 40), so this is a transport/routing problem, not an auth-credential problem —
the same 403 the proxy README documents for tools that bypass it.

**Why it matters**: the sweep is the project's self-healing mechanism for stranded `claude/*` PRs (CLAUDE.md →
"If a Routine session does end up bailing out before merging … the next session's pre-flight call to
`sweep-stranded-prs.py` will close the now-obsolete PR and delete its branch"). If the script can never reach
GitHub from the Routine environment, that safety net **silently never fires** — stranded PRs would accumulate
unnoticed. It was a no-op on 2026-06-25 only because there happened to be zero open PRs (the §0a MCP rescue check
confirmed this independently), so no strand was masked *this* run — but a real strand would be.

**Suggested fix (any of)**: (a) route the script's GitHub calls through `HTTPS_PROXY` / the proxy CA bundle the
rest of the Routine uses (read `os.environ["HTTPS_PROXY"]` and the `/root/.ccr/ca-bundle.crt` bundle), so the
existing `urllib` path works behind the proxy; (b) reimplement the script's three API calls (list PRs, read
`progress.txt` on main, delete branch) against the **GitHub MCP server**, matching the rest of routine2.md's MCP
path; or (c) at minimum, have the script **exit non-zero with a clear "could not reach GitHub — strand sweep
skipped" message** instead of a bare traceback, and have the Routine note it in the session log (as this run did)
so the curator knows the net is down. Until fixed, the §0a MCP-based rescue check (which *does* work) is the only
working strand-detection path in the Routine pre-flight.

## 34. `comprehensive_polish.md` names two cross-reference types the schema rejects — RESOLVED 2026-07-29

**Source**: 2026-07-25 routine polish run — recurring; first reported 2026-05-09

`prompts/comprehensive_polish.md` line 107 instructs the polisher to use, among others,
the cross-reference types **`formality_variant`** and **`transitivity_pair`**:

> Cross-references include obvious neighbors: synonyms, antonyms, transitivity pairs, register
> variants. Use `synonym`, `antonym`, `related`, `contrast`, `formality_variant`,
> `transitivity_pair` per the `cross-reference-entry` skill.

Neither exists. `build/schema.json`'s enum is exactly:

```
["pair", "synonym", "antonym", "keigo", "related", "see_also", "contrast", "homophone"]
```

A polisher that follows the prompt as written **fails validation**, then has to guess a
replacement mid-run (`pair` for a transitivity pair, `related` or `keigo` for a register
variant). This is not hypothetical: session logs record the detour repeatedly —
`comprehensive_2026-05-09_002` ("tried `formality_variant` but it isn't valid in schema — used
`related` instead"), `comprehensive_2026-05-20_001` and `comprehensive_2026-05-31_002` (both
"fixed cross_reference type transitivity_pair→pair"), and several 2026-05-13 entries created
with the invalid type before it was caught.

**It was already reported and never fixed.** A 2026-05-09 polish session filed it as a `[skill]`
observation, and the 2026-05-09 wiki run recorded it in `planning/wiki/log.md` as skill
recommendations (2) and (3) — but wiki sessions are forbidden from editing prompts/skills, so the
recommendation has sat un-actioned for **two and a half months** while polish runs kept hitting it.
The 2026-07-25 observation misattributes the source to `CLAUDE.md`; the string does **not** appear
there (verified this run) — the live source is `prompts/comprehensive_polish.md:107`, which is why
it keeps recurring: that is the prompt the Routine's `polish` mode follows on every run.

**Suggested fix** — a curator one-liner, either direction:

- **Correct the prompt** (recommended): replace `formality_variant` → `keigo` or `related`, and
  `transitivity_pair` → `pair`, in `prompts/comprehensive_polish.md:107`; check
  `.claude/skills/cross-reference-entry/` for the same wording while there.
- **Or extend the schema** to admit both types, if the finer distinction is judged worth having —
  but that requires a migration of existing `pair`/`related` references to stay meaningful, so the
  prompt fix is the cheaper correct answer.

Either way this belongs to the curator, not to a Routine run: `wiki` mode may not touch prompts,
and `polish` mode legitimately works around it per-entry.

**Update 2026-07-26 (third consecutive cycle, and the misattribution has now propagated into the observation stream)**: A 2026-07-26 polish run hit it again — tried `formality_variant`, failed validation, substituted `related`, and filed a fresh `[skill]` observation. That is the same detour recorded in 2026-05-09, 2026-05-20, 2026-05-31, 2026-07-25, and now 2026-07-26: **every polish run that adds a register cross-reference pays this tax.**

The new observation repeats the 2026-07-25 misattribution — it names `CLAUDE.md` as a source of the invalid types alongside the prompt. Re-verified this run: `formality_variant` appears in **`prompts/comprehensive_polish.md:107` only** (`grep -rn formality_variant CLAUDE.md prompts/ .claude/skills/` returns exactly that one line), and `build/schema.json`'s enum remains `["pair","synonym","antonym","keigo","related","see_also","contrast","homophone"]`. The misattribution matters because a curator who greps `CLAUDE.md`, finds nothing, and concludes the report is stale will leave the live source untouched — which may be part of why a one-line fix has survived two and a half months.

**One line, one file**: `prompts/comprehensive_polish.md:107` — `formality_variant` → `keigo`/`related`, `transitivity_pair` → `pair`.

**Update 2026-07-27 (fourth consecutive report; the `CLAUDE.md` attribution re-verified false a second time)**: The 2026-07-27 polish run reported this again, and again attributed the invalid types to *both* `CLAUDE.md` and `prompts/comprehensive_polish.md`. Re-verified this refresh with a grep over `CLAUDE.md`, `prompts/`, `.claude/`, and `build/schema.json`: **`formality_variant` occurs in exactly one place in the repository — `prompts/comprehensive_polish.md:107`.** `CLAUDE.md` is clean. This is the second cycle in which the misattribution has propagated through the observation stream, so it is worth stating flatly here for the next harvest that reads it.

The underlying defect is unchanged and is a **one-line curator fix** in either direction:
- `build/schema.json` allows exactly `pair, synonym, antonym, keigo, related, see_also, contrast, homophone`;
- `prompts/comprehensive_polish.md:107` tells polishing sessions to use `formality_variant` and `transitivity_pair`, both of which fail validation on write.

Either add the two types to the schema enum, or drop them from line 107 — the existing `keigo` and `pair` types already cover both concepts, which argues for dropping. Four cycles of a polishing prompt instructing sessions to write data the validator rejects is the cost of leaving it open; a `wiki` run may not touch prompts, so this stays a curator item.

**RESOLVED 2026-07-29 — fixed in the prompt, and the fix goes further than this item asked.** Verified in the source this harvest: `prompts/comprehensive_polish.md:107` now reads

> Use one of the types the schema actually accepts — `pair` (transitivity pairs), `synonym`, `antonym`, `related`, `contrast`, `see_also`, `keigo` (register/politeness variants), `homophone` — per the `cross-reference-entry` skill. The authoritative list lives in `build/constants.py`; `transitivity_pair` and `formality_variant` are **not** valid and will fail schema validation.

`grep -rn 'formality_variant\|transitivity_pair' CLAUDE.md prompts/ .claude/ build/` now returns **only** that line (as a negative example) plus an unrelated function name in `build/check_semantic_clusters.py`. The curator chose the drop-from-the-prompt direction this item recommended, and added two things it did not: a pointer to `build/constants.py` as the authoritative list, and an explicit statement of what is *not* valid — which is what stops the next run from re-deriving the invalid names from the phrase "transitivity pairs" in the same sentence.

**Elapsed: 2026-05-09 → 2026-07-29, five reported cycles, one line.** Worth recording alongside item 20 (fixed the same week after 25 days): both were one-line fixes that sat open for months while every affected run paid the tax and re-filed the observation. What changed in neither case was the argument for fixing it — what changed was that the report finally carried the exact file, line, and replacement text. The generalisable lesson for the harvest is to spend the extra minute pinning the *edit* rather than the *symptom*; two of this cycle's long-open items closed within days of getting that treatment.

One residue worth noting for accuracy: the `CLAUDE.md` misattribution that dogged this item for two cycles (runs reporting the invalid types as coming from both `CLAUDE.md` and the prompt) was false both times it was checked, and it plausibly cost time — a curator who greps the wrongly-named file, finds nothing, and concludes the report is stale leaves the live source untouched.

## 44. Consistency check: non-neutral `formality` with no REGISTER statement in the notes

**Source**: 2026-07-29 routine accuracy-review (20703–21300)

Five entries in a single 600-entry band carry `formality: formal` with no register
statement anywhere in their notes: **21031 {主観的|しゅかんてき}な, 21146 {相当|そうとう}する,
21258 {率直|そっちょく}に, 21265 {複雑化|ふくざつか}, 21279 {高度化|こうどか}**.

This produces a standing, self-renewing cost. The accuracy reviewer flags every one of
them; the standing adjudication policy (`routine2.md` §A step 4) rejects the flag,
because a formality flag is applied only when the entry's own notes *contradict* the
label — and silence is not contradiction. So the flags are correctly rejected, and
**correctly re-raised on every future pass over the same band**, forever. The ledger
records them as reviewer noise; they are better described as an unanswerable question.

**Fix**: a `check_consistency.py` rule — `formality != "neutral"` ∧ no REGISTER section in
notes → report. That converts a recurring per-pass adjudication into a one-time queue the
curator or a polish lane drains, after which the entries either gain a REGISTER note (and
the tag becomes defensible) or lose the tag.

**Scope estimate needed before acting.** Five per 600 entries extrapolates to ~250
dictionary-wide, but the class is known to be non-uniform: Cleanup P17 documents `formal`
over-application concentrated in early entries and in template-defaulted cohorts, and
the 2026-07-29 polish run found the same defect from the other direction (**06682 じわじわ**,
an onomatopoeic adverb tagged `formal` while its own notes call ⟦徐々に⟧ "more formal" —
there the notes *do* contradict the tag, so the existing policy already handles it). Run
the check before sizing the fix.

**Related sub-check with a sharper prior**: any entry with `onomatopoeia` in `pos` or
`semantic` **and** `formality: formal` is almost certainly mistagged — mimetics are
characteristically colloquial. That one is cheap enough to run standalone and is likely
to be high-precision.

### Update 2026-07-30 — the *contradiction* slice is measured, and it is tiny at high precision

The 2026-07-29 polish run's other direction (a tag contradicting the entry's own REGISTER prose)
recurred on **06697 フェス**, tagged `formality: formal` while its REGISTER section read
"Informal/casual. The full form フェスティバル is more formal." This harvest scanned the corpus for
it, and the result is a useful lesson about how tightly to write the check:

| Check | Hits | Character |
|---|---|---|
| `formality: formal` **and** the word informal/casual/colloquial appears anywhere in the notes | 1,238 | Mostly **noise** — notes routinely say "more formal than the informal X" |
| `formality: formal` **and** a `REGISTER:`/`TONE:`/`STYLE:` line whose own characterization *opens* with Informal/Casual/Colloquial/Slang | **6** | Clean: 06955, 07352, 07365, 07367, 07398, 07411 — all `REGISTER: Casual` |
| The converse (`informal`/`vulgar` tag vs a REGISTER line opening "Formal") | **0** | — |

So the deterministic, zero-judgment slice is **6 entries** and the anchor that makes it precise is
*the position of the word inside the REGISTER line*, not its presence in the notes. Worth shipping
as written (`^(REGISTER|TONE|STYLE)[^:：]*[:：]\s*\**\s*(Informal|Casual|Colloquial|Slang)` vs
`formality: formal`); the 1,238-hit loose variant is a model's job, not a checker's, and belongs
to the accuracy reviewer's register dimension if anywhere.

Schema note for whoever writes the fix: the enum is `formal`/`neutral`/`informal`/`vulgar`, so the
correction target for a `REGISTER: Casual` entry is **`informal`**, not `casual`.

## 53. `review_accuracy.py` wrote an empty `description` on every issue it raised

**Source**: 2026-07-31 routine systemic-fix run (`link-target-baseform-disagreement`)

All **26** issues raised in that run came back with an empty `description`, leaving `suggestion`
as the only adjudicable content — bare destinations like `"-> general"` and `"-> cognition"`.

Adjudication still worked, because a tag suggestion is largely self-describing. But an
`error`-severity flag whose entire evidence is a severity label, a dimension name, and a
destination is thin, and **a flag with no stated reason is one a future run cannot audit** —
which matters directly for the [decisions ledger](../topics/quality-metrics.md), whose whole
purpose is retrospective precision measurement.

Two candidate causes, cheap to distinguish: the field is being dropped by the response parser,
or it is never requested in the prompt for that dimension. Worth checking whether the same
emptiness appears on `gloss`/`translation` issues or only on `tags` — if only `tags`, it is a
prompt-template gap rather than a parser bug.

**Resolved 2026-08-06 — misdiagnosed. There is no `description` field; the field is `concern`,
and it is populated.** A 2026-08-06 accuracy-review run reported this item as a reader-side
field-name mismatch, and the check confirms it: `build/review_accuracy.py:185` specifies the issue
object as `{"dimension", "location", "severity", "concern", "suggestion"}` — `description` was
never in the contract — and a scan of the most recent reports finds `concern` present and
non-empty on every issue. Nothing is being dropped by the parser and nothing is missing from the
prompt. **The two candidate causes above are both answered "neither".**

Kept rather than deleted, for two reasons. The first is that as written this item would send
someone to patch a script that is behaving correctly — the concrete cost of leaving a
misdiagnosis on a backlog. The second is that the *residual* point survives its own diagnosis: a
flag whose evidence is a severity label and a bare destination is thin, and that is a real
property of the `tags` dimension's output, where `suggestion` really does read `"-> general"`. But
the fix for that is a prompt asking for a denotational justification, not a field-plumbing repair
— and it belongs with [item 75](#75-the-accuracy-reviewer-assigns-different-severities-to-the-same-defect-class), which is about the same dimension's other unreliable
metadata. **Status: no code change. Read together with 75.**

*Process note*: this is the second backlog item in three days whose premise dissolved when
someone ran the check instead of re-reading the item ([P22](cleanup-backlog.md#priority-22-inconsistent-free-text-part_of_speech-display-field)
was the first, 2026-08-04). Both had sat for weeks. See [Instrument Defects](../topics/instrument-defects.md).

## 55. Detector: contrast words named in notes prose but absent from `cross_references`

**Source**: 2026-07-31 routine polish run (priority lane, basic-tier verbs)

Six of eight priority-lane entries named a contrast word **in prose** — 覚える→習う,
洗う→拭く/すすぐ/磨く, やめる→続ける, 軽蔑→見下す/馬鹿にする — with no corresponding
`cross_references` object. The relationship is therefore invisible to the site's navigation and
to `check_semantic_clusters.py`: the prose is doing work the structured field exists to do.

The extraction is mechanical where the prose is already linked: take every `⟦…：entry_id⟧` that
appears inside a `SIMILAR WORDS` / `Different from` / `Opposite:` / `CONTRAST` note section, and
diff those target IDs against the entry's `cross_references` target IDs. Report the difference.
Because the section heading supplies the *relation type*, the detector can even propose the
right `type` value rather than leaving it blank.

Two caveats worth building in: it only sees entries that are already inline-linked (i.e. the
below-frontier corpus — see [Inline Link Integrity](../topics/inline-link-integrity.md)), and
not every prose mention deserves a structured ref, so this is a `verify: per-entry` queue rather
than a mechanical sweep. Closely related to
[item 52](#52-does-check_semantic_clusterspy-count-a-prominent_see_also-mention-as-satisfying-the-pair-requirement),
which asks the mirror-image question about `prominent_see_also`.

### Measured 2026-08-05 (sixth and seventh filing) — 2,795 entries, and it is two populations

Two more runs filed this shape (basic/core nouns 00486 年 / 00507 部屋 / 00631 一月 with rich
notes and an empty `cross_references`; a priority lane that hit it 6 times out of 6), so the
2026-08-05 harvest ran the detector this item specifies against all 30,205 entries. It works, and
the result splits cleanly:

| Predicate | Entries | Missing refs |
|---|---|---|
| Any inline link anywhere in a relation-bearing section | 3,050 | 6,755 |
| **Link at the head of its bullet** (the reliable signal) | **2,795** | **5,391** |
| ├─ discrimination sections (`SIMILAR WORDS`, `CONTRAST`, `OPPOSITE`, `COMPARISON`, …) | 1,402 | 2,395 |
| └─ thematic sections (`RELATED TERMS`, `RELATED WORDS`, `RELATED VOLCANIC TERMS`, …) | 1,470 | 2,999 |
| of the bullet-leading set: `cross_references` empty entirely | 858 | — |

Four things the measurement settles:

1. **Bullet position is the filter.** Requiring the link to *lead* its bullet removes 1,364
   hits, and inspection says they are the right ones to remove: mid-bullet links are
   collocational tokens, not the named neighbour. `00053 学科`'s CONTRAST bullet reads
   `学科試験 vs 実技試験`, so a position-blind scan proposes a `contrast` ref to
   `01422_shiken` (試験) — a word the bullet merely uses.
2. **The two halves are different asks.** `SIMILAR WORDS` / `CONTRAST` is near-synonym
   discrimination — precisely what `cross_references` exists to record, and where the section
   heading supplies the `type`. `RELATED VOLCANIC TERMS` on `00045 噴火` is a semantic-field
   roster; promoting its four links would make `cross_references` a topic index. The
   discrimination half (1,402 entries / 2,395 refs) is the batch-ready one; the thematic half
   is a convention question of the same shape as [Cleanup P38](cleanup-backlog.md)'s lexical
   families.
3. **The relation type is derivable**: `related` 4,820, `contrast` 488, `antonym` 41,
   `homophone` 22, `synonym` 20 — from the header alone, against the corpus's existing
   `related`/`synonym`/`antonym`/`contrast`/`homophone`/`see_also`/`pair`/`keigo` vocabulary.
4. **The caveat above is confirmed exactly**: 3,043 of the 3,050 affected entries sit below ID
   07000, 5 in the 7000s, 2 in the 9000s. This item can only ever see the inline-linked corpus,
   so its scope grows only as the frontier lane advances — and each entry the lane polishes is
   an entry this detector can then check.

Per-entry load is small (676 entries need 1 ref, 509 need 2, none more than 5), which is what
makes the discrimination half worth a queue rather than a curator decision.

## 56. Nothing checks that a headword carries furigana

**Source**: 2026-08-01 routine systemic-fix run (`27889_ageru`); measured dictionary-wide by the
2026-08-02 wiki harvest.

`headword` is the only Japanese-bearing field in the schema with **no format constraint at all**:
`{挙|あ}げる` and `挙げる` both validate. `find_missing_furigana.py` reads examples and notes;
the furigana screener reads example text; `check_furigana_format.py` checks the shape of wrappers
that exist, not their absence. So the field that renders as the page's `<h1>` is checked by
nothing, and **248 entries (0.95% of kanji-bearing headwords) ship without ruby** — see
[Cleanup P36](cleanup-backlog-resolved.md#priority-36-headwords-written-as-bare-kanji-with-no-furigana-braces-248-entries).

The check is trivial and the corpus is already 99.05% compliant, which makes this an ideal
**ratchet** in the sense of `validate_tags.py --check-no-new-unknown`: bare kanji in `headword` is
an error for new and modified entries, with the 248 known cases baselined until swept. The
predicate is one line — strip `{…|…}` groups from `headword`, then test for any character in
`[一-鿿]`.

Worth doing as one pass with
[item 47](#47-cross-reference-headword-fields-are-invisible-to-every-furigana-instrument-7-confirmed-defects):
both are the same bug (a Japanese-bearing field outside `examples`/`notes` that no instrument
visits), and the fix is a shared list of "every field that can hold Japanese" that the furigana
checkers iterate rather than a hard-coded pair of field names. That list would also pick up
`fixed_patterns` and structured-field prose, which item 22 raised separately.

**RESOLVED 2026-09-13.** `build/validate.py` now carries `find_bare_kanji_headword_errors`: a
hard ERROR, no baseline, for any kanji in `headword` outside a `{kanji|reading}` group (the
corpus was already at zero after the 2026-09-06 sweep, so no ratchet/baseline file was needed).
Item 47's cross-reference-headword gap is unaddressed and stays open separately.

## 96. `find_missing_furigana.py` never scans the `headword` field

**Source**: 2026-08-09 routine polish observation; **confirmed in the source and measured at 259
entries** (see [Cleanup P52](cleanup-backlog-resolved.md#priority-52-kanji-headwords-with-no-furigana-at-all-259-entries--invisible-to-every-furigana-instrument)).

The script reads `headword` at line 101, then builds `fields_to_scan` from notes, definition
explanations, and examples — and never appends the headword to it. The field is used only to
label output rows. `make check-furigana` therefore reports a bare-kanji headword as clean, which
is why 259 of them accumulated with 24 added in the first ten days of August alone.

**Fix**: append `('headword', headword)` to `fields_to_scan`. One line, and it converts P52 from
a recurring cleanup into a one-time one. Worth pairing with a `validate.py` check so new entries
cannot introduce the defect at all — the project's stated rule ("all kanji must have furigana —
in headwords, examples, AND notes") already justifies it as an error rather than a warning.

**RESOLVED 2026-09-13.** `find_missing_furigana.py` now scans `headword`, and `validate.py`
hard-errors on bare kanji there too (see [item 56](#56-nothing-checks-that-a-headword-carries-furigana)).
Re-verified 0/30,683 entries flagged by the fixed scanner.

## 105. Closed, not filed: extending `TAG_MIGRATION` (fourth proposal)

Measured this harvest: `TAG_MIGRATION`'s nine rows fully clear **111 of the 1,364 entries
carrying off-vocabulary semantic tags (8.1%)**, covering **135 of 1,635 instances (8.3%)**. The
residue is 477 labels with 243 singletons; the fifty most frequent cover 48% of instances.

The obvious inference is "extend the map." It has been proposed four times now (2026-07-27,
2026-08-01, 2026-08-02, and implicitly by the 2026-08-11 accuracy-review observation that these
flags "are far cheaper to obtain from the deterministic `VALID_SEMANTIC` membership check than
from a paid model call"), and it was **decided against on 2026-08-07** after measurement, on the
`unknown-semantic-tags` queue item: a static map must pick a destination **per tag name**, and
the tail is 486 names most of which occur once, whereas the reviewer picks one **per entry**,
never has to generalise, and runs at 99.4% precision for ~$0.5 per 1,000 entries.

The 8.1% figure is that decision confirmed from the other side, so this item exists to close the
loop rather than to open work. What the measurement legitimately supports:

- The head of the tail is **not** a rename problem. `place` (29) and `location` (27) need a
  ruling on whether a common-noun location concept goes to `geography` or stays `general`,
  because `place-name` is reserved for proper nouns. `loanword` (23) is a **category error, not
  a synonym** — it says where a word came from, not what it means, and has no in-list target at
  all. Those are curator taxonomy calls, which is exactly what the 2026-08-06 note said was
  blocking, and they do not become tractable by being written into a Python dict.
- The membership check *is* free and *is* worth running — as a **filter on where to send the
  reviewer**, not as a fix. Cleanup P20's block table is that filter: 09000–09499 at 48% and
  08000–08499 at 40%.

**One thing to fix, cheaply**: §A's semantic-tag policy in `prompts/routine2.md` tells the
adjudicator that "`build/check_tag_drift.py` has the 1:1 migration map," which reads as though
applying it were the job. It covers one entry in twelve and, by the decision above, always will.
One sentence.

## Retired 2026-08-12: the katakana `word_id_lookup` gap does not exist

Filed by the 2026-08-11 polish run: "`build/word_id_lookup.json` is keyed `by_headword` /
`by_reading`, but katakana headwords (ベテラン) are only reachable by headword while the schema
demands a hiragana `reading` in cross-references. Adding a katakana→hiragana reading field would
prevent the schema failure this run hit."

Measured:

```
ベテラン → by_headword: yes   by_reading['べてらん']: yes   by_reading['ベテラン']: no
アイコン → by_headword: yes   by_reading['あいこん']: yes   by_reading['アイコン']: no
by_headword['ベテラン'] = [{'id': '11121_beteran', 'reading': 'べてらん', ...}]
```

The hiragana reading the schema wants **is already the `reading` field of the record the headword
lookup returns**, and the hiragana key already resolves. What failed was a katakana query against
a hiragana-keyed index. No tool change is warranted; the fix is one sentence in the
`inline-word-links` and `cross-reference-entry` skills — *look katakana headwords up by headword
and read `reading` off the record; `by_reading` is keyed in hiragana* — recorded here rather than
made, since skills are out of scope for a knowledge-base session. (This also removes the premise
of the filter on queue item `inline-link-block-06800-07100`, which defers that block partly
because "the lookup answers katakana from `by_headword` only, tooling item 76.")

Second retirement in two harvests of a filing that blamed an instrument for a usage error, and
the pattern is worth naming: both were written by a run that hit a failure, formed a plausible
cause, and filed it without querying the artifact it was accusing. **A filing against a data file
should quote the lookup that failed.** That costs one line in the observation; not having it
costs a tooling item and a harvest to retire it.

## Retired 2026-08-12: the `style: ["literary"]` template hypothesis

Filed with the 06881 fix — "worth checking whether the same batch applied `literary` by template
elsewhere." Measured across 06800–06999: **zero entries** carry `style: ["literary"]`. 06881 was
a single mis-tag, correctly fixed, with no batch behind it.

### Correction: the `style: ["literary"]` retirement does not reproduce

Retired on 2026-08-12 with: *"Measured across 06800–06999: **zero entries** carry
`style: ["literary"]`."* Re-run this harvest over the same range: **five entries do** — 06879
運命, 06897 眉をひそめる, 06903 耳を傾ける, 06954 残らず, 06971 よろめく. Three of the five
(06879, 06954, 06971) were last modified *before* the retirement was written, so they carried the
tag at the time it was measured.

The conclusion the retirement drew still holds on the evidence available now — dictionary-wide,
`literary` appears on **443 entries**, which is a normal style label rather than a batch artifact,
and the contradiction the 2026-08-13 polish run proposed to sweep (`literary` co-occurring with
`formality: informal`) is **3 entries** corpus-wide: 02792 けち, 06000 郷愁, 07400 巡り合わせ. No
cleanup item is warranted, and やっぱ was correctly fixed by hand.

What does not hold is the *number*, and that matters more than the verdict: a retirement is the
strongest thing this wiki writes, and one written on a measurement that does not reproduce is
worse than no retirement. Recorded on
[Instrument Defects](../topics/instrument-defects.md) as case 10, with the practical rule —
**a filing that retires an item should quote the command it ran**, the same discipline the
2026-08-12 retirement note asked of filings that accuse an instrument.

### 122. `add_conjugations.py`: single-kanji サ変 verbs take 〜せる, not 〜できる

**Source**: the 2026-08-14 new-entries run, which hit it while creating 30647 処する.

The generator emits 〜できる as the potential for every `conjugation.type: "suru"` verb. Correct
for 漢語+する (勉強できる); wrong for the single-kanji サ変 verbs, which take 〜せる (愛せる,
発せる, 接せる). Scope measured at **32 live entries** (Cleanup P59). Detection is exactly the
rule the filing proposed: `type == "suru"` and the pre-する portion is one character.

**Fix the generator before sweeping the 32**, or the next `add_conjugations.py --force` run puts
all of them back. This is the standing lesson from the P16 `[Register:]` artifacts: a data
cleanup whose generator is unfixed is a scheduled regression.

**RESOLVED 2026-09-12.** `_generate_suru_forms()` now checks the furigana-stripped length of the
プレ-する prefix and emits 〜せる/〜せない when it is a single character, 〜できる/〜できない
otherwise; verified against 08053 察する (single-kanji, now せる), 00527 勉強する (multi-kanji,
still できる) and 30647 処する (the one hand-fixed entry, output now matches byte-for-byte). Full
`build/tests` suite (426 tests) still passes. The 32-entry sweep this unblocked is recorded at
Cleanup P59.

### Retired 2026-08-15: both proposed formality detectors

The two formality detectors filed on 2026-08-14 (REGISTER-line contradiction; formality read off
a neighbouring collocation) do not survive measurement — 8 hits with ~2 real, and 419 hits
dominated by the correct case respectively. The commands and the full argument are in
[Cleanup Backlog → Retired 2026-08-15](cleanup-backlog-resolved.md#retired-2026-08-15-both-proposed-formality-detectors).
The existing queue item `tag-formality-contradicts-register-note` is updated to record the
measurement rather than left implying a live batch.

### 130. `check_furigana_format.py` cannot see okurigana swallowed into the ruby — SHIPPED (2026-09-14)

**SHIPPED**: `build/check_okurigana_ruby.py` implements the detection rule below as a read-only
review-queue generator (`--json`/`--summary`/`--range`), mirroring `check_furigana_format.py`'s
shape. A 2026-09-14 systemic-fix run used it to fix 77 of 121 instances found at scan time (30
were genuine exceptions, left as-is); see [Cleanup P64](cleanup-backlog.md).

**Source**: 2026-08-16 polish run — 04651 {関節痛|かんせつつう} carries `{痛|いたみ}` in its
notes, where the correct form is `{痛|いた}み`. The run asked whether the detector sees this
shape.

**It does not.** `check_furigana_format.py --json` returns 765 findings and **04651 is not
among them** (verified 2026-08-16). The shape is invisible to every furigana instrument the
project has, for the same structural reason the katakana case was (item 121): the checks all
ask "does this kanji have a reading?", and here it does — the reading is simply too long,
having eaten the okurigana that belongs outside the wrapper.

**A detection rule that works, with the population measured.** For a single-kanji base K with
reading R, flag R when some proper prefix of R is a *common* reading of K elsewhere in the
dictionary (threshold: R occurs ≤3 times, the prefix ≥10). Measured across all single-kanji
wrappers: **90 distinct (kanji, reading) pairs / 123 instances**, and 04651 is in the set. The
signal is extremely strong at the head — `{切|きり}` ×1 against `{切|き}` ×3,631, `{入|いれ}` ×1
against `{入|い}` ×2,785, `{付|つき}` ×1 against `{付|つ}` ×2,585, `{痛|いたみ}` ×1 against
`{痛|いた}` ×810.

**Not purely mechanical, and the exceptions are visible in the same output**: `{止|とど}` is a
genuine reading (とどまる), and some entries legitimately wrap a whole word. At 123 instances
the class is small enough to verify per entry, which is the standard §B shape. Filed as
[Cleanup P64](cleanup-backlog.md).

### Correction: `word_id_lookup.json` is not undocumented, and one of the two named files is already right

The 2026-08-17 polish run reported that "CLAUDE.md and comprehensive_polish.md both describe
`build/word_id_lookup.json` as if it were a flat word→id map", costing each session a probe
call to discover the real shape.

Half-refuted on inspection. The file is
`{metadata, by_reading, by_headword}`, and:

- `CLAUDE.md:86` does say "Pre-built word→entry_id map", which is loose.
- **`prompts/comprehensive_polish.md:82` is already accurate** — "look up entry IDs by reading
  or headword" names both indexes.

So the fix is one word in CLAUDE.md's file-listing line, not a correction to the polishing
prompt. Filed here rather than as a numbered item because it is a documentation typo; recorded
for the curator, since wiki sessions do not edit `CLAUDE.md`.

### Re-discoveries needing no new item

- **The note scorer should credit `・`-bulleted blocks** (2026-08-21 polish run) — already
  recorded inside item 20's **structured-note credit** recommendation since 2026-07-02, which
  names `・`-bulleted collocation/forms blocks explicitly. The harvest measured the distortion
  it causes (24 of the top 100 priority lines against an 8.1% base rate, a 3× enrichment) and
  recorded it under [Cleanup P62](cleanup-backlog.md#p62-update-the--penalty-is-real-3--and-it-is-not-the-binding-defect);
  the fix stays part of item 20.
- **Candidate-add should normalize okurigana before comparing** (2026-08-22, 思いつき against the
  existing 27771 {思\|おも}い{付\|つ}き) — this is the fix already written into items 41/43 by the
  2026-07-30 update. Third sighting, no change to the item.

### Re-discoveries needing no new item (2026-08-27)

- **`manage_candidates.py add-batch` duplicate-gating works** (2026-08-24 polish: 13 proposed,
  9 rejected as exact matches against existing entries). Recorded as a positive confirmation, not
  a defect — and the 9/13 rate is a useful calibration: "this word feels uncovered" is a poor
  signal while writing an entry, so propose generously and let the gate filter.
- **The unknown-semantic-tag baseline goes stale after every migration** (2026-08-24): regenerating
  it removed 1,752 entries' worth of tolerance the ratchet no longer needed. CLAUDE.md already says
  to run `--write-unknown-baseline` after a migration pass; this is an adherence gap, not a
  missing tool.

### 140. `score_note_quality.py` does not recognise `COMMON COLLOCATIONS` as a patterns section — 5,748 entries penalised, and it is what the notes priority list is mostly ranking

A 2026-08-29 polish run reported that low note scores in the 40s–60s "are very often caused by a
missing *required section header*, not thin content", from seven priority-lane entries. Measured
dictionary-wide, the claim holds at a scale the run could not see, and the cause is one line of
the scorer.

**The population.** 9,067 entries have a POS whose `note_templates.json` entry declares required
sections. **5,748 of them (63%) carry substantive notes — 250 characters or more — while missing
at least one required section.** Only **2** entries in the whole dictionary are short *and*
missing one, so this is not a thin-content class at all.

| POS | Long notes missing a required section | Of scored | Rate |
|---|---|---|---|
| `verb-suru` | 2,965 | 3,715 | 79.8% |
| `verb-godan` | 1,206 | 2,042 | 59.1% |
| `adjective-na` | 774 | 1,621 | 47.7% |
| `verb-ichidan` | 449 | 823 | 54.6% |
| `adjective-i` | 214 | 468 | 45.7% |
| `adjective-no` | 104 | 269 | 38.7% |
| `particle` | 27 | 52 | 51.9% |

**The cause.** `find_sections` matches `common patterns` through the variant list
`[r'common pattern', r'patterns?:']`. **2,499 of the 2,965 verb-suru entries missing it (84%)
write the section as `COMMON COLLOCATIONS:`** — which the same function happily matches to the
*optional* section `collocations`, so the material is recognised, credited at optional weight,
and then the required-section test fails on the name. Only 87 of the 2,965 have no ALL-CAPS
header at all. The adjective-na half is the same shape: of the 774 missing `usage`, the headings
actually present are `COMMON COLLOCATIONS` (487), `SIMILAR WORDS` (401), `FORMS` (223) and
`COMMON PATTERNS` (124).

**What it costs.** Required sections are worth 30 of the 100 points, and `verb-suru` declares
exactly one required section — so every one of those 2,499 entries is capped at 70 for a heading
name. That is enough to dominate the ranking: of the **worst-scoring 100 entries in
`polishing/priority/notes.txt`, 76 are in this class**, against a dictionary-wide base rate of
18.8% — a **4× enrichment**. The priority lane is, in its top stretch, ranking a vocabulary
mismatch.

**Two fixes, and they are not equivalent.** Adding `common collocation` to the `common patterns`
variant list (and `collocations`/`forms` to `usage`) is one line and rescores thousands of
entries at once. Renaming the headings in 2,499 entries is a large sweep that changes no
content. The first is almost certainly right — the scorer's whole variant table exists to
absorb exactly this kind of synonymy — but it silently moves thousands of entries up the
ranking, so it is recorded here as a curator call rather than applied by an unattended run.
Whichever is chosen, **the notes priority list should not be trusted for lane planning until it
lands**: it is currently measuring heading vocabulary as much as note quality.

### 143. Demote katakana base forms out of `check_stale_noentry.py`'s mechanical bucket — 22 of 123 pairs, and it removes every known false positive

Two runs asked for a fix to the same recurring false positive from opposite ends. One proposed a
hard-coded denylist for the ロック → `08116_rokku` pair after its **fifth** firing (04562, 05762,
05909, 06464 — four of the sweep's rejections come from that one target). The other reported a
new shape at 06574, where コーラスパート's パート resolves to `03106_paato`, an entry covering only
パート = part-time work, and noted that because the target makes no self-declaration, **no
notes-scanning rule can see it** — correctly ruling out the refinement filed as
[134](#134-demote-same-reading-self-declared-homophones-out-of-check_stale_noentrypys-mechanical-bucket).

Both are instances of one family — *the target entry silently covers a different sense of the
same word* — and the family does have a machine-visible tell, just not in the target's notes.
It is in the base form: **the word is a katakana loanword.** Of the detector's 123
mechanical-bucket pairs, **22 have an entirely katakana base form**, and reading all 22 against
their targets:

| Verdict | Count | Examples |
|---|---|---|
| Target covers a **different sense** | 8 | ロック ×4 (lock → "rock (music)"), パート (voice part → "part-time work"), バー (scroll bar → "bar, drinking establishment"), コマ (comet's coma → "frame, panel"), フライ (baseball fly → "deep-fried food") |
| Target is right | 14 | パン, コーンスープ, ポタージュ, アンティーク ×2, ドラマチック, オファー, クレカ, ラベンダー, セラミック, … |

So the katakana subset is 18% of the bucket and holds **every instance of this family either
filing run found, plus three neither had spotted**. The rule is one predicate — base form matches
`^[ァ-ヶー]+$` → judgment queue, not mechanical — and it needs no per-target denylist, no notes
scan and no new data. It costs 14 correct pairs a human glance and buys 8 mislinks that would
otherwise be written automatically.

The reason it works is a property of the dictionary rather than of the checker: a katakana entry
here almost always documents **one** borrowed sense of a word that was borrowed more than once,
so same-spelling-different-sense is the *normal* case for loanwords and the exceptional one for
native vocabulary.

**RESOLVED 2026-09-15.** `MECHANICAL` in `check_stale_noentry.py` is now `("A1",)`; a katakana-base
match still classifies as A2 but no longer reports `mechanical: true`, so it lands in the same
per-entry judgment queue as A3/B/C instead of being auto-fixed. By the time this ran, the
detector's live mechanical bucket already held 0 A1/A2 pairs — the 22 measured on 2026-08-31 had
already been cleared by intervening new-entries/systemic-fix runs — so no entries needed a hand
fix this pass; the change closes the false-positive path for future A2 hits.

### Re-discoveries needing no new item (2026-08-31)

- **`reviews/queue.txt` rose a fourth consecutive window** (10,755 → 10,788, +33 against 343
  entries changed) — Tooling 94's `reviewed_at >= modified` predicate, unshipped; the standing
  rule that the queue length should not be quoted in either direction still holds.
- **The furigana screener yields nothing on polished ranges** — 7 of 222 flagged, all rejected,
  every one in a documented false-positive family. Fourth consecutive window at 0–5%. Recorded
  in Quality Metrics; the retirement case rests on opportunity cost, and item 141 above is the
  sharper version of it.
- **`word_id_lookup.json`'s `by_reading` returns a list of homographs**, so any helper that shows
  only the first few can hide a real entry and produce a wrong `noentry` marker (よう returned
  よう/〜用/要, hiding 酔う at 14437). The standing practice — run `check_duplicate.py` or attempt
  `manage_candidates.py add` before writing a `noentry` marker — is what caught it, which is an
  argument for making that check the documented last step rather than a lucky accident. Already
  filed among the 2026-08-27 prompt recommendations.

