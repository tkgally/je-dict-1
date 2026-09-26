## Session: Furigana Correctness
Date: 2026-04-10
Mode: Priority order (from polishing/priority/furigana.txt)
Entries checked: 00500-00559 (59 priority entries, starting from priority position after 00499)

### Entries Processed (in priority order)
00500_takai, 00501_ashita, 00502_de, 00503_hataraku, 00504_kara,
00505_michi, 00506_atarashii, 00507_heya, 00508_kaeru, 00509_kudamono,
00510_mijikai, 00511_noru, 00512_to, 00513_deru, 00514_hayai,
00515_iu, 00516_kuruma, 00517_muzukashii, 00518_nugu, 00519_hashiru,
00520_morau, 00521_okiru, 00522_densha, 00523_hana, 00524_ki,
00525_me, 00526_oshieru, 00527_benkyousuru, 00528_kesu, 00529_tooi,
00530_chikai, 00531_hajimeru, 00532_kariru, 00533_osoi, 00534_dare,
00535_harau, 00536_itsu, 00538_aruku, 00539_doko, 00540_hiru,
00541_kiru, 00542_ban, 00543_dou, 00544_gogo, 00545_oyogu,
00546_ageru, 00547_dore, 00548_gozen, 00549_haha, 00550_asobu,
00551_dono, 00552_kazoku, 00553_pan, 00554_kodomo, 00555_tomaru,
00556_umi, 00557_dekiru, 00558_kao, 00559_onna

(00537 was not present in the priority list, so skipped.)

### Corrections Made
None. All checked entries have correct furigana readings for every kanji in
headword, reading, examples, notes, and cross-references. Compound readings,
rendaku, irregular readings (e.g., 二十歳→はたち, 今日→きょう, 昨日→きのう),
and special variants (速い／早い read はやい) all verified correct.

### Observations (out of scope — not corrected)
- 00536_itsu and 00543_dou contain spurious `conjugation` tables treating
  the interrogative adverbs as godan verbs (生成 non-existent forms like
  いたない, いちます, どっている). These are data/schema bugs unrelated to
  furigana correctness and were not modified in this session. Worth reporting
  for a separate cleanup task.

### Next Entry
Next in priority list: 00560_kuchi
