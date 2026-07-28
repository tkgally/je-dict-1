# LLM Translation Quality for Japanese Language Pairs

**Last updated**: 2026-06-06

## Overview

The [Multilingual Dictionary](../ideas/multilingual-dictionary.md) plan makes language choice
a function of **demand × feasibility**, where feasibility means *"current LLMs can produce
acceptable quality for that language pair"* ([multilingual §7](../ideas/multilingual-dictionary.md#7-per-language-considerations)).
The plan supplies the demand half via [Japanese-Learner Demand by L1](japanese-learner-demand-by-l1.md)
but explicitly leaves the feasibility half to *"a calibration sample before committing."* This
page assembles the published machine-translation-quality evidence that should *precede* and
*frame* that calibration sample: what the MT-evaluation literature already says about LLM
quality on Japanese↔Chinese, Japanese↔Korean, and Japanese↔English, and — crucially — *where*
LLMs are systematically weak in exactly the way this dictionary's hardest content (false
friends, embedded fragments) exposes.

It does not replace the advisor-reviewed calibration sample; it tells us what to *expect* from
that sample and what to watch for.

## The headline: Chinese, Japanese, and Korean are all high-resource

The single most important fact for this project's feasibility question is that **Chinese,
Japanese, and Korean are all high-resource languages for current LLMs and NMT systems.** They
sit in the top tier of every recent multilingual benchmark, far from the low-resource cliff
where quality collapses.

- In the large open-LLM evaluation of Lu et al. (2025), *Multilingual Machine Translation with
  Open Large Language Models at Practical Scale*, Japanese, Chinese, and Korean cluster near
  the top of the FLORES-200 results. The strongest commercial system (Google Translate) leads,
  GPT-4-turbo is close behind, and the best open model evaluated (Gemma2-9B) is competitive
  with both and ahead of GPT-3.5-turbo — while genuinely low-resource pairs (Khmer, Lao,
  Burmese) degrade sharply in the same study. The takeaway is categorical: en↔{ja, zh, ko} are
  in the "well-served" band, not the fragile one.
- The same study's framing — that open LLMs now rival closed ones and approach specialized NMT
  (NLLB) *for high-resource pairs*, while still trailing on low-resource ones — means the model
  market for this project's first two or three target languages is competitive and cheap, not a
  bottleneck.

This corroborates, with evaluation numbers behind it, the plan's qualitative claim that
"Chinese and Korean are well-served" and that the feasibility risk lives further down the
demand list (Indonesian, Thai, Vietnamese), not at the top.

## How good is "good"? The human-translator yardstick

Raw benchmark scores (spBLEU/chrF++/COMET) are hard to map onto "acceptable for a learner's
dictionary." A more interpretable line of evidence compares LLMs directly to human translators:

- Yan et al. (2024), *Benchmarking GPT-4 against Human Translators* (and the related GPT-4
  vs. human-translator evaluation across languages, domains, and expertise levels), found
  GPT-4 performs **comparably to junior/entry-level human translators in total errors, but
  lags medium and senior translators**, and that quality **declines monotonically from
  resource-rich to resource-poor directions.** For high-resource pairs the gap to professional
  human quality is real but narrow; for low-resource pairs it widens.

The operational reading for je-dict-1: a frontier LLM on a high-resource pair produces
roughly *junior-translator-quality* first drafts. That is exactly the quality profile the
plan's pipeline is built around — **good enough for a bulk first draft, not good enough to
ship unreviewed for the highest-value content.** It is why the plan pairs a cheap bulk pass
with a stronger/advisor review pass ([multilingual §4](../ideas/multilingual-dictionary.md#4-how-the-ai-translation-should-be-done)),
and why the human advisor's time is concentrated on basic/core tiers and false-friend entries.

## The catch that matters most here: shared characters cut both ways

A general benchmark score hides the failure mode this dictionary is *most* exposed to. The
Chinese pipeline's entire reason for a per-language adaptation brief is the **同形異義語
(same-form, different-meaning) false friend** — and false friends are precisely where LLMs are
documented to be weakest.

- Multilingual LLMs **struggle to link orthography and semantics** for cognates, homographs,
  and false friends across languages (the 2025 bilingual-word-processing study,
  arXiv:2501.09127). Orthographic overlap helps a model *align* word forms but does **not
  reliably deliver correct meaning retrieval** — the model can be drawn toward the
  same-character reading. For a Japanese→Chinese pipeline this is the worst possible
  intersection: 手紙 (letter / 手纸 toilet paper), 勉強 (study / 勉强 reluctantly),
  大丈夫 (all right / 大丈夫 a real man) are exactly the items where high character overlap can
  *pull* the model toward the wrong Chinese sense.
- More broadly, **language proximity and shared training-data vocabulary drive LLM confusion
  patterns**: models most often confuse languages with high lexical and orthographic overlap
  (the language-proximity / information-loss line of work, e.g. arXiv:2506.23340 and the
  hallucination-taxonomy work). Japanese↔Chinese is a high-overlap pair *by writing system*,
  so it inherits this risk even though both languages are individually high-resource.
- Multilingual MT systems are also prone to **hallucination** — generating content not in the
  source — a documented, safety-relevant failure of large multilingual translation models
  (Guerreiro et al. 2023, *Hallucinations in Large Multilingual Translation Models*, TACL).
  For this project the hallucination risk is concrete and structural: a model translating a
  `notes` field can drop or mutate an embedded `{漢字|かんじ}` fragment or an `⟦…⟧` link.

The synthesis: **aggregate quality for en↔{ja, zh, ko} is high, but the per-item risk is
concentrated exactly on the dictionary's highest-value adaptations.** This is not a reason to
avoid the language — it is the reason the [adaptation brief](japanese-chinese-adaptation-brief.md)
routes D/O-class (false-friend) headwords to the deep/advisor pass, and the reason the
[sidecar design](../ideas/translation-sidecar-design.md) enforces byte-level fragment
preservation by post-validation rather than trusting the model.

## Per-pair feasibility read

| Pair | Resource level for LLMs | Quality expectation (high-resource band) | Project-specific risk |
|------|------------------------|------------------------------------------|-----------------------|
| **ja ↔ en** (existing pivot) | very high | best of any pair; GPT-4-class ≈ junior–mid human | the canonical source; quality here bounds everything downstream |
| **en/ja → zh** (first target) | high | strong first drafts; near junior-human | **highest** false-friend / homograph pull (same-character overlap); needs the adaptation brief + advisor |
| **en/ja → ko** (likely second) | high | strong; close grammatical alignment helps | fewer false friends than zh; Sino-Korean over-trust; MQM benchmark exists (Korean LREC 2024) for calibration |
| **en/ja → vi** | upper-mid | usable but calibrate first | Hán-Việt partial cognates without the character bridge; thinner eval coverage |
| **en/ja → id, th** | mid | calibration-gated | lower benchmark coverage; demand-strong (Indonesian) but feasibility-unproven |

The ranking matches the demand analysis: the two languages that are both **highest-demand among
unserved L1 groups** (Chinese, Korean — see [demand page](japanese-learner-demand-by-l1.md)) are
also the two that are **lowest feasibility-risk**, so demand and feasibility point the same way
for the first two languages. Divergence only appears further down (Indonesian: high demand,
unproven feasibility — the genuine wildcard).

## Why this still requires the calibration sample

Published benchmarks measure *generic* translation quality on news/wiki-style sentences. They
do **not** measure the things this project actually needs:

1. **Pedagogical-prose translation** — `notes` and `explanation` are metalinguistic
   explanations *about* Japanese, not ordinary prose; no public benchmark scores this register.
2. **Embedded-fragment preservation** — no benchmark tests whether a model keeps
   `{漢字|かんじ}` and `⟦…⟧` intact; this must be measured on real entries.
3. **False-friend adaptation quality** — whether the model *adds* the correct 同形異義語
   warning (not just avoids the wrong sense) is a dictionary-specific behavior.
4. **Human-edit rate** — the number that actually governs cost (how much advisor time per 100
   entries) can only come from the advisor reviewing real output.

So the published evidence sets the *prior* — "expect junior-translator-quality first drafts on
a high-resource pair, with concentrated false-friend failures" — and the ~50-entry
advisor-reviewed calibration sample ([multilingual §9](../ideas/multilingual-dictionary.md#9-phasing--rollout))
measures the *posterior* on this project's actual content. The calibration step is the direct
analogue of `reviews/calibration_report.md`, which calibrated the furigana reviewers before
scaling.

## Implications for je-dict-1

- **Feasibility for Chinese and Korean is confirmed at the language level.** Both are
  high-resource; frontier LLMs produce junior-human-quality first drafts; the model market is
  competitive and cheap. The "feasibility" half of the plan's demand × feasibility gate is
  green for the first two target languages.
- **The risk is per-item, not per-language, and it is predictable.** It concentrates on exactly
  the false-friend / shared-character content the adaptation brief already enumerates, plus the
  structural hallucination risk to embedded fragments. The mitigation already exists in the
  plan: brief-driven priority routing + post-validation of fragments + advisor review of
  D/O-class and basic/core entries.
- **Use the strong model where the risk lives.** The evidence supports the plan's two-pass
  design: a cheaper model for the bulk of low-risk fields (glosses, example translations,
  universal explanation prose) and the strongest available model (current Claude 4.x Opus
  class) plus the human advisor for `notes` on false-friend entries.
- **Calibration is still mandatory.** No public benchmark measures pedagogical-prose
  translation, fragment preservation, or human-edit rate. The ~50-entry sample remains the
  first concrete deliverable; this page tells the curator what result to expect and what to
  inspect for.

## References

- Lu, Y., et al. (2025). *Multilingual Machine Translation with Open Large Language Models at
  Practical Scale: An Empirical Study.* arXiv:2502.02481.
- Yan, J., et al. (2024). *Benchmarking GPT-4 against Human Translators: A Comprehensive
  Evaluation Across Languages, Domains, and Expertise Levels.* arXiv:2411.13775 (and the
  related *GPT-4 vs. Human Translators* evaluation, arXiv:2407.03658).
- *Multilingual LLMs Struggle to Link Orthography and Semantics in Bilingual Word Processing.*
  (2025). arXiv:2501.09127.
- *Information Loss in LLMs' Multilingual Translation: The Role of Training Data, Language
  Proximity, and Language Family.* (2025). arXiv:2506.23340.
- Guerreiro, N. M., et al. (2023). *Hallucinations in Large Multilingual Translation Models.*
  *Transactions of the ACL*, arXiv:2303.16104.
- *Multi-Dimensional Machine Translation Evaluation: Model Evaluation and Resource for Korean.*
  (2024). LREC-COLING 2024, ACL Anthology 2024.lrec-main.1024 — the English↔Korean MQM
  benchmark usable for Korean calibration.
- *JP-TL-Bench: Anchored Pairwise LLM Evaluation for Bidirectional Japanese-English
  Translation.* (2026). arXiv:2601.00223.

## Related pages

- [Multilingual Dictionary](../ideas/multilingual-dictionary.md) — the hub plan; this page fills the "feasibility" half of its §7 demand × feasibility gate
- [Japanese-Learner Demand by L1](japanese-learner-demand-by-l1.md) — the demand half; together they rank Chinese first, Korean second
- [Japanese→Chinese Adaptation Brief](japanese-chinese-adaptation-brief.md) — the false-friend classes that are exactly where the LLM risk concentrates, and the routing that mitigates it
- [Translation Sidecar Design](../ideas/translation-sidecar-design.md) — the fragment-preservation post-validation that answers the hallucination risk documented here
- [L1 Transfer in Japanese L2 Vocabulary](l1-transfer-japanese-vocabulary.md) — why shared characters create both cognate help and false-friend traps
- [Multi-Model Proofreading](../ideas/multi-model-proofreading.md) — the calibration-then-scale pattern (`reviews/calibration_report.md`) the calibration sample reuses
- [Dictionary Use in the Age of Machine Translation](dictionary-and-machine-translation.md) — broader context on MT quality and what dictionaries add beyond it
