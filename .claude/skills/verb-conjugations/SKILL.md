---
name: verb-conjugations
description: Full conjugation table specification for verb and i-adjective entries. Covers JSON structure, form categories, and generation rules for all verb classes and i-adjectives.
---

# Verb Conjugation Tables

Every verb entry includes a `conjugation` field containing the full set of conjugated forms, hard-coded directly in the JSON. This makes the data self-contained and usable without any generation logic.

## JSON Structure

```json
"conjugation": {
  "type": "godan",
  "forms": [
    {"label": "Present", "affirmative": "{読|よ}む", "negative": "{読|よ}まない"},
    {"label": "Present polite", "affirmative": "{読|よ}みます", "negative": "{読|よ}みません"},
    {"label": "Past", "affirmative": "{読|よ}んだ", "negative": "{読|よ}まなかった"},
    ...
  ]
}
```

- `type`: One of `godan`, `ichidan`, `suru`, `kuru`, `aru`
- `forms`: Array of objects, each with `label`, `affirmative`, and `negative` (null for forms without a negative, like volitional)

## Form Categories (17 rows for most verbs)

The standard conjugation table includes these forms in order:

| # | Label | Example (godan む) |
|---|-------|-------------------|
| 1 | Present | {読|よ}む / {読|よ}まない |
| 2 | Present polite | {読|よ}みます / {読|よ}みません |
| 3 | Past | {読|よ}んだ / {読|よ}まなかった |
| 4 | Past polite | {読|よ}みました / {読|よ}みませんでした |
| 5 | て form | {読|よ}んで / {読|よ}まなくて |
| 6 | ている present | {読|よ}んでいる / {読|よ}んでいない |
| 7 | ている polite | {読|よ}んでいます / {読|よ}んでいません |
| 8 | ている past | {読|よ}んでいた / {読|よ}んでいなかった |
| 9 | ている past polite | {読|よ}んでいました / {読|よ}んでいませんでした |
| 10 | Conditional ば | {読|よ}めば / {読|よ}まなければ |
| 11 | Conditional たら | {読|よ}んだら / {読|よ}まなかったら |
| 12 | Volitional | {読|よ}もう / (null) |
| 13 | Volitional polite | {読|よ}みましょう / (null) |
| 14 | Potential | {読|よ}める / {読|よ}めない |
| 15 | Passive | {読|よ}まれる / {読|よ}まれない |
| 16 | Causative | {読|よ}ませる / {読|よ}ませない |
| 17 | Imperative | {読|よ}め / {読|よ}むな |

**Exceptions:**
- `ある` has only 7 forms (Present through Conditional たら — no potential, passive, causative, etc.)
- Verbs whose headword is already in passive form should omit the Passive row

## Godan Verb Conjugation Bases

| Ending | a-dan | i-dan | e-dan | o-dan | て/た |
|--------|-------|-------|-------|-------|------|
| う | わ | い | え | お | って/った |
| く | か | き | け | こ | いて/いた |
| ぐ | が | ぎ | げ | ご | いで/いだ |
| す | さ | し | せ | そ | して/した |
| つ | た | ち | て | と | って/った |
| ぬ | な | に | ね | の | んで/んだ |
| ぶ | ば | び | べ | ぼ | んで/んだ |
| む | ま | み | め | も | んで/んだ |
| る | ら | り | れ | ろ | って/った |

**Special case:** 行く conjugates て form as 行って (not 行いて).

## Ichidan Verbs

Stem = headword minus final る. All suffixes attach directly to stem.

## する Compound Verbs

Prefix = everything before する (e.g., {勉強|べんきょう} for {勉強|べんきょう}する).
If headword doesn't include する (e.g., がっかり), the entire headword is the prefix.

## 来る Verbs

The kanji 来 takes different readings in different forms:
- く: Present, Conditional ば, Imperative negative
- き: Polite forms, Past, て form, ている forms, Conditional たら, Volitional polite
- こ: Negative forms, Volitional, Potential, Passive, Causative, Imperative affirmative

## Adding Conjugation to New Entries

When creating a new verb entry, include the full conjugation field with all forms.
You can use `build/add_conjugations.py` to generate conjugation data automatically:

```bash
# After creating the entry without conjugation:
python3 build/add_conjugations.py --start <id_number> --end <id_number>
```

Or include the conjugation field directly when writing the entry JSON, following the patterns above.

## Bulk Operations

To add conjugation to all verbs that don't have it yet:
```bash
python3 build/add_conjugations.py           # Process all verbs
python3 build/add_conjugations.py --dry-run # Preview without writing
python3 build/add_conjugations.py --force   # Overwrite existing conjugation data
```

## I-Adjective Conjugation

I-adjectives also use the same `conjugation` JSON structure with 6 forms (Present, Past, て form, Adverbial, Conditional ば, Conditional たら). Type values are `i-adjective` (regular) or `ii` (いい and its compounds, which conjugate with よ- stem).

```bash
python3 build/add_adjective_conjugations.py           # Process all i-adjectives
python3 build/add_adjective_conjugations.py --dry-run # Preview without writing
python3 build/add_adjective_conjugations.py --force   # Overwrite existing
```
