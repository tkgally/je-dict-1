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


def _forms(headword, reading, pos="verb-godan", eid=None):
    entry = {"headword": headword, "reading": reading, "part_of_speech": "verb",
             "metadata": {"tags": {"pos": [pos]}}}
    if eid:
        entry["id"] = eid
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



class IrregularFormTests(unittest.TestCase):
    """Special cases found by build/check_conjugations.py on 2026-09-30."""

    def test_u_onbin_verbs_keep_u(self):
        for hw, rd in (("{乞|こ}う", "こう"), ("{問|と}う", "とう"), ("{請|こ}う", "こう")):
            f = _forms(hw, rd)
            stem = hw[:-1]
            self.assertEqual(f["Past"]["affirmative"], f"{stem}うた")
            self.assertEqual(f["て form"]["affirmative"], f"{stem}うて")
            self.assertEqual(f["Conditional たら"]["affirmative"], f"{stem}うたら")
            self.assertEqual(f["Present"]["negative"], f"{stem}わない")

    def test_ordinary_u_verb_unchanged(self):
        f = _forms("{買|か}う", "かう")
        self.assertEqual(f["Past"]["affirmative"], "{買|か}った")
        f = _forms("{追|お}う", "おう")
        self.assertEqual(f["て form"]["affirmative"], "{追|お}って")

    def test_iku_compounds(self):
        for hw, rd in (("ついていく", "ついていく"), ("{持|も}っていく", "もっていく"),
                       ("{出|で}て{行|い}く", "でていく"), ("{逝|い}く", "いく")):
            f = _forms(hw, rd)
            self.assertTrue(f["Past"]["affirmative"].endswith("った"), hw)
            self.assertTrue(f["て form"]["affirmative"].endswith("って"), hw)

    def test_iku_rule_leaves_other_ku_verbs_alone(self):
        self.assertEqual(_forms("{書|か}く", "かく")["Past"]["affirmative"], "{書|か}いた")
        self.assertEqual(_forms("{抱|いだ}く", "いだく")["Past"]["affirmative"], "{抱|いだ}いた")

    def test_kureru_imperative(self):
        f = _forms("くれる", "くれる", pos="verb-ichidan")
        self.assertEqual(f["Imperative"]["affirmative"], "くれ")
        f = _forms("{暮|く}れる", "くれる", pos="verb-ichidan")
        self.assertEqual(f["Imperative"]["affirmative"], "{暮|く}れろ")

    def test_kana_kuru_compound_stays_kana(self):
        f = _forms("{持|も}ってくる", "もってくる", pos="verb-kuru")
        self.assertEqual(f["Past"]["affirmative"], "{持|も}ってきた")
        self.assertEqual(f["Present"]["negative"], "{持|も}ってこない")
        f = _forms("{来|く}る", "くる", pos="verb-kuru")
        self.assertEqual(f["Past"]["affirmative"], "{来|き}た")

    def test_gozaimasu_has_only_masu_forms(self):
        f = _forms("ございます", "ございます")
        self.assertEqual(f["Present polite"]["negative"], "ございません")
        self.assertEqual(f["Past polite"]["affirmative"], "ございました")
        self.assertNotIn("Present", f)

    def test_no_table_ids(self):
        entry = {"id": "01913_osoru", "headword": "{恐|おそ}る", "reading": "おそる",
                 "part_of_speech": "verb", "metadata": {"tags": {"pos": ["verb-godan"]}}}
        self.assertIsNone(generate_conjugation(entry))

    def test_kun_noun_suru_potential(self):
        f = _forms("{噂|うわさ}", "うわさ", pos="verb-suru")
        self.assertEqual(f["Potential"]["affirmative"], "{噂|うわさ}できる")
        f = _forms("{愛|あい}する", "あいする", pos="verb-suru")
        self.assertEqual(f["Potential"]["affirmative"], "{愛|あい}せる")


    def test_zuru_keeps_zuru_in_dictionary_based_forms(self):
        f = _forms("{案|あん}ずる", "あんずる", pos="verb-ichidan")
        self.assertEqual(f["Present"]["affirmative"], "{案|あん}ずる")
        self.assertEqual(f["Present"]["negative"], "{案|あん}じない")
        self.assertEqual(f["Conditional ば"]["affirmative"], "{案|あん}ずれば")
        self.assertEqual(f["Imperative"]["negative"], "{案|あん}ずるな")
        self.assertEqual(f["Past"]["affirmative"], "{案|あん}じた")

    def test_passive_headword_has_no_passive_potential_or_causative(self):
        entry = {"headword": "{流|なが}される", "reading": "ながされる", "part_of_speech": "verb",
                 "notes": "The passive form of 流す.",
                 "metadata": {"tags": {"pos": ["verb-ichidan"]}}}
        labels = {f["label"] for f in generate_conjugation(entry)["forms"]}
        self.assertFalse(labels & {"Passive", "Potential", "Causative"})
        entry = {"headword": "{垂|た}れる", "reading": "たれる", "part_of_speech": "verb",
                 "notes": "It describes a passive, gravity-driven motion.",
                 "metadata": {"tags": {"pos": ["verb-ichidan"]}}}
        labels = {f["label"] for f in generate_conjugation(entry)["forms"]}
        self.assertIn("Causative", labels)

    def test_stative_single_kanji_suru_has_no_potential(self):
        for hw, rd in (("{値|あたい}する", "あたいする"), ("{関|かん}する", "かんする"),
                       ("{面|めん}する", "めんする")):
            self.assertNotIn("Potential", _forms(hw, rd, pos="verb-suru"))
        self.assertEqual(_forms("{察|さっ}する", "さっする", pos="verb-suru")["Potential"]["affirmative"],
                         "{察|さっ}せる")


class AdjectiveTests(unittest.TestCase):
    def test_kawaii_compounds_are_regular(self):
        from add_adjective_conjugations import generate_adjective_conjugation
        entry = {"headword": "あざとかわいい", "reading": "あざとかわいい",
                 "metadata": {"tags": {"pos": ["adjective-i"]}}}
        conj = generate_adjective_conjugation(entry)
        self.assertEqual(conj["type"], "i-adjective")
        past = {f["label"]: f for f in conj["forms"]}["Past"]["affirmative"]
        self.assertEqual(past, "あざとかわいかった")
        entry = {"headword": "かっこいい", "reading": "かっこいい",
                 "metadata": {"tags": {"pos": ["adjective-i"]}}}
        self.assertEqual(generate_adjective_conjugation(entry)["type"], "ii")


if __name__ == "__main__":
    unittest.main()
