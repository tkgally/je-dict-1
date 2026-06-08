# Furigana Strategy

**Last updated**: 2026-06-08

## Overview

Furigana policy is one of je-dict-1's defining design decisions. The dictionary
annotates **every kanji in every field** — headwords, example sentences, notes,
definitions, and conjugation tables — with `{漢字|かんじ}` wrappers that the build
system renders as ruby text. This page covers the rationale, the wrapper format
in detail, the distinction between furigana *completeness* and *correctness* (two
problems with separate tooling), the known format-hygiene issues, and how the
policy interacts with the rest of the project.

For the catalogue of malformed wrappers currently in the entry set and the
remediation plan, see [Furigana Wrapper Anomalies](furigana-wrapper-anomalies.md).
For the research foundations, see [Kanji Learning and Dictionary
Treatment](../research/kanji-learning-dictionaries.md).

## The universal-annotation policy

je-dict-1 annotates all kanji regardless of frequency or JLPT level. This is a
deliberate choice for the target audience: intermediate learners who read kana
fluently but are still building kanji knowledge.

### Why annotate everything

**For the learner:**
- Removes the frustration of hitting an unknown kanji in an example meant to
  teach a *different* word — the example stays usable as a vocabulary/grammar
  model even when its incidental kanji are above the reader's level.
- Lets learners focus attention on the target item rather than spending it on
  kanji decoding (a load-reduction argument supported by the dual-coding and
  cognitive-load research summarised in
  [kanji-learning-dictionaries.md](../research/kanji-learning-dictionaries.md)).
- Supports self-testing: a learner can attempt the kanji first, then check
  against the reading — the ruby acts as an instant answer key.

**Against selective annotation.** Many Japanese sources annotate only "difficult"
(typically non-jōyō) kanji. That convention serves native readers but poorly
serves L2 learners, for three reasons:
- "Difficult" is learner-relative. An N3 learner may know the jōyō kanji of one
  semantic domain and almost none of another; the jōyō/non-jōyō line does not
  track any individual learner's actual knowledge.
- Inconsistent annotation produces *worse* UX than consistent full annotation —
  the reader never knows whether an un-annotated kanji is "easy" or simply
  un-marked, so the absence of furigana carries no reliable signal.
- Universal annotation eliminates the per-kanji "is this hard?" editorial
  judgment entirely, which is also what makes the policy mechanically
  enforceable (see *Completeness* below).

The research is unusually one-sided here: the scaffolding-removal literature
debates *when* to fade furigana for a progressing reader, but for a reference
work consulted by learners of mixed and unknown proficiency, full annotation is
the unambiguous default (see kanji-learning-dictionaries.md → "Universal furigana
is the right default").

## The wrapper format

**Source form** `{漢字|かんじ}` → **rendered** `<ruby>漢字<rt>かんじ</rt></ruby>`.
The schema's furigana pattern enforces the shape; `japanese_utils.FURIGANA_PATTERN`
is the single shared regex that every script uses to find and strip wrappers.

Core rules:

| Rule | Form | Not |
|------|------|-----|
| Reading covers the **kanji only** | `{食\|た}べる` | `{食べる\|たべる}` |
| Each kanji group annotated separately | `{飛行\|ひこう}{機\|き}` | `{飛行機\|ひこうき}`¹ |
| Readings are always **hiragana** | `{誰\|だれ}` | `{誰\|ダレ}` |
| Pure-kana text takes no wrapper | する, ある, ね | `{する\|する}` |

¹ Single-unit compounds where the reading cannot be cleanly split per character
are sometimes wrapped whole; the canonical preference is per-group segmentation,
which is what makes okurigana extraction and stem-finding reliable downstream.

### Why these rules exist (and what breaks when violated)

- **Okurigana on the surface side, not in the reading.** `{食|た}べる` keeps the
  trailing べる outside the wrapper so the ruby paints たover 食 only. Folding
  okurigana inside (`{食べる|たべる}`) usually still *renders* acceptably, but it
  defeats programmatic stem extraction: `add_adjective_conjugations.py` cannot
  parse a stem out of `{若い|わかい}`, which is exactly why basic-tier 若い
  (01525) shipped without a conjugation table. The wrapper format is not just
  cosmetic — downstream tools parse it.
- **Readings are hiragana even for katakana headwords.** A katakana headword
  like テレビ has no kanji and takes no wrapper at all; the hiragana-only rule
  applies to the *reading* annotations on kanji, keeping a single uniform script
  for ruby across the whole dictionary and avoiding katakana ruby that would read
  as a stylistic emphasis to Japanese eyes.
- **Reading-by-context for homographs.** The reading inside the wrapper is the
  reading *in that context*: 角 is `{角|かど}` (corner) or `{角|つの}` (horn)
  depending on sense; 描く is `{描|か}く` or `{描|えが}く`. The wrapper is where
  homograph disambiguation actually lands in the source text — see
  [Handling Homographs](homographs.md).

## Completeness vs. correctness — two problems, two pipelines

A furigana annotation can fail in two independent ways: it can be **missing**
(kanji with no wrapper) or **wrong** (wrapper present but the reading is
incorrect). The project treats these as separate problems with separate tooling,
because they have very different error profiles — completeness is mechanically
detectable, correctness is not.

### Completeness (deterministic)

A bare kanji is a regex-detectable defect. Two scripts cover it:
- `find_missing_furigana.py` scans **all** entries for kanji appearing outside a
  wrapper, across `notes`, `definitions[].explanation`, `examples[].japanese`,
  and `examples[].notes`. It is the standard post-creation gate (run it after
  every entry-creation batch; the PROJECT_STATUS change logs show most batches
  catching a handful of bare-kanji slips in prose this way).
- `verify_furigana.py` checks a single entry's notes coverage on demand.

Because completeness is deterministic, it is *enforced*, not merely audited —
this is the operational payoff of the universal-annotation policy. (See
[Deterministic vs. Semantic Tasks](deterministic-vs-semantic-tasks.md): furigana
*completeness* is the deterministic half; *correctness* is the semantic half.)

### Correctness (semantic — multi-model review)

Whether `{角|かど}` is the right reading in context is a judgment a regex cannot
make. The project's answer is the multi-model review pipeline
(`build/review_runner.py` + the `reviews/` directory), built in the 2026
Enhancement Plan:
- **Two passes**: a cheap screening model flags suspect entries; strong models
  (e.g. GPT-4.1, Gemini) deep-review the flagged set. ~100 per-entry deep-review
  reports currently sit in `reviews/`, with the queue tracked in
  `reviews/queue.txt`.
- **Calibration matters.** `reviews/calibration_report.md` (2026-04-09) records
  that the *naïve* prompt flagged ~98% of pairs as wrong — the models did not
  understand that a reading covers only the kanji portion of
  `{kanji|reading}okurigana` and kept flagging correct okurigana stems
  (`{走|はし}る` → "はし is incomplete"). After prompt iteration the system
  reached a 0.12% noise rate (≈99.88% of readings correctly classified). This is
  a concrete worked example of why furigana correctness needs a *calibrated*
  semantic checker, not a rule.
- The `polish_furigana_correctness` task applies/rejects these reports; its
  sibling `polish_furigana_completeness` handles the deterministic side.

The split is the point: completeness is cheap and total; correctness is expensive
and sampled. The dictionary spends its furigana-QA budget where machines cannot
substitute for judgment.

## Format hygiene: wrapper anomalies

Even with completeness enforced, the *shape* of wrappers can drift.
[Furigana Wrapper Anomalies](furigana-wrapper-anomalies.md) catalogues **859
instances across 624 entries** where hiragana sits inside the kanji side of a
wrapper. Most render acceptably (over-wrapped okurigana like `{若い|わかい}`,
honorific-prefix-inside like `{お酒|おさけ}`), but two sub-patterns are genuinely
broken on the live site:
- **Truncated readings** (68 entries): the surface side includes preceding kana
  but the reading covers only the kanji, so the browser paints a partial reading
  over the full surface (`かた` over the whole やり方).
- **Reversed pure-kana wrappers** like `{ところ|所}` (kanji and reading
  swapped).

These are tracked in [Cleanup Backlog → Priority 9](../ideas/cleanup-backlog.md)
and need a normalising pass (and ideally a format validator — see [Tooling
Backlog](../ideas/tooling-backlog.md)). The lesson for the format rules above is
concrete: the canonical per-group, okurigana-outside form is what keeps both the
rendering and the downstream parsers correct.

## Furigana beyond the entry page

- **Kanji index.** Every wrapper is a (kanji → reading) datum. The kanji index
  (`kanji/`, maintained by `update_kanji_index.py`) draws on this to map
  characters to the entries that use them; the universal-annotation policy means
  the index has reading data for essentially every kanji occurrence in the
  corpus. See the `kanji-index` skill (`.claude/skills/kanji-index/SKILL.md`).
- **Inline links.** Cross-reference links `⟦surface→base：id⟧` coexist with
  furigana wrappers in the same text. The interaction produces an edge case the
  extractors must tolerate — nested/double-brace wrappers
  `{{word|reading}phrase|compound}` (Cleanup Backlog Priority 9; the translation
  sidecar's preservation contract also has to survive these). Any tool that
  rewrites text must mask both `{…|…}` and `⟦…⟧` spans.

## Future considerations

- **Furigana toggle.** A "hide readings" option would let advanced users treat
  the dictionary as graded reading practice (attempt the kanji, reveal on
  demand) — directly the graduated-scaffolding-removal idea from the research.
  Because every reading is already structured data, the toggle is a rendering
  feature, not a content change.
- **Kanji-learning features.** The wrapper corpus is a ready-made dataset for
  reading drills, per-kanji reading frequency, and "kanji you've seen" tracking.
- **Furigana's function changes by L1 (multilingual).** For an English speaker
  furigana is a *decoding scaffold* for an unfamiliar glyph. For a
  Chinese-background learner the glyph is familiar but its Japanese *reading* is
  the entire difficulty, so furigana becomes the **primary content**, not a
  scaffold. The wrappers themselves are part of the invariant Japanese spine
  shared across all language versions (see
  [Multilingual Dictionary](../ideas/multilingual-dictionary.md) and
  kanji-learning-dictionaries.md → "Implications for multilingual versions"),
  but their pedagogical justification, and the surrounding gloss layer, are
  per-L1 adaptation.

## Related pages

- [Furigana Wrapper Anomalies](furigana-wrapper-anomalies.md) — the malformed-wrapper catalogue and remediation plan
- [Kanji Learning and Dictionary Treatment](../research/kanji-learning-dictionaries.md) — furigana as scaffold, dual coding, the scaffolding-removal debate, L1 function-change
- [Handling Homographs](homographs.md) — the wrapper as the locus of reading-by-context disambiguation
- [Deterministic vs. Semantic Tasks](deterministic-vs-semantic-tasks.md) — why completeness is automatable and correctness is not
- [Multi-Model Proofreading](../ideas/multi-model-proofreading.md) — the review pipeline that backs furigana correctness
- [Entry Design](../project/entry-design.md) — where furigana sits among required fields
- [Cleanup Backlog](../ideas/cleanup-backlog.md) · [Tooling Backlog](../ideas/tooling-backlog.md) — the open wrapper-hygiene and validator work
