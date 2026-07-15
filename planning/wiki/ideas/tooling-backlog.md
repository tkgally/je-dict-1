# Tooling Backlog

**Last updated**: 2026-07-14 (wiki harvest of the 20 loose 2026-07-13/14 observations from four routine polish runs + a systemic-fix run + accuracy-review sweeps — all reinforcements: **item 20** — forty-seventh/forty-eighth no-op confirmation, plus the sharpest single-run **consolidated root-cause statement** of both `score_note_quality.py` scorer bugs [(1) `has_bare_kanji` counts inline-link base-forms as bare kanji → every fully-linked entry scores furigana=0; (2) `find_sections` credits `usage` only via literal headers, missing `FORMS:`/`COMMON PATTERNS:`/descriptive headers → required=0], with the concrete IDs (00335/00464/00617/00647/00785 …) and header strings in one place — regeneration proven deterministically futile; **item 17** — seventeenth/eighteenth confirmation across three 14187–14899 accuracy-review sweeps [24.5% / ~17% tag precision; 33/48 and 84/114 flags the in-list-narrowness/formality-nit noise, genuine applies all off-vocab migrations], the two-regime split now range-independent into the 14000s; **item 21/31** — tenth truncation-class confirmation [`review_runner.py` screening hits a ~2-min wall-clock ceiling on 20–30-entry batches → a systemic-fix §4 self-check now needs 2+ invocations; recommends a `--resume`/skip-already-screened flag]; **item 23** — reinforcement [the C06000–C14000 corpus-harvested block enumerated as OCR/hallucination non-words 権使/些道/個尊/怒燥/試戦/発炭 + compositional phrases; scoped `clean_up_candidates_list.md` purge + intake plausibility heuristic]; **item 6** — a 14387–14899 systemic-fix migration [19 off-vocab tags, all 1:1-mappable via the accumulated map] confirms the cohort stays deterministic-migratable into the 14000s [dict-wide residue ~6,235 entries]. Also filed to Cleanup **P11 (new)** [the ～ハラ/harassment noun cluster carries four inconsistent tag treatments — 08788 マタハラ `social-issues`, 06466 モラハラ `emotion`, 05904/05905 both `general` → a harassment-cluster `tags` pass to `society`], **P21** [zero-link band → 06465–06479, 06400–06500 a contiguous unlinked zone], **P20** [off-vocab cohort into the 14000s, ~6,235 residue], **P17** [katakana-loanword formality drift both directions — 06474 プロフィール `informal`→neutral, 06475 `formal` vs its Neutral note], **P13** [placeholder sole-`general` + plain-wrong 入会金→`education` at 06475–06479 → a ~06400–07000 tags sweep], and **P9** [wrapper backlog thins above ID ~11000 → reprioritize sweeps to the dense 23000–29999 + pre-06000 blocks].) Prior 2026-07-11 (wiki harvest of the 9 loose 2026-07-10/11 observations — all reinforcements: **item 17** — fifteenth confirmation, a 13550–13649 accuracy-review ran **26/99 = 26% flagged**, above the 20% reviewer-noise threshold, with the dominant family again `general`-too-broad in-list narrowness [n=12, all rejected per §A — "'general' is too broad, replace with health/politics/military/history"], and the only genuine applies the two not-in-list migrations [legal→law 13640, body→body-part 13649] plus one clear existence→health mismatch [病む 13611]; reconfirms the unshipped fallback-tag-exception prompt fix separates the two regimes; **item 20** — forty-third/forty-fourth no-op confirmation [two 2026-07-10 routine polish runs ran priority lanes 5/6 and 4/4 no-op on the same closed-tier basic/function set (ない/など/いろいろ/一緒/黄色/ぐらい, then 03728_maa/02947_hikui/00025_chiisai/00533_osoi); the lone non-no-op was 02900_gurai (naked います→いる/が/なら in examples), off the notes scorer's axis; **priorities were regenerated twice earlier the same day** and the same basic-tier function words re-ranked to the top each time — regeneration proven deterministically futile a third time, so both runs advanced the priority cursor past the examined no-ops instead of resetting]; same binding fix (scorer-bug pair + structured-note credit + `prioritize_polishing.py` recency/structural-floor down-weight for closed-tier function words); **item 21 / item 31** — `review_runner.py` furigana screening remains very slow/unreliable in the Routine env [~8 s/entry with intermittent multi-minute stalls, likely gemini-2.5-flash rate-limit backoff + parse-failure retries; had to scope furigana screening to a 27-entry sub-range this run, while `review_accuracy.py` over the same range ran to completion steadily] — reinforces both item 21's ≤~150-ID range-sizing and item 31's per-request HTTP timeout + retry cap, and argues for a faster/cheaper screening model; **item 23** — reinforcement [a 2026-07-11 new-entries run surveyed ~600 candidates to hand-pick ~12 genuine standalone lexemes; candidate_words.json heavily diluted with number+counter combos (二通/四十五), transparent compounds (排水処理), particle-phrases (明かりを消す), and outright errors (アンパッサン glossed "ice cream sundae") — the standing `clean_up_candidates_list.md` purge / stricter find-candidates filter would sharply raise new-entry throughput]. Also filed to Cleanup **P20** [off-list tags dense in 13650–13724, whole 13650–14149 block a `check_tag_drift` sweep candidate] and **P21** [zero-link band → 06441–06447 + candidates C22281–C22289].) Prior 2026-07-10 (wiki harvest of the 6 loose 2026-07-09/10 observations — all reinforcements: **item 17** — fourteenth confirmation, but on the genuinely-contaminated **13350–13549** block the ~32% flag rate is mostly *legitimate* off-vocab drift [44 not-in-list flags applied 1:1] with only ~18/200 `general`-too-broad noise rejected, net genuine-error well under 20% — the tuned-prompt prescription cleanly separates the two regimes; **item 19** — two more incidental stale-`noentry` markers (05766 にやにや→29117, 05775 もぐもぐ→new candidate) reconfirm the self-healing `word_id_lookup.json` re-resolution scan's value; **item 20** — forty-second no-op confirmation [priority lane lines 36–83: 4/6 no-op on 遅い/涼しい/曜日/隣, two of them the *identical* 2026-07-09 no-ops → regeneration proven futile again; the 2 real fixes were the item-19 stale-`noentry` markers, off the scorer's axis]; same binding fixes throughout. Also filed to Cleanup **P20** [13300–13549 uniform ~40%/23% off-vocab, single-batch systemic-fix-sweep case], **P21** [zero-link band → 06438–06440 + candidates C22275–C22280], **P13** [frontier sole-`general`→specific applied at 06438 手の甲→body-part, 06439 経理→business].) Prior 2026-07-08 (wiki harvest of 2026-07-06/07/08 loose observations: **item 17** — thirteenth confirmation, the `general`-too-broad in-list-narrowness family runs into the **12507–13199** band [a 2026-07-06 accuracy-review flagged the noise at 12519/12617/12638–12665; a 2026-07-08 accuracy-review over 12674–13199 flagged 121/526 with `tags` and ran **~23% precision** (28 apply / 121 flagged), most rejects in-list narrowness/broadening substitutions the reviewer should not raise — genuine applies were all off-list migrations]; same prompt-suppression prescription, now confirmed range-independent through 13000+. **item 20** — thirty-eighth–fortieth no-op confirmation [a 2026-07-06 priority lane processed 5 entries with only 05432 じゃん a genuine note-link gap; a 2026-07-07 lane processed 8 priority entries with 6 no-op (00025/00533/03877/01003/00765/02841) and only 04376 洗面 (stale-`noentry`→now-resolved) and 02355 好き (naked です in 3 examples) fixable; the 2026-07-07 run advanced the cursor per §2 since priorities were regenerated same-day (rankings current, not stale)]; same binding fix (scorer-bug pair + structured-note credit + `prioritize_polishing.py` recency/structural-floor down-weight). **item 23** — reinforcement [a 2026-07-06 new-entries run reconfirmed the fallback pool is heavily noised below the "seen in entry" tier — derived compounds 発足後/他人の力/集客効果, bare numerals/counters 四十五/二通/三千円, phrase fragments 速やかに処理する/どれか一つ, and mis-glossed/typo items 三重「みえ」glossed "triple"/怒燥 likely 怒濤 — the standing `clean_up_candidates_list.md` purge would raise new-entries yield]. Also recorded (session log only): the accuracy-review furigana deep pass ran **0/16 precision** on the already-polished 12674–13199 range (all okurigana/compound-split/rendaku/see-also FPs) — the documented calibration/[item 24](#24-non-hiragana-reading-lint-cheap-replacement-for-the-furigana-screeners-true-positive-class) known-noise family, no new action. Prior 2026-07-06 (wiki harvest of 2026-07-05 loose observations: **item 20** — thirty-sixth/thirty-seventh no-op confirmation [two 2026-07-05 priority `notes.txt` lanes ran all-no-op on the same closed-tier basic/core set — 01118_nai/03095_nado/02947_hikui/00025_chiisai/00533_osoi/03877_youbi/01003_tonari/04376, all fully polished with structured notes + full inline links; one lane 5/5 no-change, the other 8/8, one regenerated priorities at wrap-up; restates the notes heuristic over-ranking inherently-long grammatical entries and recommends a recency+completeness discount — the same fix already filed as the scorer-bug pair + structured-note credit + `prioritize_polishing.py` recency/structural-floor down-weight]). Prior 2026-07-04 (second wiki harvest, of 2026-07-04 loose observations: **item 17** — twelfth confirmation, the `general`-too-broad in-list-narrowness family into **12002–12134** [43/133 = 32% flagged, almost all in-list `general`→narrower REJECTs: 増税→economics, 国政→politics, 変容→change; genuine applies were off-vocab migrations + one wago education→language + one 回忌 counting-offset translation fix — same prompt-suppression prescription]; **item 20** — thirty-fourth/thirty-fifth no-op confirmation [the same closed-tier set ない/だって/低い/小さい/遅い/曜日/まあ scored 33–57 yet content-complete with full inline links; one lane 5/6 clean + regenerate/reset, the other restated the rigid-POS-template root cause and the cross-run-loop risk]. Prior 2026-07-04 (wiki harvest of 2026-07-03 loose observations: **item 17** — tenth/eleventh confirmation carrying the `general`-too-broad in-list-narrowness family into the low 12000s [11894–11923 general→action/law nits rejected; 11924–12001 20/78 flagged but 6 applied] **plus a formality `formal→neutral` downgrade sub-family** [厨房/名高い/厭う/原案/喜ばしい — reviewer ignored the entries' own formal-register notes], sharpening the register sub-fix: consult the entry's register notes before any formality flag; **item 20** — thirty-second/thirty-third no-op confirmation [two 2026-07-03 priority lanes all-no-op on 02007/04376/04767/02355/00765 and だって/まあ/低い/小さい/遅い] plus a **POS-misclassification detail pinning scorer-bug #2** [まあ scored as `verb-godan`, wrong POS template applied — scorer must derive POS from `tags.pos` before choosing the section template]. Prior 2026-07-03 (harvest of 2026-07-02/03 loose observations: **item 17** — ninth confirmation, `general`-too-broad in-list nit dominates a 11647–11765 sweep [29/118, 13 "`general` too broad" alone; only genuine applies were off-list migrations + a 代名詞 education→grammatical category error — prescription sharpened to "flag only off-list tags + clear category errors"]; **item 20** — twenty-ninth/thirtieth/thirty-first no-op confirmation [three 2026-07-02/03 priority-lane runs all-no-op on the same closed-tier set; advancing the cursor past examined lines now the de-facto workaround over the futile regenerate+reset]; **item 21** — eighth truncation-class [a 11766–11893 furigana screen overran the 900 s wrapper at ~126 entries at ~9 entries/min → size to ~150 IDs/run]). Prior 2026-07-02 (harvest of 2026-07-01/02 loose observations: **item 20** — twenty-seventh/twenty-eighth no-op confirmation and the sharpest evidence yet that the *scorer*, not recency, is the binding defect [routine polish session 006 found all 6 eligible >30d entries — だって/まあ/低い/小さい/遅い/曜日 — already fully polished yet scored 30–70; recommends adding a "structured-note credit" for ・-bulleted forms/collocation blocks and inline links]. Prior 2026-07-01 (harvest of 2026-07-01 loose observations: **item 6** — a new high-precision detector signal, a physical-object/creature semantic tag on a function-word POS [adverb/particle/conjunction/interjection] is a template error by construction — cleaner than `concrete-noun-domain-mismatch` [single tag suffices, no cluster count], from 06355 どうせ tagged `furniture`; **item 20** — twenty-sixth no-op confirmation [routine_008 priority lane 0/6; recency-stacking restated]; **item 23** — reinforcement [the C05xxx–C14xxx candidate block named as the worst pocket; scoped `clean_up_candidates_list.md` purge]). Prior 2026-06-30 (harvest of 2026-06-29/30 routine runs: **new item 31** — per-request HTTP timeout + retry cap in the OpenRouter client [a screening request hung indefinitely and *survived the outer `timeout` wrapper* — child workers in a separate process group; distinct from item 21's range-sizing]; **item 17** — eighth confirmation, now on the 11188–11300 katakana-loanword/business band [20/113 ~18%, all in-list `general`/`work`-too-broad nits rejected]; **item 20** — twenty-fourth/twenty-fifth no-op confirmation [recency-stacking framing restated]; **item 23** — reinforcement [seen-in-entry 29581–29592 good, oldest-first fallback still unusable]. Prior 2026-06-28 (harvest of 2026-06-27 routine runs): **item 8** — two more degenerate wrapper sub-patterns [English/Latin-text-after-pipe `{ゴマフアザラシ|spotted seal}` at 06561; katakana-only-no-pipe `{ビル}`/`{モード}` at 06308 — both masked as `pure-kana`, both `--fix`-able]; **item 20** — nineteenth/twentieth no-op confirmation [the regenerate+reset loop now demonstrably repeats *within a single day* on an identical basic-tier set]; **item 21** — seventh truncation-class observation [screening+deep ~160 entries/~20 min exceeds one run's wall budget on a full directory]. Prior 2026-06-26: **item 30 RESOLVED** — strand-sweep + CI-gate routed through MCP, scripts now exit cleanly on the platform-policy 403, and the latent `get_status`→`get_check_runs` rescue bug fixed; **item 27 PARTIAL** — the inflow gate shipped as a baseline ratchet [`--check-no-new-unknown` + `unknown_semantic_baseline.json`, now a CI step]; item 21 — sixth truncation [560-ID screen timed out at ~74/560 → ≤~100 IDs/run]; item 20 — sixteenth no-op confirmation [the lone non-no-op was a cross-reference fix the scorer doesn't measure]. Prior 2026-06-25: item 20 — fourteenth/fifteenth no-op confirmation + the recency-skip/scorer-bug-stacking diagnosis; item 28 — second confirmation [2026-06-24 systemic-fix run again landed on scope-0 `tag-conjugation-no-verb-pos`, flipped it to `resolved`; `tag-proverb-idiom-mismatch` still open/scope-0]; **new item 30** — `sweep-stranded-prs.py` 403 against api.github.com under the agent proxy [strand-sweep safety net silently never fires]. Prior 2026-06-24: item 20 twelfth/thirteenth + recency-filter, item 23 seen-in-entry lane empty + junk families, item 24 truncation FP on 9240–9456, **new item 29** `part_of_speech` normalizer)

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

**Enhancement 2026-06-26 (an `--fix` mode for the `{お{…|…}}` nested-honorific shape)**: The detector currently emits a read-only review queue only; every fix is hand-applied. A 2026-06-26 routine polish run (frontier 06288–06300) found 06295/06296 carrying the nested-honorific wrapper `{お{香|こう}}` / `{お{土産|みやげ}}` (the `nested` + `o-go-prefix` classes together) and observed that this specific shape has a **single deterministic, provably-safe rewrite** — `{お{KANJI|reading}}` → `お{KANJI|reading}` (and the `{ご{…|…}}` analogue) — which alters only wrapper boundaries, never the surface text or reading. Add an opt-in `--fix` mode scoped to *this* transform (and the other provably-safe sub-patterns: bare-kana de-wrap, o/go-prefix lift), validated against `word_id_lookup.json` so inline-link surfaces still resolve, so the recurring 06200s–06300s honorific-batch instances (Cleanup P9 update 2026-06-26) can be cleaned mechanically instead of one entry at a time. Keep the default read-only; `--fix` writes only the sub-patterns whitelisted as never-error.

**Enhancement 2026-06-28 (two more degenerate right-side / no-pipe sub-patterns from the 06xxx frontier)**: Two 2026-06-27 routine observations surfaced wrapper shapes the current classifier folds into `pure-kana` instead of naming as their own degenerate class:
1. **English/Latin-text-after-pipe** — `{ゴマフアザラシ|spotted seal}` (found at 06561; the same shape as the ゴマフアザラシ bug fixed in [Cleanup P9 update 2026-06-27](cleanup-backlog.md)): the right side is an English gloss, not a reading, so the live site renders "spotted seal" as ruby. The detector classifies this as `pure-kana` because the left side has no kanji, masking a real content bug. Add a rule: a wrapper whose right (reading) side contains Latin letters / an English phrase is its own `english-after-pipe` class (severity = error — it renders a gloss as furigana).
2. **Katakana-only, no pipe** — `{ビル}`, `{モード}` (found at 06308): a `{...}` span wrapping katakana with no `|` at all. Katakana never needs furigana, so these render as literal braces and break inline-link/furigana expectations. This is a special case of the 2026-06-17 *no-pipe-span* rule (enhancement above) but worth surfacing distinctly because the fix is unambiguous — drop the braces entirely (`{ビル}` → `ビル`), a provably-safe `--fix` candidate alongside the `{お{…|…}}` transform.

Both cluster in the same early-2026 06xxx creation batch and are detector-cheap (right-side character-class test; no-pipe-span test already specified).

**Enhancement 2026-06-28 (the `o-go-prefix` *suggestion* assumes お/ご is honorific — verify it forms a real word first)**: A 2026-06-28 routine systemic-fix run (06650–07300 slice) caught the detector emitting a **wrong suggested rewrite**: `{おむつ替|か}` at 07140 was flagged `o-go-prefix` with suggestion `お{むつ替|か}`, but おむつ (diaper) is a *fixed kana word*, not honorific お + むつ — the only kanji is 替, so the correct rewrap is `おむつ{替|か}`. The detector's `o-go-prefix` class blindly assumes a leading お/ご is a separable honorific prefix and lifts it outside the wrapper; when the kana after お/ご is part of the lexical stem (おむつ, おやつ, おしぼり, …) the suggestion is wrong and must be hand-corrected. The flag itself is still useful (the wrapper *is* malformed — kana inside the kanji group), but the **suggested_replacement** is unreliable for this sub-family. A fix would check whether the kana run starting at お/ご forms a real word (e.g. against a kana-word list or `word_id_lookup.json`) before proposing the honorific lift, and otherwise fall back to "lift only the leading kana that are not part of a known word." Until then this remains a per-entry-verify case (and an argument against an unguarded `o-go-prefix` `--fix` mode — the `{お{…|…}}` nested-honorific transform of the 2026-06-26 enhancement is provably safe; the bare `o-go-prefix` lift is not).

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

**Update 2026-07-10 (two more stale markers found incidentally in the priority lane — the recurrence keeps confirming the detector's value)**: A 2026-07-10 routine polish priority lane fixed two more stale-`noentry` markers as its only genuine changes among 6 examined mimetic entries — **05766 にやにや** (`noentry` → now 29117) and **05775 もぐもぐ** (a naked もごもご → `noentry`, the mirror case: a base whose entry does not yet exist, harvested as candidate C22280). The observing run explicitly flagged stale `noentry` markers whose referent now has an entry as "a distinct, tractable signal a detector could catch" — an independent restatement of this item's premise. The recurrence pattern is now well-established: these markers surface one or two at a time through incidental polishing, which is exactly why the cheap mechanical self-healing scan (re-resolve every `⟦…：noentry⟧` against `word_id_lookup.json`) would clear them in bulk instead of waiting for a polish run to stumble across each one.

**Update 2026-07-12 (three more stale markers surfaced incidentally in already-"polished" entries — "likely hundreds dictionary-wide")**: A 2026-07-12 routine polish run found **three** more stale `⟦…：noentry⟧` markers whose base now resolves in `word_id_lookup.json`, all in entries that had already been through polishing: **06484 噛み殺す → 29106**, **06731 御影石 → 29109**, and **07006 ビハインド → 29128**. The observing run made the scale estimate explicit — *"likely hundreds dictionary-wide"* — and restated this item's exact premise: a read-only detector that scans example/note `：noentry⟧` markers and reports any whose (surface/base reading) now resolves in `word_id_lookup.json` would convert these into a single cheap systemic-fix batch instead of the current one-or-two-per-run incidental drip. Reinforces the still-unbuilt `check_noentry_links.py` (unambiguous single-ID resolutions auto-swap; ambiguous readings go to the per-entry judgment queue).

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

## Related pages

- [Cleanup Backlog](cleanup-backlog.md) — patterns these tools would address
- [Entry Follow-ups](entry-followups.md) — specific entry fixes
- [Architecture and Build System](../project/architecture.md) — build script overview
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis of the tag-drift patterns that items 5 and 6 address
- [Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) — analysis of the wrapper-format patterns that items 8 and 9 address
