"""validate.find_latin_furigana_errors: a furigana reading must not contain Latin letters."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from validate import find_latin_furigana_errors  # noqa: E402


class LatinFuriganaTest(unittest.TestCase):
    def test_clean_entry(self):
        entry = {"id": "x", "headword": "{漢字|かんじ}", "notes": "{漢字|かんじ} and OK (English)",
                 "examples": [{"japanese": "{日本|にほん}のCD"}]}
        self.assertEqual(find_latin_furigana_errors(entry), [])

    def test_latin_in_reading(self):
        entry = {"id": "x", "examples": [{"japanese": "{漢字|kanji}を{書|か}く"}]}
        errors = find_latin_furigana_errors(entry)
        self.assertEqual(len(errors), 1)
        self.assertIn("{漢字|kanji}", errors[0])

    def test_fullwidth_latin(self):
        self.assertTrue(find_latin_furigana_errors({"id": "x", "notes": "{字|ｊｉ}"}))


if __name__ == "__main__":
    unittest.main()
