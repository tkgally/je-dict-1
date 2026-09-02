# je-dict-1 — Fresh Assessment of the Dictionary and the Routine (2026-09-02)

**Status**: proposal for the curator. Nothing in this document has been implemented.
**Scope**: the dictionary content as it stands (30,584 entries), the twice-daily
unattended Routine (`prompts/routine2.md`), its instruments, the generated site, and
the tooling. Every number below was measured in this session from the repository at
commit `c897557fe` unless a source is named.

---

## 1. Summary

The project is in good operational shape and the dictionary's linguistic core is sound.
The Routine runs reliably: two runs a day, every one of the last sixty pull requests
merged by the run itself within about ninety seconds of creation, no open or stranded
pull requests, no orphan branches. Glosses and readings in a thirty-entry random sample
were all correct; example sentences were natural and their translations accurate.

The problems are structural, and they come down to one thing: **the Routine is spending
its expensive judgment on mechanical work, while the mechanical work is starving the
judgment work of scale.** Concretely:

- The comprehensive-polish frontier is at entry 07065 of 30,793. It advances about six
  entries per polish run, mostly because the checklist requires hand-placing an inline
  link on every word of every example and note. At the current cadence the remaining
  23,700 entries would take well over a decade. Everything ahead of the frontier has
  zero inline links, and above ID 20000 about 96 percent of entries name synonyms or
  contrasts in their notes that have entries but are not cross-referenced.
- The verification instruments are noisy where they run and absent where the errors are.
  The external reviewer's flags ran at 17 percent precision on tags and 0 percent on
  furigana over the last two weeks, so most adjudication effort goes to rejecting noise.
  Meanwhile the reviewer never reads the notes field, which is where the two factual
  errors found in this audit sit, and where the polish pass writes most of its new prose.
- The knowledge wiki has grown to roughly 500,000 words, consumed 20 of the last 142
  runs, and is almost never consulted by the runs that change entries.
- The site, which no Routine mode ever touches, hides most of what the dictionary
  contains. Typing `eat` on the home page returns no results; typing `食べた` returns
  nothing; every page downloads an 18.7 MB search index it never uses; and the inline
  links the polish lane works hardest on are switched off by default.

The proposals in section 6 re-aim the Routine at accuracy and learner-visible depth,
mechanize the linking, cross-referencing, and formatting work with scripts under the
existing CI ratchets, fix the verification instruments, and make a few one-time
infrastructure changes that shrink each run's overhead. Section 7 lists the decisions
only the curator can make.

---

## 2. The dictionary as it stands

### 2.1 Size and shape

| Metric | Value |
|---|---|
| Entries | 30,584 (basic 801, core 1,982, general 27,781, no tier 20) |
| Created per month, 2026 | Jan 9,127 · Feb 5,276 · Mar 6,594 · Apr 5,136 · May 2,143 · Jun 1,107 · Jul 705 · Aug 496 |
| Example sentences | 119,167 (mean 3.9 per entry) |
| Cross-references | 18,977 in 11,631 entries (38 percent of entries); symmetry 42.5 percent |
| Inline word links | 278,772, in 7,123 entries (23 percent) |
| Verbs | 7,273; 33 percent carry a transitivity tag; 17 percent document ている |
| Candidate queue | 195 vetted words |

The entry-creation rate has fallen by a factor of eighteen since January. The dictionary
is now in a maintenance phase whether or not that was decided explicitly.

### 2.2 Quality: what a thirty-entry random audit found

A stratified sample of thirty entries (five ID bands, mixed parts of speech) was read in
full against the project's own skills.

**What is good.** Every gloss and reading was correct. Examples were natural and
progressively longer as the guidelines require. Notes generally teach something a
learner needs: the near-synonym distinctions (支援する vs 援助する vs 応援する vs 助ける
in 25534), the homophone warnings (家計 vs 家系 in 12287), the register notes. Newer
unpolished entries in the 25000–30000 band are often *tighter* than polished early ones.

**What is wrong.** Two outright factual errors in thirty entries, both in notes:

- **30709 山手線** (created 2026-08-20): the notes state that 内回り runs clockwise and
  外回り counterclockwise. It is the reverse. This entry passed the Routine's external
  self-check as "clean", because that check does not read notes (see 3.3).
- **19731 ものの**: the GRAMMAR section says ものの "attaches to the past tense (た-form)"
  and is only "sometimes used with present tense in more formal writing". ものの takes
  any plain predicate form; 分かっているものの and 便利なものの are entirely ordinary.

Other errors found in the sample: 13380 灯り has misplaced furigana (`{明|あか}かり`,
rendering あかかり); 01856 暖まる is tagged `transitivity: both` while its own notes say
intransitive; 00567 終わる carries an antonym reference to 始める (the pair is
終える/始める); 05446 垂直 lists 平行 as an antonym (the antonym is 水平); 15263 緩める
lists itself under SIMILAR WORDS; 00924 だから marks だからこそ as `noentry` although
27569 exists; 30705's first example translates 最後に as "at the last moment".

**Recurring structural problems, with corpus-wide counts.**

| Problem | Scale |
|---|---|
| Entries with zero inline links | 23,444 (≈ every entry above the polish frontier) |
| Entries above 20000 that name a linkable synonym/contrast in notes but have no cross-reference to it | ≈ 8,700 (97 percent of the 20000 band, 96 percent of the 25000 band) |
| Distinct ALL-CAPS notes section headers | 6,026, of which 4,770 appear in exactly one entry ("PET ADOPTION", "TYPES OF ENVELOPES"); the same concept is spelled 5–18 ways (USAGE / USAGE NOTE / USAGE NOTES / NOTE / NOTES) |
| Distinct free-text `part_of_speech` strings | 404 ("verb (godan)", "godan verb", "verb-godan", "verb", "verb, ichidan"…) |
| Semantic tag is the placeholder `general` alone | 3,554 |
| Semantic tags outside the closed list of 88 | 1,021 entries (440 distinct tags in use) |
| `politeness` missing | 6,030 (3,420 in the 25000 band; 80 percent of the newest 794) |
| `formality` missing | 1,887 |
| Verbs without a transitivity tag | 4,053 (3,915 general, 138 core) |
| Entries with kanji lacking furigana | 1,351 (863 in definition explanations, 485 in examples) |
| Entries with malformed furigana wrappers | 523; some render brokenly on the live site (10080 や: `{りんご}や{みかん}`) |
| `noentry` link markers whose word still has no entry | 3,023 distinct words |
| Notes bullets using `・` instead of `- ` | ≈ 2,500 entries |

**Polished versus unpolished.** Within the same January-2026 creation cohort, entries
behind the frontier (05000–07064) have 98.5 percent link coverage against 5 percent
ahead of it, 84 percent versus 59 percent with cross-references, and notes 44 percent
longer (845 versus 586 characters, 5 percent over the 1,200-character ceiling versus 0.3
percent). A polish pass makes an entry materially better, mainly by making it navigable
and its tags trustworthy. But it also adds sections the skills warn against (INTONATION,
HISTORICAL NOTE, a self-listing SIMILAR WORDS), and its costliest step, hand-linking
every particle (41.7 links per entry in the 00000 band), is the least visible to a
learner.

### 2.3 Growth is saturating

The 2026-09-02 candidates run probed 163 words before proposing any. Common-vocabulary
sweeps returned nothing (health/medical: 0 of 28 new). Idioms (47 percent), proverbs (48
percent), and unworked proper-noun slices (47 percent) are what remain fertile. The
"seen in entry" lane, the highest-value source because it closes the dictionary on
itself, is empty (8 words). Yet the stale-`noentry` detector lists 3,023 words that
examples and notes already use and that have no entry; many are suffixes and
number-plus-counter strings, but the list also contains ordinary headword candidates
(湯呑, 箸置, 御礼, カーナビ, あんパン, 丹頂鶴, 枕草子).

---

## 3. The Routine as it runs today

### 3.1 Cadence, reliability, and throughput

- Trigger `JE-DICT-1 comprehensive polishing` fires at `15 */12 * * *` (two runs a day)
  on `claude-opus-5`. It ran eight times a day on 2026-08-12 to 08-16 and was reduced on
  2026-08-21. A run lasts 15–25 minutes from firing to merge.
- Reliability is solved. Sixty of the last sixty pull requests merged; each merged about
  90 seconds after creation; the pre-flight sweeps found nothing to rescue in any of the
  last ten runs. The engineering that went into the atomic merge tail worked.
- Allocation over the last 30 days (142 runs, most at the old cadence):

| Mode | Runs | Entries changed | Per run |
|---|---|---|---|
| polish | 47 | 963 | 20.5 (≈ 6 frontier + ≈ 8 priority + neighbours) |
| accuracy-review | 34 | 3,053 | 89.8 (of which ≈ 2,400 were off-vocabulary tag migrations) |
| systemic-fix | 15 | 2,023 | 134.9 |
| new-entries | 24 | 468 | 19.5 |
| wiki | 20 | 0 | 0 |
| candidates | 2 | 0 | 0 |

- Frontier progress: 6,350 (Jun 30) → 6,717 (Jul 31) → 7,065 (Sep 1). The wiki's own
  66-day measurement, taken at eight runs a day, was 14.3 IDs per day against 24.1 new
  entries per day. At two runs a day both numbers shrink but the gap does not close.
  The 23,700 entries ahead of the frontier will not be reached by this lane.
- The priority lane (worst-scoring notes first) is the right idea, but the scorer ranks
  header vocabulary: 連敗 and 連勝 scored in the forties with five good sections because
  the section was headed `GRAMMAR:` instead of `COMMON PATTERNS:`. Renaming the header
  moved the score more than any content added (session log 2026-09-01, PR #3250).

### 3.2 The external verification instrument

`reviews/decisions.jsonl` records 7,948 adjudications. Precision of the external
model's flags (share applied) by dimension:

| Dimension | Last 14 days | Last 30 days | All time |
|---|---|---|---|
| tags | 17 percent (82 of 483) | 63 percent (2,697 of 4,252 — almost all deterministic off-vocabulary migrations) | 59 percent |
| gloss | 25 percent | 30 percent | 26 percent |
| translation | 35 percent | 39 percent | 29 percent |
| furigana screening | 0 percent (0 of 174) | 1.6 percent (9 of 557) | 2.2 percent |
| self-check (all dims) | 46 percent | 36 percent | 38 percent |

The noise is not random; it is three known families that the policy already rejects "by
definition": in-list narrow/broad tag substitutions, `general`-is-too-broad, and
formality flags that contradict the entry's own register sentence. The wiki's metrics
page has documented this for seven consecutive refreshes. The fix belongs in the prompt
and the runner, not in the adjudicator's patience. The furigana screener over
already-polished ranges has produced no correction in three measurement windows and
manufactures flags from its own parse failures and truncations (wiki quality-metrics
§22); it should stop running on those ranges.

### 3.3 The self-check does not read the notes

`build/review_accuracy.py` reviews exactly three dimensions: gloss, translation, tags.
The notes field, where the polish pass adds roughly 260 characters of new claims per
entry and where new entries carry their grammar and cultural explanations, is never sent
to a second model. The Yamanote Line entry above is the proof: the run that created it
reported "all 20 new entries came back clean" from `google/gemini-2.5-flash`.

### 3.4 The wiki

`planning/wiki/` holds 496,000 words (4.0 MB). The log alone is 82,700 words, the two
backlog pages 153,000 words, the quality-metrics page 35,400 words across 39 refreshes.
Wiki mode took 20 of the last 142 runs. The eight most recent non-wiki session logs
cite zero wiki pages; across August the pages other modes cited were the backlog pages
and the log itself. The research library (57 pages on lexicography and acquisition) is
a genuine asset; the maintenance loop around it is mostly writing about the project's
instruments for no reader. The valuable output of that loop, the structured
`backlog-queue.json` (96 items, 55 open, 56 batch-ready), is a few kilobytes.

### 3.5 Instruction load and run overhead

Before a run does any work it reads CLAUDE.md (5,553 words), routine2.md (4,111), the
mode prompt (2,600–3,500), and typically two or three skills (700–3,000 words each),
about 12,000–15,000 words of instructions. Then, at the end, `make build` rewrites the
site and the run commits it: a polish run of 14 entries produces a pull request with
2,903 changed files. The repository carries `docs/` (521 MB, of which 445 MB is 30,000
entry pages), `reviews/` (218 MB, 53,000 per-entry review JSON files) and a 196 MB
`.git`; every run clones all of it.

Several documents are stale: CLAUDE.md says "over 12,000 entries"; PROJECT_STATUS.md
says about 3,400 cross-references (actual 18,977) and about 53,200 examples (actual
119,167); five legacy per-task progress cursors (aspect-notes at 2317, etc.) are still
tracked.

---

## 4. The generated site

The site was rendered locally in Chromium at desktop and phone widths and exercised
with real queries. No JavaScript errors; no broken internal links in 200 sampled pages
(3,367 hrefs); every entry page has a title and meta description; sitemaps exist.
Typography and density on an entry page are good. Beyond that, the site undersells the
dictionary badly, and none of the Routine's modes ever touches it.

**Search.** The home-page box auto-detects Latin text as romaji, and there is no
"English" option, so `eat` and `beautiful` return **No results** (English lookup exists
in `search.js` but is reachable only through a hidden `?type=english` parameter). The
header box on entry pages calls any Latin word of ten letters or fewer romaji, so
`refrigerator` works and `eat` does not. Conjugated forms are not indexed and the query
is not deconjugated, so `食べた`, `食べます`, `走った` return nothing, although 7,751
entries carry full conjugation tables in their JSON. Romaji is Hepburn-only (`sinbun`,
`tuku`, `hujisan`, `zikan` find nothing). Matching is substring with no ranking, sorted
by reading: `会社` puts 印刷会社 and 親会社 ahead of 会社; `つく` returns 95 hits with the
exact match at position 45; `たべ` starts with 板塀. English mode ORs the words, so
`to eat` returns 5,702 hits. There is no pagination.

**Weight.** Every one of the 33,000 entry and kanji pages loads `search-index.js`
(18.7 MB, 3.9 MB gzipped) to power a header box that only redirects to the home page
and never reads the index. A first-time visitor arriving from Google downloads 3.9 MB
before a 12 KB entry page is done; with mid-range-phone CPU throttling the page's load
event moves from about 145 ms to about 1,040 ms and the parse costs about 30 MB of
heap, on every page, because the object literal is re-parsed even when cached.
`browse.html` is a single 11.9 MB page (238,000 DOM nodes); `random.html` is 4.6 MB and
takes 9.6 seconds to load on desktop.

**The inline links are invisible.** The ⟦⟧ links render as anchors with
`pointer-events: none`, and the "Links" toggle defaults to off. When toggled on they
get a faint dotted underline and a hover tooltip; on a phone there is no hover, so the
tooltip never appears. The 278,772 links that the polish lane spends most of its effort
producing are, by default, not visible to any learner.

**Notes and metadata presentation.** Section labels (USAGE:, COMMON COLLOCATIONS:,
SIMILAR WORDS:) render as plain uppercase text inside one light-blue box, not as
headings; long notes are half of a phone-height page with no collapsing. Transitivity,
register, and semantic tags are not shown as badges or links. The kanji index is a
26,000-pixel stream of 2,800 characters with counts and no readings or meanings, though
`kanji/*.json` already holds on'yomi, kun'yomi, and a gloss; the kanji links inside
headwords are styled to look like plain text. Furigana wrappers around katakana render
as literal braces (`{モラル}`) on 37 pages. The keigo article's table overflows a phone
screen. Entry pages show only Home/Random/About in the navigation.

**Curator tooling exposed to learners.** `advanced.html` offers Tag Statistics, Find
Missing Tags, Export CSV/JSON/Copy IDs, a stale warning ("transitivity tagging is
incomplete, ~8% coverage"; actual 44 percent), and 51 semantic-category checkboxes
whose default combination is OR (basic + food returns 2,268 entries). There are no
learner-facing lists for the basic and core tiers, which are exactly the study lists an
intermediate learner wants.

**Audio.** PROJECT_STATUS.md reports 1,028 audio files. There are none: no audio files
in the repository, no audio tags in the site, no audio code in `build/`.

`<html lang="en">` is used throughout, with a Mac/Windows-only Japanese font stack, so
Android and Linux users without Japanese fonts may see Chinese glyph variants.

---

## 5. Tooling

**Build and tests.** On 30,584 entries, `validate.py` takes 17 seconds, `update_indexes.py`
6 seconds, a full `build_flat.py` 21 seconds (peak 556 MB). The 197 unit tests pass in
three seconds, but CI never runs them and `pytest` is not in `build/requirements.txt`
(they also run under `unittest`, with no dependency). The pre-commit hook in
`.githooks/` is not installed by anything. The build is not idempotent: every
`kanji/*.json` carries a `generated` timestamp and `docs/index.html` a "last update"
line, so two consecutive builds differ in 2,805 files. That is why a 14-entry polish
pull request shows 2,903 changed files.

**The external reviewer.** `review_accuracy.py` sends one entry per request to
`google/gemini-2.5-flash` at temperature 0 with no system prompt. The payload contains
headword, reading, POS, semantic and register tags, glosses, definitions, and examples,
and omits notes, tier, domain tags, and transitivity. The prompt already tells the model
not to flag in-list tags as too broad or narrow and not to dispute "neutral", and the
model ignores both instructions: of the September tag flags, 61 percent are breadth
complaints and 19 percent register, and the in-list tag precision is 3.6 percent (4 of
106). Off-vocabulary detection, which is deterministic, is half of all tag flags ever
produced and is what makes the headline precision look acceptable. The code applies no
post-filter of any kind: it does not check that a flagged tag exists on the entry, that
a suggested replacement is in the list, or that a concern is not a breadth complaint.
The furigana screener (`review_runner.py`, same model) has 2.2 percent all-time
precision; its deep pass (`gpt-4.1` + `gemini-2.5-pro`) runs about one entry per fifteen
minutes in the scheduled environment and is effectively unusable there.

**The selector.** `routine_next.py` is a smooth weighted round-robin with health
multipliers and it works as designed. Loose ends: `runs_per_day_hint` is read by
nothing, so nothing adapts per-run targets to the change from eight runs a day to two;
`params.phase` and `params.queue_count` are emitted but unused by the prompt;
`routine_lock.py` writes a gitignored file inside a fresh container, so the lock can
never see another run and the §0b/§7 lock steps are no-ops; `metrics_snapshot.py`
tallies flags by UTC day while the 00:20 run straddles midnight.

**The priority scorer.** `score_note_quality.py` awards 30 of 100 points for the
presence of required section headers matched by string, so renaming `GRAMMAR:` to
`COMMON PATTERNS:` moves a suru-verb entry from 59 to 89; 1,142 suru-verb entries in the
first 12,000 lose all 30 points this way, which is why the bottom of the priority list
is a solid block of them (18773, 18775, 18776 … all at 32). Nothing in the score measures
content. A second bug: `prioritize_polishing.py` has its own bare-kanji detector that
never received the inline-link fix `score_note_quality.py` has, so 6,757 entries are
falsely flagged and 298 of the top 300 lines of `polishing/priority/furigana.txt` are
false positives.

**Dead code.** Ten scripts in `build/` are referenced by nothing (`install_hooks.py`,
`strip_conjugation_notes.py`, `fix_register_trailers.py`, `fix_duplicate_ids.py`,
`cleanup_candidates.py`, `extract_kanji_from_entries.py`, `resolve_links.py`,
`extract_references.py`, `brainstorm_candidates.py`, `check_tag_consistency.py`); the
entries-directory loader is re-implemented in at least six scripts; there are three
bare-kanji implementations.

---

## 6. Proposals

Ranked within each group by value for effort. "Mechanical" means a script under the
existing CI ratchets with a sampled model spot check, following the project's own rule
that a mechanical transform must be one that provably cannot introduce an error or is
verified per entry.

### A. Re-aim the Routine

**A1. Change what a polish run is for.** Once linking and cross-reference harvesting
are mechanized (B1, B2), a polish run should read 25–40 entries and do only the
judgment work: fix errors, add the one contrast or warning a learner needs, trim
padding, set the tags. Cap notes growth per pass: no new section unless the POS
template lacks it; no new sense unless examples show a distinct meaning. Drop the
"full inline link coverage" tier-1 requirement from the checklist; replace it with
"review the auto-linker's flagged tokens for this entry".

**A2. Re-rank the priority lane on substance, not header names.** Rank by: accuracy
flags outstanding, never modified since creation, verb without transitivity, no
cross-references while notes name linkable words, `politeness`/`formality` missing,
notes shorter than 300 characters, notes over the ceiling. Fix the header matching in
`score_note_quality.py` with a synonym table (see B4) and add content signals (Japanese
pattern lines, per-section body length). Fix the bare-kanji detector in
`prioritize_polishing.py` (298 of the top 300 furigana-priority lines are false
positives today) and regenerate the priority files.

**A3. Reweight the modes.** Suggested `routine-config.json` weights: polish 0.30,
accuracy-review 0.30, systemic-fix 0.25, new-entries 0.10, candidates 0.05
(self-suppressing), wiki 0.00 by weight but triggered by a nudge when unharvested
observations exceed 40 lines, capped at one run per week. Systemic-fix has the highest
entries-per-run leverage of any mode (135) and a 55-item backlog.

**A4. Slim the instruction load and remove the no-ops.** Move the command catalog out
of CLAUDE.md into a reference file it points to; move the MCP pull-request/CI/merge
mechanics into one shared section that the mode prompts reference instead of
restating; delete the duplicated pre-flight text from `comprehensive_polish.md` and
`newentries.md`; drop the lock steps (the lock file is gitignored in a fresh container
and can never be seen by another run) and the unused selector params; make the
per-run targets scale with the real cadence or delete `runs_per_day_hint`. Target:
under 6,000 words of instructions before work starts. A stronger model needs fewer
guardrails, not more.

**A5. Switch the trigger to the current model.** The trigger runs `claude-opus-5`.
This is a Routine setting, not a repository change.

### B. Mechanize the mechanical

**B1. Deterministic inline linker (`build/auto_link.py`).** Link a token automatically
only when it resolves to exactly one entry: furigana-wrapped kanji words by
headword-plus-reading, katakana runs by headword, particles and function words from a
fixed table, conjugated verbs and adjectives through the conjugation tables the entries
already carry (7,269 verbs have every form spelled out). Everything else is left
unlinked or marked for review. Roll out in 500-entry blocks through systemic-fix runs,
gated by `check_link_targets.py` and `check_link_baseform.py --gate` in CI, with the §4
spot check on a sample. Recall will not be complete; precision will be near-total, and
23,000 entries become navigable in weeks instead of a decade. Option: add a tokenizer
(`fugashi` + `unidic-lite`) for kana-run segmentation; without it the linker stays
tokenizer-free and lower-recall. Curator decision (7.3).

**B2. Harvest cross-references from notes.** `build/extract_references.py` already
parses SIMILAR WORDS / RELATED / CONTRAST bullets. Run it in dry-run over the ≈ 8,700
entries above 20000 that name linkable words, take only bullets whose headword and
reading match exactly one entry, assign the reference type from the header, and let
the existing symmetry checker add back-links. A model pass confirms the labels. This is
the single highest-leverage change for a learner: it is what turns 30,000 pages into a
network.

**B3. Ratchet the metadata layer in CI.** Canonicalize the 404 `part_of_speech` strings
through a mapping table; forbid missing `politeness`/`formality` on any entry touched by
a run; require `transitivity` on godan/ichidan verbs touched by a run; add a
no-pipe-brace furigana check. Script-fix the 523 malformed-furigana entries and the 20
tierless entries in one systemic-fix run.

**B4. Freeze the notes header vocabulary.** About fifteen canonical headers with a
rename table (USAGE NOTE(S)/NOTE(S) → USAGE; RELATED/RELATED TERMS → RELATED WORDS;
COLLOCATIONS → COMMON COLLOCATIONS; GRAMMAR → COMMON PATTERNS for verbs) applied
mechanically, singleton topical headers folded into USAGE, `・` bullets normalized to
`- `, and a CI warning for any new header outside the list. This also repairs the
priority scorer for free.

**B5. Fill the transitivity gap with a cheap classifier plus adjudication.** Send the
4,053 untagged verbs to the external reviewer with a single question (transitive,
intransitive, both, with the pair verb if one exists); apply in batches with the
adjudication ledger. Transitivity is nearly deterministic for most verbs and is the
top item on the project's own v2 priority list.

### C. Fix the verification instruments

**C1. Rebuild the tags dimension and post-filter in code.** The prose prohibitions have
hit their ceiling with this model; the fix is structural. (a) Move off-vocabulary
detection out of the model entirely (`validate_tags.py` / `check_tag_drift.py` already
know the list and the migration map). (b) Ask for a closed per-tag verdict
(`keep` / `wrong-category`, where breadth is never a reason and the five fallback tags
are always `keep`) instead of free-text issues. (c) Post-filter in `review_accuracy.py`:
drop concerns matching too-broad/too-narrow/too-vague on in-list tags, drop flags naming
a tag the entry does not carry, drop out-of-list suggestions, drop `warn` on tags, and
accept a register flag only if the notes were in the payload and the model quotes the
sentence it contradicts. (d) Tag a regex-assigned `family` on every issue so precision
is computable without free-text notes. (e) Optionally require two cheap models to agree
on a tag flag. Expected effect: about 80 percent fewer tag flags, precision from
≈ 4 percent to a usable level, and adjudication effort per accuracy run cut enough that
each run can cover 1,000+ entries instead of 500.

**C2. Add a notes dimension.** Ask the second model for factual or grammatical claims in
the notes that are wrong, with the claim quoted, error severity only, no style. Run it
in the self-check for every entry a run created or rewrote, and in the accuracy sweep.
Consider two cheap models with agreement for this dimension, since it is where a
confident single-model verdict is least trustworthy.

**C3. Retire the furigana screening pass over ranges already screened or polished** and
fix the parse-failure-counted-as-flag defect. Keep it only for never-screened IDs.

**C4. Verify neighbours too.** The self-check already found that four of six applied
fixes in one run were pre-existing errors in neighbour entries opened only to add a
back-link. Send every touched entry, and a random sample of untouched entries from the
same block, to the check.

### D. Growth policy

**D1. Make new-entries an internal-closure mode.** Mine the 3,023 unresolved `noentry`
words (after the probe-first duplicate check) and the words the accuracy sweep notices,
rather than brainstormed lenses. Keep proper nouns, idioms, and proverbs as a small
curated stream if the curator wants them (7.1).

### E. Site (one-time work, not Routine work)

These are one or two interactive sessions of build-script work, and they change what a
learner experiences more than any month of Routine runs.

**E1. Stop loading the search index on entry and kanji pages.** One line in
`build/html_utils.py` (`generate_header_search_script`): the header box only redirects
to the home page. Removes 3.9 MB and about a second of phone CPU from every page.

**E2. Make English lookup real and rank results.** Add an English radio; on auto-detect
run romaji and English both; drop the ten-letter heuristic in the header script; rank
exact headword or reading first, then prefix, then substring; paginate; AND the words
in English mode.

**E3. Accept conjugated forms and non-Hepburn romaji.** Either index the
`conjugation.forms` the entries already carry (about 130,000 extra keys) or deconjugate
the query in JavaScript, and normalize `si/tu/hu/zi/ti` and macrons. `食べた → 食べる` is
the single most common intermediate-learner search and currently returns nothing.

**E4. Split the index.** A small headword/reading/romaji/gloss shard for the home page
(about 2 MB); the per-entry tag data only for the advanced page, or per-kana shards
loaded on demand.

**E5. Show what the entries already contain.** Turn word links on by default (or on
touch devices) with a visible underline; render notes labels as subheadings; show
transitivity, register, and semantic tags as badges that link to lists; print
on'yomi/kun'yomi/gloss on the kanji pages; make headword kanji links look clickable;
fix the `{カタカナ}` brace artifacts.

**E6. Learner-facing navigation.** Full navigation on entry pages; static study lists
for the basic and core tiers and for semantic categories; move Pending, Tag
Statistics, Find Missing Tags, and the exports off the public interface; fix the stale
transitivity warning; default the advanced page to AND.

**E7. Mobile polish.** Scrollable containers for article tables and conjugation
tables; `lang="ja"` on Japanese spans with a Noto Sans JP fallback; paginate
`browse.html`; cap `random.html`; add articles, `kanji.html`, and `recent.html` to the
pages sitemap.

**E8. Audio.** Either remove the claim from PROJECT_STATUS.md or add a zero-cost play
button per example using the browser's `speechSynthesis` (ja-JP). Real recorded audio is
a separate project.

### F. Infrastructure and housekeeping

**F1. Build the site in GitHub Actions instead of in the run.** Deploy Pages from an
Actions workflow that runs `make build` on every push to `main`. The Routine then
commits only entries, indexes, and logs; pull requests shrink from thousands of files
to dozens; `make build` output stops consuming run context; `docs/` leaves the working
tree (521 MB). Keep `entries_index.json`, `word_id_lookup.json`, and `kanji/` committed
since tools read them. Optional and destructive: rewrite history once to drop old
`docs/` blobs from `.git` (7.4).

**F2. Make the build idempotent and compact `reviews/`.** Drop the per-file `generated`
timestamp from `kanji/*.json` and the "last update" line from `docs/index.html` (or
derive them from the newest entry's `modified`), so a run's pull request shows only the
files it changed. The 53,000 per-entry review JSON files (218 MB) are append-only
artifacts nobody reads twice: keep one JSONL per run plus `decisions.jsonl`, or move the
per-entry files out of the repository.

**F3. Run the tests in CI and install the hook.** Add a test step
(`python3 -m unittest discover -s build/tests -t .`, under a second) to
`validate.yml` and a `make test` target; add a Makefile target that sets
`core.hooksPath` so the pre-commit validator is actually active in interactive sessions.

**F4. Fix the stale documents and archive dead code.** CLAUDE.md entry count and command
catalog; PROJECT_STATUS.md counts and the audio claim; delete or archive the five legacy
progress cursors, the deprecated prompts they belong to, and the ten unreferenced
scripts in `build/`.

---

## 7. Decisions needed from the curator

1. **Growth.** Continue adding idioms, proverbs, and proper nouns at 20 per run, or
   shift new entries to internal closure only (D1)? My recommendation: internal closure
   plus a small curated stream.
2. **Wiki.** Keep the maintenance loop at 15 percent of runs, or cut it to
   observation-triggered harvesting with the research library kept static (A3)? My
   recommendation: cut it.
3. **Tokenizer dependency.** Allow `fugashi` + `unidic-lite` in `build/requirements.txt`
   for the auto-linker (B1), or keep the linker tokenizer-free? My recommendation: allow
   it; the gain in recall on kana runs is large and the dependency is pure-Python wheels.
4. **Site build in CI and history rewrite** (F1). Changing the Pages source is
   reversible; rewriting history is not.
5. **Model.** Switch the trigger to the current model (A5).
6. **Notes growth cap** (A1) is a style decision: it changes what a polished entry looks
   like.
7. **Header vocabulary** (B4): the canonical list is an editorial choice; I will propose
   one, but it should be approved before the rename runs.

---

## 8. Suggested sequencing

**Phase 1 (one interactive session): instruments and re-aim.** C1, C2, C3, A2, A3, A4,
F2, F3, F4, and the metadata ratchets in B3. These change no entry content and make
every subsequent run more productive. E1 (one line) belongs here too.

**Phase 2 (one or two sessions plus systemic-fix runs): mechanization.** B4 header
normalization, B2 cross-reference harvest, B1 auto-linker, B5 transitivity — each
rolled out in blocks through the systemic-fix backlog with the §4 spot check.

**Phase 3 (one session each): site and infrastructure.** The rest of section E, then
F1.

After phase 2 the polish mode becomes what its name says, and the accuracy sweep
becomes the whole-dictionary correctness instrument it was designed to be. After phase
3 a learner can find 食べる by typing 食べた or `eat`, and can see the links the
Routine has been building for months.
