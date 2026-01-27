# Clean Up Candidates List Prompt

Review and clean up candidate_words.json by removing inappropriate entries that were incorrectly extracted from notes cross-references, leaving only words suitable for the dictionary.

## Background

A script extracted words from notes cross-references in dictionary entries by parsing furigana notation like `{漢字|かんじ}`. However, this extraction sometimes captured partial words—verb stems, adjective stems, or incomplete compounds—rather than complete dictionary words.

## Types of Entries to REMOVE

### 1. Verb Stems (Missing Okurigana)

Words that are clearly verb stems without their inflectional endings:

| Remove | Should be | Reason |
|--------|-----------|--------|
| 伝 (つた) | 伝える (つたえる) | Verb stem missing える |
| 始 (はじ) | 始める (はじめる) | Verb stem missing める |
| 終 (お) | 終わる (おわる) | Verb stem missing わる |
| 並 (なら) | 並ぶ (ならぶ) | Verb stem missing ぶ |
| 届 (とど) | 届く (とどく) | Verb stem missing く |
| 調 (しら) | 調べる (しらべる) | Verb stem missing べる |

### 2. Adjective Stems (Missing い or な)

Words that are i-adjective or na-adjective stems:

| Remove | Should be | Reason |
|--------|-----------|--------|
| 低 (ひく) | 低い (ひくい) | Adjective stem missing い |
| 高 (たか) | 高い (たかい) | Adjective stem missing い |
| 長 (なが) | 長い (ながい) | Adjective stem missing い |
| 静 (しず) | 静か (しずか) | Na-adjective stem |

### 3. Incomplete Compounds

Words truncated mid-compound, typically お-prefix words missing their endings:

| Remove | Should be | Reason |
|--------|-----------|--------|
| お互 (おたが) | お互い (おたがい) | Missing い |
| お参 (おまい) | お参り (おまいり) | Missing り |
| お喋 (おしゃべ) | お喋り (おしゃべり) | Missing り |
| お守 (おまも) | お守り (おまもり) | Missing り |
| お吸 (おす) | お吸い物 (おすいもの) | Incomplete compound |

### 4. Bound Morphemes Without Context

Single kanji that only function as bound prefixes/suffixes but were captured without their typical context (unless they are legitimate standalone entries like prefixes 不, 無, etc.):

- Single kanji readings that don't stand alone as words
- Partial morphemes that require attachment to other elements

### 5. Extraction Artifacts

Entries with anomalous readings or formatting issues:
- Readings that don't match standard Japanese phonology
- Entries where word and reading are identical but shouldn't be (copying errors)
- Entries with unusual characters or formatting

## Types of Entries to KEEP

### 1. Complete Standalone Words

Words that exist as independent dictionary entries:
- Full nouns: お土産 (おみやげ), お寺 (おてら)
- Complete verbs: 立ち上がる (たちあがる)
- Complete adjectives: 美しい (うつくしい)
- Adverbs, particles, etc.

### 2. Legitimate Prefix/Suffix Entries

Productive affixes that warrant their own entries:
- 不～ (ふ～) - negative prefix
- ～的 (～てき) - adjectival suffix
- ～化 (～か) - -ification suffix

### 3. Set Phrases and Idioms

Complete idiomatic expressions:
- いずれ菖蒲 (valid set phrase, though may need verification)
- Four-character compounds (yojijukugo)

## Workflow

### Step 1: Initial Assessment

```bash
# Count total candidates
head -10 candidate_words.json

# Count candidates from notes cross-reference
grep -c '"found in notes cross-reference"' candidate_words.json
```

### Step 2: Identify Problematic Entries

Focus on entries with `"notes": "found in notes cross-reference"` as these are the ones from the automated extraction. Review them systematically.

Look for patterns:
- Single kanji with kun'yomi readings (often verb/adjective stems)
- お-prefix words with short readings
- Words where the reading seems incomplete

### Step 3: Remove Inappropriate Entries

For each entry to remove, delete the entire JSON object including its surrounding comma. Be careful to maintain valid JSON structure.

**Method A: Manual editing**
Open the file and search for problematic patterns, removing entries one by one.

**Method B: Script-assisted**
Create a Python script to filter out entries matching certain patterns (single kanji with specific reading patterns, etc.), then manually review edge cases.

### Step 4: Validate JSON

After editing, verify the file is valid JSON:

```bash
python3 -c "import json; json.load(open('candidate_words.json'))" && echo "Valid JSON"
```

### Step 5: Update Metadata

After removing entries, update the metadata:

```bash
python3 -c "
import json
with open('candidate_words.json', 'r') as f:
    data = json.load(f)
data['metadata']['total_candidates'] = len(data['candidates'])
from datetime import datetime, timezone
data['metadata']['last_updated'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
with open('candidate_words.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f\"Updated: {data['metadata']['total_candidates']} candidates\")
"
```

## Decision Guidelines

When uncertain whether to remove an entry:

1. **Would a Japanese dictionary include this as a headword?** If the word only appears as part of a larger word (like verb stems), remove it.

2. **Can this word stand alone in a sentence?** Verb stems like 伝 (つた) cannot—you need 伝える or 伝わる.

3. **Is the reading complete?** If the reading seems truncated (like ひく for 低 instead of ひくい), remove it.

4. **Is this a productive affix?** Prefixes like 不～ and suffixes like ～化 are legitimate entries. But single kanji that only appear in specific compounds are not.

5. **When in doubt, remove.** It's better to have a clean candidate list. Legitimate words can always be re-added with proper forms.

## Reporting

After cleanup, report:
1. Number of entries removed
2. Categories of removals (verb stems, adjective stems, incomplete compounds, etc.)
3. Final candidate count
4. Any entries you were uncertain about (for human review)
