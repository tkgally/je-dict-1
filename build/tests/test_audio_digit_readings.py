"""Tests for build/audio_digit_readings.py and the digit-reading hook in audio_pipeline."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import audio_digit_readings as D  # noqa: E402
import audio_pipeline as P  # noqa: E402


class ConsistencyTest(unittest.TestCase):
    def test_fills_only_the_digits_and_letters(self):
        self.assertTrue(D.consistent("きっかり3じにきてください。", "きっかりさんじにきてください"))
        self.assertTrue(D.consistent("NHKのにゅーす", "エヌエイチケーのニュース"))
        self.assertFalse(D.consistent("きっかり3じにきてください。", "きっかりさんじにいってください"))
        self.assertFalse(D.consistent("ATMでおかねをおろした。", "えーてぃーえむでかねをおろした"))

    def test_counter_after_a_digit_is_read_freely(self):
        known = D.known_reading(P.parse_example("3{日|にち}ほどかかります。"))
        self.assertEqual(known, "3日ほどかかります。")
        self.assertTrue(D.consistent(known, "みっかほどかかります"))
        known = D.known_reading(P.parse_example("{図書室|としょしつ}は3{階|かい}にあります。"))
        self.assertTrue(D.consistent(known, "としょしつはさんがいにあります"))
        self.assertFalse(D.consistent(known, "としょしつはさんがいにいきます"))

    def test_norm_folds_katakana_and_drops_punctuation(self):
        self.assertEqual(D.norm("エヌ、エイチ・ケー。"), "えぬえいちけー")


class HookTest(unittest.TestCase):
    def setUp(self):
        self.x = {"ex": "21132_kikkari_ex1", "raw": "きっかり3{時|じ}に{来|き}てください。"}
        self.r = {"h": P.short_hash(self.x["raw"]), "kana": "きっかりさんじにきてください",
                  "alt_kana": [], "state": "confirmed", "added": "2026-10-23T00:00:00Z"}

    def test_confirmed_reading_makes_the_example_recordable(self):
        p = P.spoken_example(self.x, {}, {self.x["ex"]: self.r})
        self.assertTrue(p["manual_reading"])
        self.assertEqual(p["kana"], self.r["kana"])
        self.assertIsNone(P.undetermined_reason(p))

    def test_reading_for_older_text_is_ignored(self):
        r = dict(self.r, h="0000000000000000")
        p = P.spoken_example(self.x, {}, {self.x["ex"]: r})
        self.assertEqual(P.undetermined_reason(p), "digits")

    def test_production_waits_for_method_approval(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "r.json"
            f.write_text(json.dumps({"method_approved": False,
                                     "readings": {self.x["ex"]: self.r}}), encoding="utf-8")
            self.assertEqual(P.load_digit_readings(f), {})
            self.assertIn(self.x["ex"], P.load_digit_readings(f, approved_only=False))
            f.write_text(json.dumps({"method_approved": True,
                                     "readings": {self.x["ex"]: self.r,
                                                  "x_ex1": dict(self.r, state="disputed")}}),
                         encoding="utf-8")
            self.assertEqual(list(P.load_digit_readings(f)), [self.x["ex"]])


if __name__ == "__main__":
    unittest.main()
