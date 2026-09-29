"""Tests for the judgment rules in check_link_newcomers.py (2026-09-29).

A competitor is dropped when the link's kanji surface excludes it, or when
build/data/link_newcomer_judgments.json records a pair judgment for it.
"""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

_MOD = Path(__file__).resolve().parent.parent / "check_link_newcomers.py"
_spec = importlib.util.spec_from_file_location("check_link_newcomers", _MOD)
cln = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cln)

DOU = {"id": "31140_dou", "headword": "胴"}
SHI = {"id": "30975_shi", "headword": "師"}
UKAGAU = {"id": "31093_ukagau", "headword": "窺う"}


class TestJudged(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()) / "j.json"
        self.tmp.write_text(json.dumps({"judgments": [
            {"base": "どう", "target": "00543_dou", "competitor": "31140_dou",
             "surface": "kana", "decision": "keep"},
            {"base": "〜師", "target": "30801_shi", "competitor": "30975_shi",
             "surface": "any", "decision": "keep"},
        ]}), encoding="utf-8")
        self.j = cln.load_judgments(self.tmp)

    def test_kanji_surface_excludes_other_kanji(self):
        self.assertTrue(cln.judged("{伺|うかが}う", "うかがう", "01273_ukagau", UKAGAU, {}))

    def test_kanji_surface_sharing_kanji_not_excluded(self):
        self.assertFalse(cln.judged("{師|し}", "〜師", "30801_shi", SHI, {}))

    def test_kana_surface_not_excluded_without_judgment(self):
        self.assertFalse(cln.judged("どう", "どう", "00543_dou", DOU, {}))

    def test_kana_pair_judgment(self):
        self.assertTrue(cln.judged("どう", "どう", "00543_dou", DOU, self.j))

    def test_kana_scope_does_not_cover_kanji_surface(self):
        self.assertFalse(cln.judged("{胴|どう}", "どう", "00543_dou", DOU, self.j))

    def test_any_scope_with_tilde_base(self):
        self.assertTrue(cln.judged("{師|し}", "〜師", "30801_shi", SHI, self.j))

    def test_other_target_not_covered(self):
        self.assertFalse(cln.judged("どう", "どう", "03962_dou", DOU, self.j))


if __name__ == "__main__":
    unittest.main()
