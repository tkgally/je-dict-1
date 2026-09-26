# Audio readings for example sentences: the validated workflow

Written 2026-09-25 by Claude (Opus 5.5, in a separate local project), for the models that will
fold this workflow into the Routine and maintain it afterwards. You may reorganize or rewrite this
file as the workflow evolves. Keep the "What was validated" record, and log every later change in
the changelog at the end.

## 1. Goal and status

Tom wants every example sentence in the dictionary to get a recorded MP3 reading made by a
text-to-speech (TTS) model. **The readings must be correct**, meaning every word pronounced as the
dictionary's furigana says, nothing missing, added or repeated. They must be checked **by AI
only**: Tom cannot listen to 120,000 clips. When an example has an MP3, the site shows a button
that plays it, in place of the current 🔊 button that uses the browser's or operating system's
speech synthesis (`tts-btn`, `build/entry_renderer.py` and `generate_tts_script()` in
`build/html_utils.py`). Voices rotate through two female and two male voices.

About 25% of Routine sessions should do this work. The workflow below was developed and
validated on 2026-09-24/25 in a local experiment and ported into je-dict-1 on 2026-09-25
(section 11).

### What was validated

- **Test set**: 100 dictionary examples chosen to be hard: 60 with a word whose furigana picks a
  less common reading (今日＝こんにち, 上手＝うわて, 明日＝あす, 私＝わたくし, 二十日＝はつか …), 11 with
  digits or Latin letters, and 29 covering dialogue, keigo, casual speech, long sentences,
  onomatopoeia, loanwords and counters. The real dictionary is easier on average (its sentences
  are also shorter: 21 kana against 25).
- **Final workflow ("v2")**, Gemini 3.8 Flash TTS, prompt E, voices Kore (female) and Charon (male),
  200 items (100 sentences × 2 voices): 191 passed the checks on the first attempt, 199 within 5
  attempts, 1 left for a human, and that one was correct. The same workflow with Gemini 3.8 Flash
  Lite TTS: 181 first time, 200 of 200.
- **Detection**: the v2 checks caught all 44 deliberately injected errors (wrong readings forced
  through kana; omitted, substituted, inserted and repeated words) and all 3 real errors Tom found
  by ear.
- **Human confirmation**: Tom rated 113 clips by ear. Every clip the v2 workflow accepted that he
  rated (83, deliberately the riskiest: accepted although one checker objected) was correct.
- **Not yet validated**: examples containing digits or Latin letters without hand-written
  readings (section 3.1); anything at scale. The two additional voices passed the pilot on
  2026-09-25 and wait for Tom's ear (section 5).
- **Cost**: about $0.0025–0.003 per example including regenerations and checks (Flash), a little
  less with Lite. For all 119,907 examples: roughly $300 with Flash.

## 2. The pipeline in one paragraph

For each example: (1) build the expected reading from the furigana; (2) build a TTS prompt in
which every word whose intended reading is not its usual one is written in hiragana; (3) generate
the audio; (4) check it with four AI checkers from three companies; (5) accept it, or regenerate
and check again, up to 5 attempts in all; (6) if no attempt passes, leave it without audio, record
it, and put it on a list for a human. Every step is deterministic code; no judgment by the session
model is needed except for choosing which entries to do and for the digits/Latin readings.

## 3. Expected reading

Strip the link markup `⟦display→lemma：id⟧` (keep the display text), then read the furigana
markup `{漢字|かな}`:

- **Displayed text** (`plain`): kanji bases, with the kana in between.
- **Expected reading** (`kana`): each `{base|reading}` replaced by its reading. Kana and katakana
  outside furigana are kept as they are.
- **Phonetic reading** (for the particle-aware check): the expected reading with the particles
  は, へ, を written as pronounced (わ, え, お). Particles are found with MeCab (fugashi +
  unidic-lite) in the displayed text: tokens with `pos1 == "助詞"` whose surface is は, へ or を.
  They never carry furigana, so they map one-to-one onto the reading
  (`phonetic_kana()` in `audio-reference/scripts/verify.py`).

Skip for now, and log, any example whose reading is not fully determined: kanji without furigana
(82 in the dictionary on 2026-09-24), malformed markup (8), and digits or Latin letters (2,514,
2.1%). These are furigana problems for the polish modes, except the digits and Latin letters.

### 3.1 Digits and Latin letters (open)

Furigana does not cover 3時, 1泊, 20%, NHK or Wi-Fi. In the test, their readings were written by
hand, with acceptable alternatives (`にじゅっパーセント|にじっパーセント`,
`エヌエイチケー|エヌエッチケー`). For production, generate them with a strong text model, asking for
every acceptable reading, and have a second model confirm. Then validate on a sample with Tom's ear
before trusting it. Until then, leave these 2.1% of examples on browser speech.

## 4. TTS generation

- **Model**: `google/gemini-3.8-flash-tts` through OpenRouter (`POST /api/v1/audio/speech`, body
  `{"model", "input", "voice", "response_format": "pcm"}`). `google/gemini-3.8-flash-lite-tts`
  works almost as well after regeneration and is about 30% cheaper per clip. Tom liked the Flash
  voices. The response is raw 24 kHz, mono, 16-bit PCM; the billed cost is looked up afterwards at
  `GET /api/v1/generation?id=<x-generation-id header>` (it can take a few seconds to appear).
- **Output differs on every call**, even for the same prompt. That is what makes regeneration work.
- **Encoding**: production uses **32 kbps** mono MP3 at 24 kHz (Tom's choice after listening,
  2026-09-25), encoded with `lameenc` (pip; ffmpeg is not installed in Routine sessions). About
  13 KB per clip. The local experiment used 64 kbps; the checks catch errors equally well at 32,
  48 and 64 kbps (changelog, 2026-09-25). The first 308 recordings were made at 48 kbps and stay
  as they are.

### 4.1 The prompt (strategy E, `kanadict` in the reference code)

```
# AUDIO PROFILE: Narrator for a Japanese-English learner's dictionary
## DIRECTOR'S NOTES
Style: Clear, natural, neutral standard Japanese (Tokyo accent) at a moderate pace suitable for learners. Read the transcript exactly once, adding and omitting nothing.
Pronunciation: Pronounce every word exactly as written in the READING line below. The READING line is only a pronunciation guide; do not speak it separately.
READING: {expected reading}
## TRANSCRIPT
{displayed text with rare-reading words in hiragana}
```

The transcript is the displayed sentence, except that a word is written in hiragana when **either**
(a) its furigana reading differs from what MeCab/UniDic reads for it in context, **or** (b) its
reading is not the most common reading of that spelling in the dictionary's own furigana (私 is
わたし 512 times and わたくし 11 times, so わたくし is written in kana). Regions are the smallest spans
on which furigana groups and MeCab tokens align, so okurigana stay with their word. A word right
after a digit (1泊, 3本) is left to the TTS. The reading index for (b) is built from all examples by
`extract_examples.py` (spelling → reading counts). Code: `kana_substituted(sentence,
dict_rule=True)` in `evaluate.py`.

How the prompts compared (share of clips flagged as likely errors on the first attempt, Flash / Lite):

| Prompt | Flash | Lite |
|---|---|---|
| A. Sentence only | 29% | 36% |
| B. Readings in parentheses after kanji | 20% | 25% |
| C. Director's notes + READING line | 12% | 18% |
| D. As C, kana chosen by MeCab only | 6% | 6% |
| **E. As D, kana also for the dictionary's minority readings** | **4%** | 6% |
| F. As E without the READING line | 6% | 6% |
| G. Whole sentence in kana | 6% | 8% |
| H. E's transcript with no instructions | 8% | 9% |

Lessons from the prompts:
- A plain English instruction in front of the sentence gets read aloud; the structured
  "director's notes" format does not.
- Telling the model a reading is much weaker than removing the ambiguous kanji.
- Whole-sentence kana (G) invites misparsing: in one clip, the particle は in には was read "ha".
- With a READING line the TTS occasionally reads the sentence twice (about 1%); the checks catch it.
- Some habits survive every prompt: わたくし sometimes comes out わたし, いいえ as いえ, ええと as えっと,
  and an extra を in 一目置いている. Regeneration usually gets a clean take.

## 5. Voices

Production voices are listed in `audio/config.json` (`voices`): **Kore** (female), **Charon**
(male), **Erinome** (female) and **Iapetus** (male), in that order, so consecutive examples
alternate female and male. Tom approved Erinome and Iapetus after listening on 2026-09-25.

Candidates piloted on 2026-09-25: **Erinome** (female; Google calls it "clear") and **Iapetus**
(male; "clear"). They were chosen after a gender and character probe of 15 voices, in which
gemini-3.8-flash described each voice. Puck, listed by Google as male, was heard as a woman,
so the probe is worth repeating for any new candidate. Pilot on the 100-sentence test set,
48 kbps, same day, same models:

| Voice | First attempt | Within 5 | Left for a human | GPT transcriber objections per attempt | Cost |
|---|---|---|---|---|---|
| Kore | 91 | 100 | 0 | 15% | $0.31 |
| Charon | 94 | 99 | 1 (いいえ ex4) | 16% | $0.30 |
| Erinome | 91 | 99 | 1 (いいえ ex4) | 24% | $0.31 |
| Iapetus | 92 | 100 | 0 | 13% | $0.30 |

Erinome is misheard a little more often by gpt-audio-mini, which costs regenerations but lets no
error through: the rule needs the particle-aware compare to pass. At 32 kbps the four voices
scored 92, 92, 91 and 87 on the first attempt and 100, 99, 100 and 99 within five (changelog).
Tom's listening page (20 sentences × 4 voices, plus a 32/48/64 kbps comparison) is a
private claude.ai artifact: https://claude.ai/artifact/NKwVgJejhrxzh4bvjcHccL. Other
candidates, if he dislikes these: female Aoede, Leda, Zephyr, Despina; male Orus, Alnilam,
Rasalgethi.

**Adding a voice**: run `python3 build/audio_pipeline.py testset --voice <Name>` (about $0.30;
the result is written to `audio/pilots.jsonl`), get Tom's approval of its sound, then add it
to `voices` and to `voice_gender`, alternating female and male (`["Kore", "Charon", "Erinome",
"Iapetus"]`). Production refuses to run while a listed voice has no acceptable pilot for the
current TTS model, prompt, bit rate and checkers (`audio_maintenance.py due`).

Rotation (`assign_voice()`): within each entry, the examples cycle through the voices in
order, starting at (entry number mod N). A learner reading one entry hears several voices.
A re-recording keeps its previous voice while that voice is in production.

## 6. The checks

Four checkers. All are called through OpenRouter `/chat/completions` with the MP3 as
`input_audio` (base64, format mp3), `temperature: 0`, `reasoning: {"effort": "low"}`.

1. **Particle-aware compare**, `google/gemini-3.8-flash` (`pcompare_prompt()` in `verify.py`):
   ```
   You will hear a recording of a Japanese sentence. The intended pronunciation, in kana, is:
   {phonetic reading}
   (Particles are written as they are pronounced: わ for the topic particle は, え for へ, お for を.)

   Listen carefully and check whether the speaker said exactly this. Report every difference: a word pronounced differently (for example a different reading of a kanji), a particle pronounced as written instead of as spoken (for example the particle は pronounced "ha" instead of "wa"), a word missing, added or repeated, the sentence read twice, or any extra speech. Ignore intonation, pitch accent, speed, voice quality, and long-vowel spelling.

   Reply with JSON only: {"differences": [{"expected": "…", "heard": "…"}], "match": true or false}
   ```
   With several acceptable readings, list them separated by " / " and say that all are acceptable.
   Verdict: mismatch if any reported difference survives normalization (kata→hira, NFKC, long
   vowels folded, ぢ/づ→じ/ず; **particles not folded**), or if `match` is false with no
   differences. Unparseable output counts as an objection.
2. **Hiragana transcription** by `google/gemini-3.8-flash`, 3. by `openai/gpt-audio-mini`, and
   4. by `thinkingmachines/inkling`, each with:
   ```
   Transcribe the Japanese speech in this audio exactly as it is pronounced, writing everything in hiragana (katakana only for loanwords). Do not use kanji, do not correct or normalize anything, and write any non-Japanese speech verbatim. Output only the transcription.
   ```
   Compare the transcription with the expected reading after normalization, folding は/わ, へ/え,
   を/お and long-vowel spellings (こう/こお, けい/けえ) on both sides, and converting Latin letters
   and digits to kana. Verdict: mismatch if it differs from every acceptable reading. A refusal
   ("I can't listen to audio") gives no verdict and counts as an objection. Code: `check()` in
   `evaluate.py`.

**Acceptance rule (v2)**: a clip is accepted if the particle-aware compare says match **and** at
most one of the three transcribers objects. Otherwise regenerate, up to 5 attempts in all.

Why this rule: the first version rejected a clip whenever any checker objected. Tom's ratings
showed that was far too strict: 26 of 51 correct clips were rejected. Each transcriber alone
mishears now and then, especially devoiced vowels (はつか heard as はっか, ひたい as したい, ごりやく as
ごりゃく). A single transcriber's objection was a false alarm in every case Tom rated. The
particle-aware compare was the strongest single check (it caught every known error), and the
"two of three transcribers" backup catches what it might miss.

What did **not** work, so don't reach for it again without new evidence:
- Ordinary speech-to-text models (13 tried: Google Chirp 3, gpt-transcribe, Qwen-ASR, Deepgram,
  AssemblyAI, …) are blind to readings: they hear こんにち, write 今日, and the error disappears
  (0–4 of 24 injected reading errors caught).
- Qwen3.8-Omni, Meta Muse Spark and Mistral Voxtral transcriptions were tried as an independent
  audit. They were noisy (they "correct" sentences, write kanji, drop text) and **wrong every
  time** they disagreed with the pipeline's checkers on clips Tom rated. Muse is also expensive.
  Xiaomi MiMo was too slow (about 10 s per clip).
- Multiple-choice checking ("which reading of 今日 did you hear?") works for readings but is blind
  to missing or added words.
- Comparing against the reading with は/わ folded (the first compare prompt) cannot catch a
  particle read as written. That is why the phonetic reading exists.

## 7. Storage and serving (decided 2026-09-25)

Constraints (GitHub documentation, September 2026): a GitHub Pages site may publish at most
**1 GB**; repositories should stay under 1 GB (5 GB is the strong ceiling); Pages has a soft limit
of 100 GB of traffic a month per site; **Git LFS files are not served by Pages**; the Pro plan
changes none of this. je-dict-1 is already about 3 GB and every Routine session clones it, so
**no audio goes into je-dict-1**. `build/check_no_binaries.py` enforces this in CI. The one
exception is the fixed regression set.

**Setup**: separate public repositories, each served by GitHub Pages from its `main` branch
(`.nojekyll` at the root), each kept under **900 MB** of live files (`limit_mb`):
`tkgally/je-dict-audio-1`, then `-2`, … The whole dictionary is about 1.5 GB at 32 kbps (about 120
hours), so three repositories. The stores are listed in `audio/config.json` (`stores`: id,
repo, `base_url`, `limit_mb`, `status` active/full). The site builds each URL as `base_url` +
path, so moving to a custom subdomain (for example `audio1.tkgje.jp`, a CNAME to
`tkgally.github.io`) or to another host means editing `base_url` only. `tkgally.github.io`
has no user site, so the default URLs are `https://tkgally.github.io/je-dict-audio-1/…`.
Browsers play MP3s from another origin without CORS headers.

**How a Routine session writes to it** (verified 2026-09-25): a session can push only to the
repositories attached to it. `add_repo` (owner, repo, access `push`) attaches one of Tom's
repositories mid-session, because his GitHub connection can push to all of them. `publish` then
makes a thin clone (depth 1, `--filter=blob:none`, no checkout, so no audio is downloaded),
adds the new files to the index with `git hash-object` / `update-index`, removes superseded
files, commits and pushes. Only after a successful push does it write the manifest in
je-dict-1. Pages deploys a few minutes later; `verify` waits for it.

Layout in the audio repository: `<range>/<example_id>.<sha256-of-mp3, 8 hex>.mp3` (range = entry
ID rounded down to 500, as in `entries/`, so a directory holds about 2,000 files at most),
`logs/<UTC time>.jsonl` (every attempt, verdict and transcript of each run: the detailed record
stays out of je-dict-1), `review/<page>.html` (spot-check pages). A re-recording gets a new file
name, so browser caches never serve a stale clip, and the old file is deleted from the
published tree. It stays in the audio repository's history, which is why clips are not
re-recorded without cause.

When a store fills, `publish` stops with a message. Tom creates the next repository with Pages
enabled, and a session adds it to `stores` as `active` and marks the old one `full`.

Alternatives considered: Cloudflare R2 (10 GB free, no egress fees) would need credentials in the
environment and a bucket Tom sets up. GitHub release assets cannot be uploaded from a
session (no REST access) and are served as downloads. jsDelivr on top of GitHub has per-repo
size limits. Pages is the one route that needs nothing but a repository.

## 8. Data model and staleness

je-dict-1 keeps text only, all under `audio/`:
- `manifest/<range>.jsonl`: one line per recorded example: `ex` (example ID), `h` (first 16 hex
  digits of `text_hash()` of its `japanese` field: SHA-256 of the text with link markup removed
  and furigana kept), `v` voice, `s` store, `f` path in the store, `d` seconds, `b` bytes, `at`
  publication time (UTC), `wf` workflow version, `tts` model, `n` attempts used, `obj` checkers
  that objected on the accepted attempt. Sharded by entry range so a run touches few files.
- `needs_human.jsonl`: examples no attempt passed, with the verdicts and diffs of every attempt.
  They are not retried while the text and the workflow version are unchanged.
- `runs.jsonl`: one summary line per production run (examples, first-pass, needs-human,
  objections per checker, cost, bytes, store use). `audio_maintenance.py drift` reads it.
- `pilots.jsonl`, `regression/history.jsonl`, `reaudits.jsonl`, `maintenance.json`: the
  maintenance record (§10).

The site build (`build/audio_manifest.py`, used by `render_examples()` in
`build/entry_renderer.py`) gives an example the recording button only when its manifest `h`
matches the current text. Otherwise the example keeps the browser-speech button, and
`plan` queues it again as *stale*, ahead of everything else.

Each example's `has_audio` field in the entry JSON mirrors the same test, for readers of the data:
it is true exactly when the manifest holds a valid recording of the example's current text.
`build/sync_audio_flags.py` sets it (`--check` reports without changing); `publish` runs it on the
entries just recorded and `make index` runs it on every entry, so an edited example goes back to
false in the same commit. It is derived data: the sync does not change `metadata.modified`, and
nothing in the build reads the field. The Recent page lists an entry as "REVISED (audio)" when a
recording of one of its examples was published after its last text change (manifest `at`).

## 9. The Routine's `audio` mode

- **Weight 0.25** in `pipeline/routine-config.json`; the other weights were scaled by 0.75
  (polish 0.22, accuracy-review 0.22, systemic-fix 0.19, new-entries 0.08, candidates 0.04).
  Simulated over 400 runs with today's signals, audio gets 26%. The mode is suppressed while
  `audio/config.json` `production.enabled` is false, and on days when less than
  $0.50 of the OpenRouter daily cap remains.
- **Budget** (raised by Tom on 2026-09-25): `openrouter.audio_session_cap_usd` = $4.80 per audio
  run, daily cap $7.50 shared with the other modes (an audio run changes no entry text, so it needs
  no self-check). At the measured $0.0024–0.0026 per example that is about 1,800 examples per
  run, about 25 minutes of `run` calls. The Routine runs every three hours (eight runs a day),
  so about two runs a day are audio runs; the $7.50 daily cap, shared with the accuracy review,
  is then the real limit, at roughly $3–5 of audio a day (1,200–2,000 examples). At that pace the
  basic and core tiers (20,000 examples) take about two weeks and the whole dictionary (about
  117,000 recordable examples) roughly three months.
- **Access**: a session can push only to repositories attached to it (the git proxy refuses the
  rest). Each audio run checks with `audio_pipeline.py check-access` before spending anything;
  if it cannot push and cannot attach the repository, it switches production off and tells Tom.
  When a Routine lists the audio repository among its repositories, `publish` uses that clone.
- **Per run** (`prompts/audio.md`): `make audio-deps` → attach the audio repository → maintenance
  (`audio_maintenance.py due`) → `plan` (priority order) → `run` (resumable, 8-minute calls, 12
  workers) → `publish` → `verify` → note examples left for a human → session log, metrics,
  `make gate`, `make index`, PR `routine(audio): …`, merge.
- **Priorities**: stale re-recordings; basic tier; core tier; general-tier entries the polish
  frontier has passed; the rest of the general tier. Entry order within each, and an entry's
  examples are never split across runs.
- **Not recorded**: digits and Latin letters (§3.1, about 2,500), kanji without furigana (82) and
  malformed markup (8). The last two are furigana errors, queued as the systemic-fix backlog
  item `audio-undetermined-furigana`.
- **Site**: an example with a valid recording shows a 🔊 button with a thin border that plays the
  MP3 (always visible; tapping again stops it). Other examples keep the browser-speech 🔊, shown
  only when a Japanese system voice exists. The voice is not shown.

## 10. Keeping it correct over time

`build/audio_maintenance.py` turns this section into checks that every audio run performs first
(`due`); `prompts/audio.md` §2 says what to do with each.

- **Regression suite** (`build/audio_regression.py`, `audio/regression/`, about $0.25): 163 clips
  with known answers. 50 have injected errors, of which 44 are audible; 113 were rated by Tom
  (3 errors, 2 unsure, the rest correct). Production clips Tom rates in spot checks join by URL.
  Pass = every audible injected error and every error of Tom's is rejected. Also watch the false
  alarms on Tom's correct clips: 8–13 of 108 is the run-to-run range of v2. **Blocking**: `plan`
  refuses to run when no passing regression exists for the current checkers and rule (a
  fingerprint of those settings). Any checker or rule change therefore forces a rerun.
  Otherwise the suite is due every 90 days, because models can change behind the same ID.
- **Pilot** (`audio_pipeline.py testset --voice V`, about $0.30 a voice): **blocking** when the TTS
  model, prompt strategy, bit rate or checkers changed since the last acceptable pilot of each
  production voice (`audio/pilots.jsonl`).
- **Model check** (every 30 days, free): configured model IDs still served? New TTS and audio-input
  models since the last check are listed. A retired model stops production until Tom approves a
  replacement.
- **Drift** (every run): first-pass rate, left-for-human rate and cost per clip of the last six
  runs against `baseline` in the config. Warnings go to `reviews/needs_curator.txt`.
- **Spot checks by Tom** (every 30 days once 200 new clips exist): `spotcheck --n 30` builds a
  page of recent clips, two thirds of them risky (a checker objected, or more than one attempt was needed).
  The page is published in the audio repository, with ✓/✗/? buttons and a JSON download.
  Tom uploads the file to `audio/spotchecks/`, and the next audio run imports it (`import-ratings`):
  every rated clip joins the regression suite, and a clip marked wrong is re-recorded and
  logged here as a miss.
- **Re-audit** (every 90 days once 500 clips exist, at most $0.40): 100 random valid recordings are
  re-checked with the current checkers. A rejected clip loses its manifest line and is re-recorded.
  When a clearly stronger checker appears, run the re-audit with it through a trial config.
- **Re-evaluation** (every 120 days, at most $1.50): look for newer TTS and checker models and try
  them on the test set or the regression suite through a trial config (`--config`). Record the
  result here even when nothing changes. Production models change only with Tom's approval.
- **Watch for**: rising first-pass failures, a checker starting to refuse audio, cost drift, and
  repeat offenders in `needs_human.jsonl`, which are often furigana errors worth fixing in the
  entry.
- **This file**: every change to the workflow gets a changelog entry below with its evidence
  (regression and pilot numbers).

## 11. Code and data in je-dict-1

Production code (ported 2026-09-25 from the research code; same logic, verified
identical on the test set, see the changelog):

- `build/audio_text.py`: markup parsing, expected reading, `text_hash()`, phonetic reading,
  prompt E (`kana_substituted()`, `build_tts_prompt()`), normalization. Pure; MeCab is loaded
  lazily so the site build can import it without the audio dependencies.
- `build/audio_checks.py`: checker prompts, scoring (`score_compare()`,
  `score_transcript()`), the acceptance rule (`accept()`), `run_checkers()`.
- `build/audio_api.py`: OpenRouter calls (TTS, audio-input chat, cost lookup) and MP3
  encoding (`lameenc`, or ffmpeg).
- `build/audio_pipeline.py`: `status`, `plan`, `run`, `publish`, `testset` (voice pilot),
  `undetermined`.
- `build/audio_regression.py`: reruns the checks on the regression clips (`make audio-regression`).
- `build/audio_manifest.py`: read side of the manifest for the site build (recording URL,
  newest recording of an entry for the Recent page).
- `build/sync_audio_flags.py`: sets the examples' `has_audio` from the manifest (§8).
- `build/tests/test_audio.py`: unit tests for the deterministic parts.
- `build/check_no_binaries.py`: CI gate; no audio file may be added to je-dict-1 outside
  `audio/regression/`.
- `audio/config.json`: models, checkers, rule, attempts, bit rate, voices, audio stores.
- `audio/testset/`: the 100 test sentences (hand-written readings for the digit/Latin ones),
  Tom's ratings, the particle test.
- `audio/regression/`: the 163 clips, `index.json` (clip, prompt, voice, known answer;
  `audible` marks whether an injected error survived into the audio), `history.jsonl` (one
  line per regression run) and `last_run.json` (every verdict of the latest baseline run).

Dependencies: `make audio-deps` (`build/requirements-audio.txt`: fugashi, unidic-lite,
lameenc, miniaudio, requests) and `OPENROUTER_API_KEY`. On the Routine's Debian Python,
unidic-lite only builds after `pip install -U setuptools`; the make target does that.

`audio-reference/scripts/` keeps the research code of the local experiment for reference
(prompt strategies A–H, the choice checker, the latent-class analysis). It is not used by
production.

## 12. Decisions for Tom

Open:
- **Spot checks**: monthly, about 30 clips (§10), unless Tom asks for a different rhythm.
- Flash (current) or Lite (about 30% cheaper, more regenerations): Flash, since Tom liked its
  voices.

Settled 2026-09-25: hosting on GitHub Pages in separate audio repositories (§7); four voices,
Kore, Charon, Erinome and Iapetus (§5); 32 kbps (§4); $4.80 per audio run and a $7.50 daily cap
(§9).

## Changelog

- 2026-09-25: first version (workflow v2), from the local experiment "20260924 Japanese TTS
  test for dictionary examples".
- 2026-09-25: ported into je-dict-1 (`build/audio_*.py`, section 11). Evidence that the port is
  faithful: on all 100 test sentences, prompt E's transcript and the phonetic reading are
  identical to the research code's (reading index rebuilt from the current dictionary); the
  scoring gives the same verdict on all 652 checker replies of the regression run. Regression
  run with the ported code: 44/44 audible injected errors caught, 3/3 of Tom's errors caught,
  8 false alarms on the 108 clips Tom rated correct, $0.25 (`audio/regression/history.jsonl`).
- 2026-09-25: the 6 inaudible injected clips are now labelled in `audio/regression/index.json`
  (`"audible": false`): うわて, ついたち, いちば, ごりやく, にっぽん (the TTS said the right reading)
  and しきし (the TTS said いろはら: wrong, but not the injected reading; the checks reject it).
  One run's own transcribers cannot decide audibility reliably (もっか was heard by only one
  of three), so it is fixed data now.
- 2026-09-25: the recording's text hash is SHA-256 of the example with link markup removed and
  furigana kept (`text_hash()`), not of the raw `japanese` field: the linker adds and removes
  links without changing what is said, and a hash over links would invalidate recordings for
  nothing. The manifest stores its first 16 hex digits.
- 2026-09-25: the particle-aware compare now lists alternative readings separated by " / "
  and says all are acceptable, as section 6 always described; the research code gave it only
  the first reading. Affects only examples with hand-written alternatives (none in
  production yet).
- 2026-09-25: bit rate. The regression clips re-encoded (decoded and encoded again, so worse
  than production) at 48 kbps and at 32 kbps, two runs each: 44/44 and 3/3 in all four runs;
  false alarms 8 and 13 (48 kbps), 11 and 9 (32 kbps) against 8 at 64 kbps. Run-to-run noise
  is of that size, so detection does not depend on bit rate down to 32 kbps. Production uses
  48 kbps (about 2.6 GB for the dictionary); 32 kbps (about 1.7 GB) is Tom's call after
  listening.
- 2026-09-25: voice pilot at 48 kbps (§5): Kore 91/100 first attempt and 100/100 within five,
  Charon 94/99, Erinome 91/99, Iapetus 92/100, $0.30 per voice. Kore and Charon together give
  185/200 first time, against 191/200 at 64 kbps in the local experiment; the final result is
  the same (199/200, いいえ ex4 left for a human both times). Erinome and Iapetus pass the
  numeric bar and wait for Tom's ear.
- 2026-09-25: end-to-end test on real dictionary examples (entry 00006 ある, 15 examples, basic
  tier): 14 of 15 passed first time, all 15 within two attempts, $0.041 ($0.0027 per example).
- 2026-09-25: Routine integration (§9): `audio` mode, weight 0.25; `prompts/audio.md`; storage in
  separate GitHub Pages repositories (§7); manifest and site button (§8); maintenance checks
  with blocking regression and pilot gates (§10, `build/audio_maintenance.py`).
- 2026-09-25: first production batch (310 examples, 33 basic-tier entries, Kore and Charon):
  307 accepted, 292 on the first attempt, $0.80 ($0.0026 per example). The three failures were
  all real problems. (1) Two examples contain the symbol ×, which has no furigana; the TTS read
  it ばつ or ばってん and the expected reading kept a literal ×. Symbols (Unicode category S:
  × ○ + ÷ = ℃, 32 occurrences) are now "undetermined" and skipped like digits. (2) Entry 00111
  had the furigana error {少|すこ}なくとも; all four checkers heard すくなくとも in five takes.
  The entry is fixed and re-recorded.
- 2026-09-25: the audio repository `tkgally/je-dict-audio-1` exists (Tom), and the first 308
  recordings are published there and in the manifest (entries 00006–00422, basic tier). They are
  served by GitHub Pages with `content-type: audio/mp3` and `access-control-allow-origin: *`.
  Production is enabled in `audio/config.json`, so the Routine's audio mode now takes part in
  the rotation.
- 2026-09-25: Tom listened to the voice page and to part of the first spot-check page ("they all
  sounded fine"; no ratings file). He chose 32 kbps and all four voices, and raised the budget to
  $4.80 per audio run and $7.50 a day.
- 2026-09-25: 32 kbps pilots, as the new bit rate requires: first attempt / within five, out of
  100 test sentences: Kore 92/100, Charon 92/99, Erinome 91/100, Iapetus 87/99 (いいえ ex4 is the
  sentence left over, as before). Iapetus scored 92 at 48 kbps the same day. The pilot bar had
  been "first attempt within 8 points of 95.5%", a baseline from a single 64 kbps run in the local
  experiment, so 87 missed it by one sentence. The eight pilots of the day range from 87 to 94,
  and one 100-sentence run varies by about ±3 points, so the baseline is now the measured mean,
  91.5% (bar 83.5%). The gate now judges each pilot against the current baseline
  (`pilot_acceptable()`), not by a flag stored when it ran. Iapetus's first-attempt misses were
  the usual ones (long vowels, いいえ said いえ, single-checker objections), and every one was
  caught and regenerated.
- 2026-09-25: second production batch, the first with four voices at 32 kbps and run as the
  Routine will run it (plan → run → publish from a fresh thin clone → verify): 800 examples from
  95 basic-tier entries (00426 読む – 00560 口), all 800 accepted, 761 on the first attempt,
  $1.94 ($0.0024 per example), 10 MB. 1,108 examples now have recordings.
- 2026-09-26: `check-access` (dry-run push, no cost) added as the first step of every audio run, after
  checking the Routine's settings: it runs every three hours with je-dict-1 as its only
  repository, and it is not certain that `add_repo` is available there. Verified both ways:
  push allowed to the attached audio repository; refused, with the proxy naming the fix ("add the
  repository to the session's sources"), for an unattached one. §9 pacing corrected for eight
  runs a day.
- 2026-09-26: `has_audio` in the entries is set from the manifest (`build/sync_audio_flags.py`,
  run by `publish` and `make index`; §8); it had been left false. The manifest's `at` is now the
  publication timestamp rather than the date (the 1,108 existing records got the time of their
  run from the audio repository's `logs/`), so the Recent page can place audio additions among
  text changes. The spot check compares its date part. No change to generation or checking.
