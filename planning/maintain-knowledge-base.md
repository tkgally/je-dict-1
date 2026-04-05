# Knowledge Base Maintenance Session

Maintain and improve the project knowledge base at `planning/wiki/`. This prompt is designed for recurring sessions (nightly cron or manual invocation). Each session should leave the knowledge base richer, more accurate, and better connected.

## Session workflow

### 1. Orient yourself

Read the wiki index and recent log entries to understand current state:

```
planning/wiki/index.md     — page catalog and structure
planning/wiki/log.md       — what recent sessions did
```

Also read `PROJECT_STATUS.md` for the latest project changes — new entries, polishing progress, build system changes, etc. that may need to be reflected in the wiki.

### 2. Choose session activities

Each session should do **2-4 activities** from the list below. Vary the mix across sessions — don't do the same activities every night. Prioritize based on what seems most valuable given recent project changes.

#### A. Sync with project changes
- Check `PROJECT_STATUS.md` for recent changes not yet reflected in the wiki
- Update project pages (overview, architecture, pipeline, quality standards) if project practices have changed
- Update counts, statistics, and status information
- Check if new prompts, skills, or build scripts have been added that should be documented

#### B. Research and ingest
- Pick a topic relevant to the project and research it via web search
- Good research topics: lexicography methods, vocabulary acquisition studies, Japanese grammar analysis, dictionary UX patterns, corpus linguistics tools, SLA research, comparable dictionary projects
- Write findings as a new wiki page or integrate into an existing page
- Always cite sources (author, year, title) — don't fabricate references

#### C. Deepen existing pages
- Pick a wiki page that feels thin or superficial
- Add more detail, examples, or nuance
- Connect it more thoroughly to other pages (add cross-references)
- Add "implications for je-dict-1" sections where missing

#### D. Create new pages
- Identify topics mentioned in existing pages but lacking their own page
- Create pages for project concepts that aren't yet documented
- Add new idea pages for features or improvements worth considering
- Ensure new pages are added to `index.md`

#### E. Lint and maintain
- Check for broken cross-references (links to pages that don't exist)
- Look for contradictions between pages
- Identify orphan pages (not linked from index or other pages)
- Update "Last updated" dates on pages you modify
- Verify that project pages match current project reality (counts, processes, tools)

#### F. Analyze and synthesize
- Write comparison or analysis pages that synthesize information across multiple wiki pages
- Identify connections between research findings and project practices
- Document design decisions with reasoning (why je-dict-1 does X instead of Y)
- Create "lessons learned" content from project experience

#### G. Inform task prompts
- Review existing prompts in `prompts/` and check if wiki knowledge suggests improvements
- Note in `ideas/` pages where wiki research could inform new or revised prompts
- Document best practices discovered through research that should flow into entry creation guidelines
- (Do NOT modify prompts or skills directly — just document recommendations in the wiki)

### 3. Update the log

Append an entry to `planning/wiki/log.md` recording what you did:

```markdown
## [YYYY-MM-DD] maintenance | Brief description

**Session type**: Nightly maintenance (or: Manual session)

**Activities**:
- [A] Updated project/overview.md with new entry count
- [B] Researched pitch accent in Japanese learner dictionaries, created research/pitch-accent.md
- [E] Fixed 3 broken cross-references
```

### 4. Update the index

If you created new pages, add them to `planning/wiki/index.md` in the appropriate section.

### 5. Commit and merge

After completing your changes:

1. **Stage all wiki changes**: `git add planning/`
2. **Commit**: Use a descriptive message like "wiki: research pitch accent, update project stats, fix cross-refs"
3. **Push** to your branch
4. **Create PR, wait for CI, and squash-merge to main** following the standard end-of-session workflow in CLAUDE.md
5. **Post-merge cleanup**: switch to main, pull, delete feature branch

## Guidelines

### Quality over quantity
A single well-researched page is more valuable than three shallow ones. If a research topic is complex, it's fine to spend most of the session on it.

### Web research standards
- Use WebSearch and WebFetch to find real sources
- Cite authors, years, and titles — don't invent references
- Distinguish between well-established findings and speculative claims
- Note when information may be outdated

### Writing style
- Clear, direct prose — no filler
- Use tables for structured comparisons
- Use headers and bullet points for scannable content
- Always include "Related pages" links at the bottom
- Always include "Implications for je-dict-1" where relevant
- Update "Last updated" dates

### What not to do
- Don't modify dictionary entries, build scripts, or prompts — this is a knowledge-base-only session
- Don't fabricate research citations
- Don't create pages with only a title and placeholder text — write substantive content or don't create the page yet
- Don't duplicate information from CLAUDE.md or skills — instead, link to those and add analytical/contextual value

### Page template

```markdown
# Page Title

**Last updated**: YYYY-MM-DD

## Overview / Introduction

Brief description of what this page covers and why it matters.

## Main content

(Organized with clear headers)

## Implications for je-dict-1

How this information relates to or informs the dictionary project.

## Related pages

- [Page Name](relative/path.md) — brief description if not obvious
```
