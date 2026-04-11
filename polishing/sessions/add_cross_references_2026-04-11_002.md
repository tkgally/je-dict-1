## Session: Add Cross-References (Homophone Asymmetry Cluster)
Date: 2026-04-11

### Mode
Cluster Mode, restricted to `homophone` type asymmetries. Processed all 89
one-way homophone cross-references identified by
`build/find_merge_candidates.py --asymmetry-only`. No tracking file was updated
(asymmetry-driven, not sequential).

### Approach
For each asymmetric pair "source → target (homophone)", the source already had
a homophone cross-reference; the target was missing the reciprocal back-link.
Only the target entries were modified (per the `add_cross-references.md`
instruction: "When visiting target entries, ONLY add the reciprocal back-link
to the starting entry"). No other cross-references on the target entries were
audited, modified, or migrated. Per the task's homophone-specific note, no
migration from `cross_references: homophone` to `prominent_see_also` was
attempted — that is a separate concern.

### Implementation note
Because many target entries have pre-existing pairs of duplicate top-level
`conjugation` keys (legacy dead stub data alongside the live
`conjugation` forms block), edits were applied as surgical text insertions
rather than full JSON re-serialization. This preserves the duplicate-key
artifact as-is and avoids unrelated diff churn. The surgical edit targets the
last `cross_references` block (which is the one `json.load` sees) and updates
the `modified` timestamp in place.

### Label Convention
All new labels describe the TARGET of the reference (i.e., the source entry of
the original one-way link, which is now the target of the back-link). Labels
are short distinguishing glosses taken from the first comma/semicolon segment
of the source entry's `gloss` field. This matches the style used in the
existing asymmetric links on the source side.

### cross_references Added (89 back-links across 88 target entries)

Format: `SOURCE → TARGET (label applied to new back-link)`
Note: target 05617_kakushin received two back-links (from 13105 and 13682);
all other targets received one.

- 10372_tsukekomu → 09007_tsukekomu (to take advantage of)
- 11189_joujou_b → 11187_joujou (stock market listing)
- 11377_joubu → 01156_joubu (upper part, top section)
- 11639_kouen → 00581_kouen (public performance, show)
- 11679_heiki → 00095_heiki (weapon, arms)
- 11692_sadou → 04451_sadou (operation, activation (of machinery))
- 11694_shisetsu → 02503_shisetsu (envoy, delegate, diplomatic mission)
- 11711_fushi → 03713_fushi (immortality, undeath)
- 11717_kaeru → 01089_kaeru (to substitute, to replace with)
- 11724_kousen → 04144_kousen (battle, engagement in warfare)
- 11725_boutou → 09400_boutou (beginning, opening)
- 11735_shukketsu → 09604_shukketsu (bleeding, hemorrhage)
- 11743_saiken → 08870_saiken (reconstruction, rebuilding)
- 11744_saikou → 02637_saikou (reconsideration, rethinking)
- 11749_nairan → 11109_nairan (civil war, internal strife)
- 11799_shimeru → 00485_shimeru (to occupy)
- 12098_hensou → 07344_hensou (disguise, dressing up (as someone else))
- 12734_mono → 10988_mono (person (formal/written))
- 12765_toushu → 06563_toushu (head of a household, family head)
- 12766_nen → 09876_nen (thought, feeling)
- 12925_koubou → 12418_koubou (offense and defense, attack and defense)
- 12934_shishou → 12421_shishou (hindrance, obstacle, impediment)
- 12941_haisha → 01696_haisha (loser, defeated person)
- 12944_koji → 07967_koji (historical anecdote, old story, legend)
- 13005_yuushi → 04775_yuushi (volunteers, interested parties, like-minded people)
- 13075_saisoku → 04159_saisoku (fastest)
- 13091_sonchou → 03327_sonchou (village chief, village mayor)
- 13105_kakushin → 05617_kakushin (core, crux, heart of a matter)
- 13370_sumu → 00673_sumu (to become clear, to be limpid)
- 13370_sumu → 01950_sumu (to become clear, to be limpid)
- 13375_sumi → 01625_sumi (charcoal)
- 13379_kasou → 11372_kasou (cremation)
- 13390_senzai → 03304_senzai (latent, potential, hidden)
- 13391_hoteru → 01027_hoteru (to feel hot, to flush, to burn)
- 13640_hakkou → 13605_hakkou (coming into effect, taking effect)
- 13646_kanshuu → 05523_kanshuu (supervision, editorial oversight)
- 13668_kango → 13439_kango (nursing, care)
- 13682_kakushin → 13105_kakushin (conviction, confidence)
- 13682_kakushin → 05617_kakushin (conviction, confidence)
- 13698_hassei → 03133_hassei (vocalization, uttering)
- 15326_kentou → 02710_kentou (good fight)
- 15326_kentou → 02795_kentou (good fight)
- 17728_kikai → 02366_kikai (apparatus)
- 17728_kikai → 01302_kikai (apparatus)
- 17835_gishi → 02680_gishi (older sister-in-law)
- 17950_gasshou → 04900_gasshou (pressing palms together (in prayer or greeting))
- 17961_shinpu → 12981_shinpu (Catholic priest)
- 17969_seisho → 04326_seisho (Bible)
- 17973_hitome → 08728_hitome (public eye)
- 18057_kousei → 01751_kousei (rehabilitation, turning over a new leaf)
- 18057_kousei → 02729_kousei (rehabilitation, turning over a new leaf)
- 18082_kenzai → 11567_kenzai (becoming manifest, becoming apparent)
- 18084_chuusei → 05524_chuusei (neutral, neuter)
- 18165_suisei → 05053_suisei (Mercury)
- 18188_boueki → 01727_boueki (epidemic prevention)
- 18189_kyuushi → 17081_kyuushi (sudden death)
- 18262_kidou → 06360_kidou (startup)
- 18271_ichidan → 08951_ichidan (a group)
- 18281_kisei → 12419_kisei (parasitism)
- 18281_kisei → 02598_kisei (parasitism)
- 18572_seirei → 13820_seirei (Holy Spirit)
- 18641_muchi → 16915_muchi (ignorance)
- 18647_yodan → 15129_yodan (premature judgment)
- 18648_josou → 15506_josou (weeding)
- 18648_josou → 12643_josou (weeding)
- 18653_kanbu → 06875_kanbu (affected area)
- 18980_haiki → 12482_haiki (exhaust)
- 18996_shikkou → 17129_shikkou (execution)
- 19314_tenkou → 03444_tenkou (conversion)
- 19314_tenkou → 03558_tenkou (conversion)
- 19875_naisen → 04279_naisen (civil war)
- 19880_kyuukou → 01386_kyuukou (school closure)
- 19880_kyuukou → 19194_kyuukou (school closure)
- 19906_katsu → 01199_katsu (and, moreover, at the same time)
- 20058_kadou → 16938_kadou (movable)
- 20583_moukeru → 14220_moukeru (to make a profit)
- 20595_shihan → 12424_shihan (master instructor)
- 20596_kougai → 14944_kougai (disclosing)
- 20596_kougai → 01403_kougai (disclosing)
- 20597_heikou → 05445_heikou (balance)
- 20597_heikou → 11311_heikou (balance)
- 20609_kaiki → 12061_kaiki (mysterious)
- 20612_kousha → 02802_kousha (getting off (a vehicle))
- 20612_kousha → 02801_kousha (getting off (a vehicle))
- 20808_shokuzai → 04940_shokuzai (atonement)
- 22482_daisuu → 05145_daisuu (number of machines, vehicles, or equipment)
- 22485_kouei → 19436_kouei (publicly operated)
- 22486_honsen → 08239_honsen (main line (railway, road, etc.))
- 22496_magari → 22383_magari (bend)

### Statistics
- Entries modified: 88
- Back-links added: 89
- References fixed/migrated: 0
- Entry range: non-sequential (spans 00095–22383)

### Verification
- `build/validate.py`: 23021/23021 entries valid; warning counts identical to
  baseline before edits (3 cross-reference warnings, 26 homonym mismatch
  warnings, 29 hardenable refs, 545 POS consistency warnings). No new warnings
  on modified entries.
- `build/find_merge_candidates.py --asymmetry-only`:
  - Before: 3087 asymmetric, 2346 symmetric pairs (homophone: 89)
  - After:  2998 asymmetric, 2435 symmetric pairs (homophone: 0)
  - Delta: asymmetric −89, symmetric +89, as expected.
- `grep -c "cross_references: homophone"` on the post-edit asymmetry report: 0.
- `make build`: clean rebuild, 23021 entries.

### Notes
- This is a focused clean-up of the `homophone` asymmetry type, a follow-up to
  session 001 (which handled `keigo`). Remaining asymmetry types after this
  session: related, synonym, contrast, antonym, see_also,
  prominent_see_also, pair.
- A number of target entries carry legacy duplicate top-level `conjugation`
  keys (an earlier stub block alongside the live forms block). These were left
  untouched — the surgical text insertion only modifies the `cross_references`
  array and the `modified` timestamp.
- Homophone-to-`prominent_see_also` migration for easily-confused pairs was
  intentionally deferred per task instructions.

### Next Entry
N/A — asymmetry-driven session, not sequential.
