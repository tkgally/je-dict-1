# Handling Homographs

**Last updated**: 2026-08-01

## The problem

Japanese has an exceptionally high density of homophones and homographs due to its small phoneme inventory and the multiple-reading nature of kanji. This creates challenges at every level — for learners trying to look up words, for dictionary designers deciding how to organize entries, and for search systems trying to surface the right results.

The problem manifests in several distinct forms:

| Type | Description | Example |
|------|-------------|---------|
| **Homographic heterophones** | Same kanji, different readings and meanings | 角: つの (horn), かど (corner), すみ (nook) |
| **Homophones with different kanji** | Same reading, different kanji and meanings | かける: 掛ける, 欠ける, 架ける, 駆ける |
| **True homonyms** | Same reading and writing, unrelated meanings | バス: bus vs. bass |
| **Polysemy** | One word with multiple related senses | 甘い: sweet (taste), lenient, naive |
| **Reading variants** | Same kanji and meaning, different accepted readings | 頬: ほほ / ほお (cheek) |

## Scale in je-dict-1

As of April 2026, the dictionary contains:

- **117 headwords** with multiple entries (same kanji, different readings/meanings) — e.g., 角 has 3 entries, 綿 has 2 (わた "cotton" vs. めん "cotton fabric")
- **1,372 readings** shared by multiple entries (homophones) — the most extreme cases have 6-7 entries per reading
- The reading けん maps to 7 distinct entries (県, 券, 件, 剣, 圏, plus counters)
- Readings like かく, きかん, しんこう, さす, せん, and かえる each have 6 entries

The homophone problem is particularly acute for on'yomi (Chinese-derived) readings. Readings like こうてい (5 entries: 高低, 皇帝, 工程, 行程, 肯定) illustrate why kanji are essential for disambiguation in written Japanese — and why a dictionary must make these distinctions navigable.

## Current approach

### Separate entries for different readings

Words with the same kanji but different readings get separate entries, each with its own ID. They are linked via cross-references.

Example: 角 has entries for つの (horn, ID 02158), かど (corner/angle, ID 02195), and すみ (corner/nook, ID 02156). Each is a distinct entry with its own examples, notes, and cross-references to the others.

This is the right design for a learner dictionary — combining these into one massive entry would be confusing, since the readings represent genuinely different words that happen to share a kanji.

### Multi-sense for same reading

When a word has one reading but multiple distinct meanings, these are handled as separate senses within a single entry. The threshold for "separate entry" vs. "separate sense" is:

- **Same entry**: Meanings are etymologically related or the connection is clear to learners. Example: 甘い (sweet → lenient → naive) — the metaphorical extension is traceable.
- **Separate entries**: Meanings are unrelated enough that combining them would confuse learners. Example: かえる as 帰る (to return home) vs. 蛙 (frog) — completely unrelated words that happen to be homophones.

### Reading variants

Some words have two accepted readings for the same kanji and meaning — 頬 can be read as ほほ or ほお, both meaning "cheek." The dictionary currently has separate entries for these (IDs 00110 and 03717). Similarly, 日本 has entries for both にっぽん (ID 00320) and にほん (ID 03876). These are cross-referenced so learners can find whichever form they encounter.

An alternative approach would be to list both readings in a single entry, but separate entries are clearer when the readings have different usage contexts (にっぽん is more formal/emphatic than にほん).

### Search and disambiguation

The search index includes all readings and glosses, so searching for a kanji surfaces all entries that use it. The kanji index (`kanji/`) maps individual kanji characters to all entries containing them, providing an alternative access path.

## Detailed analysis of problem types

### Homographic heterophones

These are the most distinctive Japanese challenge — multiple completely different words written with the same kanji. The classic examples:

| Kanji | Readings | Notes |
|-------|----------|-------|
| 角 | つの, かど, すみ | Three unrelated meanings from one character |
| 綿 | わた, めん | Same material, different registers (native vs. Sino-Japanese) |
| 数 | かず, すう | Native vs. Sino-Japanese counting words |
| 対 | つい, たい | "Pair" (native) vs. "versus/against" (Sino-Japanese) |
| 年月 | ねんげつ, としつき | Sino-Japanese compound vs. native reading, subtly different nuance |
| 盛り | さかり, もり | "Peak/prime" vs. "serving of food" — unrelated senses |
| 追従 | ついじゅう, ついしょう | "Following blindly" vs. "flattery" — reading changes meaning |

For learners, these are particularly treacherous because encountering the kanji in text gives no reliable clue about which reading applies — context and experience are the only guides.

### Dense homophone clusters

On'yomi compounds create enormous homophone clusters. The reading きかん maps to 6 entries: 期間 (period), 既刊 (already published), 気管 (windpipe), 機関 (organization), 季刊 (quarterly), 器官 (organ). A learner hearing きかん in conversation must rely entirely on context for disambiguation.

This is less of a problem for a dictionary than for a learner in the wild — in the dictionary, each entry has its own kanji headword, and search results show both kanji and reading. But it underscores why the dictionary should:
1. Include kanji prominently in search results
2. Show brief glosses alongside headwords in result lists
3. Cross-reference related homophones where confusion is likely

### Kun-yomi near-synonyms

Native Japanese readings create a different disambiguation challenge: multiple kanji with overlapping meanings. The verb かえる has 5 distinct entries:

- 帰る — to return (home)
- 変える — to change, alter
- 換える — to exchange, convert
- 替える — to replace, substitute
- 代える — to substitute (with a replacement)

The last three (換, 替, 代) are near-synonymous, differing in nuance. This is where contrastive notes and similar-word sections become essential. A learner who looks up かえる and finds five results needs guidance on which word fits their context.

The CJK Dictionary Institute notes that authors sometimes avoid the kanji distinction entirely, writing such words in hiragana (かえる), which makes the dictionary's job harder — the search must handle both kanji and kana forms.

### Verbs with different conjugation classes

Homophones that belong to different verb classes are especially confusing because they conjugate differently:

- きる: 切る (godan, "to cut") vs. 着る (ichidan, "to wear")
- とる: 取る, 撮る, 採る, 捕る (all godan, but different meanings)

These must be separate entries. The conjugation tables in each entry serve as disambiguation aids — a learner who encounters きて and isn't sure whether it's "cutting" or "wearing" can check the conjugation patterns.

### Katakana homographs

Rare but present: バス (bus) vs. バス (bass in music). These are handled as separate entries with disambiguation in the definition. Since katakana words lack kanji as a visual distinguisher, the gloss and context examples carry the full disambiguation burden.

## Search result disambiguation

The current search system surfaces all entries matching a query. For a search like かける, the results list shows multiple entries with the same reading. The key design question is how to help users quickly identify the entry they want.

### Current state

Search results display the headword (with furigana) and the gloss. For homophone-heavy readings, this provides enough information for disambiguation in most cases — the user sees 掛ける (to hang) vs. 欠ける (to chip) vs. 駆ける (to run) and can select the right one.

### Improvement opportunities

1. **Grouping related homographs**: When a search returns multiple entries with the same kanji but different readings (e.g., searching 角), results could be visually grouped to show the relationship
2. **Disambiguation labels**: For dense homophone clusters, adding brief contextual tags (e.g., "medical," "temporal," "organizational" for the various きかん entries) could speed selection
3. **Frequency-based ordering**: Ordering search results by word frequency would put the most likely match first, benefiting the common "first-fit" lookup strategy documented in [Dictionary Lookup Behavior](../research/dictionary-lookup-behavior.md) research
4. **Kanji component search**: For learners who recognize a kanji but don't know its reading, searching by radical or component would provide an alternative access path. The kanji index already maps characters to entries; exposing this in the search UI would help

## Design principles

### When to split vs. merge

The decision of "one entry or two?" for words that share some features follows these principles:

| Split into separate entries when... | Keep as one entry with multiple senses when... |
|--------------------------------------|------------------------------------------------|
| Different readings (つの vs. かど) | Same reading, related meanings |
| Different POS (noun vs. verb) | Same POS, extended/metaphorical meanings |
| Unrelated etymologies | Shared etymology with semantic drift |
| Different conjugation classes | Same conjugation pattern |
| Combining would create an unwieldy entry | Combined entry remains navigable |

### Cross-referencing

All entries that share a written form or reading should be cross-referenced. The `prominent_see_also` field is appropriate for close relationships (e.g., 帰る ↔ 返る), while `cross_references` handles looser connections. The goal is that a learner who arrives at any entry in a homograph cluster can easily find the alternatives.

### Contrastive notes

For near-synonym homophones (the かえる cluster, the つく cluster, etc.), contrastive notes explaining the differences are high-value content. These notes should appear in each entry of the cluster, not just one, since the learner may arrive at any entry first.

## Neighbour substitution: how homographs break the project's *tools*

Added 2026-08-01. Everything above concerns how homographs are presented to the learner. A
separate problem emerged during July 2026: homographs and homophones are the single most
reliable way to make je-dict-1's automated instruments produce confident, well-formed, wrong
output. Three different instruments hit it in the same week, and the failure has the same shape
in all three — **the tool silently substitutes a neighbour that shares the surface or the sound,
then reasons correctly about the wrong word.**

### 1. The paid reviewer substitutes a homophone

| Entry | Reviewer insisted the gloss should be | The reviewer was describing |
|---|---|---|
| 23075 {講読\|こうどく} — reading and study of texts | "subscription (to a publication)" (×2 `error` flags) | 購読, a different word with the same reading |

Both flags were rejected. This is not the familiar noise family — the model is not misreading
the gloss or nitpicking style. It has replaced the headword.

### 2. The paid reviewer substitutes a *homograph* — the same characters, another reading

| Entry | Reviewer insisted | The reviewer was describing |
|---|---|---|
| 23166 {激高\|げきたか} — slang "sky-high expensive", from the productive 激〜 intensifier | "rage; fury" (×4 `error` flags) | 激高 read げきこう |
| 23182 {悪感\|あくかん} — "ill will" | "chill; nausea" (×5 `error` flags) | the おかん reading |

Both entries are internally consistent and correct. The pattern is sharp enough to predict:
**an entry documenting the minority reading of a homograph will reliably draw a full sweep of
error-severity flags across every dimension.** The model reads the kanji, retrieves the dominant
reading, and evaluates the entry against that word.

Two useful corollaries. First, a prompt fix is available and narrow: tell the reviewer that the
headword's *kanji plus its stated reading* are jointly authoritative, and that a proposed gloss
belonging to a different reading of the same characters is out of scope. Second — and this was
the more valuable outcome — **a rejected flag can still be a coverage signal**: checking the
neighbours the model had in mind showed 激高/げきこう was genuinely missing (added as candidate
C22661) while 悪寒/おかん already existed at 12670. Worth harvesting rather than discarding.

### 3. Inline-link resolution substitutes a homophone — 87 confirmed defects

The 2026-07-31 `systemic-fix` run over `link-target-baseform-disagreement` found the same
phenomenon written into the corpus itself: inline links whose base form is a real word with its
own entry, pointing at a **homophone's** entry.

機能→昨日, 状況→上京, 電気→伝記, 性格→正確, 福祉→副詞, 会社→外車 — **87 occurrences across
64 entries**, every one a Sino-Japanese compound, all repaired 1:1 with no ambiguity.

The same trap sets the boundary of the stale-`noentry` sweep
([Cleanup P35](../ideas/cleanup-backlog.md)): links whose base form matches only a single
character (角 → つの when the text means かど) or only a reading (ば → 場 when the text means the
conditional particle) cannot be resolved mechanically at all. 883 of 3,797 stale markers fall in
that class, against 2,887 that are safe.

### Why this class is invisible

The 87 broken links all rendered, resolved, and worked. The §4 self-check over those same 64
entries returned **zero** findings on the dimension that was actually broken — and offered 25
unrelated tag opinions instead. No furigana instrument, no tag check, and no accuracy review can
see a link that points at a coherent entry for the wrong word.

This is the corpus-side case of the argument on
[Instrument Defects](instrument-defects.md): homograph substitution produces output that is
*well-formed by every rule the project checks*. Only deterministic base-form resolution
(`check_link_baseform.py`) can see it, which is the argument for wiring that check into the CI
ratchet once its population is worked down.

### Implication for entry design

The dictionary's own homograph handling — separate entries per reading, cross-linked — is what
makes the mechanical repairs possible: 激高/げきこう and 悪寒/おかん are answerable questions
because reading is part of entry identity. The cost is that **entries for minority readings are
permanently expensive to review**, since every automated pass will argue with them. Flagging
such entries explicitly (a note line naming the dominant-reading neighbour, which several
already carry) is cheap and gives the next adjudicator the context to reject a sweep of flags
in one pass rather than five.

## Related pages

- [Inline Link Integrity](inline-link-integrity.md) — the link-resolution half of the substitution problem
- [Instrument Defects](instrument-defects.md) — why well-formed wrong output is the hard case
- [Entry Design](../project/entry-design.md) — entry schema and required fields
- [Cross-Reference Design](cross-references.md) — linking related entries
- [Japanese Lexicography](../research/japanese-lexicography.md) — challenges specific to Japanese dictionaries
- [Word Variants](word-variants.md) — handling words with multiple written forms
- [Dictionary Lookup Behavior](../research/dictionary-lookup-behavior.md) — how learners navigate homograph challenges
- [Digital Dictionary UX](../research/digital-dictionary-ux.md) — search and disambiguation interface design
- [Definition and Gloss Strategies](../research/definition-strategies.md) — sense ordering for polysemous entries
- [Polysemy and Sense Discrimination](../research/polysemy-sense-discrimination.md) — the polysemy-homonymy boundary and sense structure
- [Kanji Learning and Dictionary Treatment](../research/kanji-learning-dictionaries.md) — on'yomi/kun'yomi reading assignment and kanji as a disambiguation tool
