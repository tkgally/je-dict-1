# Session log: candidate-queue overhaul — 2026-08-11 (001)

**Type**: curator-directed session (not a Routine run)
**Branch**: claude/candidate-word-queue-refresh-z50v8v
**Request**: devise a new candidate-discovery workflow, wire it into the
Routine, clean up the junk queue, and bring proper nouns into scope with new
semantic categories.

## What was done

### 1. Queue cleanup
- `manage_candidates.py sync` first (0 removals), then removed **all 964
  corpus-harvested candidates** (added 2026-02 through 2026-05). Full list
  with heuristic reason labels archived to
  `planning/archive/candidate-cleanup-2026-08-11.json`
  (821 failed-headword-vetting, 66 number/counter combinations,
  41 conjugated/derived forms, 25 compositional phrases,
  11 non-Japanese/malformed).
- Kept the 5 vetted 2026-08 "seen in entry" candidates (夏目漱石,
  コインロッカー, 制限時間, 五人囃子, 三つ肴).
- Basis: my read-through of all 969 rows confirmed the six-run escalation —
  coinages (権使, 些道, 個尊), free phrases (静かに歩く), inflected forms
  (強く, 知らない), number+counter items (三歳, 二百), wrong glosses
  (アンパッサン "ice cream sundae"; 箱根 "box-shaped mountain"; 火虫
  "firefly"). Salvageable material was re-added in correct lemma form during
  the restock (e.g. 早食べ→早食い was proposed; 早食い turned out to
  already have an entry).

### 2. New verified-restock workflow
- `.claude/skills/find-candidates/SKILL.md` rewritten: generate from lexical
  knowledge aimed by gap data; vetting gates G1–G7 (real word, lemma form,
  headword-worthy unit, correct reading, correct gloss, learner value,
  proper-noun richness); ten discovery lenses; when in doubt, skip.
- `prompts/newcandidates.md` rewritten as the run playbook (now the Routine's
  `candidates` mode): read gap data → pick 3–5 lenses → generate ~1.5× →
  vet → `add-batch` → one self-check pass.
- `build/manage_candidates.py`: new `add-batch <file.json>` (per-row
  duplicate checks, loads the entries index once) and `remove <id>...`
  subcommands. `clean_up_candidates_list.md`'s broken `remove word reading`
  instruction fixed to use IDs.
- `prompts/corpus_harvesting.md` deprecated (banner added);
  `pipeline/README.md` recommendation updated; the no-proper-noun lines in
  `build/brainstorm_candidates.py` and `brainstorming/start_prompt.md`
  replaced with the new policy.

### 3. Proper nouns in scope + semantic categories
- Policy: proper nouns learners should know are valid headwords, prioritizing
  collocationally/semantically rich names (fixed expressions, metonymy,
  cultural-literacy load, navigation value). Documented in the
  find-candidates skill, `prompts/newentries.md` ("Proper-Noun Entries"),
  entry-guidelines and other-entries skills.
- `VALID_SEMANTIC` (build/validate_tags.py) gained 7 tags: `proper-noun`
  umbrella + `place-name`, `person-name`, `organization-name`, `work-name`,
  `event-name`, `brand-name`. Pairing enforced: subcategory without umbrella
  = error; umbrella without subcategory = warning. Conventions:
  `part_of_speech` "noun (proper)", `metadata.tags.pos` ["noun"].
- **56 existing proper-noun entries retro-tagged** (44 place names incl.
  日本×2/東京/富士山/countries/regions; 甲子園 as place+event; orgs 国連,
  東大, NHK, JR, 日本銀行, 日銀; events 芥川賞, 直木賞, 紅白歌合戦,
  明治維新; person 聖徳太子; work 万葉集). ヨーロッパ's off-vocab `place`
  tag migrated to `geography` in the same pass.

### 4. `candidates` Routine mode
- `pipeline/routine_next.py`: sixth mode, weight 0.10; hard-suppressed while
  queue ≥ `candidate_restock_threshold` (150); ×1.5 boost below the low
  threshold (80); in `anti_repeat_modes`; params `{approx_new: 40–60,
  queue_count}`. The new-entries "candidates low" nudge reason updated (no
  longer "curator tops up manually").
- `pipeline/routine-config.json`, `pipeline/metrics_snapshot.py`
  (VALID_MODES), `prompts/routine2.md` (§2 dispatch row, §7 cursor note,
  intro), and `CLAUDE.md` updated to match.
- `build/tests/test_routine_next.py`: 4 new tests (suppression, activation,
  boost, params); neutral fixture moved to candidate_count=120. 16/16 pass.
- Live check: with the queue at 5, the selector boosts candidates
  (~13% of simulated runs) and damps new-entries; other modes undisturbed.

### 5. First restock (the new workflow's first execution)
- 146 proposals generated and individually vetted; 88 added, 58 skipped by
  the duplicate checker (51 already had entries — evidence the dictionary's
  common-word coverage is deep and proper nouns were the real gap; 7 were
  within-batch or candidate matches).
- Added: 73 proper nouns (40 places incl. 新宿/渋谷/銀座/山手線/関ヶ原/
  箱根/伊勢/出雲 and major countries/cities; 17 persons incl. 紫式部,
  織田信長, 福沢諭吉, 芥川龍之介, 手塚治虫; 11 organizations incl. トヨタ,
  ユニクロ, 朝日新聞, ジブリ; 5 works incl. 源氏物語, ドラえもん,
  サザエさん; ポケモン as brand; 箱根駅伝 as event) + 15 common words
  (擦り寄る, 手薄, 底力, 匙を投げる, 油を売る, 渡りに船, 棚からぼたもち,
  餅は餅屋, 火の車, 自転車操業, 芋づる式, 適材適所, 玉石混交, 有耶無耶,
  好循環).
- Self-check pass done (readings re-verified; no removals needed).
- **Queue: 93, every word vetted and entry-ready.**

## Notes for future runs
- 日光/にっこう the place cannot enter the queue: entry 03515 covers
  "sunlight" with the same written form and reading, and the duplicate rule
  blocks exact word+reading matches. Adding a Nikko sense to 03515 is a
  polish/curator decision (logged as an [entry] observation).
- The proper-noun lens remains fertile: unadded ideas include 上海,
  シンガポール, remaining countries (オランダ, トルコ…), 東京タワー,
  スカイツリー, 道頓堀, 太宰治's works, Suica/LINE (blocked or messy
  headword questions — スイカ collides with the fruit).
- Next selector run: queue 93 → candidates mode active (no boost),
  new-entries undamped. After ~2 new-entries runs the boost kicks in below
  80 unless a restock fires first.
