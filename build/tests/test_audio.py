"""Unit tests for the example-audio workflow (build/audio_text.py, audio_checks.py,
audio_pipeline.py). No network. Tests that need MeCab (fugashi + unidic-lite,
build/requirements-audio.txt) are skipped when it is not installed.

Run with:  python3 -m unittest build.tests.test_audio
"""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import audio_checks as C  # noqa: E402
import audio_pipeline as P  # noqa: E402
import audio_text as T  # noqa: E402

HAS_MECAB = T.mecab_available()
needs_mecab = unittest.skipUnless(HAS_MECAB, "fugashi/unidic-lite not installed")

MAJORITY = {"私": "わたし", "上手": "じょうず", "明日": "あした", "今日": "きょう"}


class TestMarkup(unittest.TestCase):
    def test_strip_links_keeps_display_and_furigana(self):
        raw = "⟦お{金|かね}→お金：00611_okane⟧⟦が→が：00051_ga⟧{余|あま}った。"
        self.assertEqual(T.strip_links(raw), "お{金|かね}が{余|あま}った。")

    def test_parse_example(self):
        p = T.parse_example("⟦{食|た}べ{物|もの}→食べ物：02890_tabemono⟧が{余|あま}っている。")
        self.assertEqual(p["plain"], "食べ物が余っている。")
        self.assertEqual(p["kana"], "たべものがあまっている。")
        self.assertEqual(p["tokens"][:3], [["食", "た"], ["べ", None], ["物", "もの"]])
        self.assertIsNone(T.undetermined_reason(p))

    def test_undetermined_reasons(self):
        self.assertEqual(T.undetermined_reason(T.parse_example("{駅|えき}まで3{分|ぷん}です。")), "digits")
        self.assertEqual(T.undetermined_reason(T.parse_example("NHKを{見|み}る。")), "latin")
        self.assertEqual(T.undetermined_reason(T.parse_example("{駅|えき}まで歩く。")), "bare-kanji")
        self.assertEqual(T.undetermined_reason(T.parse_example("{駅|えき}|まで。")), "malformed")
        # malformed is reported before the other problems
        self.assertEqual(T.undetermined_reason(T.parse_example("3{駅|えき}|歩")), "malformed")

    def test_text_hash_ignores_links_not_furigana(self):
        linked = "⟦お{金|かね}→お金：00611_okane⟧が{余|あま}った。"
        plain = "お{金|かね}が{余|あま}った。"
        self.assertEqual(T.text_hash(linked), T.text_hash(plain))
        self.assertNotEqual(T.text_hash(plain), T.text_hash("お{金|きん}が{余|あま}った。"))
        self.assertNotEqual(T.text_hash(plain), T.text_hash("お{金|かね}が{余|あま}る。"))


class TestNormalization(unittest.TestCase):
    def test_norm_kana(self):
        self.assertEqual(T.norm_kana("コーヒー"), "こおひい")
        self.assertEqual(T.norm_kana("はなぢ、つづく！"), "はなじ" + "つずく")
        self.assertEqual(T.norm_kana("ｶﾀｶﾅ"), "かたかな")

    def test_loose_folds_particles_and_long_vowels(self):
        self.assertEqual(T.loose("わたしはがっこうへいく"), T.loose("わたしわがっこおえいく"))
        self.assertEqual(T.loose("せんせい"), T.loose("せんせえ"))
        self.assertNotEqual(T.loose("こんにち"), T.loose("きょう"))

    def test_numbers_and_letters(self):
        self.assertEqual(T.num2kanji(2026), "二千二十六")
        self.assertEqual(T.num2kanji(10), "十")
        self.assertEqual(T.num2kanji(15000), "一万五千")
        self.assertEqual(T.norm_numbers("1,500円と20%"), "千五百円と二十パーセント")
        self.assertEqual(T.latin_to_kana("NHK"), "エヌエイチケー")
        self.assertEqual(T.latin_to_kana("Wi-Fi"), "ワイファイ")

    def test_distance(self):
        self.assertEqual(T.distance("きょう", "きょう"), 0)
        self.assertEqual(T.distance("こんにち", "きょう"), 4)
        self.assertEqual(T.distance("", "あい"), 2)


@needs_mecab
class TestReadings(unittest.TestCase):
    def test_phonetic_particles(self):
        s = T.parse_example("{私|わたし}は{学校|がっこう}へ{行|い}きます。")
        self.assertEqual(T.phonetic_kana(s), "わたしわがっこうえいきます。")
        s = T.parse_example("{本|ほん}を{読|よ}む。")
        self.assertEqual(T.phonetic_kana(s), "ほんおよむ。")
        s = T.parse_example("これは{本|ほん}ではありません。")
        self.assertEqual(T.phonetic_kana(s), "これわほんでわありません。")

    def test_phonetic_leaves_non_particles(self):
        # the は of はし (a noun) is not a particle
        s = T.parse_example("はしを{使|つか}う。")
        self.assertEqual(T.phonetic_kana(s), "はしおつかう。")

    def test_phonetic_manual_reading(self):
        s = {"tokens": [["きっかり3", None], ["時", "じ"], ["には", None], ["来", "き"], ["てください。", None]],
             "kana": "きっかりさんじにはきてください。", "manual_reading": True}
        self.assertEqual(T.phonetic_kana(s), "きっかりさんじにわきてください。")

    def test_kana_substitution_mecab_rule(self):
        s = T.parse_example("{会社|かいしゃ}が{今日|こんにち}まで{続|つづ}いたのは{社員|しゃいん}のおかげだ。")
        self.assertEqual(T.kana_substituted(s), "会社がこんにちまで続いたのは社員のおかげだ。")
        s = T.parse_example("{彼|かれ}のほうが{一枚|いちまい}{上手|うわて}だ。")
        self.assertEqual(T.kana_substituted(s), "彼のほうが一枚うわてだ。")

    def test_kana_substitution_dictionary_rule(self):
        s = T.parse_example("{私|わたくし}の{意見|いけん}を{述|の}べます。")
        self.assertEqual(T.kana_substituted(s, MAJORITY), "わたくしの意見を述べます。")
        s = T.parse_example("{明日|あす}の{朝|あさ}は{早|はや}い。")
        self.assertEqual(T.kana_substituted(s, None), "明日の朝は早い。")
        self.assertEqual(T.kana_substituted(s, MAJORITY), "あすの朝は早い。")

    def test_okurigana_stay_with_word(self):
        s = T.parse_example("{彼|かれ}は{上手|うわて}に{出|で}た。")
        out = T.kana_substituted(s, MAJORITY)
        self.assertIn("うわて", out)
        self.assertTrue(out.endswith("出た。"))

    def test_prompt_e(self):
        s = T.parse_example("{明日|あす}の{朝|あさ}は{早|はや}い。")
        prompt = T.build_tts_prompt(s, MAJORITY)
        self.assertIn("READING: あすのあさははやい。", prompt)
        self.assertTrue(prompt.endswith("## TRANSCRIPT\nあすの朝は早い。"))
        self.assertIn("# AUDIO PROFILE: Narrator", prompt)

    def test_reading_index(self):
        idx = T.build_reading_index(["{私|わたし}は", "{私|わたし}も", "{私|わたくし}の", "{本|ほん}"])
        self.assertEqual(T.majority_readings(idx), {"私": "わたし"})


class TestScoring(unittest.TestCase):
    S = {"kana": "かいしゃがこんにちまでつづいたのはしゃいんのおかげだ。", "alt_kana": [],
         "tokens": [["会社", "かいしゃ"], ["が", None], ["今日", "こんにち"], ["まで", None],
                    ["続", "つづ"], ["いたのは", None], ["社員", "しゃいん"], ["のおかげだ。", None]]}

    def test_compare_match_in_code_fence(self):
        self.assertEqual(C.score_compare('```json\n{"differences": [], "match": true}\n```')["verdict"],
                         "match")

    def test_compare_spelling_only_difference_is_folded(self):
        text = '{"differences": [{"expected": "こーひー", "heard": "コーヒー"}], "match": false}'
        self.assertEqual(C.score_compare(text)["verdict"], "match")

    def test_compare_particle_as_written_is_kept(self):
        text = '{"differences": [{"expected": "にわ", "heard": "には"}], "match": false}'
        self.assertEqual(C.score_compare(text, particles=True)["verdict"], "mismatch")
        self.assertEqual(C.score_compare(text, particles=False)["verdict"], "match")

    def test_compare_reading_difference(self):
        text = '{"differences": [{"expected": "こんにち", "heard": "きょう"}], "match": false}'
        r = C.score_compare(text)
        self.assertEqual(r["verdict"], "mismatch")
        self.assertEqual(r["diff"], [["replace", "こんにち", "きょう"]])

    def test_compare_false_without_differences_and_unparseable(self):
        self.assertEqual(C.score_compare('{"differences": [], "match": false}')["verdict"], "mismatch")
        self.assertEqual(C.score_compare("I could not hear it.")["verdict"], "n/a")

    def test_transcript_match_with_spoken_particles(self):
        r = C.score_transcript(self.S, "かいしゃがこんにちまでつづいたのわしゃいんのおかげだ")
        self.assertEqual(r["verdict"], "match")

    def test_transcript_wrong_reading(self):
        r = C.score_transcript(self.S, "かいしゃがきょうまでつづいたのはしゃいんのおかげだ")
        self.assertEqual(r["verdict"], "mismatch")
        self.assertTrue(r["diff"])

    def test_transcript_repetition_and_omission(self):
        rep = "かいしゃがかいしゃがこんにちまでつづいたのはしゃいんのおかげだ"
        self.assertEqual(C.score_transcript(self.S, rep)["verdict"], "mismatch")
        om = "かいしゃがこんにちまでつづいたのはおかげだ"
        self.assertEqual(C.score_transcript(self.S, om)["verdict"], "mismatch")

    def test_transcript_refusal(self):
        self.assertEqual(C.score_transcript(self.S, "申し訳ありませんが、音声を聞くことはできません。")["verdict"],
                         "n/a")

    def test_transcript_alternative_readings(self):
        s = {"kana": "にじゅっぱーせんと", "alt_kana": ["にじっぱーせんと"], "tokens": [["20%", None]]}
        self.assertEqual(C.score_transcript(s, "にじっパーセント")["verdict"], "match")
        self.assertEqual(C.score_transcript(s, "にじゅうぱーせんと")["verdict"], "mismatch")

    @needs_mecab
    def test_transcript_with_kanji_is_aligned_by_reading(self):
        # a transcriber that writes kanji: regions that differ in spelling are
        # compared by reading (かいしゃ = 会社 = カイシャ → match; 明日 vs あさって →
        # mismatch). Identical spelling cannot be checked (the known limitation
        # that makes the hiragana prompt necessary).
        s = {"kana": "あしたかいしゃにいく。", "alt_kana": [],
             "tokens": [["明日", "あした"], ["会社", "かいしゃ"], ["に", None], ["行", "い"], ["く。", None]]}
        self.assertEqual(C.score_transcript(s, "明日カイシャに行く")["verdict"], "match")
        self.assertEqual(C.score_transcript(s, "明後日会社に行く")["verdict"], "mismatch")
        self.assertEqual(C.score_transcript(self.S, "会社が今日まで続いたのは社員のおかげだ")["verdict"],
                         "match")

    def test_acceptance_rule_p2(self):
        self.assertTrue(C.accept("p2", ["match", "match", "match", "match"]))
        self.assertTrue(C.accept("p2", ["match", "mismatch", "match", "match"]))
        self.assertTrue(C.accept("p2", ["match", "match", "n/a", "match"]))
        self.assertFalse(C.accept("p2", ["match", "mismatch", "n/a", "match"]))
        self.assertFalse(C.accept("p2", ["mismatch", "match", "match", "match"]))
        self.assertFalse(C.accept("p2", ["n/a", "match", "match", "match"]))
        self.assertFalse(C.accept("any", ["match", "mismatch", "match", "match"]))

    @needs_mecab
    def test_pcompare_prompt_lists_alternatives(self):
        s = {"tokens": [["20%", None]], "kana": "にじゅっぱーせんと", "alt_kana": ["にじっぱーせんと"],
             "manual_reading": True}
        prompt = C.pcompare_prompt(s)
        self.assertIn("にじゅっぱーせんと / にじっぱーせんと", prompt)
        self.assertIn("all acceptable", prompt)


class TestPipelineLogic(unittest.TestCase):
    def test_voice_rotation(self):
        voices = ["Kore", "Charon", "F2", "M2"]
        ex = [{"num": 7, "idx": i} for i in range(5)]
        self.assertEqual([P.assign_voice(x, voices) for x in ex], ["M2", "Kore", "Charon", "F2", "M2"])
        self.assertEqual(P.assign_voice({"num": 7, "idx": 0}, voices, previous="Charon"), "Charon")
        self.assertEqual(P.assign_voice({"num": 7, "idx": 0}, ["Kore", "Charon"], previous="F2"), "Charon")

    def test_priority_order(self):
        xs = [{"ex": "a", "tier": "general", "num": 5, "idx": 0},
              {"ex": "b", "tier": "general", "num": 20000, "idx": 0},
              {"ex": "c", "tier": "core", "num": 30000, "idx": 1},
              {"ex": "d", "tier": "basic", "num": 900, "idx": 0},
              {"ex": "e", "tier": "general", "num": 25000, "idx": 0, "stale": True}]
        order = [x["ex"] for x in sorted(xs, key=lambda x: P.priority_key(x, cursor=8000))]
        self.assertEqual(order, ["e", "d", "c", "a", "b"])

    def test_classify(self):
        raw_ok = "{本|ほん}を{読|よ}む。"
        examples = [
            {"ex": "00001_a_ex1", "entry": "00001_a", "num": 1, "idx": 0, "tier": "basic", "raw": raw_ok},
            {"ex": "00001_a_ex2", "entry": "00001_a", "num": 1, "idx": 1, "tier": "basic", "raw": raw_ok},
            {"ex": "00001_a_ex3", "entry": "00001_a", "num": 1, "idx": 2, "tier": "basic",
             "raw": "3{本|ぼん}ある。"},
            {"ex": "00001_a_ex4", "entry": "00001_a", "num": 1, "idx": 3, "tier": "basic", "raw": raw_ok},
            {"ex": "00001_a_ex5", "entry": "00001_a", "num": 1, "idx": 4, "tier": "basic", "raw": raw_ok},
        ]
        h = P.short_hash(raw_ok)
        manifest = {"00001_a_ex1": {"ex": "00001_a_ex1", "h": h, "v": "Kore"},
                    "00001_a_ex2": {"ex": "00001_a_ex2", "h": "0" * 16, "v": "Charon"}}
        needs_human = {"00001_a_ex4": {"ex": "00001_a_ex4", "h": h, "wf": "v2"},
                       "00001_a_ex5": {"ex": "00001_a_ex5", "h": h, "wf": "v1"}}
        rec, todo, und, held = P.classify(examples, manifest, needs_human, "v2")
        self.assertEqual([x["ex"] for x in rec], ["00001_a_ex1"])
        self.assertEqual([x["ex"] for x in und], ["00001_a_ex3"])
        self.assertEqual(und[0]["reason"], "digits")
        self.assertEqual([x["ex"] for x in held], ["00001_a_ex4"])
        self.assertEqual([x["ex"] for x in todo], ["00001_a_ex2", "00001_a_ex5"])
        self.assertTrue(todo[0]["stale"])
        self.assertEqual(todo[0]["previous_voice"], "Charon")
        self.assertFalse(todo[1]["stale"])

    def test_manifest_shards_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            old = P.MANIFEST_DIR
            P.MANIFEST_DIR = Path(d)
            try:
                P.write_manifest_records([{"ex": "00501_x_ex2", "h": "a"}, {"ex": "00001_y_ex1", "h": "b"}])
                P.write_manifest_records([{"ex": "00501_x_ex1", "h": "c"}, {"ex": "00501_x_ex2", "h": "d"}])
                self.assertEqual(sorted(p.name for p in Path(d).iterdir()), ["00000.jsonl", "00500.jsonl"])
                lines = (Path(d) / "00500.jsonl").read_text(encoding="utf-8").splitlines()
                self.assertEqual([json.loads(l)["ex"] for l in lines], ["00501_x_ex1", "00501_x_ex2"])
                m = P.load_manifest()
                self.assertEqual(m["00501_x_ex2"]["h"], "d")
                self.assertEqual(len(m), 3)
            finally:
                P.MANIFEST_DIR = old

    def test_entry_range(self):
        self.assertEqual(P.entry_range("07061_toraburu"), "07000")
        self.assertEqual(P.entry_range("00499_x_ex1"), "00000")
        self.assertEqual(P.entry_range("31054_y"), "31000")


class TestRegressionSummary(unittest.TestCase):
    def test_summarize(self):
        import audio_regression as R

        def row(key, truth, accepted, audible=None):
            r = {"key": key, "truth": truth, "truth_parsed": R.truth_of({"truth": truth}),
                 "accepted": accepted, "checks": [{"name": "pcompare:x", "verdict": "match" if accepted else "mismatch"}]}
            if audible is not None:
                r["audible"] = audible
            return r
        rows = [row("a", "injected error: wrong_reading こんにち → きょう", False, True),
                row("b", "injected error: omission いつも → ∅", False, True),
                row("c", "injected error: wrong_reading うわて → じょうず", True, False),
                row("d", "human: err", False),
                row("e", "human: ok", True),
                row("f", "human: ok - comment", False),
                row("g", "human: unsure - comment", True)]
        s = R.summarize(rows, None)
        self.assertEqual(s["injected_audible"], [2, 2])
        self.assertEqual(s["injected_inaudible_rejected"], [0, 1])
        self.assertEqual(s["human_err"], [1, 1])
        self.assertEqual(s["human_ok_false_alarms"], [1, 2])
        self.assertEqual(s["false_alarms"], ["f"])
        self.assertTrue(s["passed"])
        rows[0]["accepted"] = True
        self.assertFalse(R.summarize(rows, None)["passed"])


if __name__ == "__main__":
    unittest.main()


class TestSiteButton(unittest.TestCase):
    """The site shows the recording button only when the manifest's hash matches."""

    def setUp(self):
        import audio_manifest as M
        self.M = M
        self.raw = "⟦{本|ほん}→本：00100_hon⟧を{読|よ}む。"
        rec = {"ex": "00001_a_ex1", "h": T.text_hash("{本|ほん}を{読|よ}む。")[:16], "s": "a1",
               "f": "00000/00001_a_ex1.abcd1234.mp3"}
        M._CACHE = ({"a1": "https://example.org/audio/"}, {"00001_a_ex1": rec})

    def tearDown(self):
        self.M.reset_cache()

    def test_recording_url(self):
        self.assertEqual(self.M.recording_url({"id": "00001_a_ex1", "japanese": self.raw}),
                         "https://example.org/audio/00000/00001_a_ex1.abcd1234.mp3")
        self.assertIsNone(self.M.recording_url({"id": "00001_a_ex1", "japanese": "{本|ほん}を{買|か}う。"}))
        self.assertIsNone(self.M.recording_url({"id": "00001_a_ex2", "japanese": self.raw}))

    def test_render_examples(self):
        import entry_renderer as R
        html_ok = R.render_examples([{"id": "00001_a_ex1", "japanese": self.raw, "english": "x"}], {})
        self.assertIn('class="audio-btn"', html_ok)
        self.assertIn("00001_a_ex1.abcd1234.mp3", html_ok)
        self.assertNotIn("tts-btn", html_ok)
        html_stale = R.render_examples([{"id": "00001_a_ex1", "japanese": "{本|ほん}を{買|か}う。",
                                         "english": "x"}], {})
        self.assertIn('class="tts-btn"', html_stale)
        self.assertNotIn("audio-btn", html_stale)


class TestMaintenance(unittest.TestCase):
    def setUp(self):
        import audio_maintenance as M
        self.M = M
        self.tmp = tempfile.TemporaryDirectory()
        d = Path(self.tmp.name)
        self.saved = (M.REG_HISTORY, M.PILOTS, P.load_manifest)
        M.REG_HISTORY, M.PILOTS = d / "history.jsonl", d / "pilots.jsonl"
        P.load_manifest = lambda: {}
        self.cfg = {"checkers": [{"kind": "pcompare", "model": "m1"}], "rule": "p2",
                    "tts_model": "t1", "prompt_strategy": "E", "mp3_kbps": 48, "voices": ["Kore"]}

    def tearDown(self):
        self.M.REG_HISTORY, self.M.PILOTS, P.load_manifest = self.saved
        self.tmp.cleanup()

    def write(self, path, rows):
        path.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")

    def test_blocked_without_regression_and_pilot(self):
        blocked = {t for t, b, _ in self.M.due_tasks(self.cfg, st={}) if b}
        self.assertEqual(blocked, {"regression", "pilot"})

    def test_unblocked_after_regression_and_pilot(self):
        M, cfg = self.M, self.cfg
        now = P.now_iso()
        self.write(M.REG_HISTORY, [{"at": now, "checkers_rule_hash": M.checks_fingerprint(cfg),
                                    "passed": True, "kbps": None, "clips": 163}])
        self.write(M.PILOTS, [{"voice": "Kore", "acceptable": True,
                               "generation_fingerprint": M.generation_fingerprint(cfg),
                               "checks_fingerprint": M.checks_fingerprint(cfg)}])
        st = {"models": now[:10], "reevaluate": now[:10]}
        self.assertEqual(M.due_tasks(cfg, st=st), [])
        # changing a checker model blocks production again (regression and pilot)
        cfg2 = {**cfg, "checkers": [{"kind": "pcompare", "model": "m2"}]}
        self.assertEqual({t for t, b, _ in M.due_tasks(cfg2, st=st) if b}, {"regression", "pilot"})
        # changing the bit rate needs a new pilot only
        cfg3 = {**cfg, "mp3_kbps": 32}
        self.assertEqual({t for t, b, _ in M.due_tasks(cfg3, st=st) if b}, {"pilot"})
        # a failed or bit-rate-test regression run does not count
        self.write(M.REG_HISTORY, [{"at": now, "checkers_rule_hash": M.checks_fingerprint(cfg),
                                    "passed": True, "kbps": 32, "clips": 163}])
        self.assertIn("regression", {t for t, b, _ in M.due_tasks(cfg, st=st) if b})
