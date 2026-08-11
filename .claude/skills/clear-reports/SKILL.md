---
name: clear-reports
description: Write PR descriptions, end-of-run summaries, and curator-facing flags in plain, self-contained English for Tom. Use at every session wrap-up before writing the PR body or the final summary, and when appending judgment items to reviews/needs_curator.txt.
---

# clear-reports — writing for Tom, the curator

On 2026-08-11 Tom instructed: reports to him must be understandable without following the
project run by run. Internal logs and the planning wiki may stay technical; **the PR description
and the final session summary are reports to Tom, and they must stand on their own.** If this
file ever conflicts with a newer instruction from Tom, Tom wins; update this file.

## The reader

- Tom is a **professional Japanese–English lexicographer**. Never explain furigana,
  transitivity, keigo, rendaku, register, or any linguistic or lexicographic concept — that is
  his field, and explaining it to him is noise. Discussion of individual words, senses, and
  contrasts is welcome detail, not jargon.
- What he does **not** carry in his head is this project's machinery: Routine mode names,
  cursors and frontiers, P-numbers, detector and script names, ledgers, queues, sweeps. Weeks
  may pass between his visits.
- He **reads once, without opening other files**. A PR body that says "P35 A1+A2 sweep,
  01440–02229, queue 1,256/1,471" tells him nothing.

## Which texts this governs

- **PR titles and descriptions.** Each Routine run merges its own PR, so the PR body is the
  run's report to Tom and often the only thing he reads. **Keep machine-read title
  conventions** — the `routine(<mode>):` prefix is parsed by the stranded-PR sweep — and make
  everything after the prefix plain.
- The **end-of-run summary** — the final message a session leaves in the chat.
- **`reviews/needs_curator.txt`.** Every flag says, in plain words, what the item is and what
  judgment is being asked of him. Keep any line format the workflow requires (timestamps,
  `prune-branch` lines); add the plain context after it.
- **`PROJECT_STATUS.md` Recent Changes** entries, which he reads to catch up.

Not governed: session logs in `polishing/sessions/`, `polishing/observations.md`, and the
planning wiki — future runs read those, and precision there beats accessibility (though clarity
costs nothing).

## What every PR body and end-of-run summary contains

1. **What this run did to the dictionary, in one plain sentence**, with the mode named in
   passing: "This run worked on one recurring defect class (the Routine's 'systemic-fix'
   mode): …"
2. **Scale, in context of the whole.** "…reviewed 180 flagged cross-references in entries
   01440–02229 — the dictionary has about 19,000 entries, and this sweep has now covered
   everything below 02230, with roughly 1,250 flagged links remaining."
3. **The interesting content decisions.** The lexicographic substance — specific words, senses,
   contrasts, why a flag was right or wrong — is what Tom most enjoys and can best judge. Keep
   it, in full sentences.
4. **The verification outcome, in plain words.** "An independent model re-checked the entries
   this run touched and found nothing" — not "§4 self-check clean." Say briefly what outside
   suggestions were accepted or dismissed, and why.
5. **Cost, when money was spent.** "$0.007 of the $5 daily budget."
6. **What needs Tom** — a policy call, a flagged uncertainty — or, explicitly, that nothing
   does.

## Terminology rules

- **Describe the thing; the internal label follows in parentheses if it is needed at all.**
  "stale 'no entry' cross-references — links marked as pointing to a nonexistent entry back
  when that was true, though the entry has since been created (cleanup item P35)".
- **Never use a bare P-number, mode name, file path, cursor value, or script name as if it
  explained itself.** "the comprehensive frontier is at 06865" → "the entry-by-entry polishing
  sweep has reached entry 06865 of about 19,000 — roughly a third of the way through its
  current pass."
- **Counts get context**: totals against the whole dictionary, "remaining" alongside "done".
- **Adjudication verdicts in plain words**: APPLY → "accepted and fixed"; REJECT → "dismissed
  (wrong, or a stylistic preference)"; FLAG → "set aside for your judgment".
- **The report must stand alone.** File paths are optional pointers, never required reading.

## Worked example

**Not this:**

> routine(systemic-fix): P35 A1+A2 sweep. 178 pairs / 198 instances / 134 entries applied, 2
> rejected; queue 1,256/1,471; cursor→02230; §4 screening clean; ledger $0.00.

**This:**

> routine(systemic-fix): update 178 cross-reference links whose target entries now exist
>
> This run worked on one recurring defect class (the Routine's "systemic-fix" mode): inline
> cross-references that were marked "no entry exists for this word" back when that was true,
> but whose word has since gained an entry. Working in entry-ID order, it read each of 180
> flagged links in context in entries 01440–02229 and converted 178 of them into live links to
> the now-existing entries; 2 were left unchanged because the flagged word turned out to be a
> different sense of the same spelling. Everything below entry 02230 is now swept; about 1,250
> flagged links remain for future runs. An independent model re-checked the touched entries and
> found no problems, and no review budget was spent. Nothing needs your attention.

## Self-check

- Would this read cleanly to someone who last looked at the project a month ago?
- Mode names, P-numbers, cursors, queue figures — all glossed or reworded?
- Counts placed in context of the whole dictionary?
- Verification outcome and spend stated plainly?
- Does it end with what needs Tom, or say that nothing does?
