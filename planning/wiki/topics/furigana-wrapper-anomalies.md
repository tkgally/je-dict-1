# Furigana Wrapper Anomalies

**Last updated**: 2026-08-08 (the pipe-less-brace detector rule proposed in June is measured and **retired**: 931 of its 931 findings are a mention-quoting convention, not wrappers — see "The brace is also a mention-quote". Its sibling rule, unbalanced braces, is sized at **34 instances / 33 entries** and is a genuine live-site defect.)

## Overview

je-dict-1 uses an in-text furigana syntax of the form `{kanji|reading}` to attach phonetic readings to kanji. The convention is that the **part before the pipe is the surface text (kanji only)** and **the part after the pipe is the hiragana reading**. Hiragana surface characters — okurigana and the honorific prefixes お・ご — should appear *outside* the wrapper:

> Correct: `お{酒|さけ}`, `{若|わか}い`, `{走|はし}り{続|つづ}ける`
> Wrong:   `{お酒|おさけ}`, `{若い|わかい}`, `{走り続ける|はしりつづける}`

An entry-level audit of all 27,000+ entries surfaces **859 instances across 624 unique entries** where the kanji portion of a wrapper contains hiragana. The error categories range from "renders correctly but is non-standard" through "renders correctly visually but breaks search/lookup" to "produces visibly wrong furigana." This page enumerates the patterns and their consequences.

## Counts by location and category

Detected with the regex `\{([^|}{]+)\|([^}{]+)\}` over `headword`, `examples[*].japanese`, and `notes`:

| Field | Instances |
|-------|-----------|
| Headword | 22 |
| Examples | 253 |
| Notes | 584 |
| **Total** | **859** |

Across **624 unique entries**.

By sub-pattern:

| Sub-pattern | Count | Example |
|-------------|------:|---------|
| o-prefix inside wrapper (`{お…\|お…}`) | 211 | `{お客様\|おきゃくさま}` |
| go-prefix inside wrapper (`{ご…\|ご…}`) | 13 | `{ご飯\|ごはん}` |
| Pure-kana wrapper (no kanji at all) | 172 | `{どんどん\|どんどん}` |
| Okurigana inside wrapper (kanji + hiragana on left side) | 463 | `{若い\|わかい}`, `{未払い\|みばらい}` |

## Sub-pattern 1: honorific prefix inside the wrapper (224 instances)

Words like お酒, お客様, ご飯, ご縁 are commonly written with an honorific prefix お (or ご) followed by kanji. The prefix is itself a hiragana character and does **not** need furigana. The correct form is:

```
お{酒|さけ}        ご{飯|はん}
```

What appears in 224 entries is instead:

```
{お酒|おさけ}     {ご飯|ごはん}
```

This renders without visible error in most browsers — the ruby tag puts `おさけ` over `お酒`, so the visible result is **two characters with three furigana characters spread over them**, which most browsers center-align acceptably. The two downstream costs are:

1. **Search/lookup mismatch.** `build/word_id_lookup.json` is keyed by the surface form. `お{酒|さけ}` produces a clean surface of `お酒` after stripping. `{お酒|おさけ}` produces the same `お酒`, so in this particular case the lookup happens to work. But `{お会|おあ}` (a partial wrap of `お会いする`) produces a surface of `お会` — not a real word — which the lookup misses.

2. **Inline-link compatibility.** Inline cross-references take the form `⟦surface→base：entry_id⟧`. The polishing prompts derive `surface` by extracting the visible text from a furigana run. The over-wrapped form forces extraction logic to handle multi-character surfaces with leading hiragana, which is brittle.

The fix is mechanical: replace `{お(.+?)|お(.+?)}` with `お{\1|\2}`, with the same for ご. Roughly 200 instances are clean-replaceable; the rest need spot review because the kanji portion may contain interleaved okurigana.

## Sub-pattern 2: pure-kana wrapper (172 instances)

```
{どんどん|どんどん}    {いつも|いつも}    {ところ|所}    {ある|ない}
```

When the kanji portion contains **no kanji at all**, the wrapper is at best a no-op and at worst a defect:

- `{どんどん|どんどん}` — surface == reading; the wrapper does nothing useful and just adds noise.
- `{ところ|所}` — **reversed**: the hiragana `ところ` is on the surface side, and the kanji `所` is on the reading side. The renderer will display `ところ` with `所` floating above it as ruby. Visually broken.
- `{ある|ない}` — surface `ある` and reading `ない` are **different words**. This is a pure data error.

A pure-kana wrapper is never correct. Either the wrapper is unnecessary (delete it) or it has been written backwards (swap the parts), or one side is just wrong (fix the content).

## Sub-pattern 3: okurigana inside the wrapper (463 instances)

This is the largest category and the one where the consequences vary most.

```
{若い|わかい}        {未払い|みばらい}      {寄り合い|よりあい}
{やり方|かた}        {セミの羽化|うか}      {しかめ面|づら}
```

Distinguish three subtypes:

### 3a. Reading mirrors the okurigana (152 instances — over-wrapped but renders OK)

`{若い|わかい}`, `{未払い|みばらい}`, `{連れ|つれ}`, `{寄り合い|よりあい}` — the okurigana hiragana in the surface appears at the corresponding position in the reading. A single ruby tag spans the whole word; visually correct. The only problem is style: the standard convention is to put okurigana outside the wrapper, so the canonical forms would be:

```
{若|わか}い           {未払|みばら}い        {連|つ}れ        {寄|よ}り{合|あ}い
```

### 3b. Reading shorter than surface (68 instances — visibly wrong)

`{やり方|かた}`, `{さらけ出|だ}`, `{セミの羽化|うか}`, `{しかめ面|づら}` — the reading only covers the **last** kanji, but the wrapper includes preceding hiragana on the surface side. Browsers will paint the partial reading over the full surface, producing visually wrong furigana (e.g., `かた` rendered over the entire `やり方`).

This is a true rendering bug. Each instance needs targeted repair: usually splitting the wrapper into a separate hiragana prefix plus a `{kanji|reading}` segment.

### 3c. Other interleaving (243 instances — most render OK but non-standard)

`{か所|かしょ}`, `{やる気|やるき}`, `{差し水|さしみず}`, `{決め手|きめて}` — the okurigana is in the middle or beginning of the surface, and the reading is the full phonetic version. As with 3a, the ruby span covers the whole word and renders correctly. The canonical form would be:

```
か{所|しょ}     やる{気|き}     {差|さ}し{水|みず}     {決|き}め{手|て}
```

## Effects beyond rendering

Even when the rendered result is visually correct, malformed wrappers cause two downstream problems documented in the existing tooling-backlog and observations:

1. **`add_adjective_conjugations.py` skips entries with malformed headwords.** Entry 01525_wakai (`{若い|わかい}`) is currently missing its conjugation table — almost certainly because the headword's furigana parser couldn't extract a clean stem. The basic-tier i-adjective 若い is on the live site without conjugations.

2. **Inline-link surface extraction misfires.** Comprehensive-polish observation 2026-05-08-002 noted that `verify_furigana.py` raises false positives on certain inline link patterns. The malformed wrapper class compounds the problem: the surface text the script sees after stripping isn't the surface text the renderer displays.

3. **`word_id_lookup.json` misses keys.** Lookups for partial-kanji surfaces (e.g., `お会` from `{お会|おあ}`) match nothing, so polish prompts that try to add inline links via the lookup fail silently.

## Why does this happen?

The pattern's frequency suggests a specific failure mode rather than a one-off error. Inspecting the affected entries by creation date does not reveal a single cohort — these errors appear across all months of entry creation. Three causal hypotheses:

1. **Copy-paste from external sources.** Many dictionaries and reading-aid tools annotate the whole word (kanji + okurigana) with the whole reading as one ruby tag. When entry-creation prompts copy or paraphrase external content, the source's convention can leak through.

2. **LLM autocomplete drift.** The schema's documented convention is "kanji only inside the wrapper," but entry-creation prompts don't restate this on every example. An LLM filling in a notes section may default to the more visually salient pattern (annotate the whole word) when not specifically reminded.

3. **No validator.** `build/verify_furigana.py` checks for **missing** furigana (kanji without a wrapper). It does not check whether the kanji portion of a wrapper is well-formed. `build/validate.py` schema-checks structure but doesn't parse the furigana strings. Without a validator, the error pattern has no immune system.

4. **Polisher confusion about the convention.** Comprehensive-polish session 2026-05-18 (entries 02251–02273) reported `{虫除|むしよ}け` as "broken furigana with okurigana outside the brackets" and suggested the "fix" `{虫除け|むしよけ}`. In fact, `{虫除|むしよ}け` (okurigana **outside** the wrapper) is the **correct** form per project convention, and the "fix" introduces the sub-pattern 3a (okurigana inside wrapper) documented above. This suggests that some polishing sessions are inadvertently worsening furigana formatting — applying the over-wrapped pattern because it looks more "complete." The lack of a validator means neither the original convention nor the deviation is enforced, and manual polishing can push entries in either direction.

## Additional sub-pattern: dual-reading slash notation

Comprehensive-polish session 2026-05-18 (entries 02251–02273) also identified a previously undocumented pattern: **dual-reading furigana with slash separators**, e.g., `{村|むら/そん}`, `{蛍|ほたる/けい}`. The slash notation attempts to show both on'yomi and kun'yomi readings in a single wrapper. The furigana renderer does not parse slashes — it treats the entire string `むら/そん` as the reading, which renders incorrectly.

The correct treatment is to use the contextually appropriate single reading and mention the alternative reading in notes if relevant. The scope of this pattern is unknown; see [Cleanup Backlog](../ideas/cleanup-backlog.md) → Priority 12 for the detection command.

## Connection to existing wiki analyses

- [Schema Tag Reliability](schema-tag-reliability.md) describes "runaway automation" — pipelines that consume bad data and produce more bad data. Malformed furigana is the same phenomenon at the **string level**: a slightly off-spec string parses successfully but breaks downstream tools (lookup, inline links, conjugation generation).
- [Furigana Strategy](furigana-strategy.md) documents *when* to annotate kanji. This page documents *how* to format the annotation when it is present.
- [Entry Consistency](entry-consistency.md) treats consistency in note structure. Furigana-string consistency is a parallel concern that has been less visible because the errors are mostly invisible to the eye.

## Detection sketch

A `build/check_furigana_format.py` script would:

1. Walk every entry's headword, examples, and notes.
2. For each `\{[^|}{]+\|[^}{]+\}` match, classify by sub-pattern (o-prefix, go-prefix, pure-kana, okurigana-in-wrap-with-mirror, okurigana-in-wrap-truncated, okurigana-in-wrap-other).
3. Emit JSON or a fix-list of entry IDs to a polish prompt.

Sub-pattern 3b (truncated readings) should be the highest-severity output bucket because those entries display visibly wrong furigana. Sub-pattern 2 (pure-kana wrappers) is next because many of those are reversed or mismatched. Sub-patterns 1 and 3a/3c are mostly cosmetic but worth a single sweep.

## What a measured slice looks like (23500–23999, swept 2026-07-28)

The counts above are dictionary-wide estimates from 2026-05. In 2026-07 a polish run
swept a contiguous 500-entry slice and read every finding by hand. The result is worth
recording in detail, because it contradicts three assumptions a bulk sweep would
naturally make.

**110 findings in 500 entries. 100 of them were `pure-kana` wrappers inside `notes`
fields** — katakana loanwords sitting in SIMILAR WORDS and contrast lists, not in
headwords or example sentences. This is sub-pattern 2 above, but concentrated far more
narrowly than the dictionary-wide figure suggests: the defect is not "pure-kana wrappers
occur throughout entries", it is "pure-kana wrappers occur in the note field's
comparison lists". That is a create-time habit — when an entry writer lists neighbouring
words in prose, they wrap each one uniformly, including the ones with no kanji to
annotate — and this slice confirms it at scale in the scientific/technical creation
cohort.

### The detector's `suggestion` field is not a fix list

Four of the 110 were outside every known wrapper family, and all four came back from
`check_furigana_format.py` with **`suggestion: null`**:

| Entry | Wrapper | What is actually wrong |
|---|---|---|
| 23819 | `{X|がく}` | The kanji 学 is **gone** — the surface is a literal Latin `X` |
| 23874 | `{それは|あなた}` | Surface and reading are unrelated words |
| 23903 | `{人|ひと}{々|びと}` | 々 split into its own wrapper; the pair should be one span |
| 23656 | `{兎形目|うさぎがための もく}` | Stray の (and a space) inside the reading |

A sweep that applied the detector's suggestions and skipped the nulls would have **missed
or mis-fixed every one of them** — and these four are the only genuinely *wrong*
information in the slice; the other 106 render acceptably. The `suggestion: null` rows are
not residue left over after the easy cases; they are the rows where the string is damaged
in a way no template can repair, which is exactly why the detector cannot propose a
replacement. **Sort by `suggestion is null` first, not last.**

This is a specific instance of the general principle recorded in
[deterministic-vs-semantic-tasks.md](deterministic-vs-semantic-tasks.md): the detector's
confidence is a property of the *pattern*, not of the *severity*.

### Defects cluster by creation batch, so extrapolation over-counts

The slice's empty-reading wrappers (`{チーム|}`, `{ある|}`, `{マイノリティ|}`) were not spread
across the 500 entries. They fell in the **contiguous 23798–23809 run** — a single
creation batch, twelve entries wide. Scaling any of these counts linearly from a sample
therefore over-estimates when the sample happens to contain a batch and under-estimates
when it does not.

The practical rule: **measure per slice before sizing a sweep**, and expect the work to
arrive in clumps that correspond to creation sessions rather than to ID ranges. The same
clustering has now been observed independently for stale `noentry` markers (seven in one
entry) and for missing inline links (whole creation runs with zero), which suggests it is
a property of how the dictionary was built rather than a coincidence of this defect.

### A related trap in mixed-script variant forms

`build/find_missing_furigana.py` correctly flagged a bare 丸 inside the variant spelling
**丸ノコ** written in an entry's explanatory prose. Katakana-mixed forms still need their
kanji wrapped (`{丸|まる}ノコ`), and this is easy to miss because the surrounding sentence is
English: the eye reads the Japanese fragment as a citation form rather than as text that
the furigana rules apply to. Worth remembering whenever an entry documents orthographic
variants — the variant list is prose, and prose is in scope.

## The brace is also a mention-quote — and it is not documented anywhere (measured 2026-08-08)

Since 2026-06-17 the [Tooling Backlog](../ideas/tooling-backlog.md) item 8 has carried two
proposed enhancements to `check_furigana_format.py`, both prompted by a single entry
(`06147_jiboujiki`, which really did contain both shapes):

- **(a)** flag any `{` … `}` span whose interior contains no `|`
- **(b)** flag any field whose `{` and `}` counts are unequal

Neither was ever sized. Running both over the whole corpus splits them decisively: **one is
ready to ship and the other should be deleted from the backlog.**

### Rule (b): unbalanced braces — 34 instances / 33 entries, and visibly broken

Real, bounded, and deterministic. The imbalance runs **both ways** — some fields drop a `}`
(`04471`, `09020`, `09801`), others carry an extra one (`08385`, `11708`, `12060`) — so the
fix is not a single regex but it is a single sitting. Two things make this the highest-value
item on this page:

1. **It is visible on the live site.** `08385`'s rendered page reads
   `…{引|ひ}き{継|つ}ぎ} tends to be used for…` → **"ぎ} tends to be used for"**, a literal
   brace in running English prose. This is not the "mostly invisible" class the rest of this
   page describes.
2. **It can corrupt an inline link, not just display.** `04471` contains
   `かき{混→かき{混：noentry⟧|ま}ぜ` — a furigana wrapper and a `⟦…⟧` link interleaved into each
   other. Neither structure survives; the link is unrecoverable without re-authoring.

Fields: 20 in `notes`, 14 in `examples[].japanese`. No cursor, no sampling, no priority order
needed — 33 files.

### Rule (a): pipe-less spans — 931 instances, and ~100% of them are a convention

The rule fires 931 times across 623 entries. It decomposes into four populations, and **none
of them is the defect the rule was written to catch**:

| Population | Instances | Entries | What it is |
|---|---:|---:|---|
| Kana-only, in `notes`/`explanation` prose | 855 | 574 | **Mention-quoting** |
| Grouping wrapper nesting a valid `{X\|Y}` | 168 | 128 | Convention (`{お{正月\|しょうがつ}}`) |
| Kanji, in `notes` prose | 54 | 40 | **Mention-quoting** a character |
| Kana-only, inside a `⟦…⟧` link surface | 22 | 20 | Display slot; P24-adjacent |
| `{WO}`/`{NI}` pattern placeholders | 7 | 4 | Convention (pattern notation) |

The two large populations are the same thing: **the brace is being used as a quotation mark
around a linguistic object under discussion**, exactly as an English style guide would
italicise a mentioned word. The samples are unambiguous:

- `The reading {じゅうぶん} means 'enough' while {じゅっぷん/じっぷん} means '10 minutes'` (01614)
- `Usually read as {だて}, sometimes {たて}` (02002)
- `The kanji {匂} is used for general smells, while {臭} specifically refers to bad ones` (00319)
- `The distinction {制作} vs {製作} is frequently confused` (23765)
- `- {〜て}たまらない: So ~ that one can't stand it` (03409, grammar-pattern notation)

For the kanji cases a reading would frequently be **wrong to add**: 00319 exists to contrast
匂 and 臭, which share the reading にお — annotating them would erase the distinction the note
is making. This is why the rule cannot be rescued with a "flag only spans containing kanji"
refinement, which was the obvious first repair and the one this measurement was expected to
recommend.

### The actual finding: an undocumented convention generates recurring false detectors

Roughly **1,084 spans** across the corpus use braces for mention-quoting, and the convention
appears in **no skill, no schema, and not in `CLAUDE.md`**. Its absence is not cosmetic — it
is the direct cause of a recurring failure mode:

> Three separate sessions across two months (2026-06-17, 2026-06-20, and the 2026-08-07 polish
> run that filed the 06824 stray-brace observation) have proposed detectors against this
> convention, because a reader encountering `{だて}` in a notes field and knowing only the
> documented rule — "furigana notation is `{漢字|かんじ}`" — correctly concludes it is malformed.

The fix is documentation, not tooling. `CLAUDE.md` and the `vocabulary-notes` skill state that
all kanji must carry furigana but say nothing about what a brace means when it has no pipe.
Writing the convention down is what stops the fourth detector proposal — and it is cheaper
than the detector would have been.

One caveat worth carrying: mention-quoting braces and furigana wrappers are **the same
delimiter doing two jobs**, which is a latent ambiguity. `{匂}` is a mention; `{匂|にお}` is a
wrapper; a future author adding a reading to a mention silently changes it into an annotation.
If the project ever wants to disambiguate, the moment to do it is before the count grows past
1,084 — but the cost of the migration is almost certainly higher than the cost of the
ambiguity, so the recommendation here is to document, not to migrate.

## Implications for je-dict-1

1. **Add a furigana-format validator.** A small `check_furigana_format.py` pass complements the existing `verify_furigana.py` (missing-furigana detector). Without one, the error pattern keeps recurring on every new creation batch.

2. **Prioritize sub-pattern 3b (truncated readings) as a rendering bug.** 68 entries currently display visibly wrong furigana. These are not cosmetic; on the live site, learners see incorrect phonetic information.

3. **Add a one-shot cleanup pass for sub-patterns 1, 2, and 3a/3c.** Mostly mechanical replacements with regex assistance, but each replacement should be validated against `build/word_id_lookup.json` to confirm the resulting surface form is recognized.

4. **Restate the convention in entry-creation skills.** The `entry-guidelines` skill (and the inline `furigana strategy` notes within other skills) should explicitly state "okurigana and お/ご prefixes go outside the wrapper" with both the right and the wrong examples. The current documentation says "all kanji must have furigana" but doesn't address where exactly the wrapper boundaries should sit.

5. **Document why this matters.** Malformed wrappers are mostly invisible on the surface, which is why the pattern has accumulated 859 instances without notice. The notes-prose case is particularly insidious because notes don't get re-rendered as often as examples; problems can linger forever.

## Related pages

- [Furigana Strategy](furigana-strategy.md) — when and how to annotate kanji with readings
- [Schema Tag Reliability](schema-tag-reliability.md) — sibling page on metadata drift; same "no validator → silent accumulation" pattern at the tag level
- [Entry Consistency](entry-consistency.md) — consistency standards across entries
- [Cleanup Backlog](../ideas/cleanup-backlog.md) — actionable cleanup items
- [Tooling Backlog](../ideas/tooling-backlog.md) — proposed scripts (including the format validator)
- [Entry Follow-ups](../ideas/entry-followups.md) — specific entries identified
