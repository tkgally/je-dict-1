# Knowledge Base Maintenance Session

Maintain and improve the project knowledge base at `planning/wiki/`. This prompt is designed for recurring sessions (nightly cron or manual invocation). Each session should leave the knowledge base richer, more accurate, and better connected.

## Pre-flight: sweep stranded PRs

**Run this as the first step of every session, before reading the wiki or any other project files.**

```bash
python3 pipeline/sweep-stranded-prs.py
```

The script lists open PRs on `claude/*` branches and closes any whose maximum entry ID is strictly less than `polishing/tasks/comprehensive/progress.txt`'s `next:` value on main. It also deletes the head branch via the GitHub API. It will never close a wiki-only PR by accident — wiki PRs touch no entry files, and the script skips PRs that don't touch entries at all. Calling it here makes the wiki Routine help clean up after stranded comprehensive-polish runs in addition to its primary work.

The script is idempotent and safe to run any time during the session, but running it first ensures the cleanup happens even if the rest of the session bails out.

## Per-session budget

This prompt is run unattended on a schedule. Plan the session so the wrap-up phase has enough context to complete reliably.

- **Target: keep doing wiki work until you've used roughly 60% of your context window**, then start wrapping up. The wrap-up phase (commit, push, PR creation, up-to-10-minute CI wait via Monitor, merge call) needs ~40% headroom.
- **Quality over quantity**: a single well-researched page is more valuable than three shallow ones (this is also restated under "Guidelines" below).
- **Stop earlier than 60% if** tool outputs are getting truncated, you've fetched several large web pages for research, or you're partway through a large page rewrite that would make the diff unwieldy.
- **Take stock periodically**: after each activity from step 3, check how full context feels and decide whether to start another activity or wrap up.

## Session workflow

### 1. Orient yourself

Read the wiki index and recent log entries to understand current state:

```
planning/wiki/index.md     — page catalog and structure
planning/wiki/log.md       — what recent sessions did
```

Also read `PROJECT_STATUS.md` for the latest project changes — new entries, polishing progress, build system changes, etc. that may need to be reflected in the wiki.

**Catch-up context**: The 16-item Enhancement Plan 2026 (`enhancement/enhancement-plan-2026-04-09.md`, tracked in `enhancement/tracking.md`) was completed in April 2026. That plan shipped the task queue, orchestrator, multi-model review pipeline, consistency checker, semantic fields/scenarios, priority polishing, and expository articles. When reflecting changes into the wiki, `topics/enhancement-plan-retrospective.md` is the best single entry point — it summarizes what was built, which wiki hypotheses were validated, and which targets remain unmet. `build/report.py` is the authoritative source for current counts.

### 2. Harvest comprehensive-polish observations

Read `polishing/observations.md`. Comprehensive-polish sessions append tagged notes there during their normal work — these are the closest the project has to a "user-supplied" research backlog.

For each unprocessed observation:

- `[wiki]` or `[wiki:page-name]` → integrate into the wiki (existing page or new) per the activities below
- `[article]` → add to `planning/wiki/ideas/articles.md` (create if missing) for future expository article work
- `[pattern]` → consider whether the pattern merits a dedicated wiki page or a note on an existing project-practices page; if it suggests concrete cleanup work, add to `planning/wiki/ideas/cleanup-backlog.md`
- `[tooling]` → add to `planning/wiki/ideas/tooling-backlog.md`
- `[skill]` → flag in your session log; do **not** modify skills from this session (knowledge-base only) — but record the recommendation
- `[entry]` → add to `planning/wiki/ideas/entry-followups.md` so a future polishing session can pick it up

After processing each observation (whether by acting on it or filing it into a backlog page), remove it from `polishing/observations.md`. Leave any observations you couldn't classify with a brief note appended explaining why.

This harvest counts as one of the session's activities (effectively activity F: Analyze and synthesize).

### 3. Choose additional session activities

Each session should do **2-4 activities** from the list below in addition to the harvest. Vary the mix across sessions — don't do the same activities every night. Prioritize based on what seems most valuable given recent project changes.

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

### 4. Update the log

Append an entry to `planning/wiki/log.md` recording what you did:

```markdown
## [YYYY-MM-DD] maintenance | Brief description

**Session type**: Nightly maintenance (or: Manual session)

**Activities**:
- [A] Updated project/overview.md with new entry count
- [B] Researched pitch accent in Japanese learner dictionaries, created research/pitch-accent.md
- [E] Fixed 3 broken cross-references
```

### 5. Update the index

If you created new pages, add them to `planning/wiki/index.md` in the appropriate section.

### 6. Commit and merge

After completing your changes, follow the end-of-session workflow in CLAUDE.md → "End-of-session PR and merge workflow." For Routine and any unattended session, use the **MCP path** — the `gh` CLI is not authorized in those environments.

1. **Stage wiki and observations changes**: `git add planning/ polishing/observations.md`. Wiki edits are markdown only and do **not** require `make build`.
2. **Commit and push** to your branch with a descriptive message like "wiki: harvest observations, research pitch accent, update project stats".
3. **Create the PR** with `mcp__github__create_pull_request` (`owner: "tkgally"`, `repo: "je-dict-1"`, `head: "<your branch>"`, `base: "main"`, plus a title and body). Note the PR number.
4. **Wait for CI** by running `pipeline/wait-for-pr-checks.sh <pr_number>` via the `Monitor` tool. Exit codes: 0 = all green, 1 = a check failed, 2 = timeout (default 10 min), 3 = auth/API error, 4 = no checks ever appeared.
5. **Merge based on the exit code**:
   - **Exit 0**: call `mcp__github__merge_pull_request` with `merge_method: "squash"`. The session is done.
   - **Any non-zero exit**: leave the PR open, add a one-line note to your session log explaining what the helper reported, and stop. The next Routine session's pre-flight `pipeline/sweep-stranded-prs.py` call will not auto-close this one (it doesn't touch entries), so the curator should look at it on the next pass.
6. **Do not** `git checkout main`, **do not** delete the feature branch from inside this session — the session is on that branch. The repo's "Automatically delete head branches" setting handles remote cleanup once the merge fires.

Do **not** call `mcp__github__enable_pr_auto_merge` from a Routine — it usually fails because the PR is in `unstable` state immediately after creation.

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
- Don't modify dictionary entries, build scripts, or prompts — this is a knowledge-base-only session. (The exception is removing harvested entries from `polishing/observations.md`, which is part of step 2.)
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
