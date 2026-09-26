# TKG Japanese-English Learner's Dictionary

**Live site: https://www.tkgje.jp/**

An explanatory Japanese-English dictionary for intermediate learners of Japanese: people who can
read hiragana and katakana, know some kanji, and want to understand words well enough to use
them, not just to look up a translation. This repository holds all of the dictionary's data and
all of the code that builds the site.

The project is supervised by [Tom Gally](https://www.gally.net/about.html). Almost all of the
entry writing, checking and coding has been done by Claude (Anthropic) working in Claude Code,
with independent checks by models from other companies. The story of the project, in Tom's
words, is on the site's [About page](https://www.tkgje.jp/about.html).

Everything here is dedicated to the public domain under [CC0 1.0 Universal](LICENSE). You may copy,
adapt and redistribute the data and code for any purpose, including commercial use, without
asking permission. Credit is welcome but not required.

## What the dictionary contains

As of late September 2026:

| | |
|---|---|
| Entries | about 30,900 |
| Example sentences | about 120,000, each with an English translation |
| Inline links from words in examples and notes to their entries | about 1,000,000 |
| Cross-references between entries (synonyms, antonyms, verb pairs, keigo, …) | about 78,000 |
| Kanji in the kanji index | about 2,800 |
| Verbs and i-adjectives with full conjugation tables | about 7,800 |
| Articles on topics that single entries cannot cover (keigo, counters, giving and receiving, …) | 10 |

The dictionary is now in a maintenance phase. Existing entries are reviewed, corrected and
connected to one another; a new entry is added mainly when the dictionary already uses a word
that has no entry of its own.

### Vocabulary tiers

Instead of JLPT levels, every entry belongs to one of three tiers:

- **Basic** (801 entries): the words needed for simple everyday communication.
- **Core** (1,982 entries): the words an adult needs for ordinary communication.
- **General** (everything else): words a learner will meet in reading, conversation and media.

The basic and core tiers are closed. Example sentences in basic and core entries are written
with simpler vocabulary.

### What an entry offers

- Glosses and explanatory definitions, sense by sense
- Example sentences that progress from short and simple to longer and more natural
- Usage notes on grammar, register, collocations, commonly confused words and culture
- Furigana on every kanji, which readers can switch on or off
- For verbs: transitivity, the intransitive or transitive partner, how the ている form behaves, and a
  conjugation table
- Tags for part of speech, formality, politeness and meaning
- Links from every word in the examples and notes to that word's entry
- Recorded readings of the example sentences (being added; see [Example audio](#example-audio))

## Using the site

The site is fully static: HTML, CSS and JavaScript, with no server-side code. It counts page
views with GoatCounter, a privacy-friendly counter that sets no cookies.

- **Search** (the home page): look up a word by Japanese, romaji or English.
- **Browse**: entries by the first kana of their reading.
- **Kanji**: every kanji used in headwords, each with a page listing the entries that contain it.
- **Lists**: the basic and core tiers, and entries grouped by subject tag.
- **Articles**: longer explanations of topics such as keigo, counters and onomatopoeia.
- **Recent**: the most recently changed entries, marked **NEW** (a new entry), **REVISED** (its
  text was changed) or **REVISED (audio)** (recordings of its examples were added).
- **Random**: a cloud of randomly chosen headwords for browsing.

Three buttons in the header control what entry pages show: **Examples** (show or hide the example
sentences), **Furigana** (readings above kanji) and **Links** (underline the linked words in
examples and notes). The site remembers these settings in the browser.

Each example sentence has a play button. When the example has a recorded reading, the button
plays it; otherwise it uses the browser's own text-to-speech voice.

## Using the data

Each entry is a JSON file in `entries/`, named `<id>_<romaji>.json` and grouped by ID in
directories of 500 (`entries/00000/`, `entries/00500/`, …). An entry's ID is permanent: it is
also its page's URL (`https://www.tkgje.jp/entries/00000/00426_yomu.html`), so IDs are never
changed or reused. `build/schema.json` defines the format.

An abridged entry:

```json
{
  "id": "00426_yomu",
  "headword": "{読|よ}む",
  "reading": "よむ",
  "part_of_speech": "verb (godan)",
  "gloss": "to read",
  "definitions": [
    {"sense_number": 1, "gloss": "to read",
     "explanation": "To look at and comprehend written text. Used for books, newspapers, signs, emails, and any written material."}
  ],
  "examples": [
    {"id": "00426_yomu_ex1",
     "japanese": "⟦{本|ほん}→本：00111_hon⟧⟦を→を：00422_wo⟧{読|よ}む。",
     "english": "I read a book.",
     "notes": null,
     "has_audio": true,
     "sense_numbers": [1]}
  ],
  "notes": "TRANSITIVITY: ⟦{他動詞|たどうし}→他動詞：10418_tadoushi⟧ (transitive). …",
  "cross_references": [
    {"type": "contrast", "target_id": "26844_hatsuonsuru", "reading": "はつおんする",
     "headword": "{発音|はつおん}する", "label": "to pronounce"}
  ],
  "conjugation": {"…": "…"},
  "metadata": {
    "created": "2026-01-05T12:03:41Z",
    "modified": "2026-09-02T04:00:57Z",
    "vocabulary_tier": "basic",
    "tags": {"pos": ["verb-godan"], "transitivity": "transitive", "formality": "neutral",
             "politeness": "plain", "semantic": ["communication"], "verb_class": "godan-mu"}
  }
}
```

Two kinds of markup appear inside Japanese text:

- **Furigana**: `{漢字|かんじ}` puts the reading かんじ over 漢字.
- **Inline links**: `⟦surface→dictionary form：entry id⟧` marks a word and the entry it links to.
  In `⟦{読|よ}んで→読む：00426_yomu⟧`, the text says 読んで, and the link goes to the entry for 読む.

To get plain text, replace each link with its surface part (the text between `⟦` and `→`), then
each `{漢字|かんじ}` with 漢字 (or with かんじ for a kana reading).

Other data files:

- `entries_index.json`: every entry's ID, headword, reading, gloss and tier.
- `kanji/`: the kanji index (`kanji_list.json` and one file per kanji).
- `articles/`: the articles, as JSON with a markdown body using the same markup.
- `audio/manifest/`: the recorded readings (see below).

## Example audio

Example sentences are being given recorded readings, starting with the basic and core tiers.
Each recording is made by a text-to-speech model (Gemini TTS) and is accepted only after four
automatic checks, using models from different companies, agree that every word was pronounced
as the example's furigana indicate. The MP3 files are kept in a separate repository,
[tkgally/je-dict-audio-1](https://github.com/tkgally/je-dict-audio-1), and served from its
GitHub Pages site.

`audio/manifest/<range>.jsonl` lists every recording: the example ID, a hash of the text that was
recorded, the file's path and the voice used. A recording counts only while the example's text
and furigana are unchanged; when an example is edited, the site falls back to browser speech
until the example is recorded again. An example's `has_audio` field says whether it currently
has a valid recording. The whole workflow, the evidence for it and its changelog are in
[AUDIO_WORKFLOW.md](AUDIO_WORKFLOW.md).

## How the dictionary is made and maintained

The dictionary is written and maintained by Claude in scheduled sessions (Claude Code
"Routines"). Each session follows `prompts/routine2.md`: a selector (`pipeline/routine_next.py`)
chooses one kind of work, such as polishing a batch of entries, a cross-model accuracy review,
a fix for a problem found across many entries, new entries for words the dictionary uses but
does not define, or example audio. The session then:

1. makes its changes following the guidelines in `.claude/skills/`;
2. runs the deterministic passes: note formatting (`build/normalize_notes.py`), inline links
   (`build/auto_link.py`, which uses the SudachiPy morphological analyzer), and cross-references
   named in notes (`build/harvest_crossrefs.py`);
3. has a model from another company review the changed entries (`build/review_accuracy.py` and
   `build/review_links.py`, through OpenRouter) and decides on each point it raises, logging the
   decision in `reviews/decisions.jsonl`;
4. runs the same checks as continuous integration (`make gate`), updates the indexes
   (`make index`) and opens a pull request, which it merges once the checks pass.

When a pull request is merged, GitHub Actions builds the site from the JSON
(`.github/workflows/pages.yml`) and deploys it to GitHub Pages. The generated site is not stored
in the repository.

Tom reads the pull requests and the questions sessions leave for him in
`reviews/needs_curator.txt`.

## Repository layout

```
entries/          The dictionary entries (JSON), 500 per directory
articles/         The articles (JSON)
audio/            Audio manifest, workflow configuration and test data (no audio files)
kanji/            Kanji index data
build/            Site build, validation, deterministic passes, review tools, unit tests
  schema.json       Entry format
  data/             Controlled vocabularies and baselines used by the checks
  templates/        Site CSS and JavaScript
  tests/            Unit tests
  COMMANDS.md       Every command, grouped by task
prompts/          Instructions for the scheduled sessions (routine2.md and its mode prompts)
pipeline/         Session selector, metrics and spending ledgers
.claude/skills/   Editorial guidelines by entry type
planning/wiki/    Research notes on Japanese lexicography and the project backlog
polishing/        Progress of the polishing passes, session logs, observations
reviews/          Review decisions, accuracy flags, questions for the editor
.github/workflows CI checks on pull requests; site build and deployment
```

`CLAUDE.md` is the working guide for Claude sessions; `PROJECT_STATUS.md` records recent history.

## Building the site locally

Python 3.10 or later is needed.

```bash
pip install -r build/requirements.txt
make build                 # validate, update indexes, generate the site in docs/
open docs/index.html       # or open the file in any browser; no web server is needed
make gate                  # the checks CI runs on a pull request (unit tests, validation)
```

The audio tools need extra packages (`make audio-deps`) and an OpenRouter API key; the site
build does not.

## Contact

Suggestions and corrections are welcome: write to [Tom Gally](https://www.gally.net/about.html).
