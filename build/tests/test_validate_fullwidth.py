"""validate.find_fullwidth_alnum_errors: digits and Latin letters are written half-width."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validate import find_fullwidth_alnum_errors  # noqa: E402


class FullwidthTest(unittest.TestCase):
    def test_halfwidth_is_clean(self):
        entry = {"id": "x", "headword": "{自己|じこ}PR",
                 "examples": [{"japanese": "{確定申告|かくていしんこく}は3{月|がつ}だ。8GBのメモリ。"}],
                 "metadata": {"created": "２０２６"}}
        self.assertEqual(find_fullwidth_alnum_errors(entry), [])

    def test_fullwidth_digit_and_letters(self):
        entry = {"id": "x", "headword": "{自己|じこ}ＰＲ",
                 "examples": [{"japanese": "{締|し}め{切|き}りは３{月|がつ}です。"}]}
        errors = find_fullwidth_alnum_errors(entry)
        self.assertEqual(len(errors), 2)
        self.assertIn("PR", errors[0])
        self.assertIn("3", errors[1])

    def test_other_fullwidth_punctuation_is_left_alone(self):
        self.assertEqual(find_fullwidth_alnum_errors({"id": "x", "notes": "（{例|れい}）！？"}), [])


if __name__ == "__main__":
    unittest.main()
