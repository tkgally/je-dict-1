# Can TypeSafe's Jev model help the Routine? An evaluation (2026-09-22)

**Question from Tom**: TypeSafe AI released a model called Jev (`typesafe/jev-1.13` on
OpenRouter). Could it be used productively for the Routine's regular work, for example to check
furigana? Test it, spending up to $5.

**Short answer**: Jev is very cheap and fast, but its Japanese is not good enough for the checks
the Routine most needs. It is clearly worse than the current reviewer (Gemini 2.5 Flash) at
furigana, roughly equal and weak at spotting the real translation, gloss and notes errors that
remain in the dictionary, and it has a blind spot on the commonest kana-link mistake. It is
genuinely good at two narrow, structured judgments: whether a semantic tag names a domain a
word plainly does not belong to, and which numbered sense of an entry an example illustrates.
Both are worth using as cheap sweeps; neither changes how the Routine works. Total spend for the
evaluation: about $0.95 of the $5 (about $0.22 on roughly 8,000 Jev calls, about $0.72 on Gemini
baselines run on the same items).

Every number below was measured in this session; the scripts and headline figures are in
`enhancement/jev-eval/`.

---

## 1. What Jev is, in this project's terms

Jev does not write anything. You send it a piece of text (or a JSON object) and a set of typed
questions, and it returns one answer per question: a yes/no probability ("noul"), a choice from
options you supply with a probability for each, or a level on a rubric you supply. Its docs say
it is optimized for English and that CJK text is "handled but not equally well." It is served on
OpenRouter through a separate endpoint (`POST /api/alpha/decisions`); the usual chat endpoint
rejects it. Pricing is $0.042 per million input tokens and nothing for output, so a call that
checks one example sentence costs about four thousandths of a cent. Median latency in this
session was 0.43 seconds; eight parallel workers ran without a single rate-limit error.

Because there is no text, there is nothing to parse, no JSON to repair, and no prose noise to
filter. The price of that is that Jev cannot say *what* is wrong or *why*: a flag from it is a
number, and something else (the Routine's own model, or Tom) has to open the entry and look.

## 2. The tests

Each test used the project's own data as ground truth where it existed, and controlled
injected errors where it did not. Gemini 2.5 Flash, the model the Routine already uses, was run
on the same items wherever a like-for-like comparison mattered.

### 2.1 Furigana readings (the use Tom suggested)

**Set**: 890 kanji-reading pairs from real example sentences. 320 are correct as they stand; 150
more are correct pairs taken from entries where Gemini or GPT had earlier raised a furigana flag
that turned out to be false (hard cases: rendaku, unusual compound readings); 420 have a wrong
reading injected, seventy of each kind: a different reading the same kanji string takes elsewhere
in the dictionary (行う read こう), a voicing change (工場 read ごうじょう), a dropped or added long
vowel (飛行機 read ひこき), a small-kana slip (決定 read けつてい), okurigana pulled into the
reading (増える written {増|ふえ}える), and a nonsense reading.

**Result**: asked one pair at a time with the sentence and its translation, Jev separates wrong
from correct with an AUC of 0.88. Set to flag when it puts the chance of error at 70 percent or
more, it raised zero false flags on the 470 correct pairs and caught 25 percent of the injected
errors; at 50 percent it caught 40 percent with four false flags. The nonsense readings were
caught almost every time (AUC 0.99); the realistic kinds sat at 0.83 to 0.92. Asking about every
pair in a sentence in one call (the way a sweep would run) gave the same accuracy at a third of
the cost. On a further 1,500 untouched sentences (5,574 pairs), it flagged nothing at the
70 percent setting and 7 pairs at 50 percent, all of them correct on inspection.

Gemini 2.5 Flash, asked the same one-pair question, caught **70 percent** of the injected errors
with **zero** false flags on the same 470 correct pairs, including all 150 hard ones. So on
furigana the current model is nearly three times as effective at the same precision.

A second test explains why. For 400 kanji strings that take more than one reading in the
dictionary (行, 人, 好, 入 ...), Jev was shown the sentence with the reading masked and asked
which of the dictionary's readings belongs there. It chose correctly 73.5 percent of the time.
Always choosing the commonest reading would score 87 percent. Some of its confident mistakes are
telling: 贈る read ぞう (95 percent sure), 最も read さい (92 percent), 包丁 read ぼうちょう
(91 percent). Jev has a shaky grasp of how Japanese words are pronounced, which is exactly what a
furigana checker needs.

### 2.2 Kana inline links that may point at the wrong word

**Set**: the 1,323 occurrences Claude adjudicated by hand in the link ledger, with the sentence
and the marked word (661 were wrong links, such as でも the particle linked to でも the
conjunction, or いずくんぞ linked to いずい; 662 were right), plus 300 random current links that
are presumed right. This is the check `review_links.py` does with Gemini during every run's
self-check.

**Result**: Jev's AUC on the adjudicated set is 0.70. Flagging at 70 percent gives 80 percent
precision and 40 percent recall; on the 300 random links it raised 3 false flags (1 percent)
against Gemini's 12 (4 percent). But it does not see the single most common mistake at all:
every particle でも linked to the conjunction "but" got a probability of about 1 percent of being
a different word, and the same for しかし split from しか + し and ということで split from
という + ことで. Gemini on the same items: 79 percent recall at 61 percent precision on the hard
set. Using Jev only to second-guess Gemini's flags lifts precision from 61 to 76 percent but
drops recall from 79 to 51 percent. Not worth it: the Routine's own model already adjudicates
the flags, and dropping a third of the true ones costs more than the noise saved.

### 2.3 Real errors that were actually in the dictionary

**Set**: the git history was deepened to June, and for every reviewer flag the curator or the
Routine accepted and fixed, the entry was recovered as it stood before the fix. That gave 179
example sentences whose English translation was wrong, 365 glosses that were changed, and 191
notes with a corrected claim; each is paired with its fixed version. This is the truest test of
whether a model could find the errors that survive creation.

**Result**, given as how well the model tells the wrong version from the fixed one (0.5 is
chance, 1.0 is perfect):

| Dimension | Jev | Gemini 2.5 Flash |
|---|---|---|
| Example translation (172 pairs) | 0.69 | 0.68 |
| Gloss, all changes (349 pairs) | 0.65 | 0.54 |
| Gloss, meaning errors only (235) | 0.76 | 0.56 |
| Notes, whole field (180) | 0.58 | not run |
| Notes, the corrected sentence only | 0.63 | not run |
| "How likely is this entry to contain an error?" (rubric) | 0.55 to 0.64 | not run |

Jev and Gemini are equally weak on translations; Jev is somewhat better on glosses when the
change was a meaning error rather than an added sense. In absolute terms neither is a detector:
at a threshold where three out of four Jev flags are right, it finds 17 percent of the wrong
translations and 13 percent of the wrong glosses. Notes are near chance. A rubric asking Jev to
rate an entry's overall likelihood of error is useless for triage. Using Jev to filter Gemini's
flags gained nothing here either.

### 2.4 Semantic tags and other closed classifications

**Set**: 300 random entries with their formality, politeness, part-of-speech family and semantic
tags; for each, one plausible-looking wrong domain tag was injected. Then a second, realistic
set: the 201 tags the accuracy reviewer had actually flagged as belonging to the wrong domain,
172 of which the curator confirmed and removed and 29 of which were dismissed, each judged from
the entry as it stood at the time.

**Result**: Jev agrees with the dictionary's part-of-speech family 93 percent of the time and
with its politeness label 99 percent (almost everything is "plain"); formality only 75 percent,
because Jev calls many neutral words formal. On injected wrong tags it is excellent: AUC 0.99,
and at a 70 percent threshold 99 percent precision with 89 percent recall. On the realistic set
it is still good: AUC 0.87; flagging at 30 percent keeps 77 percent of the tags the curator
removed while letting through only 5 of the 29 dismissed ones. Its false-flag rate on real tags
in random entries is about 1 percent at the 70 percent setting and 0 of 211 at 90 percent.
Its misses are the subtle ones the reviewer argued about (細切り tagged food, 給仕 tagged food,
釣り tagged money).

### 2.5 Which sense an example illustrates

**Set**: 400 examples from entries with two to five numbered senses, each carrying the sense
number assigned when the entry was written.

**Result**: Jev picked the same sense 97.5 percent of the time, and 98.9 percent when it was at
least 90 percent confident (which it was for 94 percent of examples). Of the ten confident
disagreements, several look like the entry is wrong, not Jev: 今まさに出発するところだ ("just
about to leave") is filed under "at this very moment" rather than "just about to"; 戦争で亡くなっ
た人々を祭る慰霊碑 is filed under "to enshrine a deity" rather than "to honor, venerate".

## 3. Where Jev could fit

1. **Not furigana.** The current model is far better at it, and Jev's reading knowledge is below
   a frequency baseline. If a furigana sweep is ever wanted again, a per-pair Gemini prompt
   with the sentence and translation (as in this test, `run_furigana_gemini.py`) is the thing to
   build; on injected errors it ran at 70 percent recall with no false flags, which is nothing like
   the 2 percent precision of the retired entry-level screener.

2. **Not the accuracy review, and not as a filter on it.** Neither model finds the residual
   translation, gloss and notes errors well, and Jev adds nothing on top of Gemini's flags.

3. **A semantic-tag sanity sweep, once, over the whole dictionary.** One call per entry with one
   yes/no question per tag, about 600 tokens each: roughly $0.80 for all 30,800 entries. At the
   70 percent setting it would produce on the order of a few hundred false flags plus whatever
   grossly wrong tags remain (the kind the accuracy reviewer finds at 86 percent precision when it
   happens to look). Output is a list of (entry, tag, probability) for a systemic-fix run to work
   through, highest probability first. Worth doing once; there is no case for repeating it every
   run, since the accuracy review already covers tags.

4. **A sense-number consistency sweep.** Same shape: for every multi-sense entry, ask which sense
   each example illustrates and list the confident disagreements. About 2.5 percent of examples
   disagreed in the sample and some of those are entry errors. Cost for the whole dictionary well
   under $2. This is a check no current instrument performs.

5. **Possibly, in the self-check of each run**: a yes/no per semantic tag and a sense choice per
   example on the run's 30 to 40 changed entries would cost a tenth of a cent and add about one
   false flag per run. Cheap enough to be harmless, but the accuracy reviewer already checks
   tags on those entries, so the gain is small. I would do the two one-time sweeps first and
   decide about the per-run check from what they find.

None of this needs Jev's structured-decision machinery in particular; a chat model could answer
the same closed questions. What Jev brings is price (thirty to forty times cheaper than Gemini
Flash per item here), speed, and clean numeric output with no parsing. For closed questions
about English-side metadata that is a real convenience. For anything that depends on knowing
Japanese well, it is not the right tool.

## 4. What needs Tom

Two decisions, neither urgent:

- Whether to run the one-time semantic-tag sweep and the sense-number sweep (section 3, items 3
  and 4). Each is a small script on top of `enhancement/jev-eval/jevclient.py`, a systemic-fix
  style batch to work the flags, and a few dollars at most.
- Whether the per-pair Gemini furigana prompt (item 1) is worth turning into a sweep over the
  roughly 8,000 entries the retired screener never reached. That is a Gemini question, not a Jev
  one, and would cost on the order of $10 to $20.

## 5. Caveats

- Injected furigana errors are easier than real ones; the 70 and 25 percent recall figures are
  upper bounds for both models. The comparison between them is fair because both saw the same
  items.
- The "real error" sets carry label noise: some accepted flags were stylistic ("literal; natural
  English applied") or added a sense rather than fixing one. The meaning-only subsets are the
  cleaner measure and are reported separately.
- The kana-link set is deliberately hard (occurrences a model had already found doubtful), so
  precision figures on it understate both models' precision on ordinary links; the 300 random
  links give the everyday false-flag rate.
- Jev's docs warn that it reads questions literally and that accuracy falls with irrelevant
  state; the questions here were kept short and the state limited to the entry and sentence at
  hand. Other phrasings might shift the numbers a few points, not the conclusions.
- One version tested (`jev-1.13`, served as `jev-1.13-20260917`). TypeSafe's release notes
  say later versions may differ; the scripts rerun in minutes.
