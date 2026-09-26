# Example Audio (the Routine's `audio` mode)

Record MP3 readings of example sentences with Gemini TTS, check each one with
four AI checkers, and publish the accepted ones to the audio repository. The
site then plays the recording in place of browser speech. The workflow, the
evidence for it, and its changelog are in `AUDIO_WORKFLOW.md`; read §2 and §6
there before a first audio run, not every time.

Runs as `prompts/routine2.md`'s `audio` mode. `params.openrouter_session_budget_usd`
(call it B) is this run's OpenRouter cap. This mode changes no entry text (`publish`
only sets the recorded examples' `has_audio` flags), so §3 and §4 of routine2.md
(mechanical pass, self-check) do not apply. Everything is
deterministic code: your judgment is needed only for maintenance results and
for the examples left for a human.

## 1. Setup

```bash
make audio-deps                                  # MeCab/UniDic, MP3 encoder (about a minute)
python3 build/audio_pipeline.py status           # coverage; copy the numbers into the session log
```

Make sure this session can push to the audio repository (the active store in
`audio/config.json`, today `tkgally/je-dict-audio-1`) before spending anything:

```bash
python3 build/audio_pipeline.py check-access     # "push": true → go on
```

If `push` is false, call `add_repo` (owner and repo from the store, `access:
"push"`) if that tool is available, and run `check-access` again. If it is still
false (or `add_repo` is not available): set `production.enabled` to false in
`audio/config.json` with the reason "the Routine cannot push to <repo>: add it to
the Routine's repositories", append one line to `reviews/needs_curator.txt`
(`<UTC> audio-store — the Routine cannot push to <repo>; add it to the Routine's
repositories in its settings, then set production.enabled to true in
audio/config.json`), skip to §6 and wrap up. Switching production off stops the
selector from choosing this mode again until Tom has fixed the access.

## 2. Maintenance first (AUDIO_WORKFLOW.md §10)

```bash
ls audio/spotchecks/*.json 2>/dev/null           # Tom's ratings waiting to be imported
python3 build/audio_maintenance.py due           # exit 2 = production blocked
python3 build/audio_maintenance.py drift         # warnings about recent runs
```

Handle, in this order, each item that applies. Keep a running total of what
maintenance spends (each command prints its cost); it comes out of B.

- **Ratings files** in `audio/spotchecks/`: `python3 build/audio_maintenance.py
  import-ratings audio/spotchecks/*.json`. If it reports a clip Tom marked wrong,
  the checks missed an error: run `python3 build/audio_regression.py` (the new
  clip is now in the suite), write a changelog entry in `AUDIO_WORKFLOW.md`
  (what was missed, whether the suite now catches it), and flag it to the curator.
- **regression** (blocking): `python3 build/audio_regression.py` (about $0.25). PASS
  unblocks. FAIL means the checkers no longer catch known errors although the
  configuration did not change (a model changed behind its ID): set
  `production.enabled` to false in `audio/config.json` with the reason, add a
  changelog entry with the misses, flag it to the curator, and wrap up.
- **pilot** (blocking): for each production voice it names,
  `python3 build/audio_pipeline.py testset --voice <Voice>` (about $0.30 each).
  Not acceptable → as for a failed regression.
- **models**: `python3 build/audio_maintenance.py check-models`. A configured model
  in `dead` → set `production.enabled` false, flag it, wrap up (replacing a model
  is a workflow change for Tom to approve). Models in `new_since_last_check` →
  one `[tooling]` line in `polishing/observations.md` naming them.
- **spotcheck**: `python3 build/audio_maintenance.py spotcheck --n 30`. The page is
  published with the recordings in §4 and announced in `reviews/needs_curator.txt`.
- **reaudit**: `python3 build/audio_maintenance.py reaudit --sample 100 --budget 0.40`.
  Rejected clips lose their manifest line and are re-recorded by §3; list them in
  the session log.
- **reevaluate** (every 120 days; spend at most $1.50): read `AUDIO_WORKFLOW.md`
  §4–§6 and the `check-models` output. If a newer Gemini TTS model or a newer
  audio-input model from a checker's family is listed, copy `audio/config.json`
  to `audio_work/trial.json`, change that one model there, and run
  `python3 build/audio_pipeline.py testset --voice Kore --config audio_work/trial.json`
  (TTS model) or `python3 build/audio_regression.py --config audio_work/trial.json`
  (checker). Write the result in the `AUDIO_WORKFLOW.md` changelog, including "no
  better model found". Never switch production models yourself: if the trial is
  clearly better (higher first-pass rate, or the same catches with fewer false
  alarms, or cheaper at the same quality), propose it in
  `reviews/needs_curator.txt`. Then set `"reevaluate"` in `audio/maintenance.json`
  to today.
- **drift warnings**: one line in `reviews/needs_curator.txt` quoting them.

If production is still blocked, wrap up (§6).

## 3. Record

```bash
python3 build/audio_pipeline.py plan --budget <B − maintenance spend − 0.10>
python3 build/audio_pipeline.py run          # repeat until it prints "remaining": 0
```

`run` stops starting new examples after 8 minutes, so a call stays under the
tool timeout. Call it again, in the foreground, until `remaining` is 0. It
resumes where it stopped and counts earlier calls against the budget. At about
$0.0025 per example, B = $4.80 records about 1,800 examples. That is about 25
minutes of calls (three or four `run` calls) with the default 12 workers.

**Priorities** (`plan` applies them; do not reorder by hand):
1. **Stale recordings**: examples whose text or furigana changed after they
   were recorded. The site has fallen back to browser speech for them.
2. **Basic tier** (6,044 examples), then **core** (13,907): the most visited
   entries, and closed tiers whose examples rarely change.
3. **General tier, entries the polish frontier has passed**
   (below `polishing/tasks/comprehensive/progress.txt`'s `next:`). Recently
   polished text is the least likely to change again.
4. **General tier, the rest**, in ID order.

Within each group, examples go in entry order, and an entry's examples are never
split across runs. Voices rotate within each entry (`audio/config.json`
`voices`). A re-recording keeps its old voice.

**Examples that are not recorded** (`plan` skips them and counts them; nothing
to do by hand):
- *Digits and Latin letters* (3時, 20%, NHK; about 2,500 examples): furigana does
  not give their reading. They keep browser speech until readings written by a
  text model have been validated by ear (`AUDIO_WORKFLOW.md` §3.1). Do not write
  readings for them in this mode.
- *Symbols* (× ○ + ÷ = ℃, about 30 examples): their reading is not fixed (ばつ or ばってん).
  They keep browser speech, like digits.
- *Kanji without furigana* (82) and *malformed markup* (8): these are furigana
  errors in the entry. The systemic-fix backlog item
  `audio-undetermined-furigana` fixes them. List them with
  `python3 build/audio_pipeline.py undetermined --reason bare-kanji malformed`.
- *Left for a human with the same text* (`audio/needs_human.jsonl`): not retried
  until the text or the workflow version changes.

## 4. Publish and verify

```bash
python3 build/audio_pipeline.py publish      # push MP3s (and any spot-check page) to the audio repo, then write the manifest
python3 build/audio_pipeline.py verify       # waits up to 9 minutes for GitHub Pages to serve them
```

`publish` writes the manifest, and sets `has_audio` to true on the recorded
examples, only after the push succeeds, so a failed push leaves je-dict-1 unchanged. Retry once; if it fails again, flag it and wrap
up. If `publish` stops because the store is full, set that store's `status` to
`"full"` in `audio/config.json`, flag to the curator that the next audio
repository is needed (`AUDIO_WORKFLOW.md` §7), and wrap up. A `verify` timeout
is not fatal: Pages can lag. Say so in the session log and continue.

## 5. Examples left for a human

For each example this run left for a human (`audio/needs_human.jsonl` lines
with today's date), read the checkers' `diffs`. When the checkers kept hearing
one plausible reading that differs from the furigana, the furigana may be
wrong. Log `[entry] NNNNN: audio checks heard <X> for <Y> in <example id>; check
the furigana` in `polishing/observations.md`. Do not edit entries in this mode.
Otherwise the item simply waits for Tom; the report names how many there are.

## 6. Wrap up (routine2.md §5–§7)

- Metrics: `python3 pipeline/metrics_snapshot.py --mode audio --changed 0`.
- Session log `polishing/sessions/routine_{date}_{NNN}.md`: status numbers before
  and after, maintenance done and its results, examples planned / accepted /
  first-pass / left for a human, cost (`audio/runs.jsonl` last line), entry range
  recorded, `verify` result.
- `make gate`, `make index`, commit (`audio/`, the entries whose `has_audio` flags changed, the
  ledger, the session log),
  push, PR titled `routine(audio): <N> recordings, entries <first>–<last>`,
  CI, merge. The PR body says how many examples now have recordings, what it
  cost, and anything Tom must do (a spot-check page to rate, a model to approve).
- Never commit `audio_work/` (gitignored) or any MP3 to je-dict-1: CI rejects it.
