# Assessment, 23 October 2026: the Routine after the audio pass

Interactive session at Tom's request, with the Routine switched off: how the project is going,
whether the Routine's balance should change now that nearly every example has a recording, and
the decisions that have been waiting for Tom. The changes below were made in this session; the
decisions in §4 were not acted on.

## 1. Where the project stands

| | 23 Oct 2026 |
|---|---|
| Entries | 31,981 (540 added in the last two weeks, all internal-closure words) |
| Example sentences | 123,811 |
| Examples with a recording | 120,457 (97.3%) |
| Not recordable yet: digits or Latin letters | 2,590 (reading not given by furigana; AUDIO_WORKFLOW.md §3.1) |
| Held for a human by the audio checks | 727, in 594 entries |
| Waiting to be recorded (new or edited) | 37 |
| Polish frontier (sequential lane) | 11,581 of 32,204 |
| Accuracy review, second pass (with notes) | at 20,241; about 12,000 entries to go |
| Open routine PRs, orphan branches | none |

**Throughput.** Since 14 October the Routine fires every twelve hours (00:15 and 12:15 UTC)
instead of every three to six, and each run holds six to nine cycles: about 13 cycles a day,
down from about 30. The documentation still said "every three hours"; it now says twelve.

**What the cycles produced, 9–23 October** (270 cycles):

| Mode | Cycles | Entries changed | Notes |
|---|---|---|---|
| polish | 72 | 1,667 | about 23 entries per cycle |
| systemic-fix | 64 | 3,419 | one cycle in 64 changed nothing |
| accuracy-review | 44 | 306 | 368 reviewer flags applied, 1,262 rejected (22% precision) |
| audio | 39 | 0 | about 50,000 recordings; finished the first pass |
| new-entries | 27 | 642 | 540 new entries |
| conjugation-check | 13 | 3 | 12 of 13 cycles changed no entry |
| candidates | 10 | 0 | queue restocks |
| wiki | 1 | 30 | |

The machinery is in good shape: every cycle merged, nothing is stranded, the self-check and
the decision ledgers are being kept, and the accuracy review is still finding about three real
errors per hundred entries (wrong glosses, wrong translations, false claims in notes).

## 2. Findings

1. **Audio has almost nothing left to do at its old weight.** At 0.25 it would have taken a
   quarter of the cycles to record a few dozen examples each time. From now on its work is the
   examples that editing leaves behind (new entries' examples, and examples whose text changed),
   which accumulate at roughly 50–100 a day.
2. **The audio checks are an unused source of corrections.** 727 examples are "held for a
   human", and the plan was that Tom would listen to them. Nobody will listen to 727 clips, and
   most need no listening: in 642 of them the four checkers heard the same alternative reading at
   least six times, and in a sample of the top 40 about half were errors in the entry that every
   learner sees: 十四日 with じゅうよんにち, 毎月一回 with いちかい, 一週間 with いちしゅうかん,
   兄は私より二つ上 with {二|に}つ, 三十七度一度 for 三十七度一分, 上手い with じょうず, 取り越し苦労 with
   くろう, 縦横十メートル read じゅうおう. The rest are TTS slips on rare readings (明後日 みょうごにち,
   一昨年 いっさくねん) or acceptable variants (七時 なな/しち).
3. **The accuracy reviewer is old and cheap, and a stronger one finds much more.** The review
   still uses `google/gemini-2.5-flash` (about $0.60 per 1,000 entries). On 149 entries
   (19441–19590) that it had already reviewed in the second pass, and whose surviving flags had
   been adjudicated this morning, I ran four reviewers and judged every flag:

   | Reviewer | Entries flagged | Flags I judge correct | Cost per 1,000 entries (measured) |
   |---|---|---|---|
   | google/gemini-2.5-flash (current) | 4 | 0 of 5 | about $0.60 |
   | google/gemini-3.8-flash | 5 | 3 of 5 | about $2–3 |
   | openai/gpt-6.1-sol | 15 | about 12 of 15 | about $4.70 |
   | google/gemini-4-argon | 4 | 5 of 5 | about $4.60 |

   gpt-6.1-sol found, in entries the current reviewer had passed: 利害関係 glossed "conflict of
   interest" (that is 利益相反), 戦争体験者 translated "war veterans", 徳利 tagged food, 商う said
   to use 商 as ateji, 揺るぎない called the attributive form of 揺るがない, ときどき said to imply
   regular frequency, the pattern 〜が気が気でない presented as standard, アンテナ said to come from
   Portuguese, クリーニング said to mean only garment cleaning. A sample of 149 is small, but the
   difference is not: roughly one entry in twelve still has an error the current reviewer cannot
   see. This is now affordable, because audio no longer uses the daily budget (§4, D1).
4. **The conjugation check runs too often for what it finds.** Daily was one cycle in eight when
   the Routine ran four times a day; at two runs a day it is one cycle in twelve or thirteen, and
   12 of the last 13 found nothing to change.
5. **The systemic-fix queue is mostly tag hygiene.** Of its 17 open items, the largest are
   `tag-sole-general` (2,755) and `tag-sole-action-verb` (2,133). Tags help topic browsing but
   matter less to a learner than a wrong reading or gloss, so the new audio triage item goes to
   the front of the queue.
6. **Curator decisions stall for weeks.** `reviews/needs_curator.txt` holds items from 1–16
   October, and seven backlog items have been "needs-decision" since July and August, most of
   them house-style conventions (§4, D5).
7. **New entries feed themselves.** Each new entry's examples use words the dictionary lacks,
   which become candidates, which become entries: 540 entries in two weeks, increasingly
   specialized (素因数分解, 抵当権, 弦楽四重奏). That fits the internal-closure rule and Tom's goals,
   so I left the weight alone; it is worth watching.

## 3. Changes made in this session

- **Mode weights** (`pipeline/routine-config.json`, `pipeline/routine_next.py`): polish
  0.22 → 0.30, accuracy-review 0.22 → 0.26, systemic-fix 0.19 → 0.22, audio 0.25 → 0.10;
  new-entries 0.08 and candidates 0.04 unchanged. Simulated with today's signals over 1,200
  cycles: polish 32%, accuracy-review 28%, systemic-fix 23%, new-entries 13% (its seen-in-entry
  boost), candidates 4%. At 13 cycles a day that is about 4 polish, 3–4 accuracy-review and 3
  systemic-fix cycles a day.
- **Audio runs only when there is a batch worth a cycle**: suppressed while fewer than 150
  examples wait (new or stale), unless three days have passed since the last audio cycle with any
  waiting; doubled at 1,500 waiting (after a large fix that rewrites many examples). The selector
  reads the count from `audio_pipeline.py status` (four seconds; works without the audio
  dependencies). Expected: one audio cycle every two or three days.
- **Audio production switched back on.** The checker `thinkingmachines/inkling` answers again
  (`check-models`), and a 30-clip regression smoke test passed (24/24 audible errors caught).
  The three audio lines in `reviews/needs_curator.txt` were removed: both new stores are served by
  GitHub Pages, and `je-dict-audio-3` has about 890 MB free, so no further repository is needed
  for months.
- **Conjugation check every three days** instead of daily.
- **New systemic-fix item `audio-needs-human-triage`** (priority 5, first in the queue) with a
  read-only tool, `build/audio_needs_human_triage.py`: the held examples, most consistent
  mishearing first. A cycle fixes the furigana (the example then leaves the queue and is
  re-recorded) or records a `tts-error` / `ambiguous` verdict. Wrong headword readings still go
  to Tom. About 40 examples per cycle, so roughly six weeks of systemic-fix cycles.
- **Documentation**: the schedule (every twelve hours) in `CLAUDE.md`, `prompts/routine2.md`,
  `pipeline/run_clock.py`; the weights in `CLAUDE.md` and `AUDIO_WORKFLOW.md` §9; the triage in
  `prompts/audio.md` §5, `AUDIO_WORKFLOW.md`, `build/COMMANDS.md` and the cleanup backlog.
- **Spend**: this session's model calls (the reviewer calibration and the smoke test) came to
  about $5.74, recorded in `pipeline/openrouter-ledger.json` so today's cap stays honest.

## 4. Decisions for Tom

**D1. Accuracy reviewer: switch to `openai/gpt-6.1-sol`.** Recommended: yes, now, for the rest
of the second pass and the third pass, and for the self-check. Cost about $4.70 per 1,000
entries, about $150 for the whole dictionary, about $13 a day at three review cycles a day:
about what the daily cap has been spending on audio all October, inside the $15 cap you set.
Reviews would be sized to about 1,000 entries per cycle (the $5.50 per-cycle cap). I would check
its precision after the first 3,000 entries and report. Alternatives: `gemini-3.8-flash` (about
half the cost, fewer finds) or no change.

**D2. Six headword readings that the audio checks showed to be wrong** (each changes the romaji,
so `retire_entry.py rename`; the old URL redirects). Recommended: approve all six.
- 14297 軽やか: かるやか → かろやか
- 20142 一味違う: いちみちがう → ひとあじちがう
- 20226 役立たず: やくだたず → やくたたず (the standard reading; やくだたず noted as heard)
- 20732 真っ二つ: まふたつ → まっぷたつ, furigana {真|ま}っ{二|ぷた}つ
- 20854 欲深い: よくふかい → よくぶかい (both are in dictionaries; よくぶかい is the commoner; note よくふかい)
- 24323 最後尾: さいごび → さいこうび

**D3. Content rulings waiting in `reviews/needs_curator.txt`.** Recommendations:
- 02828 参考: drop `verb-suru` and the TRANSITIVITY section; teach 参考にする / 参考になる.
- 25822 演習曲: retire into 20962 練習曲 (the normal word for an étude).
- 06988 音符 / 07538 休符: switch to しぶおんぷ, はちぶおんぷ, じゅうろくぶおんぷ, にぶおんぷ (and the
  休符 equivalents); remove the link from 二分 to 二分 (にぶん, "halving"). The examples re-record
  automatically.
- 00290 文字 (もんじ): retire into 03632 文字 (もじ), with a line there that もんじ is an older
  reading.
- 00854 かける: add the sense "to multiply" (掛ける; 3に4をかける).
- 03906 冠: delete sense 2 ("top of the head") and its examples 5–7 (flagged twice).
- 09352 ため口 / 16740 タメ口: keep 16740 タメ口 (the usual spelling), retire 09352 into it; keep
  10777 タメ語 as its own short entry cross-referenced to タメ口.
- 17241 ひき肉 / 14783 挽肉: keep 17241 ひき肉 (the usual spelling), retire 14783, and name 挽肉 /
  挽き肉 in the notes.
- Candidate C23197 そうでないと: delete (30684 でないと already teaches it).

**D4. Readings for the 2,590 examples with digits or Latin letters** (3時, 20%, NHK). Recommended:
approve a one-time interactive project: a strong text model writes every acceptable reading, a
second model confirms, and you listen to a 30-clip sample before production uses them
(AUDIO_WORKFLOW.md §3.1). Model cost under $10; the recordings about $7.

**D5. Conventions stalled in the backlog since July–August.** Recommendations:
- Auxiliary verbs (〜ていく, 〜てくる, 〜てみる, 〜ておく) in kana in examples; kanji only for main
  verbs (持って来る as "bring" stays). This is the standard modern convention.
- Line-initial ・ bullets in notes (18,272 lines in 2,524 entries) → `- `, as a mechanical sweep
  limited to line starts in notes.
- Inline links for ください use the kana base form (85% already do).
- Words about language (名詞, 動詞, 音読み, 訓読み, 敬語) take the semantic tag `language`;
  `grammatical` stays for words that do grammatical work (particles, auxiliaries).
- Compound-verb notes that open with a negative / te-form / past triad (37 entries): remove the
  triad (the conjugation tab shows it).
- The seven spelling-variant pairs (捻る/捩じる, 焼き立て/焼きたて, 翳む/霞む, 追い掛ける/追いかける,
  控え目/控えめ, 見積り/見積もり, the two とき): keep the commoner spelling, retire the other.
- **A standing rule** that would keep this queue from refilling: the Routine settles
  house-style, tagging and markup conventions itself (recording the ruling in the relevant skill
  file and the decision in the backlog), and retires an entry into another when the two are the
  same word in the same reading and meaning, differing only in spelling. You would still decide
  readings that change an ID, retirements that are not pure spelling duplicates, and questions
  of sense and content. Recommended: yes.

**D6. Schedule.** Since 14 October the Routine runs every twelve hours, about 13 cycles a day.
At that pace the polish frontier needs more than a year to reach the end of the dictionary; the
accuracy review would cover the dictionary with the new reviewer in about two weeks of budget.
If the change was to save usage, nothing needs to change. If not, running every six hours again
(or letting each run go to about four hours in `pipeline/run_clock.py`) would roughly double
throughput with no other change. Your call; I made no change.
