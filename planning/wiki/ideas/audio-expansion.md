# Audio Coverage Expansion

**Last updated**: 2026-04-05

## Current state

Only ~1,028 of ~19,000 entries (~5%) have audio files. Audio is valuable for learners — hearing pronunciation reinforces reading and helps with pitch accent, which is not marked in the dictionary.

## Approaches to consider

### TTS (Text-to-Speech)
Modern Japanese TTS is high quality. Options:
- **Google Cloud TTS** — WaveNet voices for Japanese, natural-sounding
- **Amazon Polly** — Neural Japanese voice (Kazuha)
- **Azure Speech** — Multiple Japanese voices
- **Local models** — VOICEVOX (free, open-source, natural prosody)

Pros: Scalable, consistent, can cover all entries quickly
Cons: May have unnatural prosody on some words, licensing considerations

### Human recording
Pros: Most natural, includes pitch accent nuances
Cons: Expensive, slow, requires coordination with native speakers

### Hybrid approach
Generate TTS for all entries, then selectively replace with human recordings for common/tricky words.

## Implementation considerations

- File format: MP3 vs. OGG vs. both?
- Storage: Audio files add significant repository size — may need separate hosting
- Build integration: How to associate audio files with entries
- Progressive deployment: Start with basic + core tiers, expand to general

## Priority

Medium-low. The dictionary functions well without audio, but it would significantly improve the learning experience, especially for words with counterintuitive readings.

## Related pages

- [Project Overview](../project/overview.md)
- [Open Issues](../project/open-issues.md)
