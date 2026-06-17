"""Unit tests for the systemic-fix detectors' trickiest logic.

Focuses on check_furigana_format.classify_wrapper(), which classifies a single
`{surface|reading}` wrapper. The katakana-skip rule (avoiding false positives on
筋トレ / ヶ月) is the subtle part. Run with:
    python3 -m unittest build.tests.test_detectors
"""
import importlib.util
import unittest
from pathlib import Path

_MOD = Path(__file__).resolve().parents[2] / "build" / "check_furigana_format.py"
_spec = importlib.util.spec_from_file_location("check_furigana_format", _MOD)
cf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cf)

_TD = Path(__file__).resolve().parents[2] / "build" / "check_tag_drift.py"
_td_spec = importlib.util.spec_from_file_location("check_tag_drift", _TD)
td = importlib.util.module_from_spec(_td_spec)
_td_spec.loader.exec_module(td)


def sub(left, right):
    res = cf.classify_wrapper(left, right)
    return res[0] if res else None


class TestClassifyWrapper(unittest.TestCase):
    def test_clean_all_kanji_is_ok(self):
        self.assertIsNone(sub("漢字", "かんじ"))
        self.assertIsNone(sub("酒", "さけ"))

    def test_reading_truncated_is_error(self):
        # やり方 read as かた omits やり -> visibly wrong
        self.assertEqual(sub("やり方", "かた"), "reading-truncated")
        self.assertEqual(sub("ねぶた祭", "まつり"), "reading-truncated")

    def test_over_wrapped_okurigana_is_info(self):
        # reading covers the whole surface, just non-canonically wrapped
        self.assertEqual(sub("若い", "わかい"), "over-wrapped")
        self.assertEqual(sub("食べる", "たべる"), "over-wrapped")

    def test_katakana_mix_is_skipped(self):
        # kanji + katakana: reading in hiragana is not a visible bug -> skip
        self.assertIsNone(sub("筋トレ", "きんとれ"))
        self.assertIsNone(sub("ヶ月", "かげつ"))
        self.assertIsNone(sub("輪ゴム", "わごむ"))

    def test_o_go_prefix_inside_wrapper(self):
        self.assertEqual(sub("お酒", "おさけ"), "o-go-prefix")
        self.assertEqual(sub("ご飯", "ごはん"), "o-go-prefix")

    def test_slash_reading(self):
        self.assertEqual(sub("村", "むら/そん"), "slash-reading")

    def test_pure_kana_wrapper(self):
        self.assertEqual(sub("どんどん", "どんどん"), "pure-kana")
        self.assertEqual(sub("ところ", "所"), "pure-kana")  # reversed


class TestBaseHeadword(unittest.TestCase):
    def test_strips_furigana_wrappers(self):
        self.assertEqual(td.base_headword("{一期一会|いちごいちえ}"), "一期一会")
        self.assertEqual(td.base_headword("{猿|さる}も{木|き}から{落|お}ちる"),
                         "猿も木から落ちる")

    def test_plain_text_unchanged(self):
        self.assertEqual(td.base_headword("ねじ"), "ねじ")
        self.assertEqual(td.base_headword(None), "")


class TestLooksIdiomatic(unittest.TestCase):
    def test_yojijukugo_headword(self):
        # bare four-kanji compound is treated as a yojijukugo
        self.assertTrue(td.looks_idiomatic({"headword": "{大器晩成|たいきばんせい}"}, []))

    def test_expression_pos(self):
        self.assertTrue(td.looks_idiomatic({"headword": "{足|あし}が{出|で}る"},
                                           ["expression"]))

    def test_gloss_marker(self):
        self.assertTrue(td.looks_idiomatic(
            {"headword": "X", "gloss": "to shrug; idiom for indifference"}, ["noun"]))

    def test_plain_concrete_noun_is_not_idiomatic(self):
        # 顔 (face): three kanji-or-fewer, plain noun, concrete gloss -> not idiom
        self.assertFalse(td.looks_idiomatic({"headword": "{顔|かお}", "gloss": "face"},
                                            ["noun"]))
        # a four-kanji compound noun is yojijukugo-shaped, but the keyword filter
        # (not this predicate) is what spares 冷凍食品; the predicate is intentionally
        # liberal here.


class TestDistantObjectDomains(unittest.TestCase):
    def test_distant_pair_flagged(self):
        # 油絵 (oil painting) mis-tagged body-part alongside tool
        self.assertTrue(td.distant_object_domains(["body-part", "tool"]))
        # 打席 (at-bat) mis-tagged animal-mammal + electronics
        self.assertTrue(td.distant_object_domains(["animal-mammal", "electronics"]))

    def test_adjacent_pair_not_flagged(self):
        # airport: building + transportation legitimately co-occur
        self.assertEqual(td.distant_object_domains(["building", "transportation"]), [])
        # calculator: electronics + tool
        self.assertEqual(td.distant_object_domains(["electronics", "tool"]), [])
        # seafood: animal-fish + food
        self.assertEqual(td.distant_object_domains(["animal-fish", "food"]), [])

    def test_single_hard_domain_not_flagged(self):
        self.assertEqual(td.distant_object_domains(["furniture"]), [])
        self.assertEqual(td.distant_object_domains(["furniture", "emotion"]), [])

    def test_three_domains_with_one_distant(self):
        # 横断歩道: animal-mammal + clothing + transportation -> at least one distant
        self.assertTrue(
            td.distant_object_domains(["animal-mammal", "clothing", "transportation"]))


if __name__ == "__main__":
    unittest.main()
