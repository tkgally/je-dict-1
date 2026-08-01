# Cleanup Backlog

**Last updated**: 2026-07-27 (wiki harvest of the 17 loose observations from the 2026-07-27 polish, systemic-fix and accuracy-review runs — one **new priority** plus three cohort extensions: **new P28** — mixed bullet markers inside `notes`, the older `・` convention measured dictionary-wide at **18,272 line-initial instances across 2,524 entries** (~1/12 of the dictionary), normalizable by a doubly-anchored rule (line-initial AND inside `notes` only, since `・` is real punctuation elsewhere) but sequenced behind a sample check rather than swept blind. **P20** — the off-vocab band measured at **124 of 250 entries (49.6%)** in 19701–19950 (143 occurrences / 83 distinct off-list tags), with the operational finding that **the model is the wrong instrument**: the large families are 1:1 synonym renames `check_tag_drift.py`'s `TAG_MIGRATION` covers only nine of, so the ~50 safe renames belong in the map and only the ~7% judgment-dependent residue belongs in a review. **P17** — a seventh formality sub-family, 〜甲斐 nouns auto-tagged `informal` (06653/06654), notable for being a *morphological* cluster and therefore an unusually cheap detector cut. **P21** — the zero-link band unbroken through **06655**, with `・` bullets co-occurring in the same notes fields, now cross-linked to P28.) Prior 2026-07-26

Concrete cleanup work items surfaced during comprehensive-polish sessions. Each item describes a systemic pattern that affects multiple entries and could be addressed by a dedicated batch pass.

**As of 2026-06-09**, the batch-addressable items here are also indexed in machine-readable form at [`backlog-queue.json`](backlog-queue.json), which the unified Routine's `systemic-fix` mode (`prompts/routine2.md` §B) drains one bounded, per-entry-verified batch at a time. Read-only detectors back the queue: `build/check_furigana_format.py` (P9, P12), `build/check_artifacts.py` (P16, P15, P10, P4, P2), and `build/check_tag_drift.py` (P6, P7, P13, P20; plus the two high-precision P11 checks `proverb-idiom-mismatch` and `concrete-noun-domain-mismatch` shipped 2026-06-17, with `semantic-mismatch` kept experimental). Keep `backlog-queue.json` in sync with this page during wiki maintenance.

## Priority 1: Unlinked notes in older entries

**Source**: Comprehensive-polish sessions 2026-05-08 through 2026-05-09 (entries 00006–00096)
**Scope**: Virtually every entry in the January–February 2026 creation cohort

Older noun entries have linked example sentences but **unlinked notes**. Structured lists in `notes` (Common Collocations, Related Words, Types of X, Compounds, Similar Words) use bare `{kanji|reading}` without `⟦...⟧` wrappers. This is confirmed as the single most common tier-1 polish deficit for entries below ~00100, and likely extends through most pre-March 2026 entries.

The inline-links polishing task (`polishing/tasks/inline-links/progress.txt`) at entry 02730 is the primary mechanism addressing this, but comprehensive-polish sessions are also fixing entries as they encounter them starting from entry 00001.

As of comprehensive-polish session 2026-05-18 (entries 02101–02125), **particle links** (は, が, を, に, で, と in pattern examples) are now the primary remaining inline-link gap in the entry range being polished. This is a sub-case of the unlinked-notes problem: structured pattern sections use bare particles without `⟦...⟧` wrappers.

## Priority 2: Missing or broken cross-references

**Source**: Comprehensive-polish sessions 2026-05-08 through 2026-05-09

Two related sub-issues:

1. **Under-populated cross_references**: Entries mention obvious neighbors in notes but have no `cross_references` entries for them. Examples: 00010_banchi → 住所/丁目/号; 00014_biyou → 美容院/美容師/健康; 00018_booto → 船/ヨット/カヌー.

2. **Structurally invalid cross_references**: Some entries have cross-reference objects with `headword`/`reading` but no `target_id` field (e.g., 00041_fudan → 通常, 00065_genni → 実際に, 00069_gesui → 上水). `validate.py` emits a "Note" rather than an error for these, so they persist silently.

3. **Missing field entirely**: 09491_choume was missing the `cross_references` field altogether, not just having it empty. The symmetry checker may silently skip such entries.

**Suggested actions**:
- One-shot scanner listing every cross_references entry without `target_id`
- Consider `validate.py --strict` mode promoting "missing target_id" notes to errors
- Confirm `check_consistency.py` flags entries lacking the `cross_references` field

**Update 2026-06-17 (systemic-fix run)**: `build/check_artifacts.py --issue missing-target-id` now exists as the scanner (190 dangling refs across 180 entries at run start). This run filled `target_id` on the 54 refs whose **headword AND reading both** uniquely match an existing entry — the provably-correct subset where a real link had simply lost its id (antonym pairs like 12053_jigoku→天国, transitivity pairs like 00001_amaru→27283_amasu, same-kanji homophone triplets like 20859_atsui→厚い/暑い/熱い). Detector down to 136. **Caution learned this run**: a `by_reading` fallback is unsafe (homophone confusions: 有限/ゆうげん matched 幽玄, 小学/しょうがく matched 少額) — only fill `target_id` on exact headword+reading matches. The remaining 136 are "headword has no entry" cases; some are *deliberate* homophone/contrast pointers (e.g. 00250_kufuu → 工夫/こうふ "laborer (homophone)") that should be kept, not dropped. A future run must verify each before dropping.

**Update 2026-06-19 (systemic-fix run)**: detector 136 → 96. Resolved 40 refs across 37 entries: (a) **22 vestigial `id` → `target_id`** — 26 of the 136 refs carried a non-schema `id` field that the renderer ignores (it reads `target_id` only); promoted the 22 whose `id` pointed to a live entry; (b) **4 stale-`id` repoints** — pre-renumber ids 01040_shinjin/02032_tenkin/00373_ondo/00213_gaikokujin → 02500_shinjin/04555_tenkin/00333_ondo/02869_gaikokujin (resolved by exact headword+reading); (c) **14 reading/surface-verified additions** — reciprocal kana antonym pairs (24277↔24278 夏鳥/冬鳥, 26648↔26649 薄/濃灰色, 26896↔26897 水/海域, 25791↔25792 最高/最低点) and same-word kanji variants (03409 堪えられない→27249 耐えられない, 07148 満ち潮→28112 満潮, 10540 交じる→02421 混じる). All 37 self-checked via the furigana screener — clean (6 flags, all partial-reading/misparse false positives, rejected). **The remaining 96 are mostly legitimate target-less refs**: the referenced word has no entry, and many are *intentional* homophone/contrast/antonym display labels (00250 工夫/こうふ, 17797 侯爵, 00296 有限) that must be **kept, not dropped**. Captured 14 entry-worthy referenced words as candidates (有限, 低温, 高地, 父性, 答申, 近刊, 避寒, 能動, 好天, 独創, 大食, 実名, 車外, 小学). **Two tooling follow-ups** (see observations 2026-06-19): the detector should exclude `type=homophone`/`contrast` (or labeled) refs whose reading has no entry so the queue converges; and the build-time by-reading fallback should require a headword-surface match (it would mis-resolve 04026's `〜着` arrival sense to the clothing counter 27655_chaku).

**Update 2026-06-20 (systemic-fix run)**: detector 96 → 82. **The 2026-06-19 → 2026-06-20 loop closed**: 13 of last run's captured candidates (有限/小学/独創/実名/能動/低温/高地/父性/好天/近刊/避寒/大食/答申) were created by the curator as entries **29338–29351**, so this run filled their `target_id` by provably-correct exact headword+reading match (00296→29338_yuugen, 03477→29351_shougaku, 06242→29347_dokusou, 11797→29349_jitsumei, 12070→29345_noudou, 14705→29339_teion, 15551→29340_kouchi, 15688→29341_fusei, 16184→29346_kouten, 16466→29343_kinkan, 16476→29344_hikan, 16900→29348_taishoku, 17729→29342_toushin). Each target read and semantically confirmed (all antonym/related pairs). Self-checked all 13 via the furigana screener — clean (2 false-positive flags rejected: model misread どくそうてき; 毎年=まいとし is a valid reading). Captured 4 more entry-worthy referenced antonyms as candidates (悪徳/急減/軟質/一神教). **The remaining 82 are overwhelmingly intentional target-less pointers** — the referenced word has no entry and the ref is a homophone/contrast/antonym display label that must be kept. The detector now mostly re-surfaces these permanent pointers each run; the tooling follow-up above (exclude `type=homophone`/`contrast`/labeled refs with no-entry reading) is the way to make this queue actually converge rather than hover near 80.

**Update 2026-06-21 (systemic-fix run) — RESOLVED.** detector 82 → 0 (default). Two things this run: (1) **Filled the last 5 resolvable refs** — another curator restock created 29368–29383, so 06214→29383_nekonikoban (猫に小判, synonym proverb), 12651→29371_isshinkyou (一神教), 12671→29369_kyuugen (急減), 13899→29368_akutoku (悪徳), 16910→29370_nanshitsu (軟質), all exact headword+reading matches, each target read and semantically confirmed (antonym/synonym pairs). Self-checked the 5 via the furigana screener — clean (1 false positive rejected: model claimed 大切→たいせ, but the furigana is correctly たいせつ). (2) **Implemented the convergence follow-up**: `check_artifacts.py --issue missing-target-id` now flags **only refs whose referenced word actually has an entry** (resolvable = some entry shares the ref's reading *and* furigana-stripped surface). Intentional target-less pointers — homophone notes, antonym/contrast display labels, transitivity-pair pointers to words with no entry — are no longer re-surfaced every run. `--include-intentional` restores the full audit list (77 such pointers as of this run). With 0 resolvable refs remaining dictionary-wide and the detector converged, **this item is closed**; it will only re-open if a future ref's referenced word gains an entry (the detector will catch it automatically). Captured 10 more entry-worthy referenced words as candidates (妊娠する, 創造する, 肯定する, 推薦する, 企画する, 罷免, 悪者, 対義語, 鎮める, 取り付く).

## Priority 3: Cross-reference symmetry on thematic clusters

**Source**: Comprehensive-polish 2026-05-09 session 002

Back-link symmetry on thematic clusters (school types, family terms, time expressions, ceremony types) is poor. Example: 00055_gakkou ↔ 01055_shougakkou/01083_koukou had no back-links until manually fixed.

**Suggested action**: High-leverage one-shot batch — pick a cluster, ensure every member references its main parent term. `check_semantic_clusters.py` partially addresses this but focuses on transitivity/antonym/keigo clusters rather than thematic groupings.

**Update 2026-07-20 (a concrete new cluster — traditional children's games)**: A 2026-07-20 routine polish run (frontier 06553–06558) surfaced a well-defined thematic cluster with poor mutual back-linking: the **traditional children's-games** entries — お手玉 (06556), けん玉 (06523), 竹馬 (06557), 独楽 (10104), 凧揚げ (07128), あみだくじ (06554), くじ引き (06555) — **reference each other in their notes but carry few or no mutual `related` cross_references**. This is exactly the thematic-grouping gap this priority describes (analogous to the weekday cluster noted 2026-06-23 under [P2](#priority-2-missing-or-broken-cross-references) / Entry Follow-ups): the members are semantically adjacent and already co-cited in prose, so a bounded one-shot `related`-cross-reference pass over the seven would improve navigability at low risk. Ready as a small targeted batch (no detector needed — the member list is enumerated here).

## Priority 4: Duplicate conjugation keys in verb JSON

**Source**: Comprehensive-polish 2026-05-08 session 001

Many verb entries have two `"conjugation":` top-level keys: a legacy stub (e.g., `{"type":"godan","ending":"る","stem":"…"}`) plus the full conjugation table appended later by `add_conjugations.py`. JSON parsers silently take the last value, so runtime behavior is correct, but the dead stub wastes space and is confusing. Confirmed on 00001_amaru, 00002_amu, 00004_aogu, 07924_aoru; not present on 00006_aru. Likely affects most verb entries predating the conjugation-table retrofit.

**Suggested action**: See tooling-backlog for the pruning script proposal.

**Update 2026-05-21/22**: Comprehensive-polish sessions 2026-05-21 (entries 02559–02583 and 02670–02696) confirmed the duplicate-conjugation-key pattern extends well beyond the originally identified entries. Entries 02560, 02567, 02568, 02574, 02576, 02582, 02688, 02693, 02696 all had the old-format (`prefix`/`stem`/`ending`) stub followed by the correct `forms`-array block. The pattern is likely pervasive across all pre-retrofit verb entries. Reinforces the case for the batch pruner in [Tooling Backlog](tooling-backlog.md) → item 1.

**Update 2026-05-23**: Session 005 (entries 03056–03077) found the same pattern in entries 03057, 03064, 03072, 03077 — an incomplete object `{type, prefix}` or `{type, ending, stem}` appearing before the full forms array. Python's `json.load` silently uses the last occurrence, so runtime behavior is correct, but the dead first object is malformed (duplicate keys). Continues to confirm the pattern is pervasive across the entire pre-retrofit entry range.

**Update 2026-05-25**: Session 011 (entries 03211–03230) found the same pattern in 5 suru-verb entries (03214, 03216, 03218, 03220, 03222) — a lightweight conjugation stub (type+prefix format) placed before `definitions` alongside a full conjugation table at the end. The stubs were removed during polishing. Reinforces the pervasive pre-retrofit scope.

**Related sub-pattern (notes-level duplication)**: Comprehensive-polish session 033 (entries 05540–05559) found entries 05542, 05543, 05544, 05546 with redundant CONJUGATION prose sections in their `notes` field even though the entry already had a proper `conjugation` JSON field with all forms. The notes-only CONJUGATION block is a batch artifact from a period when conjugation data lived in notes rather than in a structured field. These are distinct from the duplicate-JSON-key pattern above — the notes text is well-formed but redundant once the structured conjugation field exists. Comprehensive-polish removes them case-by-case, but a one-shot scan for `CONJUGATION` headers in notes of entries that also have a `conjugation` field would catch all remaining instances.

**Update 2026-06-10 (compound-verb range)**: Routine v2 polish session found the same notes-level conjugation duplication in three 06xxx godan compound verbs — 06852_hourikomu (放り込む), 06858_ukabiagaru (浮かび上がる), 06735_sashikakaru (差し掛かる) — each of whose notes opened with a redundant negative / te-form / past bullet list duplicating the structured `conjugation` table. Removed in session; the 06xxx compound-verb cohort likely holds more. **Detector gap**: `build/check_artifacts.py --issue dup-conjugation` targets the *duplicate-JSON-key* form (P4 above) and currently returns 0 — it does **not** detect this *notes-prose* duplication. So this sub-pattern is not yet covered by any read-only detector; either extend `check_artifacts.py` with a `notes-conjugation-prose` check (CONJUGATION header **or** a leading negative/te/past bullet list in `notes` of an entry that already has a `conjugation` field) or keep handling it case-by-case in comprehensive-polish. The former would make it backlog-queue-eligible for a systemic-fix batch.

## Priority 5: Particle entry polish

**Source**: Comprehensive-polish 2026-05-09 sessions 002 and 003

Particle entries with extensive structured fields (e.g., 00051_ga and 00079_ha with `predicates_requiring`, `particle_contrasts`, `fixed_patterns`, `common_mistakes`, `information_structure`) contain dozens of small Japanese phrase fragments that lack inline link coverage. These are not addressable by ordinary tier-1 polishing — they need a dedicated particle-polish session.

**Affected entries**: At minimum 00051 (が), 00079 (は), and likely 00422 (を), 00314 (に), 00502 (で), 00504 (と), 00512 (から).

## Priority 6: Spurious conjugation tables on non-verb entries

**RESOLVED (2026-06-08).** The one-time non-verb conjugation sweep cleaned **133 entries** (101 non-expression non-verbs — adverbs, onomatopoeia, noun-adverbs, na-adjectives, nouns, auxiliaries — plus 32 reviewed `expression` entries), removing both the `conjugation` field and the stray `verb_class` tag from each. (133 vs. the 130 estimated here: the audit detector counted only entries with a `conjugation` field, whereas the pruner also catches a few that had a stray `verb_class` tag but no table, e.g. 04214_jisseki; one of the original twelve onomatopoeia, 05646_gyuugyuu, had already been cleaned on 2026-06-07.) The reusable pruner `build/prune_nonverb_conjugations.py` was built and committed, and a **defensive exact-enum verb-POS guard** was added to `add_conjugations.py` — the previous guard used the substring test `'verb' in p`, which is true for `"adverb"` and let adverbs with a stray `verb_class` tag generate godan nonsense. The detector one-liner below now returns **0**; re-running both retrofits re-adds nothing. The 31→32 expression cases were all confirmed as multi-word idioms, proverbs, adverbial phrases, or compound-ている forms (not single mis-tagged verbs); the one borderline keigo case (お会いする, 22190) was stripped and logged for a curator second look in [Entry Follow-ups](entry-followups.md).

**Standing-check re-confirmation (2026-06-24):** the systemic-fix selector surfaced this item again; `check_tag_drift.py --check conjugation-no-verb-pos --json` returned `[]` (0 dictionary-wide), so the `add_conjugations.py` exact-enum verb-POS guard is still holding against regeneration. The backlog-queue.json status was flipped `open`→`resolved` (matching the `tag-politeness-unsupported` guarded-standing-check precedent) so the selector advances to the next actionable item instead of re-picking a clean scope-0 check; the read-only detector stays indexed as a standing guard.

**Source**: Wiki maintenance 2026-05-11 (initial 12-entry onomatopoeia case) + 2026-05-12 (widened audit)

The 2026-05-11 session identified 12 adverbial onomatopoeia entries (ぐつぐつ → ぐつぐたない etc.) carrying full godan conjugation blocks with nonsense forms. The 2026-05-12 follow-up audit shows this was a partial finding: **130 entries currently have a conjugation field while their POS tag contains no `verb-*` or `adjective-i` value**. All 130 carry a stray `verb_class` tag that triggered `add_conjugations.py`.

**Breakdown by primary POS:**

| Primary POS | Count | Example | Generated nonsense |
|-------------|------:|---------|--------------------|
| adverb (non-onomatopoeia) | 79 | 著しく, すごく, おそらく, ますます, あいにく | `著しきます`, `すごかない` |
| adverb + onomatopoeia | 12 | ぐつぐつ, こつこつ, ぱくぱく | `ぐつぐたない` |
| expression | 31 | 反応を見る, 手を打つ, 場を和ませる | `反応を見らない` (mis-classifies 見る as godan) |
| noun + adverb | 5 | 真っ二つ, 多く, 遠く | varies |
| auxiliary | 2 | ～続ける | godan-ku forms |
| na-adj + adverb | 1 | べらぼう | godan forms |
| **Total** | **130** | | |

The original 12-onomatopoeia list is a subset. For the full list of 130, run:

```bash
python3 -c "
import json, glob
for p in glob.glob('entries/*/*.json'):
    d = json.load(open(p))
    pos = (d.get('metadata') or {}).get('tags', {}).get('pos', []) or []
    if d.get('conjugation') and not any(x in pos for x in ['verb-godan','verb-ichidan','verb-suru','verb-irregular','verb-kuru','adjective-i']):
        print(d['id'])
"
```

**Sub-pattern: adverb cases (96 of the 130)** are the cleanest demonstration of failure. These are adverbial forms of i-adjectives (著しく ← 著しい), adverbs derived from other roots (おそらく, ますます), or fixed phrases (あいにく). They have no verb morphology of their own, but `add_conjugations.py` saw the く ending and generated `godan-ku` conjugations like `著しきます` and `すごかない` — forms that are not Japanese.

**Sub-pattern: expression cases (31)** are partly correct, partly broken. Expressions ending in する (頼りにする, お会いする) get suru-conjugations that happen to be correct because the script conjugates する correctly regardless of the surrounding phrase. Expressions whose final verb is ichidan but tagged godan (反応を見る where 見る is ichidan) produce nonsense like `反応を見ります`.

**Suggested actions**:
1. **One-shot pruner** that finds every entry where `pos` contains no `verb-*` value but the entry has a `conjugation` field, prints them for review, and on confirmation removes the `conjugation` field and the stray `verb_class` tag. Replaces the narrower 12-entry list filed earlier. See [Tooling Backlog](tooling-backlog.md) → item 5.
2. **Defensive guard in `add_conjugations.py`**: refuse to write a conjugation block unless the entry has at least one `verb-*` POS tag. Prevents regeneration.
3. **For the 31 expression cases**: review whether they should keep a conjugation block at all. Most idioms don't conjugate as a unit; the underlying verb's conjugation is usually all the learner needs. If a conjugation block is desired, the type must match the final verb's class.
4. See [Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Runaway automation" for the broader pattern.

**Update 2026-06-05**: Comprehensive-polish session 015 (entries 05165–05184) found two more adverb entries (05173_nurunuru, 05175_tsurutsuru) with spurious `verb_class: "godan-ru"` tags and full conjugation tables producing nonsensical forms like ぬるぬらない, つるつらない. These are mimetic adverbs, not verbs. Reinforces the case for the batch pruner and defensive guard. A targeted scan of adverb entries for `verb_class` tags or `conjugation` fields would catch all remaining instances.

**Update 2026-06-06**: Comprehensive-polish session 024 (entries 05349–05373) confirmed a dense cluster of mimetic adverbs with spurious `conjugation` fields and `verb_class` tags (godan-ku, godan-ru, godan-tsu) — confirmed in 05352, 05364, 05372, 05373, likely extending into 05374+. Same claude-opus-4-5 / 2026-04-14 batch signature as the Priority 11 semantic-tag errors, so the two cleanups can be scoped together. Reinforces the case for a defensive guard in `add_conjugations.py` (Tooling Backlog item 5).

## Priority 7: Politeness tag conflation (uchi/soto, bikago, familiar suffixes)

**Source**: Wiki maintenance 2026-05-11 entry exploration

The `politeness` tag's four buckets (plain/polite/humble/honorific) are being applied too loosely. Three sub-issues:

1. **Uchi/soto kinship terms mis-tagged as humble**: 母 (はは), 父 (ちち), 兄 (あに), 姉 (あね), 息子 (むすこ) and several similar entries are tagged `politeness: humble`. They are the plain in-group reference forms, not humble forms in the technical sense. The contrast お母さん/お父さん/お兄さん etc. (out-group reference and address forms) is uchi/soto, not the speech-level politeness scale.

2. **Bikago mis-tagged as honorific**: Words where the お〜/ご〜 prefix has fused into the lexical form (ご飯, お釣り, etc.) are tagged `honorific`. They are 美化語 (bikago, beautifying language) — a separate category in the 2007 五分類 (five-category) reclassification — not productive sonkeigo.

3. **Familiar suffixes mis-tagged as honorific**: 〜ちゃん, 〜くん are tagged `politeness: honorific`. They are diminutive/familiar suffixes marking intimacy or subordinate-status address, not deference.

**Total affected**: ~58 entries with non-verb POS and `politeness: humble`; ~49 entries with non-verb POS and `politeness: honorific`. Not all are wrong, but a meaningful fraction is.

**Suggested actions**:
- These cases need semantic review, not a deterministic pass. They are a natural target for a polish-politeness-labels task (parallel to `polish_semantic_labels.md`).
- In the interim, ensure the notes prose carries the correct nuance even if the tag is coarse. Most well-polished entries (e.g., 00549_haha) already do this.
- Longer term: see [Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Implications for the schema" for the structured-politeness proposal vs. its costs.

**Progress 2026-06-22 (detector slice RESOLVED)**: The mechanically-detectable slice — `check_tag_drift.py --check politeness-unsupported`, which flags `humble`/`honorific` entries whose notes contain none of the keigo support keywords — is at **0** dictionary-wide. The 2 then-open flags were verified and fixed: 23570 つまらないものですが (humble, correct — added a 謙譲 register sentence) and 27145 閣下 (honorific, correct — added a 尊敬 clause). Both tags were right; the notes simply lacked the supporting wording, so the fix was to document the register, not retag. The `backlog-queue.json` item `tag-politeness-unsupported` is marked resolved (kept as a standing check). The **broader** semantic review above (uchi/soto kinship terms, bikago, familiar suffixes mis-tagged) is NOT covered by this detector — those entries do carry supporting notes — and remains an open polish-politeness-labels task.

## Priority 8: Unconsolidated duplicate-expression entries

**Source**: Wiki maintenance 2026-05-11 entry exploration

Some entries are duplicates of each other that were linked via `prominent_see_also` instead of being merged. Confirmed example: 02008_ikuratemo and 02461_ikuratemo both cover the expression いくら〜ても. The two entries have overlapping examples and similar (but not identical) notes. The link makes the relationship discoverable but two parallel sources of truth keep diverging on every polishing pass.

**Suggested action**: Run `python3 build/find_merge_candidates.py --merge-only` and review the output. Merge candidates where the two entries are functionally identical. The `consolidate-entries` skill describes the process; the `resolve-duplicates` skill (`.claude/skills/resolve-duplicates/SKILL.md`) is the operational guide.

Also: 02008_ikuratemo carries `semantic: ["furniture"]` — an obviously stale auto-label. This is a representative case for [Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Stale auto-labels."

**Update 2026-07-25 (two new sub-families: a plain same-reading duplicate pair, and the sharper "one entry holds a sense that another entry *is*" split)**: A 2026-07-25 routine polish run surfaced two cases that extend this priority beyond the classic near-identical-expression duplicate:

- **Plain duplicate pair** — **01385_kimochi** and **02485_kimochi** are both 気持ち, both glossed "feeling, mood". A straightforward merge candidate for a consolidation session (the low ID is the keeper by the usual rule; `find_merge_candidates.py --merge-only` should already surface it, since it groups by reading).
- **Sense-vs-entry split (new sub-family)** — **06626 見栄** carried a **sense 2 "kabuki dramatic pose" with three examples written 見栄を切る**, while the *correct* entry for that sense, **29012 見得**, already existed. The wrong sense was removed from 06626, the two entries cross-linked, and the 張る/切る verb split documented in-run. The general shape is: entry A (correct kanji for sense 1) grows a sense that is the entire subject matter of entry B (correct kanji for sense 2), because the two share a reading. **This is invisible to a "are these two entries the same?" merge check** — the entries genuinely differ; only one *sense* is misplaced.

**Suggested action for the new sub-family**: a targeted pass over homophone pairs where the two entries share a reading but differ in kanji, checking whether either entry carries a sense that the other entry already covers in full. `find_merge_candidates.py` groups by reading, so the candidate pairs are already computable; what is missing is the per-sense comparison. See [Tooling item 7](tooling-backlog.md#7-polysemic-kanji-variant-overlap-detector), which this case reinforces with a concrete worked example.

## Priority 9: Malformed furigana wrappers

**Source**: Wiki maintenance 2026-05-12 entry exploration

**859 instances across 624 unique entries** have hiragana inside the kanji portion of a furigana wrapper, in violation of the documented convention that `{kanji|reading}` puts kanji-only text on the left of the pipe. Distribution:

| Field | Instances |
|-------|----------:|
| Headword | 22 |
| Examples | 253 |
| Notes | 584 |

By sub-pattern:

| Sub-pattern | Count | Example | Renders OK? |
|-------------|------:|---------|-------------|
| お-prefix inside wrapper | 211 | `{お酒\|おさけ}` | yes, but breaks lookups on partial wraps like `{お会\|おあ}` |
| ご-prefix inside wrapper | 13 | `{ご飯\|ごはん}` | mostly yes |
| Pure-kana wrapper (no kanji) | 172 | `{どんどん\|どんどん}`, `{ところ\|所}` | varies; `{ところ\|所}` is **reversed** and renders wrong |
| Okurigana inside wrapper, reading covers full word | 152 | `{若い\|わかい}` | yes — over-wrapped only |
| Okurigana inside wrapper, **reading truncated** | 68 | `{やり方\|かた}` | **no — visibly wrong furigana** |
| Other interleaving | 243 | `{か所\|かしょ}`, `{差し水\|さしみず}` | yes — over-wrapped only |

**Highest-severity sub-pattern: 68 entries with truncated readings.** The wrapper includes preceding hiragana on the surface side, but the reading covers only the kanji. Browsers paint the partial reading over the full surface, producing visibly wrong furigana on the live site (e.g., `かた` rendered over the entire `やり方`).

**Update 2026-06-09 (RESOLVED)**: Routine systemic-fix session fixed all 74 reading-truncated entries, 9 pure-kana reversed entries, and 7 nested-brace entries. 0 remain for these sub-patterns. The 130 slash-reading entries ({七|なな/しち} style) remain open under Priority 12.

**Highest-volume sub-pattern: 463 okurigana-inside-wrapper instances.** Most render correctly but are non-standard. Canonical form would be `{若|わか}い` instead of `{若い|わかい}`, etc.

**Confirmed downstream impact**: 01525_wakai (basic-tier 若い) is currently missing its conjugation table on the live site because `add_adjective_conjugations.py` couldn't parse the headword `{若い|わかい}` to extract a stem.

**Suggested actions**:
1. **Targeted pass on sub-pattern 3b (68 truncated-reading instances)** — these are real rendering bugs. Manual review and repair.
2. **Mechanical sweep** for sub-patterns 1, 2, and 3a/3c (~791 instances). Regex-driven replacements with validation against `build/word_id_lookup.json`. Mostly cosmetic but worth doing while the pattern is fresh.
3. **Add a furigana-format validator** (`build/check_furigana_format.py`) alongside the existing `verify_furigana.py` (which checks only for *missing* furigana, not malformed wrappers). See [Tooling Backlog](tooling-backlog.md) → item 8.
4. **Restate the convention in `entry-guidelines`** so new entries don't reintroduce the pattern. The current docs state "all kanji must have furigana" but don't address where the wrapper boundaries should sit relative to hiragana characters.
5. See [Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) for the full analysis.

**Update 2026-07-26 (cosmetic sweep progress)**: The routine `systemic-fix` mode drains the cosmetic sub-patterns (o/go-prefix-inside-wrapper, pure-kana wrappers, over-wrapped okurigana/compound) incrementally, one ID slice per run, with per-entry verification. As of 2026-07-26 the 21000–21999 slice is done (58 instances / 46 entries; 1032→974), leaving **~974 filtered instances** across these three sub-patterns; the running per-slice log lives in `planning/wiki/ideas/backlog-queue.json` → `furigana-cosmetic-wrappers`. Next ready slice: 22000+ and the larger pre-06000 backlog. Note that the post-20999 slices are running roughly twice as dense as the 06000–20999 ones (58 instances in one 1,000-ID block vs. ~24 per block below it), consistent with the newer creation batches never having had a wrapper-format pass.

**Update 2026-06-06 (new sub-pattern: nested/double braces)**: Comprehensive-polish session 025 (entries 05374–05389) found a *nested* furigana wrapper form, `{{word|reading}phrase|compound-reading}`, in 05379 and 05380. This is invalid — each kanji compound should carry its own `{漢字|かんじ}` annotation rather than nesting one wrapper inside another. The furigana renderer expects a flat `{kanji|reading}` and will misrender or drop the nested form. **Detection**: `grep -rl '{{' entries/` (the literal `{{` opening is the tell). Scope unknown; this is the first range where the nested form has been observed, so a one-shot scan across all entries is warranted. The format validator proposed in [Tooling Backlog](tooling-backlog.md) → item 8 should add a "nested wrapper" check alongside its other rules.

**Update 2026-06-17 (new sub-pattern: no-pipe brace spans + stray trailing brace)**: A 2026-06-16 routine polish session found a furigana-brace malformation in **06147_jiboujiki** distinct from all the sub-patterns above: the `{...}` (kanji|reading) syntax applied to a **whole kana phrase with no `|` separator at all** (`{やけになる}`) and a valid wrapper followed by a **stray trailing `}`** (`{投|な}げやりになる}`). Both render as literal braces on the live site and — because there is no pipe — they slip past furigana-*coverage* checks entirely (those only look for kanji lacking a reading, not for degenerate wrappers). This is likely present across the **same early-2026 yojijukugo batch** (06140s idiom cohort under P21). **Detection / tool side**: extend `build/check_furigana_format.py` to flag (a) `{...}` spans that contain no `|`, and (b) unbalanced braces in a field — see [Tooling Backlog](tooling-backlog.md) → item 8. Fixed in 06147 during the originating session; the rest of the batch is unswept.

**Update 2026-06-20 (cosmetic-wrapper batch confirmed at the 06xxx frontier; a new empty-reading degenerate)**: A 2026-06-20 routine polish observation found the early-2026 06xxx creation batch carries two of the documented cosmetic sub-patterns — an **お-prefix-inside wrapper** (`{お年寄|としよ}り`-style, sub-pattern 1) and a **pure-kana / empty-reading wrapper** (sub-pattern 3) — plus a previously-unlisted degenerate form: a **valid kanji left, *empty* reading right** of the pipe (`{きつい|}`-style, i.e. `{X|}` with nothing after `|`). These render OK or near-OK (warn/info severity, not the high-severity reading-truncation class already RESOLVED in the 2026-06-09 update), but they are non-standard and cluster in the Jan-2026 06xxx batch. Current dict-wide detector counts (`build/check_furigana_format.py --summary`): **o-go-prefix = 228, pure-kana = 888, over-wrapped = 452, nested = 1** (1,569 total across 1,127 entries). The o-prefix and pure-kana sub-patterns *are* caught by the detector, so a **scoped mechanical sweep of the 06000–06400 slice** (validated against `build/word_id_lookup.json`, per the existing suggested-action #2) is a ready systemic-fix candidate. **Open tooling question**: confirm the detector flags the **empty-reading-after-pipe** form `{X|}` — if it does not, add it to [Tooling Backlog](tooling-backlog.md) → item 8 alongside the no-pipe-span and unbalanced-brace checks (the 2026-06-17 update), since `{X|}` is the natural third degenerate-wrapper case (no reading at all, vs. no pipe at all).

**Update 2026-06-23 (frontier instances at 06231 — kana-inside-group + nested braces)**: A
2026-06-22 routine polish run found **06231** carrying two of the documented malformed
forms together: a **non-kanji character inside the kanji-left group** (`{お吸|す}い{物|もの}`,
the お-prefix-inside sub-pattern 1 → should be `お{吸|す}い{物|もの}`) and **nested braces**
(`{とん{汁|じる}}`, `{けんちん{汁|じる}}`, the sub-pattern from the 2026-06-06 update → should
be `とん{汁|じる}` / けんちん{汁|じる}). Both pass schema and furigana-*coverage* checks but
render wrong. They are detector-caught (`o-go-prefix` and `nested` classes), so the 06231
instance reconfirms the 06xxx Jan-2026 batch carries these in its notes and that the scoped
**06000–06400 mechanical sweep** (validated vs. `word_id_lookup.json`, suggested-action #2)
would clean them along with the o-prefix/pure-kana wrappers already noted at this frontier.

**Update 2026-06-26 (nested お-prefix wrappers at the 06295/06296 honorific cohort — a concrete auto-fix transform)**: A 2026-06-26 routine polish run (frontier 06288–06300) found **06295** and **06296** carrying the **nested-brace + お-prefix-inside** form together — `{お{香|こう}}` and `{お{土産|みやげ}}` — i.e. an honorific お placed *inside* an outer wrapper that also nests an inner `{KANJI|reading}`. These are detector-caught (`nested` + `o-go-prefix` classes, Tooling item 8) and almost certainly recur across the same お-prefixed honorific batch in the 06200s–06300s (cf. the 06231 `{お吸|す}い{物|もの}` instance in the 2026-06-23 update). The observing run noted these have a **single deterministic rewrite** — `{お{KANJI|reading}}` → `お{KANJI|reading}` (drop the outer braces, lift the お outside) — which is provably safe because it changes only the wrapper boundaries, not the surface text or reading. This is the cleanest auto-fixable sub-pattern in P9: a candidate for an **`--fix` mode on `check_furigana_format.py`** for exactly this `{お{…|…}}` / `{ご{…|…}}` shape (validated against `word_id_lookup.json`), rather than per-entry hand-editing it as the scoped 06000–06400 mechanical sweep advances past 06400. See [Tooling Backlog](tooling-backlog.md) → item 8.

**Update 2026-06-25 (06000–06400 slice swept)**: A routine systemic-fix run worked the
predicted scoped slice end-to-end, per-entry verified, fixing **18 instances across 16
entries** (`detect` total 1565 → 1547): pure-kana wrappers around katakana loanwords
(`{リーダー|りーだー}`, `{ボランティア|ぼらんてぃあ}`, `{タバコ|たばこ}`, `{メガネ|めがね}`,
`{ブラッドムーン|…}`, `{サインポール|…}`, `{タッチ|たっち}`, `{おかわり|おかわり}`,
`{すぐ|すぐ}`, `{ばさみ|はさみ}`) de-wrapped to bare kana; お/ご-prefix wrappers
repositioned (`{お問|おと}`→`お{問|と}`, `{ご飯|ごはん}`→`ご{飯|はん}`); over-wrapped
okurigana/compounds split with the correct rendaku reading (`{数え|かぞえ}`→`{数|かぞ}え`,
`{どん底|どんぞこ}`→`どん{底|ぞこ}`, `{流れ星|ながれぼし}`→`{流|なが}れ{星|ぼし}`,
`{横ずれ断層|よこずれだんそう}`→`{横|よこ}ずれ{断層|だんそう}`). Inline-link surfaces were
preserved (links resolve by explicit `：entry_id`), validation and furigana-coverage stayed
clean, and a furigana self-check screened the changed IDs with **0 flags**. The item stays
**open** — it is dictionary-wide (remaining ~1546 across the o-go-prefix/pure-kana/over-wrapped
sub-patterns); the next ready slice is 06400+ and the larger pre-06000 backlog.


**Update 2026-06-27 (06400–06650 slice swept)**: A routine systemic-fix run worked the
next scoped slice per-entry, fixing **30 instances across 24 entries** (`detect` total 1547 →
1517): katakana-loanword de-wraps (リフォーム/カード/メイク/バレーボール/キック/プル/ボール/エース/
パワーフォワード/スモールフォワード/オフィス — hiragana ruby over katakana is redundant), o-prefix
repositions (`{お寺|おてら}` → `お{寺|てら}`, `{お正月|しょうがつ}` → `お{正月|しょうがつ}`),
over-wrapped okurigana splits (`{余り|あまり}` → `{余|あま}り`, `{やり方|やりかた}` → `やり{方|かた}`,
`{引っ越|ひっこ}` → `{引|ひ}っ{越|こ}`, `{瞬き|まばたき}` → `{瞬|まばた}き`), numeral de-wraps to bare
digits (`{20|にじゅう}` → `20`, etc.), and symbol/letter readings converted to standard parenthetical
form to drop the malformed wrapper while preserving the reading (`{#|シャープ}` → `#（シャープ）`,
`{V2|ブイツー}` → `V2（ブイツー）`). One genuine **bug** also fixed: an English gloss sitting where the
reading belongs — `{ゴマフアザラシ|spotted seal}` rendered "spotted seal" as ruby — corrected to
`ゴマフアザラシ (spotted seal)`. This **English-text-after-pipe** form is a degenerate wrapper the
detector currently lumps into `pure-kana`; a dedicated check (right side contains Latin letters /
is an English phrase) would surface the class cleanly — see [Tooling Backlog](tooling-backlog.md) →
item 8. §4 furigana self-screen: 2 model flags, both rejected (okurigana び of 喜ぶ; katakana プロ
takes no furigana). Next ready slice: 06650+ and the larger pre-06000 backlog.

**Update 2026-06-28 (06650–07300 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **34 instances across 26 entries** (`detect` total 1517 → 1485):
katakana-loanword de-wraps (コミュニケーション/チーム/コーヒー/クリニック/タオル/ゴキブリ/トイレ/
ラベンダー/シニア/プレゼント/ベビーチェア/オストメイト/イクメン/カビ/ブランド — hiragana ruby over
katakana is redundant), pure-kana de-wraps (やっぱり/しまう/めまい/ふらふら/ひょっとこ/きっかけ),
numeral de-wraps in a ratio example (`{3|さん}対{2|に}` → `3対2`), o-prefix repositions
(`{お元気|おげんき}` → `お{元気|げんき}`, similarly お{客|きゃく}/お{経|きょう}/お{盆|ぼん}), and
over-wrapped okurigana splits (`{旨み|うまみ}` → `{旨|うま}み`, `{卸し金|おろしがね}` → `{卸|おろ}し{金|がね}`,
`{下ろし金|おろしがね}` → `{下|お}ろし{金|がね}`). One detector **mis-suggestion** was caught and
corrected by hand: `{おむつ替|か}` (in 07140) was flagged `o-go-prefix` with suggestion `お{むつ替|か}`,
but おむつ is a fixed kana word (not honorific お + むつ) and the only kanji is 替, so the correct
rewrap is `おむつ{替|か}` — a reminder that the detector's `o-go-prefix` suggestion assumes the お is
honorific and must be verified per-entry. The 06860 ブランド de-wrap sat inside an inline link
(`⟦{ブランド|ぶらんど}→ブランド：05221_burando⟧` → `⟦ブランド→ブランド：05221_burando⟧`); it resolves by
explicit `：entry_id`, so the link still works. Validation and furigana-coverage stayed clean.
§4 furigana self-screen: 3 model flags, **all rejected** — each was a screener compound-reading-split
false positive (`{次々|つぎつぎ}`, `{入場料|にゅうじょうりょう}`, `{低血圧|ていけつあつ}` reported as
truncated although correct in the entry), and none touched the edited furigana. Next ready slice:
07300+ and the larger pre-06000 backlog.

**Update 2026-06-30 (07300–07600 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **24 instances across 18 entries** (`detect` total 1488 → 1463):
pure-kana katakana/kana de-wraps (プロジェクト/スキルアップ/メンバー/チーム/バー/リストラ/タオル/
ティッシュ/ボールペン/エコバッグ/ノベルティ/データ/イメージ×2/ボケ — hiragana ruby over katakana is
redundant), o-prefix repositions (`{お金|かね}` → `お{金|かね}`, `{お茶屋|おちゃや}` → `お{茶屋|ちゃや}`,
`{お菓子|おかし}` → `お{菓子|かし}`), and over-wrapped okurigana splits (`{取り消し|とりけし}` →
`{取|と}り{消|け}し`, `{女の子|おんなのこ}` → `{女|おんな}の{子|こ}`, `{すり身|すりみ}` → `すり{身|み}`,
`{届け出|とどけで}` → `{届|とど}け{出|で}`, `{太っ腹|ふとっぱら}` → `{太|ふと}っ{腹|ぱら}`). Two
non-format fixes of malformed wrappers: `{できる|できない}` (surface≠reading) → `できる/できない` to
restore the can/cannot contrast its gloss describes, and `{どこ|}` (empty reading) → `どこ`. No edit
sat inside an inline link. Validation and furigana-coverage stayed clean. §4 furigana self-screen:
2 model flags, **both rejected** — 07459's `{一見|いっけん}` is the entry's own "NOTE ON READING"
contrast with いちげん (correct, not an inconsistency), and 07364 was a model misreading ("to sing"
read as "to sin"; the 歌=うた furigana is correct). Neither touched the edited furigana. Next ready
slice: 07600+ and the larger pre-06000 backlog.

**Update 2026-07-01 (07600–07900 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **27 instances across 22 entries** (`detect` total 1463 → 1436):
pure-kana katakana/kana de-wraps (グループ×2/シーン×2/キャラ/サービス×2/コンセント/
デジタルトランスフォーメーション/オン/オフ/エンゲージメント/コンプライアンス/ネイル/ネオン/やおい/
わきまえる×2 — hiragana ruby over katakana/kana is redundant), over-wrapped okurigana splits
(`{素っ気|そっけ}ない` → `{素|そ}っ{気|け}ない`, `{肩凝り|かたこり}` → `{肩|かた}{凝|こ}り`,
`{肩こり|かたこり}` → `{肩|かた}こり`, `{か細|かぼそ}い` → `か{細|ぼそ}い`), and o-prefix repositions
(`{お互|たが}` → `お{互|たが}`, `{お世辞|おせじ}` → `お{世辞|せじ}` ×3). Two entries (07715 OB, 07716 OG)
misused the furigana wrapper for an English-source gloss (`{old girl|オールドガール}`,
`{old boy|オールドボーイ}` — base=English, reading=katakana, which renders wrong); rewritten to plain
`'old girl'`/`'old boy'` since the etymology line already gives the katakana origin. No edit sat inside
an inline link. Validation and furigana-coverage stayed clean. §4 furigana self-screen: 21 screened,
**0 flags**, 1 skipped. Next ready slice: 07900+ and the larger pre-06000 backlog.

**Update 2026-07-02 (07900–08300 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **31 instances across 25 entries** (`detect` total 1436 → 1405):
pure-kana katakana/kana de-wraps (ささみ/アナウンス/ゆうパック/パレード/プロ/ステンレス/アルミ/データ/
マッサージ/ステーキ/Wi-Fi/バッテリー/エアコン/テレビ/アルバイト/デザイン/パスポート/サラダ/つま/
チョコレート/チーズ×2/もう — hiragana ruby over katakana/kana/Latin is redundant), over-wrapped
okurigana splits (`{振り分|ふりわ}` → `{振|ふ}り{分|わ}`, `{抜てき|ばってき}` → `{抜|ばっ}てき`,
`{認め印|みとめいん}` → `{認|みと}め{印|いん}`, `{御負け|おまけ}` → `{御|お}{負|ま}け`), and
o-/go-prefix repositions (`{お土産|おみやげ}` → `お{土産|みやげ}`, `{ご飯|はん}` → `ご{飯|はん}` ×3).
The legit whole-compound `{認印|みとめいん}` was left untouched (no internal kana). No edit sat inside
an inline link. Validation and furigana-coverage stayed clean. §4 furigana self-screen: 16 screened,
**1 flag rejected** (07950 `{代引|だいび}き` — model wanted き folded into the reading, but き is genuine
okurigana of 引き; documented okurigana false-positive family, and untouched by the edits), 9 skipped.
Next ready slice: 08300+ and the larger pre-06000 backlog.

**Update 2026-07-03 (08300–08700 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **21 instances across 17 entries** (`detect` total 1405 → 1384):
pure-kana katakana/kana de-wraps (エンドツーエンド/ワンケー/おもちゃ/マンション/ライター/ハイアーチ/
サポート/ドア — hiragana ruby over katakana/kana is redundant), over-wrapped okurigana splits
(`{暑さ|あつさ}` → `{暑|あつ}さ`, `{突き当たり|つきあたり}` → `{突|つ}き{当|あ}たり`,
`{忘れ物|わすれもの}` → `{忘|わす}れ{物|もの}` ×2, `{その後|そのご}`/`{その前|そのまえ}`/`{その間|そのあいだ}`
→ `その{後|ご}`/`その{前|まえ}`/`その{間|あいだ}`, `{横ばい|よこばい}` → `{横|よこ}ばい`,
`{しめ鯖|しめさば}` → `しめ{鯖|さば}`), o-prefix repositions (`{お腹|おなか}` → `お{腹|なか}`,
`{お願|ねが}` → `お{願|ねが}`, `{お返|かえ}` → `お{返|かえ}`), and one kana-prefix correction
(`{おせち料理|りょうり}` → `おせち{料理|りょうり}`, since おせち is kana, not the honorific お prefix —
analogous to the earlier おむつ{替|か} correction). No edit sat inside an inline link. Validation and
furigana-coverage stayed clean. §4 furigana self-screen: 14 screened, **1 flag rejected** (08399
`{行|い}き{止|ど}まり` — model wanted 止=と, but ど is genuine rendaku in いきどまり; documented
rendaku false-positive family, and untouched by the edits), 3 skipped.
Next ready slice: 08700+ and the larger pre-06000 backlog.

**Update 2026-07-05 (08700–08999 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **33 instances across 23 entries** (`detect` filtered total 1384 → 1350):
mostly pure-kana katakana/loanword de-wraps in acronym entries — hiragana ruby over katakana is
redundant (テスト/キャンペーン/ボタン/ポケット/カーナビ/データ/メモリー/ケーブル ×2/タイプ/ライト/
プレーヤー ×2/ショップ/ボックス/カット ×2/ケア/ペナルティキック/ラジオ/ワイドFM/リアル/ファイナル/
パネル/プラズマ/スタッフ/ゆるキャラ), one pure-hiragana de-wrap (`{なぜなら|なぜなら}` → `なぜなら` ×2),
and over-wrapped okurigana splits (`{うつ病|うつびょう}` → `うつ{病|びょう}`,
`{一人っ子|ひとりっこ}` → `{一人|ひとり}っ{子|こ}`, `{日にち|ひにち}` → `{日|ひ}にち`).
No edit sat inside an inline link. Validation stayed clean (300/300 in range). §4 furigana
self-screen: 23 entries submitted, all skipped (kana-only acronym/loanword entries carry no
kanji ruby to screen), **0 flags**.
Next ready slice: 09000+ and the larger pre-06000 backlog.

**Update 2026-07-06 (09000–09400 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **25 instances across 21 entries** (`detect` filtered total 1350 → 1325):
mostly pure-kana katakana/loanword de-wraps (アメリカ/リスク ×2/サイレン ×3/イメージ/エネルギー/
ムード/ライオン/セキュリティ/プロ ×2/チャンス/デザイン/バグ), pure-hiragana de-wraps
(`{わかりやすく|わかりやすく}` → `わかりやすく`, `{ようやく|ようやく}` → `ようやく`, `{この|この}` → `この`),
katakana サ変動詞 de-wraps (`{サ|さ}` → `サ` in 09142/09168 — katakana サ referring to the サ-row
conjugation class takes no ruby), o-prefix repositions (`{お化|おば}` → `お{化|ば}`,
`{お金|おかね}` → `お{金|かね}`), and over-wrapped compound splits
(`{侘び寂び|わびさび}` → `{侘|わ}び{寂|さ}び`, `{天の邪鬼|あまのじゃく}` → `{天|あま}の{邪|じゃ}{鬼|く}`).
No edit sat inside an inline link. Validation stayed clean (401/401 in range). §4 furigana
self-screen: 21 entries submitted, 1 screened, 20 skipped (kana/loanword entries carry no ruby
to screen), **0 flags**.
Next ready slice: 09400+ and the larger pre-06000 backlog.

**Update 2026-07-10 (09400–09999 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **24 instances across 22 entries** (`detect` filtered total 1325 → 1301):
pure-kana katakana/loanword/numeral de-wraps (これ/パーティー/ニュース/ゴミ/プログラム/ファン/オン/
なし/すぐ/エリア ×2/クーポン/ある, and numerals `{30|さんじゅっ}` → `30`, `{1|いち}` → `1` ×2),
o/go-prefix repositions (`{お金|おかね}` → `お{金|かね}` ×2, `{ご来店|ごらいてん}` → `ご{来店|らいてん}`,
`{お好|この}` → `お{好|この}`, `{お伝|つた}` → `お{伝|つた}`, `{お腹|おなか}` → `お{腹|なか}`), and
over-wrapped okurigana splits (`{日替り|ひがわり}` → `{日|ひ}{替|がわ}り`,
`{警備する|けいびする}` → `{警備|けいび}する`). Three pure-kana de-wraps sat inside inline links
carrying explicit `entry_id`s (パーティー→02946, ニュース→04437, プログラム→01540), which resolve by
ID regardless of the display surface, so the de-wrap is safe. Validation stayed clean (595/595 in
range). §4 furigana self-screen: 22 entries submitted, 10 screened, 12 skipped (kana/loanword
entries carry no ruby to screen), **0 flags**.
Next ready slice: 10000+ and the larger pre-06000 backlog.

**Update 2026-07-10 (10000–10499 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **18 instances across 14 entries** (`detect` filtered total 1301 → 1283):
pure-kana katakana/loanword de-wraps (テレビ ×2/コンビニ/スーパー/メモ/パリ/デザイン/
コミュニケーション ×2/パソコン/チャージ/トイレ/サイズ), o-prefix repositions
(`{お浸|ひた}し` → `お{浸|ひた}し`, `{お袋|おふくろ}` → `お{袋|ふくろ}`, `{お礼|おれい}` → `お{礼|れい}`),
and one over-wrapped okurigana split (`{乗り越し|のりこし}` → `{乗|の}り{越|こ}し`). Also corrected
10232's `cross_references` headword `{嫌い|きらい}` → `{嫌|きら}い` to match target entry 02871's
canonical headword form. No inline links were touched. Validation stayed clean (485/485 in range).
§4 furigana self-screen: 14 entries submitted, all skipped (kana/loanword/already-polished entries
carry no ruby to screen), **0 flags**.
Next ready slice: 10500+ and the larger pre-06000 backlog.

**Update 2026-07-12 (10500–10999 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **22 instances across 9 entries** (`detect` filtered total 1283 → 1262):
pure-kana katakana/loanword de-wraps (ドア ×2/おでん/おこわ/おはぎ/ディレクター [empty-reading `{X|}`]/
ヘアバンド/ヘアゴム/ぬかるむ), one o-prefix reposition (`{お菓子|おかし}` → `お{菓子|かし}`), and one
over-wrapped compound split — `{木の葉|このは}` → `{木|こ}の{葉|は}` across 10668_konoha's headword and
all examples/notes, plus `{葉っぱ|はっぱ}` → `{葉|は}っぱ`. The 10668 headword rewrap is safe for its three
inbound inline links (02241_ha, 05985_zawazawa, 00524_ki), which reference it as `→木の葉：10668_konoha`
and resolve by `entry_id` regardless of the display surface. No inline-link surfaces inside the
10500–10999 range were touched. Validation stayed clean (500/500 in range). §4 furigana self-screen:
9 entries submitted, 7 screened, 1 flag **rejected** (10619 model misread 紙芝居's reading; the ruby is
correct `{紙芝居|かみしばい}` and untouched by the edit), 2 skipped.
Next ready slice: 11000+ and the larger pre-06000 backlog.

**Update 2026-07-13 (11000–12999 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **32 instances across 31 entries** (`detect` filtered total 1262 → 1230).
The 11000–12999 band is sparse (density had dropped to ~5–10 flags per 500-ID block), so the run took a
2,000-ID slice to reach a batch comparable to earlier 500-ID sweeps. Fixes: pure-kana katakana/loanword
de-wraps (クリア/チェーン/プライバシー/ストレス/エース/レスラー), pure-kana hiragana de-wraps
(おもてなし/なす/こだわり/おいしい/まるで/もてなし/すぐ), numeral/symbol de-wraps (`{１|いち}` → １,
`{30|さんじゅう}` → 30, `{＆|あんど}` → ＆), o/go-prefix repositions (`お{弁当|べんとう}`, `お{坊|ぼう}`,
`お{七夜|しちや}`, `お{盆|ぼん}`, `お{願|ねが}`, `お{化|ば}`), and over-wrapped okurigana/compound splits
(`{連|つ}れ{合|あ}い`, `{鯉|こい}のぼり`, `{入|い}り{交|ま}じる`, `{交|ま}じる`, `{付|つ}け{根|ね}`,
`まさに{地獄|じごく}`, `{幼|おさな}なじみ`, `ほうれん{草|そう}`, `{当|あ}て{字|じ}`). No inline-link
surfaces touched; every fix preserves the display surface, so `word_id_lookup.json` keys are unaffected.
Validation stayed clean (1999/1999 in range). §4 furigana self-screen: all 31 entries screened across two
passes (the runner hit its 2-min wall-clock twice but wrote per-entry results each time — a recurring
`[tooling]` friction), **0 flags**.
Next ready slice: 13000+ and the larger pre-06000 backlog.

**Update 2026-07-14 (the wrapper backlog thins sharply above ID ~11000 — reprioritize by density, not ID order)**: A 2026-07-13 systemic-fix run over the **11000–12999** slice measured the cosmetic-wrapper backlog at ~**8 filtered flags per 500-ID block**, versus **18–33 per block in the already-swept 06000–10999 ranges** — post-2026 entry-creation batches are markedly cleaner on wrapper formatting. The remaining bulk of the ~1,230 open instances is therefore *not* in the sequential frontier but in two dense pockets: the **high-ID new-entry ranges (23000–29999 blocks carry 36–110 each)** and the **un-swept pre-06000 backlog**. Recommendation: future wrapper sweeps should target those dense blocks directly rather than continuing the sparse sequential crawl, which now clears only a handful of real flags per 500-ID slice at full self-check cost. (Reinforces the 2026-07-11 `check_furigana_format` detector count of ~1,263–1,284.)

**Update 2026-07-15 (13000–14999 slice swept)**: A routine systemic-fix run cleared the next scoped slice per-entry, fixing **38 instances across 33 entries** (`detect` total 1230 → 1193). Density held at ~9.5 filtered flags per 500-ID block — consistent with the 2026-07-14 note that the sequential frontier above ~11000 is sparse. Mix: katakana/loanword and hiragana de-wraps (ウイルス/サービス/データ/エネルギー/チーム/ソファ/フランス/デモ/リクルートスーツ/ゴールデンウィーク/シルバーウィーク/コツ/ゆうパック/ぜんざい/くべる/おせち), one numeral de-wrap ({150|ひゃくごじゅっ}→150), o/go-prefix repositions (お{茶|ちゃ}/お{湯|ゆ}×2/お{土産|みやげ}/お{笑|わら}/お{守|まも}/お{盆|ぼん}/お{盆|ぼん}{休|やす}み), and over-wrapped okurigana/compound splits (〜する{動詞|どうし}/{比|ひ}ゆ/か{条|じょう}/ざる{蕎麦|そば}/かけ{蕎麦|そば}/{田|た}んぼ/{日本野鳥|にほんやちょう}の{会|かい}/{露|あら}わ/そぼろ{丼|どん}). No inline links touched. §4 self-screen: 1 flag rejected (13832 okurigana-split false positive on an untouched pair). Next ready slice: 15000+ and the larger pre-06000 backlog — but the 2026-07-14 density recommendation to jump to the dense 23000+ / pre-06000 pockets still stands for the curator to weigh.

**Update 2026-07-16 (15000–15999 slice swept)**: A routine systemic-fix run cleared the next scoped slice per-entry, fixing **25 instances across 21 entries** (`detect` filtered total 1193 → 1169). Density stayed at ~12.5 filtered flags per 500-ID block. Mix: pure-kana katakana/loanword de-wraps (きちんと/ビジネスマナー/ベストセラー/ホロスコープ/ヘドロ/アロンアルファ/リストラ/リフォーム/まだ/する/バス/ワイン/オーナー), pure-kana kana de-wraps (すげる/ゆるい/から×2/まで), one o-prefix reposition (`{お参|まい}` → `お{参|まい}`), and over-wrapped okurigana/compound splits (`{太っ腹|ふとっぱら}` → `{太|ふと}っ{腹|ぱら}`, `{供え物|そなえもの}` → `{供|そな}え{物|もの}`, `{蛇の目傘|じゃのめがさ}` → `{蛇|じゃ}の{目|め}{傘|がさ}`, `{数の子|かずのこ}`×2 → `{数|かず}の{子|こ}`, `{不確か|ふたしか}` → `{不|ふ}{確|たし}か`). No inline-link surfaces touched; every fix preserves the display surface, so `word_id_lookup.json` keys are unaffected. Validation stayed clean (997/997 in range). §4 furigana self-screen: 18 screened, **2 flags both rejected** (15265 model truncated-token misread じょうきゃ/せ — the entry's readings `{乗客|じょうきゃく}`/`{整列|せいれつ}` are actually complete; 15562 partial-reading misread of 占星術, correct in entry), 3 skipped. Next ready slice: 16000+ and the larger pre-06000 backlog — the 2026-07-14 density recommendation to jump to the dense 23000+ / pre-06000 pockets still stands for the curator to weigh.

**Update 2026-07-18 (16000–16400 slice swept)**: A routine systemic-fix run cleared the next scoped slice per-entry, fixing **12 instances across 11 entries** (`detect` filtered total 1180 → 1168). Density dropped to ~15 filtered flags across the 400-ID slice (~19/500) — a sparse, clean band consistent with the post-2026 creation batches. Mix: pure-kana katakana/kana de-wraps (ネットワーク/ドル/テレホンカード/テスト/チーム/ほぼ), o-prefix repositions (`{お金|おかね}` → `お{金|かね}`, `{お世辞|おせじ}` → `お{世辞|せじ}`), and over-wrapped okurigana/compound splits (`{あの時|あのとき}` → `あの{時|とき}`, `{大好き|だいすき}` → `{大|だい}{好|す}き`, `{取り戻す|とりもどす}` → `{取|と}り{戻|もど}す`, `{人差し指|ひとさしゆび}` → `{人|ひと}{差|さ}し{指|ゆび}`). None of the 12 findings sat inside a `⟦...⟧` surface, so `word_id_lookup.json` keys are unaffected. Validation stayed clean (398/398 in range). §4 furigana self-screen: 11 screened, **3 flags all rejected** (16008 通信網 truncated-token misread, 16117 並行 partial-reading misread, 16373 弾く partial-reading FP — none on an edited pair). Next ready slice: 16400+ and the larger pre-06000 backlog — the 2026-07-14 density recommendation to jump to the dense 23000+ / pre-06000 pockets still stands for the curator to weigh.

**Update 2026-07-19 (16400–16999 slice swept)**: A routine systemic-fix run cleared the next scoped slice per-entry, fixing **26 instances across 16 entries** (`detect` filtered total 1168 → 1141). Mix: pure-kana katakana/kana/numeral de-wraps (ドラマ/コピー/プリンター×2/リース/クラス/レッテル/おばあちゃん/おこげ, numeral `{100|ひゃく}` → `100`), over-wrapped compound/okurigana splits (`{幕の内弁当|まくのうちべんとう}` → `{幕|まく}の{内|うち}{弁当|べんとう}` across headword + 3 examples + 2 notes, `{髪の毛|かみのけ}` → `{髪|かみ}の{毛|け}`×2, `{見当たる|みあたる}` → `{見当|みあ}たる`, `{行き先|ゆきさき}` → `{行|ゆ}き{先|さき}`, `{贈り物|おくりもの}` → `{贈|おく}り{物|もの}`, `{頂き物|いただきもの}` → `{頂|いただ}き{物|もの}`, `{力いっぱい|ちからいっぱい}` → `{力|ちから}いっぱい`, `{導く|みちびく}` → `{導|みちび}く`), and o-prefix repositions (`{お歳暮|せいぼ}` → `お{歳暮|せいぼ}`, `{お中元|ちゅうげん}` → `お{中元|ちゅうげん}`, `{お盆|おぼん}` → `お{盆|ぼん}`). The `弁当` group is kept whole (`{弁当|べんとう}`, 183 uses) per the dominant convention, while `髪の毛` follows the split convention (`{髪|かみ}の{毛|け}`, 13:3). None of the findings sat inside a `⟦...⟧` surface, so `word_id_lookup.json` keys are unaffected. Validation stayed clean (579/579 in range). §4 furigana self-screen: 15 screened, **2 flags both rejected** (16588 毛髪 single-unit compound token-split FP; 16951 誘導灯/誘導路 compound readings correct — neither on an edited pair). Next ready slice: 17000+ and the larger pre-06000 backlog.

**Update 2026-07-20 (17000–17999 slice swept)**: A routine systemic-fix run cleared the next scoped slice per-entry, fixing **33 instances across 23 entries** (`detect` filtered total 1141 → 1109). Mix: pure-kana de-wraps of katakana/loanwords and a placeholder (ゲームセンター/アルバイト/コンパス/チームワーク/チェス/ケーキ/インフラ/チケット, `{〇〇|まるまる}` → `〇〇`), one hiragana de-wrap (わざわざ), three malformed **empty-reading** wrappers de-wrapped (`{ぶつかる|}` → `ぶつかる`, `{ガイドライン|}` → `ガイドライン`, `{する|}` → `する`), o/go-prefix repositions (`{ご飯|はん}` → `ご{飯|はん}`, `{お会|おあ}い` → `お{会|あ}い`, `{お支払|しはら}い` → `お{支払|しはら}い`, `{お袋|ふくろ}` → `お{袋|ふくろ}`), and over-wrapped okurigana/compound splits (`{崖っぷち|がけっぷち}` → `{崖|がけ}っぷち`, `{生え際|はえぎわ}` → `{生|は}え{際|ぎわ}`×2, `{火の見櫓|ひのみやぐら}` → `{火|ひ}の{見|み}{櫓|やぐら}`×2, `{わき見|わきみ}` → `わき{見|み}`, `{連れ合|つれあ}い` → `{連|つ}れ{合|あ}い`). The **17879_uonome headword** `{魚の目|うおのめ}` → `{魚|うお}の{目|め}` (9 instances incl. headword + all examples + notes) was verified safe against `word_id_lookup.json` first — the lookup is keyed by reading + furigana-stripped headword (both unchanged) and inbound inline links resolve by `entry_id`, so no link breakage. No `⟦...⟧` surfaces touched anywhere in the slice. Validation stayed clean (976/976 in range). §4 furigana self-screen: 23 screened, **7 flags all rejected** — all the documented partial-reading/token-split/alt-reading false-positive family (17043 軽作業, 17340 車, 17398 負ける-gloss non-issue, 17457 自ら/赴く, 17769 余熱, 17937 二次創作, 17946 中火 alternate reading ちゅうび) and **none on an edited pair**. Next ready slice: 18000+ and the larger pre-06000 backlog — the 2026-07-14 density recommendation to jump to the dense 23000+ / pre-06000 pockets still stands for the curator to weigh.

**Update 2026-07-22 (18000–18999 slice swept)**: A routine systemic-fix run cleared the next scoped slice per-entry, fixing **28 instances across 20 entries** (`detect` filtered total 1109 → 1081). Mix: pure-kana de-wraps of katakana/kana (`{パクリ|ぱくり}`→`パクリ`, `{リスク|りすく}`→`リスク`, `{シーエー|しーえー}`→`シーエー`×2, `{クロール|くろーる}`→`クロール`, `{イメージ|いめーじ}`→`イメージ`, `{システム|しすてむ}`→`システム`, `{イベント|いべんと}`→`イベント`, `{やつ|やつ}`→`やつ`), o/go-prefix repositions (`{お返|かえ}`→`お{返|かえ}`×2, `{お菓子|おかし}`→`お{菓子|かし}`, `{お茶|おちゃ}`→`お{茶|ちゃ}`, `{お疲|おつか}`→`お{疲|つか}`×3, `{お守|おまも}`→`お{守|まも}`×3), and over-wrapped okurigana/compound splits (`{花びら|はなびら}`→`{花|はな}びら`×2, `{やり直|やりなお}`→`やり{直|なお}`, `{寄り合い|よりあい}`→`{寄|よ}り{合|あ}い`, `{賭け事|かけごと}`→`{賭|か}け{事|ごと}`, `{差し水|さしみず}`→`{差|さ}し{水|みず}`, `{決め手|きめて}`→`{決|き}め{手|て}`, `{思い出横丁|おもいでよこちょう}`→`{思|おも}い{出|で}{横丁|よこちょう}`×2). Also corrected **18374_gokurousama**'s `contrast` cross_reference headword `{お疲|おつか}れ{様|さま}` → `お{疲|つか}れ{様|さま}` to match target **05208_otsukaresama**'s canonical form (a 4th お疲 fix beyond the 3 the detector flagged in notes). No `⟦...⟧` surfaces touched anywhere in the slice, so `word_id_lookup.json` is unaffected. Validation stayed clean (998/998 in range). §4 furigana self-screen: **20 screened, 0 flags, 0 skipped** — a clean pass. Next ready slice: 19000+ and the larger pre-06000 backlog.

**Update 2026-07-26 (density is ~2× higher above ID 21000 — remaining sweep effort must be estimated per-slice, not extrapolated)**: The 2026-07-26 systemic-fix sweep of **21000–21999** found **58 instances across 46 entries**, against roughly **24 instances per 1,000-ID block** measured through the 06000–20999 sweeps. The newer creation batches evidently never had a wrapper-format pass.

Two consequences for planning this backlog:

- **Do not extrapolate.** The remaining scope above 21000 is roughly double what a linear projection from the completed blocks would suggest. Re-run `check_furigana_format.py --summary` per slice before sizing a sweep.
- **The 2026-07-14 reprioritization still holds and is now better supported**: that harvest recommended shifting sweep effort to "the dense 23000–29999 + pre-06000 blocks" on the observation that the backlog *thins* above ~11000. This measurement refines it — the thin region is the middle (roughly 11000–20999), and density recovers sharply in the newest batches. Work outward from both ends, not sequentially.

**Update 2026-07-27 (a *sixth* malformed-wrapper sub-family measured dictionary-wide: no-pipe brace spans, invisible to the detector; plus a wrapper defect that silently corrupts generated conjugation tables)**: The 2026-07-27 systemic-fix sweep of **22000–23499** cleared **101 instances across 77 entries** (filtered scope 974 → 873), confirming the 2026-07-26 density finding — the slice ran ~34 instances per 1,000-ID block, well above the ~24 of the completed 06000–20999 blocks. Two findings go beyond the routine wrapper work:

- **No-pipe brace spans are a real family the detector cannot see.** `FURIGANA_PATTERN` in `build/japanese_utils.py` is `\{([^|]+)\|([^}]+)\}` — it **requires a pipe**, so a brace span with no reading (`{コンビニ}`, `{稀}`) is never matched, never stripped, and reaches the rendered page as **visible curly braces**. All five of `check_furigana_format.py`'s subpatterns (`nested`, `o-go-prefix`, `over-wrapped`, `pure-kana`, `reading-truncated`) assume a pipe is present, so this family is absent from every scope estimate in this section. Measured across the string values of all entries: **887 instances across 616 entries** — comparable in size to the entire remaining P9 backlog. This quantifies what the 2026-07-23 P21 update had seen only anecdotally (`コーラス{グループ}` / `コーラス{パート}` in 06574). Two sub-shapes: (a) kana/loanword spans to de-brace (`{コンビニ}`, `{ゴミ}`, `{スカート}`, `{おひたし}`); (b) **bare kanji with no reading at all** (`{稀}`, `{続}`, `{匂}`, `{漸}`) — worse, since those render with braces *and* leave the kanji unglossed. **Not mechanically sweepable**: a minority are intentional notation that must keep its braces (`{1, 2, 3, ...}` set notation in 23397 自然数, `{X}` pattern placeholders, `{emotion}` category labels), so per-entry verification applies here as it does to the rest of P9. Recommended: add a `no-pipe` subpattern to `check_furigana_format.py` with the notation cases as a documented reject family, and track it as a P9 sibling item.
- **An over-wrapped *verb headword* silently corrupts the generated conjugation table.** 22070 走り続ける shipped with `{走り続ける|はしりつづける}`; `add_conjugations.py` strips the ichidan る from the rendered tail, and a whole-word wrapper hides it, so all **33** generated forms doubled the stem (`{走り続ける|はしりつづける}る` → 走り続けるる, `…ます` → 走り続けるます). The entry validated cleanly and the error survived from creation (2026-04-04) until this sweep rewrapped the headword and `--force`-regenerated the table. A dictionary-wide sweep for the signature found **0 other live instances**, so this is not a backlog of its own — but it raises the stakes of the `over-wrapped` subpattern from cosmetic to **data-corrupting when the entry is a verb**, and argues for the cheap invariant proposed in `tooling-backlog.md`: for `conjugation.type` in `{ichidan, godan}`, `strip_furigana(forms[0].affirmative)` must equal `strip_furigana(headword)`.

**Update 2026-07-28 (23500–23999 swept; the "de-wrap" family is dominated by *note-field* loanword glosses)**: The 2026-07-28 systemic-fix sweep cleared **110 filtered instances across 63 entries** (filtered scope 871 → 761; total 873 → 763). Density held at the elevated post-21000 rate (~110 per 500-ID block here versus ~34 per 1,000 in 22000–23499), so the "work outward from both ends" advice above remains correct.

- **The 23500s skew overwhelmingly to `pure-kana` inside `notes`.** 100 of the 110 findings were pure-kana, and the great majority were katakana loanwords wrapped in a note's SIMILAR WORDS / usage list (`{ヘルスメーター|へるすめーたー}`, `{ファミリービジネス|ふぁみりーびじねす}`, `{スタンディングオベーション|すたんでぃんぐおべーしょん}`). This is the same **create-era note-field blind spot** flagged in the P21 2026-07-21 and 2026-07-23 updates, now visible at scale in a *scientific/technical* creation cohort where notes carry long loanword contrast lists. It reinforces the standing recommendation that the sweep must scan `notes`, not just headwords/examples.
- **Four defects in this slice were outside the wrapper family and needed hand adjudication**, none of them mechanically fixable: `{X|がく}` (23819 現象学) where the note's own "X + 学 produces field names" pattern had lost its 学 → `X{学|がく}`; `{それは|あなた}` (23874 次第で) where surface and reading were unrelated words → plain `それはあなた`; `{人|ひと}{々|びと}` (23903 原住民) → `{人々|ひとびと}`, matching the 13 existing uses dictionary-wide; and `{兎形目|うさぎがための もく}` (23656 齧歯類), a stray の with no source kanji → `{兎形目|うさぎがたもく}`, disambiguated by the entry's own `ウサギ{目|もく}` gloss. Only the last was caught by the §4 screener; the other three were only visible by reading the surrounding note. **A detector-driven sweep that trusts `suggestion` alone would have missed or mis-fixed all four** — per-entry verification continues to earn its cost.
- **Empty-reading wrappers (`{チーム|}`, `{ある|}`) cluster tightly** in 23798–23809, a contiguous creation run. Like the no-pipe family above, these are a creation-time artifact of one batch rather than a diffuse problem, which is why per-slice measurement beats extrapolation.

**Update 2026-07-29 (a measured slice, and two cautions about how to run the remaining sweep)**: The 2026-07-28 polish run swept **23500–23999** and reported three findings that change how the rest of this priority should be worked. They are written up in full in [topics/furigana-wrapper-anomalies.md](../topics/furigana-wrapper-anomalies.md) → "What a measured slice looks like (23500–23999)"; in brief:

1. **100 of 110 findings were `pure-kana` wrappers inside `notes` fields** — katakana loanwords in SIMILAR WORDS / contrast lists, not headwords or examples. The create-era note-field blind spot, confirmed at scale in the scientific/technical creation cohort.
2. **Four defects had `suggestion: null` and were outside the wrapper families entirely** — `{X|がく}` (23819, lost its 学), `{それは|あなた}` (23874, surface and reading unrelated), `{人|ひと}{々|びと}` (23903), `{兎形目|うさぎがための もく}` (23656, stray の). A sweep that trusted the detector's `suggestion` field would have missed or mis-fixed all four. **Do not treat `suggestion: null` rows as low-priority residue; they are where the real errors are.**
3. **Empty-reading wrappers cluster in the contiguous 23798–23809 creation run**, not diffusely. Per-slice measurement beats linear extrapolation for sizing these sweeps.

**Detector count this refresh**: 763 instances / 522 entries (error=2, info=272, warn=489; pure-kana=373, over-wrapped=272, o-go-prefix=116, nested=1, reading-truncated=1) — essentially flat against the 761 recorded in `backlog-queue.json`.

**Update 2026-07-30 — the katakana sub-family is already detected, and it is the one slice of `pure-kana` that needs no judgment.** A 2026-07-30 polish run found `⟦{ケーキ|けーき}→ケーキ：01356_keeki⟧` in 05837 しっとり's notes (fixed in-run) and proposed that `check_furigana_format.py` should grow a check for katakana surfaces inside `{…|…}`. **It already has one** — these land in the existing `pure-kana` subpattern, and the harvest measured **258 of the 373 `pure-kana` findings** as katakana-surfaced. (This is the third instance in two weeks of a run proposing a check the tooling already performs; see [Instrument Defects](../topics/instrument-defects.md).)

The useful change is therefore not a new check but a **subpattern split**, because the two halves of `pure-kana` have different fix rules:

| Sub-family | Count | Fix |
|---|---|---|
| Katakana surface (`{ケーキ|けーき}`, `{バイク|ばいく}`, `{チーム|ちーむ}`) | 258 | **Unconditional** — katakana needs no reading gloss; delete the wrapper, keep the surface. |
| Everything else (`{3|さん}`, hiragana surfaces, numerals) | 115 | Judgment — a numeral's reading is genuinely informative and should often stay. |

Splitting them turns 258 instances from "review queue" into "mechanical sweep with a validation pass", which is the distinction §B draws between what may be applied mechanically and what needs eyes. The residue that still needs judgment shrinks to 115. Distribution across fields is even (`examples` 197 / `notes` 175), so this is not a note-field-specific artifact like the 2026-07-29 slice above.

## Priority 10: "するする" typo in TRANSITIVITY → Pattern lines

**Source**: Comprehensive-polish 2026-05-17 sessions 001–002 (entries 01808–01856)

Multiple entries in the 01808–01856 range have `するする` instead of `する` in their TRANSITIVITY → Pattern notes field. Likely a template copy-paste error during batch creation. The originating sessions fixed all instances they encountered (01811, 01823, 01826, 01828, 01830, 01832, 01833, 01835, 01837, 01839, 01841, 01843, 01845, 01847, 01849, 01851, 01852, 01855), but the pattern may extend into ranges not yet polished.

**Detection**: `grep -rl 'するする' entries/ | head -30`

**Suggested action**: One-shot grep-and-fix pass replacing `するする` with `する` in the notes field. Low risk — the doubled form is never correct Japanese.

## Priority 11: Batch-creation semantic tag "transportation" misapplied

**Source**: Comprehensive-polish 2026-05-17 sessions 001–002 and 009 (entries 01808–02011)

Entries in the 01808–02011 range have `semantic: ["transportation"]` applied to words with no connection to transport. Examples: 01815 ({飽|あ}きる, "to get bored"), 01822 ({居眠|いねむ}り, "dozing off"), 01825 ({衣服|いふく}, "clothing"). The polish sessions fixed individual entries, but the pattern suggests systematic misapplication in this ID range during batch creation.

This is the same category of stale-auto-label error as the `furniture` tag in the 01490–01511 range and `electronics` in the 02000s, now joined by `transportation` in the 01808–02011 range. See [Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Stale auto-labels" for the broader analysis.

**Suggested action**: Spot-check entries in the 01800–02100 range for `semantic: ["transportation"]` tags that don't match entry content. If widespread, a targeted batch fix is warranted.

**Update 2026-05-19**: Two more entries with wrong semantic tags surfaced in the 02251–02273 range (02268 和紙, 02269 りんご), suggesting the pattern extends beyond the 02011 boundary identified above. Tag assignment quality appears inconsistent across multiple creation batches, not just a single cohort.

**Update 2026-05-25**: Entry 03218 手術 had `semantic: ["body-part", "time-general"]` — neither tag fits a surgical procedure (should be "medical" or "action"). This confirms the wrong-specific-tag pattern extends into the 03200+ range with novel tag combinations, not just the `transportation`/`furniture`/`electronics` labels seen in earlier ranges.

**Update 2026-05-26**: Two comprehensive-polish sessions (entries 03360–03385 and 03491–03510) surfaced five more wrong-tag instances with novel tag types: "tool" on adjective 03376_seishiki, "leisure" on 03383_tai (military unit), "time-general"/"weather" on 03385_taion (body temperature), "body-part" on 03491_choushi (condition) and 03503_chiryou (treatment), and "furniture" on grammatical word 03494_donnani. The misapplied-tag pattern now spans from the 01490s through the 03500s with at least seven distinct wrong-tag categories (transportation, furniture, electronics, clothing, body-part, tool, leisure, time-general, weather).

**Update 2026-05-27**: Three more comprehensive-polish sessions (entries 03582–03598, 03662–03676, 03677–03698) surfaced a further wave of wrong semantic tags extending the range to 03800:
- 03582–03598: "electronics" on 評価/表面/不幸; "transportation" on 服装; "body-part" on 笛; "emotion" on 不自由
- 03662–03676: "electronics" on 喜び (03672) and 理解 (03674)
- 03686–03698: "animal-mammal" on 像 (03691), "food" on 班 (03697), "body-part"/"transportation" on 進行 (03686), "body-part"/"occupation"/"time-general"/"transportation" on 操縦 (03689), "transportation" on 羽根 (03696)

The wrong-tag categories now include at least eleven distinct labels: transportation, furniture, electronics, clothing, body-part, tool, leisure, time-general, weather, animal-mammal, and food. The pattern spans 01490s through 03700s. A dedicated semantic-tag validation pass over the 03500–03800 range is warranted, as the density of wrong tags in this range appears higher than in earlier ranges.

**Update 2026-05-28**: Two more entries in the 03877–03888 range: 03881 釘 (nail) has "body-part" (should be "tool"), 03883 屑 (scrap/waste) has "furniture" (meaningless for this word). Confirmed range now extends through the 03800s. Added to [Entry Follow-ups](entry-followups.md).

**Update 2026-05-30**: Five comprehensive-polish sessions (2026-05-28 session 003 and 2026-05-29 sessions 001, 006, 007, 009) confirmed the wrong-semantic-tag pattern extends well into the 04000+ range:
- 03970–03990: "furniture", "electronics", "leisure", "animal-insect", "occupation", "time-general" on words like 我が〜, 器具, 基地, 弟子, 父母
- 04031–04042: 04038 台詞 had 5 wrong tags ("building", "electronics", "geography", "leisure"); 04039 扇子 had "electronics"; 04035 地盤 had "education"
- 04126–04149: 04134 液体 "body-part"; 04135 応用 "electronics"; 04141 系統 "furniture"; 04146 交替 "emotion"/"geography"; 04148 肯定 "electronics"/"furniture"/"geography"; 04149 鉱物 "time-general"
- 04150–04169: 04154 混合 "geography"; 04158 祭日 "geography"; 04166 資料 "furniture"; 04167 公式 "furniture"
- 04185–04204: 04198 車輪 "clothing" (→ transportation); 04201 障子 "communication"/"education" (→ building)

The confirmed range now extends from the 01490s through at least the 04300s. All sessions noted the pattern appears systematic across the 04000+ range and likely requires a bulk audit. Multiple sessions independently recommended a dedicated semantic-tag validation pass. The wrong-tag category set now includes at least fourteen distinct labels: transportation, furniture, electronics, clothing, body-part, tool, leisure, time-general, weather, animal-mammal, food, building, geography, and communication.

**Update 2026-05-31**: Four more comprehensive-polish sessions (2026-05-30, entries 04205–04349) confirmed the wrong-tag pattern continues unabated through the 04300s:
- 04205–04222: "electronics" on 申請 (application), "body-part" on 診断 (diagnosis), "education" on 実績 (track record)
- 04223–04243: "electronics" on 切り替える (should be "action"), "communication" on 振り向く/見送る (should be "action"), "food"/"tool" on 振る舞う
- 04282–04306: "electronics" on transport/work entries, "building" on 乗換 (should be transportation), "clothing" on 歯車 (should be general), "movement" on 蛙 (should be animal-insect), "furniture" on 推定 (should be general), "leisure" on 水産 (should be nature-environment)
- 04307–04326: "geography"/"time-general" on 発電 (power generation)
- 04327–04349: "body-part" on 反映, "leisure" on 売買, "education"/"leisure" on 政党, "leisure" on 引算

A recurring diagnostic: the AI model assigns semantic tags based on example sentence topics rather than the headword's semantic domain.

**Update 2026-06-01**: Two more comprehensive-polish sessions (2026-05-31, entries 04371–04395 and 04457–04466) confirmed the pattern continues into the 04400–04500 range:
- 04371–04395: Nature/food nouns (04383 全般, 04384 柿, 04387 栗, 04389 葬式) had template defaults "time-general", "transportation", "tool" — corrected in session.
- 04457–04466: Performing arts and musical instrument entries had wrong tags: 04459 脚本 "electronics", 04460 演出 "communication"/"education"/"furniture"/"leisure", 04462 フルート "body-part", 04464 三味線 "food", 04465 尺八 "body-part". All corrected to "leisure".

The confirmed range now extends from the 01490s through at least the 04500s. The wrong-tag category set remains at fourteen distinct labels.

**Update 2026-06-02**: Two more comprehensive-polish sessions (2026-06-01, entries 04533–04553 and 04574–04594) confirmed the pattern continues through the 04590s:
- 04533–04553: 04547 凸凹 "furniture"/"tool"→"general", 04549 伝染 "body-part"→"general", 04550 大金 "time-general"/"tool"→"work", 04535 サングラス "general"→"clothing", 04540 鉄砲 "general"→"weapon", 04544 団扇 "electronics"→"tool"
- 04574–04594: 04583 聞き取る "geography"/"work"→"communication"/"action", 04585 早まる "electronics"/"time-general"→"action", 04589 枯れる "furniture"→"nature"/"action", 04590 思い切る "communication"→"action"

**Update 2026-06-03**: Four more comprehensive-polish sessions (2026-06-02, entries 04730–04801) confirmed the pattern extends into the 04700–05000 range:
- 04730 フォロー had "building"/"transportation"→"communication"/"action"
- 04741–04760: 04742 決勝 "furniture"/"tool"→"sports"/"competition"; 04747 やばい "weather"→"descriptive"; 04757 クラウド "weather"→"technology"
- 04761–04782: 04768 一期一会 and 04773 四苦八苦 both had "furniture"→"expression". The "furniture" tag now confirmed as a template artifact that crept into yojijukugo and expression entries created in bulk.
- 04783–04801: 04796 関数 "electronics"→"general" (mathematics); 04799 魅力的 "furniture"→"general" (appearance); 04800 内閣 "furniture"→"general" (government)

The confirmed range now extends from the 01490s through at least the 04800s. A targeted semantic-tag audit of the 04700–05000 range is warranted.

**Update 2026-06-04**: Three more comprehensive-polish sessions (2026-06-03, entries 04985–05037) confirmed the pattern extends into the 05000+ range:
- 04985–04992: 04985 浴槽 "animal-mammal" (→ building/household); 04988 洗面台 "animal-mammal"/"transportation" (→ building/household); 04992 前菜 "electronics" (→ food)
- 05018–05032: Health/medical entries had emotion/weather/time-general tags: 05018 凍傷 "weather" (→ health); 05019 腹痛 "body-part"/"emotion" (→ health); 05020 腰痛 "emotion" (→ health); 05028 内臓 "time-general" (→ body)

A sub-pattern emerged: health/medical vocabulary is systematically receiving emotion, weather, and time-general tags — three categories with no semantic connection to medical content. The confirmed range now extends from the 01490s through at least the 05000s.

**Update 2026-06-05**: Three more comprehensive-polish sessions (2026-06-04, entries 05095–05141 and 05211–05230) confirmed the pattern extends well into the 05200+ range:
- 05095–05120: cosmetics tagged "electronics", sunscreen tagged "electronics", ガイド tagged "tool", 姑 tagged "animal-insect"
- 05121–05141: 05134 納品 (delivery) tagged "communication" — delivery of goods is not communication; should be "action" or logistics-related
- 05211–05230: 05212 取材 tagged "building"/"education"/"transportation"; 05221 忍耐 tagged "clothing"/"time-general"; 05227 広報 tagged "geography"; 05228 tagged incorrectly

The confirmed range now extends from the 01490s through at least the 05230s. A targeted bulk audit of the 05000–05500 range is warranted.

**Update 2026-06-06**: Five comprehensive-polish sessions (2026-06-05, sessions 021–025, entries 05291–05389) confirmed the pattern saturates the 05300s, with a clear common origin: most of the wrong-tagged entries were created by **claude-opus-4-5 with modified date 2026-04-14**, pointing to a single batch run whose semantic-tag data was cross-contaminated.
- 05291–05312: "transportation" on だるい/面倒くさい, "animal-mammal" on 浴室, "animal-insect" on だるい, "furniture" on 叶う
- 05318 体力: "leisure" (→ health/body); check the 気力/精力/忍耐力 cluster
- 05332–05335 (足し算, 引き算, 掛け算, 割り算): "body-part"/"furniture"/"time-general" instead of "mathematics"
- 05344 焦げる: "body-part" (→ action)
- 05349–05373 (mimetic adverbs): wrong semantic tags (food, furniture, body-part, electronics, animal-mammal, building, leisure) instead of "descriptive" — plus the spurious-conjugation problem logged under Priority 6
- 05374–05389: health entries (下痢, 便秘, インフルエンザ, 包帯, 絆創膏) tagged "general"/"body-part" instead of "health"; education entries (生徒会, 職員室) tagged "general" instead of "education"

The 2026-04-14 claude-opus-4-5 modified-date signature gives a concrete way to scope the eventual bulk fix: the tag-validation pass (Tooling Backlog item 6) could prioritize entries carrying that creation signature.

**Update 2026-06-07**: Three more comprehensive-polish sessions (2026-06-06, sessions 029/030/033, entries 05468–05559) confirmed the tag-drift pattern extends into the 05500+ range:
- 05468–05482: 05474 分量 "building"/"transportation" (→ measurement), 05475 重量 formality "informal" (→ neutral), 05476 金槌 "food"/"tool" (→ tool only)
- 05483–05502: 05484 体温計 "time-general"/"tool"/"weather" (→ health/tool), 05485 体重計 "animal-mammal"/"tool" (→ health/tool), 05486–05489 plants "general" (→ plant/nature), 05496 ジャングル "general" (→ nature/geography), 05497 高原 "food" (→ geography/nature), 05498 海辺 "general" (→ geography/nature), 05499 群島 "tool" (→ geography/nature), 05500 本土 "general" (→ geography)
- 05540–05559: 05551 えんちゅう "body-part", 05556 ないがい "electronics"/"furniture", 05557 だいしょう "building" — all fixed to "general"

The confirmed range now extends from the 01490s through at least the 05559. The pattern shows no sign of abating.

**Update 2026-06-08**: Comprehensive-polish session 037 (entries 05617–05635) surfaced four more wrong-tag instances at the leading edge of the polished range: 懸念 "electronics" (→ emotion/cognition), 端末 "building"/"transportation" (→ technology/general), 促進 "emotion"/"time-general"/"work" (→ action), 七夕 "animal-mammal" (→ culture/event). The confirmed range now extends from the 01490s through at least the 05635, tracking the comprehensive-polish frontier (main progress `next: 05735` as of this session). The signature is unchanged — example-sentence-topic contamination on a single 2026-04-14 claude-opus-4-5 batch — and the case for the Tooling Backlog item 6 tag-validation pass (scoped by that creation signature) only strengthens. Note that the comprehensive-polish frontier has now nearly reached the **upper** bound of the originally-flagged batch; once polishing passes ~05735 the live tag-drift reports should taper, leaving the *un-polished* high-ID ranges (anything from that 2026-04-14 batch sitting above the polish frontier) as the remaining audit surface — an argument for running the batch-signature audit pass rather than waiting for sequential polishing to reach every contaminated entry.

**Update 2026-06-09**: Three comprehensive-polish sessions (sessions 045, 049, 050, entries 05784–05953) confirmed the tag-drift pattern continues through the 05900s:
- 05784–05804: "electronics" on 風呂敷, "animal-fish" on じめじめ, "food" on こそこそ, "communication+education+tool" on 提灯, "furniture" on 暖簾. The "furniture" and "tool" tags appear loosely applied across the 05500–06000 range.
- 05891–05915: "electronics" on るんるん, "furniture" on 淡々, "tool" on 刻々, plus a wrong formality "informal" on 仲裁 (corrected to "neutral"). Tag drift continues unabated.
- 05936–05953: "animal-fish" on じとじと (→ "descriptive"), "animal-insect" on のそのそ (→ ["action", "descriptive"]). These are mimetic adverbs/descriptives — the same sub-pattern seen in the 05349–05373 range. The comprehensive-polish frontier now sits at entry 05954; the contaminated batch signature extends at least this far. **Cross-model accuracy-review (session 001)** independently found semantic misassignment in early entries (00016–00200) — different creation cohort, different failure mode (over-applied domain tags on multi-sense polysemous words), documented under the new Priority 17 (formality) and in [Entry Follow-ups](entry-followups.md).

**Update 2026-06-10**: Two more confirmations from Routine v2 runs.
- **Comprehensive-polish session 007 (entries 05970–05989)** found dense tag errors at the leading edge of the contaminated batch: a medical cluster (05975–05979: 通院, 処方, 感染, 炎症, 健康診断) and an aviation cluster (05981–05982: 離陸, 着陸) carried body-part/clothing/furniture/leisure/geography tags — the model had copied tags from an unrelated entry. Fixed in session; the 05970–05990 range likely holds more.
- **Cross-model accuracy-review session 002 (entries 00201–00450)** confirmed the same wrong-tag class in the *low-ID core/basic* range (a different cohort from the 2026-04-14 batch): 00281 醜い (food/leisure/slang/colloquial → emotion/appearance/literary), 00299 虫歯 (body-part → health — a dental condition, not a body part), 00240 小〜 (grammatical → size), 00232 記念 ("memory" → "memorial"). A recurring **sub-pattern** here is `body-part` misapplied to conditions/diseases (虫歯; cf. 03218 手術, 05019 腹痛 in earlier updates). The authoritative remediation path is now the accuracy-review mode's LLM `tags` pass — the [Quality Metrics Trend](../topics/quality-metrics.md) snapshot shows `tags` is the highest-precision review dimension (6.8% apply rate vs ~2% for gloss/translation), i.e. the dimension actually worth driving a fix from.

**Update 2026-06-13**: Comprehensive-polish session 008 (entries 06101–06110) found three more instances in the 06100s: 06107_junshu (遵守, compliance/observance) had `semantic: ["transportation"]` — corrected to `["action"]` (same wrong-specific-tag pattern as the rest of P11); 06101_hakumai (白米) had `semantic: ["general"]` instead of `["food"]`; 06106_katsuo (鰹, bonito) had `semantic: ["general"]` instead of `["animal-fish"]`. Note that the food/ingredient instances are the P13 under-specification pattern (correct fallback applied where a specific tag was available), while 06107 is the classic P11 wrong-specific-tag error. The contaminated range now extends at least to the 06100s. These are a different creation cohort than the 2026-04-14 claude-opus-4-5 batch that dominates the 01490–06100 range.

**Update 2026-06-14**: Comprehensive-polish session (frontier entries 06121–06128, all cultural-vocabulary nouns) found three more wrong-tag instances in this cohort: 06121_hibachi (火鉢) had `clothing` (→ `daily-life`), 06127_kouden (香典) had `time-general` (→ `culture`), and souryou (送料, shipping charge) had `communication` (→ `shopping`). Same example-topic-contamination signature as the rest of P11, now confirmed at the 06120s frontier. The session recommended a semantic-tag audit of the whole 2026-early cultural-vocabulary cohort (roughly 06100–06130), since the errors cluster tightly by creation batch rather than by word meaning.

**Update 2026-06-15**: Three more Routine runs confirmed the pattern persists at the comprehensive-polish frontier and re-confirmed a dense pocket in the 05000–05300 range:
- **Frontier 06129–06132** (consumer/business suru-noun cohort): 06129_kaiyaku had `geography,work` (→ business), 06130_henkin had `action` (→ money). Zero inline links plus template-default tags — same signature as the 06121–06128 cohort.
- **Frontier 06137–06149** (idioms / proverbs / yojijukugo): inaccurate default tags — 06139 `body-part` (→ movement), 06140 `occupation` (→ proverb), 06142 `communication`/`furniture` (→ proverb). A targeted tag-drift + inline-link pass over 06140–06170 would clean a coherent block.
- **05000–05300 pocket** (polish session): many genuine clearly-wrong tags fixed (26 in one run) — `body-part`/`communication` on 柱, `emotion` on 箪笥, `time-general` on ベランダ/わさび, `food` on コック/ウェイター, `body-part` on mimetic adverbs. This range also carries widespread **formality/politeness** data errors (茶漬け `politeness: honorific`, 羊羹 `formality: formal`) left for a dedicated register-tag pass — see P17.

The contaminated frontier now tracks to the 06140s; the 05000–05300 pocket shows the same 2026-04-14-batch signature as the rest of P11.

**Update 2026-06-12**: Comprehensive-polish session (entries 06048–06067) confirmed a **compound-verb / suru-verb sub-pattern** at the leading edge of the contaminated batch: compound verbs and suru verbs were systematically assigned object-category tags (electronics, clothing, tool, furniture, animal-mammal, occupation, body-part) instead of the action/cognition/communication/emotion tags appropriate for their meanings. Confirmed instances: 06051 clothing→movement, 06052 [food,leisure,tool]→action, 06053 [communication,furniture]→cognition, 06055 electronics→emotion, 06056 electronics→communication, 06058 animal-mammal→communication, 06060 electronics→cognition, 06062 occupation→cognition, 06066 action→emotion, 06067 action→emotion. Root cause: original AI generation applied topic-domain tags based on example sentence context rather than the verb's own semantic domain. The `check_tag_drift.py` unknown-semantic detector (P20) will flag the out-of-vocabulary cases; the correct-vocabulary-but-wrong-category cases (e.g. "action" on a cognition verb) are not detectable mechanically and require the accuracy-review `tags` pass or per-entry polishing. The 06000 range likely holds further instances of this sub-pattern.

**Update 2026-06-16**: A 2026-06-15 routine polish observation documented a dense pocket of the *in-list-but-wrong-category* tag drift across the **0552x–0570x range** (a different ID band from the 06xxx frontier but the same failure mode), with three recognisable sub-clusters:
- **Four-character idioms / yojijukugo** tagged with object domains: 起死回生, 七転八起, 自画自賛 → `furniture`; 油断大敵 → `leisure`/`emotion` (should be `expression`/`proverb`). Same artifact as the 04768 一期一会 / 04773 四苦八苦 → `furniture` cases noted in the 2026-06-03 update.
- **〜的 / 〜性 abstract adjectives/nouns** tagged with unrelated domains: 協力的, 歴史的, 政治的, 主観的, 全面的 → `time-general`/`education`.
- **Concrete nouns mis-tagged**: 天秤 → `clothing`; 苦楽/寒暖 → `body-part`; 頷く → `work`.
These are all `VALID_SEMANTIC` tags applied to the wrong domain, so the `check_tag_drift.py` unknown-semantic detector (P20) will **not** catch them — they need the accuracy-review `tags` pass or per-entry polish. The band sits just below the comprehensive-polish frontier (`next: 06147`), so sequential polishing has not yet reached it; the contaminated batch signature is consistent with the 2026-04-14 claude-opus-4-5 run that dominates the rest of P11.

**Update 2026-06-17**: Two 2026-06-16 Routine runs (an accuracy-review pass over 5704–6139 and a second accuracy-review pass over 6140–6340) re-confirmed the density of this pattern across the **5700–6340 block** and quantified it for the first time at the frontier:
- **5700–6100 block** (accuracy-review observation): ~50 entries carried genuinely-wrong or out-of-taxonomy concrete-domain tags — `electronics`/`furniture`/`weather`/`body-part`/`geography`/`leisure` misapplied, `onomatopoeia` **missing** on clearly mimetic words, plus invalid (out-of-list) `payment`/`body`/`death` tags. The invalid ones are P20 (unknown-semantic) territory; the misapplied in-list ones are the core P11 wrong-category failure.
- **6140–6340 range** (accuracy-review run): ~30% of entries carried categorically-wrong auto-assigned tags — 朱肉 (vermilion ink-pad) tagged `animal-mammal`, proverbs tagged `clothing`/`animal-insect`, idioms tagged `time-general`/`leisure`. **61 entries fixed in that single run.** The run noted that proverbs/yojijukugo should carry `proverb`/`idiom` (cf. the 04768/04773/0552x yojijukugo→`furniture` cases above) and recommended a dedicated **semantic-tag-vs-headword sanity detector** (proverbs/yojijukugo → `proverb`/`idiom`; concrete-noun headword vs concrete-domain tag mismatch) to clear the rest faster — see Tooling Backlog item 6. This is the same batch-creation signature as the rest of P11; the 5700–6340 block is the highest-density pocket measured to date and is a strong candidate for a scoped accuracy-review `tags` sweep ahead of the sequential polish frontier.

**Update 2026-06-17 (semantic-tag-vs-headword detector shipped + first batch):** The recommended sanity detector now exists. `build/check_tag_drift.py` gained two high-precision checks (read-only, JSON queue, `--check`/`--range`/`--summary`/`--cohort`), carved out of the noisy `semantic-mismatch` heuristic:
- **`proverb-idiom-mismatch`** — a proverb/yojijukugo/set-expression headword tagged with a physical-object/creature domain (furniture, clothing, electronics, food, animal-*) with no keyword support — the 一期一会/四苦八苦/起死回生 → furniture family. Identification is `yojijukugo (4 kanji) OR POS expression OR a gloss-level idiom marker`; the flagged domain set deliberately excludes tool/geography/weather/building/transportation/body-part (those legitimately apply to compositional 4-kanji compounds like 懐中電灯/都道府県/直射日光), and the keyword-absence filter spares correct cases like 三色団子→food. **Measured ~93% precision** (13–14/14) on the first batch.
- **`concrete-noun-domain-mismatch`** — a non-verb headword carrying ≥2 mutually-distant "hard" physical-object domains (横断歩道 → animal-mammal+clothing+transportation; 油絵 → body-part+tool). This is a *structural* signal (it counts incompatible domain clusters, ignoring the necessarily-incomplete keyword lists), so it sidesteps the `semantic-mismatch` noise floor — the broad keyword cross-domain variant was measured at ~5% precision (516 flags, mostly correct bench→furniture/school→building) and was NOT shipped. **Measured ~77% clear precision** (20/26); the residual ~6 are loanword/accessory polysemy (マウス animal+device) that are correct on review.

The two checks are registered in `backlog-queue.json` (`tag-concrete-noun-domain-mismatch`, `tag-proverb-idiom-mismatch`) and drained by the reusable prompt **`prompts/fix_semantic_tag_drift.md`** (deterministic checks first, then the accuracy-review `tags` pass for the in-list-but-wrong-category cases that are NOT mechanically detectable — e.g. 朱肉→animal-mammal as a *sole* tag, which keyword/structural checks cannot catch). The single-sole-wrong-tag family remains accuracy-review territory. First worked batch (2026-06-17) hand-verified and fixed **35 entries**: all 14 proverb-idiom flags, 18 concrete-noun flags, and 3 not-mechanically-detectable stragglers found by hand-walking the 5700–6340 block (臓器→body-internal, ぼうぼう→descriptive, ほっこり drop food). The 5700–6340 block itself was already clean of detector flags (the 2026-06-16 accuracy-review swept it), confirming the detector's residual value is *above* the sequential polish frontier (6375–7431) and as a standing guard on new entries. Cursor: `polishing/tasks/semantic-tag-drift/progress.txt`.

**Update 2026-06-18 (the P11 residue extends to ~6840, quantified at two more ranges)**: Two 2026-06-17 accuracy-review `tags` sweeps measured the *single-sole-wrong-category* density above the documented 5700–6340 block — the in-list-but-wrong-domain failure the deterministic detectors cannot see, so each is an accuracy-review apply:
- **6341–6540**: ~50 entries carried a flatly-wrong single semantic tag (取捨選択→body-part, どうせ→furniture, 乱視→furniture, 家畜→work, 憤慨→geography, アンチ→electronics, 健気→clothing). **50 fixes applied in one run** — category errors, not narrowness.
- **6541–6840**: **104 of 300** entries had clearly-wrong category tags (animal-mammal on ダッシュボード/打者, building+transportation on soccer-position loanwords, electronics/furniture/food on abstract nouns and adjectives). The reviewer's `tags` dimension caught these cleanly at error severity.
Both ranges sit *above* the comprehensive-polish frontier (`next: 06163`) and carry the same batch-creation signature as the rest of P11. A scoped accuracy-review `tags` sweep of **6157–~7500** ahead of the sequential frontier would keep yielding ~17–35% apply rates (these two runs drove the runs-61–77 `tags` apply rate to 51.2% — see [Quality Metrics Trend](../topics/quality-metrics.md)). This is the strongest remaining argument for running the band's `tags` sweep proactively rather than waiting for sequential polishing.

**Update 2026-06-18 (second — the residue extends to 6925)**: A 2026-06-18 accuracy-review `tags` sweep over **6840–6925** confirmed the contamination zone leaks past the 6840 boundary measured the day before: concrete-topic semantic tags (transportation / electronics / furniture / clothing / body-part / time-general) on unrelated words, **30 fixes applied in this range**. The same run also caught the formality half of the artifact — casual particles, fillers, and idioms (ぞ, なんて, やっぱ, よね, かしら, っていう, えーと) systematically mis-tagged `formality: formal` (see P17 update below). The proactive-sweep recommendation now extends to at least **6157–6925** as a confirmed dense band; the upper bound is still open.

**Update 2026-07-01 (the wrong-category drift reaches function words — a physical-object tag on an adverb)**: A 2026-07-01 routine polish run found **06355 どうせ** (an adverb) carrying the semantic tag `furniture` — nonsensical for a function word — *and* `formality: formal` directly contradicting its own notes ("Informal … inappropriate in polite or formal speech"). This is the same copy/template-error signature as the 起死回生→`furniture` / 一期一会→`furniture` yojijukugo cases, but on an **adverb**, which is a cleaner mechanical signal than the noun cases the shipped detectors target: a *physical-object/creature semantic tag on an adverb or particle POS* is almost never correct (function words have no concrete domain), and unlike the `concrete-noun-domain-mismatch` check it does not need ≥2 conflicting domains — a single such tag on a non-content POS is enough. The observing run recommends a **targeted scan of adverbs/particles for physical-object semantic tags** (see [Tooling item 6](tooling-backlog.md) update 2026-07-01 for the detector signal). The formality half is the P17 over-`formal` family (tag contradicts the entry's own REGISTER note). Both were fixed on 06355 in that run; the scan would surface siblings elsewhere in the closed adverb/particle set.

**Update 2026-07-02 (in-list-but-wrong-category drift on abstract/loanword nouns at 11573–11646)**: A 2026-07-01 accuracy-review over **11573–11646** found **5 of 14** `tags` flags genuine (≈36% precision) — a recurring **in-list-but-wrong-category** miscategorization where abstract nouns and katakana loanwords are tagged with an oddly-specific *in-list* domain rather than the fitting one: トレード and 作画 tagged `leisure`, 入浴 tagged `consumption`. This is the classic P11 signature (a valid `VALID_SEMANTIC` tag applied to the wrong domain, so **invisible to the P20 unknown-semantic detector** and to `concrete-noun-domain-mismatch` — the tag is neither off-vocab nor concrete-vs-concrete-conflicting), now confirmed still present up in the 11500s general-tier cohort, not just the 5700–6925 block. The observing run recommends a **targeted accuracy-review `tags` sweep of katakana/suru-noun entries** as the highest-yield slice for this failure mode. The furigana-screener flags in the same range were all false positives from the model truncating its own reading readout (the documented pair-extraction FP family — Tooling item 24). No mechanical detector catches this; it stays the accuracy-review `tags` dimension's job (cf. the 6157–7500 proactive-sweep argument above).

**Update 2026-07-14 (the drift reaches the ～ハラ / harassment noun cluster — an inconsistent, mixed off-vocab + wrong-category pocket)**: Two 2026-07-13 routine polish runs (frontier 06465–06470) surfaced a coherent new cohort — the *harassment / ～ハラ* nouns — carrying tags that are wrong in three different ways at once, so the cluster is internally inconsistent:
- **08788 マタハラ (matahara)** carries the off-vocab tag `social-issues` (not in `VALID_SEMANTIC`; nearest in-list is `society`) — a P20 migration.
- **06466 モラハラ (morahara)** was tagged `emotion` — a behavior/social-issue noun mistagged as an emotion (the cross-model §4 self-check caught it) — a classic P11 wrong-category error.
- The sibling terms **05904 パワハラ (pawahara)** and **05905 セクハラ (sekuhara)** both carry only the placeholder `general`.
So four members of one tight semantic cluster carry four different (mostly wrong) tag treatments. The efficient fix is a **targeted accuracy-review `tags`-dimension pass over the harassment/～ハラ cluster** (and, more broadly, the abuse/workplace-conduct nouns), settling on one consistent in-list tag — `society` is the natural home for the abstract social-problem sense. The `social-issues`→`society` slice is deterministic (P20 migration); the `emotion`→`society` and sole-`general`→`society` slices need the reviewer's per-entry judgment.

**Update 2026-07-30 (wrong-category sole tags are dense at the *frontier*, not only in the 5700–6340 block this priority was named for)**: The 2026-07-30 polish run found three of four frontier entries carrying a sole tag from an adjacent-sounding but wrong category:

| Entry | Was | Applied | Shape of the error |
|---|---|---|---|
| 06694 電子マネー | `electronics` | `money` + `technology` | tagged for the *material* of the thing, not what it is |
| 06695 小川 | `general` | `geography` + `nature` | placeholder (P13 overlap) |
| 06696 トレンド | `time-general` | `change` + `society` + `media` | a fashion/trending word filed under time |

`time-general` for トレンド is the same failure shape as the 朱肉→`animal-mammal` case that named this priority: **a tag picked from a category that sounds adjacent to some word in the gloss**, rather than from the word's domain. Finding it three times in four entries at 06694 means this priority's range estimate should extend well above the 5700–6340 block it was originally scoped to — the frontier band carries it too, at a rate high enough that a run touching four entries expects three hits.

Note the interaction with [P34](#priority-34-action-as-the-sole-semantic-tag-on-a-verb-2085-entries) and [P13](#priority-13-overuse-of-general-as-sole-semantic-tag): all three are *sole-tag* defects on the same cohorts, and only this one (wrong category) is potentially detectable without a model. A single frontier pass that re-reads `semantic` on every entry it opens clears all three cheaper than three sweeps.

## Priority 12: Dual-reading furigana with slash separators — RESOLVED 2026-06-16

**RESOLVED (2026-06-16).** A systemic-fix Routine run fixed all **118 entries** (131 slash-reading wrappers) flagged by `build/check_furigana_format.py` (`subpattern == 'slash-reading'`). Each `{漢字|よみ1/よみ2}` wrapper was replaced, per-entry, with the single reading the kanji actually takes in context: the rendaku'd compound reading where the wrapper decomposes the headword ({歩|ぽ} in 散歩, {袋|ぶくろ} in 寝袋, {顔|がお} in ドヤ顔), the inline-link target's reading where the wrapper sat inside a ⟦…⟧ link ({毎年|まいとし}→00731_maitoshi), or the primary reading for standalone/related words ({梅雨|つゆ}, {買春|ばいしゅん}). Notes that explicitly discuss the reading variation (e.g. 七 なな/しち, 分 ふん/ぷん) kept their prose explanation; the wrapper just dropped to one reading. Two malformed English-in-reading wrappers were also repaired (28654 アプリ内課金: `{課金|billing/charging}`→`{課金|かきん}`, `{内|inside}`→`{内|ない}`). The detector now returns **0** slash-reading instances. A furigana self-check screened 59 of the 118 changed IDs before the 540 s `timeout` wrapper killed `review_runner.py` (logged as a `[tooling]` observation); its 11 flags were all false positives (rendaku-in-compound, okurigana/partial readings "correct by design", and screener input-truncation artifacts), 0 applied. Tracked as `furigana-slash-reading` in `backlog-queue.json`.

**Source**: Comprehensive-polish 2026-05-18 session 010 (entries 02251–02273)

Several entries in this range used non-standard dual-reading furigana notation with slash separators, e.g., `{村|むら/そん}`, `{蛍|ほたる/けい}`. These were normalized to single readings during the polishing session.

The slash-separator pattern is not documented in the `{kanji|reading}` convention and is likely ignored or misrendered by the furigana renderer (which expects a single reading string). The correct treatment is to pick the primary reading for the context and mention the alternative reading in notes.

**Detection**: `grep -rP '\{[^|}{]+\|[^}{]*\/[^}{]*\}' entries/ | head -30`

**Suggested action**: One-shot scan across all entries for the slash-in-reading pattern. Each instance needs manual review to select the correct single reading. The scope is unknown — this is the first range where the pattern has been observed.

## Priority 13: Overuse of "general" as sole semantic tag

**Source**: Comprehensive-polish 2026-05-23 sessions 003 (entries 03011–03035) and 005 (entries 03056–03077)

Many entries have `semantic: ["general"]` as their only semantic tag where a more specific tag (time, transportation, work, weather, etc.) clearly applies. This is distinct from the misapplied-specific-tag pattern in Priorities 11–12 — here the problem is under-specification rather than wrong specification. The tag "general" functions as a catch-all default that was never replaced with a meaningful label.

Session 003 noted the pattern in the 03011–03035 range. Session 005 confirmed it extends into the 03056–03077 range, finding 7 of 22 entries with "general" as the sole semantic tag. The pattern likely extends across much of the entry set, particularly entries created in early batch runs.

**Detection**: `python3 -c "import json, glob; [print(json.load(open(p))['id']) for p in sorted(glob.glob('entries/*/*.json')) if json.load(open(p)).get('metadata',{}).get('tags',{}).get('semantic') == ['general']]" | wc -l`

**Suggested action**: A targeted sweep replacing `["general"]` with more specific semantic tags. This overlaps with the tag-drift detector proposal in [Tooling Backlog](tooling-backlog.md) → item 6 — a semantic-tag/gloss keyword matcher could prioritize entries where "general" is the sole tag and suggest a replacement based on the English gloss. Unlike Priorities 10–12 (wrong specific tags), this is a classification gap rather than an active error, so it is lower urgency.

**Update 2026-06-18 (curator policy question — `general` → *clearly-correct* specific)**: Two 2026-06-17 accuracy-review sweeps (6341–6540 and 6541–6840) surfaced ~51 + ~28 "general → more-specific in-list tag" suggestions where the specific tag is **unambiguous and obviously correct** (害虫/蜜蜂→animal-insect, 踝→body-part, 経理→business, chisel→tool, stag beetle→animal-insect, cosmos→plant-flower, USB drive→electronics, carbon→science). The standing semantic-tag policy (2026-06-11, §A) rejects all in-list narrowness substitutions to suppress the `general`-too-broad reviewer noise (Tooling item 17), so **all were rejected** — but the observing runs flagged that many of these are *lazy-default* `general` on single-domain nouns, not a deliberate fallback, and the policy currently can't distinguish the two. **This is a curator decision, not a Routine one**: should `general` → a *clearly-correct single-domain* specific tag be an APPLY case (distinct from the leisure-vs-daily-life churn the policy rightly rejects)? If yes, it would need a tightened reviewer instruction (apply only when exactly one specific domain is unambiguous) to avoid reopening the noise floor. Logged here for the curator; no Routine action until policy is set. Related: P11 (wrong-category, already APPLY) vs. this (under-specification, currently REJECT).

**Update 2026-06-28 (the under-specification is itself a create-era batch signature)**: A 2026-06-27 routine polish §4 self-check on the **06298–06303** medical/finance cohort caught a *systematic* under-specified-tag pattern in one creation batch: medical-symptom nouns (筋肉痛/動悸/息切れ/痙攣) tagged semantic `general` where `health` clearly fits (and matches the sibling 06298, which already carries `health`), plus 収益 tagged `work` where `finance` fits. **4 of 5 tag flags were applied** — these were treated as APPLY rather than the usual narrowness-REJECT because each is the *clearly-correct single-domain* case the 2026-06-18 curator-policy question carves out (exactly one specific domain unambiguous, and confirmed by a same-batch sibling already carrying the specific tag). This is a concrete data point for that open policy question — the lazy-default `general` here is not a deliberate fallback but a create-era batch artifact, and a `check_tag_drift`-style sweep keyed on "single-domain noun with sole `general` whose gloss/sibling implies one specific tag" would surface the rest of this 06298–06303 batch (and likely its neighbors) deterministically. The 収益→`finance` slice is wrong-category (P11), not under-specification.

**Update 2026-06-28 (the placeholder-`general` signature continues at the 06309–06340 frontier)**: A 2026-06-28 routine polish §4 self-check flagged `general`→`nature`/`tool` "too broad" on four concrete-noun frontier entries (06310/06311/06312 astronomy, 06315 stepladder); per the standing semantic-tag policy these are in-list→in-list narrowness nits and were **rejected**. But the observing run noted the underlying signature: the **06309–06340 frontier block carries `general`/`science` placeholder semantic tags on specific concrete nouns** — the same lazy-default create-era artifact as the 06298–06303 medical/finance batch above, just one band further on. As with that batch, a **curator-led bulk migration keyed on "single-domain concrete noun with sole `general`/`science`"** (not per-entry accuracy-review, which rejects these as narrowness nits) is the efficient fix; the per-run §4 lane cannot apply them under the current policy. Another data point for the open 2026-06-18 curator-policy question.

**Update 2026-06-29 (the placeholder-`general` signature continues into the 06323–06340 playground/gardening/car-parts cluster)**: A 2026-06-29 routine polish §4 self-check flagged `general` "too broad" on the **06323–06340** frontier cluster (playground equipment, gardening actions, car parts) — concrete single-domain nouns carrying a sole `general` semantic tag where one specific domain is unambiguous (playground equipment → `leisure`, gardening actions → `plant-general`). The cross-model reviewer flagged **06324–06328** specifically; per the standing semantic-tag policy these in-list→in-list narrowness substitutions were **rejected** in the run. But the cluster is the same create-era lazy-default signature as the 06298–06303 medical/finance and 06309–06340 astronomy batches above — one more contiguous band of the same artifact. The efficient fix remains a **curator-led bulk migration** (or a deliberate systemic-fix P13 pass with proper per-entry tag verification), not per-entry accuracy-review, which rejects these as narrowness nits under the current policy. Yet another data point for the open 2026-06-18 curator-policy question, now with a third concrete cohort (06298–06340) in evidence.

**Update 2026-07-08 (the signature now applied *at the frontier* as clearly-correct single-domain)**: two 2026-07-06/07 routine polish runs found the placeholder sole-`general` tag on concrete-noun frontier entries and, unlike the earlier §4-lane narrowness-rejects, **applied the retag directly during frontier polishing** where exactly one specific domain is unambiguous — 06420 (technology) and 06430 害虫 → `animal-insect`. Both observing runs recommend a `check_tag_drift` sweep over **06427–06600** to surface the rest of the sole-`general`-on-concrete-noun placeholders in the ~06400+ early-2026 batch ahead of the sequential crawl (which retags only one or two per run). This is the same lazy-default create-era artifact as the 06298–06340 cohorts above, now reaching the loanword/technical-noun 06400s; the frontier lane can APPLY the unambiguous ones itself (they are the entry's *own* tag, not a cross-model narrowness suggestion), so the open curator-policy question bears only on the accuracy-review lane's REJECT behaviour, not on frontier polishing.

**Update 2026-07-10 (the frontier-applied high-precision family persists past 06430)**: A 2026-07-10 routine polish §4 self-check applied two more clear-cut sole-`general`→specific retags at the frontier — **06438 手の甲 → `body-part`** and **06439 経理 → `business`** — concrete single-domain nouns where exactly one in-list tag fits. The observing run drew the standing distinction sharply: these frontier applies are the **high-precision family** (the entry's own sole `general` on a concrete noun with an unambiguous domain), *not* the too-broad in-list-narrowness noise family the accuracy-review lane keeps rejecting ([Tooling item 17](tooling-backlog.md)). The sole-`general`-on-concrete-noun placeholder is now confirmed continuous past 06430, reinforcing the recommended `check_tag_drift` sweep over 06427–06600 to clear the batch ahead of the one-or-two-per-run frontier crawl.

**Update 2026-07-14 (the placeholder-`general` signature — and occasional plain-wrong tags — reaches the 06475–06479 early-2026 tech/loanword cohort)**: A 2026-07-14 routine polish run (frontier 06475–06479: ユーチューバー / 画面共有 / プッシュ通知 / 入会金 / 添加物) found the same create-era signature one band further on — concrete single-domain general-tier nouns carrying the placeholder sole-`general` where a precise in-list tag fits (occupation / electronics / food / money), **plus an occasional flatly-wrong tag** (06475-era 入会金 "enrollment fee" tagged `education` where `money` fits). The new datum is that the cross-model `tags` review flags these **reliably at `error` severity** on this cohort (not the in-list-narrowness nit territory the accuracy-review lane rejects), so — consistent with the 2026-07-06/08 "apply at the frontier" updates — a **tags-dimension accuracy sweep over the ~06400–07000 early-2026 tech/loanword band would clean up many at once**, pairing naturally with the P21 inline-link sweep over the same range. A `formal` formality tag contradicting the entry's own "REGISTER: Neutral" note also recurred here (06475) — see [P17](#priority-17-formal-formality-tag-over-applied-in-early-entries) update 2026-07-14.

**Update 2026-07-18 (the frontier-applied high-precision family reaches the 06527–06532 swimming/tide/appetite cohort)**: A 2026-07-18 routine polish frontier run (session 006) applied four more clear-cut sole-`general`→specific retags where exactly one in-list tag fits — **06527 背泳ぎ → `sports`**, **06530 満潮 / 06531 干潮 → `nature`**, **06532 空腹 → `health`** (the swimming/tide/appetite cohort of the 06500 Jan-2026 creation block). Same high-precision frontier-apply family as 06420/06430/06438/06439 above (the entry's own placeholder sole-`general` on a concrete single-domain word, applied in-run — *not* the accuracy-review lane's rejected in-list-narrowness noise, [Tooling item 17](tooling-backlog.md)). Confirms the sole-`general` create-era placeholder is continuous into the 06500 block, reinforcing the recommended `check_tag_drift` sweep over the ~06400–07000 batch ahead of the one-or-two-per-run frontier crawl. (These four also got their examples inline-linked in the same run; their notes were deferred — see the [P21](#priority-21-unlinked-自動詞他動詞-labels-and-particles-in-compound-verb-notes) 2026-07-18 second update.)

**Update 2026-07-19 (the family continues into the 06542–06545 baseball/swimming cohort — two swimming loanwords migrated at the frontier)**: A 2026-07-19 routine polish frontier run applied two more clear-cut sole-`general`→specific retags on the 06542–06545 baseball + swimming cluster — **06544 バタフライ / 06545 クロール → `sports`** (swimming strokes). Same high-precision frontier-apply family as 06527/06530/06531/06532 above, now on katakana sport loanwords; the placeholder sole-`general` was applied at creation despite an unambiguous single-domain fit. Notably these entries were among the **06542/06543/06547 batch tag-touched 2026-06-17 but never inline-linked** — a metadata-only touch that set (or left) the placeholder tag *and* left examples/notes naked, reinforcing that neither the sole-`general` placeholder nor the link gap self-heals under ordinary metadata edits. Continuous with the swimming/tide cohort into the 06540s; same `check_tag_drift` sweep over ~06400–07000 remains the higher-throughput fix than the frontier crawl. (Their examples and notes were fully inline-linked in the same run — see the [P21](#priority-21-unlinked-自動詞他動詞-labels-and-particles-in-compound-verb-notes) 2026-07-19 update.)

**Update 2026-07-23 (the family continues onto the 06585 soccer-position loanword cluster)**: A 2026-07-22 routine polish frontier run migrated **06585 ゴールキーパー** from sole-`general` to `sports` while inline-linking the soccer-position cluster (06585–06588), matching its three already-`sports`-tagged siblings 06586/06587/06588. Same high-precision frontier-apply family as the 06544/06545 swimming loanwords above (the entry's own placeholder sole-`general` on a concrete single-domain word, applied in-run where a same-batch sibling already carries the specific tag) — continuous with the 06527–06558 sport/game cohort. The ~06400–07000 `check_tag_drift` sweep remains the higher-throughput fix than the frontier crawl. (Its examples and notes were fully inline-linked in the same run — see the [P21](#priority-21-unlinked-自動詞他動詞-labels-and-particles-in-compound-verb-notes) 2026-07-23 update.)

**Update 2026-07-20 (the frontier-applied family reaches the 06546–06558 tool + traditional-games cohort)**: Two routine polish frontier runs applied more clear-cut sole-`general`→specific retags where exactly one in-list tag fits — **06546 のみ (chisel) → `tool`** (2026-07-19 run), and **06556 お手玉 / 06557 竹馬 → `leisure`** (2026-07-20 run, matching their traditional-games siblings 06554 あみだくじ / 06555 くじ引き). Same high-precision frontier-apply family as the 06527–06545 swimming/tide cohort above (the entry's own placeholder sole-`general` on a concrete single-domain word, applied in-run — *not* the accuracy-review lane's rejected in-list-narrowness noise). Confirms the sole-`general` create-era placeholder is continuous through the tool/game clusters of the 06500 block; the recommended `check_tag_drift` sweep over ~06400–07000 (now also covering leisure/game nouns) remains the higher-throughput fix than the one-or-two-per-run frontier crawl. (Paired with the [P17](#priority-17-formal-formality-tag-over-applied-in-early-entries) update 2026-07-20 `formal`-on-game-nouns finding — the two template-default artifacts co-occur on the same game/toy cohort.)

**Update 2026-07-24 (the frontier-applied family continues across the 06589–06605 tech/loanword band)**: Two 2026-07-23 routine polish frontier runs found the sole-`general`-on-specific-nouns signature unbroken through the 06589+ create-era block: 06589 スタメン (was `["leisure","occupation"]`) → `sports`, 06590 ビート → `music`, 06591 怨念 → `emotion`, all migrated in-run as clearly-correct single-domain; and the 06599–06605 tech/food cohort (06600 deep-learning → `science`, 06602 USB-memory / 06603 hard-disk → `technology`, 06604 track-and-field → `sports`, 06605 processed-food) where the §4 self-check flagged `general`→specific as "too broad" at `error` severity — **rejected per the standing §A in-list-narrowness policy, but the underlying lazy-default is real**. Same high-precision frontier-apply family as the 06544/06545/06585 loanware cohorts; continuous through the 06500–06600 block, reinforcing the ~06400–07000 `check_tag_drift` sole-`general` sweep as the higher-throughput fix than the frontier crawl.

**Update 2026-07-30 (the frontier crosses 06687–06690, and the within-block control case is the strongest evidence yet that these are template defaults)**: The 2026-07-30 polish run applied three more at the frontier — **06687 物覚え → `cognition`**, **06689 心掛け → `cognition`**, **06690 期末試験 → `education`** — and found the control case this item has been arguing from inference:

> **06691 中間試験 (mid-term exam), the adjacent and near-identical entry, was already tagged `education`.**

Two entries for the same kind of thing, created in the same batch, one tagged correctly and one left at sole-`general`. That is not a judgment the tagger made and got wrong; it is a default that was overwritten in one case and not the other. **Within-block inconsistency between near-identical neighbours is a stronger diagnostic than any single entry's tag**, and it is mechanically detectable: entries sharing a semantic neighbourhood where some carry a specific tag and others carry sole-`general`. Worth adding as a `check_tag_drift` heuristic — it would rank the sweep by confidence instead of treating all 3,790 sole-`general` entries alike.

**Update 2026-07-30 (second) — the accuracy reviewer pushes *toward* this queue, and that suggestion family must be rejected as a family.** The 2026-07-30 accuracy-review over 22501–22766 found that roughly a **quarter of the reviewer's semantic-tag suggestions were "replace this off-vocabulary tag with `general`"** — `location`, `place`, `position`, `object`, `space`, `status`, `document`. Applying them would trade a descriptive (if off-vocabulary) tag for the catch-all and inflate this priority's 3,790-entry queue, so they were rejected as one aggregated family.

The important part is *why* the reviewer keeps suggesting it: those seven strings are all spatial, positional, or metadata concepts, and **`VALID_SEMANTIC` has no slot for any of them**. The model is not being lazy — asked for an in-list destination for `position`, it correctly reports that the only honest answer in the list is `general`. So this is a **taxonomy question for the curator** (does the vocabulary want a spatial/positional tag? a document-type tag?) and not 100 per-entry questions. Until it is answered, both the reviewer and the migration map will keep routing that whole conceptual region into `general` or into `needs_curator.txt`. Standing rule meanwhile: **a `→ general` suggestion is rejected on sight**, the same way in-list narrowness nits are.

**Co-occurring defect worth reading at the same time** — 06687 物覚え carried sole-`general` **and** `formality: formal`, for an everyday spoken word. Both fields look like creation-time template values rather than judgments, and they are cheap to check together since a run already has the file open. This is the [P17](#priority-17-formal-formality-tag-over-applied-in-early-entries) family arriving on the same entries as this one; the standing recommendation is now explicitly **re-read `formality` whenever the frontier lane touches a sole-`general` entry**, rather than treating the two sweeps as independent.

## Priority 14: Notes content copied from wrong entry

**Source**: Comprehensive-polish 2026-05-25 session 021 (entries 03491–03510)

Entry 03500_nakaba ({半|なか}ば) had a note reading "泥んこ = muddy, mud play" — content that clearly belongs to a nearby entry about mud, not to なかば (midway/halfway). The correct note content should reference 〜なかば usage patterns.

This is a different failure mode from semantic tag drift: the note *text itself* was copied from or generated for the wrong entry, possibly during a batch creation that interleaved entries. Worth scanning notes for obviously mismatched content (note text containing keywords that have no semantic connection to the headword or gloss).

**Detection**: No simple grep — this requires semantic comparison between note content and entry headword/gloss. A lightweight heuristic: extract English words from notes, compare against gloss keywords, flag entries with zero overlap. False-positive-heavy but could surface the worst cases.

**Suggested action**: Low priority as a batch — comprehensive-polish catches these case by case. Worth a targeted spot-check of entries in the same batch cohort as 03500 (roughly 03400–03600).

## Priority 15: `{ている}` furigana brace artifact in ASPECT notes

**RESOLVED (2026-06-10).** Routine systemic-fix session fixed all **49** entries: `{ている}` → plain `ている` in the `ASPECT (...)` section headers (the only context the artifact appeared in — all 49 hits were in `notes`, none in examples). Following the semantic-verification-first rule, each entry was opened and confirmed individually before saving, even though the transform is mechanically safe (`ている` is pure kana, so dropping the braces drops no reading); the `modified` timestamp was bumped on each. A furigana self-check screened the 49 changed IDs and returned 5 flags, **all rejected** as partial-reading false positives / model hallucinations unrelated to the edit (e.g. `捻|ねじ`, `逃|に` for 逃がす, `果|は` in 果てる). `python3 build/check_artifacts.py --issue teiru-brace --json` now returns 0; the `grep` detector below returns 0. Tracked as `artifact-teiru-brace` in `backlog-queue.json`.

**Source**: Comprehensive-polish 2026-06-01 session 003 (entries 04574–04594)

Multiple verb entries use `{ている}` (furigana brace syntax) instead of plain `ている` or `(ている)` in their ASPECT section headers or notes. The furigana brace syntax `{X|Y}` is intended for kanji with readings, not for hiragana-only strings. The wrapped `{ている}` is a template artifact from batch entry creation.

**Scope**: 49 entries confirmed across the entry set — concentrated in the 00000–00500 and 03500–04600 ranges.

**Detection**: `grep -rl '{ている}' entries/ | wc -l`

**Suggested action**: Simple regex replacement: `{ている}` → `ている` across all entries. Pure text substitution, no semantic judgment needed. Low risk.

## Priority 16: `[Register: Neutral]` legacy artifact in notes — RESOLVED 2026-06-10

**Source**: Comprehensive-polish 2026-06-01 session 003 (entries 04574–04594)

Multiple entries have `[Register: Neutral]` or similar `[Register: ...]` strings at the end of their notes field. These are template artifacts from batch creation — the register information should be expressed via the `formality` metadata field rather than as trailing text in notes.

**Scope**: 188 entries confirmed.

**Detection**: `grep -rc '\[Register: ' entries/ | grep -v ':0$' | wc -l`

**Resolution (2026-06-10)**: All 188 entries fixed in one systemic-fix Routine run. Per-entry verification confirmed all `formality` fields already carried the equivalent register info. Schema has no "polite" value (→ "neutral" is correct); "Casual" in trailer maps to "informal" in schema. Furigana self-check on all 188 IDs found 5 flags, all rejected as pre-existing false positives. Detector now reports 0.

## Priority 17: "formal" formality tag over-applied in early entries

**Source**: Cross-model accuracy-review session 001 (entries 00001–00200), 2026-06-09

The accuracy-review pipeline flagged `formality: "formal"` applied to neutral/everyday words across the early entry range (00016–00200). Words confirmed incorrectly tagged formal include: ボーイ (00016, waiter), 近頃 (00028, recently), 近々 (00029, soon), ドレス (00037, dress), 吹雪 (00040, blizzard), 普段 (00041, usually), 行事 (00078, event), 筆記 (00101, writing), 方々 (00116, various people), 格別 (00154, exceptional), 貸家 (00195, rental house), 各自 (00157, each person). Nine entries were corrected in the accuracy-review session; more are likely in the 00100–00500 range.

The pattern: early batch entry creation defaulted to `"formal"` for any word that was not obviously colloquial — treating "not slang" as equivalent to "formal." The correct value for most of these words is `"neutral"`. This is distinct from the politeness-tag mis-bucketing documented in Priority 7 (which concerns the `politeness` field about keigo system categories, not the `formality` field about register level).

**Scope**: Likely 00001–00500+. The accuracy-review started from entry 1, so the 00001–00200 sub-range is now partially cleaned.

**Detection**:
```bash
python3 -c "
import json, glob
for p in sorted(glob.glob('entries/0000*/*.json') + glob.glob('entries/0050*/*.json')):
    d = json.load(open(p))
    tags = (d.get('metadata') or {}).get('tags', {})
    if tags.get('formality') == 'formal':
        print(d['id'], d.get('headword',''), d.get('reading',''), d.get('gloss','')[:40])
" | head -40
```

**Suggested action**: Review all `formality: "formal"` entries in the 00001–00500 range and change to `"neutral"` where the word is used in everyday/neutral contexts. Requires semantic judgment, not a mechanical sweep — "formal" is genuinely correct for a small subset (legal terms, bureaucratic vocabulary). The accuracy-review mode is well-suited to this pass, since the cross-model signal helps distinguish genuinely formal vocabulary from over-tagged neutrals.

**Update 2026-06-10**: Cross-model accuracy-review session 002 (entries 00201–00450) extended the confirmed range. More neutral words tagged `formal`: 清い, なお, 年月, 日時, 稀. The pattern now spans at least 00016–00450, consistent with "early batch creation defaulted to formal for anything not obviously colloquial." The accuracy-review mode is fixing these as it advances through the low-ID range.

**Update 2026-06-15 (the pattern is not just low-ID)**: Two 2026-06-15 polish runs found `formality: "formal"` over-applied well beyond the early-entry range:
- **Everyday compound action verbs at the frontier**: 06135 突き飛ばす, 06136 投げ捨てる carry `formal` even though their own REGISTER notes say "Neutral." This is a distinct cohort from the early-batch low-ID entries — it suggests the `formal` default also contaminated the 06xxx compound-verb creation batch. Worth a `check_tag_drift`-style sweep over -飛ばす/-捨てる/-出す compound verbs (the contradiction between a `formal` tag and a "Neutral" REGISTER note is mechanically detectable).
- **05000–05300 register pocket**: widespread formality/politeness errors (茶漬け `politeness: honorific`, 羊羹 `formality: formal`) noted but left for a dedicated register-tag pass (see P11 Update 2026-06-15). The mechanically-detectable slice (tag contradicts the entry's own REGISTER note) is the natural systemic-fix candidate; the rest needs semantic review.

**Update 2026-06-18 (the inverse error — slang/colloquial neologisms tagged `formal`)**: A 2026-06-17 accuracy-review sweep over 6341–6540 found a distinct sub-family: casual/slang neologisms systematically mis-tagged `formality: formal` despite their own glosses labeling them slang — 陰キャ, 陽キャ, リア充, コミュ障. This is the same "default landed on `formal`" artifact as the early-entry over-tagging above, but applied to vocabulary that is the *opposite* of formal, so it is more clearly wrong (gloss contradicts the tag). Like the 06135/06136 "Neutral REGISTER note vs `formal` tag" case, the mechanically-detectable slice is **gloss/notes contain a slang/casual marker while `formality == formal`** — a high-precision detector signal worth adding to a register-tag drift check. The accuracy-review `tags`/formality pass catches them when it reaches the range; they cluster in the 6157–~7000 neologism-heavy band.

**Update 2026-06-18 (second — casual particles/fillers/idioms too)**: A 2026-06-18 accuracy-review sweep over 6840–6925 extended this inverse-error family beyond neologisms to **casual sentence-final particles, fillers, and idioms** mis-tagged `formality: formal` — ぞ, なんて, やっぱ, よね, かしら, っていう, えーと. These are register-defining *casual* markers, so the `formal` tag is the maximally-wrong value; the same gloss/notes-slang-marker-vs-`formal` detector slice catches them (a sentence-final particle or filler glossed as colloquial/casual should never carry `formal`). Confirms the artifact runs the full length of the 6157–6925 contaminated band, not just its neologism pockets.

**Update 2026-06-28 (a third sub-family — verb-suru entries carrying a template-default `formal`)**: A 2026-06-27 routine polish run (frontier 06304–06308) found **06307 仲直りする** tagged `formality: formal` even though the entry's own notes explicitly say it is **NOT** for formal/diplomatic contexts and all its examples are casual — the cross-model §4 self-check (Gemini) flagged it independently. This is the verb-suru analogue of the early-entry over-tagging above: the creation template appears to have defaulted **verb-suru** entries to `formal`, contradicting everyday/casual usage and the entries' own register notes. The mechanically-detectable slice is the same family as the 06135/06136 case — **`formality == formal` while the entry's own REGISTER/notes prose describes neutral/casual use** — so a targeted formality audit of `verb-suru` entries tagged `formal` against their notes/examples would likely surface many mislabels. Folds into the accuracy-review `tags`/formality pass; no dedicated sweep needed unless the verb-suru cohort proves dense.

**Update 2026-07-14 (a fourth sub-family — everyday katakana loanwords auto-tagged `informal`/`formal` against their own neutral register)**: Two 2026-07-13 routine polish runs found the formality-default artifact on **everyday katakana loanword nouns** at the frontier, in *both* directions:
- **06474 プロフィール (purofīru)** was tagged `formality: informal` even though it is a standard neutral loanword (official/performer profiles); the cross-model §4 self-check flagged it, corrected to `neutral`.
- **06475** (early-2026 tech cohort) carried `formality: formal` contradicting its own "REGISTER: Neutral" note (see [P13](#priority-13-overuse-of-general-as-sole-semantic-tag) update 2026-07-14).
Both are the same "creation template picked a non-neutral formality on a register-neutral word" artifact as the low-ID over-`formal` and the slang-neologism sub-families, now on the katakana-noun class and running in both directions. The mechanically-detectable slice is unchanged — **the formality tag contradicts the entry's own REGISTER note** — so a **targeted formality review of the katakana-loanword-noun cluster** (both `informal`-tagged everyday loanwords and `formal`-tagged neutral ones) is the natural next slice; the ~06400+ early-2026 loanword band already flagged for the P21 link sweep and the P13 retag is the highest-density place to run it.

**Update 2026-07-15 (a fifth sub-family — everyday colloquial i-adjectives auto-tagged `formal`)**: A 2026-07-15 routine polish §4 self-check caught **06498 しつこい ("persistent, insistent, cloying")** tagged `formality: formal` and corrected it to `neutral` — an everyday colloquial adjective given the formal default. This is the i-adjective analogue of the katakana-loanword (2026-07-14) and slang-neologism (2026-06-18) sub-families: the creation template picked a non-neutral formality on a register-neutral/colloquial word. The observing run's tooling suggestion is a **high-precision deterministic detector for i-adjectives tagged `formality: formal`** — most common colloquial adjectives should be `neutral`, so an `adjective-i` POS carrying `formal` (especially with a casual/colloquial gloss) is a cheap drift signal, filed to [Tooling item 6](tooling-backlog.md#6-tag-drift-detector) alongside the register-note-contradiction slice already noted above. Mechanically-detectable slice unchanged (formality tag contradicts the entry's own register); the i-adjective+`formal` heuristic is the new, even cheaper cut.

**Update 2026-07-20 (the katakana-loanword sub-family reconfirmed at the frontier, now joined by everyday game/toy nouns)**: Two routine polish frontier runs found the `formal`-default artifact one band further into the 06500 block. The 2026-07-19 run (frontier 06546–06552) corrected **06550 ウインカー ("winker/turn signal") and 06551 ダッシュボード** from `formality: formal` to `neutral` — everyday katakana car-part loanwords, the same fourth sub-family as the 2026-07-14 プロフィール case. The 2026-07-20 run (frontier 06553–06558) extended it beyond loanwords to an **everyday native game noun**: **06555 くじ引き ("drawing lots")** carried `formality: formal`, corrected to `neutral`. Both are the same "creation template picked a non-neutral formality on a register-neutral word" artifact; the mechanically-detectable slice is unchanged (formality tag contradicts the entry's own neutral register). Consistent with the [P13](#priority-13-overuse-of-general-as-sole-semantic-tag) update 2026-07-20 sole-`general`-on-game-nouns finding, this argues a **targeted template-default sweep over the leisure/game-noun + katakana-loanword clusters** (both `formal`-tagged everyday words) would be high-precision.

**Update 2026-07-24 (a sixth sub-family — compound nouns whose own notes contrast them against a *more*-formal variant)**: A 2026-07-24 routine polish run's §4 self-check (gemini-2.5-flash) flagged `formality: formal` on three compound nouns whose OWN notes describe them as the *casual/standard* member of a formal↔casual pair — **06607 ビデオ通話** (vs the more-formal ビデオ会議), **06609 でいり 出入り** (vs しゅつにゅう 出入), **06611 おもてうら 表裏** (vs ひょうり 表裏) — all correctly corrected `formal`→`neutral` in-run. This is a mechanically-detectable slice sharper than the plain register-note contradiction: **`formality: formal` while the notes describe this reading/word as casual/standard/less-formal than a *named* variant**. A deterministic check keyed on that "less-formal-than-<variant>" note phrasing would catch the family across the compound-pair bands; recommended as a [Tooling item 6](tooling-backlog.md) detector cut alongside the existing `adjective-i`+`formal` and register-note-contradiction slices.

**Update 2026-07-26 (a sixth sub-family — casual personality adjectives auto-tagged `literary`/`formal` — recurring in the same 066xx band as P21)**: The 06645–06649 frontier run found **06646 せっかち** carrying `style: ["literary"]` and **06647 そそっかしい** carrying `formality: "formal"`. Both are plainly wrong: these are everyday casual personality adjectives, and nothing in either entry's own notes supports the label. Both corrected in-run.

The band matters — 066xx is the same creation cohort as [P21](#priority-21-unlinked-自動詞他動詞-labels-and-particles-in-compound-verb-notes)'s zero-link block and [P18](#priority-18-descriptive-semantic-tag-over-applied-as-a-catch-all)'s `descriptive` cluster. Three independent template-default defects (register tags, missing links, catch-all semantic tags) in one contiguous ID range is a strong argument that **a single batch sweep over 06600–06700 should check all three at once** rather than three separate passes over the same entries.

**Update 2026-07-27 (a seventh sub-family — 〜甲斐 nouns auto-tagged `informal`)**: The 06650–06655 frontier polish run found **06653 やり甲斐** and **06654 生き甲斐** both carrying `formality: informal`. The external §4 reviewer flagged 06654; the observing run verified the same error on 06653 and corrected both to `neutral`. These are ordinary native compound nouns of entirely neutral register — the same "creation template picked a non-neutral formality on a register-neutral word" artifact as the katakana-loanword (2026-07-14) and personality-adjective (2026-07-26) sub-families, but running in the `informal` direction and, unusually, over a **morphological** cluster rather than a semantic one. That makes the detector cut unusually cheap: `formality: informal` on any 〜甲斐 headword, and more broadly on ordinary Sino-Japanese/native nouns, which should default to `neutral`. Same 066xx cohort as the P18/P21 defects, reinforcing the single-combined-sweep recommendation of the 2026-07-26 update.

**Update 2026-07-29 (two more bands, and the sub-family that will *never* migrate mechanically)**: Two consecutive accuracy-review sweeps re-measured the density above the polish frontier:

| Band | Entries carrying ≥1 off-list tag | Rate |
|---|---|---|
| 20451–21050 | 237 / 599 | ~40% |
| 20703–21300 | 159 / 598 | ~27% |

The reviewer flags them reliably — this is the one dimension where the external model earns its cost — but `TAG_MIGRATION` in `build/check_tag_drift.py` **still has only 9 pairs**, so the applies are hand-adjudicated one entry at a time. The 20451–21050 pass left 32 flagged entries with no canonical destination; the 20703–21300 pass hand-adjudicated **70+ distinct off-vocab tags**.

**The enumerated 1:1 map.** The 2026-07-29 run recorded the unambiguous pairs it decided, which is the concrete deliverable this item has been missing. Extending `TAG_MIGRATION` with these would convert most of the remaining ~5,900 instances from per-entry adjudication into a mechanical `systemic-fix` batch:

| Off-list | → In-list | | Off-list | → In-list |
|---|---|---|---|---|
| `architecture` | `building` | | `literature` | `media` |
| `housing` | `building` | | `publishing` | `media` |
| `house` / `household` | `furniture` | | `math` | `number` |
| `medicine` / `medical` | `health` | | `commerce` | `business` |
| `psychology` | `cognition` | | `crime` | `law` |
| `grammar` | `grammatical` | | `legal` | `law` |
| `mimetic` | `onomatopoeia` | | `seasonal` | `time-season` |
| `academic` | `education` | | `martial-arts` | `sports` |
| `daily life` / `daily_life` | `daily-life` | | `astronomy` | `science` |

Two cautions before anyone runs this as a bulk transform. First, `daily life`/`daily_life`→`daily-life` is a *spelling* normalisation, not a semantic decision, and should arguably be a separate always-on lint rather than a migration entry — it can never be wrong. Second, `astronomy`→`science` and `martial-arts`→`sports` are genuine losses of specificity; they are correct under the current closed vocabulary, but if `VALID_SEMANTIC` is ever widened they are the first candidates to re-add, so record them as *deliberate* coarsenings rather than silent ones.

**And the sub-family that must stay in the semantic-verification lane: `place`.** Twelve instances in the 20703–21300 band alone, with **no single in-list destination** — it splits between `building` (storefront, ward, annex, clinic, wharf) and `geography` (alley, path). Any mechanical migration of `place` needs the headword, so it belongs with the per-entry lane no matter how large `TAG_MIGRATION` grows. This is the clean statement of the mappable/unmappable split the 2026-07-28 harvest asked for a discriminating test on: the split is not primarily about creation-batch vocabulary, it is about whether the off-list tag names a *category* (mappable) or a *superordinate* spanning several in-list categories (not mappable, ever).

**Detector count moved**: `unknown-semantic` 6,218 → **5,939** this refresh, so the two sweeps are outrunning new-entry growth in this class — the first refresh where that is clearly true.

## Priority 18: "descriptive" semantic tag over-applied as a catch-all

**Source**: Cross-model accuracy-review session 002 (entries 00201–00450), 2026-06-10

A new tag-drift mode distinct from the wrong-specific-tag (P11) and the
sole-`general` under-specification (P13) patterns: the `semantic: ["descriptive"]`
tag is being applied broadly to words it doesn't characterise — confirmed on 謙虚
(humble), 懸命 (earnest), 無限 (infinite), もしかすると (perhaps), 自ら (oneself).
The reviewer reads `descriptive` as meaning "this word can describe something,"
which is true of almost any adjective or adverb and therefore carries no
classifying information. It has become a second catch-all alongside `general`.

This is partly a *correct* destination tag — mimetic adverbs genuinely are
`descriptive` (P11 updates routinely retag じとじと/のそのそ to `descriptive`), so
the value is not itself wrong. The problem is that it is applied as a default to
abstract/grammatical words where a more specific or simply *no* domain tag fits
better. The underlying issue is that `descriptive` is under-defined: the tag
vocabulary doesn't state what semantic content it asserts. See
[Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Stale auto-labels"
for the analysis and the proposed criterion (reserve `descriptive` for mimetics
and manner/quality words; do not use it for abstract nouns, grammatical words, or
words that already have a real domain).

**Detection**: No clean grep — like P11, this needs the headword-vs-tag judgment
the accuracy-review `tags` dimension provides. A first-pass audit aid: list
entries whose only semantic tag is `descriptive` and whose POS is noun or
grammatical, which surfaces the clearest mismatches.

**Suggested action**: Lower urgency than P11/P17 — fold into the accuracy-review
`tags` pass rather than a dedicated sweep. When reviewing, replace a stray
`descriptive` on an abstract/grammatical word with the right domain tag, or drop
it in favour of `general`.

**Update 2026-07-26 (a high-precision detector slice: `adjective-na` + human-subject examples + sole `descriptive`)**: The 06639–06644 な-adjective block showed the catch-all applied to **personality** adjectives specifically — 06644 無口 carried sole `descriptive` where `personality` is the accurate in-list tag (fixed in-run); 06640 鈍感 and 06641 敏感 are borderline and were deliberately left as `descriptive`.

What makes this filable rather than anecdotal: **06643 頑固, in the same creation batch, already uses `personality`** — so the inconsistency is *within* a single batch, not between eras. That rules out a policy change over time and points at per-entry tagger variance, which a detector can catch cheaply.

**Suggested `check_tag_drift.py` sub-check**: `pos` contains `adjective-na` **and** the semantic tag list is exactly `["descriptive"]` **and** the examples take human subjects → propose `personality`. The human-subject test keeps it away from the legitimate uses (物の状態 descriptors), and the sole-tag condition keeps precision high. Emit as a review queue, not an auto-fix — 鈍感/敏感 show the boundary is genuinely fuzzy for perception adjectives.

**Update 2026-07-29 (the class splits cleanly in two, and only one half is adjudicable)**: Two runs added evidence that this priority is really two problems wearing one tag.

**(a) `formal` contradicted by the entry's own notes — adjudicable today, and being fixed.** The 2026-07-29 polish run found **06682 じわじわ** tagged `formal` while its own notes describe ⟦徐々に⟧ as "more formal" — the entry disagreeing with itself. The standing policy (`routine2.md` §A step 4) already licenses applying these, and it did. The run also proposed a sharper prior for finding more: **any entry with `onomatopoeia` in `pos` or `semantic` and `formality: formal` is almost certainly mistagged**, since mimetics are characteristically colloquial. That is a cheap, high-precision standalone scan and the best next action on this priority.

**(b) `formal` with *no* register statement at all — currently unanswerable, and re-flagged forever.** The 2026-07-29 accuracy-review found five in one 600-entry band: **21031 {主観的|しゅかんてき}な, 21146 {相当|そうとう}する, 21258 {率直|そっちょく}に, 21265 {複雑化|ふくざつか}, 21279 {高度化|こうどか}**. The reviewer flags all five; the policy rejects all five, correctly, because silence is not contradiction; and the next pass over that band will flag them again. This half cannot be resolved by adjudication at all — it needs the *entry* to gain a REGISTER note or lose the tag, which is polish work, not review work.

Filed as **Tooling item 44** (a `check_consistency.py` rule: non-neutral `formality` ∧ no REGISTER section → report). Sizing note carried there: five per 600 extrapolates to ~250 dictionary-wide, but this priority's whole thesis is that the class is concentrated in early and template-defaulted cohorts rather than uniform, so run the check before believing the extrapolation.

The distinction matters beyond bookkeeping: half (a) is a defect the project can detect, decide, and fix on its own evidence, while half (b) is a *missing* piece of evidence that no amount of reviewing will supply. Counting them together has been making the reviewer's formality dimension look noisier than it is.

## Priority 19: Noun examples that never contain their headword

**Source**: Curator review of 00472 仕様 (2026-06-10) + systematic scan

The curator-flagged case: 00472 仕様 (しよう) carried the example
こんなに{壊|こわ}れたら{直|なお}しようがない — but 直しようがない is
直し + よう(様) + がない; the string しよう only appears **across a morpheme
boundary**. The example taught the wrong word. (A second example in the same
entry showed どうしようもない, its own lexeme at 18862.) Both replaced
2026-06-10 with genuine 仕様がない／…の仕様がない examples.

A systematic scan (`build/check_example_headword.py`, read-only) of entries
whose POS is exactly `noun` and whose headword contains kanji found **143
suspect examples in 94 entries**, in two tiers:

- **reading-only** (14): the kana reading appears but the kanji form doesn't.
  Either a cross-boundary misparse (the 仕様 case) or legitimate kana
  orthography (ごちそう for ご馳走, おむすび for お結び) — per-entry judgment.
- **headword-absent** (129): neither form appears. The example may illustrate a
  related compound (東経 in the 経度 entry), a verb form of the nominal
  (仕組まれた in the 仕組み entry, 炙って in 炙り), a suffix usage (犯罪歴 in
  the 歴史 entry, 食べ方 in the 仕方 entry), or simply the wrong word
  (目玉焼き in the 卵 entry).

**Detection**: `python3 build/check_example_headword.py --summary` (or `--json`
for the systemic-fix review queue).

**Suggested action**: systemic-fix batches with per-entry verification. Replace
each bad example with a genuine example of the headword (full inline links), or
delete it when the entry has examples to spare; skip legitimate kana-orthography
cases. Queued as `example-headword-missing` in `backlog-queue.json`.

**Status 2026-06-14 (clean-entry frontier exhausted, `batch_ready` → false)**:
The 2026-06-14 routine run adjudicated all 31 then-flagged entries (53 examples)
and found only **one** genuine fix (00472-style verb-form misparse): 22875 出回り
had a verb example (出回る) replaced with the noun collocation 出回りの時期. Every
other flagged entry is now either (a) U+FFFD-corrupted, which the detector
mis-flags because the kanji headword is mojibake — these are owned by
**tooling-backlog #16** (the replacement-character repair pass), or (b) a
legitimate detector false positive: kana/katakana orthography of the headword
(ごちそう, おむすび, ヤギ, シミ, カツオ, カキ, しわ寄せ), documented compound forms
(退職届/婚姻届 in 届け), the radical sense (うかんむり in 冠), or a ～-prefix headword
(〜時) whose plain-kanji examples the matcher can't bind. So `batch_ready` is set
false: genuine cases now hiding behind mojibake will re-surface for this lane only
after tooling-backlog #16 repairs the corrupted text.

## Priority 20: Out-of-taxonomy semantic tags (post-expansion migration)

**Source**: Curator tag-policy decision 2026-06-11 (see
[Schema Tag Reliability](../topics/schema-tag-reliability.md) → "The
tag-vocabulary contradiction and its resolution")

A 2026-06-11 audit found 17,762 semantic-tag instances across 1,204 distinct
tags outside `VALID_SEMANTIC` — the root cause of the contradictory tag
adjudications in the first Routine v2 runs. The taxonomy was expanded with 30
established categories (≥100 uses each), legitimizing ~49% of those instances.
What remains to migrate (measured at expansion time): **9,036 instances across
7,292 entries**.

- **Near-duplicates with 1:1 targets** (~2,060 instances): `time`→`time-general`,
  `people`→`person`, `social`→`society`, `description`→`descriptive`,
  `medical`/`medicine`→`health`, `transport`→`transportation`,
  `animals`→`animal-general`, `economy`→`economics`. The detector suggests the
  target; still verify per entry (a word tagged `medical` may be better served
  by `body-internal`, etc.).
- **Long tail** (~7,000 instances, 1,160+ distinct tags, 889 of them used <5
  times): no automatic target — choose the best `VALID_SEMANTIC` tag per entry.

**Detection**: `python3 build/check_tag_drift.py --check unknown-semantic
--summary` (or `--json` for the systemic-fix review queue; each record carries
the offending tag and, for near-duplicates, the suggested target).

**Suggested action**: systemic-fix batches with per-entry verification,
starting with the 1:1 near-duplicates (highest confidence). The
accuracy-review mode also drains this organically — reviewer prompt v3 flags
out-of-list tags with suggested in-list replacements, and the standing
adjudication rule (routine2.md §A) is to apply them. Queued as
`unknown-semantic-tags` in `backlog-queue.json`.

**Update 2026-06-21 (the drift extends to a dense 7815–8037 block — a new
creation cohort, 73% out-of-taxonomy)**: A 2026-06-21 accuracy-review run over
**7815–8037** ran a deterministic scan against `build/validate_tags.VALID_SEMANTIC`
and found **163 of 223 entries (73%)** carrying at least one out-of-taxonomy
semantic tag — a far higher density than the 01490–06925 batch P11 documents, and
a different creation cohort (the 7000–8500 band appears to share a free-form
tagging origin, distinct from the 2026-04-14 claude-opus-4-5 batch). The run
migrated only the **43** that the cross-model accuracy reviewer flagged at `error`
severity (architecture/house→building, social/speech→communication,
economy→economics, progress / 'change of state'→change); **120 entries still carry
invalid tags.** The drift families are large and mostly **1:1-mappable**, so this
is **systemic-fix territory, not per-run accuracy-review** (the reviewer surfaces
only a fraction per pass and at high adjudication cost; the deterministic detector
is the scalable instrument):
- **Free-form domain words** (no current 1:1 entry in the migration map):
  `career`, `lifestyle`, `place`, `document`, `accommodation`, `commerce`,
  `accounting`, `employment`, `logistics`, `personnel`.
- **Underscore/space variants**: `daily_life` / `daily life` → `daily-life`;
  `Japanese_cuisine` / `Japanese cuisine` → drop (entries already carry `food`).
- **Body/health splits**: `body` → `body-part`, `sleep` → `health`,
  `injury` → `health`.

**Recommended next action**: expand `build/check_tag_drift.py`'s migration map
(Tooling item 6) to cover these families, commit it, then run a
deterministic+spot-checked systemic-fix sweep over the whole 7815–8037 block **and
the adjacent ~7000–8500 creation cohort** that appears to share the origin. This
is the highest-yield migration target measured to date and is queued under the
existing `unknown-semantic-tags` backlog item.

**Update 2026-06-21 (the cohort continues unbroken into 8038–8237 — even denser)**:
A 2026-06-21 accuracy-review run over **8038–8237** (cross-model-review cursor;
phase furigana) ran the same deterministic `VALID_SEMANTIC` scan and found **177
of 200 entries (88%)** carrying ≥1 out-of-taxonomy semantic tag — **305 instances
across 162 distinct out-of-list tags** — confirming the free-form creation cohort
extends contiguously from 7815 through at least 8237 and is *denser* here than the
7815–8037 block (88% vs 73%). New distinct families seen this block beyond those
already enumerated: `loanword`, `household`, `instrument`/`equipment` (→`tool`/`music`),
`competition`, `office`/`stationery`/`documents`/`writing`, `kitchen`/`ingredient`/
`food-preparation`, `perception`/`clarity`/`meaning`/`vision` (→`cognition`),
`gardening`/`agriculture`/`plants` (→`plant-general`), `anatomy` (→`body-internal`),
`body` (→`body-part`/`health` per sense). The run migrated only a **14-entry
hand-verified slice** of the highest-confidence near-duplicates (per-entry verified,
logged in `reviews/decisions.jsonl`) and **deferred the ~240-instance long tail to
the systemic sweep** — reconfirming this is systemic-fix territory, not per-run
accuracy-review. The recommended 7000–8500 sweep should now be scoped to **at least
7815–8237** (and likely the full 7000–8500 band).

**Update 2026-06-23 (dict-wide scale quantified; the long tail has no 1:1 target and is
now being mass-escalated)**: Two findings sharpen the scope and the remedy.
- **Dict-wide count**: as of 2026-06-22, `check_tag_drift.py --check unknown-semantic`
  reports **8,698 unknown-semantic flags** dictionary-wide. A 2026-06-22 routine polish
  observation spot-measured **8459–8632 at ~95 of 174 entries (55%)** carrying
  non-`VALID_SEMANTIC` tags (ability, medical, kitchen, baseball, psychology, train, …) —
  the free-form creation cohort continues unbroken above 8237.
- **The long tail is judgment-dependent, not mechanically mappable**: a 2026-06-23
  accuracy-review over **8633–9239** found **496 not-in-list semantic tags across 323 of
  607 entries (~180 distinct off-list names**: positive, body, medical, object, aesthetics,
  quality, psychology, concept, childcare, …). Critically, `check_tag_drift`'s
  `unknown-semantic` map returns `-> None` for nearly all of them (no 1:1 target), so they
  need **per-word judgment, not a mechanical migration**. That run applied **102
  provably-safe 1:1 migrations** (plural/synonym/strict-subdomain: emotions→emotion,
  train→transportation, medical→health, etc.) across 91 entries and **escalated 394
  judgment-dependent tags across 288 entries to the curator/systemic-fix lane** (logged in
  `reviews/decisions.jsonl`). Combined with the 2026-06-21 240-flag escalation, the
  decision ledger now carries **635 flags →curator this metrics window** — the first
  large escalation event in the project (all-time →curator was 16 before 2026-06-21).

**Recommended next action (updated)**: the per-run accuracy-review budget cannot drain an
8,698-flag dict-wide backlog one ~600-entry range at a time, and the bulk of it has no 1:1
map. This needs (a) a **dedicated systemic-fix/curator pass with an expanded *curated*
migration table** (more than the deterministic 1:1 families now in `check_tag_drift.py`),
and (b) **promoting unknown-semantic from a `validate_tags.py` warning to a CI error /
pre-commit gate** so new entries stop adding to the backlog (see
[Tooling Backlog](tooling-backlog.md) → item 27). Without (b), the systemic-fix pass drains
a backlog that new-entry creation keeps refilling.

**Update 2026-06-24 (the free-form cohort continues unbroken into 9240–9456)**: A 2026-06-23
accuracy-review over **9240–9456** ran the deterministic `VALID_SEMANTIC` scan and found
**~121 of 217 entries (56%)** carrying out-of-list semantic tags — confirming the pre-March
general-tier creation cohort runs contiguously above 9239 at the same ~55% density. The run
**migrated the 35 error-severity-flagged entries** to in-list tags (5 track-and-field events
`leisure`→`sports`; `place`/`manner`/`behavior`/`location`/`physical-state`→best in-list) and
left **~86 entries still carrying out-of-list tags** (top residual offenders: `location`×11,
`behavior`×10, `urban`×5, `state`/`manner`/`social`/`place`/`degree`×4 each). The observing
run reiterates the standing recommendation: a **dictionary-wide `check_tag_drift` sweep over
the whole pre-March general range** would clear this far faster than per-range accuracy-review,
which migrates only the error-severity flags it surfaces each pass. This is the same
`unknown-semantic-tags` backlog item; the per-run accuracy-review lane is keeping the frontier
honest but cannot drain the dict-wide 8,698-flag backlog one ~200-entry range at a time
(reinforces the [Tooling item 27](tooling-backlog.md) CI-gate sequencing).

**Update 2026-06-25 (the cohort reaches a denser daily-life/errands sub-batch at ~9657–9740)**: A 2026-06-24
routine polish run reported a distinct, even-denser pocket of the same free-form creation cohort: the
**~09689–09740 daily-life/errands batch** (delivery, dining, medical, housing, mobile themes) was created with an
ad-hoc out-of-taxonomy semantic vocabulary, and **48 of 84 entries in 9657–9740 (57%)** carried invalid tags —
`daily_life` underscore form plus `restaurant`/`delivery`/`medical`/`housing`/`payment`/`service`/`lifestyle`/
`real_estate`/`device`/`phone`. The run migrated that batch to the controlled vocabulary, but the observing run
flagged that **adjacent ID ranges from the same thematic creation batch likely carry the same drift** and
recommended a confirming `check_tag_drift.py --check unknown-semantic` sweep over **9600–9800**. This is the same
`unknown-semantic-tags` backlog item — a further data point that the pre-March general-tier cohort is themed in
contiguous blocks (each errands/daily-life sub-batch shares one ad-hoc tag vocabulary), which is exactly the shape
a dictionary-wide `check_tag_drift` migration (vs. per-range accuracy-review) is best suited to drain.

**Update 2026-06-26 (the daily-life/errands cohort continues into 9741–9814; and a *new* shopping/tech cohort at 9815–9849)**: Two more themed sub-batches of the same pre-March free-form creation cohort were measured and migrated this window:
- A 2026-06-25 accuracy-review over **9741–9814** found **14/70 entries (20%)** carrying out-of-list tags, concentrated in two themed blocks — subscriptions/services/promotions at 9741–9748 (`subscription`, `service`, `promotion`, `restaurant`, `facility`, `daily_life`-underscore) and civil-paperwork at 9809–9814 (`administrative`, `documents`, `moving`, `stationery`, `legal`, `housing`, `smartphone`); all migrated to `VALID_SEMANTIC` this run.
- A 2026-06-26 new-entries run reported a **distinct, denser shopping/tech cohort at 9815–9849** (recently-created vocabulary) with **21/35 entries (60%)** carrying off-list tags (`smartphone`, `internet`, `marketing`, `retail`, `housing`, `bathing`, `delivery`, `service`, `medicine`, `environment`, `contract`); all 21 migrated to in-list tags in that run. The observing run recommends sweeping the surrounding range **and adding a note to the new-entry skill**, since entry creation in this period kept reaching for an off-vocabulary tag set.

These reconfirm the cohort's defining shape — **contiguous, theme-named sub-batches each sharing one ad-hoc tag vocabulary** — and that per-range migration keeps the frontier honest but cannot drain the dict-wide backlog (see the enforcement note below for why fresh inflow is now gated). The recommended single systemic-fix `check_tag_drift.py --check unknown-semantic` sweep over ~9600–9850 still stands.

**Update 2026-06-26 (enforce-side shipped — the off-vocab ratchet now blocks *new* drift in CI)**: A 2026-06-25 tooling-fix session closed the inflow half of this problem (the [Tooling item 27](tooling-backlog.md) sequencing). `validate_tags.py` previously only *warned* on out-of-`VALID_SEMANTIC` tags and CI ran only `validate.py` (schema), so the cohort passed CI silently. The session re-measured the live dict-wide scope at **8,267 instances / 6,759 entries / 1,109 distinct tags** and added a **baseline ratchet** — `build/data/unknown_semantic_baseline.json` + `validate_tags.py --check-no-new-unknown`, now a CI step — that fails only when an entry introduces a *new* off-vocab tag, leaving the legacy tail to the gradual accuracy-review/systemic-fix migration. Regenerate the baseline after each migration batch with `--write-unknown-baseline`. This is the partial-and-correctly-sequenced form of Tooling item 27: a hard *error* on the whole legacy tail would block legitimate work on 6,759 existing entries, so the ratchet gates inflow now and the full error-gate flip waits on the curated-migration drain. Documented in [Schema Tag Reliability](../topics/schema-tag-reliability.md). No mass content migration was done in that session — that stays the gradual lane's job.

**Update 2026-06-28 (the free-form cohort reaches the 10400–10700 band — and the reviewer misses ~9 even where it migrates 64)**: Two 2026-06-27 accuracy-review observations push the mapped cohort far above the previously-documented ~9849 ceiling, into the **10xxx** general-tier batch:
- A **10469–10527** sub-batch (created onomatopoeia/adverbs/adjectives) carries an ad-hoc out-of-taxonomy vocabulary — `texture-quality`, `degree-extent`, `emotion-feeling`, `action-physical`, `manner-style`, `quality-evaluation`, `state-change` — with **~50 of 100 entries in 10450–10549** carrying a tag not in `VALID_SEMANTIC`. The accuracy-review migrated this range; adjacent batch blocks (10550+ and similar) very likely share the density.
- A **10550–10715** accuracy-review caught off-vocab tags well (**64 migrated**) but **missed ~9 in the same range** — `emotion-feeling` on 10587/10594/10629/10630, `social` on 10636/10661, `marriage` on 10617, `culture-tradition` on 10691, `action-physical`/`position` on 10613. This is the key new diagnostic: **the reviewer-driven mode leaves a residue even in ranges it has "reviewed,"** so the deterministic `check_tag_drift.py --check unknown-semantic` sweep is still needed to clear unflagged off-vocab drift in nominally-reviewed ranges, not just ahead of the frontier. Reinforces the standing recommendation (a dict-wide deterministic sweep + the [Tooling item 27](tooling-backlog.md) CI gate) over per-range accuracy-review, and confirms the contiguous free-form creation cohort runs at least through 10715. Same `unknown-semantic-tags` backlog item.

**Update 2026-06-28 (the cohort reaches the 10700–11000 katakana/slang/loanword block — a dense, contiguous pocket worth a single scoped sweep)**: Two 2026-06-28 accuracy-review observations push the mapped cohort up another ~300 IDs and pin down a concentrated cluster:
- A **10716–10887** accuracy-review found **45 of 67 tag flags** were off-vocab semantic tags on the 10700–10800 katakana/slang/loanword block (`housing-architecture`, `discourse-connector`, `food-sweets`, `shopping-product`, …) — entries created with a richer-but-off-list tag vocabulary; all migrated. The `general`-too-broad family (12) and formality flags (2) were the usual reviewer noise (rejected), and furigana screening was 0/9 (rendaku/okurigana/alt-reading FPs).
- A **10888–10947** range (spot-measured during a furigana phase) carried off-taxonomy tags on **25 of 60 entries** in a tight 10905–10934 pocket — a **2026-02 creation batch by claude-opus-4-6** with a pre-taxonomy vocabulary: `abstract-concept`→abstract ×9, `people-personality`→personality ×6, `food-ingredient`/`food-dish`/`food-fruit`→food, `nature-plant`→plant-general, `nature-geography`→geography, `place-description`/`people-description`/`body-action`→descriptive/action, `commerce`→business, `group`→society, `reasoning`→cognition, `time`→time-general; all migrated this window.

Together these confirm the free-form cohort runs contiguously through at least **10947**, with the 10700–11000 band a particularly dense, mostly-1:1-mappable katakana/loanword pocket. Both observing runs recommend **a single scoped `check_tag_drift.py --check unknown-semantic` sweep over 10700–11000** rather than chipping at it 25–67 entries per accuracy-review pass — the same `unknown-semantic-tags` backlog item, and another data point that per-range review keeps the frontier honest but cannot drain the dict-wide backlog (reinforces [Tooling item 27](tooling-backlog.md)).

**Update 2026-06-30 (the cohort reaches the 11300s 不-/中-/下-/両- compound band)**: A 2026-06-30 accuracy-review run pushed the mapped cohort into the **11300s**, where the off-vocab drift clusters in negative/positional kanji-prefix compounds (不-, 中-, 下-, 両-). The recurring families are mostly **1:1-mappable**: `quality`→`descriptive`, `position-direction`→`direction`, `people`→`person`, `place`→`geography`, plus one-offs (`information`→`cognition`, `emotion-feeling`→`emotion`, `rank`→`society`, `nature-water`, `time-manner`). The run migrated the genuine cluster (**24 applied / 11 rejected** — the rejects are the in-list `general`-too-broad narrowness family, Tooling item 17). The observing run reiterates the standing recommendation: fold these families into `check_tag_drift.py`'s migration map (Tooling item 6) and clear the band with a deterministic `--check unknown-semantic` sweep rather than the monthly per-range accuracy-review cadence — same `unknown-semantic-tags` backlog item, another data point that the free-form/off-vocab cohort runs contiguously well above 11000.

**Update 2026-07-01 (the cohort reaches the 11500s — a dense ~Feb-2026 claude-opus-4-6 batch)**: A 2026-07-01 accuracy-review run over **11515–11553** found **26 of ~72 entries** carrying at least one tag absent from `VALID_SEMANTIC` — a finer, more granular off-taxonomy tag set than the earlier bands, pointing to the same early batch-creation era (~Feb 2026, `ai_model: claude-opus-4-6`) already documented at 10905–10934. The offending tags were an over-specified hyphenated vocabulary: `action-physical`, `action-consumption`, `action-addition`, `action-repair`, `event`, `sensation`, `work-process`, `deception`, `crime`, `sign-indication`, `quantity-comparison`, `quantity-change`, `religion-buddhism`, `religion-philosophy`, `person-occupation`, `status-rank`, `quality-aesthetic`, `quality-positive`, `cause-reason`, `origin`, `space-room`, `economics-price`, `business-operation`, `politics-diplomacy`, `location`, `behavior`, `attitude`. All migrated 1:1 to in-list tags this run (`action-*`→`action`, `religion-*`→`religion`, `quality-*`→`descriptive`, `person-occupation`→`occupation`, `location`→`geography`, `behavior`/`attitude`→`descriptive`, etc.). The observing run recommends a **targeted systemic-fix sweep over 11500–12500** with `build/validate_tags.py --check-no-new-unknown`, since this granular hyphenated tag set is likely shared across the surrounding claude-opus-4-6 batch. Same `unknown-semantic-tags` backlog item; another data point that the free-form/off-vocab cohort runs contiguously well above 11300, and that its tag vocabulary shifts by creation batch (the 11500s batch used compound `noun-subtype` names rather than the free-form domain words seen lower down).

**Update 2026-07-08 (the cohort reaches the 12507–13199 band — a dense off-list pocket that needs an expanded migration map, not per-range review)**: Two 2026-07-06/08 accuracy-review runs pushed the mapped cohort into the **12507–13199** range and quantified how much of it needs curator judgment rather than a 1:1 map:
- A **12507–12673** run migrated **39** off-vocab tags. The 12520–12577 sub-band is a single creation batch that systematically used compound off-vocab tags — `action-construction`, `action-creation`, `action-coercion`, `thought-cognition`, `thought-intention`, `society-role`, `society-welfare`, `society-population`, `culture-traditional-arts`, `abstract-concept`, `language-writing`, `place-general`, `space-area`, `nature-landscape`, `quality-strength`, `attitude-stance` — the same `noun-subtype` compounding as the 11500s batch, migrated to in-list parents.
- A **12674–13199** run flagged **121 of 526** entries on `tags`; **65** carried genuinely off-list semantic tags (place, war, degree, quality, material, crime, information, sensation, …). **28** were auto-migrated via a provably-safe hyponym→parent map; **37** had no safe 1:1 target and were escalated to `reviews/needs_curator.txt` for per-entry judgment.

The new datum is that this band's long tail is **judgment-dependent** (37 curator escalations in one run), so per-range accuracy-review only partially drains it. Both observing runs recommend a **dedicated systemic-fix pass with an expanded migration map** — `degree`→`quantity`/`general`, `place`→`geography`/`building`, `quality`→`evaluation`, `information`→`cognition`/`communication` — over 12507–13199 and its adjacent same-signature batches, folded into `check_tag_drift.py` (Tooling item 6). Same `unknown-semantic-tags` backlog item; the cohort is now confirmed contiguous well past 13000, and the escalation count is the metric to watch (it feeds the [Quality Metrics](../topics/quality-metrics.md) escalation trend).

**Update 2026-07-09 (the 13200–13299 death/crime/martial-arts cohort — six clean 1:1 mappings to add to the migration map)**: A 2026-07-09 accuracy-review over **13200–13299** (a death/crime/martial-arts vocab cluster) migrated a recurring set of off-taxonomy tags that, unlike the 12674–13199 judgment-dependent tail, are **clean context-independent 1:1 mappings**: `death`→`existence`, `crime`→`law`, `martial-arts`→`sports`, `writing`→`language`, `sport`→`sports`, `body`→`body-part`. They recurred across ~11 entries in the range (13224/13225/13226/13236/13237/13240/13241/13243/13244/13247/13248). None are yet in `check_tag_drift.py`'s `TAG_MIGRATION`, so this is a concrete, safe expansion of the migration map ([Tooling item 6](tooling-backlog.md) update 2026-07-09) that would let `--check unknown-semantic` auto-detect and the systemic-fix mode auto-migrate them dictionary-wide — exactly the deterministic-over-per-range-review argument this priority has made since the 7000–8500 cohort. Same `unknown-semantic-tags` backlog item; the free-form/off-vocab cohort now confirmed contiguous into the 13200s.

**Update 2026-07-10 (the 13300–13549 block is uniformly ~40% off-vocab — the strongest single-batch case yet for a dedicated systemic-fix pass)**: Two 2026-07-09/10 accuracy-review runs measured the density across the whole 13300s block and found it consistent and high: a **13300–13349** run migrated **20 of 50 entries (40%)** and a **13350–13549** run migrated **46 of 200 entries (23%)** carrying off-vocabulary semantic tags, all mapped 1:1 to in-list tags this window. The recurring families are the now-familiar `noun-subtype`/`action-subtype` compound vocabulary plus a batch-specific nature/abstract set: `motion`→`movement`, `nature-water`/`nature-weather`/`nature-geology`/`nature-ocean`→`nature`, `action-general`→`action`, `house`→`building`, `nature-plant`→`plant-general`, `season`→`time-season`, `quality`→`abstract`/`descriptive`, `spatial`→`size`, `conflict`→`action`, `food-cooking`→`food`, `abstract-concept`→`abstract`, and the `*-concept`/`*-speech` families. Both observing runs independently reached the same conclusion the P20 chain has drawn since the 7000–8500 cohort — **the whole 13xxx block (and likely adjacent ranges) is a single mostly-1:1-mappable off-vocab creation batch that a dedicated `check_tag_drift.py --check unknown-semantic` systemic-fix sweep would clear far faster than incremental per-range accuracy-review**, which chips ~20–46 entries at a time at high adjudication cost. This is the same signature and recommendation as the 12507–13199 band above, now confirmed contiguous through **13549**. Same `unknown-semantic-tags` backlog item.

**Update 2026-07-14 (the cohort confirmed contiguous into the 14000s; the systemic-fix mode migrated a 14387–14899 pocket; and the ~6,235-entry dict-wide residue restated)**: A 2026-07-13 systemic-fix run (working the furigana-wrapper item but capturing tag drift in its accuracy-review self-check window) migrated **19 legacy off-vocab semantic tags** across **14387–14899** — place, conflict, relation, time, medicine, transport, household, philosophy, interpersonal, quality — all 1:1-mappable to in-list tags, confirming the free-form/off-vocab creation-batch cohort runs contiguously into the 14000s. The observing run put the dict-wide residue at **~6,235 entries still carrying baselined off-vocab tags** and reiterated the standing conclusion of this whole priority: a single `build/check_tag_drift.py --check unknown-semantic` **systemic-fix sweep with the expanded migration map would migrate them far faster than the accuracy reviewer surfacing them one range at a time** (which, per [Tooling item 17](tooling-backlog.md), also drags ~4× the adjudication cost through the in-list-narrowness noise on these ranges). Same `unknown-semantic-tags` backlog item; reinforces [Tooling item 27](tooling-backlog.md) (promote unknown-semantic to a CI error once the migration drain lands). A separate small P20 instance the same window: **08788 マタハラ** tagged `social-issues` (→`society`) — see the [P11](#priority-11-batch-creation-semantic-tag-transportation-misapplied) harassment-cluster update 2026-07-14.

**Update 2026-07-15 (the cohort reaches the 15100s; a 15100–15153 accuracy-review migrated ~30/54)**: A 2026-07-15 accuracy-review over **15100–15153** found **~30 of 54 entries** carrying off-vocabulary semantic tags — `people`, `body`, `degree`, `sensation`, `manner`, `behavior`, `place`, `state`, `substance`, `classification`, `housing`, plus a run of compound coinages (`administrative-procedure`, `achievement-success`, `social-behavior`) — and migrated them to in-list tags in-run. This range predates the closed-vocabulary tag policy, extending the contiguous off-vocab creation-batch cohort from the already-mapped 13xxx–14xxx blocks into the **15000s**; the observing run recommends a confirming `check_tag_drift.py --check unknown-semantic` systemic-fix sweep over **15000–15500** to clear the neighbours the sequential accuracy-review lane hasn't reached. Same `unknown-semantic-tags` backlog item; the deterministic-sweep-beats-per-range argument (with the ~6,235-entry dict-wide residue) is unchanged.

**Update 2026-07-18 (the cohort reaches the 15567–15766 band — ~45 genuine off-vocab migrations at a 28% flag rate)**: A 2026-07-17 accuracy-review over **15567–15766** flagged **56 of 200 entries (28%)** on `tags`, above the 20% reviewer-noise line. The breakdown is the now-standard two-regime split: **~45 genuine off-vocab semantic tags** (`object`, `legal`, `behavior`, `medical`, `housing`, `description`, …) migrated to in-list tags in-run — a real, recurring quality issue in this ~2026-03 creation band that predates closed-vocabulary enforcement — versus **~15 low-value in-list `general`-too-broad narrowness substitutions** the reviewer keeps proposing (rejected per §A; see [Tooling item 17](tooling-backlog.md)). The observing run again recommends tuning `review_accuracy.py`'s tags prompt to suppress the in-list narrowness family and focus on the off-vocab tags that are the genuine signal. This extends the contiguous off-vocab creation-batch cohort from the 15100s into the **15700s**; same `unknown-semantic-tags` backlog item, same deterministic-sweep-beats-per-range conclusion. (Furigana screening over the same band ran 19/191, 100% documented false-positive families — okurigana splits, prompt-context truncation, contextual readings like お腹→なか — deep pass skipped per the known-noise shortcut; see [Tooling item 24](tooling-backlog.md).)

**Update 2026-07-18 (second) (the cohort runs contiguous through 16166 — ~35–39% off-vocab across two back-to-back accuracy-review blocks)**: Two 2026-07-18 accuracy-review runs measured the next contiguous slice above the 15700s and found the same dense, mostly-1:1-mappable off-vocab creation-batch signature:
- A **15767–15966** run flagged **85 off-vocab semantic tags across 76 of 197 entries (~39%)** — all `claude-opus-4-6` batch creations carrying the familiar pre-taxonomy vocabulary (`quality`, `thought`, `writing`, `social`, `body`, `time`, `people`, `manner`, …) — migrated 1:1 in-run.
- A **15967–16166** run flagged **~30% of entries (60 of 199)** carrying off-vocabulary tags (`body`, `social`, `place`, `sport`, `animal`, `time`, `thought`, `manner`, `spatial`, `quality`), all 1:1-migratable to in-list tags; the 15900–16200 block "looks systematically pre-enforcement" (created ~2026-03).

Both observing runs independently reach the same conclusion the P20 chain has drawn since the 7000–8500 cohort: the whole **15000–17000 band is a single mostly-1:1-mappable off-vocab creation batch that a dedicated `build/check_tag_drift.py --check unknown-semantic` systemic-fix sweep would clear far faster than incremental per-range accuracy-review** (which chips 60–85 tags at a time at ~4× adjudication cost through the in-list-narrowness noise, [Tooling item 17](tooling-backlog.md)). Cohort now confirmed contiguous through **16166**; the dict-wide `unknown-semantic` residue stands at **7,323** (detector 2026-07-18, down from 7,505 on 2026-07-16 as this window's migrations landed). Same `unknown-semantic-tags` backlog item; reinforces [Tooling item 27](tooling-backlog.md) (promote unknown-semantic to a CI error once the curated-migration drain lands).

**Update 2026-07-20 (the cohort reaches the 16424–16623 band — a dense 92/200 off-list pocket)**: A 2026-07-20 accuracy-review over **16424–16623** found a **dense block of 92 of 200 entries (46%)** carrying off-list semantic tags from an older batch-creation cohort — `social`, `medical`, `linguistics`, `food-drink`, `sport`, `body-part` (e.g. `body-type` on 体型), and similar free-form/compound tags — and migrated them to `VALID_SEMANTIC` in-run (98 applied / 19 rejected that run, the rejects the standing in-list `general`-too-broad narrowness family). This extends the contiguous off-vocab creation-batch cohort from the already-mapped 15767–16166 block into the **16400–16600s** (with a short reviewed gap around 16167–16423). The observing run reiterates the standing conclusion of this whole priority: **adjacent ranges above the polish frontier likely carry the same drift, and a single `build/check_tag_drift.py --check unknown-semantic` systemic-fix sweep would clear it faster than per-range accuracy-review**. Same `unknown-semantic-tags` backlog item; the dict-wide `unknown-semantic` residue stands at **7,211** (detector 2026-07-20, down from 7,323 on 2026-07-18 as this window's migrations land). Reinforces [Tooling item 27](tooling-backlog.md) (promote unknown-semantic to a CI error once the curated-migration drain lands).

**Update 2026-07-21 (the cohort runs contiguous through 16900 — and 16711–16900 is the densest pocket yet, with a judgment-dependent tail that has no clean 1:1 target)**: Two 2026-07-21 accuracy-review blocks measured the slice just above the 16424–16623 pocket and found the off-vocab creation-batch signature continuing, denser than ever:
- A **16624–16710** run flagged **44 of 87 entries (~51%)** carrying off-vocabulary semantic tags (`household`, `object`, `commerce`, `literature`, `social`, `time`, `body`, `game`, …), migrated to `VALID_SEMANTIC` in-run.
- A **16711–16900** run flagged **92 of 173 entries (~53%)** — the densest off-vocab pocket the P20 chain has measured. **54 were auto-migrated in-run via safe 1:1 synonym renames** (`time`→`time-general`, `description`→`descriptive`, `transport`/`vehicle`→`transportation`, `people`→`person`, `medicine`→`health`, `animal`→`animal-general`, `psychology`/`thinking`/`logic`/`perception`→`cognition`, `position`→`direction`, `culture-traditional`→`culture`, `arts`/`craft`→`art`, `life`/`lifestyle`→`daily-life`, `crime`→`law`, `government`→`politics`, `calendar`/`holiday`→`time-general`, `season`→`time-season`, `social`→`society`, `property`→`finance`, `food-eating`→`consumption`), but **47 entries still carry judgment-dependent off-vocab tags with no clean 1:1 target** (`body`, `state`, `degree`, `gift`, `effort`, `achievement`, `ceremony`, `celebration`, `interpersonal`, `household`, `food-cooking`/`ingredient`/`drink`, `material`, `sound`, …) — these need per-entry systemic-fix adjudication, not a mechanical rename. This is the same batch-creation-cohort signature with a consistent off-vocab vocabulary; the observing run recommends a **targeted systemic-fix sweep of 16700–17250** (with the expanded migration map for the 1:1 families and per-entry judgment for the residue) to clear most of it faster than the per-range accuracy-review lane. Cohort now confirmed contiguous through **16900**; same `unknown-semantic-tags` backlog item, same deterministic-sweep-beats-per-range conclusion, reinforcing [Tooling item 27](tooling-backlog.md).

**Update 2026-07-22 (the cohort runs contiguous into 17085 — a 45/150 off-list pocket migrated in-run; detector 7,103→7,041)**: A 2026-07-22 accuracy-review over the next contiguous slice found the off-vocab creation-batch signature continuing just above the 16900 mark: **16936–17085 carried off-vocabulary semantic tags on 45 of 150 entries (~30%)** — `food-drink`×8, `body`×4, `social`×3, plus architecture / service / community / writing / commerce / mathematics and similar free-form/compound tags — all migrated to in-list `VALID_SEMANTIC` in-run. This extends the contiguous off-vocab cohort from the 16711–16900 densest-pocket band into the **17000s**, consistent with the observing run's read that "ranges just above ~16900 look like a batch-creation cohort with a pre-taxonomy tag vocabulary" — reinforcing the standing recommendation for a **targeted `check_tag_drift.py --check unknown-semantic` systemic-fix sweep of 16700–17250** (the same window the 2026-07-21 update proposed, now with a confirmed second dense block inside it). The dict-wide `unknown-semantic` residue stands at **7,041 flags across 5,718 entries** (detector 2026-07-22, down from 7,103 on 2026-07-21 as this window's migrations land). Same `unknown-semantic-tags` backlog item; reinforces [Tooling item 27](tooling-backlog.md).

**Update 2026-07-23 (the cohort runs contiguous into 17086–17202 — a dense 53/117 off-list pocket migrated in-run)**: A 2026-07-22 accuracy-review over **17086–17202** found **53 of 117 entries (~45%)** carrying semantic tags outside `VALID_SEMANTIC` and migrated all 53 to in-list tags in-run — extending the contiguous off-vocab creation-batch cohort just above the 16936–17085 block into the 17200s. The off-list families were the now-familiar free-form set: `human-relations`, `motion`, `disaster`, `environment`, `medical`/`medicine`, `industry`, `competition`, `hobby`, `literature`, `house`, `object`, `material`, `place`, `social`, `body`, `sensation`, `grammar`, `formal-writing`, `keigo`, `behavior`, `children`, `people`, `time` — nearly all cleanly 1:1-mappable (the observing run's suggested additions to `check_tag_drift.py`'s `TAG_MIGRATION` are recorded in the [Tooling item 6](tooling-backlog.md) update 2026-07-23). The run reiterated the standing conclusion of this whole priority: **adjacent ranges from the same creation batch (roughly 16000–18000) likely carry the same drift, and a single `check_tag_drift.py --check unknown-semantic` systemic-fix sweep across that band would clear it faster than the accuracy-review frontier**. Same `unknown-semantic-tags` backlog item; reinforces [Tooling item 27](tooling-backlog.md).

**Update 2026-07-24 (the cohort runs contiguous through 17203–17560 — two more dense off-list pockets migrated in-run)**: A 2026-07-23 accuracy-review continued the sweep above 17202 and found the off-vocab creation-batch signature unbroken: **17203–17301** carried a high density of off-vocab semantic tags (`time`, `thinking`, `decision`, `learning`, `body`, `people`, `relationships`, `space`, `behavior`, `news`, `vehicle`, `transport`, `cleaning`, `manufacturing`, `life-stage`, `documents`, `energy`, `infrastructure`, `writing`, `calligraphy`, `academic`, `martial-arts`, `hospitality`, `position`, `place`, `house`, `sensation`, `time-frequency`) — 30 entries migrated in one run — and **17374–17560** carried a further dense block (**56 entries / 76 invalid tags in one 250-ID range**: `medicine`, `culture-tradition`, `social-interaction`, `stationery`, `body-sensation`, `commerce`, `writing`, `place`, `degree`, …), migrated to in-list tags in the same run. This extends the contiguous off-vocab cohort from the 17086–17202 block through **17560**, reconfirming the whole ~16000–18000 band predates closed-vocabulary enforcement. The dict-wide `unknown-semantic` residue stands at **6,875 flags** (detector 2026-07-24, down from 6,983 on 2026-07-23 as this window's migrations land) with semantic-mismatch 809 alongside. Same `unknown-semantic-tags` backlog item; the observing runs again recommend a **dedicated `check_tag_drift.py --check unknown-semantic` systemic-fix sweep of the 17000–17999 band** over incremental per-range accuracy-review, reinforcing [Tooling item 27](tooling-backlog.md).

**Update 2026-07-25 (the cohort runs contiguous into the 17561–17760 band — 75 entries migrated in-run; detector 6,875→6,721)**: A 2026-07-24 accuracy-review continued the sweep above 17560 and found the off-vocab creation-batch signature unbroken into the **17561–17760** band, with the now-standard free-form pre-taxonomy vocabulary — `celestial`, `ability`, `memory`, `martial-arts`, `culture-tradition`, `location`, `place`, `land`, `property`, `equipment`, `audio`, `housing`, `rooms`, … — and **migrated 75 entries** to in-list `VALID_SEMANTIC` tags in the same run. This extends the contiguous off-vocab cohort from the 17203–17560 block through **17760**; the observing run notes the broader **17000–17700 band likely needs the same treatment** and reiterates the standing conclusion of this whole priority — a **dedicated `check_tag_drift.py --check unknown-semantic` systemic-fix `unknown-semantic` batch over the 17000–17999 band would clear it faster than incremental per-range accuracy-review**. The dict-wide `unknown-semantic` residue stands at **6,721 flags across ~10,060 entries** (detector 2026-07-25, down from 6,875 on 2026-07-24 as this window's migrations land; semantic-mismatch 813, sole-general 3,825 alongside). Same `unknown-semantic-tags` backlog item; reinforces [Tooling item 27](tooling-backlog.md).

**Update 2026-07-25 (second run of the day — the cohort continues into 18250–18300; detector 6,721→6,696)**: A 2026-07-25 accuracy-review over the 17911–18345 band reported the off-vocab cluster continuing into the **18250–18300** block (`security`, `vision`, `speech`, `group`, `tourism`, `place`, `posture`, `strategy`, `event`, `shape`, `body`, `biology`, `reading`). The observing run adds a **throughput judgment worth recording**: the `tags` dimension of `review_accuracy.py` "reliably surfaces them and the migrations are unambiguous, so this is the cheapest remaining lever on the off-vocab backlog." That is a *qualified* counterpoint to this priority's standing recommendation — the dedicated `check_tag_drift --check unknown-semantic` sweep is still the higher-throughput instrument per dollar, but where an accuracy-review is already pointed at a band, its tag flags convert to migrations at near-100% and should always be worked rather than deferred to the eventual sweep. Dict-wide `unknown-semantic` residue now **6,696** (detector 2026-07-25 second reading, down from 6,721 earlier the same day; total `tag_drift` 11,339 across 10,037 entries — sole-general 3,823, semantic-mismatch 813, concrete-noun-domain-mismatch 6, proverb-idiom-mismatch 1). Same backlog item; reinforces [Tooling item 27](tooling-backlog.md).

**Update 2026-07-26 (the cohort runs unbroken through 19200 — and the decisive measurement that the *model* is the wrong detector for this class)**: Two sweeps this cycle extend the cohort and settle a method question.

**Extent.** 18550–18660 came back dense with off-vocab tags (location, people, place, thing, object, commerce, character, thought, quality, organization, event, method, desire, judgment, assistance, environment, degree) — **37 migrated in-run from reviewer flags alone**. The next sweep, over **18653–19200**, found **51 of 548 entries (9.3%)** carrying tags absent from `VALID_SEMANTIC` (`body`, `transport`, `time`, `thought`, `interpersonal`, `event`, `commerce`, `crime`, `state`, …). The contaminated creation-batch cohort is therefore contiguous from the 15000s (2026-07-18 update) through **19200** with no clean gap.

**Method — the finding that should change how every accuracy-review run starts.** In that same 548-entry range the cross-model reviewer caught **32 of the 51**. A deterministic scan of `metadata.tags.semantic` against `VALID_SEMANTIC` found **all 51, in seconds, for free**. The model missed 37% of a defect class that is decidable by set membership.

> **Run the deterministic off-vocab scan first in every accuracy-review run, and treat the model's tag flags as corroboration rather than as the detector.**

`build/check_tag_drift.py --check unknown-semantic` already implements the scan — nothing needs building. What is missing is the **run-level habit**, which belongs in routine2.md §A step 3 (do the free scan, migrate the 1:1 cases, *then* spend model budget on the residue). This also explains part of the chronic tag-dimension noise measured in [Tooling 17](tooling-backlog.md#17-accuracy-review-prompt-suppress-general-tag-noise-false-positives): the reviewer spends its attention proposing in-list narrowness substitutions while under-detecting the one tag defect that actually matters.

**Recommended next sweep**: `unknown-semantic` over **18500–19000**, which the 2026-07-25 run flagged as clearable far faster by systemic-fix than by accumulating accuracy-review flags.

**Update 2026-07-27 (the band measures 50% of *entries* at 19701–19950 — and the ~50 safe renames each sweep re-derives belong in `TAG_MIGRATION`)**: The 2026-07-27 accuracy-review over **19701–19950** found **124 of 250 entries (49.6%)** carrying at least one tag outside `VALID_SEMANTIC` — **143 occurrences across 83 distinct off-list tags**. The cross-model `tags` dimension produced **130 of the run's 131 flags** in this band, and essentially all were applicable: "tag not in the list" is true by construction, not a judgment call. (Window `tags` apply-among-decided: 71.1% — see [quality-metrics](../topics/quality-metrics.md).)

The operational finding is that **the model is the wrong instrument for most of this work**. The large families are unambiguous 1:1 synonym renames — `time`→`time-general`, `body`→`body-part`, `thought`→`cognition`, `social`→`society`, `medical`/`medicine`→`health`, `people`→`person`, `description`→`descriptive`, `transport`→`transportation`, `grammar`→`grammatical`, `food-drink`/`food-and-drink`→`food` — of which `check_tag_drift.py`'s `TAG_MIGRATION` map covers only **nine**. At ~250 entries per accuracy-review run this band alone would take ~20 runs; a mapped deterministic sweep plus per-entry review of the ambiguous residue (~7% of occurrences) could clear it in a few. Dictionary-wide scope is unchanged in kind and large in size: `validate_tags.py --check-no-new-unknown` reports **5,109 entries / 6,325 tolerated off-vocab uses** still baselined, and `check_tag_drift.py --summary` counts **6,325 unknown-semantic** flags this refresh.

The genuinely judgment-dependent residue splits in two, and neither part is a rename: **compound tags with no in-list synonym** (`safety`, `logic`, `degree`, `object`, `deception`, `event`, `physical`, `material`, `sensation`, `craft`, `quality-*`), and **labels that are not semantic categories at all** (`figurative`, `loanword`, `yojijukugo`) which should simply be dropped. Filed as a map extension to [Tooling item 6](tooling-backlog.md#6-tag-drift-detector); promoting the mapped portion to a dedicated `systemic-fix` item is the recommended next step.

**Update 2026-07-28 (the band holds at ~44% into 19951–20450, and the *unmappable* residue is now the larger half)**: A 2026-07-28 accuracy-review over **19951–20450** found **221 of 498 entries (44%)** carrying at least one off-vocabulary semantic tag — the cohort is contiguous from 19701 through 20450 at 44–50% of entries, and the observing run calls it "the single largest quality defect in this ID band."

The new datum is the **mappable/unmappable split, which has inverted**. Of the 221 entries, only **99** had a 1:1 migration target (the official `TAG_MIGRATION` map plus orthographic variants such as `food-drink`→`food`); **129 need a taxonomy decision** and cannot be swept. Earlier bands ran the other way — the 2026-07-27 measurement at 19701–19950 put the judgment-dependent residue at ~7% of occurrences. Two readings are consistent with that, and they have different consequences:

- **The 19951+ creation batch used a genuinely different tag vocabulary** from the 19701–19950 one, in which case the residue is a one-band problem and the ~50-rename `TAG_MIGRATION` extension already filed under [Tooling item 6](tooling-backlog.md#6-tag-drift-detector) still clears most of what lies beyond it.
- **The map extension has been absorbing the easy families as it grows**, so what is left in each successive band is increasingly the hard tail. On this reading the mapped-sweep strategy has a natural stopping point, and the curator taxonomy decision (which off-vocab tags become in-list, which get dropped, which get a nearest-in-list home) becomes the binding constraint rather than tooling.

Distinguishing them is cheap and worth doing before the next sweep is sized: run `check_tag_drift.py --check unknown-semantic` over 19701–20450 and compare the *distinct off-list tag sets* of the two halves. If they overlap heavily, the second reading holds and the taxonomy decision should be escalated to the curator ahead of further migration runs.

## Priority 21: Unlinked 自動詞/他動詞 labels and particles in compound-verb notes

**Source**: 2026-06-11 comprehensive-polish session (entries 06038–06047)

Compound verb entries created in the ~2026-04-10 batch era (06038+ range) have a
systemic inline-link gap distinct from the general P1 unlinked-notes pattern.
Three sub-patterns:

1. **Unlinked transitivity labels**: `{自動詞|じどうし}` and `{他動詞|たどうし}` in
   TRANSITIVITY lines are furigana-wrapped but not enclosed in `⟦...⟧` inline-link
   wrappers. These should be `⟦{自動詞|じどうし}→自動詞：xxxxx⟧` pointing to the
   entry for 自動詞 or 他動詞.
2. **Unlinked particles**: Particles (を、が、から、に、で) in `Pattern:` bullets are
   bare rather than wrapped as `⟦を→を：xxxxx⟧`.
3. **Unlinked content words**: Content words in `COMMON PATTERNS` bullets lack both
   content-word links and particle links.

The same sub-patterns appear at lower ID ranges (confirmed: 00735_naoru, 00739_oboeru range) —
P1's inline-links polishing task will eventually reach them, but the 06038+ cohort
is beyond its current frontier and will not be addressed for months under sequential
processing.

**Broader context (2026-06-12)**: The 06048–06067 polish session found the **general** inline-link gap is even wider — the 06000 range batch was created before inline-link polishing was standard practice, so many entries in this cohort have no `⟦...⟧` markup in either examples or notes, not just the three specific sub-patterns enumerated above. The P21 sub-patterns are the most systemic-fix-amenable slice (they occur in a predictable structural location); the general inline-link absence is the broader P1 problem for this cohort and will be addressed as comprehensive-polish advances through the 06000 range.

**Scope**: Likely affects hundreds of compound verb entries in the 06000–09000 range
(the 2026-03 through 2026-04 creation cohort). The tooling-backlog item 15
(`check_artifacts.py` lint rule for unlinked 自動詞/他動詞) would establish the
exact count.

**Update 2026-06-14**: The 06121–06128 frontier polish session confirmed the
general inline-link absence reaches the 06120s — all eight cultural-vocabulary
nouns (火鉢, 掛軸, 手拭い, 硯, お中元, お歳暮, 香典, 送料) had **zero** `⟦...⟧` links in
both examples and notes. This is the noun-cohort counterpart of the compound-verb
gap above (same pre-inline-link-polishing creation batch). The same session also
surfaced a distinct **malformed-link sub-pattern** in the low-ID priority-lane
entries it polished (00391, 00717, 01312, 00908, 00478, 00964): inline-link **base
forms carry leftover furigana** — e.g. `⟦花→{花|はな}：xxxxx⟧` where the base after
the arrow should be bare kanji (`⟦花→花：xxxxx⟧`). Furigana belongs only on the
*surface* form before the arrow; a base form with `{...|...}` braces will not match
the `word_id_lookup.json` key and breaks the lookup. This is a different defect
class from the P9 furigana-wrapper anomalies (it is in the link *target* segment,
not the furigana wrapper) and would be cheap for a detector to catch: scan for
`→` followed by `{` inside a `⟦...⟧` span.

**Update 2026-06-15**: The general inline-link absence continues to track the
comprehensive-polish frontier — the 06129–06132 consumer/business suru-noun cohort
and the 06137–06149 idiom/proverb/yojijukugo cohort both had **zero** `⟦...⟧` links
in examples and notes (same pre-inline-link-polishing creation batch). A new
**base-form orthography sub-pattern** also surfaced: entries created by
**claude-opus-4-6** (e.g. 00740 oishii) use the **hiragana reading** as the inline-link
base form (`⟦魚→さかな：xxxxx⟧`) instead of the kanji headword (`⟦魚→魚：xxxxx⟧`). Unlike
the furigana-in-base-form malformation above, this one is **cosmetic only** — the
links still resolve via `word_id_lookup.json` (which keys on both readings and
headwords) — but it is inconsistent with the kanji-base convention and a detector
could normalise it (scan for a `→` followed by all-hiragana before `：` where the
surface form contains kanji).

**Update 2026-06-16**: A 2026-06-15 routine polish observation re-confirmed the
idiom-cohort gap with a concrete instance — the yojijukugo/proverb entries in the
**06143–06149** range (created Jan 2026, e.g. 06143_oninikanabou 鬼に金棒) carry
**zero** `⟦...⟧` links in either examples or notes (naked Japanese throughout). This
is the same pre-inline-link-polishing creation batch as the 06137–06149 cohort noted
above, so the whole 06140s idiom block should be backfilled together. The idiom cohort
differs from the compound-verb/noun cohorts only in that its notes carry fewer
structured TRANSITIVITY/Pattern lines, so the backfill is mostly example-sentence and
free-prose links rather than the P21 sub-pattern labels.

**Update 2026-06-17**: A 2026-06-16 routine polish session began backfilling the
06140s idiom cohort by hand — full inline-link coverage was added to **06147, 06148,
06149** (idioms/proverbs) and **06150** (コーディング) in that run. **06151 onward in
the same pre-inline-link creation batch remain pending.** This confirms the backfill
is tractable per-entry (mostly example-sentence and free-prose links, few P21
sub-pattern labels, as predicted in the 2026-06-16 update) but that sequential
hand-polishing will be slow over the whole 06140–06170+ block; the detector (Tooling
item 15) is still the prerequisite for a systemic-fix batch.

**Update 2026-06-18**: Two 2026-06-17 routine polish runs continued the hand-backfill at
the frontier and re-confirmed the gap reaches the loanword/suru-noun cohort above the
idiom block: **06154–06156** (loanword + 出社/退社 cluster) and **06157–06160** had
**zero** `⟦...⟧` links in examples *and* notes. The example links were added per-entry in
those runs, but the dense glossary-style notes (COMPONENTS / CONTRAST WITH RELATED TERMS /
COMMON COLLOCATIONS sections + loanword synonym lists) of the 06157+ batch remain
unlinked — and partly `noentry` (loanword synonyms). Notable: **06156 was modified
2026-06-16 yet still had no links**, so a prior touch advanced the entry without adding
inline links — i.e. the gap is not self-healing through ordinary polishing. The whole
06150–06170+ band is the same pre-inline-link 2026-01-17 creation batch; a dedicated
inline-link sweep focused on the *notes* glossaries (the heavy, partly-noentry part) is
the remaining work after examples are linked. Still gated on the Tooling item 15 detector
for a systemic-fix batch.

**Update 2026-06-18 (second — the 〜的 cluster, and the Jan-2026 band hypothesis)**: A
2026-06-18 routine polish run reached the **06169–06176 〜的 adjective/adverb cluster**
(実質的, 比較的, 定期的, 段階的, 総合的, 保守的) and found it created in **January 2026 with zero
inline-link coverage in examples *or* notes** — it predates the inline-link polishing step
entirely. This is the same pre-inline-link cohort as the 06150–06170 band above, now
confirmed to continue through the 06176 〜的 sub-cluster. The working hypothesis from the
observing run: as the sequential frontier climbs into the Jan-2026 creation band, **most
06000–07000 entries will need full tier-1 inline linking** (examples *and* notes), so the
inline-link gap is the dominant remaining tier-1 deficit for the whole 06xxx frontier — not
an occasional miss. Argues for either a dedicated inline-link sweep of 06150–07000 or
budgeting extra inline-link time into each frontier polish run until the band is cleared.

**Update 2026-06-19**: Two 2026-06-19 routine polish runs carried the frontier through
the next slice of the same Jan-2026 pre-inline-link band: **06177–06183** (onomatopoeia
adverbs + tech loanwords) and **06184–06189** both had **zero** inline-link coverage in
examples *and* notes — and crucially **despite some recent `modified` timestamps** in the
06177–06183 block, confirming again (cf. 06156 in the second 2026-06-18 update) that the
gap is **not self-healing through ordinary polishing**: an entry can be touched without
its links being added. Both observing runs reached the same conclusion — a large
pre-inline-link cohort sits unbroken between the sequential polish frontier (now ~06190)
and ~07000, and the per-entry hand-backfill at the frontier is doing genuine net-new work
(no duplication of prior polish) but cannot outpace the band's width. **Recommendation
restated with more force**: a dedicated inline-link sweep of the whole ~06150–07000 band
(examples *and* the heavy notes glossaries) is the right shape of work, still gated on the
Tooling item 15 detector for a verified systemic-fix batch.

**Update 2026-06-20**: Two 2026-06-20 routine polish runs carried the frontier through
the next contiguous slice and re-confirmed the band is **unbroken**: **06190–06196**
(nouns/proverbs, Jan-2026) and **06204–06209** (general nouns 車掌/序文/付録/栄養素/炭水化物/太陽光)
both had **zero** `⟦...⟧` links in examples *and* notes despite being otherwise
schema-valid and furigana-complete — the gap is purely inline-link coverage, not a
content defect. Both runs hand-linked their frontier entries (06194 was also pointed at
01385_kimochi, the surviving 気持ち sense). Crucially, the **priority/notes.txt lane ran
6/6 no-op in the same session** (basic-tier particles/adjectives already fully linked),
so the notes-quality ranking is pointing away from the real frontier deficit: the
binding tier-1 gap on the 06xxx general-tier frontier is inline-link coverage (this
P21 band), not note quality. The unbroken zero-link band is now confirmed from ~06150
(idiom cohort) through **06209** without interruption — reinforcing the dedicated
~06150–07000 inline-link-sweep recommendation (still gated on the Tooling item 15 detector).

**Update 2026-06-21**: Two 2026-06-21 routine polish runs carried the frontier
through **06210–06213** (compound verbs すりおろす/誘い込む/殴り倒す, created 2026-01-17,
last touched 2026-04-10 by claude-opus-4-5) and into the **06214+ proverb/yojijukugo
block** — both had **zero** `⟦...⟧` links in examples *or* notes, again **despite
06214+ carrying recent (2026-06-16) `modified` timestamps** (those bumps were not
comprehensive polish — the same not-self-healing signature as 06156 and the
06177–06183 block in prior updates). Both runs hand-linked their frontier entries.
The unbroken zero-link band is now confirmed continuous from ~06150 through
**06214+** without interruption. One observing run added a sharper recommendation:
the whole 06200–06250 band (compound verbs + four-character idioms/proverbs)
predates the inline-link polishing step and should be backfilled as a block; the
furigana and structure are otherwise clean, so the work is purely link coverage.

**Update 2026-06-22**: A 2026-06-21 routine polish run carried the frontier through
**~06222–06230** and re-confirmed the band is still unbroken: these entries were
created with **zero** inline links in examples *and* with **`・` (nakaguro) bullets**
in their notes lists (the older bullet convention, in place of the current
`⟦...⟧`-linked list items). The frontier lane is fixing these one block at a time as
it advances. The nakaguro-bullet detail is the same pre-inline-link-polishing creation
signature already documented across 06150–06214 — the band now runs unbroken from
~06150 through **06230**. No new diagnosis; the dedicated ~06150–07000 inline-link
sweep recommendation (still gated on the Tooling item 15 detector) stands.

**Update 2026-06-23**: Two routine polish frontier lanes (2026-06-22 over **06231–06236**
and 2026-06-23 over **06241–06246**) carried the band further: the 06231–06236 cohort
(nouns) and the 06241–06244 〜的 na-adjectives + 06245–06246 four-character idioms all
shipped with **zero** `⟦...⟧` links in examples *and* notes despite otherwise-complete
content (good notes, cross-refs, conjugation). Both runs hand-linked their frontier
entries. The unbroken zero-link band is now confirmed continuous from ~06150 through
**06246**. Same diagnosis, same recommendation: the sequential frontier lane is where the
real link backlog lives, and a one-off bulk inline-link sweep of the 06000+ general range
(still gated on the Tooling item 15 detector) would clear it far faster than per-entry
frontier polishing.

**Update 2026-06-26 (the band now reaches the 06270s mimetic/keigo cohort — and it is not just onomatopoeia)**: A 2026-06-25 routine polish run flagged that the **06271+ mimetic/onomatopoeia adverbs** were created with **no** inline links in examples *or* notes, and a 2026-06-26 frontier run over **06275–06281** confirmed the gap extends well past the onomatopoeia: that slice mixes mimetics (ほんのり / ほっこり / ちゃっかり), four-character idioms (軽挙妄動 / 温厚篤実), and **拝〜 humble-keigo nouns** (拝読 / 拝聴) — **all** with fully naked examples AND notes. This is the same contiguous pre-inline-link create-era cohort documented across 06150–06246 (created 2026-01-17–19, `ai_model: claude-opus-4-5`); the band is now confirmed effectively unbroken from ~06150 through **06281**. The 2026-06-26 run hand-linked its frontier entries (each takes ~15 lookups) and restated the now-standing recommendation with a concrete next target: a **dedicated inline-link sweep over ~06275–06600** (the block is large and the sequential frontier finds these one at a time). Same diagnosis, same gating on the Tooling item 15 detector for a verified systemic-fix batch.

**Update 2026-06-26 (second — the band reaches the casual/conjunction & cultural-noun cohort through 06300)**: Two 2026-06-26 routine polish runs carried the frontier through the next two contiguous slices and re-confirmed the band is still unbroken. (1) The **06282–06287** casual/slang & conjunction band (とはいえ, とはいうものの, てか, ワンチャン, エモ, 界隈) had **completely naked** Japanese in examples *and* notes — the third run to note this specific sub-band. (2) The **06288–06300** cohort (cultural nouns + proverbs, created in one Jan batch) was given furigana but **never inline-linked** — naked examples and notes throughout. Both runs hand-linked their frontier entries. The zero-link create-era band is now confirmed effectively unbroken from ~06150 through **06300**. Same diagnosis, same recommendation, now with the concrete next target restated by both runs: a **dedicated inline-link sweep over ~06294–06600** would clear the block far faster than the sequential frontier finding entries one at a time (still gated on the Tooling item 15 detector for a verified systemic-fix batch).

**Update 2026-06-28 (the band reaches the 06294–06308 cultural/medical/finance cohort — and these are heavy full-coverage jobs)**: Three 2026-06-27 routine polish frontier runs carried the band through **06294–06308** without interruption and added a quantitative note on the *cost* of the remaining backfill. (1) The **06294–06300** traditional-culture block (montsuki / bangasa / kouro / hatsunetsu and neighbors) had **zero** inline-link coverage in examples *and* notes, and its notes are encyclopedic glossary lists dense with rare `noentry` compounds (黒留袖, 貸衣装, 油紙, 仏前香炉, 聞香用香炉, 香道) — **15–30 lookups per entry**. (2) The **06298–06303** medical-symptom (筋肉痛/動悸/息切れ/痙攣) + finance (収益/抵当) cohort was likewise fully naked in examples *and* notes, each a **30–50-link** full-coverage job with dense rare medical/finance `noentry` compounds. (3) The **06304–06308** frontier was hand-linked the same way. The runs hand-linked their frontier entries (06294–06297, then 06298–06303, then 06304–06308). The zero-link create-era band is now confirmed effectively unbroken from ~06150 through **06308**, and the new datum is that the 06294+ cultural/technical cohorts are the **heaviest** slices yet (15–50 lookups each, much of it `noentry`), which strengthens the case that the sequential frontier lane alone cannot outpace the band: a **dedicated inline-link sweep over ~06304–06600** is the right shape of work (still gated on the Tooling item 15 detector).

**Update 2026-06-29 (the band reaches 06323–06328 — and recent `modified` dates confirm the not-self-healing signature yet again)**: A 2026-06-29 routine polish frontier run carried the band through **06323–06328** (playground/gardening/car-parts general-tier nouns) and re-confirmed it is still unbroken: all had **zero** `⟦...⟧` links in examples *and* notes. The sharper datum this run added is on the *recency* point already raised at 06156 / 06177–06183 / 06214+: several entries in this slice carry **recent `modified` timestamps yet remain fully naked** — **06327 sentei (剪定)** modified 2026-06-25, and **06331 handoru / 06332 akuseru** modified 2026-06-16 — so the late touches were tag/metadata edits, not linking, and the inline-link gap is once more shown **not to self-heal through ordinary polishing**. The run hand-linked its frontier entries. The zero-link create-era band is now confirmed effectively unbroken from ~06150 through **06328**; same diagnosis and same recommendation — a **dedicated inline-link sweep over ~06320–06600** (still gated on the Tooling item 15 detector) would clear it far faster than the sequential frontier finding entries one at a time.

**Update 2026-06-30 (the band reaches the 06338–06343 four-char-idiom/compound-verb cohort)**: A 2026-06-30 routine polish frontier run carried the band through **06338–06343** (four-character idioms and compound verbs from the 2026-01-17 creation batch) and re-confirmed it is still unbroken: all shipped with **zero** `⟦...⟧` links in examples *or* notes — naked Japanese throughout. The observing run's datum is that the low-ID priority-lane entries it also processed were already fully linked, so the link-coverage gap is **concentrated in this mid-ID creation batch**, not spread evenly: a targeted ~06338–06500 sweep would clear a large, well-defined block. The zero-link create-era band is now confirmed effectively unbroken from ~06150 through **06343**; same diagnosis, same recommendation — a dedicated ~06338–06600 inline-link sweep (still gated on the Tooling item 15 detector) would clear it far faster than the sequential frontier finding entries one at a time.

**Update 2026-07-03 (the band reaches 06376–06388 — three consecutive frontier runs, all fully naked)**: Three routine polish frontier runs (2026-07-02 session 004 over **06370–06375**, session 007 over **06376–06380**, and 2026-07-03 session 008 over **06381–06388**) carried the band through the next contiguous slice — a mix of early-2026 bulk yojijukugo, katakana loanwords, keigo/compound-verb entries, and 〜的 adjectives — all of which shipped with **zero** `⟦...⟧` links in examples *and* notes. Every entry across the three runs needed full example + collocation-note linking (hand-linked at the frontier). Both session 007 and 008 restated the same conclusion the band has produced since 2026-06-20: the 06300–06400+ range is a **contiguous un-linked frontier zone**, and a dedicated frontier link-completion sweep of ~06300–06500 would be materially higher-throughput than the incremental per-entry frontier polishing, which finds these one block at a time. The zero-link create-era band is now confirmed effectively unbroken from ~06150 through **06388**; same diagnosis, same recommendation (still gated on the Tooling item 15 detector for a verified systemic-fix batch).

**Update 2026-07-04 (the band reaches 06389–06393 — a four-character-idiom cluster, links lagging recent edits)**: A 2026-07-03 routine polish frontier run found the **06389–06393** four-character-idiom cluster (壊滅的, 抱腹絶倒, 傍若無人, 意気投合, 厚顔無恥) all furigana-complete but carrying **zero** `⟦...⟧` links, some despite recent `modified` dates (06392 was 2026-06-25). The new datum reinforces the not-self-healing signature already recorded for the band: recent modifications are touching these frontier entries **without** adding inline links, so inline-link completion is lagging behind other edits across the 06000+ range. Band now confirmed unbroken ~06150→06393; same ~06300–06500 dedicated-sweep recommendation (still gated on the Tooling item 15 detector).

**Update 2026-07-04 (second) (the band crosses into the 6400s modern-vocab/loanword cluster — 06398–06404)**: Two 2026-07-04 routine polish frontier observations carried the band past the yojijukugo cluster and into the **6400s modern-vocabulary/loanword cohort** (a January-2026 creation batch): **06398–06401** — the katakana/business-loanword block マインドセット / ワークショップ / 仮想通貨 / ブロックチェーン — and **06402–06404** — the tech block 電子決済 / QRコード / ロボット — all shipped with **zero** `⟦...⟧` links in examples *and* notes. The frontier polish run hand-linked 06402–06404 (which the comprehensive cursor advanced through, to `next: 6405`), so the frontier itself is closing the band entry-by-entry as it climbs, but the un-linked create-era cohort continues unbroken ahead of it. The new datum is that the band's character shifts here from four-character idioms to **modern loanword/tech vocabulary**, the same zero-link create-era signature in a different word class; band now confirmed effectively unbroken ~06150→06404. Same ~06300–06500+ dedicated-sweep recommendation (still gated on the Tooling item 15 detector); the loanword ranges above the frontier remain the highest-value contiguous target.

**Update 2026-07-08 (the band runs unbroken ~06150 → 06430; frontier link yield now demonstrably high)**: Frontier polish runs across 2026-07-05/06/07 carried the band through **06405–06430** — 06405–06417 (early-2026 loanword/business: ノマド/コワーキング/イノベーション/ベンチャー/ソリューション/脱炭素…), 06418–06422 (保活/泡立てる/ハッシュタグ/インフルエンサー/飼育 — social/parenting + cooking + katakana social-media vocab), ~06423–06426 (academic + construction/building nouns), and 06427–06430 (断熱/防水/灌漑/害虫 — technical noun/suru-verb) — all furigana-complete but with **zero** `⟦...⟧` links in examples *and* notes until each run hand-linked its frontier entries (comprehensive cursor now `next: 6431`). Two new data points this window: (1) several of these general-tier nouns also carried the placeholder sole-`general` semantic tag with a clean in-list fit (06420→technology, 06430 害虫→animal-insect, both retagged in-run) — see the [P13](#priority-13-overuse-of-general-as-sole-semantic-tag) 2026-07-08 update; (2) **link yield here is high** — the dense collocation/composition note blocks are rich in domain compounds that mostly DO now have entries (排水/撥水/防塵/益虫/殺虫剤…), so the ~06400+ band is not just a gap but a high-value one. Band now confirmed effectively unbroken **~06150 → 06430**; the dedicated ~06300–06600 frontier link-completion sweep (still gated on the Tooling item 15 detector) remains the highest-throughput fix, with a paired sole-`general`-retag pass on the same range (P13).

**Note on bound-morpheme linking (2026-07-07, [skill] carve-out — recorded, no wiki/skill edit)**: while linking the 06427–06430 technical entries, a frontier run confirmed that rare **bound component kanji** in COMPOSITION/kanji-breakdown lines (断/灌/漑/潅) and **variant spellings of the headword** (潅漑) have no standalone entry and are not candidate-worthy, so they were marked `noentry` **without** adding a candidate. The `inline-word-links` skill's "always pair a `noentry` link with a candidate" rule should carve out bound morphemes and kanji-citation glosses; this extends the 2026-07-03 bound-compound-verb-suffix carve-out already recorded in [compound-verbs.md](../topics/compound-verbs.md). Knowledge-base sessions do not edit skills — logged here and in the session log for the curator.

**Update 2026-07-09 (the band reaches 06433–06434 — an energy/infrastructure cluster, with paired candidate harvesting)**: A 2026-07-09 routine polish run found the **06433–06434** renewable/nuclear-energy compound nouns shipped with **zero** `⟦...⟧` links in examples *and* their dense collocation notes — the same create-era signature, now in an energy/infrastructure word class. The new datum reinforces the "high link yield" observation from the 2026-07-08 update *and* its complement: these notes list nuclear-policy vocabulary that has **no entries yet** (再稼働 restart, 廃炉 decommissioning, 揚水 pumped-storage), so the run added them as candidates **C22260–C22262**. The band is now confirmed effectively unbroken ~06150 → 06434, and energy/infrastructure clusters in the 06xxx range need **both** the inline-link sweep *and* candidate harvesting of their technical note vocabulary — the two feed each other (harvest → create → the links then resolve). Same ~06300–06600 dedicated-sweep recommendation (still gated on the Tooling item 15 detector), now understood to pair naturally with a candidate-harvest pass over the same notes.

**Update 2026-07-10 (the band reaches 06438–06440, high link yield reconfirmed, another paired candidate harvest)**: A 2026-07-10 routine polish run carried the band through **06438–06440** (手の甲 back of the hand / 経理 accounting / タイムライン timeline) — again **zero** `⟦...⟧` links in examples *and* dense collocation-heavy notes, with **very high link yield (~20–40 links/entry)** once hand-linked at the frontier, exactly the 2026-07-08/09 pattern in a body-part/business/social-media word class. The run again harvested the note vocabulary that lacks entries as candidates — ひび割れ, 足の甲, 仕訳, マネージャー, フィード, もごもご (**C22275–C22280**) — reconfirming the link-sweep↔candidate-harvest feedback loop (harvest → create → the links resolve). The band is now confirmed effectively unbroken **~06150 → 06440**; the ~06300–06600 dedicated sweep (gated on Tooling item 15) remains the highest-throughput fix and continues to pair naturally with candidate harvesting of the same notes.

**Update 2026-07-13 (the band reaches 06457–06462; the create-era signature restated precisely as "notes-only" — examples linked, notes not)**: A 2026-07-12 routine polish run (frontier 06457–06462) sharpened the characterization of this cohort's gap: the pre-inline-link-standard General-tier entries consistently carry **bare `{漢字|かな}` furigana in their notes** (collocation / pattern / related-terms lists) with **no `⟦...⟧` links**, *while their example sentences are fully linked*. So the residual backlog above the polish frontier is now specifically a **notes-field** link gap, not a whole-entry one — the examples were linked at some point but the note glossaries were not. This matters for the detector design (see the item-15 reinforcement below): the highest-signal query is "notes contain furigana `{…|…}` tokens **outside** `⟦…⟧`," which targets exactly this notes-only residue and does not re-flag the already-linked examples. Band now confirmed effectively unbroken **~06150 → 06462**; the ~06300–06600 dedicated sweep (gated on Tooling item 15) remains the highest-throughput fix.

**Update 2026-07-14 (the band runs unbroken through 06479; the 06400–06500 range confirmed a contiguous unlinked zone across four runs)**: Four routine polish runs on 2026-07-13/14 carried the frontier through **06465–06479** and every cohort shipped with **zero** `⟦...⟧` links in examples *and* notes at birth — 06465–06470 (2010s–2020s slang/loanword coinages チルい / モラハラ / ガチ勢 / KY), 06471–06474 (堆肥 / 果樹園 / アンチ / プロフィール — 2020s vocab), and 06475–06479 (ユーチューバー / 画面共有 / プッシュ通知 / 入会金 / 添加物 — early-2026 tech/loanword), all hand-linked at the frontier. Both observing runs independently conclude the **whole 06400–06500 range is a contiguous unlinked zone** created before the inline-linking polish reached it, and restate the dedicated ~06400–07000 link-coverage sweep as higher-yield than the sequential crawl (which clears ~4–5 dense-note entries per run). Band now confirmed effectively unbroken **~06150 → 06479**; still gated on the Tooling item 15 notes-furigana detector.

**Update 2026-07-15 (band reaches 06489; per-entry spottiness confirmed in the 06480s, and the notes-glossary residue is mostly a cross-ref/link opportunity not a candidate gap)**: Two routine polish runs on 2026-07-14 carried the frontier through **06480–06489**. The 06480–06486 run found the create-era gap is **spotty per-entry in this stretch, not range-wide**: 06480/06481/06482/06483/06486 (verbs + nouns) all needed full linking in examples *and* notes, yet their immediate neighbors **06484 あくび / 06485 まばたき were already fully linked** — so within the 06480s the link coverage is per-entry inconsistent rather than a clean contiguous zone (contrast the solidly-unlinked 06400–06479). The 06487–06489 run (襟 / 裾 / チャック, plus 下駄箱 / humidifier-dehumidifier neighbors in the same ~06400–06500 concrete-noun band) reconfirmed the whole-entry gap — rich notes with **zero `⟦...⟧` links in examples** and note glossaries listing many bare `{漢字|かな}` terms (袖, 裾, 丸襟) with no links or `noentry` markers. The new datum for the sweep design: **most of those note-listed compounds already have entries** (襟元, 襟足, 裾野 all exist), so the notes residue is predominantly a **cross-reference/link opportunity, not a candidate gap** — the link sweep will resolve most of them against `word_id_lookup.json` without new candidate harvesting. Band now confirmed effectively unbroken **~06150 → 06489**; still gated on the Tooling item 15 notes-furigana detector.

**Update 2026-07-15 (band reaches 06499; notes-linking tractability confirmed splits by note density)**: Two 2026-07-15 routine polish runs carried the frontier through **06490–06499**. The 06490–06494 run (加湿器 / 除湿機 / 踏切 …) found the cohort naked in **examples** at birth and added full example-link coverage, but **deferred the dense technical notes** (式-type appliance lists, single-kanji COMPOSITION breakdowns like 加/湿/器) as lower learner-value and higher `noentry` churn — a concrete datum that the notes-linking half of this band is where the cost sits. The 06495–06499 run (地下道 / 処方箋 / てんとう虫 / しつこい / 健気, created Jan 2026, with only June `modified` bumps and **zero links in examples OR notes**) found the opposite tractability and **completed notes linking too**, the `noentry` churn manageable (調剤薬局 / 院内処方 / 院外処方 / ナナホシテントウ / 涙ぐましい added as candidates). Together they refine the sweep design: **example-linking is uniformly cheap across the band; notes-linking cost varies with a cohort's note density** (deep collocation/composition glossaries defer well; ordinary notes complete in-run). Band now confirmed effectively unbroken **~06150 → 06499**; still gated on the Tooling item 15 notes-furigana detector.

**Update 2026-07-16 (the band crosses into the 06500 block; still contiguous, still a whole-entry gap)**: A 2026-07-16 routine polish run carried the frontier into the **06500 creation block** (06500 ペンギン / 06501 路地 / 06502 横断歩道 / 06503 ねじ回し / 06508 鍋敷き, created 2026-01-17) and found the same signature — **zero `⟦...⟧` links in examples *and* notes despite complete furigana**, confirming the whole Jan-2026 06500-block predates the inline-linking polish pass. Band now confirmed effectively unbroken **~06150 → 06508**; the observing run restated the standing recommendation for a **dedicated inline-link sweep of 06500–06999** (and adjacent create-era ranges) as far higher-yield than the sequential frontier reaching them one entry per run. A paired datum for the sweep's candidate side: the 06500/06501/06508 notes glossaries list **katakana species/material names with no entries** (アデリーペンギン and other penguin species, シリコン, 籐, コースター, ナチュラル) — the lexical (non-species) items were added as candidates while the species/material citations were correctly left `noentry`, consistent with the [inline-word-links `noentry` carve-out for bound morphemes / species / material citations](../ideas/tooling-backlog.md) recorded 2026-07-03/07-08 (these are not candidate gaps and should not block the link sweep).

**Update 2026-07-18 (the sequential frontier begins draining the 06500 block — first entries linked)**: A 2026-07-17 routine polish frontier run linked **06517 ガードレール / 06518 足場 / 06519 応急処置 / 06520 じゃんけん** — the first entries in the documented zero-inline-link 06500 Jan-2026 creation block to receive **full `⟦...⟧` coverage in examples AND notes** (previously flagged as naked in the 2026-07-16 update). The run harvested ~15 candidates from their `noentry` glossary terms (中央分離帯, 単管, 心肺蘇生, 救命講習, グー/チョキ/パー, 後出し, …), reconfirming the link-sweep↔candidate-harvest feedback loop. The new datum is confirmation that **the band is now being drained sequentially from the frontier cursor, not merely re-flagged each run** — but at ~4 dense-note entries/run the sequential crawl still lags far behind the ~06150→06508 backlog, so the dedicated 06500–06999 sweep (gated on the Tooling item 15 notes-furigana detector) remains the higher-throughput fix. Frontier cursor advanced past 06520.

**Update 2026-07-18 (second) (the frontier drains through 06532 — but a new precise datum: examples + tags done in-run, NOTES deliberately deferred)**: A 2026-07-18 routine polish frontier run (session 006) carried the cursor through **06527 背泳ぎ / 06530 満潮 / 06531 干潮 / 06532 空腹** and did two things: (1) added **full `⟦...⟧` coverage to their example sentences** and (2) **fixed their sole-`general` placeholder semantic tags** to the correct in-list values (背泳ぎ→`sports`, 満潮/干潮→`nature`, 空腹→`health` — see the [P13](#priority-13-overuse-of-general-as-sole-semantic-tag) frontier-applied family) — but **left the NOTES fields entirely naked**, because their note glossaries carry morphology fragments (WORD FORMATION single-kanji breakdowns) and domain jargon (swimming バタ足/腕の回転/メドレー; tides 引き潮/上げ潮/小潮/潮見表; medical 空腹時血糖値) that need **candidate triage before linking**. This sharpens the "notes-only residue" characterization from the 2026-07-13 update into a concrete two-phase workflow the frontier lane is now following: examples + tags are cheap and done at the frontier, while the dense-note linking is deferred to a dedicated notes-linking pass (or comprehensive-polish's notes lane) once the note vocabulary is harvested as candidates. `modified` was bumped this run, so the §2 30-day skip window now applies to these four — a caveat for whoever runs that notes pass (they will be skipped until ~2026-08-17 unless targeted explicitly). Band now drained sequentially through **06532**; the dedicated 06500–06999 notes-linking sweep (gated on Tooling item 15) remains the higher-throughput fix.

**Batch readiness**: `batch_ready: false` until the Tooling Backlog item 15 detector
exists. Once it exists, this becomes a systemic-fix candidate with per-entry
semantic verification (the TRANSITIVITY/Pattern/COMMON PATTERNS context must be
read to supply the correct entry ID for each link).

**Update 2026-07-19 (the frontier drains through 06545 across two runs — full one-pass linking now the standard, and a precise "June-17 tag-only touch" sub-pattern named)**: Two routine polish frontier runs carried the cursor further into the 06500 block. The 2026-07-18 (third) run (session 009) drained **06533–06536** (満腹 / 眠気 / 図々しい / 気まずい) with **full `⟦...⟧` coverage in examples AND notes in a single pass** — deliberately *contra* the session-006 "defer dense notes, examples+tags only" pacing note above. The trade-off is now confirmed: full one-pass linking runs ~4 entries/session vs ~6 examples-only, but both reach the same end state, and the 06526 precedent already established fully-linked notes as the current tier-1 standard; dense-note candidate triage was light here (6 `noentry` lexical gaps: ホルモン / 腹八分 / 元カレ / 元カノ / ぎくしゃく). The 2026-07-19 run drained **06542–06545** (打席 / 完封 / バタフライ / クロール — a baseball + swimming cluster), again with full examples+notes coverage in one pass, and migrated the two swimming loanwords' sole-`general` tags to `sports` (06544 バタフライ, 06545 クロール — the [P13](#priority-13-overuse-of-general-as-sole-semantic-tag) frontier-applied family). The new characterization datum: **06542/06543/06547 had been tag-touched 2026-06-17 but never inline-linked**, so a June-2026 metadata edit left the examples/notes naked — the same not-self-healing "recent-`modified` but unlinked" signature seen since 2026-06-29, now pinned to a specific tag-only touch batch. ~10 baseball/swimming `noentry` terms harvested (素振り/打数/継投/完全試合/ノーヒットノーラン/ドルフィンキック/ストローク/入水/バタ足). The chisel pair 06546/06547 (tool sub-type-dense notes) and 06532 (antonym of 06533, predates the notes push) remain deferred/bare, eligible when the frontier or a targeted pass reaches them. Band now drained sequentially through **06545**; the dedicated 06500–06999 notes-linking sweep (gated on Tooling item 15) remains the higher-throughput fix.

**Update 2026-07-20 (the frontier drains through 06558; the band is confirmed unbroken to the ~06559 cursor, now reaching a traditional-games / folklore-yōkai cohort)**: Two routine polish frontier runs carried the cursor further into the 06500 block. The 2026-07-19 session (frontier **06546–06552**) and the 2026-07-20 session (frontier **06553–06558**: クラッチ / あみだくじ / くじ引き / お手玉 / 竹馬 / 座敷童) both found **zero `⟦...⟧` links in examples AND notes** at birth despite otherwise-complete content — the 06546–06552 block a tool / car-part cluster, the 06553–06558 block a traditional-games + folklore-yōkai cluster — and hand-linked their frontier entries. The observing runs note the inline-linking sweep is "only now reaching ~6550" and that **contiguous unlinked ranges continue above 06558** (06559 shinkirō onward). Band now confirmed unbroken **~06150 → 06558**; the dedicated 06500–06999 notes-linking sweep (gated on Tooling item 15) remains the higher-throughput fix than the ~4-entries/run frontier crawl. (The same 06553–06558 cohort also surfaced two adjacent tag/cross-reference issues — the sole-`general`/`formal` template default on game/toy nouns, see [P13](#priority-13-overuse-of-general-as-sole-semantic-tag) update 2026-07-20 and [P17](#priority-17-formal-formality-tag-over-applied-in-early-entries) update 2026-07-20, and the missing mutual `related` cross-references across the traditional-games cluster, see [P3](#priority-3-cross-reference-symmetry-on-thematic-clusters) update 2026-07-20.)

**Update 2026-07-21 (the frontier drains through 06568; 06563–06600 confirmed uniformly zero-linked; and a genuinely-new datum — note-field furigana *reading* errors surface during the link sweep)**: Two 2026-07-20 routine polish frontier runs carried the cursor further into the 06500 block — **06559–06562** (animal/plant/science nouns) and **06563–06568** (baseball/music/construction clusters) — both **zero `⟦...⟧` in examples AND notes** at birth, hand-linked at the frontier. The later run confirmed **all 38 entries in 06563–06600 carry zero inline links**, so the band remains unbroken and uniformly naked well past the cursor. Two genuinely-new data points this window:
1. **Note-field furigana can carry outright *reading* errors, not just missing/malformed wrappers.** While linking 06563 投手's notes the run found `{中継|ちゅうけい}ぎ` for the relief-pitcher sense (correct reading なかつぎ, fixed to `{中|なか}{継|つ}ぎ`) and a malformed `{クローザー}` wrapper (katakana inside furigana braces with no reading, fixed to plain クローザー) — both corrected in-run. The [pattern] behind it: **note-field furigana was never reading-checked at creation** — `verify_furigana.py` historically scanned headword/examples, and the cross-model furigana reviewer (`review_runner.py`) reviews headword/examples too, so **no automated check validates the correctness of readings inside `notes`**. The 06500s notes (and likely other create-era ranges) may hide similar reading errors; the frontier link sweep is currently the only thing surfacing them, incidentally. A note-field furigana reading-correctness check is an **open tooling gap**, distinct from the [P9](#priority-9-malformed-furigana-wrappers) *format*-wrapper backlog and from [Tooling item 22](tooling-backlog.md)'s structured-field *completeness* sweep.
2. new-entries deliberately defers linking, so **every un-polished new-entry range is expected to be link-empty** — the sequential polish frontier is where these first get links, which is why the band stays unbroken as the cursor climbs.

Band now drained sequentially through **06568**; the dedicated 06500–06999 notes-linking sweep (gated on Tooling item 15) remains the higher-throughput fix than the ~5-entries/run frontier crawl.

**Update 2026-07-22 (the frontier drains through 06574; 06569–06600 reconfirmed uniformly zero-linked; a 2026-01-18 creation batch pinned at 06578–06582; and the note-field malformed-wrapper sub-family recurs during the link sweep)**: A 2026-07-21 routine polish frontier run carried the cursor through **06569–06574** and hand-linked them, reconfirming (as the 2026-07-21 run did for 06563–06600) that the **entire 06569–06600 block is link-empty** — a contiguous create-era band that the sequential frontier is converting at ~5 entries/run while new-entry growth outpaces it. A separate observation pinned a **2026-01-18 creation batch at 06578–06582** (finance / legal / construction nouns) shipped with **zero** `⟦...⟧` links in examples *or* notes — the same date-stamped-cohort signature seen across the band, and a datum that a **targeted sweep keyed on `created` date (the 2026-01-17–19 batches) could close the gap faster** than the ID-sequential frontier crawl. The link-empty band is now confirmed unbroken **~06150 → ~06600**.

**Update 2026-07-23 (the frontier drains through 06588; the soccer-position loanword cluster and the 06583–06592 general-tier band reconfirmed uniformly zero-linked)**: Two 2026-07-22 routine polish frontier runs carried the cursor further into the band. One reported the general-tier nouns **06583 炭素 / 06584 ファウル / 06589 スタメン / 06590 ビート / 06591 怨念 / 06592 開墾** (created Jan 2026) shipped with **zero** `⟦...⟧` links in examples and only partial linking in notes; the other hand-linked the **soccer-position loanword cluster 06585 ゴールキーパー / 06586 フォワード / 06587 ミッドフィルダー / 06588 ディフェンダー** (created/modified Jan–Jun 2026) — again **zero** `⟦...⟧` links in examples *or* notes at birth — with full example+notes coverage, and migrated 06585's sole-`general` tag to `sports` to match its three siblings (see the [P13](#priority-13-overuse-of-general-as-sole-semantic-tag) update 2026-07-23). Both runs restated the now-standard conclusion: **these general-tier create-era entries are invisible to the notes-quality priority scorer** (which keeps ranking already-polished basic/core adjectives; [Tooling item 20](tooling-backlog.md)), so the **sequential frontier sweep remains the effective instrument for inline-link completion**, and the ~06150→~06600 band stays uniformly zero-linked ahead of the ~5-entries/run cursor. Band now drained sequentially through **06588**; the dedicated 06500–06999 notes-linking sweep (gated on Tooling item 15) remains the higher-throughput fix.

The recurring note-field datum this window is the **malformed-wrapper** counterpart to the 2026-07-21 note-field *reading*-error finding above: while linking the 06500s notes the frontier run again found furigana wrappers that were never checked at creation because they sit in `notes` — `{プロ野球|やきゅう}` (06573; the reading やきゅう belongs only to 野球, not the whole プロ野球 span → the whole-span wrap paints わきゅう over プロ野球) and single-argument / no-pipe brace spans `コーラス{グループ}` and `コーラス{パート}` (06574; katakana inside furigana braces with no reading), all fixed in-run. This reconfirms the standing recommendation that **`check_furigana_format.py`'s systemic-fix sweep should scan `notes` fields, not just headwords/examples** — the detector's field table already *counts* 584 note-field instances (see the [P9](#priority-9-malformed-furigana-wrappers) opening table), but the ID-range systemic-fix sweeps have historically worked headword/examples and let these create-era note-field wrappers accumulate; they surface only incidentally when the frontier link sweep reaches them. This is the same open note-field tooling gap as the P21 2026-07-21 update (both *reading* correctness and *format* wrappers inside `notes` are unchecked), distinct from [Tooling item 22](tooling-backlog.md)'s structured-field *completeness* sweep.

_(Filing note: the two updates below were appended to the Priority 23 section in error by the 2026-07-24 / 2026-07-25 wiki runs and were moved here, where they belong, by the 2026-07-25 wiki run.)_

**Update 2026-07-24 (the create-era band drains through 06613 across two runs; the 06599–06613 tech/loanword/legal/directional block is uniformly link-empty at birth)**: Two 2026-07-23 routine polish frontier runs continued draining the 06500 Jan-2026 creation block, both reconfirming the not-self-healing signature: **06599–06605** (deep-learning/USB-memory/hard-disk/track-and-field/processed-food) and **06606–06613** (tech/loanword/legal/directional nouns, created 2026-01-18) had **zero `⟦...⟧` links in examples AND notes** despite complete furigana, and were fully hand-linked in-run (glossary-style notes — synonym/collocation/direction term-lists — resolve cleanly once each term is looked up against `word_id_lookup.json`). Band now confirmed unbroken **~06150 → 06613**; the 06614+ block is expected to continue the same. The sequential frontier stays the effective inline-link instrument here because this gap is invisible to the notes-quality scorer ([Tooling item 20](tooling-backlog.md)); the dedicated **06500–06999 notes-linking sweep** remains the higher-throughput fix (gated on [Tooling item 15](tooling-backlog.md)).

**Update 2026-07-25 (the create-era band drains into the 06614–06617 agricultural block; a new "examples linked, notes deferred" split where the notes are dense with rare technical compounds)**: A routine polish frontier run continued into the **06614–06617** agricultural cluster (恥辱 / 精米 / 脱穀 / 耕作), again finding **zero `⟦...⟧` links in examples AND notes** at birth. The run **fully linked the EXAMPLES of 06614/06615/06616** but **deferred the notes-linking** because those notes are dense with rare technical compounds that mostly lack entries — 胚芽米, 精米歩合, 大吟醸, 糠, 千歯こき, 足踏み脱穀機, 籾摺り, 耕作放棄地 — each of which would need candidate creation first. This is a **new sub-signature of the create-era band**: not merely naked, but naked-with-notes-that-can't-be-linked-yet, so even a dedicated notes-linking sweep would stall on these until the underlying domain vocabulary is harvested as candidates. Band now extends unbroken **~06150 → 06617**. Two words surfaced in the block were captured per §3 (コンバイン already exists as entry 30081; 雪ぐ すすぐ, seen in 06614 恥辱, added as a candidate). Same P21 item; reinforces the paired inline-link-sweep + candidate-harvest recommendation for domain-dense 06xxx notes (cf. the 2026-07-09 energy/infrastructure update).

**Update 2026-07-25 (the band is confirmed to continue *past* the frontier — 06627–06632 spot-checked at zero coverage; first per-entry cost estimate for the frontier lane)**: A 2026-07-25 routine polish run carried the cursor to **06631** and reported the first forward-looking measurement of this band rather than another behind-the-cursor confirmation: entries from **~06627 onward have zero `⟦...⟧` markers in examples *and* notes**, spot-checked across **06627–06632**, i.e. the create-era zero-link band does **not** end at the frontier — it simply has not been reached. The run also puts a **cost figure** on the frontier lane for the first time: roughly **10–15 minutes per entry** for a 9-example entry needing full tier-1 link work, which it calls "the dominant cost of the frontier lane from here on." Two consequences worth recording: (1) at ~4–5 entries/run the frontier converts this band far slower than new-entry inflow adds to it, so the **dedicated 06500–06999 (and beyond) notes+examples linking sweep** ([Tooling item 15](tooling-backlog.md#15-lint-rule-unlinked-自動詞他動詞-labels-in-notes-fields)) is not a nice-to-have but the only instrument that can close the band; (2) the per-entry figure is the number to use when sizing that sweep. Band now confirmed unbroken **~06150 → at least 06632**, drained sequentially through 06631.

**Update 2026-07-26 (the band is unbroken to 06649, and a second formatting defect travels with it: `・` bullets instead of the house `- `)**: Three 2026-07-26 polish runs worked 06631–06649 and found the zero-link signature in **every** entry: 06631–06638, the な-adjective block 06639–06644, and the frontier 06645–06649 all had **zero `⟦…⟧` links in examples *and* notes at birth**. The band now runs **~06150 → 06649** without a gap.

**The new datum is a second, co-occurring defect from the same creation template**: these entries bullet their notes with `・` rather than the `- ` required by the `vocabulary-notes` skill. Both misses are formatting-level and share a source, so a sweep should fix them together — and the `・` bullets give the band a **cheap grep-able boundary marker** for sizing the remaining scope without opening entries.

**Cost measured**: the な-adjective block needed **3–6 example rewrites and 5–10 note links per entry**, roughly one entry per two minutes of link lookup. At that rate the sequential frontier will spend many runs inside this band.

**The case for a batch-scoped sweep is now strong.** A dedicated 06600–06700 (or 06150–06699) inline-link pass would run far faster than the frontier does, because **the vocabulary repeats heavily across the block** — な, だ, に, なる, 人, 性格 recur in nearly every entry, so the link lookups amortize across the batch instead of being re-derived per entry. The frontier pays full lookup cost on every entry; a batch pays it once.

**Sub-pattern worth noting for scoping** (from the 06614–06617 agricultural block, 2026-07-25): some entries in the band are "examples-linked, notes-deferred" — the notes are dense with rare technical compounds (胚芽米, 精米歩合, 千歯こき, 籾摺り, 耕作放棄地) that each need candidate creation before they can be linked. A batch sweep should link what resolves and log the rest as candidates rather than stalling.

**Update 2026-07-27 (band unbroken through 06655)**: The 06650–06655 frontier polish run again found **every** entry in its range with zero `⟦...⟧` links in examples *and* notes, all hand-linked in-run. The zero-link create-era band is now confirmed unbroken from ~06150 through **06655**. Nothing new in kind — this is roughly the fifteenth consecutive frontier run to report it — but it is the datum that keeps the block-sweep recommendation alive: at ~5 entries per polish run the frontier will not cross this band for years, while the vocabulary inside it repeats enough that a dedicated sweep amortises its lookups. Co-occurring template defect this run: `・` bullets in the same notes fields, now filed as [P28](#priority-28-mixed-bullet-markers--vs----inside-notes-fields).

**Update 2026-07-29 (the frontier's link-free stretch is now mapped ahead of the lane, with a pace warning)**: Two polish runs measured the same creation-batch signature immediately ahead of the comprehensive frontier (`next: 06684`):

- **06678–06680 and 06973/06981** (created 2026-01-18, last touched 2026-03-29): **zero** inline links in examples or notes.
- **06684 そこそこ, 06685 とうてい, 06686 いやおうなく and the rest of the 06681–06690 run**: also zero — the whole block was created before inline links were part of entry creation.

**Pace consequence, stated so the next run can plan for it**: an entry in this stretch needs roughly six examples plus a full notes field linked from scratch, i.e. **~3–4 entries per run rather than the usual pace**. A run that budgets for the normal rate through 06684–06690 will either overrun its context or leave entries half-linked, and half-linked is worse than untouched because the entry then looks polished. Better to plan three entries done properly.

**A second, separable defect in the same cohort**: these entries' notes open with three throwaway conjugation bullets (`X → Xない (negative)` …) that duplicate the conjugation table the renderer already displays from the `conjugation` field. The note-quality scorer already penalises it (this cohort scores 47–62), so the priority lane will keep surfacing these entries for a reason that has nothing to do with their missing links. Filed separately as **Priority 31** below, because it is mechanically detectable and does not need the per-entry judgment that linking does — and because fixing it silently improves this cohort's scores without improving the entries, which is worth doing *after* the links, not before.

**Update 2026-07-30 (the band is confirmed *all-or-nothing*, which changes how a run should be sized)**: The 2026-07-30 polish run worked 06688–06693 and found the coverage binary rather than partial: **not one `⟦…⟧` link across 23 examples and 6 notes fields**, in entries that already had complete furigana. The previous update predicted the pace; this one identifies the reason the pace is unpredictable.

**Frontier-lane throughput is bimodal, not variable.** An already-linked entry is a 2-minute tag and cross-reference check; an unlinked one is 15+ minutes of lookups. There is very little in between, because linking was either part of an entry's creation or it was not. So a run's capacity depends almost entirely on *which kind of block it enters*, and it cannot find out until it opens the files.

**The gap this exposes**: `polishing/priority/cross_refs.txt` orders entries by score but does not distinguish "no links at all" from "some links" — the two states that differ by an order of magnitude in cost. A run reading the priority file cannot see whether the next ten entries are a two-hour job or a twenty-minute one.

**Update 2026-07-30 (second) — the band continues through 06704, and the cost is now split into its mechanical and judgment halves.** Two further polish runs (06694–06697 + 07004, then 06698–06704) found zero link coverage in every entry they opened, extending the confirmed all-or-nothing band to **~06150→06704 unbroken**. One of them measured the work on a single entry — 06702, ten unlinked examples — and the split was roughly **90/10: ~60 dictionary lookups against `word_id_lookup.json`, then a handful of genuine judgments** (homograph choice, word boundaries, whether a bound morpheme counts as a word).

That ratio is the argument for [Tooling item 49](tooling-backlog.md#49-read-only-inline-link-suggester-propose--never-write) — a read-only link *suggester* that proposes `⟦…⟧` spans and lists its ambiguities without ever writing an entry. It would not make this priority automatic; it would move a polish run's budget from the 90% that is lookup to the 10% that is judgment, which on this band is the difference between three entries per run and eight or nine. Given the band is ~550 entries wide and the frontier crosses it at ~7/run, the tooling is worth building before the crawl finishes it.

**Entries too large for a frontier slot should be split out, not squeezed**: 06703 振り切る (15 examples, zero links, core tier) was left untouched by the 2026-07-30 run and filed to [Entry Follow-ups](entry-followups.md) instead. That is the right call — an entry needing an hour does not belong in a lane budgeted in minutes — and the pattern is worth generalising: **when the frontier meets an entry whose link debt exceeds the remaining slot, file it and move on rather than half-linking it.**

The fix is small and lives in `prioritize_polishing.py`: emit a link-count (or a simple `zero-links` flag) alongside each ID. That would let a run either budget honestly or deliberately choose a homogeneous batch, and it would let this item's mapping work — currently done by hand, one polish run at a time — fall out of the priority build for free. Filed as a note here rather than a separate tooling item because it only matters while this band exists; once the create-era block is linked, the bimodality goes away.

## Priority 22: Inconsistent free-text `part_of_speech` display field

**Source**: 2026-06-23 routine polish run (frontier 6250–6254)

The free-text `part_of_speech` field — the human-readable POS string shown in the
entry-page header — is **wildly inconsistent dictionary-wide**, with many surface variants
for the same grammatical category: e.g. `adjective (i-adjective)` (98 entries) vs
`i-adjective` (256); and `noun, suru verb` / `noun / suru-verb` / `noun, verb-suru` /
`verb (suru)` all coexisting for suru-verbs. This is a **display-text** inconsistency only:
the validated structured tag `metadata.tags.pos` (e.g. `adjective-i`, `verb-suru`) is
correct and canonical, and the renderer/search rely on `tags.pos`, not the free-text field.
So there is no functional bug — but the entry-page headers read inconsistently across
otherwise-parallel entries.

**Suggested action**: a one-time normalization pass that maps the long tail of
`part_of_speech` surface variants onto a **canonical display string per `tags.pos` value**
(driven by the structured tag, which is the source of truth). Because `tags.pos` already
encodes the category unambiguously, the mapping is deterministic — the only design choice is
the canonical display wording (e.g. pick `i-adjective` over `adjective (i-adjective)`,
`noun, suru verb` over the other three suru-verb spellings). This is **systemic-fix
territory once a normalizer/detector exists** (see
[Tooling Backlog](tooling-backlog.md) → item 29): the detector lists every entry whose
`part_of_speech` text is not the canonical string for its `tags.pos`, and the transform is
a safe text substitution validated against the structured tag. Low risk (display-only), and
the canonical map should be agreed with the curator before a bulk run since it changes
visible header text on thousands of pages.

## Priority 23: 20 entries (29181–29200) missing `metadata.vocabulary_tier`

**Source**: 2026-07-04 wiki-maintenance tier sync (Activity E / light sync)

A single contiguous new-entries batch created on **2026-06-12** — IDs **29181 through
29200** — shipped with **no `metadata.vocabulary_tier` field at all** (not `null`, absent).
The schema (`build/schema.json`) makes the field optional (`enum` includes `null`, and it
is not in `metadata.required`), so these 20 entries validate cleanly and CI never caught
them; they surface only as a small discrepancy in tier-count reports (`build/audit_tiers.py`
buckets them as `unknown`, so its General total under-counts by 20). Per CLAUDE.md — *"All
new entries go in the general vocabulary tier"* — every one of these should carry
`vocabulary_tier: "general"`. The 20 headwords are ordinary general-tier vocabulary
(一級建築士/二級建築士, 脱サラ, 演奏家, 社会運動/平和運動, 職業訓練校, UFOキャッチャー,
ファッションデザイナー, 絹織物, 抗ウイルス薬, 水泳選手, … ), so the correct tier is
unambiguous for the whole block.

**Scope**: exactly 20 entries (29181–29200); not an ongoing regression — the surrounding
batches (both below 29181 and the later 29338+ restocks) carry the field, so this is a
one-off omission by the single 2026-06-12 batch.

**Detect** (no dedicated detector needed — a one-line scan):
```bash
python3 -c "import json,glob; [print(json.load(open(f)).get('id')) for f in glob.glob('entries/*/[0-9]*.json') if json.load(open(f)).get('metadata',{}).get('vocabulary_tier') not in ('basic','core','general')]"
```

**Suggested action**: a **mechanical-safe** systemic-fix batch — set
`metadata.vocabulary_tier: "general"` on the 20 flagged IDs, bump each `modified` timestamp,
rebuild. No per-entry semantic judgment is required (the tier is `general` by the
new-entry rule and confirmed by the headwords), but the batch is small enough to eyeball in
one pass. A durable follow-up worth considering: have `validate.py` (or the pre-commit hook)
warn on a **missing** `vocabulary_tier`, since the schema's `null`-permissive enum lets the
omission through silently. Tracked as `entry-missing-vocabulary-tier` in
[`backlog-queue.json`](backlog-queue.json) (`batch_ready: true`, scope 20).

## Priority 24: Inline-link base forms written with furigana braces

**Source**: 2026-07-25 routine polish run (frontier; fixed in 00969)

The inline-link syntax is `⟦surface→base：entry_id⟧`, where the **base** segment is meant to be
the plain dictionary form in kanji — `⟦来て→来る：00254_kuru⟧`. **39 entries** instead write the
base form with furigana braces intact — `⟦{来|き}て→{来|く}る：00254_kuru⟧` — carrying wrapper
markup into a field that is never rendered as ruby text.

**Scope**: 39 entries (measured 2026-07-25, dictionary-wide).

**Detect**:
```bash
grep -rl '→[^：⟧]*{[^}]*|[^}]*}[^：⟧]*：' entries/
```
(The character class stops at `：` and `⟧`, so the match is restricted to the segment between
the arrow and the colon — the base-form slot — and cannot be confused with legitimate furigana
in the *surface* slot, where braces are correct and expected.)

**Suggested action**: this is one of the rare **provably-safe mechanical transformations** that
[the systemic-fix playbook](../../../prompts/routine2.md) permits without per-entry semantic
verification: strip `{` , `|reading` and `}` from the base-form segment only, leaving the kanji
run. The regex is anchored on both sides (`→` … `：`) so it cannot escape the slot. Validate with
`build/validate.py` and spot-check ~10 entries before commit. Worth confirming afterwards that
the resulting base forms resolve in `build/word_id_lookup.json` — a braced base form may have been
masking a lookup that never worked, which is exactly the failure mode
[Tooling item 11](tooling-backlog.md#11-inline-link-target-id-resolution-gate-in-validatepy-or-pre-commitci)
exists to catch.

**Update 2026-07-29 — this is a *user-visible* defect, not link metadata, and the corpus is now measured.** The 2026-07-29 polish run found the fact that reframes this priority: **`docs/styles.css:245` renders `content: attr(data-baseform)` as the hover tooltip.** Whatever sits between `→` and `：` in an inline link is shown to the learner. So `⟦{言|い}う→{言|い}う：00515_iu⟧` puts a literal `{言|い}う` — braces, pipe and all — on screen.

Dictionary-wide sweep, two families:

| Family | Occurrences | Entries |
|---|---|---|
| **Braces left in the baseform** (this priority) | 254 | 39 |
| **Kana instead of the dictionary form** (new, Priority 32 below) | 3,567 | 1,712 |

Both are mechanically fixable from the target entry as ground truth: replace the baseform with the target's furigana-stripped headword. The transformation is decidable from `build/word_id_lookup.json`, touches **only link metadata**, and **cannot alter any Japanese text in an example or note** — which makes this one of the few genuinely safe candidates for the "purely-mechanical application" exception in `routine2.md` §B step 3, rather than the per-entry semantic verification that section defaults to.

The scope estimate in this item's original text (39 entries) was right; what was wrong was the framing. This was filed as cosmetic tidying of an internal field. It is the tooltip a learner sees when they hover a word they do not know.

**Update 2026-07-30 — filed a third time, from a third run, still unworked. Re-measured: 36 entries.** The 2026-07-30 polish run found the same defect in 00711 かかる (every notes link written `⟦{時間|じかん}→{時間|じかん}：00468_jikan⟧`), grepped the corpus, and filed it again — independently, without knowing this priority existed. That is a useful signal about the backlog rather than about the defect: **an item that is batch-ready, provably safe, user-visible, and 36 entries wide has now been discovered three times (2026-07-25, 2026-07-29, 2026-07-30) and worked zero times.** Its `backlog-queue.json` priority is 24, so the `systemic-fix` selector never reaches it; meanwhile each polish run that stumbles across it pays the discovery cost again. Small, safe, cheap items should be *promoted* in the queue precisely because they clear in one run — this one is a candidate for the next `systemic-fix` slot on those grounds alone.

The run also contributed a tighter regex than the one above, anchored on the brace immediately after the arrow:

```bash
grep -rlE '→\{[^}]*\|[^}]*\}：' entries/     # 36 entries, 2026-07-30
```
```python
re.sub(r'→\{([^|}]+)\|[^}]+\}：', r'→\1：', s)   # strips a reading from a slot that must not carry one
```

(The two regexes find the same class; this one cannot match a base form containing a nested brace, the other cannot match past a `：`. Either is safe.)

*(Priorities 31 and 32, both filed from the same 2026-07-29 sweep, are at the end of this page in numeric order.)*

## Priority 25: Fabricated conjugation tables from a mis-assigned verb class

**Source**: 2026-07-25 routine polish run (06624 甘える; second case found at 09361)

A verb entry's `conjugation` field is generated from its `pos` tag, so a **wrong verb-class tag
produces an entire table of invented morphology** — every form wrong, in a field learners are
most likely to trust verbatim. **06624 甘える** (ichidan) was tagged `verb-godan` / `godan-ru`,
so `add_conjugations.py` generated 甘えらない / 甘えります / 甘えった. A dictionary-wide scan for
`verb-godan` entries whose reading ends in **-える / -いる** found **38 hits**, of which **36 are
genuine godan** (the well-known 帰る / 滑る / 蹴る / 返る / 入る / 炒る family) and **one further
real case** — **09361 バックレる**, contradicted by its own example (バックレた). Both were
corrected in-run with `add_conjugations.py --force`.

**Scope**: 2 known cases, both fixed. The residual detector population is **31 entries**
(re-measured 2026-07-25 after the fixes) and is a **stable, enumerable false-positive family**:
入る/返る compounds (むせ返る, 若返る, 跳ね返る, 呆れ返る, 裏返る, 覆る, 甦る, 反り返る, 翻る,
気に入る, 痛み入る) plus 炒る / 煎る. That family can simply be allowlisted.

**Detect** (reading-shape heuristic — the 31-entry FP family above is expected):
```bash
python3 -c "
import json,glob,re
for f in glob.glob('entries/*/[0-9]*.json'):
    d=json.load(open(f))
    pos=(d.get('metadata',{}).get('tags',{}) or {}).get('pos',[])
    if 'verb-godan' in pos and re.search(r'(える|いる)\$', d.get('reading','')):
        print(d['id'], d['headword'], d['reading'])
"
```

**The sharper detector**, suggested by the observing run and specified in
[Tooling item 35](tooling-backlog.md#35-verb-class-misassignment-detector-conjugation-tables-contradicted-by-the-entrys-own-examples),
is **self-contradiction**: flag a `verb-godan` entry whose **own examples contain the ichidan
past/て form of its headword** (甘えた / バックレた where the table claims 甘えった / バックレった).
That has no false-positive family at all, because the entry is disagreeing with itself — and it
generalises to the reverse case (an ichidan-tagged godan verb) and to `verb-suru` mis-tags.

**Suggested action**: build the self-contradiction detector, run it dictionary-wide, and re-run
`add_conjugations.py --force` on whatever it flags after confirming the class per entry. Until
then the reading-shape scan above plus the 31-entry allowlist is a usable one-off pass.

## Priority 26: Auxiliary verbs written in kanji in example sentences

**Source**: 2026-07-25 routine polish run (01092_oku)

Contemporary Japanese writes **auxiliary** (helper) verbs in hiragana — 〜ておく, 〜てみる,
〜ていく, 〜てくる — reserving kanji for the same verbs used as **main** verbs (物を置く,
映画を見る). 01092_oku wrote the auxiliary as 〜て{置|お}く in **5 of its own examples** while its
notes wrote it in kana: the entry contradicts itself, and the examples model a spelling that
learner-facing prose should not.

**Scope** (measured 2026-07-25, dictionary-wide, occurrences / distinct entries):

| Written form | Occurrences | Entries |
|---|--:|--:|
| 〜て{行\|い}く | 222 | 200 |
| 〜て{来\|く}る | 203 | 34 |
| 〜て{見\|み}る | 168 | 138 |
| 〜て{置\|お}く | 7 | 7 |

**This priority is not uniformly actionable and must not be swept mechanically.** The counts
above are a *superset*: the same strings are correct when the verb is the **main** verb of a
te-form sequence (「持って{来|き}て」, 「駅で{見|み}た」 — 見る as a full verb after a te-form
clause is not an auxiliary at all). The 〜ておく row is the cleanest cut (7 entries, and おく is
almost never a main verb in that position); 〜ていく / 〜てくる are the most contested, since 行く
and 来る in kanji after て are common in edited prose and a blanket rewrite would be a style
imposition rather than a correction.

**Suggested action**: treat the **〜ておく family (7 entries) as a bounded, verifiable batch**
— open each, confirm the auxiliary reading, convert to kana, update `modified`. Treat 〜てみる /
〜ていく / 〜てくる as a **documentation question first**: decide and record a house convention
(the `example-sentences` skill is the natural home) before any sweep, then size the work from the
convention. The detector rule — te-form immediately followed by a kanji-written
置く/見る/来る/行く/しまう — is cheap to write but needs the main-verb-vs-auxiliary discrimination
above to be useful, so it is best paired with the convention decision rather than shipped alone.

## Priority 27: Dead inline-link target IDs

**Source**: 2026-07-26 routine polish runs (two, 10 + 2 bad links written) → dictionary-wide scan run by the 2026-07-26 wiki harvest

**Scope**: **292 dead links across 160 entries** (144 distinct nonexistent target IDs) out of 262,189 inline links dictionary-wide — 0.11%. Every occurrence is in **00000–07999**, densest at **05000–05999 (112)** then 03000–03999 (64) and 04000–04999 (49).

An inline link `⟦surface→base：entry_id⟧` whose `entry_id` names no existing entry renders as a dead cross-reference on the live site. `build/validate.py` does not check target resolution, so these pass every gate the project has — see [Tooling 11](tooling-backlog.md#11-inline-link-target-id-resolution-gate-in-validatepy-or-pre-commitci) for the full measurement, the detect snippet, and the gate that has to ship first.

**Why this one is genuinely batch-ready** (unusual for this backlog):

- **217 of 292 (74%) are unambiguous 1:1 repairs.** The link's base form resolves to exactly one entry in `build/word_id_lookup.json`, and the dead ID's romaji already matches it — only the digits are wrong (`見る`：`00433_miru` → `00283_miru`, `する`：`00003_suru` → `00392_suru`, `まで`：`01035_made` → `00490_made`). Verification per link is a single lookup, not a semantic judgment.
- **74 need judgment** — homographs where the base form has several entries (`こと` → `01164`/`02152`/`11804`, `いる` → four, `から` → three, `後` → `03545_nochi`/`09580_ato`, `体` → `00784_karada`/`09872_tai`). These are exactly the cases a mechanical pass must *not* guess at; route them per-entry with the surrounding sentence in view.
- **1 has no target at all** — `逆転する`. Either create the entry or convert the link to `noentry`.

**Do not sweep before the gate exists.** The population is entirely iatrogenic — created by inline-link polishing, which is ongoing — so repairing the corpus first just refills it. Ship the `validate.py` resolution check, then batch the 217.

**Suggested batching**: one systemic-fix run per 1,000-ID band, worst first (05000–05999, then 03000–03999, 04000–04999). Apply the unambiguous repairs, defer the ambiguous ones to a second pass, update `modified` on each entry touched, and re-run the detect snippet at the end of the run to confirm the band is clear.

**RESOLVED 2026-07-29 (routine systemic-fix) — swept whole, not band by band, because the fix unit turned out to be the mapping and not the entry.** Final count on a fresh scan: **291 links / 159 entries / 143 distinct dead IDs** (one had been repaired since the 2026-07-26 scan). `build/check_link_targets.py --summary` now reports **0**.

The suggested band-by-band batching was the wrong decomposition. The 291 links reduce to **143 distinct `(dead_id, baseform)` pairs**, and 47 of them are a single mapping (`00347_de` → `00502_de`) spread across 18 entries — so verifying per *entry* would have re-verified the same decision eighteen times while a per-*mapping* pass verified it once. Adjudicating all 143 mappings, then applying each to every occurrence, fit in one run with room for the gate as well. **For a systemic fix whose occurrences share a small set of decisions, verify the decision set, not the occurrence set** — and spot-check occurrences in situ to confirm the decision transfers.

Outcome against this item's own predictions:

- The **74%-unambiguous** estimate held (216 of 291 single-candidate, vs 217 predicted), and the 74 ambiguous / 1 unresolvable splits were exact.
- The ambiguous 74 were **much cheaper than "route them per-entry"** suggested: 32 mappings, and all but a handful resolve by one deterministic rule — *prefer the candidate whose headword is the baseform character-for-character* — which picks the particle over its homographs every time (`も` over 藻/喪, `から` over 殻/空, `こと` over 琴/古都). Contexts were checked anyway and every one confirmed. The genuinely bivalent handful (`いる` = exist/要る/炒る, `やすい` = 安い/〜やすい, `もの`, `よく`, `ない`) needed the sentence, and in every case it was decisive at a glance: all six `いる` links were `〜ている` auxiliaries, both `やすい` links were `使いやすい`/`持ちやすい`.
- **The one thing this item got wrong: "verification per link is a single lookup, not a semantic judgment."** Not quite. The dangerous class is a **kana baseform matching a kanji-headword entry**, where the lookup returns exactly one confident answer that is a *reading homophone*: `ば` (conditional particle) → `03699_ba` 場 "place". Treating single-candidate as self-verifying would have replaced a visibly-dead link with an invisibly-wrong working one. The class is small and detectable up front — 3 of 111 single-candidate mappings, the other two correct (`いっぱい`→一杯, `たち`→達) — so screen for it and read those in situ.
- **1 unresolvable became 2**: `逆転する` as predicted, plus `ば` after the above rejection. Both set to `noentry` and queued as candidates.

**"Do not sweep before the gate exists" was right, and both shipped together** — see [Tooling 11](tooling-backlog.md#11-inline-link-target-id-resolution-gate-in-validatepy-or-pre-commitci) for why the gate needed wiring rather than writing (the check existed; three of four CLI paths never called it). Because the corpus reached 0 in the same run, the gate is an absolute error rather than the ratchet this item assumed, so no baseline file is needed. The follow-on population — links that resolve but not to their own base form, 418 after normalization — is filed as `link-target-baseform-disagreement`.

## Priority 28: Mixed bullet markers (`・` vs `- `) inside notes fields

**Source**: 2026-07-27 routine polish observation (00908–07441 priority lane, 06650–06655 frontier).

Older `notes` fields use `・` (nakaguro) as their list-bullet marker; newer ones use `- `.
Both render, but the mixed convention is visible on the live site, and
`score_note_quality.py`'s bullet check treats the two alike, so nothing ever surfaces it.
**7 of the 13 entries** polished on 2026-07-27 still carried `・` bullets — consistent with
the co-occurrence noted in [P21](#priority-21-unlinked-自動詞他動詞-labels-and-particles-in-compound-verb-notes)
update 2026-07-23, where `・` bullets travel with the same pre-2026 note templates as the
zero-link band.

**Measured scope (2026-07-27)**: **18,272 line-initial `・` instances across 2,524 entries**
— i.e. the older convention is not a pocket, it is roughly a twelfth of the dictionary.

**Proposed normalization**: line-initial `・` → `- `, **inside the `notes` field only**.

**What must not be touched**: `・` is real Japanese punctuation — the compound-name and
loanword separator (コーヒー・ブレイク, ニュー・ヨーク) and the list separator *within* a line.
The rule is therefore anchored twice: start-of-line **and** inside `notes`. `・` in example
sentences, headwords, glosses, and mid-line inside a notes bullet stays.

**Risk and sequencing**: the anchored rule is close to mechanically safe, but at 18k
instances a blind sweep is exactly the kind of "provably safe" transformation that has
burned this project before (see [P25](#priority-25-fabricated-conjugation-tables-from-a-mis-assigned-verb-class)).
Sequence it as: (1) add the count to a detector so the number is reproducible, (2) sample
~30 entries for line-initial `・` used as genuine punctuation, (3) sweep in ID blocks with
validation after each. Cheap, cosmetic, dictionary-wide — a good low-risk `systemic-fix`
item once step 2 clears.

## Priority 29: Adjective examples that teach a phrase where the language uses a set compound

**Source**: 2026-07-27 routine polish observation (00908–07441 priority lane).

Several colour and temperature adjective entries illustrate the adjective with an
attributive phrase in a slot where Japanese overwhelmingly uses an established compound:
**×青い信号** for 青信号, **×赤い信号** for 赤信号. The phrase is grammatical, so nothing in
the validation chain objects; it is simply not what a learner will meet, and an example
sentence is the one place in an entry that claims to show real usage.

**Why this class is worth a sweep rather than incidental fixing.** It is invisible to every
instrument the project has. `validate.py` sees well-formed JSON; the note scorer sees a
present EXAMPLES section; the cross-model accuracy reviewer judges whether the English
translation matches the Japanese — and it does, faithfully, because the Japanese is
grammatical. The defect lives in the gap between "correct" and "idiomatic", which only a
reader who knows the compound will notice.

**Shape of the population.** The trigger is a **lexicalized N+N compound that competes with
the adjective's own attributive form**, so the affected clusters are small and enumerable
rather than dictionary-wide:

- **Colour** — 青/赤/黒/白/黄色 before 信号, and the same adjectives before 字 (赤字/黒字),
  板 (黒板), 紙 (白紙), 熱 (黄熱).
- **Temperature** — 熱/冷/温 before 湯 (熱湯), 水 (冷水/温水), 蔵 (冷蔵).
- Likely also 早/速 (早朝, 速球), 高/低 (高熱, 低温), 大/小 (大雨, 小雨).

**Suggested approach**: this is a *review queue*, not a mechanical rewrite — the adjective
phrase is sometimes exactly right (青い空 is not a compound candidate), so each hit needs a
reader. Enumerate the ~15 competing compounds above, grep the example sentences of the
corresponding adjective entries for the adjective-plus-noun phrase, and hand-judge the
hits. Small, bounded, and a genuine content improvement rather than a format one.
Related: [research/collocations.md](../research/collocations.md) covers why this failure
mode is systematically hard for non-native (and model-written) examples.

## Priority 30: Latin characters inside furigana readings — RESOLVED 2026-07-28

**Source**: 2026-07-28 routine accuracy-review (19951–20450).

Eight entries dictionary-wide had Latin letters embedded in a furigana reading —
`{旅|たbi}`, `{形式|けいしiki}`, `{敷金|しikikん}`, `{間違|まちga}`, plus four wrapper
misuses. The cause is mechanical: a romaji-input IME sequence left uncommitted, so the
un-converted keystrokes were written into the reading verbatim.

**All 8 were fixed in that run and the class is now empty.** It is recorded here because
of *how* it was found, which is the more durable lesson: the paid furigana screener caught
**one** instance (in 19961); a one-line regex scan for `[A-Za-z]` inside a reading found the
other **seven** in seconds. A reading containing a Latin letter is a defect **by
construction** — there is no case where it is correct — which makes it the cheapest, most
reliable check the project could run, and precisely the true-positive class that
[Tooling item 24](tooling-backlog.md#24-non-hiragana-reading-lint-cheap-replacement-for-the-furigana-screeners-true-positive-class)
proposes replacing the screener with.

**Recommended follow-up**: promote the scan to a permanent CI check so the class cannot
refill. Unlike most items on this page, that requires no review queue and no judgment —
any match is a failure. Tracked as the concrete first rule of Tooling item 24.

## Priority 31: Redundant conjugation bullets at the head of notes

> **Update 2026-08-01 — the na-adjective half is confirmed, and the band is contiguous.** The
> 2026-07-31 polish run found all eight of 06705–06712 carrying the pattern: the five
> i-adjectives (06705–06709) open their notes with `・Xい → Xく (adverbial)` bullets *while also
> having a full generated `conjugation` table that the renderer already displays*, and the three
> na-adjectives (06710–06712) carry an equivalent FORMS block. So the family is not
> i-adjective-specific — it is a note-template habit spanning both adjective classes, and the
> redundant block pushes the genuinely useful USAGE/NUANCE content below the fold.
> The run deliberately **left them in place**: changing eight entries' note structure would make
> them inconsistent with the rest of the dictionary, so this needs a decision plus a sweep, not
> per-entry drift. That is the right call and it is also the reason the item has not moved —
> it is blocked on a **curator decision** (is the generated table authoritative?), not on
> detection.

**Source**: 2026-07-28 routine polish run (second run), 06678–06680 / 06973 / 06981 cohort

Entries in the 2026-01-18 compound-verb creation batch open their `notes` field with three
throwaway conjugation bullets in the shape

```
・X → Xない (negative)
・X → Xます (polite)
・X → Xて (te-form)
```

These duplicate, in prose, the conjugation table the renderer already builds from the
entry's structured `conjugation` field — so the learner sees the same three forms twice on
the page, once as a hand-written list and once in the full table. They also consume the
first and most valuable lines of the notes, where a learner looks for what the word
*means* and how it is used.

**Detection**: notes whose first non-empty line is a `・` bullet matching
`→ .*(ない|ます|て)\s*\(`. Bounded and mechanical to find; the *removal* still wants a glance
per entry, because a few entries may use the same shape to document a genuinely irregular
form worth calling out.

**Interaction with the priority lane** (the reason this is filed rather than left as a
note): `build/score_note_quality.py` penalises this pattern, so the cohort scores 47–62 and
the notes-priority lane keeps surfacing it. A run that arrives expecting a thin note finds
a note that is not thin, just badly ordered. Clearing this class removes a standing source
of priority-lane no-ops — but it should be sequenced **after** the inline-link work on the
same cohort (Priority 21), since deleting the bullets raises the score and would drop these
entries down the ranking while they still have zero links.

**Update 2026-07-30 — the band is unbroken and the detector is now specified.** Three
consecutive polish runs found this in *every* verb entry they touched in the 066xx band:
06678–06680 / 06973 / 06981 (the original), 06694–06697 + 07004, then 06701 and 06704. Two runs
finding it in every candidate entry is no longer a cohort observation — it is a property of the
band, and the frontier is walking it one entry at a time at ~7 entries per run.

The runs also converged on a detector sharper than the "first non-empty line" test above, because
it does not depend on bullet position or marker:

> **a verb or adjective entry whose `notes` contain a line matching `→ ?.*(ない|ます|て|た)\s*\(`
> *while the entry has a populated `conjugation` field*.**

The conjugation field is the discriminator that makes it precise: the defect is not "the notes
mention a conjugated form", it is "the notes hand-list forms the structured field already holds
and the renderer already tables". Worth building before the frontier walks the rest of the band —
a detector turns ~7 entries/run of incidental cleanup into one bounded systemic-fix pass.

**Band signature (2026-07-30).** The 066xx–070xx create-era entries carry three defects together,
and a run that opens one of these entries should expect all three: **zero inline-link coverage**
(furigana braces present, not one `⟦…⟧` — [P21](#priority-21-unlinked-自動詞他動詞-labels-and-particles-in-compound-verb-notes)),
**`・` bullets instead of `- `** ([P28](#priority-28-mixed-bullet-markers--vs----inside-notes-fields)),
and the redundant conjugation head-block (this priority). They share a cause — one creation batch,
one template — so the three queues are three views of the same cohort, and clearing them in one
pass per entry is strictly cheaper than three sweeps.

## Priority 32: Inline-link base forms written in kana instead of the dictionary form

**Source**: 2026-07-29 routine polish run (dictionary-wide sweep)

**3,567 inline links across 1,712 entries** carry a kana baseform where the dictionary form
is kanji — e.g. `⟦{期間|きかん}→きかん：00229_kikan⟧`. Measured as: the link's declared baseform
equals the target entry's `reading` while the target's `headword` differs.

Per the tooltip finding in Priority 24 above, this is user-visible: hovering 期間 shows a
tooltip reading `きかん` rather than `期間`. The learner gets the pronunciation they can
already see in the furigana, instead of the headword they would need in order to look the
word up — the one piece of information the tooltip exists to supply.

**Fix**: identical to Priority 24 — replace the baseform with the target entry's
furigana-stripped headword, resolved through `build/word_id_lookup.json`. Same safety
argument (link metadata only, no Japanese text touched), same suitability for a mechanical
`systemic-fix` batch. The two priorities should be done in one pass; they differ only in
which malformed shape the baseform took.

**Sizing note**: at 3,567 occurrences this is fourteen times Priority 24 and the largest
mechanically-safe cleanup currently open. Worth running as its own `systemic-fix` item
rather than as a rider on 24.

## Priority 33: Mimetic entries whose notes announce they are onomatopoeia but whose tags do not (77 entries)

**Source**: 2026-07-30 routine polish run (05xxx onomatopoeia block); scope measured by the 2026-07-30 wiki harvest

Entries for mimetic and onomatopoeic words in the 05xxx band carry
`semantic: ["descriptive"]` with **no `onomatopoeia` tag** — including entries whose own notes
open with the literal heading `ONOMATOPOEIA:` or state outright that the word "is an
onomatopoeic word (オノマトペ)". The entry text and the entry's tags disagree, in the same file.

Four were fixed at the frontier this run (**05268 はらはら**, **05836 ひんやり**,
**05837 しっとり**, **05893 がっくり**), with **05374 ひやひや** and **05267 そわそわ** showing the
same shape untouched.

**Scope: 77 entries dictionary-wide**, measured by the harvest with the detector rule below.
The population is not confined to 05xxx as the observing run supposed — it reaches from
**01047 レンジ** and **01161 揺れる** up through the 05xxx block — but the *cause* the run
identified still holds, because **19924 ぱらぱら**, a much later entry, **does** carry
`onomatopoeia`. So this is a creation-era default that was corrected at some point, leaving a
bounded historical population rather than an ongoing leak.

**Detector rule** (deterministic, no semantic judgment beyond confirming the note text):

> the entry's `notes` contain `ONOMATOPOEIA` or `オノマトペ`, **and** `onomatopoeia` is absent
> from `tags.semantic`.

**Why this is a good `systemic-fix` candidate.** It is the rare tag-drift family where the
evidence is *inside the entry being changed* — the fix does not require deciding what the word
means, only reading what the entry already says about itself. That puts it at the mechanical end
of §B's verification spectrum, unlike the sole-`general` and off-vocabulary families where the
destination tag is a judgment. Precision should be near 1.0; the only checks needed are that the
note text is an assertion about the headword rather than a contrast with some other word, and
that `descriptive` is retained alongside rather than replaced.

**Related**: [Tooling 44](tooling-backlog.md#44-consistency-check-non-neutral-formality-with-no-register-statement-in-the-notes) proposes the mirror check — an `onomatopoeia` entry tagged `formality: formal` is almost certainly wrong, since mimetics are characteristically colloquial. The two run over overlapping populations and would compose well in one pass. See also [research/onomatopoeia-mimetics.md](../research/onomatopoeia-mimetics.md) for why the tag matters to a learner: mimetics are a category learners systematically under-produce, and the tag is what makes them findable as a class.

## Priority 34: `action` as the sole semantic tag on a verb (2,085 entries)

**Source**: 2026-07-30 routine polish run (00684 歌う, 00711 かかる, 06701 差し引く, 06704 飛び付く — four of the six verbs the run touched); sized by the 2026-07-30 wiki harvest

Four of six verbs in one polish slot carried `semantic: ["action"]` where a specific in-list tag
was available and obvious:

| Entry | Was | Should be | Note |
|---|---|---|---|
| 00684 歌う | `action` | `music` | its own noun 歌 is already tagged `music` |
| 00711 かかる | `action` | `time-general` + `money` | the entry's own notes are about time and cost |
| 06701 差し引く | `action` | `finance` | |
| 06704 飛び付く | `action` | `movement` | |

**Scope**: **2,085 entries** dictionary-wide have `semantic == ["action"]` and a `verb*` POS tag
(measured 2026-07-30, all 30,049 entries). That is ~7% of the dictionary and by a wide margin the
largest single tag-drift family on this page after `tag-sole-general`.

**Why no existing instrument sees it.** `action` **is** in `VALID_SEMANTIC`, so the off-vocabulary
detector (`check_tag_drift.py --check unknown-semantic`, [P20](#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration))
is blind to it by construction, and the semantic-mismatch heuristic has no reason to fire. The
defect is not that the tag is wrong — a verb *is* an action — but that **it carries no information
the POS field did not already carry**. `pos: ["verb-godan"], semantic: ["action"]` is a tautology
occupying the slot that should tell a learner what domain the word belongs to. This is the same
failure as sole-`general` ([P13](#priority-13-overuse-of-general-as-sole-semantic-tag)), one
category over: a placeholder that survives review because it is never *false*.

**Detect** (deterministic, exact):

```bash
python3 - <<'PY'
import json, pathlib
for f in sorted(pathlib.Path("entries").rglob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    t = (d.get("metadata") or {}).get("tags") or {}
    if t.get("semantic") == ["action"] and any(str(p).startswith("verb") for p in (t.get("pos") or [])):
        print(f.name[:5], d.get("headword"), "|", d.get("gloss"))
PY
```

**Fix requires a model, per entry.** Unlike the off-vocabulary families there is no migration
table — the destination depends on what the verb *means*, and the right answer is often two tags
(かかる → `time-general` + `money`). The detector's job is to produce the queue and the gloss;
the judgment cannot be batched away. Sequence it behind the off-vocabulary drain (P20), which is
mechanisable, and consider capping it per run: at 2,085 entries this is a standing lane, not a
sweep. A reasonable first cut is verbs whose gloss already names a domain the taxonomy has a tag
for.

**Related**: [P13](#priority-13-overuse-of-general-as-sole-semantic-tag) (the sole-`general`
analogue — same shape, different placeholder),
[P11](#priority-11-batch-creation-semantic-tag-transportation-misapplied) (wrong-category tags,
which a detector *can* see).

## Priority 35: Stale `noentry` inline links — 3,797 markers now resolve (2,887 mechanically)

**Source**: 2026-08-01 routine polish run (5 hits in a ~14-entry sample, estimated "hundreds");
2026-07-31 routine accuracy-review (spot checks: ロープ 27860, 鉢 29581, ために 28332, 返る 29164);
originally described as [Tooling 19](tooling-backlog.md#19-stale-noentry-inline-link-detector).
**Measured dictionary-wide by the 2026-08-01 wiki harvest.**

A polishing run that meets a word with no entry writes `⟦水→水：noentry⟧`. The marker is correct
when written. A later `new-entries` run creates that word, and nothing sweeps back — so the
reader sees plain text where a working link now exists.

Of **7,320** `noentry` links in the corpus, **3,797 (52%) now resolve** to a real entry.
Stratified by resolution confidence:

| Class | Count | Fix mode | Example |
|---|---|---|---|
| A1 headword match, multi-char, unique target | **2,123** | mechanical | 理容院 → `27288_riyouin` |
| A2 katakana headword, unique target | **764** | mechanical (no reading ambiguity) | ボストンバッグ → `27285_bosutonbaggu` |
| A3 headword match, multi-char, ambiguous | 27 | per-entry | 明日 → `00501_ashita` *or* `27453_myounichi` |
| B headword match, **single character** | 498 | per-entry | 角 → `02158_tsuno` (つの), but the link's 角 is usually かど |
| C reading-only match, multi-char | 337 | per-entry | たち → `01551_tachi` (達) — often the suffix, not the word |
| D reading-only match, single character | 48 | reject by default | ば → `03699_ba` (場) — the link's ば is the conditional particle |

**The batch is A1 + A2 = 2,887 links** with a full headword match and exactly one candidate
entry. The evidence needed to accept each fix is entirely inside the link, so precision should
be near 1.0 — this is the largest provably-safe, user-visible item on this page.

**B, C and D (883) must not ride along.** A match on a single character or on a reading alone is
as likely to be a homograph as the word — the same family (b) trap that made
`link-target-baseform-disagreement` a `verify: per-entry` item.

**This is a live leak, not historical residue.** Grouping A-class links by the band of the entry
that now exists: 441 in 00000–25999, 662 in 26000–27999, **1,678 in 28000–29999**, 133 above
30000. **85% was created by entry creation in the last few months**, and every `new-entries` run
adds more. Tooling 19's incremental half — `manage_candidates.py sync` already computes the
crossed-over word set for free — closes the source; this sweep only clears what has accumulated.

**Related**: [Inline Link Integrity](../topics/inline-link-integrity.md) (full analysis and the
other five link classes), [P24](#priority-24-inline-link-base-forms-written-with-furigana-braces),
[P27](#priority-27-dead-inline-link-target-ids),
[P32](#priority-32-inline-link-base-forms-written-in-kana-instead-of-the-dictionary-form).

## Informational: Entries with zero inline links (23,294) are the polish frontier, not a defect

**Source**: 2026-07-31 and 2026-08-01 routine polish runs, both reporting a frontier block
"created with zero inline links … a creation batch that predates the requirement" and proposing
a `check_link_coverage.py` detector plus a targeted backfill. **Measured and closed with no
action by the 2026-08-01 wiki harvest.**

There is no batch. Zero-link entries are 0–1.2% of every band below ID 06000, 62.7% of
06000–07999 (the comprehensive frontier sits at 06723, inside that band), and ~100% of
everything above 08000. Essentially all 265,750 inline links in the dictionary live below ID
08000.

`CLAUDE.md` states the cause directly: links are *never* added at creation time, only in a
separate polishing step. So an unpolished block has no links by design, and **the frontier lane
is the backfill**. A `check_link_coverage.py` would faithfully report "77% of the dictionary,"
which is the frontier's position restated.

Recorded here so the next run that trips over an unlinked block does not file it a fourth time.
The strategic consequence — the frontier lane advances 4–8 entries per run against 23,294
unlinked entries, so it cannot close the gap, and
[Tooling 49](tooling-backlog.md#49-read-only-inline-link-suggester-propose--never-write) is the
only filed item that attacks the real cost — is written up on
[Inline Link Integrity](../topics/inline-link-integrity.md).

## Informational: `ている` has no entry and is `noentry` in 37 ASPECT notes — a convention decision, not a defect

**Source**: 2026-07-25 routine polish run

`ている` — arguably the single most important aspectual form a learner meets — has **no entry**,
so every ASPECT note that mentions it links to `noentry`. **37 entries** currently carry that
marker (measured 2026-07-25). Nothing here is broken: `noentry` is the documented way to record
"this word was considered and has no entry yet," and the
[stale-`noentry` detector](tooling-backlog.md#19-stale-noentry-inline-link-detector) exists to
convert such markers once an entry appears.

What makes it worth recording is that it is a **standing curator decision** rather than a
backlog item a Routine run can work: either (a) the dictionary gains grammar-form entries for
core auxiliaries (ている, ておく, てしまう, …), which is a scope decision about what this
dictionary *is*, or (b) the project documents a convention that auxiliary/grammatical forms are
never inline-linked, in which case those 37 markers should be removed rather than left waiting
for an entry that will never come. A third path — an **expository article** on ている rather than
an entry — is filed under [Expository Articles](expository-articles.md) as the lowest-cost option
that still serves the learner. Until the curator picks one, polishing runs should keep writing
`noentry` (the status quo) and should not invent an entry for it.

## Informational: Pre-polished cohort around 00083–00090

Four entries in the 00074–00096 range (00083 俳句, 00086 発揮, 00087 花火, 00088 判事) were already fully linked — suggesting a prior polish pass touched that range. Subsequent sessions entering this area should expect occasional entries needing no work.

## Related pages

- [Tooling Backlog](tooling-backlog.md) — tool improvements surfaced alongside these patterns
- [Entry Follow-ups](entry-followups.md) — specific entry fixes
- [Content Pipeline](../project/content-pipeline.md) — how polishing tasks work
- [Entry Consistency](../topics/entry-consistency.md) — consistency standards
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis of recurring tag-drift patterns (covers P6–P8 above)
- [Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) — analysis of malformed wrapper patterns (covers P9 above)
