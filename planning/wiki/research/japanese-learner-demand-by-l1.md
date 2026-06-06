# Japanese-Learner Demand by L1 (Language-Priority Input)

**Last updated**: 2026-06-06

## Purpose

The [Multilingual Dictionary](../ideas/multilingual-dictionary.md) plan chooses additional
target languages by **demand × LLM feasibility** ([§7](../ideas/multilingual-dictionary.md#7-per-language-considerations)),
and explicitly defers the demand half to "a future research pass over JLPT/JF learner-population
statistics — do not fabricate figures here." This page is that pass. It supplies the real
learner-population data needed to rank candidate target languages, and reads it against
feasibility to sanity-check the plan's "Chinese first, then demand-driven" sequencing.

The headline caveat governs everything below: **the surveys count learners by country, but the
dictionary cares about L1 (and hence target language).** Country is a proxy for L1, and a leaky
one — Australia and the USA are huge Japanese-learning populations whose L1 is *English*, already
served. The useful move is to map country counts onto L1 groups, then drop the groups already
covered.

## The data: Japan Foundation Survey 2021

The Japan Foundation conducts a worldwide *Survey on Japanese-Language Education Abroad* every
three years (most recent: 2021; the 2024 round postdates this writing). The 2021 survey counted
**~3,794,714 learners** across 141 countries/regions — a slight decline from ~3.85 million in
2018, attributed to the pandemic (Japan Foundation 2021; Nippon.com 2022).

Top learner populations by country/region (2021):

| Rank | Country/region | Learners | Dominant L1 → target language |
|------|----------------|----------|-------------------------------|
| 1 | China | 1,057,318 | Chinese (Mandarin; simplified) |
| 2 | Indonesia | 711,732 | Indonesian |
| 3 | South Korea | 470,334 | Korean |
| 4 | Australia | 415,348 | English *(already served)* |
| 5 | Thailand | 183,957 | Thai |
| 6 | Vietnam | 169,582 | Vietnamese |
| 7 | United States | 161,402 | English *(already served)* |
| 8 | Taiwan | 143,632 | Chinese (Mandarin; traditional) |
| 9 | Philippines | 44,457 | Filipino/English |
| 10 | Malaysia | 38,129 | Malay/Chinese/Tamil (multilingual) |

Source: Japan Foundation, *Survey Report on Japanese-Language Education Abroad 2021* (figures
from the country/region ranking and Chapter 1 overview).

## Re-reading the data by L1 / target language

Collapsing the country table onto target languages, and setting aside the English-L1
populations the dictionary already serves:

| Target language | Demand signal (2021 learners) | Notes |
|-----------------|-------------------------------|-------|
| **Chinese** | **~1.20M** (China 1,057,318 + Taiwan 143,632) | Largest non-English group by a wide margin. Splits into simplified (mainland) and traditional (Taiwan) — see the plan's [§7](../ideas/multilingual-dictionary.md#7-per-language-considerations) zh-Hans/zh-Hant decision. |
| **Indonesian** | ~711,732 | Second-largest. Driven heavily by secondary-school programs; demand profile differs from the tertiary/professional Chinese and Korean cohorts. |
| **Korean** | ~470,334 | Third-largest. Closest L1 to Japanese typologically (SOV, particles, Sino-Korean vocabulary). |
| **Thai** | ~183,957 | Growing; technical-intern and tourism-linked. |
| **Vietnamese** | ~169,582 | Sharp recent growth tied to technical-intern and study programs (noted in the plan). |
| English | (Australia + USA + others) | **Already the base language**; counted here only to explain why the raw country ranking overstates "unserved" demand. |

The single most important fact for the priority ranking: **Chinese is the largest unserved L1
group by a factor of ~1.7× over the next (Indonesian) and ~2.5× over Korean.** The plan's choice
of "Chinese first" is strongly supported by demand, independent of the advisor-availability
reason. (The advisor is why Chinese is *feasible to start now*; the demand data is why it is
*the right* first choice.)

## Cross-referencing demand with feasibility

Demand alone does not set the order; the plan multiplies it by LLM feasibility for the pair.
Combining the two:

| Target language | Demand | LLM feasibility (Japanese↔X) | Combined read |
|-----------------|--------|------------------------------|---------------|
| Chinese | Highest | High — high-resource pair, frontier models strong | **First** (matches plan) |
| Korean | High | High — high-resource, close typology | Strong second candidate |
| Indonesian | High | Medium — moderate-resource; needs calibration | Demand argues for it; feasibility needs a calibration sample first |
| Vietnamese | Medium, growing | Medium — Hán-Việt partial cognates but lower-resource | Plan flags it as an intermediate case (character bridge lost) |
| Thai | Medium | Medium-low — lower-resource; calibration essential | Later |

This reproduces the plan's intuition with numbers behind it: **Chinese first, Korean as the
natural second** (high demand × high feasibility × infrastructure reuse), with Indonesian's large
demand held back only by a feasibility unknown that a calibration sample (à la
`reviews/calibration_report.md`) would resolve. The order is demand-and-feasibility-driven exactly
as the plan specifies; the data simply confirms the ranking rather than overturning it.

### Demand-profile nuance the raw counts hide

- **Cohort type matters for the dictionary's usefulness.** China/Korea/Vietnam skew toward
  tertiary and professional learners (the intermediate audience je-dict-1 targets); Indonesia and
  Australia skew toward secondary-school programs, where a learner's-dictionary-of-this-depth fit
  is weaker. Raw head-counts therefore overstate Indonesian *fit* relative to its rank.
- **Country ≠ L1 for multilingual states.** Malaysia (Malay/Chinese/Tamil) and the Philippines
  (Filipino/English) cannot be assigned a single target language; their learners partly fold into
  the Chinese and English buckets.
- **The surveys are triennial and lag.** The 2024 round (and JLPT application volumes, a separate
  higher-frequency signal) should refresh this when available; treat 2021 as the current best
  estimate, not a live figure.

## Implications for je-dict-1

- **Confirms "Chinese first."** Chinese is the largest unserved-L1 learner population worldwide
  (~1.2M, combining mainland and Taiwan), so the plan's first-language choice is the
  demand-maximizing one as well as the advisor-enabled one.
- **Names the second language with evidence.** Korean is the highest demand × feasibility
  candidate after Chinese, supporting the plan's "likely Korean" second-language assumption
  ([§9](../ideas/multilingual-dictionary.md#9-phasing--rollout)).
- **Flags Indonesian as the high-demand / unknown-feasibility wildcard.** Its #2 raw rank argues
  for an early calibration sample to learn whether current LLMs clear the quality bar for the
  pair — the same de-risking move the plan prescribes for every lower-resource language.
- **Gives the curator a real number to weigh against cost.** Each additional language multiplies
  the translation, staleness-maintenance, and (if per-language static rendering is chosen) build
  cost; the demand table is the benefit side of that trade-off.

## References

- The Japan Foundation (2021). *Survey Report on Japanese-Language Education Abroad 2021*. Tokyo: The Japan Foundation. https://www.jpf.go.jp/e/project/japanese/survey/result/survey21.html (country/region learner counts; ~3,794,714 learners worldwide).
- Nippon.com (2022). "Worldwide Number of Students of Japanese Sees Slight Decline Amid Pandemic." https://www.nippon.com/en/japan-data/h01521/ (summary of the 2021 survey, total and trend).

## Related pages

- [Multilingual Dictionary](../ideas/multilingual-dictionary.md) — the plan whose §7 demand/feasibility ranking this page supplies data for
- [LLM Translation Quality for Japanese Language Pairs](llm-translation-quality-japanese-pairs.md) — the *feasibility* half of the same demand × feasibility gate this page supplies the *demand* half of
- [Japanese→Chinese Adaptation Brief](japanese-chinese-adaptation-brief.md) — the first-language brief justified by this demand ranking
- [L1 Transfer in Japanese L2 Vocabulary](l1-transfer-japanese-vocabulary.md) — why each L1 group needs different note adaptation (the feasibility/quality axis is partly about how distinct each L1's needs are)
- [Vocabulary Size and Text Coverage](vocabulary-size-coverage.md) — the other sizing axis (how big the dictionary must be), complementary to how many languages it serves
