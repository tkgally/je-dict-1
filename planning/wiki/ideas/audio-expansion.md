# Audio Coverage Expansion

**Last updated**: 2026-04-05

## Current state

The dictionary currently has no audio files. An earlier experiment with human-recorded audio for ~1,028 entries was discontinued in early 2026 (the files were removed from the repository). Audio remains valuable for learners — hearing pronunciation reinforces reading and helps with pitch accent, which is not marked in the dictionary. Any future audio effort will likely be TTS-based rather than human-recorded.

## TTS landscape (as of 2026)

The Japanese TTS field has advanced dramatically. Several viable options exist:

### Cloud services

| Service | Japanese quality | Cost | Notes |
|---------|-----------------|------|-------|
| **Google Cloud TTS** | High (WaveNet/Neural2) | $4-16 per 1M characters | Strong Asian language support; Studio voices available |
| **Microsoft Azure** | High (Neural) | $4-16 per 1M characters | 446+ voices across 144 languages; custom voice training available |
| **Amazon Polly** | Good (Neural) | $4 per 1M characters | NTTS Japanese voice; reliable at scale |
| **ElevenLabs** | Very high | $5-22/month (tiered) | Best-in-class naturalness; voice cloning possible |

For ~22,200 entries averaging ~10 characters per headword, total character count would be ~220K — well within free tiers for a one-time generation.

### Open-source / local models

| Model | Japanese quality | License | Notes |
|-------|-----------------|---------|-------|
| **VOICEVOX** | Very good | Free/open-source | Japanese-native; anime-style voices but natural prosody; offline; accurate kanji reading; emotional expression control |
| **Qwen3-TTS** (Alibaba, Jan 2026) | Very good | Apache 2.0 | 10 languages including Japanese; 1.7B model for quality, 0.6B for speed; voice cloning and design; runs locally on consumer hardware |
| **Voxtral** (Mistral) | Good | Open weights | Multilingual; newer but less Japanese-specific |

### Recommendation for je-dict-1

**VOICEVOX** is the strongest candidate for a first pass:
- Free and open-source with permissive licensing
- Designed specifically for Japanese, with accurate kanji reading
- Runs offline (no API costs, no rate limits)
- Multiple voice characters available
- An Anki integration already exists (showing the Anki/Japanese-learning community trusts it)
- Generates audio that Japanese learners are already familiar with

**Qwen3-TTS** is a strong alternative if a more "natural" (non-character) voice is preferred, or for future multilingual expansion.

VOICEVOX for bulk generation would be the simplest path to full coverage at no cost.

## Implementation plan

### Phase 1: Headword audio (lowest effort, highest impact)
- Generate pronunciation audio for each entry's headword
- One audio file per entry: the word spoken in isolation
- Priority order: basic tier → core tier → general tier
- Estimated: ~22,200 files, each <5 seconds

### Phase 2: Example sentence audio (higher effort, high value)
- Generate audio for example sentences
- Start with the first (simplest) example per entry
- Estimated: ~22,200+ files at 5-15 seconds each

### Phase 3: Selective human re-recording
- Replace TTS with human recordings for:
  - Basic tier entries (most looked-up)
  - Words with counterintuitive readings
  - Words where pitch accent significantly changes meaning
  - Any entries where TTS quality is inadequate

### Technical considerations

**File format**: MP3 at 128kbps is the pragmatic choice — universally supported, small files (~50KB per headword clip). OGG could save ~30% but has browser compatibility concerns.

**Storage**: 22,200 MP3 headword files at ~50KB each ≈ 1.1GB. This is too large for the Git repository. Options:
- **Git LFS** — keeps files in Git workflow but uses external storage
- **Separate CDN/bucket** — S3, Cloudflare R2, or GitHub Releases
- **GitHub Pages submodule** — separate repo for audio assets
- **Build-time download** — audio fetched during build, not stored in repo

**Build integration**: 
- Add `has_audio: true` field to entry JSON (already exists in examples)
- Build script generates `<audio>` element on entry pages
- Lazy-load audio to avoid slowing page loads

**Filename convention**: `{entry_id}_headword.mp3` (e.g., `00645_ko.mp3`)

### Quality assurance

TTS-generated audio should be spot-checked for:
- Correct reading selection (important for homographs like 生)
- Natural pitch accent
- Appropriate speed (not too fast for learners)
- No artifacts or truncation

A validation script could cross-reference audio files against the entry index to ensure coverage and detect missing/orphan files.

## Cost estimate

| Approach | One-time cost | Ongoing cost |
|----------|--------------|--------------|
| VOICEVOX (local) | $0 (compute time only) | $0 per new entry |
| Google Cloud TTS | ~$1-4 (within free tier) | Negligible |
| Human recording (full) | $2,000-5,000+ | Per new entry |
| Hybrid (TTS + selective human) | $0-4 + selective human | Minimal |

## Priority

Medium. The dictionary functions well without audio, but pronunciation support would significantly improve the learning experience, especially for:
- Words with counterintuitive readings (e.g., 今日, 大人)
- Counter sound changes (いっぽん, さんびき)
- Words where pitch accent distinguishes meaning
- Learners who primarily study by listening

The availability of free, high-quality Japanese TTS makes this more feasible than it was even a year ago.

## Related pages

- [Project Overview](../project/overview.md)
- [Open Issues](../project/open-issues.md)
- [Pitch Accent](../research/pitch-accent.md) — pitch accent notation and learner implications
- [Japanese Counters and Classifiers](../research/counters-classifiers.md) — sound changes make audio especially valuable for counters
- [Digital Dictionary UX](../research/digital-dictionary-ux.md) — user behavior and interface design
