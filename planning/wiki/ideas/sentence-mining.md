# Sentence Mining Integration

**Last updated**: 2026-04-05

## Concept

"Sentence mining" is a popular vocabulary acquisition technique where learners collect example sentences containing target words and add them to spaced repetition systems (SRS) like Anki. je-dict-1's rich example sentences could support this workflow.

## Possible features

### Anki export
- Button on each entry page to export examples as Anki cards
- Front: Japanese sentence (with or without furigana). Back: English translation + word definition.
- Bulk export for word lists

### API endpoint
- JSON endpoint returning entry data for programmatic access
- Would allow third-party Anki add-ons to pull from je-dict-1
- Challenge: the site is fully static — would need a separate API or pre-generated JSON files

### Sentence difficulty scoring
- Rate sentences by vocabulary complexity using tier data
- Help learners pick sentences at their level
- "i+1" filtering: sentences where only the target word is unknown

## Technical considerations

- Static site limitation: no server-side processing, so everything must be pre-generated or client-side
- Could generate downloadable Anki decks as build artifacts
- Privacy: no tracking of user vocabulary knowledge (no accounts)

## Priority

Low. Interesting for power users but adds significant complexity. The dictionary's primary value is as a reference, not a study tool.

## Related pages

- [Vocabulary Acquisition](../research/vocabulary-acquisition.md)
- [Digital Dictionary UX](../research/digital-dictionary-ux.md)
