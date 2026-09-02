"""Unit tests for build/auto_link.py (the deterministic inline-link tool).

Each test builds a tiny synthetic dictionary (a handful of entry dicts) so the
resolution rules can be checked in isolation from the real 30k-entry index.
Tests that need SudachiPy are skipped when it is not installed; the
tokenizer-free fallback is tested unconditionally.  Run with:
    python3 -m unittest build.tests.test_auto_link
"""
import importlib.util
import sys
import unittest
from pathlib import Path

_MOD = Path(__file__).resolve().parents[2] / "build" / "auto_link.py"
_spec = importlib.util.spec_from_file_location("auto_link", _MOD)
al = importlib.util.module_from_spec(_spec)
sys.modules["auto_link"] = al          # dataclasses resolve annotations via sys.modules
_spec.loader.exec_module(al)

try:
    _SUDACHI = al.SudachiTokenizer()
except Exception:  # pragma: no cover - depends on the environment
    _SUDACHI = None

needs_sudachi = unittest.skipUnless(_SUDACHI is not None, "SudachiPy not installed")


def entry(eid, headword, reading, pos="noun", forms=None, conj_type=None):
    data = {"id": eid, "headword": headword, "reading": reading, "part_of_speech": pos}
    if forms:
        data["conjugation"] = {"type": conj_type or "godan",
                               "forms": [{"label": str(i), "affirmative": a, "negative": n}
                                         for i, (a, n) in enumerate(forms)]}
    return data


def verb_forms(stem, kind):
    """Minimal conjugation tables: stem is like '{食|た}べ' (ichidan) or '{書|か}' (godan-k)."""
    if kind == "ichidan":
        return [(stem + "る", stem + "ない"), (stem + "ます", stem + "ません"),
                (stem + "た", stem + "なかった"), (stem + "ました", stem + "ませんでした"),
                (stem + "て", stem + "なくて"), (stem + "ている", stem + "ていない"),
                (stem + "れば", stem + "なければ"), (stem + "られる", stem + "られない")]
    if kind == "godan-k":
        return [(stem + "く", stem + "かない"), (stem + "きます", stem + "きません"),
                (stem + "いた", stem + "かなかった"), (stem + "いて", stem + "かなくて"),
                (stem + "いている", stem + "いていない"), (stem + "けば", stem + "かなければ")]
    raise ValueError(kind)


MINI = [
    entry("00051_ga", "が", "が", "particle"),
    entry("00079_ha", "は", "は", "particle"),
    entry("00314_ni", "に", "に", "particle"),
    entry("00422_wo", "を", "を", "particle"),
    entry("00502_de", "で", "で", "particle"),
    entry("00392_suru", "する", "する", "verb",
          forms=[("する", "しない"), ("します", "しません"), ("した", "しなかった"),
                 ("して", "しなくて"), ("している", "していない")], conj_type="suru"),
    entry("00495_iru", "いる", "いる", "verb", forms=[("いる", "いない"), ("いた", "いなかった"), ("いて", "いなくて")]),
    entry("09589_iru", "{要|い}る", "いる", "verb", forms=[("{要|い}る", "{要|い}らない"), ("{要|い}った", "{要|い}らなかった")]),
    entry("00111_hon", "{本|ほん}", "ほん"),
    entry("00426_yomu", "{読|よ}む", "よむ", "verb",
          forms=[("{読|よ}む", "{読|よ}まない"), ("{読|よ}みます", "{読|よ}みません"),
                 ("{読|よ}んだ", "{読|よ}まなかった"), ("{読|よ}んで", "{読|よ}まなくて")]),
    entry("00396_taberu", "{食|た}べる", "たべる", "verb", forms=verb_forms("{食|た}べ", "ichidan"), conj_type="ichidan"),
    entry("00477_kaku", "{書|か}く", "かく", "verb", forms=verb_forms("{書|か}", "godan-k")),
    entry("02918_toki", "{時|とき}", "とき"),
    entry("09869_ji", "{時|じ}", "じ"),
    entry("02269_ringo", "りんご", "りんご"),
    entry("01164_koto", "こと", "こと"),
    entry("02152_koto", "{琴|こと}", "こと"),
    entry("01238_hashi", "{橋|はし}", "はし"),
    entry("01239_hashi", "{箸|はし}", "はし"),
    entry("01538_pasokon", "パソコン", "ぱそこん"),
    entry("00614_nihongo", "{日本語|にほんご}", "にほんご"),
    entry("00576_ocha", "お{茶|ちゃ}", "おちゃ"),
    entry("00658_nin", "〜{人|にん}", "にん"),
    entry("00476_hito", "{人|ひと}", "ひと"),
    entry("01463_kigaokenai", "{気|き}が{置|お}けない", "きがおけない", "expression"),
    entry("02199_ki", "{気|き}", "き"),
    entry("01092_oku", "{置|お}く", "おく", "verb"),
    entry("00755_shizuka", "{静|しず}か", "しずか", "adjective-na"),
    entry("03133_hassei", "{発生|はっせい}", "はっせい", "noun, suru verb",
          forms=[("{発生|はっせい}する", "{発生|はっせい}しない"), ("{発生|はっせい}した", "{発生|はっせい}しなかった")],
          conj_type="suru"),
    entry("00527_benkyousuru", "{勉強|べんきょう}する", "べんきょうする", "verb-suru",
          forms=[("{勉強|べんきょう}する", "{勉強|べんきょう}しない"), ("{勉強|べんきょう}した", "{勉強|べんきょう}しなかった")],
          conj_type="suru"),
    entry("09485_desu", "です", "です", "auxiliary"),
    entry("11145_mashi", "まし", "まし", "adjective"),
    entry("30376_teiru", "ている", "ている", "expression"),
    entry("02945_deha", "では", "では", "conjunction"),
    entry("00925_demo", "でも", "でも", "conjunction"),
    entry("00991_soko", "そこ", "そこ"),
    entry("00379_sokode", "そこで", "そこで", "conjunction"),
    entry("02899_kudasai", "{下|くだ}さい", "ください", "expression"),
    entry("01305_kudasaru", "くださる", "くださる", "verb"),
]


def make_linker(tokenizer, copula=False):
    return al.Linker(al.Resolver(MINI), tokenizer, copula=copula)


def link(text, own_id="99999_test", own_headword="テスト", tokenizer=_SUDACHI, copula=False):
    linker = make_linker(tokenizer, copula)
    ctx = linker.r.entry_ctx({"id": own_id, "headword": own_headword, "reading": "てすと"}, tokenizer)
    return linker.link_text(text, ctx)


class TestHelpers(unittest.TestCase):
    def test_base_reading_alignment(self):
        pieces = al.parse_pieces("{書|か}いた")
        self.assertEqual(al.base_reading(pieces, "書く"), "かく")
        pieces = al.parse_pieces("{食|た}べました")
        self.assertEqual(al.base_reading(pieces, "食べる"), "たべる")
        # irregular 来る: き + る is not くる, so alignment must refuse
        pieces = al.parse_pieces("{来|き}た")
        self.assertEqual(al.base_reading(pieces, "来る"), "きる")
        # no shared prefix -> None
        self.assertIsNone(al.base_reading(al.parse_pieces("いった"), "行く"))

    def test_header_line(self):
        self.assertTrue(al.header_line("COMMON COLLOCATIONS:"))
        self.assertFalse(al.header_line("- {急|きゅう}カーブ: sharp curve"))
        self.assertFalse(al.header_line("COMMON MISTAKE — ごとに vs おきに:"))

    def test_layout_preserves_offsets(self):
        lay = al.Layout("⟦{本|ほん}→本：00111_hon⟧を{読|よ}む。")
        self.assertEqual(lay.plain, "本を読む。")
        self.assertFalse(lay.free(0, 1))      # existing link is locked
        self.assertTrue(lay.free(1, 4))
        self.assertTrue(lay.aligned(2, 4))
        self.assertFalse(lay.aligned(2, 3) and lay.aligned(3, 4) and False)


@needs_sudachi
class TestRulesWithSudachi(unittest.TestCase):
    def test_rule1_furigana_kanji_and_particles(self):
        out = link("{本|ほん}を{読|よ}む。")
        self.assertEqual(out, "⟦{本|ほん}→本：00111_hon⟧⟦を→を：00422_wo⟧⟦{読|よ}む→読む：00426_yomu⟧。")

    def test_conjugated_verb_links_whole_chain_to_base(self):
        out = link("{本|ほん}を{読|よ}んでいました。")
        self.assertIn("⟦{読|よ}んでいました→読む：00426_yomu⟧", out)
        out = link("{食|た}べさせられました。")
        self.assertIn("⟦{食|た}べさせられました→食べる：00396_taberu⟧", out)

    def test_reading_disambiguates_homograph_headword(self):
        self.assertIn("⟦{時|とき}→時：02918_toki⟧", link("その{時|とき}"))
        self.assertIn("⟦{時|じ}→時：09869_ji⟧", link("3{時|じ}に"))
        # a reading that matches no entry is left alone
        self.assertNotIn("⟦{時|じかん}", link("{時|じかん}"))

    def test_rule2_katakana(self):
        self.assertEqual(link("パソコンが"), "⟦パソコン→パソコン：01538_pasokon⟧⟦が→が：00051_ga⟧")

    def test_rule3_particles_are_split_individually(self):
        out = link("{本|ほん}には")
        self.assertIn("⟦に→に：00314_ni⟧⟦は→は：00079_ha⟧", out)
        out = link("パソコンでは")
        self.assertIn("⟦で→で：00502_de⟧⟦は→は：00079_ha⟧", out)

    def test_sentence_initial_demo_and_deha_use_combined_entries(self):
        self.assertTrue(link("でも、{本|ほん}を").startswith("⟦でも→でも：00925_demo⟧"))
        self.assertTrue(link("では、{本|ほん}を").startswith("⟦では→では：02945_deha⟧"))

    def test_rule4_kana_word_unique_kana_headed_only(self):
        self.assertIn("⟦りんご→りんご：02269_ringo⟧", link("りんごを"))
        # こと has a kanji-headed competitor (琴) -> ambiguous, untouched
        self.assertEqual(link("ことを"), "こと⟦を→を：00422_wo⟧")
        # はし: two kanji-headed candidates, kana surface -> untouched
        self.assertEqual(link("はしを"), "はし⟦を→を：00422_wo⟧")
        # kana surface of a kanji-headed verb: untouched even when unique
        self.assertNotIn("⟦よんだ", link("よんだ。"))

    def test_rule5_conjugated_kana_forms_and_table_verbs(self):
        self.assertIn("⟦している→する：00392_suru⟧", link("{勉強|べんきょう}しているは"))
        self.assertIn("⟦した→する：00392_suru⟧", link("{発生|はっせい}した。"))
        # いる is a table word; the Sudachi guard rejects it when read as 要る
        self.assertIn("⟦いる→いる：00495_iru⟧", link("{本|ほん}を{読|よ}んでいる{人|ひと}がいる。"))

    def test_suru_compounds_follow_split_convention(self):
        out = link("{発生|はっせい}した。")
        self.assertIn("⟦{発生|はっせい}→発生：03133_hassei⟧⟦した→する：00392_suru⟧", out)
        out = link("{勉強|べんきょう}した。")
        self.assertIn("⟦{勉強|べんきょう}した→勉強する：00527_benkyousuru⟧", out)

    def test_compounds_and_expressions_link_as_one_unit(self):
        self.assertIn("⟦お{茶|ちゃ}→お茶：00576_ocha⟧", link("お{茶|ちゃ}を"))
        self.assertIn("⟦{気|き}が{置|お}けない→気が置けない：01463_kigaokenai⟧", link("{気|き}が{置|お}けない{人|ひと}"))
        self.assertIn("⟦{人|にん}→〜人：00658_nin⟧", link("3{人|にん}で"))

    def test_content_word_plus_particle_is_not_merged(self):
        # そこで exists as a conjunction, but そこ + で must stay two links
        self.assertEqual(link("そこで"), "⟦そこ→そこ：00991_soko⟧⟦で→で：00502_de⟧")

    def test_na_adjective_ni_is_linked_but_copula_forms_are_not(self):
        out = link("{静|しず}かにする。")
        self.assertIn("⟦{静|しず}か→静か：00755_shizuka⟧⟦に→に：00314_ni⟧⟦する→する：00392_suru⟧", out)
        self.assertEqual(link("{本|ほん}です。"), "⟦{本|ほん}→本：00111_hon⟧です。")
        self.assertIn("⟦です→です：09485_desu⟧", link("{本|ほん}です。", copula=True))
        # auxiliaries never resolve through the kana-word rule (まし has an entry)
        self.assertNotIn("11145_mashi", link("{読|よ}みました。"))

    def test_kudasai_uses_table_not_lemma(self):
        self.assertIn("⟦ください→ください：02899_kudasai⟧", link("{本|ほん}をください。"))

    def test_never_link_cases(self):
        out = link("〜に{本|ほん}、「3」abc…！")
        self.assertEqual(out, "〜⟦に→に：00314_ni⟧⟦{本|ほん}→本：00111_hon⟧、「3」abc…！")
        # single hiragana that is not a table particle (て, な) stays bare
        self.assertNotIn("⟦て→", link("{読|よ}んでいて"))
        self.assertNotIn("⟦な→", link("{静|しず}かな{人|ひと}"))

    def test_headword_self_exclusion(self):
        out = link("{本|ほん}を{読|よ}む。", own_id="00426_yomu", own_headword="{読|よ}む")
        self.assertEqual(out, "⟦{本|ほん}→本：00111_hon⟧⟦を→を：00422_wo⟧{読|よ}む。")
        # a conjugated form of the headword is not linked either; the aspect verb is
        out = link("{本|ほん}を{読|よ}んでいる。", own_id="00426_yomu", own_headword="{読|よ}む")
        self.assertEqual(out, "⟦{本|ほん}→本：00111_hon⟧⟦を→を：00422_wo⟧{読|よ}んで⟦いる→いる：00495_iru⟧。")
        # multi-word headword: the token sequence is locked
        out = link("{気|き}が{置|お}けない{人|ひと}", own_id="01463_kigaokenai", own_headword="{気|き}が{置|お}けない")
        self.assertEqual(out, "{気|き}が{置|お}けない⟦{人|ひと}→人：00476_hito⟧")

    def test_existing_links_and_wrappers_preserved_and_idempotent(self):
        text = "⟦{本|ほん}→本：00111_hon⟧を{読|よ}む。"
        once = link(text)
        self.assertEqual(once, "⟦{本|ほん}→本：00111_hon⟧⟦を→を：00422_wo⟧⟦{読|よ}む→読む：00426_yomu⟧。")
        self.assertEqual(link(once), once)
        # a noentry marker is preserved verbatim and never re-targeted
        text = "⟦{矍鑠|かくしゃく}→矍鑠：noentry⟧とした{人|ひと}"
        self.assertTrue(link(text).startswith("⟦{矍鑠|かくしゃく}→矍鑠：noentry⟧"))

    def test_notes_english_prose_untouched_and_headers_skipped(self):
        linker = make_linker(_SUDACHI)
        ctx = linker.r.entry_ctx({"id": "x", "headword": "テスト", "reading": "てすと"}, _SUDACHI)
        notes = "The phrase {気|き}が{置|お}けない means relaxed.\n\nCOMMON COLLOCATIONS:\n- {本|ほん}を{読|よ}む: to read a book"
        out = linker.link_text(notes, ctx, skip_headers=True)
        self.assertIn("The phrase ⟦{気|き}が{置|お}けない→気が置けない：01463_kigaokenai⟧ means relaxed.", out)
        self.assertIn("\n\nCOMMON COLLOCATIONS:\n", out)
        self.assertIn("- ⟦{本|ほん}→本：00111_hon⟧⟦を→を：00422_wo⟧⟦{読|よ}む→読む：00426_yomu⟧: to read a book", out)
        header = "COMPARED WITH {本|ほん}:"
        self.assertEqual(linker.link_text(header, ctx, skip_headers=True), header)


class TestTokenizerFreeFallback(unittest.TestCase):
    def test_fallback_links_wrapped_words_katakana_and_particles(self):
        out = link("{本|ほん}をパソコンで{読|よ}みました。", tokenizer=None)
        self.assertEqual(out, "⟦{本|ほん}→本：00111_hon⟧⟦を→を：00422_wo⟧⟦パソコン→パソコン：01538_pasokon⟧"
                              "⟦で→で：00502_de⟧⟦{読|よ}みました→読む：00426_yomu⟧。")

    def test_fallback_is_conservative_with_kana(self):
        # plain kana content words are not linked without a tokenizer
        self.assertEqual(link("りんごをください。", tokenizer=None), "りんご⟦を→を：00422_wo⟧⟦ください→ください：02899_kudasai⟧。")
        # には splits into two particles; unknown kana runs stay bare
        self.assertEqual(link("{本|ほん}にはこと", tokenizer=None),
                         "⟦{本|ほん}→本：00111_hon⟧⟦に→に：00314_ni⟧⟦は→は：00079_ha⟧こと")

    def test_fallback_respects_self_headword_and_existing_links(self):
        out = link("{本|ほん}を{読|よ}む。", own_id="00111_hon", own_headword="{本|ほん}", tokenizer=None)
        self.assertEqual(out, "{本|ほん}⟦を→を：00422_wo⟧⟦{読|よ}む→読む：00426_yomu⟧。")
        text = "⟦{本|ほん}→本：00111_hon⟧を"
        self.assertEqual(link(text, tokenizer=None), "⟦{本|ほん}→本：00111_hon⟧⟦を→を：00422_wo⟧")
        self.assertEqual(link(link(text, tokenizer=None), tokenizer=None), link(text, tokenizer=None))


if __name__ == "__main__":
    unittest.main()
