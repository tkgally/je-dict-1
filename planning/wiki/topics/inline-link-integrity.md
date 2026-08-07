# Inline Link Integrity

**Last updated**: 2026-08-07 (measured the braced-base-form class, which turned out to be
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
| **Entries with zero links** | **23,294** | **Not a defect — see below** | *(structural; do not file)* |
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

## Zero-link entries — 23,294, and *not* a defect

Two polish runs (2026-07-31, 2026-08-01) reported that a frontier block "was created with
zero inline links … consistent with a creation batch that predates the inline-link
requirement," and proposed both a `check_link_coverage.py` detector and a targeted backfill.

The corpus says there is no batch. Zero-link entries by ID band:

| Band | Entries | Zero-link | % | Links in band |
|---|---|---|---|---|
| 00000–01999 | 1,989 | 0 | 0.0% | 86,455 |
| 02000–03999 | 1,989 | 23 | 1.2% | 79,929 |
| 04000–05999 | 1,987 | 3 | 0.2% | 72,782 |
| 06000–07999 | 1,918 | 1,202 | 62.7% | 25,518 |
| 08000–09999 | 1,995 | 1,857 | 93.1% | 1,055 |
| 10000–29999 | 19,912 | 19,911 | ~100% | 11 |
| 30000+ | 298 | 298 | 100% | 0 |

This is not a batch signature. It is a **cliff at the comprehensive-polish frontier**, which
sits at 06723 — in the middle of the one band that is partially linked. Essentially every
link in the dictionary lives below ID 08000, and essentially every entry above it has none.

Inline links are not added at creation time at all; `CLAUDE.md` says so explicitly ("Never
add inline word links (⟦...⟧) during entry creation — those are added in a separate polishing
step"). So the observation's premise — "this block predates the requirement" — inverts the
causality. The block has no links because the polish frontier has not reached it. **The
frontier lane *is* the backfill.**

The consequence is worth stating plainly, because it is a strategic fact rather than a
cleanup item:

- 23,294 entries are unlinked.
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

## Implications for je-dict-1

1. **File the A1+A2 stale-`noentry` batch (2,887 links) as a high-priority systemic-fix
   item.** It is larger, safer, and more user-visible than anything currently in the top ten.
2. **Close the source before the backlog.** The `manage_candidates.py sync` hook prevents the
   next few thousand; the sweep only clears the current ones.
3. **Do not file a zero-link detector.** It measures the polish frontier, which is already
   measured.
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
