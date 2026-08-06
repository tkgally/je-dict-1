# Schema Tag Reliability: When Metadata Drifts from Reality

**Last updated**: 2026-08-06 (new section "The shape of the semantic-tag debt": the off-vocabulary queue measured whole-corpus at 2,530 entries / 3,208 instances / 687 names, with the taxonomy gap — `place`/`location`/`object`/`state`/`quality`/`manner`/`degree` — as its largest single block at 322 instances, confirmed from the corpus side after the reviewer side reached the same ten strings; and the sole-`general` gloss-keyword suggester measured and closed at 14.8% coverage, since inference from surrounding prose cannot be denotational and would manufacture P11 defects)

Prior 2026-06-13 (added `general`-tag reverse-direction noise finding to "The tag-vocabulary contradiction" section: ~88% of tag flags in the 03301–04300 range flag `general` as "too broad"; bulk-rejected; fix tracked in Tooling Backlog item 17)

## Overview

Every je-dict-1 entry carries a `metadata.tags` block that classifies the word along several axes: part of speech, formality, politeness, semantic field, verb class, transitivity, and so on. These tags are not just decoration — they drive search facets, page rendering decisions, automated polishing tasks (which entries to inspect for transitivity, which to retrofit with conjugation tables), and consistency checking. When a tag is wrong, downstream tools either skip work they should do or perform work they shouldn't.

This page documents a class of recurring problem surfaced by entry-level inspection: cases where the tag block disagrees with the entry's actual content or with established Japanese-linguistics categorization. The mismatches fall into three broad patterns — **runaway automation** (a tag triggers machinery the entry didn't need), **categorical compression** (the schema's options can't represent the actual phenomenon), and **stale auto-labels** (a tag that was plausible at creation time but no longer matches the polished entry).

The page is descriptive, not prescriptive. Concrete cleanup work belongs in [Cleanup Backlog](../ideas/cleanup-backlog.md); tooling proposals belong in [Tooling Backlog](../ideas/tooling-backlog.md). This page tries to step back and ask why these mismatches keep appearing.

## Runaway automation: when a tag triggers wrong machinery

### Case study: spurious adverb and expression conjugations

The 2026-05-11 wiki session identified twelve adverbial onomatopoeia entries (ぐつぐつ, ぱくぱく, …) with full godan **conjugation blocks** producing nonsense forms:

| Headword | Generated "present negative" | Generated "polite" |
|----------|-----------------------------|--------------------|
| ぐつぐつ | ぐつぐたない | ぐつぐちます |
| こつこつ | こつこたない | こつこちます |
| ぱくぱく | ぱくぱかない | ぱくぱきます |

A subsequent audit (2026-05-12) widened this finding considerably. **130 entries currently carry a conjugation field while their POS tag contains no `verb-*` or `adjective-i` value**, and every one of them has a stray `verb_class` tag. Distribution by primary POS:

| Primary POS | Entries | Sub-pattern |
|-------------|--------:|-------------|
| `adverb` | 91 | Mostly adverbs ending in く tagged `verb_class: godan-ku`; includes 12 onomatopoeia |
| `expression` | 31 | Idiomatic phrases (反応を見る, 場を和ませる, 頼りにする, …) |
| `noun` | 5 | Nouns also tagged adverbially (真っ二つ, 多く, …) |
| `auxiliary` | 2 | ～続ける, similar |
| `adjective-na` | 1 | べらぼう (also tagged adverb) |

The adverb cases are the cleanest demonstration of the failure: 著しく ("remarkably"), すごく ("very"), 多く ("many"), 遠く ("far"), 全く ("completely"), あいにく ("unfortunately"), ますます ("more and more"), おそらく ("probably"), 漸く ("finally") — all are adverbial / fixed forms with no verb structure of their own. Their generated conjugations include constructions like:

| Headword | Surface meaning | Generated "polite present" | Generated "past" |
|----------|-----------------|----------------------------|------------------|
| {著\|いちじる}しく | "remarkably" | {著\|いちじる}しきます | {著\|いちじる}しいた |
| すごく | "very" | すごきます | すごいた |
| {漸\|ようや}く | "finally" | {漸\|ようや}きます | {漸\|ようや}いた |

None of these are Japanese. The closest valid forms come from the parent i-adjectives (著しい→著しかった, すごい→すごかった) — i.e., the entries should not have **verb** conjugation tables at all.

The expression cases are more subtle. Some like {頼\|たよ}りにする and {場\|ば}を{和\|なご}ませる generate forms that happen to be correct because the final verb in the phrase is conjugated correctly (する → します, 和ませる → 和ませます). But others mis-classify the final verb's class: {反応\|はんのう}を{見\|み}る is tagged `godan` even though 見る is ichidan, producing nonsensical "godan-ized" forms like `反応を見らない` instead of `反応を見ない`.

The mechanism is the same as for onomatopoeia: `build/add_conjugations.py` reads `metadata.tags.verb_class` and treats it as authoritative. Once a stale `verb_class` tag is present — for whatever reason — the retrofit generates a conjugation block whose forms have no relationship to actual Japanese morphology.

The lesson is broader than these 130 entries. **Tags become inputs to deterministic pipelines, and pipelines don't sanity-check their inputs.** Once a tag is wrong, every downstream tool that reads the tag inherits the error and may write further wrong data — in this case, 17 generated forms per entry, ~2,200 generated forms in aggregate.

This is the same dynamic that [Deterministic vs. Semantic Tasks](deterministic-vs-semantic-tasks.md) describes from the other direction: deterministic scripts can do tremendous work when the upstream data is right, but they have no judgment to push back when it isn't.

### Cleanup vs. defense in depth

The narrow fix is a one-shot script that scans for entries where `pos` contains no `verb-*` value and yet a `conjugation` block exists, then removes the block. **130 entries currently match this rule** (the original 12-onomatopoeia case was a 9.2% subset of the real scope).

The broader fix is a guard inside `add_conjugations.py` itself: refuse to write a conjugation block unless the entry has at least one verb POS tag. The retrofit script becomes self-defending: if a future pass mis-tags more entries with a stray `verb_class`, they still won't get a conjugation table. This is filed in [Tooling Backlog](../ideas/tooling-backlog.md) → item 5.

**Resolved (2026-06-08).** Both fixes shipped: `build/prune_nonverb_conjugations.py` cleaned **133 entries** and an exact-enum verb-POS guard now defends `add_conjugations.py`. The decisive root cause turned out to sharpen this section's lesson rather than merely confirm it. The guard *did* exist — `if not any('verb' in p for p in ([pos] + pos_tags))` — but it used a **substring** test, and `'verb' in 'adverb'` is `True` because the literal string "adverb" contains "verb". So the failure wasn't only "a deterministic pipeline trusted a stale tag"; the guard meant to gate the pipeline **mis-parsed the POS itself**, silently classifying every adverb as verb-like. A stray `verb_class: "godan-*"` then did the rest. The lesson compounds: when a tag feeds a pipeline, sanity-check the *input*, but also make the gate test an **exact membership check against a known enum**, never a substring match — substring matches over a controlled vocabulary are a latent bug waiting for the first value that contains another as a prefix/substring (`adverb` ⊃ `verb`, and similarly `noun`/`pronoun`, etc.). `add_adjective_conjugations.py` was already written with the correct exact-membership form (`'adjective-i' not in pos_tags`) and had zero spurious tables — a useful contrast showing the right pattern was already in the codebase.

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

**Formality "formal" over-applied in early entries (new finding, 2026-06-09).** The cross-model accuracy-review pipeline (session 001, entries 00001–00200) independently surfaced a systematic formality-tag error in the earliest creation cohort: `formality: "formal"` applied to neutral/everyday words including 近頃 (recently), ドレス (dress), 吹雪 (blizzard), 普段 (usually), 行事 (event). Nine entries were corrected; the pattern likely extends through the 00100–00500 range. The failure mode: early batch creation defaulted to `"formal"` for any word that was not obviously slang or colloquial — treating "not informal" as equivalent to "formal." For the `formality` field (which has three values: `informal`, `neutral`, `formal`) this is a systematic third-bucket over-assignment. The correct label for general-register vocabulary is `"neutral"`. This is distinct from the politeness-tag mis-bucketing in the "Categorical compression" section above (which concerns the `politeness` field's inability to represent uchi/soto, bikago, and familiar suffixes). Both the `politeness` and `formality` fields suffer from over-assignment in the high-status direction, but for different reasons and in different cohorts. See [Cleanup Backlog](../ideas/cleanup-backlog.md) → Priority 17 for the actionable cleanup plan.

**Semantic over-application on polysemous entries.** A related stale-label pattern, also surfaced by the accuracy-review in the 00001–00200 range: entries covering multiple unrelated senses carry a domain tag that is correct for one sense but wrong for the others. Examples: ボール (00017) was tagged `semantic: ["leisure"]` (correct for the ball sense), but the entry also covers a bowl sense — leisure has nothing to do with bowls. グラス (00076) was tagged `semantic: ["food"]` for its drinking-glass sense, ignoring the eyewear sense. This is a structural limitation: the current schema applies semantic tags at the entry level, not the sense level. Well-handled polysemous entries use `semantic: ["general"]` when no single domain covers all senses. The fix is per-entry semantic review rather than a mechanical sweep.

### Undefined tag semantics: when the value itself isn't pinned down

A distinct cause of drift is not that a tag went stale, but that the tag's
*meaning was never written down*, so creation passes and reviewers reinvent it
inconsistently. Two cases surfaced in 2026-06-10 Routine runs.

**The `descriptive` catch-all.** Cross-model accuracy-review (session 002,
entries 00201–00450) found `semantic: ["descriptive"]` applied to 謙虚 (humble),
懸命 (earnest), 無限 (infinite), もしかすると (perhaps), and 自ら (oneself). The
reviewer was reading `descriptive` as "this word can describe something" — true
of nearly any adjective or adverb, and therefore empty as a classifier.
`descriptive` has quietly become a *second* catch-all alongside `general`. The
nuance is that `descriptive` is a perfectly good destination for some words: the
P11 cleanup routinely retags mimetic adverbs (じとじと, のそのそ) **to**
`descriptive`, which is correct — they describe manner/quality and belong to no
concrete domain. So the value isn't wrong; it's *under-defined*. A workable
criterion: **reserve `descriptive` for mimetics and manner/quality words that
genuinely lack a concrete domain; do not apply it to abstract nouns, grammatical
words, or words that already have a real domain tag.** Tracked for cleanup as
[Cleanup Backlog](../ideas/cleanup-backlog.md) → Priority 18.

**The `body-internal` vs `body-part`/`health` convention.** Routine v2's
new-entries run created four anatomy entries (頸動脈 carotid artery, 冠動脈
coronary artery, 胆嚢 gallbladder, 十二指腸 duodenum) and initially tagged them
`["body-part", "health"]`. The §4 self-check flagged the redundant `health` tag,
and the correct value turned out to be `["body-internal"]` — which is exactly
what the *existing* organ entries already use (心臓 03262, 胃 01706, 腎臓 13953).
The convention is real and consistently followed in the data, but it is **not
documented** in `entry-guidelines` or `other-entries`, so it gets reinvented at
creation time. (`health` stays correct for diseases and procedures — 膵臓癌, 聴診
— just not for the organs themselves.) This is a `[skill]` recommendation:
document, in the tag vocabulary reference, that internal organs use
`body-internal`, external/surface anatomy uses `body-part`, and `health` is for
conditions/procedures, not anatomy. Pinning the value down is cheaper than
re-catching the same redundancy every time anatomy vocabulary is added.

The general pattern is that tags are **write-rarely, read-often**. Once written, they participate in every downstream lookup. The dictionary lacks a systematic re-check pass: there is no tool that compares an entry's current notes/glosses/examples against its tags and flags inconsistencies.

## Connection to existing wiki analyses

This phenomenon sits at the intersection of several existing topics:

- [Deterministic vs. Semantic Tasks](deterministic-vs-semantic-tasks.md) frames the broader problem of which work can run on tags alone. Tag drift makes the deterministic side more brittle than it appears.
- [Entry Consistency](entry-consistency.md) treats consistency mostly at the notes/cross-references level. Tag consistency is a parallel and currently less-addressed dimension.
- [Keigo: Honorific Language](../research/keigo-honorifics.md) and [Register and Formality Marking](../research/register-formality-marking.md) document the multidimensional structure that the four-bucket politeness tag cannot represent.
- [Grammar Information in Learner Dictionaries](../research/grammar-in-dictionaries.md) covers the broader tradition of grammar codes in learner dictionaries (Hornby's L,D,T codes; LDOCE's grammar patterns) — all of which face the same compression problem.
- [Handling Homographs](homographs.md) and [Word Variants](word-variants.md) face a related issue: when one entry covers multiple kanji-variant senses (e.g., 取る's sense 2 actually written 撮る), the entry's tags can describe only one of the senses well.
- [Furigana Wrapper Anomalies](furigana-wrapper-anomalies.md) is the string-level analogue of this page's tag-level analysis: slightly off-spec furigana wrappers parse successfully and accumulate silently because no validator checks them.

## Detection sketches

These are not implementation plans, just notes on what a tag-drift detector might do.

**Mismatched POS / conjugation:** Trivial — any entry with `conjugation` whose `pos` list contains no `verb-*` (or `adjective-i`) tag is suspicious. **130 entries currently match.** All 130 carry a stray `verb_class` tag that triggered `add_conjugations.py`.

**Politeness tag vs. note prose:** Where the politeness tag is `humble` or `honorific`, the notes should contain the keyword "humble" or "honorific" (or equivalent explanation). Where they don't, either the tag is misapplied or the notes need expansion. Cheap to implement; flags both directions of error.

**Semantic tag vs. gloss / definition:** Compare the entry's semantic tags against keywords extracted from the gloss and example translations. Outliers (e.g., a `semantic: ["furniture"]` tag with no furniture-related words in any field) should be flagged. This needs a hand-curated keyword-per-tag list, but the tag vocabulary is small enough (~80 values) to make this tractable.

**Cross-entry tag consistency:** Across entries linked by `cross_references` of type `synonym` or `antonym`, the semantic tags should largely agree. Big divergences flag either a wrong cross-reference or a wrong tag.

## What review-flag precision tells us (first measured, 2026-06-10)

For most of this page's life, "tag drift is the highest-yield thing to re-check"
was a hypothesis from entry-level inspection. The Routine v2 decision ledger
(`reviews/decisions.jsonl`) now puts a number on it. Of 485 external-model flags
adjudicated on 2026-06-10, the **apply rate by review dimension** was:

| Dimension | Flags | Applied | Apply rate |
|-----------|------:|--------:|-----------:|
| **tags** | 88 | 6 | **6.8%** |
| translation | 166 | 4 | 2.4% |
| gloss | 222 | 4 | 1.8% |
| furigana | 9 | 0 | 0% |

The `tags` dimension's apply rate is **3–4× the gloss/translation rate**. Two
things follow. First, it confirms the thesis: among the content dimensions, the
tag layer is where a cross-model reviewer most often finds a *genuine* error —
because the batch tag-drift documented above (P11) is real and pervasive, and
because a tag is a discrete claim against the headword that adjudicates cleanly
("body-part on a verb meaning 'to discard'" is decidable), whereas gloss and
translation flags are mostly stylistic "could be fuller" nits on deliberately
concise basic/core glosses. Second, it tells the Routine *which* knob to turn:
the authoritative remediation for P11/P18 is the accuracy-review mode's `tags`
pass (`review_accuracy.py --dimensions tags`), which judges each tag against the
headword rather than the example topics — not the noisy keyword detector
(`check_tag_drift.py --check semantic-mismatch`, kept experimental/non-batch).

Even at 6.8%, tag flags are far from auto-applicable — they are a manual-review
queue, not an autofix. But a reviewer dimension worth ~3–4× the others is worth
weighting accordingly. The full breakdown, the precision-by-*source* split
(self-check on a run's own changes adjudicates at ~13% vs ~1.5% for the
whole-dictionary sweep), and the trend over time live in
[Quality Metrics Trend](quality-metrics.md).

### The tag-vocabulary contradiction and its resolution (2026-06-11 policy decision)

**CORRECTION (2026-06-11).** An earlier version of this section claimed that
the reviewer's "invalid tag" flags on `culture`, `religion`, `business`,
`nature`, etc. were *reviewer hallucinations*, because those tags "are all
valid values in `build/schema.json`." That analysis was wrong on the facts:
`schema.json` deliberately has **no enum for semantic tags** (free strings),
and the closed taxonomy that the project actually documents — in
`VALID_SEMANTIC` in `build/validate_tags.py`, in the `entry-guidelines` skill,
and **embedded in the reviewer's own prompt** by `review_accuracy.py` — did
not contain those tags. The reviewer was correctly enforcing the list it was
given. "The tag has hundreds of uses" was never the standard: a 2026-06-11
audit found **17,762 tag instances across 1,204 distinct out-of-taxonomy
tags**, i.e. the de-facto vocabulary had drifted far from the documented one,
and adjudication flip-flopped between runs depending on which source a session
consulted (one run bulk-rejected ~120 such flags as "false positives"; the
next run applied 57 migrations for the same flag type).

**The resolution (curator decision, 2026-06-11): expand, then enforce.** The
taxonomy was expanded with 30 established-by-usage categories (each had 100+
uses: `business`, `culture`, `abstract`, `nature`, `daily-life`, `society`,
`health`, `technology`, `science`, `politics`, `personality`, `sports`,
`evaluation`, `language`, `law`, `travel`, `religion`, `history`, `finance`,
`appearance`, `money`, `music`, `cooking`, `change`, `media`, `shopping`,
`entertainment`, `art`, `military`, `economics`), legitimizing ~49% of the
out-of-taxonomy instances at a stroke. Near-duplicates were deliberately NOT
blessed and carry 1:1 migrations (`time`→`time-general`, `people`→`person`,
`social`→`society`, `description`→`descriptive`, `medical`/`medicine`→`health`,
`transport`→`transportation`, `animals`→`animal-general`,
`economy`→`economics` — the map lives in `build/check_tag_drift.py`). The
remaining **~9,000 instances across ~7,300 entries** (measured at expansion
time) are tracked by the new `unknown-semantic` detector check and migrate
gradually via accuracy-review and systemic-fix
([Cleanup Backlog](../ideas/cleanup-backlog.md) → Priority 20). Note: the
`tag_drift` queue-depth metric in `pipeline/metrics-history.jsonl` jumps when
the new check lands — that is the new instrument, not a regression.

**The standing adjudication rule** (now also in `prompts/routine2.md` §A):
`VALID_SEMANTIC` is the **single source of truth**. A reviewer flag that a tag
is not in the list is *correct by definition* — apply it by migrating to the
best in-list tag. Never reject such a flag because the tag is widely used.

**Subjective "too narrow/too broad" substitutions remain noise.** The reviewer
also suggests replacing specific-but-defensible in-list tags (`education`,
`communication`, `work`, `art`) with broader ones (`cognition`, `general`,
`action`). These are editorial preference nits, not errors, and replacing a
specific tag with a fallback is usually a regression toward less information.
Reject them. Prompt v3 of `review_accuracy.py` (2026-06-11) instructs the
reviewer not to produce them (and to restrict formality flags to unambiguous
register contradictions), so this family should shrink in the precision data —
`reviews/decisions.jsonl` segments by `prompt_version` via the review files if
it doesn't.

**The `general`-tag reverse-direction noise (new, 2026-06-12/13).** A
symmetrically opposite noise family has emerged in the 03301–04300 range: the
reviewer flags entries tagged `general` as needing more specific replacements —
the *reverse* of the specific→broad substitution above. The 03301–03800 run
showed a 54.6% flag rate; the 03801–04300 run showed a 50% flag rate; in both
cases, ~88% of tag flags were of this form. `general` is a valid
`VALID_SEMANTIC` tag and an intentional editorial choice for words that don't
fit a narrower domain — flagging it as "too broad" is the same noise category as
the specific→broad substitution, just pointing in the other direction. The
standing adjudication rule (REJECT "too narrow/too broad" substitutions between
in-list tags) covers both directions. The challenge is volume: ~180 bulk
rejections per run dominate the adjudication workload and obscure the genuine
catches. The fix — adding an explicit instruction "Do not flag entries tagged
`general`, `descriptive`, `action`, or `expression` as needing a more specific
tag; these are valid fallback tags" — is tracked in
[Tooling Backlog](../ideas/tooling-backlog.md) → item 17.

**Enforcement gate: the off-vocabulary ratchet (2026-06-25).** "Expand, then
enforce" had no actual *enforce* step until now: `validate_tags.py` emitted
off-vocab semantic tags only as **warnings**, and CI
(`.github/workflows/validate.yml`) ran only `validate.py` (schema), so a new
entry could introduce yet another out-of-taxonomy tag and nothing would fail —
the off-vocab cohort passed CI silently. A 2026-06-25 recount measured the live
scope at **8,267 off-vocab instances across 6,759 entries / 1,109 distinct
tags**: the gradual-migration lane (accuracy-review + systemic-fix) was roughly
keeping pace but could be silently outrun by new drift. The gap is now closed
with a **baseline ratchet** — not a mass migration, which would contradict the
gradual-migration policy and turn CI red on ~56% of the dictionary:

- `build/data/unknown_semantic_baseline.json` records every off-vocab semantic
  tag each entry already carries (keyed by file path, so duplicate-ID entries
  are tracked independently). Regenerate with
  `python3 build/validate_tags.py --write-unknown-baseline`.
- `python3 build/validate_tags.py --check-no-new-unknown` (a new CI step) fails
  only when an entry carries an off-vocab tag **absent from the baseline** — a
  net-new one. The tolerated set can therefore only shrink (as migrations remove
  tags), never grow.
- Existing migration work is unaffected: removing an off-vocab tag keeps CI
  green, and the polish / accuracy-review lanes never *add* off-vocab tags. A
  brand-new entry with an off-vocab tag fails the gate — which is exactly the
  `routine2.md` §2 "no Unknown semantic tag warnings on new IDs" rule, finally
  enforced rather than merely requested.
- After a migration batch, regenerate the baseline so the gate stays tight.
- Scope: semantic tags only. There are currently **no** off-vocab `domain` tags
  (that field's controlled list is already clean and already error-gated inside
  `validate_tags.py`).

This is deterministic-defense-at-the-boundary (Implication 2, below) applied to
the semantic field: the controlled vocabulary is enforced at PR time for new
content, while the legacy tail stays on the gradual lane.

## The shape of the semantic-tag debt (measured 2026-08-06)

Two years of tag observations have produced two standing recommendations that
sound like engineering and turn out not to be: *extend the migration map until
the off-vocabulary queue is batch-fixable*, and *infer the missing specific tag
from the gloss*. Both were measured in the 2026-08-06 harvest, against the whole
corpus rather than against the range that prompted them, and both failed — for
the same underlying reason, which is worth stating once here rather than
re-deriving per item.

### The off-vocabulary queue is a long tail with a taxonomy gap at its head

The repo-wide count: **2,530 entries carry 3,208 off-list semantic-tag instances
across 687 distinct tag names.** The nine mappings shipped in
`check_tag_drift.py`'s `TAG_MIGRATION` cover 364 of those instances (11.3%);
438 of the names occur two times or fewer.

| lever | reach |
|---|---|
| the 9 shipped mappings | 364 instances (11.3%) |
| every mechanically-derivable mapping (depluralize, strip qualifier, add `-general`, normalize separators) | 78 names / 196 instances (6.1%) |
| the 55 highest-frequency unmapped names, hand-mapped | 1,304 instances (40.6%), leaving 623 names |
| top 100 names | 62.4% · top 249 names | 82.1% |

The distribution is the finding. A frequency-ranked map cannot finish this
queue, and the mechanical family — the one that needs no judgment — is 6% of the
mass, not the bulk of it. What sits at the head instead is a block of names for
concepts the controlled vocabulary has no slot for: `place` (54), `location`
(50), `object` (46), `state` (32), `quality` (32), `manner` (30), `degree` (30),
`document` (20), `position` (14), `objects` (14) — **322 instances in one
conceptual region.**

That region was independently identified from the opposite direction. The
2026-07-30 accuracy-review found roughly a quarter of the reviewer's tag
suggestions were "replace this off-vocabulary tag with `general`", on exactly
`location, place, position, object, space, status, document`, and concluded the
model was answering honestly: asked for an in-list destination for `position`,
the only truthful answer available is the catch-all. **A reviewer-behaviour
observation and a corpus count converging on the same ten strings is the
strongest evidence this wiki has that the gap is in the vocabulary, not in the
tagger or the model.** It is also the reason the migration lane keeps stalling:
its largest single block is blocked on a curator taxonomy decision, and no
amount of mapping work reaches it.

One prioritization datum falls out of the same scan. Of the 2,530 affected
entries, **1,121 carry off-list tags and nothing else** — zero valid semantic
tags, hence functionally untagged for search and browse — while 1,409 already
carry a valid tag alongside. Only the first half is a user-visible defect.

### Tags cannot be inferred from gloss text, because inference is not denotation

The other standing proposal is a gloss-keyword suggester for the 3,741 entries
whose only semantic tag is `general`. Built empirically — 899 gloss tokens that
concentrate ≥80% on a single tag across the 20,257 specifically-tagged entries —
it proposes a tag for **14.8%** of the queue at that threshold and **2.9%** at a
threshold worth trusting, and roughly one proposal in five is wrong.

The errors all have one shape: 眉 (eyebrow) → `nature` because its explanation
says "ridge"; 保険料 (insurance premium) → `transportation` because the gloss
illustrates car insurance; 負け惜しみ (sour grapes) → `food`. The tag is taken
from the *context the gloss mentions* rather than from what the headword
*denotes* — which is precisely the [P11](../ideas/cleanup-backlog.md) defect the
tag lane exists to clean up, and precisely why the project defines semantic tags
denotationally. **A tool that infers a tag from surrounding text cannot be
denotational.** It is not that this instrument is low-yield; it is pointed the
wrong way, and running it would manufacture the defect class it was meant to
reduce.

The population resists it for a structural reason, too: an entry ends up with
sole `general` *because* no domain was obvious to the tagger, so the set is
enriched for words with no domain signal at all (万端, 概説, 座標, 型, 連鎖,
特価). The transparent domain compounds that observing runs keep noticing —
視覚障害 → `health`, 選挙運動 → `politics` — are the visible slice, together
with the 350 katakana entries retaggable from their English source word. Between
them, ~10–15% of the queue.

### Why both failures are one failure

Neither result is about tooling quality. Both are cases of an **instrument being
asked to supply judgment that was never encoded in the data it reads.** The
migration map reads a tag name and can only rewrite it into another name — it
cannot invent a category the vocabulary lacks. The gloss suggester reads
English prose written to explain a word and can only correlate — it cannot
recover which of the concepts the prose mentions is the one the headword *is*.
Where the missing judgment is small and bounded (the 78 mechanical names, the
350 katakana loanwords), automation works and should be used. Where it is the
substance of the task, the honest queue entry is "N entries need a
lexicographer", and the useful engineering is the part that **sizes** that
number and **routes** the blocked share to whoever can unblock it — which for
322 of these instances is a curator answering one taxonomy question, not a
script.

## Implications for je-dict-1

1. **Treat tags as cached judgments, not ground truth.** When a polish pass updates an entry, the tags should be re-evaluated against the polished content, not assumed correct. The polish prompts currently don't ask for this.

2. **Defend deterministic scripts at their boundaries.** `add_conjugations.py` should require a verb POS tag, not just a verb_class hint. `validate_tags.py` should reject the combination of `onomatopoeia` POS plus a `verb_class` tag.

3. **Don't widen the schema until cheaper interventions are exhausted.** A structured politeness object would be more accurate but expensive to migrate and harder for entry-creation prompts to fill. The notes prose already carries the nuance for well-polished entries; the leverage is in making polish passes regenerate suspect tags.

4. **Build a tag-drift detector pass.** Even a simple heuristic check (mismatched POS/conjugation; politeness tag with no politeness keyword in notes; semantic tag with no semantic-keyword overlap) would surface most cases. Tag drift is a quietly accumulating debt: small per entry, large in aggregate.

5. **Document the schema's known limits explicitly.** The entry-guidelines and other skills should state plainly that the `politeness` tag is a four-bucket compression of a multidimensional system, and that the notes prose carries the nuance. This sets expectations for both prompts and curators.

## Related pages

- [Quality Metrics Trend](quality-metrics.md) — the measured per-dimension and per-source flag precision that quantifies this page's thesis
- [Deterministic vs. Semantic Tasks](deterministic-vs-semantic-tasks.md) — broader frame for where automation reliably works and where it doesn't
- [Entry Consistency](entry-consistency.md) — consistency in notes structure and cross-references
- [Keigo: Honorific Language](../research/keigo-honorifics.md) — the full structure that the politeness tag compresses
- [Register and Formality Marking](../research/register-formality-marking.md) — diasystematic labels and the consultation gap
- [Cleanup Backlog](../ideas/cleanup-backlog.md) — actionable cleanup items
- [Tooling Backlog](../ideas/tooling-backlog.md) — proposed scripts (including onomatopoeia conjugation pruner)
- [Entry Follow-ups](../ideas/entry-followups.md) — specific entries identified
