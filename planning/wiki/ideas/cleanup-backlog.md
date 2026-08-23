# Cleanup Backlog

**Last updated**: 2026-08-23 (harvest of the 12 observations from the 2026-08-21/22 runs — **one new priority, two hot spots identified, three proposals refuted**. **P67**: the interrogative family is **12 basic-tier entries carrying six semantic labels and four POS labels** — a genuinely closed set, the most-looked-up words in the dictionary, tagged six different ways; filed `needs-decision` because migrating without a convention ruling just re-scatters it. **P20's hot spot has a cause**: measuring off-list tags by *creation date* rather than ID band — a first for this page, after three refuted ID-band cohorts — shows the **2026-01-25 run produced 330 entries of which 191 (57.9%) carry off-list tags**, and all 191 sit inside 08000–08999, which is exactly the hot spot the 2026-08-16 refresh found without being able to explain; the filing run's own 2026-02-22 cohort is **2.0%, below the 3.0% dictionary-wide rate**, the fourth ID-correlated false cohort in five weeks. **P50's backfill is settled by refuting both keyings**: all 57 members fall in one eight-day creation window, but the worst day inside it runs 3.8% against 21% for the 03900–03999 block, so block-keying is 5× more efficient — and at 57 entries total neither keying is needed, it is one bounded batch. Also **refuted**: a `formality: formal` detector for everyday concrete nouns (214 flags, of which the precise cut is 4), and the suggestion that the sole-`general` check filters 06985–06994 (the observing run had already fixed all ten). **P62's distortion reproduces and finally gets a base rate**: `・` entries are 24 of the top 100 priority lines (matching the 26%-of-top-500 measured 2026-08-15) against an **8.1% dictionary-wide base rate** — a real 3× enrichment, and still not the binding defect, since 76 of the top 100 are not `・` entries.) Prior 2026-08-16 (harvest of the 30 observations from the 2026-08-15/16 runs — **two new priorities, one hot spot relocated**. **P63**: 730 entries use a near-synonym of a collocation/pattern heading the dictionary already standardises on — but the filing run's proposal to rename *everything* to `COMMON COLLOCATIONS:` is refused, because it would merge 3,460 entries' `COMMON EXPRESSIONS:`/`SIMILAR EXPRESSIONS:`/`PARTICLE PATTERNS:` sections into a category they are not; the 55% false-positive rate that prompted it is a checker defect (Tooling 125). **P64**: okurigana swallowed into the ruby (`{痛|いたみ}` for `{痛|いた}み`), **90 pairs / 123 instances**, structurally the mirror of P60 and invisible to every furigana instrument for the same reason — the kanji *does* have a reading, it is just too long. **P20 relocated**: 934 entries carry off-vocabulary semantic tags and the largest concentration is **08000–08999 (201, 22% of the population)**, not the 11750+ band its filing run named — 348 sit below ID 11000, and this is the third ID-correlated false cohort in three weeks.) Prior 2026-08-13 (2026-08-13 (harvest of the 26 observations from the 2026-08-12/13 runs — **two new priorities, one hypothesis refuted, one curator ruling requested**. **P55**: 23 inline links that resolve to a homophone of the intended word (終身→就寝, 用地→幼稚, 詩的→指摘), measured over all 273,656 links — the tail of the class the 2026-07-31 batch repaired 87 of, and invisible to every checker the project has. **P56**: body-part idioms and their body-part nouns never cross-reference each other, seen on 6 of 6 frontier entries, scope unmeasured. **Refuted**: the off-vocabulary semantic tags are *not* one contiguous creation band — IDs span 00333–27818, 24 of 62 blocks are clean, five blocks hold 54% — although the queue did fall 55% in a week. **For the curator**: `VALID_SEMANTIC` has no place/location and no sound/perception tag, so ~75 off-list instances have nowhere to go and four sole-`general` entries cycle through the P13 detector forever.) Prior 2026-08-12 (wiki harvest of the 26 loose observations from the 2026-08-11/12 runs — **no new priority**; two filings that read as new findings are re-discoveries of open, batch-ready items, and the third re-scope lands opposite to what its filing implied. **P24 re-filed a fourth time**: braced inline-link base forms measured at **35 entries** (two closed 2026-01 cohorts, 00697–00716 and 00965–00988), an item promoted to priority 5 on 2026-07-30 *because* three runs had already found it — and worked by none of the four, which is a selector question, not a backlog one. **P43's block is no longer upcoming**: 79 of 101 IDs in 06880–06980 carry zero links and the unbroken run starts at **06896**, exactly the polish frontier, so the 2026-08-06 prediction of one-fifth speed and the filing run's measured 8–10 min/entry now agree from both sides — the routing decision is live, not deferred. **P20 re-scoped**: 1,364 entries / 1,635 instances / 486 labels; hot spots at 09000–09499 (48%) and 08000–08499 (40%) hold a third of the population while 23 of 62 blocks are clean; and `TAG_MIGRATION`'s nine rows clear **8.1%** — which is evidence *for* the 2026-08-07 decision to keep the map at nine rows and let the per-entry reviewer be the instrument, this being the fourth time extending it has been proposed.) Prior 2026-07-27 (wiki harvest of the 17 loose observations from the 2026-07-27 polish, systemic-fix and accuracy-review runs — one **new priority** plus three cohort extensions: **new P28** — mixed bullet markers inside `notes`, the older `・` convention measured dictionary-wide at **18,272 line-initial instances across 2,524 entries** (~1/12 of the dictionary), normalizable by a doubly-anchored rule (line-initial AND inside `notes` only, since `・` is real punctuation elsewhere) but sequenced behind a sample check rather than swept blind. **P20** — the off-vocab band measured at **124 of 250 entries (49.6%)** in 19701–19950 (143 occurrences / 83 distinct off-list tags), with the operational finding that **the model is the wrong instrument**: the large families are 1:1 synonym renames `check_tag_drift.py`'s `TAG_MIGRATION` covers only nine of, so the ~50 safe renames belong in the map and only the ~7% judgment-dependent residue belongs in a review. **P17** — a seventh formality sub-family, 〜甲斐 nouns auto-tagged `informal` (06653/06654), notable for being a *morphological* cluster and therefore an unusually cheap detector cut. **P21** — the zero-link band unbroken through **06655**, with `・` bullets co-occurring in the same notes fields, now cross-linked to P28.) Prior 2026-07-26

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

**Update 2026-08-06 — the slice that sits inside an inline-link surface, and why it should lead the sweep.** A 2026-08-05 polish run found `⟦{あの|あの}→あの：00915_ano⟧` in 00792 首 and asked for "a targeted scan for `{かな|same-かな}` wrappers inside link surfaces". Measured across all entries: **108 instances across 94 entries** where a pure-kana `{…|…}` wrapper sits inside the surface or base-form field of a `⟦…⟧` link — **84 katakana** (`{バイク|ばいく}`, `{ニュース|にゅーす}`, `{グループ|ぐるーぷ}`) and 24 hiragana (`{どんどん|どんどん}`, `{ここ|ここ}`, `{なる|なる}`). These are a subset of the 373 `pure-kana` findings above, not a new family, so this is a targeting hint rather than a new item — but three properties make it the right slice to sweep first:

- **It is where the defect stops being cosmetic.** Elsewhere a pure-kana wrapper renders a redundant reading; inside a link surface it is text a lookup may be matched against. All 108 currently resolve (5 point at `noentry`), so nothing is broken today — the risk is that the *next* tool to read link surfaces has to know about the wrapper.
- **The katakana majority (84) inherits the unconditional fix rule** established for the 258 above: delete the wrapper, keep the surface. And the same 24 hiragana that need judgment as wrappers need none as link surfaces, since a link surface has no reason to carry a reading gloss at all.
- **It has an obvious neighbour in the tooling backlog.** The dominant shape — a katakana word wrapped with a hiragana pseudo-reading — is the same script asymmetry [Tooling 76](tooling-backlog.md#76-word_id_lookupjson-answers-katakana-lookups-from-by_headword-only) describes in `word_id_lookup.json`, where `by_reading` holds zero katakana keys. A writer who believes a katakana word needs a hiragana reading to be looked up produces exactly this wrapper. Worth fixing the belief in the `inline-word-links` skill at the same time as the 108 instances.

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

**Update 2026-08-04 — the katakana slice, measured.** A polish run over the 06763–06774 loanword
block found sole-`general` on 06763 フィードバック and 06764 プロジェクト and proposed a
`--check sole-general` pass filtered to katakana headwords as "high-yield". Measured: **350 entries
whose headword is pure katakana carry `semantic: ["general"]` and nothing else** — about 9% of this
priority's queue, concentrated in the low IDs (00005 アップ, 00017 ボール, 00032 ダイヤ, 00034 ダム,
00058 ガム, 00073 ゴム …). The filter is worth using because loanwords are the easiest sole-`general`
entries to retag: the English source word usually names the destination directly (ボール→`sports`,
ゴム→`material`… noting that `material` is itself off-vocabulary, so P20 and this item land on the
same entries). Not a separate item — a targeting hint for this one.

**Update 2026-08-06 — the gloss-keyword suggester measured, and it does not work.** The
2026-08-06 accuracy-review saw 11 sole-`general` entries whose correct tag "follows directly from
the gloss text" (視覚障害/低体温症/癒合/抗菌薬 → `health`, 選挙運動 → `politics`, 不敬罪 → `law`,
相対性 → `science`, 丸括弧/角括弧 → `language`, 忌中 → `culture`+`religion`) and proposed that
"a gloss-keyword suggester over the 3,791-entry queue would likely propose a defensible tag for
most of it". This is the oldest recommendation on this item — the original 2026-05-23 entry
proposes the same instrument via [Tooling 6](tooling-backlog.md#6-tag-drift-detector) — so it was
measured rather than filed again.

The suggester was built empirically rather than by hand, which is the strongest version of the
idea: for every English token in the gloss/explanation text of the **20,257** entries that carry a
specific tag, compute the distribution of tags among entries containing it, and keep the tokens
that concentrate ≥80% on one tag (n≥5). That yields 899 discriminating tokens. Run against the
**3,741** sole-`general` entries:

| threshold | discriminating tokens | entries receiving any proposal |
|---|---|---|
| ≥80% concentration, n≥5 | 899 | **554 / 3,741 (14.8%)** |
| ≥90% concentration, n≥10 | 146 | 109 / 3,741 (2.9%) |

So "most of it" is 15% at the loose threshold and 3% at a threshold you would actually trust —
and the loose threshold's proposals are visibly wrong about one time in five. From a random 16:
**眉** (eyebrow) → `nature` because its explanation says "ridge"; **保険料** (insurance premium) →
`transportation` because the gloss illustrates car insurance; **負け惜しみ** (sour grapes) →
`food`; **田んぼ** (rice paddy) → `food`.

Two things follow, and the second is the one worth keeping:

- **The population is not gloss-legible, and that is structural.** An entry ends up with sole
  `general` precisely *because* no domain was obvious to the tagger, so the sole-`general` set is
  enriched for words whose gloss carries no domain signal. A random sample reads: 万端, 概説,
  座標, 型, 連鎖, 特価, 書斎, リベラル, 抱き合わせ. The 11 transparent domain compounds the
  observing run saw are the visible slice, not a sample of the population — and the katakana
  slice measured 2026-08-04 (350 entries, retaggable from the English source word) is the other
  visible slice. **Between them they are ~10–15% of the queue; the rest needs a lexicographer.**
- **An automated gloss-keyword pass would manufacture [P11](#priority-11-batch-creation-semantic-tag-transportation-misapplied) defects.** Every error above has the same
  shape: the tag was taken from the *context the gloss mentions* rather than from what the
  headword *denotes* — 保険料 is not about transportation, it is about money, and the word "car"
  appears only because insurance was being illustrated. That is the exact defect P11 exists to
  clean up and the exact reason the project's semantic tags are defined denotationally. **A tool
  that infers tags from surrounding text cannot be denotational**, so this instrument is not
  merely low-yield, it is pointed the wrong way. Tooling 6 should record that.

**Status of the instrument question**: closed. The remaining levers on this item are the ones
already named — the katakana filter (350), the within-block-inconsistency heuristic (2026-07-30
update: neighbours where one sibling carries a specific tag and the other sole-`general`, the
06690/06691 exam pair being the control case), and frontier applies. None of them read the gloss.

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

**Update 2026-08-02 (dictionary-wide measurement — the shipped map has 660 unapplied hits, and the tail says the map strategy stops near half)**: The 2026-08-02 wiki harvest measured the whole population directly rather than band by band, which answers the 2026-07-28 question above and reframes the sequencing.

**Population**: **4,900 off-vocabulary instances across 3,874 entries and 818 distinct labels.** The distribution is far flatter than any single band suggested — 345 labels occur exactly once, only 199 occur five times or more, and the top 50 labels account for just 48.4% of instances.

| Instrument | Labels | Instances covered | Share |
|---|---|---|---|
| `TAG_MIGRATION` **as shipped today** | 9 | **660** | **13.5%** |
| Shipped 9 + the 22 mappings proposed in the 2026-08-01 observations | 31 | 1,365 | 27.9% |
| A curated map over the top 50 labels | 50 | 2,370 | 48.4% |
| The remaining tail | 768 | 2,530 | 51.6% |

**The first row is the finding.** `TAG_MIGRATION` has covered `time`→`time-general` (204 live instances), `people`→`person` (129), `social`→`society` (73), `medical`/`medicine`→`health` (95), `transport`→`transportation` (52), `description`→`descriptive` (51), `animals`→`animal-general` (34) and `economy`→`economics` (22) since it shipped — and all 660 are still in the corpus. Meanwhile successive accuracy-review runs have been migrating 35–104 tags apiece by paid LLM review, re-deriving decisions the map already encodes. **A deterministic sweep of the nine mappings already in the repo is free, needs no judgment, and clears more instances than the last ten LLM runs combined.** It should run before any further map extension is debated.

**Where the residue sits settles the "reviewed ranges are clean" question**: 79 instances (1.6%) below the polish frontier, **2,290 (46.7%) inside 6739–23607 — the band accuracy-review has already swept** — and 2,531 (51.7%) above the un-reviewed frontier at 23608. Reviewer-driven migration leaves roughly as much behind in the ranges it covered as sits in the ranges it has never seen. The 2026-06-28 observation that a 10550–10715 review "migrated 64 but missed ~9" was not a local miss; it is the dictionary-wide rate. The deterministic sweep should therefore run over the **whole** corpus, not just ahead of the frontier.

**And the tail settles the 2026-07-28 fork** in favour of the second reading: with 818 labels and half the population outside the top 50, the mapped-sweep strategy has a natural ceiling near 50%. Extending the map past the top ~50 labels buys less per entry added, and what remains is not a rename problem — it is the curator taxonomy decision (which off-vocab labels join `VALID_SEMANTIC`, which map to a nearest in-list home, which are not semantic fields at all and get dropped). **Recommended sequencing: (1) sweep the shipped nine, dictionary-wide; (2) extend the map to the top ~50 labels and sweep again; (3) escalate the ~2,500-instance tail as one taxonomy decision rather than 768 individual ones.** Steps 1 and 2 are `systemic-fix` work; step 3 is not Routine work at all.

**Update 2026-08-02 — step 2's map splits into two provably different classes, and `drop` is the correct default for one of them.** A 2026-08-02 accuracy-review run (23608–23907) built a migration map by hand, caught its own first draft producing wrong destinations, and reported the distinction:

- **Forced renames** — the destination is determined by the tag *name alone*, with no reference to the entry: `medicine`→`health`, `linguistics`→`language`, `animals`→`animal-general`, `transport`→`transportation`. These are the shipped nine plus their obvious siblings, and a sweep cannot get them wrong.
- **Context-dependent labels** — `academic`, `safety`, `environment`, `winter`, `conflict`, `industry`, `bureaucracy`, `department`, `statistics`, `innovation` — have **no entry-independent destination**. The run's first-draft map produced `education` for 立証 "proof", `nature` for 焼却炉 "incinerator", `time-season` for ゲレンデ "ski slope", and `business` for 溶鉱炉 "blast furnace": four wrong claims from four plausible-looking map rows.

**The asymmetry that resolves it: dropping an off-vocabulary tag never adds a false claim, while migrating one can.** An entry that loses `environment` is under-tagged; an entry that gains `nature` is wrong. So for the context-dependent class the safe default is **drop**, and migration should be reserved for the cases where the destination is forced. That converts most of step 3's "taxonomy decision" into a mechanical drop plus a much smaller list of labels genuinely worth admitting to `VALID_SEMANTIC` — and it means step 2 should extend the map only with forced renames, not with the top 50 by frequency.

### Update 2026-08-03 — the drop-vs-migrate rule survived its first deliberate test

The 2026-08-03 accuracy-review run (24501–25100) applied the asymmetry above as a *procedure*
rather than a principle: it split the block's 138 off-vocabulary labels into **forced renames**
(destination follows from the label itself) and **context-dependent labels** (destination depends
on the entry), inspected every entry in the second class before choosing, and then **re-audited
the finished diff against the entries**.

The audit caught **8 wrong or weak destinations that the generic map had produced** — the clearest
being `place`→`building`, which turned **パリ** into a building — plus `environment`→`nature` on
焼却場 (an incinerator plant is not about nature) and `material`→`nature` on 銅板. **Every one was
in the context-dependent class; zero forced renames were wrong.** The rule is therefore promoted
from a proposal to a procedure:

> Run forced renames mechanically. For context-dependent labels, either read the entry or drop the
> tag — and **audit the resulting diff against the headwords**, because reading the entry *list* is
> not the same as reading the *diff*.

Two further measurements from the same window:

- **Density is holding at 40–53% for a third consecutive high-ID block** (23908–24500: 315/592
  entries, 374 occurrences over 142 labels; 24501–25100: 246/600 entries over 138 labels). The
  *shape* is what changed: **106 of the 138 labels occur once or twice**, so plural/synonym
  variants (`arts`, `people`, `transport`, `tools`) are now a minority of label *types* even
  though they remain most of the *occurrences*. A frequency-ranked migration map hits diminishing
  returns fast; the residue is all one-off context-dependent labels — which is precisely the class
  the rule above says to drop rather than map.
- **A `--dimensions tags` pass over freshly-migrated entries is an independent check, not a
  redundant one.** The external reviewer caught one of the same run's own migrations (`math`→
  `number` on 直方体 and 交点, both geometry rather than arithmetic) — the same defect class the
  self-audit exists to catch, found from the opposite direction, at ~$0.0004/entry.

**Named residue**: the off-vocabulary tag `interrogative` survives on exactly three entries — 00534 誰, 00543 どう, 23898 でしょうか — after a 2026-08-02 polish run migrated 00536 いつ to `grammatical`. Too small for its own item; fold into the next systemic-fix or accuracy-review pass. Recorded so it is not rediscovered a fourth time.

**Update 2026-08-04 — a fourth consecutive high-ID block at the same density.** The 2026-08-04
accuracy-review over 25101–25600 found **201 of 495 entries (41%) carrying tags outside
`VALID_SEMANTIC`** (top labels: `body` 19, `time` 14, `transport` 8, `people` 7, `material` 7), of
which the reviewer's `tags` dimension independently caught ~136. The run recorded the reading that
matters for adjudication policy: **the standing ">20% of entries flagged means reviewer noise"
heuristic misfires on this cohort**, because the underlying rate really is ~40%. Off-vocabulary
density is now measured at 40–53% across four consecutive 500-entry blocks from 23908 to 25600,
which makes it a property of the high-ID creation cohort rather than of any one batch — and
strengthens the case for tooling item 67 (a per-range density report), since the CI ratchet can
gate but cannot target.

**Update 2026-08-05 — a fifth consecutive block, and the first sign of the density falling.** The
2026-08-04 accuracy-review measured **197 of ~600 entries (33%)** off-vocabulary in 25601–26200
(`time`, `body`, `people`, `social`, `emotions`, `place`, `transport`, `household`) and migrated 45
of them in range. The label families are the same ones the four earlier blocks named, so this is
the same cohort continuing rather than a new one; the datum worth keeping is that 33% is the first
reading below the 40–53% band, on the highest block measured so far. The repo-wide baseline still
counts **2,808 affected entries**, and the arithmetic that has driven this item for three harvests
is unchanged: a per-range paid pass migrates tens per run against a residue in the thousands, so
the **step-1 sweep of the nine mappings already shipped in `TAG_MIGRATION`** — still unrun after
four harvests recommending it — remains the highest-yield action available and needs no new
detector, no budget, and no curator decision.

**Update 2026-08-06 — the whole population counted, and the map-extension premise sized against
it.** The 2026-08-06 accuracy-review proposed extending `TAG_MIGRATION` with "~55 more 1:1
mappings" to make "the remaining ~2,500 baselined entries batch-fixable". The full repo scan that
proposal implies had never been run, so this harvest ran it. Current state of the whole queue:

| measure | value |
|---|---|
| entries carrying ≥1 off-list semantic tag | **2,530** (was 2,808 at the last harvest — the lane *is* converging) |
| off-list tag instances | **3,208** |
| distinct off-list tag *names* | **687** |
| instances the 9 shipped `TAG_MIGRATION` mappings already cover | **364 (11.3%)** |
| names occurring ≤2 times | 438 names / 574 instances |

Four results, in the order they change decisions:

1. **The standing step-1 sweep is a 364-instance job, not a thousands-instance one.** Five
   harvests have recommended sweeping the nine already-shipped mappings without anyone counting
   what they cover. They cover 364 instances — one bounded systemic-fix batch, verifiable per
   entry, needing no detector, no budget and no curator decision. The reason to do it is no
   longer "highest-yield"; it is that it is *small*, and it has been deferred five times on the
   assumption that it was not.
2. **"~55 more mappings" buys 40.6%, not the remainder.** Mapping the 55 highest-frequency
   unmapped names covers 1,304 of 3,208 instances and leaves **1,540 instances across 623
   names**. The distribution is the reason: the top 20 names carry 28.3% of the mass, the top 100
   carry 62.4%, and you need 249 names for 82%. A frequency-ranked map cannot finish this queue;
   it can only decapitate it.
3. **The head is not spelling variants — that family is 6% of the mass.** Applying every
   mechanical rule that could generate a mapping without judgment (depluralize, strip a
   `-qualifier` suffix, add `-general`, normalize separators/case) yields exactly **78 names /
   196 instances (6.1%)** — `arts`→`art`, `tools`→`tool`, `food-drink`/`food-cooking`→`food`,
   `emotion-feeling`→`emotion`, `daily life`/`daily_life`→`daily-life`. Everything above them in
   the ranking requires a decision.
4. **What the head actually is, is the taxonomy gap this backlog already named from the other
   direction.** The ten largest unmapped names after `body`(85) are `place`(54), `location`(50),
   `object`(46), `state`(32), `quality`(32), `manner`(30), `degree`(30), `document`(20),
   `position`(14), `objects`(14) — **322 instances in the spatial/positional/metadata region
   `VALID_SEMANTIC` has no slot for**. [P13](#priority-13-overuse-of-general-as-sole-semantic-tag)'s
   2026-07-30 update reached the same seven strings (`location, place, position, object, space,
   status, document`) from the *reviewer* side and concluded the model was answering honestly
   about a gap in the list. This count confirms it from the *corpus* side and adds the number:
   the gap is not a reviewer artifact, it is the single largest identifiable block of this
   migration queue, and no mapping work can touch it until the curator answers the taxonomy
   question.

**Prioritization datum, new here**: of the 2,530 affected entries, **1,121 carry off-list tags
*and nothing else*** — they have zero valid semantic tags today, so they are functionally
untagged for search and browse — while 1,409 already carry a valid tag alongside the off-list one.
The two halves are not equally urgent: the migration changes user-visible behaviour for the 1,121
and is bookkeeping for the 1,409. If this queue is ever worked by priority rather than by ID
range, that is the split to use.

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

### Update 2026-08-04 — measured, and the "display-only, no information lost" premise is wrong for 71 entries

A 2026-08-03 polish run re-filed this item ("`part_of_speech` has no house style … candidate for a
mechanical normalization pass driven by `metadata.tags.pos`"), so the 2026-08-04 wiki harvest
measured it. The scale first: **401 distinct values across 30,187 entries**, and the disagreement
is *within* categories, not between them —

| `pos` tag set | Entries | Distinct spellings | Top spellings |
|---|---|---|---|
| `noun` + `verb-suru` | 4,033 | 39 | `noun, suru verb` 1,206 · `noun` 604 · `noun, verb (suru)` 381 · `noun, suru-verb` 331 |
| `verb-godan` | 1,720 | 26 | `verb (godan)` 724 · `godan verb` 405 · `verb-godan` 180 · `verb` 88 |
| `verb-ichidan` | 859 | 15 | `verb (ichidan)` 376 · `ichidan verb` 173 · `verb-ichidan` 102 |
| `adjective-na` | 849 | 8 | `na-adjective` 495 · `adjective-na` 157 · `adjective` 88 · `な-adjective` 19 |
| `adjective-na` + `noun` | 716 | 30 | `noun, na-adjective` 157 · `na-adjective, noun` 155 · `noun / na-adjective` 82 |
| `adjective-no` + `noun` | 415 | 19 | `noun` 155 · `noun, no-adjective` 123 |

**6,573 entries (21.8%) deviate from their own tag set's plurality spelling.** Separator (`,` vs
`/` vs `;`), affix order (`noun, na-adjective` vs `na-adjective, noun`) and naming convention
(`verb-godan` vs `godan verb` vs `verb (godan)`) vary independently — which is how one category
acquires 39 spellings.

**The part that changes the plan.** This item and tooling item 29 both assert the transform is
"deterministic" and "display-only" because `tags.pos` encodes the category unambiguously. It does
not encode everything the free text says. Regenerating the field from tags would silently delete:

| Information only in the free text | Entries | Structured home that already exists |
|---|---|---|
| transitivity (`godan verb, transitive`) | 486 stated · **50 with no `tags.transitivity`** | `metadata.tags.transitivity` (3,230 entries use it) |
| proverb | 18 stated · **8 without the tag** | `semantic: proverb` (in `VALID_SEMANTIC`) |
| idiom / four-character idiom | 18 stated · **13 without the tag** | `semantic: idiom` (in `VALID_SEMANTIC`) |
| humble / slang | 2 | `politeness` / `style` |
| "verb phrase" (`expression, verb phrase`) | 19 | **none** |

So the field is the *sole* record of something for **71 entries** — all with a structured
destination — plus **19** whose "verb phrase" qualifier has no home in the schema at all.

**This inverts the sequencing.** The first step is not the normalizer, it is a **backfill**, and
the backfill is worth doing whether or not the sweep ever happens: it adds 50 machine-readable
transitivity tags (which `find_missing_transitivity.py` reports as missing today), 8 `proverb` and
13 `idiom` tags that currently exist only as English prose no query can reach. Afterwards the
regeneration is lossless by construction for 30,168 of 30,187 entries, and the residue is a
one-line curator decision (keep the qualifier on those 19, or add a `verb-phrase` pos tag).

The normalizer itself stays blocked on the house-style choice — `verb (godan)` is the plurality,
`verb-godan` matches `tags.pos` and the CLAUDE.md convention. The **backfill is batch-ready and
carries no style question**: queue item `pos-freetext-transitivity-backfill`.

The generalisable point, and the reason this update exists: *"regenerate a derived field from its
source" is only safe once you have checked that the field really is derived.* Here 99.8% of it was
and 0.2% was not, and the 0.2% is recoverable rather than fatal — but only if someone counts first.

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

**"Do not sweep before the gate exists" was right, and both shipped together** — see [Tooling 11](tooling-backlog.md#11-inline-link-target-id-resolution-gate-in-validatepy-or-pre-commitci) for why the gate needed wiring rather than writing (the check existed; three of four CLI paths never called it). Because the corpus reached 0 in the same run, the gate is an absolute error rather than the ratchet this item assumed, so no baseline file is needed. The follow-on population — links that resolve but not to their own base form, 418 after normalization — is filed as `link-target-baseform-disagreement`. **RESOLVED 2026-08-06: queue 0, gate armed** (99 verified same-word pairs allowlisted; see the closeout batch below). Was 101 links / 75 entries, after the 2026-07-31 compound-homophone batch (87 links), the 2026-08-01 kanji-variant-verb batch (90 links, 18 base-form families), the 2026-08-03 noun-homophone batch (51 links / 36 entries, 34 decision families), the 2026-08-04 reading-match wrong-word batch (39 links / 33 entries, 31 decision families), the 2026-08-05 judgment-tail batch (30 links / 24 entries, 19 decision families, which also cleared the ambiguous bucket), and the 2026-08-06 batch that took everything outside the benign family (13 links / 12 entries, 13 decision families). The 2026-08-03 batch added a triage step worth reusing: **split the queue by whether the proposal's reading matches the surface furigana before adjudicating**. Reading-match findings are near-mechanical wrong-word repairs (鮭→酒, 麺→面, 鐘→金, 街→町, 者→物, 級/急→九); reading-MISMATCH findings are where the judgment lives — some resolve to an entry under the surface's own reading (者しゃ→`04662_sha`, an off-by-two ID slip from `04660_sha` 〜社), some to the same-kanji entry as the same morpheme (探究心 の 心しん→`01321_kokoro`, 20畳 の 畳じょう→`02224_tatami`), some have no correct target at all and are honestly repaired to `noentry` (性質上 の 〜上 じょう, 温帯 の 〜帯 たい — both now candidates), and some are benign and must be left (下/元, 本/元, 球/玉, 敵/仇, and お得 where the target is right and only the link's base label is loose). What is left is the benign orthographic family (頃→〜ころ 24, 上げる→あげる 18, 捩じる 8, 付ける→つける 7, 通り→どおり 5, 焼きたて 4, 霞む 4, いい/良い 4, 羽 3, 被る 3, 追いかける 3) that must be left alone — and after the 2026-08-06 batch that is *all* that is left.

**2026-08-04 batch (reading-match wrong-word class).** The batch-3 reading-match split kept paying: every finding whose *proposal's* reading matched the surface furigana and whose declared headword was a *different word* under the same reading was a near-mechanical 1:1 repair, and 31 such families cleared 39 links in one run — 参加する/酸化, クリーム/クレーム, オタク/お宅, 深い/薄い, 離す/話す, 掘る/彫る, 囲う/下降, 効く/聞く, 利く/効く, 嫌/否, 辺り/当たり, 解消する/快勝, 込む/混む, 切る/着る, 変える/帰る, 返る/帰る, 冷める/覚める, 応える/答える, 載せる/乗せる, 熱い/暑い, 温かい/暖かい, 締める/閉める, 充てる/当てる, 務める/勤める, 生ける/いける, 何か/何, 上げる/上がる, 長い/長〜. Two sub-families are worth naming because they are not homophone confusions at all: **transitive/intransitive slips** (上げる linked to 上がる, 返る linked to 帰る, 取れる linked to 取る) and **noun-vs-suru-verb pairs** — 入院 and 退院 were each linked to the *other* entry's する form, so both entries repaired to the bare-noun entries 02091/02090. The mirror-image family also firmed up: when the surface reading matches the **declared** entry and the proposal's reading differs, the proposal is wrong and the finding is benign — 様→01114_you (base spelled with the kanji of よう), 臭い→00874_nioi (臭い and 匂い are spellings of one におい), 羽→03696_hane (羽根 is the same word; the proposal is the bird counter 〜羽). Reject those without reading the sentence.

**2026-08-06 batch (everything outside the benign family — and what the benign family actually is).** 13 decision families, 13 links / 12 entries, 114 → 101. Two classes. The first is new: a **bound suffix mislinked to its free-standing homophone**. Both surviving 的 findings (`00445` 開放的, `02627` 外交的な) pointed the adjectival suffix 〜的 at `03546_teki` 敵 "enemy" instead of the suffix entry `09839_teki`. The detector's proposal (`19356_mato` 的 まと) was correctly *ignored* — its reading does not match the surface furigana てき — which is the batch-3 reading filter doing its job in the negative direction: the filter rejects a wrong proposal as readily as it confirms a right one, and the correct target then has to be found by search. This is the mirror image of the 者→`04662_sha` and 〜軒/件 repairs in batch 3, where the *base* was the free word and the target was the suffix. A deterministic check for it — links whose base is a single kanji that also heads a `〜X` suffix entry but whose target is the free-standing noun — would find the class dictionary-wide.

The second class is the familiar kanji-variant one, repaired by the batch-2 rule (link to the entry matching the *written surface*): 観る→`22793` (from 見る, 映画を観る), 生む→`29531` (from 産む, 電流を生む "generate"), 硬い→`01116` (from 固い, 表情が硬い), 暖まる→`01856` (from 温まる), 造る→`17751` (from 作る), 放す→`29986` (from 離す, in 手放す's own etymology note), and the entire 差す family →`17637` (from 挿す ×2, 指す, 射す). Plus one base-label repair: `05653_gacchiri` had `⟦{作|つく}り→造る：00481⟧` — right target, wrong label — relabelled 作る, the third instance of that pattern after お得 (batch 3) and 一本/一個 (batch 5).

**The finding that redirects this item, though, is about what remains.** The ~79 surviving benign findings are not link defects at all; they are mostly a symptom of **near-duplicate entry pairs** — one word carrying two entries under two okurigana spellings. Six were identified this run: `09160` 控え目 / `17234` 控えめ, `04699` 見積り / `05153` 見積もり, `08344` 焼き立て / `16735` 焼きたて, `03937` 捻る / `04474` 捩じる, `04628` 追い掛ける / `16734` 追いかける, `02586` 巨大 / `25544` 巨大な. Every link into either member of a pair reports forever, because both readings of "correct" are correct. **So the way to drain the rest of this queue is `consolidate_entries.md`, not more link adjudication** — and the `--count` ratchet this item has been aiming at should be armed at the post-consolidation floor rather than at 0. One detector improvement would help immediately: accept a **na-adjective normalization** (strip a trailing な from the base before the headword-identity test), exactly parallel to the existing suru-noun rule, which retires the 巨大な→巨大 class outright.

**2026-08-05 batch (the judgment tail, and the "ambiguous" bucket was never curator work).** The 13 findings the detector marks `ambiguous` (>1 lookup candidate) had been reserved for the curator by four consecutive batches. All 13 were decidable, and the rule is one line: **the surface furigana names the reading, and the reading selects one candidate outright.** `⟦{後|あと}→後：02174_ato⟧` is ambiguous only if you ignore あと — with it, `09580_ato` "after, later" is the sole fit and `02174_ato` 跡 "trace, mark" is plainly the wrong word. Same for 分 ぶん→`26216_bun` (was 文), 船 せん→`09875_sen` (was 千), 方 かた→`10665_kata` (was 肩), 館 かん→`17308_kan` (was 缶). **Lookup ambiguity is not decision ambiguity**, and an `ambiguous` bucket should be triaged, not deferred — the reading-match split from batch 3 dissolves most of it. One genuinely undecidable finding remains (05020_youtsuu とき→`10077_toki`), and it is not a link error at all: it is an artifact of `02918_toki` 時 and `10077_toki` とき being near-duplicate entries for the same word, now logged as a consolidation candidate.

The rest of the batch cleared the wrong-word singletons the earlier class-based sweeps left behind — 要る→`09589_iru` (was いる "to exist"), 欠ける→`13167_kakeru` (was かける "to hang"), 利く→`11845_kiku` (was 効く), 蕎麦→`14329_soba` (was そば "beside"), 湧く→`13321_waku_welling` (was 沸く), 痛める→`13613_itameru` (was 傷める), 修行→`05522_shugyou` (was 修業) — plus a family not seen before: **grammatical patterns linked to their component word**. `てしまう` pointed at 仕舞う, `につれて` at 連れて, `のように` at ように "so that", and `楽しみにする` at the noun 楽しみ; each has a dedicated pattern entry (`03102_teshimau`, `28400_nitsurete`, `30291_noyouni`, `26825_tanoshiminisuru`) and each was relinked. A na-adjective attributive copula was mislabelled as a particle (失礼**な**態度 → `09472_no` の, repaired to `09497_na`). Two findings were **base-label** repairs rather than retargets: 04959_dango's counter links wrapped the surfaces 一本/一個 but declared the bases 〜本/〜個, so the labels were corrected to match the (already correct) targets — the same shape as the お得 case in batch 3, and the general rule is *check which half of the link is wrong before repairing the other half*.

Three left alone with reasons worth recording, because each is a trap: 00233_kingyo すくい→`09994_sukuu` (金魚すくい is scooping — the *proposal* `12884_sukui` 救い "salvation" is the error, not the link); 05020_youtsuu, above; and 04230_uchiakeru, where the notes derive 打ち明ける from 打つ + 明ける and gloss 明ける as "(to open)" — **neither** entry fits (`00563_akeru` is 開ける "to open", `21288_akeru` is 明ける "to dawn; to end a period"), so the etymology note itself needs a curator decision and the link was not touched. 144 → 114; dead targets still 0; the §4 furigana screen over the 24 changed entries returned 0 flags. What remains is now almost purely the benign orthographic family that must never be swept (頃 24, 上げる 18, 捩じる 8, 付ける 7, 通り 5, 焼きたて 4, 霞む 4, いい/良い 4, 羽 3, 被る 3, 追いかける 3) plus a thin tail of same-word spelling variants needing sense judgment rather than repair (造る/作る, 観る/見る, 硬い/固い, 暖まる/温まる, 生む/産む, 差す/挿す・指す・射す).

**2026-08-06 closeout batch (RESOLVED — the queue is 0 and the ratchet is armed).** The two cases batches 4 and 5 deferred as "neither entry fits" both turned out to be decidable, and they were the last findings link repair could touch. `03654_yutaka`'s 石油や天然ガスがたくさん{採|と}れる linked 採れる to `00565_toru` 取る; the right target is `20862_toru` 採る, whose sense 1 is literally "to pick or gather natural things like plants, mushrooms, shellfish, **or minerals** from their environment" — the deferral had only ever compared 取る against the detector's proposal `02376_toreru` "to come off" and stopped at "neither fits" without searching for a third entry. **When both the declared target and the proposal are wrong, the answer is usually a fourth entry, not a `noentry`.** `04230_uchiakeru`'s etymology note (打つ + 明ける "to open") was a **base-label** repair, the fourth after お得, 一本/一個, and 作る/造る: the target `00563_akeru` 開ける is semantically right — the note glosses it "(to open)" and `21288_akeru` "to dawn; to end a period" does not fit — and only the label, written 明ける to match the compound's kanji, disagreed.

That emptied the queue of everything a link change can fix, which forced the question this item had deferred for six batches: **what do you do with 99 findings that are all correct?** Family by family they are one word reached under a different spelling — 頃/〜ころ, 上げる/あげる, 羽/羽根, いい/良い, 下・本/元, 敵/仇, 球/玉, 臭い/匂い — and string comparison cannot see it. Three answers were available and two are wrong. Leaving them reported means every future batch re-triages the same 99 (this run would have been the seventh). Arming a **count ratchet at 99** looks equivalent and is not: the benign families *grow with normal entry creation* — every new entry that links 頃 adds one — so the gate would have failed ordinary new-entry PRs while still tolerating a real wrong-word link that displaced an allowlisted one. **A ratchet on a population that legitimately grows is not a ratchet.** So the pairs are now enumerated in `build/data/link_baseform_allowlist.json`, each with a written reason and a class, accepted as a fourth normalization path in the detector, and the gate is armed absolutely at 0 in `validate.yml` — the same shape the dead-target gate reached in Priority 27, and for the same reason: the corpus was driven to zero first.

Two details make it a real gate rather than a comfortable one. It was **negative-tested** — dropping the 頃 pair from the allowlist reproduces a 24-link `FAIL`, so the green is evidence, not a no-op — and `--no-allowlist` still prints the raw 99, so nothing was hidden, only classified. The allowlist's own discipline is the load-bearing part: a pair belongs there **only** when base and target are the same word, never to silence a link that points somewhere else, and the failure message says so at the moment someone is tempted.

Of the 99, **7 families are a different problem wearing this one's clothes**: 捻る/捩じる, 焼き立て/焼きたて, 翳む/霞む, 追い掛ける/追いかける, 控え目/控えめ, 見積り/見積もり, and the とき pair `02918`/`10077` are **near-duplicate entries**, where both targets are defensible because the word is held twice. No amount of link work converges them. They are tagged `near-duplicate-pair` in the allowlist file and filed as `entry-pair-consolidation` (needs-decision — merging touches live URLs and is the curator's call). Deferring them now costs nothing, because the allowlist keeps them out of the CI gate. **The general lesson: when a detector's queue stops shrinking, check whether the residue is a different defect class before spending another batch on it.**


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

### Update 2026-08-02 — provenance split: 12% were *wrong when written*, not stale, and that subclass is closed

A 2026-08-02 polish run found `01004_tsu` marking 一二三四五六八九 as `noentry` when **all eight
are basic-tier entries that predate the linking pass**, and proposed a detector for "`noentry`
false positives" as distinct from stale markers. The harvest measured the distinction rather than
filing a second item, by comparing each resolving marker's target `created` date against the
`created` date of the entry the marker sits in. A target that already existed before the source
entry was even written cannot have been correct when the link was written.

| Class | Markers | Entries | Reading |
|---|---|---|---|
| Target **predates** the source entry | **447** | 317 | provably wrong when written |
| Target **postdates** the source entry | 3,362 | 1,944 | genuinely went stale |
| Do not resolve at all | 3,515 | — | still correct (or unlinkable — see the residue section) |

**447 is a lower bound**, not an estimate: a marker written during a *later* polish pass against a
target created after the source entry is counted as "stale" here even though it was also wrong
when written. The true wrong-when-written count is somewhere between 447 and 3,809; what the
measurement establishes is the floor and, more usefully, the shape.

**The wrong-when-written subclass is bounded and finished.** By ID band: 12 in 00000–00999, 13,
35, 78, 97, 45, and 21 up to 06999 — and **zero above 07000**, because above the polish frontier
there are no inline links at all. It was produced by the January 2026 linking pass over the
earliest entries and cannot grow, which is the opposite of the stale class (85% pointing at bands
26000+, growing with every `new-entries` run).

**301 of the 447 are full-headword matches with exactly one candidate** — the same A1/A2
mechanical criterion as the main batch. The remaining 146 are the reading-only and ambiguous
homograph traps (たち → `01551_tachi`, つる → `01236_tsuru`, うち → `01328_uchi`) and must not
ride along.

The failure mode the observing run guessed is visible in the samples: the linking session looked
up the **surface form as it appeared in the sentence** rather than the dictionary form — 形 →
`02193_katachi`, 間 → `00914_aida`, 家 → `00612_ie`, 本 → `00111_hon`, 都 → `03747_miyako`. These
are common words whose entries existed from the first week of the project.

**Consequence for the sweep: none.** The proposed false-positive detector is this item's detector
with one extra column, and the fix is the identical token substitution. Do not file it separately;
the provenance column is worth emitting because a wrong-when-written marker needs no "does the
sense still match" check — the entry was there all along. `01004_tsu` was fixed by the observing
run and carries no `noentry` markers today.

### Update 2026-08-03 — the number/date cluster, and the reading test that finds the rest

A 2026-08-02 polish run hand-fixed **20 entries in the number/date cluster**, and the breakdown
shows this item and its neighbours are one family seen from three angles:

- `{十|とお}` linked to `00708_juu` (じゅう) when `28376_too` is the とお entry — 8 entries
- `{五日|いつか}` marked `noentry` although `28460_itsuka` exists — 6 entries (this item)
- `{間|かん}` split between `noentry` and `00914_aida` (あいだ) when the duration suffix
  `28469_kan` is correct — 10 entries

Only the middle group is a stale `noentry`; the other two are **live links pointing at an entry
with a different reading**. That second class now has a measured detector spec — 998 links where
the surface reading is exactly some *other* entry's headword reading — filed as
[Tooling 66](tooling-backlog.md#66-detector-an-inline-link-whose-surface-reading-disagrees-with-its-target-entrys-reading).
Run the two scans together when this item is swept: they share the cluster, and fixing only the
`noentry` half leaves the wrong-target half looking correct.

### Update 2026-08-08 — detector built, 999 pairs swept, and the "mechanical" claim is wrong for short bases

The 2026-08-08 `systemic-fix` run built the standing detector this item had been asking for —
**`build/check_stale_noentry.py`** (read-only; classes A1/A2/A3/B/C/D plus a new R, a
`wrong_when_written` column, `--mechanical`, `--json`) — and swept the safe half of the batch:
**999 pairs / 1,129 instances across 739 entries**. An independent model checked a stratified
60-pair sample of the applied fixes and flagged none; the same checker, run as a control over
known-bad class-R cases, did flag them, so the clean result is informative rather than
agreeable.

**What was applied**: every mechanical pair whose base is **4+ characters** (903 pairs — a
45-pair spot check across the whole ID span was clean), plus the 2–3 character pairs below entry
00443 that were hand-read with context.

**What the sweep disproved.** This page predicted precision "near 1.0" for all of A1+A2 because
"the evidence needed to accept each fix is entirely inside the link". That holds for long
compounds and fails for short bases. Hand review of 110 short-base pairs found ~4% false
positives in three families:

| Family | Example | Caught by |
|---|---|---|
| Polysemous loanword in another sense | baseball ⟦フライ⟧ → `11124_furai` *deep-fried food* | judgment only |
| Abbreviation inside a compound | ⟦パン⟧ in 海パン (swim trunks) → `00553_pan` *bread* | judgment only |
| Homograph read differently | ⟦{臭\|にお}い⟧ → `01133_kusai` (くさい) | **detector class R** |
| Bound, rendaku'd compound element | ⟦{張\|ば}る⟧ in 形式張る → `12583_haru` (はる) | **detector class R** |

The last two are now mechanical: class **R** compares the marker's own furigana against the
target entry's reading (with prefix/honorific/suru-verb tolerances) and refuses the substitution
when they contradict. The first two are invisible to any string test, so **the remaining 1,580
pairs — all of them 2–3 character bases — are `verify: per-entry`, not mechanical.** The item's
`fix_type` in `backlog-queue.json` was changed accordingly.

**Free by-product**: class R is a 40-pair queue of *genuine furigana errors in source entries*,
found by an inline-link scan rather than a furigana instrument — 来春/らいはる (らいしゅん),
農作物/のうさくもつ (のうさくぶつ), 墓石/はかいし (ぼせき), 完全試合/かんぜんしあい (かんぜんじあい),
白和え/しろあえ (しらあえ), 部屋干し/へやほし (へやぼし), 言い及ぶ written {言|い}{及|およ}ぶ.
This is the same "a field outside examples/notes falls through every net" shape as P36: the
furigana screener reads example *text*, and these errors sit inside link surfaces.

Remaining after the sweep: 1,580 mechanical-class pairs (1,827 instances), 406 B, 352 C, 42 D,
40 R, 3,082 markers that still do not resolve.

**2026-08-09 systemic-fix run** — first per-entry short-base batch. 180 A1/A2 pairs
(196 instances, 124 entries, IDs 00443–01435) were each read in context before substitution
and applied; the queue is now **1,423 pairs / 1,658 instances**. Sweeping in entry-ID order
turned out to be the right unit of work: consecutive entries repeat the same families
(counter compounds 六千/八百/三十人, day-of-month readings 十四日/十五日, direction and
compass compounds 北側/西日本, katakana loanwords ウール/ミトン/コンポ), so the context read is
cheap once the family is established. **Zero polysemy false positives in 180 pairs** — the
one candidate the batch flagged for a closer look, レア in a steak-doneness sentence, turned
out to be correct because `11251_rea` carries an explicit second sense for doneness. That is
consistent with the ~4% rate measured on the 2026-08-08 hand sample, but suggests the rate is
lower once class R has removed the reading contradictions: the surviving trap is narrow
(polysemous katakana loanwords and abbreviations inside compounds), not diffuse. Resume at
the lowest remaining `entry_id` — everything below 01436 is now swept for A1+A2.

**2026-08-11 systemic-fix run** — second per-entry short-base batch. 178 A1/A2 pairs
(198 instances, 134 entries, IDs 01440–02229) were read in context and applied; the queue is
now **1,256 pairs / 1,471 instances**. Everything below **02230** is swept for A1+A2. The
ID-order finding held: this band's repeating families were faculty compounds (商学部/薬学部/
農学部), style and origin suffixes (日本式/西洋式, 日本製/中国製/金属製), city and ward names
(横浜/札幌/特別区), and 猿/竹/貝 compound clusters, each cheap to judge once the family was
established.

**A new false-positive family: proper names whose target entry carries only the common-noun
sense.** The batch's only two rejections were both in `01440_shinbun`'s newspaper list —
⟦朝日⟧ in 朝日新聞 resolves to `23495_asahi` ("morning sun") and ⟦毎日⟧ in 毎日新聞 to
`00729_mainichi` ("every day"). Each newspaper is named after the word, so the link is
etymologically true and pragmatically wrong: the reader clicking it lands on a sense the
sentence is not using. This family is invisible to class R because the readings agree, and it
is distinct from the polysemous-loanword (フライ) and abbreviation (海パン) families already
documented. It does **not** generalise to place names used as place names — 上野 in 上野動物園
→ `28394_ueno`, and 横浜/札幌 in a list of cities, were all applied without hesitation, because
there the target entry *is* the proper noun. The discriminator is whether the target entry
covers the proper-noun sense, not whether the surface is a name.

Running false-positive rate across the 358 hand-verified short-base pairs (2026-08-09 plus
2026-08-11): **~0.6%** — low, but not zero, which is what keeps this item `verify: per-entry`
rather than mechanical.

**2026-08-12 systemic-fix run** — third per-entry short-base batch, and the first fully clean
one. 180 A1/A2 pairs (214 instances, 147 entries, IDs 02232–03163) were read in a ±45-character
context window and applied, with **zero rejections**; the queue is now **1,101 pairs / 1,287
instances** and everything below **03164** is swept for A1+A2. The band was dominated by
families that are cheap to judge in bulk: date and counter words (十一日/十四日/七人/六人/二枚,
all resolving into the 30xxx counter entries created by recent new-entries runs), meat compounds
(羊肉/馬肉), surname examples inside phone-call and self-introduction entries (田中/山田/鈴木 →
`0952x`), place names used as places (成田/横浜/青森県), and grammar terminology (五段活用 →
`28275_godan`, whose entry covers the grammar sense alongside "fifth dan").

**Figurative compounds are not the proper-name family.** This band contained several markers
whose sentence uses the word metaphorically while the target entry defines it literally —
猫に小判 → `27868` (koban coin), 歩行者天国 → `27976` (heaven), 手玉に転がす → `28101`
(juggling ball), 早起きは三文の徳 → `28481` (three mon / a pittance). All were applied. The
discriminator against the 朝日新聞 family is whether the surface and the target are the *same
lexeme*: in 歩行者天国 the word really is 天国 used figuratively, and the entry is where a
learner should land; in 朝日新聞 the surface is a company name that merely contains the word.
One marginal apply is worth recording for future runs: ソフト飲料 → `01532_sofuto`, whose
sense 2 ("soft; not hard or firm") covers the "non-alcoholic" collocation only approximately.

Running false-positive rate across the 538 hand-verified short-base pairs (2026-08-09,
2026-08-11, 2026-08-12): **~0.4%**.

**2026-08-13 systemic-fix run** — fourth per-entry short-base batch, and the second consecutive
fully clean one. 181 A1/A2 pairs (221 instances, 131 entries, IDs 03167–03756) were read in a
±60-character context window and applied, with **zero rejections**; the queue is now **920 pairs
/ 1,070 instances** and everything below **03757** is swept for A1+A2.

Families that carried this band, all judgeable in bulk once one member is checked:

- **Suffix entries** — 〜家, 〜者, 〜的, 〜代, 〜戦 (→ `28339`, `04662`, `09839`, `28331`,
  `28346`). The marker's *surface* is the bare kanji (`{家|か}`) while its *base* carries the
  tilde, so a context dump that prints the base looks alarming (「思想〜家として」) when the
  rendered text is correct. Future runs should print the surface, not the base, when spot-checking
  these.
- **Compound sets inside one entry's notes** — needles (縫い針/編み針/注射針/釣り針), fences
  (板塀/石塀), multiple births (三つ子/四つ子/双生児), fields (重力場/電磁場).
- **Katakana loanwords whose target entry carries the needed sense as a *later* sense** —
  ベスト → `04681` (sense "best", not "vest"), カード → `03836` (sense 1 "identification,
  payment"), マネー, タイル, シニア. The polysemous-loanword family that produced the フライ
  false positive in 2026-08-08 is the same shape; what separates a keeper from a reject is
  whether the target entry actually *has* the sense, not whether the word is polysemous.

Two marginal applies recorded for future runs. **年寄り臭い → `01133_kusai`**: the target's
glosses cover only "smelly" and "suspicious", neither of which is the suffixal 〜くさい sense in
play — but the entry's notes carry a full "AS A SUFFIX (〜くさい)" section, so the reader does
land in the right place. Gloss text alone would have made this look like a reject; the notes
decided it. **焼き物 → `04974_yakimono`**: lead gloss is "grilled dish" with "pottery, ceramics"
as a later sense, applied on the same reasoning as 五段活用 → `28275`.

Running false-positive rate across the 719 hand-verified short-base pairs (2026-08-09,
2026-08-11, 2026-08-12, 2026-08-13): **~0.3%**. Two consecutive clean bands are now the strongest
argument yet that the per-entry read is cheap insurance rather than the thing finding the errors —
but the two rejections it did catch (朝日新聞, フライ) were both invisible to every mechanical
test, so the item stays `verify: per-entry`.

**2026-08-14 systemic-fix run** — fifth per-entry short-base batch, and the third consecutive
fully clean one. 174 A1/A2 pairs (210 instances, 141 entries, IDs 03757–04458) were read in a
±60-character context window and applied, with **zero rejections**; the queue is now **751 pairs
/ 865 instances** and everything below **04459** is swept for A1+A2.

The band's one genuinely new question was **compound-element markers** — a marker sitting on one
half of a lexicalized compound, pointing at that half's standalone entry. Three 込む pairs
(`04226` 持ち込む, `04229` 打ち込む, `04237` 押し込む, all in "formed from X + 込む (into)"
decomposition notes) target `00719_komu`, whose *gloss* is "to be crowded" — a different sense
from the compound suffix. Likewise `03916`'s 思い浮かぶ targets `10248_omoi` "thought, feeling",
the noun rather than the verb stem. Both were **applied** after opening the target entries:
`00719`'s notes carry an explicit `〜{込|こ}む (compound suffix: into)` line, and `10248`'s notes
list 思い出/思い入れ/思い込み under COMMON COMPOUNDS. This is the 年寄り臭い → `01133_kusai`
precedent again, and the rule it establishes is now firm enough to state generally: **for a
compound-element marker, the test is whether the target entry's notes document the compound role,
not whether its gloss expresses it.** Gloss-only screening would have rejected all four.

Families verified as groups in this band: morphological-decomposition notes in compound-verb
entries (取り除く = 取る + 除く, 振り返る = 振る + 返る, 再生 = 再〜 + 生), kendo and karate
equipment/scoring terms (小手/組み手/面), Tokyo district names used as places
(上野/浅草/新宿/成田), medical term lists (心不全/狭心症/心電図/弁膜症/見当識), plant and food
compounds (甘栗/毬栗/白桃/甘柿/芍薬/藤棚), and katakana loanwords whose target entry carries the
needed sense (ツボ "the right spot", オール "oar", エース "top player") — the same shape as the
2026-08-13 ベスト/カード family.

`04379` 銀杏 is worth recording as a clean demonstration of **class R doing its job**: the entry
documents both readings (いちょう the tree, ぎんなん the nut), and only the `{銀杏|ぎんなん}`
marker was linked to `28490_ginnan`. The homograph family that produced 2026-08-08's rejections
is now genuinely handled mechanically.

Running false-positive rate across the 893 hand-verified short-base pairs (2026-08-09 through
2026-08-14): **~0.2%**.

**2026-08-16 systemic-fix run** — sixth per-entry short-base batch. 177 A1/A2 pairs (212
instances, 120 entries, IDs 04459–04999) were read in a ±60-character context window; **176 were
applied and one was rejected**. The queue is now **602 pairs / 685 instances** and everything
below **05000** is swept for A1+A2 apart from the deliberate rejections.

The single rejection is the cleanest example of the polysemous-katakana family yet, and it points
at a mechanical improvement. `04562` (a home-security entry) has 二重⟦ロック⟧ "double lock", and
the only ロック entry is `08116_rokku`, glossed "rock (music); rock 'n' roll". Its notes end with
the sentence *"ロック as 'lock' (to lock something) is a different word with the same reading.
Context makes the meaning clear."* — i.e. **the target entry itself already declares the
homophone split in prose**. Class R catches contradictions between the marker's furigana and the
target's reading; it cannot catch a same-reading, different-word split. A cheap new class would
be: if the candidate target's notes match a pattern like *"X as 'Y' is a different word"*, demote
the pair out of the mechanical bucket. That would have caught this one without any semantic
judgment, and it is the same shape as the 2026-08-08 フライ/パン rejections.

Marginal applies worth recording, all resolved by opening the target entry rather than trusting
its gloss — the 2026-08-14 rule holding up:

- `04795` 連立⟦方程式⟧ "system of equations" → `14492_renritsu`, glossed "coalition; alliance
  (especially of political parties)". Applied because the entry's notes close with "Also used in
  mathematics: {連立|れんりつ}{方程式|ほうていしき} means simultaneous equations."
- `04703` 年少/年中/年長 as **kindergarten age-group names** → `29613_nenshou` / `29601_nenchou`,
  glossed only "young; junior in age" / "senior in age". Applied: `29613`'s collocation list has
  "{年少|ねんしょう}{組|ぐみ}: the younger group (e.g. in kindergarten)".
- `04969` おしゃれ{着|ぎ}⟦コース⟧ (a washing-machine cycle) → `10864_koosu`, whose SENSE 2 is
  program/set menu. Applied as the nearest documented sense; the appliance-setting use is a
  reasonable extension of it rather than a separate lexeme.
- `04468` {購読|こうどく}⟦{料|りょう}⟧ → `03797_ryoukin` 料金 and ⟦{購|こう}⟧ → `03057_kounyuu`
  購入: bare-kanji markers whose *base* is the full compound word, the same authoring shape as the
  〜{者|しゃ}/〜{家|か} suffix family.

Families verified as groups in this band: 〜{者|しゃ} and 〜{長|ちょう} title lists (`04662`,
`04665` — twelve and nine pairs respectively, each pointing at the entry for that exact title),
Japanese traditional-arts vocabulary (義太夫/長唄/虚無僧/室内楽), bird and plant name lists
(白鷺/青鷺/朱鷺, 唐松/杜若/花菖蒲), kitchen and appliance terms (七輪/蒸籠/中力粉/上新粉/天つゆ),
tax and finance compounds (税別/税率/税込み/年利/月給制/週給), and compound-decomposition notes
({仕|し}+{上|あ}げる, {出|で}る+{迎|むか}える, {申|もう}し+{込|こ}む).

Running false-positive rate across the 1,070 hand-verified short-base pairs (2026-08-09 through
2026-08-16): **~0.2%**.

**2026-08-20 systemic-fix run** — seventh per-entry short-base batch. 181 A1/A2 pairs (210
instances, 139 entries, IDs 05000–05857) were read in a ±70-character context window; **179 were
applied and two were rejected**. The queue is now **453 pairs / 511 instances** and everything
below **05858** is swept for A1+A2 apart from the deliberate rejections.

Both rejections belong to the family the 2026-08-16 run named, and its recurrence is the main
finding of this batch:

- `05053` ({彗星|すいせい}, comet) has an ANATOMY OF A COMET list whose middle item is ⟦コマ⟧ —
  the coma, the gas cloud around the nucleus. The only コマ entry is `11110_koma`, whose senses are
  the manga panel and the class period, and whose notes carry a HOMOPHONE NOTE listing {駒|こま}
  and {独楽|こま} — but not the astronomical term. The prose declares a homophone split; it simply
  does not enumerate this member of it.
- `05762` ({解除|かいじょ}) has ⟦ロック⟧{解除|かいじょ} "unlock" → `08116_rokku` — the *same pair*
  rejected at `04562` four days earlier, on the strength of the same sentence in the same target
  entry's notes.

That makes three occurrences of the family (フライ/パン 2026-08-08, ロック 2026-08-16,
コマ + ロック 2026-08-20) and the second time `08116_rokku` specifically has had to be rejected by
hand. The proposed detector class from 2026-08-16 — *if the candidate target's notes contain a
"X as 'Y' is a different word (with the same reading)" self-declaration, demote the pair out of
the mechanical bucket* — would have caught both of this batch's rejections with no semantic
judgment, and would have prevented the ロック repeat outright. It is now the highest-value
mechanical improvement available to this item.

One marginal apply is worth recording because it sits right on the boundary of the 2026-08-11
proper-name false-positive family and lands on the *other* side of it. `05387` ({紅葉|もみじ})
lists famous viewing spots, one of them ⟦{日光|にっこう}⟧ "Nikko in Tochigi Prefecture", and the
target `03515_nikkou` is glossed only "sunlight". Under the 朝日新聞/毎日新聞 rule that would be a
rejection — except that `03515`'s notes end with *"{日光|にっこう} is also a famous tourist
destination in Tochigi Prefecture, known for Tōshō-gū shrine. Context determines whether the word
refers to the place or sunlight."* The reader clicking the link therefore does land on the place
sense, so the 2026-08-14 rule (open the target entry rather than trusting its gloss) governs and
the pair was applied. The operative distinction for this family is **whether the target entry
documents the proper-noun sense at all**, not whether its lead gloss carries it. ヘビー級 →
`29473_hebii` (`05235`, `05515`) was applied on the same basis: same lexeme, no contradicting note.

Families verified as groups in this band: geometry vocabulary (六角形/内角/角錐/角柱/表面積),
arithmetic and math terms ({四則|しそく}演算, {円周率|えんしゅうりつ}, {対数|たいすう},
{線形|せんけい}代数), medical and anatomy lists (歯周病/胆汁/冠動脈/頸動脈/聴診/三角巾/ガーゼ),
wedding-ceremony types (神前式/教会式/人前式/釣書/余興), school-club and student-council terms
(運動部/文化部/児童会/学生会), milestone-birthday lists (古希/喜寿), banking terms
({当座|とうざ}/ATM/{手数|てすう}), place names used as places (新宿/広島/箱根/軽井沢/鎌倉/富山県/
伊豆諸島), and compound-element markers whose target entry documents that compound role
(しゃがみ⟦{込|こ}む⟧ → `00719_komu`, {寝返|ねがえ}り's ⟦{返|かえ}る⟧ → `29164_kaeru`,
{卸売|おろしうり}'s ⟦{卸|おろ}す⟧ → `02463_orosu`), matching the 2026-08-14 precedent.

Running false-positive rate across the 1,251 hand-verified short-base pairs (2026-08-09 through
2026-08-20): **~0.3%**.

## Priority 36: Headwords written as bare kanji with no furigana braces (248 entries)

**Source**: 2026-08-01 routine systemic-fix run, reporting one entry — `27889_ageru`'s headword
is `挙げる`, not `{挙|あ}げる`, and neither `validate.py` nor `find_missing_furigana.py` sees it.
**Measured dictionary-wide by the 2026-08-02 wiki harvest**, where it turned out to be a
250-fold larger and still-active defect.

`headword` is a free-form string with a sibling `reading` field. The schema constrains `reading`
to kana but places no constraint at all on `headword`, so both `{娯楽|ごらく}` and `娯楽`
validate. The corpus has effectively decided the question anyway:

| Headword form | Count | Share of kanji-bearing headwords |
|---|---|---|
| Furigana-braced | **25,773** | **99.05%** |
| Bare kanji | **248** | 0.95% |
| Kana-only (no kanji) | 4,087 | — |

The 248 are a defect, not a variant convention. `entry_renderer.py` builds the entry page's
`<h1>` through `process_headword_with_kanji_links(headword)`, which emits ruby from the braces —
so a bare headword renders **without ruby on the one line of the page a learner reads first**,
in a dictionary whose stated rule is that all kanji carry furigana.

**Why every instrument misses it.** `find_missing_furigana.py` scans examples and notes;
`validate.py` checks the schema, which has no headword pattern; the furigana screener reads
example text. The field is checked by nothing. This is the same shape as
[Tooling 47](tooling-backlog.md#47-cross-reference-headword-fields-are-invisible-to-every-furigana-instrument-7-confirmed-defects)
— a `headword` outside `examples`/`notes` falls through every net — and the two should be fixed
by one pass over "every field that can hold Japanese".

**Fix stratification** — the `reading` field supplies the answer, so most of the batch is
provably safe:

| Class | Count | Fix mode |
|---|---|---|
| Headword is **all kanji** → `{headword\|reading}` is correct by construction | **197** | mechanical |
| Headword **mixes kana and kanji** (okurigana, katakana, 送り仮名) — needs alignment | 51 | per-entry |

The mixed class is where judgment lives: `挙げる`/あげる must become `{挙|あ}げる` (not
`{挙げる|あげる}`), and `エネルギー資源`/えねるぎーしげん must brace only the kanji tail.
51 entries is one comfortable systemic-fix batch.

**This is an active creation-time defect, not a legacy tail.** By creation month: **126 in
2026-07, 83 in 2026-05, 19 in 2026-06, 13 in 2026-08** — and only 7 predate 2026. By ID the
population is a series of recent creation blocks (27882–27906, 28000–28044, 28157–28174,
29443–29462, 29762–29791, 29856–29875, 30029–30048, **30165–30221**, **30298–30317**), with the
newest block created this month. Sweeping the 248 without the check in
[Tooling 56](tooling-backlog.md#56-nothing-checks-that-a-headword-carries-furigana) refills it
within weeks; the check is the item that matters, and it is a two-line ratchet
(`bare kanji in headword` → error) because 99.05% of the corpus already passes.

**Related**: [Furigana Strategy](../topics/furigana-strategy.md),
[Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md),
[Tooling 47](tooling-backlog.md#47-cross-reference-headword-fields-are-invisible-to-every-furigana-instrument-7-confirmed-defects).

## Priority 38: Semantic tags disagree *within a closed lexical family* (tableware: 32 entries, 12 tag-sets)

**Source**: 2026-08-02 routine polish run, which standardised the four 皿 entries to `["tool"]`
after its §4 self-check flagged `food` on a plate, and noted that 茶碗, 箸 and コップ were left
drifting. **Measured across the whole tableware family by the 2026-08-02 wiki harvest.**

This is a different defect from [P20](#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration)
(tags outside `VALID_SEMANTIC`) and from [P11](#priority-11-batch-creation-semantic-tag-transportation-misapplied)
(tags describing the example rather than the headword). Here **every entry is individually
defensible and the set is collectively incoherent**: the tag depends on which run created the
entry, not on the word. 32 vessel/utensil entries carry **12 distinct tag-sets**, with no
plurality:

| Tag set | Entries | Examples |
|---|---|---|
| `["general"]` | 7 | グラス, コップ, フォーク, スプーン, 灰皿, 箸置き, マグカップ |
| `["tool"]` | 7 | 皿, お皿, 小皿, 大皿, 中皿, 急須, 鉢皿 |
| `["food"]` | 6 | 椀, 箸, 汁椀, 湯呑み, お椀, お箸 |
| `["culture","food"]` | 3 | 茶托, 抹茶碗, 吸い物椀 |
| nine further one-off sets | 9 | `["building","food"]` (菜箸), `["gardening","tools"]` (スコップ), `["consumption","tool"]` (割り箸), `["daily-life","food"]` (箸箱), `["food","objects"]` (薬味皿), `["food","tableware"]` (盛り皿), `["culture","tool"]` (取り皿), `["food","tool"]` (カトラリー), `["household","food"]` (飯椀) |

Two of the four large sets are *wrong on the project's own terms*: `food` on 箸 and 椀 describes
what the vessel holds, and `general` on コップ and スプーン is the sole-`general` placeholder
[P13](#priority-13-overuse-of-general-as-sole-semantic-tag) already covers. Five of the one-off sets use
off-vocabulary labels (`tableware`, `objects`, `tools` — note the plural against the valid
singular `tool` — `gardening`, `household`), so they are also P20 instances.

**Scope beyond tableware.** Tableware is the family that happened to be observed; nothing about
the mechanism is specific to it. The general shape is the one
[Tooling 57](tooling-backlog.md#57-check_semantic_clusterspy-has-no-closed-paradigm-symmetry-rule)
identified for cross-references: **where the members of a closed set are enumerable, disagreement
among them is mechanically detectable and cannot be a false positive.** Writing the family list is
the whole cost; the check is a `set()` comparison. Worth sizing two or three more families
(kitchen appliances, stationery, clothing) before deciding whether the instrument is worth
building or whether hand-standardising the ~30 tableware entries is cheaper.

**Blocked on the same decision as P20**: whether the taxonomy gains a `container`/`tableware`-like
tag or whether these all collapse into `tool`. The observing run chose `tool`, which is the
in-vocabulary answer available today.

### Update 2026-08-03 — a second family, and it behaves the same way

This item asked for "2–3 more families sized before an instrument is worth building". The
2026-08-02 polish run supplied the second one without being asked: **native counters and
day-of-month entries** carried sole-`general` semantic tags while their already-polished siblings
used `number` / `time-general`. **Twelve entries were retagged** to match their siblings.

The mechanism is identical to the tableware case and is worth stating as the item's thesis: **a
lexical family drifts apart when its members are polished at different times**, because each run
tags the entry in front of it correctly and in isolation. Neither family's members are individually
wrong; the set is. That is why per-entry review — human or model — cannot find this class, and why
the detector has to compare *within* an enumerable family.

Two families now differ in one useful respect. Tableware is blocked on a taxonomy decision
(`tool` vs a new `container` tag), but the counter/date family is **not blocked at all** — the
correct tags (`number`, `time-general`) are already in `VALID_SEMANTIC` and already used by the
majority of the family. Closed paradigms that the dictionary can enumerate (counters, days of the
month, weekdays, months, seasons) are therefore the place to start: the plurality answer is
computable and the fix needs no curator sign-off. It also overlaps
[P34](#priority-34-action-as-the-sole-semantic-tag-on-a-verb-2085-entries) and the sole-`general`
queue item, so a family-aware pass would drain part of those too.

The practical rule for polish runs, until an instrument exists: **when you touch one member of an
enumerable family, check the whole family.** Both fixes this week came from a run doing exactly
that by hand.

## Priority 37: `politeness: "polite"` on plain vocabulary — and the detector that reports zero

**Source**: 2026-08-01 routine polish run, which found and fixed **78** of them in one 566-entry
creation block. **Measured dictionary-wide by the 2026-08-02 wiki harvest.**

`politeness` is the keigo field: it should be reserved for です/ます-style forms, lexically polite
words, and 美化語. Two batch-created blocks (22504–22526, 22670–22729) had it set to `polite` on
ordinary plain vocabulary — nouns like {県民|けんみん} and {庁舎|ちょうしゃ}, plain-form verbs
like {待|ま}ち{伏|ふ}せる. **79 of the dictionary's 252 `polite` entries sat in that one 566-entry
range**, which is a batch-creation defect rather than a distribution.

**The residue is smaller and harder than the observation assumed.** 174 `polite` entries remain.
Of those, **99 carry an overt honorific marker in the headword** (お/ご prefix, 様, です/ます) and
are plausibly correct as tagged. A hand sample of the other 75 shows the heuristic over-flags
badly: こちら/そちら/あちら/どちら are genuinely polite demonstratives, and すみません,
{行|い}ってらっしゃい, よろしく are set polite expressions. **So this is a per-entry review of a
few dozen entries, not a sweep** — the remaining blocks worth looking at are 9336–10326 (27) and
23265–23577 (10).

**The instrument finding is the more important half.** `check_tag_drift.py --check
politeness-unsupported` reports **0 flags across 0 entries** on this corpus. Its predicate is
`politeness in ("humble","honorific")` with no supporting wording in the notes — it never examines
`polite` at all. So the detector was green through an entire batch-creation defect that a human
found by reading twenty entries. This is a clean instance of the pattern
[Instrument Defects](../topics/instrument-defects.md) documents: **a check reporting zero is
evidence about the check's predicate before it is evidence about the corpus.** Extending the
predicate to `polite` — flag it when the headword carries no honorific marker *and* the notes say
nothing about register — would have caught the 78 at creation time.

**Related**: the same two creation blocks also carry `formality: "formal"` on neutral descriptive
compounds ({乾燥地帯|かんそうちたい}, {工業地帯|こうぎょうちたい}, {経理課|けいりか}). The
cross-model reviewer flagged ~15; per the §A policy they were correctly rejected (the entries'
notes do not contradict the label), but the concentration matches the politeness defect exactly,
which suggests the whole register block from that batch was set carelessly. Whether `formality`
deserves its own detector is a curator question — see
[Tooling 44](tooling-backlog.md#44-consistency-check-non-neutral-formality-with-no-register-statement-in-the-notes).

### Update 2026-08-03 — register drift is a low-ID phenomenon; the high-ID blocks carry tag-*vocabulary* drift instead

The 2026-08-03 accuracy-review run measured both register classes across the 600 entries of
24501–25100 and found them **effectively clean**: exactly **one** `politeness: polite` non-verb
(お銚子, where the honorific prefix makes it correct) and **one** sole-`general` (判断ミス, caught
by the reviewer). Against a block where 41% of entries carried off-vocabulary *semantic* tags,
that is a sharp dissociation.

So the two defect families do not travel together. The dense politeness/formality pockets this
item and [P17](#priority-17-formal-formality-tag-over-applied-in-early-entries) describe are a
property of the **early, low-ID creation batches**; the recent high-ID cohorts inherited a
different bad habit — inventing semantic vocabulary at creation time ([P20](#priority-20-out-of-taxonomy-semantic-tags-post-expansion-migration)).
Useful for targeting: a sweep aimed at register should work upward from the low IDs, and a sweep
aimed at tag vocabulary should work downward from the top. Running either across the whole
dictionary spends most of its budget on the half that does not have the defect.

**Update 2026-08-04 — the low-ID rule has an exception, and it is the loanword blocks.** A polish
run over 06769–06774 (ピザ, アイス, ロフト, バルコニー, バスケ, バレー) found `formality: "formal"`
on abbreviated loanwords whose own notes say the opposite — 06773 バスケ: "バスケ is the everyday
form. Use バスケットボール in formal writing" — and fixed it to `informal`. Measured: **24 pure-katakana
headwords carry `formality: "formal"`**, including パート, バイク, レシート, ライブ, ミーティング,
バイト. Some are defensible (リポート, エネルギー); the abbreviations are not. This is the same
*template-default* mechanism as the low-ID pockets, arriving on a later cohort through a different
route, and it is small enough to clear in one pass. Note the diagnostic the run used: the entry's
own notes contradicting its own tag is an **entry-internal** contradiction — no corpus comparison,
no model needed — which is the same shape as P41 and tooling item 68.

### Update 2026-08-05 — the entry-internal test is sound, nearly exhausted, and blind to 89% of the population

A 2026-08-04 polish run proposed generalising that diagnostic into a sweep, having found
`06779 いずれにせよ` and `06780 ともかく` both tagged `formality: "formal"` while 06779's notes list
ともかく under `CASUAL EQUIVALENTS`. The 2026-08-05 harvest measured it, and the result corrects
the premise as well as sizing the item:

- **The naive predicate is unusable.** "Entry tagged `formal`, notes mention casual/colloquial/
  neutral" returns **1,560 of the 5,068 `formal` entries** — and the great majority are *correct*.
  A formal word's notes listing its casual equivalents is exactly what a good entry does. 06779 is
  one of them: its own REGISTER section reads "written/formal expression … sounds stiff in casual
  conversation", so `formal` is right and the CASUAL EQUIVALENTS section names *other words*. The
  run's real find was 06780, which it fixed (now `neutral`), and 06776 キャンセル's sole-`general`
  semantic tag.
- **The sound predicate is nearly exhausted.** Reading only the REGISTER/FORMALITY section's
  description *of the headword itself* returns **5 entries dictionary-wide** — 07352 ぼやく,
  07367 ややこしい, 07397 待ち合わせ, 07398 後回し, 07411 しんどい — all in one contiguous
  07352–07411 creation cohort, each with a REGISTER note that opens "Casual" or "Neutral". That
  is the whole live scope of the `tag-formality-contradicts-register-note` queue item (previously
  estimated 6; measured 5).
- **And it cannot be the instrument for this priority**, because only **555 of 5,068** `formal`
  entries have a REGISTER or FORMALITY section at all. The test is unarguable where it fires and
  silent for 89% of the population — a ratchet for new entries, not a sweep for old ones. The
  katakana-abbreviation slice above stays the batch-ready half of P37, because it is identified by
  headword shape rather than by prose the entry may not contain.

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

**Filed a fourth and fifth time on 2026-08-02** by both of that day's polish runs (06739–06744:
"zero inline links anywhere"; 06745–06750: "whole sub-ranges appear to predate the inline-link
pass", again proposing a range-scan detector). Both are the 06000–07999 band described above,
both are correct observations of the frontier, and neither is a defect. One of the two added a
genuinely new nuance worth keeping: above the frontier the deficit is not *partial* coverage
needing completion but *no* coverage needing creation from scratch — the expensive case, and the
one Tooling 49 is aimed at. That nuance is now on the topic page; the block itself needs no
further filing.

**Filed an eighth and ninth time on 2026-08-03/04** by two more polish runs (06763–06768 「zero
inline links … 25–40 links per entry, almost all mechanical」; 06769–06774 「every entry in this
cohort needs full tier-1 linking from scratch, ~3x the cost of a normal polish entry」). Both
propose the same targeted linking sweep over 06758–07000. The measurement stands and the answer
is unchanged — this is the frontier, not a defect — but the **cost estimate has now been taken
three times independently and agrees**: ~25–40 links per entry, ~3x a normal polish entry, 4–8
entries per run. That number, not the existence of the block, is the thing to carry into any
scheduling decision (see the frontier-versus-growth gap on
[Quality Metrics](../topics/quality-metrics.md)).

**Filed a tenth and eleventh time on 2026-08-04/05** (06775–06780 and 06781–06786, the latter noting
all six were created 2026-01-18 in one batch). Nothing new; the band is now traced continuously from
~06150 to 06786 with no exception found by any run. Recorded only to keep the count honest — this
is the single most-refiled observation in the project, and every filing has been a correct
observation of the frontier.

**Filed a twelfth and thirteenth time on 2026-08-05/06** (06787–06792 and 06793–06798, the latter
the 2026-01-18 compound-verb batch). The band now runs continuously from ~06150 to 06798. Two runs
independently recommended a dedicated link-coverage pass over the whole 067xx–068xx compound-verb
block rather than one-entry-at-a-time frontier work, which is the same recommendation the eighth
and ninth filings made about 06000–07999. **The count is the argument now**: thirteen filings, one
answer, and the answer has never changed — the band is the frontier, not a defect, and it will be
refiled every run until either the frontier passes it or someone schedules the block sweep.

## Informational: Inline-link base forms labelled `Xする` while targeting the bare noun entry (441 links)

**Source**: 2026-08-02 routine polish run (06749 遅延 uses `→発生する：03133_hassei` and
`→安定する：01703_antei` — a する-form label on a noun entry — "worth a decision on which
convention wins before a sweep"). **Measured by the 2026-08-02 wiki harvest; it is a convention
gap, and a sweep in either direction would be wrong for a third of the population.**

Of the inline links whose declared base form ends in `する`:

| Situation | Links | Can a sweep fix it? |
|---|---|---|
| Target headword **is** `Xする` (the する entry) | 822 | already consistent |
| Target is the bare noun `X`, **and a separate `Xする` entry exists** | 267 | only these — retarget or relabel |
| Target is the bare noun `X`, **and no `Xする` entry exists** | 174 | **no** — the noun entry is the only target there is |

The 174 forced cases are what makes this a decision rather than a cleanup. A rule of "the base
label must equal the target's headword" would require deleting the する from 174 links whose
sentences genuinely contain 発売する, 成長する — losing the information that the linked token is
the verb. A rule of "always label the verb" leaves 174 links pointing at a noun entry by
necessity and 267 pointing at one by accident.

The three coherent options: (a) label the base as the target's headword always, and accept that
verbal uses link to the noun; (b) label the verb always, and treat a noun-entry target as
acceptable when no する entry exists; (c) prefer the `Xする` entry when one exists — a 267-link
retarget — and fall back to (b). Only (c) is a sweep, and it is a small one. Recorded here
because the decision is the curator's and no instrument can infer it. Related:
[P24](#priority-24-inline-link-base-forms-written-with-furigana-braces),
[P32](#priority-32-inline-link-base-forms-written-in-kana-instead-of-the-dictionary-form),
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

## Priority 39: `definitions[].explanation` is a verbatim copy of its own `gloss` (201 senses, 179 entries)

**Source**: 2026-08-03 routine accuracy-review run, which found `24542 突出` and `24544 可憐`
carrying an `explanation` identical to the sense's `gloss` and proposed a one-line detector.
**Measured dictionary-wide by the 2026-08-03 wiki harvest.**

The check is `definitions[i].explanation == definitions[i].gloss`, string-exact. Across 30,148
entries / 36,199 senses (36,153 of which carry an `explanation`), it fires **201 times in 179
entries** — and normalising whitespace and punctuation adds **zero** further hits, so the defect
is pure duplication rather than near-duplication.

The distribution is the useful part. It is not spread across the dictionary; it sits in **six
tight contiguous blocks**:

| Block | Entries | Created |
|---|---|---|
| 04470–04563 | 49 | 2026-01 |
| 24159–24188 | 29 | 2026-04 |
| 24539–24558 | 20 | 2026-04 |
| 24786–24815 | 30 | 2026-04 |
| 25222–25245 | 21 | 2026-04 |
| 25301–25330 | 30 | 2026-04 |

Zero occurrences outside them. This is the batch-creation signature the project has now seen
several times (P11, P20, P21): a generation run adopts a bad habit, carries it for a few hundred
consecutive IDs, and stops. The 2026-01 block is the loanword/household cohort (お玉, 箸置き,
テーブル, ベッド, シャワー…) where the gloss is a single word and an "explanation" repeating it
is visibly empty; the 2026-04 blocks are Sino-Japanese nouns with multi-clause glosses.

**Why it matters**: the renderer emits gloss and explanation as separate lines, so every one of
these entries shows the learner the same text twice. It is also a silent quality signal — a sense
that has never had an explanation written is indistinguishable, downstream, from one that has.

**The fix has a provably-safe option.** `build/schema.json` requires only `sense_number` and
`gloss` in a definition; `explanation` is optional. Deleting a verbatim-duplicate `explanation`
therefore **removes no information and cannot introduce a false claim** — it is the same asymmetry
the 2026-08-03 accuracy-review run established for off-vocabulary tags (`drop` is safe where
`migrate` is not). Writing a real explanation for 201 senses is the better outcome but is a
content task, not a sweep; the drop is the mechanical action, and it leaves the sense in exactly
the state of the ~99.4% of senses that were never given a duplicate.

**Suggested sequencing**: drop the 201 duplicates as one systemic-fix batch (validated by a
re-scan returning zero), then let the ordinary polish frontier write real explanations for the
04470–04563 block when it arrives. Queue item: `definition-explanation-duplicates-gloss`.

## Informational: `〜の前で` where `〜の前に` is meant — measured at zero live scope

**Source**: 2026-08-02 routine polish run, which corrected `06757_uzuuzu`'s
「{試合|しあい}の{前|まえ}で」 (temporal "before the match") to 前に and proposed a detector for
"〜の前で followed by a stative/psychological predicate".

**Measured 2026-08-03: the detector would return nothing.** There are 100 occurrences of の前で
across 90 entries, 83 of them in furigana-wrapped form, and **not one** has an event/temporal noun
in front of it (試合, 会議, 授業, 出発, 食事, 本番, 締切, 手術 … — the whole tested set returns
zero). Every remaining instance is the ordinary locative reading — 上司の前で, 仏壇の前で,
子供たちの前で, ホームドアの前で — where 前で is correct and 前に would be wrong.

The observed defect was real; it was also, as far as the corpus can show, unique. Filed here so a
later session does not re-propose the scan: **no detector, no sweep**. The generalisable lesson is
the one this file has recorded before — a particle error found in a single example is evidence
about that example, and the cheap thing to do before designing an instrument is to run the count.

## Informational: Pre-polished cohort around 00083–00090

Four entries in the 00074–00096 range (00083 俳句, 00086 発揮, 00087 花火, 00088 判事) were already fully linked — suggesting a prior polish pass touched that range. Subsequent sessions entering this area should expect occasional entries needing no work.

## Priority 40: `body-part` on entries that cannot denote a body part (41 verb-POS entries)

**Source**: 2026-08-03 routine accuracy-review run, which corrected six entries in one 531-entry
range where `body-part` had been applied to actions (脱毛, 除毛, 大あくび, 姿勢矯正), measurements
(体脂肪率), conditions (しもやけ), products (コンディショナー) and physique descriptions (中肉中背),
and proposed a dictionary-wide rule. **Measured 2026-08-04.**

The project's semantic tags are **denotational** — the accuracy reviewer's `tags` dimension judges
each tag against the *headword*, not against the example topics — so a verb can never denote a
body part. That makes one slice of the family mechanically decidable with no judgment at all:
**41 entries carry `body-part` while their `pos` includes a verb class.**

Splitting them by whether a body part appears in the headword separates two very different cases:

- **11 entries name a body part in the headword** — 目を伏せる, 目を逸らす, 目が回る, 首を傾げる,
  息が詰まる, 声が枯れる, 頬杖をつく, 手術, 発汗, 整髪, 洗髪. Here `body-part` is a *topical* read
  of a phrase that contains one. Defensible under a loose reading of the tag, wrong under the
  denotational one, and worth deciding once rather than per entry.
- **30 entries contain no body part anywhere** — and these are pure drift: 調査 "investigation",
  舞う "to dance", 描く "to draw", 溢れる "to overflow", 染まる "to be dyed", なびく "to sway",
  ときめく "to throb", タヌキ寝入り "pretending to be asleep", 火傷, 日焼け, 閉経, 大便, 出産する.

**There are in-list destinations**, so this is not the tag-vocabulary gap that P20 documents:
`health` covers 火傷 / 日焼け / 閉経 / 大便 / 化膿 / しもやけ, `appearance` covers 中肉中背 / カール,
`action` covers あくびをする / さする, and `body-internal` exists for organs. The correct action is
per-entry (migrate or drop), not a single mapping — but the *detection* is free, which is the same
economics P39 and the `VALID_SEMANTIC` diff have: pay for the destination, never for the search.

This is the third measured shape of the same underlying defect after P11 (batch-creation topical
tags) and P38 (families that drift apart when polished at different times). What makes this one
distinct is that the mismatch is provable from the entry's own `pos` tag — no corpus comparison,
no family enumeration. **Generalisable check**: any semantic tag naming a concrete *thing*
(`body-part`, `body-internal`, `tool`, `furniture`, `clothing`, `animal-*`, `plant-*`) on an entry
whose `pos` is verb-only is a type error. Queue item: `tag-bodypart-non-denotational`.

## Priority 41: Conjugation tables generate the potential of a verb that is already potential

**Source**: 2026-08-03 routine new-entries run, which noticed `add_conjugations.py` producing
待ちきれられる and 待ちきれろ for `30367 待ちきれる` and suggested a suppression flag.
**Measured 2026-08-04, and the scope reaches basic-tier vocabulary.**

Conjugation tables are hard-coded into the entry JSON and rendered as a full table on the entry
page, so every wrong row is live on the site. Three of the dictionary's most common verbs publish
a potential form of a potential:

| Entry | Headword | Published "Potential" / "Passive" | Published "Imperative" |
|---|---|---|---|
| `00557_dekiru` | できる | できられる | できろ |
| `01165_mieru` | {見\|み}える | 見えられる | 見えろ |
| `01229_kikoeru` | {聞\|き}こえる | 聞こえられる | 聞こえろ |

できる is a **basic-tier** entry — the highest-traffic band in the dictionary.

**Two mechanical tests, and only one of them is usable.**

- *Headword shape* (`-きれる`): returns 9 entries, all carrying a Potential row — but it mixes the
  lexicalized potentials (待ちきれる, 割り切れる) with ordinary intransitive pair members (千切れる,
  途切れる, 振り切れる) whose potential is merely rare, not ungrammatical. **Unusable as a rule.**
- *Self-declaration*: the entry's own notes or gloss describe it as a potential form, and its
  conjugation table still carries a Potential row. Returns **6 — 取れる, 眠れる, いける, 聞こえる,
  できる, 待ちきれる — and all 6 are true positives.** This is an entry-internal contradiction:
  the prose and the generated table disagree with each other, which is exactly the class of defect
  `check_consistency.py` exists for.

The self-declaration test under-generates (見える does not say so in prose), so the shippable form
is: run the contradiction check, hand-add the small list of known lexicalized potentials, and
suppress `Potential`/`Passive`/`Imperative` rows for that set. Suppression is safe by construction
— a row that is not rendered teaches nothing wrong, while a wrong row teaches ungrammatical
Japanese. Queue item: `conjugation-potential-of-potential`; generator-side fix in tooling item 70.

## Informational: 105 entries have no semantic tag at all — and it is two populations, not one

**Source**: 2026-08-03 polish run (「pronoun semantic tagging is inconsistent overall; 12 entries
carry no semantic tag at all」) and a 2026-08-04 polish run (`06781 っぽい` has no semantic tags).
**Measured 2026-08-04: 105 entries dictionary-wide** (19 basic, 4 core, 82 general).

The distribution by `pos` splits them cleanly:

| Class | Entries | Examples |
|---|---|---|
| **Closed-class function words** | 53 | suffix 18, prefix 14, pronoun 12, pre-noun-adjectival 5, auxiliary 3, interjection 1 (`01994_in`, `02003_chan`, `01574_anna`, `02185_ore`, `06781_ppoi`) |
| **Open-class content words** | 52 | noun 15, noun+verb-suru 8, verb-godan 6, adjective-i 6, verb-ichidan 4, … |

For the second group an empty `semantic` is simply an omission and the ordinary polish pass fixes
it. For the first, "no semantic tag" is arguably *correct* under a denotational reading — a suffix
denotes nothing — and the project's own convention is inconsistent about it: person-referring
pronouns are tagged `person` on 7 entries and `grammatical` on 12, and two second-person pronouns
(てめえ, 貴公) were the only entries in the dictionary tagged `language` until a polish run fixed
them. `grammatical` exists in `VALID_SEMANTIC` precisely for this class.

Filed as Informational rather than a priority because the closed-class half needs a one-sentence
convention ("function words take `grammatical`") before any sweep, and with that convention the
work is 53 mechanical additions plus 52 ordinary polish decisions. The useful measurement is that
the population is **small and bounded** — this is not a systemic hole, and it does not justify an
instrument.

## Priority 42: Neighbours named in notes prose but absent from `cross_references` (1,402 entries, discrimination half)

**Source**: six independent polish runs between 2026-07-31 and 2026-08-05, most recently a
priority lane that hit the shape **6 times out of 6** (00486 年, 00507 部屋, 00631 一月 — rich
notes naming obvious neighbours, `cross_references` empty or holding one item).
**Measured dictionary-wide by the 2026-08-05 wiki harvest**; full numbers and method in
[Tooling 55](tooling-backlog.md#55-detector-contrast-words-named-in-notes-prose-but-absent-from-cross_references).

An entry's notes say `SIMILAR WORDS: ⟦科目⟧ ⟦教科⟧ ⟦専攻⟧` and its `cross_references` array lists
one of the three. The relation is stated in prose, where the site's navigation cannot use it and
`check_semantic_clusters.py` cannot see it, while the structured field that exists to carry it
sits half-empty. This is not missing knowledge — the entry already *did* the lexicographic work,
including finding the target's ID — it is knowledge stranded in the wrong field.

**Scope**: 2,795 entries / 5,391 refs where a link *leads its bullet* inside a relation-bearing
note section and is absent from `cross_references`. That splits into two populations that should
not be worked the same way:

| Population | Entries | Refs | Disposition |
|---|---|---|---|
| **Discrimination** — `SIMILAR WORDS`, `CONTRAST`, `OPPOSITE`, `COMPARISON`, `SYNONYMS` | **1,402** | **2,395** | batch-ready; the header supplies the `type` |
| Thematic — `RELATED TERMS`, `RELATED WORDS`, `RELATED VOLCANIC TERMS`, … | 1,470 | 2,999 | convention question first |

The discrimination half is the near-synonym contrast material `cross_references` was designed
for, and 676 of those entries need exactly one ref (509 need two, none more than five). The
thematic half is a semantic-field roster: promoting 噴火's four `RELATED VOLCANIC TERMS` links
would turn `cross_references` into a topic index, which is a curator decision of the same shape
as [P38](#priority-38-semantic-tags-disagree-within-a-closed-lexical-family-tableware-32-entries-12-tag-sets)'s
lexical families — and should be decided once rather than 1,470 times.

**Two constraints on any sweep.** (1) The link must *lead* its bullet: mid-bullet links are
collocational tokens, not the named neighbour — 00053 学科's CONTRAST bullet reads
`学科試験 vs 実技試験`, and a position-blind scan proposes a `contrast` ref to 試験. Requiring
bullet-leading position removes 1,364 of 6,755 raw hits. (2) The population is bounded by the
link frontier by construction — 3,043 of 3,050 affected entries are below ID 07000 — so this
queue *grows* as the polish lane advances, and every entry the lane links becomes an entry this
check can then verify. Adding the back-link on the target side is the second half of each fix and
is not counted above.

Queue item: `crossref-missing-from-notes-prose` (now scoped and batch-ready for the
discrimination half). Mirror image of
[Tooling 52](tooling-backlog.md#52-does-check_semantic_clusterspy-count-a-prominent_see_also-mention-as-satisfying-the-pair-requirement);
the above-frontier cases it cannot see are
[Tooling 57](tooling-backlog.md#57-check_semantic_clusterspy-has-no-closed-paradigm-symmetry-rule)'s
closed-paradigm problem.

## Priority 43: The 06800–07100 block is 96% unlinked — a bounded batch, not a frontier problem

**Scope**: 288 of 301 entries (**96%**) have zero inline word links in examples or notes
**Status**: open, batch-ready
**Filed**: 2026-08-06 (measured); the underlying band has now been reported by fifteen runs

The 06000–07999 zero-link band is the most-refiled observation in the project — traced
continuously from ~06150 to 06798 with no exception found by any run — and the standing wiki
position has been that it is *not* a defect: zero-link entries are the polish frontier, and
[the informational item below](#informational-entries-with-zero-inline-links-23294-are-the-polish-frontier-not-a-defect)
says so at length. That position is still right about the 23,294 entries as a whole. It is
wrong about this block, for one measured reason.

**The frontier crawls through it at roughly one-fifth normal speed.** These are largely
grammar-expression and advanced-vocabulary entries created in one batch on 2026-01-18 (として,
にとって, に伴い, DM, プライバシー, 運休 …), and a comprehensive-polish run that meets them
spends its entire entry budget writing links from scratch instead of polishing. Runs
immediately below the block (06802–06808) and immediately above it, polished more recently,
are fully linked — so the block is not a frontier position, it is a **wall the frontier is
grinding through at a cost the frontier cadence was not sized for**.

That is what makes it a batch rather than a backlog entry. The work is the same work either
way; doing it as a dedicated `systemic-fix` sweep over 06800–07100 removes it from the
critical path of every polish run for the next several weeks, and it is exactly the workload
[Tooling 82](tooling-backlog.md)'s link proposer was prototyped against — the run that wrote
the prototype reported it cut per-entry cost on 15-example entries "by a large factor".

**Sequencing note**: run [Tooling 78](tooling-backlog.md)'s wrong-target detector and the
[P35](#priority-35-stale-noentry-inline-links--3797-markers-now-resolve-2887-mechanically)
stale-`noentry` resolution *before* the sweep, not after. Writing 288 entries' worth of new
links against a lookup that answers katakana from `by_headword` only
([Tooling 76](tooling-backlog.md#76-word_id_lookupjson-answers-katakana-lookups-from-by_headword-only))
is how a fresh cohort of spurious `noentry` markers gets created — and a `noentry` written
today is a P35 item tomorrow.

## Priority 44: Naked sentence-final です/だ in the 00700–00900 basic block

**Scope**: not yet counted (reported across the 00700–00900 basic-tier band)
**Status**: needs-detector
**Filed**: 2026-08-06

Entries in this band link every particle and content word in their examples but leave the
sentence-final copula bare — inconsistently with their own notes, which discuss です/だ as a
form worth knowing. The pattern is mechanical to detect (a sentence-final です/だ/でした/だった
outside any `⟦…⟧` span, in an entry that has links elsewhere) and mechanical to fix.

Two cautions before it is swept:

- It needs a count first. "The 00700–00900 block" is a report from one run's working range,
  and the band's neighbours were the subject of two other measurements this week that both
  came back concentrated in one authoring cohort rather than spread across the tier.
- Whether the sentence-final copula *should* be linked at all is a convention question, not
  a defect finding — the same shape as the `Xする` label convention and the `ている`-has-no-entry
  question already filed as informational items. If the answer is "yes", this is a sweep; if
  "no", the inconsistency is in the entries that *do* link it.

## Updates 2026-08-07 (wiki harvest)

**P20 (off-vocabulary semantic tags) — the density series now has five points and is falling.**
Per-block off-vocabulary density measured by consecutive accuracy-review sweeps:
53% (23908–24500) → 41% (24501–25100) → 33% (25601–26200) → **28%** (26701–27000, 92 tags
across 83 entries) → the 27001–27313 block, where off-vocabulary tags were **the entire
applicable yield: 34 of 39 applied tag fixes** (`places`/`place` 5, `medical` 3, `people` 3,
`location` 3, `conflict` 3, `body` 3, `fashion` 2, plus singletons). Two consequences. First,
the falling density is the mechanical cause of the `tags` dimension's apparent precision
decline — see [Quality Metrics §14](../topics/quality-metrics.md), which retires the blended
number. Second, a new sub-slice: **counter entries carry the same drift** (27625 二回 tagged
`time`, which is not in `VALID_SEMANTIC`; `time-general` is). A `check_tag_drift.py` sweep
restricted to `pos: counter` would size that family cheaply, and counters are enumerable, so
disagreement within the family cannot be a false positive — the P38 argument.

**P24 (braced inline-link base forms) — measured, and it is one cohort.** **226 instances
across 36 entries**, 6.3 per affected entry, with **33 of the 36 below ID 01000** and most of
those in two tight runs: 00697–00716 (numerals and counters — 一, 二, 人, 枚, 個, 中, 時, 歳)
and 00966–00984. So this is not a 226-occurrence dictionary-wide sweep; it is **36 files, one
basic-tier authoring cohort, one regex**, comfortably inside a single `systemic-fix` run. The
transformation is provably safe (the `entry_id` resolves the link; the base form is
display-adjacent), but the diff lands on the dictionary's most-read pages, so spot-check the
rendered output rather than only the JSON. Full analysis:
[Inline Link Integrity](../topics/inline-link-integrity.md).

**P35 (stale `noentry` markers) — the whole-corpus scan, and the half that must not be
touched.** A 2026-08-07 scan against `build/word_id_lookup.json` found **7,386 `noentry`
markers total**, of which **2,633 instances across 2,351 distinct multi-character base forms
now resolve to a real entry**. Hand-confirmed in the same run: 二時間→27637, 何時間→30372,
お願いいたします→27603, 料理屋→27551; and by a second run: リスト→09786,
ネットショッピング→29757, 釣り銭→27568, 佐藤→27597, 便数→30234, 粉薬→27515, 三階→27617,
一万→27599, 千万→28267. **The exclusion is the important part**: a further 403 instances on 189
*single-character* bases must **not** be bulk-fixed — they are mostly bound morphemes inside
compounds (業, 形, 角), where the marker is correct and the "resolving" entry is a different
word. Restrict any detector to multi-character bases. This is now the highest-yield mechanical
item on this page and it **grows with every new-entries run**, which is the argument for
building the detector rather than sweeping by hand.

**P42 (neighbours named in notes prose but absent from `cross_references`) — 8 of 8 again, and
a prioritization gap.** A 2026-08-06 priority lane hit the shape in **all eight** entries it
processed (00832, 00849, 00853, 00878, 00879, 00884, 00893, 00897) and a 2026-08-07 lane hit it
in all eight of its own — following 6-of-6 on 2026-08-04. In every case the cross-references
could be lifted straight out of the existing notes. The new datum is *why they keep
resurfacing*: **the `notes` priority score cannot see this defect**, because the notes are
good — that is the whole point of the item. Proposal, and it is cheap: add a
"notes name neighbours but `cross_references` is empty" signal to
`prioritize_polishing.py`, or to `check_consistency.py`. Without it the priority lane will keep
rediscovering the same population one run at a time.

**P13 (sole-`general`) — no sweep needed.** 44 entries in one block (26701–27000) were
corrected to specific in-list tags by the accuracy-review lane, mostly suru-verbs and technical
compound nouns from one creation batch. Combined with the 2026-08-06 refutation of the
gloss-keyword suggester, the position is now settled: **P13 is tractable through the
accuracy-review lane and needs no instrument of its own.** One local confirmation from a polish
run: 06809 下味 carried sole `["general"]`, retagged `["cooking","food"]` — and the rest of the
06800–06900 block, created in the same 2026-01-18 batch as [P43](#priority-43-the-0680007100-block-is-96-unlinked--a-bounded-batch-not-a-frontier-problem), likely shares the default.

## Priority 45: Unbalanced furigana braces (34 instances / 33 entries) — visible on the live site

**Source**: 2026-08-07 routine polish observation (06824 `magirawashii` carried a stray closing
brace, `{分|わ}かりにくい}`, fixed in-run); sized 2026-08-08 by whole-corpus scan.
**Detect**: for every string field in every entry, compare `count('{')` with `count('}')`.
**Scope**: **34 instances across 33 entries** — 20 in `notes`, 14 in `examples[].japanese`.
**Status**: open, batch-ready, no cursor needed.

This is the smallest genuinely-broken class currently on this page, and the only one on the
furigana side that is **plainly visible to a reader**. `08385`'s rendered page reads
"**ぎ} tends to be used for**" — a literal brace sitting in English prose. The imbalance runs
in both directions (dropped `}` in 04471/09020/09801; extra `}` in 08385/11708/12060/16849),
so the repair is per-entry rather than one regex, but 33 files is a single sitting.

One instance is worse than cosmetic and should be looked at first: **04471** contains
`かき{混→かき{混：noentry⟧|ま}ぜ`, a furigana wrapper and an inline `⟦…⟧` link interleaved into
one another. Neither structure parses; the link cannot be recovered mechanically and the
phrase needs re-authoring.

**Why it went unnoticed for two months**: the check was proposed on 2026-06-17 as half of
[Tooling 8](tooling-backlog.md#8-furigana-format-validator)'s enhancement, bundled with a
second rule that turned out to be worthless (see the Informational entry below). Bundling a
34-instance real defect with a 931-instance false positive is what kept both unbuilt.

## Informational: the brace is also a mention-quote (1,084 spans) — a convention, not a defect

**Measured 2026-08-08.** The other half of Tooling 8's June proposal — "flag any `{…}` span
whose interior contains no `|`" — fires **931 times across 623 entries**, and essentially none
of them is a malformed wrapper. Braces are doing a **second, undocumented job**: quoting a
linguistic object under discussion, the way an English style guide italicises a mentioned word.

- `The reading {じゅうぶん} means 'enough' while {じゅっぷん/じっぷん} means '10 minutes'` (01614)
- `Usually read as {だて}, sometimes {たて}` (02002)
- `The kanji {匂} is used for general smells, while {臭} specifically refers to bad ones` (00319)
- `- {〜て}たまらない: So ~ that one can't stand it` (03409, grammar-pattern notation)

855 of the 931 are kana-only spans in `notes`/`explanation` prose; 54 are kanji mentions; 168
are grouping wrappers that nest a valid `{X|Y}` (`{お{正月|しょうがつ}}`); 7 are `{WO}`/`{NI}`
pattern placeholders; 22 sit inside `⟦…⟧` link surfaces (P24-adjacent). Adding the obvious
refinement — "flag only spans containing kanji" — does **not** rescue the rule: in the kanji
cases a reading is often actively wrong, since 00319 exists precisely to contrast 匂 and 臭,
which share the reading にお.

**Disposition: retire the rule and document the convention instead.** Full analysis in
[Furigana Wrapper Anomalies → "The brace is also a mention-quote"](../topics/furigana-wrapper-anomalies.md).
The convention appears in no skill, no schema, and not in `CLAUDE.md`, and that gap is the
measurable cause of a recurring cost: **three sessions across two months have proposed
detectors against it**, because a reader who knows only the documented rule
(`{漢字|かんじ}`) correctly concludes that `{だて}` is malformed.

## Updates 2026-08-08 (wiki harvest)

**P35 (stale `noentry` markers) — the affix cohort resolves only through a tilde form (+159).**
A polish run noted that `01447`'s `⟦{全|ぜん}→全：noentry⟧` should resolve to `28337_zen`, whose
headword is `全〜` with a tilde, and that a lookup must therefore try both the bare and the
affixed form. Measured: **159 instances across 47 distinct bases** resolve *only* via `〜X` or
`X〜`, against 3,536 that resolve on the bare headword and 3,686 that stay unresolved. The
population has a single clear provenance — it is almost entirely the **28xxx suffix cohort**
(〜感 28578, 〜代 28331, 〜書 28467, 〜賃 28343, 〜化 28335, 〜展 28468, 〜系 28466, 〜士 28352,
〜史 28471, …), a deliberate affix batch created *after* the entries that reference those
morphemes. That is the same "correct when written, rotted as the dictionary grew" mechanism
P35 already documents, arriving through a batch rather than one entry at a time.

+4.5% on the mechanically-fixable set is small, but the item is worth recording for a
different reason: applying it writes links whose **label is bare (`全`) while the target
headword carries a tilde (`全〜`)**, which is exactly the shape
[`check_link_baseform.py`](tooling-backlog.md#83-check_link_baseformpy-accept-na-adjective-normalization)
flags. The affix-tilde relationship needs to join na-adjective normalization (巨大な → 巨大)
and する-normalization (参加する → 参加) in that script's accepted-relationship list, **before**
the P35 sweep runs — otherwise the sweep manufactures 159 new baseform findings.

**P42 (neighbours named in notes prose but absent from `cross_references`) — 8 of 8 and 7 of 7,
again.** Two independent 2026-08-07 polish runs each reported that *every* priority-lane entry
they touched had `"cross_references": []` while its notes named 2–4 neighbours in prose under
`RELATED TERMS:` / `SIMILAR WORDS:` / `CONTRAST` headings (01080, 01332, 01385, 01393, 01447,
01606, 01706, 01745; and 01763, 01769, 02204, 02210, 02211, 02234, 02240). This is the third
and fourth consecutive 100% hit rate. The diagnosis on file is unchanged and was restated
independently by both runs: `score_note_quality` ranks these entries low **because the notes
are good** — long, structured, full of prose neighbours — so the `notes` priority lane keeps
delivering entries whose actual defect is a different, empty field. Both runs also supply the
extraction signal in the same words: a note section headed RELATED/SIMILAR/CONTRAST whose
inline links carry target IDs absent from `cross_references` is a near-certain miss, and the
IDs are already in the file.

**P43 (the 06800–07100 block is 96% unlinked) — confirmed at the frontier, with a cost figure.**
The first polish run to reach the block reported **7 of 7 frontier entries (06813–06819) with
literally zero inline links** in examples *and* notes, matching the 96% measured on 2026-08-06.
It also priced the block: **~4× a normal frontier entry**, and named the technique that made
seven affordable — batch the lookups (one `by_reading`/`by_headword` query for the whole
entry, then a single scripted write) rather than per-word `Edit` calls. A second run
independently budgeted "~2 entries per 10% of context" for 06820–06825. Both figures belong
with the queue item `inline-link-block-06800-07100`, which is sized in entries but whose real
constraint is context per entry.

## Priority 46: Notes fully linked, examples completely bare (33 entries) — behind the frontier

**Source**: 2026-08-08 routine polish observation on 06835–06841 ("entries have fully-linked
notes but zero inline links in their examples … looks like a creation-era batch signature").
**Sized 2026-08-08 by whole-corpus scan**, and the measurement changes the diagnosis.

**Detect**: entry has ≥1 `⟦…⟧` in `notes` **and** zero `⟦…⟧` across every
`examples[].japanese`. Mechanical, no judgment.
**Scope**: **33 entries**. **Status**: open, batch-ready, no cursor needed.

The observing run's own block does not appear in the result — it fixed it in-run. What remains
is a different and more interesting population, because **32 of the 33 sit behind the polish
frontier** (`next: 06842`) in six tight consecutive runs, plus one outlier far beyond it:

| Run | IDs | n |
|---|---|---|
| 1 | 06038–06047 | 10 |
| 2 | 06457–06462 | 6 |
| 3 | 06631–06638 | 8 |
| 4 | 06669 | 1 |
| 5 | 06723–06729 | 7 |
| — | 18725 | 1 |

**These are not unlinked entries — they are half-linked ones.** Each carries 8–11 links in its
notes while its examples, which are full of linkable vocabulary, carry none: 06038 `閉め出す`
has ten note links and examples containing 鍵/忘れる/家/猫/外; 06631 `面影` has eleven and
examples containing 町/昔/母親/残る. Their `modified` stamps are polish-run dates
(06631: 2026-07-26; 06723: 2026-08-08), so **the frontier passed them and left the examples
bare** — this is not a creation-era signature but a *session-shape* one. The runs are
contiguous and end abruptly, which is what a session that linked notes for a batch and then
ran out of context before the examples looks like.

**Why it matters beyond 33 entries**: [P43](#priority-43-the-06800-07100-block-is-96-unlinked)
treats unlinked stretches as work the frontier has not yet reached. This class is work the
frontier *did* reach and completed only half of, so no cursor will ever return to it. That
makes the detector worth keeping as a standing check rather than a one-off sweep — it is the
cheapest available audit of whether the inline-link step actually finished.

## Priority 47: Compounds split across two adjacent links although the compound has an entry (443 pairs / 391 entries)

**Source**: 2026-08-08 routine polish observation (02274 linked フランス+語 and ドイツ+語
separately although `24509_furansugo` / `28074_doitsugo` exist; 02646 split 筋肉+痛 although
`06298_kinnikutsuu` exists), proposing "a detector for any adjacent link pair whose
concatenated surface form matches an existing headword."

**This is already project policy, not an open question.** The `inline-word-links` skill's
common-mistakes table has carried the rule since the skill was written: *"Compound splitting —
日本語 → 日本 + 語 — should link as single compound if entry exists."* The observation
rediscovered a documented standard, which is the useful part: the standard has no instrument.

**Measured 2026-08-08 against `build/word_id_lookup.json`**, and the naive rule is **not**
batch-ready — it fires **1,579 times across 1,296 entries**, and more than half of that is a
single false-positive family:

| Family | n | Verdict |
|---|---|---|
| Second half is a short kana grammatical element (に 291, する 204, も 96, の 54, な 45, で 26, から 20, でも 16, ずつ 15, たち 12 …) | **847** | **Exclude by rule.** 前+に, 一緒+に, 少し+ずつ are correct links that happen to concatenate into a lexicalized entry. |
| Second half is a 1-character morpheme (人 58, 円 12, 中 11, 的 11 …) | 289 | Mixed; needs judgment per base. |
| **Both halves ≥2 characters** (写真+撮影, 身分+証明書, 婚約+指輪, 運転+免許, 最高+裁判所, 災害+対策) | **443 pairs / 391 entries** | **The real class.** Unambiguously covered by the skill's rule. |

**Detect**: adjacent `⟦…⟧⟦…⟧` pairs, de-furigana both surfaces, concatenate, look up in
`by_headword`; keep only pairs where both surfaces are ≥2 characters.
**Scope**: **443 pairs / 391 entries**. **Status**: open, needs detector, then batch-ready.

The `する` sub-family (204) is the same rule applied to suru-verbs — 勉強+する where
`00527_benkyousuru` exists — and deserves a **separate decision** rather than inclusion here:
the split is legible, both halves resolve, and reversing 204 of them is a larger change to
reader-facing text than the compound-noun case. Note the shape this shares with the
2026-08-08 stale-`noentry` finding: **precision splits on the length and script of the second
element, not on the pair as a whole**, which is now the second sweep where that axis carved a
clean batch out of a noisy population.

## Priority 48: Inline links with the base-form segment missing entirely (17 instances / 7 entries)

**Source**: 2026-08-08 routine polish observation; **sized 2026-08-08**, and the scan found one
shape the observation did not.

`validate.py` already reports these, so they are not undetected — they are unfixed.
The malformed links are `⟦surface→noentry⟧`: the base-form segment and its full-width colon
are gone, where the well-formed shape is `⟦surface→base：entry_id⟧`. Because every `noentry`
scan in the project anchors on `→base：noentry`, **these are invisible to
[P35](#priority-35-stale-noentry-markers)'s sweep and to `check_stale_noentry.py`**, and would
have survived it silently.

**Scope**: **17 instances across 7 entries** — 01340, 03022, 04757, 06443, 06444 (5 instances),
06447 and one other; concentrated in 064xx as reported. **Status**: open, batch-ready.

**Two shapes, not one.** Fifteen are the reported `⟦X→noentry⟧`, repairable mechanically: the
base form equals the de-furigana'd surface in every sampled case
(`⟦{数十万円|すうじゅうまんえん}→noentry⟧` → `…→数十万円：noentry⟧`). The other two, both in
**03022**, are `⟦{観光|かんこう}⟧` — **no arrow at all**, neither base form nor target. Those
need a lookup (観光 has an entry) rather than a rewrite, so handle 03022 by hand.

## Priority 49: Wrong furigana inside inline-link surfaces (40 pairs) — a blind spot in every furigana instrument

**Source**: 2026-08-08 routine polish observation on `check_stale_noentry.py`'s class R
(link surface's furigana contradicts the target entry's reading).

The detector was built to find stale `noentry` markers; class R is an **unintended furigana-error
detector**, and the hand-checked pairs are genuine errors in the source entries:
来春 written らいはる, 農作物 のうさくもつ, 墓石 はかいし, 完全試合 かんぜんしあい,
白和え しろあえ, 部屋干し へやほし, and 言い及ぶ wrapped as `{言|い}{及|およ}ぶ`.

**Scope**: **40 pairs**. **Status**: open; verify each against the target entry before applying
(the target's reading is the authority, but a link surface may legitimately carry an inflected
reading).

**Why these survived every net**: all 40 sit inside a `⟦…⟧` link *surface*, and both
`find_missing_furigana.py` and the OpenRouter furigana screener read past link surfaces to the
sentence text. This is the third instance of the same shape —
[P36](#priority-36-headwords-missing-furigana) (headword field) and
[Tooling 47](tooling-backlog.md#47-cross-reference-headword-reading-disagreement)
(cross-reference headwords) were the first two: **a field outside `examples[].japanese` and
`notes` falls through every furigana instrument the project owns.** The recurring fix is not 40
edits but folding link surfaces into the instruments, which is why this is filed here *and*
noted against Tooling 47's family.

## Informational: the `〜的` note skeleton is templated, but the link gap is 234 entries wide

**Measured 2026-08-08.** A polish run observed that 06826–06830 share an identical note
skeleton — ETYMOLOGY as `{X}` + `{的|てき}`, then FORMS with adverbial に / predicative だ /
attributive な — needing the same five links every time (`09839_teki`, `00314_ni`, `09496_da`,
`09497_na`, plus the base noun), and proposed a templated linker as "a safe, high-yield
mechanical sweep."

The corpus holds **281 `〜的` entries**, of which **47 already link `09839_teki` in their notes
and 234 do not**. The convention is therefore real and established, and the gap is an order of
magnitude larger than the observing block. But 234 is an *upper bound on the opportunity, not a
batch*: only the subset carrying the full ETYMOLOGY/FORMS skeleton takes all five links
positionally, and the rest need the base-noun link resolved per entry. Recorded here as the
sizing so the next run that proposes this sweep does not re-measure it; it needs the skeleton
sub-count before it becomes a queue item.

## Updates 2026-08-08 (wiki harvest, run 2)

**P11 (semantic tag drift) — the largest single migration yet, and the remaining scope is now
known.** The 2026-08-08 accuracy-review of 28351–28900 found off-vocabulary semantic tags in
**236 of 549 entries** (270 instances, 101 distinct invented labels: `time`, `people`,
`animal`, `plant`, `object`, `mathematics`, `sensation`, …) and migrated all 236 in-run. The
provenance is unambiguous batch-creation drift — the creating session invented plausible labels
instead of drawing from `VALID_SEMANTIC`. **Dictionary-wide, 1,902 entries still carry
baselined off-vocabulary tags**, which makes this the largest remaining tag-quality item on this
page by an order of magnitude, and the one with the highest measured apply rate (see the
quality-metrics note below).

**New: `domain` has the same shape as `semantic` did, and no instrument.** Two polish
observations flagged `domain: business` on entries with no business character (06838 余白,
margins and aesthetics; 06839 逆転, sports comebacks) and `domain: medical` on 06830 劇的 from
a single medical example — the same single-example-contamination shape as P11. **Measured
2026-08-08: 3,593 domain instances across 3,278 entries**, and the distribution is lopsided in
exactly the way a template default looks:

| domain | n | | domain | n |
|---|---|---|---|---|
| `business` | **1,162** | | `colloquial` | 328 |
| `academic` | 566 | | `internet` | 70 |
| `technical` | 556 | | | |
| `legal` | 476 | | | |
| `medical` | 435 | | | |

`business` alone is 32% of all domain tags. Unlike `semantic`, `domain` has a closed
`VALID_DOMAIN` list that these all satisfy, so `check_tag_drift.py` and the
off-vocabulary reviewer flag — the two instruments that made P11 tractable — are both blind
here **by construction**: every one of these tags is valid, just wrong. Status: open, needs a
detection idea before it can be sized. The reviewer's `tags` dimension judges semantic tags
against the headword and could plausibly be pointed at `domain` the same way; that is the
cheapest available route and is filed as a tooling item rather than assumed here.

**Reinforced: reviewer formality flags remain a clean noise family (5/5, third window).** All
five formality flags in 27851–28350 (27906, 27918, 27965, 27989, 27995) were contradicted by
the entry's own REGISTER line. §A's guard — apply only when the entry's own notes contradict
the label — held perfectly again. This is now measured across three windows and belongs with
the queue item `reviewer-formality-noise`; the standing recommendation is unchanged (have the
reviewer prompt read the notes before judging register).

**Reinforced: P43 confirmed at 9 of 9.** The 06826–06834 frontier block was uniformly
pre-inline-link — all nine entries had zero links in examples *and* notes, eight of nine needed
the notes' ETYMOLOGY/COLLOCATIONS sections linked from scratch — and the run independently
re-derived the ~2-entries-per-10%-of-context budget for the 06800+ stretch. Fourth consecutive
confirmation; no change to the item.

**Reinforced: basic-tier entries arrive with empty `cross_references` and template-default
tags.** All six priority-lane entries in the 2026-08-08 polish run had zero cross-references,
and three carried a default (`general` semantic on 02907/02938; `plain` politeness on the
explicitly-polite どうぞ). This is the same population as
[P42](#priority-42-neighbours-named-in-notes-prose-but-absent-from-cross_references), and the
run restated its diagnosis independently: the notes already name the neighbours in prose, so
extraction is largely mechanical.

**Curator taxonomy question — a third gap, and this one is bigger than reported.**
`VALID_SEMANTIC` has no category for sound or acoustic phenomena. The observing run met three
in 27851–28350 (28327 爆発音, 28328 銃声, and one more) and had to migrate them to weaker
destinations (`abstract`, `military`) because nothing in the list fits, filing it as a minor
vocabulary addition. **Measured: 896 entries have a gloss naming a sound, voice, noise or
acoustic concept**, and their current tags are dominated by catch-alls — `general` (92),
`action` (77), `descriptive` (48). That keyword net is loose and 896 is an upper bound, but it
is enough to move this off the "minor addition" pile: it joins the **spatial/positional and
document-type gaps (322 instances)** already routed to the curator as one taxonomy decision,
not three small ones.

## Priority 50: Zero links *anywhere*, behind the frontier (55 entries) — the other half of P46

> **Re-measured 2026-08-15: 54 entries**, and they fall in six contiguous ID runs rather than
> scattered — see [Updates 2026-08-15 (run 2)](#p50-re-measured-54-from-55-and-the-residue-is-contiguous-runs).

**Source**: two independent 2026-08-09 routine polish observations, both proposing the same
instrument — "a detector that reports entries with Japanese examples containing no ⟦⟧ at all
would size this block precisely and is cheap to write — it is a pure absence test, no judgment
needed" (on 06842–06844), and "worth a targeted detector for entries with kanji-bearing
examples and no ⟦…⟧ at all" (on 06844/06975/07099). **Sized 2026-08-09 by whole-corpus scan**,
and as with P46 the measurement changes what the item is.

**Run unfiltered, the proposed detector returns 23,404 of 30,316 entries (77%)** — and the
split says exactly what it is measuring:

| Population | Entries |
|---|---|
| Zero-link, **below** the polish frontier (`next: 06845`) | **55** |
| Zero-link, **above** the frontier | 23,349 |

To within 0.2%, "entries with kanji examples and no links" *is* "entries the frontier has not
reached." That is the finding already recorded in the Informational note above and in
[Inline Link Integrity](../topics/inline-link-integrity.md#zero-link-entries--23404-and-not-a-defect),
whose standing instruction is **"do not file a zero-link detector."** These two observations
are its sixth and seventh independent rediscovery, which is itself the item's most useful
signal (see P46 and the "why these keep being rediscovered" section on that page).

**Filtered to below the frontier, however, the same scan yields a real 55-entry queue** — the
strict sibling of [P46](#priority-46-notes-fully-linked-examples-completely-bare-33-entries--behind-the-frontier).
P46 is *half*-linked entries the frontier passed; this is *un*-linked entries the frontier
passed. Both are work no cursor will ever return to. The 55 are almost entirely contiguous
blocks, not scattered singletons:

| IDs | n | Character of the block |
|---|---|---|
| 03949–03969 | **21** | single-kanji `〜` entries (空/元/後/今/最/際/初/所/前/相/…), created 2026-01-13 |
| 06006–06014 | 9 | anatomy block (脊椎, 人体, 毛細血管, リンパ, 骨髄, 呼吸器, 消化器, 循環器, のどぼとけ) |
| 06670–06676 | 7 | i-adjective block (細長い, 平たい, みずみずしい, ずぶとい, かいがいしい, 生真面目, 愚か) |
| 06593–06598 | 6 | mixed nouns (保存料, 納品書, 骨組み, オフサイド, オンデマンド, ペーパーレス) |
| 06363–06367 | 4 | ピント, 編み物, ミシン, 断層 |
| 04620, 04623 | 2 | 乗り越える, 追い越す (15 and 10 examples each) |
| 03100, 03356, 04974, 06109, 06703, 06747 | 6 | isolated |

**Detect**: entry has ≥1 `examples[].japanese` containing kanji, zero `⟦…⟧` anywhere in the
file, and numeric ID < the comprehensive frontier. Mechanical.
**Scope**: **55 entries**. **Status**: open, batch-ready, no cursor needed.

**These are not unlinkable entries.** Spot-checks confirm ordinary linkable vocabulary sitting
bare: 03949 空〜 has 空港/予約/迎える/行く; 06670 細長い has 廊下/指/島国; 06006 脊椎 has
病気/手術/座る. And their `modified` stamps are polish-run dates spread across 2026-03 to
2026-07 (03949: 2026-04-07; 06671: 2026-07-28; 06674: 2026-07-28), so these entries were
*worked on* — repeatedly — and the linking step simply did not run on them.

**Why the block shape matters**: 21 of the 55 are one run of single-kanji `〜` entries, whose
own headword is a bound morpheme rather than a word. A linking pass that reached them may have
stopped because the *headword* is not linkable and treated the entry as done — a plausible
session-shape cause distinct from P46's "ran out of context." Whoever works this queue should
take that block last and decide the convention for bound-morpheme entries once, rather than 21
times.

## Updates 2026-08-09 (wiki harvest)

**Informational refresh: zero-link entries 23,294 → 23,404, and the frontier lost ground while
the number was measured.** Between the 2026-08-07 sizing (frontier 06723) and this one
(frontier 06845) the frontier advanced **122 IDs** and the zero-link population **grew by 110**.
That is the [frontier-versus-growth gap](../topics/quality-metrics.md) expressed on the link
metric for the first time, and it lands on the pessimistic side of the 44–50% band: the linking
lane is running at roughly break-even against new-entry supply, so the two-year projection on
`topics/inline-link-integrity.md` is not conservative. No change to the standing instruction —
the answer remains Tooling 49/82 (a read-only link *suggester*), not a detector.

**P11 (semantic tag drift) — the remaining scope is confirmed, but "extend `TAG_MIGRATION`" is
now measured and will not close it.** The 2026-08-09 accuracy-review of 28901–29294 found
off-vocabulary tags in **54 of 550 entries (~10%)** and proposed extending
`build/check_tag_drift.py`'s migration map with the eight families it met
(`medical`→`health`, `food-drink`→`food`, `body`→`body-part`, `motion`→`movement`,
`sensation`/`manner`/`physical-property`→`descriptive`, `people`→`person`, `time`→`time-general`,
`animals`→`animal-bird`). Whole-corpus scan, 2026-08-09:

- **1,848 entries / 2,436 uses** still carry a baselined off-vocabulary semantic tag —
  confirming the 08-08 figure (1,902) and its slow decline.
- The uses are spread over **643 distinct invented labels**.
- `TAG_MIGRATION`'s current **9 rules cover 181 uses (7%)**. The **ten families this
  observation names cover 202 uses (8%)**.
- Coverage curve: top 25 labels → 29%; top 50 → 43%; top 100 → 59%; top 200 → 75%.
- **300 labels are used exactly once**; 486 labels (76% of the vocabulary) are used ≤3 times,
  accounting for 734 uses.

The head is thin and the tail is enormous, so a hand-maintained 1:1 map is the wrong shape for
this item: doubling the map from 9 rules to ~25 would take it from 7% to 29%, and reaching even
three-quarters of the backlog needs **200 hand-written rules**. This does not retire the
mechanical path — it re-scopes it. The right instrument for the tail is the one already
measured at ~97% apply rate on exactly this class: the reviewer's off-vocabulary flag, which
names a destination per instance without anyone enumerating the vocabulary in advance. Extend
`TAG_MIGRATION` with the top ~25 labels because it is nearly free, and plan the remaining ~70%
as accuracy-review coverage, not as map maintenance.

**Retired before filing: "a detector for furigana wrappers whose left side contains no kanji."**
The 2026-08-09 accuracy-review offered this as "a cheap, high-precision check" after entry
28929's `{苦悶|くもん}{に|み}ちた` (dropped 満) was found. Measured against all **1,110,639**
wrappers in the corpus:

| Left-side class | n | Verdict |
|---|---|---|
| hiragana, reading identical (`{おもちゃ\|おもちゃ}`) | 65 | harmless identity wrapper |
| **katakana** (`{データ\|でーた}`) | **276** | separate class, see below |
| numeral / symbol (`{3\|さん}`, `{400\|よんひゃく}`, `{〇\|まる}`, `{々\|おの}`) | 47 | **correct and useful** |
| hiragana, reading differs | **3** | the only candidate defects |

391 hits, of which at most 3 are worth looking at — **under 1% precision**, not "high." The
observation's own trigger case is not in the result, because that run fixed it. Worse, the
47-item "other" bucket is a **fourth undocumented brace convention**: numerals are wrapped to
give their spoken reading (`{1990|せんきゅうひゃくきゅうじゅう}`), which is precisely what
furigana is for, and a naive no-kanji rule would flag every one as malformed. Filed to
[Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md); this is the *fourth*
detector proposal in three months killed by an undocumented convention, which is the same
mechanism recorded in [Instrument Defects vs. Corpus Defects](../topics/instrument-defects.md).

**Informational (new, and genuinely tiny): wrappers with an empty side — 3 instances.** The one
high-precision rule hiding inside the proposal above is "a wrapper with an empty surface or an
empty reading": `00961_koko {どこ|}`, `23799_nojuku {キャンプ|}`, `25376_junkansuru {うまく|}`.
All three are malformed and none is caught by any current instrument. Three entries is not a
sweep, but the rule costs one regex and belongs in the validator rather than in a queue.

**Open policy question: 276 katakana wrappers give katakana a hiragana "reading."** Measured at
276 instances / 230 entries / 208 distinct surfaces (`{データ|でーた}` ×8, `{バランス|ばらんす}`
×5, `{チーム|ちーむ}` ×4 …), with only 2 identity cases. This is large, consistent, and looks
deliberate rather than accidental, so it needs a **policy decision before any sweep** — the
project's stated rule is that readings are always hiragana and that furigana annotate kanji;
katakana needs no reading aid, but a hiragana gloss of a katakana word is at least internally
consistent with "readings are hiragana." Recorded, not queued.

**Refined: keigo-label drift on plain vocabulary (16 entries, not 82).** The 2026-08-09 polish
run fixed 00806 両親 (tagged `formality: formal` + `politeness: honorific`, although the
honorific form is ご両親 and 両親 itself is plain) and suggested "similar keigo-label drift may
sit on other family-term entries." The obvious rule — `politeness` is honorific/humble but the
headword has no お/ご prefix — returns **82 entries and is mostly correct**: 申す, いらっしゃる,
いたす, 参る, 召し上がる are genuinely keigo verbs with no prefix. Adding "POS is a noun" and
"the gloss does not itself say humble/honorific/polite/respect" narrows it to **16**, of which
several are unambiguous drift of the 両親 kind — `03189_riyousha` 利用者 "user, customer" tagged
honorific; `01454_sonkei` 尊敬 "respect, esteem" tagged honorific (the word *means* respect, it
does not *encode* it); `04142_kenson` 謙遜 "modesty" tagged humble; `07430_haiguusha` 配偶者
"spouse" tagged humble — while others are genuine (`14566_heika` 陛下, `27145_kakka` 閣下,
`23324_sunshi` 寸志). **The distinguishing error is treating a word whose *meaning* is
deference as a word whose *use* is deferential**, which is the same meaning-versus-use confusion
[Schema Tag Reliability](../topics/schema-tag-reliability.md) documents for semantic tags.
Status: open, 16 entries, needs per-entry judgment (not batch-ready).

**Reinforced: P35 stale `noentry` residue is much larger than the frontier's own rate suggests.**
Two 2026-08-09 observations independently make this point — a single 8-entry priority batch
turned up two stale markers (05834 しょげる → 29029_shogeru; 01910 勃発する → 11823_boppatsu),
both in entries the sequential frontier had already passed, and a separate run found 04262's
`⟦擦れる→擦れる：noentry⟧` resolving to 28426_kosureru. Current detector state: **6,026 `noentry`
instances / 5,348 distinct pairs in 2,689 entries**, with the mechanical A1+A2 classes at
**1,423 pairs / 1,658 instances**. The priority lane reaches entries the frontier cannot
revisit, which is why it keeps surfacing these; the standing recommendation — run
`check_stale_noentry.py --mechanical` as its own `systemic-fix` pass rather than waiting for
polish to stumble on them — is now backed by three independent sightings in one day.

**Method note carried from the same run: sweep stale `noentry` in entry-ID order, not detector
order.** The 2026-08-09 systemic-fix run verified **180 pairs with zero polysemy false
positives** and reported why: consecutive entries repeat the same families (counter compounds
六千/八百/三十人, day-of-month readings 十四日/十五日, compass compounds 北側/西日本, katakana
loanwords ウール/ミトン/コンポ), so one context read settles a dozen pairs. This is a
throughput property of the *ordering*, and it should be the default for any future P35 batch.

**Reinforced: tag errors cluster on the category axis, not the narrowness axis.** The
2026-08-09 accuracy-review adds 財布 tagged `clothing`, けが tagged `body-part`, 定期券 tagged
`person` to the pile, and restates the operational consequence: these are flatly wrong parents,
worth applying on sight, and unlike in-list narrowness nits they are not a matter of taste. The
same run measured its in-list substitution flags at **0 of 12 applied** — the twelfth-plus
consecutive confirmation of that noise family. Both halves belong to the standing prescription
in [Tooling 17](tooling-backlog.md): suppress in-list narrowness suggestions entirely, keep
off-list migrations and category errors. No change to the item; the evidence is now
overwhelming and the fix remains unshipped.

## Priority 51: Stale calendar-month links — 29 entries point 「月」(がつ) at the *moon* entry

**Source**: 2026-08-10 routine polish observation (fixed in 00956 か月 during that run, the rest
left). **Measured 2026-08-10 by whole-corpus grep: 29 entries**, confirming the filing exactly.

The suffix entry `30418_gatsu` (〜{月|がつ}, the calendar-month suffix) was created after the
links were written, so every earlier linking pass had nowhere to point but `02230_tsuki`
({月|つき}, moon / month-as-a-period). The result is 29 entries whose 一月/七月/九月 examples
link the learner to the wrong word.

**Detect**: literal string `がつ}→月：02230_tsuki` anywhere in an entry file.
**Fix**: replace `⟦{月|がつ}→月：02230_tsuki⟧` with `⟦{月|がつ}→月：30418_gatsu⟧`; bump `modified`.
**Scope**: **29 entries**. **Status**: open, batch-ready.

This is one of the rare items that qualifies as **provably safe under the §B "purely-mechanical"
carve-out**: the reading がつ is unambiguously the counter-suffix reading of 月 — the moon sense
is つき and the month-period sense is つき/げつ — so the surface `{月|がつ}` cannot denote the
target the link currently names. No per-entry semantic judgment is required, only the usual
post-sweep validation and spot-check.

**Generalise before running it.** The same shape must exist wherever a suffix, counter, or
bound-morpheme entry was created *after* the homographic free noun it shares a kanji with:
every link written in the interval points at the noun. A worthwhile companion scan is "inline
links whose surface reading disagrees with the reading of the entry they target" — that is a
mechanical string comparison against `entries_index.json` and would find this family and its
siblings in one pass, rather than one stale-suffix filing at a time. Filed as
[Tooling 97](tooling-backlog.md).

## Priority 52: Kanji headwords with no furigana at all (259 entries) — invisible to every furigana instrument

**Source**: 2026-08-09 routine polish observation. **Measured 2026-08-10 across all 30,345
entries: 259 entries**, confirming the filed count exactly.

`CLAUDE.md` states the rule without qualification — "All kanji must have furigana:
`{漢字|かんじ}` — in headwords, examples, AND notes." These 259 entries carry a bare kanji
headword: `萼`, `言い値`, `召し上がる`, `ご覧になる`, `赤ん坊`, `瓦礫`, `早炊き`.

**The reason nothing catches them is confirmed in the source.** `build/find_missing_furigana.py`
reads the headword at line 101 — but only to label its output. The `fields_to_scan` list it
builds immediately after contains notes, definition explanations, and examples; **the headword
field is never appended to it**. So the one field every learner reads first is the single field
the project's furigana scanner does not scan, and `make check-furigana` reports these entries as
clean.

**Severity is presentational, not data loss.** The rendered page still shows the reading — it is
emitted as a separate `entry-reading` line under the headword — so the learner is not left
without it. What breaks is the ruby presentation every other entry has, plus per-kanji reading
attribution on multi-kanji headwords (瓦礫 renders as two kanji links with a single がれき
underneath, where 「{瓦|が}{礫|れき}」 would attribute each).

**This is an active regression, not settled debt** — the creation-date distribution says the
leak is in the current entry-creation path:

| Entry created | Bare-kanji headwords |
|---|---|
| 2026-07 | **126** |
| 2026-05 | 83 |
| 2026-08 (10 days) | **24** |
| 2026-06 | 19 |
| 2026-01 | 7 |

At 24 in the first ten days of August the backlog is growing by roughly 70/month, so a cleanup
sweep run without the validator check would be re-filed within a quarter.

**Detect**: `re.search(r'[一-鿿]', headword) and '{' not in headword`. One line.
**Fix**: mechanical where the `reading` field is the whole headword's reading (single kanji:
萼 → `{萼|がく}`; opaque compounds: 瓦礫 → `{瓦|が}{礫|れき}` needs the per-kanji split);
**needs care** for mixed kana/kanji forms — 言い値 → `{言|い}い{値|ね}`, 召し上がる →
`{召|め}し{上|あ}がる` — where the kana in the headword must be aligned out of the reading first.
Roughly half the 259 are the easy class.
**Scope**: **259 entries**. **Status**: open, batch-ready in two passes (easy class first).

**Ship the validator check with the sweep, not after it.** Adding the headword to
`fields_to_scan` costs one line and converts this from a recurring cleanup into a one-time one.
Filed as [Tooling 96](tooling-backlog.md).

## Priority 53: Counter entries with an empty `cross_references` array (39 of 79)

**Source**: 2026-08-10 routine polish observation on the basic-tier counters — 00620 台,
00650 枚, 00666 冊 and 00688 本 each named rival counters in their notes prose while all four
had a completely empty `cross_references` array. Those four were fixed in that run.
**Measured 2026-08-10: 79 counter-POS entries, 39 still with zero cross-references.**

The counters are the project's cleanest closed set: every counter contrasts with a handful of
others over the same referent class (flat things / long things / bound things / machines), and
the contrast is nearly always already written out in the entry's own notes. That makes this the
rare cross-reference queue where the target set is enumerable in advance rather than inferred
per entry.

**Detect**: `metadata.tags.pos` contains `counter` and `cross_references` is empty.
**Fix**: per entry, extract the counters its own notes contrast it with and add them as
`contrast` references (the shape 00620 台 now has); add the `related` link to the homographic
free noun where one exists (00620 → 13039 台). Semantic verification per entry, but the
notes supply the answer.
**Scope**: **39 entries**. **Status**: open, batch-ready.
**Sample**: 00196 か所, 00108 歩, 00407 トン, 00443 位, 02446 軒, 27628 合, 27655 着,
27977 坪, 28160 便, 28497 一箱, 19765 号車, 30419 客.

## Priority 54: The compound-verb conjugation preamble (37 entries) — bounded, pending a curator call

**Source**: filed twice — 2026-08-10 routine polish (removed by hand in 06850, 06853, 06854,
06855) and again on the 06856–06864 block in the same run's second observation.
**Measured 2026-08-10: 37 entries** whose notes open with a negative / te-form / past triad and
also carry a `FORMATION:` section.

Every one of those three lines restates information the entry's `conjugation` field already
holds and the page already renders as a table, so the preamble is duplicated content occupying
the top of the notes — the position a learner reads first and where the FORMATION and USAGE
material should be.

**Detect**: notes contain `FORMATION` and the first ~400 characters mention negative, te-form,
and past. **Scope**: **37 entries** (01935, 03102, 06703, 06856, 06857, 06859, 06861–06864,
06972, 06974, …). **Status**: **needs-decision** — batch-ready the moment it is taken.

**Why it is parked rather than open.** The polish run that removed four of them noted the
consistency risk and left the rest, and that instinct is right in general — but the measurement
changes the calculus. The filing assumed the preamble is a dictionary-wide convention that
would be expensive to break; it is **37 entries**, a creation-batch habit rather than a house
style. Either decision can therefore be executed in a single run, which makes this cheap to
settle rather than something to keep deferring.

## Updates 2026-08-10 (wiki harvest)

**P50 holds at exactly 55 while the frontier advanced 15 IDs — and the re-scan retires the
"contiguous runs" proposal that was filed twice this window.**

Two polish observations (06845–06849, then 06850–06855) proposed the same new instrument: *"a
detector that reports contiguous runs of zero-link entries so systemic-fix can target the
densest block instead of the frontier lane crawling them one at a time."* The premise behind it
is correct and was well observed — the zero-link population **is** creation-batch-shaped, not
scattered drift. The prescription does not survive measurement.

Run over all 30,345 entries, the zero-link population is **23,420**, and it decomposes into
**34 runs total** — of which three are almost all of it:

| Run | Entries | Share |
|---|---|---|
| 18726–30554 | 11,810 | 50.4% |
| 09809–18724 | 8,847 | 37.8% |
| 07442–09477 | 2,036 | 8.7% |
| **top three combined** | **22,693** | **96.9%** |
| the other 31 runs | 727 | 3.1% |

So a run-length detector returns "everything above the frontier" in three rows instead of
23,420 — a prettier rendering of the same fact the standing **"do not file a zero-link
detector"** instruction already records. "The densest block" is not a target; it is the
unpolished dictionary. These are the **eighth and ninth** independent rediscoveries of that
finding, and the second time in two windows that splitting the population at the cursor is what
turns it into work.

**The cursor split, meanwhile, brings good news.** Zero-link entries *behind* the frontier are
**55** — identical to the 55 measured on 2026-08-09, and **zero** of the 15 IDs the frontier
crossed since (06845–06859) entered the set. [P50](#priority-50-zero-links-anywhere-behind-the-frontier-55-entries--the-other-half-of-p46)
is a fixed, non-growing queue: the polish lane is linking what it passes, so this backlog can be
cleared once and stay cleared. Total zero-link count rose 23,404 → 23,420 (+16) purely from
the 43 new entries created in the window.

**P11 (semantic-tag drift): the contaminated band extends into 06926–07265, and the ratchet is
blind to all of it.** A cross-model accuracy pass over 240 never-reviewed entries there returned
**147 tag flags on 135 entries (56% of entries flagged)**, and on adjudication the great
majority were gross-category errors rather than breadth nits: {司書|ししょ} (librarian) tagged
`clothing`, カビ (mold) tagged `weather`, {打率|だりつ} (batting average) tagged `animal-mammal`,
{位牌|いはい} (Buddhist memorial tablet) tagged `electronics`, ぴえん tagged `food`,
{一触即発|いっしょくそくはつ} and {危機一髪|ききいっぱつ} both tagged `geography`. 77 were
corrected in that run.

**Every one of those tags is in `VALID_SEMANTIC`.** `validate_tags.py` and the
`--check-no-new-unknown` ratchet see a clean entry, because what is wrong is not the vocabulary
but the attachment — the right label on the wrong word. The band looks creation-batch-shaped
(these entries were created 2026-01), which means the rest of 07266+ probably carries it too and
the accuracy sweep will take ~9 more runs to crawl there at ~240 entries/run. Recorded as the
strongest current argument for a dedicated systemic-fix pass over 07266+ rather than waiting for
the sweep. (The in-list apply rate this window — **58.9%**, against 5.0% last window — is this
block and nothing else; see the metrics page's 34th refresh.)

**P35 (stale `noentry` markers): two more sightings, plus a class the detector cannot see.**
02052 狂う marks 狂気 `noentry` though 27800_kyouki exists; 04438 報道 marks 各 `noentry` though
00449_kaku exists. Both are ordinary P35, detected by `build/check_stale_noentry.py`. The
*related* miss is not: エリア in 04438 sat entirely naked — no link and no `noentry` marker —
though 10726_eria exists, and nothing detects a bare word with no marker at all. The cheap
approximation proposed in the observation is sound and worth building: **a katakana run of ≥2
characters appearing in an example outside any ⟦…⟧ that matches a `word_id_lookup.json`
headword key**. Katakana needs no tokenizer, which is exactly why it is the tractable slice of
the naked-word problem. Filed as [Tooling 98](tooling-backlog.md).

**RETIRED: "formality `formal` with no supporting REGISTER note" as a detector.** Proposed from
the 06926–07265 accuracy pass, where ゴミ箱, デバイス, 獣医, 観客席, プレッシャー, 手入れ and
打合わせ all carried `formal` with nothing in the notes supporting it. Measured across the
corpus: **5,079 entries carry `formality: formal`, and 4,357 of them (85.8%) have no REGISTER
note.** The detector returns six-sevenths of the population it is meant to discriminate within.

This is the **third** instance of the rule recorded on
[Inline Link Integrity](../topics/inline-link-integrity.md) after the zero-link and
kanji-in-example cases: *when a coverage detector returns most of the population, it is
measuring a documentation habit, not a defect.* Most entries simply do not write REGISTER
sections; `formal` with no note is the norm. The discriminating rule is the one §A already
applies — flag only when the entry's **own notes contradict the label** (バイト's notes saying
"Casual", {有給休暇|ゆうきゅうきゅうか} tagged `informal`) — and that rule needs no new detector
because the reviewer already implements it. The observation also measured the band's `formal`
share at 14% against the dictionary's 16.7%, i.e. the block is *not* contaminated; the filing
was a false alarm about a real-looking pattern, correctly caught by its own author's check.

## Updates 2026-08-11 (wiki harvest)

**The "25 entries with no semantic tags at all" block does not exist — and the dictionary-wide
population is 79, not 105.** A 2026-08-11 accuracy-review observation reported "a contiguous
block of 25 (07832–07861) that no current check reports" as a second defect class alongside
off-vocabulary tags. Re-measured this harvest across all 30,365 entry files: **zero** entries in
07566–08065 lack a semantic tag, so the block is not there now. The likely explanation is in the
same run's own report — its first census read `entry["tags"]` instead of
`entry["metadata"]["tags"]` and returned "0 off-vocabulary tags" for a band that had 208. A
wrong-path read on this schema returns `{}` rather than raising, so **both** of that census's
numbers are suspect, the reassuring one and the alarming one. (The general lesson is filed as
tooling item 101.)

The correction is worth more than the retraction, because the real population is bounded and its
shape is different from what was filed:

| Measure | 2026-08-04 | 2026-08-11 |
|---|---|---|
| Entries with no semantic tag | 105 | **79** (19 basic, 4 core, 56 general) |

The largest contiguous runs are nowhere near the reported band — **08635–08659 (13)**,
**03948–03969 (12)**, **02814–02924 (10)**, **08812–08840 (10)**; the remaining ~34 are
scattered singletons. So this stays what the informational section above called it — a small,
non-growing queue — and the right instrument is a `--check missing-semantic` predicate inside
`check_tag_drift.py` rather than the new standalone `check_missing_semantic_tags` script the
observation proposed. Four batches clear half of it. **Do not re-file this as a large discovery**;
it is 79 entries and has been shrinking.

**P20 (out-of-taxonomy tags) is confirmed as a defect class genuinely distinct from P11, and it
remains the largest batch-ready target on this page.** Two 2026-08-11 observations, from
different runs, isolate the distinction the last several updates had been blurring:

- **P11** = tags that are *in* `VALID_SEMANTIC` but wrong for the headword (司書→`clothing`,
  打率→`animal-mammal`). Invisible to `validate_tags.py` **and** to the CI ratchet; only a
  semantic judgment finds them.
- **P20** = tags that are simply *not in* `VALID_SEMANTIC` (`document`, `food-cooking`,
  `culinary-technique`, `japanese-food`, `office-equipment`, `housing`, `tax`, `machine`…).
  Mechanically detectable, mostly 1:1 migratable, and **invisible to CI for a different
  reason**: `--check-no-new-unknown` grandfathers existing tags into
  `unknown_semantic_baseline.json` and blocks only *new* ones, exactly as designed.

Both are creation-batch artifacts with the same cause — a session invents a local taxonomy per
topic run and never checks it against the closed list — and the observation shows it plainly:
07472–07481 kitchen cuts, 07482–07494 office documents, 07495–07501 home/utilities, each with
its own invented vocabulary. The 07566–08065 band measured **208 of 500 entries (42%)** affected,
inside the 40–53% band this page has recorded for every creation-cohort block since July.

Current dictionary-wide residue, measured this harvest (post the 2026-08-11 migration of the
07566–08065 band): **2,065 `unknown-semantic` flags across 1,603 entries**; total tag drift 6,720
flags / 6,220 entries (sole-general 3,681, semantic-mismatch 957,
concrete-noun-domain-mismatch 15, proverb-idiom-mismatch 2). The standing recommendation —
a dedicated `systemic-fix` run on `check_tag_drift.py --check unknown-semantic` rather than
incremental per-band accuracy-review — is now made for at least the sixth time and is the single
highest-value batch-ready item in the queue: 1,603 entries, a ready detector, and a documented
1:1 migration map.

**P11: the contaminated band runs continuously from 06926 to at least 07430, and per-band
crawling will not finish it.** A 2026-08-11 polish observation corrected **57** in-vocabulary
wrong-category tags in 07266–07430 (`transportation` on 虚栄心/進捗/捗る, `furniture` on
目処/初対面/日常茶飯事, `electronics` on 愛嬌/同人誌/待ち合わせ, `animal-insect` on けだるい,
`color` on 音色, `geography` on 宿命/井戸端会議, `existence` on ひらめく/揉める) — the **second
consecutive band at ~30%**, after 06926–07265 at 56% flagged. Two consecutive bands mean the
block is at least 500 entries wide; at ~300 entries per accuracy-review run it needs ~7 more
runs, against one or two for a dedicated sweep over **06926–07600**. Same conclusion as P20,
reached from the other defect class.

**P43 (06800–07100, 96% unlinked) takes a third confirming cohort.** The 06865–06875 block
(na-adjectives and compound nouns created 2026-01-18) arrived with **zero** inline-link coverage
in both examples *and* notes, and full coverage is a tier-1 requirement, so each entry cost far
more on the frontier lane than a targeted sweep would. Alongside it in the same eleven entries:
**5 sole-`general` semantic tags** (06870 世帯, 06871 手掛かり, 06873 取り柄, 06874 言い分, plus
06869 窮屈 mis-tagged `emotion`), all replaceable with precise in-list tags → [P13](#priority-13-overuse-of-general-as-sole-semantic-tag);
and **5 entries naming a synonym or antonym in their notes with that word absent from
`cross_references`** (06865 and 06869 had entirely empty lists while their notes carried an
explicit ANTONYM section) → queue item `crossref-missing-from-notes-prose`. Three separate
backlog items, one creation cohort, which is the argument for banded sweeps in one more form.

**Formality-vs-REGISTER: a cost argument, not a precision argument — and it does not overturn
the 2026-08-10 finding above.** The previous update concluded that flagging only when an entry's
own notes contradict its label "needs no new detector because the reviewer already implements
it." A 2026-08-11 observation adds the piece that reasoning was missing: of 19 formality flags,
**13 confirmed and 6 rejected purely by reading the entry's own REGISTER sentence**
(`formal` on しんどい whose note reads "Casual. Very common in everyday conversation"; `vulgar`
on むしゃむしゃ whose note reads "Casual"; and rejections where the note read "Neutral to
formal", supporting the label). All 19 adjudications are reproducible with no API call. So both
findings stand: the *rule* is right and needs no change, and a detector implementing it moves
this family off the OpenRouter budget **wherever an entry has a REGISTER section to read**.
That caveat is the limit, and it is a real one: only 555 of 5,068 `formal` entries carry such a
section (measured 2026-08-05), so the detector is a **ratchet on entries that document their
register**, not a dictionary-wide sweep — which is exactly why the standing scope estimate for
`tag-formality-contradicts-register-note` is 5 entries even though the reviewer keeps flagging
~10 per sweep. What the 19/19 result establishes is that the reviewer is spending API budget to
compute something deterministic on the subset where it can be computed at all. Queue item
`tag-formality-contradicts-register-note` (open, batch-ready); tooling item 77.

## Updates 2026-08-12 (wiki harvest)

Twenty-six observations from the 2026-08-11/12 polish, candidates, new-entries, systemic-fix
and accuracy-review runs. **No new priority came out of them.** Two filings that read as new
findings turned out to be re-discoveries of items already open and batch-ready, and the
harvest's contribution is to say what each re-discovery costs and what has actually changed
underneath it. The third finding re-scopes P20 — and lands on the *opposite* conclusion from
the one the observation implied, because a decision already on record answers it.

### P24 re-filed a fourth time (braced inline-link base forms) — the item has never been worked

The 2026-08-12 polish run filed "37 entry files contain links written as
`⟦{広|ひろ}さ→{広|ひろ}さ：00105_hirosa⟧`; the remaining ~36 are a clean, mechanical
systemic-fix candidate." That is queue item `inline-link-braced-base-form`, open since
2026-07-25, **promoted to priority 5 on 2026-07-30 precisely because three separate polish runs
had already found it independently**, with notes that already record the 00697–00716 and
00966–00984 clustering.

Re-measured 2026-08-12: **35 entries** (36 in the queue, minus 00704 which the filing run
fixed). Two contiguous runs — 00697–00716 (16) and 00965–00988 (14) — plus 01484, 04471,
09760. **34 of the 35 were created in 2026-01**, so the cohort is closed and cannot regrow.

The number is not the news. The news is that a **provably-safe, user-visible, 35-entry,
one-regex item at priority 5 has now been found independently by four polish runs across
nineteen days and worked by none of them.** The 2026-07-30 promotion note predicted exactly
this — "worked zero times because priority 24 is below anything the systemic-fix selector
reaches" — and promoting it did not change the outcome. Whatever the selector is doing with
`batch_ready` items at priority 5, it is not reaching this one; that is a selector question,
not a backlog question, and it is the fifth re-discovery that will otherwise arrive next week.

### P43's block is no longer upcoming — the polish frontier is inside it

Filed twice within a day: "06893 to about 06905" (13 entries), and "06884–06887 and probably the
surrounding range". Both are inside `inline-link-block-06800-07100`, open since 2026-08-06 at
288 of 301 entries (96%) with zero inline links.

What is new is a boundary. Measured over 06880–06980: **79 of 101 IDs have no inline link
anywhere**, and the unbroken zero-link run begins at **06896** — which is the current value of
`polishing/tasks/comprehensive/progress.txt`.

The existing item was filed on a prediction: "the comprehensive frontier crawls through it at
roughly one-fifth normal speed — a polish run that meets it spends its whole entry budget
writing links from scratch." **The frontier has now met it**, and the filing run independently
measured the predicted cost from the inside: "budget roughly one entry per 8–10 minutes." The
prediction and the observation agree, which retires the question of whether the block is worth
routing around.

So the decision the 2026-08-06 filing deferred is now live, and it has a deadline rather than a
priority: either hand 06896–07100 to a `systemic-fix` link-building pass and let the frontier
resume above it, or accept that every polish run for the next several weeks spends its whole
budget in this block. At this window's frontier rate — 36 IDs, the fastest in the series — the
lane is inside the block for roughly six more runs. Note the filter the existing queue item
carries: run it *after* `inline-link-stale-noentry` and the wrong-target detector, or writing
288 entries of new links manufactures a fresh cohort of spurious `noentry` markers.

### P20 re-scope: the population, the hot spots, and why the map should *not* be extended

The 2026-08-11 accuracy-review run asked for a dictionary-wide scan — "worth scanning for other
hot-spot ID blocks rather than treating P20 as an even dictionary-wide sweep." Done, with a
third measurement it did not ask for that changes what the answer means.

**1. Population, post-migration.** **1,364 of 30,385 entries (4.5%)** carry a semantic tag
outside `VALID_SEMANTIC`: **1,635 instances**, **486 distinct labels**. Down from 1,603 entries
on 2026-08-11 — the difference is the 189 entries the 2026-08-12 accuracy-review migrated.

**2. Concentration confirmed, and the hot spots are not where it was measured.**

| Block | Off-vocab entries | Share of block |
|---|---|---|
| 09000–09499 | 239 / 500 | **48%** |
| 08000–08499 | 201 / 500 | **40%** |
| 10000–10499 | 141 / 485 | 29% |
| 20000–20499 | 127 / 498 | 26% |
| 22000–22499 | 86 / 500 | 17% |
| 16500–16999 | 58 / 479 | 12% |

The top two blocks hold **32% of the whole population** between them; the top five hold 58%;
**23 of 62 blocks are completely clean**. The filing measured 8066–8565 at 68% — a band
straddling the 08000–08499 hot spot and the clean 08500–08999 block (7%), which is how one
band's rate overstated both the level and the uniformity.

**3. The map covers 8%, and that is an argument for the standing decision, not against it.**
`TAG_MIGRATION` in `build/check_tag_drift.py` has nine rows. Against the current population it
fully clears **111 of 1,364 entries (8.1%)** and covers **135 of 1,635 instances (8.3%)**. The
residue is **477 labels, 243 of them used exactly once**; top-50 covers 48% of instances,
top-200 covers 80%.

The natural reading — *extend the map* — has been proposed three times (2026-07-27 "~50 safe
renames", 2026-08-01 "22 mappings", 2026-08-02 "curated top-50 = 48.4%") and was **decided
against on 2026-08-07**, on the queue item itself, after measurement: a static map must choose
a destination **per tag name** (486 names, most of them singletons), whereas the reviewer
chooses one **per entry** and never has to generalise — at 99.4% precision and ~$0.5 per 1,000
entries. This harvest's 8.1% is the same finding from the other end, and it is the fourth time
the extension has been proposed. Recording it here so the fifth proposal meets the decision
instead of the temptation: **the map stays at nine rows; the reviewer is the instrument.**

Two things follow that are *not* blocked by that decision:

- **Route the instrument by density.** If the reviewer is the tool, point it at 09000–09499 and
  08000–08499 rather than letting the sweep arrive there in ID order — a third of the
  population at 40–48% density, against a sweep that has been averaging ~240 entries/run
  through blocks that are 23-of-62 clean.
- **Fix the descriptions.** Several pages, and §A's semantic-tag policy in `prompts/routine2.md`,
  point at "the 1:1 migration map" as though applying it were the job. It is one entry in
  twelve, and the decision of record says it will stay that way. See tooling item 105.

## Updates 2026-08-13 (wiki harvest)

Twenty-six observations from the 2026-08-12 wiki/polish/accuracy-review runs and the 2026-08-13
new-entries/polish runs. Two become new priorities, both because this harvest measured them
dictionary-wide instead of filing the local sighting; one long-running hypothesis is refuted by
its own measurement; and the rest go to the tooling backlog and entry follow-ups.

### Priority 55: Inline links that resolve to a homophone of the intended word — 23 instances

A 2026-08-13 new-entries run found 04231 振り返る linking the base form 顧みる at
`13656_kaerimiru`, which is 省みる — a different verb with the same reading. It asked for a
sweep. This harvest ran the sweep, and the useful result is how small the class is after the
2026-07-31 `systemic-fix` batch already repaired 87 of them (機能→昨日, 性格→正確, 会社→外車).

Of 273,656 inline links, 1,491 have a base form that matches neither the target's headword nor
its reading, and **97% of those are legitimate conventions** — affix headwords (`〜的`),
slash headwords (`速い／早い`), する-verb bases against noun headwords, and orthographic
variants. The residue that is a real defect: **about 23 links whose base form is a different
word that merely shares the target's reading.**

| link base → target | reading |
|---|---|
| 終身 → `09947` 就寝 | しゅうしん |
| 用地 → `04088` 幼稚 | ようち |
| 詩集 → `05411` 刺繍 | ししゅう |
| 詩的 → `05630` 指摘 | してき |
| 詐称 → `18658` 査証 | さしょう |
| 天賦 → `07376` 添付 | てんぷ |
| 進水 → `09238` 心酔 | しんすい |
| 専任 → `11607` 仙人 | せんにん |
| 書架 → `11740` 初夏 | しょか |
| 五時 → `16131` 誤字 | ごじ |
| 深く → `14884` 不覚 | ふかく |
| 科す → `00537` 貸す | かす |
| 感 → `01076` 缶 · 温 → `02550` 恩 · 系 → `02691` 計 · 純 → `03342` 順 · 吸 → `01057` 酢 · 腑 → `09512` 負 · 焼 → `03096` 〜屋 | single kanji |

Source entries: 00181, 00230, 00365, 00445, 00451, 00504, 02139 (×2), 02494, 02496, 02628,
02772, 03445, 03460, 04472, 04475, 04479, 04484, 04489, 04840, 04875, 04955, 05984.

**Why it is worth doing as a batch**: the link resolves, renders and clicks, so nothing in the
project can see it — `validate.py` checks that the ID exists, and the §4 semantic self-check
demonstrably does not read links (the 2026-07-31 batch's self-check returned zero findings on
the dimension it had just repaired). The fix per instance is to repoint or drop one link, and
the evidence is in the two entries. A second, cosmetic residue of ~13 (陽射し/日差し,
産まれる/生まれる, 鍼/針, 龍/竜, 棹/竿 …) is the right word spelled non-canonically in the base
slot; leave it. Full filter cascade and method:
[Inline Link Integrity](../topics/inline-link-integrity.md) → "Shape 1, measured dictionary-wide".

### Priority 56: Body-part idioms and their body-part nouns never link to each other

The 2026-08-12 polish run's six frontier entries — 肩をすくめる, 眉をひそめる, 足を運ぶ,
顔を出す, 胸を張る, 腰を据える — all had zero or one cross-reference, and **none linked to the
body-part noun that heads the idiom**, even though each entry's notes list two or three sibling
idioms built on the same noun. The reverse direction is equally bare: 02192 肩, 04267 眉,
00972 胸, 02210 腰 link only to neighbouring body parts, never to the idioms that use them.

The shape is deterministic and therefore detector-friendly: **an `expression` entry whose
headword begins with a noun that has its own entry, where neither entry references the other.**
Scope is unmeasured — the observation covers 06880–06980, where such idioms cluster, but the
family runs throughout the dictionary. Worth measuring before scheduling; the detector is the
work, not the fix.

### The "contiguous off-vocabulary tag band" hypothesis is refuted

A 2026-08-12 accuracy-review measured 46% off-vocabulary density in 08851–09350, matched it to
the 46% previously measured in 08066–08565, and proposed that the dictionary-wide remainder sits
in one contiguous batch-creation band that a single scoped `systemic-fix` could clear far more
cheaply than rediscovering it 500 entries at a time.

Measured across all 62 blocks (2026-08-13): **there is no band.** Affected IDs run 00333–27818,
**24 of 62 blocks are completely clean**, and only five exceed 10% density — 8000–8499 (40.2%),
10000–10499 (29.1%), 20000–20499 (25.5%), 22000–22499 (17.2%), 16500–16999 (12.1%) — together
holding 54% of the population. The two 46% blocks the observation generalised from are adjacent
to one of those five hot spots, which is why they looked like the start of something.

The good news underneath it: the queue is **1,134 entries / 1,329 instances / 431 tag names**,
down from 2,530 / 3,208 / 687 one week earlier — **55% cleared in seven days** by the
accuracy-review lane. The correct scheduling consequence is unchanged from the 2026-08-12
harvest's independent conclusion: route the reviewer by block density, and expect the tail to be
scattered singletons. Details and the accompanying `TAG_MIGRATION` coverage finding in
[Schema Tag Reliability](../topics/schema-tag-reliability.md).

### For the curator: two tag-vocabulary rulings would close ~75 instances and stop a detector loop

Not a cleanup item — a decision only the curator can make, restated here because two separate
2026-08-13 observations arrived at it from different directions.

`VALID_SEMANTIC` has no tag for **place/location** (`location` 24 + `place` 23 instances in use
off-list) and none for **sound/perception** (`perception` 12 + `sound` 9 + `sensation` 7; the
only tag in that region is `music`). Entries that decline to invent a tag fall back to
`general` — 音 `00743`, 物音 `03633`, 騒音 `03315`, 足音 `02991` are all sole-`general` — which
means the P13 sole-`general` detector re-surfaces them on every sweep and **no sweep can ever
fix them**, because there is nothing correct to change them to. Adding two names to a Python set
closes both. `schema.json` deliberately has no tag enum, so this is not a schema change.

### `inline-link-block-06800-07100` re-discovered a fifth time, now from inside the block

The 2026-08-13 polish run reports the 06902–06909 idiom entries created 2026-01-18 as having
zero inline links and recommends a targeted 06900–06999 sweep. That is the open queue item, at
288 entries and priority 7 — and the frontier has now entered it, so each polish run pays the
per-entry linking cost the sweep would pay once. The routing decision the 2026-08-12 harvest
flagged as "live rather than deferred" has been live for a day and is still open; nothing new to
file, and the fifth filing is the strongest argument yet for working it.

## Updates 2026-08-14 (wiki harvest)

Thirty-four observations from the two 2026-08-13 accuracy-review/polish runs, the 2026-08-13
new-entries run, and the 2026-08-14 accuracy-review and polish runs. Two become new priorities;
one filing's premise is refuted and the item survives in a different shape; and one standing
curator escalation is **half-closed by measurement** rather than by a ruling.

### Priority 57: Cross-reference targets that hold no references of their own — 1,550 entries

**Source**: two polish runs, 2026-08-13 (00812 宿題, 00970 緑, 01392 毛, 01510 星, 02206 草,
02265 野菜 — "six for six") and 2026-08-13 again (02266 休み, 02273 映画, 02883 先, 00151 括弧,
00374 私鉄, 01351 お見舞い — six for six a second time). The second filing added a hypothesis:
*"the asymmetry report may be under-reporting because it only looks at entries that have at
least one reference."*

**The hypothesis is wrong, and the item is real anyway.** `find_asymmetric_references()` in
`build/find_merge_candidates.py` iterates over *sources* and reports every A→B with no B→A, so
a target holding zero references is exactly the case it does report. Nothing is invisible.

What is true is that its output is undifferentiated. Measured over the current corpus:

| | count |
|---|---|
| references with a `target_id` | 21,444 |
| symmetric pairs | 6,242 |
| **asymmetric one-way pairs** | **8,633** |
| …of which the target has **no references at all** | **2,183** |
| distinct such bare targets | **1,550** (19 basic, 202 core, 1,329 general) |
| entries with no references of either kind, dictionary-wide | 17,763 |

The 2,183-pair sub-class is the one worth batching, because for those entries the back-reference
decision is already made: another entry has judged the relationship worth recording, and the
target has no reference list to weigh it against. The remaining 6,450 pairs are genuine
editorial judgment — the target has references and chose differently — and should not be swept.
Most-pointed-at bare entries: 01433 正月 (10 inbound), 01464 注意, 02504 秘密, 04117 温泉 (8
each), 00478 持つ, 02773 裁判, 03663 予算 (7 each).

**Distinct from `crossref-missing-from-notes-prose` (1,402)**, which is about words named in
notes prose; this one needs no text analysis at all — it is two set operations over `target_id`s.
**Detect**: pairs from `--asymmetry-only` whose target's `cross_references` **and**
`prominent_see_also` are both empty. **Scope**: 2,183 pairs / 1,550 entries. **Status**: open.
The twelve entries the two polish runs fixed by hand are already out of the set, which is why
none of them appears in this measurement.

### Priority 58: Baseball vocabulary split between `sports` and `leisure` — 24 entries

**Source**: 2026-08-13 accuracy-review (09309–09808), which counted "about 30 `sports` and about
12 `leisure`" and proposed a cheap sweep. Measured dictionary-wide over entries whose gloss or
definitions mention baseball: **132 entries — 83 `sports`, 24 `leisure`, 12 sole-`general`, 12
other, 1 both.** `sports` is the convention by better than three to one.

The `leisure` cohort: アウト, 大リーグ, 代打, ソフトボール, 野球 itself, ストライク, 防御率,
ノーヒット, 変化球, ノック, キャップ, フォアボール, ツーストライク, ダッグアウト, スリーボール,
バッター, 野手, 豪速球, 外野, 内野 …

**The false-positive family is inside the cohort, not outside it.** キャップ (a cap), ノック (a
knock) and アウト (out, in several senses) mention baseball in *one* sense of a polysemous entry;
`leisure` may be right for them on other grounds and the tag should be judged against the
headword, not the mention. So this is a per-entry systemic-fix batch of ~24, not a mechanical
substitution — small enough that the verification is the cheap part. **Status**: open,
batch-ready. **Detect**: gloss/definitions match `baseball` AND `semantic` contains `leisure`.

### The `location`/`urban` off-vocabulary family has an in-list destination — half the standing escalation closes

The 2026-08-13 harvest escalated to the curator that `VALID_SEMANTIC` has no place/location tag
and no sound/perception tag, so ~75 off-list instances have nowhere to go and cycle through the
sole-`general` detector forever. The 2026-08-13 accuracy-review run then answered the first half
from inside the corpus: the street/district words (路地裏, 裏通り, 繁華街, 住宅街, 地下街) belong
with the **54 street/district/area entries that already use `geography`** (横丁, 表通り, 並木道,
道端, 沿道, 区域, 付近), with `transportation` for road infrastructure (交差点, 車線, T字路).

Measured this harvest: `geography` is used by **617 entries**, so it is a well-established
destination rather than a stretch, and the off-list place family is **~40 instances** —
`place` 23, `location` 13, `places` 2, `location-area` 1, `regional` 1. All of it maps to
`geography`, and the mapping belongs in `check_tag_drift.py`'s `TAG_MIGRATION`.

**The sound/perception half of the escalation stands**: `perception` 11, `sound` 9, `sensation`
7, `taste` 2 — 29 instances with no in-list destination, and 音/物音/騒音/足音 still sitting at
sole-`general`. A third gap was filed this window from 04095 足跡: no in-list category covers a
*physical trace or mark*. Two names in a Python set close the first and third; the escalation is
now smaller and sharper than when it was raised.

**Off-vocabulary queue re-measured**: **998 entries / 1,161 instances / 394 distinct names**,
down from 1,134 / 1,329 / 431 on 2026-08-13 and 2,530 / 3,208 / 687 on 2026-08-06. The lane is
still the fastest-clearing on this wiki.

### Register markedness on ordinary vocabulary — 231 basic/core nouns

**Source**: 2026-08-14 polish (03552 徹夜 carrying `style: slang` + `domain: colloquial`, when
the slang item was オール, mentioned in its *notes*; 04095 足跡 carrying `formality: formal` +
`style: literary`, of footprints in snow). Both look like a tagger that read the notes instead
of the headword — the same failure mode P17 (`tag-formality-over-applied`) and
`politeness-denotes-vs-encodes` record.

Measured over basic- and core-tier noun entries — words that are foundational vocabulary by
definition and therefore should almost never be register-marked: **231 carry a marked register**.

| tags | entries |
|---|---|
| `formality: formal`, no marked style | 173 |
| `style: literary`, neutral formality | 26 |
| `style: literary` + `formality: formal` | 19 |
| `style: slang` | 8 |
| `style: archaic` (± formal) | 5 |

Samples: 00147 価格 (price) `formal`; 00146 果実 (fruit) `formal`; 00129 自宅 (one's home)
`formal`; 00028 近頃 (recently) `literary`; 00157 各自 (each person) `literary`; 00012 ×/バツ
`slang`. Some of these are defensible — 給与 and 夫妻 really are the formal members of their
pairs — so this is a **review queue, not a fix list**, and it is the tier restriction that makes
it worth reviewing: the same predicate over the whole dictionary returns 5,079 `formal` entries,
which the 2026-08-10 harvest already retired as a detector for exactly that reason. Restricting
it to basic/core cuts it to 231 and to words whose register is decidable in one glance.
**Status**: open, review-queue shaped.

### Re-discoveries needing no new item

- **`inline-link-block-06800-07100`**, sixth, seventh and eighth filings: 06910–06913
  (interjections/fillers), 06915–06918 (colloquial particles), 06919–06925 (っていう, ていうか,
  及び, 並びに, 若しくは, 故に) — all reported as *zero* links in examples and notes. The frontier
  is inside the block and paying per-entry what the sweep would pay once. Unchanged advice.
- **`inline-link-split-compound` (P47, 443 pairs)**: 03795 我々's notes link 私 and たち as two
  adjacent separate links although 28351_watashitachi (私たち) has its own entry. Textbook
  instance, and the shape the polish run proposed as a check — adjacent link pairs whose
  concatenation is itself a headword — is precisely P47's detector.
- **`inline-link-stale-noentry` (P35, 920 pairs)** and **`stale-calendar-month-links` (29)**:
  three more sightings — 06916 ぜ pointing わよ/のよ at `noentry` with 30248/30249 live, 03500
  半ば pointing 月 (がつ) at `noentry` three times with 30418 live, 04091 利害 pointing 利 at
  `noentry` with 29142 live. Both detectors already find these. The 2026-08-13 polish run adds
  the most useful datum yet for scheduling it: **a fourth consecutive band (03167–03756, 181
  pairs) where the external self-check raised zero objections to a link-target substitution**,
  so the context-checked short-base fix is now well evidenced as safe. Four polish runs in three
  days have each cleared a handful by hand; one `systemic-fix` run would clear the class.
- **`tag-sole-general` (3,681)**: two independent density readings this window — 47 of 129 tag
  flags in 09309–09808 were sole-`general` narrowness swaps (all rejected as a family, per
  standing policy), and 7 of a 33-entry self-check sample in the 03xxx band carried
  `semantic: ["general"]` on a word with an obvious in-list category (all seven applied). The
  contrast is the whole argument for working it deterministically: the *detector's* hit rate in
  the 03xxx band is high and the *reviewer's* re-report of the same population is noise the
  project pays for by the range.

## Updates 2026-08-15 (wiki harvest)

Nineteen observations from the 2026-08-14 accuracy-review, polish, new-entries and systemic-fix
runs and the 2026-08-15 accuracy-review run. **Two become new priorities, both provably
mechanical and both visible on the live site.** Two proposed detectors are **retired by
measurement** — they were the same sighting described twice, and neither survives counting. One
filing asking for a "dedicated backlog item" turns out to be asking for an item that has existed
since 2026-08-01. And one sighting that named a small closed set turns out to be a convention gap
five tags wide, which needs a curator ruling rather than a sweep.

### Priority 59: Single-kanji サ変 verbs whose generated potential form is not Japanese — 32 entries

**Source**: the 2026-08-14 `new-entries` run (30635–30653), which hit the bug while creating
30647 処する, fixed that one entry by hand, and filed the class with two named witnesses
(08053 察する, 14629 面する) and a detection rule.

**The rule is right and the scope is 32 entries.** `build/add_conjugations.py` builds the
potential form of every `conjugation.type: "suru"` verb as 〜できる. That is correct for
漢語+する compounds (勉強する → 勉強できる) but wrong for the single-kanji サ変 verbs, which take
〜せる: 愛せる, 発せる, 接せる. 愛できる is not a possible Japanese word, and it is currently
printed in the conjugation table on 32 entry pages of the live site.

Measured 2026-08-15 (`conjugation.type == "suru"`, headword's pre-する portion one character,
reading the `Potential` row out of `conjugation.forms`):

| | count |
|---|---|
| `suru`-type conjugation tables | 4,592 |
| …whose stem is a single character | 33 |
| …**carrying the impossible 〜できる potential** | **32** |
| …already correct | 1 (30647 処する, fixed by hand at creation) |

The 32: 01811 愛する, 02045 関する, 02126 対する, 02129 達する, 02297 適する, 02401 罰する,
08053 察する, 09142 屈する, 09168 臆する, 09794 熱する, 11664 介する, 11906 制する, 11966 反する,
11970 博する, 11971 即する, 12003 呈する, 12402 属する, 12567 徹する, 12776 扮する, 12920 接する,
13400 有する, 13401 瀕する, 13639 発する, 14342 要する, 20837 さする, 21490 没する, 23992 議する,
25545 値する, 27887 害する, 28650 脱する, 29124 喫する.

**Batch-ready and mechanical**: rewrite the `Potential` row's `affirmative`/`negative` from
〜できる/〜できない to 〜せる/〜せない. The transformation cannot introduce an error for this class
because 〜できる is not a possible form of it. Fix `add_conjugations.py` first (Tooling 122) or
the next `--force` run reintroduces all 32.

**One of the 32 is a different and worse defect.** 20837 さする is tagged `verb-godan` (correctly
— 擦る is a godan verb) but carries a **サ変 conjugation table end to end**: さします, さした,
さしよう, さすれば. Every row is wrong, not just the potential. It is in this list only because
its headword happens to end in する. See Entry Follow-ups; the deterministic check that found it
is Tooling 120.

### Priority 60: Katakana wrapped in furigana braces — 275 instances / 229 entries

**Source**: the 2026-08-14 `systemic-fix` run (P35 band 03757–04458), which found
`{ラベル|らべる}` in 03995 宛名, noted that neither `validate.py` nor `find_missing_furigana.py`
can see the inverse case (furigana supplied where none is wanted), proposed the detector cut
("brace groups whose base is all-katakana"), and recorded the scope as unmeasured.

**Measured 2026-08-15: 275 instances across 229 entries**, spread over the whole ID range rather
than one creation batch — 00138 through 30640.

| field | instances |
|---|---|
| `notes` | 135 |
| `examples[].japanese` | 129 |
| `definitions[].explanation` | 11 |

It renders. `docs/entries/00000/00138_kaisetsu.html` currently emits
`<ruby>ニュース<rp>(</rp><rt>にゅーす</rt><rp>)</rp></ruby>` — the live site prints にゅーす as
ruby text above ニュース, which is information-free and reads as a mistake to the learner the
ruby is for. This is the first class on this page that is both invisible to every furigana
instrument *and* visibly wrong to a reader.

**Provably safe to strip.** Of the 275, **271** have a reading that is the exact kana
transliteration of the katakana base, and 3 more repeat the katakana unchanged
(`{ホスト|ホスト}` in 30640, `{コンピュータ|コンピュータ}` in 27356, `{ホルモン|ホルモン}` in
28936) — for all 274, deleting the wrapper and keeping the base loses nothing.

**The 275th is a genuine reading error the class was hiding**: 23394 二枚貝 carries
`{カキ|がき}` — oyster, read がき instead of かき. No furigana instrument could ever have found
it, because they all key on kanji. Fix that one by hand; sweep the other 274.

### Priority 61: `validate_tags.py`'s 11 standing errors — mechanical, and stalled on one ruling

**Source**: the 2026-08-14 polish run, which reported "11 pre-existing errors unrelated to any
entry touched this run: five 〜ずる verbs … plus a proper-noun entry".

**The count is right; the composition is not.** Measured 2026-08-15 —

| class | count | entries |
|---|---|---|
| 〜ずる verbs: `verb_class: ichidan` vs POS `verb-irregular` | 5 | 09029 準ずる, 13144 案ずる, 18394 乗ずる, 19600 禁ずる, 20377 断ずる |
| proper nouns carrying `organization-name` without the `proper-noun` umbrella | **3** (not 1) | 08853 NGO, 08907 NBA, 08908 MLB |
| the three irregular verbs themselves | 3 | 00006 ある, 00254 来る, 00392 する |

The middle three are a one-line fix each. The 〜ずる five need a call the validator cannot make:
〜ずる verbs *are* morphologically irregular and *do* inflect like ichidan verbs, so either tag
is defensible and the two fields simply disagree about which axis they describe. The last three
are the dictionary's genuinely irregular verbs, where `verb_class` is already carrying the
precise value (`suru`, `kuru`, `irregular`) and the POS tag is carrying the coarse one — that is
arguably the validator's bug, not the entries'. Worth resolving as a set, because as long as
these 11 sit in the output every future run has to re-read them to confirm they are not its own.

### A "small closed set" that is a five-way convention gap — grammar terminology

**Source**: the 2026-08-14 accuracy-review run: "Part-of-speech term entries drift to the
`education` tag. 名詞 and 音読み were both fixed this run; 形容詞 is still tagged `education`
while 動詞 and 助詞 correctly use `grammatical`. A small closed set — worth a one-shot sweep."

**There is no convention to sweep toward.** Measured over 26 grammar-and-writing terminology
headwords, the cohort uses **five different semantic tags**:

| tag | count | examples |
|---|---|---|
| `grammatical` | 8 | 主語, 助詞, 動詞, 名詞, 活用, 命令形, 目的語, 過去形 |
| `language` | 8 | 品詞, 感動詞, 漢字, 自動詞, 音読み, 命令形, 目的語, 過去形 |
| `education` | 6 | 他動詞, 形容詞, 接続詞, 訓読み, 語彙, 送り仮名 |
| `general` | 4 | 助動詞, 平仮名, 片仮名, 述語 |
| `communication` | 3 | 副詞, 敬語, 文法 |

(Three entries carry two tags, which is why the column exceeds 26.)

The sharpest evidence is inside the filing itself. The run reports fixing 名詞 and 音読み
together — and it fixed them to **different tags**: 名詞 is now `grammatical`, 音読み is
`language`. Its sibling 訓読み is still `education`, and 他動詞 (`education`) and 自動詞
(`language`) split the same pair. The reviewer is not drifting toward `education`; it is picking
freely among four in-list tags that all fit, because the project has never chosen one.

**This needs a curator ruling, not a systemic-fix run**: is the house tag for metalinguistic
vocabulary `grammatical` or `language`, and does `education` belong to the学習 sense at all?
Once chosen, the sweep is 26 entries and trivial. Filed to `reviews/needs_curator.txt`.

### Retired 2026-08-15: both proposed formality detectors

Two runs on 2026-08-14 filed what is recognisably the same sighting from opposite ends, each
proposing a mechanical detector. Neither survives measurement. Per the Instrument Defects case-10
rule, the commands are quoted.

**(a) "`formality: formal` where the entry's own REGISTER line says neutral."** Filed by the
polish run, which saw it on three of four frontier entries (06927, 06928, 06929). Scanning all
**5,067** `formality: formal` entries for a `REGISTER` line containing "neutral" returns **8**,
and six of the eight are correct as tagged — they say "Neutral **to** formal" (01182 尋ねる,
06289 新規, 06938 疎外感, 03103 について), "Formal/polite for sense 1; neutral … for sense 2"
(07801 粗相), or "Somewhat formal/literary; neutral to negative *connotation*" (09232 辟易する),
where "neutral" is describing connotation, not register. At most two are candidates. The class
the run saw was real and the run fixed it; the residue does not justify an instrument. The
existing queue item `tag-formality-contradicts-register-note` (scope 5) is updated to reflect
this rather than left implying a live batch.

**(b) "`formality: formal` where the only 'formal' string in notes attaches to a
cross-referenced word."** Filed by the systemic-fix run from 03922 削る, 04077 火傷, 04222 取り除く.
All three **already read `formality: neutral`** — the same run fixed them, so the filing describes
its own completed work. Testing the proposed rule anyway (formal-tagged entries whose notes
contain "more formal"/"is the formal"/"formal equivalent" preceded by Japanese text) returns
**419** entries, and the sample is dominated by the *correct* case: 00122 寺院 ("寺院 is more
formal than お寺"), 00147 価格 ("the formal term for price"), 00252 苦情, 00264 給与 — all
entries where the formal word being described **is the headword**. Separating "this word is
formal" from "that other word is the formal one" is the semantic judgment, and it is the whole
of the task. Not mechanizable as specified.

### Re-discoveries needing no new item

- **"A dedicated systemic-fix backlog item listing every sole-`general` entry"** (2026-08-14
  accuracy-review; 13 of 39 applied fixes that run were sole-`general` swaps) —
  `tag-sole-general` has been open and `batch_ready` since 2026-08-01. Re-measured 2026-08-15 at
  **3,642 entries** (3,151 general, 442 core, 49 basic), down from 3,681 on 2026-08-14, i.e. the
  hand-clearing is running at roughly 40/day against a class of 3,600. The second sighting the
  same window (systemic-fix: 7 of 36 sampled in 03900–04450, ~19%) is a density reading of the
  same population, consistent with the dictionary-wide 12%.
- **Off-vocabulary tags cluster by creation batch, not ID neighbourhood** (2026-08-15
  accuracy-review, 22 in 10687–11200 concentrated in 10688–10810 and 10968–10975) — a shape note
  on `unknown-semantic-tags` (998 entries), not a new item. The run's own conclusion, that a
  deterministic `VALID_SEMANTIC` sweep finds these far more cheaply than a paid model review,
  is the same finding as Tooling 118 below and is now the third independent measurement of it.
- **Stale `noentry` markers** (2026-08-14 polish, 04930 からし/水戸) — P35 /
  `inline-link-stale-noentry`, already the lowest-numbered open batch-ready item.
- **Compound-element inline links are decided by the target entry's notes, not its gloss**
  (2026-08-14 systemic-fix; 込む → 00719, 思い → 10248, four applies that gloss-only screening
  would have rejected) — the 2026-08-13 年寄り臭い → 01133 臭い precedent, now with three
  witnesses. Recorded on [Inline Link Integrity](../topics/inline-link-integrity.md); no item.
- **The 06900+ zero-link band** (filed twice this window as a "creation batch that skipped
  linking, worth a targeted sweep") — it is not a batch artifact. See
  [Inline Link Integrity](../topics/inline-link-integrity.md#zero-link-entries--23404-and-not-a-defect),
  where this harvest replaced the single-window growth note with a 66-day measurement.

## Updates 2026-08-15 (wiki harvest, run 2)

Twelve observations from the three runs since the midday harvest. One new priority, one
re-measurement, and — the useful part — **the zero-link "creation cohort" claim finally has an
explanation for why it keeps coming back.**

### Priority 62: `・` bullets in notes — 2,496 entries the note scorer silently penalises

**Source**: the 2026-08-15 polish run, which met eight of them on the priority lane, converted
them, and watched each score go 77 → 87.

`.claude/skills/vocabulary-notes/SKILL.md` mandates `- ` (hyphen-space) for note bullet lists.
`build/score_note_quality.py` credits only `- `. Entries that use `・` instead therefore lose a
fixed 10 points for a defect that is purely typographic, and those 10 points are enough to push
an otherwise-sound entry up the notes priority ranking.

Measured 2026-08-15 across all 30,464 entries:

| | count |
|---|---|
| entries with line-initial `・` in `notes` | **2,496** |
| `・` bullet lines across them | 18,089 |
| of the **top 500** entries on `polishing/priority/notes.txt`, carrying `・` bullets | **130 (26%)** |

The 26% figure is the item's real argument. It is lower than the filing's "the priority lane is
currently full of them", but a quarter of the worst-scoring queue being mis-ranked for a
character substitution is still the largest single distortion measured on that ranking, and it
compounds with the [item 20](tooling-backlog.md) staleness problem: the lane spends a quarter of
its attention re-deciding entries whose notes are fine.

**Why this is batch-safe.** The transformation is `^・` → `- `, per line, **notes field only**.
`・` is also the katakana middle dot (ローマ・カトリック, an author's ・-joined name), so a
global replace would corrupt running text — but a line-initial `・` in a bullet list cannot be a
mid-word separator. This is the shape §B calls "provably cannot introduce an error", and it is
still worth validating and spot-checking before commit.

**Sequencing note, from P16's standing lesson**: nothing generates `・` bullets today (they are
hand-written), so unlike P59/P60 there is no generator to fix first. But `make priorities`
should be re-run *after* the sweep, or the ranking keeps the pre-sweep order.

### P50 re-measured: 54 (from 55), and the residue is contiguous runs

Re-scanning below the current frontier (`next: 06947`) gives **54** zero-link entries, one fewer
than the 2026-08-09 sizing — the frontier advanced ~100 IDs in six days and cleared one. The
item is not converging on its own.

What the re-scan adds is the *shape*: the 54 are not scattered. They are six contiguous runs —
03949–03969 (21), 06006–06014 (9), 06670–06676 (7), 06593–06598 (6), 06363–06367 (5), plus
seven singletons (03100, 03356, 04620, 04623, 04974, 06109, 06747). A block of 21 consecutive
IDs is a lane that skipped a directory's worth of work, not entries that individually resisted
linking. Whoever works P50 should work it run-by-run; the runs are large enough that a single
session clears three of them.

### The zero-link "creation cohort" is the polish frontier seen through the creation-date axis

**Source**: the 2026-08-15 polish run — "four of the five entries with no links at all were
created in the same 2026-01-18/19 window; inline linking appears to have been added to the
entry-creation flow after that batch, so the January-18/19 cohort is systematically unlinked
rather than randomly so."

This is the **eighth** independent rediscovery of the finding that
[Inline Link Integrity](../topics/inline-link-integrity.md#zero-link-entries--23404-and-not-a-defect)
already records with a standing "do not file a zero-link detector". It is also the first one to
arrive on a new axis, and measuring that axis explains the whole recurrence pattern.

Zero-link rate by `metadata.created` date:

| created | zero-link / total | rate |
|---|---|---|
| 2026-01-16 | 9 / 1,098 | 0.8% |
| 2026-01-17 | 5 / 525 | 1.0% |
| **2026-01-18** | **207 / 590** | **35.1%** |
| 2026-01-19 | 234 / 240 | 97.5% |
| 2026-01-20 onward | ~100% every day | ~100% |

That is a clean cliff on 2026-01-18, and it looks exactly like a process change. It is not one.
Entries were created in ID order, so creation date is a proxy for entry ID, and the same scan by
ID band puts the cliff between **06000–06999 (7.5% zero-link)** and **07000–07999 (98.9%)** —
i.e. at `next: 06947`, the comprehensive-polish frontier, to within one band.

The creation-flow hypothesis is also refuted directly by policy: CLAUDE.md has always said
*"Never add inline word links (⟦...⟧) during entry creation — those are added in a separate
polishing step."* Linking was never in the creation flow, so it cannot have been removed from it.

**Why this matters beyond the correction.** The recurrence has been treated as sessions failing
to read the standing note. The mechanism is simpler and not the sessions' fault: a polish run
sees four or five unlinked entries, checks one shared field to explain them, and *any* field
that correlates with entry ID — creation date, creation batch, ID neighbourhood — returns a
perfect-looking cluster, because the frontier is a step function in ID. The finding will keep
being rediscovered on new axes until the sessions' own instrument answers it. The cheap fix is
not another wiki note: it is to make the frontier visible where a polishing session already
looks (see [Tooling 124](tooling-backlog.md)).

### Note-header kanji without furigana — 8 entries, and the global scanner already reports them

**Source**: the 2026-08-15 new-entries run — English note headers that embed a Japanese suffix
(`THE 〜物 SERIES:`, `THE 〜顔 SERIES:`) carry bare kanji, because the kanji reads as a display of
the suffix rather than as running text. Two of that run's 20 entries had the shape; both were
caught by `find_missing_furigana.py` and fixed before the PR.

Dictionary-wide the surviving population is **8 entries**: 00950 (`NOTE ON 九:`), 01588
(`TYPES OF 公務員:`), 02156 (`READINGS OF 角:`), 03114 (`SIMILAR 大 COMPOUNDS:`), 23465
(`TYPES OF 御神体:`), 26870 (`RELATED ～内 COMPOUNDS:`), 26879 (`RELATED ～力 COMPOUNDS:`),
26884 (`RELATED 初～ COMPOUNDS:`).

All 8 are reported by `find_missing_furigana.py` today, so this is not a detector gap — it is
an eight-item queue that nobody has drained, and it is small enough to fold into whichever run
next touches those IDs rather than to schedule. The observation's second suggestion (write the
header in plain English and annotate the suffix in the sentence below) is the better standing
convention and belongs in the vocabulary-notes skill; recorded for the curator, since wiki
sessions do not edit skills.


### P63. Collocation-section heading near-synonyms — 730 entries, heading-only rename

**Source**: 2026-08-16 polish run, via [Tooling 125](tooling-backlog.md).

`check_consistency.py --issue no-collocations` flags 6,759 entries, **55% of them wrongly**
(Tooling 125). Most of that is a checker defect and is filed there. What remains here is the
genuinely mechanical residue: headings that are near-synonyms of a heading the dictionary
already uses overwhelmingly, where the rename loses nothing.

**Measured 2026-08-16 (30,484 entries), line-anchored on the `notes` field:**

| Heading | Entries | Action |
|---|---|---|
| `COMMON COLLOCATIONS:` | 19,928 | house standard — leave |
| `COMMON PATTERNS:` | 3,544 | house standard — leave |
| `COLLOCATIONS:` | 330 | → `COMMON COLLOCATIONS:` |
| `PATTERN:` | 154 | → `COMMON PATTERNS:` |
| `PATTERNS:` | 115 | → `COMMON PATTERNS:` |
| `USAGE PATTERNS:` | 92 | → `COMMON PATTERNS:` |
| `KEY PATTERNS:` | 39 | → `COMMON PATTERNS:` |

**Scope: 730 entries.** Transformation is line-anchored on the heading only; no body text moves.

**Explicitly out of scope, and this is the point of the item.** The filing run proposed
standardising *everything* to `COMMON COLLOCATIONS:`. That would destroy real distinctions:
`COMMON EXPRESSIONS:` (1,668), `SIMILAR EXPRESSIONS:` (531), `RELATED EXPRESSIONS:` (257) and
`PARTICLE PATTERNS:` (196) are different sections documenting different things, and merging
3,460 of them into "collocations" to satisfy a checker inverts the dependency. Fix the checker
(Tooling 125); rename only these 730.

### P64. Okurigana swallowed into the furigana ruby — 123 instances, invisible to every checker

**Source**: 2026-08-16 polish run (04651 {関節痛|かんせつつう} carries `{痛|いたみ}` where the
correct form is `{痛|いた}み`). Detection rule and confirmation that no existing detector sees
it: [Tooling 130](tooling-backlog.md).

Structurally the mirror of P60 (katakana wearing ruby): every furigana instrument asks *"does
this kanji have a reading?"*, and here it does — the reading has simply absorbed the okurigana
that belongs outside the braces. The site renders `<ruby>痛<rt>いたみ</rt></ruby>み` or drops
the okurigana entirely, and the learner reads a wrong reading for the kanji.

**Detection**: for a single-kanji base K with reading R, flag R when a proper prefix of R is a
common reading of K elsewhere (R occurs ≤3×, prefix ≥10×).

**Measured 2026-08-16: 90 distinct (kanji, reading) pairs / 123 instances.** The head of the
distribution is about as strong a signal as this project has produced —
`{切|きり}` ×1 vs `{切|き}` ×3,631; `{入|いれ}` ×1 vs `{入|い}` ×2,785; `{付|つき}` ×1 vs
`{付|つ}` ×2,585; `{受|うけ}` ×1 vs `{受|う}` ×2,236; `{痛|いたみ}` ×1 vs `{痛|いた}` ×810.

**Per-entry verification required — not mechanical.** The same output contains genuine readings:
`{止|とど}` is correct (とどまる), and a few entries deliberately wrap a whole word. 123
instances is small enough to open each one, which is the standard §B batch shape.

### P20 re-measured 2026-08-16 — 934 entries, and the hot spot is not where the filing run put it

The 2026-08-15 accuracy-review run (11501–12000) reported that "the 11750–11950 band is where
the dictionary's off-vocabulary semantic tags cluster… almost all of them sit above ID 11750.
The entry-creation cohort in that band evidently invented tag names freely."

**Measured against `VALID_SEMANTIC` across all 30,484 entries: 934 entries carry at least one
off-vocabulary semantic tag** (the queue's `unknown-semantic-tags` estimate of 998 is close and
mildly stale). By 1,000-ID band:

| Band | Entries |
|---|---|
| 08000–08999 | **201** |
| 20000–20999 | 162 |
| 16000–16999 | 102 |
| 22000–22999 | 86 |
| 10000–10999 | 68 |
| 27000–27999 | 57 |

**348 of the 934 sit below ID 11000**, and the single largest concentration — 201 entries,
**22% of the whole population in one band** — is 08000–08999, nowhere near the filing run's
range. The 11000-band is not in the top six.

This is the same reading error the 2026-08-15 harvest named: the run saw 31 off-vocabulary
corrections in its own 500-entry range and generalised the *band* from the *sample it was
looking at*. It is the third time an ID-correlated observation has produced a false cohort, and
it reproduces the 2026-08-07 finding that this population is **not** one contiguous creation
band (IDs then measured 00333–27818).

**Operationally the correction matters**, because the filing run's recommendation was right and
its target was wrong: a `systemic-fix` pass driven by
`check_tag_drift.py --check unknown-semantic` would clear these faster than the accuracy sweep
will reach them — and it should start at **08000–08999**, which is 201 entries of the highest-
precision flag family the project has (87–99% applied across five windows).

Top off-list names remain a long tail of near-misses: `time` 37, `body` 25, `place` 23,
`loanword` 23, `degree` 21, `quality` 19, `mathematics` 17, `interpersonal` 16.

## Updates 2026-08-21 (wiki harvest)

Harvested the 18 observations from the 2026-08-16 accuracy-review run, the 2026-08-17 polish
run, and the three 2026-08-20 runs (new-entries, systemic-fix P35, polish). Everything below
was **measured before filing**; two of the harvested proposals were refuted by the measurement
and are recorded as refutations rather than items.

### P50 is growing, and its members were *visited*, not skipped — 57 (from 54)

Two separate polish runs (2026-08-17 and 2026-08-20) proposed building a detector for "entries
with a non-empty `examples` array and no `⟦` anywhere". Dictionary-wide that population is
**23,460 of 30,504 entries (77%)**, which is the standing structural fact recorded in
[Inline Link Integrity](../topics/inline-link-integrity.md#zero-link-entries--23444-and-not-a-defect)
under an explicit *do not file a zero-link detector* ruling. These are the sixth and seventh
re-discoveries of that class. No new item.

What the re-measurement *does* add is a sharper reading of **P50**, the actionable
below-the-frontier residue:

| Measured | Frontier | Zero-link below frontier |
|---|---|---|
| 2026-08-09 | 06845 | 55 |
| 2026-08-15 | 06947 | 54 |
| **2026-08-21** | **06985** | **57** |

The frontier advanced 38 IDs in this window and P50 **grew by three**. The 2026-08-15 reading —
"the item is not converging on its own" — is too generous: it is diverging, and the frontier
lane is the source. All three new members (**06958 アジェンダ, 06959 ストレージ, 06960 デバイス**)
sit inside the band the lane crossed during the window.

The composition finding is stronger still. Because the comprehensive cursor stands at 06985,
**the lane has by definition already walked past every one of the 57**. They are not entries
the lane has yet to reach; they are entries it reached and left unlinked. Five of them
(03100, 06109, 06594, 06959, 06960) still carry a `modified` date from the 2026-01-19 creation
cleanup, meaning the lane visited them and changed *nothing at all*.

Spot-checks confirm the residue is not a legitimately-unlinkable class:

- **03949 {空|くう}〜** (prefix headword) — examples contain 予約, 空港, 迎え, 行く, 好き, and
  the notes list roughly a dozen 空〜 compounds. Every one is a lookup away.
- **06011 {呼吸器|こきゅうき}** — examples contain 病気, 入院, 喫煙, 大きな, 負担.

So the 2026-08-15 diagnosis ("a lane that skipped a directory's worth of work") should be
replaced with **"a lane that visited and silently dropped the linking checklist item"**. That
changes the remedy: the fix is not scheduling a backfill pass over the runs, it is understanding
why the checklist item is being dropped on whole contiguous blocks. The contiguity recorded on
2026-08-15 still holds — 43 of the 57 are in four runs (03949–03969 ×21, 06006–06014 ×9,
06670–06676 ×7, 06593–06598 ×6) — and contiguity is consistent with a per-session drop rather
than per-entry difficulty.

**Recommended for the curator**: P50 is small, bounded, batch-ready, and now known to be
growing. It is a good `systemic-fix` candidate, and the 2026-08-20 polish run's scripted
longest-match linker (filed as Tooling 131 this harvest) is the tool for it.

### The standing zero-link ruling is not reaching the sessions that keep re-proposing it

Seven re-discoveries of one class is a knowledge-routing failure, not seven independent
insights. `prompts/comprehensive_polish.md` and `.claude/skills/inline-word-links/SKILL.md`
were both checked this harvest: **neither mentions the zero-link ruling, P50, or
`inline-link-integrity.md` at all.** The answer lives in the wiki; the working prompt does not
point at it. This is the same shape as [Tooling 124](tooling-backlog.md#124-show-the-polish-frontier-where-polishing-sessions-already-look)
("show the polish frontier where polishing sessions already look") and is filed alongside it as
Tooling 133 rather than as a cleanup item, since the fix is a prompt line, not entry work.

### Priority 31 finally has a number — conjugation tables transcribed into notes, 46 entries

The 2026-08-20 polish run filed this as new: every entry in the 06972–06984 compound-verb block
opens its notes with a bulleted conjugation list
(`・{踏|ふ}み{込|こ}む → {踏|ふ}み{込|こ}まない (negative)` …) duplicating the entry's own
`conjugation` field, which the site already renders as a table.

It is **not new** — it is P31, carried in the queue as `notes-duplicate-conjugation-block`
(which itself supersedes the vaguer `notes-leading-conjugation-bullets`), and three polish runs
in 2026-07 already reported it from the same 066xx band. What has been missing since it was
filed is a **scope estimate**: both queue entries carried `scope_estimate: null`, which is why
the item has sat at `needs-detector` without ever being sized.

Measured dictionary-wide this harvest (notes containing ≥3 `→` and a
`・…→…(negative|past|te-form|polite|potential)` bullet): **46 entries**. Representative IDs:
03470, 03658, 03748, 03997, 06346, 06468, 06670–06677, 06705–06707. The queue entry is updated
with this figure.

Forty-six is small enough to change the item's character: the earlier reports read as if a whole
creation batch were affected, and the honest scope is two dozen-ish entries in the 066xx–067xx
band plus a scatter. It is one bounded `systemic-fix` batch once a detector exists.

Two reasons to remove it rather than leave it:

1. It is **redundant on the rendered page** — the reader sees the same forms twice, once as
   prose bullets and once as the conjugation table.
2. It **inflates the note-length signal** that drives the polishing priority lists, so these
   entries score as well-documented when the extra length is duplication.

`build/check_artifacts.py` does not currently recognise this shape (it reports only
`missing-target-id`, 40 instances). Adding it as a detector class is filed as Tooling 132.
Scope is small enough that the removal is a single bounded `systemic-fix` batch, but it is
**not** purely mechanical — some of the 46 may pair the list with genuine commentary that must
survive, so per-entry verification applies.

### P66. `⟦ください⟧` inline links are split across two base forms — 1,560 instances

Filed from the 2026-08-17 polish run. Links to 02899_kudasai are written both ways:

| Base form written | Instances | Share |
|---|---|---|
| `⟦ください→ください：02899_kudasai⟧` | 1,323 | 84.8% |
| `⟦ください→下さい：02899_kudasai⟧` | 237 | 15.2% |

The entry's own headword is `{下|くだ}さい`, so the 237 are the technically-correct form and the
1,323 are the common-practice form. Both resolve, so nothing is broken — this is a consistency
item, not an integrity one.

The observation asked "which base form wins". The recommendation is **`ください`**, on two
grounds: it is 85% of existing usage, and the auxiliary/polite-request ください that these links
almost always mark is conventionally written in kana. Normalising the 237 is a one-line
mechanical sweep once the ruling is made; normalising the 1,323 is not.

**This needs a curator ruling before any sweep runs**, and the ruling belongs in the
`inline-word-links` skill (recorded as a recommendation in Tooling 133's prompt-guidance note),
because the split will otherwise regenerate as fast as it is cleaned.

### Refuted: `check_stale_noentry.py` under-weights notes

The 2026-08-20 polish run's `[entry]` observation reported three stale `noentry` links living in
*notes* rather than examples (01107 欲しい `⟦～たい⟧`, 06983 組み込む `⟦{込|こ}む⟧`, 01384 君
`⟦あんた⟧`) and asked whether the detector weights notes as heavily as examples.

It does. `build/check_stale_noentry.py:135` scans `notes` and `usage_notes` before it reaches
`examples` at line 139. The three sightings are outside the ID bands the P35 sweep has covered
(the 2026-08-20 run worked 05000–05857), not detector blind spots.

Current P35 population, measured this harvest: **4,877 `noentry` instances / 4,372 distinct
pairs in 2,300 entries**, of which the safe mechanical bucket (A1+A2) is **452 pairs / 510
instances**. The item is healthy and simply has more bands to walk.

### Re-discoveries needing no new item

- **Sole-`general` on basic/core abstract nouns** (2026-08-17: 00770 勉強, 00882 最初 vs.
  legitimately-general 00829 場所) — already open and batch-ready; the observation's genuinely
  new content is the **"location/space" vocabulary gap** it identifies, which is added to the
  standing tag-vocabulary escalation below rather than filed separately.
- **The accuracy reviewer's `tags` dimension is dominated by in-list narrowness nits**
  (2026-08-16: 30 of 38 flagged entries) — this is [Tooling 111/118](tooling-backlog.md)'s
  measured family, reproduced for a sixth window in
  [Quality Metrics §21](../topics/quality-metrics.md).
- **Furigana screening's truncated-reading false positive** (2026-08-16: all 45 flags in
  12342–12900) — [Tooling 119](tooling-backlog.md#119-screening-prompt-should-quote-the-furigana-pair-verbatim-before-judging-it),
  now with two consecutive exactly-zero adjudication windows behind it (§21).
- **The "target's own notes declare a same-reading different word" P35 false positive**
  (2026-08-20, third firing, including the *identical* 08116_rokku pair rejected by hand at
  04562 on 2026-08-16) — the demotion rule proposed on 2026-08-16 is restated with its
  recurrence count as Tooling 134.
- **The 2026-08-11 proper-name P35 false-positive family needs a boundary** (2026-08-20:
  05387 ⟦日光⟧ → 03515_nikkou looks like a member but is not, because 03515's notes document the
  place-name sense). The operative test is **whether the target entry documents the proper-noun
  sense anywhere, not whether its lead gloss carries it** — the same "open the target rather
  than trusting its gloss" rule recorded on 2026-08-14. Added to the family's description in
  the P35 notes; no new item.

### For the curator: a "location/space" semantic tag

`VALID_SEMANTIC` has no tag for physical location or space. The 2026-08-17 polish run hit this
on **00829 場所**, where sole-`general` is not drift but the correct answer for lack of an
alternative. The standing off-list tally on this page independently shows `place` at 23
instances among the near-miss names. A `location` or `space` tag would close both the 00829
class and part of the off-list tail, and it is the second time a location tag has surfaced from
opposite directions (the `location`/`urban` family noted 2026-08-14 resolved to an in-list
destination for the *urban* half only). This is a one-word vocabulary decision that only the
curator can make.

## Updates 2026-08-23 (wiki harvest)

Harvested the 12 observations from the 2026-08-21 wiki run, the 2026-08-21 polish run, and the
2026-08-22 accuracy-review run. Everything below was **measured before filing**. One new
priority; two standing items get their hot spots identified; three harvested proposals were
refuted by the measurement and are recorded as refutations rather than items.

### P67. The interrogative family — 12 basic-tier entries, six semantic labels and four POS labels

Two observations arrived from opposite ends of the same family. The 2026-08-21 polish run found
**00534 誰** carrying the off-list semantic tag `interrogative` and guessed it was "likely a small
family (question words) worth migrating together". The 2026-08-22 accuracy-review run found
**01484 なぜ** tagged `pos: ["noun"]` while its near-synonyms どうして and なんで are both `adverb`,
and guessed "worth checking the whole interrogative family for the same slip". Measured, both
guesses are right, and the family is smaller and worse than either run supposed:

| Entry | Tier | `pos` | `semantic` |
|---|---|---|---|
| 00498 {何\|なに} | basic | `pronoun` | *(none)* |
| 00534 {誰\|だれ} | basic | `pronoun` | `interrogative` ← off-list |
| 00536 いつ | basic | `adverb` | `grammatical` |
| 00539 どこ | basic | `pronoun` | `direction`, `grammatical` |
| 00543 どう | basic | `adverb` | `interrogative` ← off-list |
| 00547 どれ | basic | `pronoun` | `grammatical` |
| 00551 どの | basic | `pre-noun-adjectival` | `grammatical` |
| 00834 どうして | basic | `adverb` | `descriptive` |
| 00927 どちら | basic | `pronoun` | `direction` |
| 01484 なぜ | basic | **`noun`** | `general` |
| 02924 どんな | basic | `pre-noun-adjectival` | *(none)* |
| 03875 {何\|なん}で | basic | `adverb` | `descriptive` |

**Twelve entries, all basic tier**, carrying **six different semantic labels** (`interrogative`
×2, `grammatical` ×4, `direction` ×2, `descriptive` ×2, `general` ×1, nothing at all ×2) and
**four POS labels**. This is the same shape as
[P38 (tag incoherence inside a closed lexical family)](#priority-38), but on a far more visible
population: these are among the first words any learner looks up, and they are a genuinely
closed set — there is no judgment call about membership, unlike the tableware family P38 was
measured on.

Three of the labels are defensible on their own and only look wrong beside each other
(`grammatical`, `direction` for the place/choice words, `descriptive` for the manner words).
Three are not:

- **`interrogative` (00534, 00543) is off-list** and therefore a P20 migration by definition;
  both are already in `build/data/unknown_semantic_baseline.json`.
- **`pos: ["noun"]` on 01484 なぜ is plainly wrong** — it is an interrogative adverb, and the two
  entries for the same meaning (00834 どうして, 03875 なんで) are both `adverb`. This is the
  template-default slip the observing run suspected.
- **00498 何 and 02924 どんな carry no semantic tag at all**, which is
  [`tag-missing-semantic-entirely`](#updates-2026-08-11) territory (79 entries dictionary-wide).

**Scope**: 12 entries. **Blocked on one convention decision** — which in-list tag the family
takes. `grammatical` is the plurality (4 of 10 tagged) and is the only candidate that fits all
twelve; adopting it would retire `interrogative` from the off-list tail and give the
`direction`/`descriptive` members a consistent home. Filed at `needs-decision` rather than
`open` for that reason: migrating without a ruling just re-scatters the family.

### P20's largest hot spot has a name: the 2026-01-25 creation run

The 2026-08-22 accuracy-review run found six off-list tags in a 50-ID window (12743 `sensation`
/ `body`, 12746 `place` / `war`, 12749 `place`, 12756 `crime`, 12758 `sensation`, 12764
`supernatural`) and proposed a `systemic-fix` sweep over "the whole 2026-02-22 creation cohort".

**Refuted, and the measurement points somewhere much better.** Off-list tags now stand at
**920 entries** (from 934 on 2026-08-16). The 2026-02-22 cohort holds **399 entries with 2
off-list survivors** — and even counting back the six that run fixed, 8 of 399 is **2.0%,
below the 3.0% dictionary-wide rate**. There is no 2026-02-22 hot spot. This is the fourth
ID-correlated false cohort filed in five weeks.

Measuring the same population by **creation date** instead — an axis this page has not tried
before, after three refuted ID-band cohorts — produces the first cohort claim that survives:

| Creation day | Off-list / cohort size | Rate |
|---|---|---|
| **2026-01-25** | **191 / 330** | **57.9%** |
| 2026-03-28 | 105 / 371 | 28.3% |
| 2026-03-11 | 38 / 150 | 25.3% |
| 2026-04-04 | 33 / 133 | 24.8% |
| 2026-04-05 | 66 / 339 | 19.5% |
| *(dictionary-wide)* | *920 / 30,524* | *3.0%* |

And the creation axis turns out to **explain the ID axis rather than compete with it**: all
**191** of the 2026-01-25 cohort's off-list entries sit inside **08000–08999**, which is the
201-entry hot spot [the 2026-08-16 re-measurement identified](#p20-re-measured-2026-08-16--934-entries-and-the-hot-spot-is-not-where-the-filing-run-put-it)
without being able to say why it was a hot spot. It is a hot spot because **one day's entry
creation produced 330 entries with a single ad-hoc tag vocabulary** — `gardening` ×10,
`loanword` ×10, `competition` ×8, `services` ×7, `technique` ×6, `behavior` ×6 — and 58% of
that day's output carries it.

For batching this is the difference between a guess and a plan: the hot spot is not a range
that happens to be dirty, it is **one authored batch with one vocabulary**, so a single
`systemic-fix` run over 08000–08999 clears 21% of the entire P20 population and can lean on the
fact that the same handful of ad-hoc names recur throughout it. ID-band keying stays the right
*operational* handle (it is what the tools take); creation date is the right *diagnostic* one.
Note also that ID-band concentration is still tighter overall — the top 3 ID bands hold 50% of
the population against the top 5 creation days — so this does not displace the existing
hot-spot table, it annotates its first row.

### P50: the creation-batch backfill is refuted; the block backfill is 5× better — and the population is only 57

The 2026-08-21 polish run confirmed [P50](#p50-is-growing-and-its-members-were-visited-not-skipped--57-from-54)
directly (frontier block 06985–06994 had zero inline links, all ten) and proposed that "the gap
tracks *creation batches* rather than polish visits… a backfill sweep keyed on creation batch
would likely be more efficient than one keyed on the polish frontier."

Measured against a control, the premise is half right and the recommendation is wrong. All **57**
zero-link entries below the frontier were created inside a single eight-day window
(2026-01-11 → 2026-01-18), which is suggestive — until the control is run over *every*
sub-frontier entry:

| Creation day | Zero-link / created | Rate |
|---|---|---|
| 2026-01-05 → 01-10 | 0 / 2,057 | 0.0% |
| 2026-01-11 | 1 / 754 | 0.1% |
| 2026-01-12 | 1 / 699 | 0.1% |
| **2026-01-13** | **21 / 735** | **2.9%** |
| 2026-01-14 | 3 / 527 | 0.6% |
| 2026-01-16 | 9 / 1,098 | 0.8% |
| 2026-01-17 | 5 / 525 | 1.0% |
| **2026-01-18** | **17 / 445** | **3.8%** |
| *(all sub-frontier)* | *57 / 6,970* | *0.8%* |

The first six creation days are **perfectly clean across 2,057 entries**, so the window is real —
but inside it the worst day still runs 3.8%, i.e. a creation-batch backfill would read **445
entries to find 17**. The ID axis is far tighter: **03900–03999 holds 21 of the 57 in one
hundred-ID block (21% of the block, 25× the sub-frontier baseline)**, so a block backfill reads
100 entries to find 21 — **five times more efficient per entry read**.

The operative conclusion, though, is that **neither keying is needed**: the whole population is
57 entries. That is one bounded `systemic-fix` or polish batch, and it should simply be worked as
a list rather than as a sweep over anything. The `modified` dates confirm there is no shortcut —
they are scattered from 2026-01-19 to 2026-07-28, so these entries have been opened repeatedly
since creation without gaining links, which is the "visited and silently dropped" reading the
2026-08-21 harvest arrived at, now with the creation-window detail that the drop starts partway
through one week's output and never affects the week before it.

### P62 update: the `・` penalty is real, 3× — and it is not the binding defect

The 2026-08-21 polish run reported that `build/note_templates.json` rewards uppercase `SECTION:`
headers and `- ` bullets while many older entries use `・`, costing them 15–25 points and
inflating their position in `polishing/priority/notes.txt` (it named 01142, 01194, 01217, 01219
as entries with substantively good notes scoring 77).

This is P62, and the distortion was already measured once — **"130 of the top 500 priority
entries (26%) carry the shape"**, recorded 2026-08-15. Re-measured here at a different depth it
reproduces cleanly: **24 of the top 100**. What the earlier measurement did not state is the
comparison that makes the number mean something — the **dictionary-wide base rate is 8.1%**
(2,484 of 30,524 entries), so the top of the list is enriched **3×** for a purely typographic
property. The penalty demonstrably moves entries up the ranking.

But 76 of the top 100 are *not* `・` entries, so this is a contributing
distortion, not the cause of the priority lane's long-running no-op problem. The binding fix
remains the [Tooling 20](tooling-backlog.md) scorer-bug pair plus its **structured-note credit**
recommendation — which, from 2026-07-02, *already names accepting `・`-bulleted blocks as quality
signal*. So the observation's proposed remedy is filed, and this measurement sizes it: worth
doing, worth ~a quarter of the top-of-list distortion, not worth a dictionary-wide rewrite of
2,484 entries' bullets ahead of the scorer fix.

### Refuted: a `formality: formal` detector for everyday concrete nouns

The 2026-08-21 polish run fixed **06994 ゴミ箱**, tagged `formality: "formal"` for a household
rubbish bin, and proposed "a cheap detector for `formality: formal` on daily-life concrete
nouns".

As specified the detector would flag **214 entries** (`formal` + `noun` + a concrete/daily-life
semantic tag), and the overwhelming majority are Sino-Japanese words that are *legitimately*
register-marked — 00146 果実, 01616 昼食, 01825 衣服, 02861 お手洗い, 01593 ご主人. Precision would
be very low by construction, because the predicate cannot distinguish "concrete everyday object"
from "formal word for a concrete everyday object", which is exactly what the tag is for.

The high-precision cut inside it is tiny and worth recording: restricted to **pure-katakana
headwords** the population is **4 entries** — 05081 バイク, 06960 デバイス, 08988
オペレーティングシステム, 03855 タイトル — and three of the four look wrong on sight. (03855 タイトル
is a bonus find: its semantic tags read `communication`, `food`, `leisure`, `tool`, a textbook
[P11](#priority-11) example-topic contamination.) Four entries is not a detector, it is a
follow-up, and it is recorded in [Entry Follow-ups](entry-followups.md).

Note also that the 29 basic/core-tier members of the 214 are already inside
[`tag-register-marked-basic-core`](#register-markedness-on-ordinary-vocabulary--231-basiccore-nouns)
(231 entries), so the genuinely actionable slice of this proposal was open before it was made.

### Refuted: the sole-`general` detector is not filtering 06985–06994

The same run observed that 6 of the 10 frontier entries carried sole-`general` semantic tags and
asked whether `check_tag_drift.py`'s sole-`general` check "should be reaching these… worth
confirming they are in its queue rather than being filtered out."

It is not filtering them. The check's current queue holds **3,591 entries** and starts at
00005; none of 06985–06994 appear in it because **that run fixed all ten**, on 2026-08-21
(06985 → `art`/`culture`, 06986 → `leisure`/`entertainment`, 06987–06988 → `music`, 06990 →
`art`/`culture`, 06991 → `tool`/`leisure`, 06992 → `nature`/`leisure`). A detector queue read
after the fix cannot show the entries the fix removed. No defect; no item.

### Re-discoveries needing no new item

- **Verb notes that transcribe the conjugation table** (2026-08-22, entries 06999–07003, fixed
  in that run) — this is [Priority 31 / `notes-duplicate-conjugation-block`](#priority-31),
  measured at 46 entries on 2026-08-21 and waiting on [Tooling 132](tooling-backlog.md#132-a-duplicate-conjugation-in-notes-class-for-check_artifactspy)'s
  detector class, plus its compound-verb sibling [P54](#priority-54-the-compound-verb-conjugation-preamble-37-entries--bounded-pending-a-curator-call)
  (37 entries). Fifth filing of this family.
- **Candidate-queue orthography twins** (2026-08-22: 思いつき queued while
  {思\|おも}い{付\|つ}き 27771 existed) — filed since 2026-07-30 as the okurigana-normalization gap
  in [Tooling 41/43](tooling-backlog.md), whose stated fix is exactly the "reading plus
  normalized okurigana" match the observation proposes. Third sighting.
- **06995–07003 carry no inline links while 07004 is fully linked** (2026-08-22) — above the
  frontier, so this is the standing *do-not-file* zero-link structural fact, not a defect. Its
  genuinely useful content is the cost note (20–40 lookups per frontier entry in this band),
  which belongs with [P43](#priority-43-the-0680007100-block-is-96-unlinked--a-bounded-batch-not-a-frontier-problem)
  and is consistent with it.

### `entry-pair-consolidation` gains a member, with a direction

The 2026-08-22 run flagged **02485 {気持\|きも}ち** as a duplicate of **01385 {気持ち\|きもち}** — same
word, same reading, overlapping glosses. Confirmed, and the merge direction is measurable rather
than a judgment call:

| | 01385 | 02485 |
|---|---|---|
| Tier | basic | core |
| Senses | 2 (feeling/sensation; mood) | 3 (feeling/emotion; sensation; **intention, sentiment**) |
| Inbound references | **187** | 19 |
| Headword furigana | `{気持ち\|きもち}` — **malformed** | `{気持\|きも}ち` — correct |

**Keep 01385** (basic tier, 187 inbound references against 19) and fold in 02485's third sense
("intention, sentiment"), which 01385 lacks. The merge must also fix 01385's headword, which
swallows the okurigana ち into the ruby — a [P64](#p64-okurigana-swallowed-into-the-furigana-ruby--123-instances-invisible-to-every-checker)
instance sitting on the entry that 187 links point at. Added to the `entry-pair-consolidation`
item (now 10 pairs).

### For the curator: `formality` cannot express register that differs by sense

The 2026-08-22 run hit this on **12766 {念\|ねん}**, whose own notes say sense 1 (感謝の念, 畏敬の念)
is formal while sense 2 (念のため) is everyday. `formality` is an entry-level field, so both
`formal` and `neutral` are wrong for half the entry, and the accuracy reviewer flagged the tag as
wrong — correctly, in the sense that no available value is right.

This is a schema question, not a tagging error: should `formality` (and by extension `politeness`
and `style`) be permitted at the definition level for the handful of entries with split register?
The population is unmeasured and probably small, and the cost is not zero — every renderer,
detector and reviewer prompt that reads `metadata.tags.formality` would need to fall back when a
definition overrides it. Recorded in [Register](../topics/register.md) alongside the
encodes-versus-denotes distinction, which is the same field failing to say two different things.

## Related pages

- [Tooling Backlog](tooling-backlog.md) — tool improvements surfaced alongside these patterns
- [Entry Follow-ups](entry-followups.md) — specific entry fixes
- [Content Pipeline](../project/content-pipeline.md) — how polishing tasks work
- [Entry Consistency](../topics/entry-consistency.md) — consistency standards
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis of recurring tag-drift patterns (covers P6–P8 above)
- [Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) — analysis of malformed wrapper patterns (covers P9 above)
