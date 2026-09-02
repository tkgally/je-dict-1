# Knowledge Base Maintenance (the Routine's `wiki` mode)

Harvest what the working runs noticed into the structured backlog, keep the
wiki's index honest, and regenerate the metrics page. That is the whole job.

Since 2026-09-02 this mode is **trigger-only**: the selector schedules it when
`polishing/observations.md` holds at least 40 unharvested observation lines
and at least seven days have passed since the last wiki run. The research
library under `planning/wiki/research/` is a finished asset; it is not
extended by this mode. The 500,000-word maintenance loop that ran before
(essays on the instruments, thirty-nine refreshes of a metrics narrative) is
retired; its history is in git.

## Hard limits

- Change at most six wiki pages per run, and never grow a page by more than
  300 words. Prefer deleting stale prose to adding new prose.
- No "Last updated" paragraphs that summarize the run: the log entry does that.
- `planning/wiki/topics/quality-metrics.md` is generated; never edit it by hand.
- Do not add research pages, ideas pages, or new topic pages unless an
  observation names a topic no page covers, and then keep it under 400 words.
- Finish by 55 percent of the context window.

## Workflow

1. **Orient**: read `planning/wiki/index.md` (the catalog only) and the tail
   of `planning/wiki/log.md`.
2. **Harvest** `polishing/observations.md`, oldest first. For each observation
   line:
   - `[pattern]` or `[tooling]` describing something a detector could find and
     a batch could fix → add or update an item in
     `planning/wiki/ideas/backlog-queue.json` (fields: `id`, `title`,
     `source`, `detect` command, `filter`, `fix_type`, `verify`, `priority`,
     `batch_ready`, `status: "open"`, `scope_estimate`, `severity`, `notes`).
     If no detector exists, set `status: "needs-detector"` and describe the
     rule in `notes`.
   - `[entry]` → append one line to `planning/wiki/ideas/entry-followups.md`
     (ID, what is wrong, suggested fix); if the fix is a few minutes' work and
     you are certain, make it now and validate the entry.
   - `[skill]` → make the skill edit if it is a clarification; otherwise one
     line in `planning/wiki/ideas/tooling-backlog.md` under "Skill updates".
   - `[wiki]` or `[wiki:page]` → the smallest edit to the named page that
     records the fact.
   - `[article]` → one line in `planning/wiki/ideas/expository-articles.md`.
   Then delete the harvested lines from `observations.md` (keep the header and
   template). Record the count harvested.
3. **Reconcile the backlog**: for every `backlog-queue.json` item whose
   detector exists, rerun the detector's `--summary` and update
   `scope_estimate`; mark items with zero scope `resolved` with today's date.
   Keep the prose backlog pages consistent with the JSON only where they
   disagree; the JSON is the source of truth.
4. **Regenerate the metrics page**:
   ```bash
   python3 pipeline/metrics_report.py
   ```
   If a metric is moving the wrong way for three weeks in a row (frontier
   stalled, review queue growing, precision falling), add one `[pattern]`
   observation naming it.
5. **Index and log**: update `planning/wiki/index.md` only if a page was added
   or removed. Append one log entry of at most 150 words to
   `planning/wiki/log.md`:
   ```
   ## [YYYY-MM-DD] maintenance | <one-line summary>
   Harvested N observations: N backlog items (new/updated), N entry follow-ups,
   N skill notes. Backlog reconciled: N resolved. Metrics page regenerated.
   ```
6. **Wrap up** per routine2.md §5–§7 (metrics snapshot, session log, commit,
   PR, merge). Wiki-only runs skip `make index`.

## Writing rules

- Plain, specific English. Numbers with their source command. No rhetoric.
- A backlog item is written so that a systemic-fix run can execute it
  without reading anything else: the detector command, the filter, the fix,
  and the check.
- Never delete a research page. Never rename a page (links break).
