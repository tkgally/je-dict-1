# Register and Formality

**Last updated**: 2026-08-01

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
