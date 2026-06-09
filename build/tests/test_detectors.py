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


if __name__ == "__main__":
    unittest.main()
