## Session: Furigana Completeness
Date: 2026-04-10
Mode: Priority-ordered (polishing/priority/furigana.txt)
Entries processed: priority list, IDs ≥ 08051 (~232 entries scanned, 131 modified)

### Approach
Processed entries from the priority file in order, but filtered to IDs ≥ 08051
based on the progress file. Identified real missing-furigana issues by writing
a filter that ignores false positives from inline link base forms
(⟦surface→base：id⟧ — kanji inside the `base` portion don't need furigana).

This reduced the apparent count from 4,011 (raw `find_missing_furigana.py`
output) to 131 genuine issues in the priority list, all of which were fixed.

### Common issues fixed
- Grammar-term words mentioned in notes without furigana:
  - `形容動詞`, `連用形`, `連体詞`, `他動詞`, `五段動詞`, `四字熟語`, `擬態語`,
    `擬音語`, `謙譲語`, `尊敬語`, `格助詞`, `自動詞`, `サ変`
- Cross-referenced kanji words in notes/explanations without furigana
  (e.g. `秀才`, `凡人`, `造花`, `自立`, `自律`, `更`, `凡人`, `源氏物語`)
- `的` suffix missing furigana on adjectival forms (`伝統的`, `熱狂的`,
  `意味合い` context, `役割分担`, `異端的`, `伝統的`, etc.)
- Malformed furigana constructs fixed:
  - `{お{願|ねが}い→お願い}した` → `お{願|ねが}いした` (10135_teishisei)
  - `{熱狂|ねっきょう}{ぶり|}` → `{熱狂|ねっきょう}ぶり` (13479_nekkyou)
  - `{柔軟|じゅうなん}性{|せい}` → `{柔軟性|じゅうなんせい}` (13101_juunan)
  - `{着|き}心地{ごこち}` → `{着|き}{心地|ごこち}` (08349_sumigokochi)
- Example sentences with unwrapped kanji (`二人`, `百年`, `一人一人`, `一組`,
  `二週間`, `商習慣`, etc.)

### Changes Made (131 entries)
All entries in priority list with ID ≥ 08051 that had genuine missing-furigana
issues were fixed. A non-exhaustive sample:

- 08319_keihin, 08349_sumigokochi, 08704_naniyara, 08726_sakenosakana,
  08862_inkuruushibu, 08864_fashiriteetaa, 08871_bougyoritsu, 08884_iishii,
  08919_ippin, 09311_moteru, 09476_yori, 09495_sanzui, 09497_na, 09500_au,
  09511_sei, 09512_fu, 09585_dentou, 09590_imiai, 09751_neru, 09782_ondo,
  09885_sugi, 09896_shuuhen, 09900_manen, 10001_soukan, 10044_zure,
  10049_yakuwaribuntan, 10135_teishisei, 10351_shikameru, 11051_janpu,
  11547_tsukaeru, 11548_tahou, 11551_kari, 11561_reinen, 11792_sougyou,
  12131_kokusei, 12185_daikibo, 12327_kawaigaru, 12543_houfutsu, 12568_kokochi,
  13101_juunan, 13323_shimeru_damp, 13479_nekkyou, 13552_igi, 13575_itan,
  13811_zeppin, 13955_jiritsu, 14631_najimu, 14867_koui, 15133_shinobiyoru,
  15219_teikuu, 15331_muragaru, 15524_fukahi, 15841_kyuuseichou, 15925_menkai,
  15929_tsuyogaru, 15930_isuwaru, 16011_isseini, 16014_kachitoru, 16644_genji,
  16646_renyoukei, 16647_gangu, 16648_bakuyasu, 16649_aisowarai, 16652_ittou,
  16653_chuukanhoukoku, 16655_senpukukikan, 16656_chokuryuu, 16657_kyouzaihi,
  16658_jikosuisen, 16663_gakushuuzukue, 16664_getsudo, 16666_honsekichi,
  16670_shidouan, 16671_mamedenkyuu, 16672_koorigashi, 16673_yuwakashiki,
  16675_kakujoshi, 16676_sangakurenkei, 16677_kourigyou, 16679_byousoku,
  16680_funsoku, 16682_shoutokutaishi, 16683_nennensaisai, 16684_himatsubushi,
  16685_donjiri, 16686_tekishita, 16687_mimuku, 16954_keigen, 16956_kanbyou,
  16964_saranaru, 17274_omieninaru, 17540_dosha, 17567_koode, 17569_keshikakeru,
  17576_suriyoru, 17758_bouzen, 18297_shuusai, 18298_bonjin, 18300_zouka,
  18312_shikinkyori, 18317_sokudan, 18321_koyama, 18328_zataku, 18367_yasui,
  18368_zurai, 18369_owaru, 18370_hajimeru, 18371_naosu, 18511_daikokubashira,
  18549_takarakuji, 19337_sake, 19341_shiba, 19354_hyou, 19355_kiwa,
  19356_mato, 19792_kikite, 20354_watashidomo, 20377_danzuru, 20379_nabebuta,
  20573_bukabuka, 20658_hanashikomu, 20668_nakagayoi, 21018_omona,
  21893_yogoto, 21900_nekkyouteki, 22141_guigui, 22191_tadano, 22663_ankokugai,
  22835_eizoku, 22836_hidarigawa, 22837_nichiyou

### Note on remaining issues
The raw `find_missing_furigana.py` report still shows ~4,000 entries, but the
vast majority are false positives caused by kanji appearing inside inline link
base forms (`⟦surface→base：id⟧`), which is by convention and does not require
furigana. A smarter filter that strips inline link base forms first confirms
that all priority-listed entries (ID ≥ 8051) are now clean.

### Next Entry
22991 (end of priority list reached for IDs ≥ 8051)
