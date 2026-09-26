## Session: Comprehensive Polish
Date: 2026-05-12
Entries processed: 00826 through 00850 (25 entries)

### Per-entry changes
- 00826 (aji 味): completed inline link coverage in notes (COMMON PATTERNS, FLAVOR TYPES, COMPOUNDS, figurative use); tier-1 only
- 00827 (arau 洗う): completed inline link coverage in notes; added contrast cross-ref to 洗濯する (09656_sentakusuru)
- 00828 (asatte 明後日): completed inline link coverage in notes (day-sequence section with おととい, きのう, きょう, あした, あさって linked)
- 00829 (basho 場所): completed inline link coverage in notes
- 00830 (benri 便利): completed inline link coverage in notes
- 00831 (daitai だいたい): completed inline link coverage in notes
- 00832 (dandan だんだん): completed inline link coverage in notes (similar words: 少しずつ→20047, 徐々に→04131, しだいに→13399)
- 00833 (dekakeru 出かける): completed inline link coverage in notes
- 00834 (doushite どうして): completed inline link coverage in notes
- 00835 (erabu 選ぶ): completed inline link coverage in notes
- 00836 (fuan 不安): completed inline link coverage in notes; added antonym cross-ref to 安心 (01288_anshin)
- 00837 (fukuro 袋): completed inline link coverage in notes (compound types linked: レジ袋→09531, ゴミ袋→22230, etc.)
- 00838 (foku フォーク): completed inline link coverage in notes (tableware links: スプーン→00704, はし→02265, etc.)
- 00839 (furu 降る): completed inline link coverage in notes (tier-1 only, entry was clean)
- 00840 (gomi ゴミ): completed inline link coverage in notes (trash categories: 燃えるゴミ→17105, 資源ゴミ→09537, 生ゴミ→08044, etc.)
- 00841 (hajimaru 始まる): completed inline link coverage in notes (tier-1 only)
- 00842 (hatake 畑): completed inline link coverage in notes
- 00843 (hazukashii 恥ずかしい): completed inline link coverage in notes
- 00844 (henji 返事): completed inline link coverage in notes
- 00845 (hirou 拾う): completed inline link coverage in notes
- 00846 (hitsuyou 必要): completed inline link coverage in notes
- 00847 (hotondo ほとんど): completed inline link coverage in notes
- 00848 (ike 池): completed inline link coverage in notes (湖→00867, 沼→02160, 電池→01472, 日本庭園→19199, 鯉→02209)
- 00849 (iro 色): completed inline link coverage in notes (赤→02842, 青→02841, 黄色→02870, 白→13854, 黒→02205, 赤色→23327, 青色→22937, 色々→02352, 顔色→25468)
- 00850 (iwa 岩): completed inline link coverage in notes (石→02177, 岩山→23863, 溶岩→13328, 日本庭園→19199; noentry: 岩場, 岩肌, 岩登り)

### Candidates added
- 岩場 (いわば): rocky area; seen in entry 00850
- 岩肌 (いわはだ): rock face, bare rock surface; seen in entry 00850
- 岩登り (いわのぼり): rock climbing; seen in entry 00850

### Observations logged
- [tooling] verify_furigana.py incorrectly flags kanji in the baseform part of inline link markers (e.g., ⟦{湖|みずうみ}→湖：...⟧ — the 湖 after → is not display text). All entries with inline links in notes will spuriously fail verify_furigana.py even when all display kanji have proper furigana. The schema validator (validate.py) correctly passes. Script needs updating to skip content between → and ⟧ in inline links.

### Next entry
00851
