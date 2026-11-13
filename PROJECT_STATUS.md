# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-10-26
**Current phase**: Phase 6 - Continued Expansion & Polish

**Live site**: https://www.tkgje.jp/

> **Full history**: Older change logs are archived in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
> **Quick reference**: See [PROJECT_CONTEXT_BRIEF.md](PROJECT_CONTEXT_BRIEF.md) for a concise session-start overview.
> **Project setup**: See [CLAUDE.md](CLAUDE.md) for commands, file placement, and skills.

## Current State

**Phase 6: Continued Expansion & Polish** — Adding vocabulary while maintaining v2 quality standards, with an automated pipeline for batch maintenance tasks. The dictionary uses an original three-tier vocabulary classification (basic, core, general) instead of JLPT levels.

### Content Status

These counts are approximate. Run `make report` for accurate, up-to-date numbers.

| Metric | Value |
|--------|-------|
| Total entries | ~30,764 |
| Basic tier | 801 (closed) |
| Core tier | ~1,982 (closed) |
| General tier | ~27,981 (open) |
| Candidate words | ~188 (all vetted; queue cleaned 2026-08-11) |
| Cross-references | ~19,000 |
| Example sentences | ~119,000 |

## v2 Quality Standards

Based on multi-model LLM evaluation (Claude Haiku 4.5, GPT-5.2, Gemini 3 Flash), these are the priority enhancements:

### HIGH PRIORITY
1. **Verb transitivity** - Add 自動詞/他動詞 and pair verbs to all verb entries
2. **Aspect notes** - Explain ている behavior for verbs with non-obvious meanings
3. **Particle predicate lists** - List verbs/adjectives requiring each particle
4. **Collocation patterns** - Add common noun-verb pairings

### MEDIUM PRIORITY
1. **Register labels** - Mark casual/neutral/formal for all entries
2. **Similar words** - Add contrastive sections for semantic neighbors
3. **Adjective forms** - Add adverbial (〜く/〜に) and noun forms (〜さ)
4. **Example progression** - Ensure simple → complex ordering

### LOW PRIORITY
1. **Kanji orthography notes** - When to use kanji vs. hiragana
2. **Cultural notes** - Expand where significant
3. **Keigo references** - Link to honorific forms

## Recent Changes

### 2026-11-13 (20 new entries, first cycle of the 16:15 UTC run)

33481–33500. Closure: 酒樽, 過料, 着回す, 国外退去, 御託宣, 文部省, 竜宮城. Brainstorm: ずる休み, 所持金, 時は金なり, 大学入試, 国立大学, 軒を並べる, 上野公園 (each cross-referenced to its seed). ezFurigana lookups: ばかりに, 離れ, 半球, 場末, バラ色, 伴走.
Self-check: 2 notes flags applied (旧帝大 are not the oldest national universities; 繁華街 described correctly); 17 kana links judged, 0 flagged. New candidates: 母屋, 仮病.

### 2026-11-13 (candidates: 10 brainstorm candidates, ninth cycle of the run started 2026-11-12 23:36 UTC)

One seeds batch (headwords 200–219): own proposals plus gpt-6.1-sol and gemini-3.8-flash ($0.09); 26 survived the filter, 10 added (羽田空港, 成田空港, 関西国際空港, 泣き声, 相合傘, 秋分の日, 折れ曲がる, 中ほど, 隙間風, 北国), 16 rejected (existing entries or variants, free phrases, compositional compounds, slang, one wrong reading). Unit kept small to fit the run clock; closure stream not run.

### 2026-11-12 (21 new entries, first cycle of the 23:36 UTC run)

33460–33480. Closure: 土俵際, 理学療法士, 玉手箱, 国民主権, 虫垂炎, 片膝, 無念. Brainstorm: もう少し, 山ほど, いささか, ときたま, 年がら年中, よくよく, 並び (each cross-referenced to its seed). ezFurigana lookups: にしても (as にせよ), 年内, 寝泊まり, 柔和, 盗み見る, 迫害, 発出.
Self-check: clean (0 of 21 flagged; 18 kana links judged, 0 flagged). New candidates: 作業療法士, 乙姫.

### 2026-11-13 (Explore page: phone layout, smooth flight to a clicked word)

On a phone the cloud now fills the page. The site header opens from a menu button, the settings from a Settings button, the places from one button that names the current place; the selected word is a short sheet along the bottom (word, reading, meaning) that unfolds to the examples and connections. Held sideways, the word card stands on the right. On every screen a click on a word now turns the view toward it and then flies in, over 1.7 to 4.6 seconds, along a path that goes around the word rather than through it; with the system's reduced-motion setting the old view dissolves into the new one. Only `build/templates/explore.{html,css,js}` changed.

### 2026-11-12 (Explore page: the dictionary as a 3D word cloud)

`explore.html` replaces Browse in every header; the alphabetical listing is now linked from the Lists page. Places are the 90 semantic tags (`explore/tags.json`) until curated groups (`explore/groups/`) replace them; connections are the entries' cross-references. New Routine mode `explore-groups` (weight 0.12, `prompts/explore_groups.md`) writes the curated groups; the other weights were scaled by 0.88. See CLAUDE.md, "Explore page".

