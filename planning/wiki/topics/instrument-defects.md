# Instrument Defects vs. Corpus Defects

**Last updated**: 2026-07-30

## Overview

Every quality signal this project acts on arrives through an instrument: a detector script, a
validator, a scoring function, or a model prompt. When such a signal says *"many entries are
wrong"*, there are always two explanations, and they are not equally likely:

1. **A corpus defect** — the entries really are wrong.
2. **An instrument defect** — the thing measuring the entries is wrong.

A run reading the signal cannot tell these apart from inside the signal, because the
instrument's output is the only view of the corpus it has. Distinguishing them requires going
to the source file, or to the instrument's own code, and checking by hand.

This page collects the cases where that check was eventually performed, extracts what they have
in common, and states the detection heuristics they support. It exists because the project has
now spent, by conservative count, **several months of accumulated sweep effort and a
non-trivial share of its OpenRouter budget** acting on signals that turned out to be
instrument defects — and because in every case, once someone finally looked at the instrument,
the fix was a one-liner.

## The documented cases

### 1. `score_note_quality.py` — `"adverb"` contains `"verb"`

**Signal**: the priority polishing lane kept surfacing entries that turned out, on inspection,
to need no changes. Recorded as a "no-op" roughly **65 times** across two months of runs.

**Hypothesis the signal invited**: the priority rankings are *stale* — they were computed before
recent polishing, so they keep re-surfacing entries that have since been fixed. This is a
completely reasonable reading, and the Routine prompt was amended to regenerate the priority
files and reset the cursor whenever the no-op rate went above half.

**Actual cause** (found 2026-07-27/28, fixed 2026-07-28): two independent bugs in the scorer.

- `normalize_pos()` tested `'verb' in pos.split(',')[0]` — and **`"adverb"` contains
  `"verb"`**, so every `adverb, …` entry was scored against the *verb* template and required to
  have sections an adverb entry cannot have. `00266_maido` sat at 54 after a complete rewrite.
- `has_bare_kanji()` did not strip the inline-link tail before applying the furigana pattern,
  producing phantom unannotated-kanji penalties.

Together these **mis-scored 6,529 of 29,993 entries (22%)**.

**What the mis-diagnosis cost**: the regenerate-and-reset workaround, applied faithfully, made
things worse — it re-ranked against the same broken scorer and demonstrably **looped within a
single day**, sending runs back to entries they had just cleared. And when the bugs were fixed,
every conclusion the priority lane had produced since its introduction had to be re-opened,
*including the staleness hypothesis itself*, because all of them were drawn against a
ranking that was wrong for 22% of the dictionary.

### 2. `validate.py` — the check existed; three of four code paths never called it

**Signal**: polish runs kept introducing inline links pointing at non-existent entry IDs, and
`validate.py --id <entry>` reported *"Entry is valid!"* every time. Six consecutive cycles,
across at least six separate runs.

**Hypothesis the signal invited**: `validate.py` has no inline-link target check. The item was
filed under that description on 2026-06-10 and re-confirmed under it five more times. Three
different sessions wrote their own ad-hoc link scanners to work around the gap.

**Actual cause** (found and fixed 2026-07-29): `check_word_links()` had been in `validate.py`
all along, resolving link targets correctly, and a full `make validate` had been reporting
**308 word-link warnings** the entire time. But `validate_single_entry()` — the function behind
**both `--entry` and `--id`** — never called it. Neither did `validate_changed_only()` nor
`validate_range()`.

> The check ran only in the one code path a polishing session never invokes. The pre-commit
> hook, which uses `--entry`, was blind for the same reason.

**What the mis-diagnosis cost**: 291 dead links accumulated across 159 entries. Three sessions
re-implemented, in throwaway scripts, code that already existed in the file they were running.
Every proposed fix would have added a *second* implementation beside a working one.

**The single command that would have closed six cycles**: `grep -n check_word_links build/validate.py`.

### 3. `review_runner.py` — a truncated context snippet the model read as a reading

**Signal**: the paid furigana screener flagged large numbers of entries in already-polished
ranges as having incomplete readings — up to **16% of entries** in one range.

**Hypothesis the signal invited**: initially, that the dictionary had a systemic truncated-reading
problem. Once precision was measured (0–5%), that the *model* was unreliable on this dimension —
leading to a standing recommendation to consider retiring the screener.

**Actual cause** (located 2026-07-28, fixed 2026-07-30): `extract_furigana_pairs()` captured only
**10 characters** of following context, and `build_screening_prompt()` rendered it as
`(followed by: {協議会|きょうぎか)`. A 10-character window almost always cuts *inside* the next
`{kanji|reading}` wrapper — and **the closing paren of the annotation then reads as the
wrapper's closing brace**. The model was shown a syntactically complete wrapper containing a
truncated reading, and correctly reported what it was shown.

**Why it survived four cycles of diagnosis**: the artifact is not a malformed string the model
mishandled. It is a *well-formed* string that means something different from what the entry
says. Each cycle described the mechanism slightly better ("pair extraction truncates readings"
→ "the context snippet is clipped mid-wrapper" → "the paren closes the clipped span") without
reaching the delimiter collision that made it invisible.

**What the mis-diagnosis cost**: four ranges' worth of screening budget spent at 0–5% precision,
plus the adjudication effort of rejecting the flags one by one — and a nearly-adopted decision
to retire an instrument that was never actually being tested, since **every precision figure on
record predates the fix**.

### 4 and 5. Two more, found while writing this page

Both surfaced in the 2026-07-30 harvest, from observations proposing new tooling:

- **`check_furigana_format.py` and katakana wrappers.** A polish run found
  `{ケーキ|けーき}` in an entry's notes and proposed that the detector should grow a check for
  katakana surfaces inside furigana braces. It already has one — such findings land in the
  existing `pure-kana` subpattern, **258 of the 373** `pure-kana` findings being katakana-surfaced.
  The useful change turned out to be a *subpattern split* (the katakana half is an unconditional
  fix, the rest needs judgment), not a new check.
- **`check_artifacts.py` and target-less cross-references.** A polish run asked whether the
  `missing-target-id` check covers references with **no `target_id` key at all**, as opposed to
  an empty one. It does — the test is `not ref.get("target_id")`. But it then *skips* any
  reference whose word has no entry, treating it as an intentional pointer. A malformed
  reference — one whose declared reading does not match its own headword — is not an intentional
  pointer, and the resolvability filter is precisely what hides it. The check is right; a filter
  in front of it suppresses the subclass that matters.

Neither is a bug exactly. Both are the same epistemic shape: **a run inferred the absence of a
capability from the absence of an output.**

### 6. The lint written to check this page's own links

Recorded because it happened while writing the section above, and it is the cleanest
demonstration of the base-rate argument the page makes.

The 2026-07-30 wiki run wrote a throwaway cross-reference lint to verify the anchors in this
page and the day's other edits. Successive runs reported **119**, then **24**, then **7**
broken anchors across the wiki. The true count was **0**. Every reported failure came from the
lint's own slug function disagreeing with GitHub's, in three independent ways:

| Iteration | Reported | Actual defect — in the lint |
|---|---|---|
| 1 | 119 | Anchor table keyed on relative paths, looked up with resolved ones — so *every* anchor lookup missed |
| 2 | 24 | Collapsed runs of spaces to one hyphen; GitHub maps each space separately, so ` & ` → `--` not `-` |
| 3 | 7 | Converted `–`/`—` to hyphens; GitHub **drops** them, so ` — ` → `--` not `---` |

Three things make this worth the space:

- **Iteration 1 was 100% false positives, and looked like a catastrophe.** A run that had
  reacted to the number rather than sampling a case would have "fixed" 119 working links into
  broken ones — the workaround-makes-it-worse property from cases 1 and 2, in its purest form.
- **The confirming evidence was already in the repo.** An existing anchor,
  `#priority-23-20-entries-2918129200-missing-metadatavocabulary_tier`, contains
  `2918129200` — the en-dash in `29181–29200` silently dropped. That anchor *works*, so it
  encodes GitHub's actual rule, and reading it settled iteration 3 immediately. **When an
  instrument disagrees with the corpus, artifacts already known to work are the calibration
  set.**
- **The corpus was clean the whole time.** Every wiki anchor was correct, including seven the
  lint accused across three separate runs. Prior sessions had done that work; the instrument
  simply could not see it.

### 7. The CI gate — and the cross-check that agreed with it

The first case on this page to sit in the **merge** path, where a wrong reading strands finished
work rather than wasting a cycle.

On PR #3069, the 2026-07-30 wiki run polled `mcp__github__pull_request_read --method
get_check_runs` **eight times over ~14 minutes** and got `total_count: 0` every time. Suspecting
the endpoint, it cross-checked with `actions_list --workflow validate.yml --branch <branch>` —
which **agreed**, also returning `total_count: 0`. Two independent endpoints, same answer.

The answer was wrong. The workflow job's own `started_at` was 07:46:00Z: it had been queued
*before* most of those polls. It surfaced only after a later push, then ran to `success` in 60
seconds. By then the run had written a session-log section concluding "no workflow run was ever
queued" and had stopped without merging.

What makes this case worth adding to a page that already has six:

- **The cross-check did not help, and could not have.** Every other case here was settled by
  finding a second source of evidence. Here the second source was the same kind of instrument
  asking the same question of the same eventually-consistent API, so it reproduced the error
  instead of catching it. *Independent* means independent of the failure mode, not merely a
  different endpoint.
- **The correct inference was available and weaker than the one made.** `total_count: 0` licenses
  "no check run is **visible**"; the run wrote "no check run was **queued**". The durable rule:
  **absence of a check run is evidence of "not visible yet", never of "not queued"** — these APIs
  are authoritative about presence and silent about absence.
- **The cost asymmetry is the reverse of the usual one.** Elsewhere on this page, over-trusting an
  instrument caused wasted work. Here it caused *finished* work to sit unmerged, and the log to
  record a false cause for it — which is worse, because the next reader inherits the wrong
  explanation.

Filed as [Tooling 48](../ideas/tooling-backlog.md#48-the-7-ci-gate-cannot-distinguish-ci-is-slow-from-ci-never-started--and-its-cross-check-agrees-with-it-when-it-is-wrong).
The actionable part is small and is about *wording*: a timed-out run should log "checks not
visible within the cap", not "no run was queued". The polling policy itself was already correct.

## What the cases have in common

| | Symptom presented as | Actual locus | Cycles to find | Fix size |
|---|---|---|---|---|
| `score_note_quality.py` | corpus is already clean (no-ops) | substring match in POS normalizer | ~65 sightings | one line |
| `validate.py` | corpus is silently accumulating dead links | check not wired into 3 of 4 entry points | 6 cycles | a few lines |
| `review_runner.py` | corpus has systemic reading truncation | prompt context cut mid-markup | 4 cycles | one function |
| `check_furigana_format.py` | detector lacks a check | check exists under another name | 1 | none (rename/split) |
| `check_artifacts.py` | detector lacks a check | a filter suppresses the subclass | 1 | one condition |
| wiki link lint | 119 broken anchors | slug function wrong 3 independent ways | 3 (same hour) | 3 lines |

Five properties recur:

**1. The instrument's output was the only evidence considered.** In every case the diagnosis was
built by reasoning about *what the instrument reported*, carefully and at length, without opening
the instrument or the source file. The reasoning was usually excellent; it was reasoning about
the wrong object.

**2. The wrong hypothesis was the more interesting one.** "The rankings are stale", "no
link-target check exists", "the model is unreliable on furigana" are all substantive claims that
generate work. "The tool has a typo" generates a one-line diff. Attention flowed to the
interesting hypothesis and stayed there.

**3. Repetition reinforced the wrong hypothesis instead of challenging it.** The no-op streak
was recorded 65 times *as confirmations*. Each recurrence was read as strengthening the
staleness case, when a defect reproducing perfectly across unrelated ranges, entry types, and
months is far better explained by a deterministic bug than by a data property. **Perfect
reproducibility is evidence for a bug, not for a pattern.**

**4. The workaround made things worse.** Twice, acting on the wrong diagnosis was actively
harmful — the regenerate-and-reset backstop looped within a day, and three sessions wrote
duplicate link scanners. A workaround built on a mis-diagnosis inherits the mis-diagnosis.

**5. The fixes were trivial and had been available the whole time.** All five are one-liners or
near. The 2026-07-29 process note recorded what finally moved them: not a better argument or
more urgency, but **a report that named the file, the line, and the replacement text**.

## Why the base rate now favours the instrument

This is the part that has changed with the project's maturity, and it is the reason this page is
worth having.

Early on, a high flag rate over a range of entries was *good evidence of corpus damage*, because
much of the dictionary was genuinely unpolished. That is no longer the prior. Ranges reached by
the sweeps have been through furigana completeness, tag validation, schema validation, and at
least one cross-model pass. So when an instrument reports that 16% of an already-polished range
is defective, two things are being compared:

- **P(the corpus has a 16% defect rate in a swept range)** — low, and falling as coverage grows.
- **P(an instrument has a bug)** — roughly constant, and there are now a dozen instruments,
  several with model prompts in the loop, all under active modification.

As corpus quality rises, the second term overtakes the first. **A sudden jump in flag rate over
an already-polished range should now be treated as a tooling hypothesis first and a corpus
hypothesis second** — which inverts the reading that was correct a year ago.

Two corollaries:

- The inversion applies to *rates*, not to individual findings. A single flag on a single entry
  is still most likely about that entry.
- It applies with most force where the instrument is newest or most recently edited. The
  screener bug was introduced by a prompt-assembly detail; prompts change often and are not
  covered by tests.

## Detection heuristics

Cheap checks, in rough order of cost, that would have caught the documented cases:

1. **Before proposing a new check, grep for it.** Cases 4 and 5 die here, and case 2 dies to
   `grep -n check_word_links build/validate.py`. Absence of output is not absence of capability.
2. **When a documented check reports nothing, verify which code path the documented invocation
   takes.** This is case 2's durable lesson and the one with the widest application: the
   documented command and the working code can diverge silently and permanently.
3. **Check whether the flag's own quoted evidence is well-formed by the project's rules.** The
   screener's quotes — `{分別|ふんべ)`, `{発狂|はっ)` — are *not valid furigana at all*. A
   quoted defect that could not exist in a validating entry did not come from the entry; it came
   from the instrument. This is the single highest-yield tell, because it needs no source lookup.
4. **Spot-check three flags against the source file before acting on any of them.** This is the
   §4/§A "verify before you apply" rule, and it is what actually caught cases 2 and 3. Three
   files is a few minutes against a sweep costing hours.
5. **Treat a dominant single-shape family as an instrument signature.** Corpus defects are
   heterogeneous because they come from different entries written at different times. When 47 of
   48 flags share one shape, that shape is the instrument's, not the corpus's.
6. **Suspect the tool when the result is too uniform** — a no-op rate near 100%, a flag rate that
   does not vary with the range's age or type. Real corpus properties vary by creation cohort;
   this project's cleanup backlog is largely organized around that fact.

## Implications for je-dict-1

**The verification discipline is load-bearing, and it is working.** §4 (verify your own changes)
and §A step 4 (apply corrections with judgment, never blindly) were written to stop bad
corrections from being applied. Their larger payoff has turned out to be different: they are what
surfaced cases 2 and 3, because both were found by a run checking flags against source before
acting. Any future proposal to trust an instrument's output and skip the check should be weighed
against that.

**Instrument fixes should outrank corpus sweeps when both are queued.** The scorer bug corrupted
22% of a ranking that then drove months of lane selection; the `validate.py` wiring gap let 291
dead links accumulate. A defective instrument does not merely fail to find defects — it
*generates* work, in the form of sweeps that fix nothing and diagnoses that must later be
retracted. The cost is superlinear in how long it stays open, and the fixes are one-liners.

**Filings should name the file, the line, and the replacement text.** The 2026-07-29 process
observation is the one lever the ledger data supports: three items open for 25 and 81 days were
all fixed within days of a report in that form. Symptom-level filings, however well argued,
did not move.

**No precision figure survives its instrument's repair.** Every screener precision number on
`topics/quality-metrics.md` predates the 2026-07-30 fix, so the "retire the screener" argument is
suspended, not resolved. When an instrument is repaired, its historical metrics measure the old
instrument — they should be annotated as such rather than compared across the boundary.

**Where this most likely applies next.** The instruments carrying the least verification today
are the ones with model prompts inside them (`review_accuracy.py`'s dimensions, the deep furigana
pass) and the scoring functions that feed lane selection. Both are edited without tests —
`build/tests/` has never run in an unattended session, because the container image lacks `pytest`
([Tooling 42](../ideas/tooling-backlog.md#42-routine-container-image-lacks-jsonschema-and-pytest)).
That gap is the common ancestor of several cases above, and closing it is the structural fix
this page argues for.

## Related pages

- [Quality Metrics Trend](quality-metrics.md) — the time series these instruments produce, and what each is worth
- [Deterministic vs. Semantic Tasks](deterministic-vs-semantic-tasks.md) — which checks can be mechanical and which need judgment; the case-4/5 pattern is a failure to know which one already exists
- [Furigana Wrapper Anomalies](furigana-wrapper-anomalies.md) — the corpus-side patterns the furigana instruments look for
- [Schema Tag Reliability](schema-tag-reliability.md) — tag drift, where instrument and corpus defects also interleave
- [Tooling Backlog](../ideas/tooling-backlog.md) — items 11, 20, 24, 42, 45–47 are the case files above
- [Cleanup Backlog](../ideas/cleanup-backlog.md) — the corpus-side queues these instruments feed
