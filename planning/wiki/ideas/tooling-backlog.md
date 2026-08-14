# Tooling Backlog

**Last updated**: 2026-08-13 (harvest of the 26 observations from the 2026-08-12/13 runs — **four new items, one escalation, one long-running item confirmed again**. **109 is escalated to the curator**: the Routine's CI gate waits with a *backgrounded* `sleep 30` that returns immediately, so an unawaited poll loop spends its whole ~16-poll budget in under a minute and reads "still running" as "the API is stale" — the likely explanation for all three stale-`get_check_runs` reports, and a one-sentence fix in a prompt this session may not edit. **110**: `review_accuracy.py`'s `reviewed_at` is not stamped at write time, which blocks both items 94 and 107, since both consume it. **111**: the accuracy reviewer's `tags` dimension should report only off-vocabulary tags — its not-in-list flags run 87–99% applied, its in-list substitutions ~5%. **112**: `check_duplicate.py` is blind to kanji/kana variants of the same word, to kana-headword entries queried by kanji, and to new senses of existing words — four of twenty-four candidates in one batch. Item 20 gains its first throughput number: 39 priority lines read to find 4 workable entries.) Prior 2026-08-12 (wiki harvest of the 26 loose 2026-08-11/12 observations — **three new items, two retirements, one proposal closed**. **105 closes rather than opens**: `TAG_MIGRATION`'s nine rows clear **8.1%** of the 1,364 off-vocabulary-tagged entries, which is the 2026-08-07 decision confirmed from the other side — a static map picks a destination per *tag name* (486 names, 243 singletons) where the reviewer picks one per *entry* at 99.4% precision — so the map stays at nine rows, this being the fourth proposal to extend it; the head of the tail (`place`, `location`, `loanword`) is a curator taxonomy call, and `loanword` has no in-list target because it is a category error. **New 106**: a `links` dimension for `review_accuracy.py`, fourth request, second measurement — **0 of 13 flags on a link-only run concerned a link** — now with a stated rule to check (same-lexeme, which separates the 朝日新聞 family from the 猫に小判 family). **New 107**: check for existing `reviews/accuracy/{id}.json` before paying for a pass; same predicate as Tooling 94, and the reason §A's "400–600 entries per run" is only honest on pre-covered ranges at the measured 1.5–2.6 entries/min. **New 108**: the **59 dangling cross-references** `check_artifacts.py` correctly suppresses are a candidate vein at a ~2% duplicate rate by construction, only 1 of 59 queued, against the 72–100% duplicate rates the candidates run measured on common-vocabulary lenses. **Retired**: the katakana `word_id_lookup` gap — `by_reading['べてらん']` resolves and `by_headword['ベテラン']` carries the hiragana reading, so this was a katakana query against a hiragana-keyed index, the second usage-error-filed-as-defect in two harvests — and the `style: ["literary"]` template hypothesis (**zero** entries in 06800–06999).) Prior 2026-07-27 (wiki harvest of the 17 loose 2026-07-27 observations — **three new items** and six updates, the theme being work a model was paid to do that a string comparison would have done: **new item 38** — `review_accuracy.py --ids` overwrites `reviews/accuracy/{id}.json`, so a §4 self-check destroys the §A review record for exactly the entries that changed; **new item 39** — cross-reference-pair tag consistency (06528 連勝 `formal`/`action` vs 06529 連敗 `neutral`/`leisure`), a free check whose disagreements prove *one of two* entries wrong, a far stronger prior than any single-entry heuristic; **new item 40** — the conjugation-vs-headword invariant behind 22070 走り続ける, whose whole-word furigana wrapper silently doubled the stem in all 33 generated forms while validating clean. Updates: **item 8** — the no-pipe family finally measured (**887 instances / 616 entries**, absent from every P9 scope estimate); **item 24** — a screen at 13/102 flagged / **0 applicable**, plus the two deterministic fixes (stop scheduling screening past the accuracy frontier; drop flags whose quoted reading isn't in the file); **item 11** — a *second* consecutive cycle of a polish run improvising its own link checker and finding real dead links; **item 6** — the ~50-rename `TAG_MIGRATION` extension and a free `domain-tag-in-semantic-slot` check; **item 23** — the candidate pool quantified at **~1,030 of 1,044** entries of corpus residue in four decidable families; **item 20** — the exact heading strings behind the scorer's section-name mismatch; **item 34** — fourth report, `CLAUDE.md` attribution re-verified false.) Prior 2026-07-26

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

## 7. Polysemic kanji-variant overlap detector

**Source**: Wiki maintenance 2026-05-11 entry exploration

Some polysemic entries have a sense that is largely covered by a separate entry with a kanji-variant headword. Example: 00565_toru (取る) sense 2 ("to take a photo") duplicates the entirety of 00760_toru (撮る). The `prominent_see_also` link makes the relationship navigable, but the duplicated content drifts.

A detector would:
1. Walk through each polysemic entry's sense list
2. For each sense, check whether any cross-referenced or `prominent_see_also` target has the same reading and gloss family
3. Flag the overlap so a curator can decide: keep duplicated for browsing convenience, prune the sense, or convert the sense into a pointer

**Scope**: Lower priority than the tag-drift items above, but a useful long-term audit tool. See [Word Variants](../topics/word-variants.md) and [Handling Homographs](../topics/homographs.md) for the design context.

**Update 2026-07-25 (a concrete worked example, and a sharper detector cut: the overlap is at the *sense* level, not the entry level)**: A 2026-07-25 routine polish run found the exact case this item was designed for and fixed it by hand: **06626 見栄** carried a **sense 2 "kabuki dramatic pose"** with three examples written **見栄を切る**, while **29012 見得** — the correct kanji for that sense — already existed as a full entry. The wrong sense was removed from 06626, the two entries cross-linked, and the 見得を切る / 見栄を張る verb split documented in the notes.

Two refinements to the spec above follow from the case:

1. **The overlap unit is the sense, not the entry.** A whole-entry duplicate check (`find_merge_candidates.py --merge-only`) cannot see this: 見栄 and 見得 are genuinely different entries and *should* both exist. Only one *sense* of one of them is misplaced. The check must compare each sense of entry A against the *whole* of entry B.
2. **The candidate pairs are already computable.** `find_merge_candidates.py` groups by reading, so same-reading / different-kanji pairs are in reach today; what is missing is the per-sense comparison on top of that grouping. That makes this a small addition to an existing script rather than a new tool.

Filed alongside as [Cleanup P8](cleanup-backlog.md#priority-8-unconsolidated-duplicate-expression-entries)'s new "sense-vs-entry split" sub-family, which also records a plain duplicate pair found the same run (01385_kimochi / 02485_kimochi, both 気持ち "feeling, mood").

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

**Update 2026-07-25 (the strongest evidence yet: a single polish run silently introduced NINE dead links, all of which passed `validate.py` clean — and the documented check is the one that fails)**: A 2026-07-25 routine polish run wrote **nine inline links with plausible-but-nonexistent target IDs** (`00478_tomodachi`, `09048_koukyuu`, `09502_noni`, …). Every one of them **validated clean**. They were caught only by an **ad-hoc scan against the set of entry filenames** that the run happened to write for itself; without that improvisation they would have shipped.

The sharp point this adds to the item is that **the documented check is the broken one**. Both `CLAUDE.md` and `prompts/comprehensive_polish.md` advise `python3 build/validate.py --id X | grep -i "word link"` as *the* way to verify inline links — so a polishing session that follows the documented procedure exactly, and sees a clean result, has verified nothing about target-ID existence. The failure is silent, it is introduced by the very sessions whose job is to *improve* linking, and it accumulates invisibly between the rare occasions someone writes an ad-hoc scan.

This makes the item's priority materially higher than "worth running once the gate is built":

- **Minimum viable fix**: have `validate.py` resolve every `⟦…：entry_id⟧` target against the set of existing entry IDs (or `build/word_id_lookup.json`) and report unresolvable targets as an error. The set is already loaded by other build steps, so the cost is negligible.
- **Then run it once dictionary-wide** to size the existing dead-link population — nine were created in a *single* run, so the standing total is unlikely to be small.
- **Related**: [Cleanup P24](cleanup-backlog.md#priority-24-inline-link-base-forms-written-with-furigana-braces) (39 entries whose link *base form* carries furigana braces) is the same blind spot seen from the other side — malformed link internals that no check looks at.

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

**Update 2026-07-24 (leading-bare-`[`-array / prose-preamble intolerance drops single-entry tag flags)**: A 2026-07-23 routine accuracy-review hit a `Failed to parse response` on **06602** even though the model emitted a well-formed JSON array (visible in the truncated output) — the response extractor appears intolerant of a leading bare `[` array or a prose preamble before the JSON, so a legitimate single-entry `tags` flag was silently dropped. Harden the extractor to accept a top-level array and to strip any prose preamble/`json` fences before parsing, matching the robustness already recommended for `review_runner.py` here. Low scope but silent-drop is the worst failure mode (a real correction lost with no error surfaced).

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

**Update 2026-07-13 (the highest-signal generalization: "furigana tokens outside `⟦…⟧` in the `notes` field")**:
A 2026-07-12 routine polish run (frontier 06457–06462) sharpened both the target and the query for
option 2's standalone detector. The residual create-era gap above the polish frontier is specifically a
**notes-field** link gap — the entries' *example* sentences are fully linked, but their notes glossaries
(collocation / pattern / related-terms lists) still carry **bare `{漢字|かな}` furigana with no `⟦...⟧`
wrappers** (see Cleanup P21 update 2026-07-13). The observing run's proposed query is therefore the most
direct form of this detector: **flag any `notes` field containing a furigana token `{…|…}` that is not
inside a `⟦…⟧` inline link** (regex like `(?<!⟦[^⟧]*)\{[^}|]+\|[^}]+\}` restricted to the `notes` string,
or simpler: strip all `⟦…⟧` spans first, then look for any surviving `{…|…}`). This is broader than the
自動詞/他動詞-label slice above (it catches all unlinked content words in notes, the dominant P21 residue)
and is the query the notes-priority ranking has repeatedly *failed* to surface (Tooling item 20): a
dedicated "notes contain furigana outside `⟦…⟧`" detector would target the P21 backlog far better than the
`score_note_quality.py` heuristic, which keeps ranking already-polished basic adjectives at the top instead.
Building this detector is the single highest-leverage unblock for both P21 (`batch_ready:false → true`) and
the item-20 no-op loop (it replaces the mis-firing notes ranking for the frontier-link backlog).

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

**Update 2026-06-29 (the `general`-too-broad noise family now confirmed up in the 11000s)**: A 2026-06-29 accuracy-review run over **11088–11187** flagged 23% of entries (above the 20% noise threshold), but **19 of 23 flags were the same "`general` is too broad/vague, prefer a more specific tag" in-list anti-pattern** — e.g. 11106 窒素→`science`, 11107/11108→`change`, 11161/11102→`action`. Per the 2026-06-11 semantic-tag policy these in-list narrowing nits are **rejected** (only ~4/23 were potentially genuine). This is the seventh independent confirmation, now well above the 03301–~07500 band where the family was originally measured: the `general`-too-broad noise is **range-independent** — it appears wherever entries carry the legitimate `general` fallback tag, not just on already-polished low ranges. Reinforces the unshipped prompt fix (fallback-tag exception + severity rule): the reviewer prompt should down-weight or suppress "`general` too broad" suggestions when the more-specific tag is merely a *narrowing within a valid category*, since they dominate the `tags` dimension and inflate the flag rate without yielding fixes.

**Update 2026-06-30 (eighth confirmation — the `general`/`work`-too-broad family on katakana loanwords + business terms)**: A 2026-06-29 accuracy-review over **11188–11300** flagged **20 of 113 entries (~18%)**, and **all 20 were in-list→in-list narrowness substitutions** — `general`/`work`-too-broad suggestions that the §A tag policy rejects (上場 work→finance, メロディ leisure→music, リピーター work→business). This is the eighth independent confirmation and the second in the 11000s (cf. the 2026-06-29 11088–11187 update directly above), now specifically on the katakana-loanword / business-term band: the noise persists wherever entries carry the legitimate `general`/`work` fallback tags and a more-specific in-list tag is merely *defensible*, not *required*. The observing run's prescription matches the standing one: the reviewer prompt should suppress "too broad" suggestions when the current tag is in `VALID_SEMANTIC` and defensible. Reinforces the unshipped fallback-tag-exception + severity-rule prompt fix; the genuine wrong-domain catches in the same general band are the **P20 11300s off-vocab cluster** ([Cleanup Backlog](cleanup-backlog.md) → P20 update 2026-06-30), which the reviewer migrates correctly — it is only the in-list narrowness layer that is noise.

**Update 2026-07-02 (ninth confirmation — the `general`-too-broad in-list nit dominates again on the 11647–11765 general-tier band)**: A 2026-07-02 accuracy-review over **11647–11765** flagged **29 of 118 entries (~25%)**, above the 20% noise threshold, and ~23 of the tag flags were in-list "too broad/narrow" swaps rejected per policy — of which **13 were "`general` is too broad" alone** (11656/11657/11677/11687/11707/11715/11716/11734/11749 …). The only genuine applies were off-list migrations (`time`→`time-general` ×2, `death`→`law`) and one clear category error (`education`→`grammatical` on 代名詞 "pronoun"). Ninth independent confirmation, still range-independent into the 11700s: the reviewer keeps proposing a more-specific in-list tag for entries carrying the legitimate `general` fallback, and per the §A semantic-tag policy those are rejected. The observing run's prescription matches the standing one and sharpens it: **tune the tags-review prompt to suppress "prefer a more specific in-list tag" suggestions entirely and flag only (a) off-list tags and (b) clear category errors** — the two families that produced every genuine apply this run. Reinforces the unshipped fallback-tag-exception + severity-rule prompt fix.

**Update 2026-07-04 (tenth/eleventh confirmation — 11894–12001, and the formality-downgrade family sharpens the register sub-fix)**: Two 2026-07-03 accuracy-review sweeps carry the family into the low 12000s. (1) **11894–11923**: the `tags` dimension again flagged in-list `general` as "too broad" with a narrower suggestion (11905→`action`, 11907→`law`, 11915→`action`, 11923→`action`), all rejected per the §A policy — a fresh instance of the recurring low-precision in-list-narrowness family. (2) **11924–12001**: **20 of 78 entries (26%)** flagged but only **6 applied**, with two dominant reviewer-noise families in the `tags` dimension — sole-`general`→narrower in-list substitutions (8 cases, rejected) **and a formality `formal→neutral` downgrade family** (5 cases: 厨房, 名高い, 厭う, 原案, 喜ばしい) where **the entry's own notes explicitly describe a formal/literary register** and the reviewer ignored that in-entry evidence. Genuine applies were all off-list migrations (`action-physical`→`action`, `thought`→`cognition`, `interaction`→`action`) plus two clear category errors (助数詞 `education`→`grammatical`, 古びる `existence`→`change`). This is the tenth/eleventh independent confirmation and adds a **concrete strengthening of the register sub-fix** already sketched in the 2026-06-12 secondary-noise note: the tags/register prompt should be told to **consult the entry's own register notes before emitting a `formal→neutral` (or reverse) downgrade** — the formality analogue of the fallback-tag exception. Combined prescription is now precise on both axes: (a) suppress in-list narrowness `general`→specific suggestions, flag only off-list tags + clear category errors; (b) flag a formality change only when the entry's notes/examples *contradict* the current label, never on perceived neutrality. Reinforces the unshipped prompt fix (see also item 26 for the `formality` enum embed).

**Update 2026-07-04 (second) (twelfth confirmation — 12002–12134, 32% flagged)**: A 2026-07-04 routine accuracy-review over **12002–12134** flagged **43 of 133 entries (32%)** — again above the ~20% reviewer-noise line — and the noise was "almost entirely" the same in-list-narrowness family: the reviewer re-flagging in-list `general` (and other valid in-list tags) as "too broad/vague" with a narrower in-list suggestion (増税 general→`economics`, 国政 general→`politics`, 変容 general→`change`), all REJECTs per the 2026-06-11 semantic-tag policy — pure precision drag. Genuine applies this run were off-vocab migrations (thought/economy/spatial/administrative/…→in-list) plus one wago education→language category fix and one 回忌 counting-offset **translation** correction. The observing run restated the same prescription: tune the `review_accuracy` prompt to **suppress "too broad" complaints against `general`/other valid in-list tags** and flag only off-vocab tags or clear miscategorizations. Twelfth independent confirmation; the family is now continuous from the low ranges through 12134, entirely range-independent.

**Update 2026-07-08 (thirteenth confirmation — 12507–13199, ~23% precision on a genuinely-contaminated band)**: Two accuracy-review runs carried the family into the **12507–13199** range. A 2026-07-06 run flagged the noise at 12519/12617/12638/12639/12640/12644/12646/12648/12651/12663/12665 — "`general` is too broad → [narrower]" raised at **error** severity on entries where `general` is a valid in-list fallback, all rejected per the §A policy. A 2026-07-08 run over **12674–13199** flagged **121 of 526** entries on `tags` and applied only **28 (~23%)** — but note this band is *genuinely* contaminated (65 entries carried off-list tags; see [Cleanup P20](cleanup-backlog.md#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration) 2026-07-08), so unlike the earlier already-`general`-tagged bands the rejects here are a mix of in-list narrowness *and* the reviewer proposing narrower in-list tags for the off-list migrations the run handled deterministically. Thirteenth independent confirmation; prescription unchanged (suppress "too broad" against valid in-list tags; flag only off-list tags + clear category errors). The datum this run adds is a caution for the recommended P20 systemic-fix sweep: on a contaminated band the reviewer's raw flag count overstates work by ~4× (121 flagged → 28 applied), so the deterministic `check_tag_drift` migration map, not the reviewer, must drive the sweep — the reviewer is the coverage instrument, not the adjudicator.

**Update 2026-07-10 (fourteenth confirmation — on a genuinely-contaminated band the high raw flag rate is mostly legitimate drift, not noise)**: A 2026-07-10 accuracy-review over the genuinely-contaminated **13350–13549** block flagged **~32%** of entries — above the 20% "noise" line — yet the flag mix inverts the usual reading: the **not-in-list tag flags are high-precision and correct-by-definition** (44 applied as 1:1 migrations, per the §A tag policy), and the reviewer-noise residue was the familiar **`general`-too-broad→narrower in-list** family (~18/200, rejected) plus a few "faithful-translation misread" gloss/translation nits. Net genuine-error rate is well **under** the 20% threshold; the high *raw* rate was mostly legitimate off-vocab tag-drift the run migrated (see [Cleanup P20](cleanup-backlog.md#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration) 2026-07-10), not reviewer over-flagging. This sharpens the standing interpretation: on **already-polished/already-`general`-tagged** ranges a >20% flag rate is the in-list-narrowness noise this item tracks, but on a **genuinely-off-vocab creation batch** the same raw rate is real drift the not-in-list flag catches correctly — the prescription (suppress "too broad against valid in-list tags"; flag only off-list tags + clear category errors) cleanly separates the two, and this run's 44-apply/18-reject split is exactly what the tuned prompt should produce. Fourteenth independent confirmation; prescription unchanged.

**Update 2026-07-12 (sixteenth confirmation — 13725–13874, the two-regime split holds)**: A 2026-07-12 accuracy-review over **13725–13874** flagged **37 of 150 entries (~25%)**, again above the 20% noise line, and the mix was the now-standard two-regime split: the dominant family was the rejected **`general`-too-broad → narrower in-list** narrowness nit (**21 entries**, all REJECTs per the §A policy), plus a **formality-nit false-positive family** on entries whose own notes *support* the `formal` label (the register-note-ignored sub-family, cf. the 2026-07-04 update); the only genuine applies were **4 not-in-list tag migrations** (~11% applicable). Sixteenth independent confirmation; prescription unchanged and now well-worn — suppress "too broad against valid in-list tags," consult the entry's register notes before any formality flag, and flag only off-list tags + clear category errors. (The furigana-screener false positives over this range were again all the model's reading-truncation family — [item 24](#24-non-hiragana-reading-lint-cheap-replacement-for-the-furigana-screeners-true-positive-class).)

**Update 2026-07-14 (seventeenth/eighteenth confirmation — three accuracy-review sweeps across 14187–14899, precision ~17–31%, the two-regime split holds into the 14000s)**: Three 2026-07-13 accuracy-review sweeps carried the family into the mid-14000s. (1) **14187–14386**: **49/200 (24.5%)** flagged, above the noise line; **33 of 48 tag flags** were in-list "too broad/narrow" substitutions (general→science, education→language) or formality flags contradicted by the entry's own notes — all rejected per §A; the **15 genuine applies were all off-vocabulary tags** VALID_SEMANTIC doesn't contain (social, crime, object, commerce, sound, ceremony, result, literature, place, martial-arts, time). (2) **14387–14899** (accuracy-review window of the systemic-fix run): **84 of 114 tag flags** were the in-list `general`-too-broad→specific narrowness family (rejected) and 11 were formality nits unsupported by entry notes (rejected); only **19 off-vocab migrations** were genuine applies — reviewer tag precision here ~**17%**, the "too broad/narrow between in-list tags" family again the dominant noise source. Seventeenth/eighteenth independent confirmation; prescription unchanged and now range-independent well into the 14000s — **flag only (a) off-list tags and (b) clear category errors, and suppress in-list narrowness/broadening substitutions**; consult the entry's register notes before any formality flag. The genuine off-vocab catches feed the [Cleanup P20](cleanup-backlog.md#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration) 14387–14899 migration.

**Update 2026-07-15 (nineteenth confirmation — 14900–15099, the two-regime split holds into the 15000s)**: A 2026-07-14 routine accuracy-review over **14900–15099** flagged **32 of 199 entries** on `tags`, and the mix was again the now-standard two-regime split: **21** were the rejected in-list **`general`-too-broad → narrower** narrowness family, **5** were formality `formal→neutral` nits contradicted by the entries' own register notes (rejected), and only **6** were genuine applies — off-list migrations (medical/manners/body/`daily life`/people → in-list) plus one clearly-wrong tag (`body-part` on 舌打ち, an action not an organ). The observing run restated the standing complaint that the reviewer prompt **still treats `general` as an error** when per the §A tag policy it is a valid in-list fallback. Nineteenth independent confirmation; the family is now range-independent into the 15000s and the prescription is unchanged and well-worn — **flag only (a) off-list tags and (b) clear category errors; suppress in-list narrowness/broadening substitutions; consult the entry's register notes before any formality flag.**

**Update 2026-07-15 (twentieth confirmation — the `general`-too-broad family surfaces on the create-era frontier §4 self-check too, not just accuracy-review sweeps)**: A 2026-07-15 routine polish run's §4 self-check (frontier 06490–06494) had the external model flag in-list `general` as "too broad" on **3 of 5** create-era general-tier entries — 加湿器 → electronics/tool, 除湿機 → electronics, 踏切 → transportation — all **rejected** per the §A tag policy (in-list broad→narrow nit). The datum this adds: the same `general`-too-broad narrowness noise family the accuracy-review sweeps keep producing (nineteen prior confirmations) also fires on the create-era frontier when the §4 self-check reviews *newly-linked* frontier entries, so the tuned-prompt fix (suppress "too broad against valid in-list tags") benefits the per-run self-check lane exactly as it does the whole-range sweeps. Twentieth independent confirmation; prescription unchanged.

 **Update 2026-07-18 (twenty-first confirmation — 15567–15766, the two-regime split holds into the 15700s)**: A 2026-07-17 accuracy-review over **15567–15766** flagged **56 of 200 entries (28%)** on `tags`, above the noise line, and the mix was again the standard split: **~45 genuine off-vocabulary migrations** (`object`, `legal`, `behavior`, `medical`, `housing`, `description`, …) — the real signal in this ~2026-03 pre-closed-vocabulary creation band — versus **~15 low-value in-list `general`-too-broad narrowness substitutions** the reviewer keeps proposing (all rejected per §A). Twenty-first independent confirmation; the family is now range-independent well into the 15000s and the prescription is unchanged and well-worn — **flag only (a) off-list tags and (b) clear category errors; suppress in-list narrowness/broadening substitutions**. The genuine off-vocab catches feed the [Cleanup P20](cleanup-backlog.md#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration) 15567–15766 migration.

**Update 2026-07-22 (twenty-second confirmation — the in-list `general`→specific narrowness family surfaces again on the 16901–17085 frontier accuracy-review)**: A 2026-07-21 routine accuracy-review over **16901–16935** had **3 of 6 tag flags** be the standing in-list `general`-too-broad substitution family — `general`→`culture`/`law`/`media` swaps the §A tag policy rejects (a more-specific in-list tag is *defensible*, not *required*) — and the follow-on 2026-07-22 accuracy-review over the genuinely-contaminated 16936–17085 off-vocab pocket showed the usual two-regime split (45 genuine off-list migrations applied, the in-list-narrowness residue rejected). Twenty-second independent confirmation, now on the 16900s frontier; prescription unchanged and well-worn — **flag only (a) off-list tags and (b) clear category errors; suppress in-list narrowness/broadening substitutions** (tell the reviewer not to flag a valid in-list `general` as "too broad" when the alternative is merely a narrowing within a valid category). The genuine off-vocab catches feed the [Cleanup P20](cleanup-backlog.md#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration) 16936–17085 migration.

**Update 2026-07-23 (twenty-third confirmation — the in-list `general`→specific narrowness family surfaces on the 06583–06584 frontier §4 self-check, at `error` severity)**: A 2026-07-22 routine polish frontier run's §4 self-check had `review_accuracy`'s `tags` dimension flag in-list `general` as too broad on two create-era general-tier nouns — **06583 炭素** (`general`→`science`) and **06584 ビート** (`general`→`music`) — **both raised at `error` severity** and **both rejected** per the §A/§C policy (a too-broad substitution *between* in-list tags is not an error). Twenty-third independent confirmation, and a reminder that this noise family fires on the per-run frontier §4 self-check exactly as on the whole-range sweeps (cf. the 2026-07-15 twentieth-confirmation update): the reviewer keeps treating a valid in-list `general` fallback as an error merely for being broad. Prescription unchanged and well-worn — **flag only (a) off-list tags and (b) clear category errors; suppress in-list narrowness/broadening substitutions**; the recurring `error`-severity mis-classification argues specifically for damping the prompt so a valid in-list `general` is never flagged just for breadth.

**Update 2026-07-26 (twenty-second confirmation — the noise family now measured at 95 instances in one run, ~two-thirds of the whole tag-dimension flag volume)**: A 2026-07-26 accuracy-review over **18653–19200** flagged **155 of 548 entries (28%)**, above routine2.md §A's 20% "this is reviewer noise" threshold. The run then attributed the excess to a single family with a hard count: **95 instances of "replace in-list `general` with a narrower in-list tag"** (`general`→`finance`/`politics`/`art`/`law`), **all rejected** per the semantic-tag policy. That is the first time the family has been counted rather than sampled, and it means the prompt fix filed here would cut tag-dimension noise by **roughly two-thirds** and restore the 20% threshold as a meaningful signal — currently the threshold fires on essentially every sweep, so it discriminates nothing.

The prescription is unchanged and now has a one-sentence form worth pasting into the reviewer prompt verbatim: **`general` is an acceptable terminal tag, and breadth substitutions between two in-list tags are out of scope — flag a semantic tag only when it is absent from `VALID_SEMANTIC` or plainly contradicts the headword.**

The same run also produced the decisive argument for **not using the model as the tag detector at all** (see [Cleanup P20](cleanup-backlog.md#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration)): a deterministic scan found **51** off-vocab entries in the range where the model caught **32**. The model is the corroborator; `check_tag_drift.py --check unknown-semantic` is the detector.

**Update 2026-07-28 (a *second* invented rule surfaces — "suru-verbs must carry the `action` tag" — and the tag dimension is now 96% of all flag volume)**: A 2026-07-28 accuracy-review over **19951–20450** flagged **44% of entries**, more than double routine2.md §A's 20% noise threshold, and the concentration is now extreme: **234 of the run's 244 issues (96%) came from the `tags` dimension alone**. As on the 19701–19950 band, most of that volume is legitimate — a not-in-list flag is correct by construction, and the band genuinely carries off-vocab tags at ~44% (see [Cleanup P20](cleanup-backlog.md#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration) 2026-07-28) — so the raw rate is not by itself evidence of noise here.

What *is* new is a **second invented rule**, distinct from the twenty-plus-times-confirmed "too broad/narrow between in-list tags" family this item tracks: the reviewer asserts that **`verb-suru` entries must carry the `action` semantic tag**. No such requirement exists anywhere — not in `VALID_SEMANTIC`, not in `schema.json`, not in the `entry-guidelines` skill — and it is a POS-conditioned rule about tag *presence* rather than a judgment about tag *correctness*, which puts it outside what the `tags` dimension is asked to do at all.

That matters more than one extra noise family, because it changes the diagnosis. The standing prescription has been "damp the prompt's enthusiasm for narrower tags." Two independently-invented rules suggest the model is **inferring editorial policy from the tag distribution it sees** and then enforcing its inference — which will keep generating new rules as the corpus shifts, and no amount of per-family suppression will get ahead of it. The prompt fix should therefore be **positive and closed** rather than a growing list of prohibitions:

> Flag a semantic tag only if (a) it is absent from the `VALID_SEMANTIC` list supplied above, or (b) it plainly contradicts the headword's meaning. Do not propose additional tags, do not propose narrower alternatives to a valid tag, and do not apply rules about which tags a part of speech ought to carry.

Clause (b) plus the two explicit "do not"s is the whole scope; anything else the model has inferred is out of bounds by construction. Twenty-fourth independent confirmation of the noise problem, and the first that argues the *form* of the fix rather than its content.

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

> **Update 2026-08-01 — the scope is measured, and it is 3,797, not "hundreds".** The
> 2026-08-01 wiki harvest ran the detector this item describes: of 7,320 `noentry` links,
> **3,797 (52%) now resolve**, of which **2,887 have a full headword match with exactly one
> candidate entry** (mechanical) and 883 match only on a single character or a reading alone
> (per-entry — homograph trap). **85% of the stale population points at entries in bands
> 26000+**, i.e. it was created by the last few months of `new-entries` runs and is still
> growing. That makes this item's *incremental half* — the `manage_candidates.py sync` hook —
> the part that matters: it closes the source, while the sweep only clears the arrears. Filed
> as [Cleanup P35](cleanup-backlog.md) with the full stratification; analysis on
> [Inline Link Integrity](../topics/inline-link-integrity.md).

> **Update 2026-08-02 — emit a provenance column; do not build a second detector.** A polish run
> proposed a separate "`noentry` false positive" detector for markers that were *never* correct
> (`01004_tsu` marked 一二三四五六八九 `noentry` when all eight are basic-tier entries older than
> the marker). The harvest measured it: **447 of the 3,809 resolving markers have a target created
> before the source entry** — provably wrong when written — **all of them below ID 07000**, 301 of
> them mechanically safe. That is the same scan, the same queue, and the same one-token fix as
> this item; the only difference is one comparison of two `created` dates. Add it as an output
> column (`wrong_when_written: true`), because such a marker needs no sense-drift check — the
> target existed the whole time. Full numbers in
> [Cleanup P35](cleanup-backlog.md#update-2026-08-02--provenance-split-12-were-wrong-when-written-not-stale-and-that-subclass-is-closed).

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

**Update 2026-07-10 (two more stale markers found incidentally in the priority lane — the recurrence keeps confirming the detector's value)**: A 2026-07-10 routine polish priority lane fixed two more stale-`noentry` markers as its only genuine changes among 6 examined mimetic entries — **05766 にやにや** (`noentry` → now 29117) and **05775 もぐもぐ** (a naked もごもご → `noentry`, the mirror case: a base whose entry does not yet exist, harvested as candidate C22280). The observing run explicitly flagged stale `noentry` markers whose referent now has an entry as "a distinct, tractable signal a detector could catch" — an independent restatement of this item's premise. The recurrence pattern is now well-established: these markers surface one or two at a time through incidental polishing, which is exactly why the cheap mechanical self-healing scan (re-resolve every `⟦…：noentry⟧` against `word_id_lookup.json`) would clear them in bulk instead of waiting for a polish run to stumble across each one.

**Update 2026-07-12 (three more stale markers surfaced incidentally in already-"polished" entries — "likely hundreds dictionary-wide")**: A 2026-07-12 routine polish run found **three** more stale `⟦…：noentry⟧` markers whose base now resolves in `word_id_lookup.json`, all in entries that had already been through polishing: **06484 噛み殺す → 29106**, **06731 御影石 → 29109**, and **07006 ビハインド → 29128**. The observing run made the scale estimate explicit — *"likely hundreds dictionary-wide"* — and restated this item's exact premise: a read-only detector that scans example/note `：noentry⟧` markers and reports any whose (surface/base reading) now resolves in `word_id_lookup.json` would convert these into a single cheap systemic-fix batch instead of the current one-or-two-per-run incidental drip. Reinforces the still-unbuilt `check_noentry_links.py` (unambiguous single-ID resolutions auto-swap; ambiguous readings go to the per-entry judgment queue).

**Update 2026-07-27 (four more concrete instances; the case for a bulk re-resolve pass rather than per-entry discovery)**: The 2026-07-27 polish run found dead `noentry` markers on words that have since been created — **03754 命令文→28285**, **06529 スランプ→29125 / 喫する→29124 / 一勝→29129** — plus **03682 百万人**, which is not a missing entry at all but a splittable compound (百万 + 人). These keep surfacing one at a time because the only thing that looks at a `noentry` marker is a human reading the entry it sits in.

The detector specified in this item resolves the whole class in one pass: re-resolve every `noentry` marker against `word_id_lookup.json` and emit (a) markers whose word now has an entry, with the target ID, and (b) markers whose word decomposes into two linkable entries. Both are review-queue output, not auto-fix — (a) still needs a human to confirm the sense matches, and (b) is a judgment call about link granularity. The recurrence rate (four this run, two in each of several earlier runs) makes this a self-healing scan worth having on a schedule rather than a one-off.

**Update 2026-07-28 (the drip becomes a distribution: seven stale markers in a *single* entry, plus three more elsewhere)**: Two 2026-07-28 polish runs between them found ten more, and one of them breaks the "one or two at a time" pattern this item has documented since June:

- **05091_ryoukai carried seven stale markers by itself** — です, 分かる, かかる, 明日, 時, メール, いい — every one of them a high-frequency word that has had an entry for months.
- Three more singly: **00587 白無垢 → 27472_shiromuku**, **03436 通行人 → 28570_tsuukounin**, and **06662 未払い金**, which like 03682 百万人 in the previous update is not a missing entry but a mis-split compound.

The seven-in-one-entry case is the genuinely new information, and it revises the scale estimate upward in a specific way. The drip pattern made stale markers look **Poisson-distributed** — a low uniform rate, a couple per run, "likely hundreds dictionary-wide." Seven in one entry says they are **clustered by entry age instead**: an entry written when the dictionary was small marks *everything* `noentry`, and every one of those markers goes stale together as the dictionary fills in around it. The population is therefore concentrated in the oldest entries and is plausibly larger than "hundreds" — but it is also **cheaper to clear than a uniform distribution would be**, because the hits arrive in dense per-entry batches where one file open resolves many markers.

That is an argument for running the detector **entry-major and oldest-first** rather than scanning markers uniformly, and it strengthens the case for building it: the ten found this cycle were all incidental, and the entry that held seven of them was reached by the priority lane by luck, not by search.

**Update 2026-07-29 (two more sightings, and the first case where the decay was demonstrably *self-inflicted within the Routine*)**:

- **02983 / 02985 (八日 / 四日)** marked 間, ぶり, and 五日 as `noentry`; all three have had entries for some time (28469_kan, 28358_buri, 28460_itsuka).
- **02985 {四日|よっか}** additionally marked {十四日|じゅうよっか} and {二十四日|にじゅうよっか} as `noentry` — and the **2026-07-29 `new-entries` run created both** (30216, 30217) in the same 24 hours that a polish run was reading the stale markers. The detector this item proposes would have converted them automatically; without it, the dictionary now contains an entry that tells the learner a word has no entry, three doors down from that word's entry.

That second case sharpens the argument. The population is not only decaying passively as the dictionary grows — **the Routine's own `new-entries` mode is a first-class producer of stale `noentry` markers**, at a rate proportional to how well the mode is doing its job. Every date-vocabulary entry written makes the date-vocabulary `noentry` markers staler. So the detector is not a one-off cleanup that can be deferred until the queue is worth the trouble; it is the missing back-edge of the entry-creation loop, and the right place to run it is **at the end of every `new-entries` run over the words that run just created** — a bounded scan of ~20 surfaces against `word_id_lookup.json`, essentially free — with the full entry-major oldest-first sweep (per the 2026-07-28 clustering finding) as the periodic catch-up for the historical backlog.

**Update 2026-07-30 (the implementation site found — `manage_candidates.py sync` already computes exactly the input the detector needs)**: A 2026-07-30 polish run found **05836 ひんやり** marking すーすー and ひやっと as `noentry`; both have had entries (**29047**, **29048**) since they were created from candidates that 05836's own note had queued.

The new information is not the sighting — it is the **placement**. `manage_candidates.py sync` already exists to remove candidates that have become entries, which means it already knows, on every run, the exact set of `(surface, reading)` pairs that just crossed from "no entry" to "has an entry". That set *is* the stale-marker work list, computed for free as a side effect of work the pipeline already does.

This makes the 2026-07-29 update's conclusion concrete. That update established that `new-entries` is a first-class *producer* of stale markers and that the detector is "the missing back-edge of the entry-creation loop"; `sync` is where that back-edge already almost exists. Recommended shape:

- **Incremental (closes the source)** — extend `sync` to rewrite `⟦…→<surface>：noentry⟧` to the new ID for each candidate it retires. Bounded by the size of the sync (~20 words after a `new-entries` run), so the cost is negligible and it runs on exactly the cadence that creates the problem.
- **Historical (periodic catch-up)** — the full entry-major, oldest-first sweep above, for markers that went stale before the hook existed.

The two halves are independent and the first is much the smaller change, so it should not wait on the second.

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

**Update 2026-06-26 (sixth truncation — and the prescription tightened to ≤~100 IDs)**: A 2026-06-25
accuracy-review furigana phase sized its screening range to **9741–10300 (560 IDs)** and **timed out at ~74
entries in ~9 min** (~7 s/entry against single-stream gemini-2.5-flash), the sixth confirmed truncation in three
weeks. The observing run's prescription is **≤~100 IDs/run** (slightly tighter than the standing ~200 figure,
reflecting the shorter wall budget some runs get) **or add batching/concurrency** so the furigana pass completes
inside the Routine's time budget. No new diagnosis — the binding constraint remains the serial per-entry
gemini-2.5-flash latency; option (a) (size the range to the budget) is still the smallest fix, with internal
batching/concurrency (option b/d) the durable one if furigana screening is to cover large ranges in one run.

**Update 2026-06-28 (seventh confirmation — combined screening+deep over a full directory exceeds one run's wall budget)**: A 2026-06-27 routine accuracy-review observation reconfirmed the wall-clock bound from the other direction: `build/review_runner.py`'s screening + deep furigana passes run at roughly **160 entries / ~20 min**, which exceeds the Routine's per-step wall-clock and times out mid-pass when a run tries to cover a full ~450-entry directory in one invocation. Same binding constraint (serial per-entry gemini-2.5-flash latency), same prescription — size a single furigana invocation to the budget (≤~100–200 IDs/run per the 2026-06-26 tightening) or add internal batching/concurrency; consider a faster screening model so a single run can finish furigana over a whole directory. Seventh confirmed truncation-class observation in roughly a month.

**Update 2026-07-03 (eighth confirmation — ~9 entries/min reconfirmed; ≤~150 IDs/run)**: A 2026-07-02 routine furigana screening (`review_runner.py --pass screening`) over the **11766–11893** direction processed at roughly **9 entries/min** and **overran the 900 s (15-min) run wrapper at ~126 entries**, the eighth confirmed truncation-class observation in about six weeks. Per-entry results for the covered IDs were kept. The observing run's prescription is **size furigana screening ranges to ~150 IDs per run** so the pass completes cleanly rather than being SIGTERM-killed — consistent with the standing ≤~100–200 ID band (the exact cap tracks the wall budget a given run receives). Same binding constraint (serial per-entry gemini-2.5-flash latency), same two fixes — size the range to the budget (smallest fix) or add internal batching/concurrency (durable fix), plus a faster screening model as the durable way to cover a whole directory in one run.

**Update 2026-07-13 (ninth confirmation — a 526-ID screen SIGTERM-killed at 214/526 after 25 min)**: A 2026-07-12 accuracy-review furigana screening pass over **13975–14500 (526 IDs)** was killed by the run wrapper at **25 min having completed only 214 entries (13975–14186)**, the ninth truncation-class observation in about seven weeks. Per §A resilience the 214 covered results were kept and adjudicated (the range's cursor advanced only to 14186). At the observed ~9 entries/min this is the same serial per-entry latency, and the prescription is unchanged: **size a single furigana screening invocation to ~150–200 IDs** (the exact cap tracks the wall budget a run receives) or add per-entry timeout/checkpointing + internal batching/concurrency so a Routine run reliably spends its OpenRouter budget instead of being SIGTERM-killed mid-pass. A faster/cheaper screening model remains the durable way to cover a whole directory in one run.

**Update 2026-07-14 (tenth confirmation — the 2-min wall-clock ceiling now forces multiple invocations per systemic-fix self-check)**: A 2026-07-13 systemic-fix run (furigana-cosmetic-wrappers, 11000–12999 slice) reconfirmed that `build/review_runner.py --pass screening` repeatedly hits a **~2-minute wall-clock ceiling on batches of only ~20–30 entries** against `google/gemini-2.5-flash` (~5–10 s/entry, mostly network latency), so a single §4 furigana self-check of one systemic-fix slice now needs **2+ invocations** to cover all its IDs. Per-entry results are written incrementally so nothing is lost, but the friction recurs on every systemic-fix run of this size. The observing run's prescription matches the standing one and adds a concrete option not yet emphasized: besides sizing the range to the budget, add a **`--resume` / skip-already-screened flag** so re-invocation only covers the un-screened remainder (cheaper than re-running the whole slice), or parallelize the per-entry API calls. Reinforces item 21's range-sizing *and* [item 31](#31-per-request-http-timeout--retry-cap-in-the-openrouter-client-runner-hangs-survive-the-outer-timeout-wrapper)'s per-request HTTP timeout + retry cap; a faster/cheaper screening model remains the durable fix.

**Update 2026-07-22 (eleventh confirmation — ~8 s/entry reconfirmed, plus a genuinely-new state-integrity datum: filter "this run's" entries by `screened_at`, not file mtime)**: A 2026-07-21 routine accuracy-review reconfirmed the binding wall-clock bound — `review_runner.py --pass screening` ran at **~8 s/entry**, making the 400–600-entry furigana ranges the §A budget math nominally allows **impractical within one unattended run** (the standing ≤~100–200-ID sizing holds). The genuinely-new datum this window is about the runner's **interrupted-state integrity**, not just its speed: the screener **processes entries out of ID order (it appears to fan out in parallel), so an interrupted pass leaves non-contiguous partial state**, and — critically — the **written file mtime does not match the internal `screened_at` timestamp**, so filtering "the entries this run screened" by file mtime is unreliable and can miss or mis-attribute results. The fix is to **filter by the `screened_at` field the runner already records**, not by mtime. This matters for any §4 self-check or cursor-advance logic that reasons about "which entries did this invocation cover" after a truncation — the same truncation-resilience path items 21/31 already harden. Eleventh confirmation of the range-sizing constraint; the `screened_at`-vs-mtime point is a new, small, self-contained robustness fix for downstream result-attribution.

**Update 2026-07-25 (twelfth confirmation — the first direct side-by-side throughput measurement against `review_accuracy.py`: ~8/min vs ~29/min, a 3.6× gap)**: A 2026-07-25 routine accuracy-review ran **both** review scripts over the same 490-entry range and measured them against each other for the first time: `review_runner.py --pass screening` sustained **~8 entries/min** while `review_accuracy.py` sustained **~29 entries/min** over identical inputs. The consequence is exactly the one this item predicts — **accuracy completed the full 490-entry range; screening was cut off at 18345 (421/490)** by the ~50-minute wrapper timeout. Per §A resilience the 421 covered results were kept and adjudicated.

Two things this measurement settles:

1. **The bottleneck is the screener specifically, not OpenRouter or the network.** Both scripts call the same API from the same host in the same run; a 3.6× gap is a property of the screener's request pattern (serial per-entry calls, no batching), which is what items 21/31 have inferred but never measured against a control.
2. **The practical range cap is ~350 entries per Routine run**, the observing run's own recommendation and a number now backed by a measured rate rather than an estimate — 350 entries ÷ 8/min ≈ 44 min, inside the wrapper timeout with margin. That supersedes the looser "≤~100–200 IDs" guidance in the 2026-07-13/14 updates *for a full-length run*, while the smaller figures remain right for the short §4 self-check invocations.

The durable fixes are unchanged and now better justified: **concurrency in the screener** (the accuracy script demonstrates the achievable rate on the same infrastructure), a `--resume`/skip-already-screened flag, or a faster screening model. Note that this per-run cost buys almost nothing at present — see [item 24](#24-non-hiragana-reading-lint-cheap-replacement-for-the-furigana-screeners-true-positive-class), where the same 2026-07-25 run measured the screener at **~2% precision**.

**Update 2026-07-26 (the first side-by-side per-pass throughput numbers, and a concrete cursor-desync consequence)**: A 2026-07-25 accuracy-review measured both runners through the agent proxy: `review_accuracy.py` **~3–5 entries/min**, `review_runner.py --pass screening` **~3/min**, and **running both concurrently halves each** — so the two passes should be run *sequentially*, not in parallel, and accuracy-review ranges should be sized at **~300 entries per run** rather than the 400–600 that routine2.md §A suggests.

A 2026-07-26 sweep then produced the sharpest consequence yet: over 18653–19200, screening needed **~6.6 s/entry** and was **killed at 437 of 548 entries** (having reached 19178), while the accuracy pass over the *same* range ran at ~4 s/entry and finished. Because both passes advance the *same* cursor, the furigana and accuracy dimensions **silently drift out of sync** — the cursor records the accuracy pass's endpoint and the un-screened tail (19179–19200 here) is never revisited. That upgrades the fix from "size the range smaller" to one of: **checkpoint-and-resume in the runner**, or **separate cursors per pass**, or at minimum a warning when a pass ends short of the requested range. Range-sizing alone cannot prevent the desync, only make it rarer.

**Update 2026-07-28 (thirteenth confirmation — the widest ratio yet measured, ~6×, and it puts the screener's *whole* wall-clock cost in one number)**: A 2026-07-28 accuracy-review measured `review_runner.py --pass screening` at **~8–9 entries/min** against `review_accuracy.py` at **~55 entries/min** on the same range — a **~6× gap**, wider than the 3.6× of 2026-07-25 and much wider than the ~1× the proxy-throttled 2026-07-26 run saw when both ran concurrently. The spread across measurements is itself informative: the accuracy script's rate varies with network conditions (29→55/min across runs) while the screener's sits stubbornly at 8–9/min in every measurement since 2026-07-03, which is the signature of a **fixed serial per-entry cost** rather than a shared bottleneck.

The observing run stated the consequence in the plainest available terms: **a 500-entry screening pass takes ~55 minutes of wall clock and dominates the entire accuracy-review run.** That is essentially the whole time budget of an unattended Routine run spent on the pass which [item 24](#24-non-hiragana-reading-lint-cheap-replacement-for-the-furigana-screeners-true-positive-class) measures at 0–5% precision — and, per that item's 2026-07-28 update, whose false positives are now traced to a fixable bug in this same runner.

Read together, items 21 and 24 have converged on one conclusion that neither reaches alone: **the screener's cost and its noise have a common home in `review_runner.py`, and both are fixable there.** Batching or parallelizing the per-entry calls addresses the 6× gap; fixing the context-snippet truncation addresses the ~75–98% false-positive rate. Until one of them lands, §A's known-noise shortcut (skip the deep pass on polished ranges) is not a workaround but the correct default.

**Update 2026-07-29 (fourteenth confirmation — and a concrete API proposal from a run that worked around it successfully)**: The 2026-07-28 accuracy-review measured both scripts at **~2–4 entries/min serial**, so a 600-entry range is hours of wall clock and the mode's own range target (400–600 entries, §A step 1) is not reachable in one run at all. The run's workaround is the useful new information: it **sharded by disjoint `--range` across several concurrent processes and it worked** — the per-entry output files (`reviews/accuracy/{id}.json`, `reviews/screening/{id}.json`) make the design naturally shard-safe, with no shared mutable state to race on. The one rough edge is that each shard needs its own `--budget`, so the operator has to divide the session budget by hand and no single process sees the true total.

That converts this item from "chunk to fit the timeout" into a smaller, better-specified ask: **a `--workers N` flag** on `review_accuracy.py` and `review_runner.py` that fans the ID list across a thread/process pool and divides `--budget` internally. The correctness argument is already demonstrated by the manual sharding; what a flag adds is a single accurate cost total and no operator arithmetic.

Note the split with item 24: the fixed serial per-entry cost is worst in the **screener** (~8–9/min vs `review_accuracy.py` ~55/min at its best), and item 24 argues that the screener's output on polished ranges is ~2–5% precision. Parallelising a low-value pass buys throughput on work that mostly should not run; **sequence matters** — take item 24's deterministic-lint substitution first, then parallelise what remains.

**Update 2026-08-01 (fifteenth confirmation — and the first run to state the concurrency asymmetry as a design fact rather than a measurement)**: A 2026-08-01 accuracy-review measured the screener at **~7–8 entries/min** — one sequential API call per entry — so its 566-entry range needed ~75 minutes and was cut off by the 1800s wrapper at 22585 (264/566 done). `review_accuracy.py` covered **the same 566 entries in ~13 minutes**. The observing run drew the right inference from the shape rather than the ratio: *the accuracy script is evidently already concurrent, and the screener evidently is not.* That is why the screener's rate is stable at 7–9/min across every measurement since 2026-07-03 while the accuracy script's swings with network conditions — they are not two samples of one bottleneck, they are a concurrent client and a serial one.

So `--workers N` is not a symmetric ask. `review_runner.py` needs the concurrency `review_accuracy.py` already has; `review_accuracy.py` needs only the budget-division and total-cost accounting that manual sharding lacks. Interim sizing for the screener is unchanged and now measured three ways: **≤~250 entries per run**, or a longer wrapper timeout.

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

**Update 2026-06-24 (selector now has no high-priority lane to fall back on; new junk families)**: A
2026-06-24 routine new-entries run (29443–29462) sampled ~300 candidates plus probed ~25 extracted base
words to find 20 entry-worthy headwords, and reported the selector's `seen_in_entry_count` had reached
**0** — so the high-quality seen-in-entry lane that earlier runs leaned on is now empty, leaving only the
polluted backlog (the oldest unprocessed block ~C06000–C16000 is the worst). Two **junk families to add
to the pre-filter** beyond those above:
- **Place-name readings mis-glossed as common words** — 尾張 (おわり) glossed "end, finish"; 三重 (みえ)
  glossed "triple". These are proper nouns whose kana reading collides with a common word, so a naive
  reading-based gloss is wrong; the pre-filter's proper-noun rule should catch the surface even when the
  gloss looks lexical.
- **Niche technical jargon** (尾椎, 腋窩, 網点, 受水槽) and **outright coinages / non-words / wrong glosses**
  (権使, 個尊, 些道, 解退, 消痛, 自紹介, 内疎外内; 怒燥 どとう glossed "raging waves" — should be 怒涛;
  アンパッサン glossed "ice cream sundae" — actually *en passant*).
This reconfirms the <10%-signal rate and sharpens the throughput finding: with both the seen-in-entry lane
empty **and** the fallback lane unusable, new-entries production now requires scanning hundreds and
cherry-picking. Both the **pre-filter** (this item) and a **curator restock + `clean_up_candidates_list.md`
purge** (Open Issues → candidate-pool quality) are needed before the next new-entries-mode run, otherwise it
will be forced to mine transparent compounds.

**Update 2026-06-30 (reinforcement — seen-in-entry lane good, oldest-first fallback still unusable)**: A 2026-06-30 routine new-entries run created the **12 "seen in entry" candidates (29581–29592), all good**, but reconfirmed the oldest-first fallback pool is unusable: derived/inflected forms (potential verbs 与えられる, negations 信用できない, 〜化/〜性/〜者 nominalizations), compound numbers (三桁/四桁/二通/十通), proper-noun fragments, and OCR/coinage artifacts (些道, 個尊, 怒燥, 権使) plus mislabeled glosses (アンパッサン glossed "ice cream sundae"). No new junk family beyond those already enumerated above — pure reconfirmation of the <10%-signal finding and the throughput cap (production effectively limited to the seen-in-entry inflow). The standing recommendation is unchanged: the **pre-filter** (this item) plus a **curator `clean_up_candidates_list.md` purge** of the pre-March vintage (Open Issues → candidate-pool quality).

**Update 2026-07-01 (reinforcement — the C05xxx–C14xxx block is the worst pocket)**: A 2026-07-01 routine new-entries run reconfirmed the <10%-signal finding on the oldest non-"seen in entry" candidates, naming the **C05xxx–C14xxx block** specifically as corpus noise: compositional phrases (図書センター, 情報提供者), bare numbers/counters (二通, 六歳, 四桁), typos, and dialect fragments (どういうことや). No new junk family beyond those already enumerated — pure reconfirmation. The run reiterates that a `clean_up_candidates_list.md` purge **scoped to that C05xxx–C14xxx block** would raise new-entries throughput most directly, since runs currently hand-curate around it. Standing recommendation unchanged (the **pre-filter** in this item + a **curator `clean_up_candidates_list.md` purge**; see Open Issues → candidate-pool quality).

**Update 2026-07-14 (reinforcement — the C06000–C14000 corpus-harvested block enumerated as OCR/hallucination noise)**: A 2026-07-13 routine new-entries run reconfirmed the <10%-signal finding and named the **roughly C06000–C14000 corpus-harvested block** as the worst pocket: heavily polluted with OCR/hallucination artifacts and non-words (権使, 些道, 個尊, 怒燥/怒濤, 試戦, 発炭, 人義, 印示, 下告, 混雑物, 近遠感) plus compositional phrases (本人の意向, 引越センター, 三年前). Most old candidates in that block are unusable and must be individually rejected, which is what makes new-entries mode slow. No new junk family beyond those already enumerated — pure reconfirmation. Standing recommendation unchanged and restated with the block bound: a **dedicated `clean_up_candidates_list.md` purge scoped to the C06000–C14000 block** (curator side) plus this item's **candidate-reading plausibility heuristic** so the pool is not re-polluted at harvest time (a validator flagging implausible readings/glosses would catch the OCR non-words at intake). See Open Issues → candidate-pool quality.

**Update 2026-07-18 (reinforcement — a quality-first new-entries run sampled ~600 of 1,116 and found only ~12–15 usable; the seen-in-entry lane is nearly empty)**: A 2026-07-18 routine new-entries run sampled **~600 of the 1,116 candidates across the full added-date range** and found the large majority unsuitable as standalone learner-dictionary entries, re-enumerating every already-filed junk family with fresh examples: bare numbers/counters (三百, 八時, 二冊), compositional phrases (三年前, 一週間前, 髪を切る, 線を引く), place/proper names mis-glossed as common words (尾張 glossed "end/finish"), coined/non-standard compounds (個尊, 些道, 怒燥 for 怒濤), wrong-kanji/wrong-gloss entries (剥れる/はぐれる glossed "peel off" — really 逸れる, and already an entry as **28244**), and adult/brand terms. Only **~12–15 genuinely dictionary-worthy words** were creatable this run, and the **seen-in-entry lane is nearly empty (3 candidates)** — matching the selector's `seen_in_entry_count: 0` signal. No new junk family; pure reconfirmation of the <10%-signal finding. Standing recommendation unchanged and now doubly urgent: a **curator `clean_up_candidates_list.md` purge** of the corpus-harvested junk (much of C11xxx–C19xxx) **plus a restock of genuinely useful mid-frequency vocabulary**, so future new-entries runs aren't starved; this item's intake plausibility heuristic prevents re-pollution. See Open Issues → candidate-pool quality.

**Update 2026-07-20 (the seen-in-entry lane is now effectively exhausted)**: A 2026-07-19 routine polish run reported that after its frontier work only **two "seen in entry" candidates remain unbuilt** — バタ足 and ノーヒットノーラン (both baseball/swimming terms seen in 06542/06543). The selector's `seen_in_entry_count` has been reading **0** since ~2026-06-24, and this is the concrete confirmation that the internal-completeness candidate lane (the highest-quality source for new-entries mode) is drained: it only refills as the comprehensive-polish frontier advances into new naked-note ranges and harvests their `noentry` glossary terms. With the seen-in-entry lane empty, new-entries mode must fall back on the corpus-harvested pool, which this item documents as <10%-signal. Reinforces the standing recommendation — a curator **restock of brainstormed/corpus candidates** plus a `clean_up_candidates_list.md` purge of the C05xxx–C19xxx junk block — now more urgent, since without it new-entries runs will keep drawing from the noisiest pool.

**Update 2026-07-23 (reinforcement — a 20-entry run had to cherry-pick across many date-batches because the 2026-02/03 corpus dumps are largely unusable)**: A 2026-07-22 routine new-entries run reconfirmed the <10%-signal finding, naming the oldest corpus-harvested dumps (the **2026-02-25 / 03-18 / 03-28 batches**) as the worst pocket and re-enumerating the now-standard junk families with fresh examples: wrong kanji (怒燥 for 怒濤), wrong glosses (アンパッサン = "ice cream sundae"), fragments (がまま, 何かなり), compositional phrases (三年前, 本人の意向), and reading/gloss mismatches (三重 = みえ glossed "triple"). Because the seen-in-entry lane is drained (`seen_in_entry_count` reading ~0 since 2026-06-24), the run had to **cherry-pick genuine standalone words across many date-batches to fill the 20-entry run**. No new junk family; pure reconfirmation. Standing recommendation unchanged — a **curator `clean_up_candidates_list.md` bulk-prune of the corpus dumps** (routed *before* the next new-entries-heavy period) plus this item's intake plausibility heuristic to keep the pool from re-polluting. See Open Issues → candidate-pool quality.

**Update 2026-07-25 (reinforcement — ~200 candidates scanned to assemble a batch of 15 — plus a genuinely-new intake gap: the seen-in-entry logger does not check the *reading* against existing entries)**: A 2026-07-25 routine new-entries run reconfirmed the <10%-signal finding with a fresh throughput figure — **scanning ~200 candidates was required to curate a clean batch of 15** — and re-enumerated the standing junk families with the now-familiar examples (OCR/coinage non-words 権使 / 些道 / 個尊 / 怒燥 / 発炭; compositional number-counter phrases 二通 / 八時 / 四十分; transparent compounds ○○部品 / ○○機能 / ○○鋼). Standing recommendation unchanged: curator `clean_up_candidates_list.md` bulk-prune plus this item's intake plausibility heuristic.

The **new** datum concerns the *high*-quality lane, not the corpus junk. Two of the run's **"seen in entry" priority candidates were variant readings of entries that already exist**:

- **雪ぐ / すすぐ** duplicates **30089** — and the source entry (06614 恥辱) actually uses **そそぐ**, so the logged reading was wrong as well as redundant;
- **裏面 / うらめん** duplicates **18245** (裏面 / **りめん**) — same headword, different reading.

Both slipped through because the comprehensive-polish "seen in entry" logger adds a candidate **without checking the reading against existing entries**. `build/check_duplicate.py` already performs exactly this check and is documented as the pre-creation gate, but it runs at *entry-creation* time, i.e. one stage too late: the polish run spends nothing to log a duplicate, and the new-entries run downstream pays the cost of discovering it. Worse, a same-headword/different-reading pair is precisely the case a naive surface-string check misses.

**Suggested fix** (small, and it protects the one candidate lane that still has signal): call the `check_duplicate.py` logic — or `manage_candidates.py check` — at **candidate-add** time in the polish path, matching on **headword *and* reading independently**, and skip or annotate the candidate when either already resolves to an entry. Cheap, and it keeps the seen-in-entry lane's quality advantage from eroding as it refills.

**Update 2026-07-26 (the purge is now specified as three mechanical rules, and the self-feeding "seen in entry" lane is measured — it refills at half the rate it drains)**: Two data points, one of which finally makes the purge implementable without judgment.

**(1) Three mechanically-detectable junk classes.** A 2026-07-25 new-entries run characterized the pool concretely: of ~1,060 candidates, the oldest several hundred are misparsed fragments (権使, 些道, 個尊, 怒燥, 機成り), transparent compounds (片面コピー, 目標温度, 参加者数), inflected forms (与えられる, 勝てない, 信用できない), bare numerals (三百, 八十, 六人), and at least one non-Japanese string (C15326 `"famine"`). It also named the three filters that need **no** semantic judgment and could ship as a `manage_candidates.py --purge` pass or an intake guard:

- word contains **no Japanese script** (C15326 `famine`);
- word is a **pure numeral + counter** (三百 / 八十 / 六人);
- reading contains **を / に / へ** → a phrase fragment, not a lexeme.

Everything else (transparent compounds, inflected forms, plausible-but-wrong glosses) still needs a human or model call, but these three would clear the bulk of the mechanical noise for free and are safe to run repeatedly.

**(2) The seen-in-entry lane is self-feeding at ~50% replacement.** The same cycle measured the always-on §3 capture loop closing **within a day**: 5 of the 10 "seen in entry" candidates created by a 2026-07-26 run had been logged by the *previous day's* new-entries run from its own new entries (30108/30109/30113/30118/30122), and that run's SIMILAR WORDS lists generated 9 more captures in turn. So the high-quality lane runs at roughly **10 in / 9 out per run** — healthy and near-steady-state, but it **cannot grow the pool**, only hold it. The binding constraint on new-entry quality therefore remains what this item says it is: the fallback pool is polluted, and **curator restock of good standalone candidates** is the only inflow that improves the mix. The purge above raises the *yield* per run; it does not substitute for restock.

**Update 2026-07-27 (the pool quantified: ~1,030 of 1,044 non-"seen in entry" candidates are corpus residue)**: The 2026-07-27 polish run measured what the new-entries lane has been describing qualitatively. Of **1,044** candidates, only ~**14** carry the "seen in entry" provenance that makes them reliable; the other **~1,030** are dominated by four junk families:

| Family | Examples |
|---|---|
| Inflected forms (not lemmas) | 勝てない, 動かない, 強く |
| Transparent numeral + counter | 四十五, 三千円, 六歳 |
| Phrase fragments | 周囲の状況, 本人の意向 |
| Coinages / mis-glosses | 個尊, 些道, 怒燥, アンパッサン (glossed "ice cream sundae") |

The throughput cost is concrete: **a new-entries run that needs 20 words hand-sifts several hundred lines to find seven usable ones.** All four families are decidable without judgment — inflection is detectable morphologically, numeral+counter by character class, fragments by particle-final/genitive structure, and the mis-glosses by the same off-vocabulary check that catches tag drift. Either the `manage_candidates.py` quality filter this item specifies, or a scored one-off cleanup pass over the pool, would restore the lane; the "seen in entry" sub-lane is high-quality (13 of 13 usable this run) but, as measured 2026-07-24, **self-feeding at ~10 in / 9 out per run — it holds the pool, it cannot grow it**.

**Update 2026-07-29 (third and fourth consecutive reports; the pool is now measured as *two* pools with opposite yields)**: Both the 2026-07-28 and 2026-07-29 `new-entries` runs re-filed this, and the 2026-07-29 run supplied the decomposition that makes it actionable:

| Sub-pool | Size | Yield |
|---|---|---|
| `seen in entry` candidates | 12–14 at any time | **All real, useful headwords.** (2 of 14 turned out to be orthographic variants of existing entries and were dropped as stale — an 86% write rate.) |
| Corpus-harvested remainder | ~1,000 | Dominated by non-words and free syntax. |

The corpus remainder fails in three distinct ways, and they want different treatment:

1. **Hallucinated / OCR non-words** — `権使`, `些道`, `個尊`, `怒燥`, `多角的一面`, and `アンパッサン` glossed "ice cream sundae". Not Japanese words at all; safe to delete in bulk.
2. **Free syntax and inflected forms** — `静かに歩く`, `髪を切る`, `点を取る`, `与えられる`. Grammatical but not lexemes; a headword-selection decision, not a queue entry.
3. **Transparent compounds and numerals** — `三年前`, `八時`, `二百`, `全文字`. Real strings, but compositional; deliberately out of scope per the tier guidelines.

Consequence, now measured across three runs: **candidate triage is the single largest context cost of the `new-entries` mode** — each run scans several hundred rows to hand-pick 10–15 writable lexemes, which is budget that produces no entries.

Two cheap fixes, both still open:
- **(a) A `source` field on each candidate** (`corpus` / `seen-in-entry` / `curator`) so a run can filter to the high-yield pool in one pass instead of inferring provenance from the free-text gloss. This is the smaller change and captures most of the benefit.
- **(b) A one-off bulk prune** via `prompts/clean_up_candidates_list.md` over the ~1,000 remainder, deleting families (1) and (2) outright. After the prune the pool would reflect genuine gaps, which is what the selector's `candidates_low` signal assumes it already does — note that the signal currently reads **1,021 candidates** and therefore never fires, while the *writable* pool is **12**. That gap is the sharpest statement of the problem: the Routine's own low-candidate alarm is measuring the wrong number by roughly two orders of magnitude.

**Update 2026-07-30 — the writable pool reached zero.** The 2026-07-29 `new-entries` run **drained the `seen in entry` pool completely**: 20 available, 19 created, 1 removed as a stale okurigana variant. Every subsequent `new-entries` run falls back to the ~1,000-row corpus remainder until comprehensive-polish runs replenish the good pool.

This is the predicted failure arriving on schedule, and it converts item (b) from a nice-to-have into the binding constraint. The two pools have opposite dynamics: the writable pool is **produced** by polish runs at a few words per run and **consumed** by new-entries runs at ~20 per run, so it empties whenever new-entries is selected more than about one run in five — which the selector's weighting makes routine. The corpus remainder, meanwhile, is large, static, and mostly unusable.

Two consequences worth recording separately from the fix:

- **The `candidates_low` signal is now not merely inaccurate but anti-correlated.** It reads ~1,024 and stays silent at the exact moment the pool a run can actually write from is empty. A run that trusts it spends its budget on triage.
- **Pool depletion is a legible scheduling signal the selector could use.** A `source` field (fix (a)) would let `routine_next.py` count the writable pool directly and either fire `candidates_low` honestly or bias toward `polish` — which is what replenishes it. That makes (a) worth more than the context saving it was originally proposed for: it closes a feedback loop the selector currently cannot see.

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

**Update 2026-07-26 (9/9 false positives in one range — and the failure is not the enum, it is that the reviewer never reads the entry's own register text)**: A 2026-07-25 accuracy-review of **18346–18652** produced **nine** `formality: formal → neutral` flags and **all nine were wrong**: 口頭で, 何らか, 念珠, 必然的, 多くとも, 面目ない, 百貨店, 陣中見舞い, 雇い止め. In every single case the entry's own REGISTER line or notes **explicitly state that the word is formal** — the information that refutes the flag was already in the text the reviewer was given.

That reframes this item. Embedding the valid enum (this item's original fix) prevents *invalid* values; it does nothing about a reviewer that proposes a valid-but-contradicted value. Two additional prescriptions follow, in order of cheapness:

1. **Prompt fix**: instruct the reviewer to read the entry's REGISTER / notes text before raising any formality flag, and to suppress the flag when that text states a register — i.e. the entry's own prose is authoritative over the reviewer's intuition for this dimension specifically.
2. **If that fails, retire the dimension.** Across the ledger, formality flags have never yet produced a sustained applicable rate; the 2026-07-04 harvest recorded the same `formal→neutral` sub-family (厨房 / 名高い / 厭う / 原案 / 喜ばしい, same root cause), so this is a **recurrence, not a first observation**. Two independent ranges at ~0% precision, with an identified and un-fixed cause, is the standard this project has used elsewhere to stop paying for a check.

Note the asymmetry worth preserving if the dimension survives: routine2.md §A already says to apply a formality flag **only when the entry's own notes contradict the label**. The reviewer is being asked for exactly the judgment it is demonstrably worst at, so the prompt should encode the §A rule rather than leave it to adjudication.

## 24. Non-hiragana-reading lint (cheap replacement for the furigana screener's true-positive class)

> **Update 2026-08-01 — fourth and fifth post-fix data points, both zero.** 2026-07-31
> accuracy-review (22213–22275): **63 entries screened, zero flags raised** — not zero applied,
> zero raised. 2026-07-31 accuracy-review (22276–22333): **58 entries, 3 flags, 0 applied**, all
> three in documented false-positive families (`{砲丸投|ほうがんな}げ` okurigana split,
> `{集|たか}り`, and `{艶|あで}やか` appearing inside 22288's *own* similar-words contrast).
> Cumulative post-fix: **0 applied of ~35 flags across five consecutive runs**, with no
> counter-evidence since the context-snippet repair. Throughput remains the binding constraint
> at ~1.8–2 entries/min against the accuracy pass's ~13, and because the shared cursor
> `polishing/tasks/cross-model-review/progress.txt` is pinned to the *screener's* frontier, the
> slower instrument sets the pace of the faster one. The retire-or-downsample recommendation
> now has five data points; a fixed 50-entry sample per run would unpin the cursor without
> discarding the instrument outright. **Curator decision.**

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

**Update 2026-06-24 (truncation FP family reconfirmed on a fresh, never-reviewed range)**: A 2026-06-23
accuracy-review furigana screen over **9240–9456** again produced the `review_runner.py` pair-extraction
truncation false positives on long all-kanji compounds — 駐輪場→「ちゅうり」 (actual ちゅうりんじょう), 分岐点→
「ぶんきて」 (ぶんきてん), 実体経済→「じった」 (じったいけいざい) — all flagged as "incomplete reading" while the
entries hold the correct full readings (~8 verified, all FP). This is the same extraction bug (the screener is
shown the reading cut off mid-word), now observed on a *never-reviewed* range rather than a polished one, so it is
not range-state-dependent — it is a pure `review_runner.py` context-extraction defect. Reinforces the unchanged
fix: **send the example/reading fields to the screener untruncated (or truncate only at furigana-pair
boundaries)**, which would erase this dominant noise family on every range without any model change.

**Update 2026-07-13 (~4.5% precision reconfirmed on the already-polished 13975–14186; the one true positive was a genuine reading error, not a grouping/charset defect)**: A 2026-07-12 furigana screening pass over **13975–14186** (the completed slice of the truncated 13975–14500 screen, see item 21) flagged **~22 entries with only 1 genuine** (~4.5% precision), matching the documented **0–5% on already-polished ranges** (`reviews/calibration_report.md`). The sole real error was **14102 いしょ→いしょう** in 衣装替え (an incomplete/incorrect reading, applied in-run); every other flag was the standing FP family — the runner's pair-extraction reading-truncation artifact, compound rendaku (14020 茶屋/ぢゃや), or a model misread of a correct wrapper (14488 ござん). Pure reinforcement of the calibration figure and of both this item's theses: (a) the truncation FP family is range-state-independent and would be erased by sending untruncated fields, and (b) on a polished range the screener's entire net value was again a single hit — here a reading error rather than the item-16/charset or grouping classes — underscoring that the deterministic charset/grouping lints proposed above would leave only the genuine-reading-error residue for the (expensive) model, which should be reserved for never-reviewed ranges.

**Update 2026-07-15 (0% precision on the already-polished 14900–15099 — every flag a truncation/rendaku/name-reading FP)**: A 2026-07-14 accuracy-review furigana screen over **14900–15099** flagged **21 of 200 entries at 0% precision** — every single flag was a false positive from the documented families: the runner's pair-extraction **display-truncation** artifact ("missing final kana" where the entry's actual wrap is complete, e.g. {群衆|ぐんしゅう} shown cut off), compound **rendaku** (隣国→りんごく), **okurigana/compound-split** truncations (占→じ), and **name/nanori readings** (展→あつし). Reconfirms the 0–5% calibration figure on already-polished ranges and both theses of this item: the truncation family is range-state-independent and would be erased by **sending the reading/example fields untruncated**, and on a polished range the screener's entire net value is once again zero genuine hits — a deterministic charset/grouping/reading lint would leave only true reading errors for the (expensive) model, which should be reserved for never-reviewed ranges.

 **Update 2026-07-18 (100% FP on 15567–15766 — a nominally never-reviewed range, yet all documented families)**: A 2026-07-17 accuracy-review furigana screen over **15567–15766** flagged **19 of 191 entries, 100% false positives** — every flag one of the documented families (okurigana splits, the runner's prompt-context/pair-extraction truncation artifact, contextual readings like お腹→なか). The deep pass was skipped per the known-noise shortcut (`reviews/calibration_report.md`). The datum worth noting: this band's `tags` dimension was genuinely contaminated (28% real off-vocab flags, see item 17 / Cleanup P20), yet its **furigana** was already clean — so tag drift and furigana quality are independent per range, and the screener produced zero value here even though the range had never been furigana-reviewed. Reconfirms both theses: the truncation family would be erased by sending untruncated fields, and a deterministic charset/grouping/reading lint would leave only true reading errors for the model.

**Update 2026-07-24 (0% precision reconfirmed on the already-polished 17311–17560 range)**: A 2026-07-23 `review_runner.py` furigana screen over **17311–17560** flagged **37 of 241 entries at 0% precision** — every flag the documented screener context-truncation family (the reading display cut off, e.g. `変化球|へんかき` for へんかきゅう) plus okurigana/rendaku FPs; the deep pass was correctly skipped per the known-noise shortcut. Consistent with the documented 0–5% precision on already-structured ranges. Reinforces the untruncated-field fix (send the entry's full stored reading, and suppress a flag when the stored reading already matches the "should-be" full reading) and the deterministic-lint thesis for the screener's one true-positive class.

**Update 2026-07-25 (the truncation artifact is now *quantified and verified entry-by-entry*: ~37 of 48 flags in one pass, measured precision 1/48 ≈ 2%)**: A 2026-07-25 accuracy-review furigana screen over **17911–18345** produced the cleanest characterisation of this bug so far. The reviewer's concerns quoted readings that were **cut off mid-word and in several cases carried a stray closing parenthesis** — `{配布物|はいふぶ)`, `{茶店|さて)`, `{防腐剤|ぼうふざ)` — and then flagged the truncation *it had itself produced* as an "incomplete reading."

The observing run then **verified every one against the entry files**: 17917, 17920, 17928, 17944, 17945, 17978, 18012, 18023, 18057, 18070, 18148, 18152, 18161, 18162, 18183, 18292, 18297, 18298, 18312, 18315 **all carry the full, correct reading**. This single artifact accounts for **~37 of the 48 screening flags in the range**, and the pass's measured precision was **1 of 48 ≈ 2%**.

Why this update matters more than another 0%-precision datapoint:

- The **stray `)`** is a smoking gun. It shows the truncation happens in the **prompt builder's context-window assembly**, not in the model's reading of a correct prompt — the string is being cut mid-token and the surrounding punctuation left dangling. That localises the fix to one place in `review_runner.py`.
- It puts a number on the payoff: fixing the context assembly would remove **roughly three-quarters of all screening flags** in a typical pass, at which point the residual (okurigana splits, rendaku, nanori) is small enough for the deterministic charset/grouping lint this item proposes to handle without a model at all.
- Paired with [item 21](#21-chunk-the-reviewscreening-runners-to-fit-the-session-timeout)'s same-run measurement that the screener runs at ~8 entries/min (3.6× slower than `review_accuracy.py`), the current cost-benefit is stark: **the slowest instrument in the Routine is spending its budget generating its own false positives.** Until the context-assembly fix lands, the known-noise shortcut in §A (bulk-reject the documented families, skip the deep pass) is doing the right thing, and shrinking or skipping furigana screening on already-structured ranges costs the dictionary essentially nothing.

**Update 2026-07-26 (two more 100%-FP screens, and the truncated-token family is confirmed *mechanically checkable before the flag is emitted*)**: Two independent screens this cycle:

- **18653–19178**: 49 flags, **all 49 rejected (100% FP)**. Every one fell into the truncated-token family (魅力→みりょ, 正体→し, 強制執行→き, while the entry carries the full reading) or the documented-variant family (18990 物悲しい, where the flagged ものがな appears only in the notes line that *labels it a variant reading*).
- **A 21000-band systemic-fix self-check**: 9 flags / 46 entries, **all rejected**, of which **6 were truncated-token** (家庭→かて, 名産→め, 悲願→ひ).

Both are consistent with the 0–5% precision measured 2026-06-10/11 and with the 2026-07-25 diagnosis that the truncation lives in the **prompt harness**, not the entries. The new and actionable point is that **both families are decidable without a model**:

1. **Truncated-token**: before emitting a flag, check the claimed-incomplete reading against the entry text. If the entry already contains a *longer* reading for that kanji run of which the claimed reading is a prefix, the flag is an artifact — drop it silently.
2. **Documented-variant**: if the flagged reading occurs only inside a notes line that names it a variant/alternative reading, drop it.

Implemented as pre-emission filters in the screener, these two rules would remove essentially the entire adjudication load that §4 self-checks currently pay for furigana — which, at 0–5% precision, is close to the whole cost of the pass. This strengthens the standing recommendation on this item: the cheap deterministic lint should **replace** the screener for the format-artifact class rather than sit beside it.

**Update 2026-07-27 (13/102 flagged, *zero* applicable — plus the scheduling fix that would stop paying for it)**: A furigana screen over **19452–19554** flagged **13 of 102 entries (12.7%)** with **0 applicable** findings. Every flag fell in a documented false-positive family: truncated-reading hallucination (the model misquotes `{両腕|りょう)` where the entry has `{両腕|りょううで}` — the 18448 index-confusion artifact, **now the dominant family**), okurigana splits, rendaku in compounds, and readings the entry's own VARIANTS section already documents (19530 愛想/あいそう). This is consistent with the 0–5% precision measured 2026-06-10/11 and with every screen since. The run also re-measured the throughput gap — screening ran **~5× slower** than `review_accuracy.py` and **appeared to throttle it when the two ran concurrently**.

Two fixes, both outside the model:
1. **Stop scheduling it where it cannot pay.** The selector's `accuracy-review` `phase: "furigana"` should not screen ranges that the accuracy sweep has already passed; on structured, already-reviewed ranges the screener's entire yield has repeatedly been zero or one deterministically-detectable hit.
2. **Post-filter the artifact family deterministically.** Drop any flag whose quoted reading does not appear verbatim in the entry's actual wrapper text. That is a string comparison against the file the run already has open, and by the 2026-07-25 measurement (~37 of 48 flags in one pass) plus this one it would remove the large majority of all screening flags — at which point what remains is small enough to judge honestly.

The item's original proposal stands: the screener's genuine true-positive class (non-hiragana readings) is a **lint**, not a model call.

**Update 2026-07-28 (the false-positive mechanism is finally *located in the source*, and the proposed lint outperforms the screener 7:1 in a head-to-head)**: This item's two halves both got their decisive datum in one run.

**(1) The FP mechanism is the prompt builder's `followed by:` context snippet.** Prior updates localized the truncation to "the prompt harness" from the evidence of stray punctuation. The 2026-07-28 run named the field: `review_runner.py`'s screening prompt includes a **`followed by:` context snippet clipped at a fixed character width**, which routinely cuts mid-`{kanji|reading}` markup — `の{死者数|ししゃす`, `{記者会見|きしゃか}`. The model reads the clipped fragment as if it were the entry's actual furigana pair and reports an incomplete reading. Two independent measurements the same day:

- **19951–20388**: **47 of 48 flags** were this one artifact — precision **~2%**.
- **New entries 30165–30175**: **7 of 18 flags**, all seven verified correct at source. Note the range: these are *brand-new* entries in a §4 self-check, so the artifact is not a property of old or unpolished data.

The fix is now concrete enough to specify: **clip the context at a wrapper boundary, or strip `{…|…}` markup from the context field entirely.** The second is simpler and loses nothing — the model is being asked about the headword's reading, not about the readings of neighbouring words, so the markup in the *context* is pure distraction even when it is not truncated.

**(2) The proposed lint was run by hand and beat the screener 7:1.** The same run scanned the dictionary for Latin characters inside furigana readings — exactly the deterministic check this item proposes — and found **8 entries**: `{旅|たbi}`, `{形式|けいしiki}`, `{敷金|しikikん}`, `{間違|まちga}` and four wrapper misuses. **The paid screener had caught one of them** (in 19961); the regex found the other seven in seconds. All 8 were fixed and the class is empty (recorded as [Cleanup P30](cleanup-backlog.md#priority-30-latin-characters-inside-furigana-readings--resolved-2026-07-28)).

That is the head-to-head this item has wanted since June, and it settles the cost-benefit: over the same corpus, **the free scan found 8× what the slowest and noisiest instrument in the Routine found**, and did so with zero false positives, because a Latin letter in a reading is wrong by construction rather than by judgment. The recommendation firms up accordingly — **ship the charset lint as a permanent CI check first** (it needs no review queue: any match fails), then either fix the context-snippet truncation or stop scheduling the screener on structured ranges. The lint is not a supplement to the screener; on this class it is a strict improvement over it.

**Update 2026-07-29 (two further confirmations at 3% and ~5% precision; the artifact is now the *named* dominant flag family in consecutive sweeps)**: Two more accuracy-review runs measured the same truncation artifact the 2026-07-28 harvest located in the source:

| Range | Flags | Truncation-family or documented-FP | Precision |
|---|---|---|---|
| 20451–21050 | 31 | 30 | ~3% |
| 20703–21300 | — | "still the dominant flag source" | ~5% |
| 19951–20388 (prior) | 48 | 47 | ~2% |
| 30165–30175 (prior, brand-new entries) | 18 | 7 | — |

The reported quotes are now diagnostic on sight, because they are *not valid furigana at all*: `{過小評価|かしょ}` where the entry has `{過小評価|かしょうひょうか}`; `{分別|ふんべ)`, `{発狂|はっ)`, `{低所得世帯|てい)` with a stray `)` closing the clipped span; `{調教|ちょうきょ}`. The model is reading the prompt's fixed-width `followed by:` snippet — clipped mid-`{kanji|reading}` — as the entry's actual reading and reporting the clip as an incomplete reading. **Fixing the context builder in `build/review_runner.py` to never truncate inside a `{kanji|kana}` pair removes most of this at zero model cost**, and the change is local to the prompt-assembly function.

**The true-positive class, and why it argues against retiring the screener outright.** The same 20451–21050 pass found a genuine defect the deterministic lints cannot see: **20908 {省力化|しょうりょくか}** contained `{急|きゅう}がれている` — 急 wrapped with its *on'yomi* in a context where the verb is 急ぐ (いそ). Every character is in the right script, the wrapper is well-formed, the reading is a real reading of that kanji; only the okurigana `がれている` reveals that the wrong reading was chosen. Item 24's proposed charset lint (which beat the screener 7:1 on Latin-letter readings) is blind to this by construction, because nothing about the string is out of place.

That suggests a **third, narrow, deterministic check** worth its own small script rather than a model call: *a kanji wrapped with an on'yomi reading immediately followed by okurigana that forms a known verb/adjective inflection*. The kanji index already carries on'yomi and kun'yomi per kanji, so the test is "wrapper reading matches an on'yomi ∧ the following kana are inflectional okurigana" — enumerable, cheap, and it would have caught 20908. Worth sizing before the next screener spend: if the class is more than a handful of entries dictionary-wide, it is the second deterministic win taken off the screener's plate, and the residue left for the paid pass gets correspondingly harder to justify.

### The context-snippet half — RESOLVED 2026-07-30 (routine accuracy-review, 21901–22500)

The prompt-construction bug this item had been describing since 2026-06-18 — under three
successive descriptions (*"pair-extraction truncating long compound readings"*, then
*"the `followed by:` context snippet clipped mid-`{kanji|reading}`"*) — was fixed at the
source. The final mechanism, verified in `build/review_runner.py` before the change:

> `extract_furigana_pairs()` captured only **10 characters** of following context, and
> `build_screening_prompt()` rendered it as `(followed by: {協議会|きょうぎか)`. A 10-character
> window almost always cuts *inside* the next `{kanji|reading}` wrapper, and **the closing
> paren of the annotation then reads as the wrapper's closing brace** — so the model was
> shown a syntactically complete wrapper holding a truncated reading, and correctly
> reported what it was shown.

That last step is why the family survived four cycles of diagnosis: the artifact is not a
malformed string the model mishandles, it is a *well-formed* string that means something
different from what the entry says. `21902 協議会`, `21912 注力`, `21935 防衛線` were all
verified against source and hold the full correct reading.

**What shipped** (both the screening and deep prompts): 24-character capture, a
`trim_context()` that cuts back to a wrapper boundary, `「」` delimiters that cannot be
confused with `{…|…}` markup, and an explicit instruction that the excerpt may stop early
and truncation must never be inferred from it.

**Final precision measurements before the fix**, the two worst in the series:

| Range | Flags | True positives | Precision |
|---|---|---|---|
| 21301–21900 | 21 | 0 | **0%** |
| 21901–22500 | ~16% of entries | 0 inspected | **~0%** |

Thirteen of the 21 flags in the first range quote a snippet cut mid-pair, with the stray
`)` tell (`{急峻|きゅうしゅ)`, `{高圧的|こうあつ)`).

**The durable lesson, which generalizes past this script**: *any context excerpt shown to a
model must be cut at a token boundary of the markup it contains, and the delimiter wrapping
the excerpt must not be confusable with that markup.* Both halves were needed — widening
the window alone would have moved the cut, not removed it.

**Still open in this item**: the charset lint (shipped as a hand-run scan, not yet CI) and
the on'yomi-plus-okurigana check sketched above.

### Post-fix measurement — 2026-07-30: three runs, zero precision, and a new cost argument

The measurement this item asked for has now been taken, and it removes the last defence of the
screener. **Three consecutive measured runs postdate the context-snippet fix and all three
applied nothing**: 0 of 29 flags across the twenty-eighth metrics window. The 2026-07-30 (004)
run screened 140 entries and produced **2 flags** — one a variant reading (毎年 まいとし, which
the model itself called "not strictly incorrect") and one an okurigana split (一握). Both are
documented false-positive families. So the "its noise may be an artefact of the truncation bug"
objection is answered: the noise is the instrument.

Two further findings from the same window:

1. **A self-refuting flag.** On 22097 the screener wrote: *"The reading for 本屋大賞 should be
   ほんやたいしょう, but the provided reading is ほんやたいしょう."* Expected and provided are the
   identical string — the flag's own body refutes it. A one-line post-filter (drop any concern
   whose quoted expected reading equals the provided one) suppresses this for free, and the shape
   generalises cheaply to the other dimensions.
2. **The screener is now the rate-limiting instrument in `accuracy-review` mode.** Measured
   2026-07-30: **~1.9 entries/min** against the accuracy pass's **~3.4/min** over the same window.
   One run can no longer cover a common range on both dimensions, so
   `polishing/tasks/cross-model-review/progress.txt` is pinned to the slower of the two.

That is the whole argument in one place: **zero measured precision post-fix, and it halves the
range the accuracy pass could otherwise cover.** The recommendation is to **retire or heavily
downsample** the furigana screening pass — keep the deterministic replacements this item already
specifies (the non-hiragana-reading lint, the grouping/orphan-kana detector, item 47's
self-checking cross-reference readings), which between them cover every true-positive class the
screener has produced in two months. Downsampling — e.g. screening only *newly created* entries,
never re-screening polished ranges — is the conservative version if retiring outright feels
premature; the data does not require the conservative version.

### Update 2026-08-02 — a further run at zero, and the flag-by-flag breakdown of *why*

A 2026-08-02 accuracy-review run (23608–23907) screened **103 entries**, produced **7 flags
(6.8%)**, and applied **0**. Counting only post-fix runs this is the fourth consecutive zero; the
[quality-metrics page](../topics/quality-metrics.md) now records **six consecutive windows at
zero precision, 0 of ~64 cumulative**. What this run adds is the itemised disposition, which
shows the flags are not a scatter of near-misses but the same four documented families:

| Disposition | n |
|---|---|
| Partial-reading / index-confusion false positive (in `calibration_report.md`) | 4 |
| The documented 毎年 まいとし variant-reading family | 1 |
| The model's own concern text concludes it is **not** an error | 1 |
| Escalated to the curator rather than applied (兎形目 reading) | 1 |

Only the last is even arguably a finding, and it was escalated precisely because the run could
not confirm it. The self-refuting family (row 3) recurs a second time here, which is the strongest
case for the one-line post-filter proposed above — it is free and it removes a flag class that has
now cost adjudication effort in two separate windows.

The rate argument also held at the larger gap: **~1.4 entries/min for the screener against ~7/min
for the accuracy pass** in this run (the 2026-08-01 harvest measured ~2 vs ~13 on a longer
window). Because both passes share
`polishing/tasks/cross-model-review/progress.txt`, the slower one sets the cursor, so the cost of
keeping the screener is paid in accuracy-pass coverage — the dimension that *is* producing
applied fixes.

### Update 2026-08-03 — two more zero windows, and the false-positive families are now regex-shaped

Two further accuracy-review runs reported the pass, both at zero:

| Run | Range | Flags | Applied | Throughput |
|---|---|---|---|---|
| 2026-08-02 | 23908–24500 | 13 / 294 entries | **0** | ~7 s/entry vs ~1.5 for accuracy |
| 2026-08-03 | 24501–25100 | 3 / 34 entries | **0** | **~1.3 entries/min** vs ~3 |

That is **seven consecutive windows at zero** and roughly **0 applied of ~86 flags** post-fix. The
second run killed the pass early and handed the remaining wall clock to the accuracy pass.

The new datum is that the surviving false positives have collapsed to **two families, both
mechanically recognisable without a model**:

1. **Okurigana reading-splits** — the flag's quoted "correct" reading is the entry's reading plus
   the trailing okurigana ({命取|いのちと}り flagged as いのちとり, {誤|あやま}り as あやまり).
2. **Katakana adjacency** — a katakana run next to the braces is read as missing furigana
   (フランス{料理|りょうり}, キャッシュフロー{計算書|けいさんしょ}).

Both are a string comparison against the flag itself: *if the proposed reading equals the wrapped
reading plus an adjacent kana/katakana run, the flag is a false positive by construction.* Several
flags in these runs visibly argue themselves out mid-sentence — the model states the alternate
reading is valid and flags it anyway.

**Recommendation, now made independently by three runs**: gate the screening pass behind that
pre-filter, or drop it from `accuracy-review` over already-polished ranges and keep only the
deterministic non-hiragana-reading lint this item originally proposed. The seventh zero window
plus the throughput gap makes this the clearest retire-or-gate case in the backlog.

### Update 2026-08-04 — eighth consecutive zero window, and the flag rate is partly an artifact

The 2026-08-04 accuracy-review screened 25101–25320 and flagged **11 of 217 entries (5.1%),
precision 0%**. The itemised disposition is the familiar list with nothing new in it: okurigana
reading-splits (`{手入|てい}れ`, `{鉢植|はちう}え`, `{爆|は}ぜる`), katakana+kanji compounds
(`ラジオ{体操|たいそう}`), rendaku (`鳴き{声|ごえ}`) — and **3 of the 11 were not flags at all** but
parse failures recorded as flags (see item 73). The deep pass was skipped under the known-noise
shortcut, as designed.

Two things follow. First, eight windows at zero is no longer evidence being accumulated; it is a
settled result, and the run also confirmed the pre-filter design — every one of the 8 real flags
falls inside a family expressible as a regex over the flag text itself. Second, the **measured
flag rate has been running ~25–30% high** for the whole series because parse failures inflate it,
which slightly understates how noisy the pass is rather than overstating it.

The throughput datum was taken a fourth time: screening covered only the first 220 of a 500-entry
range before the run wrapped up, against the accuracy pass's full coverage of the same range. The
cost of keeping the screener continues to be paid in accuracy-pass coverage, and the accuracy pass
is the one with measured precision.

> **Update 2026-08-05 — the zero streak ends at one, and the one is real.** Two data points this
> window. (a) A 2026-08-04 run screened 25601–25792 and raised **0 flags on 78 entries** — the
> first sample taken after the context-window repair, and consistent with the repair having
> removed the false-positive family rather than with the pass being uninformative. (b) The
> 2026-08-03 screen produced the first genuine hit since the repair: `24842`, katakana `プロ`
> sealed inside a kanji group, applied. The window closes at **1 applied of 27 flags (3.7%)**.
>
> This is the first evidence in nine windows that argues *against* retirement, and it should be
> weighed honestly: one true positive is not a rate, and the class it belongs to (a non-hiragana
> character inside a reading) is exactly the one this item proposes to catch with a regex for
> free. What the datum actually settles is the *diagnosis* — the pass is not broken, it is
> low-yield — which leaves the throughput argument (~1.3–2 entries/min against the accuracy
> pass's ~3–13, on a shared cursor) as the whole of the retire-or-gate case. Recommendation
> unchanged, evidence now cleanly separated: **retire on cost, not on precision**.

> **Update 2026-08-06 — the throughput number measured directly, and the cost now falls on the
> paying pass.** Two runs this window put figures on the wall-clock argument. A 2026-08-05
> accuracy-review stopped screening deliberately (not a crash) after **0 flags on 69 entries**,
> $0.0073 spent, and recorded the ratio as **~8 entries/min for screening against ~50/min for
> `review_accuracy.py`** — a 512-entry range is ~10 minutes of accuracy review and ~65 minutes of
> furigana screening. The 2026-08-06 run truncated screening at 26418 of a planned 26700 for the
> same reason. **The new datum is second-order and worse**: in the run that measured it, the
> *accuracy* pass also fell short (316 of a planned 569 entries) — the first time the throughput
> ceiling has bound the dimension that produces applied fixes. Precision that window was **1 of 9**
> (26189–26418), and the eight rejects were the documented false-positive families (rendaku,
> okurigana splits, pair-index confusion), so the numbers keep landing in the same place: the
> screener is not wrong, it is slow, and it is now slow *at the expense of* the paying pass.
>
> One incidental finding is worth keeping for whatever replaces it: the single true positive,
> `{歴史書|れきしょ}` for れきししょ in 26418, was in a **notes COMMON COLLOCATIONS block** — not a
> headword, not an example. Both true positives this month came from the least-swept surface.
> A cheap replacement (the non-hiragana-reading regex this item proposes, plus a
> reading-length sanity check) should run over notes furigana, which nothing else inspects.

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

**Update 2026-06-26 (PARTIAL — the inflow gate shipped as a baseline ratchet)**: A 2026-06-25 tooling-fix
session shipped the **inflow half** of this item without blocking the legacy tail — the correctly-sequenced
intermediate the note above asks for. It added `validate_tags.py --check-no-new-unknown` (now a CI step) backed
by `build/data/unknown_semantic_baseline.json`, which **fails CI only when an entry introduces a *new*
off-`VALID_SEMANTIC` tag**, while the pre-existing legacy tail (re-measured at **8,267 instances / 6,759 entries
/ 1,109 distinct tags**) passes. This is exactly step (1.5): new entries can no longer add to the backlog (closing
the "draining a backlog new creation keeps refilling" losing race), but legitimate work on the 6,759 existing
entries is not blocked. Regenerate the baseline after each migration batch with `--write-unknown-baseline`.
**Remaining work for this item**: the full step-(2) flip to a hard *error* on any off-list tag, to be done after
the curated-migration systemic-fix drain (Cleanup P20) brings the legacy count to zero (or near it). Documented in
[Schema Tag Reliability](../topics/schema-tag-reliability.md).

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

**Update 2026-06-24 (second confirmation — a systemic-fix run again landed on a scope-0 standing check)**: A
2026-06-24 routine systemic-fix run was again handed `tag-conjugation-no-verb-pos` (priority 6), a scope-0 standing
check whose detector has returned 0 since the 2026-06-08 P6 sweep + the `add_conjugations.py` regeneration guard.
The run **flipped that item to `status: resolved`** in `backlog-queue.json` (the read-only detector stays indexed
as a regression guard) so it stops topping the open/`batch_ready` queue — but the observing run noted the **same
latent no-op risk still applies to `tag-proverb-idiom-mismatch`** (priority 12, also scope-0/`status: open`/standing
check). This is the convention half of the fix in action (mark guarded clean checks `resolved` rather than `open`)
and is exactly why option (a)/(b) above is still worth shipping: a selector rule that skips open items whose detector
currently returns 0 would make the convention self-enforcing instead of relying on each systemic-fix run to notice
and hand-flip. Confirmed in `backlog-queue.json`: `tag-conjugation-no-verb-pos` is now `resolved` (scope 0);
`tag-proverb-idiom-mismatch` remains `open` (scope 0) and is the next one a systemic-fix run could waste a turn on.

**Counter-evidence 2026-07-29 — scope-0 standing checks refill, and two of them just did.** This wiki refresh re-ran all four detectors as part of the routine `backlog-queue.json` resync and found:

| Item | Recorded | Actual 2026-07-29 |
|---|---|---|
| `artifact-missing-target-id` | `resolved`, 0 | **12 instances / 12 entries** |
| `example-headword-missing` | `open`, 0 | **33 suspect examples / 13 entries** |

Both had been driven to zero and stayed there long enough to look permanent. The refill mechanism is not a regression in the fix — it is the dictionary growing: `missing-target-id` was deliberately narrowed on 2026-06-21 to flag only refs whose referenced word *has* an entry, so every new entry can convert a legitimately target-less homophone/antonym label into a resolvable one. This is the same back-edge that item 19 describes for stale `noentry` markers, and it will recur at a rate proportional to entry creation.

**This does not overturn the item, but it changes the fix.** The problem the item names is real — a selector that repeatedly hands a run a check with nothing in it wastes the run. But "skip scope-0 items" as written would have made these two invisible indefinitely, since nothing else re-measures them. The right shape is **stale-count-aware**: skip a scope-0 item *only while its recorded count is fresh*, and re-run the detector (which is read-only and cheap — all four completed inside this wiki run) when the count is older than some threshold, rather than trusting a zero written weeks ago. Concretely: store `scope_measured_at` alongside `scope_estimate`, treat a zero older than ~7 days as unknown rather than as empty, and let the periodic wiki resync be the thing that refreshes it — which is what already happens in practice.

## 29. `part_of_speech` display-field normalizer (driven by canonical `tags.pos`)

**Source**: 2026-06-23 routine polish run (frontier 6250–6254)

The free-text `part_of_speech` field (the human-readable POS string in the entry-page header)
is inconsistent dictionary-wide — `adjective (i-adjective)` (98) vs `i-adjective` (256), and
four spellings of suru-verb (`noun, suru verb` / `noun / suru-verb` / `noun, verb-suru` /
`verb (suru)`) coexisting. This is display text only; the validated `metadata.tags.pos`
(`adjective-i`, `verb-suru`, …) is canonical and is what the renderer/search use. See
[Cleanup Backlog](cleanup-backlog.md) → Priority 22 for the entry-level pattern.

**Suggested implementation**: a small read-only **detector** that lists every entry whose
`part_of_speech` text is not the agreed canonical display string for its `tags.pos` value,
plus a **normalizer** that rewrites the field to the canonical string (validated against the
structured tag, `modified` bumped). Because `tags.pos` already encodes the category
unambiguously, the detector is a deterministic table lookup and the transform is a safe
text substitution — once the canonical `tags.pos → display-string` map is agreed with the
curator (the one editorial choice). Read-only `--json` queue + a separate `--apply` pass,
sibling to `check_artifacts.py`; this is what would convert Cleanup P22 from a prose item to
a `batch_ready` systemic-fix item. Low risk (display-only), but it changes visible header
text on thousands of pages, so spot-check after the canonical map is fixed.

**Update 2026-08-04 — "display-only" is true for 30,116 entries and false for 71.** The field was
measured dictionary-wide (401 distinct values; 6,573 entries deviating from their tag set's
plurality spelling; full tables in
[Cleanup P22 → Update 2026-08-04](cleanup-backlog.md#update-2026-08-04--measured-and-the-display-only-no-information-lost-premise-is-wrong-for-71-entries)).
The normalizer as specified here would delete transitivity from **50** verbs that state it only in
the free text, plus `proverb` from 8 and `idiom` from 13 entries, and would drop the "verb phrase"
qualifier from 19 with no structured field to receive it.

So this item needs a **step 0**: a backfill pass that parses the free text and writes what it
finds into `tags.transitivity` / `semantic` before anything rewrites the display string. The
backfill is a separate, smaller, and independently useful tool — it turns English prose into
queryable tags — and it is the batch-ready half. Only after it runs is the normalizer's
"deterministic table lookup" description actually true.

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

## 31. Per-request HTTP timeout + retry cap in the OpenRouter client (runner hangs survive the outer `timeout` wrapper)

**Source**: 2026-06-30 routine accuracy-review run (screening pass stalled)

`build/review_runner.py` (screening) and `build/review_accuracy.py` can **hang
indefinitely on a single OpenRouter request** and, crucially, **survive an outer
`timeout` wrapper** because their per-entry work runs in child workers in a
*separate process group* — the wrapper's SIGTERM does not reach the stuck child.
On 2026-06-30 a screening pass stalled at **~entry 33/500** and had to be killed by
name (SIGKILL) before the run could proceed. This is distinct from
[item 21](#21-chunk-the-reviewscreening-runners-to-fit-the-session-timeout):
item 21 is about *sizing the ID range* so a healthy pass finishes inside the wall
budget; this item is about a *single request that never returns*, which no amount of
range-sizing fixes — a 1-entry pass would hang just as hard.

**Suggested fix**: add a **per-request HTTP timeout** to the OpenRouter client (e.g.
`requests`/`httpx` `timeout=(connect, read)` on every call) plus a **hard cap on
retries** with backoff, so a single slow/dead request fails that entry cleanly
(logged and skipped, per the item-13 per-entry try/except hardening) instead of
wedging the whole pass. Secondarily, ensure child workers share the parent's process
group (or install a SIGTERM handler) so the outer `timeout` wrapper can actually stop
them. Both are small, localized client-side changes and would make the OpenRouter
review modes reliably bounded under the Routine's time budget. Cross-reference
[item 13](#13-review_runnerpy-response-parsing-robustness) (per-entry robustness) and
item 21 (range sizing).

**Update 2026-07-21 (two more indefinite hangs in one run-window — the bug is live and recurring, and the outer `timeout` wrapper is the only mitigation)**: A 2026-07-21 accuracy-review run hit the hang **twice**: (1) `review_runner.py --pass screening` hung indefinitely on an OpenRouter/proxy call **after ~370 entries (16624→16993)**, process alive but no network progress and low CPU; and (2) on the same day a screening pass **wedged on a single entry (17046)** mid-range with no per-request timeout/retry — process alive but no network progress for ~10 min — and had to be **SIGKILLed**, keeping the 259 already-written results (16711–17045). The operator's workaround both times was to **wrap the invocation in `timeout` and run it backgrounded**, which bounds the wall-clock but discards the in-flight entry rather than skipping-and-continuing. This reconfirms the item exactly: a single stuck request strands the whole pass regardless of range size, and the only relief today is the coarse outer wrapper. The per-request HTTP timeout + skip-and-continue (fix above) would let the pass drop the one dead entry cleanly and finish; still the top-priority hardening for the OpenRouter review modes.

## 32. `add_adjective_conjugations.py` mishandles slash-variant i-adjective headwords

**Source**: 2026-07-11 routine polish run (priority lane, 00514_hayai)

For a slash-variant i-adjective headword like `{速|はや}い／{早|はや}い`,
`add_adjective_conjugations.py` treats the entire string as a single stem and
conjugates only the **trailing** variant, leaving the first variant frozen in
dictionary form across every inflected form (Present-negative / Past / て / ば /
たら). For example the Past-negative comes out
`{速|はや}い／{早|はや}くなかった` (first variant un-conjugated) instead of the
correct `{速|はや}くなかった／{早|はや}くなかった`. Running with `--force`
reproduces the bug.

**Scope**: only **2** slash-variant i-adjectives exist in the dictionary —
00475_yasashii (`{優|やさ}しい／{易|やさ}しい`) and 00514_hayai
(`{速|はや}い／{早|はや}い`) — and **both** carried the frozen-first-variant
tables. Both were hand-fixed in the 2026-07-11 run, so the current live scope is
zero. This is filed as a latent-defect / regression-guard item, not a backlog of
broken entries: any future slash-variant i-adjective created and run through the
tool would silently inherit the bug, and the conjugation tables are a live-site
feature.

**Suggested fix**: split the headword on the full-width slash `／`, conjugate each
variant independently through the existing single-headword path, then rejoin the
conjugated forms with `／`. Add a regression test covering a two-variant headword
so the per-variant conjugation is asserted on every form category. (The verb-side
`add_conjugations.py` should be checked for the same slash-headword assumption if
any slash-variant verbs exist or are later added.)

## 33. `prioritize_polishing.py --task notes` crashes with `KeyError: 'furigana'`

**Source**: 2026-07-15 routine polish run (priority lane wrap-up)

`build/prioritize_polishing.py --task notes` (and, by inspection, any single
-`--task` invocation) crashes with `KeyError: 'furigana'`: the code path that
handles a single requested task still indexes `results['furigana']`
unconditionally instead of the requested task's key, so it dies whenever the
requested task is anything other than `furigana`. Only the **arg-less**
`make priorities` path (which computes every task) currently works; the
per-task flag documented in `CLAUDE.md`
(`python3 build/prioritize_polishing.py --task notes # Generate priority for one task only`)
is therefore broken for `notes` and presumably for the other non-`furigana`
task names too.

**Impact**: low but real — a Routine `polish` run that wants to regenerate *just*
the notes priority file (the >half-no-op wrap-up path in routine2.md §2) cannot
use the documented targeted flag and must fall back to the full `make priorities`
regeneration. It also means the documented command in `CLAUDE.md` fails if a
curator runs it directly.

**Suggested fix**: index `results[task]` (the requested task key) rather than the
hard-coded `results['furigana']` in the single-task branch, and add a smoke test
that runs `--task notes` / `--task furigana` / `--task links` and asserts each
writes its own priority file without touching the others. Until fixed, either
correct the `CLAUDE.md` example to note the flag is `furigana`-only or point it
at `make priorities`.

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

## 35. Verb-class misassignment detector: conjugation tables contradicted by the entry's own examples

**Source**: 2026-07-25 routine polish run (06624 甘える, 09361 バックレる)

A verb entry's whole `conjugation` table is generated from its `pos` tag, so a **single wrong
class tag fabricates the entire table** — see
[Cleanup P25](cleanup-backlog.md#priority-25-fabricated-conjugation-tables-from-a-mis-assigned-verb-class)
for the two confirmed cases (06624 甘える tagged `verb-godan`, producing 甘えらない / 甘えります /
甘えった; 09361 バックレる likewise). This is among the worst silent-error classes the dictionary
can carry: conjugation tables are exactly what a learner copies without checking, and nothing in
the current pipeline looks at them again after generation.

**The detector to build is self-contradiction, not reading shape.** The obvious heuristic —
`verb-godan` + reading ending in -える/-いる — has a large, permanent false-positive family
(31 entries measured 2026-07-25: the 入る/返る compounds 若返る / 跳ね返る / 裏返る / 覆る / 甦る /
翻る / 気に入る / 痛み入る …, plus 炒る / 煎る), so it can only ever be a one-off scan with an
allowlist. The **self-contradiction** rule has no false-positive family at all:

> Flag a verb entry whose **own examples contain a conjugated form of its headword that its
> declared class cannot produce** — e.g. an entry tagged `verb-godan` whose examples show the
> ichidan past 甘えた / バックレた while its generated table claims 甘えった.

The entry is disagreeing with itself, so every hit is real: either the tag is wrong (regenerate
the table) or the example is wrong (fix the example). Both cases need a human decision, but
neither is a false alarm.

**Implementation sketch**: for each verb entry, generate the candidate conjugated forms for the
*declared* class (the logic already lives in `build/add_conjugations.py`) **and** for the
plausible alternative classes; scan the entry's own example sentences for occurrences of the
headword stem followed by an inflectional ending; flag when the observed ending is derivable only
from a class other than the declared one. Generalises to the reverse case (an ichidan-tagged godan
verb) and to `verb-suru` mis-tags, and pairs naturally with the existing conjugation-hygiene items
[5](#5-non-verb-conjugation-pruner--defensive-guard-in-add_conjugationspy) and
[10](#10-add_conjugationspy-false-positive-suru-detection-on-godan-verbs-ending-in-する).

**Then**: re-run `add_conjugations.py --force` on the confirmed mis-tagged entries after correcting
`pos`, and record the dictionary-wide hit count — two cases surfaced from a single frontier run's
incidental scan, which is not evidence that two is the total.

## 36. `verify_furigana.py` can't see entries created earlier in the same session

**Source**: 2026-07-25 routine new-entries run

`build/verify_furigana.py <id>` resolves the entry through `entries_index.json`, so during a
new-entries session — where entries are written to disk but `update_indexes.py` has not run yet —
it reports **"Entry not found"** for every entry the session just created. The tool is therefore
unusable at precisely the moment it is most wanted: immediately after writing an entry, before the
build. `build/find_missing_furigana.py` scans the filesystem and does find them, which is why the
gap goes unnoticed — the session falls back to the bulk scanner and never learns the per-entry tool
was silently inapplicable.

**Two fixes, either acceptable:**

- **Preferred** — fall back to a filesystem lookup when the index misses: glob
  `entries/*/{id}_*.json` before declaring the entry absent. This makes the tool
  order-independent and costs one `glob`. (`build/get_entry_path.py` already does filesystem
  resolution and can be reused.)
- **Minimum** — document the ordering requirement in `prompts/newentries.md`: per-entry furigana
  verification only works *after* `update_indexes.py`.

Note the same index-vs-filesystem split is the documented reason `get_next_id.py` scans the
filesystem (`CLAUDE.md`: "this script scans the filesystem, so it is accurate even mid-session").
The convention exists; `verify_furigana.py` just does not follow it. Distinct from
[item 2](#2-fix-verify_furiganapy-false-positives-on-inline-links), which is about what the tool
reports *once it finds* the entry.

## 37. Detector: copula て-form `で` inline-linked to the particle `で`

**Source**: 2026-07-26 routine polish run (な-adjective block 06639–06644)

Inline linking systematically confuses two different `で`. In `元気で`, `不器用で`, `頑固で` the
`で` is the **te-form of the copula だ** (→ `09496_da`), not the **particle で** (`00502_de`) — but
existing entries link it to the particle. The error is invisible to every current check: the link
resolves, the surface matches, and only the grammar is wrong.

**Detector rule** (high precision, cheap): flag `⟦で→で：00502_de⟧` occurring **immediately after a
na-adjective stem** — i.e. the preceding token is the headword of a `adjective-na` entry, or the
link directly follows another inline link whose target is an `adjective-na` entry. The same shape
covers the noun-predicate case (`学生で…`), which is also copula, so the rule may be worth widening
to "`で` preceded by a noun/na-adjective and followed by a clause boundary" once the narrow version
is calibrated.

**Also needed, and cheaper than the detector**: the `inline-word-links` skill should **state the
rule explicitly**. The polisher currently has no guidance and defaults to the particle because that
is the entry the reading lookup returns first. Documenting it stops new instances; the detector
cleans up the existing ones. (Curator action — a `wiki` run may not edit skills.)

**Related**: the same "the link resolves so nothing complains" blind spot as
[item 11](#11-inline-link-target-id-resolution-gate-in-validatepy-or-pre-commitci) and
[Cleanup P24](cleanup-backlog.md#priority-24-inline-link-base-forms-written-with-furigana-braces) —
three distinct defect classes inside `⟦…⟧` markup that no check inspects.

## 38. `review_accuracy.py --ids` destroys the §A review record when §4 re-reviews the same entry

**Source**: 2026-07-27 routine accuracy-review observation.

`build/review_accuracy.py` writes each entry's findings to `reviews/accuracy/{id}.json` and
**overwrites in place**. Within a single `accuracy-review` run that is a self-inflicted data
loss: §A reviews a range and writes the records, the run applies corrections, and then §4
self-verifies the entries it just changed with `--ids <same ids>` — overwriting each original
review with the post-fix one. The evidence for *why* a correction was applied is gone by the
time anyone reads the ledger.

**Impact**: the `reviews/accuracy/` tree is the only per-flag artifact with the model's actual
reasoning; `reviews/decisions.jsonl` keeps a ≤10-word note. Precision analysis that wants to
re-read a disputed flag can only do so for entries no self-check touched — a silent, biased
gap in exactly the entries that changed.

**Fix (either is cheap)**:
- add a `--phase <label>` argument that suffixes the output path
  (`reviews/accuracy/{id}.self-check.json`), or
- write to `reviews/accuracy/{id}.{n}.json` when a record already exists.

The first is preferable: it matches the `src` values already used in `reviews/decisions.jsonl`
(`accuracy` vs `self-check`), so the artifact tree and the ledger stay joinable.

**Related**: [quality-metrics](../topics/quality-metrics.md) (flag-precision analysis depends on
these records); the routine's §4 self-verification step.


## 39. Cross-reference-pair tag consistency check (antonym/pair tag drift)

**Source**: 2026-07-27 routine polish observation (frontier 06650–06655).

Entries linked as `antonym` or `pair` describe the same semantic field from opposite ends, so
their `semantic` and `formality` tags should almost always match. They frequently do not,
because each entry was tagged independently, often months apart. Measured instance: **06528
連勝** carried `formal` / `action` while **06529 連敗** carried `neutral` / `leisure` — same
domain, same register, same day's reading, four tags between them and three disagreements.

**Detection rule**: for every `cross_references` entry of type `antonym` (and `pair`), compare
the two entries' `tags.semantic` sets and `tags.formality` / `tags.politeness` values. Flag
when the semantic sets are **disjoint**, or when formality/politeness differ. Both are
review-queue signals, not auto-fixes — a genuine register asymmetry exists (謙譲 pairs,
slang↔standard antonyms), so the output needs a glance per pair.

**Why it is high-yield**: the check is free (no model call), it runs over a small population
(cross-referenced pairs only), and a disagreement means **at least one of the two entries is
wrong** — which is a much stronger prior than any single-entry tag heuristic on this page.
It also catches drift the accuracy reviewer structurally cannot see, since that reviewer
judges one entry at a time against its own headword.

**Natural home**: `build/check_semantic_clusters.py`, which already walks
transitivity/antonym/keigo clusters looking for *missing* links — this adds "present but
inconsistent" to the same traversal.

**Related**: [Cleanup P11](../ideas/cleanup-backlog.md#priority-11-batch-creation-semantic-tag-transportation-misapplied),
[Cleanup P17](../ideas/cleanup-backlog.md#priority-17-formal-formality-tag-over-applied-in-early-entries),
[item 6](#6-tag-drift-detector).


## 40. Conjugation-table-vs-headword invariant in `check_consistency.py`

**Source**: 2026-07-27 routine systemic-fix observation (22000–23499 wrapper sweep).

An over-wrapped verb headword silently corrupts the entry's generated conjugation table.
**22070 走り続ける** shipped with the whole-word wrapper `{走り続ける|はしりつづける}`;
`add_conjugations.py` strips the ichidan る by inspecting the *rendered* tail, and a whole-word
wrapper hides that tail, so all **33** generated forms doubled the stem —
`{走り続ける|はしりつづける}る` renders as 走り続けるる, `…ます` as 走り続けるます, and so on down
the table. The entry **validated cleanly** and the defect survived from creation (2026-04-04)
until a wrapper sweep happened to rewrap the headword and `--force`-regenerate.

**The invariant**: for `conjugation.type` in `{ichidan, godan}`,
`strip_furigana(forms[0].affirmative)` must equal `strip_furigana(headword)`. One line of
comparison per verb entry, no model, no heuristics.

**Scope**: a dictionary-wide sweep for the signature after the fix found **0 other live
instances**, so this is not a backlog — it is a guard. That is the point: the check costs
nothing, would have caught 22070 at creation, and any future over-wrapped verb headword
reintroduces the same silent corruption. It also raises the stakes of
`check_furigana_format.py`'s `over-wrapped` class from cosmetic to **data-corrupting when the
entry is a verb**, which is worth reflecting in that detector's severity assignment.

**Related**: [Cleanup P9](../ideas/cleanup-backlog.md#priority-9-malformed-furigana-wrappers)
update 2026-07-27, [item 35](#35-verb-class-misassignment-detector-conjugation-tables-contradicted-by-the-entrys-own-examples)
(the other family of wrong-but-valid conjugation tables), [item 5](#5-non-verb-conjugation-pruner--defensive-guard-in-add_conjugationspy).

## 41. `manage_candidates.py` cannot queue a homograph — the duplicate check is (surface, reading), not (surface, reading, sense)

**Source**: 2026-07-28 routine polish run (00304_nandemo and the 〜でも question-word cluster).

`manage_candidates.py add` refuses a word when an entry already exists with the same
surface form and reading. That is the right default and it prevents most accidental
duplicates — but it makes the tool **structurally unable to queue a homograph**, which is
exactly the case where a new entry is most clearly needed.

**The worked case.** The particle **でも** ("any ~" in 何でも / 誰でも / いつでも, and "even ~")
has no entry. The two entries that occupy the surface form are different words:
`00925_demo` is the sentence-initial conjunction "but, however", and `19416_demo` is デモ
"demonstration". A polishing session that wants to link ⟦でも⟧ therefore has to write
`：noentry⟧` — and then cannot even leave a candidate behind, because `add` sees
`でも/でも` and rejects it as a duplicate. **The gap is self-concealing**: the one mechanism
the project has for recording "this word needs an entry" refuses precisely the words whose
absence is hardest to notice. The same block applies to the sibling gaps in
`08498_daredemo`, `03826_itsudemo`, and `08499_dokodemo`.

**Why this is worth fixing rather than working around.** The `noentry` marker is not a
neutral placeholder — [item 19](#19-stale-noentry-inline-link-detector) documents how those
markers go stale and accumulate. A `noentry` that *cannot* be paired with a candidate is
permanently stale by construction: nothing will ever create the entry that would resolve
it, because nothing recorded that it was wanted. Every homograph gap thus quietly converts
into a permanent dead link.

**Suggested fix**, in increasing order of effort:

1. **A `--force` flag** on `add`, which downgrades the duplicate check to a warning. One
   line, unblocks the immediate case, but discards the reason for the override.
2. **A disambiguator field** — `add "でも" "でも" "gloss" --sense "particle: any ~/even ~"` —
   stored on the candidate and surfaced to the new-entries session, which is the consumer
   that actually needs to know *which* でも it is being asked to write. This is the form
   that matches how the block manifests: the problem is not that the check is too strict,
   it is that (surface, reading) is the wrong key for a language with this many homographs.
3. Have `check_duplicate.py` report the *senses* of the colliding entries rather than just
   their IDs, so the session can tell a genuine duplicate from a homograph without opening
   both files.

Option 2 is the one worth building; 1 is an acceptable stopgap. Related:
[item 23](#23-candidate-pool-pre-filter-for-corpus-harvesting--manage_candidates)
(the same script's other structural problem, from the opposite direction — it accepts far
too much corpus residue while rejecting words that are genuinely needed).

## 42. Routine container image lacks `jsonschema` and `pytest`

**Source**: 2026-07-28 routine polish run

The unattended Routine container ships without two Python packages the project's own
documented commands need:

- **`jsonschema`** — `build/validate.py` self-installs it on first use, which works but
  costs a network round-trip at the start of every run and **needed a retry after a proxy
  read timeout** on 2026-07-28. That is a per-run failure mode sitting in front of the
  single most-called script in the project: a validation step that fails for an
  infrastructure reason is indistinguishable, from the run's point of view, from a
  validation step that fails for a data reason.
- **`pytest`** — absent entirely, so **`build/tests/` cannot be run in a Routine at all**.
  The project has a unit-test suite that no unattended run has ever executed. Every
  build-script change shipped by a Routine (and several have been) went out with the
  suite unrun, relying on CI to catch regressions after the merge rather than before it.

**Fix**: pre-install both in the image (`pip install jsonschema pytest` at build time).
This is a curator/infrastructure action, not a repo change.

**Why it is worth more than its size suggests**: the second half changes what a Routine
is *allowed to do safely*. Several items in this backlog (11's validate.py gate, 19's
detector, 24's lint) are one-line-to-fifteen-line build-script changes that a Routine
could in principle ship itself, but shipping a build-script change without being able to
run the tests is a step the current discipline correctly refuses. Making `pytest`
available is the cheapest available widening of the Routine's safe scope — and note the
alternative reading before acting on it: if the intended design is that Routines *never*
modify build scripts (which is what `prompts/routine2.md` currently implies by routing
every such item to the curator), then only `jsonschema` needs pre-installing and the
`pytest` gap is by design. Worth a curator decision either way, since the status quo —
tests exist, cannot run, and their absence is discovered per-run — is the one option
that serves neither reading.

## 43. `check_duplicate.py`: a reading-identical hit deserves a stronger verdict than a parenthetical

**Source**: 2026-07-29 routine new-entries run

`build/check_duplicate.py` keys its headline verdict on the (surface, reading) pair, and
reports reading-only matches as a trailing note. In this run, **のこぎり** and
**折りたたみ傘** both came back `OK` — while being plain orthographic variants of existing
entries **05477 {鋸|のこぎり}** and **20390 {折|お}り{畳|たた}み{傘|がさ}**. The homophone note
did fire, but as `[Note: Homophones exist: …]` beneath a green verdict, which is exactly
the shape a run skims past.

**Fix**: when a candidate's reading matches an existing entry's reading *exactly*, emit a
distinct verdict — `LIKELY VARIANT` — rather than `OK` with a footnote. The information is
already computed; only its prominence is wrong.

**Why the distinction is real**: a true homophone (different word, same sound) and an
orthographic variant (same word, different script) are the same string comparison but
opposite editorial outcomes — the first *should* become a separate entry, the second
should be merged into the existing one per the `word-variants` policy. The script cannot
tell them apart automatically, and it should not try; what it can do is stop presenting
the ambiguous case as a clean pass. A careless run reading `OK` writes a duplicate; a run
reading `LIKELY VARIANT — check 05477` opens the file.

Note the relationship to **item 41** (`manage_candidates.py` cannot queue a homograph):
the two scripts have inverted failure modes on the same comparison — one refuses genuine
homographs as duplicates, the other passes genuine duplicates as distinct words. Both
follow from treating (surface, reading) as an identity key when the project's actual
identity criterion is (surface, reading, **sense**). Fixing them together, with one
shared helper that returns a three-way classification, is more likely to be right than
patching either alone.

**Update 2026-07-30 — a third failure mode on the same key, this one on the write side: okurigana variants enter the queue as new words.** The 2026-07-29 `new-entries` run found **売り上げ** queued as a candidate; it is an okurigana variant of the existing **04102_uriage** (`{売上|うりあげ}`), not a distinct word, and was removed rather than written.

The mechanism is the same identity key seen from a third angle. `売り上げ` and `売上` are different *surfaces* with the same reading, so a (surface, reading) comparison sees no duplicate and the candidate is accepted — even though okurigana variation is precisely the case where surface difference does not imply word difference. Capture during polishing writes whatever spelling the source text used, so the queue accumulates these silently and each one costs a future `new-entries` run a lookup and a deletion.

The fix belongs with items 41/43 rather than beside them: the shared identity helper should **normalize okurigana before comparing** (strip optional kana between kanji, or compare against the existing entry set by reading and then check surface compatibility). That makes the same helper answer all three questions — homograph, duplicate, orthographic variant — from one classification, which is the argument items 41 and 43 already make for consolidating them. Relatedly, [Cleanup P32](cleanup-backlog.md#priority-32-inline-link-base-forms-written-in-kana-instead-of-the-dictionary-form) and [Entry Follow-ups](entry-followups.md) show the same normalization gap in inline links and merge candidates; the notion of "same word, different spelling" is missing project-wide, not just from `manage_candidates.py`.

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

## 45. Extend the decisions-ledger `n` aggregation from `reject` to `flag`

**Source**: 2026-07-29 routine wiki harvest (raised by the harvest itself while compiling the twenty-seventh metrics refresh)

`prompts/routine2.md` §C permits one aggregated ledger line with an `"n"` count when a run
bulk-**rejects** a recurring noise family, but provides no equivalent for bulk
**escalations**. The asymmetry produced a measurable distortion the week it first mattered:

> A single 2026-07-29 accuracy-review escalated **161 off-vocabulary tags that had no
> destination in `TAG_MIGRATION`**. Because each needed its own `flag` line, the ledger
> recorded 161 events, and the series' summary statistics recorded **the largest escalation
> event on record (162)** — where the honest description is *"one missing lookup table,
> 161 instances"*.

Every downstream consumer inherits the distortion: `topics/quality-metrics.md`'s escalation
counts, `metrics_snapshot.py`'s `flags_to_curator` field, and `reviews/needs_curator.txt`,
which stood at 102 lines mostly describing one cause. The metrics page has since added
finding 11 ("escalation *volume* is a queue signal, not a quality signal, and should be
weighted by distinct cause") — but that is a reader-side caveat compensating for a
recording-side defect, which is the weaker of the two places to fix it.

**Fix**: one sentence in §C extending the `n` convention to `flag` decisions, with the same
shape already specified for rejections (no `entry` field, an `"n"` count, a `note` naming
the family). Cost: one sentence. Benefit: escalation counts become countable by *cause*,
which is what every reader of them actually wants.

**Second-order benefit worth noting**: `needs_curator.txt` becomes readable. A curator
opening a 102-line file of near-identical entries cannot see how many distinct decisions
are being asked of them; a file with one line saying "161 off-vocab tags, no 1:1 target"
states the actual ask. The escalation channel's value depends on the curator reading it,
and 161-line families are how that stops happening.

**Caveat for whoever implements it**: the existing ledger already contains the 161 individual
lines, so any precision statistic spanning 2026-07-29 needs the aggregation applied
retroactively (or the window annotated) before it can be compared with later windows.

## 46. Pre-scan off-vocabulary tags deterministically and feed the list to the accuracy reviewer

> **Update 2026-08-01 — two more blocks, and the ordering is now settled practice.** In
> 22767–23100, **110 of the 118 entries the paid reviewer flagged on `tags` had already been
> identified by the free `VALID_SEMANTIC` diff**; the reviewer's marginal contribution was 10
> flags on in-list tags (2 applied) plus concrete destinations for tags the 1:1 map cannot
> reach. In 23101–23500 the free scan found **171 of 400 entries (43%)** off-vocabulary, and of
> the paid pass's 54 tag flags on post-migration entries, **38 either re-suggested a tag the
> free scan had already applied or proposed `general`** — only 4 were novel and correct
> (`action` on 鋳造/団体行動, `shopping` on 即日配送, `appearance` on コンシーラー). Five
> consecutive blocks now agree: **the free scan is the detector; the paid pass is a destination
> oracle plus in-list check.** Running them in that order is what the last two accuracy-review
> runs did, and it should be the documented default rather than a per-run choice.

**Source**: 2026-07-30 routine accuracy-review (21301–21900)

The accuracy reviewer flagged off-vocabulary semantic tags on **245 of 598** entries in
21301–21900. A free deterministic scan of the same range against `VALID_SEMANTIC` found
**275** — so the model **missed ~11%** of a class that is decidable by set membership,
without a model, in milliseconds.

This is a different criticism from item 17's (which is about the reviewer's *false
positives* on in-list narrowness nits). Here the reviewer is being paid to perform a set
lookup and is performing it **imperfectly**, which is the worst combination: it costs money,
it is slower, and its output cannot be trusted as complete, so a deterministic scan has to
be run anyway to know what was missed.

**Proposed sequencing change** — the reviewer should never be asked "is this tag in the
list?":

1. Run `check_tag_drift.py --check unknown-semantic` over the range first (free).
2. Auto-migrate whatever `TAG_MIGRATION` resolves 1:1 (item 6).
3. Pass the *residue* to the model as an explicit input — "these tags are known to be
   off-vocabulary; choose the best in-list destination for each" — rather than asking it to
   find them.

Step 3 is the part only a model can do, and giving it the list converts the task from
*detection* (where it underperforms a regex) to *judgment on a supplied list* (where it is
the only available instrument). Item 6's 2026-07-30 update measures why step 3 cannot be
eliminated: the ~100-distinct-string tail is genuinely judgment-dependent.

This also composes with the §A budget rule. Detection currently consumes a share of the
per-run OpenRouter budget to produce an incomplete answer; moving it out leaves the same
dollars buying only judgment, which is the scarce thing.

**Update 2026-08-06 — a sixth confirmation, a stable ratio, and the ceiling on the pre-scan's own
map.** The 2026-08-06 accuracy-review over 25872–26188 measured the split again: **118 of 146
reviewer `tags` flags (81%) were the same off-vocabulary family the free
`check_tag_drift.py --check unknown-semantic` diff finds for $0**, leaving 28 flags of genuine
marginal value, 11 of those being sole-`general` entries with an obvious in-list replacement. Six
measurements now agree that the paid reviewer's marginal contribution on this dimension is
**~19% of its flags**, which is the number this item's ordering argument rests on.

The same run proposed the natural extension — grow `TAG_MIGRATION` by "~55 more 1:1 mappings" so
the pre-scan suggests destinations as well as detecting offenders. That premise was measured in
the [P20 2026-08-06 update](cleanup-backlog.md#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration)
and it bounds this item rather than extending it: the off-list population is **687 distinct names
over 3,208 instances**, 55 more head mappings reach 40.6% cumulative coverage, and every rule
that generates a mapping *without judgment* covers only 78 names / 196 instances. So the honest
specification for the pre-scan is: **detect exhaustively (it already does), suggest for the ~11%
the shipped map covers plus whatever head mappings get added, and hand the rest over as
detected-but-undestined**. A pre-scan that promises destinations it cannot supply would re-import
the judgment cost this item exists to move off the paid pass.

## 47. Cross-reference `headword` fields are invisible to every furigana instrument (7 confirmed defects)

**Source**: 2026-07-30 routine wiki harvest (raised while checking whether `check_artifacts.py` covers a target-less cross-reference shape reported by the 2026-07-29 polish run)

Every furigana instrument the project owns — `check_furigana_format.py`, the OpenRouter
screening and deep passes, `find_missing_furigana.py`, `verify_furigana.py` — scans
`examples` and `notes`. **None scans the `headword` field inside `cross_references` and
`prominent_see_also` entries**, which are furigana-annotated strings rendered on the live
site exactly like any other.

The gap is measurable because those reference objects carry a redundant `reading` field, so
each one **checks itself**: expand the `headword`'s furigana and compare it with the declared
`reading`. Over the whole dictionary:

| Stage | Count |
|---|---|
| Refs whose expanded headword disagrees with the declared reading | 869 |
| …restricted to *fully* furigana-annotated headwords (a fair comparison) | 116 |
| …after normalizing `〜`/`～` affix markers, `／` slash-variants, and katakana | **11** |

All eleven survivors were inspected and **seven are genuine furigana defects**, in three
families:

- **Over-wrapped okurigana** — `{見積|みつも}もり` → みつも**も**り (×3, entries 08312 / 04699 / 05153 as `{見積|みつも}もる`), `{肩透|かたすか}かし` → かたすか**か**し (17589), `{届|とどけ}け` → とどけ**け** (07555). The wrapper swallows a kana the surface then repeats.
- **Missing okurigana inside the wrapper** — `{弾|は}む` where 弾む is はずむ (04378).
- **Unmarked rendaku** — `ぎっくり{腰|こし}` declared ぎっくり**ご**し (08034).

The remaining four are one benign family: `{面倒|めんどう}くさい` declared めんどくさい (×4),
where both readings are current and the reference is recording the colloquial one.

Three things make this worth its own item rather than a note on item 8:

1. **The check needs no external data and has no judgment component.** It compares a field
   against another field in the same object. Precision here was 7/11 — and the 4 misses are
   a single enumerable family that can be whitelisted.
2. **The normalizations are already written.** `〜`/`～` affix markers and slash-variants are
   the same two families item 11 had to normalize for base-form agreement; the katakana one
   is a kana-folding call. Reusing that logic is most of the implementation.
3. **The field is user-visible.** These strings render in the cross-reference block, so a
   wrong reading here teaches a wrong reading, with no more excuse than one in an example.

**Related finding — `check_artifacts.py`'s `missing-target-id` has a filter that hides
malformed refs.** The same harvest checked the 2026-07-29 report that target-less
cross-references still exist (06686 否応なく carried
`{"type":"synonym","reading":"ひっすに","headword":"{必然|ひつぜん}に"}` — no `target_id`, and the
reading not even matching its own headword). The detector's test is
`not ref.get("target_id")`, which correctly catches both the absent key and an empty value.
But it then skips any ref whose word has no entry, treating it as an *intentional pointer*
(`ref_is_resolvable`). A ref like 06686's — whose declared reading does not match its own
headword — is not an intentional pointer, it is malformed, and the resolvability filter is
exactly what suppresses it. The self-consistency check above is the cheap way to see that
class, and it should run **regardless of resolvability**, since a ref that disagrees with
itself is wrong whether or not a target exists.

**Suggested implementation**: a `--check ref-reading-disagreement` sub-check on
`check_artifacts.py` (it already walks both reference fields), emitting the 11-row queue
with the `面倒くさい` family whitelisted. Read-only, JSON queue, no auto-fix — three of the
seven defects need a human to decide the correct wrapper split.

## 48. The §7 CI gate cannot distinguish "CI is slow" from "CI never started" — and its cross-check agrees with it when it is wrong

**Source**: 2026-07-30 routine wiki run (raised by that run's own merge path, on PR #3069)

`mcp__github__pull_request_read --method get_check_runs` returned `total_count: 0` on **eight
consecutive polls over ~14 minutes**. The run cross-checked with
`actions_list --workflow validate.yml --branch <branch>`, which **agreed** — also `total_count: 0`.
Both were wrong: the workflow job's own `started_at` was 07:46:00Z, i.e. it had been queued
*before* most of those polls. It became visible only after a later push, then ran to `success`
in 60 seconds.

By then the run had written a session-log section concluding "no workflow run was ever queued"
and had stopped without merging.

**The durable rule**: *absence of a check run is only ever evidence of "not visible yet", never
of "not queued".* Neither endpoint is authoritative about absence — only about presence. This is
the same shape as every case on [Instrument Defects](../topics/instrument-defects.md): the
instrument's silence read as a fact about the world. What makes this one worse than the others is
its position — it sits in the **merge** path, where a wrong reading strands finished work.

**Consequence for `routine2.md` §7** (documentation only; the wiki mode does not edit prompts):

- The `actions_list` cross-check does **not** buy an unattended run the ability to tell a slow CI
  from a dead one. Adding it as a tie-breaker would be false precision.
- The honest options are unchanged: keep polling to the cap, or leave the PR for the next run's
  §0a rescue. Both are already in the prompt.
- What should change is the **log wording**. A run that times out should write "checks not visible
  within the cap" — never "no workflow run was queued". The first is what was observed; the second
  is an inference the data does not support, and it is the sentence that turns a recoverable strand
  into a misleading record for whoever reads the log next.

A cheap mitigation worth considering: when the poll cap is reached, fetch the PR head commit's
`started_at`/`created_at` via `get_commit` before writing the log line, so the record at least
carries the timestamp evidence rather than the inference.

**Update 2026-08-01 — a third failure mode, and it inverts the first two.** The 2026-08-01 wiki
run's own §7 gate hit something the item did not anticipate: `get_check_runs` served a **stale
`in_progress` for ~19 minutes on a check that had already succeeded**. PR #3084's `validate` check
started at 03:31:02 and completed `success` at 03:31:59 — **57 seconds**. The poll loop called
`mcp__github__pull_request_read method=get_check_runs` ten times across ~19 minutes of wall clock
and got `status: "in_progress"` every time, including polls made 15+ minutes after the job had
finished. The run hit the ~8-minute cap, correctly took the documented fallback (leave the PR open
for the next run's §0a rescue), and merged only because an unrelated stale background-sleep
notification prompted one more opportunistic poll — which returned the true state instantly.

Two consequences:

1. **A pending reading is not evidence that the check is pending.** The first two failure modes
   were both about *under*-reporting progress ("is CI slow or dead?"); this one is the endpoint
   being stale in the **success** direction, which no amount of patience distinguishes from a slow
   check. Without the accidental extra poll this PR would have stranded, and the session log would
   have recorded "CI never went green" — a sentence that is simply false.
2. **There is a usable staleness predicate, and it is one line.** The stale payloads omitted
   `completed_at` entirely. So: *a check-run object with no `completed_at` whose `started_at` is
   more than a few minutes old is more likely stale than running.* The gate's classifier could
   treat that as "re-poll once after a longer delay before declaring a timeout" rather than
   counting it as an ordinary pending. On this PR that predicate would have merged on the third poll.

Worth recording positively alongside it: **the strand-recovery design worked exactly as
specified** — PR left open, no further pushes that would restart CI, lock released so the next run
was unblocked, §0a rescue standing by. The defect is detection latency, not recovery design, and
the two cheap mitigations above (re-poll once past the cap; test `completed_at` rather than only
`status`) need no new instrument.

## 49. Read-only inline-link *suggester* (propose `⟦…⟧`, never write)

**Source**: 2026-07-30 routine polish run (measured on 06702, 10 unlinked examples)

**Inline-link coverage is the dominant cost of `polish` mode, and roughly 90% of it is
mechanical.** The measured split for one entry: ~60 dictionary lookups against
`build/word_id_lookup.json`, then a handful of genuine judgments — homograph choice, word
boundaries, whether a bound morpheme counts as a word. Batching all of an entry's lookups into
one query already helped materially; the remaining cost is the model doing greedy longest-match
segmentation by hand, one span at a time, which is what a program does better.

**Proposal**: a read-only script that takes an entry ID, runs greedy longest-match over
`by_headword` / `by_reading`, and emits (a) a proposed `⟦surface→base：id⟧` rewrite of each
example and note line and (b) an **explicit ambiguity list** — spans with more than one candidate
target, spans matching only by reading, and spans it declined to link. It never writes an entry.

The precedent is the detector family: **propose, never apply**. The value is not automation, it is
*budget reallocation* — a polish run would spend its judgment on the 10% that needs judgment and
could plausibly cover 2–3× the entries at the same quality. Sequenced naturally ahead of
[Cleanup P21](cleanup-backlog.md#priority-21-unlinked-自動詞他動詞-labels-and-particles-in-compound-verb-notes),
which is a several-hundred-entry backlog of exactly this work.

Known hazards the ambiguity list must surface rather than resolve: kana-only spans matching
multiple homophones (the standing `by_reading` false-match caveat, Cleanup P2), particles and
copula forms (`で` as copula vs particle — item 37), and base forms whose target headword needs
furigana stripping (items 11 / Cleanup P24, P32).

## 50. `find_missing_furigana.py --json` is accepted but does not emit JSON

**Source**: 2026-07-30 routine new-entries run

The flag is accepted silently and the output is human-formatted, JSON-ish text that `json.load`
rejects. Any caller that trusts the flag gets an exception, or — worse in an unattended run —
falls back to parsing the human format with a regex.

Two acceptable fixes: implement a real `--json` mode (the tool already has the records in hand),
or drop the flag so the failure is loud at argument-parsing time. Either is a few lines. The
current state is the one state that should not exist: an option that claims a contract it does
not honour.

## 51. A cross-reference with no `target_id` validates cleanly — but the obvious schema fix would break 59 intentional refs

**Source**: 2026-07-30 routine polish run (06704, removed in-run) + this harvest's corpus scan

`build/validate.py` checks that a `target_id` *resolves*, not that one is *present*. A reference
object of the shape `{type, reading, headword, label}` with no `target_id` at all therefore passes
validation and renders as nothing on the page — silently invisible.

The polish run proposed a one-line schema `required: ["target_id"]` on `cross_references[]`.
**A corpus scan says that would fail.** Dictionary-wide, 64 reference objects have no `target_id`:

| Shape | Count | Verdict |
|---|---|---|
| No `target_id`, **has** a `label` | 59 | **Intentional** — homophone/contrast pointers to words with no entry (`{工夫\|こうふ}` "laborer (homophone)", `イエス` "yes"), the class [Cleanup P2](cleanup-backlog.md#priority-2-missing-or-broken-cross-references) and item 25 already documented |
| No `target_id`, **no** `label` | 5 | **Defects** — 06057, 06060, 06063, 29601, 29610 |

So the rule the schema wants is not "`target_id` is required" but **"`target_id` or `label` is
required"** — a reference must either point somewhere or say why it does not. That expresses the
existing convention exactly, closes the 5 defects, and leaves the 59 deliberate pointers valid.

Scope is small enough to fix by hand (5 entries: each names a real word — 推薦する, 創造する,
肯定する, 年少, 炭素 — that has or deserves an entry), but the schema clause is what prevents the
class from returning.

## 52. Does `check_semantic_clusters.py` count a `prominent_see_also` mention as satisfying the pair requirement?

**Source**: 2026-07-30 routine polish run (00649 曲がる / 02529 曲げる, 00711 かかる / 00854 かける)

Both transitivity pairs described the pair **in their notes**, listed it in **`prominent_see_also`**,
and had **`cross_references: []`** on both sides — so the machine-readable pair link did not exist
in either direction, and `check_semantic_clusters.py` did not report it.

If the checker treats a `prominent_see_also` mention as satisfying the pair requirement, that is
the hole, and it is a one-condition fix. If it does not, then these pairs should have been in its
queue and the miss has a different cause worth finding.

**Scope**: entries with an empty `cross_references`, a non-empty `prominent_see_also`, and
transitivity prose in the notes number **407** dictionary-wide (this harvest's scan). Not all are
pair defects — the filter is deliberately loose — but it bounds the class, and 407 is large enough
that "the checker sees this and stays quiet" is worth verifying before more of the frontier is
polished on the assumption that it does not.

Related: item 39 (cross-reference-pair tag consistency), item 25 (target-id resolution).

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

## 54. Candidate-list quality filter: reject inflected forms and number+counter strings at harvest time

**Source**: 2026-07-31 routine new-entries run (30259–30278) and 2026-07-31 routine
accuracy-review — two independent runs reporting the same thing within a day

The ~1,000 candidates outside the `seen in entry` set are dominated by corpus-harvesting noise
in three families:

| Family | Examples |
|---|---|
| Inflected forms of words that already have entries | 激しく, 知らない, 勝てない, 優しく |
| Compositional phrases and number+counter strings | 三年前, 一年前, 四十五, 二千円, 森の中, 片面印刷 |
| Apparent non-words / coinages | 権使, 些道, 個尊, 怒燥, 多角的一面 |

Sampled windows put usable headwords at roughly **1 in 10**, so a `new-entries` run working the
oldest-first fallback order burns a large share of its context sifting rather than writing.

Two fixes, and they are complementary: a **harvest-time filter** (an inflected form is
detectable by lemmatising against `word_id_lookup.json`; number+counter is a regex) stops the
inflow, and a **scoring pass** that demotes rather than deletes makes the existing fallback
order usable without a destructive edit to `candidate_words.json`. A manual
`clean_up_candidates_list` pass would clear the arrears but not the source.

**Interacts with [item 23](#23-candidate-pool-pre-filter-for-corpus-harvesting--manage_candidates)**: the selector's `candidates_low`
signal counts ~1,000 candidates and stays quiet, while the pool a run can actually write from is
near empty. Scoring would make that count mean something.

**Update 2026-08-02 (third and fourth independent reports; the ratio is now measured twice the same way).**
A 2026-08-02 `new-entries` run reported the identical shape: **all 15 "seen in entry" candidates
were good**, and it had to hand-pick **7 defensible words out of hundreds scanned** from the
remaining ~990 (三百, 六歳, 全商品, 倍率器, 個尊, 些道, 怒燥 …). That is the same ~1-in-10 usable
rate from a different day and a different run, so it is a property of the pool rather than of one
sample. The run also restated the selector consequence sharply: the real supply of entry-worthy
candidates is **~15 per run** — i.e. roughly one run's worth — while `routine_next.py` reads
`candidate_count: 998` and reports the pool as plentiful.

Three options were named, and they are not equivalent: (a) a curator restock of genuine
vocabulary, (b) a `clean_up_candidates_list.md` sweep to purge compositional residue, (c) teach
the selector to count only candidates passing a quality heuristic. **(c) is the one a Routine can
build**, and it is this item's scoring pass wired into the selector signal rather than a new
capability — but note it changes *reporting*, not supply. Only (a) and (b) change what a run can
actually write from, and (b) is arrears-clearing while the harvest-time filter above closes the
inflow. Sequenced: filter the inflow, score for the selector, then let the curator decide whether
to restock or sweep.

### Update 2026-08-03 — the variant-orthography check, measured, with the rule that works

A 2026-08-02 polish run found two "seen in entry" candidates (気ぜわしい, ぶり) that were
orthographic or notation variants of existing entries (気忙しい `15598`, 〜ぶり `28358`), and asked
for a variant check at add time. The polish-mode capture step records the surface form *as written
in the example*, so kana/kanji and 〜-prefixed variants of existing headwords enter the pool
looking new.

**Measured against the current 997 candidates:**

| Rule | Hits | Useful? |
|---|---|---|
| candidate reading matches an existing entry's reading | 28 | no — mostly homophones (権使/剣士, 三重/見得, 試戦/支線) |
| kana-only candidate whose reading matches an entry | 3 | too narrow — misses 気ぜわしい (mixed kana/kanji) |
| **shared reading AND ≥1 shared character** | **13** | **yes** |

The third rule is the one to implement. Its 13 hits are ~11 actionable: genuine variants
(おどりこ/踊り子 `14344`, りんご農家/林檎農家 `24042`, 摺り寄せる/擦り寄せる `26584`), notation
variants (〜着/着 `27655`, 中/〜中 `09840`), and coinages the pre-filter wants gone anyway
(計量化 vs 軽量化 `19238`, 些道 vs 茶道, 印示 vs 印字, 晶体 vs 正体, 解退 vs 解体). The two
arguable misses are 千人/仙人 and 自体/字体, real distinct words that share a character.

Note this is a *warning* at add time, not a rejection — `manage_candidates.py add` should print
the matching entry and let the caller decide, which also addresses
[item 64](#64-manage_candidatespy-add-does-not-say-what-it-rejected-or-why)'s complaint that the
command says nothing about what it did.

### Update 2026-08-04 — the supply is inside the pool, not outside it

A full scan of the non-"seen in entry" candidate pool (~980 words) by a 2026-08-04 systemic-fix run
found it "heavily polluted" in the ways this item already describes — compositional phrases
(裸足で歩く, 速やかに処理する), numeric fragments (四十五, 三千円), apparent non-words (権使, 些道,
個尊, 怒燥) — but added the observation that changes what the filter should *do*:

> The genuinely useful base words are usually buried **inside** a longer compound candidate —
> 換気扇掃除 (換気扇), 五月病患者 (五月病), 皆無である (皆無), 目盛り線 (目盛り), 人影もない (人影).

So the same string that fails the quality filter often *contains* a word worth an entry. A filter
that only rejects therefore throws away supply at the moment it identifies it, and the cheap
addition is a **split** step: when a compound candidate fails, try its plausible head (longest
prefix or suffix that is itself a known word or a plausible noun), check that against
`entries_index.json` and the candidate list, and queue the head instead of the whole string.

This matters because of the ratio this item has now measured twice: roughly 1 usable candidate in
10. A splitter recovers real supply from the 9 without any new harvesting — which is the cheapest
source of candidates available, and it does not depend on the corpus tooling at all.

### Update 2026-08-05 — the ~1-in-10 ratio, measured a third time

A `new-entries` run sampled ~200 candidates across the non-"seen in entry" pool and reported
"almost nothing entry-worthy", against 16 "seen in entry" candidates that were "all high-value by
contrast" — the same ratio, taken a third time by a third method, and the same three junk families
already enumerated above: transparent compounds (参加者数, 全商品, 三千円), inflected forms mistaken
for words (潔くない, 戦わない, 動かない), and coinages (権使, 些道, 個尊). No new family and no
change of recommendation. Recorded because three independent measurements agreeing is what makes
the ~980-candidate headline count safe to plan against as **~100 usable words** — which is the
number that should drive the curator-restock cadence, not the raw count the selector reports.

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
[Cleanup P36](cleanup-backlog.md#priority-36-headwords-written-as-bare-kanji-with-no-furigana-braces-248-entries).

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

## 57. `check_semantic_clusters.py` has no closed-paradigm symmetry rule

**Source**: 2026-08-01 routine polish run (ko-so-a-do demonstratives, 16 entries fixed);
2026-08-01 routine polish run (the non-negative ない adjective family);
2026-08-01 routine polish run (the 毎-/来-/今- calendar series).

The cluster linter checks *relations it knows the name of* — transitivity pairs, antonyms, keigo
levels. It has no concept of a **closed paradigm**: a small fixed set whose members should all
point at each other. Three independent runs hit the same failure in one week:

- **Demonstratives.** The そ- and ど- members (そこ, そちら, それ) carried `related` refs to their
  こ-/あ- siblings; ここ, こちら, これ, あれ, あそこ, あちら, どちら, どれ, どこ, こっち had
  `cross_references: []`. Sixteen entries, one direction only.
- **The non-negative ない adjectives** (せわしない, おぼつかない, {切|せつ}ない, はしたない,
  えげつない) — a family learners systematically misparse, where each entry explains the trap in
  isolation and none linked to the others.
- **The calendar series** (先月/今月/来月, the 毎- series) — documented in prose in every member's
  notes, structurally connected in none.

The shared tell is that **the paradigm is stated in prose in every member and structured in
none**, so it is invisible when reading an entry and shows up only in the rendered
cross-reference block. That also makes it undetectable by the generic "notes mention a word that
isn't in `cross_references`" heuristic of [item 55](#55-detector-contrast-words-named-in-notes-prose-but-absent-from-cross_references),
which needs the mention to be inline-linked; these paradigms sit largely above the link frontier.

The tractable form is a **declared-paradigm table** — a small data file listing each closed set by
entry ID (demonstratives, weekdays, months, the 毎-/来-/今- series, counter series, the ない
family) — and a linter rule that every member links to every other. Membership is a curator
judgment made once per set; enforcement is then mechanical and permanent. Unlike a heuristic
detector this cannot produce false positives, because the set is declared rather than inferred.

## 58. The review cursor advances to `end+1` even when the range above is already reviewed

**Source**: 2026-08-01 routine accuracy-review run (cursor regressed 23608 → 22900).

`polishing/tasks/cross-model-review/progress.txt` is set by §A step 6 to the end of the range just
reviewed, plus one. When a run works a range *below* the frontier — as run #3086 did, reviewing
22334–22899 after 22900–23400 had already been reviewed and adjudicated the day before — that
rule **moves the cursor backwards**, and the next run re-reviews and re-pays for entries that are
already covered.

The correct rule is to set the cursor to the lowest entry ID with **no** `reviews/accuracy/{id}_*.json`
file, which is derivable in one glob and is what the cursor was always meant to mean. Applying it
by hand this run moved the cursor to 23608 and exposed the true shape of the remaining work: the
un-reviewed frontier is **23608–30317 (~6,700 entries)** plus scattered holes below it (6926–7179,
7262–7640, 8238–8528, 9850–10449, 13975–14186, 16167–16373). Those holes are invisible to a
monotonic cursor and will never be reviewed until the rule changes.

This is a prompt/§A change rather than a script change, so it needs the curator (a `wiki` run may
not edit prompts). A small helper — `python3 build/next_unreviewed_id.py` — would make the rule
mechanical instead of a per-run instruction.

## 59. `check_link_baseform.py` should suppress proposals that change the reading

**Source**: 2026-08-01 routine systemic-fix run (link-target-baseform-disagreement, batch 2).

One queue finding proposed retargeting `被る` (かぶる) at `18070_koumuru` (こうむる). Inline links
are keyed on the surface word as it appears in the sentence, so **a proposal whose target has a
different reading than the link's base form is wrong by construction** — no per-entry reading can
make it right. Bucketing those separately (or suppressing them) removes a whole class of
never-appliable findings before a human sees them.

Two related refinements from the same run, both cheap:

- **`--by-base` should be the documented entry point, not `--json`.** Verifying the *decision set*
  (18 base-form families) rather than the occurrence set (90 links) collapsed the work ~5× — the
  same ratio the P27 dead-target retro recorded. Group by `(baseform, declared_target)` first for
  any link-integrity item.
- **The queue's real split is a semantic one worth surfacing in the output**: where the two kanji
  spell *different senses of one reading* (治る/直る, 抑える/押さえる, 越える/超える, 量る/測る,
  温める/暖める) the link is a genuine wrong-word error and the example sentence decides it at a
  glance; where they are the *same word under different orthography* (頃/〜ころ, 上げる/あげる,
  追いかける/追い掛ける, 焼きたて/焼き立て) there is nothing to fix. The tell is deterministic:
  **does the dictionary give the two spellings separate glosses?** If it does, the distinction is
  real. That predicate could pre-sort the queue.

### Update 2026-08-03 — the reading test is a *triage axis*, not just a suppression rule

A 2026-08-02 polish run worked a 56-item `check_link_baseform.py` queue and reported the sharper
form of this item's principle: the reliable split is **whether the proposal's reading matches the
surface furigana**, not whether the base and the declared headword "look different".

- **Reading MATCHES** → near-mechanical wrong-word repairs, decidable at a glance
  (鮭→酒, 麺→面, 級/急→九).
- **Reading MISMATCHES** → every trap in the queue: benign variant spellings (下/元, 球/玉,
  敵/仇), cases where the target is right and only the link's base label is loose (お得), and cases
  with **no correct target at all**.

Splitting on that one predicate turned a 56-item adjudication into **44 fast + 12 careful**. So
the refinement to this item is not only "suppress reading-changing proposals" but "**report the
reading-match verdict as a field**" and sort by it — the suppression is then the caller's choice,
and the queue arrives pre-triaged. The same run also recorded the honest outcome for the third
class: when the correct word has no entry and the same-kanji entry would mislead (性質上 の 〜上
じょう pointed at 状; 温帯 の 帯 たい pointed at 対), the fix is to rewrite the link to `noentry`
and add a candidate, not to find a less-wrong target.

### Update 2026-08-04 — the benign family the reading test already separates, and one it does not

A fourth `link-target-baseform` systemic-fix batch named the largest benign family explicitly:
**"imprecise base label, correct target"** — a link whose declared base is written with a kanji
spelling the target entry files under kana or different okurigana (様→`01114_you` よう;
臭い→`00874_nioi` におい as a spelling of 匂い). The link resolves to the right word; only the label
is spelled unhelpfully. The batch-3 reading test separates these reliably and the rule is worth
stating as code: *if the surface furigana reading matches the **declared** target's reading and the
proposal's reading differs, reject the proposal.*

The same batch found a family the reading test does **not** catch, because both sides read
identically: **noun ↔ suru-verb pairs cross-linked to each other's opposite form** (入院/入院する,
退院/退院する mutually pointing at the other's する entry). Where a bare-noun entry exists, a
bare-noun base should target it. Small, mechanical once spotted, and it is the same distinction
the `Xする` label Informational in the cleanup backlog is about — seen from the target side rather
than the label side.

**Update 2026-08-06 — the `ambiguous` bucket is not a curator queue, and treating it as one cost
four batches.** Four prior systemic-fix batches deferred the detector's 13 "ambiguous" findings
(more than one lookup candidate) to the curator. A 2026-08-05 run worked them and found **all 13
decidable, by the test this item already specifies**: the surface's own furigana names the reading,
and the reading selects exactly one candidate — 後 あと → 09580, 分 ぶん → 26216, 船 せん → 09875,
方 かた → 10665, 館 かん → 17308. The rule worth keeping is one line long:

> **Lookup ambiguity is not decision ambiguity.** `by_headword` returning several entries means
> the *index* cannot choose; it does not mean the *link* is unclear, because the link carries a
> reading the index did not consult.

Two consequences. The detector should apply the reading filter *before* bucketing, so ambiguous
means "still ambiguous after the reading is known" — which would have emptied this bucket to 1.
And the one genuine residual (05020_youtsuu's 持ち上げたとき) is not a link defect at all but a
symptom of the 02918/10077 とき duplication — see [Entry Follow-ups](entry-followups.md). A
bucket that shrinks from 13 to 1 under a filter the detector already implements is a labelling
bug, not a judgment queue.

## 60. `onomatopoeia` is valid in both `pos` and `semantic` — and the corpus uses both

**Source**: 2026-08-01 routine new-entries run, reporting that the accuracy reviewer flags
`onomatopoeia` as missing from `tags.semantic` on a mimetic entry (30301) that carries it in
`tags.pos`, and proposing the reviewer prompt be told that "`onomatopoeia` lives in `pos` and
mimetics take `descriptive` in `semantic`." **Measured by the 2026-08-02 harvest, that convention
does not exist.**

`onomatopoeia` is in **both** `VALID_POS` and `VALID_SEMANTIC`, and the corpus is genuinely split:
**172 entries** carry it in `pos`, **116** carry it in `semantic`, **71** carry it in both. The
reviewer is not misreading a convention; it is reporting the absence of one.

This matters because two filed items now sit on opposite sides of the same undecided question.
[Cleanup P33](cleanup-backlog.md#priority-33-mimetic-entries-whose-notes-announce-they-are-onomatopoeia-but-whose-tags-do-not-77-entries)
is a 77-entry batch that would add `onomatopoeia` to `semantic`; this observation asks for a
reviewer-prompt rule that would stop it being suggested there. **Running either before the
curator decides would make the corpus less consistent, not more.** The decision is one line —
is `onomatopoeia` a part of speech, a semantic field, or legitimately both? — and it unblocks
P33, the reviewer prompt, and the entry-creation skill together. Filed here rather than acted on.

## 61. `check_artifacts.py`'s duplicate-conjugation detector covers verbs but not i-adjectives

**Source**: 2026-08-01 routine polish run (five entries cleaned: 06733, 06734, 06736, 06737, 06738).

The `FORMS:` / conjugation bullet lists at the head of adjective and compound-verb notes
(`・せわしない → せわしなく (adverbially)` …) restate the entry's own generated `conjugation` table
verbatim. The detector already recognises this for verbs; the i-adjective variant produces the
same redundancy from the same cause (`add_adjective_conjugations.py` post-dating the notes) and is
the same one-line fix in the detector's POS filter. Directly extends
[Cleanup P31](cleanup-backlog.md#priority-31-redundant-conjugation-bullets-at-the-head-of-notes),
whose open curator question — is the generated table authoritative? — governs both.

## 62. `find_missing_furigana.py` cannot tell "wrap this" from "rewrite this"

**Source**: 2026-08-01 routine polish run.

The checker flags metalinguistic mentions of a character in otherwise-English prose ("the kanji
今", "Different from 雨 (ame, rain)"). The flag is **correct** under the project rule — but the
fix is not the obvious one. Wrapping gives `the kanji {今|いま}`, which is wrong twice over (the
prose is discussing the glyph, not the word, and the reading it asserts may not be the one meant);
the right fix is almost always to rewrite the prose so the glyph is named by its reading or moved
into an example. A single line in the checker's output — *prose mentions should be rewritten, not
wrapped* — would save the rediscovery, which has now cost two runs.

This is the same rule collision documented as the **unlinkable residue** in
[Inline Link Integrity](../topics/inline-link-integrity.md#the-unlinkable-residue-japanese-that-no-rule-can-currently-handle),
and both should be resolved by the same convention decision.

## 63. `validate_tags.py` collapses 13,037 warnings into one number with no breakdown

**Source**: 2026-08-02 routine accuracy-review run (23608–23907).

The run needed to know how many off-vocabulary semantic tags the dictionary carries. The standard
tool for that question reports **13,037 warnings** as a single count, with no per-category
grouping, so the run had to write a throwaway script against `VALID_SEMANTIC` to recover the
4,899-instance / 818-label off-vocab population. That is the second harvest in a row to write the
same throwaway script.

A `--summary` mode — or simply grouping the warning tail by warning type and printing counts —
would make **the largest known content defect in the dictionary visible in the standard report**
instead of hidden behind a number that is too large to read. It is a few lines over a
`Counter`, and it feeds [Cleanup P20](cleanup-backlog.md#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration)
directly. Related: [item 6](#6-tag-drift-detector),
[item 46](#46-pre-scan-off-vocabulary-tags-deterministically-and-feed-the-list-to-the-accuracy-reviewer)
— the deterministic pre-scan item this would make trivial to run.

## 64. `manage_candidates.py add` does not say *what* it rejected or *why*

**Source**: 2026-08-02 routine new-entries run (a batch of 17 adds).

On a duplicate hit the command prints only `Use --force to bypass this check`. It does not echo
the word, and it does not distinguish "this already exists as an entry" from "this is already in
the candidate list" — two outcomes with opposite meanings for the caller (the first means stop,
the second means the word is already queued). In a batch of adds the operator cannot tell which
of the 17 were skipped without re-running them one at a time.

The fix is one line in the rejection path: echo the word, the reading, and the matched target
(`entry 12345_foo` / `candidate C22661`). Cheap, and it removes a real source of silent data loss
— a run that cannot see which adds were dropped will not retry them.

## 65. `validate.py` accepts an inline link whose base form contradicts its target

**Source**: 2026-08-02 routine polish run, which hand-wrote two links that passed validation and
were wrong: `これ→00959_kiiroi` and `同じ→00591_isogashii`.

`validate.py` checks that a link's target **ID exists**. It does not check that the target's
headword or reading has anything to do with the link's declared base form, so a mistyped or
copy-pasted ID validates cleanly and ships. Both defects above were caught by a human re-reading
the entry, which is exactly the review channel the frontier lane cannot afford.

The comparison is already implemented — [item 59](#59-check_link_baseformpy-should-suppress-proposals-that-change-the-reading)'s
`check_link_baseform.py` does it, and `build/word_id_lookup.json` is already loaded by the build.
What is missing is the **ratchet**: running the agreement test at validation time, on changed
entries only, so a wrong link cannot enter the corpus in the first place. That is a different
posture from the detector, which cleans up arrears
([Cleanup P27](cleanup-backlog.md#priority-27-dead-inline-link-target-ids) is the accumulated
version of the same defect). The same asymmetry the
[headword-furigana ratchet](#56-nothing-checks-that-a-headword-carries-furigana) argued: for an
actively-growing defect the guard matters more than the sweep.

Care is needed on the false-positive side — a legitimate link may point at a variant spelling —
so the validation-time form should require *disagreement in both headword and reading* before
failing, and the exploratory form stays in the detector.

## 66. Detector: an inline link whose surface reading disagrees with its target entry's reading

**Source**: 2026-08-02 routine polish run, which repaired 20 links in the number/date cluster —
`{十|とお}` pointing at `00708_juu` (じゅう) when `28376_too` exists, `{間|かん}` pointing at
`00914_aida` (あいだ) when the duration suffix `28469_kan` is the correct target — and proposed
"flag links whose furigana reading disagrees with the target's `reading`". A second observation
from the same run proposed a sibling rule: **adjacent-ID slips**, where 〜者 (しゃ) was linked to
`04660_sha` 〜社 rather than `04662_sha`, two IDs away.

**Measured 2026-08-03 across all 266,899 inline links (259,578 resolving).** The naive rule is
unusable and the reason is instructive:

| Rule | Hits | Verdict |
|---|---|---|
| surface reading ≠ target reading (all links) | **28,906** | unusable — dominated by inflection (した→する ×1,016, なった→なる ×467, あります→ある ×283) |
| …restricted to targets with only non-conjugating POS | 2,790 | still noisy — particle/copula tails (ために, 静かに, では) |
| …then stripping trailing particle/copula kana | 2,113 | the real residue, in 1,451 entries |
| …**and an entry with exactly the surface reading exists** | **998** | the shippable slice |

The last row is the one worth building. It is not "this link's reading is odd" but "**this link's
reading is another entry's headword reading**" — a claim with a named alternative, which is what
makes it adjudicable. It reproduces the reported family exactly: `{何|なん}`→`00498_nani` while
`03100_nan` exists (107 links), `{会社|がいしゃ}`→`00607_kaisha` while `19013_gaisha` exists (19),
`{通|どお}り`→`01475_toori` while `09884_doori` exists (17), `{国|こく}`→`02204_kuni` while
`20672_koku` exists (13), `では`→`00502_de` while `02945_deha` exists (19).

Two cautions for whoever builds it:

- **Not every hit is a defect.** Rendaku and on-kun alternation inside a compound (`{日|び}`,
  `{口|ぐち}`, `{型|がた}`) are the same morpheme, and pointing at the base entry may be the
  intended convention. The output should be a *review queue*, not a fix list — and grouping by
  `(surface, target)` collapses 998 links into a few dozen decisions, the same ~5× collapse
  [item 59](#59-check_link_baseformpy-should-suppress-proposals-that-change-the-reading) records.
- **The 1,115 hits with no alternate entry are a different question** — `{月|がつ}`, `{分|ぷん}`,
  `{力|りょく}` are compound-only readings with no dedicated entry, so there is nothing to retarget
  them to. They are candidates for suffix/counter entries, not link repairs.

The adjacent-ID variant is cheap to add to the same scan: flag a link whose target is within ±3 of
an entry whose headword matches the link's base form **exactly**. Both rules are read-only,
deterministic, and need no model.

## 67. Per-range off-vocabulary tag density report

**Source**: 2026-08-02 routine accuracy-review run, observing that the CI ratchet cannot see this
class by design.

`validate_tags.py --check-no-new-unknown` compares against `unknown_semantic_baseline.json` and
fails only on tags that are *new* relative to the baseline. That is the correct design for the
inflow gate — but it means a block where **53% of entries carry off-vocabulary tags sits silently
inside the baseline** and is discovered only when an accuracy-review sweep happens to reach it.
Three consecutive high-ID blocks have now come in at 40–53% (23908–24500: 315/592; 24501–25100:
246/600), each found by accident.

What is missing is a **targeting** instrument, not a gate: a report that buckets entries by ID
range (say per 500) and prints the count and share carrying baselined off-vocabulary semantic
tags, so the Routine's `systemic-fix` and `accuracy-review` modes can be pointed at the worst
block instead of the next sequential one. Everything it needs already exists — the `VALID_SEMANTIC`
set, the baseline file, and the entry scan — so this is a reporting flag on `validate_tags.py`
(`--density-by-range`), not a new tool. It pairs with
[item 63](#63-validate_tagspy-collapses-13037-warnings-into-one-number-with-no-breakdown), which
asks the same script for a breakdown by tag; this asks for the breakdown by *location*.

## 68. `check_consistency.py`: `explanation` that is a verbatim copy of `gloss`

**Source**: 2026-08-03 routine accuracy-review run (24542 突出, 24544 可憐).

One-line check — `definitions[i].explanation == definitions[i].gloss`, string-exact — with a
measured live scope of **201 senses in 179 entries**, all inside six contiguous creation blocks
(see [Cleanup P39](cleanup-backlog.md#priority-39-definitionsexplanation-is-a-verbatim-copy-of-its-own-gloss-201-senses-179-entries)).
Normalised comparison adds zero hits, so no fuzzy matching is needed. It belongs in
`check_consistency.py` as a new issue type rather than in a standalone detector: it is an
entry-internal invariant, which is exactly that script's remit, and the fix (drop the duplicate)
is schema-safe because `explanation` is optional.

Worth adding as a `validate.py` warning at the same time — the defect is created at generation
time in batches, so catching it at entry-creation is what stops the seventh block from existing.

## 69. `add_conjugations.py` picks the する branch from the *reading*, not the headword

**Source**: 2026-08-03 routine polish run, which found `09300_disuru` (ディスる) and `09318_misuru`
(ミスる) carrying suru-verb conjugation tables — publishing the non-words ディスるした / ディスるして
on the live site — and traced it to `reading.endswith('する')` at `build/add_conjugations.py:238`.
Both entries were fixed by hand that run.

**Measured 2026-08-04: the family is exactly 4 entries, and 2 of them are not loanwords.** Entries
whose reading ends in する while the headword does not: ディスる (でぃする), ミスる (みする),
**{擦|こす}る (こする)** and **{啜|すす}る (すする)**. The two native verbs currently hold correct
godan tables — they were generated before the branch existed or written by hand — but they sit on
the same trap and any `--force` regeneration would corrupt them.

That is the useful part for the fix: **a "skip katakana loanwords" guard would miss half the
family**. The reliable tests are the two the entry already carries — `metadata.tags.verb_class`
(all four say `godan-ru`) and the headword's own final characters (none ends in する) — so the
branch should read

```python
if headword_plain.endswith('する') and verb_class != 'godan-ru':
```

rather than testing the reading. Zero live defects after the hand fixes; this is a **guard against
regeneration**, not a sweep — the same category as items 65 and 56, where the cheap permanent win
is refusing to create the defect again.

## 70. Suppress `Potential` / `Passive` / `Imperative` rows for lexicalized potential verbs

**Source**: 2026-08-03 routine new-entries run (`30367 待ちきれる` → 待ちきれられる, 待ちきれろ) —
"a potential-derived verb flag on such entries could suppress those rows". Corpus side of
[Cleanup P41](cleanup-backlog.md#priority-41-conjugation-tables-generate-the-potential-of-a-verb-that-is-already-potential).

`add_conjugations.py` derives every row from the verb class, which is correct morphology and wrong
Japanese for verbs that are already potential in meaning: `00557_dekiru` publishes **できられる**
and **できろ**, `01165_mieru` 見えられる, `01229_kikoeru` 聞こえられる. できる is basic tier.

**The mechanical test that works is entry-internal.** Detecting the class from the headword fails
(the `-きれる` shape returns 9 entries but mixes 待ちきれる with ordinary intransitives like 途切れる).
Detecting it from the entry's *own prose* works: 6 entries describe themselves as a potential form
in notes or gloss **and** still carry a Potential row — 取れる, 眠れる, いける, 聞こえる, できる,
待ちきれる, all true positives. That check belongs in `check_consistency.py` (prose contradicting
generated data is its remit), and the generator needs a small curated `NO_POTENTIAL` list seeded
from those 6 plus 見える, since the prose test under-generates.

Suppression is asymmetric in the same way P39's drop is: an omitted row teaches nothing, a wrong
row teaches ungrammatical Japanese to a learner who has no way to know.

## 71. `check_tag_drift.py`: `metadata.tags.pos` and `metadata.tags.verb_class` can disagree

**Source**: 2026-08-03 routine polish run, which scanned for the disagreement after hitting it on
`06762_ishukusuru` and fixed all live cases the same run: `06762`, `08736_otomosuru`,
`02941_kopiisuru` (suru verbs tagged `verb-godan`) and `09300_disuru`, `09318_misuru` (godan verbs
tagged `verb_class: "suru"`). `00392_suru` is the one legitimate mismatch (`verb-irregular`).

Live scope after that run: **0 of 7,226 entries carrying `verb_class`.** The item is therefore a
*ratchet*, not a queue: flag any entry where `verb_class == "suru"` but `pos` lacks `verb-suru`,
or where `pos` contains `verb-godan`/`verb-ichidan` while `verb_class` says `suru`, with
`00392_suru` allow-listed. Two fields that must agree and nothing checking that they do is the
same gap items 61 and 65 describe; the fix is a dozen lines and it protects the conjugation
generator (item 69) which reads both.

## 72. Detector: "naked Japanese" in examples and notes (link-coverage checking, mechanically)

**Source**: 2026-08-04 routine polish run — "written ad hoc twice now in polish runs; belongs in
build/ as a proper check script."

Tier-1 link coverage is currently judged by eye: a run reads an example, notices which Japanese
runs sit outside `⟦…⟧`, and decides which of them should be linked. The mechanical half of that is
a scan — report every maximal run of Japanese characters in `examples[].japanese` and in `notes`
that is **not** inside a `⟦…⟧` wrapper and is not the entry's own headword — and it is the half
that costs a polish run its attention.

Two design notes from the runs that wrote it ad hoc:

- It should report **counts per entry**, not just hits, because the decision it informs is
  "is this entry linked at all?" (0 links = the frontier case, P-Informational) versus "which
  tokens did the pass miss?" (partial coverage, the marginal case).
- It must **not** treat particles and copula mentions inside notes prose as noise. A 2026-08-04
  polish run found that even fully-linked entries leave 「The location is marked with で」,
  「takes を for what is felt」 and 「Type: 他動詞」 unlinked, because the linking pass stops at
  collocation lists and never enters explanatory prose (fixed on 00545 and 02044). Those runs are
  exactly what this detector would surface and a naive stop-word list would hide.

Complements item 49 (the link *suggester*): this one says where to look, that one says what to
write. Cheap, read-only, and it converts the most repetitive part of frontier polish into a queue.

## 73. `review_runner.py --pass screening` records parse failures as flags

**Source**: 2026-08-04 routine accuracy-review run. Screening over 25101–25320 wrote
`"Parse failure"` as the sole concern for **3 of 217 entries** (25207, 25213, 25268) while still
setting `flagged: true`.

Two costs, both small but compounding: the run must open and adjudicate an entry about which
nothing was actually reported, and the flag rate that item 24's precision argument depends on is
inflated by an unrelated failure mode. The screening result should carry `"error": "parse"` with
`flagged: false`, and the summary should count parse failures separately — a rising parse-failure
rate is a *model or prompt* signal, which is worth seeing rather than burying in the flag count.

## 74. `check_consistency.py`: literal `\n` stored in a notes field

**Source**: 2026-08-04 routine polish run — notes rewritten programmatically are easy to corrupt,
because writing `"\\n"` in a Python heredoc stores a literal backslash-n that validates cleanly and
renders as visible garbage on the site.

**Measured 2026-08-04: exactly 1 entry** (`17662_kakuyasushimu`) in 30,187. So this is not a sweep
— it is a two-line guard against a failure mode that only exists because entries are increasingly
edited by scripts rather than by hand. Worth adding for the same reason as item 69: the check costs
nothing to run forever, and the defect is invisible to `validate.py` by construction (a literal
backslash-n is a perfectly valid JSON string). The single live instance is filed on
[Entry Follow-ups](entry-followups.md).

## 75. The accuracy reviewer assigns different severities to the same defect class

**Source**: 2026-08-04 routine accuracy-review run (25601–26200).

Identical "this semantic tag is not in the valid list" findings came back as `severity: "error"`
on some entries and `severity: "warn"` on others *within a single range*. The defect class is
binary and machine-checkable — a tag either is or is not in `VALID_SEMANTIC` — so there is no
entry-level fact the model could be responding to.

This matters more than a cosmetic inconsistency because
[`routine2.md` §A step 4](../../../prompts/routine2.md) **triages by severity**: error-severity
issues are worked individually, warn-severity ones are sampled ~10 per dimension and the rest
bulk-rejected as a family. A tag-vocabulary flag that lands in the `warn` bucket is therefore
liable to be bulk-rejected even though its class runs at the highest apply rate of any dimension
(83.0% this window; see [Quality Metrics](../topics/quality-metrics.md)).

Two fixes, either sufficient: have the prompt fix the severity per issue *type* rather than
letting the model choose, or — better, and consistent with
[item 46](#46-pre-scan-off-vocabulary-tags-deterministically-and-feed-the-list-to-the-accuracy-reviewer)'s finding
that the free `VALID_SEMANTIC` diff already finds 110 of 118 and 38 of 54 of what the reviewer
flags — stop routing tag-vocabulary flags through severity at all and adjudicate them against
the deterministic list. The standing rule for the Routine in the meantime: **severity is not a
triage axis for `dim: tags`**.

## 76. `word_id_lookup.json` answers katakana lookups from `by_headword` only

**Source**: 2026-08-05 routine polish run — a linker looked up ピンク, got nothing, and was about
to write a `noentry` marker for a word that has an entry (`04718_pinku`).

**Measured 2026-08-05**: `by_reading` holds **0** pure-katakana keys — a katakana entry is keyed
there under its hiragana transliteration (ピンク → ぴんく) — while `by_headword` holds **2,159**,
including every katakana headword. So the lookup is not missing; it is **asymmetric**, and a
caller that consults `by_reading` first (the natural choice when working from an example
sentence's furigana) silently gets nothing for the entire loanword vocabulary.

This is the same transliteration trap already recorded for `cross_references` in
[Cross-References](../topics/cross-references.md) (a katakana headword's `reading` must be
hiragana), showing up one layer down. Three options, in increasing order of cost: document it in
the `inline-word-links` skill (a two-line note — the cheap fix, and the one that would have
prevented this instance); have `generate_word_lookup.py` additionally key katakana headwords into
`by_reading` under their own surface; or give callers a single `lookup(word)` helper that tries
both maps. The first is worth doing regardless — a stale `noentry` marker written today becomes
[Cleanup P35](cleanup-backlog.md) tomorrow.

**[skill] recommendation** (this session does not modify skills): add the katakana note to
`inline-word-links`.

## 77. The accuracy reviewer's `formality` flags run at 10% — split them out or suppress them

**Status**: open, measured 2026-08-07
**Effort**: small (a paragraph in the reviewer prompt) — or zero, if §A simply stops reading them

`dim: tags` carries three unrelated sub-families, and the `formality` one is noise. Measured
across the 2026-08-05 → 2026-08-07 ledger window: **3 applied of 30 decided (10.0%)**, against
99.4% for off-vocabulary migrations and 28.1% for in-list substitutions in the same window
(see [Quality Metrics §14](../topics/quality-metrics.md)).

Two runs found the same failure independently and described it the same way. On 26701–27000
the reviewer ran 1 applied of 10; on 27001–27313 it ran **0 of 5** (27098 短期大学, 27170 通俗的,
27194 積乱雲, 27208 手違い, 27232 眠りにつく), and in four of those five **the entry's own notes
state that the word is the formal or literary term** — "the formal name for…", "the formal
meteorological term", "commonly used in… formal apologies", "more refined than 寝る". The
reviewer is judging register from the headword alone while holding a register description that
contradicts it.

This is the same defect shape as `check_tag_drift.py`'s formality check, which routine2.md §A
already resolves correctly at the policy level: *apply a formality flag only when the entry's
own notes/register description contradicts the label*. The reviewer is not being told the
rule its adjudicator uses.

**Fix, in cost order:**
1. One line in the reviewer prompt: before flagging `formality`, read the entry's REGISTER /
   FORMALITY section; if it describes the headword as formal, written, literary or refined, do
   not flag.
2. Emit `formality` findings under their own `dim` so the ledger separates them without
   note-string heuristics — which would also make Quality Metrics §14's split a query rather
   than a reconstruction.
3. If (1) does not move the rate, drop the sub-dimension. At 10% it costs more adjudication
   than it returns.

Related: [75](#75-the-accuracy-reviewer-assigns-different-severities-to-the-same-defect-class) (severity is not a triage axis for `dim: tags`) — the note-family split is the axis that is.

## 78. Detector: inline links that resolve, but to the wrong word

**Status**: open, specified 2026-08-07
**Effort**: small — one pass over the link corpus answers both shapes

`check_link_targets.py` asks "does this ID exist?"; `check_link_baseform.py` asks "is this ID
the base form's own entry?". A link can pass both and still send the reader to a different
word. Three runs hit instances of it in the first week of August. Full analysis:
[Inline Link Integrity → the two wrong-target classes](../topics/inline-link-integrity.md).

**Shape 1 — reading agrees, headword does not.** 00897 店員's note linked 店長 to
`07537_tenchou` = 転調 "modulation (in music)". Rule: for each inline link, compare the base
form to the target entry's headword *and* reading; report where the reading matches and the
headword does not. This is the mirror of item 59's reading test — same two fields, opposite
sign.

**Shape 2 — bound suffix linked to its free-standing homophone.** Both remaining 的 findings
(00445 開放的, 02627 外交的な) linked the adjectival suffix 〜的 to `03546_teki` 敵 "enemy"
instead of `09839_teki` 〜的. Rule: base form is a single kanji that also heads a `〜X` suffix
entry, but the declared target is the free-standing noun of the same reading. The `〜` in the
suffix entry's headword makes the pair machine-separable.

Neither shape needs a judgment queue: everything required to decide is already in the two
entries. Both were fixed by hand this month, which is the argument for the detector — nothing
stops them being written again.

## 79. `backlog-queue.json`'s `scope_estimate` has no unit

**Status**: open, filed 2026-08-07
**Effort**: trivial (one field, plus a pass over 51 items)

`scope_estimate` counts entries for some items, instances for others, and distinct target
strings for a third group. Nothing records which. Twice in one week a run has read one unit and
reported the other as a contradiction:

- `inline-link-braced-base-form` carries **36** (entries); a 2026-08-07 run measured **226**
  (instances) and reported the item as understated. Both numbers are correct.
- `inline-link-stale-noentry` carries **2,887**; the same population has been published as
  7,386 (all markers), 3,809 (occurrences), 2,633 (resolving instances) and 2,351 (distinct
  base forms) in different places.

Add `scope_unit` (`entries` | `instances` | `targets`) and backfill it. The value is not
tidiness — it is that a `systemic-fix` run sizes its batch from this field, and "226 things to
fix" and "36 files to open" are different afternoons.

## 80. `validate.yml` has no `workflow_dispatch:` escape hatch

**Status**: open, filed 2026-08-07 — **preparedness, not repair**
**Effort**: trivial (three lines of YAML)

`validate.yml` triggers on `pull_request` only, so a run whose checks never appear cannot
re-trigger them. During the 2026-08-06 outage (see
[Content Pipeline → the 2026-08-06 CI outage](../project/content-pipeline.md)) two PRs sat with
`total_count: 0` check runs and no way forward.

Adding `workflow_dispatch:` would let a stranded run call `actions_run_trigger` with
`ref: <its own branch>`; the resulting run attaches a check run to that branch's head SHA,
which is the PR's head SHA, so the §7 `get_check_runs` gate would see it.

File it as preparedness rather than as a fix, because the outage self-resolved after 8 h 54 m
and the work was recovered by commit absorption, not by dispatch. The reason to build it anyway
is that absorption only works while a *later* run is still scheduled to absorb into.

## 81. The §0b stranded-PR sweep can discard `systemic-fix` work

**Status**: open, filed 2026-08-06, confirmed 2026-08-07
**Effort**: small (one predicate in the sweep description)

§0b closes an open `claude/*` PR when the maximum entry ID among the entry files it touches is
below `polishing/tasks/comprehensive/progress.txt`'s `next:`. That heuristic assumes a PR's
entry IDs track the polish frontier. True for `polish` PRs; **false for `systemic-fix` PRs,
which touch low IDs by nature** — the 2026-08-06 batch spanned 00445–06031, entirely below the
6809 frontier.

Two runs in a row (#3130, #3131) had to leave manual "do not sweep me" comments, and they were
stranded by a CI outage, i.e. the sweep was most dangerous exactly when the failure it was
cleaning up after was not the failure it assumes.

**Options, in preference order:**
1. Exempt PRs whose title starts with `routine(systemic-fix)` from the max-ID test.
2. Require positive evidence of supersession — main already contains an equivalent change —
   rather than inferring it from ID ordering.
3. Gate on age (older than one run interval) rather than on entry IDs alone. Weakest: it would
   not have protected #3130 either.

## 82. `build/propose_inline_links.py` — the mechanical half of inline linking

**Status**: open, prototyped and discarded 2026-08-06
**Effort**: medium

Inline linking is the dominant cost of the polish frontier (see item 72 and
[Cleanup P43](cleanup-backlog.md)). A 2026-08-06 polish run wrote a throwaway proposer —
tokenize `{kanji|furigana}` markup, greedy longest-match against `build/word_id_lookup.json`,
emit `id` + gloss candidates for human adjudication — and reported that it "cut the per-entry
cost of full link coverage on 15-example entries by a large factor". Then it threw it away.

The split is the point: **matching is mechanical, and only conjugated-form base lookup and
homograph choice need judgment.** A proposer that emits candidates and refuses to write them
keeps the judgment where it belongs while removing the typing.

Known gaps in the prototype, to fix in the real one:
- No inflection handling — `{描|えが}かれた` splits wrong.
- Should skip ASCII runs in notes.
- Should consult `by_headword` as well as `by_reading` (item 76): the katakana vocabulary is
  invisible to a `by_reading`-first lookup, which is how spurious `noentry` markers get written.

## 83. `check_link_baseform.py`: accept na-adjective normalization

**Status**: open, filed 2026-08-06
**Effort**: trivial (strip a trailing な before the headword-identity test)

Base `巨大な` → entry `巨大` is the same accepted relationship as base `参加する` → entry `参加`,
which the script already normalizes. Without the な rule it reports a whole false-positive class
as disagreements. Cheap, and it shrinks the residue the judgment tail has to read.

## Updates 2026-08-07 to existing items

**Item 24 (retire or gate the furigana screener) — the cost case closes.** A fourth
consecutive run stopped the screening pass early and skipped the deep pass under §A step 2:
on 27001–27313 the screener covered **~14 entries in the time `review_accuracy.py` covered
~150**, roughly 10× slower per entry, which is not what a "cheap bulk" pass is for. Its single
flag was a textbook okurigana-split false positive **that the model itself annotated
"technically not an error"**. The ledger window puts it at 1 applied of 24 (**4.2%**), a
second consecutive window at exactly one true positive. The precision argument has been settled
in the screener's favour for a month — it is not broken, it is low-yield — so the whole case
now rests on cost, and the cost is measured twice: ~8 entries/min vs ~50, and a paying pass
that falls short in the same run because the screener consumed the wall clock. Item 12's
observation that `RATE_LIMIT_INTERVAL = 6.0` caps it near 7 entries/min is the mechanism.
**Recommendation unchanged and now four-times-evidenced**: gate it to entries never previously
screened, or retire it in favour of the free non-hiragana lint.

**Item 46 (pre-scan the free detectors before paying the reviewer) — the reviewer turns out to
be the migration-map generator the 2026-08-06 measurement said could not exist.** That
measurement concluded that a frequency-ranked `TAG_MIGRATION` map decapitates the P20 queue but
cannot finish it (55 more head mappings reach 40.6%; 249 names needed for 82%). The 2026-08-07
accuracy-review adds the complement: on 27001–27313, off-vocabulary tags were **the entire
applicable yield — 34 of 39 applied tag fixes** — and *the reviewer itself supplied an
unambiguous in-list destination for every one* (`places`/`place`→5, `medical`→3, `people`→3,
`location`→3, `conflict`→3, `fashion`→2, `body`→3, plus singletons). The two results are
compatible and jointly decisive: a static map cannot cover the 687-name tail because it must
choose a destination per *name*, whereas the reviewer chooses one per *entry* and therefore
never has to generalise. **Extending `TAG_MIGRATION` beyond the mechanical 78 names is the
wrong lever**; the accuracy-review lane already resolves the tail at 99.4% precision and $0.5
per 1,000 entries. The pre-scan item survives unchanged — detect exhaustively for free, then
let the paid reviewer supply destinations.

**Item 73 (screening records parse failures as flags) — now quantified.** ~4% of screened
entries return a bare `"Parse failure"` concern (5 of 124 in 26701–26866, 2026-08-06). These
are unparsed model responses, not entry defects, and they land in `reviews/screening/*.json` as
`flagged: true`, inflating the apparent flag rate — which matters because the screener's flag
rate is the number item 24's retirement argument is measured against. Log the raw response and
retry once before recording a flag.

**Item 6 / Cleanup P13 (sole-`general` tags) — the lane is settled even though the instrument
was refuted.** The 2026-08-06 measurement closed the gloss-keyword suggester as structurally
mis-aimed. The 2026-08-07 evidence says the work is being done anyway by a different route:
**44 sole-`general` entries were corrected to specific in-list tags in a single accuracy-review
block** (26701–27000), most of them suru-verbs and technical compound nouns from one creation
batch. The reviewer's `tags` dimension detects this class reliably because it judges the
*headword*, not the gloss's surrounding prose — precisely the property the refuted suggester
lacked. **P13 needs no sweep and no detector; it needs the accuracy-review lane to keep
running.**

## 84. `review_runner.py`'s 6-second serial rate limit is what bounds an accuracy-review run

**Source**: 2026-08-07 accuracy-review run, measured directly.
**Status**: open, cheap, high-leverage.

Two review scripts ran concurrently over the same block against the same model. Throughput:

| Script | Rate | Coverage |
|---|---|---|
| `review_runner.py --pass screening` | **~6.6 entries/min** | 332 entries in 50 min, killed by its own `timeout` |
| `review_accuracy.py` | **~19 entries/min** | 534 entries in 28 min |

The difference is not the model and not the prompt — it is `RATE_LIMIT_INTERVAL = 6.0`, a
serial inter-request sleep that `review_accuracy.py` does not have. The two ran **concurrently
with no rate-limit errors** for **$0.31 combined**, which is the evidence that the interval is
not buying anything: if 19/min plus 6.6/min against the same endpoint provokes no throttling,
6 s of enforced idle per request is pure wall clock.

The consequence is not academic. §A sizes a run at 400–600 entries in both dimensions; at
6.6/min the screening pass cannot finish that range in a session, so recent accuracy-review
runs have covered the full range on the accuracy side and **~62% of it on the furigana side**
— a coverage gap created entirely by a constant. Lowering the interval (or threading the pass
the way the cost figures suggest is safe) would let one run cover its whole range in both
dimensions. Note this interacts with [Tooling 24](#24-non-hiragana-reading-lint-cheap-replacement-for-the-furigana-screeners-true-positive-class):
if the screener is retired on cost, this item becomes moot — but it is *far* cheaper to test,
and it changes the cost side of that very argument.

## 85. The 20% "reviewer noise" heuristic misreads a tag-contaminated block

**Source**: 2026-08-07 accuracy-review run (27314–27850).
**Status**: open — a prompt change to `routine2.md` §A step 4, not a script.

§A step 4 says that if more than ~20% of entries come back flagged, that is reviewer noise
rather than dictionary error. On this block **221 of 534 entries (41%)** were flagged, which
the rule would classify as noise. It was not: **234 of the 257 issues were tag flags**, and
**156 of those correctly reported a tag genuinely absent from `VALID_SEMANTIC`** — which §A's
own semantic-tag policy makes *correct by definition*.

The proposed carve-out is one line: **compute the flag rate per dimension after removing
off-vocabulary tag flags.** On this block that yields gloss 18/534 (**3.4%**) and translation
5/534 (**0.9%**) — precisely inside the 4–13% error-severity band the prompt already predicts
elsewhere. The heuristic then works as intended instead of firing on the one dimension whose
high yield is structural.

This converges independently on [Quality Metrics §14](../topics/quality-metrics.md), which
retired the blended `tags` precision figure for the same underlying reason: **off-vocabulary
tag flags are a different instrument from the rest of the reviewer's output, and any statistic
that pools them moves with cohort composition rather than with reviewer behaviour.** Two
different runs reached that conclusion from different directions in the same week, which is
about as strong as evidence gets here. The triage axis both imply — "does this flag name a tag
outside the closed list?" — is answerable by a two-line check before any flag is read.

## 86. Cheap validator check: Hangul outside a documented loanword etymology

**Source**: 2026-08-07 accuracy-review run (27316 `{通常|つうじょう}` carried `(often used for
"평상시" …)` — 平常時 rendered in Hangul inside an English note).
**Status**: open, trivially cheap, scope 1 — file as a validator line, not a sweep.

A whole-corpus scan found **only 4 entries containing Hangul**, and the other three are
legitimate Korean-loanword etymologies (10838 キムチ, 12729 明太子, 16310 ナムル). So this is a
one-off, not a family — but it is the right *shape* for a permanent one-line check in
`check_consistency.py`, because the rule is exact (Hangul outside a documented loanword
etymology is always a defect), the false-positive set is enumerable at 3, and the cost of
carrying the check forever is one regex. Worth having precisely because the next instance will
not be found by anyone looking for it.

## Updates 2026-08-08 to existing items

**Item 8 (furigana format validator) — both June enhancements measured; one ships, one is
retired.** The 2026-06-17 update proposed two additional rules, neither ever sized. Measured
over the whole corpus on 2026-08-08:

- **(b) unbalanced braces: 34 instances / 33 entries.** Real, deterministic, and *visible on
  the live site* (`08385` renders "ぎ}" in English prose). **Ship it** — now filed as
  [Cleanup P45](cleanup-backlog.md#priority-45-unbalanced-furigana-braces-34-instances--33-entries--visible-on-the-live-site).
- **(a) pipe-less `{…}` spans: 931 instances / 623 entries, ~100% false.** The rule collides
  head-on with an undocumented convention — braces are also used as **mention-quotes** around
  a word, reading, or character under discussion (`Usually read as {だて}`). **Retire it.**

The bundling is the lesson worth keeping: these two rules were proposed together, in one
sentence, from one entry (`06147_jiboujiki`) that genuinely contained both shapes. They have
sat unbuilt for seven weeks because the pair looked like one medium-sized job. Sized
separately they are a 33-file afternoon and a rule that should never be written. **When an
item bundles two detection rules, size them separately before scheduling either** — the
bundle's cost is the sum, but its value is not.

**Item 19 (stale-`noentry` detector) — add affix-tilde forms to the lookup, and the
normalization to `check_link_baseform.py` first.** Two 2026-08-07 polish runs independently
hit the same shape: a marker whose base form is bare (`全`, `感`, `代`) while the entry that now
exists carries a tilde (`全〜`, `〜感`, `〜代`). Measured at **159 instances / 47 distinct
bases**, essentially all of them the 28xxx affix cohort. The detector change is two extra
lookup attempts per marker; the *sequencing* matters more than the change, because the links
it produces are exactly what [item 83](#83-check_link_baseformpy-accept-na-adjective-normalization)
exists to stop flagging. See [Cleanup P35 update 2026-08-08](cleanup-backlog.md#updates-2026-08-08-wiki-harvest).

**Item 19, second update — the four-times-filed detector is now filed a fifth and sixth time.**
Both 2026-08-07 polish runs proposed `build/check_stale_noentry.py` from scratch, each citing
its own incidental catches (01332 キャラクター → 23518, 01447 全 → 28337, 01745 リビングルーム →
28876; and 01763's four アジア compounds, 01769's 中央アメリカ + 米, 02211's 冷や/洋酒, 02240's
羊肉/馬肉). Neither run knew the item existed. The dictionary-side scope has been measured five
times and the detector still does not exist; this is now the longest-running gap between a
sized item and its instrument on this page, and it is the direct upstream dependency of
[Cleanup P43](cleanup-backlog.md#priority-43-the-0680007100-block-is-96-unlinked--a-bounded-batch-not-a-frontier-problem)'s
sequencing constraint.

**Item 76 (`word_id_lookup.json` answers katakana from `by_headword` only) — reinforced by the
tilde measurement.** The 159-instance affix finding was produced by trying `X〜`/`〜X` against
`by_headword`; `by_reading` would not have helped, for the same structural reason item 76
records. Both findings say the lookup's key space is narrower than its callers assume, and
both were discovered by a caller working around it rather than by reading it.

## 87. `review_accuracy.py` should run its own subranges in parallel

**Source**: 2026-08-08 accuracy-review run, measured in-run.
**Status**: open, well-evidenced, and the highest-leverage throughput item currently filed.

The script runs at **~2.4 entries/min single-process**. The same run launched **four parallel
processes over disjoint subranges and measured ~30 entries/min with no rate-limit errors** —
better than 4× because the serial path is latency-bound, not quota-bound. At the single-process
rate a 550-entry range costs ~4 hours of wall clock, which is what forces runs to stop mid-range
to protect the wrap-up budget; at 30/min it is under 20 minutes.

Build it into the script (`--workers N`, splitting the range into N contiguous chunks, each
writing its own `reviews/accuracy/{id}.json`) rather than leaving each run to hand-roll it. The
per-entry output files are independent, so there is no merge step and no shared state beyond the
cost tally — which should be summed across workers before the ledger write.

This is the same bound [item 84](#84-review_runnerpys-6-second-serial-rate-limit-is-what-bounds-an-accuracy-review-run)
identified from the other side: 84 says the *furigana* pass is rate-limited by a hard-coded
6-second interval, this says the *accuracy* pass is latency-limited by seriality. Together they
explain why recent runs cover their whole range on the accuracy side and a fraction of it on the
furigana side.

## 88. `get_next_id.py` should print the target directory alongside the ID

**Source**: 2026-08-08 new-entries run.
**Status**: open, trivial, and it has already cost a session once.

Entries 30495–30499 were written into `entries/30500/` before `validate.py` caught the mismatch.
The ID/directory rule is "round *down* to the nearest 500", so an ID like 30495 belongs in
`entries/30000/`, but the visual similarity of `304xx`/`305xx` to the directory name `30500`
makes the wrong choice look right — and the trap is worst **exactly at a 500 boundary**, which is
where new-entry batches inevitably sit as they extend the corpus.

`get_entry_path.py` already computes this correctly. The fix is to have `get_next_id.py` print
the directory it implies (`30495 → entries/30000/`) and, better, to warn when a batch of the
requested size would cross a boundary. One line of output removes a class of error that
currently depends on `validate.py` catching it after the files are written.

## Updates 2026-08-08 (run 2) to existing items

**Item 84 (`review_runner.py`'s 6-second rate limit) — a second, larger bound found:
cross-pass concurrency starves the screener.** A 2026-08-08 run executed
`review_runner.py --pass screening` and `review_accuracy.py` concurrently against the same
OpenRouter model and measured screening at **67 entries in ~45 minutes (~1.2/min) versus ~19/min
for the accuracy pass in the same window**. Screening recovered its normal rate as soon as it
was the only job. So item 84's `RATE_LIMIT_INTERVAL = 6.0` is the *floor*; running a second pass
on the same model is a larger and undocumented one. **Operational rule for §A until this is
fixed: run the two passes sequentially, or point screening at a different model.** Note this
interacts directly with new item 87 — parallelising the accuracy pass will make the starvation
worse, so 87 should land with a shared throttle or distinct models, not on its own.

**Item 47 (fields outside `examples`/`notes` fall through every furigana instrument) — third
confirmed member, and this one arrived with 40 instances attached.**
`check_stale_noentry.py`'s class R compares an inline link's *surface* furigana against the
target entry's reading, and in doing so found 40 pairs of genuine furigana errors
(来春/らいはる, 農作物/のうさくもつ, 墓石/はかいし, 完全試合/かんぜんしあい, 白和え/しろあえ,
部屋干し/へやほし, 言い及ぶ as `{言|い}{及|およ}ぶ`). It found them **by accident** — it was built
to detect stale `noentry` markers. Every one sits inside a `⟦…⟧` surface, which
`find_missing_furigana.py` and the OpenRouter screener both read past. Filed as
[Cleanup P49](cleanup-backlog.md#priority-49-wrong-furigana-inside-inline-link-surfaces-40-pairs--a-blind-spot-in-every-furigana-instrument);
the durable fix is to fold link surfaces into the furigana instruments' input, not to hand-fix
40 pairs and wait for the fourth member.

**Items 5/6 (tag-drift detection) — the `domain` field needs the same treatment and cannot get
it the same way.** The 2026-08-08 measurement of `domain` (3,593 instances / 3,278 entries,
`business` alone 1,162) is described in
[Cleanup Backlog → Updates 2026-08-08 run 2](cleanup-backlog.md#updates-2026-08-08-wiki-harvest-run-2).
The tooling point: every instrument that made the `semantic` cleanup tractable keys on
**off-vocabulary values**, and `domain` has no off-vocabulary values — all 3,593 are in
`VALID_DOMAIN`. The only instrument in the project that could see the defect is the reviewer's
`tags` dimension, which already judges a semantic tag against the *headword* rather than the
example topics; extending its prompt to judge `domain` the same way is the cheap experiment, and
should be tried on a 100-entry sample before anything is sized.

## 89. `reviews/decisions.jsonl` needs an explicit `fam` key on `tags` lines

**Source**: 2026-08-09 wiki-harvest observation, filed by the run that wrote the thirty-third
metrics refresh.
**Status**: open, one field, and it removes the weakest link in the project's headline metric.

The `tags` dimension's apply rate is no longer a single number — the last two metrics refreshes
(§14, §15 of [Quality Metrics Trend](../topics/quality-metrics.md)) headline it as a *mixture*:
off-vocabulary migrations at ~97%, in-list substitutions at ~5%, formality/register at ~18%.
That decomposition is the most useful thing the ledger produces, because it is what justifies
keeping one sub-family and retiring another.

But `decisions.jsonl` has no family key. Each refresh **re-derives the split by keyword-matching
the free-text `note` field**, which is a ≤10-word telegraphic string written by a different run
each time. The classifier is therefore the least stable component of the most-cited statistic:
the in-list figure moved 28.1% → 5.0% between consecutive refreshes, and the two are not
strictly comparable because the note vocabulary drifted, not necessarily the underlying rate.

**Fix**: add an optional `"fam"` key on `tags`-dimension lines, under the same fixed-lowercase
discipline §C already imposes on `src`/`dim`/`decision`:

| `fam` | Meaning |
|---|---|
| `offvocab` | tag absent from `VALID_SEMANTIC`; migrate to the named destination |
| `inlist` | substitution between two in-list tags ("too narrow"/"too broad") |
| `formality` | formality/politeness/register label |
| `category` | flatly wrong parent category (財布 → `clothing`) |

Cost: one key in §C of `prompts/routine2.md` and one line in the metrics script. Benefit: the
decomposition becomes a `collections.Counter` over a controlled field instead of a regex over
prose, and the series becomes comparable across refreshes for the first time. Backfill is not
required — an absent `fam` can keep using today's classifier, so the series improves forward
from whenever this ships.

## 90. `review_accuracy.py --dimensions links` — a link-only run currently verifies nothing it did

**Source**: 2026-08-09 systemic-fix run (the 180-pair stale-`noentry` sweep).
**Status**: open; the gap is structural, not a bug.

§4 of the Routine sends *the entries the run changed* to an independent model, which is the
right unit for a content run. On a **link-only** run it silently stops being a self-check: the
reviewer reads glosses, example translations, and tags — none of which the run touched — so
every flag it returns is about **pre-existing content**, and the change actually under test
(which base form a `⟦…⟧` link points at) is never examined.

The observing run measured both halves of this. The pass was *useful*: six real tag and
translation errors surfaced in entries the run happened to open. It was also *not verification*:
180 link edits went to merge with zero independent review, on a run whose whole content was
those 180 edits.

Two candidate instruments, cheapest first:

1. **`check_link_targets.py` + a context sample.** Resolution correctness is mostly mechanical —
   does the target ID exist, does its reading match the surface, is the base form the entry's
   headword. That is a deterministic check the project can already almost do, and it needs no
   model calls. It cannot judge *sense* selection (the homograph trap documented in
   `topics/homographs.md`), so pair it with a sampled model read of N links in context.
2. **A `--dimensions links` mode** on `review_accuracy.py` that shows the model the example
   sentence and each link's target gloss, and asks only "is this the word being used here."
   Costs a model call per entry but catches the sense errors the deterministic check cannot.

Either way the principle generalises past links: **§4's unit should be the change, not the
entry.** Any future run whose edits live outside gloss/translation/tag space will hit the same
silent gap.

## 91. The GitHub MCP check-run status is cached, and it strands green PRs

**Source**: 2026-08-09 accuracy-review run, observed on PR #3152.
**Status**: open; affects `prompts/routine2.md` §7 step 5.2 and `CLAUDE.md`'s MCP path.
**Severity**: this is a direct, measured cause of the stranded-PR class the §0a rescue exists
to clean up.

Measured behaviour on PR #3152: the `validate` check ran for **67 seconds**
(`started_at` 06:45:18 → `completed_at` 06:46:25, conclusion `success`). For roughly **30
minutes afterwards**, `pull_request_read method=get_check_runs` continued to report
`status: "in_progress"`. `actions_get method=get_workflow_run` agreed, with its `updated_at`
frozen at the run's start time.

A Routine polling to the documented ~8-minute cap therefore sees "pending" for the entire
window, gives up, and leaves a **green** PR open — costing a full extra run for the next §0a
rescue to merge something that was mergeable minutes after the push. The current polling loop
cannot distinguish this from a genuinely slow check, because both look like `in_progress`.

**Proposed mitigations for the §7 polling loop**, in order of cheapness:

1. **Treat a frozen `updated_at` as "no fresh data," not "still running."** If `updated_at` has
   not moved across several consecutive polls while wall-clock time has, the response is a
   cached one; the loop is measuring the cache, not the check.
2. **Re-poll once after a long gap before declaring timeout.** A single extra poll ~2 minutes
   after the cap costs one call and converts a large fraction of these into same-run merges.
3. **Cross-check with a second endpoint on the last poll only.** `get_commit`'s check-run
   summary and `actions_list` are populated by different paths and may not share the stale
   cache; worth one probe before giving up, not on every iteration.

The §0a rescue remains the correct backstop and should not be removed — but it is a backstop
that costs an entire run, so the polling loop should stop feeding it avoidable cases.

### Attempted reproduction, same day — and the reproduction was the defect (2026-08-09, PR #3156)

The run that filed this item tried to reproduce it on its own PR and **failed to, in an
instructive way.** Believing it was watching a green check report `in_progress` for ~19
minutes, it drafted a confident falsification of mitigation 3. Then it checked the wall clock.

Ground truth on PR #3156: `validate` ran **15:32:04 → 15:33:12, `success`**. The run's eight
polls all fell between **15:32 and 15:35** — every one of them *accurate*, including an
`actions_get method=get_workflow_job` call at ~15:33:05 that correctly showed step 7
`in_progress` and a later one that correctly showed it complete. **There was no staleness. The
run had simply not waited.**

**The actual defect is in the polling loop, and it is ours.** `CLAUDE.md` §"MCP path" and
`prompts/routine2.md` §7.5.2 both instruct: *"run `sleep 30` via the Bash tool with
`run_in_background: true`, and when it returns, go back to 5.1."* But a backgrounded Bash
command **returns its tool result immediately** — the sleep continues in another process and
notifies later. A run that issues the sleep and then makes its next poll in the same turn has
waited **zero seconds**. The documented procedure produces a busy-loop that reads as a paced one.

The consequence is exactly the strand class this item was opened about, reached by a different
road:

- The loop's "poll at most ~16 times (~8 min)" cap is denominated in polls, and the polls are
  free. **~16 polls elapse in well under a minute.**
- CI here needs 60–90 seconds of *runtime* and frequently several minutes to *start*.
- So a run can exhaust its entire polling budget before the check has plausibly finished,
  declare a timeout, and leave a PR that goes green moments later — costing a whole extra run
  for the §0a rescue. **No API staleness is required to produce the symptom.**

**This is now the leading candidate explanation for PR #3152 as well**, since that run followed
the same documented procedure. That does not disprove the original observation — its author
reported concrete `started_at`/`completed_at` values and a frozen `updated_at`, and this run
cannot re-examine that PR's timeline — but a local, verified, mechanically-sufficient cause
should be ruled out before an unfalsifiable remote-cache one is accepted. **Downgrade this item
from "the MCP cache is stale" to "the polling loop does not wait," pending a measurement taken
against a checked wall clock.**

**Fix (cheap, and it belongs in the prompt rather than in a tool):**

1. **Verify elapsed time, don't assume it.** Have the loop call `date -u` in the same Bash
   invocation as the wait, and treat the printed timestamps as the record of pacing. One extra
   token per poll makes the failure self-evident.
2. **Cap on wall-clock, not on poll count.** "Stop after 8 minutes" survives a broken sleep;
   "stop after 16 polls" does not.
3. **Prefer a blocking wait.** If a foreground `sleep` is unavailable, a single backgrounded
   wait whose *completion notification* gates the next poll is the correct shape — the
   notification is the signal, not the tool result.

**Method note worth keeping**: this run wrote and pushed a detailed, confident, entirely wrong
falsification before checking `date`. It is a clean instance of the
[Instrument Defects](../topics/instrument-defects.md) thesis applied to a Routine's own
telemetry rather than to the corpus — **when a measurement implies a remote system is
misbehaving, check the local clock before writing it down**, because the observer's timebase is
the cheapest thing in the chain to verify and the easiest to get wrong.

## Updates 2026-08-09 to existing items

**Item 27 (`validate_tags.py` unknown-semantic warnings) — the reporting gap is why the class
stayed invisible for months.** The 2026-08-09 accuracy-review notes that off-vocabulary semantic
tags are printed **only under `--verbose`**, where 11,013 warnings collapse to a bare count in
normal runs. So the single largest tag-quality backlog on this page
([P11](cleanup-backlog.md), 1,848 entries / 2,436 uses) is, in the tool that already detects it
perfectly, rendered as one integer. A `--list-unknown` summary mode — tag → count → entry IDs,
sorted by frequency — turns it into a work queue at the cost of a `Counter` and a print loop,
and it is the natural companion to the ratchet this item already shipped
(`--check-no-new-unknown`). **The 2026-08-09 measurement makes the case sharper**: the
vocabulary is 643 distinct labels with 300 of them used exactly once, which is precisely the
distribution a human cannot see without the tool printing it.

**Items 5/6 (tag-drift detection) — `TAG_MIGRATION` is measured, and it is a head-only
instrument.** `check_tag_drift.py`'s 9 migration rules cover **181 of 2,436 off-vocabulary uses
(7%)**. The ten families proposed by the 2026-08-09 accuracy-review would cover **202 (8%)**.
Reaching 75% requires ~200 hand-written rules, because 486 of the 643 labels are used ≤3 times.
The full curve is in
[Cleanup Backlog → Updates 2026-08-09](cleanup-backlog.md#updates-2026-08-09-wiki-harvest).
**Prescription**: extend the map with the top ~25 labels (7% → 29%, nearly free), and stop
treating map maintenance as the path to the tail — the reviewer's off-vocabulary flag already
runs at ~97% apply rate on this exact class and names a destination per instance without anyone
enumerating the vocabulary first.

**Item 17 (suppress in-list narrowness suggestions) — twelfth-plus confirmation, 0 of 12.** The
2026-08-09 accuracy-review measured error-severity tag flags at ~70% applicable overall, but
"almost all of the applicable ones were the mechanical *tag not in the valid list* family," and
**every in-list substitution flag was rejected — 12 for 12**. The observing run reached this
item's standing prescription independently ("the reviewer prompt could stop emitting in-list
substitution suggestions entirely and lose nothing"). The evidence for this fix is now the
strongest on the page and it remains unshipped; see also new item 89, which would make the
sub-family rates countable without a keyword classifier.

**Item 84 (review-pass throughput) — an operational hazard, not just a rate.** A backgrounded
`review_runner.py` pass **survived `pkill -f`** at a 2026-08-09 run's §6 context checkpoint and
kept writing result files *after* the run's `git add -A`, stranding **25 artifacts outside the
PR** (recovered in a follow-up commit). Only `kill -9 <pid>` stopped it. Two consequences worth
recording with this item: (a) any Routine that stops a review pass early must **confirm
termination by PID** before staging, not assume a pattern kill worked; (b) the review scripts
write incrementally with no completion marker, so "process gone" and "output complete" are
independent facts. A `--pidfile` option, or writing results to a staging directory promoted on
clean exit, would remove the hazard rather than documenting around it.

## 92. The §7 CI-wait loop does not wait, and that alone can strand a green PR

**Source**: 2026-08-10 routine polish observation, verified against PR #3156's timestamps.

`CLAUDE.md` → "MCP path" step 5 and `prompts/routine2.md` §7.5.2 both instruct the run to wait
between check-run polls by issuing `sleep 30` through the Bash tool with
`run_in_background: true`, "and when it returns, go back to 5.1". **A backgrounded Bash call
returns its tool result immediately** — that is what backgrounding means. A run that follows the
instruction literally, polling again as soon as the tool result comes back, waits **zero
seconds** between polls.

The documented safety margin evaporates with it: the "~16 polls (~8 min)" cap becomes ~16 polls
in well under a minute, against CI that needs 60–90 s to *run* and frequently minutes to be
scheduled at all. The run then reports "still pending at the cap", leaves the PR open, and stops
— which is precisely the stranded-PR failure mode §0a exists to clean up after.

**Verified, not inferred.** On PR #3156 the `validate` check ran 15:32:04 → 15:33:12 while all
eight of the run's polls landed between 15:32 and 15:35. Every individual reading the API
returned was accurate; the loop simply consumed its whole budget inside the check's own runtime.

**Fixes, cheapest first:**
1. **Print `date -u` inside the wait call itself** — one token of output that makes a
   zero-second wait immediately visible in the transcript instead of invisible.
2. **Cap on wall-clock, not on poll count** — record the start time and keep polling until 8–10
   real minutes have elapsed, so a fast-returning wait costs an extra poll rather than the
   entire budget.
3. **Wait in the foreground with something that is not `sleep`** — the harness blocks foreground
   `sleep`, but a foreground `python3 -c "import time; time.sleep(45)"` blocks the turn for a
   real 45 seconds, which is the semantics the procedure assumed all along.
4. Or gate the next poll on the backgrounded command's **completion notification** rather than
   its tool result.

**This supersedes most of [item 91](#91-the-github-mcp-check-run-status-is-cached-and-it-strands-green-prs).**
PR #3152's "check-run status is ~30 minutes stale" report came from a run following the same
zero-wait procedure, so the simplest reading is that the run polled for well under a minute and
attributed its own haste to a stale cache. Item 91 is downgraded to unconfirmed pending a
sighting with timestamps that rule out this explanation.

## 93. `review_accuracy.py` should read `reviews/decisions.jsonl` before it flags

**Source**: two 2026-08-09/10 accuracy-review observations — one measuring **26 of 26** flagged
entries in 29295–29743 as already carrying a same-dimension decision (24 of them prior
REJECTs, net applicable flags this run: **zero**), the other documenting two reviewer
oscillations.

**Measured 2026-08-10 across all 28,284 accuracy reports:** 10,139 reports carry open issues,
covering **10,613 distinct (entry, dimension) pairs**. Of those, **4,479 (42.2%) already have a
decision recorded on that same dimension**, and **1,081 (10.2%) already have a REJECT**. The
filed run's 100%/92% figures were a heavily-reviewed band; corpus-wide the re-litigation rate is
42%, which is smaller but still means two of every five flags reaching adjudication concern a
question the project has answered in writing.

**The oscillations are the sharp end, and there are two in one 449-entry range.** 29451 塁打:
a 2026-06-24 run APPLIED a gloss change reasoning "ruida is total bases, not generic base hit";
the 2026-08-09 run flagged **that result** as an error and asked to revert to the original
wording. 29634 ネガティブ: a 2026-07-02 run APPLIED "removed technology; core sense is attitude",
and the 2026-08-09 reviewer asks to **add `technology` back** for the photographic-negative
sense. Without the ledger in front of the adjudicator, both would have been applied — undoing
deliberate corrections that a later sweep would presumably flip again. The ledger currently
prevents this only when a human happens to check it.

**Two implementations, and they are not alternatives:**
- **(a) Suppress**: drop an issue whose `(entry, dimension)` already has a REJECT unless the
  entry's `modified` is newer than that decision. Cheap, purely local, removes ~1,081 pairs
  (10%) of adjudication volume, and would have turned the filed run into a no-op detectable in
  seconds.
- **(b) Inform**: pass prior decision notes for the entry into the reviewer prompt so the model
  is told what was considered and why. Covers the full 42%, catches the oscillation class that
  (a) misses (both oscillations were prior **APPLYs**, not REJECTs), and costs a few tokens per
  entry.

(a) is a filter over output; (b) changes what the model is asked. Ship (a) this week and (b)
when the prompt is next revised.

## 94. Review recency, not "changed at some point": filter `reviews/queue.txt` and the sweep cursor

**Source**: two 2026-08-10 accuracy-review observations — one that the cursor pointed at
29744–30539, a band of 796 entries where every entry already had a current report from the §4
at-birth self-check; one that `queue.txt` "does not converge because it is not deduped against
review recency."

**Measured 2026-08-10.** Queue depth **9,932**. Of those, 9,700 have an accuracy report and 232
have none. Comparing each report's `reviewed_at` against its entry's `metadata.modified`:

| Queue population | Entries |
|---|---|
| Report is **newer** than the entry's last modification (already current) | **3,513** |
| Report is older than the entry's last modification (genuinely stale) | 6,187 |
| No report at all | 232 |

**35% of the queue is entries that have already been reviewed since they last changed.** The
filed estimate was 776; the real figure is 4.5× that. CI appends on any change and nothing ever
removes an entry when a review lands, so the queue measures "changed at some point since the
queue was created" — which is why its depth is a slow-moving number that no amount of reviewing
visibly dents.

**Fix**: one predicate, `reviewed_at >= modified`, applied in two places — as a filter when CI
writes the queue (dropping it straight to ~6,400) and as a skip in the sweep cursor, which would
also let the cursor jump directly to the **2,062 entries never reviewed at all** instead of
crawling bands the §4 at-birth checks have already covered. The same predicate makes queue depth
a real health metric rather than a monotone counter.

## 95. Constrain the reviewer's tag suggestions to `VALID_SEMANTIC`, and tell it `general` is a legal fallback

**Source**: two 2026-08-09/10 accuracy-review observations, and now three consecutive metrics
windows.

Two families make up roughly half of all tag-flag volume, and **both are mechanically
suppressible before they reach a human**:

- **Off-vocabulary suggestions.** The prompt embeds `VALID_SEMANTIC` and the model proposes
  outside it anyway — 6 of 21 tag flags in one run (`mathematics` ×2, `astronomy` ×2,
  `literature`, `manufacturing`). The suggestion field should be an **enum**, or off-list
  suggestions should be post-filtered before adjudication. (Note the asymmetry: a flag saying
  the *entry's existing* tag is off-vocabulary is the project's highest-precision signal at
  **97.6%** applied this window. It is the *suggested destination* that needs constraining, not
  the flag.)
- **Sole-`general` → specific.** **40 of 147 tag flags (27%)** this window, rejected under the
  standing §A policy, as in the 2026-08-09 runs and the window before that. Apply rate on the
  family: **5 applied / 40 rejected (11%)**.

One line in the prompt — *"`general` is an accepted fallback tag; do not propose replacing a
sole `general` tag with a more specific one"* — retires the second family at zero cost.

**The curator alternative deserves a decision rather than another deferral.** The observation
asks it fairly: entries like {湿疹|しっしん} (eczema, sole `general`) and {音符|おんぷ} (musical
note, sole `general`) arguably *should* carry the obvious specific tag, in which case the
reviewer is right every time and the policy is what is wrong. Either answer ends the recurring
cost; only the current ambiguity pays it every sweep.

## 96. `find_missing_furigana.py` never scans the `headword` field

**Source**: 2026-08-09 routine polish observation; **confirmed in the source and measured at 259
entries** (see [Cleanup P52](cleanup-backlog.md#priority-52-kanji-headwords-with-no-furigana-at-all-259-entries--invisible-to-every-furigana-instrument)).

The script reads `headword` at line 101, then builds `fields_to_scan` from notes, definition
explanations, and examples — and never appends the headword to it. The field is used only to
label output rows. `make check-furigana` therefore reports a bare-kanji headword as clean, which
is why 259 of them accumulated with 24 added in the first ten days of August alone.

**Fix**: append `('headword', headword)` to `fields_to_scan`. One line, and it converts P52 from
a recurring cleanup into a one-time one. Worth pairing with a `validate.py` check so new entries
cannot introduce the defect at all — the project's stated rule ("all kanji must have furigana —
in headwords, examples, AND notes") already justifies it as an error rather than a warning.

## 97. Scan for inline links whose surface reading disagrees with the target entry's reading

**Source**: generalised from the 2026-08-10 stale calendar-month finding
([Cleanup P51](cleanup-backlog.md#priority-51-stale-calendar-month-links--29-entries-point-月-がつ-at-the-moon-entry)).

29 entries link `⟦{月|がつ}→月：02230_tsuki⟧` — a がつ surface pointing at an entry whose reading
is つき. The cause is structural rather than careless: the suffix entry `30418_gatsu` was created
*after* those links were written, so every link authored in the interval had nowhere correct to
point. The same trap is set whenever a suffix, counter, or bound-morpheme entry is created after
the homographic free noun it shares a kanji with, and it will keep being set as the dictionary
grows into its own gaps.

**Detect**: for every `⟦surface→base：entry_id⟧`, compare the reading inside the surface's
furigana wrappers against the target entry's `reading` in `entries_index.json`; report
mismatches. Pure string comparison over data the build already loads — no model, no judgment.

**Expect false positives and design for them**: legitimate rendaku (はな/ばな), counter voicing
(ほん/ぼん/ぽん), and okurigana-driven splits will all trip a naive comparison. A first pass
should whitelist the regular voicing alternations and report only residue; even at moderate
precision this is the instrument that finds the stale-suffix family as a class rather than one
filing at a time.

## 98. A naked-katakana detector — the tractable slice of the unlinked-word problem

**Source**: 2026-08-10 routine polish observation, arising from エリア in 04438 報道 sitting
with no link and no `noentry` marker although 10726_eria exists.

`check_stale_noentry.py` (P35) finds words explicitly marked `noentry` whose entry now exists.
It cannot find the strictly worse case: a word that was never marked at all. The general
version of that problem needs Japanese tokenization, which the project has deliberately avoided.

**Katakana does not.** A katakana run of ≥2 characters is self-delimiting in a way kanji and
kana runs are not, so the rule *"katakana run of ≥2 characters appearing in an example outside
any ⟦…⟧ that matches a `build/word_id_lookup.json` headword key"* needs no tokenizer and no
model. Loanwords are also disproportionately the words a learner most wants a link for.

**Caveats to build in**: skip runs inside an existing `⟦…⟧` surface, skip the entry's own
headword, and expect the katakana-with-hiragana-reading wrapper convention (276 instances,
[blocked on a curator decision](cleanup-backlog.md)) to interact with the match. Precision
should be estimated on a 50-entry sample before this is turned into a sweep — the last four
detector proposals on furigana data died to undocumented conventions.

## 99. Run furigana screening and the accuracy pass sequentially, not concurrently

**Source**: 2026-08-09 accuracy-review observation, measured during the run.

Run concurrently, `review_runner.py --pass screening` managed **28 entries in ~40 minutes**
(~1.7 min/entry) while `review_accuracy.py` covered ~200 in the same window; **stopping the
screener immediately sped the accuracy pass up**, which is the signature of two processes
contending for one provider rate limit rather than of a slow model.

Since screening precision over already-polished ranges has been measured at **0–10%** across a
month (2 applied / 9 rejected this window, 18.2%; 3 of 31 the window before, 9.7%), the trade is
lopsided: the concurrent screener costs several hundred entries of accuracy coverage per run to
buy a pass whose flags are rejected nine times in ten. **Prescription**: drop screening from
runs whose purpose is accuracy coverage, and when both are wanted, run them sequentially.
Worth encoding in §A step 2 rather than leaving to per-run judgment.

## 100. `manage_candidates.py add` should run the duplicate check itself

**Source**: 2026-08-10 new-entries observation — **4 of the 20 "seen in entry" candidates
worked that run were duplicates of existing entries under a variant orthography**: にかけて /
〜にかけて, しかない / 〜しかない, 焼印 / 焼き印, 一人ぼっち / 独りぼっち.

The capture step in `comprehensive_polish.md` adds a candidate the moment a polish run meets a
word it thinks lacks an entry, and the variant-orthography cases are exactly the ones a human
eye misses: the dictionary's entry is prefixed with 〜, or spells the okurigana out, or uses a
different kanji for the same word. The cost lands two weeks later on a `new-entries` run, which
spends its scarce "seen in entry" lane on words that already exist.

**Fix in the tool, not the prompt.** `manage_candidates.py add` should call the same logic as
`check_duplicate.py` (**without** `--skip-candidates`) and refuse — or at minimum warn loudly —
on a hit, normalising a leading 〜 and okurigana variants before comparing. Every capture site
then inherits the check, and no prompt has to remember it. This is strictly better than the
prompt-side instruction the observation proposes, which would need repeating in every prompt
that captures candidates.

## Updates 2026-08-11 to existing items

**Item 24 (furigana screener) — sixth, seventh and eighth data points, all zero, and the
retirement case is now also an *arithmetic* one.** Two 2026-08-11 observations:

- 07566–08065: **85 flags across 60 entries, zero true positives** — the third consecutive
  sweep at ~0%. Every "incomplete reading" flag cited a pair that **does not exist in the entry**
  (flagged `{空席|くうせ}`; the entry holds `{空席|くうせき}`); the rest were correct rendaku
  (`{買|が}い` in まとめ買い, `{時計|どけい}` in 仕掛け時計) or readings the entry itself documents
  as variants (07958 粗利/そり).
- 07266–07565: **38 screening flags written 2026-06-19 and never deep-reviewed**, every one
  verified false **at zero API cost** by extracting the actual `{kanji|reading}` pairs from the
  entry files (裁量→さいりょ, 同人誌→どうじん, 不可思議→ふか, 逡巡→しゅんじゅ, 調味料→ちょ — all
  artifacts of the truncated display string, all held complete in the entries).

Both observations diagnose this as the screener's prompt builder still passing a fixed-width
window instead of the full `{kanji|reading}` pair. **That diagnosis is wrong, and checking it
changes the item.** `trim_context()` (`build/review_runner.py:152`) was fixed on 2026-07-30 and
is correct today: it cuts the context back to the last wrapper boundary, and the pair itself was
never windowed — it comes straight from the regex match. The prompt builder is fine.

**What is actually happening: the fix was never applied retroactively to stored results, and
sweeps re-adjudicate pre-fix output as though it were current.** The 07586 flag quoted above
(「item 11, `{空席|くうせ}`, is incomplete」) sits in `reviews/screening/07586.json` with
`screened_at: 2026-06-19` — six weeks before the fix. Measured across all stored results this
harvest:

| Stored screening results | Count | Flagged | Flag rate |
|---|---|---|---|
| Screened **before** the 2026-07-30 fix | 19,368 (85%) | 1,950 | **10.1%** |
| Screened **after** the fix | 3,454 (15%) | 170 | **4.9%** |

In the 07566–08065 band specifically, the run that reported "85 flags across 60 entries" was
reading **54 pre-fix flags and 7 post-fix ones**. So the dominant false-positive family in that
report is pre-fix residue, correctly diagnosed as an artifact — of an instrument that no longer
produces it.

Two consequences, and the second is the important one:

1. **The fix worked, by the only measure available**: the flag rate halved, 10.1% → 4.9%.
2. **Every "post-fix precision" figure on this page is contaminated**, including the "0 applied
   of ~158 flags across eight consecutive runs" above — those runs adjudicated a majority of
   pre-fix flags in an unmeasured proportion. The retire-or-downsample decision has therefore
   never been evaluated against the fixed instrument. Before that decision is made, the honest
   number to compute is precision over the **170 post-fix flags only**.

This is the same shape as the original defect one level up: a correct fix to the instrument left
its *stored output* carrying the old defect, and the stored output is what everyone read. Filed
as case 8 in [Instrument Defects vs. Corpus Defects](../topics/instrument-defects.md). Item 102
is the fix.

**Item 77 (formality flags at 10%) — the family is now provably free to adjudicate.** A
2026-08-11 accuracy-review reproduced **all 19** of its formality adjudications mechanically:
13 confirmed and 6 rejected by reading the first sentence of the entry's own REGISTER section
(casual/colloquial/everyday → `informal`, "Neutral to…" → `neutral`, formal/official/legal →
`formal`). This does not change the *rule* — the 2026-08-10 cleanup-backlog update established
that flagging only on a notes-vs-label contradiction is already correct and already what the
reviewer does — it changes **where the rule should run**. A ~10%-precision family that costs
OpenRouter budget every sweep can be moved to a free deterministic check with no loss of
accuracy on this sample. Combine with queue item `tag-formality-contradicts-register-note`.

**Item 90 (`--dimensions links`) — third data point, and the clearest one yet.** A 2026-08-11
stale-`noentry` sweep reported that of **19 error-severity flags on 45 changed entries, 17 were
pre-existing tag-narrowness or gloss nits unrelated to the edit and 0 concerned a link target**.
A link-only run therefore pays full whole-entry review cost to verify nothing it actually did.
Same conclusion as 2026-08-09 and 2026-08-10; the instrument remains missing.

**Item 94 (review recency) — the padding is measured and the queue's headline is affected.** A
2026-08-10 observation re-states the measurement behind this item as a metric moving the wrong
way: **3,513 of 9,932 queued entries (35%) already carry an `reviews/accuracy/` report newer
than the entry's `metadata.modified`**, much of it self-inflicted (the §4 at-birth self-check
reviews every new entry, then CI queues those same entries for the review they just had). The
review-queue depth has been the headline health metric for four `quality-metrics.md` refreshes;
the *direction* survives the correction (padding is roughly proportional) but the *level* does
not. One predicate fixes both the queue and the sweep cursor.

**Item 95 (`general` is a legal fallback) — fourth and fifth filings; escalated to the curator.**
Two more 2026-08-11 observations report the same family: ~41 flags in one sweep and ~30 in
another, both rejected wholesale under the standing §A policy, both noting this is now
**~25–30% of all tag-flag volume every sweep** and pure adjudication cost for a foregone
conclusion. The observations are explicit that this needs a decision rather than a sixth
filing, and they name the two clean exits: (a) teach the reviewer prompt that `general` is an
accepted fallback and that in-list narrowness substitutions are out of scope, or (b) the curator
rules `general` unacceptable as a sole tag, at which point it becomes a deterministic detector
(`check_tag_drift.py --check sole-general`, already built, 3,681 flags) and stops being an API
question either way. Escalated to `reviews/needs_curator.txt` this harvest.

## 101. Any census must assert it found the field before reporting zero

**Source**: 2026-08-11 accuracy-review observation, plus a verification failure this harvest.
**Status**: open. **Effort**: trivial per script; the value is the convention.

A 2026-08-11 run's first census reported "**0 entries with off-vocabulary tags**" for a band
that actually had **208**. The cause: it read `entry["tags"]`, but tags live at
`entry["metadata"]["tags"]`. The wrong path returns an empty dict rather than raising, so the
defect renders as *the most reassuring possible result* — a clean bill of health, in the exact
shape a correct run would produce.

This is not a one-off. The same run's other novel finding — "a contiguous block of 25 entries
(07832–07861) with no semantic tags at all" — **did not reproduce** when re-measured this
harvest against `metadata.tags.semantic` (zero such entries in 07566–08065; 79 dictionary-wide,
none in that band). One buggy census produced both a false negative and a false positive in the
same run, and both were filed as findings.

**The convention**: any ad-hoc census or new detector should assert non-emptiness on a
known-good sample before it reports a count — e.g. fail loudly if `metadata` is absent, or if
100% of scanned entries return an empty tag set. A zero that cannot distinguish "nothing there"
from "looked in the wrong place" is worse than no measurement, because it gets written into the
backlog as fact. Worth a line in the detector-writing guidance and a helper
(`load_entry_tags(entry)`) in `build/coverage_utils.py` so no future script re-derives the path.

## 102. Expire stored screening results when the screener changes — and re-read the entry before paying for a deep pass

**Source**: 2026-08-11 accuracy-review observations (38 stale flags closed at zero cost; 85 flags
at 0% precision), plus the stored-result measurement in the item 24 update above.
**Status**: open. **Effort**: small (a date gate + a string comparison).
**Relation to item 24**: item 24 is the retire-or-downsample *decision*; this is what has to ship
before that decision can be evaluated honestly.

**19,368 of 22,822 stored screening results (85%) predate the 2026-07-30 `trim_context()` fix**
and carry 1,950 flags produced by a defect that no longer exists. Nothing invalidated them, so
`--pass deep` and every adjudicating run treat them as current evidence — which is why three
consecutive sweeps concluded "0% precision, third consecutive sweep" while actually
re-adjudicating June output.

**Two fixes, both cheap:**

1. **Date-gate the cache.** Record a `screener_version` — or simply compare `screened_at`
   against a `SCREENER_CHANGED_AT` constant bumped whenever the prompt builder changes — and
   treat older results as absent: skip them in `--pass deep` and re-screen rather than trust
   them. A stale result is worse than a missing one, because a missing result prompts a
   measurement and a stale result prompts a conclusion.
2. **Re-read the entry before queueing a deep review.** Independently of dating, drop a flag when
   (a) the cited `{surface|reading}` pair does not appear in the entry at all, or (b) the cited
   reading is a proper prefix of a pair the entry does contain. Both conditions are exactly the
   truncation artifact and both are decidable by string comparison. On the 07266–07565 sample
   this closes **38 of 38** flags for free — a run did it by hand and reported it as such.

The principle is worth lifting out of this item: **paid judgment should only be spent on flags
that survive a free mechanical check**, and any cached model output needs a version stamp, or it
will outlive the model, the prompt, or the bug that produced it.

## 103. `check_stale_noentry.py`: a `proper_name_risk` column

**Source**: 2026-08-10 stale-`noentry` sweep (entries 01440–02229).
**Status**: open. **Effort**: small.

The sweep found a false-positive family that class R cannot see: **proper names whose target
entry carries only the common-noun sense**. ⟦朝日⟧ inside 朝日新聞 resolves to 23495_asahi
"morning sun"; ⟦毎日⟧ inside 毎日新聞 resolves to 00729_mainichi "every day". Readings agree, so
no mechanical reading check catches it, and the link is wrong in a way a learner would feel
immediately. Place names used *as* place names are the correct contrast case (上野動物園 →
28394_ueno is right).

**Proposed**: flag a marker when the surrounding text places the base immediately before a
name-forming suffix (新聞 / 銀行 / 大学 / 株式会社 / 高校 / 病院) **and** the sole candidate
entry's gloss carries no proper-noun sense. That surfaces the family without a per-entry read.
Note this interacts with the 2026-08-11 proper-noun scope decision: as proper-noun entries are
created, some of these resolve by the target entry gaining the sense, so the column should be
re-run rather than acted on from a stale snapshot.

## 104. Two linking traps no validator can see: copula-で and na-adjective-な

**Source**: 2026-08-10 and 2026-08-11 polish observations.
**Status**: open. **Effort**: small per detector; the skill-side note is the more urgent half.

Both are cases where a correct-looking inline link is a semantic error, and nothing in
`validate.py` or the link checkers can tell:

1. **The te-form of the copula is graphically identical to the particle で.** In 「性格で、」 the
   で is the copula, and linking it to 00502_de (location/means particle) teaches the wrong
   word. A detector could flag ⟦で⟧→00502 where the preceding token is a noun/na-adjective stem
   followed by a comma — a heuristic, so it belongs in a review queue, not an auto-fix.
2. **The attributive な after a na-adjective is linked inconsistently dictionary-wide.** 00175
   可能 links it as 09497_na; 01120 特別 and 01674 適当 had it naked in every example until the
   2026-08-10 run. A detector for `\{[^}]+\}な` immediately following a `adjective-na` headword,
   with the な not already inside ⟦⟧, would quantify the backlog before anyone decides which
   convention is right — and the decision is the prerequisite, since both treatments are
   currently defensible.

Related: the `inline-word-links` skill gives no rule for **single-kanji morphemes cited inside
FORMATION / ETYMOLOGY sections** ({軽|けい} + {率|そつ}). They are not words in use, so linking
them is wrong, and marking them `noentry` would pollute the candidate queue with bound
morphemes. The 2026-08-11 polish run left them unlinked, which is the right call; the skill
should say so explicitly, or different sessions will keep resolving it differently. (Skill
change — recorded here, not made from a wiki session.)

## Updates 2026-08-12 (wiki harvest)

Three new items, two retirements, and one proposal closed against a decision already on record.

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

## 106. `review_accuracy.py --dimensions links` — fourth request, second measurement

Requested 2026-08-09, 2026-08-11, and twice on 2026-08-12. The 2026-08-12 systemic-fix run
supplied the second consecutive measurement: of **13 flags on a 37-entry stratified sample from a
link-only run, zero concerned a link target**; all thirteen were pre-existing gloss/tag
observations on entries the run happened to touch.

The general statement is that **§4's self-verification instrument is mismatched to link-only
runs**. A whole-entry accuracy review costs a model call per entry and returns findings about
dimensions the run did not change, which then either get adjudicated — spending the run's
scarcest resource on unrelated work — or skipped, which trains the run to ignore its own
verification. A `links` dimension would ask the one question such a run needs: does the surface
in `⟦surface→base：id⟧` denote the entry that `id` defines?

It would also have a stated rule to check against rather than a vibe. The same window produced
both halves of the discriminator: the 朝日新聞 family (2026-08-11), where the surface is a
company name that merely *contains* the word, must not be linked; the 猫に小判 / 歩行者天国 /
早起きは三文の徳 family (2026-08-12), where the sentence uses the word figuratively and the entry
defines it literally, **should** be, and was. The test is **same-lexeme**, not
literal-versus-figurative — which is a rule a reviewer prompt can hold.

## 107. Accuracy-review pre-flight: check for existing reviews before paying for a pass

The 2026-08-12 accuracy-review run over 08347–08850 found that most of the range **already had
`reviews/accuracy/{id}.json` files from 2026-06-22 that had never been adjudicated**, and
regenerated them. That is a full pass's cost spent reproducing judgments already on disk.

It is the second half of a problem whose first half is Tooling 94 (35% of `reviews/queue.txt` is
entries whose review is newer than their last modification). Both halves are the same predicate
at different call sites — *does a review newer than `metadata.modified` already exist for this
entry?* — with complementary consequences: **94 stops the queue from padding; 107 stops the mode
from paying twice.**

A default follows: an accuracy-review run should **start in adjudication mode** where its range
already has coverage, and generate only for the uncovered residue. The same run measured the
generation rate at **1.5–2.6 entries/minute**, so a 500-entry range needs 3–5 hours of wall clock
— far more than one Routine run has. §A's "~400–600 entries per run" is therefore reachable
*only* on ranges where reviews already exist, which makes this pre-flight the thing that turns a
documented target into an honest one instead of a standing over-promise.

## 108. The 59 dangling cross-references are a zero-duplicate candidate vein

This began as a reported blind spot and measured out as a supply of new-entry candidates.

`check_artifacts.py`'s `missing-target-id` check reports 37 instances across 33 entries; a direct
scan finds **97 target-less references across 86 entries**. The gap is not a defect.
`ref_is_resolvable()` deliberately suppresses references whose word has no entry, because a
`target_id` cannot be filled in for a word that does not exist — which also answers the
2026-08-11 filing that asked whether the detector covers the 06880–06882 shape (references to
気が利かない, 気が軽い, 気が長い, none of which were ever created). It sees them and excludes
them, correctly.

What is new is what is inside the suppressed set. Measured 2026-08-12: **59 target-less
references naming 59 distinct words with no entry, across 57 entries — and exactly one of the 59
is in `candidate_words.json`.** Samples: 一昨日, メンテナンス, ぞっとする, 内閣改造, くるまる,
保冷, 入閣, 削れる, ほしい, お坊さん, アルカリ性, 仕事始め.

Why this matters now: the 2026-08-11 candidates run measured the common-vocabulary discovery
lenses at **72–100% duplicate rates** across four probe batches and concluded that restock runs
must generate 3–4× their target to hit it. This vein has a **duplicate rate of ~2% by
construction** — every word in it was tested for existence by the same `by_reading` lookup
`check_duplicate.py` uses — and every word in it is already named by a live entry, so creating it
closes an internal gap instead of adding a leaf. It is the same argument the 2026-08-12 polish
run made for the RELATED-EXPRESSIONS sibling idioms (口が滑る, 頭に来る, 手が空く…), and it
generalises: **the dictionary's own dangling references are its highest-yield candidate source,
and nothing was reading them.**

Ship as a flag on the existing detector — `check_artifacts.py --check missing-target-id
--unresolvable-as-candidates`, emitting word / reading / source-entry rows for
`manage_candidates.py add-batch` — rather than as a new script. 59 words is roughly one and a
half restock runs' output, at a survival rate no lens has come close to.

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

## Update to item 100 (`manage_candidates.py add` should duplicate-check itself)

The related furigana-markup defect reported by the 2026-08-12 new-entries run — candidates stored
as `{口|くち}が{滑|すべ}る`, which `sync` then cannot match against the entry created from them —
is **clean as of this harvest: 0 of 170 candidate rows carry brace markup**, the ten known cases
(C23094–C23103) having been removed by hand in that run. The ask is therefore prevention, not
cleanup: strip `{kanji|kana}` wrappers in `add`/`add-batch` before storing, or normalise both
sides in `sync`. Cheap while the queue is small and vetted; it becomes a real cleanup again the
first time a polish run captures ten more.

## Updates 2026-08-13 (wiki harvest)

### 109. The Routine's CI gate spends its whole poll budget in under a minute

**Escalated to the curator — this is a one-sentence fix in `prompts/routine2.md` §7 step 5.2,
and knowledge-base sessions do not edit prompts.**

§7 tells the run to wait between check-run polls with a backgrounded `sleep 30`
(`run_in_background: true`, because foreground `sleep` is disabled in this harness). A
backgrounded command returns to the model **immediately**. Unless the run explicitly waits for
that background task to finish before re-polling, the ~16-poll budget is consumed in well under
a minute — against a CI job that in this repo often takes 3–6 minutes just to *start*. The run
then reports a PR as stuck, or concludes the check-runs API is serving stale results, having
observed about forty seconds of wall clock.

Three Routine runs have now reported the symptom, two of them as "the GitHub MCP
`get_check_runs` endpoint is stale". The 2026-08-13 new-entries run traced the mechanism and
confirmed the API was answering correctly in its own case (its job had genuinely failed at
00:38:49 and the API said so). Full argument in
[Instrument Defects, case 9](../topics/instrument-defects.md).

The fix, in the curator's words if he prefers his own: **§7 step 5.2 must say to await the
backgrounded sleep before re-polling**, and should point at `get_job_logs` for per-step detail
when a check has genuinely failed. Cost of not fixing it: stranded PRs, which is the exact
failure §0a exists to clean up after.

### 110. `review_accuracy.py` writes a `reviewed_at` that is not when the entry was reviewed

Reported by the 2026-08-12 accuracy-review run: a self-check started at 22:45 on 2026-08-12
produced result files stamped **21:32**. The field appears to be stamped once at pass start (or
inherited from a template) rather than at write time, so anything that reasons about *order* —
"was this entry reviewed before or after I edited it?" — cannot use it. That run briefly
mis-read two already-fixed flags as surviving errors because of it.

This is small but load-bearing: item 94 proposes retiring the review-queue padding with a
`reviewed_at >= modified` predicate, and item 107 proposes skipping entries that already carry a fresh review. **Both consume this field, and
neither can be trusted until it is stamped at write time.** The working discriminator today is
incidental — a `--dimensions tags` self-check writes `["tags"]` into `dimensions`, so the array
identifies the pass — which is not something to build on.

### 111. The accuracy reviewer's `tags` dimension should report only off-vocabulary tags

Two independent measurements now say the same thing about the highest-yield review dimension.
Its **not-in-`VALID_SEMANTIC`** flags are close to always right — 87–99% applied across the last
five refreshes of [Quality Metrics](../topics/quality-metrics.md) — while its **in-list
substitution** suggestions are narrowness nits that §A's standing policy rejects by design, at
around 5%. The prompt currently invites both.

Telling the reviewer to report only tags **absent from the supplied vocabulary**, and to stop
proposing substitutions between two valid tags, would raise the dimension's precision without
losing anything the project acts on. This refines items 14 and 17 rather than replacing them:
those addressed the reviewer's false claims *about* the vocabulary; this addresses the half of
its true claims the project has decided not to act on.

### 112. `check_duplicate.py` is blind to three duplicate shapes that reach entry creation

The 2026-08-13 new-entries run lost session time to all three, and a 2026-08-13 polish run hit
the second independently:

1. **Kanji/kana orthographic variants of the same word** — 擦り寄る vs 摺り寄る (17576),
   さじを投げる vs 匙を投げる (20433), 首をかしげる vs 首を傾げる (17531), うやむや vs 有耶無耶
   (08049). The script reports these as *"Homophones exist"*, which is the label for a genuinely
   different word with the same reading, so they pass candidate vetting. **Four of twenty-four
   candidates in one batch.** Same reading + one side a kanji/kana respelling of the other should
   be reported as a duplicate, not a homophone.
2. **Kana-headword entries queried by their kanji spelling** — 多分/たぶん reports "not in the
   dictionary" although `00815_tabun` exists with headword たぶん. A reading-based fallback fixes
   it.
3. **A new *sense* of an existing word arriving as a new headword** — C23011 ぶり ("manner or
   style of doing") was queued although `28358_buri` existed with the "for the first time in"
   sense. Vetting compares headword+reading against existing entries but never against the senses
   those entries already carry. Handled correctly in-run (sense 2 added to 28358 instead of a
   duplicate headword), but only because the run noticed.

(1) and (2) are cheap and mechanical. (3) is not solvable by string comparison and probably
belongs in the candidates-mode vetting prompt as an instruction to read the existing entry when
the reading collides, rather than in the script.

### Update to item 20 (the priority lane's ranking is stale by construction)

The 2026-08-12 polish run adds the sharpest throughput measurement the item has: at
`priority/notes.txt` lines 80–110 it skipped **31 consecutive entries** as modified inside the
30-day window, and read **39 lines to find 4 workable entries**. Its diagnosis is item 20's, in
one sentence: the list is re-ranked from note *scores*, and polishing frequently does not raise
that score (adding cross-references and inline links leaves the note text alone), so
recently-polished entries keep their rank and keep re-surfacing at the head.

Its proposal — a `--exclude-recent` flag on `prioritize_polishing.py` so the generated file is
pre-filtered instead of every run paying the skip cost — **is the generation-time recency
down-weight this item has recommended since 2026-06-25**, arrived at independently for the
forty-something-th time. Nothing new to decide; recorded because the throughput number (4 of 39)
is the concrete cost figure the item has otherwise lacked.

## Updates 2026-08-14 (wiki harvest)

### 113. The asymmetry report needs a "target holds no references" grouping

`find_merge_candidates.py --asymmetry-only` emits **8,633 one-way pairs** as a flat list. Two
polish runs in two days independently guessed it was blind to bare entries; it is not (see
Cleanup P57). What it lacks is the one split that turns its output into work: **2,183 of those
pairs point at a target with no `cross_references` and no `prominent_see_also` at all** — 1,550
distinct entries — where the back-reference decision needs no judgment, against 6,450 pairs
where the target has a reference list and chose differently.

Ask: a `--bare-targets` flag (or a `bare_target: true` field in `--json`) plus grouping by
target, so 正月 appears once with its ten inbound references rather than ten times among 8,633
lines. Both are read-only additions to an existing report. **Cost**: small. **Value**: converts
a report nobody works into a queue a `systemic-fix` run can take.

### 114. The furigana screening cache cannot express "re-screen entries screened before X"

The 2026-08-14 accuracy-review run measured the cost of the stale cache directly: in 9809–10400,
**46 of 48 `flagged` entries had been screened before the 2026-08-11 `trim_context` fix**;
re-screening the same entries with the current prompt cut them to 10, of which 2 were real. The
~36 eliminated flags were all the truncated-wrapper family (`{天文台|てんもんだ)`) that
`trim_context` was written to remove — and `--pass deep --range` deep-reviews every one of them
at ~$0.01/entry.

The run asked for a `--rescreen-before DATE` flag. **As stored, that cannot be implemented**:
`reviews/screening/screening_status.json` is `{"screened": {id: "ok"|"flagged"}, "last_updated":
<one timestamp for the whole file>}` — 10,888 entries, **1,002 currently `flagged`**, and not one
per-entry timestamp. So the item is two changes, in order:

1. **Stamp per entry** — store `{"status": ..., "screened_at": ..., "prompt_version": ...}`.
   This is the same defect as item 110 (`reviewed_at` not written at pass time) in the other
   review instrument, and the same fix.
2. Then `--rescreen-before` becomes trivial. Until then the only available remedy is a one-time
   reset of the 1,002 `flagged` values so they re-screen cheaply (~$0.0001/entry) instead of
   being deep-reviewed at 100× the price.

Related: `quality-metrics.md` attributes the `furigana` dimension's ~1% apply rate partly to
this cache, so the fix also un-contaminates a headline metric.

### 115. `--notes-only` mode for the inline-link checks

From the 2026-08-13 polish run: in the priority-lane entries it worked, examples were usually
fully linked while the *notes* were bare — 00970 緑 was the extreme case, every example linked
and ~12 unlinked words in the notes. The existing queue item
`inline-link-examples-bare-notes-linked` (33) is the mirror image of this and was found because
someone looked; nobody has measured the notes-bare direction, because every link instrument
scans both fields together and reports one number per entry. A `--notes-only` switch on the
link checks would size it in one run.

### 116. A rendaku sanity check in `manage_candidates.py add`

Candidate C23122 stored 足手まとい as あしてまとい; the standard modern reading is あしでまとい.
It was caught at entry creation, but nothing in the candidate pipeline checks it — and a wrong
reading in the queue becomes a wrong `romaji` in the entry ID, which
[CLAUDE.md](../../../CLAUDE.md) forbids renumbering later because IDs are URLs. Ask: when a
candidate's reading contains a compound-second-element kanji whose standard reading voices
(手→で, 川→がわ, 箱→ばこ, 紙→がみ, 花→ばな …) and the stored reading uses the unvoiced form, warn.
Rendaku is not fully rule-governed, so this must warn rather than rewrite — but the warning is
free and the class of error it catches is permanent.

### 117. Two furigana detectors the polish and review lanes asked for

- **Ruby spans that cross a word boundary.** 06925 故に carried `{我思|われおも}う` as a single
  span, which had to be split into `{我|われ}{思|おも}う` before either word could be linked. A
  span whose kanji run contains a boundary between two known headwords blocks linking silently,
  and the linking step is where it surfaces — one entry at a time.
- **Single-kanji spans carrying their in-compound reading.** Component/etymology sections present
  a kanji with the reading it takes *inside* the compound rather than its own: 10043
  `{風|ぷう}` (from 薫風), 10082 `{面|なも}` (from 水面). Both were genuine errors; 10083 陽炎 does
  the same job correctly with standalone readings. Cheap predicate: a single-kanji span whose
  reading begins with a voiced or handakuten mora that is unvoiced in the kanji's own readings —
  and `kanji/` already holds on'yomi and kun'yomi for every kanji in the dictionary, so the
  check needs no new data.

### Update to item 111 (the reviewer's `tags` dimension should report only off-vocabulary tags)

New evidence from the 2026-08-13 accuracy-review: of 45 entries carrying an off-vocabulary tag
in 09309–09808, the model reported **5 at `error` severity and 40 at `warn`** — for a property
that is decidable by set membership against a list the prompt itself supplies. §A's
effort-scaling rule invites working `error` flags individually and sampling `warn` flags, so a
run that follows it misses 89% of the highest-precision class the reviewer produces. Two
remedies, either sufficient: force `error` for set-membership failures in the prompt, or have
accuracy-review runs start from the free, complete deterministic scan
(`validate_tags.py`) and use the model only for the attachment question. The second is
preferable because it stops paying a model to re-derive a set difference.

### Update to item 84 (`RATE_LIMIT_INTERVAL` is what bounds review coverage)

Second independent measurement, from the same run and the same account at the same time:
`review_accuracy.py` covered 495 entries in ~20 minutes (~37/min) while
`review_runner.py --pass screening` took ~50 minutes for 277 entries (~9/min). Screening also
cost **eight times less** ($0.035 vs $0.216). The constraint on the cheaper instrument is
therefore latency, not budget — the same conclusion item 84 reached from the other side, now
with the two instruments measured against each other rather than against a target rate.

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

## Related pages

- [Cleanup Backlog](cleanup-backlog.md) — patterns these tools would address
- [Entry Follow-ups](entry-followups.md) — specific entry fixes
- [Architecture and Build System](../project/architecture.md) — build script overview
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis of the tag-drift patterns that items 5 and 6 address
- [Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) — analysis of the wrapper-format patterns that items 8 and 9 address
