"""ID romaji vs reading, including the する allowance (reading-missing-suru)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from validate import id_romaji_matches  # noqa: E402


class TestIdRomaji(unittest.TestCase):
    def test_exact_match(self):
        self.assertTrue(id_romaji_matches("shoukaisuru", "しょうかいする"))
        self.assertTrue(id_romaji_matches("kumamotojou", "くまもとじょう"))

    def test_suru_verb_id_without_suru(self):
        self.assertTrue(id_romaji_matches("keishi", "けいしする"))
        self.assertTrue(id_romaji_matches("chuumon", "ちゅうもんする"))

    def test_mismatch_still_caught(self):
        self.assertFalse(id_romaji_matches("keishi", "けいじする"))
        self.assertFalse(id_romaji_matches("keishi", "けいしゃ"))
        self.assertFalse(id_romaji_matches("keishisuru", "けいし"))

    def test_allowance_only_for_final_suru(self):
        self.assertFalse(id_romaji_matches("su", "する"))  # empty stem is not an allowance case


if __name__ == "__main__":
    unittest.main()
