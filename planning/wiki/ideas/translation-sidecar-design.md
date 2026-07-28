# Translation Sidecar Schema and Staleness Mechanism (Worked Design)

**Last updated**: 2026-06-06

## Overview

This is a worked-out companion to the [Multilingual Dictionary](multilingual-dictionary.md)
plan. That plan recommends **Option B — sidecar translation files** ([§3](multilingual-dictionary.md#3-schema-and-storage-options))
and **per-field source hashing** for staleness ([§2](multilingual-dictionary.md#2-source-of-truth-and-the-staleness-problem)),
and its own "Implications" section names the **source-of-truth + staleness design** as *"the
single highest-leverage early decision."* But the plan leaves both at the sketch level. This
page turns the sketch into a concrete, reviewable design: an actual sidecar JSON shape, the
referential-integrity rules a `build/translation_schema.json` would enforce, the exact
normalization-and-hashing procedure, the staleness state machine, the re-translation queue
format, and the embedded-Japanese-fragment preservation contract.

It is still **design, not implementation** — nothing here has been built, and (per the
session constraints) this page does not modify any schema, script, or entry. It exists so a
future implementation session, or the curator, can critique a specific proposal rather than
re-derive one.

## 1. What the sidecar must hold — derived from the real schema

An audit of `build/schema.json` (the live entry schema, re-read 2026-06-06) lets us partition
every entry field into **invariant** (Japanese spine — never enters a sidecar) and
**translatable** (target-language — the sidecar's payload). This is the precise version of
the inventory in [multilingual §1](multilingual-dictionary.md#1-what-is-invariant-vs-what-is-translated),
keyed to actual JSON paths.

### Invariant — stays in `entries/**`, never copied into a sidecar

| JSON path | Why invariant |
|-----------|---------------|
| `id`, `schema_version`, `headword`, `reading`, `part_of_speech` | identity + Japanese spine |
| `examples[].id`, `examples[].japanese` | the example's identity key and its Japanese sentence (with furigana + `⟦…⟧` links) |
| `examples[].has_audio`, `examples[].sense_numbers` | language-neutral structural data |
| `conjugation.*` (entire object) | generated Japanese forms; `label` is a closed set handled by an i18n map, **not** per-entry |
| `metadata.tags.*` (pos, transitivity, verb_class, formality, politeness, style, domain, semantic) | language-neutral **codes**; rendered through a per-language label map |
| `predicates_requiring.verbs[].word/example`, `fixed_patterns[].pattern/example`, `particle_contrasts[].particle/examples` | the Japanese members of structured particle fields |
| `prominent_see_also[].target_id/reading/headword`, `cross_references[].type/target_id/reading/headword` | the relationship graph keys (resolve on invariant `target_id`/`reading`) |
| all of `metadata.created/modified/ai_model/vocabulary_tier` | provenance of the **English** entry |

### Translatable — the sidecar payload

| JSON path | Translation character (per multilingual §1) |
|-----------|---------------------------------------------|
| `gloss` (top level) | short equivalent — direct |
| `definitions[].gloss` | short equivalent — direct (keyed by `sense_number`) |
| `definitions[].explanation` | prose — translate, light adapt |
| `examples[].english` | sentence translation → stored under a neutral key |
| `examples[].notes` | usually null; prose when present |
| `notes` | the hard field — translate **with** L1 adaptation; embeds Japanese fragments |
| `cross_references[].label`, `prominent_see_also[].note` | short relationship labels |
| `common_mistakes[].mistake/explanation` (and possibly `incorrect`/`correct` strings) | **high adaptation** — L1-specific |
| `predicates_requiring.description`, `predicates_requiring.verbs[].meaning` | prose/short gloss |
| `fixed_patterns[].meaning`, `fixed_patterns[].example_english` | gloss + example translation |
| `particle_contrasts[].explanation`, `particle_contrasts[].key_points[]` | prose — translate, some adapt |

Two design consequences fall straight out of this table:

1. **The sidecar mirrors the entry's array structure but only its translatable leaves.** A
   sidecar is not a free-form blob; it is a *shaped subset* whose array elements must line up
   with the canonical entry by stable key — `examples[].id`, `definitions[].sense_number`,
   and (for the structured particle fields) array index. That alignment requirement is what
   the validator in [§3](#3-the-translation-schema-and-referential-integrity) exists to guard.
2. **`examples[].english` must be renamed on the way into the sidecar.** The canonical key is
   English-specific. Inside `translations/zh/…` the same string lives under a neutral
   `translation` key. (multilingual §3 "Cross-cutting schema notes" already calls for this;
   here it is concrete.)

## 2. A concrete sidecar file

Using entry `05000_manjuu` (the plan's running example) and Chinese (`zh-Hans`) as the target:

```jsonc
// translations/zh-Hans/05000/05000_manjuu.json
{
  "id": "05000_manjuu",            // MUST equal the canonical entry id
  "target_lang": "zh-Hans",        // BCP-47-ish code; zh-Hans / zh-Hant / ko / vi …
  "source_lang": "en",             // the pivot the translation was derived from
  "schema_version": "t1.0",        // translation-sidecar schema version (independent of entry schema_version)

  "fields": {
    "gloss": {
      "value": "馒头（日式甜馅蒸包）",
      "src": "steamed bun with sweet filling",
      "src_hash": "sha256:1f3a…",        // hash of the normalized English source string
      "model": "anthropic/claude-sonnet-4-6",
      "date": "2026-06-06T00:00:00Z",
      "human_reviewed": false,
      "status": "fresh"                   // derived field, see §4 (may be omitted and computed at build)
    },

    "definitions[1].explanation": {
      "value": "…",                       // Chinese prose
      "src": "…",                         // the English explanation it was translated from
      "src_hash": "sha256:9c2b…",
      "model": "anthropic/claude-sonnet-4-6",
      "date": "2026-06-06T00:00:00Z",
      "human_reviewed": false
    },

    "examples[05000_manjuu_ex1].translation": {
      "value": "…",                       // Chinese sentence; the Japanese stays in the canonical entry
      "src": "…",
      "src_hash": "sha256:7e10…",
      "model": "anthropic/claude-sonnet-4-6",
      "date": "2026-06-06T00:00:00Z",
      "human_reviewed": false
    },

    "notes": {
      "value": "…",                       // Chinese notes WITH embedded {漢字|かんじ} and ⟦…⟧ preserved
      "src": "…",
      "src_hash": "sha256:b4d8…",
      "model": "anthropic/claude-opus-4-8",  // deep/adaptation pass for the hard field
      "date": "2026-06-06T00:00:00Z",
      "human_reviewed": true,
      "human_reviewer": "advisor-zh-01",
      "adaptations": ["false-friend:饅頭", "drop:gairaigo-contrast"]  // audit trail of §5-style edits
    }
  }
}
```

### Why this shape (flat field-map, not a deep mirror)

The payload is **a flat map keyed by a field path**, not a recursive copy of the entry tree.
Reasons:

- **Sparse by construction.** A sidecar holds only the fields that have been translated. A
  half-done language is just a sidecar with fewer keys — exactly the "degrade field by field"
  behavior the plan's UI section wants ([multilingual §6](multilingual-dictionary.md#6-ui-storage-and-delivery)).
  A deep mirror would force null-filling every untranslated branch.
- **Per-field provenance is the natural unit.** Staleness, model, and human-review status are
  all *per field* (you re-translate `notes` without disturbing `gloss`). A flat field-keyed
  map puts the provenance exactly where it is checked.
- **Stable keys, not positional.** `examples[05000_manjuu_ex1].translation` keys on the
  example's **id**, and `definitions[1].explanation` on its **sense_number** — both invariant
  identifiers — so reordering examples or senses in the canonical entry does not silently
  misalign translations. (Index-based keys like `examples[0]` would; avoid them.) The one
  unavoidable positional case is the particle structured fields, which have no per-element id;
  those need either an added stable key or careful index validation — flagged as an open
  question in [§7](#7-open-questions-this-design-surfaces).

## 3. The translation schema and referential integrity

A new `build/translation_schema.json` validates sidecars. Beyond ordinary JSON-Schema typing,
it must enforce **cross-file referential integrity** against the canonical entry — checks
JSON Schema cannot express alone, so they live in a `validate.py --lang` mode that loads both
files:

1. **`id` agreement** — sidecar `id` equals the canonical entry's `id`, and the file lives at
   the path implied by that id and `target_lang`.
2. **Example-id existence** — every `examples[<id>].translation` key references an
   `examples[].id` that exists in the canonical entry. (Catches translations stranded on a
   deleted/renumbered example.)
3. **Sense-number existence** — every `definitions[<n>].*` key references a `sense_number`
   present in the canonical entry.
4. **No invariant fields** — the sidecar must **not** contain `headword`, `reading`,
   `examples[].japanese`, `conjugation`, `metadata.tags`, etc. A sidecar that carries an
   invariant field is a bug (it will silently diverge from the spine).
5. **Provenance completeness** — every translated field carries `src_hash`, `model`, `date`,
   and `human_reviewed`. Missing provenance = cannot compute staleness = reject.
6. **Embedded-fragment preservation** — see [§5](#5-embedded-japanese-fragment-preservation).
   The set of `{漢字|かんじ}` furigana wrappers and `⟦…→base：id⟧` links in a translated
   `notes`/`explanation` must be a **superset-compatible** transform of the source: every
   `entry_id` inside a `⟦…⟧` link in the source must still appear, and every furigana wrapper's
   `漢字|かんじ` core must be byte-identical to one in the source. (The Chinese version may
   *add* a false-friend warning carrying *new* Japanese fragments — see the note below — so it
   is not strict equality, but nothing from the source may vanish or mutate.)

> **Why "superset-compatible," not "equal":** the [Japanese→Chinese Adaptation Brief](../research/japanese-chinese-adaptation-brief.md)
> establishes that for 同形異義語 words the Chinese notes legitimately carry *more* embedded
> Japanese than the English notes (a false-friend warning the English version never had). So
> the validator forbids **loss or mutation** of source fragments but permits **addition** of
> new well-formed ones. A pure equality check would wrongly reject exactly the highest-value
> adaptations.

## 4. The staleness mechanism in detail

This is the part the plan flags as non-optional. The mechanism has four parts: what is
hashed, how it is normalized, the state machine, and the queue.

### 4a. What is hashed, and how it is normalized

Each translated field stores `src_hash` = `sha256` of the **normalized** English source
string for that field. Normalization matters: without it, a cosmetic English edit (a
double-space collapse, a trailing-newline change from a reformat) would spuriously mark every
translation stale and flood the queue. The normalization, applied to the English source
*before* hashing, is:

1. Unicode NFC.
2. Strip leading/trailing whitespace; collapse internal runs of whitespace to a single space.
3. **Leave `{漢字|かんじ}` wrappers and `⟦…⟧` links byte-exact** — they are content, and a
   change to an inline link's target *should* invalidate the translation.
4. No case-folding, no punctuation stripping (punctuation can be meaning-bearing).

The same normalizer must be used at write time and at check time, or every field reads stale.
It belongs in a shared `build/translation_util.py` imported by both `translate_runner.py` and
`check_translation_staleness.py`.

> **Store the hash, not the source?** The example in [§2](#2-a-concrete-sidecar-file) stores
> both `src` (the full English source text) and `src_hash`. Storing the full source costs
> repo size but buys two things: a **human-readable diff** when a field goes stale (advisor
> sees old-English vs. new-English side by side), and the ability to **re-normalize and
> re-hash** if the normalizer ever changes without re-reading every historical entry. The
> recommendation is **store both**; the hash is the fast check, the text is the audit and
> diff surface. (If repo size becomes a real constraint at 12,000 × N, drop `src` for the
> general tier and keep it for basic/core, where advisor review is concentrated.)

### 4b. The staleness state machine

`check_translation_staleness.py` computes, per translated field, one of four states by
comparing the stored `src_hash` against the live normalized English field:

| State | Condition | Action |
|-------|-----------|--------|
| **fresh** | stored hash == current hash | none |
| **stale** | stored hash != current hash | enqueue for re-translation; UI keeps showing the (now-stale) translation with an optional "may be outdated" marker, OR falls back to English — a UI policy choice |
| **missing** | field exists in canonical, no sidecar entry | enqueue for first translation; UI falls back to English |
| **orphan** | sidecar entry whose canonical field no longer exists | flag for deletion (e.g. a sense was removed) |

The **stale** state is the whole reason the mechanism exists: it is produced *automatically*
every time a polishing pass edits an English field, with no action by the polishing session.
This is what keeps the non-English versions honest as the English keeps moving
([Content Pipeline](../project/content-pipeline.md) advances comprehensive-polish daily; the
divergence risk is the same "two parallel sources of truth" failure documented at
[Cleanup Backlog](cleanup-backlog.md) → Priority 8).

### 4c. The re-translation queue

Output is a queue file per language, modeled on `reviews/queue.txt` and the existing task
queue (the project "already knows how to run find-the-stale-things, queue them, work the
queue"):

```
# translations/zh-Hans/queue.txt — regenerated by check_translation_staleness.py
05000_manjuu  notes            stale    src_changed=2026-06-06
05000_manjuu  gloss            fresh    -
05012_xxxx    definitions[1]   missing  -
05033_yyyy    examples[..ex2]  stale    src_changed=2026-06-05
```

`translate_runner.py` consumes the queue exactly as `review_runner.py` consumes its range/ids,
with the same budget cap and two-pass (cheap-screen → strong/advisor) shape. A `--priority`
flag should let basic/core-tier and false-friend (D/O-class) entries jump the queue, reusing
the [polishing priority](../project/content-pipeline.md) idea.

### 4d. report.py coverage section

`report.py` gains a per-language **TRANSLATION COVERAGE** block: % fields fresh / stale /
missing per tier, and the queue depth. This makes drift visible the way the health dashboard
already makes furigana and cross-reference gaps visible, so a language silently rotting is a
dashboard regression rather than an invisible one.

## 5. Embedded-Japanese-fragment preservation

The `notes` field (and sometimes `explanation`) is target-language prose that embeds Japanese
collocations with furigana (`{漢字|かんじ}`) and inline `⟦surface→base：entry_id⟧` links. The
translation pipeline must preserve these structurally. Two enforcement points:

- **At generation:** the model is instructed to copy embedded fragments verbatim, and the
  structured-output contract is post-validated. A response that altered a furigana wrapper's
  `漢字|かんじ` core, or dropped/renamed an `entry_id` inside a `⟦…⟧` link, is **rejected and
  retried** — never trusted. (multilingual §4 "Structured output contract.")
- **At validation:** rule 6 of [§3](#3-the-translation-schema-and-referential-integrity)
  re-checks the same invariants on the stored sidecar, so a hand-edit by a reviewer that
  breaks a wrapper is caught by CI, not shipped.

The asymmetry from [§3](#3-the-translation-schema-and-referential-integrity) holds: **nothing
from the source may be lost or mutated; new well-formed fragments may be added** (the
false-friend-warning case). A practical extraction regex pair:

- furigana wrappers: `\{([^|{}]+)\|([ぁ-んァ-ヶー]+)\}` (note: the live data also contains a
  rarer nested/double-brace variant flagged at [Cleanup Backlog](cleanup-backlog.md) →
  Priority 9 — the extractor must tolerate it or the preservation check will false-positive on
  those entries).
- inline links: `⟦[^⟧]*→[^：]*：([0-9]{5}_[a-z]+(?:_[a-z]+)?)⟧` — the captured `entry_id` is
  the invariant that must survive.

Because inline links resolve on the invariant `entry_id`, the **entire cross-reference graph
is shared across all languages for free** — only the short human-readable label needs
translating. This is the quiet structural win the plan notes; the preservation validator is
what makes it safe to rely on.

## 6. Build-time join and rendering contract

`build_flat.py` gains a `--lang <code>` / `--all-langs` mode. For each entry it **joins** the
canonical entry with the requested sidecar:

1. Start from the canonical (English/invariant) entry.
2. For each translatable field, if the sidecar has a **fresh** translation, substitute it;
   otherwise keep English (the universal fallback).
3. Render tag labels and conjugation `label`s through `build/data/i18n/<lang>.json` (the
   once-per-language label map — never per entry).
4. Emit per-language static pages (`/zh-Hans/05000_manjuu.html`) with `hreflang` alternates,
   and/or ship the sidecar fields for a client-side toggle. The static-vs-client trade-off is
   its own design question ([multilingual §6](multilingual-dictionary.md#6-ui-storage-and-delivery))
   and is **out of scope here** — this page is about the data layer the renderer consumes,
   not the delivery layer. That delivery layer is now worked out in
   [Multilingual Rendering and Delivery Architecture](../topics/multilingual-rendering-architecture.md),
   which consumes this join and reuses the field-level fallback contract below.

The key contract for the renderer: **field-level fallback, never entry-level.** A Chinese page
for an entry with a translated `gloss` but a stale `notes` shows Chinese gloss + English notes,
not an all-or-nothing switch. This is what lets a language ship at 10% coverage and grow,
instead of blocking on 100%.

## 7. Open questions this design surfaces

- **Particle structured fields have no per-element stable key.** `particle_contrasts[]`,
  `predicates_requiring.verbs[]`, and `fixed_patterns[]` are positional arrays. Keying sidecar
  translations to them safely needs either (a) adding a stable `id` to each element in the
  canonical schema (a real entry-schema change, deferred), or (b) index-based keys guarded by
  a strict "array length and Japanese members unchanged" check, with the field marked stale
  whenever the array shape changes. Recommendation: **(b) for now**, since particles are a
  small, slow-changing entry set; revisit (a) if particle entries start churning.
- **Hashing granularity for `notes`.** A single hash over the whole `notes` field means *any*
  English edit re-flags the whole (expensive, advisor-reviewed) Chinese note as stale, even a
  one-word fix far from the adapted part. A future refinement is paragraph- or
  sentence-level sub-hashing so only the changed span re-queues. Deferred — start whole-field,
  measure how often `notes` churns, refine if the re-translation cost is real.
- **`src` storage cost at scale.** See [§4a](#4a-what-is-hashed-and-how-it-is-normalized) — the
  store-both recommendation may need a tier-conditional exception.
- **Where English itself lives.** This design leaves English in `entries/**`. A later option
  is to migrate English into its own sidecar (`translations/en/…`) so the canonical entry is
  *purely* invariant and every language including English is symmetric. Cleaner, but a large
  migration touching every entry — explicitly deferred by the plan, and nothing here depends
  on it.

## Implications for je-dict-1

- This page makes the plan's recommended Option B + per-field hashing **concrete enough to
  prototype**: a fixed sidecar shape, six referential-integrity rules, a four-state staleness
  machine with a normalizer, a queue format, and a field-level fallback contract. The next
  step toward implementation is not more design — it is the ~50-entry Chinese calibration
  sample ([multilingual §9](multilingual-dictionary.md#9-phasing--rollout)), which would
  exercise this sidecar shape against real advisor edits and reveal whether the
  whole-field-hash granularity and the superset-preservation rule survive contact with actual
  adaptations.
- The design deliberately **reuses existing project patterns** (queue + budget + two-pass from
  `review_runner.py`; dashboard coverage from `report.py`; priority from polishing) rather than
  inventing parallel machinery — lowering both build cost and the chance of a second
  divergent source of truth.
- The **highest-risk simplification** to validate early is whole-field `notes` hashing
  ([§7](#7-open-questions-this-design-surfaces)): if English `notes` churn turns out to be
  frequent and advisor `notes` review is the scarcest resource, sub-field hashing may need to
  move from "deferred refinement" to "ship from day one."

## Related pages

- [Multilingual Dictionary](multilingual-dictionary.md) — the hub plan this page develops (§2 staleness, §3 storage); see its §3 and "Implications" for why a worked sidecar/staleness design was the flagged next step
- [Japanese→Chinese Adaptation Brief](../research/japanese-chinese-adaptation-brief.md) — supplies the D/O false-friend classes that justify the "superset, not equality" preservation rule and the priority routing
- [Chinese Simplified/Traditional Handling](../topics/chinese-simplified-traditional.md) — why the example `target_lang` here is `zh-Hans` (not bare `zh`), and how a future `zh-Hant` becomes a parallel additive sidecar tree
- [LLM Translation Quality for Japanese Language Pairs](../research/llm-translation-quality-japanese-pairs.md) — the feasibility evidence for *whether* the model passes that feed this pipeline are good enough, and where (false friends) they are weakest
- [Content Pipeline](../project/content-pipeline.md) — the daily polishing flow that produces the staleness obligation this mechanism answers
- [Cleanup Backlog](cleanup-backlog.md) — Priority 8 (parallel sources of truth diverging) is the failure this design prevents; Priority 9 (nested furigana wrappers) is the edge case the preservation extractor must tolerate
- [Multi-Model Proofreading](multi-model-proofreading.md) — the `review_runner.py` queue/two-pass shape the translation pipeline reuses
- [Multilingual Rendering and Delivery Architecture](../topics/multilingual-rendering-architecture.md) — the delivery layer that consumes this join (§6) and the field-level fallback contract; the static-vs-client-side question this page scoped out
- [Architecture and Build System](../project/architecture.md) — the build pipeline `--lang` mode extends
