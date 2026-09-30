"""Unit tests for build/check_conjugations.py (the deterministic checks).

Run with:  python3 -m unittest build.tests.test_check_conjugations
"""
import sys
import unittest
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT / "build") not in sys.path:
    sys.path.insert(0, str(_ROOT / "build"))

import check_conjugations as C  # noqa: E402
from add_conjugations import generate_conjugation  # noqa: E402


def entry(headword, reading, pos, examples=(), notes="", eid="99999_test"):
    e = {"id": eid, "headword": headword, "reading": reading, "part_of_speech": "verb",
         "metadata": {"tags": {"pos": [pos]}}, "notes": notes,
         "examples": [{"japanese": j} for j in examples]}
    e["conjugation"] = generate_conjugation(e)
    return e


class ExampleCheckTests(unittest.TestCase):
    def test_flags_form_the_table_lacks(self):
        # a godan verb mis-tagged ichidan: the examples say ふけった
        e = entry("ふける", "ふける", "verb-ichidan", ["{空想|くうそう}にふけっていた。"])
        flags = C.check_examples(e, e["conjugation"])
        self.assertEqual(len(flags), 1)
        self.assertIn("ふけって", flags[0][1])

    def test_quiet_when_examples_agree(self):
        e = entry("{乞|こ}う", "こう", "verb-godan", ["{命|いのち}を{乞|こ}うた。"])
        self.assertEqual(C.check_examples(e, e["conjugation"]), [])

    def test_skips_desiderative_compounds_and_not_notes(self):
        e = entry("{会|あ}う", "あう", "verb-godan", ["{友達|ともだち}に{会|あ}いたい。"],
                  notes="{会|あ}った (not {会|あ}いた)")
        self.assertEqual(C.check_examples(e, e["conjugation"]), [])
        e = entry("{勝|か}つ", "かつ", "verb-godan", ["{優勝|ゆうしょう}した。"])
        self.assertEqual(C.check_examples(e, e["conjugation"]), [])

    def test_links_are_read_as_their_surface(self):
        self.assertEqual(C.plain("⟦{乞|こ}うた→乞う：28921_kou⟧。"), "乞うた。")


class ClassAgreementTests(unittest.TestCase):
    def test_godan_rows(self):
        self.assertTrue(C.class_agrees("五段-ワア行", "動詞", "godan", "う"))
        self.assertTrue(C.class_agrees("文語四段-マ行", "動詞", "godan", "む"))
        self.assertFalse(C.class_agrees("五段-ラ行", "動詞", "ichidan", "る"))
        self.assertFalse(C.class_agrees("下一段-ラ行", "動詞", "godan", "る"))
        self.assertTrue(C.class_agrees("上一段-ザ行", "動詞", "zuru", "る"))


class GeneratorCheckTests(unittest.TestCase):
    def test_stale_table_flagged_once(self):
        e = entry("{乞|こ}う", "こう", "verb-godan")
        for f in e["conjugation"]["forms"]:
            f["affirmative"] = f["affirmative"].replace("うた", "った").replace("うて", "って")
        flags = C.check_generator(e, e["conjugation"])
        self.assertEqual(len(flags), 1)
        self.assertIn("乞うた", flags[0][1])

    def test_current_table_clean(self):
        e = entry("{読|よ}む", "よむ", "verb-godan")
        self.assertEqual(C.check_generator(e, e["conjugation"]), [])

    def test_table_hash_changes_with_table(self):
        e = entry("{読|よ}む", "よむ", "verb-godan")
        h = C.table_hash(e["conjugation"])
        e["conjugation"]["forms"][0]["negative"] = "x"
        self.assertNotEqual(h, C.table_hash(e["conjugation"]))


if __name__ == "__main__":
    unittest.main()
