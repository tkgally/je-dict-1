# Project Overview

**Last updated**: 2026-06-15

## What je-dict-1 is

je-dict-1 is a Japanese-English learner's dictionary hosted as a static website at [tkgje.jp](https://www.tkgje.jp/). It targets intermediate learners of Japanese — people who can read kana and are actively building vocabulary. As of June 2026, it contains over 29,000 entries with over 114,000 example sentences and over 16,400 cross-references.

The dictionary is entirely static: HTML, CSS, and JavaScript generated from JSON source files by a Python build pipeline, deployed via GitHub Pages. There is no server, no database, and no user accounts.

## What makes it distinctive

### LLM-built and maintained

This is not a traditional dictionary compiled by human lexicographers over years. The entries are created by LLMs (primarily Claude) working from candidate word lists, with human oversight on quality standards and editorial direction. This enables rapid expansion — dozens of entries per session — while maintaining consistent quality through automated validation and schema enforcement.

### Three-tier vocabulary system

Rather than using JLPT levels (which are exam-oriented and have well-known problems), je-dict-1 uses an original three-tier classification:

- **Basic** (801 entries) — foundational words needed for survival communication. Closed tier.
- **Core** (~1,982 entries) — essential vocabulary for adult communication. Closed tier.
- **General** (26,000+ entries, growing) — everything else. All new entries go here. There is no maximum size for the dictionary. (Current count: 26,761 tagged `general`, plus 20 newly-created entries — 29181–29200, a 2026-06-12 batch — pending a `vocabulary_tier` backfill [see [Cleanup Backlog](../ideas/cleanup-backlog.md#priority-23)], of 29,564 total as of 2026-07-11.)

See [Vocabulary Tier System](vocabulary-tiers.md) for details.

### Rich entry structure

Each entry goes beyond simple word-translation pairs. Entries include:
- Multiple senses with numbered definitions
- 3+ example sentences per sense, progressively longer
- Structured notes with collocations, similar-word distinctions, register labels
- Cross-references to related entries
- Full conjugation tables for verbs and i-adjectives
- Furigana on all kanji in all fields

### Automated quality pipeline

A suite of Python tools validates entries against a JSON schema, checks furigana coverage, generates conjugation tables, detects duplicates, and builds the static site. GitHub Actions CI runs validation on every push.

## Who it's for

The primary audience is English-speaking learners of Japanese at the intermediate level — roughly JLPT N3-N2 equivalent. These learners:
- Can read hiragana and katakana fluently
- Are learning kanji but benefit from furigana
- Need English explanations but can process Japanese example sentences
- Want to understand nuance, register, and usage patterns, not just translations

## Project history

The dictionary has been in active development through multiple phases, currently in Phase 6 (Continued Expansion & Polish). The project uses a candidate word system where potential entries are queued in `candidate_words.json` and then created in batch sessions.

## Related pages

- [Architecture and Build System](architecture.md)
- [Entry Design](entry-design.md)
- [Quality Standards](quality-standards.md)
- [Content Pipeline](content-pipeline.md)
