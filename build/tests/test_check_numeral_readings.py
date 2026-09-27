"""Unit tests for build/check_numeral_readings.py (numeral + counter furigana).

Run with:  python3 -m unittest build.tests.test_check_numeral_readings
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import check_numeral_readings as C  # noqa: E402


def found(text, notes=False):
    return [(f["surface"], f["reading"]) for f in C.findings_in(text, notes=notes)]


class TestNumeralReadings(unittest.TestCase):
    def test_sound_changes_missing(self):
        self.assertEqual(found("ペンを{一|いち}{本|ぽん}ください。"), [("一本", "いちぽん")])
        self.assertEqual(found("{九|きゅう}{時|じ}に{寝|ね}ます。"), [("九時", "きゅうじ")])
        self.assertEqual(found("{十八|じゅうはち}{歳|さい}で"), [("十八歳", "じゅうはちさい")])
        self.assertEqual(found("{二十|にじゅう}{分|ぷん}ぐらい"), [("二十分", "にじゅうぷん")])
        self.assertEqual(found("{四|よん}{人|にん}で"), [("四人", "よんにん")])
        self.assertEqual(found("コーヒーを{二|に}つください。"), [("二つ", "につ")])
        self.assertEqual(found("{十四|じゅうよん}{日|にち}に"), [("十四日", "じゅうよんにち")])

    def test_correct_readings_pass(self):
        for t in ("{一|いっ}{本|ぽん}", "{十六個|じゅうろっこ}", "{二十|にじゅっ}{分|ぷん}",
                  "{一週間|いっしゅうかん}", "{十四日|じゅうよっか}", "{七時|しちじ}", "{七時|ななじ}",
                  "{二十歳|はたち}", "{二十日|はつか}", "{十一人|じゅういちにん}", "{一日|いちにち}"):
            self.assertEqual(found(t), [], t)

    def test_other_words_pass(self):
        for t in ("{十分|じゅうぶん}だ", "{三日月|みかづき}", "{三|みっ}{日|か}{月|づき}",
                  "{公園|こうえん}を{一回|ひとまわ}りした", "{四|よ}つん{這|ば}い",
                  "{三分|さんぶん}の{二|に}", "{段取|だんど}り{八分|はちぶ}", "{三十日|みそか}に",
                  "{五月|さつき}", "{二分|にぶん}の{一|いち}"):
            self.assertEqual(found(t), [], t)

    def test_bound_forms_only_in_notes(self):
        self.assertEqual(found("{三|み}つ (three) + {編|あ}み", notes=True), [])
        self.assertEqual(found("{三|み}つのRを{実践|じっせん}"), [("三つ", "みつ")])

    def test_links_are_read_through(self):
        t = "⟦{九|きゅう}{月|がつ}→九月：00646_kugatsu⟧から"
        self.assertEqual(found(t), [("九月", "きゅうがつ")])


if __name__ == "__main__":
    unittest.main()
