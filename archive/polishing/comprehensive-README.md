# Comprehensive Polish

The default ongoing-improvement task for je-dict-1. Each session works through 20–30 entries (targeting roughly 70% context use), applying a tiered checklist that covers everything from schema validity to **full inline link coverage on every Japanese word in both examples and notes** to note quality, and logs longer-term observations for follow-up.

See `prompts/comprehensive_polish.md` for the full instructions and `.claude/skills/polish-entries/SKILL.md` for the underlying quality standards.

## Files

- `progress.txt` — `next:` pointer; advances entry-by-entry.
- The session log lives at `polishing/sessions/comprehensive_{YYYY-MM-DD}_{NNN}.md`.
- Long-term observations go to `polishing/observations.md` (one shared, append-only file).

## Relationship to targeted polish tasks

The comprehensive task subsumes the work done by the targeted `polish_*` prompts
(furigana, examples, inline links, cross-references, semantic labels,
transitivity, aspect, expand-short-notes). The targeted prompts remain
available for special-purpose sweeps (e.g., a focused furigana correctness pass
after a multi-model review), but `comprehensive_polish.md` is the default.
