## Session: Semantic Labels
Date: 2026-04-11
Entries checked: priority positions 1-640 (approximately 640 entries)

### Summary
First session for this polishing task. Used priority mode (polishing/priority/notes.txt).
Reviewed ~640 entries from the top of the priority list and corrected 56 with wrong semantic tags.

### Corrections Made

#### Template artifacts (object/furniture/electronics on abstract/grammatical words)
- 03095_nado (particle): time-general → grammatical
- 05432_jan (particle): communication → grammatical
- 02900_gurai (particle): electronics, furniture → grammatical
- 06914_yone (particle): furniture → grammatical
- 06921_kashira (particle): emotion → grammatical
- 03476_doushitemo (adverb): furniture → descriptive
- 04113_ooyoso (adverb): electronics, furniture, time-general → descriptive
- 07124_chokochoko (adverb): building → descriptive
- 05274_gatagata (adverb): food → descriptive
- 04814_hirahira (adverb): body-part → descriptive
- 05889_pachipachi (adverb): electronics → descriptive
- 05893_gakkuri (adverb): electronics → descriptive
- 05268_harahara (adverb): body-part → descriptive
- 05836_hinyari (adverb): body-part → descriptive
- 05985_zawazawa (adverb): emotion → descriptive

#### Invalid tag names (not in VALID_SEMANTIC)
- 01706_i (stomach): body → body-internal
- 02173_ase (sweat): body → body-part
- 01156_joubu (sturdy): quality → descriptive
- 01201_nigai (bitter): taste, emotion → descriptive
- 00793_kusuri (medicine): health → general
- 01080_kiwotsukete (take care): farewell → expression
- 01074_ganbatte (good luck): encouragement → expression
- 01745_ima (living room): place → building
- 01763_ajia (Asia): place → geography
- 01767_afurika (Africa): place → geography

#### Multi-tag template errors
- 04438_houdou (news coverage): building, communication, education, time-general, transportation → communication
- 05644_houkokusuru (to report): building, communication, education, transportation → communication
- 03129_nasakenai (miserable): emotion, food, leisure, time-general → emotion
- 04467_shichou (viewing): clothing, time-general, tool → cognition
- 01466_chuusha (parking): building, transportation → transportation
- 06732_uchiageru (launch): clothing, leisure → action
- 00760_toru (take photo): electronics, leisure → action
- 03032_doukyuusei (classmate): furniture → person, education
- 03743_mikata (ally): building, transportation → person
- 05871_torikomu (take in): building, transportation → action
- 04933_kemushi (caterpillar): animal-insect, body-part → animal-insect
- 04427_juuden (charging): animal-mammal, electronics → electronics
- 00972_mune not changed; 01108_itai: body-part, emotion → descriptive

#### Single-tag mis-categorizations
- 01118_nai (is not): kept descriptive (already correct)
- 00696_genki (healthy): emotion → descriptive
- 00785_karui (light weight): size → descriptive
- 00804_omoi (heavy): size → descriptive
- 01093_rippa (splendid): emotion → descriptive
- 06735_sashikakaru (approach): electronics → movement
- 06662_issai (all/entirely): transportation → quantity
- 04442_saisei (playback): time-general → action
- 01460_tanjou (birth): action → existence
- 02047_kiniiru (to like): greeting → emotion
- 03435_choudai (please give): greeting → expression
- 03754_meirei (order): communication, time-general → communication
- 05100_touron (debate): animal-mammal → communication
- 05463_yousei (request): electronics → communication
- 05337_baeru (photogenic): time-general → action
- 06529_renpai (losing streak): work → leisure
- 04622_ondanka (warming): time-general, weather → weather
- 00618_atatakai (warm): time-general, weather → weather
- 02154_shita (tongue): body-part, direction → body-part
- 02159_tsume (nail/claw): education, tool → body-part
- 03579_hitai (forehead): general → body-part
- 03553_hakushu (applause): electronics → action
- 03575_bakuhatsu (explosion): geography → action
- 03670_yome (bride/wife): education → family

### Common Patterns Observed
1. **Template artifact tags** — many entries had default tags (furniture, electronics,
   building, transportation) that don't match the word meaning at all. These are
   clearly generated defaults never revised.
2. **Invalid tag names** — several entries used tags not in VALID_SEMANTIC list:
   `body` (should be `body-part` or `body-internal`), `health`, `place`,
   `farewell`, `encouragement`, `taste`, `quality`. The `quality` tag alone
   appears in 78 entries across the dictionary.
3. **Multi-tag spam** — some entries had 4-5 unrelated tags glued together
   (`04438_houdou` had 5, `03129_nasakenai` had 4).
4. **Onomatopoeia/gitaigo adverbs** — often tagged with object categories
   (body-part, food, electronics) instead of `descriptive`.
5. **Particles/function words** — sometimes tagged with emotional or content
   categories instead of `grammatical`.

### Next Entry
03677 (priority position 641)
