# Verb Transitivity Pairs

**Last updated**: 2026-04-05

## Why transitivity matters for Japanese learners

Japanese has a rich system of transitive/intransitive verb pairs that English largely lacks. Many actions have two verbs — one for doing the action (transitive, 他動詞) and one for the action happening by itself (intransitive, 自動詞):

- 開ける (あける, to open something) ↔ 開く (あく, to open by itself)
- 落とす (おとす, to drop something) ↔ 落ちる (おちる, to fall)
- 始める (はじめる, to start something) ↔ 始まる (はじまる, to begin)

English speakers often struggle with this because English uses the same verb for both: "I opened the door" and "The door opened."

## How je-dict-1 handles transitivity

### Marking
Verb entries should include transitivity in their notes:
```
TRANSITIVITY:
- 他動詞 (transitive)
- Intransitive pair: {開|あ}く (to open by itself)
```

### Linking
Transitivity pairs use `prominent_see_also` with relationship labels "transitive pair" or "intransitive pair". This ensures the pair is displayed prominently, not buried in a generic "see also" list.

### Example sentences
Both transitive and intransitive uses should be illustrated in examples. For the transitive verb, show a clear agent acting on an object. For the intransitive verb, show the subject changing state without an explicit agent.

## Current status

Transitivity marking is a **high priority** v2 quality standard. Many older entries lack it. The polishing pipeline addresses this incrementally, but complete coverage requires:
1. Identifying all verb entries missing transitivity labels
2. Determining the correct pair for each verb
3. Adding notes, cross-references, and ensuring both members of each pair exist as entries

## Common patterns

| Transitive | Intransitive | Pattern |
|-----------|-------------|---------|
| 〜す | 〜る | 出す/出る, 返す/返る |
| 〜せる | 〜れる | 見せる/見える, 聞かせる/聞こえる |
| 〜める | 〜まる | 集める/集まる, 決める/決まる |
| 〜す | 〜れる | 壊す/壊れる, 汚す/汚れる |
| 〜ける | 〜く | 開ける/開く, 付ける/付く |

## Related pages

- [Quality Standards](../project/quality-standards.md)
- [Entry Design](../project/entry-design.md)
