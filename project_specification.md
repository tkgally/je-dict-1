# je-dict-1: Project Specification

A Japanese-English learner's dictionary emphasizing quality over quantity, delivered as a static website.

---

## 1. Project Vision and Goals

### 1.1 Core Purpose

**je-dict-1** is a Japanese-English dictionary designed for learners of Japanese as a second language. Unlike existing resources like Jisho.org or JMdict, which prioritize breadth, this dictionary prioritizes **depth and quality**—fewer entries, but each one carefully crafted with explanatory definitions, natural example sentences, and usage guidance.

### 1.2 What Makes This Different

| Existing Resources | je-dict-1 |
|-------------------|-----------|
| Brief glosses ("eat; have a meal") | Explanatory definitions with nuance |
| Inconsistent example quality | AI-generated naturalistic examples optimized for learning |
| Reference-oriented | Study and exploration-oriented |
| Dependent on external services | Fully self-contained, offline-capable |

### 1.3 Working Title

The project will use the folder name **je-dict-1** as its working title until a permanent name is chosen.

---

## 2. Target Users

### 2.1 Primary Audience

Intermediate learners of Japanese—people who:
- Can read hiragana and katakana fluently
- Know some kanji and are building vocabulary
- Are comfortable reading English (no controlled defining vocabulary needed)

### 2.2 Level-Agnostic Design

The dictionary should serve learners across proficiency levels (N5 through N1). Rather than hiding information based on level, the interface shows all available data and trusts users to navigate what's relevant to them.

### 2.3 Primary Use Case

**Vocabulary study and exploration**—users actively studying Japanese who want to spend time with entries, explore related concepts, and deeply understand words. This is not optimized for split-second lookups while reading (though it should still be usable for that).

---

## 3. Lexicographic Philosophy

### 3.1 Prescriptive/Descriptive Balance

The dictionary takes a **hybrid approach with clear labeling**:
- Include informal, colloquial, and slang usage
- Always label register, formality, and context clearly
- Note when usage is non-standard or could cause problems if misused
- Do not make judgments about "correct" Japanese—document actual usage

### 3.2 Definition Style

**Multiple formats per entry:**
1. **Quick gloss**: Brief English equivalent for scanning (e.g., "to eat")
2. **Explanatory definition**: Fuller explanation of meaning, nuance, and what distinguishes this word from similar words

This follows the spirit of Longman/Oxford learner's dictionaries but assumes fluent English readers, so there is no need to restrict the defining vocabulary.

### 3.3 Example Sentences

- **AI-generated naturalistic examples** optimized for teaching
- Examples should sound natural (not textbook-stilted) while clearly illustrating the target word's usage
- Each example includes Japanese text and English translation

### 3.4 Register and Formality

Include formality/politeness information **where relevant**:
- Not every entry needs a register label
- Note when a word is specifically formal, casual, humble, honorific, or could be inappropriate in certain contexts
- Express in free-form prose notes rather than rigid category fields

### 3.5 Particles and Auxiliary Verbs

Include particles (は, が, を, に, etc.) and auxiliary verbs (ている, てある, etc.) as dictionary entries **with rich explanations**. These are crucial for learners and often poorly explained elsewhere.

### 3.6 Loanwords

Treat katakana loanwords (外来語) like any other vocabulary. No special handling or de-prioritization.

---

## 4. Entry Schema

### 4.1 Minimum Viable Entry

An entry must contain at minimum:
- Headword (kanji form if applicable)
- Reading (hiragana)
- At least one gloss (brief English equivalent)

This allows shipping early with minimal entries while maintaining usefulness.

### 4.2 Full Entry Fields

```json
{
  "id": "taberu_00001",
  "headword": "食べる",
  "reading": "たべる",
  "part_of_speech": "verb (ichidan)",
  "gloss": "to eat",
  "definitions": [
    {
      "sense_number": 1,
      "gloss": "to eat",
      "explanation": "The most common verb for eating. Used for consuming food by putting it in the mouth and swallowing. Unlike 召し上がる (meshiagaru), this is the neutral form without politeness implications."
    }
  ],
  "examples": [
    {
      "japanese": "朝ごはんを食べましたか。",
      "english": "Did you eat breakfast?",
      "notes": null
    }
  ],
  "notes": "This is the plain/dictionary form. In polite speech, use 食べます. The te-form 食べて is commonly used in compound structures like 食べている (eating/have eaten) and 食べてみる (try eating).",
  "cross_references": [],
  "metadata": {
    "created": "2025-01-15T10:30:00Z",
    "modified": "2025-01-15T10:30:00Z",
    "ai_model": "claude-3-opus",
    "confidence": "high",
    "review_status": "verified",
    "jlpt_level": "N5",
    "frequency_rank": null
  }
}
```

### 4.3 Field Descriptions

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Unique identifier (see §6.3 for format) |
| `headword` | Yes | Dictionary form, kanji if applicable |
| `reading` | Yes | Hiragana reading |
| `part_of_speech` | Yes | Grammatical category |
| `gloss` | Yes | Brief English equivalent for quick scanning |
| `definitions` | No | Array of sense objects with detailed explanations |
| `definitions[].sense_number` | Yes (if definitions) | Numeric sense identifier |
| `definitions[].gloss` | Yes (if definitions) | Brief gloss for this sense |
| `definitions[].explanation` | No | Fuller explanatory definition |
| `examples` | No | Array of example sentence objects |
| `examples[].japanese` | Yes (if examples) | Japanese sentence |
| `examples[].english` | Yes (if examples) | English translation |
| `examples[].notes` | No | Notes about this specific example |
| `notes` | No | Free-form prose: grammar notes, usage notes, cultural notes |
| `cross_references` | No | Array of related entry IDs (semantic field links) |
| `metadata` | Yes | Entry metadata (see below) |

### 4.4 Metadata Fields

| Field | Required | Description |
|-------|----------|-------------|
| `created` | Yes | ISO 8601 timestamp of entry creation |
| `modified` | Yes | ISO 8601 timestamp of last modification |
| `ai_model` | No | Which AI model generated/edited this entry |
| `confidence` | No | Confidence level: "high", "medium", "low" |
| `review_status` | Yes | "draft", "reviewed", or "verified" |
| `jlpt_level` | No | N5, N4, N3, N2, or N1 |
| `frequency_rank` | No | Numeric frequency rank if available |

### 4.5 Cross-References

For MVP, cross-references are **deferred**. When implemented, they will link entries within the same **semantic field** (e.g., all cooking verbs, all weather words). Other relationship types (synonyms, antonyms, word families) are out of scope for initial release.

### 4.6 Future Fields (Not for MVP)

These fields are planned for future phases but should not block initial development:
- `pitch_accent`: Tokyo-standard pitch accent pattern
- `audio_url`: Link to pronunciation audio
- `kanji_breakdown`: Component analysis of kanji in headword

---

## 5. Headword Organization

### 5.1 What Constitutes a Headword

Headwords are **full words** (単語, 熟語, etc.), not individual kanji. This is a vocabulary dictionary, not a kanji dictionary. Kanji lookup features may be added later but are not part of the core design.

### 5.2 Multiple Readings

When a word has multiple readings:
1. **One reading is designated as primary** and contains the full entry (definitions, examples, notes)
2. **Other readings get variant entries** that cross-reference the main entry
3. Variant entries are stored in a separate `/variants/` directory

Example:
- Main entry: `/entries/ka/kawaru_00001.json` (変わる, かわる)
- Variant: `/variants/ka/kawaru_00002.json` references main entry (if there's an alternate reading)

### 5.3 Homonyms

Words with the same reading but different meanings get **separate entries** with different IDs:
- `hashi_00001.json` (橋, bridge)
- `hashi_00002.json` (箸, chopsticks)
- `hashi_00003.json` (端, edge)

---

## 6. File Organization

### 6.1 Directory Structure

```
je-dict-1/
├── entries/                    # Main entry files
│   ├── a/                      # あ行 (a, i, u, e, o)
│   ├── ka/                     # か行 (ka, ki, ku, ke, ko, ga, gi, gu, ge, go)
│   ├── sa/                     # さ行 (sa, shi, su, se, so, za, ji, zu, ze, zo)
│   ├── ta/                     # た行 (ta, chi, tsu, te, to, da, ji, zu, de, do)
│   ├── na/                     # な行 (na, ni, nu, ne, no)
│   ├── ha/                     # は行 (ha, hi, fu, he, ho, ba, bi, bu, be, bo, pa, pi, pu, pe, po)
│   ├── ma/                     # ま行 (ma, mi, mu, me, mo)
│   ├── ya/                     # や行 (ya, yu, yo)
│   ├── ra/                     # ら行 (ra, ri, ru, re, ro)
│   └── wa/                     # わ行 (wa, wo, n)
├── variants/                   # Alternate reading entries (same structure as entries/)
│   ├── a/
│   ├── ka/
│   └── ...
├── build/                      # Build scripts and tooling
│   ├── build.py                # Main build script
│   ├── validate.py             # Entry validation
│   ├── generate_index.py       # Search index generation
│   └── requirements.txt        # Python dependencies
├── web/                        # Web application source
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── docs/                       # Generated output (served by GitHub Pages)
│   ├── data/
│   │   ├── entries.json        # Compiled entry data
│   │   └── index.json          # Search index
│   └── ...
├── .gitignore
├── project_specification.md    # This file
├── PROJECT_STATUS.md           # Session continuity file (see §16)
└── README.md
```

### 6.2 50-on Directory Mapping

Entries are organized by the first kana of their reading, following traditional Japanese dictionary order (五十音順). Directories use romaji names:

| Directory | Kana | Includes |
|-----------|------|----------|
| `/a/` | あ行 | あ, い, う, え, お |
| `/ka/` | か行 | か, き, く, け, こ, が, ぎ, ぐ, げ, ご |
| `/sa/` | さ行 | さ, し, す, せ, そ, ざ, じ, ず, ぜ, ぞ |
| `/ta/` | た行 | た, ち, つ, て, と, だ, ぢ, づ, で, ど |
| `/na/` | な行 | な, に, ぬ, ね, の |
| `/ha/` | は行 | は, ひ, ふ, へ, ほ, ば, び, ぶ, べ, ぼ, ぱ, ぴ, ぷ, ぺ, ぽ |
| `/ma/` | ま行 | ま, み, む, め, も |
| `/ya/` | や行 | や, ゆ, よ |
| `/ra/` | ら行 | ら, り, る, れ, ろ |
| `/wa/` | わ行 | わ, を, ん |

### 6.3 File Naming Convention

Files use a **compound naming scheme**: `{romanized_reading}_{id}.json`

**Romanization rules** (Modified Hepburn with kana-faithful long vowels):
- Use standard Hepburn: し = shi, つ = tsu, ち = chi, ふ = fu
- Long vowels follow kana spelling, not pronunciation:
  - 東京 (とうきょう) → `toukyou` (not `tōkyō` or `tokyo`)
  - 景気 (けいき) → `keiki` (not `kēki`)
  - ケーキ → `keeki` (not `kēki`)
  - 大きい (おおきい) → `ookii`
- Maintain close correspondence to kana renderings used in kokugo dictionaries
- ASCII letters and numbers only—no macrons, no kana in filenames

**ID assignment:**
- Sequential numeric IDs per directory
- Format: 5-digit zero-padded number
- First entry in `/ka/` is `00001`, second is `00002`, etc.

**Examples:**
- 食べる (たべる) in `/ta/`: `taberu_00001.json`
- 東京 (とうきょう) in `/ta/`: `toukyou_00001.json`
- 橋 (はし, bridge) in `/ha/`: `hashi_00001.json`
- 箸 (はし, chopsticks) in `/ha/`: `hashi_00002.json`

---

## 7. Search and Indexing

### 7.1 Search Capabilities

Users can search by:
1. **Japanese headword** (kanji or kana)
2. **English meaning** (searches glosses and definitions)
3. **Romaji** (as accessibility fallback for learners still building kana fluency)
4. **Conjugated forms** (e.g., searching 食べて finds 食べる)

### 7.2 Conjugation Indexing

All verb and adjective conjugations should be searchable:
- 食べる: 食べて, 食べた, 食べます, 食べない, 食べられる, 食べさせる, etc.
- Searching any conjugated form returns the dictionary-form entry

**Implementation approach**: Deferred to implementation phase. Options include pre-computed index (generate all forms at build time) or runtime deconjugation (algorithm recognizes forms). The spec does not mandate a specific approach.

### 7.3 Search Results

- Results ordered **alphabetically** (simple, predictable ordering)
- No relevance scoring or frequency-based ranking for MVP
- Exact matches displayed first, then partial matches

### 7.4 Index Architecture

For MVP, use a **single index file** loaded at startup:
- `index.json` contains all searchable terms mapped to entry IDs
- Sharding and optimization deferred until performance becomes a concern
- Target: acceptable performance up to ~10,000 entries with single index

---

## 8. Web Application

### 8.1 Technology Constraints

- **Completely static**: HTML, CSS, JavaScript only
- **No external dependencies**: No React, Vue, jQuery, etc.
- **No build step for web**: The web app source is the distribution
- **Offline-capable**: Works from local files without a server

### 8.2 Visual Design

**Pleasant but restrained:**
- Clean, readable, professional
- Content is the star—avoid flashy design elements
- Good typography for both Japanese and English text
- Appropriate whitespace—not cramped, not sparse
- Works well on both desktop and mobile

### 8.3 Entry Display

**Japanese-first layout:**
- Large Japanese headword prominently displayed at top
- Reading (hiragana) directly below headword
- Part of speech
- Quick gloss
- Detailed definitions (if available)
- Example sentences with translations
- Notes

All information is visible by default—no hidden sections or "show more" toggles.

### 8.4 Search Interface

- **Explicit search**: User must press Enter or click a search button
- No search-as-you-type (avoids distraction and unnecessary processing)
- Clear search input with appropriate Japanese IME support
- Search type selector: Japanese / English / Romaji (or auto-detect)

### 8.5 Accessibility

- Romaji search as accessibility feature for learners still building kana fluency
- Proper semantic HTML
- Keyboard navigable
- Readable font sizes

---

## 9. Build System

### 9.1 Technology

- **Python scripts** for all build tooling
- Dependencies managed via `requirements.txt`
- No Node.js required

### 9.2 Build Process

1. **Validation**: Check all entry files against schema, report errors
2. **Compilation**: Combine entries into optimized format for web app
3. **Index generation**: Build search index including conjugated forms
4. **Output**: Generate distribution files in `/docs/`

### 9.3 Build Outputs

```
docs/
├── index.html
├── styles.css
├── app.js
├── data.js               # Embedded entry data and search index
└── data/
    ├── entries.json      # All entry data (JSON format)
    └── index.json        # Search index (JSON format)
```

**Note**: Output directory is `docs/` for GitHub Pages compatibility. The site is served at https://tkgally.github.io/je-dict-1/

### 9.4 Validation Rules

The validation script should check:
- Required fields present
- Field types correct
- ID uniqueness
- Cross-reference targets exist (when cross-refs are implemented)
- Romanization in filename matches reading
- File is in correct directory for its reading

---

## 10. Content Creation

### 10.1 Authorship Model

**Primarily AI-generated** with human oversight:
- AI generates entry drafts
- Human reviews and edits for quality
- Staged rollout: personally verify core vocabulary, looser validation for expansion

### 10.2 Multi-Model Architecture

Entry generation will use **multiple AI models**:

1. **Claude Code** (Anthropic): Primary tool for interactive development, schema refinement, and high-quality exemplar entries
2. **Other models via OpenRouter API**: For batch generation, experimentation, and cost optimization

**OpenRouter integration** (details TBD):
- Python scripts will call OpenRouter API to generate entries
- Each entry's `metadata.ai_model` field records which model produced it
- Allows comparison of model quality and selection of best outputs
- Enables parallel generation across multiple models

This multi-model approach provides:
- Flexibility to use the best model for each task
- Cost optimization (cheaper models for drafts, expensive for refinement)
- Redundancy if one provider has issues
- Ability to compare outputs and choose the best

### 10.3 AI Workflow: Seed and Expand

1. Create high-quality **exemplar entries** manually or with heavy AI collaboration
2. AI uses exemplars as templates to generate similar entries
3. Human reviews and edits AI output
4. Refined entries become new exemplars for further expansion

### 10.4 Quality Control Strategy

**Staged rollout approach:**
1. **Phase 1**: Manually verify all entries in core vocabulary (N5-N4)
2. **Phase 2**: AI-generate with sampling review for N3-N2 vocabulary
3. **Phase 3**: Lighter review for N1 and specialized vocabulary
4. Ongoing: Community error reporting (implementation deferred)

### 10.5 Initial Content

**Start with JLPT N5-N4 vocabulary** as the seed content:
- Well-defined word lists available
- Pedagogically sequenced
- Covers most common vocabulary
- Achievable target for "critical mass"

### 10.6 Critical Mass

**500-1000 core words** is the target for a genuinely useful dictionary. This is achievable within 3-6 months of steady work.

---

## 11. Distribution

### 11.1 Multiple Channels

The dictionary will be distributed via:
1. **Web hosting**: Static site on personal domain or GitHub Pages
2. **Downloadable package**: ZIP file for offline use

Single build process outputs to both channels.

### 11.2 Licensing

**Source-available but curated:**
- Code is visible (likely on GitHub)
- Content contributions by invitation only
- Maintainer controls what gets merged
- Specific license TBD

---

## 12. Risk Mitigation

### 12.1 Quality Control at Scale

**Risk**: AI errors slipping through, publishing incorrect information

**Mitigations**:
- Staged rollout with tighter review for core vocabulary
- Detailed metadata tracking (AI model, confidence, review status)
- Plan for community error reporting (deferred implementation)
- "Draft" vs "verified" status visible in entries

### 12.2 Scope Creep

**Risk**: Getting lost in features, never shipping

**Mitigations**:
- MVP clearly defined: cut cross-references, defer audio, defer pitch accent
- Minimum viable entry is just headword + reading + gloss
- Critical mass is only 500-1000 words
- Phased roadmap with working dictionary at each phase

### 12.3 Motivation and Abandonment

**Risk**: Losing interest before reaching critical mass

**Mitigations**:
- Architecture enables small, frequent wins—ship improvements weekly
- JLPT vocabulary provides clear, measurable progress (% of N5 complete, etc.)
- Working dictionary from day one, even if tiny
- Personal use keeps it relevant

### 12.4 Technical Complexity

**Risk**: Scaling, search performance, or offline support harder than expected

**Mitigations**:
- Start simple: single index file, no sharding
- Defer optimization until it's actually needed
- Vanilla JS, no framework complexity
- Static architecture is inherently simple to deploy

---

## 13. Phased Roadmap

### Phase 1: Foundation (Current)
- Project structure and schema finalized
- Build and validation scripts working
- Basic web interface (search, display)
- 50-100 sample entries demonstrating full entry quality
- **Deliverable**: Working dictionary with limited content

### Phase 2: Core Vocabulary
- Complete N5 vocabulary (~800 words)
- Begin N4 vocabulary
- Reach "critical mass" of 500-1000 high-quality entries
- **Deliverable**: Genuinely useful dictionary for beginners

### Phase 3: Conjugation and Search
- Implement conjugation indexing
- Enhance search (better partial matching, romaji support)
- Performance testing and optimization if needed
- **Deliverable**: Full-featured search experience

### Phase 4: Content Expansion
- Complete N4, begin N3 vocabulary
- Refine AI generation workflow
- Implement cross-references (semantic fields)
- **Deliverable**: Intermediate-level coverage

### Phase 5: Polish and Distribution
- Offline package generation
- PWA features (if warranted)
- Community feedback mechanism
- Audio pronunciation (if pursued)
- **Deliverable**: Production-ready dictionary

---

## 14. Implementation Notes

### 14.1 Decisions Deferred to Implementation

The following are explicitly **not specified** and should be decided during implementation based on what works:

- Conjugation indexing approach (pre-computed vs runtime)
- Exact search index structure and sharding strategy
- PWA/service worker implementation details
- Error reporting mechanism

### 14.2 Constraints Summary

| Constraint | Value |
|------------|-------|
| Web dependencies | None (vanilla JS only) |
| Build tooling | Python |
| File format | JSON |
| File names | ASCII only |
| Index structure | Single file (MVP) |
| Minimum entry | headword + reading + gloss |
| Critical mass | 500-1000 entries |
| Initial content | JLPT N5-N4 vocabulary |

---

## 15. Implementation Status

The following items from the original specification have been completed:

1. **Project structure** - All directories created (entries/, variants/, build/, web/, docs/)
2. **Entry schema** - JSON schema defined in `build/schema.json`
3. **Validation script** - `build/validate.py` validates entries against schema
4. **Build script** - `build/build.py` compiles entries and generates search index
5. **Web interface** - Fully functional with search and sidebar browser
6. **Sample entries** - 47 entries created (N5 vocabulary + particles)
7. **Furigana system** - All entries have `{kanji|reading}` notation, toggle in UI
8. **GitHub Pages** - Live site at https://tkgally.github.io/je-dict-1/

### 15.1 Technical Decisions Made

- **Static data embedding**: Data is embedded in `data.js` at build time, allowing the dictionary to work from `file://` URLs without a server
- **Sidebar browser**: Entry browser grouped by kana row (あ行, か行, etc.) for easy browsing
- **Wider layout**: Max-width increased to 1100px for better desktop experience
- **GitHub Pages**: Output to `docs/` folder for direct GitHub Pages serving
- **Furigana toggle**: Button in header toggles ruby annotations on/off, preference saved in localStorage

### 15.2 Current Next Steps

1. Continue expanding N5 vocabulary toward critical mass (500-1000 entries)
2. Add more particle and grammar entries
3. Consider implementing conjugation search

---

## 16. Session Continuity System

This project will be developed intermittently over months, with work sessions separated by days or weeks. To enable seamless handoff between sessions (and between different AI assistants), the project maintains a **status file** that records the current state and next steps.

### 16.1 The Status File

**Location**: `PROJECT_STATUS.md` in the project root

**Purpose**: When starting a new conversation, the user points the AI to this file, which contains everything needed to understand where the project is and what to do next.

### 16.2 Status File Structure

```markdown
# je-dict-1 Project Status

**Last updated**: [ISO 8601 timestamp]
**Last session**: [Brief description of what was accomplished]

## Current State

### Phase
[Which phase from the roadmap: Foundation / Core Vocabulary / etc.]

### Infrastructure Status
- [ ] Directory structure created
- [ ] Build scripts working
- [ ] Validation scripts working
- [ ] Web interface functional
- [x] Example: checked items are complete

### Content Status
- **Total entries**: [number]
- **Verified entries**: [number]
- **Draft entries**: [number]
- **N5 coverage**: [X/~800 words] ([percentage]%)
- **N4 coverage**: [X/~700 words] ([percentage]%)

### Recent Changes
- [List of significant changes from recent sessions]

## Next Steps

### Immediate (next session)
1. [Specific, actionable task]
2. [Specific, actionable task]
3. [Specific, actionable task]

### Upcoming (future sessions)
- [Broader goals not yet started]

## Known Issues
- [Any bugs, problems, or blockers]

## Notes for AI Assistants
- [Any context that would help a new AI understand the current state]
- [Conventions established during development]
- [Decisions made that aren't in the main spec]
```

### 16.3 Maintenance Protocol

**At the end of each work session**, the AI assistant should:
1. Update `PROJECT_STATUS.md` with:
   - What was accomplished this session
   - Current counts and completion percentages
   - Clear next steps for the following session
   - Any new issues or decisions made
2. Commit the updated status file

**At the start of each work session**, the user should:
1. Point the AI to `PROJECT_STATUS.md`
2. Optionally provide specific goals for the session
3. The AI reads the status and continues from where work left off

### 16.4 Why This Matters

- **No context loss**: Each session starts with full project awareness
- **Multi-AI compatibility**: Different AI assistants (Claude, GPT, etc.) can pick up the project
- **Human readability**: The status file is also useful for the human maintainer
- **Accountability**: Clear record of progress and decisions

---

*Specification version: 1.2*
*Created: January 2026*
*Updated: January 2026*
- v1.1: Added session continuity system, multi-model architecture
- v1.2: Updated to reflect implementation status (47 entries, static data embedding, sidebar browser)
*Based on detailed requirements interview*
