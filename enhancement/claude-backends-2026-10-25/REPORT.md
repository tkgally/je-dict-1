# Can Claude on the subscription replace the OpenRouter models? (25 October 2026)

**Question (Tom):** the Routine pays OpenRouter for every non-audio model check: the accuracy
review, the self-check after each cycle, the kana-link review, the conjugation check and candidate
brainstorming. Could Claude subagents or headless Claude (`claude -p`, billed to the Max
subscription instead of per token) do this work as well or better, and what would it cost in
money, quality, subscription usage and time?

**Short answer:** yes for one model and no for the other two. **Claude Opus 5.5, called headless
once per entry, is as good an accuracy reviewer as gpt-6.1-sol, and it finds a different quarter of
the errors.** Sonnet 5.5 and Haiku 5.5 are not good enough for the accuracy review: they find a
fifth as many errors. Subagents and batched calls lose most of the gain. The OpenRouter bill
outside audio is only about $10–11 a day, almost all of it the accuracy review. So the real choice
is whether to save about $300 a month by moving that review to Opus, or to keep sol and add Opus
as a second reviewer, which catches more errors and uses the subscription you are not using. I
recommend the second, with the details in §6.

Nothing in the dictionary or on `main` was changed. Everything below is in this directory.

---

## 1. What runs on OpenRouter today (outside audio)

Spend per day from the Routine's spending log since the reviewer change on 23 October:

| Job | Model now | Spend per day | Share |
|---|---|---|---|
| Accuracy review (glosses, translations, tags, notes; about 1,500 entries a day) | openai/gpt-6.1-sol | $8–10 | ~88% |
| Self-check of the entries each cycle changed (same review) | openai/gpt-6.1-sol | ~$1 | ~9% |
| Candidate brainstorming | gpt-6.1-sol + gemini-3.8-flash | ~$0.13 | ~1% |
| Kana-link review (is this あげる really the linked entry's word?) | google/gemini-2.5-flash | a few cents | <1% |
| Conjugation-table check (every three days) | gpt-6.1-sol | ~$0.3 a run | <1% |

So almost all the money is in one job, the accuracy review. That job got the most testing.

## 2. How headless Claude was called

`claude -p` with our own one-line system prompt and nothing else: no tools, no MCP servers, no
project settings, no saved session (`claude_backend.py`). Each call carries about 1,300 tokens of
fixed overhead and starts a CLI process that uses about 1.5 seconds of CPU. It runs on the
subscription the container is signed in with, so the Routine's cloud sessions can use it with no
API key. Subagents were tested through the Agent tool from this session.

## 3. Accuracy review: the main test

**Test set.** 200 entries from the last two accuracy sweeps (entries 21514–22473), each exactly as
the reviewer saw it, recovered from git. 114 of them are entries where sol raised at least one
flag (127 flags, and the Routine accepted and fixed 118 of them); 86 are a random sample of
entries sol passed.

**Reviewers.** All used the production prompt and the production filters, so only the model
differed: sol rerun on OpenRouter; Haiku, Sonnet and Opus headless, one entry per call; the same
three with a "tuned" prompt (§3.3); Sonnet and Opus with 10 entries per call; Sonnet and Haiku as
subagents given 20 entries each (40 entries in all).

**Judging.** Every flag from every reviewer was pooled, shuffled and stripped of its source, and
two judges from different model families (Opus 5.5 headless and google/gemini-4-argon) ruled each
one valid or invalid and grouped flags that point at the same problem. A flag counts as valid
below only when **both** judges called it valid. Both judges were lenient (they called 95% of all
709 flags valid), so precision barely separates the reviewers; **the useful measure is how many
of the real problems each reviewer found** (148 distinct problems were found by at least one
reviewer). I checked the judges by hand on a blind stratified sample of 30 problems (§3.4).

### 3.1 Results

| Reviewer | Flags | Real problems found (of 148) | Share found | Precision |
|---|---|---|---|---|
| **sol (this rerun)** | 117 | 102 | **69%** | 91% |
| **Opus, tuned prompt, keeping "warn" flags** | 119 | 99 | **67%** | 96% |
| Opus, production prompt, keeping "warn" flags | 103 | 90 | 61% | 97% |
| Opus, tuned, as production filters it (drops "warn") | 81 | 69 | 47% | 100% |
| Opus, tuned, 10 entries per call | 78 | 70 | 47% | 99% |
| Sonnet, tuned | 32 | 29 | 20% | 97% |
| Sonnet, production prompt | 33 | 27 | 18% | 82% |
| Sonnet, 10 entries per call | 17 | 16 | 11% | 100% |
| Haiku, tuned | 33 | 28 | 19% | 85% |
| Haiku, production prompt | 20 | 16 | 11% | 80% |
| Sonnet subagent (40 entries) | 3 | 3 | 12% of its 40 | — |
| Haiku subagent (40 entries) | 2 | 2 | 8% of its 40 | — |

**sol and Opus each find about two thirds of the problems, and not the same two thirds.** 75
problems were found by both, 27 only by sol, 24 only by Opus. Together they find 126 of 148
(85%). Neither run is complete on its own: even sol run twice on the same entries found 98 problems
both times, 15 only the first time and 4 only the second.

**The test set favours sol**, because 114 of its 200 entries were picked for having a sol flag.
On the 86 entries sol had passed, the reviewers found 14 real problems between them: Opus found
10 and the fresh sol run found 2. A sample that small proves little, but it is what a second
reviewer is for: Opus catches what sol misses. Examples of problems only Opus found:

- 公認会計士: the notes call the CPA exam one of the three hardest national exams "alongside the bar
  exam and the medical exam". The usual trio is 司法試験, 公認会計士 and 不動産鑑定士; the medical
  licensing exam has a pass rate near 90%.
- 加えて: the notes rank it "less formal than さらに", which is the wrong way round.
- 区役所: the notes limit it to designated cities; Tokyo's special wards have 区役所 too.
- 鳥小屋 glossed "birdcage" (that is 鳥かご); 日例 offered as a word for a daily regular event;
  体に無理する given as a collocation (体に無理をさせる is the natural form); 都合 called informal;
  いかに said to express manner rather than degree (いかに大切か); 勇ましい called "more literary".

And only sol: 寝坊 said to name only the act, not the person (お寝坊さん); 立ち会う's example
弁護士が立ち会いのもとで (should be の); 宗家 translated "founding school"; 貫通する called only
intransitive (弾丸が壁を貫通する); 中断 said to imply a deliberate stop. Found by both: 消却 given for
amortization in the notes of 焼却 (that is 償却), 無色 glossed "transparent", 転勤 limited to company
employees, 調印する limited to treaties.

### 3.2 Why Sonnet and Haiku fall short

They are not short of thinking time. Sonnet at its maximum effort setting spent about 2,400
reasoning tokens per entry and still flagged 2 of the 12+ problems sol had found in the same 12
entries. They read the prompt's warnings ("most entries are correct", "do not report claims merely
simplified for learners") as permission to pass overstatements such as "used exclusively for
precipitation" or "神経科 is exclusively neurology". Opus does too, to a lesser degree.

### 3.3 Two adjustments Opus needs

- **Keep its "warn" flags.** The production filter drops every flag the reviewer marks "warn",
  because gemini-2.5-flash's warns were about 1% right. sol marks everything "error". Opus marks
  a third to a half of its flags "warn", and about 90% of those were real. With the filter as it
  is, Opus would lose 30% of its finds.
- **The tuned prompt** adds one paragraph listing the kinds of error the Routine has been accepting
  (an "only"/"exclusively"/"never" the language does not have; a false statement about a
  neighbouring word; a gloss that reverses who does what; a translation that shifts meaning; a
  wrong etymology). It raised Opus from 61% to 67% and Haiku from 11% to 19%, and left Sonnet
  where it was. The categories come from the Routine's past decisions, not from this test set,
  but they describe the kinds of error sol flags here, so part of the gain may not carry over.

### 3.4 Hand check of the judges

I judged 30 problems myself without seeing who raised them: 12 found only by sol, 12 only by Opus,
6 by both. My verdicts: Opus-only 10 real and 2 borderline (滑走 glossed "taxiing", 数え年 and 還暦);
sol-only 8 real, 2 borderline (鉱石, 人名) and 2 wrong (body-part on 涼しい顔 is defensible, and
四拍子 has no established figurative use like 三拍子揃う); both 6 of 6 real. So the judges are somewhat
generous, but they do not favour either reviewer, and Opus's own finds hold up at least as well
as sol's.

### 3.5 Subagents and batching

Batching costs most of the gain. With 10 entries per call, Opus fell from 67% to 47%; subagents
reviewing 20 entries in one go found 2–3 problems in 40 entries. Subagents were not cheaper
either: 81,000–93,000 tokens per 20 entries, about the same per entry as one headless call per
entry, and their output passes through the Routine's own context. **One headless call per entry
is the right way to do it.**

## 4. The other jobs (labeled test sets from the 10 October study)

The 10 October decision-model study left labeled test sets (1,444 items with known right
answers) and OpenRouter scores for four models. The same sets, with the same batched prompt (20
items per call), were run through headless Claude. Accuracy:

| Task | gemini-2.5-flash | gpt-6.1-sol | Haiku via OpenRouter (10 Oct) | Haiku headless | Sonnet headless | Opus headless |
|---|---|---|---|---|---|---|
| Kana links (right entry or a homophone?) | 0.66 | 0.86 | 0.84 | 0.82 | 0.76 | **0.86** |
| Conjugation forms | 0.87 | 1.00 | 0.99 | **1.00** | 0.98 | 1.00 |
| Furigana readings | 0.95 | 0.99 | 0.97 | **0.99** | 0.89 | 0.99 |
| Translation matches the Japanese | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 |
| Transitivity | 0.81 | 0.93 | 0.90 | 0.91 | 0.82 | **0.94** |
| Which sense is used | 0.96 | 0.97 | 0.95 | 0.96 | 0.97 | 0.96 |
| Should this review flag be applied? | 0.51 | 0.59 | 0.60 | 0.61 | 0.55 | 0.60 |

- **Kana-link review** today uses gemini-2.5-flash, the weakest model here (0.66). Headless Opus
  matches sol (0.86) and Haiku comes close (0.82). This is the clearest quality gain on offer,
  and it costs almost nothing either way.
- **Conjugation check**: headless Haiku is perfect on this set, as sol is. Moving it saves only
  cents.
- **Sonnet 5.5 is surprisingly weak** on links, furigana and transitivity, often below Haiku. I
  would not use it for checking work.
- No model can yet decide whether a review flag should be applied (all near 0.6). That judgement
  stays with the Routine's own reading.

**Brainstorming** (one 20-headword seed batch and the insect field, with the same prompt for every
model; new proposals judged blind by Opus and gemini-4-argon):

| Model | Seed batch: new words accepted by both judges | Insect field: new words accepted by both judges | Words no other model proposed |
|---|---|---|---|
| gpt-6.1-sol | 10 | 21 | 9 |
| gemini-3.8-flash | 8 | 26 | 10 |
| Opus headless | 9 | 21 | 6 |
| Sonnet headless | 10 | 17 | 6 |
| Haiku headless | 7 | 0 (it mostly proposed insects already in the dictionary) | 1 |

Opus and Sonnet do about as well as sol, but the Routine's own Opus already brainstorms first,
and the point of the outside models is to come at the question differently. Each batch costs
about $0.08 on OpenRouter. Nothing to gain here.

## 5. Costs, subscription usage and time

**Money.** Moving the accuracy review and the self-check to Opus would save about $9–11 a day,
roughly $300 a month. Moving everything else saves under $10 a month.

**Subscription.** Headless calls report list-price-equivalent cost, which is not billed on Max but
shows how much of the plan's allowance they use. One accuracy review by Opus costs about $0.04 an
entry at list price (about 4,100 tokens in, 350 out), against sol's $0.0056. The Routine's daily
1,500 entries would therefore use about $60 a day of list-price-equivalent Opus usage.

The CLI also reports the plan's rate-limit windows. Over this whole experiment (about $40 of
list-equivalent Claude usage, plus this session itself) the five-hour window went from 5% to 10%
and the seven-day window from 13% to 14%. So one point of the five-hour window is roughly $8 of
list usage. The seven-day number moves in whole points, too coarsely to measure well; the best
estimate is that the Opus accuracy review would use something like 10–20% of the weekly
allowance. Two cautions: the container reports the limit type as `ccr_promotional`, so cloud
sessions may be drawing on a promotional pool whose size could change; and **the Routine's own
sessions draw on the same subscription**, so a review that exhausts a window also stalls the
Routine. A production version must read the windows before each batch and stop at a threshold.
`usage_probe.py` shows how.

**Time.** About the same. Opus headless averages 6 seconds per call and sol 4.5; with six parallel
calls, 200 entries take about four minutes either way, so a 600-entry cycle takes about 12
minutes. The container has four CPUs, so more than about six simultaneous `claude` processes
make every call slower.

**Other differences.** Headless Claude has no temperature setting, so runs are not repeatable
(sol's are not entirely either: it found 15 different problems on its second run). There is no API
key to manage and no daily dollar cap; the subscription windows take the cap's place.

## 6. Recommendation

1. **Accuracy review: keep sol and add Opus headless as a second reviewer** on the same entries,
   with the tuned prompt and its "warn" flags kept. The two together found 85% of the known
   problems, against 69% for sol alone, at no extra money and an estimated 10–20% of the weekly
   subscription allowance. If you would rather save the ~$300 a month, Opus alone is as good as
   sol alone, but each misses errors the other catches, and the dictionary was written by Claude:
   a reviewer from another model family is the safer single choice.
2. **Self-check after each cycle: keep sol.** It checks work Claude just did, so a different model
   family is the point, and it costs about $1 a day.
3. **Kana-link review: switch from gemini-2.5-flash to headless Opus** (or Haiku, for almost no
   subscription use). This is a quality gain, not a saving.
4. **Conjugation check: optional switch to headless Haiku.** Equal quality, saves cents.
5. **Brainstorming: leave as is.**
6. **Do not use subagents or Sonnet 5.5 for checking work, and do not batch entries.**

If you want any of this, the change is small: a `--backend claude` option in
`review_runner.py`'s call function (the code is `claude_backend.py` here), the tuned paragraph and
`--keep-warn` for Claude in `review_accuracy.py`, a rate-limit guard, and Routine prompt edits. I
have not made any of these changes.

## 7. Spend

OpenRouter: about $2.40 today (sol rerun $1.12, gemini-4-argon judging $0.75, brainstorm calls
$0.16). This is **not** in the Routine's spending log, because that log lives on `main`. Today's log
showed $5.57 of the $15 cap when I started, so there is room, but the Routine will
underestimate today's spend by about $2.40. Subscription: about $40 of list-equivalent usage, as
above.

## Files

| File | What |
|---|---|
| `build_accuracy_set.py` → `sets/accuracy.jsonl` | the 200-entry test set (entry as reviewed, sol's flags, the Routine's decisions) |
| `claude_backend.py` | headless Claude as a drop-in for the OpenRouter call |
| `run_accuracy.py` | runs a reviewer with the production prompt and filters (`--tuned`, `--batch`) |
| `subagent/`, `convert_subagent.py` | subagent inputs, outputs and token/time figures |
| `judge.py`, `score_accuracy.py` → `accuracy_summary.json` | blind two-judge adjudication and scoring |
| `spot/` | the 30-problem blind hand check (`blind.txt`, `key.json`) |
| `run_sets.py` → `sets_summary.json` | the 10 October labeled sets through headless Claude |
| `run_brainstorm.py`, `judge_brainstorm.py` → `brainstorm_summary.json` | brainstorming comparison |
| `usage_probe.py`, `logs/usage.jsonl` | subscription-window readings during the experiment |
| `results/` | raw per-entry and per-item results |
