# Enhancement: Expository Articles Pilot

**Enhancement plan section**: [1.3.3] Expository Articles

## What This Prompt Creates/Modifies

| Artifact | Action |
|----------|--------|
| `build/article_schema.json` | **Create** — JSON schema for article files |
| `articles/` | **Create** — directory for article source files |
| `articles/counters.json` | **Create** — pilot article: counters/classifiers |
| `articles/keigo.json` | **Create** — pilot article: basic keigo system |
| `articles/onomatopoeia.json` | **Create** — pilot article: common onomatopoeia |
| `build/build_flat.py` | **Modify** — add article rendering |
| `build/entry_renderer.py` | **Modify** — add article-to-entry links |
| `build/templates/` | **Modify** — add article page template/styles |
| `docs/articles/` | **Create** — generated article pages |
| `CLAUDE.md` | **Modify** — document article system |

## Overview

Some topics — counters, keigo, onomatopoeia families — deserve standalone treatment beyond what fits in individual entry notes. This prompt creates a lightweight article system and three pilot articles to evaluate the concept.

## Implementation Steps

### Part A: Design the Article Schema

Create `build/article_schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["id", "title", "body", "metadata"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9-]*$"
    },
    "title": {
      "type": "object",
      "required": ["english", "japanese"],
      "properties": {
        "english": { "type": "string" },
        "japanese": { "type": "string" }
      }
    },
    "body": {
      "type": "string",
      "description": "Markdown content with furigana support"
    },
    "related_entries": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["entry_id", "headword"],
        "properties": {
          "entry_id": { "type": "string" },
          "headword": { "type": "string" },
          "note": { "type": "string" }
        }
      }
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" }
    },
    "metadata": {
      "type": "object",
      "required": ["created", "modified", "author"],
      "properties": {
        "created": { "type": "string", "format": "date-time" },
        "modified": { "type": "string", "format": "date-time" },
        "author": { "type": "string" }
      }
    }
  }
}
```

Design principles:
- Lighter than entry schema — no senses, examples, conjugations
- Body is markdown with `{漢字|かんじ}` furigana support (same as entry notes)
- `related_entries` links to dictionary entries for cross-navigation
- All kanji in body must have furigana (same rule as entries)

### Part B: Write Three Pilot Articles

Create `articles/` directory and write three articles:

#### 1. `articles/counters.json` — Japanese Counters and Classifiers
Content should cover:
- What counters are and why they matter
- The universal counter (つ) and when to use it
- Common counters by category: people (人), flat things (枚), long things (本), small things (個), machines (台), books (冊), animals (匹/頭), buildings (軒), etc.
- Sound change rules (1本→いっぽん, 3杯→さんばい, etc.)
- Link to all counter entries in the dictionary via `related_entries`

#### 2. `articles/keigo.json` — Basic Keigo System
Content should cover:
- Three types: 尊敬語 (respectful), 謙譲語 (humble), 丁寧語 (polite)
- Common verb transformations (table format)
- When to use each type (social context)
- Common mistakes
- Link to keigo-related entries via `related_entries`

#### 3. `articles/onomatopoeia.json` — Common Onomatopoeia Groups
Content should cover:
- What onomatopoeia/mimetic words are in Japanese (擬音語, 擬態語)
- Major groups: rain sounds, emotional states, textures, movement, eating/drinking
- Usage patterns (〜と, 〜する, adverbial use)
- Link to onomatopoeia entries via `related_entries`

For each article:
- Use `python3 build/get_timestamp.py` for created/modified timestamps
- All kanji must have furigana
- Look up related entry IDs with `python3 build/check_duplicate.py`
- Content should be 500-1000 words, written for intermediate learners
- All explanatory text in English; Japanese for examples only

### Part C: Build System Integration

#### Modify `build/build_flat.py`:
1. Add article discovery — scan `articles/*.json` for article files
2. Add article validation — validate against `build/article_schema.json`
3. Add article page generation — render each article to `docs/articles/{id}.html`
4. Add article index page — `docs/articles/index.html` listing all articles

#### Article page template:
- Match existing entry page styling
- Title (English + Japanese)
- Rendered markdown body (with furigana rendering)
- "Related Entries" sidebar/section linking to dictionary entries
- Navigation back to article index

#### Modify `build/entry_renderer.py`:
- For entries that appear in an article's `related_entries`, add an "See also: [Article Title]" link on the entry page
- This creates bidirectional navigation: article → entries and entry → article

### Part D: Add Article Navigation

Add an "Articles" link to the site navigation (alongside Browse, Search, Recent, etc.):
1. Read the existing navigation template in `build/templates/` or `build/page_generators.py`
2. Add "Articles" navigation item pointing to `docs/articles/index.html`

### Part E: Validation

```bash
# Validate articles against schema
python3 -c "
import json, jsonschema
with open('build/article_schema.json') as f:
    schema = json.load(f)
import glob
for path in glob.glob('articles/*.json'):
    with open(path) as f:
        data = json.load(f)
    jsonschema.validate(data, schema)
    print(f'OK: {path}')
"

# Full build to generate article pages
make build

# Verify article pages exist
ls docs/articles/
```

### Part F: Evaluate the Pilot

After building, briefly assess:
1. Do the article pages render correctly?
2. Do entry→article and article→entry links work?
3. Does the Articles navigation item appear?
4. Note any issues for future improvement in the commit message

### Part G: Documentation

Update CLAUDE.md:
- Add `articles/` to the project structure section
- Add article schema to build system documentation
- Note that articles are a pilot feature

## PR and Merge Workflow

Follow the complete workflow described in CLAUDE.md:

1. **Run `make build`** to generate all pages including articles
2. **Commit ALL changes** including build artifacts:
   ```bash
   git add -A && git commit -m "Add expository articles pilot: counters, keigo, onomatopoeia

   Creates article schema, three pilot articles, and build system
   integration. Articles link bidirectionally with dictionary entries.
   Enhancement plan [1.3.3]."
   ```
3. **Push** to the feature branch
4. **Create PR** with description of what was added
5. **Poll CI** every 60 seconds (up to 10 minutes)
6. **Squash-merge** once CI is green
7. **If CI fails**: read logs, fix, push, repeat
8. **Post-merge cleanup**: switch to main, pull, verify clean, delete feature branch locally and remotely
