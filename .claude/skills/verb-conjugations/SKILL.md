---
name: verb-conjugations
description: Guidelines for adding verb conjugation tables to dictionary entries. Covers JSON structure, form generation for all verb classes, and display format.
---

# Verb Conjugation Tables

Every verb entry in je-dict-1 includes a `conjugation` field that stores the data needed to generate a full conjugation table on the entry page. The table appears in a collapsible `<details>` element between the gloss/prominent-see-also section and the definitions/examples.

## JSON Structure

The `conjugation` field is a top-level object in the entry JSON, placed after `gloss` and before `definitions`.

### Godan Verbs

```json
"conjugation": {
  "type": "godan",
  "ending": "つ",
  "stem": "{立|た}"
}
```

- **type**: `"godan"`
- **ending**: The dictionary-form ending kana. One of: `う`, `く`, `ぐ`, `す`, `つ`, `ぬ`, `ぶ`, `む`, `る`
- **stem**: Everything before the ending, with furigana notation. For 立つ → `{立|た}`. For 歩く → `{歩|ある}`. For 話す → `{話|はな}`.

### Ichidan Verbs

```json
"conjugation": {
  "type": "ichidan",
  "stem": "{食|た}べ"
}
```

- **type**: `"ichidan"`
- **stem**: Everything before る, with furigana. For 食べる → `{食|た}べ`. For 見る → `{見|み}`. For 起きる → `{起|お}き`.

### する Verbs

```json
"conjugation": {
  "type": "suru",
  "prefix": "{挨拶|あいさつ}"
}
```

- **type**: `"suru"`
- **prefix**: The noun part before する, with furigana. For 挨拶する → `{挨拶|あいさつ}`. For 勉強する → `{勉強|べんきょう}`. For する itself (entry 00392), use `""` (empty string).

### 来る Verbs

```json
"conjugation": {
  "type": "kuru",
  "prefix": ""
}
```

- **type**: `"kuru"`
- **prefix**: Any prefix before 来る. Empty string for 来る itself. For compound verbs like 持って来る, use the prefix portion: `{持|も}って`.

### ある

```json
"conjugation": {
  "type": "aru"
}
```

- **type**: `"aru"` — special handling because the negative is ない (not あらない), and it has no progressive, potential, passive, causative, or imperative forms.

### Irregular Verbs

For verbs with irregular forms (e.g., 行く with irregular て form), add an `overrides` object:

```json
"conjugation": {
  "type": "godan",
  "ending": "く",
  "stem": "{行|い}",
  "overrides": {
    "te_affirmative": "{行|い}って",
    "past_affirmative": "{行|い}った",
    "past_negative": "{行|い}かなかった",
    "conditional_tara_affirmative": "{行|い}ったら",
    "conditional_tara_negative": "{行|い}かなかったら",
    "progressive_present_affirmative": "{行|い}っている",
    "progressive_present_negative": "{行|い}っていない",
    "progressive_present_polite_affirmative": "{行|い}っています",
    "progressive_present_polite_negative": "{行|い}っていません",
    "progressive_past_affirmative": "{行|い}っていた",
    "progressive_past_negative": "{行|い}っていなかった",
    "progressive_past_polite_affirmative": "{行|い}っていました",
    "progressive_past_polite_negative": "{行|い}っていませんでした"
  }
}
```

Override keys correspond to table cells. Use overrides sparingly — only for genuinely irregular forms, not for regular conjugation.

#### Known Irregular Verbs

| Verb | Issue | Override needed |
|------|-------|-----------------|
| {行|い}く | て/た form uses って/った (not いて/いた) | te, past, progressive, conditional たら forms |
| いらっしゃる | ます form is いらっしゃいます (not いらっしゃります) | present_polite, past_polite, volitional_polite |
| おっしゃる | ます form is おっしゃいます | present_polite, past_polite, volitional_polite |
| くださる | ます form is くださいます | present_polite, past_polite, volitional_polite |
| なさる | ます form is なさいます | present_polite, past_polite, volitional_polite |
| ある | Negative is ない; no progressive/potential/passive/causative | Use type `"aru"` |
| くれる | Imperative is くれ (not くれろ) | imperative_affirmative |

## Display Format (Option D: Affirmative/Negative Table)

The conjugation table is displayed as a two-column table with row groups. All forms use ruby annotation for furigana, matching the dictionary's standard display.

### Table Structure

The table has 18 rows organized in 5 groups:

#### Group 1: Basic Forms

| | Affirmative | Negative |
|---|---|---|
| Present | {立|た}つ | {立|た}たない |
| Present polite | {立|た}ちます | {立|た}ちません |
| Past | {立|た}った | {立|た}たなかった |
| Past polite | {立|た}ちました | {立|た}ちませんでした |
| て form | {立|た}って | {立|た}たなくて |

#### Group 2: Progressive (ている) Forms

| | Affirmative | Negative |
|---|---|---|
| ている present | {立|た}っている | {立|た}っていない |
| ている present polite | {立|た}っています | {立|た}っていません |
| ている past | {立|た}っていた | {立|た}っていなかった |
| ている past polite | {立|た}っていました | {立|た}っていませんでした |

#### Group 3: Conditional

| | Affirmative | Negative |
|---|---|---|
| ば form | {立|た}てば | {立|た}たなければ |
| たら form | {立|た}ったら | {立|た}たなかったら |

#### Group 4: Volitional

| | Affirmative | Negative |
|---|---|---|
| Volitional | {立|た}とう | — |
| Volitional polite | {立|た}ちましょう | — |

#### Group 5: Other Forms

| | Affirmative | Negative |
|---|---|---|
| Potential | {立|た}てる | {立|た}てない |
| Passive | {立|た}たれる | {立|た}たれない |
| Causative | {立|た}たせる | {立|た}たせない |
| Imperative | {立|た}て | {立|た}つな |

### HTML Rendering

The table appears inside `<details class="conjugation-details">` with `<summary>Conjugation</summary>`, positioned after the entry-header div (which includes gloss and prominent-see-also) and before the definitions-with-examples section.

## Conjugation Rules by Verb Class

### Godan Verb Sound Changes

The godan verb stem combines with different vowel rows. The ending kana determines the て/た form sound change.

| Ending | Negative (あ-row) | ます (い-row) | Conditional (え-row) | Volitional (お-row) | て/た form |
|--------|-------------------|--------------|---------------------|---------------------|-----------|
| う | わ | い | え | お | って/った |
| く | か | き | け | こ | いて/いた |
| ぐ | が | ぎ | げ | ご | いで/いだ |
| す | さ | し | せ | そ | して/した |
| つ | た | ち | て | と | って/った |
| ぬ | な | に | ね | の | んで/んだ |
| ぶ | ば | び | べ | ぼ | んで/んだ |
| む | ま | み | め | も | んで/んだ |
| る | ら | り | れ | ろ | って/った |

**Exception**: 行く uses って/った (not いて/いた).

### Godan Complete Form Generation

Given stem S and ending kana, for each row:

| Form | Construction |
|------|-------------|
| Present aff. | S + う-row |
| Present neg. | S + あ-row + ない |
| Present polite aff. | S + い-row + ます |
| Present polite neg. | S + い-row + ません |
| Past aff. | S + て/た-row (た) |
| Past neg. | S + あ-row + なかった |
| Past polite aff. | S + い-row + ました |
| Past polite neg. | S + い-row + ませんでした |
| て form aff. | S + て/た-row (て) |
| て form neg. | S + あ-row + なくて |
| ている present aff. | て form + いる |
| ている present neg. | て form + いない |
| ている present polite aff. | て form + います |
| ている present polite neg. | て form + いません |
| ている past aff. | て form + いた |
| ている past neg. | て form + いなかった |
| ている past polite aff. | て form + いました |
| ている past polite neg. | て form + いませんでした |
| Conditional ば aff. | S + え-row + ば |
| Conditional ば neg. | S + あ-row + なければ |
| Conditional たら aff. | Past aff. + ら |
| Conditional たら neg. | S + あ-row + なかったら |
| Volitional aff. | S + お-row + う |
| Volitional polite | S + い-row + ましょう |
| Potential aff. | S + え-row + る |
| Potential neg. | S + え-row + ない |
| Passive aff. | S + あ-row + れる |
| Passive neg. | S + あ-row + れない |
| Causative aff. | S + あ-row + せる |
| Causative neg. | S + あ-row + せない |
| Imperative aff. | S + え-row |
| Imperative neg. | S + う-row + な |

**Note on う-ending verbs**: The negative あ-row form uses わ (not あ). E.g., 買う → 買わない (not 買あない).

### Ichidan Complete Form Generation

Given stem S (everything before る):

| Form | Construction |
|------|-------------|
| Present aff. | S + る |
| Present neg. | S + ない |
| Present polite aff. | S + ます |
| Present polite neg. | S + ません |
| Past aff. | S + た |
| Past neg. | S + なかった |
| Past polite aff. | S + ました |
| Past polite neg. | S + ませんでした |
| て form aff. | S + て |
| て form neg. | S + なくて |
| ている present aff. | S + ている |
| ている present neg. | S + ていない |
| ている present polite aff. | S + ています |
| ている present polite neg. | S + ていません |
| ている past aff. | S + ていた |
| ている past neg. | S + ていなかった |
| ている past polite aff. | S + ていました |
| ている past polite neg. | S + ていませんでした |
| Conditional ば aff. | S + れば |
| Conditional ば neg. | S + なければ |
| Conditional たら aff. | S + たら |
| Conditional たら neg. | S + なかったら |
| Volitional aff. | S + よう |
| Volitional polite | S + ましょう |
| Potential aff. | S + られる |
| Potential neg. | S + られない |
| Passive aff. | S + られる |
| Passive neg. | S + られない |
| Causative aff. | S + させる |
| Causative neg. | S + させない |
| Imperative aff. | S + ろ |
| Imperative neg. | S + るな |

**Note**: For ichidan verbs, potential and passive have the same form (S + られる). This is correct and should be displayed in both rows.

### する Complete Form Generation

Given prefix P (noun part, empty string for する itself):

| Form | Construction |
|------|-------------|
| Present aff. | P + する |
| Present neg. | P + しない |
| Present polite aff. | P + します |
| Present polite neg. | P + しません |
| Past aff. | P + した |
| Past neg. | P + しなかった |
| Past polite aff. | P + しました |
| Past polite neg. | P + しませんでした |
| て form aff. | P + して |
| て form neg. | P + しなくて |
| ている present aff. | P + している |
| ている present neg. | P + していない |
| ている present polite aff. | P + しています |
| ている present polite neg. | P + していません |
| ている past aff. | P + していた |
| ている past neg. | P + していなかった |
| ている past polite aff. | P + していました |
| ている past polite neg. | P + していませんでした |
| Conditional ば aff. | P + すれば |
| Conditional ば neg. | P + しなければ |
| Conditional たら aff. | P + したら |
| Conditional たら neg. | P + しなかったら |
| Volitional aff. | P + しよう |
| Volitional polite | P + しましょう |
| Potential aff. | P + できる |
| Potential neg. | P + できない |
| Passive aff. | P + される |
| Passive neg. | P + されない |
| Causative aff. | P + させる |
| Causative neg. | P + させない |
| Imperative aff. | P + しろ |
| Imperative neg. | P + するな |

**Note**: For suru verbs, the potential is formed with できる, not しられる. For entries like 挨拶する, this becomes 挨拶できる.

### 来る Complete Form Generation

Given prefix P (empty for 来る itself):

| Form | Construction |
|------|-------------|
| Present aff. | P + {来|く}る |
| Present neg. | P + {来|こ}ない |
| Present polite aff. | P + {来|き}ます |
| Present polite neg. | P + {来|き}ません |
| Past aff. | P + {来|き}た |
| Past neg. | P + {来|こ}なかった |
| Past polite aff. | P + {来|き}ました |
| Past polite neg. | P + {来|き}ませんでした |
| て form aff. | P + {来|き}て |
| て form neg. | P + {来|こ}なくて |
| ている present aff. | P + {来|き}ている |
| ている present neg. | P + {来|き}ていない |
| ている present polite aff. | P + {来|き}ています |
| ている present polite neg. | P + {来|き}ていません |
| ている past aff. | P + {来|き}ていた |
| ている past neg. | P + {来|き}ていなかった |
| ている past polite aff. | P + {来|き}ていました |
| ている past polite neg. | P + {来|き}ていませんでした |
| Conditional ば aff. | P + {来|く}れば |
| Conditional ば neg. | P + {来|こ}なければ |
| Conditional たら aff. | P + {来|き}たら |
| Conditional たら neg. | P + {来|こ}なかったら |
| Volitional aff. | P + {来|こ}よう |
| Volitional polite | P + {来|き}ましょう |
| Potential aff. | P + {来|こ}られる |
| Potential neg. | P + {来|こ}られない |
| Passive aff. | P + {来|こ}られる |
| Passive neg. | P + {来|こ}られない |
| Causative aff. | P + {来|こ}させる |
| Causative neg. | P + {来|こ}させない |
| Imperative aff. | P + {来|こ}い |
| Imperative neg. | P + {来|く}るな |

**Note**: 来る changes its reading depending on the form: く (dictionary, conditional ば, prohibitive), き (ます, て, た, ている), こ (ない, volitional, potential, passive, causative, imperative).

### ある Form Generation

ある is a special case with limited conjugation:

| Form | Affirmative | Negative |
|------|------------|---------|
| Present | ある | ない |
| Present polite | あります | ありません |
| Past | あった | なかった |
| Past polite | ありました | ありませんでした |
| て form | あって | なくて |
| Conditional ば | あれば | なければ |
| Conditional たら | あったら | なかったら |

ある does **not** have: progressive (ている), volitional, potential, passive, causative, or imperative forms. These rows are omitted from the table.

## Batch Processing Script

A helper script at `build/add_conjugations.py` automates adding conjugation data to entries in bulk. See `prompts/polish_verb_conjugations.md` for usage instructions. The script handles the majority of entries but flags ambiguous cases for manual review.

## Determining Verb Class from Existing Entries

Many existing entries have inconsistent `part_of_speech` values. Use these guidelines:

### Identifying Verb Entries

Check **both** `part_of_speech` and `metadata.tags.pos` — some entries have verb info in only one place.

**IMPORTANT**: The word "adverb" contains "verb". When searching POS strings, use word-boundary-aware matching (e.g., regex `(?<!ad)verb`) to avoid classifying adverbs as verbs.

**Entries that ARE verbs** (add conjugation):
- Any POS containing "verb" (but not "adverb"), "godan", "ichidan", "suru", "kuru"
- POS containing "verbal" (these are する nouns)
- POS containing "noun (する)" (another する variant)
- `metadata.tags.pos` containing "verb-suru", "verb-godan", "verb-ichidan", etc.
- "auxiliary verb" entries (e.g., ～続ける)
- "expression, verb phrase" entries (e.g., 頭を抱える)

**Entries that are NOT verbs** (do NOT add conjugation):
- Adverbs (POS "adverb" or "adverb, noun")
- Proverbs ("expression (proverb)", "proverb")
- ている expressions ("expression (verb て-form + いる)") — already conjugated
- Noun forms of verbs where the headword ends in a non-dictionary kana like り, し, い (e.g., 申し送り, 仕送り) — even if POS says "godan verb"

### Identifying Godan vs Ichidan

1. **Check existing `verb_class` tag** if present (in `metadata.tags.verb_class`)
2. **Check `part_of_speech`** for explicit markers: "godan", "ichidan", "五段", "一段"
3. **Verify the reading ends in a valid dictionary-form kana** (うくぐすつぬぶむる for godan; る for ichidan). If it ends in り, し, き, etc., the entry is likely a noun form, not a verb — skip it.
4. **Check the dictionary ending**:
   - Ends in a kana other than る → always godan
   - Ends in る with an え-row kana before it → almost always ichidan (食べる, 見える, 教える)
   - Ends in る with an い-row kana before it → usually ichidan (見る, 起きる), but some are godan (帰る, 走る, 知る, 入る, 切る, 散る)
   - Ends in る with an あ-row, う-row, or お-row kana before it → usually godan (分かる, 作る, 通る)
   - For ambiguous cases, use your linguistic knowledge
5. **Check the notes field** for transitivity info that reveals the class

### Identifying する Verbs

**All known POS patterns for する verbs** (compiled from the actual dictionary):
- "noun, suru verb", "noun, verb (suru)", "noun, suru-verb", "noun / suru verb", "noun / suru-verb"
- "verb (suru)", "suru verb", "verb-suru", "suru-verb"
- "noun, verb (する)", "noun / verb (する)", "noun, する-verb", "する verb"
- "noun; suru verb", "noun; verb (suru)", "noun; suru-verb", "noun/suru-verb", "noun/suru verb"
- "noun (verbal)" — a する noun without explicit "suru" mention
- "noun; noun (する)" — another variant without explicit "suru"
- "adverb, suru verb", "adverb, verb (suru)"
- "noun, suru verb, na-adjective" (e.g., 乾燥)
- "noun, suru-verb, interjection" (e.g., 乾杯)
- Plain "noun" **with `verb-suru` in `metadata.tags.pos`** — IMPORTANT: many entries have POS="noun" but are する verbs only identifiable from the tags array

For all する verbs: use type `"suru"` with the prefix being the headword (without する if it ends in する).

### Identifying 来る

Very few entries: 来る itself, plus compounds like 持ってくる, やって来る. Check if POS contains "kuru" or headword ends in 来る/くる.

## Adding the `verb_class` Tag

When adding conjugation data, also ensure the `verb_class` tag is set correctly in `metadata.tags`. Valid values:

- `godan-u`, `godan-ku`, `godan-gu`, `godan-su`, `godan-tsu`, `godan-nu`, `godan-bu`, `godan-mu`, `godan-ru`
- `ichidan`
- `suru`
- `kuru`
- `irregular`

This tag should match the conjugation type and ending.

## Full Example: 立つ (Godan, つ-ending)

```json
{
  "id": "00758_tatsu",
  "headword": "{立|た}つ",
  "reading": "たつ",
  "part_of_speech": "verb (godan)",
  "gloss": "to stand",
  "conjugation": {
    "type": "godan",
    "ending": "つ",
    "stem": "{立|た}"
  },
  "definitions": [ ... ],
  "examples": [ ... ]
}
```

## Full Example: 食べる (Ichidan)

```json
"conjugation": {
  "type": "ichidan",
  "stem": "{食|た}べ"
}
```

## Full Example: 挨拶する (する verb)

```json
"conjugation": {
  "type": "suru",
  "prefix": "{挨拶|あいさつ}"
}
```

## Full Example: 行く (Godan with irregular て form)

```json
"conjugation": {
  "type": "godan",
  "ending": "く",
  "stem": "{行|い}",
  "overrides": {
    "te_affirmative": "{行|い}って",
    "past_affirmative": "{行|い}った",
    "past_negative": "{行|い}かなかった",
    "conditional_tara_affirmative": "{行|い}ったら",
    "conditional_tara_negative": "{行|い}かなかったら",
    "progressive_present_affirmative": "{行|い}っている",
    "progressive_present_negative": "{行|い}っていない",
    "progressive_present_polite_affirmative": "{行|い}っています",
    "progressive_present_polite_negative": "{行|い}っていません",
    "progressive_past_affirmative": "{行|い}っていた",
    "progressive_past_negative": "{行|い}っていなかった",
    "progressive_past_polite_affirmative": "{行|い}っていました",
    "progressive_past_polite_negative": "{行|い}っていませんでした"
  }
}
```

## Override Key Reference

All valid override keys (matching table rows and columns):

**Basic forms**: `present_affirmative`, `present_negative`, `present_polite_affirmative`, `present_polite_negative`, `past_affirmative`, `past_negative`, `past_polite_affirmative`, `past_polite_negative`, `te_affirmative`, `te_negative`

**Progressive forms**: `progressive_present_affirmative`, `progressive_present_negative`, `progressive_present_polite_affirmative`, `progressive_present_polite_negative`, `progressive_past_affirmative`, `progressive_past_negative`, `progressive_past_polite_affirmative`, `progressive_past_polite_negative`

**Conditional**: `conditional_ba_affirmative`, `conditional_ba_negative`, `conditional_tara_affirmative`, `conditional_tara_negative`

**Volitional**: `volitional_affirmative`, `volitional_polite`

**Other**: `potential_affirmative`, `potential_negative`, `passive_affirmative`, `passive_negative`, `causative_affirmative`, `causative_negative`, `imperative_affirmative`, `imperative_negative`

## Checklist

When adding conjugation to an entry:

- [ ] Correctly identify verb class (godan/ichidan/suru/kuru/aru/irregular)
- [ ] For godan: correct ending kana identified
- [ ] Stem/prefix has correct furigana notation
- [ ] `verb_class` tag is set in metadata.tags
- [ ] Overrides added for any irregular forms
- [ ] Run `python3 build/validate.py` after changes
