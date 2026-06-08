# Quality Standards

**Last updated**: 2026-06-08

This page describes je-dict-1's quality standards, the tooling that now *measures*
each one, and where the project actually stands against them. The standards
themselves were set by an early multi-model evaluation; what has changed since is
that most of them are now backed by a concrete metric or audit script (built
during the 2026 Enhancement Plan — see
[Enhancement Plan Retrospective](../topics/enhancement-plan-retrospective.md)), so
"quality" is increasingly something the project can quantify rather than only
assert.

## v2 Quality Standards

Based on multi-model LLM evaluation (Claude Haiku 4.5, GPT-5.2, Gemini 3 Flash),
the project identified specific areas for improvement, prioritized into three
tiers. Each is now paired with the tool that tracks it.

### High priority

1. **Verb transitivity** — every verb should mark 自動詞/他動詞 and link its paired
   verb when one exists. *Measured by* `find_missing_transitivity.py` and the
   cluster lint `check_semantic_clusters.py`. See [Verb Transitivity
   Pairs](../topics/verb-transitivity.md).
2. **Aspect notes** — verbs with non-obvious ている meanings need explicit
   documentation (結婚する + ている = "is married", resultative state, not "is
   getting married"). Polished by the `polish_aspect_notes` task against the
   reference list in the `verb-entry` skill.
3. **Particle predicate lists** — particle entries should list the verbs and
   adjectives that require them (に → 行く, 住む, あげる …). See the
   `particle-entry` skill and [Japanese Particles in
   L2](../research/japanese-particles-l2.md).
4. **Collocation patterns** — common noun-verb pairings (電話をかける, 写真を撮る)
   documented in notes. See [Collocations in Learner
   Dictionaries](../research/collocations.md).

### Medium priority

1. **Register labels** — mark casual/neutral/formal/honorific where relevant.
   (Caveat: the politeness tag is being applied too loosely in places — see
   [Cleanup Backlog → Priority 7](../ideas/cleanup-backlog.md) and [Schema Tag
   Reliability](../topics/schema-tag-reliability.md).)
2. **Similar words** — contrastive sections distinguishing near-synonyms (見る
   vs. 観る vs. 眺める). See [Near-Synonym
   Discrimination](../research/near-synonym-discrimination.md).
3. **Adjective forms** — document adverbial (〜く/〜に) and noun (〜さ) forms.
4. **Example progression** — examples within each sense go simple → complex. See
   [Example Sentence Design](../research/example-sentences.md).

### Low priority

1. **Kanji orthography notes** — when to use kanji vs. hiragana (する usually kana).
2. **Cultural notes** — expand where culturally significant (お中元, 七五三). See
   [Cultural Content in Bilingual
   Dictionaries](../research/cultural-content-dictionaries.md).
3. **Keigo references** — link to honorific forms (食べる → 召し上がる). See
   [Keigo: Honorific Language](../research/keigo-honorifics.md).

## Where the project stands (2026-06-08)

The standards are no longer purely aspirational; the dashboards put numbers on
them. Current state across 28,743 entries:

- **Furigana completeness** is effectively *enforced*, not just targeted —
  `find_missing_furigana.py` is a deterministic gate run after every creation
  batch, so bare kanji rarely survive to the live site. **Furigana correctness**
  (is the reading right *in context*?) is a separate, semantic problem handled by
  the multi-model review pipeline at a calibrated 0.12% noise rate. See [Furigana
  Strategy](../topics/furigana-strategy.md) for the completeness-vs-correctness
  split.
- **Verb transitivity**: of ~7,060 verbs, only **11.0% are fully complete** (tag
  + notes + pair link) and **50.6% have no transitivity data at all**. Basic tier
  is **100% done**, core ~80%, but the general tier (54.4% missing) is the open
  frontier. The bottleneck is the pair link and contrastive note, not the tag.
- **Note quality** (`score_note_quality.py`): average **81.5/100**, with **71.6%**
  of entries scoring 80+ and only 0.3% below 40. The distribution is healthy, but
  the POS breakdown is revealing — see below.

### Verbs are the quality frontier

The metrics agree on where the remaining work concentrates. Note-quality by POS
runs from **noun 88.0** down to **verb-suru 61.3** (the single lowest-scoring
category, across 3,681 entries), with the other verb classes (godan 70.1, ichidan
72.2) also below the dictionary average. Verbs are simultaneously the weakest on
**note quality**, on **transitivity coverage** (50.6% missing), and the POS that
carries the **aspect/ている** burden. A learner-dictionary's verbs are also its
highest-traffic encoding targets (production hinges on getting particles and
transitivity right). The convergence is an argument for a verb-focused polishing
push: a `verb-suru` note-and-transitivity pass would move three high-priority
standards at once. (Suru-verbs are a natural cluster because their notes are often
thin — gloss + one example — where the transitive/intransitive and aspect
dimensions could carry real content.)

## Entry-level quality checklist

For any new or revised entry:

- [ ] All kanji have furigana in headword, examples, and notes
- [ ] 3+ examples per sense, progressively longer
- [ ] Notes have section headers, bullet points, paragraph breaks
- [ ] Notes include collocations and at least one additional section
- [ ] All prose is in English; Japanese only in examples/collocations
- [ ] POS tags use correct hyphenated format
- [ ] Verbs have conjugation tables; i-adjectives have conjugation tables
- [ ] Conjugation tables exist **only** on verbs and i-adjectives — never on
      adverbs, onomatopoeia, or other POS (a 2026-06-08 cleanup stripped 133
      spuriously-conjugated non-verb entries; the `add_conjugations.py` guard now
      prevents recurrence)
- [ ] Cross-references link to related entries where appropriate
- [ ] Vocabulary tier is "general" for new entries

## How quality is measured and maintained

The Enhancement Plan turned several standards into running checks. Rather than
re-list the commands (they live in CLAUDE.md), here is what each tool *measures*:

| Tool | Standard it tracks |
|------|--------------------|
| `report.py` | The dashboard: tier/POS counts, examples, cross-reference coverage **and symmetry**, furigana completeness |
| `score_note_quality.py` | Note depth and structure (the 81.5 average above) |
| `check_consistency.py` | Note structure, transitivity presence, and other per-entry consistency issues across similar entries |
| `find_missing_transitivity.py` | The transitivity standard, by tier |
| `check_semantic_clusters.py` | Bidirectional links in transitivity / antonym / keigo clusters |
| `review_runner.py` + `reviews/` | Furigana *correctness* via cross-model verification |

The **comprehensive-polish** task (the default scheduled job) walks entries one at
a time applying a tiered checklist that unifies all the targeted polish tasks
(transitivity, aspect, furigana, inline links, semantic labels, note expansion).
Each polish task tracks progress so it resumes across sessions, and can run in
**priority order** (worst-first) when `polishing/priority/` files are present.
Systemic issues that polish sessions notice are logged to
`polishing/observations.md` and harvested into this knowledge base — that loop is
how the [Cleanup Backlog](../ideas/cleanup-backlog.md) and [Entry
Follow-ups](../ideas/entry-followups.md) pages stay current. See [Content
Pipeline](content-pipeline.md) for the full workflow.

## Related pages

- [Entry Design](entry-design.md) — the schema and required fields the checklist enforces
- [Content Pipeline](content-pipeline.md) — how entries are created and polished against these standards
- [Verb Transitivity Pairs](../topics/verb-transitivity.md) · [Furigana Strategy](../topics/furigana-strategy.md) — the two high-priority standards in depth, with coverage numbers
- [Entry Consistency](../topics/entry-consistency.md) — uniformity across similar entries, and the consistency checker
- [Enhancement Plan Retrospective](../topics/enhancement-plan-retrospective.md) — what the QA tooling layer above was built to do
- [Example Sentence Design](../research/example-sentences.md) · [Collocations in Learner Dictionaries](../research/collocations.md) — research informing the example and collocation standards
