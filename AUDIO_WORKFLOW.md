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
- **Not yet validated**: the two additional voices (section 5); examples containing digits or Latin
  letters without hand-written readings (section 3.1); anything at scale.
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
- **Encoding**: the test used 64 kbps mono MP3 (ffmpeg, libmp3lame). For storage, 32–48 kbps mono is
  probably enough for speech (section 6); check that it still sounds clean before switching. If
  ffmpeg is not available in the session, the pip package `lameenc` encodes MP3 in pure Python.

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

Validated: **Kore** (female) and **Charon** (male). Tom wants **two female and two male voices** in
rotation. Candidates among Gemini's prebuilt voices: female Aoede, Leda, Zephyr; male Puck, Orus,
Fenrir. Check the current voice list, and whether each voice is female or male, before choosing.

**Before any new voice is used in production**, run the full v2 pipeline on the 100-sentence test
set (`audio/testset/sentences.json`) with that voice (`python3 build/audio_pipeline.py testset --voice <Name>`) (about $1 per voice). Accept the
voice if its first-pass and final acceptance rates are close to Kore's and Charon's, and if Tom,
listening to about 20 of its clips, is satisfied with the sound. A voice that misreads more often
only costs more regenerations, but a voice the checkers hear less clearly would weaken the checks,
so compare the checkers' objection rates too.

Rotation: assign voices deterministically, so that a regenerated clip keeps its voice. For example,
within each entry cycle through the four voices in example order, starting at (entry ID mod 4).
That way a learner reading one entry hears several voices.

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

## 7. Storage and serving (must be solved before production)

Constraints (GitHub documentation, September 2026; check again):
- A GitHub Pages site may be at most **1 GB** published. The source repository should stay under
  1 GB, with 5 GB strongly recommended as the ceiling. Soft bandwidth limit: 100 GB a month per
  site. The Pro plan does not change these.
- **Git LFS files cannot be served by GitHub Pages.**
- je-dict-1 is already about **3 GB** (GitHub API `size`, which is in KB). Every Routine session
  clones it, so **do not commit audio to je-dict-1**.
- GitHub sets no limit on the number of files in a repository, and files over 100 MB are blocked
  (not a concern for clips of about 30 KB). About 120,000 files in one repository is manageable,
  but keep them in subdirectories (for example by the entry ID's range of 500, as `entries/` does)
  so that no directory holds more than about 1,000 files.
- The whole dictionary is about **120 hours** of audio (mean about 3.6 s per example): about
  3.5 GB at 64 kbps, 2.6 GB at 48 kbps, 1.7 GB at 32 kbps.

Recommended: **separate public audio repositories**, each published with GitHub Pages and kept
under about 900 MB. When one fills, start the next (`je-dict-audio-1`, `-2`, …). Point a custom
subdomain at each, such as `audio1.tkgje.jp` (Tom needs to set this up in DNS), or use the
`tkgally.github.io/<repo>/` URLs. The site's `<audio>` or `new Audio(url)` can play MP3s from
another origin without CORS headers. Alternatives, if the GitHub-only route proves awkward:
Cloudflare R2 (10 GB free, no charge for downloads; needs credentials in the environment), or
another static host. Discuss with Tom before choosing.

Things to verify in the first session:
- **Can a Routine session push to a second repository?** It is connected to je-dict-1, and the
  GitHub MCP tools may or may not reach other repositories, or accept binary files.
- If not, the fallback is to generate in the session, then hand the MP3s to a GitHub Actions
  workflow that pushes them to the audio repository with a token stored as an Actions secret (Tom
  would add it). Keep the MP3s out of je-dict-1's history.
- Replacing a file in a git repository keeps the old version in history, so name files by content
  hash (`<example_id>.<hash8>.mp3`) and avoid rewriting the same clip over and over. The hash in
  the name also keeps browser caches correct.

## 8. Data model and staleness

Examples change: the polish modes edit them. A recording is valid only for the exact text and
reading it was made from.
- Keep a manifest in je-dict-1, small text only, for example `audio/manifest.jsonl`, one line per
  recorded example: example ID, voice, TTS model, prompt strategy, workflow version, SHA-256 of
  the example's `japanese` field (the markup with furigana, since readings matter), audio URL,
  duration, date, and the checkers' verdicts. The existing `has_audio` field on each example can
  mirror it, but a manifest avoids touching thousands of entry files (and their CI gates).
- The site build attaches an MP3 to an example only when the manifest's hash matches the example's
  current text. Otherwise it falls back to browser speech, and the example goes back into the
  queue.
- Keep a separate log of items left for a human, and of skipped examples with the reason.

## 9. Folding it into the Routine

Suggested shape, for the session that integrates this to decide:
- A new mode, `audio`, with weight about 0.25 in `pipeline/routine-config.json` (Tom's request),
  with the other weights scaled down.
- **Budget**: OpenRouter caps are currently $2.50 a session and $5 a day, shared with the
  accuracy review. At about $0.003 an example, one session can record about 500–800 examples.
  Agree an audio budget with Tom; he may want to raise the caps. Record spending per run as the
  other modes do.
- **Order**: the session decides. Reasonable priorities: basic and core tiers first (their
  entries are the most visited and most stable), then general-tier entries by traffic
  (GoatCounter) or by how recently they were polished (recently polished text is less likely to
  change again).
- **Per run**: pick entries → build expected readings (skip the undetermined ones) → generate and
  check with the v2 rule, running calls in parallel → upload the accepted MP3s → update the
  manifest → log items left for a human → build and push as usual. The pipeline is I/O-bound:
  400 items took about 20 minutes with 10–16 parallel workers.
- **Site change** (once): examples in the manifest get a play button for their MP3; everything
  else keeps the 🔊 browser-speech button. Consider a visible sign that a recording exists, and
  show which voice it is only if Tom wants that.

## 10. Keeping it correct over time

- **Regression suite**: `audio/regression/` holds 163 clips with known answers:
  50 with injected errors, and 113 rated by Tom (3 errors, 2 unsure, the rest correct), plus
  `index.json`. Run it with `python3 build/audio_regression.py`. Before changing any part of the workflow
  (a new TTS model, a new checker or checker model, a prompt edit, a rule change), run the checks
  on these clips. The changed workflow must still catch all 44 audible injected errors (6 of the
  50 turned out inaudible: the TTS "corrected" them) and all 3 of Tom's errors. Its false-alarm
  rate on Tom's correct clips should not rise much.
- **Spot checks by Tom**: about once a month, or after any workflow change, sample about 30
  recently accepted clips, biased toward risky ones (a checker objected, the sentence has a
  minority reading, a new voice). Present them on a simple review page with ✓/✗ buttons and an
  export, like the review site of the local experiment (not included here; Tom has it). Add his
  verdicts to the regression suite.
- **Re-audit**: when a clearly stronger audio model appears, re-check a sample of existing
  recordings with it, and regenerate any it rejects that the current checkers also doubt.
- **Revisit** every few months: model IDs change or are retired; prices change; newer TTS models
  may need fewer tricks (retest prompts A–H on the test set); newer checkers may make the rule
  stricter or cheaper. The test set and code make each retest about an hour and a few dollars.
- **Watch for**: rising first-pass failure rates (a model update), a checker starting to refuse
  audio, cost per example drifting, and repeat offenders (examples that are always left for a
  human). The last are often furigana errors, which are worth fixing in the entry.

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

- Flash (slightly more accurate first time, the voices he liked) or Lite (about 30% cheaper)?
- Which two additional voices, after hearing samples?
- Where the audio is hosted (section 7), and a subdomain if wanted.
- The audio budget, and whether to raise the OpenRouter caps.
- Whether to spot-check monthly (section 10).

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
