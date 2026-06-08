# Verb Transitivity Pairs

**Last updated**: 2026-06-08

## Overview

Japanese has a rich system of paired transitive/intransitive verbs that English
largely lacks. Marking transitivity — the tag, a notes explanation, and a link
to the paired verb — is a **high-priority v2 quality standard** for verb entries.
This page covers why it matters, the morphological pattern families, how
je-dict-1 encodes it, current coverage (with real numbers), the auditing tools,
and the interaction with aspect.

## Why transitivity matters for learners

Many Japanese actions have two verbs — one transitive (他動詞, an agent acts on an
object) and one intransitive (自動詞, the action happens by itself):

- {開|あ}ける (to open something) ↔ {開|あ}く (to open by itself)
- {落|お}とす (to drop something) ↔ {落|お}ちる (to fall)
- {始|はじ}める (to start something) ↔ {始|はじ}まる (to begin)

English uses one verb for both ("I opened the door" / "The door opened"), so the
pairing is a genuine learning hurdle. The difficulty is not only lexical — it has
**grammatical consequences a learner cannot guess**:

- **Particle selection.** The transitive member takes を on its object
  (ドアを開ける); the intransitive takes が on its subject (ドアが開く). Choosing the
  wrong verb forces the wrong particle, so transitivity errors surface as
  particle errors. Learner-corpus research treats the two as linked (see
  [Error Analysis and Learner Corpora](../research/error-analysis-japanese-l2.md)).
- **Aspect.** The resultative ている reading lives mostly on the intransitive
  member (開いている = "is open"); the transitive member's ている is usually
  progressive (開けている = "is opening"). See *Interaction with aspect* below.
- **Voice and agency.** Intransitive verbs let a speaker describe a result
  without naming (or blaming) an agent — a pragmatically important option in
  Japanese (お皿が割れた "the plate broke" vs. お皿を割った "I broke the plate").

## Morphological pattern families

The okurigana endings cluster into recurring transitive/intransitive shapes:

| Transitive | Intransitive | Examples |
|-----------|-------------|----------|
| 〜す | 〜る | {出|だ}す / {出|で}る, {返|かえ}す / {返|かえ}る |
| 〜せる | 〜れる | {見|み}せる / {見|み}える, {聞|き}かせる / {聞|き}こえる |
| 〜める | 〜まる | {集|あつ}める / {集|あつ}まる, {決|き}める / {決|き}まる |
| 〜す | 〜れる | {壊|こわ}す / {壊|こわ}れる, {汚|よご}す / {汚|よご}れる |
| 〜ける | 〜く | {開|あ}ける / {開|あ}く, {付|つ}ける / {付|つ}く |

These families are a **hint, not a rule.** The mapping is only partly
predictable: 〜す reliably marks the transitive, but the intransitive partner may
end 〜る, 〜れる, or 〜える, and many verbs have no partner at all. This residual
unpredictability is exactly why a dictionary must *state* each verb's transitivity
and pair rather than expect learners to derive it — see
[Grammar Information in Learner Dictionaries](../research/grammar-in-dictionaries.md)
on valency and the limits of rule-based generation.

## How je-dict-1 encodes transitivity

Per the `verb-entry` skill (`.claude/skills/verb-entry/SKILL.md`), a complete
treatment has **three components**:

1. **Tag** — a transitivity value in `metadata.tags` (transitive / intransitive),
   so the property is queryable and renderable as a label.
2. **Notes** — a `TRANSITIVITY` section stating the type, the paired verb (with
   reading), and the particle pattern (Xが〜 / Xを〜).
3. **Pair link** — a link to the partner verb. The skill specifies
   `prominent_see_also` (not a generic `cross_references` entry) so the pair
   displays prominently, with the `note` field saying what the *target* is
   ("transitive" / "intransitive"). The build also recognises a dedicated `pair`
   cross-reference type (97 such links in the current report). **The back-link
   must exist on the partner** — a one-directional pair link is an incomplete
   pair.

### Not every verb has a pair

A crucial nuance the audit surfaces: many verbs are **unpaired**. {来|く}る,
する, {食|た}べる, {歩|ある}く have no transitive/intransitive partner. For these,
the correct treatment is a transitivity tag plus a note stating *there is no
pair* — **not** inventing a spurious partner. The audit tool flags unpaired verbs
as "missing pair link" because it cannot know whether a partner exists, so this is
a place where the report needs human judgment rather than mechanical clearing.

## Coverage status (2026-06-08)

`find_missing_transitivity.py` over the current 7,060 verb entries:

| Component | Verbs | Share |
|-----------|------:|------:|
| Transitivity **tag** | 3,141 | 44.5% |
| Transitivity in **notes** | 1,969 | 27.9% |
| **Pair link** | 1,330 | 18.8% |
| **Fully complete** (all three) | 777 | 11.0% |
| **No transitivity data at all** | 3,574 | 50.6% |

By tier, the work tracks priority cleanly:

| Tier | Verbs | Missing | Missing % |
|------|------:|--------:|----------:|
| basic | 116 | 0 | 0.0% |
| core | 585 | 117 | 20.0% |
| general | 6,359 | 3,457 | 54.4% |

**Basic-tier transitivity is complete**; core is mostly done; the general tier is
the open frontier (more than half still untouched). The gap between "has a tag"
(44.5%) and "fully complete" (11.0%) shows the bottleneck is the *pair link and
notes*, not the tag — tagging a verb's transitivity is easy; identifying and
bidirectionally linking its partner (and writing the contrastive note) is the
labour-intensive part.

Cluster-level health, from `check_semantic_clusters.py --summary`: of **247**
transitivity pairs already linked, **239 are complete** and 8 are missing a
back-link, with a further **35 pairs mentioned in notes but never linked** — the
single most tractable batch of work, since the partner is already named in prose.

## Tooling

- `find_missing_transitivity.py` — the coverage audit above (`--tier`, `--json`,
  `--missing-only`). The standard way to find and prioritise the work.
- `check_semantic_clusters.py` — lints transitivity pairs (plus antonym and keigo
  clusters) for **missing bidirectional links**; surfaces the "mentioned but
  unlinked" cases. `make check-clusters` for the summary.
- `polish_verb_transitivity.md` — the targeted polishing task that adds tags,
  notes, and pair links and ensures both members of each pair exist as entries.
  It can run in priority order (worst-first) when priority files are present.

## Interaction with aspect

Transitivity and the ている aspect system are tightly coupled, which is why the
two should be polished with an eye on each other:

- The **resultative** ている reading (state, not ongoing action) attaches mostly
  to the **intransitive** member: {開|あ}いている = "is open", {壊|こわ}れている =
  "is broken", {決|き}まっている = "is decided".
- The **transitive** member usually reads progressive: {開|あ}けている = "is
  opening (it)".
- てある is the **agent-marked resultative** on transitives: {開|あ}けてある =
  "has been opened (by someone, on purpose)" — a result state that, unlike the
  intransitive resultative, implies a deliberate agent.

So a learner who picks the wrong member of a pair gets not only the wrong particle
but the wrong aspectual meaning. See [Japanese Aspect and
ている](../research/japanese-aspect-teiru.md) for the full treatment; the
`verb-entry` skill (`.claude/skills/verb-entry/SKILL.md`) lists the
resultative-state verbs whose ている behaviour is non-obvious enough to warrant an
explicit ASPECT note.

## Example-sentence treatment

Both members should be illustrated. For the transitive verb, show a clear agent
acting on an を-marked object; for the intransitive, show a が-marked subject
changing state with no explicit agent. A well-built pair lets a learner read the
two entries side by side and see the particle and aspect contrast directly.

## Remaining work

1. Close the general-tier gap (3,457 verbs with no transitivity data) — the
   largest single quality-standard backlog among verbs.
2. Clear the 35 "mentioned-but-unlinked" pairs and 8 missing back-links
   (`check_semantic_clusters.py`) — the cheapest wins.
3. Distinguish *genuinely unpaired* verbs (tag + "no pair" note) from
   not-yet-linked ones, so the audit's "missing pair link" count reflects real
   gaps rather than verbs that have no partner to link.

## Related pages

- [Japanese Aspect and ている](../research/japanese-aspect-teiru.md) — ている resultative readings and てある, which ride on transitivity
- [Grammar Information in Learner Dictionaries](../research/grammar-in-dictionaries.md) — valency, transitivity, and grammatical encoding
- [Error Analysis and Learner Corpora](../research/error-analysis-japanese-l2.md) — transitivity confusion as a source of particle errors
- [Sense Relations and Semantic Networks](../research/sense-relations-semantic-networks.md) — transitivity pairs as a Japanese-specific sense relation
- [Cross-Reference Design](cross-references.md) — how pair links fit the broader cross-reference system and its symmetry targets
- [Quality Standards](../project/quality-standards.md) · [Entry Design](../project/entry-design.md)
