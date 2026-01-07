# Dictionary Evaluation Specification

**Purpose**: This document provides specifications for Claude Code to conduct a multi-model LLM evaluation of the je-dict-1 Japanese-English Learner's Dictionary.

**Date Created**: 2026-01-07

---

## 1. Overview

### 1.1 Evaluation Goals

The primary purpose of this evaluation is to obtain useful guidelines and strategies for improving and enhancing the dictionary. This is NOT a comprehensive proofreading pass; rather, it seeks diverse perspectives from multiple LLMs to identify:

1. **Entry-level improvements** - Specific suggestions for individual entries
2. **Systematic improvements** - Patterns and missing categories of information that should be added across multiple entries
3. **Feature suggestions** - Content-focused features that would benefit learners

### 1.2 Key Constraints

- Do NOT inform evaluating models that entries were AI-generated
- Focus on content improvements only (not workflow or technical infrastructure)
- The evaluation should produce actionable, prioritized recommendations

---

## 2. Technical Setup

### 2.1 Environment Requirements

- Python 3.x
- OpenRouter API access (API key available as environment variable)
- Internet connectivity for API calls

### 2.2 OpenRouter Configuration

```python
# Configuration template
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Models to use (user will configure 2-3 models)
EVALUATION_MODELS = [
    # Examples - user will specify actual models:
    # "anthropic/claude-3.5-sonnet",
    # "openai/gpt-4-turbo",
    # "google/gemini-pro",
]
```

### 2.3 API Testing Protocol

Before running automated evaluation:

1. **Manual test each model** - Send a simple test prompt to verify API connectivity
2. **Test with sample entry** - Send one dictionary entry to verify the model can process and respond appropriately
3. **Verify response format** - Ensure responses are parseable and usable
4. **Only then proceed** to automated batch evaluation

### 2.4 Error Handling

- On API failure: Retry up to 3 times with exponential backoff (2s, 4s, 8s delays)
- On unparseable response: Retry up to 2 times with a clarified prompt
- After max retries: Log the failure and continue with remaining evaluations
- Save progress after each successful evaluation to enable resume on interruption

### 2.5 Progress Tracking

Maintain a progress file (`evaluation_progress.json`) with:
- Completed evaluations (model, round, entry IDs)
- Timestamp of last successful evaluation
- Any failures encountered
- Current round number

---

## 3. Entry Sampling Strategy

### 3.1 Sample Size

- **~30 entries per model per round**
- **Different models evaluate different subsets** (to maximize coverage and diverse perspectives)
- **4 rounds total** with refinement between rounds

### 3.2 Systematic Selection Criteria

Select entries to ensure coverage across:

#### By Part of Speech
| Category | Target Count per Sample | Examples |
|----------|------------------------|----------|
| Verbs (ichidan) | 4-5 | taberu, miru, ireru |
| Verbs (godan) | 4-5 | iku, nomu, aruku |
| Verbs (irregular) | 1-2 | suru, kuru |
| Nouns (concrete) | 4-5 | mizu, hon, eki |
| Nouns (abstract) | 2-3 | imi, kangae, keiken |
| I-adjectives | 3-4 | ookii, atarashii, samui |
| Na-adjectives | 2-3 | benri, shizuka, genki |
| Particles | 2-3 | ha, ga, ni, de |
| Adverbs | 2-3 | totemo, itsumo, yukkuri |
| Expressions | 1-2 | arigatou, sumimasen |
| Other (counters, etc.) | 2-3 | nin, mai, nichi |

#### By Complexity
- Simple entries (1 sense, brief notes): ~10 entries
- Medium entries (1-2 senses, moderate notes): ~12 entries
- Complex entries (multiple senses, detailed notes): ~8 entries

#### By Entry Length
- Shorter entries: ~10 entries
- Medium-length entries: ~12 entries
- Longer, more detailed entries: ~8 entries

### 3.3 Sample Generation Script

Create a script (`select_samples.py`) that:
1. Loads all entries from `entries/` directories
2. Categorizes entries by part of speech, complexity, and length
3. Generates non-overlapping samples for each model
4. Ensures each sample meets the distribution criteria above
5. Outputs sample lists as JSON files for each model

---

## 4. Evaluation Rounds

### 4.1 Round Structure (Graduated Context)

#### Round 1: Fresh Eyes (Minimal Context)
**Context provided**: Only basic framing
- "You are evaluating entries from a Japanese-English learner's dictionary"
- "The target users are intermediate learners who can read hiragana/katakana"
- No schema, no design philosophy, no project documentation

**Focus**: First impressions, intuitiveness, clarity

#### Round 2: Informed Critique (Partial Context)
**Context provided**: Add target user profile and entry schema
- Include the target user description from README
- Show the JSON schema structure
- Explain the furigana notation system

**Focus**: Alignment with stated goals, schema completeness

#### Round 3: Deep Analysis (Full Context)
**Context provided**: Complete project context
- Full README content (excluding technical build instructions)
- Project philosophy and quality standards
- Entry template and all field descriptions

**Focus**: Systematic patterns, missing information categories

#### Round 4: Synthesis and Recommendations
**Context provided**: Full context plus findings from previous rounds
- Summary of key themes from Rounds 1-3
- Request for prioritized, actionable recommendations

**Focus**: Consolidation, prioritization, concrete improvement tasks

### 4.2 Refinement Between Rounds

After each round:
1. Review responses from all models
2. Identify emerging themes and valuable lines of inquiry
3. Adjust prompts for next round to dig deeper into promising areas
4. Update sample selection if certain entry types need more attention

---

## 5. Evaluation Prompts

### 5.1 Core Evaluation Areas

Every round should solicit feedback on:

1. **Definition Quality**
   - Accuracy and completeness
   - Appropriate level of detail for learners
   - Balance between conciseness and thoroughness

2. **Example Sentences**
   - Naturalness and authenticity
   - Appropriateness for target level
   - Variety and usefulness for understanding usage

3. **Usage Notes**
   - Level of detail (too much? too little?)
   - Relevance to learner needs
   - Coverage of common mistakes and pitfalls

4. **Learner Appropriateness**
   - Suitability for intermediate learners
   - Clarity of explanations
   - Pedagogical effectiveness

5. **Systematic Patterns**
   - Missing categories of information
   - Inconsistencies across entries
   - Suggestions for entry type-specific improvements

6. **Feature Ideas**
   - Content-related features that would help learners
   - Information that should be added to entries
   - Ways to make entries more useful

### 5.2 Prompt Templates

#### Round 1 Prompt Template

```
You are evaluating entries from a Japanese-English learner's dictionary designed for intermediate learners of Japanese who can read hiragana and katakana fluently.

Please review the following dictionary entries and provide feedback on:

1. **Entry-Level Feedback**: For each entry, note any specific issues or suggestions regarding:
   - Clarity and accuracy of definitions
   - Naturalness of example sentences
   - Usefulness of any notes or explanations
   - Overall effectiveness for a learner

2. **General Observations**: After reviewing all entries, share:
   - Common strengths you noticed
   - Common weaknesses or areas for improvement
   - Any patterns that could be improved systematically
   - Features or information types that seem to be missing

3. **Prioritized Suggestions**: List your top 5-10 suggestions for improving these entries, in order of importance.

Here are the entries to evaluate:

[ENTRIES_JSON]
```

#### Round 2 Prompt Template

```
You are evaluating entries from a Japanese-English learner's dictionary.

**Target Users**: Intermediate learners of Japanese who:
- Can read hiragana and katakana fluently
- Know some kanji and are building vocabulary
- Want to deeply understand words, not just look them up quickly

**Entry Structure**: Each entry contains:
- headword: The word with furigana notation {kanji|reading}
- reading: Hiragana reading
- part_of_speech: Grammatical category
- gloss: Brief English equivalent
- definitions: Array of senses with explanations
- examples: Japanese sentences with English translations
- notes: Usage notes, grammar notes, cultural context
- cross_references: Links to related entries

**Furigana Notation**: {kanji|reading} indicates reading annotations, e.g., {食|た}べる shows た above 食.

Please evaluate these entries with particular attention to:

1. **Definition Quality**: Do explanations go beyond simple glosses? Are they helpful for understanding nuance?

2. **Example Effectiveness**: Are examples natural? Do they demonstrate typical usage patterns?

3. **Note Completeness**: Do notes cover what learners need to know? What's missing?

4. **Schema Utilization**: Are all fields being used effectively? Should any information be added?

5. **Systematic Improvements**: What patterns should change across all entries of similar types?

Here are the entries:

[ENTRIES_JSON]
```

#### Round 3 Prompt Template

```
You are conducting a deep analysis of entries from a Japanese-English learner's dictionary.

**Project Philosophy**: This dictionary prioritizes depth and quality over quantity. Each entry should provide:
- Explanatory definitions that go beyond simple glosses
- Natural example sentences optimized for learning
- Usage notes covering grammar, register, and common patterns
- Rich coverage of particles and grammar words crucial for learners

**Target Users**: Intermediate learners who want to deeply understand words, not just look them up quickly.

**Quality Standards**:
- Every entry should have 2-3 example sentences minimum
- Definitions should explain nuance, not just provide translations
- Notes should cover grammar patterns, common mistakes, and usage tips
- Particles deserve especially thorough explanations

[FULL_SCHEMA_DESCRIPTION]

Based on this context, please provide:

1. **Systematic Analysis**: What categories of information are missing that should be added to certain types of entries? (e.g., "verb entries should include X", "adjective entries would benefit from Y")

2. **Entry Type Recommendations**: For each major part of speech, what improvements would make entries more effective?

3. **Quality Gaps**: Where do entries fall short of the stated quality standards?

4. **Enhancement Ideas**: What content-based features would significantly help learners?

5. **Specific Entry Feedback**: Note any particular issues with individual entries.

Here are the entries:

[ENTRIES_JSON]
```

#### Round 4 Prompt Template

```
You are providing final recommendations for improving a Japanese-English learner's dictionary.

**Context**: [Include full project context]

**Findings from Previous Evaluation Rounds**:
[SUMMARY_OF_PREVIOUS_FINDINGS]

Based on all context and previous findings, please provide:

1. **Prioritized Improvement Tasks**: List specific, actionable improvements ranked by priority (High/Medium/Low). Format each as a concrete task, e.g., "Add conjugation examples to all verb entries" rather than "Consider adding conjugation information."

2. **Systematic Changes**: What changes should be applied across multiple entries? Group by entry type where relevant.

3. **New Information Categories**: What new fields or information types should be added to the entry schema?

4. **Feature Recommendations**: What content-based features would most benefit learners?

5. **Quality Guidelines**: What guidelines should be followed when creating or improving entries?

Please be specific and actionable. Each recommendation should be clear enough that someone could implement it without further clarification.

Here are additional entries for reference:

[ENTRIES_JSON]
```

---

## 6. Output Specifications

### 6.1 Intermediate Outputs

After each round, save:

```
evaluation_results/
├── round_1/
│   ├── model_1_responses.json
│   ├── model_2_responses.json
│   ├── round_1_summary.md
│   └── refinement_notes.md
├── round_2/
│   └── ...
├── round_3/
│   └── ...
└── round_4/
    └── ...
```

### 6.2 Final Consolidated Report

Create `evaluation_report.md` with:

1. **Executive Summary** - Key findings and top recommendations
2. **Methodology** - Models used, sampling approach, round structure
3. **Entry-Level Findings** - Specific issues found in evaluated entries
4. **Systematic Findings** - Patterns and themes across entries
5. **Feature Recommendations** - Suggested content enhancements
6. **Model Comparison** - Notable differences in feedback between models
7. **Raw Feedback Appendix** - Complete responses organized by round

### 6.3 Updated Project Specification

Create an updated `project_specification_v2.md` that incorporates evaluation findings:

1. **Enhanced Quality Standards** - Updated based on feedback
2. **Entry Type Guidelines** - Specific guidance for each part of speech
3. **Required Information Categories** - New fields or information to add
4. **Prioritized Task List** - Concrete improvements with priority levels:
   - **High Priority**: Should be addressed before adding new entries
   - **Medium Priority**: Should be addressed during next enhancement pass
   - **Low Priority**: Nice-to-have improvements for future consideration
5. **Content Feature Roadmap** - Suggested features for future implementation

---

## 7. Execution Workflow

### 7.1 Pre-Execution Checklist

1. [ ] Verify OpenRouter API key is set in environment
2. [ ] Configure EVALUATION_MODELS list with desired models
3. [ ] Run API connectivity tests for each model
4. [ ] Generate sample entry sets for each model
5. [ ] Create output directories

### 7.2 Execution Steps

```
For each round (1-4):
    For each model:
        1. Load appropriate prompt template
        2. Insert context based on round number
        3. Load entry sample for this model
        4. Send evaluation request to model
        5. Parse and save response
        6. Update progress tracker

    After all models complete:
        1. Generate round summary
        2. Review findings and create refinement notes
        3. Adjust prompts/samples for next round if needed
        4. Prompt operator to review before proceeding

After all rounds:
    1. Generate consolidated report
    2. Generate updated project specification
    3. Save all outputs
```

### 7.3 Manual Intervention Points

The script should pause and request human review:
- After Round 1 (to refine approach based on initial findings)
- After Round 2 (to adjust focus for deep analysis)
- After Round 3 (to prepare synthesis prompts)
- Before finalizing outputs (to verify quality)

---

## 8. File Structure

After execution, the repository should contain:

```
je-dict-1/
├── evaluation_spec.md          # This file
├── evaluation/                  # New directory for evaluation artifacts
│   ├── scripts/
│   │   ├── select_samples.py
│   │   ├── run_evaluation.py
│   │   └── generate_report.py
│   ├── samples/
│   │   ├── model_1_samples.json
│   │   ├── model_2_samples.json
│   │   └── ...
│   ├── results/
│   │   ├── round_1/
│   │   ├── round_2/
│   │   ├── round_3/
│   │   └── round_4/
│   ├── evaluation_progress.json
│   ├── evaluation_report.md     # Final consolidated report
│   └── project_specification_v2.md  # Updated specification
└── ... (existing files)
```

---

## 9. Success Criteria

The evaluation is successful if it produces:

1. **Actionable Recommendations**: At least 20 specific, implementable improvement tasks
2. **Systematic Insights**: Identification of at least 5 patterns or missing information categories
3. **Priority Ranking**: All recommendations clearly prioritized as High/Medium/Low
4. **Feature Ideas**: At least 5 content-focused feature suggestions
5. **Updated Specification**: A comprehensive project_specification_v2.md ready to guide future development

---

## 10. Notes for Claude Code

### 10.1 Key Reminders

- Test all API calls manually before automating
- Save progress frequently to enable resume on failure
- Do NOT mention that entries are AI-generated in prompts
- Focus evaluation on content, not technical infrastructure
- Pause for human review at designated intervention points

### 10.2 Response Processing

When processing model responses:
- Extract specific entry feedback and tag with entry IDs
- Identify and categorize systematic recommendations
- Note any disagreements between models (valuable signal)
- Flag any responses that seem off-topic or unhelpful

### 10.3 Quality Checks

Before finalizing outputs:
- Verify all recommendations are actionable (not vague)
- Ensure priority levels are assigned consistently
- Check that systematic recommendations apply to multiple entries
- Confirm feature suggestions are content-focused (not UI-focused)

---

## Appendix A: Entry Schema Reference

```json
{
  "id": "string (format: {romaji}_{5-digit-number})",
  "headword": "string (with furigana: {kanji|reading})",
  "reading": "string (hiragana only)",
  "part_of_speech": "string",
  "gloss": "string (brief English equivalent)",
  "definitions": [
    {
      "sense_number": "integer",
      "gloss": "string",
      "explanation": "string (detailed explanation)"
    }
  ],
  "examples": [
    {
      "japanese": "string (with furigana)",
      "english": "string",
      "notes": "string or null"
    }
  ],
  "notes": "string (usage notes, grammar, cultural context)",
  "cross_references": ["array of entry IDs"],
  "metadata": {
    "created": "ISO 8601 timestamp",
    "modified": "ISO 8601 timestamp",
    "ai_model": "string",
    "confidence": "high|medium|low",
    "review_status": "verified|draft",
    "jlpt_level": "N5|N4|N3|N2|N1|null",
    "frequency_rank": "integer or null"
  }
}
```

---

## Appendix B: Part of Speech Categories

For sampling and analysis, use these categories:

| Category | part_of_speech values |
|----------|----------------------|
| Verb (ichidan) | "verb (ichidan)" |
| Verb (godan) | "verb (godan)" |
| Verb (irregular) | "verb (irregular)" |
| Noun | "noun" |
| I-adjective | "adjective (i-adjective)" |
| Na-adjective | "adjective (na-adjective)" |
| Particle | "particle" |
| Adverb | "adverb" |
| Counter | "counter" |
| Expression | "expression", "interjection" |
| Conjunction | "conjunction" |
| Pronoun | "pronoun" |
| Other | any other value |

---

## Appendix C: Sample Entry for Reference

```json
{
  "id": "iku_00001",
  "headword": "{行|い}く",
  "reading": "いく",
  "part_of_speech": "verb (godan)",
  "gloss": "to go",
  "definitions": [
    {
      "sense_number": 1,
      "gloss": "to go, to move (toward a destination)",
      "explanation": "Expresses movement away from the speaker's current location toward a destination. The opposite of {来|く}る (to come). Used when the speaker is not at the destination."
    },
    {
      "sense_number": 2,
      "gloss": "to proceed, to continue",
      "explanation": "When attached to the te-form of another verb (〜ていく), indicates an action continuing into the future or moving away from the speaker's perspective."
    }
  ],
  "examples": [
    {
      "japanese": "{学校|がっこう}に{行|い}きます。",
      "english": "I go to school.",
      "notes": null
    },
    {
      "japanese": "{明日|あした}、{東京|とうきょう}に{行|い}く{予定|よてい}です。",
      "english": "I plan to go to Tokyo tomorrow.",
      "notes": null
    },
    {
      "japanese": "これから{暑|あつ}くなっていく。",
      "english": "It will get hotter from now on.",
      "notes": "〜ていく expressing change continuing into the future"
    }
  ],
  "notes": "{行|い}く has an irregular te-form: {行|い}って, not {行|い}いて. This is one of the most common verbs in Japanese. The kanji can also be read as ゆく in literary or formal contexts, though いく is standard in modern Japanese.",
  "cross_references": [],
  "metadata": {
    "created": "2026-01-05T10:00:00Z",
    "modified": "2026-01-06T22:15:00Z",
    "ai_model": "claude-opus-4-5",
    "confidence": "high",
    "review_status": "verified",
    "jlpt_level": "N5",
    "frequency_rank": null
  }
}
```
