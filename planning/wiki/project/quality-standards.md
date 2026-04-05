# Quality Standards

**Last updated**: 2026-04-05

## v2 Quality Standards

Based on multi-model LLM evaluation (Claude Haiku 4.5, GPT-5.2, Gemini 3 Flash), the project identified specific areas for improvement, prioritized into three tiers.

### High priority

1. **Verb transitivity** — Every verb entry should indicate 自動詞 (intransitive) or 他動詞 (transitive), and link to the paired verb when one exists. Many early entries lack this.

2. **Aspect notes** — Verbs with non-obvious ている meanings need explicit aspect documentation. For example, 結婚する + ている = "is married" (resultative state), not "is getting married" (ongoing action).

3. **Particle predicate lists** — Particle entries should list the verbs and adjectives that require them. For example, に should list 行く, 住む, あげる, etc.

4. **Collocation patterns** — Common noun-verb pairings (e.g., 電話をかける, 写真を撮る) should be documented in entry notes.

### Medium priority

1. **Register labels** — Mark entries as casual, neutral, formal, or honorific where relevant.

2. **Similar words** — Add contrastive sections distinguishing near-synonyms (e.g., 見る vs. 観る vs. 眺める).

3. **Adjective forms** — Document adverbial (〜く/〜に) and noun (〜さ) forms for adjectives.

4. **Example progression** — Ensure examples within each sense go from simple to complex.

### Low priority

1. **Kanji orthography notes** — When to use kanji vs. hiragana (e.g., する is usually in hiragana).

2. **Cultural notes** — Expand where culturally significant (e.g., お中元, 七五三).

3. **Keigo references** — Link to honorific forms (e.g., from 食べる to 召し上がる).

## Entry-level quality checklist

For any new or revised entry:

- [ ] All kanji have furigana in headword, examples, and notes
- [ ] 3+ examples per sense, progressively longer
- [ ] Notes have section headers, bullet points, paragraph breaks
- [ ] Notes include collocations and at least one additional section
- [ ] All prose is in English; Japanese only in examples/collocations
- [ ] POS tags use correct hyphenated format
- [ ] Verbs have conjugation tables
- [ ] I-adjectives have conjugation tables
- [ ] Cross-references link to related entries where appropriate
- [ ] Vocabulary tier is "general" for new entries

## Metrics

The `build/report.py` dashboard tracks dictionary health:
- Total entries, per-tier counts
- Example sentence counts and averages
- Cross-reference coverage
- Furigana completeness
- Tag distribution

## Ongoing polish processes

The polishing pipeline works through all entries systematically, improving them against these standards. Each polish task tracks progress so it can resume across sessions.

## Related pages

- [Entry Design](entry-design.md)
- [Content Pipeline](content-pipeline.md)
- [Example Sentence Design](../research/example-sentences.md)
- [Collocations in Learner Dictionaries](../research/collocations.md) — research informing the collocation patterns priority
