# Digital Dictionary UX

**Last updated**: 2026-04-05

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

The site uses a pre-generated JavaScript search index with client-side search. This handles the offline/performance requirement well. Areas for potential improvement:

- **Fuzzy matching**: Not currently implemented
- **Inflected form search**: Conjugation data exists in entries but may not feed into the search index
- **Mobile UX**: Functional but not mobile-first
- **Progressive disclosure**: Entry pages show all content; collapsible sections could help
- **Romaji search**: Status unclear — worth investigating

## Research references

- Lew, R. (2012). "How can we make electronic dictionaries more effective?" — Studies on user behavior
- De Schryver, G.-M. (2003). "Lexicographers' Dreams in the Electronic-Dictionary Age" — Simultaneous feedback concept
- Müller-Spitzer, C. et al. (2012). Research on dictionary use — Information avoidance patterns
- De Schryver, G.-M. & Joffe, D. (2004). Log file analysis of online dictionary use

## Related pages

- [Architecture and Build System](../project/architecture.md)
- [Open Issues](../project/open-issues.md)
