# Agent 3: Learner Experience Assessment

## Executive Summary

The TKG Japanese-English Learner's Dictionary (TKGJE) is a remarkably ambitious project that, even in its current state, delivers genuine value to intermediate learners of Japanese. With 10,306 entries, a thoughtful three-tier vocabulary system, and carefully structured entry guidelines, the dictionary already surpasses many free online resources in explanatory depth. The strongest aspects are the particle entries (で, だけ), which combine definitions with contrastive analysis and common mistake sections; the verb entries with transitivity and aspect information; and the cultural notes in entries like 玄関 and 神社. The main areas for improvement are: (1) inconsistency in entry depth across tiers, with some basic-tier entries falling well below v2 quality standards; (2) the need for more cross-references to create a connected learning network; and (3) interface features that could better support vocabulary building workflows. The inline word linking feature, still in progress, has the potential to be transformative for learners once fully deployed.

---

## 1. Entry Content Assessment

### Definitions

**Strengths:**
- Multi-sense entries are well-structured, with clear sense numbering (e.g., 高い with three distinct senses: tall, expensive, high-degree)
- Definitions include brief explanations beyond the gloss, providing context that helps learners distinguish nuances
- Particle entries like で have six well-differentiated senses with explanatory text that addresses learner confusion points directly
- The explanation field in definitions often includes example collocations inline, reinforcing understanding

**Weaknesses:**
- Some basic-tier entries have minimal definitions. For example, 映画 (movie) has a single sense with the explanation "A motion picture." -- just two words. For a basic-tier word, this is inadequate. An intermediate learner would benefit from knowing that 映画 covers both the medium and the event (going to see a movie), and how it differs from ドラマ or アニメ.
- A few entries have definitions that are circular or too brief to add value beyond the English gloss (e.g., 映画's "A motion picture" does not expand on the gloss "movie, film")
- Some general-tier entries like 訪れる lack the "politeness" tag in metadata, creating inconsistency

### Example Sentences

**Strengths:**
- The progressive length requirement (short to long) is well-implemented in the best entries. 高い demonstrates this clearly: from "この山は高いです" (7 chars) to "この仕事は難しいですが、成功する可能性が高いと思います" (27+ chars)
- Example notes are often pedagogically valuable -- e.g., noting "〜すぎる = too much" in a 高い example, or "Direct quotation with と particle" in 言う
- Multi-sense entries group examples under their respective senses in the HTML output, which is excellent for learners
- Basic-tier entries like 高い have 16 examples across 3 senses, well above the minimum of 5 per sense

**Weaknesses:**
- Significant inconsistency across the basic tier. 映画 (basic tier) has only 2 examples total -- far below the required 5 per sense. This entry appears to have been created early and never polished.
- 言う (basic tier) has exactly 5 examples for a single sense -- meeting the minimum but not demonstrating the richness seen in 高い or で
- Some example notes duplicate information already in the definition (e.g., example notes for こと just say "Sense 1: thing/matter" or "Sense 2: nominalizer" without adding pedagogical value)
- The vocabulary restriction system (basic-tier examples 1-2 should use only basic vocabulary) is well-designed but difficult to verify at scale -- it is unclear how many entries actually comply

### Notes

**Strengths:**
- The structured note format (TRANSITIVITY, ASPECT, COMMON PATTERNS, etc.) is excellent for scan-reading. Learners can quickly find what they need.
- Cultural notes in entries like 玄関 and 神社 provide real-world context that goes beyond what standard dictionaries offer (e.g., the components of a genkan, the distinction between shrine and temple)
- Contrastive sections (e.g., だけ vs しか, で vs に) directly address learner confusion points
- The keigo entry for 召し上がる clearly shows the three-level keigo relationship (plain/honorific/humble)

**Weaknesses:**
- Notes formatting is inconsistent. Some entries use `・` for bullet points (言う), while the standard calls for `- `. Some use SECTION HEADERS, others don't.
- The 階 (counter) entry has a notes formatting issue: "Unlike American English\n- there is no 'ground floor'" has a line break in the middle of a sentence, which renders oddly
- Some notes are overly long relative to the word's complexity, while others are too sparse. 映画 has extensive notes (genres, compounds, related terms) but only 2 examples -- an inverted priority
- The notes in 訪れる list conjugation forms (negative, te-form, past), which is arguably unnecessary since conjugation is regular for ichidan verbs. This space could be better used for collocations or register guidance.

---

## 2. Vocabulary Tier System

### Design Assessment

The three-tier system (basic: 795, core: 1,998, general: 7,513) is pedagogically sound. The self-containment principle -- requiring complete semantic groups within a tier -- is a particularly intelligent design decision that avoids the fragmented knowledge common in JLPT-based systems.

**Strengths:**
- The tier system is well-documented with clear criteria for assignment
- The self-containment principle prevents awkward gaps (e.g., all days of the week in the same tier)
- The policy of freezing basic/core tiers and adding all new entries to general prevents scope creep
- Tier badges are visually differentiated in the HTML output (green for basic, blue for core, yellow for general)

**Areas for Improvement:**
- The tier system is currently invisible to learners in the browse interface. There is no way to filter or browse by tier. An intermediate learner who wants to study "all core tier words" cannot do so without using the Advanced search.
- しか is classified as general tier, while だけ is basic tier. For an intermediate learner, understanding the だけ/しか distinction is essential. しか arguably belongs in core at minimum, but the current policy forbids tier changes. The notes and cross-references partially compensate for this, but the tier mismatch means a learner studying "basic words" will encounter だけ but not the contrasting しか.
- The tier labels themselves ("basic", "core", "general") are somewhat opaque. "General" in particular could be misread as "generic" rather than "advanced/specialized." A brief tooltip or explanation on the entry pages would help.

---

## 3. Example Sentence Quality

### Naturalness

The example sentences are generally natural and avoid textbook stiffness. Sentences like "母は「早く起きなさい」と毎朝言いますが、私は起きたくないといつも思っています" feel like authentic Japanese rather than constructed grammar drills.

### Pedagogical Progression

The best entries demonstrate excellent progression:
- で (particle): 31 examples covering all 6 senses, from "図書館で勉強します" to "兄は毎日自転車で会社に通っていますが、雨の日は電車で行きます"
- 高い: 16 examples across 3 senses with clear length progression

However, progression quality varies widely:
- こと: 10 examples that are all roughly similar in length (10-20 characters), with little progression from simple to complex
- 映画: 2 examples, both under 10 characters -- no progression at all

### Vocabulary Compliance

I could not verify at scale whether basic-tier examples 1-2 actually restrict vocabulary to basic-tier words only, or whether core-tier examples 1-2 restrict to basic+core. This is a critical quality feature that appears to depend on manual verification during entry creation.

### Unique Pedagogical Value

Several entries demonstrate example notes that genuinely aid learning:
- "Literally: popularity is high" on 人気が高い helps learners understand the Japanese conceptualization
- "Te-iru form for ongoing action" on 何を言っているの helps connect grammar to usage
- "できるだけ = as much as possible" teaches a high-frequency expression within an example

---

## 4. Notes and Cross-References

### Cross-Reference Quality

The cross-reference system is well-designed with 7 types (pair, antonym, keigo, synonym, contrast, related, see_also) and a hybrid resolution system. However:

- **Coverage is sparse.** Only 567 cross-references across 10,306 entries means the average entry has fewer than 0.06 cross-references. Most sampled entries had zero cross-references.
- **The best cross-references are excellent.** 召し上がる links to both plain forms (食べる, 飲む) and the humble form (いただく) with keigo-type references. だけ links to しか (contrast) and ばかり (related).
- **Many obvious connections are missing.** 高い has no cross-reference to 低い or 安い despite mentioning them in notes. こと has no cross-reference to もの despite the definition explicitly contrasting them. 映画 has no cross-references at all.

### Notes Quality

The notes field is the entry's most valuable learning asset when done well. The structured format (TRANSITIVITY, ASPECT, COMMON PATTERNS) is a genuine innovation over traditional dictionaries.

**Best-in-class examples:**
- で: Concise contrastive explanation of で vs に as the core takeaway
- だけ: Grammar patterns, common expressions, and the critical contrast with しか
- 玄関: Cultural components, vocabulary for parts of the entrance, and natural expressions

**Below-standard examples:**
- 映画: Notes are comprehensive but lack the structured format (no SECTION HEADERS)
- 訪れる: Lists conjugation forms for a regular verb instead of focusing on register/usage
- 階: Formatting error in the notes field

---

## 5. Interface Assessment

### Navigation

**Strengths:**
- Sticky header with search, toggle buttons, and navigation works well
- Browse page with collapsible kana sections is a natural way to explore
- Recent page shows latest additions with new/revised status
- Random page provides serendipitous discovery
- Pending page shows transparency about what is yet to come

**Weaknesses:**
- Entry pages have a reduced navigation bar (only Home, Random, About) compared to the main pages (which also include Advanced, Browse, Recent, Pending). This means a learner on an entry page cannot easily navigate to Browse or Recent.
- No "next entry" / "previous entry" navigation on entry pages. Learners studying sequentially through a tier have no way to advance without going back to browse.
- No breadcrumb navigation on entry or kanji pages
- The header search on entry pages redirects to the home page for results, which is a jarring experience

### Search

**Strengths:**
- Auto-detection of query type (Japanese, English, romaji) is user-friendly
- Search supports partial matching (startsWith for romaji/English, includes for Japanese)
- The Advanced search with tag-based filtering is a powerful tool

**Weaknesses:**
- English search uses word-initial matching only (`key.startsWith(word)`), meaning a search for "eat" would not find entries glossed as "to eat" (since "to" would be a separate token). This likely works in most cases but could miss entries.
- No search suggestions or autocomplete as the user types
- Search results show headword, reading, and gloss but not the tier badge, which would help learners prioritize results

### Readability

**Strengths:**
- Clean, uncluttered design with good use of whitespace
- Font choices are appropriate (system sans-serif with Japanese font fallbacks)
- Furigana display using ruby elements is standard and accessible
- The furigana toggle, examples toggle, and word links toggle give learners control over information density
- Furigana color (accent blue) provides visual distinction without being distracting
- Notes section has a distinctive blue-left-border style that makes it visually scannable

**Weaknesses:**
- On multi-sense entries with many examples, the page becomes very long. 高い with 16 examples and で with 31 examples require significant scrolling. There is no collapse/expand for individual senses.
- The example notes appear in italic gray, which may be too subtle for important pedagogical information
- No dark mode support
- Entry metadata (tier badge, dates) is at the very bottom, where learners may not see it

### Mobile Experience

The CSS includes responsive breakpoints at 600px that collapse the browse layout, hide toggle labels, and reformat the metadata. The design appears mobile-functional but the narrow header search input (100px on mobile, expanding to 120px on focus) is quite small for Japanese input.

---

## 6. Proposed Improvements

Each proposal below is sized for a single Claude session (10-15 minutes, within context window limits). Proposals are ordered by estimated impact on learner experience.

### Proposal 1: Audit and Upgrade Under-Example'd Basic/Core Entries

**Prompt to Claude:**
```
Read the example-sentences skill. Then check which basic and core tier entries
have fewer than the required number of examples (5 per sense for basic/core).
Write a Python script that scans all entries and outputs a report: entry_id,
tier, number_of_senses, total_examples, examples_per_sense, and a compliance
flag (PASS/FAIL). Sort by tier (basic first), then by examples_per_sense
ascending. Save the report to build/reports/example_compliance.txt.
```
**Why:** This identifies the exact entries that need remediation. The report becomes an actionable worklist for subsequent sessions that add examples.

**Follow-up session prompt:**
```
Read build/reports/example_compliance.txt. Pick the 10 basic-tier entries with
the fewest examples relative to their required minimum. For each one, read
the existing entry, then add examples following the example-sentences skill
guidelines (progressive length, vocabulary restrictions). Update the modified
timestamp. Validate with python3 build/validate.py after each entry.
```

### Proposal 2: Extract Cross-References from Notes Fields

**Prompt to Claude:**
```
Read the cross-reference-entry skill. Then read 40 basic-tier entries that
currently have zero cross-references. For each entry, read its notes field
and identify words that should be cross-referenced: antonyms mentioned in
CONTRAST sections, pair verbs in TRANSITIVITY sections, similar words in
SIMILAR WORDS sections, and keigo forms. Add appropriate cross-references
to each entry. Run python3 build/harden_references.py --apply to resolve
any that can be resolved. Validate afterward.
```
**Why:** Many entries already mention related words in their notes but lack formal cross-references. This is semantic work -- it requires understanding which relationships are meaningful -- making it ideal for Claude rather than scripts.

### Proposal 3: Add Structured Notes to Shallow Entries

**Prompt to Claude:**
```
Read the vocabulary-notes skill and the entry-guidelines skill. Then find
15 basic-tier noun entries whose notes are shorter than 100 characters or
lack structured sections (COMMON EXPRESSIONS, RELATED, etc.). For each one,
rewrite the notes to include: (1) a clear core explanation, (2) at least
3 common collocations in a bulleted COMMON EXPRESSIONS section, (3) a
contrast or related words section if applicable. Follow the noun notes
template from the vocabulary-notes skill. Maintain all furigana. Validate.
```
**Why:** Entries like 映画 have notes that are lists of compounds without structured sections, while entries like 玄関 demonstrate the ideal format. Standardizing raises the floor.

### Proposal 4: Improve Navigation on Entry Pages

**Prompt to Claude:**
```
Read the build script (build/build_flat.py) to understand how entry HTML
pages are generated. Then modify the entry page template to include the
full navigation bar (Home, Advanced, Browse, Recent, Random, Pending, About)
instead of the reduced set (Home, Random, About). Also add a "Back to
Browse" link in the entry header area. Rebuild and verify a few entry pages
look correct.
```
**Why:** Learners on entry pages are currently stranded with minimal navigation options. This is a straightforward template change with high usability impact.

### Proposal 5: Add Tier Badge to Search Results

**Prompt to Claude:**
```
Read the search.js file and the search-index.js structure. Modify the
search system to include vocabulary_tier in the search index entries, and
update the displayResults function in search.js to show a small tier badge
(styled like the one on entry pages) next to each search result. This helps
learners prioritize which words to study based on their level. Rebuild the
search index and verify.
```
**Why:** Search results currently show headword, reading, and gloss but not the tier. An intermediate learner searching for a word cannot tell at a glance whether it is basic, core, or general vocabulary.

### Proposal 6: Verify Vocabulary Tier Compliance in Basic-Tier Examples

**Prompt to Claude:**
```
Read the example-sentences skill, focusing on vocabulary restrictions by
tier. Then select 20 basic-tier entries that have been polished (modified
date after January 20, 2026). For each entry, read examples 1-2 and verify
that every content word (noun, verb, adjective, adverb) is in the basic
tier. Read examples 3-5 and verify that every content word is in basic or
core tier. Flag any violations. For entries with violations, suggest
replacement words that are in the correct tier. Document findings in
build/reports/tier_compliance_spot_check.txt.
```
**Why:** The vocabulary restriction system is a key differentiator of this dictionary but compliance is hard to verify automatically since it requires understanding what constitutes a "content word" in each sentence. A spot check establishes a baseline.

### Proposal 7: Standardize Counter Entry Format

**Prompt to Claude:**
```
Read the 階 (kai) counter entry and 5 other counter entries. Assess
whether they share a consistent format. Design a counter-entry template
that includes: (1) irregular reading table for numbers 1-10, (2) common
usage contexts, (3) related counters, (4) what the counter counts. Then
revise 10 counter entries to match this template. Validate.
```
**Why:** Counter entries are a distinct word type with specific learner needs (irregular readings, usage scope). A consistent format helps learners study them systematically. The 階 entry already partially does this but has formatting issues.

### Proposal 8: Create Learner-Facing Tier Study Lists

**Prompt to Claude:**
```
Write a build script (build/build_tier_pages.py) that generates three
HTML pages in docs/: basic.html, core.html, general.html. Each page
lists all entries in that tier, organized by semantic category (from
metadata.tags.semantic), with headword, reading, and gloss. Include
a count per category. Use the same styling as browse.html. Add links
to these pages from the main navigation. Rebuild.
```
**Why:** Learners currently cannot browse by tier. An intermediate learner wanting to review all core vocabulary has no way to do so except through the Advanced tag search, which is less intuitive. Dedicated tier pages create a natural study progression path.

### Proposal 9: Improve だけ/しか Interconnection as a Model for Contrastive Pairs

**Prompt to Claude:**
```
Read the entries for だけ (03093_dake) and しか (09959_shika). Both
entries mention the other in their notes, and だけ has a cross-reference
to しか. However, しか has no cross-reference back to だけ. Also, しか
is in the general tier with only 3 examples, while だけ is basic tier
with 10 examples.

Improve both entries as a model for contrastive pairs:
1. Add a cross-reference from しか to だけ (type: contrast)
2. Add 2 more examples to しか showing the contrast with だけ
3. Ensure both entries' notes use the same contrastive explanation
   framework so a learner reading either entry gets the full picture
4. Add example notes highlighting the emotional nuance difference
Validate both entries.
```
**Why:** The だけ/しか pair is one of the most common learner confusion points. Making these entries model contrastive pairs improves the dictionary's value as a learning tool and establishes a pattern for other pairs (は/が, に/で, etc.).

### Proposal 10: Assess and Improve Example Sentence Notes Utility

**Prompt to Claude:**
```
Read 30 entries across all three tiers that have example notes. Categorize
each note into one of: (a) grammar point explanation, (b) vocabulary gloss,
(c) sense label only (e.g., "Sense 1: limiting"), (d) cultural/usage note,
(e) collocation highlight. Assess which categories provide genuine learning
value vs. which are redundant with other information in the entry. Write
a brief report with recommendations for note guidelines, and revise 10
examples where notes say only "Sense 1: [gloss]" to instead provide a
genuinely useful grammar or usage observation.
```
**Why:** Example notes are a prime learning micro-moment, but many currently just label the sense ("Sense 1: only") rather than teaching something. Converting these to mini grammar explanations or cultural notes significantly increases per-example learning value.

---

## Appendix: Entries Sampled

| Entry ID | Word | Tier | Type | Examples | Cross-refs | Assessment |
|----------|------|------|------|----------|------------|------------|
| 00006_aru | ある | basic | verb | 15 (3 senses) | 1 | Excellent -- inline links, comprehensive |
| 00500_takai | 高い | basic | adj | 16 (3 senses) | 0 | Good examples, missing cross-refs |
| 00502_de | で | basic | particle | 31 (6 senses) | 1 | Excellent -- model entry |
| 00515_iu | 言う | basic | verb | 5 (1 sense) | 1 | Meets minimum, could be richer |
| 01034_kai | 階 | core | counter | 5 (1 sense) | 0 | Good but notes have formatting issue |
| 01164_koto | こと | basic | noun | 10 (2 senses) | 0 | Good, missing cross-ref to もの |
| 01310_meshiagaru | 召し上がる | core | verb/keigo | 5 (1 sense) | 3 | Excellent cross-refs, good keigo notes |
| 01620_jinja | 神社 | general | noun | 3 (1 sense) | 0 | Good cultural notes |
| 02273_eiga | 映画 | basic | noun | 2 (1 sense) | 0 | **Below standard** - needs 5 examples |
| 03093_dake | だけ | basic | particle | 10 (2 senses) | 2 | Strong notes, good cross-refs |
| 05003_genkan | 玄関 | general | noun | 3 (1 sense) | 0 | Excellent cultural notes |
| 07678_otozureru | 訪れる | general | verb | 3 (2 senses) | 0 | Missing tags, lists conjugation unnecessarily |
| 09959_shika | しか | general | particle | 3 (1 sense) | 0 | Good notes, missing back-ref to だけ |
| 10000_you | 要 | general | noun | 3 (1 sense) | 0 | Practical, well-targeted |
| 10006_nantokanaru | 何とかなる | general | expression | 3 (1 sense) | 0 | Good tone description |
| 10015_kokorogakeru | 心がける | general | verb | 3 (1 sense) | 0 | Well-structured notes |
| 00104_hiroba | 広場 | general | noun | 5 (1 sense) | 0 | Demonstrates inline word links |

**Key observations from sampling:**
- Basic-tier entries vary dramatically in quality (compare で with 16 entries vs. 映画 with 2)
- General-tier entries consistently meet the 3-example minimum but rarely exceed it
- Cross-references are severely underutilized across all tiers
- The inline word linking feature (visible in ある and 広場) is a powerful learning aid that deserves priority deployment
- Structured notes (with SECTION HEADERS and bullet lists) are present in approximately 60% of sampled entries; the remainder use paragraph format
