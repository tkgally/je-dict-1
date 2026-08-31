# Inline Link Integrity

**Last updated**: 2026-08-15 (**replaced the two-day growth delta with 66 days of rate data**:
across 516 Routine runs the frontier advances **14.3 IDs/day** against **24.1 entries/day** of
growth, a net **+9.8/day**, and the gap has not closed in a single 7-, 14-, 30- or 66-day window.
Zero-link re-measured at **23,444** against **23,508** entries ahead of the frontier — the two
populations are now the same set to within 64 entries. Also corrected the eighth and ninth
"creation batch skipped linking" filings, which were reading the cliff edge at 06900–06999 from
inside the frontier's own bucket.)

Prior 2026-08-09 (re-measured the zero-link population at **23,404** with the
frontier at 06845: it **grew by 110 while the frontier advanced 122 IDs**, which is the
frontier-versus-growth gap expressed on the link metric for the first time. Separated out the
**55 zero-link entries that sit *behind* the frontier** — the actionable residue the "77% of
the dictionary" headline hides — and filed them as Cleanup P50.)

Prior 2026-08-07 (measured the braced-base-form class, which turned out to be
36 entries and 226 instances — one small cohort, not a sweep — and added the two
*wrong-target* classes that three runs surfaced in the first week of August)

## Overview

Inline word links — `⟦surface→base：entry_id⟧` inside example sentences and notes — are
je-dict-1's densest piece of internal machinery. There are **265,750** of them across the
corpus, roughly nine per entry that has any, and they are the only mechanism by which a
learner reading an example can jump to the word that puzzles them without retyping it.

They are also the project's least-instrumented data. Furigana has four checkers and two
OpenRouter passes; semantic tags have a closed vocabulary, a deterministic diff, and a paid
reviewer. Inline links have exactly one gate in CI (`check_link_targets.py`: does the target
exist?) and one detector added in July (`check_link_baseform.py`: is the target the base
form's own entry?). Everything else about them is unmeasured — which is why six separate
defect and coverage classes have been discovered independently by six different runs over
five weeks, each one paying the discovery cost again.

This page collects those classes, gives each a measured scope, and separates the two that
are batch-ready from the four that are not.

## The six classes

| Class | Scope | Nature | Where filed |
|---|---|---|---|
| Dead `target_id` (points at no entry) | 292 → gated | Defect | [Cleanup P27](../ideas/cleanup-backlog.md#priority-27-dead-inline-link-target-ids), CI ratchet |
| Base form written with furigana braces | **36 entries / 226 instances** | Defect, provably safe | [Cleanup P24](../ideas/cleanup-backlog.md#priority-24-inline-link-base-forms-written-with-furigana-braces) |
| Base form written in kana, not dictionary form | 3,567 | Cosmetic/lookup | [Cleanup P32](../ideas/cleanup-backlog.md#priority-32-inline-link-base-forms-written-in-kana-instead-of-the-dictionary-form) |
| Target disagrees with the base form (homophone substitution) | 405 → 318 | Defect, per-entry | `link-target-baseform-disagreement` |
| **Stale `noentry` markers** | **3,809** (2,887 unique-target; 447 never correct) | **Defect, batch-ready** | [Cleanup P35](../ideas/cleanup-backlog.md) *(new, this page's measurement)* |
| **Entries with zero links** | **23,444** (of which **55** behind the frontier) | **Not a defect above the frontier — see below**; the 55 are | *(structural; do not file)* + [Cleanup P50](../ideas/cleanup-backlog.md#priority-50-zero-links-anywhere-behind-the-frontier-55-entries--the-other-half-of-p46) |
| `Xする` base label on a bare-noun target | 441 (267 decidable) | Convention gap, not a defect | [Cleanup informational](../ideas/cleanup-backlog.md#informational-inline-link-base-forms-labelled-xする-while-targeting-the-bare-noun-entry-441-links) |

The two bold rows were both proposed as backlog items by 2026-07-31 / 2026-08-01 polish runs
on the strength of small samples. Measuring them against the corpus before filing changed
both, in opposite directions: one is three to ten times larger than estimated and highly
actionable, and one should not be filed at all.

## Stale `noentry` markers — 3,797 occurrences, and mostly mechanical

A polishing run that encounters a word with no entry writes `⟦水→水：noentry⟧`. The marker is
correct when written. Then a later `new-entries` run creates that word, and nothing sweeps
back. The link stays inert, and the reader sees plain text where a working link now exists.

Dictionary-wide, of **7,320** `noentry` links, **3,797 (52%) now resolve** to a real entry.
Stratified by how confidently they resolve:

| Class | Count | Confidence | Example |
|---|---|---|---|
| A1 — headword match, multi-char, unique target | **2,123** | High | 理容院 → `27288_riyouin` |
| A2 — katakana headword, unique target | **764** | Highest (no reading ambiguity) | ボストンバッグ → `27285_bosutonbaggu` |
| A3 — headword match, multi-char, **ambiguous** | 27 | Needs sense judgment | 明日 → `00501_ashita` *or* `27453_myounichi` |
| B — headword match, **single character** | 498 | Low — homograph trap | 角 → `02158_tsuno` (つの), but the link's 角 is usually かど |
| C — reading-only match, multi-char | 337 | Medium | たち → `01551_tachi` (達) — often a suffix, not the word |
| D — reading-only match, single character | 48 | Very low | ば → `03699_ba` (場) — the link's ば is the conditional particle |

**A1 + A2 = 2,887 occurrences with exactly one candidate entry and a full headword match.**
That is the batch: the largest provably-safe, user-visible item on the backlog, and one where
the evidence needed to accept each fix is entirely inside the link itself.

Classes B, C, and D (883 occurrences) are the same trap as the base-form-disagreement item's
family (b) — a match on a short or reading-only key is as likely to be a homograph as the
word. They need per-entry verification and should not ride along with the batch.

### Where the staleness comes from

Grouping A-class links by the ID band of the entry that now exists:

| Band of the *target* entry | Stale links pointing at it |
|---|---|
| 00000–25999 | 441 |
| 26000–27999 | 662 |
| 28000–29999 | **1,678** |
| 30000+ | 133 |

**85% of the staleness was created by entry creation in the last few months**, not by ancient
drift. This is a live leak, not a historical residue: every `new-entries` run adds to it, and
the population will keep growing at roughly the rate the dictionary grows.

That makes [Tooling 19](../ideas/tooling-backlog.md#19-stale-noentry-inline-link-detector)'s
incremental half — `manage_candidates.py sync` already computes, for free, the exact set of
words that just crossed from "no entry" to "has an entry" — the part that matters most. It
closes the source. The 2,887-link sweep is the one-time backlog behind it, and doing the
sweep without the hook buys a few months.

### …and 447 of them were never correct in the first place

"Stale" assumes the marker was right when it was written. A 2026-08-02 polish run found a
counterexample sharp enough to test: `01004_tsu` marked 一二三四五六八九 as `noentry` when all
eight are **basic-tier entries created in the project's first week** — months before the link.
It proposed a separate "false positive" detector.

The test is one date comparison. If a marker's resolved target was created *before the entry the
marker sits in*, the target already existed at every moment the link could have been written:

| | Markers | Entries |
|---|---|---|
| Target predates the source entry — **wrong when written** | **447** | 317 |
| Target postdates the source entry — genuinely went stale | 3,362 | 1,944 |

447 is a **floor, not an estimate**: a marker written during a later polish pass against a target
created after the source entry is counted as "stale" here even though it was also wrong when
written. The true figure lies between 447 and 3,809.

The two subclasses behave in opposite directions, which is the reason to keep them apart:

- **The stale class is growing.** 85% of it points at bands 26000+, and every `new-entries` run
  adds more.
- **The wrong-when-written class is closed.** By ID band it runs 12 / 13 / 35 / 78 / 97 / 45 / 21
  from 00000 up to 06999, and **zero above 07000** — because above the polish frontier there are
  no inline links at all. It was produced by one pass, the January 2026 linking sweep over the
  earliest entries, and that pass is over.

The failure mode is legible in the samples: the linker looked up the **surface form in the
sentence** rather than the dictionary form — 形 → `02193_katachi`, 間 → `00914_aida`, 家 →
`00612_ie`, 本 → `00111_hon`, 都 → `03747_miyako`. Every one an extremely common word whose entry
had existed from the start. It is the same root cause as classes B/C/D above (a key that is a
surface string rather than a lemma), showing up at write time instead of at resolve time.

**No second detector is warranted.** 301 of the 447 meet the same A1/A2 criterion as the main
batch, the queue is the same queue, and the fix is the same token substitution. What is worth
emitting is a `wrong_when_written` column, because it removes a check: a marker whose target
predates it needs no "has the sense drifted since?" judgment — nothing changed, the link was
simply wrong.

### A third question the same scan raises: `Xする` labels on noun entries

441 links declare a base form ending in `する` while targeting the bare noun entry
(`→発生する：03133_hassei`), against 822 that target an actual `Xする` entry. A 2026-08-02 polish
run asked which convention wins. The measurement says the question cannot be settled by a sweep:
**267 of the 441 have a separate `Xする` entry available, but 174 do not** — for those the noun
entry is the only target that exists, so a rule of "the label must match the target's headword"
would delete a する the sentence actually contains. Filed as a
[Cleanup informational](../ideas/cleanup-backlog.md#informational-inline-link-base-forms-labelled-xする-while-targeting-the-bare-noun-entry-441-links)
with the three coherent options; only the "prefer the する entry where one exists" reading is a
sweep, and it is a 267-link one.

## Zero-link entries — 23,444, and *not* a defect

Two polish runs (2026-07-31, 2026-08-01) reported that a frontier block "was created with
zero inline links … consistent with a creation batch that predates the inline-link
requirement," and proposed both a `check_link_coverage.py` detector and a targeted backfill.

The corpus says there is no batch. Zero-link entries by ID band (re-measured 2026-08-09;
the 2026-08-07 figures are in parentheses where they moved):

| Band | Entries | Zero-link | % | Links in band |
|---|---|---|---|---|
| 00000–01999 | 1,989 | 0 | 0.0% | 86,851 |
| 02000–03999 | 1,989 | 23 | 1.2% | 80,030 |
| 04000–05999 | 1,987 | 3 | 0.2% | 72,829 |
| 06000–07999 | 1,918 | **1,084** (1,202) | 56.5% | 30,111 |
| 08000–09999 | 1,995 | 1,857 | 93.1% | 1,055 |
| 10000–29999 | 19,912 | 19,911 | ~100% | 11 |
| 30000+ | **526** (298) | **526** | 100% | 0 |

This is not a batch signature. It is a **cliff at the comprehensive-polish frontier**, which
sits at 06845 — in the middle of the one band that is partially linked. Essentially every
link in the dictionary lives below ID 08000, and essentially every entry above it has none.

**The two-day delta is the whole strategic argument in miniature.** Between the two
measurements the frontier advanced 122 IDs and the 06000–07999 band shed 118 zero-link
entries — the lane working exactly as designed. Over the same window the 30000+ band grew from
298 entries to 526, all of them unlinked. Net movement in the total: **23,294 → 23,404, up by
110 while the lane was running at full speed.** The linking deficit is not merely failing to
shrink; it is growing, and it would still be growing if the frontier ran twice as fast.

Inline links are not added at creation time at all; `CLAUDE.md` says so explicitly ("Never
add inline word links (⟦...⟧) during entry creation — those are added in a separate polishing
step"). So the observation's premise — "this block predates the requirement" — inverts the
causality. The block has no links because the polish frontier has not reached it. **The
frontier lane *is* the backfill.**

The consequence is worth stating plainly, because it is a strategic fact rather than a
cleanup item:

- 23,404 entries are unlinked.
- The frontier lane advances **4–8 entries per Routine run** when it hits unlinked entries
  (06705–06712 in one run, 06713–06716 in another, 06717–06722 in a third).
- At 6 entries/run and ~5 runs/day, the frontier reaches ID 30,000 in roughly **two years**,
  during which the dictionary will have grown by more entries than the lane linked.

The frontier lane cannot close this gap, and no detector will change that — a
`check_link_coverage.py` would faithfully report "77% of the dictionary," which is already
known. What could change it is
[Tooling 49](../ideas/tooling-backlog.md#49-read-only-inline-link-suggester-propose--never-write),
the read-only link *suggester*: the measured cost split on a linking slot is roughly 90%
dictionary lookup and 10% editorial judgment, so a tool that proposes `⟦…⟧` candidates
without writing them attacks the 90%.

Until that exists, the honest framing is that inline links are a **feature of the polished
below-frontier corpus**, not of the dictionary — and the curator may want to decide that
deliberately rather than by accumulation.

Both 2026-08-02 polish runs filed the block a fourth and fifth time (06739–06744 and 06745–06750,
each proposing a coverage detector). One of them sharpened the strategic point rather than
repeating it, and the distinction matters for costing Tooling 49: **below the frontier the
deficit is partial coverage needing completion; above it there is no coverage at all, needing
creation from scratch.** A partially-linked entry gives the linker a worked example of its own
conventions — which words the previous pass considered worth linking, which base forms it chose —
and the remaining decisions are marginal. An entry with zero links offers none of that, so every
token is an open question. The 4–8 entries/run figure above is measured on exactly this expensive
case, which is why it is the right number to plan against, and why a suggester that pre-resolves
the lookups changes the economics more above the frontier than below it.

### The 55 that *are* actionable — filtering the same scan by the frontier

Two more runs filed the detector on 2026-08-09 (sixth and seventh rediscovery), and this time
the measurement was split at the frontier rather than reported as a total. That single filter
turns a non-item into a real queue:

| Population | Entries | Meaning |
|---|---|---|
| Zero-link **above** `next: 06845` | 23,349 | the frontier position, restated |
| Zero-link **below** `next: 06845` | **55** | work the frontier reached and did not do |

The 55 are the strict sibling of [Cleanup P46](../ideas/cleanup-backlog.md#priority-46-notes-fully-linked-examples-completely-bare-33-entries--behind-the-frontier)
(notes linked, examples bare). P46 is half-finished linking; this is un-started linking in
entries the cursor has already passed. **Neither will ever be revisited**, because the
comprehensive cursor only moves forward — which is the entire reason a below-frontier filter
makes a "do not file" detector worth running.

They are also not scattered. 21 of the 55 are one contiguous run of single-kanji `〜` entries
(03949–03969), 9 are an anatomy block (06006–06014), 7 an i-adjective block (06670–06676), and
the rest fall into four smaller runs plus six isolates. Block shape has diagnostic value here:
P46's blocks end abruptly mid-range, which reads as a session running out of context, whereas
the 03949–03969 block is *complete* — every member of a creation batch skipped together. The
likely cause is different: these entries' headwords are bound morphemes (空〜, 元〜, 後〜), so a
linking pass that judges "is the headword linkable" rather than "are the examples linkable"
would skip the whole batch consistently. Their examples are ordinary and full of linkable
vocabulary (03949's contain 空港, 予約, 迎える, 行く).

The operational lesson generalises past this class: **when a coverage detector returns most of
the dictionary, the useful query is almost always the same detector intersected with a cursor
position.** "77% of entries are unlinked" is a restatement of the schedule; "55 entries the
schedule already passed are unlinked" is a bug report.

### The gap has never once closed — 66 days of rate data (measured 2026-08-15)

Every previous version of this section argued the growth point from a **two-day delta**
(23,294 → 23,404 while the frontier advanced 122 IDs). Two days is not enough to distinguish a
trend from a busy Tuesday, and the argument deserved better evidence than it had. It now has it:
`pipeline/metrics-history.jsonl` has recorded `comprehensive_next` and `entries_total` on every
Routine run since 2026-06-10, which is **516 runs over 66 days**.

| Window | Frontier | Dictionary | Net gap |
|---|---|---|---|
| Last 7 days | +16.1 IDs/day | +22.8 entries/day | **+6.7/day** |
| Last 14 days | +15.5 IDs/day | +26.5 entries/day | **+11.0/day** |
| Last 30 days | +14.4 IDs/day | +25.8 entries/day | **+11.4/day** |
| **Full 66 days** | **+14.3 IDs/day** | **+24.1 entries/day** | **+9.8/day** |

**The dictionary has grown faster than the frontier has advanced in every window measured, and
the ratio is stable at roughly 3:5.** This is no longer an inference from a delta; it is the
shape of the whole series. The frontier is not slowly catching up, not holding even, and not
noisy around break-even — it loses about ten entries of ground per day, and has done so
continuously for two months.

The link metric confirms it independently. Re-measured 2026-08-15 with the frontier at **06936**:

| | 2026-08-09 | 2026-08-15 | change |
|---|---|---|---|
| Frontier (`comprehensive_next`) | 06845 | 06936 | +91 |
| Zero-link entries | 23,404 | **23,444** | **+40** |
| Entries ahead of the frontier | — | 23,508 | — |

The frontier advanced 91 IDs and the zero-link population still grew by 40, because ~130 new
entries arrived unlinked in the same window. And the two right-hand numbers are the finding:
**23,444 zero-link entries against 23,508 entries ahead of the frontier — a difference of 64.**
Zero-link status and above-the-frontier status are now very nearly the same set. Inline linking
is not a property of the dictionary that happens to be incomplete; it is a property of the
polished prefix, and its boundary *is* the cursor.

Per-bucket, re-measured 2026-08-15, the cliff is sharper than the older band table suggested,
because 500-entry buckets resolve it and 2,000-entry bands blur it:

| Bucket | Entries | Zero-link |
|---|---|---|
| 06000–06499 | 500 | 3% |
| 06500–06999 | 500 | 15% |
| **06900–06999** (the frontier's own bucket) | 100 | **59%** |
| 07000–07499 | 418 | 98% |
| 07500–09499 | 2,000 | 95–100% |
| 09500–09999 | 495 | 77% |
| 10000–30653 | 20,900 | **100.0%** (one entry has links) |

**This is what the two "creation batch" filings of 2026-08-14 were looking at.** Both polish runs
that window reported the same thing — that 06926–06929 and 06930–06935 have *zero* links in both
examples and notes, "not partial coverage, none at all", and proposed a targeted sweep of the
06900–07000 band on the theory that one creation batch skipped linking. The frontier sat at 06936
when they filed. They were standing on the cliff edge and describing the drop: 59% of the 06900
bucket is unlinked because the cursor is *inside* that bucket, and the 97–100% they would have
found one bucket further on has nothing to do with any batch. This is the eighth and ninth
rediscovery of the same non-item, and the first pair to land close enough to the cursor that the
band they proposed sweeping is genuinely bounded — which is exactly why it looked like a batch.

The corrected framing for future runs: **a zero-link report is only interesting below the
cursor.** Above it, the number is the schedule. The one below-cursor queue remains the 55 of
`zero-link-behind-frontier`, plus P46's 33.

What changes with better data is not the diagnosis but its urgency. The 2026-08-09 conclusion —
that the frontier lane cannot close this gap and that
[Tooling 49](../ideas/tooling-backlog.md#49-read-only-inline-link-suggester-propose--never-write)
(the read-only link suggester) is the only lever that would — was reasoned from two days and
happened to be right. At the measured 66-day rates the "roughly two years to reach ID 30,000"
estimate is optimistic in a specific way: it treats ID 30,000 as a fixed target. The target moves
at 24 entries/day while the frontier closes at 14, so **at current rates the frontier does not
converge on the end of the dictionary at all.** That is a curator-level fact about what the
polish lane is for, and it should be decided deliberately: either the lane is a quality pass over
a permanently-bounded prefix, or something has to change the 3:5 ratio — a faster linker
(Tooling 49), a linking step at creation time (which `CLAUDE.md` currently forbids by design), or
a slower growth rate.

## The unlinkable residue: Japanese that no rule can currently handle

The six classes above are all *defects* — a link that exists and is wrong, or a link that should
exist and doesn't. There is a seventh thing, and it is not a defect: **Japanese text that both
project rules apply to and neither rule can satisfy.**

The rules are (1) every kanji carries furigana, and (2) every Japanese word in an example or note
is either inline-linked or marked `noentry`. Together they assume that every Japanese span in the
corpus is a *lookup-able lexical item* — something that has, or could have, an entry. Three
independent runs on 2026-08-01 hit spans where that assumption fails, and each had to invent a
treatment on the spot:

| Case | Why both rules fail | Measured scope |
|---|---|---|
| **Bound morphemes** — 今-, 毎-, 来-, 義- | Not a word, so no entry and no candidate is warranted. Bare `毎` trips `find_missing_furigana.py`; `{毎|まい}` satisfies the furigana rule but leaves naked Japanese that rule (2) then demands a link for. | 8 of the 17 entries one polish run touched |
| **Copula and auxiliary inflections** — `で、`, `ではありません` | The lemma has an entry (`09485_desu`) but the inflected form is grammar, not vocabulary; linking it would assert a lemma the reader didn't meet. | `⟦で→です：09485_desu⟧` occurs **0** times corpus-wide; `→です` in any form, **3** times — against **2,384** links to plain `だ`. **225** polished examples (0.6% of the 36,087 that carry any link) contain an unlinked て-form `で、`; 24 contain an unlinked `ではない`/`ではありません`/`じゃない`. |
| **Morphemes whose surface form is already occupied** — prohibitive sentence-final な | It genuinely has no entry, and `manage_candidates.py` **refuses the candidate** because `09497_na` (attributive copula な) holds the (surface, reading) key. So it cannot be linked and cannot be queued. | 1 confirmed (06737); the blocking mechanism is [Tooling 41](../ideas/tooling-backlog.md#41-manage_candidatespy-cannot-queue-a-homograph--the-duplicate-check-is-surface-reading-not-surface-reading-sense) |
| **Metalinguistic mentions** — "the kanji 今", "Different from 雨 (ame, rain)" | The glyph is being *mentioned*, not used. Furigana-wrapping asserts a reading the prose isn't claiming; linking asserts a word the prose isn't using. | Recurrent; filed as [Tooling 62](../ideas/tooling-backlog.md#62-find_missing_furiganapy-cannot-tell-wrap-this-from-rewrite-this) |

**The scope numbers are the useful part, and they point the opposite way from the frustration.**
The copula gap — the one a run described as "the full-coverage tier-1 rule technically fails on
any sentence containing them" — is 0.6% of polished examples. None of these classes is a sweep.
What they cost is not corpus damage but **rediscovery**: every polishing session that meets an
affix in a note re-derives the same reasoning, and three of the four have now been re-derived at
least twice by different runs. That cost is unbounded and recurs forever; the fix is four lines in
a skill file and costs nothing after that.

The treatments the runs converged on independently are consistent, which is itself evidence they
are right:

- **Affixes** — refer to the affix by its *reading* in English prose ("the まい- prefix", "the ぎ-
  prefix") and drop the glyph. Both rules are satisfied vacuously, and it reads fine because the
  series list immediately below always shows the kanji in context.
- **Copula and auxiliary inflections** — exempt. This is already the de-facto rule (2,384 links to
  `だ`, three to `です`, none to the て-form), and it matches the existing decision recorded for
  `ている`, which is `noentry` in 37 ASPECT notes rather than linked to a lemma page.
- **Blocked homographs** — `noentry` is the correct marker, and the real fix is sense-keyed
  candidates (Tooling 41), not a per-entry workaround.
- **Metalinguistic mentions** — rewrite the prose, never wrap.

All four are skill-level conventions, which a `wiki` run may not write. They are recorded here and
routed to the curator as one decision rather than four, because they share a single cause: **the
link rule was written for words, and the corpus contains Japanese that is not a word.**

## Braced base forms: 226 instances, but only 36 files — measured 2026-08-07

A 2026-08-07 polish run reported "inline-link base forms are sometimes furigana-braced
(`→{痛|いた}い：01108_itai`) where the convention is plain kanji; **220 occurrences repo-wide**",
and proposed a bulk `systemic-fix` item with a one-line regex. The queue item
(`inline-link-braced-base-form`) had carried `scope_estimate: 36` since it was filed. The two
numbers looked like a contradiction and were reported as one.

They are not. **The measurement is 226 instances across 36 entries** — the queue's field counts
files and the observation counted occurrences, and both were right. But the ratio is the part
that matters, because it changes what the item *is*:

- **6.3 braced base forms per affected entry.** This is not a thin defect scattered over the
  corpus; it is a handful of files where the convention was applied wrongly and then applied
  wrongly again on every link in the file.
- **33 of the 36 entries sit below ID 01000**, and they cluster tighter than that: 00697–00716
  (the numerals and counters — 一, 二, 人, 枚, 個, 中, 時, 歳) and 00966–00984. One authoring
  cohort, one habit, one afternoon.
- The remaining three are singletons at 01xxx, 04xxx and 09xxx.

So the honest description is **not** "a 226-occurrence dictionary-wide sweep" but "**36 files,
one basic-tier cohort, one regex**" — which is a single bounded batch well inside one
`systemic-fix` run, and which needs no sampling strategy, no priority ordering, and no cursor.
It is also genuinely provably safe in the sense P24 claims: the `entry_id` is what resolves the
link, and the base form is display-adjacent text, so stripping `{…|…}` to the kanji cannot
change what the link points at. The one caution is that the affected entries are basic tier,
so the resulting diff is on the dictionary's most-read pages and should be spot-checked in the
rendered output rather than only in JSON.

**The generalisable point is about the queue's own schema.** `backlog-queue.json`'s
`scope_estimate` has no unit. Some items count entries, some count instances, some count
distinct target strings — and this is the second time in a week that a run has read one unit
and reported the other as a discrepancy (the stale-`noentry` item carries 2,887 for a
population that has also been described as 7,386, 3,809 and 2,633 depending on what is being
counted). The fix is one field, not a convention: `scope_unit`. Filed as
[Tooling 79](../ideas/tooling-backlog.md).

## The two *wrong-target* classes — where the link resolves but points at the wrong word

`check_link_targets.py` asks "does this ID exist?" and `check_link_baseform.py` asks "is this
ID the base form's own entry?". Both pass on a link whose ID exists and whose base form
matches *some* entry — which leaves a class where the link is live, renders normally, and
sends the reader to a different word. Three runs found instances of it in the first week of
August, and they fall into two shapes with different detection stories.

**Shape 1 — the homophone that isn't the word.** 00897 店員's note linked 店長 to
`07537_tenchou`, which is 転調 "modulation (in music)". The reading matches (てんちょう); the
headword does not. This is mechanically detectable and the check is a one-liner: for every
inline link, compare the base form against the target entry's headword *and* reading, and
report where the reading agrees but the headword does not. It is the mirror image of
[Tooling 59](../ideas/tooling-backlog.md#59-check_link_baseformpy-should-suppress-proposals-that-change-the-reading)'s reading test — that test suppresses proposals that change the reading, and this one
promotes disagreements that keep it. Both read the same two fields.

**Shape 2 — the bound suffix linked to its free-standing homophone.** A 2026-08-06
`systemic-fix` batch found both remaining 的 cases (00445 開放的, 02627 外交的な) linking the
adjectival suffix 〜的 to `03546_teki` 敵 "enemy" rather than to `09839_teki` 〜的. The same
shape repaired 〜社/者 and 〜軒/件 in an earlier batch, but those were suffix-vs-noun confusions
in the *surface*; here the base form genuinely is the suffix and the target genuinely is a
free-standing noun that shares its reading. The detection rule is narrower and fully
deterministic: **a link whose base form is a single kanji that also heads a `〜X` suffix entry,
but whose declared target is the free-standing noun of the same reading.** The `〜` prefix in
the suffix entry's headword is what makes the pair machine-separable.

Both shapes share the property that makes them worth building: the evidence needed to decide
them is already in the two entries, so there is no judgment queue and no curator step. They
are filed together as [Tooling 78](../ideas/tooling-backlog.md), because one pass over the link
corpus answers both.

### Shape 1, measured dictionary-wide for the first time (2026-08-13)

Tooling 78 was filed on two anecdotes. The 2026-08-13 wiki harvest ran the proposed comparison
over the whole corpus — every inline link's base form against its target entry's headword and
reading — after a 2026-08-13 new-entries run re-reported the class from a third instance
(04231 振り返る linked 顧みる at `13656_kaerimiru`, which is 省みる, a different verb). The
population is small and the naive form of the check is almost all false positives:

| Filter stage | Instances |
|---|---|
| Inline links in the corpus | 273,656 |
| Base form ≠ target headword and ≠ target reading | 1,491 |
| — minus affix (`〜X`), slash-headword (`速い／早い`) and する-verb normalisations | 456 |
| — minus base forms that are not a headword anywhere (variant spellings) | 94 |
| — minus base forms whose own entry shares the target's reading (orthographic variants) | 48 |
| **Residue: base form has its own entry, different reading from the target** | **48** (39 entries) |
| **Separate residue, drawn back out of the 362 "not a headword anywhere" rows: base form shares no kanji with the target headword** | **47** (39 entries) |

**The naive check's precision is about 3%.** Four normalisation filters remove 97% of what a
straight string comparison reports, and every one of them corresponds to a legitimate
convention this dictionary already uses. Any future version of this detector has to ship with
all four or it will bury its own signal — which is the same lesson the furigana screener
taught from the other direction (see [Instrument Defects](instrument-defects.md)).

The two residues are different defects:

- **The 48-instance residue is mostly *not* an error.** It is dominated by links whose base
  slot carries a kanji spelling whose default reading belongs to another entry — 頃 (ごろ)
  linked at `03091` 〜ころ, 本 and 下 both linked at `03878` 元 (もと), 良い at `00118` いい,
  臭い at `00874` 匂い. In context the *target* is right and the base slot is spelled with a
  homograph. This is [Homographs](homographs.md) territory, not a broken link, and it should be
  filtered out of any queue rather than worked.
- **The 47-instance residue contains the real class**, and splits about 23 / 13 on inspection:
  - **Homophone mislinks — the link resolves and sends the reader to a different word**:
    終身→`09947` 就寝 (しゅうしん), 用地→`04088` 幼稚 (ようち), 詩集→`05411` 刺繍 (ししゅう),
    詩的→`05630` 指摘 (してき), 詐称→`18658` 査証 (さしょう), 天賦→`07376` 添付 (てんぷ),
    進水→`09238` 心酔 (しんすい), 専任→`11607` 仙人 (せんにん), 書架→`11740` 初夏 (しょか),
    五時→`16131` 誤字 (ごじ), 深く→`14884` 不覚 (ふかく), plus single-kanji cases
    (感→缶, 温→恩, 系→計, 純→順, 吸→酢, 腑→負, 焼→〜屋) and 科す→`00537` 貸す.
  - **Orthographic variants — right word, non-canonical spelling in the base slot**:
    陽射し/日差し, 産まれる/生まれる, 表れ/現れ, 交じる/混じる, 鍼/針, 成す/為す, 捩る/捻る,
    旱魃/干ばつ, 食らう/喰らう, 生かす/活かす, 龍/竜, 町づくり/街づくり, 棹/竿. Cosmetic.

The homophone half is the same defect the 2026-07-31 `systemic-fix` run repaired 87 of
(機能→昨日, 性格→正確, 会社→外車) — so this is the *tail* of a class that has already been
swept once, not a new discovery, and its size after that sweep is the useful number: **about
23 instances across ~20 entries dictionary-wide.** That is a single sitting's work, it needs no
curator judgment, and it is filed as
[`inline-link-homophone-target`](../ideas/cleanup-backlog.md) at scope 23.

### Shape 3 — the target entry silently covers a different sense (2026-08-31)

Shapes 1 and 2 are both *wrong-word* errors: the base form and the target headword are different
words that happen to share a reading. There is a third shape where the base form and the target
headword are the **same word**, spelled identically, and the link is still wrong — because the
target entry documents a different sense of it. `check_stale_noentry.py` promotes exactly these
into its mechanical bucket, since every test it runs (base form has an entry, readings agree,
spelling agrees) passes.

Two runs found it from opposite ends and neither could see the other's case:

- **The self-declaring half.** ロック → `08116_rokku` "rock (music)" has now fired **five** times
  in lock contexts (04562 盗難, 05762 解除, 05909 認証, 06464 二重の) and is four of the whole
  sweep's rejections. 08116's own notes say outright that "ロック as 'lock' is a different word
  with the same reading", which is what
  [Tooling 134](../ideas/tooling-backlog.md#134-demote-same-reading-self-declared-homophones-out-of-check_stale_noentrypys-mechanical-bucket)
  proposed keying a demotion on.
- **The silent half.** 06574's コーラスパート resolves パート to `03106_paato`, an entry covering
  only パート = part-time work, which never mentions the section/voice-part sense. The target
  makes no self-declaration, so **no notes-scanning rule can see it** — 134's refinement is
  structurally blind to this half, and the observing run concluded there was no detectable tell.

There is one, and it is not in the target entry. It is in the base form: **the word is a katakana
loanword.** Of the detector's 123 mechanical-bucket pairs, 22 have an entirely katakana base, and
reading all 22 against their targets gives 8 sense mismatches — ロック ×4, パート, バー (scroll
bar → drinking establishment), コマ (a comet's coma → "frame, panel"), フライ (a baseball fly →
"deep-fried food") — against 14 that are correct (パン, ポタージュ, アンティーク, セラミック and
the rest). That is 18% of the bucket holding every instance either filing run found plus three
neither had spotted, and the rule needs no denylist and no notes scan. Filed as
[Tooling 143](../ideas/tooling-backlog.md).

The reason a spelling test works here is a fact about the dictionary, not about the checker.
A katakana entry almost always documents **one** borrowed sense of a word Japanese borrowed more
than once, from different source words, at different times — ロック from *lock* and from *rock*,
パート from *part-time* and from *part* (a voice in a chorus). For native vocabulary the same
spelling normally means the same word, which is why Shapes 1 and 2 are detectable by comparing
readings and this one is not. **Same-spelling-different-sense is the normal case for loanwords
and the exceptional case for everything else**, so "base form is katakana" is a proxy for
"polysemy the link cannot see" that costs 14 correct pairs a human glance.

## Why these keep being rediscovered

Every class on this page was found by a run that did not know it existed, and four of the six
were found more than once. The braced-base-form item was filed three times by three runs
before being worked. The stale-`noentry` class was described by Tooling 19 in July, then
independently re-reported by two polish runs in the last two days, each estimating "hundreds"
against a true figure of 3,797.

The common cause is that inline links are **invisible to every semantic instrument the
project has**. The clearest demonstration is from the 2026-07-31 `systemic-fix` run: it
repaired 87 links whose targets were outright homophones of the intended word (機能→昨日,
性格→正確, 会社→外車), and the §4 self-check over those same 64 entries returned **zero**
findings on the dimension that was actually broken — offering 25 unrelated tag opinions
instead. A link that resolves, renders, and is clicked is indistinguishable from a correct
one to any checker that reasons about meaning.

Deterministic base-form resolution is the only instrument that can see this class. That
argues for the same treatment the dead-target check already got: wire
`check_link_baseform.py --count` into the CI ratchet once the population is worked down, so
the class cannot silently regrow.

**The zero-link "class" is rediscovered by a different mechanism, and the count is now seven.**
Two more runs proposed it on 2026-08-09, both describing it as cheap and judgment-free ("a pure
absence test"). Unlike the defect classes above, this one is not invisible — it is *documented
on this page with a standing instruction not to file it*. What keeps regenerating it is that
every polish run meets the same local evidence: the block in front of the cursor has no links,
and its neighbours behind the cursor do. From inside a six-entry window that is
indistinguishable from a bad creation batch, and no amount of documentation reaches a run that
has not read this page. The durable fix is not another paragraph here — it is to make the
frontier position visible where the observation gets written, so "the entries ahead of the
cursor are unlinked" reads as a tautology rather than a discovery. Until then, treat repeat
filings as free measurements of an inaccessible fact rather than as noise: the 2026-08-09 pair
is what produced the below-frontier split and P50, which six earlier filings had missed.

## Implications for je-dict-1

1. **File the A1+A2 stale-`noentry` batch (2,887 links) as a high-priority systemic-fix
   item.** It is larger, safer, and more user-visible than anything currently in the top ten.
2. **Close the source before the backlog.** The `manage_candidates.py sync` hook prevents the
   next few thousand; the sweep only clears the current ones.
3. **Do not file a zero-link detector — file a zero-link-*behind-the-frontier* detector.** The
   unfiltered version measures the polish frontier, which is already measured. Intersected with
   the cursor it returns 55 entries the schedule passed and left bare, which is a real queue
   ([P50](../ideas/cleanup-backlog.md#priority-50-zero-links-anywhere-behind-the-frontier-55-entries--the-other-half-of-p46)).
   The same intersection is what makes P46 an item rather than an anecdote, and it is worth
   applying to any future coverage detector before deciding it is useless.
4. **Treat "this looks like a bad creation batch" as a hypothesis, not a finding.** Both
   observations this page corrects had the same shape, and both dissolved on contact with a
   band-level count. This is the corpus-side twin of the argument in
   [Instrument Defects](instrument-defects.md): as the corpus gets larger, a band-shaped
   observation from a six-entry sample is more likely to be a property of the *lane* than of
   the *entries*.

## Related pages

- [Cross-Reference Design](cross-references.md) — the structured `cross_references` field, and the field-level traps that parallel these
- [Instrument Defects](instrument-defects.md) — the companion argument on the tooling side
- [Homographs](homographs.md) — the substitution family behind classes B, C, D and the base-form disagreements
- [Cleanup Backlog](../ideas/cleanup-backlog.md) — P24, P27, P32, P35
- [Tooling Backlog](../ideas/tooling-backlog.md) — items 19, 49
- [Content Pipeline](../project/content-pipeline.md) — where linking sits in the polishing workflow
