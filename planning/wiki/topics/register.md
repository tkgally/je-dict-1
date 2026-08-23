# Register and Formality

**Last updated**: 2026-08-23 (added a third way the register fields fail: `formality` is
entry-level, so an entry whose senses differ in register — 12766 念, formal 感謝の念 beside
everyday 念のため — has no right value to carry. Recorded as a curator question with the cost of
a per-sense override spelled out, and with the note that a count of split-register entries should
precede the ruling, since nobody has one)

Prior 2026-08-09 (added the measured `politeness`-tag drift class: the 両親 error
generalises to **16 noun entries**, about half of them genuine, and the distinguishing failure
is tagging a word that *denotes* deference — 尊敬, 謙遜 — as one that *encodes* it)

Prior 2026-08-01

## Why register matters

Japanese has one of the most elaborate register systems of any major language. The same concept can be expressed at multiple formality levels, and using the wrong register is a significant social error — more so than in English. For intermediate learners, understanding register is critical for natural communication.

Unlike English, where register is conveyed mostly through word choice and tone, Japanese encodes register directly into grammar: verb endings (plain vs. ます form), copula choice (だ vs. です), and entire lexical substitutions for keigo. A learner who knows only the dictionary form of words will sound abrupt or rude in most real-world situations; one who uses only です/ます will sound stiff among friends.

## The Japanese register system

Japanese register operates along two independent axes that the schema captures separately:

### Axis 1: Formality (social distance)

How formal or casual the expression is, independent of politeness direction:

| Level | Schema value | Context | Characteristics |
|-------|-------------|---------|-----------------|
| **Vulgar** | `vulgar` | Crude speech, insults, emphatic anger | Taboo vocabulary, rough sentence-final particles (ぞ, ぜ) |
| **Informal** | `informal` | Close friends, family, inner circle (ウチ) | Plain form, casual contractions (してる, 食べちゃう), masculine/feminine particles |
| **Neutral** | `neutral` | Default; appropriate in most situations | です/ます form, standard vocabulary |
| **Formal** | `formal` | Business, ceremonies, official documents | Formal vocabulary (いたす, 申す), complex sentence structures, written-style grammar |

### Axis 2: Politeness / Keigo (social hierarchy)

The honorific system expresses the speaker's position relative to others:

| Type | Schema value | Japanese | Function | Example |
|------|-------------|----------|----------|---------|
| **Honorific** | `honorific` | 尊敬語 (sonkeigo) | Elevates the subject's actions | いらっしゃる (to be/go), 召し上がる (to eat), ご覧になる (to look) |
| **Humble** | `humble` | 謙譲語 (kenjougo) | Lowers the speaker's actions relative to the listener | 参る (to go), いただく (to receive/eat), 拝見する (to look at) |
| **Polite** | `polite` | 丁寧語 (teineigo) | General politeness via verb endings | です/ます forms |
| **Plain** | `plain` | 普通体 (futsūtai) | Unmarked; no politeness marking | だ/dictionary form |

### Axis 3: Style and domain

The schema also captures medium and domain associations:

- **Style tags**: `written`, `spoken`, `literary`, `archaic`, `slang`
- **Domain tags**: `business`, `academic`, `technical`, `legal`, `medical`, `colloquial`, `internet`

These are orthogonal to formality. A word can be formal + spoken (business speech), or informal + written (casual texting).

## Register in je-dict-1's schema

The entry schema (`build/schema.json`) provides four structured fields for register:

```json
{
  "formality": "formal" | "neutral" | "informal" | "vulgar" | null,
  "politeness": "honorific" | "humble" | "polite" | "plain" | null,
  "style": ["written", "spoken", "literary", "archaic", "slang"],
  "domain": ["business", "academic", "technical", "legal", "medical", "colloquial", "internet"]
}
```

These fields live in `senses[].tags` within the entry JSON. They complement prose register notes in the `notes` field, which can capture nuances that structured fields cannot.

### Current coverage

As of April 2026:
- Approximately 107 entries contain the word "register" in their notes — typically prose descriptions like "This word is more formal than…" or "Used in casual speech."
- The structured `formality` and `politeness` fields exist in the schema but are used only in newer entries (roughly ID 21400+).
- Older entries rely entirely on prose notes for register information, with no structured tags.

## Gendered language

Japanese has traditionally associated certain speech patterns with gender, though these distinctions are weakening in modern usage:

### Feminine speech patterns
- First person: わたし, あたし (vs. masculine おれ, ぼく)
- Sentence-final particles: わ, の, かしら
- Frequent use of honorific prefixes お〜, ご〜
- Generally perceived as softer and more polite

### Masculine speech patterns
- First person: おれ, ぼく
- Sentence-final particles: ぞ, ぜ, だぜ, かな
- Plain copula だ in contexts where women might use の or わ
- Generally perceived as rougher and more direct

### Implications for the dictionary
- Gendered speech patterns are relevant to register notes, especially for first-person pronouns and sentence-final particles.
- The dictionary should note when a word or usage is strongly gendered (e.g., あたし is primarily feminine, おれ is primarily masculine) without being prescriptive about who "should" use them.
- Written Japanese and polite speech show almost no gender differences — the distinctions are concentrated in casual spoken Japanese.

## Keigo handling in entries

### Current approach

je-dict-1 handles keigo forms in two ways:

1. **Separate entries** for keigo forms that are distinct lexical items:
   - 召し上がる (meshiagaru, honorific "to eat") gets its own entry with a cross-reference to 食べる
   - いらっしゃる (irassharu, honorific "to be/go/come") gets its own entry
   - いただく (itadaku, humble "to receive/eat") gets its own entry

2. **Notes within the base entry** for productive keigo patterns:
   - The お〜になる pattern (honorific) is documented as a grammatical note, not as separate entries for every possible verb
   - The お〜する pattern (humble) is similarly handled

### Design considerations

The separate-entry approach works well for suppletive keigo (where the honorific/humble form is a completely different word) but would create entry bloat for productive patterns. The current hybrid approach is sound.

One gap: many base verb entries don't mention their keigo equivalents. Ideally, 食べる should note that its honorific form is 召し上がる and its humble form is いただく. The cross-reference system (`prominent_see_also` or `cross_references`) is the right mechanism for this.

## Register in example sentences

Example sentences should reflect the register of the headword:
- A casual word like やばい should have casual example sentences (plain form, informal particles)
- A formal word like における should appear in formal/written example sentences
- Neutral words should primarily use です/ます form in examples

This alignment helps learners internalize not just the meaning but the appropriate context for each word. Currently, register-appropriate examples are a v2 quality aspiration rather than a systematically enforced standard.

## Register challenges for learner dictionaries

### The "default register" problem
Most bilingual dictionaries present words without register context, implying a flat equivalence between translation pairs. But Japanese words that translate to the same English word can occupy very different register positions:

| English | Casual | Neutral | Formal |
|---------|--------|---------|--------|
| to eat | 食う (くう) | 食べる (たべる) | 召し上がる (めしあがる) |
| to say | 言う (いう) | 申す (もうす, humble) | おっしゃる (honorific) |
| to be | いる | おる (humble) | いらっしゃる (honorific) |
| a little | ちょっと | 少し (すこし) | 少々 (しょうしょう) |

Without register labels, a learner might use 食う in a business meeting or 召し上がる with friends — both errors.

### Context-dependent register
Some words shift register depending on context:
- 全然 (ぜんぜん) is neutral with negatives ("not at all") but informal with positives ("totally")
- ちょっと as a refusal softener operates at a different register level than ちょっと meaning "a little"

These nuances are best captured in prose notes rather than structured tags.

### Register acquisition order
SLA research suggests learners should acquire register awareness in stages:
1. First: the plain/polite distinction (だ/です, る/ます)
2. Then: awareness of casual and formal vocabulary
3. Finally: keigo (sonkeigo/kenjougo), which even native Japanese speakers find challenging

This maps loosely to vocabulary tiers: basic/core entries should have clear register marking; general-tier entries handle the full range.

## Gap: no field expresses "dated"

Added 2026-08-01, from a 2026-07-31 accuracy-review adjudication.

23060 {外套|がいとう} (overcoat) drew a flag asking to change `formality: formal` to "'archaic'
or 'old-fashioned' if such tags exist, or 'neutral'". The model is **right about the word** —
外套 is dated beside コート, and a learner needs to know that before using it — but both
destinations it offered are wrong, so the flag was rejected:

- `formal` is a point on the **register** axis (how the situation constrains word choice).
- Datedness is a point on a **currency** axis (whether contemporary speakers still use the word
  at all).
- `neutral` would erase the register signal without adding the currency one.

The two axes are independent: 外套 is both formal *and* dated; ちょっと is both casual and
entirely current; 拙者 is dated and was never neutral. Collapsing them into one enum forces
every dated word to lie about one of its properties.

Entries currently express datedness, when they express it at all, in prose — a notes line saying
the word "sounds old-fashioned". That is invisible to filtering, to the reviewer, and to any
consistency check, which is exactly why the reviewer proposed overwriting a correct `formality`
value: from its side of the schema there was nowhere else to put the observation.

**Options**, in increasing order of cost: (a) document the convention that datedness lives in a
REGISTER notes line and add a standing rejection for flags that propose `formality: archaic`;
(b) add a `currency` field (`current` / `dated` / `archaic`) alongside `formality`; (c) extend
the semantic tag vocabulary, which is the wrong home — this is a property of the word's use, not
its meaning.

Same shape as the taxonomy question behind
[Cleanup P13](../ideas/cleanup-backlog.md#priority-13-overuse-of-general-as-sole-semantic-tag):
a real distinction with no slot, resolving by default into a field that means something else.
**Curator decision** — a Routine run cannot add a schema field.

## The `politeness` tag conflates *encoding* deference with *denoting* it (measured 2026-08-09)

A 2026-08-09 polish run fixed entry 00806 {両親|りょうしん}, which carried
`formality: formal` + `politeness: honorific`. The word 両親 is the ordinary, neutral term for
"parents"; the honorific form is ご両親. The tag had migrated from the *honorific derivative* to
the *plain base word*. The run suspected a family of similar drift on kinship terms and filed
it for measurement.

The obvious detector — `politeness` is `honorific` or `humble` while the headword carries no
お/ご prefix — returns **82 entries and is mostly right to**. 申す, いらっしゃる, いたす, 参る,
召し上がる, くださる, なさる and the rest of the suppletive keigo verbs are exactly the words
this page's Axis 2 exists to label, and none of them takes a prefix. Prefix-absence is not
evidence of anything.

What isolates the error is **part of speech plus the gloss**: nouns tagged honorific/humble
whose own gloss does not describe deferential use. That narrows 82 to **16**, and the 16 split
cleanly in two:

| | Entries | Why |
|---|---|---|
| **Genuine** | 陛下, 閣下, 寸志, 高配, 引き立て, 夫人, 奥さん, 王様, 主人 | The word itself is deferential in use — you cannot say 陛下 neutrally |
| **Drift** | **利用者** "user, customer", **尊敬** "respect, esteem", **謙遜** "modesty", **配偶者** "spouse", 無沙汰, 茶漬け, 拝観料, 不徳 | The word *names* deference, or merely appears in deferential contexts |

尊敬 is the clearest case: a noun meaning "respect" is not itself respectful language, any more
than the English noun *politeness* is polite. 謙遜 "modesty" is its humble-side twin. 利用者
"user" appears to have been tagged from the surrounding register of the texts it occurs in
(service announcements), and 配偶者 from the formality of legal and administrative prose — both
are **context contamination**, tagging the word with the register of its typical habitat rather
than with a property of the word.

**The general shape**: `politeness` is a property of *how a word positions speaker and
referent*, not of *what the word is about* and not of *where the word tends to appear*. All
three of those get confused, and the schema gives no way to distinguish them because there is
only one field. This is the register-axis instance of the meaning-versus-use confusion that
[Schema Tag Reliability](schema-tag-reliability.md) documents for semantic tags — 財布 tagged
`clothing` because wallets live in pockets is the same error in a different field.

Two consequences worth carrying:

1. **The population is small and needs judgment, not a sweep.** 16 entries, roughly half
   correct. No mechanical rule separates them, because the distinction is semantic. Filed at
   [Cleanup Backlog → Updates 2026-08-09](../ideas/cleanup-backlog.md#updates-2026-08-09-wiki-harvest)
   as open and explicitly *not* batch-ready.
2. **It reinforces §A's formality guard from the opposite direction.** The Routine's rule for
   external reviewers is to change a formality label only when the entry's own notes contradict
   it — a guard measured at 5-of-5 correct rejections across three windows. The 両親 class shows
   the same evidence source works for *finding* errors, not just rejecting them: in every one of
   the eight drift cases the gloss already says the word is neutral. A tag that contradicts its
   own entry's gloss is checkable without a model.

## Gap: `formality` is entry-level, but register can differ by sense (2026-08-22)

A third way the same field fails to say what it needs to. The two above are about *which*
distinction the label draws; this one is about *how many* labels the entry gets: exactly one,
regardless of how many senses it has.

**The case**: **12766 {念|ねん}** is tagged `formality: "formal"`, and its own notes say so only
for half of it. Sense 1 — deep feeling, as in 感謝の念 (gratitude), 畏敬の念 (awe) — is unambiguously
formal, literary, and largely confined to written and set-phrase use. Sense 2 is the everyday
念のため ("just in case"), which any speaker uses in ordinary conversation. `formal` is wrong for
sense 2; `neutral` would be wrong for sense 1. There is no third value that is right, because
the problem is not the value.

The 2026-08-22 accuracy reviewer flagged the tag as wrong, which is correct in the only sense
available to it — but the flag is unactionable, and a reviewer that keeps flagging entries where
no available value is right is generating noise that looks like signal. That is the practical
cost of the gap: it does not just mislabel entries, it contaminates the flag-precision statistics
on [Quality Metrics](quality-metrics.md).

**The question for the curator**: should `formality` — and by extension `politeness` and `style`
— be permitted at the definition level, overriding the entry-level value for the handful of
entries with split register?

Arguments and costs, so the decision is not made on the strength of one example:

- **For**: the entry-level field is a *lexeme* claim, and register is a property of a sense, not
  of a spelling. Split-register entries are exactly the ones where a learner most needs the
  label, because the two senses look identical on the page.
- **Against**: every consumer of `metadata.tags.formality` — the renderer, `check_tag_drift.py`,
  `validate_tags.py`, the accuracy-reviewer prompt, and the register-markedness detectors behind
  [Cleanup P37](../ideas/cleanup-backlog.md#priority-37) and
  [`tag-register-marked-basic-core`](../ideas/cleanup-backlog.md) — would need a fallback rule.
  A per-sense override that most consumers ignore is worse than no override, because entries
  would then carry a correct label that nothing reads.
- **Unmeasured**: how many entries actually split. 念 is one. The population is probably small —
  polysemy that crosses a register boundary is not the common case — but nobody has counted, and
  the answer decides whether this is a schema change or four hand-written notes. **A count should
  precede the ruling**: the cheap proxy is entries whose notes name a register distinction
  between numbered senses.

**Interim handling**: where the two senses differ, the entry-level tag should take the value that
fits the *more common* sense and the notes should state the split explicitly, as 12766's already
do. That is not a fix — it just means the entry is right where a learner will read it, and wrong
only where a detector will.

## Implementation roadmap

Register marking is a **medium priority** v2 quality standard. The path forward:

1. **Immediate**: Continue adding register notes in prose for new entries and during polishing
2. **Short-term**: Systematically populate `formality` and `politeness` structured fields in new entries
3. **Medium-term**: Create a polishing task to backfill structured register fields in older entries
4. **Long-term**: Consider adding register-based search/filtering to the site UI
5. **Ongoing**: Add keigo cross-references (base ↔ honorific ↔ humble) during cross-reference polishing sessions

## Related pages

- [Quality Standards](../project/quality-standards.md) — v2 enhancement priorities
- [Translation Equivalence](../research/translation-equivalence.md) — the bilingual mapping problem
- [Entry Design](../project/entry-design.md) — schema structure and required fields
- [Learner Lexicography](../research/learner-lexicography.md) — pedagogical dictionary design principles
- [Open Issues](../project/open-issues.md) — loanword handling and other design questions
- [Error Analysis and Learner Corpora](../research/error-analysis-japanese-l2.md) — register-mixing and keigo errors in learner production
- [Gairaigo: Loanwords in Japanese](../research/gairaigo-loanwords.md) — register connotations of gairaigo vs. wago/kango synonyms
- [Pragmatics and Speech Acts](../research/pragmatics-speech-acts.md) — speech act theory, indirectness, and pragmatic competence in bilingual dictionaries
- [Register and Formality Marking](../research/register-formality-marking.md) — diasystematic labels, the consultation gap, and encoding strategies for register information
- [Keigo: Honorific Language](../research/keigo-honorifics.md) — keigo system structure, L2 acquisition, uchi/soto dynamics, and dictionary treatment
