# Cleanup Backlog — resolved and closed items

Items moved here from [cleanup-backlog.md](cleanup-backlog.md) on 2026-09-26 because they are resolved, shipped, retired or refuted (by their `backlog-queue.json` status where they have one, otherwise by the status the item itself records). Kept for the record and for their measurements. If an item here turns out to be open, move it back.

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

## Priority 12: Dual-reading furigana with slash separators — RESOLVED 2026-06-16

**RESOLVED (2026-06-16).** A systemic-fix Routine run fixed all **118 entries** (131 slash-reading wrappers) flagged by `build/check_furigana_format.py` (`subpattern == 'slash-reading'`). Each `{漢字|よみ1/よみ2}` wrapper was replaced, per-entry, with the single reading the kanji actually takes in context: the rendaku'd compound reading where the wrapper decomposes the headword ({歩|ぽ} in 散歩, {袋|ぶくろ} in 寝袋, {顔|がお} in ドヤ顔), the inline-link target's reading where the wrapper sat inside a ⟦…⟧ link ({毎年|まいとし}→00731_maitoshi), or the primary reading for standalone/related words ({梅雨|つゆ}, {買春|ばいしゅん}). Notes that explicitly discuss the reading variation (e.g. 七 なな/しち, 分 ふん/ぷん) kept their prose explanation; the wrapper just dropped to one reading. Two malformed English-in-reading wrappers were also repaired (28654 アプリ内課金: `{課金|billing/charging}`→`{課金|かきん}`, `{内|inside}`→`{内|ない}`). The detector now returns **0** slash-reading instances. A furigana self-check screened 59 of the 118 changed IDs before the 540 s `timeout` wrapper killed `review_runner.py` (logged as a `[tooling]` observation); its 11 flags were all false positives (rendaku-in-compound, okurigana/partial readings "correct by design", and screener input-truncation artifacts), 0 applied. Tracked as `furigana-slash-reading` in `backlog-queue.json`.

**Source**: Comprehensive-polish 2026-05-18 session 010 (entries 02251–02273)

Several entries in this range used non-standard dual-reading furigana notation with slash separators, e.g., `{村|むら/そん}`, `{蛍|ほたる/けい}`. These were normalized to single readings during the polishing session.

The slash-separator pattern is not documented in the `{kanji|reading}` convention and is likely ignored or misrendered by the furigana renderer (which expects a single reading string). The correct treatment is to pick the primary reading for the context and mention the alternative reading in notes.

**Detection**: `grep -rP '\{[^|}{]+\|[^}{]*\/[^}{]*\}' entries/ | head -30`

**Suggested action**: One-shot scan across all entries for the slash-in-reading pattern. Each instance needs manual review to select the correct single reading. The scope is unknown — this is the first range where the pattern has been observed.

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
[Tooling item 11](tooling-backlog-resolved.md#11-inline-link-target-id-resolution-gate-in-validatepy-or-pre-commitci)
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

**RESOLVED 2026-09-12 — fifth discovery is the one that finally cleared it.** The 2026-09-12
`systemic-fix` run (backlog item `inline-link-braced-base-form`, priority 5) ran the anchored
detector: 30 entries remained (01484 and 04471 had already cleared since the 08-12 measurement,
leaving the two clustered cohorts 00697-00716 / 00965-00988 plus 09760). Applied the base-form
strip to all 147 matched instances, including two multi-brace bases the single-group regex above
doesn't show (`{紙|かみ}{袋|ぶくろ}` → `紙袋` in 00712, `{話|はなし}{上手|じょうず}` → `話上手` in
00707) — both still anchored between `→` and `：`, so still in scope. `validate.py --changed-only`
came back 30/30 clean. The detect regex now matches zero files dictionary-wide.

The lookup cross-check this item asked for surfaced four **pre-existing, unrelated** cases where
the base form (now plain) still doesn't resolve against `build/word_id_lookup.json` by exact
string match: `人→00658_nin` (four occurrences across 00975/00976/00984/00985 — the entry's own
headword is `〜{人|にん}` and the link is missing the counter tilde, in both slots, since before
this fix), `話上手→08467_hanashijouzu` (the entry's headword is `話し上手` with okurigana; the
note already wrote the kanji-only variant before this fix), and two cosmetic-only mismatches
(`早い` vs. the dual-orthography headword `速い／早い` on 00514; `〜やすい` using a plain tilde
where 18367's headword uses a full-width `～`). None of these are broken links — `validate.py`
confirms every target ID exists — and none were introduced or altered by this run's brace-strip;
they were masked behind braces before and are now just visible as lookup-string mismatches. Not
fixed here (outside this item's anchored, mechanical-safe scope); logged in
`polishing/observations.md` 2026-09-12 for a future item.

Also out of scope, left untouched by design: base forms where furigana wraps only part of a
conjugated form with plain kana outside the braces, e.g. `{書|か}く→{書|か}く：00477_kaku` (the
braces cover only 書, the く sits outside) — the detector's `→\{[^}]*\|[^}]*\}：` requires the
*entire* base segment between arrow and colon to be one or more consecutive brace groups, so a
form with interleaved plain characters (okurigana, or 折り紙-style `{折|お}り{紙|がみ}`) never
matched and was never touched. That is a different, unscoped defect shape (a genuinely braced
tooltip, just not this item's anchored pattern) and would need its own detector.

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

**2026-08-25 systemic-fix run** — eighth per-entry short-base batch. 173 A1/A2 pairs (196
instances) across 116 entries in **05879–06388**, each judged against a ±70-character context
window around the marker. **Two rejections, both polysemous katakana loanwords**: 05909's
スマホの⟦ロック⟧ → `08116_rokku`, which is rock *music* (the fourth firing of this same target,
after 04562, 05762, and the 2026-08-08 フライ/パン pair), and 06183's scrollbar ⟦バー⟧ →
`07060_baa`, a drinking establishment. Everything below **06389** is now swept for A1+A2; the
queue stands at **290 pairs** (a recount; the 453 carried in the item was stale).

**The proposed "target's notes declare a same-reading different word" detector class was tested
against this band and needs one refinement to be usable.** Three previous updates proposed
scanning a link target's `notes` for a self-declaration and demoting such pairs out of the
mechanical bucket. Run naively over this band it fired on **7 of 175 pairs and only 1 was a real
false positive** (ロック). The other six were good entries doing exactly their job: 臨む's notes
distinguish it from 望む, 端午's from 単語, 利く's from 聞く/効く, 生む's from 産む, 五円玉's from
ご縁. The refinement is one clause: **the declaration is a demotion signal only when it names the
marker's own base form.** ロック's notes say "ロック as 'lock' … is a different word" — naming
ロック itself; 臨む's name 望む, a *different* surface. That test keeps all six good pairs, catches
ロック, and would also have caught the 2026-08-08 フライ/パン and 2026-08-20 コマ rejections. It
would **not** have caught this run's バー rejection, whose target contrasts バー only with 居酒屋
and スナック — so the class raises precision without replacing the context read.

Families verified as groups in this band: the twelve zodiac sign names (06313), omikuji fortune
levels (中吉/小吉/末吉), medical and anatomical compounds (胆嚢/膵臓癌/飛沫/胸痛/電解質/熱性痙攣),
corporate-finance terms (監査役/決算書/決算期/不渡り/当座/使用料), funeral and Buddhist vocabulary
(火葬/忌明け/服す/仏事/仏前/香道/聞香), aviation terms (駐機場/降下/降機/航空法/空撮), gardening
supplies (培養土/鉢底石/鉢皿/植木屋), and counter and number words (一曲/何時間/何十年/三大).
Marginal applies resolved by opening the target entry rather than trusting its gloss (the
2026-08-14 rule): ヘビーゲーマー/コアゲーマー → `29473_hebii` / `29474_koa`, whose entries carry
"intense, demanding" and "hardcore, devoted (modifier)"; {当座|とうざ}{小切手|こぎって} →
`29548_touza` sense 2 "current account"; {邪気|じゃき}を{追|お}い{払|はら}う → `29599_jaki`
sense 2 "evil spirit"; and {大器|たいき}{晩成|ばんせい}'s ⟦{大器|たいき}⟧ → `29641_taiki`, the
literal-decomposition precedent.

One incidental repair worth a separate detector: 06303 carried the marker surface `{ローン}` —
kana wrapped in furigana braces with **no reading and no pipe**, which `validate.py` does not
flag as either a furigana or a word-link warning. Fixed while rewriting that marker; two more
instances (06299 `{めまい}`, 06301 `{ふくらはぎ}`) sit in markers this sweep did not touch and
were left in place. This is a `check_furigana_format.py` class: `\{[^|{}]*\}` whose contents are
entirely kana. (Related to the 2026-06-17 no-pipe brace sub-pattern under P9.)

Running false-positive rate across the 1,426 hand-verified short-base pairs (2026-08-09 through
2026-08-25): **~0.4%**.

**2026-08-29 systemic-fix run** — ninth per-entry short-base batch. 177 A1/A2 pairs (203
instances) across 123 entries, entries 06389-06810, each judged against a ±70-character context
window around the marker. **Two rejections, both polysemous katakana loanwords:**

- 06464's `二重のロック` (a door's double lock) → `08116_rokku`, *rock (music)*. This is the
  **fifth** firing of this single target, after 04562, 05762, 05909 and the original 2026-08-08
  フライ/パン pair. The 2026-08-25 refined rule still catches it — 08116's own notes state that
  "ロック as 'lock' is a different word with the same reading", and the declaration names the
  marker's own base form — so the case for shipping that detector class keeps strengthening. In
  the meantime a one-line denylist for `ロック → 08116_rokku` would have saved four adjudications.
- 06574's `コーラスパート` (chorus part, i.e. backup vocals) → `03106_paato`, whose entry covers
  **only** パート = part-time work. This is a **new false-positive family**: *the target entry
  silently covers a different sense*. It is not the self-declaring homophone family (03106 makes
  no disambiguating statement at all) and not the 2026-08-11 proper-name family (the readings and
  the lexeme agree). No notes-scanning rule can see it; the only tell is that the target's glosses
  and every collocation it lists belong to one sense while the marker's context belongs to
  another. Reading the context remains irreplaceable.

Families verified as groups in this band: reference-apparatus terms (頭注/傍注/巻末注/後注 →
2971x), building and infrastructure vocabulary (内壁/遮熱/単管/容積率/揚水/配電), baseball
statistics and roles (打数/奪三振/中継ぎ/抑え/好打者/四番), swimming technique (蛙足/プル/バタ足/
入水), janken hands (グー/チョキ/パー → 29915-29917, plus 後出し), legal-code lists (商法/訴訟法/
判例/法体系), body and medical terms (上腕/前腕/熱性/留置場), emotion nominalizations (悲しさ/
嬉しさ ← 悲しい/嬉しい), and place and proper names used as themselves (長崎, 成田, カナダ,
甲子園, 夏目漱石). Marginal applies resolved by opening the target entry rather than trusting its
gloss (the 2026-08-14 rule): 06783's `一部始終` → `04192_shijuu`, glossed as the adverb
"constantly" but whose notes carry an explicit second usage, "Noun: the whole story/sequence";
06450's `終活` decomposition → `29777_shuumatsu`; and 06798's `デジタル化` → `28335_ka`, the
bare-kanji-surface/tilde-base suffix precedent.

Running false-positive rate across the 1,603 hand-verified short-base pairs (2026-08-09 through
2026-08-29): **~0.4%**.

**The leak is now visible in the residue.** After this band, 123 mechanical pairs remain — but
41 of them sit *below* 06811, in territory already swept. About ten are the accumulated
deliberate rejections; the other ~31 are **new arrivals**, created by later `new-entries` runs
adding the target entry beneath a marker written months earlier (00622 名様, the 00658 counter
words, 01510 北極星, 02273 映画祭, and a run of place names). This is exactly the regrowth this
priority predicted from the start, and it is the standing argument for Tooling 19's
`manage_candidates.py` sync hook. The next sweep should be a low-ID catch-up band from 00007
rather than a continuation above 06810.

### Update 2026-09-02 — RESOLVED: 0 mechanical pairs remain

A 2026-09-02 `systemic-fix` run selected this item and, before opening any entry, re-ran the
detector: `check_stale_noentry.py --summary` and `--mechanical --json` both report **0 A1/A2
pairs dictionary-wide** (4,380 `noentry` instances examined; all fall in classes B/C/D/R/A3 or
unresolved). The 123-pair residue the 2026-08-29 update measured — including the 41 below 06811
and the predicted low-ID leak — is gone. The most likely cause is the 2026-09-02 dictionary-wide
mechanical relink (`build/auto_link.py`, 1,007,002 links placed as part of the Routine v3
overhaul; see `PROJECT_STATUS.md`), which appears to have re-resolved the remaining short-base
`noentry` markers as a side effect of its own headword/reading match, on top of the incidental
9-marker link from the 2026-08-29 new-entries run (30734–30753). No entries were opened or
changed this run. **Status set to `resolved`, `scope_estimate: 0`** in `backlog-queue.json`. The
underlying leak mechanism (new-entries runs creating targets for markers written earlier) is
unchanged, so if `--mechanical --json` ever returns pairs again, reopen this item rather than
filing a duplicate.


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
[Tooling 56](tooling-backlog-resolved.md#56-nothing-checks-that-a-headword-carries-furigana) refills it
within weeks; the check is the item that matters, and it is a two-line ratchet
(`bare kanji in headword` → error) because 99.05% of the corpus already passes.

**Related**: [Furigana Strategy](../topics/furigana-strategy.md),
[Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md),
[Tooling 47](tooling-backlog.md#47-cross-reference-headword-fields-are-invisible-to-every-furigana-instrument-7-confirmed-defects).

**RESOLVED 2026-09-06.** A re-detect at run time found 258, not 248 (10 more created since the
2026-08-02 measurement — the active-defect prediction held). All 258 swept: 203 all-kanji
headwords braced mechanically as `{headword|reading}`; 55 mixed kana/kanji headwords braced
per-entry, each new bracing validated by stripping braces and pipes back down to the original
headword and reading before writing. Zero bare-kanji headwords remain dictionary-wide.

**Ratchet shipped 2026-09-13.** [Tooling 56](tooling-backlog-resolved.md#56-nothing-checks-that-a-headword-carries-furigana)
/ [Tooling 96](tooling-backlog-resolved.md#96-find_missing_furiganapy-never-scans-the-headword-field) are
both closed: `build/validate.py` now carries `find_bare_kanji_headword_errors`, a hard ERROR
(no baseline needed — the corpus was already at zero) for any kanji in `headword` outside a
`{kanji|reading}` group; `build/find_missing_furigana.py` now scans `headword` too. Re-verified
0/30,683 entries flagged by either instrument at ship time.

## Priority 41: Conjugation tables generate the potential of a verb that is already potential — RESOLVED 2026-09-07

**Source**: 2026-08-03 routine new-entries run, which noticed `add_conjugations.py` producing
待ちきれられる and 待ちきれろ for `30367 待ちきれる` and suggested a suppression flag.
**Measured 2026-08-04, and the scope reaches basic-tier vocabulary.**

**Resolved 2026-09-07** by a `routine(systemic-fix)` run: `Potential`/`Passive`/`Imperative` rows
deleted from all 7 curated entries (`00557 できる`, `01165 見える`, `01229 聞こえる`, `02376 取れる`,
`06957 いける`, `15166 眠れる`, `30367 待ちきれる`), each verified individually, validated, and
self-checked. No further scope: the 7-entry list below was the whole shippable set. Queue item
`conjugation-potential-of-potential` closed; the generator-side guard remains open as tooling
item 70.

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
[Inline Link Integrity](../topics/inline-link-integrity.md#zero-link-entries--23444-and-not-a-defect),
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

**RESOLVED 2026-09-13 (duplicate filing).** This is the same defect as
[Priority 36](#priority-36-headwords-written-as-bare-kanji-with-no-furigana-braces-248-entries)
(same detector regex, same population), which a 2026-09-06 systemic-fix run already swept to
zero — this item's `backlog-queue.json` record was never updated to reflect that, which is why
the scheduler picked it again today. Re-verified 0/30,683 entries at run time. The validator
fix this item asked for is shipped in the same run (see the P36 resolution note): `validate.py`
now hard-errors on bare kanji in `headword`, and `find_missing_furigana.py` scans it.

### Priority 55: Inline links that resolve to a homophone of the intended word — RESOLVED (2026-09-11)

A 2026-09-11 systemic-fix run worked all 23 confirmed occurrences across the 22 source entries
listed below: 12 repointed to the entry the base form actually names (深く→深い, 感→〜感, 系→〜系,
純→純〜), 5 consolidated from a link split across two or three markers (お好み焼き, 吸い物,
終身雇用, 腑に落ちない) into one link on the compound's own entry, and 6 unlinked because no entry
exists for the base form (用地, 専任, 五時, 詩的, 詩集, 詐称, 天賦, 進水, 書架, 科す — each queued
as a candidate) or because the base was a bare kanji-component gloss rather than a word (温 in
温帯's etymology note). `check_link_baseform.py --no-allowlist` now returns 0 DISAGREE cases
outside the allowlist. Decisions logged in `reviews/decisions.jsonl`; see also the self-check's
two unrelated adjudications on 00181 and 02496 logged the same run.

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

**RESOLVED 2026-09-12.** A 2026-09-12 systemic-fix run fixed `add_conjugations.py` first (Tooling
122), then re-ran this section's own detection rule against the live dictionary rather than
trusting the list above verbatim, and found two discrepancies worth recording. First, the "The
32" list above enumerates only 31 IDs — it omits 14629 面する, which the rule does catch and which
was genuinely still affected. Second, 20837 さする was **already fully correct** (a proper godan
table, no サ変 residue) by the time of this run — some other session fixed it outside this item,
so the "different and worse defect" above is stale and needed no action. Net: 31 entries fixed
(the 30 above still affected, plus 14629; 20837 excluded as already fixed; 30647 excluded as
already correct per the original measurement). One of the 31, 27887 害する, turned out to have
lost furigana across its *entire* conjugation table, not just the Potential row — a separate,
pre-existing defect, fixed by regenerating its whole table with the corrected generator rather
than patching one row. All 31 validate; self-check and link-check ran clean apart from three
unrelated pre-existing flags on two entries (adjudicated, see `reviews/decisions.jsonl`
2026-09-12T00:46:00Z). Status moved to `resolved` in `backlog-queue.json`.

### Priority 60: Katakana wrapped in furigana braces — RESOLVED (was 275 instances / 229 entries)

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

**Resolved 2026-09-13.** A systemic-fix run re-scanned every entry field directly for a
katakana-only furigana base (not via `check_furigana_format.py`'s `pure-kana` bucket, which also
catches numerals and other non-katakana kana-only bases and does not isolate this class) and found
only the one instance above still standing — the other 274 had already been stripped by
intervening polish/systemic-fix runs without this item being marked resolved. Fixed 23394 by hand
(`{カキ|がき}` → `カキ` in `definitions[].explanation`, matching the correct かき reading already
given elsewhere in the entry's notes) and re-scanned: zero katakana-base furigana wrappers remain
in the dictionary. The merge with `katakana-hiragana-reading-wrappers` proposed below is still an
open queue-hygiene action for whoever owns that item.

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
  [Inline Link Integrity](../topics/inline-link-integrity.md#zero-link-entries--23444-and-not-a-defect),
  where this harvest replaced the single-window growth note with a 66-day measurement.

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

### P64. Okurigana swallowed into the furigana ruby — RESOLVED 2026-09-14

**Resolved** by a 2026-09-14 systemic-fix run: shipped `build/check_okurigana_ruby.py` (the rule
below, as a standing script) and hand-verified every hit. 77 of 121 instances (76 entries) were
real bugs and were fixed; 30 across 20 (kanji, reading) pairs were genuine exceptions — complete
atomic readings with no separate kana slot in real orthography (`{冷|ひや}{奴|やっこ}`,
`{源|みなもとの}{頼朝|よりとも}`), name/nanori readings (黒澤`{明|あきら}`), and on-yomi +
sokuon misread as kun-yomi okurigana (`{換|かん}`, `{悪|あっ}化`) — and were left as-is. Detail
in [Tooling 130](tooling-backlog.md). The script stays in `build/` for the next sweep, since new
entries can reintroduce the pattern.

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

### Refuted as a batch item: `existence` as a catch-all for action verbs

The 2026-08-24 accuracy-review run found seven entries in 12913–13412 carrying `existence` as
their sole or lead semantic tag on words denoting actions or events (13290 {浸|つ}かる,
13068 {明|あ}け{暮|く}れる, 13166 {欠|か}く, 13339 {浸|ひた}る, 13226 {殺害|さつがい},
13360 {滅亡|めつぼう}, 13240 {死去|しきょ}), rejected each under the in-list narrowness rule, and
suggested a detector or a `systemic-fix` pass for the cluster.

Measured dictionary-wide: **112 entries lead with `existence`** (129 carry it anywhere) — 0.37%
of the dictionary against 1.4% in that range, so the range really was ~4× enriched. But reading
the 92 verbs among them dissolves the family: 死ぬ, 滅亡, 消失, 現存, 生息, 実在, 尽きる, 絶える,
夭折, 逝去 and most of the rest are *about* existing or ceasing to exist, and `existence` is the
right tag. The tightest defensible cut — lead-`existence` verbs whose gloss opens "to become / to
turn / to grow", i.e. state-change words that belong under `change` — is **6 entries** (00756
すく, 11062 {空|あ}く, 12291 {寂|さび}れる, 14612 {青|あお}ざめる, 14680 {霞|かす}む, 18770
{肥|こ}える).

So there is no detectable family here, only a handful of individually-wrong tags that the
existing in-list narrowness policy correctly declines to sweep. Recorded so the next run that
notices the cluster does not re-propose the pass; fix the six opportunistically if a polish run
lands on them.

### P69. Furigana braces around kana-only text — 529 entries, 753 instances

The 2026-08-24 polish run found three instances of kana wrapped in furigana braces with no
reading (`{ローン}`, `{めまい}`, `{ふくらはぎ}`), noted that `build/validate.py` reports nothing
for them, and asked for a `check_furigana_format.py` class matching `\{[^|{}]*\}` with all-kana
contents.

The class is real and larger than the sighting: **753 instances across 529 entries**. It is not
one family, though, and the two members want different fixes:

- **~29 inside inline links** — `⟦{いい}→いい：00118_ii⟧`, `⟦{おもちゃ}→おもちゃ：01334⟧`,
  `⟦{パソコン}→パソコン：01534⟧`. The braces are pure noise around a link's surface form; deleting
  them is mechanical and safe.
- **~724 outside links**, and a sample shows these split again: some are the same noise in plain
  example text, but others are notes using braces to *quote a reading* — 02002 reads "usually
  read as {だて}, sometimes {たて}". That is a real communicative act being performed with
  furigana syntax the renderer cannot honour (no `|`, so no ruby). Dropping the braces there
  loses the quotation; the right repair is 「だて」.

So: build the detector, and split its output by "inside a `⟦…⟧` marker" before fixing anything.
Only the first bucket is mechanical.

### Re-discoveries needing no new item (2026-08-27)

- **`・` bullets instead of `- ` in 07005–07012 notes** (2026-08-24 polish) — this is
  [P62](#p62-update-the--penalty-is-real-3--and-it-is-not-the-binding-defect), measured at 2,484
  entries with the fix belonging to Tooling 20's structured-note credit. Third filing.
- **Verb notes opening with a conjugation stub that duplicates the `conjugation` field**
  (07005, 07007, 07008, 07009) — P31/P54 and Tooling 132, which already owns the fixed
  three-line shape. Sixth filing.
- **Sole-`general` semantic tags clustering in 07013–07022 and at 03658/03726/03729/03760** —
  `check_tag_drift.py`'s sole-general check already sees these, and Quality Metrics has recorded
  six consecutive windows of the accuracy sweep proposing the same family and the adjudicator
  rejecting it wholesale. The standing ruling stands: sole-`general` is a **polish-lane** side
  task, fixed with the entry open, never a sweep.

### Refuted: the legacy ALL-CAPS notes template is not a January cohort — it is the dictionary's majority style

Three observations across two polish runs (07023–07042, then 07043–07058) reported that the
2026-01 creation batch "predates both conventions" — no inline links, and ALL-CAPS
`FORMATION:` / `COLLOCATIONS:` / `SIMILAR WORDS:` headers with `・` bullets instead of the house
prose-plus-hyphen style — and inferred that entries created on those dates elsewhere in the ID
space would be in the same state.

Half of that is right and half is backwards. **21,073 of 30,564 entries (69%) use ALL-CAPS note
headers**, and the rate is *higher* on recent creation days than on the January ones:

| Creation date | ALL-CAPS notes | Created that day | Rate |
|---|---|---|---|
| 2026-03-28 | 331 | 371 | 89.2% |
| 2026-02-22 | 355 | 399 | 89.0% |
| 2026-04-02 | 359 | 419 | 85.7% |
| 2026-01-18 | 348 | 590 | 59.0% |
| 2026-01-16 | 470 | 1,098 | 42.8% |

So ALL-CAPS headers are not a legacy artifact at all; they are what the dictionary does, and
`score_note_quality.py` awards its 10-point formatting bonus only to that style
([Tooling 20](tooling-backlog.md)) — a polish run that converts them to prose costs the entry
those points. **The link coverage half of the observation stands** (the block genuinely has zero
inline links, which is `inline-link-block-06800-07100`), and so does the `・` bullet half (P62).
The template claim does not, and the frontier lane should not budget for "full notes rewrites"
on the strength of it.

### Refuted: no copied "colour words are na-adjectives" family

A 2026-08-29 run corrected 00959 きいろい, whose notes claimed "many color words function as
na-adjectives (like 緑)" — wrong, since 緑 is a noun used with の — and asked for a grep in case
the claim had been copied across the colour entries of the same batch.

Measured: **two entries in the dictionary pair "colour" with "na-adjective" in the same
sentence**, 10803 カラフル and 18036 華やか, and both are correct — those words *are*
na-adjectives. Eight further entries mention "na-adjective" somewhere near colour vocabulary and
none makes the false claim. 00959 was a one-off, already fixed. No item.

### Re-discoveries needing no new item (2026-08-31)

- **Sole-`general` was the norm in 07026–07042** (eight entries, all with an obvious better tag).
  P13 / `tag-sole-general`; standing ruling unchanged — polish-lane side task, never a sweep.
- **01385 / 02485 {気持|きも}ち duplicate**, re-filed a fourth time. Already decided on
  2026-08-23 by inbound-reference count (187 vs 19: keep 01385, fold in 02485's "intention,
  sentiment" sense, and fix 01385's okurigana-swallowing headword in the same edit). It is on
  `entry-pair-consolidation` and needs execution, not another filing.
- **03522 {次々|つぎつぎ} / 07028 {次々|つぎつぎ}と**, the same adverb with and without the
  particle. Cross-linked both ways as a stopgap by the observing run; belongs on
  `entry-pair-consolidation` with the 気持ち pair.
- **Cross-references with no `target_id`** — reported at "44 across 40 entries", which is exactly
  what `check_artifacts.py` returns today. The queue item `artifact-missing-target-id` still
  carried `scope_estimate: 12` from its filing and is rescoped to 44. The observation's second
  half is a tooling question already covered by 111/127's shape: `validate.py` reports these as a
  *note* rather than an error, so they pass CI silently and render as dead rows.

