# Candidate Restock (the Routine's `candidates` mode)

Restock `candidate_words.json`, the queue the `new-entries` mode draws from. Since 2026-10-23
the queue has two streams, and every run works both:

1. **Internal closure**: words the dictionary already uses in examples or notes but has never
   defined, so that a learner who meets a word inside an entry can look it up.
2. **Brainstorming**: words that should be in a learner's dictionary and are not, found by
   thinking outward from the headwords the dictionary already has (synonyms, antonyms, words of
   the same kind, compounds and set phrases, register counterparts, culturally important proper
   names) and by asking what is missing from each semantic field. Tom asked for this on
   2026-10-23: the brainstorm on the first seeds found the particles さえ and すら, あり得る and
   ある程度 missing, and a field pass on birds found フラミンゴ, ペリカン, 七面鳥 and ダチョウ.

Every word comes from knowledge of Japanese (yours and other models'), **never from an existing
dictionary or word list** (Tom's rule). Every word is vetted one by one against the
`find-candidates` gates before it is added.

Runs as `prompts/routine2.md`'s `candidates` mode when the queue falls below the restock
threshold (200). `params.approx_new` is the target (40–80); about a third should come from
closure while it has depth, the rest from brainstorming. `params.openrouter_session_budget_usd`
caps the model calls (at most $0.50).

## Stream 1: internal closure (about a third of the target)

1. **Words marked as missing inside entries.**
   ```bash
   python3 build/check_stale_noentry.py --json > /tmp/stale.json
   ```
   Take the `unresolved` class, ranked by `instances`. Skip suffixes and prefixes standing alone
   (権, 化, 系), number-plus-counter strings (三冊), inflected or partial forms, proper nouns of no
   cultural weight, and variant spellings of existing entries.
2. **Words the reviewer or a polish run noticed**: `[entry]` lines in
   `polishing/observations.md` and recent session logs.
3. **Unlinked words in example text**: words in examples that the linker left bare because no
   entry exists (most hits are other spellings of existing entries; skip those).

Notes for this stream say `seen in entry NNNNN`.

## Stream 2: brainstorming (the rest)

The tool serves one batch per run and alternates two lenses: **seeds** (the next 20 headwords
in tier order, basic first) and **field** (one semantic field with the words the dictionary
already has in it, proper-name fields included).

```bash
python3 build/brainstorm_candidates.py next > /tmp/bs_batch.json
```

1. **Your own brainstorm first**, before reading any model's list (so you are not anchored).
   For a seeds batch, for each headword think of: synonyms and near-synonyms; antonyms and
   opposites; other members of the same category; broader and narrower words; established
   compounds, set phrases and idioms built on it; formal, casual, honorific and humble
   counterparts; culturally important proper names closely tied to it (places, people, works,
   events, organizations with cultural weight; see the find-candidates skill). For a field
   batch, read the member list and name the common words a learner would miss first. Write
   them to `/tmp/bs_own.json` as
   `[{"word": "…", "reading": "…", "gloss": "…", "relation": "antonym", "seed_id": "00006_aru", "by": "self"}]`.
2. **Independent models** (skip if the budget is under $0.05):
   ```bash
   python3 build/brainstorm_candidates.py ask /tmp/bs_batch.json --out /tmp/bs_models.json --budget <params.openrouter_session_budget_usd>
   ```
   It asks `openai/gpt-6.1-sol` and `google/gemini-3.8-flash` the same question, prints
   `EST_COST=` (billed, about $0.05–0.10 a batch) and records the spend in
   `pipeline/openrouter-ledger.json` itself (mode `candidates`).
3. **Merge and filter**:
   ```bash
   python3 build/brainstorm_candidates.py filter /tmp/bs_own.json /tmp/bs_models.json --out /tmp/bs_new.json
   ```
   It drops entries, candidates, retired IDs and anything an earlier run rejected, and prints
   counts. In what remains, `by` lists who proposed it (agreement ranks first),
   `possible_variant_of` names an existing entry with the same reading that may be the same
   word in another spelling (usually drop it: 出掛ける when 出かける exists), and `alt_spellings`
   groups proposals that are one word in several spellings (keep one: the spelling the word is
   usually written in, katakana for most birds and animals, ダチョウ not 駝鳥).
4. **Vet each survivor** against gates G1–G7 of the `find-candidates` skill. Models propose
   rare or bookish words, words that do not exist in that form, and free phrases; when in doubt,
   leave it out. Usefulness 1 words need a reason to stay.

Notes for this stream name the lens and the link to an existing entry, so `new-entries` can
cross-reference them: `brainstorm: antonym of 00204 数`, `brainstorm: same category as 00001 鳥`,
`brainstorm: field animal-bird`. Proper nouns keep the `proper noun (place | person | …)` marker.

## Workflow

1. Load the `find-candidates` skill (gates G1–G7).
2. Run both streams to a proposal list of about 1.5× the target.
3. **Probe first, then vet.** For stream 1 (stream 2's filter already did this):
   ```bash
   python3 build/check_duplicate.py --batch --skip-candidates 'word:reading' 'word:reading' …
   ```
4. Vet each survivor: real, lemma-form, headword-worthy, correct hiragana reading, correct
   gloss, learner value.
5. Write the survivors to a scratch JSON file outside the repo:
   ```json
   [{"word": "湯呑", "reading": "ゆのみ", "notes": "teacup (handleless); seen in entry 05612"},
    {"word": "数少ない", "reading": "かずすくない", "notes": "few, scarce; brainstorm: compound of 00204 数"}]
   ```
6. Batch-add with automatic duplicate checking:
   ```bash
   python3 build/manage_candidates.py add-batch <scratch-file>.json
   ```
7. **Record the brainstorm verdicts** (every stream-2 proposal you vetted, added or rejected),
   which also advances the lens cursor:
   ```bash
   python3 build/brainstorm_candidates.py record /tmp/bs_batch.json /tmp/bs_verdicts.json
   ```
   `/tmp/bs_verdicts.json` is `[{"word": "…", "reading": "…", "verdict": "added" | "rejected", "reason": "…"}]`.
   Rejected words are not proposed to you again. Proposals dropped as existing entries need no
   verdict.
8. Re-read `git diff candidate_words.json` once and remove any slip
   (`manage_candidates.py remove C12345`). One pass, no ping-pong.
9. Wrap up per routine2.md §5–§7 (update PROJECT_STATUS.md Recent Changes, `make index`,
   commit, push, PR, merge).

## Quality bar

- Real, stable, lemma-form headwords with correct readings and glosses; useful to intermediate
  learners; general tier.
- Not: bulk-extracted lists, uncertain words, conjugated or derived forms, free phrases,
  number+counter strings, ephemeral slang, vulgar or discriminatory terms, archaic or dialect
  items, hyper-specialized jargon (most bird species beyond the familiar ones; most technical
  terms of a field).

## Report

At the end: proposed / added / rejected, per stream; for stream 2 the lens and batch (seeds
and their range, or the field), how many proposals each source made and how many survived;
queue total.
