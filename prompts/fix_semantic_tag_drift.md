# Fix Semantic Tag Drift (Cleanup P11 / Tooling item 6)

> **Note (2026-09-02):** this prompt predates the current process. Where it says `make build` or
> to commit `docs/`, run `make index` instead — the site is built by GitHub Actions after the merge
> and `docs/` is no longer tracked. Where it says to place inline links or `noentry` markers by hand,
> run `python3 build/auto_link.py --ids <ids> --apply` instead and add missing words as candidates.
> The scheduled Routine is `prompts/routine2.md`; see `enhancement/assessment-2026-09-02.md`.

Drive the dictionary-wide remediation of **semantic-tag-vs-headword drift** — the
pervasive batch-creation error where a word carries a semantic tag that has
nothing to do with its meaning (一期一会 → `furniture`, 朱肉 → `animal-mammal`,
障子 → `communication`). See `planning/wiki/ideas/cleanup-backlog.md` → Priority 11
for the full history and `planning/wiki/topics/schema-tag-reliability.md` for why
it happens.

This task pairs two **high-precision read-only detectors** with the **accuracy-review
`tags` pass** so that the cheap-and-certain fixes happen mechanically-verified and
the subtle ones get a cross-model second opinion. It is designed to be run
repeatedly on a schedule and to converge.

> **The cardinal rule: never retag mechanically.** P11 was *caused* by mechanical
> tag assignment (tags copied from example-sentence topics, or from an unrelated
> entry, with no one reading the word). Every tag you change must be decided by
> reading **that entry's** headword, gloss, and notes. The detectors only tell you
> *where to look*; they never tell you what the answer is. When in doubt, verify.

---

## How this slots into the Routine

This prompt is a **`systemic-fix`** lane (deterministic detector queues) that hands
off to the **`accuracy-review`** lane (LLM `tags` pass) for the cases detectors
cannot catch. A scheduled Routine reaches it two ways:

- **As `systemic-fix`**: the selector picks `tag-concrete-noun-domain-mismatch` or
  `tag-proverb-idiom-mismatch` from `planning/wiki/ideas/backlog-queue.json`
  (`prompts/routine2.md` §B). Do **Phase 1** below for that one check, then wrap up.
- **As `accuracy-review`**: when the selector picks `accuracy-review`
  (`prompts/routine2.md` §A) and you want to front-load the contaminated block,
  do **Phase 2** below over the cursor range.

Run **standalone** (manual / `claude --print`) to do a full pass: Phase 1 (both
detector checks) then Phase 2 (cursor range), then the shared wrap-up.

---

## Starting point — the progress cursor

```bash
cat polishing/tasks/semantic-tag-drift/progress.txt   # e.g. "next: 06341"
```

If the file is missing, create it with `next: 05700` — the cursor **front-loads
the 5700–6340 block**, the highest-density P11 pocket measured to date (Cleanup
P11 update 2026-06-17). The cursor governs **Phase 2** (the sequential hand pass);
Phase 1 (detector queues) is dictionary-wide and not cursor-bound.

---

## Phase 1 — deterministic high-precision checks (do these first)

Two checks in `build/check_tag_drift.py`, in this order (highest precision first).
Both are read-only and emit a JSON review queue; add `--cohort` to restrict to the
contaminated `claude-opus-4-5` batch, or `--range A B` to scope by ID.

### 1a. `proverb-idiom-mismatch` (~93% precision)

```bash
python3 build/check_tag_drift.py --check proverb-idiom-mismatch --json
```

Flags a **proverb / yojijukugo / set-expression** headword tagged with a
physical-object/creature domain (`furniture`, `clothing`, `electronics`, `food`,
`animal-*`) that has no keyword support — the 一期一会/四苦八苦/起死回生 → `furniture`
family. For each flagged entry:

1. Open it. Confirm from the headword/gloss/notes that it **is** a proverb,
   four-character idiom (四字熟語), or set phrase.
2. Replace the object-domain tag with **`idiom`** (figurative set phrases, body
   idioms like 肩をすくめる, most yojijukugo) or **`proverb`** (full aphorisms /
   sayings). Keep a genuinely-applicable abstract co-tag (`emotion` on 厚顔無恥) and
   drop the rest. Grammatical set phrases (に伴い) take **`grammatical`**.
3. If the entry turns out to be a compositional compound that genuinely belongs to
   the object domain (rare — the keyword filter usually spares these), **reject**
   the flag and leave it.

### 1b. `concrete-noun-domain-mismatch` (~77% precision)

```bash
python3 build/check_tag_drift.py --check concrete-noun-domain-mismatch --json
```

Flags a **non-verb headword carrying ≥2 mutually-distant hard physical-object
domains** — the batch garbage multi-tag signature (横断歩道 →
`animal-mammal`+`clothing`+`transportation`; 油絵 → `body-part`+`tool`). For each:

1. Open it. Decide the **single** object domain the headword actually belongs to.
2. Drop the unrelated object-domain tag(s); set the semantic list to the correct
   domain (油絵 → `art`; 打席 → `sports`; ぞ → `grammatical`; 食器棚 → `furniture`).
3. **KEEP genuine polysemy.** The known false-positive family is loanword /
   accessory / fixture polysemy where both tags are correct: マウス (`animal-mammal`
   the rodent + `electronics` the device), 腕時計, ショルダーバッグ, 車席, 電話ボックス,
   化粧ポーチ. If reading the entry shows both domains genuinely apply, **reject**
   the flag and leave the tags. Do not force a single tag onto a real dual-domain
   word.

> The keyword `--check semantic-mismatch` is **experimental / noisy** (it flags
> boat=transportation, school=building). Do **not** drive a fix from it; use the
> two checks above and Phase 2.

---

## Phase 2 — accuracy-review `tags` pass (the cases detectors cannot catch)

The detectors above catch only the *mechanically visible* drift: object tags on
idioms, and garbage multi-tag clusters. They **cannot** catch a **single
in-list-but-wrong-category tag** (朱肉 → `animal-mammal` as the *sole* tag; 障子 →
`communication`) — there is no keyword or structural signal, only meaning. Those
need a model that judges each tag against the headword. That is the
**accuracy-review `tags` dimension** (`planning/wiki/topics/quality-metrics.md`
measures `tags` as the highest-precision review lane, ~6.8% apply rate).

Walk the cursor range (start at `next:`, front-loading 5700–6340), sized to the
§6 budget rule (below):

```bash
python3 build/review_accuracy.py --range <start> <end> --dimensions tags --budget <cap>
```

For each `reviews/accuracy/{id}.json`, **APPLY / REJECT / FLAG** per `routine2.md`
§A step 4 and the **semantic-tag policy**:

- A flag that a tag is **not in `VALID_SEMANTIC`** is correct by definition →
  **APPLY** the migration (`build/check_tag_drift.py` has the 1:1 map).
- A **wrong-domain in-list tag** (the P11 core: `animal-mammal` on an ink pad) →
  open the entry, confirm, **APPLY**.
- A **"too narrow/too broad" in-list substitution** (`general`→specific,
  `education`→`cognition`) is editorial noise → **REJECT**. `general`, `descriptive`,
  `action`, `expression` are valid fallback tags.
- Genuine uncertainty → **FLAG** to `reviews/needs_curator.txt`.

**Log every adjudication** to `reviews/decisions.jsonl` (`routine2.md` §C;
`src:"accuracy"`, `dim:"tags"`). Bulk-reject a recurring noise family with one
aggregated line. **Skip Phase 2 entirely if `params.openrouter_session_budget_usd`
is 0/missing** (daily cap spent) — do Phase 1 only.

Even without the budget, you can hand-walk the cursor range yourself: open each
entry carrying a concrete-object semantic tag and confirm it matches the headword.
This is slower but free, and it is exactly the per-entry verification the cardinal
rule demands.

---

## Batch sizing (the §6 context rule)

Process a **bounded** batch, not the whole queue. Plan to finish the content work
by ~55% of your context window; the wrap-up (self-check, build, PR, merge) needs
~40% headroom. In practice that is roughly **50–80 verified entries per run**
(detector flags are quick; the accuracy-review adjudication is the slow part —
shrink the range if it runs long). Better one fewer entry than a stranded PR.

Each entry you change: update its `metadata.modified` timestamp
(`python3 build/get_timestamp.py`).

---

## Self-check your own changes (`routine2.md` §4)

After the content work and **before** `make build`, send exactly the entries you
changed to an independent model and adjudicate:

```bash
git status --porcelain -- entries/ | sed -E 's/^.{3}//' | sed -E 's|.*/([0-9]{5})_.*|\1|' | sort -u
python3 build/review_accuracy.py --ids <id1,id2,...> --budget 0.25
```

One verification pass, one fix round, then stop (no ping-pong). Adjudicate per §C;
log each decision to `reviews/decisions.jsonl` with `src:"self-check"`. If budget
< $0.05, note "self-check skipped: budget" and continue. A clean self-check is the
expected steady state — say so in the log.

---

## Metrics snapshot (`routine2.md` §5)

Just before writing the session log:

```bash
python3 pipeline/metrics_snapshot.py --mode systemic-fix --changed <N entries changed>
```

(Use `--mode accuracy-review` if this run was the Phase 2 lane.) Never let metrics
block the wrap-up — note and continue if it errors.

---

## Wrap up

1. **Advance the cursor.** Set `polishing/tasks/semantic-tag-drift/progress.txt`
   to `next: <first un-reviewed ID after the range you hand-walked in Phase 2>`.
   (Phase-1-only runs that did not walk a range leave the cursor unchanged.)
2. **Update the backlog item(s)** you drained in `backlog-queue.json`
   (`tag-proverb-idiom-mismatch`, `tag-concrete-noun-domain-mismatch`): refresh
   `scope_estimate` from a fresh `--summary`, and mark `status:"resolved"` only if
   a check returns 0 dictionary-wide *and* you judge no new entries will
   reintroduce it (otherwise keep it open as a standing check). Mirror any status
   change into the Cleanup P11 prose page.
3. **Write a session log** `polishing/sessions/semantic-tag-drift_{YYYY-MM-DD}_{NNN}.md`:
   checks run, entries changed (id: old → new tags), flags rejected (with reason),
   self-check outcome, and the next cursor value.
4. **Build, commit, PR, merge** — the standard atomic tail (`routine2.md` §7, MCP
   path): `make build` once → `git add -A && git commit` → push → create PR →
   poll `mcp__github__pull_request_read` `method: "get_check_runs"` until green
   (backgrounded `sleep 30` between polls; `wait-for-pr-checks.sh` 403s here) →
   squash-merge. Leave the PR open on any non-green result; the next run's §0a
   rescue completes it.

---

## Always-on capture (`routine2.md` §3)

- Any Japanese word you meet without an entry → `python3 build/manage_candidates.py
  add "言葉" "ことば" "gloss; seen in entry XXXXX"`.
- Any systemic observation (a new drift sub-pattern, a detector false-positive
  family, a tag-vocabulary gap) → append to `polishing/observations.md` with the
  right tag (`[pattern] [tooling] [skill] [entry]`).

## Reference — valid semantic tags

The single source of truth is `VALID_SEMANTIC` in `build/validate_tags.py` (also
in the `entry-guidelines` skill and the `polish_semantic_labels.md` table). After
your changes, `python3 build/validate_tags.py` must report **no new** "Unknown
semantic tag" warnings for the IDs you touched. Common correct destinations for
P11 fixes: idioms/yojijukugo → `idiom`/`proverb`; particles/conjunctions →
`grammatical`; mimetic adverbs → `descriptive`/`onomatopoeia`; internal organs →
`body-internal`; sports terms → `sports`; performing arts → `art`; abstract
business nouns → `business`/`work`.
