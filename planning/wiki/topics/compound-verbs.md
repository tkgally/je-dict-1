# Compound Verb Representation

**Last updated**: 2026-07-03 (added "Bound suffix morphemes in decomposition prose" — the convention to leave bound V2 suffixes like 込む unlinked, since their compound sense has no standalone entry)

## Overview

Japanese compound verbs (複合動詞, fukugō dōshi) are verbs formed by combining two verb stems: V1 (the first verb in stem/連用形 form) + V2 (the second verb). They are extremely productive in Japanese — the NINJAL Compound Verb Lexicon catalogs over 2,700 common examples. How to represent these in a learner's dictionary is an ongoing design question for je-dict-1.

## Types of compound verbs

Compound verbs fall into two broad categories with very different lexicographic implications:

### Lexical compounds

True compound verbs where V1 + V2 creates an idiomatic meaning not fully predictable from the components:

| Compound | V1 | V2 | Meaning |
|----------|----|----|---------|
| 飛び込む (とびこむ) | 飛ぶ (jump) | 込む (into) | to dive/jump into; to drop in |
| 打ち明ける (うちあける) | 打つ (strike) | 明ける (open) | to confess, to confide |
| 取り消す (とりけす) | 取る (take) | 消す (erase) | to cancel, to retract |
| 落ち着く (おちつく) | 落ちる (fall) | 着く (arrive) | to calm down, to settle |

These clearly merit their own dictionary entries because the meaning cannot be derived from the parts.

### Syntactic/aspectual compounds

Semi-productive patterns where V2 functions as an auxiliary, adding aspectual or directional meaning to any V1:

| V2 pattern | Meaning added | Example |
|------------|---------------|---------|
| ～始める (はじめる) | inception ("begin to V") | 食べ始める, 読み始める |
| ～続ける (つづける) | continuation ("keep V-ing") | 走り続ける, 考え続ける |
| ～終わる (おわる) | completion ("finish V-ing") | 読み終わる, 食べ終わる |
| ～出す (だす) | sudden onset ("burst out V-ing") | 泣き出す, 笑い出す |
| ～込む (こむ) | inward/thorough ("V deeply into") | 考え込む, 飛び込む |
| ～直す (なおす) | redo ("V again, V over") | やり直す, 書き直す |
| ～合う (あう) | reciprocal ("V each other") | 話し合う, 助け合う |
| ～かける | partial/attempt ("almost V, start to V") | 言いかける, 倒れかける |
| ～過ぎる (すぎる) | excess ("V too much") | 食べ過ぎる, 飲み過ぎる |
| ～回る (まわる) | thoroughness ("V all around") | 走り回る, 探し回る |

These are more problematic for dictionary treatment because the V2 pattern is productive — it can combine with hundreds of V1 verbs.

### The gray area

Many compound verbs sit between these categories. 飛び込む is partly compositional (flying + into) but has idiomatic extensions (dropping in unexpectedly). 考え込む is transparent (thinking + deeply-into) but the specific nuance (becoming absorbed/worried) goes beyond simple composition. The boundary is a continuum, not a line.

## Current je-dict-1 approach

### What gets its own entry

je-dict-1 currently creates entries for compound verbs on a case-by-case basis:

- **Lexical compounds** with idiomatic meaning always get entries (取り消す, 落ち着く, 打ち明ける)
- **Frequently used aspectual compounds** sometimes get entries, especially when the combination has specific nuances:
  - 考え込む (to become lost in thought) — entry exists
  - 走り続ける (to keep running) — entry exists
  - 書き間違える (to write incorrectly) — entry exists
  - 動き始める (to begin to move) — entry exists
- **Fully productive combinations** where meaning is V + "begin/continue/finish" generally do not get entries (食べ始める, 読み終わる)

### POS tagging

Compound verbs use the same POS tags as simple verbs: `verb-godan`, `verb-ichidan`, `verb-suru`. There is no special "compound verb" tag. The V2 determines the conjugation class (e.g., ～込む compounds are godan, ～始める compounds are ichidan).

### Cross-referencing

Entries for compound verbs note the ～込む or ～直す pattern in their explanation. Some entries cross-reference the base verbs or the V2 pattern verb. This is inconsistent — there's no systematic policy for linking compound verb entries to their components.

## The entry-vs-pattern decision

The key design question from [Open Issues](../project/open-issues.md): should compound verbs get their own entries, or should they be documented as patterns under the component verbs?

### Arguments for separate entries

1. **Findability** — A learner encountering 考え込む in text needs to look it up. If it's not its own entry, they must know to decompose it into 考える + 込む, which requires grammatical knowledge they may lack.
2. **Nuance documentation** — Even semi-transparent compounds often have nuances worth documenting. 泣き出す doesn't just mean "begin to cry" — it implies sudden, uncontrolled onset.
3. **Example sentences** — Each compound verb has its own collocational patterns and typical contexts that are hard to capture in a V2 pattern description.
4. **Search** — Users search for the full compound form. Without an entry, they get no result.

### Arguments for pattern documentation

1. **Scalability** — With ~2,700 compound verbs and dozens of productive V2 patterns, creating entries for all combinations is impractical. 始める alone could combine with hundreds of V1 verbs.
2. **Redundancy** — Entries for 食べ始める, 読み始める, 書き始める, 走り始める etc. would all essentially say "begin to [V1]" with minor variations.
3. **Teaching the pattern** — Documenting ～始める as a pattern teaches learners to decompose and understand new compound verbs independently, which is a more valuable skill than memorizing individual entries.
4. **Entry count bloat** — At 25,000 entries, adding thousands of transparent compound verbs would dilute the dictionary's signal-to-noise ratio.

### Recommended approach

A hybrid strategy, which je-dict-1 already follows informally:

1. **Create entries for lexical compounds** — any compound verb where the meaning is idiomatic or where the combination has specific nuances beyond V1 + V2.
2. **Create entries for high-frequency aspectual compounds** — common combinations that learners will encounter and want to look up (考え込む, 泣き出す, やり直す), even when the meaning is somewhat transparent.
3. **Document V2 patterns in the V2 verb's entry** — The entry for 始める should document the ～始める pattern and give examples. Same for 込む, 出す, 直す, etc.
4. **Don't create entries for fully transparent combinations** — 食べ始める, 読み始める etc. don't need their own entries if the ～始める pattern is well-documented.

The decision criterion: **if a learner who knows V1 and V2 separately would still need help understanding the compound, it deserves its own entry.**

## The NINJAL Compound Verb Lexicon

The National Institute for Japanese Language and Linguistics (NINJAL) maintains an online Compound Verb Lexicon covering over 2,700 verb-verb compound verbs. Key features:

- Explicit V1/V2 structure representation
- Classification as lexical vs. syntactic compounds
- Semantic descriptions of both components
- Example sentences
- Available in English and Japanese

This resource could inform which compound verbs je-dict-1 should prioritize for entry creation: lexical compounds that NINJAL flags as non-compositional are strong candidates.

## Future directions

1. **Systematic V2 pattern documentation** — Ensure all major V2 auxiliary verbs (始める, 続ける, 込む, 出す, 直す, 合う, etc.) have well-documented pattern descriptions in their entries.
2. **Cross-reference network** — Link compound verb entries back to their V1 and V2 components, and link V2 pattern verbs forward to notable compound verb entries.
3. **Candidate identification** — Use NINJAL data or corpus frequency to identify high-priority compound verbs missing from the dictionary.
4. **Search improvement** — Consider whether the search system could recognize compound verb patterns and suggest the V2 entry when no exact match is found.

## Known quality patterns in compound verb entries (polishing findings)

Comprehensive-polish sessions through 2026 have identified several recurring
quality issues in compound verb entries, particularly in the 06000–09000 range
(the 2026-03 through 2026-04 creation cohort). These inform polishing priorities
and backlog items.

### Semantic tag errors: object-category tags on action verbs

The most systemic compound-verb quality problem is **wrong semantic tag category**.
Compound verbs and suru verbs have been assigned object-domain tags
(electronics, clothing, tool, furniture, animal-mammal, occupation, body-part)
instead of the process/action tags appropriate for their meanings
(action, cognition, communication, emotion, movement).

Root cause: the AI that created these entries applied semantic tags based on
*example sentence topic* rather than the *headword's semantic domain*. A compound
verb about a computer task received "electronics"; one about a body movement received
"body-part". The fix is straightforward: select the semantic tag that characterizes
the verb's core meaning (action, cognition, communication, etc.), not the domain of
its example sentences.

Confirmed in multiple comprehensive-polish sessions from the 01490s through the
06000s. The `check_tag_drift.py --check unknown-semantic` detector (Cleanup Backlog
P20) catches out-of-vocabulary tags; the correct-vocabulary-but-wrong-category
sub-pattern (e.g. "action" on a cognition verb) requires per-entry judgment via the
accuracy-review `tags` pass or comprehensive-polish. See also
[Schema Tag Reliability](schema-tag-reliability.md) → "Stale auto-labels" and
[Cleanup Backlog](../ideas/cleanup-backlog.md) → P11.

### Inline link gaps in the 06000-range cohort

The 06000–09000 creation cohort was built before inline-link (`⟦...⟧`) polishing
was standard practice. Many entries have no inline links in either examples or
notes. Within notes specifically, three structural positions are systematically
unlinked (Cleanup Backlog P21):

1. **Transitivity labels**: `{自動詞|じどうし}` / `{他動詞|たどうし}` in TRANSITIVITY
   lines have furigana wrappers but no `⟦...⟧` link to the 自動詞/他動詞 entries.
2. **Particles in pattern examples**: `を`, `が`, `から`, `に`, `で` in `Pattern:`
   bullets are bare rather than linked.
3. **Content words in COMMON PATTERNS**: noun and verb arguments in collocation
   bullets lack both content-word links and particle links.

These are candidates for a systemic-fix batch once the Tooling Backlog item 15
detector (`check_artifacts.py` lint rule for unlinked 自動詞/他動詞) is built.

### Bound suffix morphemes in decomposition prose (linking convention)

Compound-verb notes frequently contain a decomposition line such as
`COMPOUND VERB: 流し + 込む ("into")` and a `RELATED ～込む COMPOUND VERBS` header.
A recurring per-session question (2026-07-03 routine polish, entries 06381–06388)
is whether the bound V2 suffix in such prose should be inline-linked. The answer
is **no**: the suffix *sense* the compound relies on has no matching standalone
entry. For 込む, both existing 込む entries gloss as "to be crowded" — the
directional/completive suffix sense ("into / thoroughly") is a different morpheme,
so a link to `00719_komu` would be **semantically wrong**, not merely imprecise.
The established convention (consistent with how the 拝〜 humble prefix and the 〜的
suffix are handled) is to **leave bound compound-verb suffixes unlinked** in
decomposition prose and `RELATED ～X` headers, linking only the free V1 element and
any standalone content words. This is a candidate for an explicit note in the
`inline-word-links` skill so future sessions don't re-derive it each time (logged
as a `[skill]` recommendation, 2026-07-03).

### Notes-level conjugation duplication

A subset of godan compound verbs in the 06xxx range have redundant CONJUGATION
prose sections in their `notes` field even though the entry already has a proper
`conjugation` JSON field with all forms. This is a batch artifact from a period
when conjugation data lived in notes rather than in a structured field. Examples
found: 06852_hourikomu, 06858_ukabiagaru, 06735_sashikakaru. Comprehensive-polish
removes these case-by-case; a one-shot scanner is proposed in [Tooling Backlog](../ideas/tooling-backlog.md)
(extension to `check_artifacts.py --issue dup-conjugation`). See also
[Cleanup Backlog](../ideas/cleanup-backlog.md) → P4 "notes-level duplication"
sub-pattern.

### Implications for compound-verb polishing

- **Semantic tag review**: When polishing a compound verb entry, always verify that
  the semantic tag reflects the verb's own action/process domain, not the domain of
  its example sentence topics.
- **Inline link audit**: Entries in the 06000+ range should be assumed to have
  incomplete inline links until verified. The P21 structural positions are the
  highest-priority gaps.
- **Notes prose cleanup**: Check whether the notes open with a conjugation table
  (negative/te/past bullets) that duplicates the structured `conjugation` field;
  remove if present.

## Implications for je-dict-1

The compound verb question affects multiple project concerns:

- **Entry creation**: The `newentries.md` prompt and candidate word selection should have clear guidance on when compound verbs merit entries.
- **Quality standards**: Compound verb entries should note the pattern they belong to and cross-reference components.
- **Search UX**: Learners searching for unlisted compounds should get useful results (e.g., redirecting to the V2 pattern entry).
- **Candidate list**: `candidate_words.json` likely contains compound verbs that fall on both sides of the entry/pattern line — the cleanup process should be informed by this framework.

## Related pages

- [Open Issues](../project/open-issues.md) — the compound verb design question
- [Entry Design](../project/entry-design.md) — schema structure and POS tags
- [Verb Transitivity Pairs](verb-transitivity.md) — related verb classification question
- [Cross-Reference Design](cross-references.md) — linking compound verbs to components
- [Content Pipeline](../project/content-pipeline.md) — entry creation workflow
- [Word Formation and Morphology](../research/word-formation.md) — broader context of Japanese compounding and derivation
- [Multiword Expressions](../research/multiword-expressions.md) — compound verbs as one category in the broader MWE taxonomy
- [Lemmatization and Headword Selection](../research/lemmatization-headword-selection.md) — entry scope criteria: when compounds merit their own entry
