# Schema Tag Reliability: When Metadata Drifts from Reality

**Last updated**: 2026-05-11

## Overview

Every je-dict-1 entry carries a `metadata.tags` block that classifies the word along several axes: part of speech, formality, politeness, semantic field, verb class, transitivity, and so on. These tags are not just decoration — they drive search facets, page rendering decisions, automated polishing tasks (which entries to inspect for transitivity, which to retrofit with conjugation tables), and consistency checking. When a tag is wrong, downstream tools either skip work they should do or perform work they shouldn't.

This page documents a class of recurring problem surfaced by entry-level inspection: cases where the tag block disagrees with the entry's actual content or with established Japanese-linguistics categorization. The mismatches fall into three broad patterns — **runaway automation** (a tag triggers machinery the entry didn't need), **categorical compression** (the schema's options can't represent the actual phenomenon), and **stale auto-labels** (a tag that was plausible at creation time but no longer matches the polished entry).

The page is descriptive, not prescriptive. Concrete cleanup work belongs in [Cleanup Backlog](../ideas/cleanup-backlog.md); tooling proposals belong in [Tooling Backlog](../ideas/tooling-backlog.md). This page tries to step back and ask why these mismatches keep appearing.

## Runaway automation: when a tag triggers wrong machinery

### Case study: spurious onomatopoeia conjugations

Twelve adverbial onomatopoeia entries — ぐつぐつ, ぱくぱく, じゃぶじゃぶ, ぼうぼう, ぽつぽつ, ごつごつ, むくむく, ごうごう, ぷくぷく, ぶるぶる, こつこつ, ぎゅうぎゅう — currently carry a full godan **conjugation block**. The block produces nonsense forms:

| Headword | Generated "present negative" | Generated "polite" |
|----------|-----------------------------|--------------------|
| ぐつぐつ | ぐつぐたない | ぐつぐちます |
| こつこつ | こつこたない | こつこちます |
| ぱくぱく | ぱくぱかない | ぱくぱきます |

These are not real Japanese forms. The entries themselves are correctly written as adverbs / mimetic words with `pos: ["adverb", "onomatopoeia"]` and notes that explain particle usage (`と` insertion before verbs) without claiming the word is itself a verb. The conjugation block is dead weight inherited from an upstream pipeline decision.

The mechanism is straightforward: `build/add_conjugations.py` looks at the entry's `metadata.tags.verb_class` and ending sound. At some point in the dictionary's history these adverbial mimetics were tagged with `verb_class: "godan-tsu"` (presumably because they end in つ) and the retrofit pass treated that tag as authoritative, generating conjugations as if the headword were a verb stem.

The lesson is broader than these twelve entries. **Tags become inputs to deterministic pipelines, and pipelines don't sanity-check their inputs.** Once a tag is wrong, every downstream tool that reads the tag inherits the error and may write further wrong data — in this case, a 17-form conjugation block.

This is the same dynamic that [Deterministic vs. Semantic Tasks](deterministic-vs-semantic-tasks.md) describes from the other direction: deterministic scripts can do tremendous work when the upstream data is right, but they have no judgment to push back when it isn't.

### Cleanup vs. defense in depth

The narrow fix is a one-shot script that scans for `pos: [..., "onomatopoeia"]` (or any non-verb POS) co-occurring with a `conjugation` block and removes the block. This is filed in [Tooling Backlog](../ideas/tooling-backlog.md).

The broader fix is a guard inside `add_conjugations.py` itself: refuse to write a conjugation block unless the entry has at least one verb POS tag. The retrofit script becomes self-defending: if a future pass mis-tags more onomatopoeia as `verb_class: "godan-tsu"`, it still won't get a conjugation table.

## Categorical compression: when the schema can't represent reality

### Case study: the four-bucket politeness field

The entry schema offers four values for `metadata.tags.politeness`: `plain`, `polite`, `humble`, `honorific`. This compression is too aggressive for the actual Japanese politeness system, which is multidimensional and overlapping. Three failure modes recur.

**Uchi/soto referent confusion.** The kinship terms 母 (はは), 父 (ちち), 兄 (あに), 姉 (あね), 息子 (むすこ) are all tagged `politeness: humble`. These are not humble forms in the technical keigo sense — they're the **plain** kinship terms used when referring to one's own family members in conversation with outsiders. The contrasting forms お母さん, お父さん, お兄さん, お姉さん are not "honorific" relative to them either — they're the address forms (used to address one's own family directly or to refer to other people's family members deferentially).

This is the **uchi/soto** (内/外, in-group/out-group) referent system, which [Keigo: Honorific Language](../research/keigo-honorifics.md) covers in detail. It is orthogonal to the speech-level honorific system (尊敬語/謙譲語/丁寧語), and the schema's single `politeness` axis cannot represent it without distortion.

**Bikago vs. true honorifics.** ご飯 (gohan), お釣り (otsuri), and several other entries are tagged `politeness: honorific`. These are 美化語 (bikago, "beautifying language") — words where the お〜/ご〜 prefix has fused into the lexical form. They are not productive honorifics referring to a respected party; they're just the polite-register variants of everyday nouns. Marking them `honorific` puts them in the same bucket as ご{覧|らん}になる ("to look at" — true sonkeigo) and いらっしゃい ("welcome" — true keigo expression), which obscures the actual distinction.

The 2007 Agency for Cultural Affairs reclassification ([Keigo: Honorific Language](../research/keigo-honorifics.md) → 5-category model) explicitly broke bikago out as its own category for this reason. je-dict-1's schema cannot.

**Diminutive suffixes labeled as honorifics.** The suffixes 〜ちゃん and 〜くん are tagged `politeness: honorific`. They are not honorifics — they are familiar/diminutive address suffixes, used with subordinates, children, classmates, or romantic partners. They mark *intimacy*, not deference. (Compare 〜さん, which is more neutral, and 〜様, which is genuinely deferential.)

Once again, the schema collapses things that the [Register and Formality Marking](../research/register-formality-marking.md) literature consistently treats as separate dimensions: deference (high/low), familiarity (close/distant), age-power asymmetry (superior/subordinate), and gender (male-marked/female-marked/neutral).

### Implications for the schema

The straightforward fix would be to widen `politeness` into a structured object:

```json
"politeness": {
  "speech_level": "plain | polite | humble | honorific",
  "referent_orientation": "in_group | out_group | neutral",
  "register_class": "bikago | sonkeigo | kenjōgo | teineigo | familiar_suffix | none",
  "familiarity": "intimate | neutral | distant"
}
```

But the cost is high: every existing entry would need a migration pass that is itself semantic (not deterministic). And the new structure is harder for entry-creation prompts to fill correctly.

A cheaper intervention is to **narrow the current tag's semantics by documenting what it does and does not cover**, then push the multidimensional information into notes prose. This is what the well-written entries already do — 00549_haha (母) explains the full system in its notes:

> 母: my mother (humble, to outsiders)
> お母さん: mother (neutral, direct address or others' mothers)
> お母さま: mother (very polite/formal)
> ママ: mom (casual, childish)

The notes carry the correct nuance; the tag is a coarse-grained search facet. As long as users encounter notes prominently in the rendered entry, the tag doesn't need to be the source of truth for nuance — only for filtering.

## Stale auto-labels: tags that no longer reflect the entry

Some tags were plausible at creation but became wrong as the entry evolved (or were never accurate). They persist because nothing currently re-checks them.

**Semantic field mismatches.** Entry 02008_ikuratemo (いくら〜ても, "no matter how much…") has `"semantic": ["furniture"]`. This is obviously wrong — it's a grammatical pattern, not a furniture word. The tag is almost certainly a hallucination or copy-paste artifact from an early creation session. Comprehensive-polish doesn't currently regenerate semantic tags, so the error persists across hundreds of revisions to the entry. The `polish_semantic_labels` task targets this class of issue but at 13.4% progress hasn't reached the broader sweep.

**Stale verb_class tags after POS clarification.** The onomatopoeia conjugation case (above) is essentially this: at some point the entries had a verb_class tag that survived a later POS reclassification.

**Domain tags that overstate specificity.** A handful of entries carry domain tags that are technically correct but mislead — e.g., a general action verb domain-tagged with a narrow specialty because one of its example sentences happens to use specialty vocabulary.

The general pattern is that tags are **write-rarely, read-often**. Once written, they participate in every downstream lookup. The dictionary lacks a systematic re-check pass: there is no tool that compares an entry's current notes/glosses/examples against its tags and flags inconsistencies.

## Connection to existing wiki analyses

This phenomenon sits at the intersection of several existing topics:

- [Deterministic vs. Semantic Tasks](deterministic-vs-semantic-tasks.md) frames the broader problem of which work can run on tags alone. Tag drift makes the deterministic side more brittle than it appears.
- [Entry Consistency](entry-consistency.md) treats consistency mostly at the notes/cross-references level. Tag consistency is a parallel and currently less-addressed dimension.
- [Keigo: Honorific Language](../research/keigo-honorifics.md) and [Register and Formality Marking](../research/register-formality-marking.md) document the multidimensional structure that the four-bucket politeness tag cannot represent.
- [Grammar Information in Learner Dictionaries](../research/grammar-in-dictionaries.md) covers the broader tradition of grammar codes in learner dictionaries (Hornby's L,D,T codes; LDOCE's grammar patterns) — all of which face the same compression problem.
- [Handling Homographs](homographs.md) and [Word Variants](word-variants.md) face a related issue: when one entry covers multiple kanji-variant senses (e.g., 取る's sense 2 actually written 撮る), the entry's tags can describe only one of the senses well.

## Detection sketches

These are not implementation plans, just notes on what a tag-drift detector might do.

**Mismatched POS / conjugation:** Trivial — any entry with `conjugation` whose `pos` list contains no `verb-*` tag is suspicious. Twelve entries currently match.

**Politeness tag vs. note prose:** Where the politeness tag is `humble` or `honorific`, the notes should contain the keyword "humble" or "honorific" (or equivalent explanation). Where they don't, either the tag is misapplied or the notes need expansion. Cheap to implement; flags both directions of error.

**Semantic tag vs. gloss / definition:** Compare the entry's semantic tags against keywords extracted from the gloss and example translations. Outliers (e.g., a `semantic: ["furniture"]` tag with no furniture-related words in any field) should be flagged. This needs a hand-curated keyword-per-tag list, but the tag vocabulary is small enough (~80 values) to make this tractable.

**Cross-entry tag consistency:** Across entries linked by `cross_references` of type `synonym` or `antonym`, the semantic tags should largely agree. Big divergences flag either a wrong cross-reference or a wrong tag.

## Implications for je-dict-1

1. **Treat tags as cached judgments, not ground truth.** When a polish pass updates an entry, the tags should be re-evaluated against the polished content, not assumed correct. The polish prompts currently don't ask for this.

2. **Defend deterministic scripts at their boundaries.** `add_conjugations.py` should require a verb POS tag, not just a verb_class hint. `validate_tags.py` should reject the combination of `onomatopoeia` POS plus a `verb_class` tag.

3. **Don't widen the schema until cheaper interventions are exhausted.** A structured politeness object would be more accurate but expensive to migrate and harder for entry-creation prompts to fill. The notes prose already carries the nuance for well-polished entries; the leverage is in making polish passes regenerate suspect tags.

4. **Build a tag-drift detector pass.** Even a simple heuristic check (mismatched POS/conjugation; politeness tag with no politeness keyword in notes; semantic tag with no semantic-keyword overlap) would surface most cases. Tag drift is a quietly accumulating debt: small per entry, large in aggregate.

5. **Document the schema's known limits explicitly.** The entry-guidelines and other skills should state plainly that the `politeness` tag is a four-bucket compression of a multidimensional system, and that the notes prose carries the nuance. This sets expectations for both prompts and curators.

## Related pages

- [Deterministic vs. Semantic Tasks](deterministic-vs-semantic-tasks.md) — broader frame for where automation reliably works and where it doesn't
- [Entry Consistency](entry-consistency.md) — consistency in notes structure and cross-references
- [Keigo: Honorific Language](../research/keigo-honorifics.md) — the full structure that the politeness tag compresses
- [Register and Formality Marking](../research/register-formality-marking.md) — diasystematic labels and the consultation gap
- [Cleanup Backlog](../ideas/cleanup-backlog.md) — actionable cleanup items
- [Tooling Backlog](../ideas/tooling-backlog.md) — proposed scripts (including onomatopoeia conjugation pruner)
- [Entry Follow-ups](../ideas/entry-followups.md) — specific entries identified
