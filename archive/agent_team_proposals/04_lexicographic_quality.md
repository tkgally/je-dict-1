# Agent 4: Lexicographic Quality Assessment

## Executive Summary

The je-dict-1 dictionary demonstrates strong lexicographic fundamentals with 10,306 entries, well-defined skill specifications, and a thoughtful quality framework (v2 standards). Definitions are generally accurate and pedagogically appropriate. The particle entries (ga, ha, ni, de, wo) are exceptionally thorough, serving as models for the project. The notes field is present in all entries, with a healthy median length of ~490 characters. However, significant quality gaps remain that require sustained semantic work:

**Key Findings:**
1. **Definition quality is solid** -- English glosses are accurate and natural, with multi-sense entries properly disambiguated. No factual errors found in the 25+ entries sampled.
2. **Example sentences need significant work** -- 1,401 of 2,799 basic/core entries lack the required 5 examples per sense, and 1,706 of 7,507 general entries fall below 3 per sense.
3. **Notes field quality is inconsistent** -- All entries have notes, but only 1,228 of 3,119 verbs include transitivity information and only 726 include aspect/ている notes, despite these being HIGH PRIORITY requirements.
4. **Cross-references are sparse** -- 7,626 of 10,306 entries (74%) have zero cross-references. Only 2,023 entries include SIMILAR WORDS distinctions. This is the largest gap for a dictionary focused on helping humans distinguish near-synonyms.
5. **Inline word linking covers only 6%** -- 608 of 10,306 entries have inline links in examples. The project acknowledges this is in progress.
6. **Quality evolution is positive** -- Recent entries (10000+ range) consistently include transitivity, aspect, similar words, and nuance sections. Early entries (00000-01000) vary widely; some are excellent (particles, basic verbs), others are skeletal.

---

## 1. Definition Quality Assessment

### Strengths

- **Multi-sense disambiguation is well handled.** Entries like `kodawaru` (10319) properly separate the positive ("particular about quality") and negative ("fixated on") senses, with clear explanations of the nuance shift. `Tsukkomu` (07000) correctly identifies the physical, motion, and comedy retort senses.
- **English glosses are natural and accurate.** The glosses avoid overly literal translations and provide immediately usable English equivalents. For example, `ga` (00051) is glossed as "subject marker" and "object marker (with certain predicates)" rather than attempting a single all-encompassing translation.
- **Cultural and pragmatic information is woven into definitions.** `Gobusata` (10326) explains the social function of the word within the definition. `Sumimasen` (00998) captures the triple function (excuse me / sorry / thank you) that a monolingual dictionary would not convey.
- **Explanations complement glosses well.** The `explanation` field in definitions consistently adds something beyond the gloss, providing usage context or boundary conditions.

### Areas for Improvement

- **Some definitions could be more precise about register boundaries.** `Bakari` (02006) is tagged as `formality: informal`, but its three senses span different registers (sense 3, "approximately," is not particularly informal). Multi-register words need per-sense register notes.
- **Scope clarifications are sometimes missing for nouns.** The other-entries skill template calls for "Scope Clarification (when needed)" -- explaining when Japanese meaning differs from English. This is present in some entries but absent in many nouns where it would be valuable. For example, `te` (hand) should note it can include the arm; `kao` (face) should note its extended meaning of reputation/dignity.
- **Compound entries lack decomposition notes.** Many compound nouns (e.g., `tennenkinen`, `toshokan`, `yuubinkyoku`) would benefit from notes explaining their kanji components, helping learners predict and understand compound meanings.

### Model Entries (Definitions)
- `ga` (00051) -- Excellent three-sense breakdown with detailed predicates_requiring section
- `kodawaru` (10319) -- Well-calibrated positive/negative sense distinction
- `sumimasen` (00998) -- Properly captures pragmatic polysemy

---

## 2. Example Sentence Assessment

### Strengths

- **Progressive length is generally well implemented.** In entries like `aru` (00006) and `ni` (00314), examples clearly progress from short to long. The particle entry for `ni` demonstrates excellent pedagogical progression with 30 examples across 6 senses.
- **Natural Japanese is prioritized.** Example sentences read as authentic Japanese rather than textbook constructions. Entries like `garari` (10313) use realistic contexts ("the shop's image changed completely with the new manager").
- **Sense number assignment is accurate.** Multi-sense entries consistently tag examples to the correct sense.

### Areas for Improvement

- **Example count shortfall is the largest mechanical gap.** 1,401 basic/core entries need additional examples (having fewer than 5 per sense). This is ~50% of all basic/core entries. For general entries, 1,706 (23%) fall below the 3-per-sense requirement.
- **Counter entries lack sound-change demonstration examples.** The counter for `ken` (01993) has only 3 examples but does not demonstrate the voiced reading (sanGen vs. sanKen). The skill specification calls for examples showing "sound change patterns (1, 3, 6, 8, 10)." Counter entry `ten` (01553) fares better with 10 examples but still lacks explicit sound-change coverage.
- **Vocabulary tier restrictions may not be enforced.** The polishing system has example-sentence checking at position `next: 01059`, meaning only early entries have been verified for tier-appropriate vocabulary in examples. Basic/core entries in the 01059+ range likely contain unchecked vocabulary violations.
- **Some entries lack collocation examples.** The skill specification requires "at least one example shows a common collocation" per sense, but some entries use generic contexts rather than demonstrating high-frequency pairings.

### Model Entries (Examples)
- `ni` (00314) -- 30 examples across 6 senses, excellent progression
- `aru` (00006) -- 15 examples across 3 senses, clear and natural
- `ha` (00079) -- 10 examples covering both topic and contrast uses

### Entries Needing Example Work
- Counter entries in general (only 3 examples each for `ken`, `choume`)
- General-tier entries created in bulk (05000-09000 range) frequently have only 3 examples regardless of sense count

---

## 3. Notes Section Assessment

### Strengths

- **All 10,306 entries have non-empty notes** (minimum 81 characters, median 491). This is exceptional for a dictionary of this size.
- **Recent entries (10000+ range) follow the template well.** `kodawaru` (10319) includes TRANSITIVITY, ASPECT, COMMON PATTERNS, and NUANCE sections. `kimama` (10311) includes COMMON COLLOCATIONS, NUANCE, and SIMILAR WORDS. `gobusata` (10326) includes COMMON PATTERNS, USAGE, and FORMALITY SCALE.
- **Cultural notes are excellent when present.** `manjuu` (05000) provides types, fillings, cultural significance, and even a rakugo reference. `garari` (10313) correctly distinguishes giongo vs. gitaigo usage.
- **Formatting is consistent.** Section headers use ALL CAPS followed by colons. Bullet points use `- ` format. Paragraphs are separated by blank lines. This matches the vocabulary-notes skill specification.

### Areas for Improvement

- **Verb notes are the highest-priority gap.**
  - Only 1,228/3,119 verbs (39%) include transitivity information despite this being HIGH PRIORITY.
  - Only 726/3,119 verbs (23%) include aspect/ている notes despite this being HIGH PRIORITY.
  - The gap is concentrated in mid-range entries (02000-09000), where entries were likely created before the v2 quality standards were established.
- **SIMILAR WORDS sections exist in only 2,023/10,306 entries (20%).** Given that distinguishing near-synonyms is a core value proposition of this dictionary, this represents significant untapped potential. Many adjective and adverb entries that share semantic space (e.g., big/large/wide, fast/early/quick) lack contrastive notes.
- **COMMON PATTERNS coverage is good but inconsistent.** 6,246/10,306 entries (61%) include some form of collocation listing. The remaining 39% would benefit from even brief collocation notes.
- **Inline links in notes are inconsistent.** Some entries (e.g., `aru` 00006) have inline links (⟦...⟧) within the notes field, while most do not. The notes in `kodawaru` (10319) mention パランス without furigana for the katakana, and use plain text for cross-referenced words like 気をつける. A systematic pass to add inline links to notes would increase navigability.
- **Counter entries are missing the full 1-10 counting table.** The skill specification requires a "Full Counting Pattern (1-10)" but most counter entries provide only partial counts. `ken` (01993) shows only 1, 2, 3, 4, and "how many" -- missing 5-10. `choume` (09491) shows only 1-3.

### Model Entries (Notes)
- `kodawaru` (10319) -- Includes all required verb sections plus historical nuance note
- `gobusata` (10326) -- Includes formality scale comparison (casual through formal)
- `ga` (00051) -- Comprehensive particle contrast notes
- `manjuu` (05000) -- Rich cultural and variety information

### Entries Needing Notes Work
- Mid-range verb entries (02000-09000) generally lack transitivity and aspect sections
- Counter entries lack full counting tables
- Many adjective entries lack FORMS (adverbial, noun form) sections

---

## 4. Cross-Reference Quality

### Current State

| Reference Type | Count | Description |
|---|---|---|
| related | 1,867 | General topical relationship |
| antonym | 493 | Opposite meanings |
| see_also | 296 | Supplementary reference |
| contrast | 287 | Confused/similar words |
| synonym | 181 | Near-synonyms |
| pair | 119 | Transitivity pairs |
| keigo | 30 | Polite form references |
| homophone | 5 | Same reading, different meaning |
| **Total** | **3,278** | |
| Entries with 0 refs | **7,626** (74%) | |

### Strengths

- **Particle entries are well cross-referenced.** `ga` links to `ha`; `ni` links to `de` and `he`; `de` links to `ni`. These are the most important cross-references for learners.
- **Transitivity pairs are systematically linked.** 119 pair-type references correctly connect intransitive/transitive verb pairs (e.g., `amaru`/`amasu`).
- **Keigo references are present** for common verbs linking to honorific/humble forms (e.g., `taberu` links to `meshiagaru`).

### Areas for Improvement

- **74% of entries have no cross-references at all.** Even entries with obvious related words (e.g., `kimama` has SIMILAR WORDS in notes mentioning `wagamama`, `jiyuu`, and `maipeesu` but no cross_references linking to them).
- **The "contrast" type is underused** at only 287 entries. This is the most pedagogically valuable reference type for this dictionary, as it directly helps learners distinguish confusable words. Currently, contrast notes exist in the notes text but are not formalized as cross-references.
- **Homophone cross-references are almost nonexistent** (5 total). Japanese has many homophones (koushi, kikan, seiki, etc.) and learners struggle with these. A systematic homophone-linking pass would be highly valuable.
- **Similar words mentioned in notes are not always formalized as cross-references.** The notes for `kimama` (10311) mention `wagamama`, `jiyuu`, and `maipeesu` as similar words, but the `cross_references` array is empty. This means the UI cannot create clickable navigation between these related entries.

### Model Cross-References
- `taberu` (00396) -- Links to `nomu` (see_also), `meshiagaru` (keigo)
- `tsukkomu` (07000) -- Links to `tsukkomi` (related) and `komu` (related)
- `ga` (00051) -- Links to `ha` (contrast)

---

## 5. Consistency Analysis

### Formatting Consistency (Good)

- Part of speech labels are mostly consistent but have some variation:
  - "godan verb" vs. "verb (godan)" vs. "verb" -- this is inconsistent across early vs. recent entries
  - Tags in metadata use standardized values (`verb-godan`, `adjective-na`, etc.)
- Notes formatting is remarkably consistent across the dictionary -- ALL CAPS headers, bullet points, paragraph breaks
- Example sentence formatting follows the `{kanji|reading}` pattern consistently

### Depth Consistency (Needs Work)

- **Particle entries are uniformly excellent** -- all include predicates_requiring, particle_contrasts, fixed_patterns, common_mistakes, and extensive examples
- **Basic/core tier entries are generally more thorough** than general-tier entries, as expected
- **Significant depth gap between early and recent entries:**
  - Recent entries (10000+): consistently include TRANSITIVITY, ASPECT, COMMON PATTERNS, SIMILAR WORDS, NUANCE
  - Early entries (00000-01000): some are excellent (basic verbs, particles) but many mid-range entries lack these sections
  - Mid-range entries (02000-08000): most variable quality; these were likely created during expansion phases before v2 standards
- **Counter entries are consistently thin** -- most have only 3 examples and partial counting tables
- **Expression entries are adequate but could be richer** -- `kamoshirenai` (00164) has 5 examples and reasonable notes but lacks the "Response Pairs" and deeper "Situational Context" that the skill specification calls for

### Quality Evolution (Positive Trend)

The dictionary shows clear quality improvement over time:

| Period | Typical Features | Example |
|---|---|---|
| Early (00000-01000) | Good definitions, variable notes, 3-5 examples | `amaru` (00001) |
| Mid (02000-08000) | Adequate notes, 3 examples, some cross-refs | `bakari` (02006) |
| Recent (10000+) | Full template compliance, rich notes, 3-6 examples | `kodawaru` (10319) |

---

## 6. Particle Entry Assessment

The 10 core particle entries (ga, ha, ni, de, wo, kara, to, mo, made, he) plus additional particles (bakari, dake, nado, gurai, nara, shika, ya, jan, ze, zo, etc.) represent the project's strongest lexicographic work.

### Strengths

- **Structured `predicates_requiring` sections** list verbs and adjectives that take each particle, with examples -- this is invaluable for learners
- **`particle_contrasts` sections** provide side-by-side comparisons (ga vs. ha, ni vs. de, ni vs. he) with contrastive examples
- **`common_mistakes` sections** address specific learner errors with incorrect/correct pairs
- **`fixed_patterns` sections** list grammatical constructions using each particle
- **`information_structure` section** in `ha` (00079) explains the new/old information distinction -- a genuinely sophisticated linguistic point rarely covered in learner dictionaries
- **Example counts are generous** -- `ni` has 30 examples, `ga` has 15, `ha` has 10

### Areas for Improvement

- **Secondary particles are less thorough.** `bakari` (02006) has good examples but its notes lack the structured sections (PREDICATES REQUIRING, CONTRAST, COMMON MISTAKES) that core particles have. Same for `dake`, `nado`, `gurai`.
- **Sentence-ending particles** (`ne`, `yo`, `yone`, `ze`, `zo`, `jan`, `kashira`) have shorter treatments. These are important for understanding conversational register.
- **Some particle entries are missing from the core set.** The project notes 10 core particles with predicate lists, but particles like `to` (quotation/conditional) and `kara` (from/because) are multi-function and could benefit from the same exhaustive treatment as `ni`.
- **The `de` particle entry** (00502) is thorough but could add more emphasis on the compound function で as a te-form of だ, which causes frequent confusion.

### Recommendations for Particle Entries

1. Bring all secondary particles (bakari, dake, nado, gurai, nara, shika) up to the quality standard of the core particles -- add predicates_requiring, particle_contrasts, common_mistakes, and fixed_patterns sections.
2. Expand sentence-ending particle entries with more register and gender notes.
3. Ensure all particle entries have at least 5 examples per sense (several currently have only 3).

---

## 7. Proposed Improvements

The following proposals are organized as concrete prompts that can be given to Claude in single sessions (~10-15 minutes each). Each prompt includes the scope, methodology, and expected output.

### HIGH PRIORITY: Verb Transitivity and Aspect Notes

**Gap:** 1,891 verbs lack transitivity information; 2,393 verbs lack aspect/ている notes. These are the #1 and #2 HIGH PRIORITY items in the v2 standards.

**Prompt 1: Verb Transitivity Batch (Session 1 of ~10)**
```
Review the next 100 verb entries (by ID order) that lack "TRANSITIVITY" in their notes
field. For each verb:
1. Add TRANSITIVITY section with Type (自動詞/他動詞), Pair verb (if exists), and
   Pattern (Xが/Xを)
2. Add transitivity tag to metadata.tags if missing
3. If a pair verb exists in the dictionary, add a "pair" type cross_reference

Start from the first verb missing transitivity after ID 00001. Track which verb you
stopped at so the next session can continue.

Use the verb-entry skill for formatting. Do NOT add inline links.
Run validate.py when done.
```

*Repeat for ~10 sessions to cover all verbs. Each session handles ~100 verbs.*

**Prompt 2: Verb Aspect/ている Batch (Session 1 of ~10)**
```
Review the next 100 verb entries (by ID order) that lack "ている" in their notes field.
For each verb, add an ASPECT (ている) section explaining:
- Whether ている is progressive ("is doing"), resultative ("has done" / state), or both
- A brief example: [verb]ている = [meaning]
- Special cases (知る→知っている = "know", not "is learning")

Focus on verbs where the ている meaning is non-obvious or differs from what English
speakers would expect. Skip verbs where ている is straightforwardly progressive.

Start from ID [last stopping point]. Run validate.py when done.
```

### HIGH PRIORITY: Example Sentence Expansion

**Gap:** 1,401 basic/core entries need more examples (50% compliance). The polishing system has checked only through entry 01059.

**Prompt 3: Basic/Core Example Expansion (Session 1 of ~20)**
```
Find the next 25 basic or core tier entries (by ID order starting from 01059) that
have fewer than 5 examples per sense. For each entry:
1. Add examples to bring each sense up to 5 examples minimum
2. Ensure progressive length (short -> medium -> long)
3. For basic tier: examples 1-2 must use only basic-tier vocabulary; examples 3-5
   may use basic+core vocabulary
4. For core tier: examples 1-2 must use only basic+core vocabulary
5. Include at least one collocation example per sense

Follow the example-sentences skill. Do NOT add inline links.
Update the polishing/tasks/example-sentences/progress.txt with the last entry checked.
Run validate.py when done.
```

*Repeat for ~20 sessions. Each session adds examples to ~25 entries.*

### HIGH PRIORITY: Cross-Reference Expansion

**Gap:** 74% of entries have zero cross-references. This severely limits the dictionary's usefulness for distinguishing similar words.

**Prompt 4: Similar Word Cross-Reference Mining (Session 1 of ~5)**
```
Review all entries whose notes field contains "SIMILAR WORDS" or "SIMILAR EXPRESSIONS"
but whose cross_references array is empty. For each entry:
1. Extract the similar words mentioned in notes
2. Check if those words exist in the dictionary (use entries_index.json)
3. Add appropriate cross_references (type: "contrast" for confusable words,
   type: "synonym" for near-synonyms)
4. Ensure the referenced entry also gets a reciprocal cross_reference back

This is a mechanical-plus-semantic task: the notes already identify the similar words,
but judgment is needed to set the correct reference type and verify the relationships
are bidirectional.

Process entries in ID order. Run validate.py when done.
```

**Prompt 5: Homophone Cross-Reference Pass**
```
Using entries_index.json, identify all groups of entries that share the same reading
but have different headwords (homophones). For each homophone group:
1. Add "homophone" type cross_references between all members of the group
2. In the notes of each entry, add a brief disambiguation note if not already present

Focus on the most common/confusable homophones first (e.g., readings with 3+ entries
sharing the same reading). Currently only 5 homophone references exist in the entire
dictionary.

Process the top 50 homophone groups (by frequency). Run validate.py when done.
```

### MEDIUM PRIORITY: Counter Entry Enhancement

**Gap:** Counter entries lack full 1-10 counting tables and sound-change explanations.

**Prompt 6: Counter Entry Standardization**
```
Review all counter entries (approximately 50). For each counter entry:
1. If missing, add a full 1-10 counting table with readings
2. Highlight irregular readings (sound changes: gemination, voicing)
3. Add WHAT IT COUNTS / WHAT IT DOES NOT COUNT sections
4. Ensure at least 3 examples (5 for basic/core tier)
5. Add cross_references to related counters where applicable

Use the counter template from the other-entries skill. Model entry: 軒 (01993_ken)
for structure, but note it also needs expansion (missing readings 5-10).

Run validate.py when done.
```

### MEDIUM PRIORITY: Adjective Forms and Similar Words

**Gap:** Many adjective entries lack FORMS sections (adverbial, noun form) and SIMILAR WORDS distinctions.

**Prompt 7: Adjective Enhancement Pass (Session 1 of ~3)**
```
Review the next 50 adjective entries (by ID order) that lack "FORMS" in their notes.
For each:
1. Add FORMS section with adverbial form (〜く for i-adj, 〜に for na-adj) and noun
   form (〜さ) where natural
2. If the adjective has obvious semantic neighbors (大きい/広い, 嬉しい/楽しい,
   怖い/恐ろしい), add a SIMILAR WORDS section
3. Add "contrast" type cross_references for the similar words

Use the adjective-entry skill for formatting. Run validate.py when done.
```

### MEDIUM PRIORITY: Notes Consistency for Mid-Range Entries

**Gap:** Entries in the 02000-08000 range have the most variable quality.

**Prompt 8: Mid-Range Entry Notes Upgrade (Session 1 of ~10)**
```
Review the next 50 entries in the 02000-03000 range that have notes shorter than
300 characters. For each entry, upgrade the notes to v2 standards:

For verbs: Add TRANSITIVITY, ASPECT, COMMON PATTERNS sections
For nouns: Add COMMON EXPRESSIONS, scope notes where relevant
For adjectives: Add FORMS, SIMILAR WORDS sections
For adverbs: Add POSITION, MODIFIES, REGISTER sections

Use the vocabulary-notes skill for formatting. Prioritize entries in basic and core
tiers. Do NOT add inline links. Run validate.py when done.
```

### LOW PRIORITY: Particle Predicate List Expansion

**Prompt 9: Secondary Particle Enhancement**
```
Bring the following secondary particle entries up to core particle quality:
- ばかり (02006_bakari)
- だけ (03093_dake)
- など (03095_nado)
- ぐらい (02900_gurai)
- なら (09575_nara)
- しか (09959_shika)

For each, add:
1. predicates_requiring section (where applicable)
2. particle_contrasts section (e.g., だけ vs. しか vs. ばかり)
3. common_mistakes section
4. fixed_patterns section
5. Expand to 5+ examples per sense

Model these on the ga (00051) and ni (00314) entries. Run validate.py when done.
```

### LOW PRIORITY: Scope and Cultural Notes

**Prompt 10: Noun Scope Clarification Pass**
```
Review the following nouns where the Japanese semantic scope differs significantly
from the English translation. Add SCOPE NOTE sections:
- 手 (hand -- includes arm in Japanese)
- 顔 (face -- also means reputation/dignity)
- 足 (foot/leg -- includes both in Japanese)
- 首 (neck -- also means dismissal/firing)
- 頭 (head -- also means intelligence)
- 腹 (stomach -- also means feelings/intentions)
- 胸 (chest -- also means heart/feelings)
- 目 (eye -- also means experience/viewpoint)
- 口 (mouth -- also means opening/entrance)

For each, add:
1. SCOPE NOTE explaining the Japanese semantic range vs. English
2. Additional examples demonstrating the extended meanings
3. Cross-references to body-part entries

Run validate.py when done.
```

---

## 8. Priority Matrix

| Task | Priority | Sessions Needed | Entries Affected | Automated? |
|---|---|---|---|---|
| Verb transitivity notes | HIGH | ~10 | ~1,900 verbs | No (semantic) |
| Verb aspect/ている notes | HIGH | ~10 | ~2,400 verbs | No (semantic) |
| Example sentence expansion | HIGH | ~20 | ~1,400 entries | No (creative) |
| Cross-ref from notes mining | HIGH | ~5 | ~2,000 entries | Partially |
| Counter entry standardization | MEDIUM | ~1 | ~50 counters | No (semantic) |
| Adjective forms/similar words | MEDIUM | ~3 | ~400 adjectives | No (semantic) |
| Mid-range notes upgrade | MEDIUM | ~10 | ~4,000 entries | No (semantic) |
| Secondary particle enhancement | LOW | ~1 | ~6 particles | No (semantic) |
| Homophone cross-references | LOW | ~2 | ~200 entries | Partially |
| Noun scope clarification | LOW | ~1 | ~50 nouns | No (semantic) |

**Estimated total: ~63 sessions for full quality coverage**

---

## 9. Quality Metrics to Track

To monitor progress on these improvements, the project could track:

1. **Verb transitivity coverage**: % of verbs with TRANSITIVITY in notes (currently 39%)
2. **Verb aspect coverage**: % of verbs with ている info in notes (currently 23%)
3. **Example compliance rate**: % of entries meeting minimum example counts by tier (currently ~50% for basic/core)
4. **Cross-reference density**: Average cross_references per entry (currently 0.32)
5. **SIMILAR WORDS coverage**: % of entries with similar word notes (currently 20%)
6. **Polishing progress**: Tracking the "next" pointer in each polishing task

These metrics could be computed by a simple script run after each session, making quality trends visible over time.

---

## 10. Conclusion

The je-dict-1 project has built an impressive foundation with accurate definitions, natural examples, and comprehensive particle entries. The quality trajectory is clearly positive -- recent entries set a high standard that can be backported to earlier entries through systematic polishing. The most impactful improvements are:

1. **Verb transitivity/aspect notes** -- affects the largest number of entries, is the top priority in v2 standards, and requires genuine linguistic knowledge
2. **Example sentence expansion** -- essential for the basic/core tiers that are the dictionary's pedagogical backbone
3. **Cross-reference formalization** -- the notes already contain much of this knowledge; it needs to be structured into the cross_references array for UI navigation

All proposed improvements are sized for single Claude sessions and require semantic understanding -- they cannot be automated with scripts. This aligns with the project's core philosophy of handcrafted dictionary entries.
