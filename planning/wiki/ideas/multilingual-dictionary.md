# Multilingual Dictionary: Adding Target Languages Beyond English

**Last updated**: 2026-06-06

## Overview

je-dict-1 is currently a Japanese→English learner's dictionary. The curator wants to
extend it into a **Japanese→multilingual** learner's dictionary, where the same Japanese
content (headwords, readings, example sentences) is paired with explanations in a
user-chosen target language: Japanese→Chinese, Japanese→Korean, Japanese→Vietnamese, and
others. The user would pick a target language with a toggle at the top of the page, and
the choice would persist in the browser.

This page is the standing plan for that project. It is intentionally comprehensive so that
future wiki-maintenance sessions can pick up any sub-thread — schema design, the AI
translation pipeline, note adaptation, build-script changes, UI — and develop it further
without re-deriving the whole picture. **It is a plan, not a record of work done.** Nothing
here has been implemented yet.

### The curator's stated design intent (anchor constraints)

These came directly from the curator and should be treated as fixed unless explicitly
revisited:

1. **Headwords and example sentences stay identical across all language versions.** The
   Japanese is the invariant spine of the dictionary. Only the *explanatory* material
   changes language.
2. **Notes are *largely* the same across languages, with targeted adaptation** for calques,
   false friends, cultural differences, and other L1-specific issues. They are not
   re-authored from scratch per language; they are translated and then selectively adapted.
3. **Glosses, definitions, explanations, and notes are rendered in the target language.**
4. **Chinese is the first additional language.** A native Chinese teacher of Japanese has
   agreed to advise. It is not yet known whether she is from the mainland (→ simplified,
   Putonghua norms) or Taiwan (→ traditional, Guoyu norms) — see
   [§7 Per-language considerations](#7-per-language-considerations).
5. **Further languages are demand- and feasibility-driven.** Add a language when (a) there
   is real learner demand from that L1 group and (b) current LLMs can produce acceptable
   quality for that language pair.

## 1. What is invariant vs. what is translated

The single most important technical fact for this project is that the entry JSON cleanly
separates Japanese-invariant content from target-language content. An audit of
`build/schema.json` (2026-06-06) gives the exact field inventory.

### Language-invariant fields (shared by every language version)

| Field | Notes |
|-------|-------|
| `id`, `schema_version` | identity |
| `headword`, `reading`, `romaji` | the Japanese spine |
| `part_of_speech`, `metadata.tags` (pos, semantic, formality, politeness) | classification — language-neutral codes, *rendered* via per-language label maps |
| `examples[].japanese` | the Japanese sentence, **including** its furigana wrappers and inline `⟦…→base：id⟧` links |
| `conjugation.forms[].form` (the Japanese forms) | generated tables; the Japanese is invariant |
| `predicates_requiring`, `fixed_patterns`, `particle_contrasts[]` Japanese fragments | the Japanese members of these structured particle fields |

### Target-language fields (translated/adapted per language)

| Field | Translation character |
|-------|----------------------|
| `gloss` (top-level) | short equivalent — direct translation |
| `definitions[].gloss` | short equivalent — direct translation |
| `definitions[].explanation` | prose — translation, light adaptation |
| `examples[].english` → `examples[].<lang>` | sentence translation |
| `examples[].notes` | usually null; prose when present |
| `notes` | the big structured field — translation **with** L1-specific adaptation |
| `cross_references[].label`, `prominent_see_also[].label` | short relationship labels |
| `common_mistakes[].explanation` | prose — **high adaptation** (errors are L1-specific) |
| `particle_contrasts[].explanation` | prose — translation, some adaptation |
| `conjugation.forms[].label` ("Past", "Negative", …) | a **fixed, closed set** — belongs in a shared per-language label map, **not** translated per entry |

The `examples[].english` key name is English-specific and will need generalizing (see
[§3](#3-schema-and-storage-options)). The `conjugation.forms[].label` insight matters: there
are ~30 distinct form labels repeated across thousands of verb/adjective entries.
Translating them per entry would be 30 × N wasted translations and a consistency hazard.
They should be translated **once per language** as a build-time label dictionary, exactly as
the POS/semantic/politeness tag display names should be.

### The notes field is the hard case

`notes` is target-language prose, but it embeds Japanese collocations with furigana
(`{漢字|かんじ}`) and inline `⟦…⟧` links (see the 05000_manjuu entry for a representative
example). A translation pipeline must:

- translate the surrounding prose into the target language,
- **preserve** the embedded Japanese fragments and their furigana wrappers byte-for-byte,
- **preserve** the `⟦surface→base：entry_id⟧` link structure (the `entry_id` is invariant;
  only any human-readable label inside would change), and
- adapt the *content* where the note makes a claim that is English-specific (e.g.
  "like the English word X") — see [§5](#5-how-notes-adapt-per-target-language).

This is the field where naive machine translation will most often corrupt structure, and
where the most editorial judgment is needed. It should drive the design of the translation
tooling.

## 2. Source of truth and the staleness problem

The English version is the **pivot and source of truth**. Translations are derived from it.
This creates a synchronization obligation that is the central long-term maintenance risk:
**when an English entry is polished or revised, its translations silently go stale.**

The project already revises entries constantly (comprehensive-polish advances daily; see
[Content Pipeline](../project/content-pipeline.md)). Any multilingual design must answer:
when `notes` on entry 05000 changes, how does the Chinese version know it is out of date?

**Recommended mechanism: per-field source hashing.** Each translated field stores a hash
(or a copy) of the English source text it was translated from, plus a timestamp and the
model/translator used. A `check_translation_staleness.py` script compares the stored hash
against the current English field and emits a re-translation queue. This mirrors the
existing multi-model review queue pattern (`reviews/queue.txt`) and the polishing-priority
mechanism — the project already knows how to run "find the stale things, queue them, work
the queue."

This staleness machinery is **not optional** and should be designed in from the start, not
bolted on. Without it, the non-English versions decay into permanent disagreement with the
English version on every polishing pass — the same "two parallel sources of truth keep
diverging" failure already documented for duplicate entries in
[Cleanup Backlog](cleanup-backlog.md) → Priority 8.

> The sketch in this section is now worked out concretely — the normalization-and-hashing
> procedure, the four-state staleness machine (fresh / stale / missing / orphan), the
> re-translation queue format, and a `report.py` coverage block — in the companion page
> **[Translation Sidecar Design](translation-sidecar-design.md) §4**.

## 3. Schema and storage options

Three broad architectures. The recommendation is **Option B (sidecar files)**. A worked-out
version of the recommended option — a concrete sidecar JSON shape, the six referential-integrity
rules a `translation_schema.json` would enforce, the field-by-field invariant/translatable
partition keyed to the real `schema.json`, and the build-time join contract — now lives in
**[Translation Sidecar Design](translation-sidecar-design.md)**. The summary below states the
options and the recommendation; that page is the design.

### Option A — Nested fields in the canonical entry

Replace each translatable string with a per-language object:
`"gloss": {"en": "...", "zh": "...", "ko": "..."}`.

- **Pros**: one file per entry; everything co-located; atomic.
- **Cons**: every entry file is rewritten when *any* language is added; merge-conflict
  surface explodes for the parallel-agent pipeline; the file balloons; the English-only
  build and the daily polishing workflow now have to step around N languages they don't
  care about. Rejected as the default because it couples the (very active) English workflow
  to the translation workflow.

### Option B — Sidecar translation files (recommended)

Keep `entries/**/{id}_{romaji}.json` exactly as today (English remains in-place, or English
itself migrates to a sidecar later). Store each language's translated fields in a parallel
tree, e.g. `translations/zh/{range}/{id}.json`, containing **only** the target-language
fields plus the source hashes from [§2](#2-source-of-truth-and-the-staleness-problem):

```jsonc
// translations/zh/05000/05000.json
{
  "id": "05000_manjuu",
  "source_lang": "en",
  "gloss": "馒头（日式甜馅蒸包）",
  "definitions": [{ "sense_number": 1, "gloss": "…", "explanation": "…" }],
  "examples": [{ "id": "05000_manjuu_ex1", "translation": "…" }],
  "notes": "…",
  "_provenance": {
    "notes": { "src_hash": "…", "model": "…", "date": "…", "human_reviewed": true }
  }
}
```

- **Pros**: the canonical entry and the English-only workflow are untouched; adding a
  language is purely additive (new directory, no churn on `entries/`); per-language files
  are small; merge conflicts stay within one language; staleness hashes live next to the
  translation; build can include/exclude languages independently; a language can be at any
  completeness level without blocking others.
- **Cons**: an entry's content is split across files; tooling must join canonical + sidecar
  at build time; referential integrity (sidecar `id` and `examples[].id` must match the
  canonical entry) needs a validator.

### Option C — Per-language full copies of every entry

A complete `entries_zh/` tree. Rejected: duplicates all invariant content (furigana,
inline links, conjugation tables — the bulk of each file), so every furigana fix or new
inline link would have to be propagated by hand to N trees. This is Option A's coupling
problem made worse.

### Cross-cutting schema notes

- **Generalize `examples[].english`.** Rename to a neutral key (`translation`) inside the
  sidecar, or keep `english` only in the canonical file and use `translation` in sidecars.
- **Tag display names and conjugation labels** become per-language label maps stored once
  (e.g. `build/data/i18n/zh.json`), consumed by the renderer — not per-entry data.
- **A `translations` schema** (`build/translation_schema.json`) should validate sidecars,
  including that every `examples[].id` exists in the canonical entry and that embedded
  furigana/inline-link structure is preserved.

## 4. How the AI translation should be done

### Pivot strategy: translate from the polished English, not the Japanese

Counter-intuitively, the best source for the target-language explanations is usually the
**English** explanation, not the Japanese headword/examples. Reasons:

- The English `notes`/`definitions` already encode the *pedagogical* decisions (which
  senses to split, what to contrast, register warnings). Re-deriving these from the Japanese
  per language would re-do editorial work and produce inconsistent coverage across languages.
- Frontier LLMs are strongest at English↔X for most X.
- It keeps the English version canonical and the others faithful to it, which is what the
  curator wants ("notes largely the same").

But the **Japanese must be supplied as context** alongside the English, because (a) the
embedded Japanese fragments in `notes` have to be preserved, and (b) some adaptations
(false friends, calques) require reasoning about the Japanese word against the *target*
language, not against English. So each translation call gets: the Japanese entry (headword,
reading, examples) **and** the English fields to translate, **and** a per-language adaptation
brief (see [§5](#5-how-notes-adapt-per-target-language)).

### Pipeline shape (reuse existing infrastructure)

The project already has the right scaffolding; the translation pipeline should be modeled
on it rather than invented fresh:

- **Batch driver** analogous to `build/review_runner.py` (OpenRouter, range/ids selection,
  budget cap, dry-run, `--report`). Call it `build/translate_runner.py`.
- **Queue** analogous to `reviews/queue.txt` / the task queue — fed by
  `check_translation_staleness.py` and by "never-translated" detection.
- **Two-pass quality**, mirroring the screening→deep review design: a cheaper model does
  the bulk first-draft translation; a stronger model (or the human advisor) reviews flagged
  or high-value entries (basic/core tier, particles, culturally loaded items).
- **Structured output contract**: the model returns JSON matching the sidecar schema, with
  the embedded-Japanese-fragment preservation enforced by post-validation (reject and retry
  if a `{漢字|かんじ}` wrapper or `⟦…⟧` link was altered).

### Model choice and the "which Claude" note

Use the latest and most capable Claude models for the quality-sensitive passes (the current
family is Claude 4.x; Opus for deep/adaptation passes, Sonnet for bulk first drafts), with
OpenRouter access to other frontier models for cross-checking, exactly as the existing
multi-model review pipeline does. Per-language feasibility is partly a question of *which
models are good at that pair* — Chinese and Korean are well-served; lower-resource targets
(e.g. Vietnamese, and later Thai/Indonesian) need a calibration pass before committing, just
as `reviews/calibration_report.md` calibrated the furigana reviewers. The published evidence
behind these feasibility claims — high-resource status for ja/zh/ko, the junior-translator
quality yardstick, and the documented LLM weakness on the *false-friend* items this dictionary
cares about most — is now assembled in
[LLM Translation Quality for Japanese Language Pairs](../research/llm-translation-quality-japanese-pairs.md).

### Human-in-the-loop

For Chinese specifically, the curator has a native-speaker advisor. The pipeline should make
her work tractable: produce a **review-friendly diff view** (Japanese + English + proposed
Chinese, side by side), let her approve/edit, and record `human_reviewed: true` in
provenance. Prioritize her limited time on (a) the basic/core tiers, (b) false-friend and
cultural-difference entries, and (c) a calibration sample that tells us how good the raw LLM
output is before scaling.

## 5. How notes adapt per target language

This is the linguistically richest part of the project and the reason "just machine-translate
everything" is wrong. The English notes are written for an English-speaking learner. Some of
their content is **universal** (true of Japanese regardless of the learner's L1); some is
**English-specific** and must be replaced for other L1 groups.

### A taxonomy of note content by adaptation need

| Content type | Adapt for target language? | Example |
|--------------|---------------------------|---------|
| Core semantic explanation of the Japanese word | No — universal | "饅頭 is a steamed bun with sweet filling" |
| Collocations, compounds, type lists (the embedded Japanese) | No — preserve verbatim | 温泉饅頭, 紅白饅頭 |
| Cultural/encyclopedic background | Mostly no, but framing may shift | "given at weddings and celebrations" |
| **Contrast with the *English* word** | **Yes — replace** | "unlike English 'mansion', マンション means apartment" |
| **False friends** | **Yes — language-specific** | see below |
| **Calque / cognate warnings** | **Yes — language-specific** | Sino-Japanese vs. Sino-Chinese readings |
| Register/politeness guidance | Mostly universal; sometimes reframed | keigo explanations |
| L1-specific common mistakes (`common_mistakes`) | **Yes — fully L1-specific** | particle errors differ by L1 |

The guiding principle matches the curator's intent: **translate the universal content,
replace the L1-contrastive content.** The adaptation brief handed to the translation model
(and to the human reviewer) should enumerate, per target language, the specific contrastive
phenomena to watch for.

### Chinese-specific adaptation (the first language)

The fully developed version of this section now lives in its own page:
**[Japanese→Chinese Adaptation Brief](../research/japanese-chinese-adaptation-brief.md)** — the
operational reference for the Chinese pipeline and the human advisor. It expands the seed table
below into the 文化庁 S/O/D/N triage, a sourced false-friend (同形異義語) table, the
partial-overlap (O) and calque/part-of-speech production hazards, the L1-specific
`common_mistakes` to substitute (の-overgeneralization from 的, transitivity-pair confusion), and
a "what to drop from the English notes" table. The summary below is the seed; the brief is the
working document.

The wiki also contains the research backbone for this in
[L1 Transfer in Japanese L2 Vocabulary](../research/l1-transfer-japanese-vocabulary.md). Key
adaptation drivers for a Japanese→Chinese version:

- **Kanji/hanzi false friends (同形異義語)** are the single highest-value addition. Chinese
  learners arrive with high (often wrong) confidence about kanji compounds. Notes for these
  words should *lead* with the divergence. Documented examples to seed an adaptation list:

  | Japanese | Japanese meaning | Chinese (same/similar characters) meaning |
  |----------|------------------|-------------------------------------------|
  | 勉強 | study | 勉强 = reluctantly; barely |
  | 手紙 | letter | 手纸 = toilet paper |
  | 大丈夫 | all right; safe | 大丈夫 = a real man |
  | 新聞 | newspaper | 新闻 = news |
  | 丈夫 | sturdy; healthy | 丈夫 = husband |
  | 経理 | accounting | 经理 = manager |

  These divergences are **irrelevant to an English speaker** (the English notes mostly don't
  mention them) but **essential** for a Chinese speaker. So Chinese notes are not merely a
  translation of the English notes — for this class of word they carry *additional*
  content the English version never had. This is the clearest case where "largely the same,
  with adaptation" means "plus a Chinese-only false-friend warning."

- **Reading interference**: Chinese learners must suppress hanzi pronunciations and learn
  on'yomi/kun'yomi. Notes can lean on the shared character meaning while flagging that the
  reading is unrelated to Mandarin.

- **What to drop**: the gairaigo false-friend warnings that are valuable for English
  speakers (マンション, サービス, ナイーブ…) are *less* central for Chinese speakers, though
  still useful since the loanwords are from English. Keep them but they are lower priority
  than the kanji false friends.

- **`common_mistakes` are L1-specific.** Particle-error research shows acquisition patterns
  differ by L1 (Korean > English > Chinese for case markers; see
  [Japanese Particles in L2 Acquisition](../research/japanese-particles-l2.md)). The
  English-oriented mistake notes should be replaced, not translated, for each L1.

### Generalizing to later languages

- **Korean**: shares Sino-Korean vocabulary (on'yomi correspondences) — emphasize the
  systematic phonological correspondences and the close grammatical alignment (SOV,
  particles), while warning against over-reliance on superficial similarity. False friends
  exist but are fewer than Chinese.
- **Vietnamese**: has a large Sino-Vietnamese stratum (Hán-Việt) giving partial cognate
  access to kango, but the modern script (Latin, chữ Quốc ngữ) removes the character bridge —
  an intermediate case between Chinese (full character bridge) and English (none).
- The **adaptation brief per language** is itself a wiki-maintainable artifact: a page per
  target language listing the false-friend tables, the calque pitfalls, the
  common-mistake patterns, and what to drop from the English notes. These briefs feed both
  the LLM pipeline and the human reviewers.

## 6. UI, storage, and delivery

- **Language toggle** at the top of every page (entry pages, browse, search, articles).
  Persist the choice in `localStorage`; read it on load and render the chosen language's
  fields, falling back to English when a translation is missing or stale.
- **Default and fallback**: English remains the default for first-time visitors and the
  universal fallback. A partially translated language must degrade gracefully field by field
  (translated gloss, English notes) rather than all-or-nothing.
- **Static-site implications**: the site is fully static (GitHub Pages). Two sub-options:
  1. **Per-language static pages** — `build_flat.py` emits `/zh/05000_manjuu.html` etc. Best
     for SEO and for serving users who land via search engines in their language; multiplies
     the page count by N.
  2. **Single page + client-side swap** — ship all languages' fields in the page (or fetch a
     per-entry language JSON) and swap text via JS on toggle. Lighter to build, weaker SEO,
     larger initial payload.
  A hybrid is likely best: per-language static pages for SEO with a client-side toggle that
  navigates between them and remembers the preference. This needs a dedicated design pass.
- **Search index per language**: `search_index_builder.py` builds a JS index over
  headwords, readings, glosses, and tags (see
  [Architecture](../project/architecture.md#search)). Glosses and tag display names are
  language-specific, so a per-language search index (or a language dimension within the
  index) is required so a Chinese user can search by Chinese gloss. Headword/reading/romaji
  search is shared.
- **`hreflang` / SEO**: per-language pages should declare `hreflang` alternates so search
  engines serve the right language version.
- **Font and rendering**: simplified vs. traditional Chinese, Korean, and Vietnamese
  diacritics all have font-stack implications in `styles.css`.

## 7. Per-language considerations

### Chinese: simplified vs. traditional (open decision)

The advisor's origin (mainland vs. Taiwan) is unknown. This is not a cosmetic choice:

- **Script**: simplified (mainland, Singapore) vs. traditional (Taiwan, Hong Kong).
- **Vocabulary and norms**: 软件/軟體 (software), 信息/資訊 (information), and many everyday
  terms differ between Putonghua and Guoyu norms beyond mere character simplification.
- **Conversion is not purely mechanical**: simplified↔traditional has one-to-many mappings
  (e.g. 后/後) that need context, so auto-converting one into the other is lossy.

**Recommendation**: treat "Chinese (Simplified)" and "Chinese (Traditional)" as potentially
*two* target languages (`zh-Hans`, `zh-Hant`) rather than one, even if only one ships first.
Pick the advisor's variant as the first deliverable; design the language code space so the
other variant can be added later (possibly seeded by assisted conversion + human review
rather than full re-translation). **This question should be resolved with the advisor before
the Chinese pipeline is built**, since it affects the language code, the model prompt, and
the glossary.

### Demand- and feasibility-ranking for later languages

The curator will choose later languages by demand × LLM feasibility. Inputs the wiki can
help assemble:

- **Demand**: now quantified in
  [Japanese-Learner Demand by L1](../research/japanese-learner-demand-by-l1.md) from the Japan
  Foundation's 2021 survey (~3.79M learners worldwide). Re-read by L1 and dropping the
  already-served English populations, **Chinese is the largest unserved group (~1.2M, China +
  Taiwan), then Indonesian (~712K), then Korean (~470K)**, with Thai and Vietnamese growing via
  technical-intern and study programs. The data confirms "Chinese first" and points to Korean as
  the strongest second candidate; see that page for the country→L1 mapping and the caveats
  (country ≠ L1; cohort-type fit; triennial lag).
- **Feasibility**: high-resource pairs (Chinese, Korean) are low-risk for current LLMs;
  lower-resource pairs need a calibration sample before committing. The calibration step is
  a direct analogue of `reviews/calibration_report.md`. The MT-evaluation evidence is now
  collected in [LLM Translation Quality for Japanese Language Pairs](../research/llm-translation-quality-japanese-pairs.md),
  which confirms ja/zh/ko are all high-resource (feasibility "green" for the first two
  targets) but warns that the per-item risk concentrates on exactly the false-friend content
  the Chinese brief targets — so demand and feasibility agree on Chinese-first, Korean-second.

## 8. Build-script and pipeline adaptations (inventory)

A first-cut list of what changes. Most are additive; the English-only path must keep working
throughout.

| Script / area | Change |
|---------------|--------|
| `build/schema.json` | unchanged (canonical stays English/invariant) |
| `build/translation_schema.json` (new) | validate sidecar translation files |
| `build/validate.py` | optional `--lang` mode to validate sidecars + referential integrity |
| `build/translate_runner.py` (new) | batch LLM translation, modeled on `review_runner.py` |
| `build/check_translation_staleness.py` (new) | compare source hashes, emit re-translation queue |
| `build/build_flat.py` | join canonical + sidecar; emit per-language pages; `--lang`/`--all-langs` |
| `build/entry_renderer.py` | render chosen language's fields; English fallback; language toggle |
| `build/page_generators.py` | per-language navigation/browse pages |
| `build/search_index_builder.py` | per-language gloss/tag index |
| `build/data/i18n/<lang>.json` (new) | translated tag display names + conjugation form labels |
| `build/article_renderer.py` | same language treatment for expository articles |
| `report.py` | a "TRANSLATION COVERAGE" section (per-language % translated, % stale) |
| inline-link tooling (`generate_word_lookup.py`) | unaffected — links key on invariant `entry_id` |
| CI (`validate.yml`) | validate sidecars when present |
| task queue / orchestrator | a `translate` and `translate-review` task type for parallel work |

The inline-link system is a quiet win: because links resolve on invariant `entry_id`, the
entire cross-reference graph is **shared across all languages for free** — only any
human-readable label needs translating, and labels are short.

The new files in this table — `translation_schema.json`, the sidecar layout, the staleness
checker, and the build-time join — are specified concretely in
[Translation Sidecar Design](translation-sidecar-design.md).

## 9. Phasing / rollout

A staged plan that de-risks before scaling:

1. **Design lock-in**: resolve the storage option ([§3](#3-schema-and-storage-options)), the
   staleness mechanism ([§2](#2-source-of-truth-and-the-staleness-problem)), and the
   simplified/traditional question with the advisor ([§7](#7-per-language-considerations)).
2. **Calibration sample**: translate ~50 entries (spanning a verb, a na-adjective, a
   culturally loaded noun, a particle, a false-friend kanji compound) into Chinese with the
   pipeline; have the advisor review; write a calibration report. This tells us the real
   raw-LLM quality and the human-edit rate before committing to 12,000+.
3. **Tier-first rollout**: translate basic (~800) then core (~2,000) tiers — the highest-value,
   most-consulted entries — with human review, before touching the general tier.
4. **UI pilot**: ship the toggle with English + Chinese-for-translated-entries (English
   fallback elsewhere) and gather user feedback.
5. **Scale the general tier** via the two-pass pipeline with spot-check review.
6. **Second language** (likely Korean) reusing all infrastructure; the only new artifacts are
   the per-language adaptation brief and i18n label map.
7. **Maintain sync** indefinitely via the staleness queue as English entries keep being
   polished.

## 10. Open questions and risks

- **Storage option** — sidecar (recommended) vs. nested; lock before building.
- **Simplified vs. traditional Chinese** — resolve with the advisor; design for both codes.
- **Staleness at scale** — every English polish invalidates translations; the hash-queue must
  exist from day one or the versions diverge permanently (cf.
  [Cleanup Backlog](cleanup-backlog.md) → Priority 8).
- **Adaptation vs. translation boundary** — over-adapting loses the "largely the same"
  intent and multiplies maintenance; under-adapting ships notes that ignore the learner's
  actual L1 (the whole point of false-friend warnings). The per-language adaptation brief is
  the control surface.
- **Embedded-Japanese preservation** — translation must not touch furigana wrappers or
  `⟦…⟧` links; enforce by post-validation, not by trusting the model.
- **Per-language page explosion** — N × 12,000 static pages has build-time and repo-size
  cost; measure before committing to full per-language static rendering.
- **Quality accountability** — for languages with no human advisor, what review bar ships?
  The multi-model cross-check pattern is the fallback, but it is weaker than a native
  reviewer.
- **Translating the embedded *English-in-notes* contrasts** — some notes explicitly compare
  to English ("like the English word…"); these must be detected and rewritten, not literally
  translated into "像英语单词…", which would be useless to a Chinese learner.

## Implications for je-dict-1

- This is the largest structural expansion contemplated for the project — larger than proper
  names ([Dictionary Growth](dictionary-growth.md)) — because it multiplies the *content*
  axis rather than just adding entries. But it is unusually tractable here because the schema
  already isolates target-language fields from the invariant Japanese spine, and because the
  existing review/queue/orchestrator infrastructure is the right shape to reuse.
- The **single highest-leverage early decision** is the source-of-truth + staleness design.
  Get that right and translations stay honest as the English version evolves; get it wrong
  and the project accrues silent divergence on every polishing pass. This decision is now
  developed into a concrete, critique-able proposal in
  [Translation Sidecar Design](translation-sidecar-design.md) — a fixed sidecar shape, six
  referential-integrity rules, a four-state staleness machine with a normalizer, the queue
  format, and a field-level fallback contract — so the next step toward it is the calibration
  sample, not more design.
- The **first concrete deliverable** should be small and advisor-reviewed: a ~50-entry
  Chinese calibration sample that measures raw LLM quality and human-edit rate. Everything
  else scales from what that reveals.
- The per-language **adaptation brief** for Chinese now exists as a developed page —
  [Japanese→Chinese Adaptation Brief](../research/japanese-chinese-adaptation-brief.md) — seeded
  from the false-friend table above and expanded with the 文化庁 S/O/D/N triage, sourced D/O
  tables, calque/POS production hazards, L1-specific `common_mistakes`, and a what-to-drop table.
  Both halves of the **demand × feasibility** gate now have dedicated pages
  ([demand](../research/japanese-learner-demand-by-l1.md) and
  [feasibility](../research/llm-translation-quality-japanese-pairs.md)), and the **sidecar
  schema** is now a worked draft ([Translation Sidecar Design](translation-sidecar-design.md)).
  Future sessions can still productively develop: the **per-language static vs. client-side
  rendering** trade-off (the one major design question still only sketched, in §6); the
  simplified/traditional (`zh-Hans`/`zh-Hant`) handling as its own worked design; or the
  parallel **Korean** and **Vietnamese** adaptation briefs (same structure, different contents).

## Related pages

- [Translation Sidecar Design](translation-sidecar-design.md) — the worked design for the recommended storage option (§3) and staleness mechanism (§2): concrete sidecar shape, referential-integrity rules, hashing/queue, fallback contract
- [Japanese→Chinese Adaptation Brief](../research/japanese-chinese-adaptation-brief.md) — the developed per-language brief for the first additional language (S/O/D/N triage, false-friend tables, L1-specific mistakes, what to drop)
- [Japanese-Learner Demand by L1](../research/japanese-learner-demand-by-l1.md) — JF 2021 learner-population data re-read by L1, supplying the §7 demand ranking
- [LLM Translation Quality for Japanese Language Pairs](../research/llm-translation-quality-japanese-pairs.md) — the feasibility half of the §7 demand × feasibility gate: ja/zh/ko all high-resource, but per-item false-friend risk concentrated
- [L1 Transfer in Japanese L2 Vocabulary](../research/l1-transfer-japanese-vocabulary.md) — the research backbone for note adaptation (Chinese/Korean/English false friends, transfer by stratum)
- [Translation Equivalence](../research/translation-equivalence.md) — the bilingual mapping problem, now multiplied across languages
- [Definition and Gloss Strategies](../research/definition-strategies.md) — gloss-writing techniques that each language version must re-apply
- [Cultural Content in Bilingual Dictionaries](../research/cultural-content-dictionaries.md) — culture-bound terms and the encyclopedic boundary, which shift by audience
- [Architecture and Build System](../project/architecture.md) — the build pipeline these changes extend
- [Entry Design](../project/entry-design.md) — the schema whose fields split into invariant vs. translated
- [Content Pipeline](../project/content-pipeline.md) — the polishing flow that creates the staleness obligation
- [Multi-Model Proofreading](multi-model-proofreading.md) — the review pipeline whose shape the translation pipeline should reuse
- [Dictionary Growth and Long-Term Vision](dictionary-growth.md) — the other major expansion axis (more entries vs. more languages)
- [Japanese Particles in L2 Acquisition](../research/japanese-particles-l2.md) — why `common_mistakes` are L1-specific and must be replaced, not translated
