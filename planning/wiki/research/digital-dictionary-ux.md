# Digital Dictionary UX

**Last updated**: 2026-04-06

## How users actually use online dictionaries

Research on dictionary use behavior reveals patterns that should inform interface design.

### Look-up-then-leave behavior
Most dictionary visits last under 30 seconds. Users are mid-task (reading, writing, translating) when they consult a dictionary. They want an answer, not an experience.

### Search dominance
Users strongly prefer typing queries over browsing (Lew, 2012, 2013). They expect results instantly. De Schryver (2003) coined "simultaneous feedback" for the pattern where results update as the user types.

### Inflected form searching
L2 learners frequently search for inflected forms and multi-word expressions, not just lemmas. A Japanese learner might type 食べられない rather than 食べる. Lemmatization (matching inflected forms to headwords) is essential.

### Power-law distribution
De Schryver & Joffe (2004) found that log analysis of online dictionaries reveals a power-law distribution: a small percentage of words account for most lookups, but the long tail is enormous.

### Information avoidance
Müller-Spitzer et al. (2012) showed that users overwhelmingly ignore information that requires extra clicks. The default view matters enormously.

## Best practices

### Progressive disclosure
Show the most-needed information first (headword, primary gloss, POS) and let users expand into examples, usage notes, and cross-references on demand. This reduces cognitive load for the majority use case (quick lookup) while supporting deeper exploration.

### Search quality over visual polish
Invest in:
- Fuzzy matching for typos
- Kana/romaji flexibility (accept both とうきょう and tokyo)
- Partial matching
- Multi-word expression matching
- Bidirectional search (J→E and E→J from one box)

### Mobile-first design
Mobile now accounts for the majority of dictionary lookups. Key constraints:
- Limited viewport (one sense at a time is ideal)
- Touch targets minimum 44px
- Slow/intermittent connectivity (favor local search over server round-trips)
- Swipe gestures for entry navigation
- Sticky headers for long entries

### Offline capability
For static sites like je-dict-1, a client-side search index enables offline use. This is both a performance advantage (no server round-trip) and a resilience feature.

## Current state of je-dict-1

The site uses a fully client-side architecture with a pre-generated JavaScript search index. Here is a detailed assessment of current capabilities:

### Search architecture

The search index (`search-index.js`) is generated at build time by `search_index_builder.py`. It creates three parallel indexes:

| Index | What it indexes | Match strategy |
|-------|----------------|----------------|
| **Japanese** | Headword (kanji stripped of furigana) + reading (hiragana) | Substring match (`key.includes(query)`) |
| **Romaji** | Romanized reading (auto-converted from hiragana) | Prefix match (`key.startsWith(query)`) |
| **English** | Individual words from glosses and sense definitions | Prefix match per word |

Query type is auto-detected: if the input contains Japanese characters (hiragana, katakana, kanji), it searches the Japanese index; otherwise it uses romaji. Users can also manually select Japanese, romaji, or English mode via radio buttons.

### What works well

- **Zero-latency search**: No server round-trip — results appear as soon as the user submits. The entire index loads with the page.
- **Romaji support**: English-keyboard users can search by romaji (e.g., "taberu" finds 食べる). This is a major usability win for learners who know pronunciation but not kanji.
- **Three-mode search**: Japanese, romaji, and English search from a single interface.
- **Tag-based browsing**: A dedicated tag search page (`tag-search.js`) supports filtering by POS, semantic tags, formality, transitivity, tier, and domain. Includes statistics mode, missing-tag detection, and combined queries. Paginated at 50 results per page.
- **Header search**: A persistent search box in the site header forwards queries to the main search page via URL parameters, enabling search from any page.
- **URL-based deep linking**: Searches can be triggered via `?q=query&type=auto` URL parameters, supporting external linking to search results.
- **Offline capability**: Since the index is a static JS file, the site works fully offline once loaded.

### Current limitations and improvement opportunities

| Area | Current state | Potential improvement |
|------|--------------|---------------------|
| **Fuzzy matching** | Not implemented — typos return zero results | Levenshtein distance or phonetic similarity matching |
| **Inflected form search** | Not indexed — searching 食べられない won't find 食べる | Feed conjugation table forms into the search index |
| **Katakana normalization** | Katakana input works (matched against Japanese index) but no half/full-width normalization | Normalize ｶﾀｶﾅ → カタカナ before search |
| **Simultaneous feedback** | Results appear only on submit (Enter or button click) | Live-as-you-type results (debounced) |
| **Result ranking** | Results sorted alphabetically by reading | Relevance ranking: exact match > prefix > substring; tier weighting |
| **English multi-word** | Each word searched independently — "to eat" returns all entries containing "to" OR "eat" | Phrase matching or AND logic for multi-word queries |
| **Progressive disclosure** | Entry pages show all content at once | Collapsible sections for examples, notes, cross-references |
| **Mobile optimization** | Functional but desktop-first layout | Touch-optimized spacing, swipe navigation between entries |

### Inflected form search — a high-value opportunity

je-dict-1 already stores full conjugation tables for verbs and i-adjectives. The data is there — it just isn't fed into the search index. Adding conjugated forms to the Japanese/romaji indexes would enable a major UX improvement: learners could search for forms they encounter in the wild (食べさせられる, 美しくない) and find the dictionary entry directly.

This is particularly valuable because inflected-form searching is one of the most researched pain points in digital dictionary UX. Lew (2012) found that failed lookups due to inflection are a significant source of user frustration with L2 dictionaries.

Implementation would require:
1. Adding conjugation forms to `search_index_builder.py` — iterating through `conjugation` field values and indexing them as additional Japanese/romaji keys pointing to the entry
2. Managing index size — full conjugation tables add many forms per entry. Selective indexing (common forms only) might be needed
3. Distinguishing base-form matches from conjugated-form matches in results display

### Search index size considerations

With 22,000+ entries, the search index JS file is already substantial. Adding conjugated forms could multiply its size significantly. Potential mitigations:
- Index only high-frequency conjugation forms (masu, te, nai, ta)
- Use compressed representations (shared prefix encoding)
- Split the index into lazy-loaded chunks
- Use a proper client-side search library (e.g., Fuse.js, FlexSearch) that handles indexing more efficiently

## Entry page UX

Beyond search, the entry pages themselves have UX considerations:

### Information density
Entry pages display headword, reading, POS, definitions, examples, notes, conjugation tables, and cross-references. For entries with many examples and detailed notes, this can be quite long. Research on information avoidance (Müller-Spitzer et al., 2012) suggests that content below the fold is often ignored.

### Navigation between entries
Cross-references and `prominent_see_also` links enable entry-to-entry navigation, supporting the "vocabulary network" browsing pattern. The kanji index provides another navigation path: clicking a kanji in a headword shows all entries containing that kanji.

### Audio
Audio files were removed in early 2026. Future TTS-based audio (see [Audio Coverage Expansion](../ideas/audio-expansion.md)) would improve the lookup experience, especially for pronunciation-sensitive learners.

## Research references

- Lew, R. (2012). "How can we make electronic dictionaries more effective?" — Studies on user behavior and inflected form lookup failure
- De Schryver, G.-M. (2003). "Lexicographers' Dreams in the Electronic-Dictionary Age" — Simultaneous feedback concept
- Müller-Spitzer, C. et al. (2012). Research on dictionary use — Information avoidance patterns
- De Schryver, G.-M. & Joffe, D. (2004). Log file analysis of online dictionary use — Power-law distribution of lookups
- Lew, R. (2013). Online dictionary skills — Search behavior and user expectations

## Related pages

- [Architecture and Build System](../project/architecture.md) — technical details of the build pipeline
- [Open Issues](../project/open-issues.md) — known problems including UX items
- [Audio Coverage Expansion](../ideas/audio-expansion.md) — TTS-based pronunciation audio plans
- [Learner Lexicography](learner-lexicography.md) — pedagogical principles informing UX decisions
