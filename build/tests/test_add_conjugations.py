"""Unit tests for build/add_conjugations.py.

Run with:  python3 -m unittest build.tests.test_add_conjugations
"""
import sys
import unittest
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT / "build") not in sys.path:
    sys.path.insert(0, str(_ROOT / "build"))

from add_conjugations import generate_conjugation  # noqa: E402


def _forms(headword, reading):
    entry = {"headword": headword, "reading": reading, "part_of_speech": "verb",
             "metadata": {"tags": {"pos": ["verb-godan"]}}}
    return {f["label"]: f for f in generate_conjugation(entry)["forms"]}


class HonorificAruTests(unittest.TestCase):
    def test_kudasaru_takes_i_before_masu_and_in_imperative(self):
        f = _forms("くださる", "くださる")
        self.assertEqual(f["Present polite"]["affirmative"], "くださいます")
        self.assertEqual(f["Past polite"]["negative"], "くださいませんでした")
        self.assertEqual(f["Volitional polite"]["affirmative"], "くださいましょう")
        self.assertEqual(f["Imperative"]["affirmative"], "ください")
        self.assertEqual(f["Past"]["affirmative"], "くださった")

    def test_irassharu_and_nasaru(self):
        self.assertEqual(_forms("いらっしゃる", "いらっしゃる")["Present polite"]["affirmative"], "いらっしゃいます")
        self.assertEqual(_forms("なさる", "なさる")["Imperative"]["affirmative"], "なさい")

    def test_ordinary_ru_godan_unchanged(self):
        f = _forms("{帰|かえ}る", "かえる")
        self.assertEqual(f["Present polite"]["affirmative"], "{帰|かえ}ります")
        self.assertEqual(f["Imperative"]["affirmative"], "{帰|かえ}れ")


if __name__ == "__main__":
    unittest.main()
