"""Unit tests for build/fix_furigana_format.py — the safe furigana-wrapper
fixes (kana-only, over-wrapped okurigana, fused お/ご prefix) and what is
deliberately left alone. Run with:
    python3 -m unittest build.tests.test_fix_furigana_format
"""
import importlib.util
import sys
import unittest
from pathlib import Path

_BUILD = Path(__file__).resolve().parents[2] / "build"
if str(_BUILD) not in sys.path:
    sys.path.insert(0, str(_BUILD))
_spec = importlib.util.spec_from_file_location("fix_furigana_format", _BUILD / "fix_furigana_format.py")
ff = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ff)


def fix(surface, reading=None):
    return ff.fix_wrapper(surface, reading)


class TestKanaOnly(unittest.TestCase):
    def test_no_pipe(self):
        self.assertEqual(fix("ている"), ("ている", ["kana-only"], None))
        self.assertEqual(fix("コンビニ"), ("コンビニ", ["kana-only"], None))

    def test_pipe_same_or_hiragana_reading_or_empty(self):
        self.assertEqual(fix("どんどん", "どんどん")[0], "どんどん")
        self.assertEqual(fix("コンビニ", "こんびに")[0], "コンビニ")
        self.assertEqual(fix("ラーメン", "らーめん")[0], "ラーメン")
        self.assertEqual(fix("どこ", "")[0], "どこ")

    def test_reading_mismatch_left_alone(self):
        text, kinds, hold = fix("ところ", "所")
        self.assertEqual((text, kinds, hold), ("{ところ|所}", [], "kana-only-reading-mismatch"))
        self.assertEqual(fix("カキ", "がき")[2], "kana-only-reading-mismatch")


class TestOverWrapped(unittest.TestCase):
    def test_trailing_okurigana_moves_out(self):
        self.assertEqual(fix("痛み", "いたみ")[0], "{痛|いた}み")
        self.assertEqual(fix("食べる", "たべる")[0], "{食|た}べる")
        self.assertEqual(fix("美しい", "うつくしい")[0], "{美|うつく}しい")
        self.assertEqual(fix("三つ", "みっつ")[0], "{三|みっ}つ")
        self.assertEqual(fix("申し訳ありません", "もうしわけありません")[0], "{申し訳|もうしわけ}ありません")

    def test_internal_kana_only_trailing_part_moves(self):
        self.assertEqual(fix("引き出し", "ひきだし")[0], "{引き出|ひきだ}し")

    def test_no_change_cases(self):
        self.assertEqual(fix("漢字", "かんじ"), ("{漢字|かんじ}", [], None))
        self.assertEqual(fix("人々", "ひとびと"), ("{人々|ひとびと}", [], None))   # 々 is not hiragana
        self.assertEqual(fix("筋トレ", "きんとれ"), ("{筋トレ|きんとれ}", [], None))  # katakana tail
        # reading does not end with the surface kana -> truncated reading, not ours to fix
        self.assertEqual(fix("やり方", "かた"), ("{やり方|かた}", [], None))

    def test_never_empties_reading(self):
        self.assertEqual(fix("子", "こ"), ("{子|こ}", [], None))
        # surface kana equal to the whole reading would leave nothing for the kanji
        self.assertEqual(fix("子こ", "こ"), ("{子こ|こ}", [], None))


class TestPrefix(unittest.TestCase):
    def test_o_go_prefix(self):
        self.assertEqual(fix("お茶", "おちゃ")[0], "お{茶|ちゃ}")
        self.assertEqual(fix("ご飯", "ごはん")[0], "ご{飯|はん}")
        self.assertEqual(fix("お客様", "おきゃくさま")[0], "お{客様|きゃくさま}")

    def test_prefix_then_okurigana(self):
        text, kinds, _ = fix("お祝い", "おいわい")
        self.assertEqual(text, "お{祝|いわ}い")
        self.assertEqual(kinds, ["o-go-prefix", "over-wrapped"])

    def test_prefix_not_applied_when_kana_follows_or_reading_differs(self):
        self.assertEqual(fix("ごみ箱", "ごみばこ"), ("{ごみ箱|ごみばこ}", [], None))
        self.assertEqual(fix("おかげ様", "おかげさま"), ("{おかげ様|おかげさま}", [], None))
        self.assertEqual(fix("御飯", "ごはん"), ("{御飯|ごはん}", [], None))
        self.assertEqual(fix("お", "お")[0], "お")   # kana-only rule wins


class TestSymbolsAndNoPipe(unittest.TestCase):
    def test_symbol_surfaces_left_alone(self):
        self.assertEqual(fix("3", "さん"), ("{3|さん}", [], "symbol-surface"))
        self.assertEqual(fix("〜", "〜"), ("{〜|〜}", [], "symbol-surface"))

    def test_no_pipe_with_kanji_left_alone(self):
        self.assertEqual(fix("稀"), ("{稀}", [], "no-pipe-with-kanji"))
        self.assertEqual(fix("verb stem"), ("{verb stem}", [], "no-pipe-symbol"))


class TestFixText(unittest.TestCase):
    def test_link_base_forms_protected(self):
        text = "⟦{食べる|たべる}→{食べる|たべる}：00001_taberu⟧と{お茶|おちゃ}"
        new, fixes, holds = ff.fix_text(text)
        self.assertEqual(new, "⟦{食|た}べる→{食べる|たべる}：00001_taberu⟧とお{茶|ちゃ}")
        self.assertEqual(fixes, {"over-wrapped": 1, "o-go-prefix": 1})

    def test_unbalanced_skipped(self):
        text = "{チームに{残|のこ}る{どんどん|どんどん}"
        new, fixes, holds = ff.fix_text(text)
        self.assertEqual(new, text)
        self.assertEqual(holds, {"skipped-unbalanced": 1})
        self.assertEqual(ff.fix_text("{残|のこ}る}")[2], {"skipped-unbalanced": 1})


class TestNestedOuter(unittest.TestCase):
    def test_outer_without_reading_is_dropped(self):
        self.assertEqual(ff.fix_text("{お{正月|しょうがつ}}")[0], "お{正月|しょうがつ}")
        self.assertEqual(ff.fix_text("{{誇|ほこ}}り")[0], "{誇|ほこ}り")
        self.assertEqual(ff.fix_text("{スチーム{式|しき}}")[0], "スチーム{式|しき}")
        self.assertEqual(ff.fix_text("{新{入荷|にゅうか}}")[0], "新{入荷|にゅうか}")   # no info lost
        new, fixes, holds = ff.fix_text("{お{茶|ちゃ}を{点|た}てる}")
        self.assertEqual(new, "お{茶|ちゃ}を{点|た}てる")
        self.assertEqual(fixes, {"nested-outer": 1})

    def test_kana_only_inner_fixed_in_same_pass(self):
        new, fixes, _ = ff.fix_text("called {あご{ひも}} sometimes")
        self.assertEqual(new, "called あごひも sometimes")
        self.assertEqual(fixes, {"nested-outer": 1, "kana-only": 1})

    def test_outer_reading_dropped_only_when_redundant(self):
        self.assertEqual(ff.fix_text("{ガス{代|だい}|がすだい}")[0], "ガス{代|だい}")
        self.assertEqual(ff.fix_text("{お{守|まも}り|おまもり}")[0], "お{守|まも}り")
        self.assertEqual(ff.fix_text("{アミノ{酸|さん}|}")[0], "アミノ{酸|さん}")
        text = "{教{室|しつ}|きょうしつ}"
        new, fixes, holds = ff.fix_text(text)
        self.assertEqual(new, text)
        self.assertEqual(holds, {"nested-outer-reading-needed": 1})

    def test_deeper_nesting_and_limits(self):
        self.assertEqual(ff.fix_text("{a{b{漢|かん}}}")[0], "ab{漢|かん}")
        long = "{" + "x" * 130 + "{漢|かん}}"
        new, fixes, holds = ff.fix_text(long)
        self.assertEqual(new, long)
        self.assertEqual(holds, {"nested-outer-too-long": 1})
        multi = "{line one\n{漢|かん}}"
        self.assertEqual(ff.fix_text(multi)[0], multi)

    def test_outer_braces_inside_link_base_form_untouched(self):
        text = "⟦x→{お{茶|ちゃ}}：00001_ocha⟧"
        self.assertEqual(ff.fix_text(text)[0], text)
        text = "{⟦{人質|ひとじち}→人質：09678_hitojichi⟧は{解放|かいほう}された}"
        self.assertEqual(ff.fix_text(text)[0], "⟦{人質|ひとじち}→人質：09678_hitojichi⟧は{解放|かいほう}された")

    def test_plain_text_untouched(self):
        self.assertEqual(ff.fix_text("no braces here")[0], "no braces here")


class TestFixEntry(unittest.TestCase):
    def test_fields_and_skips(self):
        entry = {
            "id": "00001_ocha", "headword": "{お茶|おちゃ}", "reading": "おちゃ",
            "gloss": "tea", "part_of_speech": "noun",
            "definitions": [{"sense_number": 1, "gloss": "tea", "explanation": "Often {ゆっくり} drunk."}],
            "examples": [{"id": "00001_ocha_ex1", "japanese": "{お茶|おちゃ}を{飲みます|のみます}。",
                          "english": "I drink tea.", "sense_numbers": [1]}],
            "notes": "See {お茶|おちゃ}.",
            "cross_references": [{"type": "related", "reading": "こうちゃ", "headword": "{紅茶|こうちゃ}",
                                  "target_id": "00002_koucha"}],
            "conjugation": {"type": "godan", "forms": [{"label": "Present", "affirmative": "{飲む|のむ}",
                                                        "negative": "{飲まない|のまない}"}]},
            "metadata": {"tags": {"pos": ["noun"]}, "modified": "2026-01-01T00:00:01Z"},
        }
        fixes, holds, changed = ff.fix_entry(entry)
        self.assertEqual(entry["headword"], "お{茶|ちゃ}")
        self.assertEqual(entry["reading"], "おちゃ")
        self.assertEqual(entry["examples"][0]["japanese"], "お{茶|ちゃ}を{飲|の}みます。")
        self.assertEqual(entry["examples"][0]["id"], "00001_ocha_ex1")
        self.assertEqual(entry["definitions"][0]["explanation"], "Often ゆっくり drunk.")
        self.assertEqual(entry["notes"], "See お{茶|ちゃ}.")
        self.assertEqual(entry["cross_references"][0]["headword"], "{紅茶|こうちゃ}")
        self.assertEqual(entry["conjugation"]["forms"][0]["affirmative"], "{飲|の}む")
        self.assertEqual(entry["conjugation"]["forms"][0]["negative"], "{飲|の}まない")
        self.assertEqual(entry["metadata"]["modified"], "2026-01-01T00:00:01Z")
        self.assertEqual(fixes["o-go-prefix"], 3)
        self.assertEqual(fixes["kana-only"], 1)
        self.assertEqual(fixes["over-wrapped"], 3)
        self.assertIn("headword", changed)
        self.assertIn("notes", changed)


if __name__ == "__main__":
    unittest.main()
