# Chinese Simplified/Traditional Handling (zh-Hans / zh-Hant) — Worked Design

**Last updated**: 2026-06-06

## Overview

This is a worked-out companion to the [Multilingual Dictionary](../ideas/multilingual-dictionary.md)
plan. The plan's [§7](../ideas/multilingual-dictionary.md#7-per-language-considerations) raised
"simplified vs. traditional Chinese" as an **open decision** and flagged the
simplified/traditional handling as a candidate for its own worked design. That decision is now
**resolved**:

> **Decision (curator, 2026-06): Simplified Chinese (簡体字, `zh-Hans`) ships first.** The
> native-speaker advisor who has agreed to help works in simplified script and Putonghua
> (mainland) norms, so the first Chinese deliverable is `zh-Hans`. Traditional Chinese
> (`zh-Hant`) is **deferred**, not cancelled — the design must keep room for it.

This page turns the now-settled "simplified first, traditional later" position into a concrete
data-and-pipeline design: the language-code space, why traditional cannot be produced by a
mechanical script flip, the **assisted-conversion + human-review** path for seeding `zh-Hant`
from `zh-Hans` when the time comes, and the font/search/UI consequences. Like its sibling pages
it is **design, not implementation** — it modifies no schema, script, or entry.

## 1. Why this is not a cosmetic choice

"Add traditional later by running a converter" is the intuition this page exists to refute.
Simplified↔traditional is not a reversible 1:1 transcoding, for two independent reasons.

### 1a. One-to-many character merges (the irreversible part)

The 1950s–60s simplification merged several distinct traditional characters into a single
simplified form. Going simplified→traditional therefore requires choosing *which* traditional
character is meant — a decision that needs the word's meaning, not just its shape. Canonical
hard cases:

| Simplified | Possible traditional | Disambiguation needed |
|------------|----------------------|------------------------|
| 干 | 干 (shield) / 乾 (dry) / 幹 (to do; trunk) | three unrelated meanings collapsed onto one glyph |
| 后 | 后 (empress) / 後 (after, behind) | temporal vs. royal sense |
| 发 | 發 (to emit/issue) / 髮 (hair) | unrelated morphemes |
| 里 | 里 (village; li unit) / 裡 (inside) | locative vs. measure |
| 面 | 面 (face) / 麵 (noodles) | the food sense splits off |

Because "in most cases these traditional characters are homonyms with the same pronunciation
but different meanings, converting from simplified to traditional is difficult to automate"
([Wikipedia, *Ambiguities in Chinese character simplification*](https://en.wikipedia.org/wiki/Ambiguities_in_Chinese_character_simplification)).
A blind character map will silently emit 乾 where 幹 was meant. Traditional→simplified is mostly
safe (many-to-one); **simplified→traditional is the lossy direction** — and it is precisely the
direction this project would travel, since `zh-Hans` is authored first.

### 1b. Regional vocabulary divergence (the part character mapping never touches)

Even with characters resolved correctly, mainland (Putonghua) and Taiwan (Guoyu) / Hong Kong
norms use **different words** for the same modern concept. Script conversion does not, and
cannot, fix this:

| Concept | Mainland (zh-Hans) | Taiwan (zh-Hant-TW) |
|---------|--------------------|---------------------|
| software | 软件 (ruǎnjiàn) | 軟體 (ruǎntǐ) |
| information | 信息 (xìnxī) | 資訊 (zīxùn) |
| network/internet | 网络 (wǎngluò) | 網路 (wǎnglù) |
| video clip | 视频 (shìpín) | 影片 (yǐngpiàn) |
| marketing | 营销 (yíngxiāo) | 行銷 (xíngxiāo) |

A naïve converter turns 软件 into 軟件 — a character-correct string that no Taiwan reader would
write ([toolkk, *Simplified to Taiwan Traditional: Are You Doing It Right?*](https://www.toolkk.com/en/posts/simplified-traditional-translation-tutorial);
[Laoret, *Traditional vs Simplified Chinese*](https://laoret.com/blog/simplified-and-traditional-chinese/)).
For a *learner's dictionary*, where the explanatory prose must read as natural target-language
text, shipping mechanically-converted Taiwan Chinese would undercut the whole value proposition.

**Conclusion:** `zh-Hans` and `zh-Hant` are genuinely **two target languages** at the data
level, even though they share ~100% of the *adaptation content* (the false-friend phenomena in
the [Chinese adaptation brief](../research/japanese-chinese-adaptation-brief.md) are identical
for both audiences — only the surface rendering and a handful of norm-divergent terms differ).

## 2. Language-code space

Use the BCP-47 script subtags so the design has room for both variants (and the regional norms)
without rework:

| Code | Meaning | Status in this project |
|------|---------|------------------------|
| `zh-Hans` | Chinese, Simplified script (Putonghua norms) | **first deliverable** |
| `zh-Hant` | Chinese, Traditional script (generic) | deferred; design keeps the slot |
| `zh-Hant-TW` | Traditional, Taiwan norms (軟體, 資訊…) | the realistic shape of any future "traditional" |
| `zh-Hant-HK` | Traditional, Hong Kong norms | further deferred; noted for completeness |

This matters concretely in three places already specified in the sibling designs:

- **Sidecar directory tree** — `translations/zh-Hans/{range}/{id}_{romaji}.json`
  ([Translation Sidecar Design §2](../ideas/translation-sidecar-design.md#2-a-concrete-sidecar-file)
  already uses `zh-Hans` as the example `target_lang`). A future `zh-Hant` is a *parallel*
  sidecar tree — purely additive, the recommended Option B's whole point.
- **i18n label map** — `build/data/i18n/zh-Hans.json` for tag display names and conjugation
  form labels; `zh-Hant.json` later.
- **`hreflang`** — per-language static pages declare `zh-Hans` (and later `zh-Hant`) alternates
  so search engines serve the right script
  ([Multilingual §6](../ideas/multilingual-dictionary.md#6-ui-storage-and-delivery)).

Treating "Chinese" as a single undifferentiated `zh` would be the one decision that is
expensive to undo, because it would bake the script choice into paths, search indexes, and
stored translations. Naming it `zh-Hans` from day one costs nothing now and preserves `zh-Hant`
as a clean later addition.

## 3. How `zh-Hant` should be seeded later (assisted conversion + human review)

When traditional is eventually prioritized (demand- and feasibility-driven, like every language
after the first — [Multilingual §7](../ideas/multilingual-dictionary.md#7-per-language-considerations)),
it should **not** be re-translated from scratch, and it should **not** be a blind character
flip. The right path is a two-stage seed:

1. **Machine pre-conversion with a phrase-aware, region-aware tool.** [OpenCC (Open Chinese
   Convert)](https://github.com/BYVoid/OpenCC) is the standard open-source library here. It
   "strictly distinguishes one-simplified-to-many-traditional from one-simplified-to-many-variant
   mappings" and ships **region-and-phrase-aware configurations** — crucially `s2twp.json`
   ("Simplified to Taiwan Traditional **with Taiwan-specific phrases**"), which converts
   软件→軟體, not 軟件. The relevant configs:

   | Config | Effect |
   |--------|--------|
   | `s2t` | simplified → traditional, character level only (does *not* fix vocabulary) |
   | `s2tw` | simplified → Taiwan traditional (script + Taiwan character variants) |
   | `s2twp` | simplified → Taiwan traditional **+ Taiwan phrase/vocabulary** (软件→軟體) |
   | `s2hk` | simplified → Hong Kong traditional variant |

   `s2twp` is the right default for seeding `zh-Hant-TW`: it handles both the one-to-many
   character choices (via phrase context) and the lexical-norm swaps in one pass. But it is a
   *seed*, not a finished product — OpenCC's phrase tables are broad but not exhaustive, and the
   dictionary's prose includes embedded Japanese fragments the converter must leave untouched
   (see §4).

2. **Human review of the seed, prioritized like every other pass.** A native traditional-script
   reviewer corrects residual one-to-many errors, norm-divergent terms OpenCC missed, and any
   register infelicities, working a queue ordered by tier (basic/core first) exactly as the
   [staleness/re-translation queue](../ideas/translation-sidecar-design.md#4c-the-re-translation-queue)
   orders the simplified pipeline. The review effort for a converted seed is far smaller than
   for a from-scratch translation — the seed is ~right — which is exactly why "convert + review"
   beats both "blind convert" (wrong) and "re-translate" (wasteful).

This is the same *assisted-draft → human-review* shape the project already uses everywhere
(furigana review, multi-model proofreading, the simplified translation pipeline itself). The
only Chinese-specific twist is that the "draft" comes from a deterministic converter (OpenCC),
not an LLM, because for *script* conversion a rules+phrase-table tool is more reliable and far
cheaper than a model.

### What is shared vs. variant-specific (the maintenance win)

Because the [adaptation brief](../research/japanese-chinese-adaptation-brief.md) is written
**script-neutrally**, the expensive, judgment-heavy content is authored once and reused:

| Layer | Shared across zh-Hans / zh-Hant? |
|-------|----------------------------------|
| Which entries are false friends (D/O-class routing) | **Shared** — same phenomena |
| `common_mistakes` content (の/的 transfer, transitivity) | **Shared** — same L1 |
| "what to drop" decisions (gairaigo warnings, morphemic glosses) | **Shared** |
| Embedded Japanese fragments + furigana + `⟦…⟧` links | **Shared** (invariant spine) |
| Surface script of the Chinese prose | **Variant-specific** (the OpenCC pass) |
| Norm-divergent vocabulary (软件/軟體, 信息/資訊) | **Variant-specific** (OpenCC `s2twp` + review) |

So `zh-Hant` inherits all the costly editorial decisions and pays only for surface conversion +
a lighter review. This is the concrete reason to treat them as two codes but one *content*
stream.

## 4. Preservation hazard: the converter must not touch the spine

The dictionary's translated `notes`/`explanation` prose **embeds Japanese fragments** —
`{漢字|かんじ}` furigana wrappers and `⟦surface→base：entry_id⟧` inline links — that are part of
the invariant Japanese spine and must survive byte-for-byte
([Translation Sidecar Design §5](../ideas/translation-sidecar-design.md#5-embedded-japanese-fragment-preservation)).
A simplified→traditional converter run over `zh-Hant` sidecar prose would, if applied naïvely,
"helpfully" convert the kanji *inside* those Japanese fragments — turning 勉強 into 勉強/勉強's
traditional form, corrupting the furigana core and the link surface, and breaking the
preservation invariant.

The `zh-Hant` seeding step must therefore:

- run OpenCC only over the **Chinese prose spans**, masking out `{…|…}` wrappers and `⟦…⟧`
  links first (the same extraction regexes the preservation validator already specifies), and
- re-run the existing embedded-fragment preservation check (rule 6 of the sidecar schema) on
  the converted output, so any leak is caught by CI rather than shipped.

This is a real, Chinese-specific reason the conversion cannot be a one-liner — and a reason to
keep `zh-Hant` seeding inside the project's validated pipeline rather than as an external batch
job.

## 5. Font, search, and UI consequences

- **Font stack.** Simplified and traditional want different default fonts (e.g. Noto Sans SC
  vs. Noto Sans TC); a few characters even render with region-specific glyph shapes under the
  same Unicode codepoint (the Han unification "source separation" issue). `styles.css` needs a
  per-`lang` font stack keyed on the `lang`/`hreflang` attribute — trivial once the language
  code is `zh-Hans` vs. `zh-Hant`, impossible if both hide under a single `zh`.
- **Search index.** The [per-language gloss/tag index](../ideas/translation-sidecar-design.md)
  ([Architecture §search](../project/architecture.md#search)) is built per `target_lang`, so a
  simplified user searches simplified glosses and a (future) traditional user searches
  traditional glosses. Headword/reading/romaji search is shared (the invariant spine), so the
  index split is only over the translated glosses — cheap.
- **UI toggle granularity.** The language toggle
  ([Multilingual §6](../ideas/multilingual-dictionary.md#6-ui-storage-and-delivery)) lists
  "中文（简体）" now and can later add "中文（繁體）" as a sibling entry — no special-casing,
  because they are two ordinary language codes. The `localStorage` preference stores the full
  code (`zh-Hans`), so a returning user lands on the right script.

## 6. Decision record and what stays open

**Decided:**

- Simplified Chinese (`zh-Hans`, Putonghua norms) is the first Chinese deliverable, because the
  advisor works in simplified.
- The language-code space uses BCP-47 script subtags (`zh-Hans`, `zh-Hant`, `zh-Hant-TW`) from
  day one, so traditional is a later additive sidecar tree, never a retrofit.
- When traditional ships, it is seeded by OpenCC `s2twp` (phrase/region-aware) + human review,
  not by from-scratch translation and not by blind character substitution.

**Still open (deferred until traditional is actually prioritized):**

- **Whether `zh-Hant` ever ships at all** — gated on real Taiwan/HK learner demand
  ([Japanese-Learner Demand by L1](../research/japanese-learner-demand-by-l1.md) counts Taiwan
  inside the ~1.2M Chinese-L1 group; the within-group simplified/traditional split is not
  separately quantified there and would need its own demand read).
- **Generic `zh-Hant` vs. `zh-Hant-TW` vs. `zh-Hant-HK`** — "traditional" in practice means a
  *regional norm*, not a neutral script; the realistic deliverable is `zh-Hant-TW` (or `-HK`),
  and which one depends on where the demand is.
- **Whether the simplified advisor can also vet the traditional seed**, or whether a second
  traditional-script reviewer is needed — a staffing question, not a design one.

## Implications for je-dict-1

- The curator's "simplified first" decision is **fully compatible with later traditional
  support at near-zero rework cost**, *provided* the language code is `zh-Hans` (not bare `zh`)
  from the first sidecar written. That single naming choice is the entire forward-compatibility
  cost, and it is free.
- Traditional is cheap to add *later* but only because the [adaptation brief](../research/japanese-chinese-adaptation-brief.md)
  is script-neutral: the costly editorial content is authored once and inherited. This is an
  argument for keeping that brief script-neutral as it grows, rather than letting simplified
  examples harden into it.
- Simplified→traditional conversion is **lossy and must stay inside the validated pipeline**
  (one-to-many merges + vocabulary norms + embedded-fragment preservation), which is why this
  is a pipeline design question and not a post-processing afterthought.

## Related pages

- [Multilingual Dictionary](../ideas/multilingual-dictionary.md) — the hub plan; this page resolves and develops its §7 simplified/traditional open question
- [Japanese→Chinese Adaptation Brief](../research/japanese-chinese-adaptation-brief.md) — the script-neutral adaptation content that both variants share; its §7 points here
- [Translation Sidecar Design](../ideas/translation-sidecar-design.md) — the sidecar tree (`translations/zh-Hans/…`), the per-language i18n map, and the embedded-fragment preservation rule the converter must respect
- [Japanese-Learner Demand by L1](../research/japanese-learner-demand-by-l1.md) — the demand data that gates whether/when traditional ships
- [Multilingual Rendering and Delivery Architecture](multilingual-rendering-architecture.md) — generalizes this page's §5 font-stack and per-language search-index split into the full delivery design (separate URLs, `hreflang`, the GitHub Pages 1 GB ceiling); the language toggle lists 中文（简体） now and 中文（繁體） later as ordinary sibling codes
- [Architecture and Build System](../project/architecture.md) — the per-language search index and build join these codes parameterize

## References

- *Ambiguities in Chinese character simplification.* Wikipedia. (One-to-many simplified→traditional merges: 干/乾/幹, 后/後, 发/發/髮, 里/裡, 面/麵; why the direction is hard to automate.)
- BYVoid (Carbo Kuo). *OpenCC — Open Chinese Convert.* GitHub: https://github.com/BYVoid/OpenCC. (Conversion configs `s2t`/`s2tw`/`s2twp`/`s2hk`; phrase- and region-aware mapping; distinguishes one-to-many character vs. variant mappings.)
- *Simplified to Taiwan Traditional Chinese: Are You Doing It Right?* toolkk.com. (软件→軟件 vs. 軟體; why script conversion ≠ localization.)
- *Traditional vs Simplified Chinese: Key Differences Explained.* Laoret. (Mainland/Taiwan vocabulary divergence: 信息/資訊, 网络/網路, 视频/影片, 营销/行銷.)
