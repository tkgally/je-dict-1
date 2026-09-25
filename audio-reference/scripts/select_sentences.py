"""Build data/sentences.json: the 100 test sentences.

Each item: (example id, category, focus note, manual kana override or None).
Heteronym items name the spelling whose intended reading the TTS must follow
(given by the dictionary's furigana).  Items containing digits or Latin
letters have no furigana for those parts, so their full reading is given by
hand (with acceptable alternatives after "|")."""
import json

from common import DATA

H = "heteronym"
PICKS = [
    # --- words whose furigana selects a less common / context-dependent reading
    ("11695_konnichi_ex2", H, "今日＝こんにち (not きょう)", None),
    ("30530_nikakete_ex2", H, "明日＝あす", None),
    ("27453_myounichi_ex2", H, "明日＝みょうにち; 十時", None),
    ("27458_uwate_ex1", H, "上手＝うわて (not じょうず)", None),
    ("27458_uwate_ex6", H, "上手＝かみて, 下手＝しもて", None),
    ("00499_sakana_ex4", H, "市場＝いちば; particle へ", None),
    ("10993_tsuitachi_ex1", H, "一日＝ついたち; 元日", None),
    ("27454_sakujitsu_ex3", H, "昨日＝さくじつ; 行った＝おこなった", None),
    ("00092_hashigo_ex3", H, "昨夜＝ゆうべ", None),
    ("10603_kiten_ex3", H, "大事＝おおごと (not だいじ)", None),
    ("12866_yoridokoro_ex5", H, "故郷＝ふるさと", None),
    ("00635_juuichigatsu_ex3", H, "紅葉＝もみじ", None),
    ("12617_shinjuu_ex2", H, "心中＝しんじゅう", None),
    ("16081_samuke_ex2", H, "寒気＝さむけ", None),
    ("14765_shikishi_ex2", H, "色紙＝しきし", None),
    ("28020_monaka_ex2", H, "最中＝もなか (the sweet)", None),
    ("10340_sanaka_ex2", H, "最中＝さなか", None),
    ("06464_futae_ex4", H, "二重＝ふたえ", None),
    ("28066_ikkou_ex1", H, "一行＝いっこう", None),
    ("20452_funbetsu_ex1", H, "分別＝ふんべつ", None),
    ("20494_mokka_ex2", H, "目下＝もっか", None),
    ("20909_doujouteki_ex2", H, "世論＝せろん", None),
    ("29953_shoubaihanjou_ex2", H, "利益＝りやく", None),
    ("10535_kazaguruma_ex2", H, "風車＝かざぐるま", None),
    ("19257_ichimokuoku_ex2", H, "一目＝いちもく", None),
    ("02778_katagata_ex4", H, "方々＝かたがた; keigo", None),
    ("00320_nippon_ex1", H, "日本＝にっぽん", None),
    ("07459_ichigen_ex3", H, "一見＝いちげん", None),
    ("08809_nanibun_ex4", H, "何分＝なにぶん", None),
    ("20383_tassha_ex3", H, "身体＝からだ", None),
    ("26869_akindo_ex1", H, "商人＝あきんど", None),
    ("30278_hantaihoukou_ex3", H, "十分＝じゅっぷん (not じゅうぶん)", None),
    ("26895_ooyasan_ex2", H, "大家＝おおや", None),
    ("12582_tsuwamono_ex1", H, "強者＝つわもの", None),
    ("28490_ginnan_ex2", H, "銀杏＝ぎんなん", None),
    ("26786_kuroko_ex2", H, "黒子＝くろこ", None),
    ("26231_kagerou_ex1", H, "蜻蛉＝かげろう; 一日＝いちにち", None),
    ("16272_misoka_ex1", H, "三十日＝みそか", None),
    ("16962_hiyori_ex1", H, "日和＝ひより", None),
    ("21222_kobara_ex3", H, "空いた＝すいた", None),
    ("10587_yorisou_ex6", H, "辛い＝つらい (not からい)", None),
    ("00555_tomaru_ex4", H, "止んで＝やんで", None),
    ("19365_aruji_ex2", H, "主＝あるじ", None),
    ("05998_keno_ex2", H, "抱いた＝いだいた", None),
    ("02987_watakushi_ex2", H, "私＝わたくし", None),
    ("02933_hatachi_ex4", H, "二十歳＝はたち", None),
    ("02934_hatsuka_ex8", H, "二十日＝はつか", None),
    ("02983_youka_ex9", H, "八日＝ようか", None),
    ("15498_amata_ex1", H, "数多＝あまた", None),
    ("10082_minamo_ex3", H, "水面＝みなも", None),
    ("03458_toshitsuki_ex1", H, "年月＝としつき; 経った＝たった", None),
    ("00310_nengetsu_ex5", H, "年月＝ねんげつ (contrast with としつき)", None),
    ("13571_kanmi_ex5", H, "甘味処＝かんみどころ", None),
    ("26262_sokuseki_ex3", H, "足跡＝そくせき", None),
    ("05797_tokonoma_ex3", H, "床＝とこ; 生けて＝いけて", None),
    ("13000_tsukigime_ex1", H, "月極＝つきぎめ", None),
    ("28376_too_ex2", H, "十＝とお", None),
    ("29264_nijimidasu_ex1", H, "額＝ひたい", None),
    ("10452_hatsuhinode_ex3", H, "初日の出＝はつひので", None),
    ("00801_obasan_ex1", H, "上手＝じょうず (contrast with うわて)", None),
    # --- digits and Latin letters (no furigana; reading supplied by hand)
    ("07142_shukuhakuryou_ex2", "digits", "1泊1万円",
     "しゅくはくりょうはいっぱくいちまんえんだ。"),
    ("21132_kikkari_ex1", "digits", "3時",
     "きっかりさんじにきてください。"),
    ("16680_funsoku_ex3", "digits", "徒歩5分, 分速80メートル",
     "ふどうさんのこうこくで「えきからとほごふん」はふんそくはちじゅうメートルでけいさんされている。"),
    ("08827_manyoushuu_ex1", "digits", "約4,500首",
     "まんようしゅうにはやくよんせんごひゃくしゅのうたがある。"),
    ("24999_kabuken_ex3", "digits", "2009年",
     "にせんきゅうねんにかぶけんのでんしかがかんりょうし、かみのかぶけんはげんそくとしてはいしされた。"),
    ("00005_appu_ex4", "digits", "20%",
     "うりあげがぜんねんよりにじゅっパーセントアップした。|うりあげがぜんねんよりにじっパーセントアップした。"),
    ("00010_banchi_ex3", "digits", "3丁目5番地",
     "さんちょうめごばんちにすんでいます。"),
    ("08852_enueichikee_ex3", "latin+digits", "NHK, 約2,000円",
     "エヌエイチケーのじゅしんりょうはげつがくやくにせんえんだ。|エヌエッチケーのじゅしんりょうはげつがくやくにせんえんだ。"),
    ("05398_waifai_ex1", "latin", "Wi-Fi", "ワイファイにせつぞくする。"),
    ("24762_shinteishi_ex2", "latin", "AED",
     "しんていしのばあいは、すぐにエーイーディーをしようしてください。"),
    ("07758_tiipiioo_ex2", "latin", "TPO", "ティーピーオーをかんがえてこうどうしなさい。"),
    # --- dialogue, questions, register
    ("10767_maane_ex2", "dialogue", "two speakers, casual", None),
    ("04011_naninani_ex9", "dialogue", "何々＝なになに; exclamation", None),
    ("02845_iie_ex4", "dialogue", "basic polite exchange", None),
    ("00973_nanji_ex3", "question", "何時＝なんじ", None),
    ("02922_docchi_ex8", "question", "casual question", None),
    ("13042_kyuu_ex3", "question", "polite request", None),
    ("29011_kinkyouukagai_ex3", "keigo", "humble business language", None),
    ("18008_kiden_ex3", "keigo", "formal letter language", None),
    ("01062_tadaima_ex9", "keigo", "ただいま＝right now", None),
    ("23425_eeto_ex2", "casual", "filler ええと, っけ", None),
    ("05432_jan_ex4", "casual", "じゃん", None),
    ("16617_tteiuka_ex3", "casual", "っていうか, quotative って", None),
    # --- long sentences
    ("13994_renkon_ex3", "long", "long, quotation inside", None),
    ("27385_shingaasonguraitaa_ex4", "long", "long katakana compound", None),
    ("03201_shimai_ex5", "long", "two sentences", None),
    ("00750_semai_ex5", "long", "three sentences, basic tier", None),
    ("24064_tsuitotsujiko_ex4", "long", "long relative clause", None),
    # --- sound symbolism, katakana, counters, short basics
    ("05375_meramera_ex2", "onomatopoeia", "めらめら", None),
    ("05992_patapata_ex3", "onomatopoeia", "ぱたぱた", None),
    ("30702_puripeidokaado_ex3", "katakana", "loanwords", None),
    ("10293_taguzuke_ex3", "katakana", "SNS loanwords", None),
    ("24582_ochoushi_ex1", "counter", "一本＝いっぽん", None),
    ("06447_enchou_ex9", "counter", "十二回", None),
    ("20845_irochigai_ex3", "counter", "三枚", None),
    ("02973_muika_ex9", "counter", "六日間＝むいかかん", None),
    ("00671_soto_ex1", "short", "very short, basic", None),
    ("09476_yori_ex2", "short", "私＝わたし (contrast with わたくし)", None),
    ("03991_yuge_ex4", "core", "湯気, 美味しそう", None),
    ("05056_keisatsukan_ex5", "core", "二人＝ふたり", None),
]

if __name__ == "__main__":
    ex = {}
    for line in open(DATA / "all_examples.jsonl"):
        e = __import__("json").loads(line)
        ex[e["id"]] = e
    out = []
    for i, (eid, cat, focus, manual) in enumerate(PICKS, 1):
        e = ex[eid]
        kana = e["kana"]
        alts = []
        if manual:
            kana, *alts = manual.split("|")
        out.append({
            "n": i, "id": eid, "category": cat, "focus": focus,
            "tier": e["tier"], "headword": e["headword"], "entry": e["entry"],
            "plain": e["plain"].strip(), "kana": kana.strip(), "alt_kana": alts,
            "tokens": e["tokens"], "english": e["english"],
            "manual_reading": bool(manual),
        })
    assert len(out) == 100, len(out)
    assert len({o["id"] for o in out}) == 100
    json.dump(out, open(DATA / "sentences.json", "w"), ensure_ascii=False, indent=1)
    import collections
    print(collections.Counter(o["category"] for o in out))
    print(collections.Counter(o["tier"] for o in out))
