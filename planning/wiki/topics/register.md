# Register and Formality

**Last updated**: 2026-04-05

## Why register matters

Japanese has one of the most elaborate register systems of any major language. The same concept can be expressed at multiple formality levels, and using the wrong register is a significant social error — more so than in English. For intermediate learners, understanding register is critical for natural communication.

## Register levels in je-dict-1

The project uses these informal register labels in entry notes:

| Label | Description | Example |
|-------|------------|---------|
| Very casual | Slang, close friends, potentially rude in other contexts | めっちゃ, やばい, うざい |
| Casual | Friends, family, informal situations | 食べる, すごい, ちょっと |
| Neutral | Default register, appropriate in most situations | 食べます, 少し |
| Formal | Business, official documents, polite interaction | 召し上がる, いただく |
| Written/literary | Newspapers, academic writing, formal documents | における, に関して |
| Archaic | Historical texts, set phrases, proverbs | なり, たり |

## Implementation status

Register marking is a **medium priority** v2 quality standard. Current coverage is inconsistent:
- Some entries have register notes in the notes field
- No standardized tag system for register (it's in free-text notes, not structured metadata)
- Many entries lack any register indication

## Design questions

### Should register be a structured field?
Currently register information lives in the notes field as prose. A structured field (e.g., `"register": "formal"`) would enable:
- Filtering by register in search
- Consistent display
- Easier validation

But register is often nuanced — a word might be "casual when used as an exclamation, neutral when used as an adjective." A single tag may oversimplify.

### Keigo handling
Japanese honorific language (敬語) has three main types:
- **尊敬語** (sonkeigo) — elevates the subject's actions
- **謙譲語** (kenjougo) — humbles the speaker's actions
- **丁寧語** (teineigo) — general politeness (です/ます)

Should keigo forms be separate entries, or documented within the base verb's entry? Current practice: separate entries with cross-references for forms that are distinct words (e.g., 召し上がる), notes within the base entry for regular conjugational keigo (e.g., お〜になる pattern).

## Related pages

- [Quality Standards](../project/quality-standards.md)
- [Translation Equivalence](../research/translation-equivalence.md)
