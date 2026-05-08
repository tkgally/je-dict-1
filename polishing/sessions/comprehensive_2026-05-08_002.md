## Session: Comprehensive Polish
Date: 2026-05-08
Entries processed: 00006 through 00025 (20 entries)

### Per-entry changes
- 00006 (ある): tier 1 clean — schema, furigana, inline links, back-links to 00495_iru and 01118_nai all valid. No changes. (verify_furigana.py false-positive on inline link metadata after `→`; logged as tooling.)
- 00007 (アウト): added full inline link coverage to ex4–ex6 (15+ new links), plus いる/なる/だ on others; updated modified timestamp.
- 00008 (バッグ): linked all bag-type compounds and counters in notes; added 鞄 alt-form link; added back-link from 00637_kaban; ボストンバッグ added as candidate.
- 00009 (バイオリン): linked バイオリニスト (noentry) and counters 台/丁 in notes; バイオリニスト added as candidate.
- 00010 (番地): full inline link coverage of address-structure example in notes; added cross_references to 01430_juusho, 09491_choume, 13040_gou and back-links on all three (09491_choume previously had no cross_references field at all).
- 00011 (ばね): full inline link coverage of COMMON EXPRESSIONS, COMPOUNDS sections in notes; コイル added as candidate.
- 00012 (×/バツ): linked SLANG, CONTRAST sections in notes (バツイチ→11119, 一→00705, 丸→02167, さんかく→04177); バツニ added as candidate.
- 00013 (ベンチ): full inline link coverage on ex4–ex6 and notes (COMMON COLLOCATIONS, SPORTS USAGE); ベンチプレス, ダッグアウト added as candidates.
- 00014 (美容): linked examples ex1, ex4, ex5; full link coverage in notes (compounds, contrast, related); added cross_references to 06319_biyouin, 15428_biyoushi, 02706_kenkou; back-links added on 06319_biyouin and 15428_biyoushi (15428 previously had empty cross_references); 理容院 added as candidate.
- 00015 (盆地): linked 盆, 京都, 平野, 谷 and noentry markers for 奈良/甲府 in notes; added cross-ref to 02223_tani; back-link added on 02223_tani.
- 00016 (ボーイ): full inline link coverage on ex4–ex8 and notes; カウボーイ, プレイボーイ, ボーイフレンド, ボーイスカウト, カウボーイハット added as candidates.
- 00017 (ボール): linked ex8, ex9, ex15 and full inline link coverage in notes (sports/baseball/cooking sections); サッカーボール, フォアボール, スリーボール, ツーストライク added as candidates.
- 00018 (ボート): full inline link coverage in notes (collocations, types, related words); モーターボート, ゴムボート, 手漕ぎ, カヤック added as candidates.
- 00019 (ぼろ): full inline link coverage on COMMON EXPRESSIONS, ADJECTIVE FORM, IDIOM sections; added cross-ref to 05164_boroboro.
- 00020 (部品): full inline link coverage in notes; added cross-ref to 11272_paatsu and reciprocal back-link.
- 00021 (分布): linked ex1 (分布する→する); full inline link coverage in notes; 図 link corrected to existing 03368_zu; 地理的 added as candidate.
- 00022 (ブレーキ): full inline link coverage on ex4–ex6 and notes; サイドブレーキ, フットブレーキ, エンジンブレーキ added as candidates.
- 00023 (部首): full inline link coverage in notes (radical names, related terms); added cross_references to 09480_kanji and 13581_kakusuu; てへん, くさかんむり added as candidates.
- 00024 (チャイム): full inline link coverage in notes (DOORBELL, SCHOOL BELL, OTHER); added cross-ref to 04885_intaahon; ドアチャイム, 時報 added as candidates.
- 00025 (小さい): full inline link coverage in notes (special forms, meanings, antonym); added cross-ref to 02913_chiisana and reciprocal back-link.

### Candidates added
- ボストンバッグ (ぼすとんばっぐ): Boston bag, duffel bag; seen in 00008
- バイオリニスト (ばいおりにすと): violinist; seen in 00009
- コイル (こいる): coil; seen in 00011
- バツニ (ばつに): divorced twice (slang); seen in 00012
- ベンチプレス (べんちぷれす): bench press; seen in 00013
- ダッグアウト (だっぐあうと): dugout (baseball); seen in 00013
- 理容院 (りよういん): barbershop; seen in 00014
- カウボーイ (かうぼーい): cowboy; seen in 00016
- プレイボーイ (ぷれいぼーい): playboy; seen in 00016
- ボーイフレンド (ぼーいふれんど): boyfriend; seen in 00016
- ボーイスカウト (ぼーいすかうと): Boy Scouts; seen in 00016
- カウボーイハット (かうぼーいはっと): cowboy hat; seen in 00016
- サッカーボール (さっかーぼーる): soccer ball; seen in 00017
- フォアボール (ふぉあぼーる): walk, four balls (baseball); seen in 00017
- スリーボール (すりーぼーる): three balls (baseball); seen in 00017
- ツーストライク (つーすとらいく): two strikes (baseball); seen in 00017
- モーターボート (もーたーぼーと): motorboat; seen in 00018
- ゴムボート (ごむぼーと): rubber dinghy; seen in 00018
- 手漕ぎ (てこぎ): rowing by hand; seen in 00018
- カヤック (かやっく): kayak; seen in 00018
- 地理的 (ちりてき): geographical (-na adjective); seen in 00021
- サイドブレーキ (さいどぶれーき): hand/parking brake; seen in 00022
- フットブレーキ (ふっとぶれーき): foot brake; seen in 00022
- エンジンブレーキ (えんじんぶれーき): engine brake; seen in 00022
- てへん (てへん): hand radical (扌); seen in 00023
- くさかんむり (くさかんむり): grass crown radical (艹); seen in 00023
- ドアチャイム (どあちゃいむ): door chime; seen in 00024
- 時報 (じほう): time signal, hourly chime; seen in 00024

### Observations logged
- [tooling] verify_furigana.py false-positive on inline link metadata after `→`
- [pattern] Many older noun entries with "RELATED WORDS"/"COMMON COLLOCATIONS"/"COMPOUNDS"/"TYPES OF X" sections in notes have unlinked Japanese; this is the dominant tier-1 work in this 0006–0025 stretch
- [pattern] フライ (00007) is a homograph: existing 11124_furai is "deep-fried food", but the baseball "fly ball" sense has no entry; expanding 11124_furai with the baseball sense would resolve this rather than adding a separate entry

### Next entry
00026
