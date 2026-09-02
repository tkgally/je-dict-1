"""Unit tests for build/review_transitivity.py: prompt builder, response parser,
and the apply logic on a temp copy. No API calls.

Run with:  python3 -m unittest build.tests.test_review_transitivity
"""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

_BUILD = Path(__file__).resolve().parents[1]
if str(_BUILD) not in sys.path:
    sys.path.insert(0, str(_BUILD))
_spec = importlib.util.spec_from_file_location("review_transitivity", _BUILD / "review_transitivity.py")
rt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rt)
import xref_common as xc  # noqa: E402
from review_runner import parse_model_response  # noqa: E402


def make_verb(eid, headword, reading, gloss, pos="verb-godan", transitivity=None, examples=3,
              prominent_see_also=None):
    entry = {
        "id": eid, "headword": headword, "reading": reading, "part_of_speech": "verb",
        "gloss": gloss,
        "examples": [{"id": f"{eid}_ex{i}", "japanese": f"⟦{{例|れい}}→例：1⟧{i}{headword}。",
                      "english": f"Example {i}."} for i in range(1, examples + 1)],
        "metadata": {"created": "2026-01-01T00:00:00Z", "modified": "2026-01-01T00:00:00Z",
                     "vocabulary_tier": "general",
                     "tags": {"pos": [pos], "transitivity": transitivity}},
    }
    if prominent_see_also is not None:
        entry["prominent_see_also"] = prominent_see_also
    return entry


FIXTURES = [
    make_verb("18701_shimeru", "{閉|し}める", "しめる", "to close", "verb-ichidan"),
    make_verb("18702_shimaru", "{閉|し}まる", "しまる", "to close (intr.)"),
    make_verb("18703_akeru", "{開|あ}ける", "あける", "to open", "verb-ichidan"),
    make_verb("18704_aku_a", "{開|あ}く", "あく", "to open (intr.)"),
    make_verb("18705_aku_b", "{開|あ}く", "あく", "to open (variant)"),          # makes 開く ambiguous
    make_verb("18706_kanryousuru", "{完了|かんりょう}する", "かんりょうする", "to complete", "verb-suru"),
    make_verb("18707_hashiru", "{走|はし}る", "はしる", "to run", transitivity="intransitive"),
    make_verb("18708_deru", "{出|で}る", "でる", "to go out", "verb-ichidan", transitivity="intransitive",
              prominent_see_also=[{"target_id": "18709_dasu", "reading": "だす", "headword": "{出|だ}す",
                                   "note": "transitive"}]),
    make_verb("18709_dasu", "{出|だ}す", "だす", "to take out"),
]
FIXTURES[1]["examples"] = []                 # no examples at all
FIXTURES[2]["metadata"]["tags"]["pos"] = ["noun"]   # wait: 開ける must stay a verb — fixed below
FIXTURES[2]["metadata"]["tags"]["pos"] = ["verb-ichidan"]
NOUN = {"id": "18710_mado", "headword": "{窓|まど}", "reading": "まど", "part_of_speech": "noun",
        "gloss": "window", "examples": [],
        "metadata": {"created": "2026-01-01T00:00:00Z", "modified": "2026-01-01T00:00:00Z",
                     "tags": {"pos": ["noun"]}}}


def write_fixtures(root, no_newline_ids=("18702_shimaru",)):
    root = Path(root)
    for e in FIXTURES + [NOUN]:
        n = int(e["id"][:5])
        d = root / f"{(n // 500) * 500:05d}"
        d.mkdir(parents=True, exist_ok=True)
        text = json.dumps(e, ensure_ascii=False, indent=2)
        if e["id"] not in no_newline_ids:
            text += "\n"
        (d / f"{e['id']}.json").write_text(text, encoding="utf-8")
    return root


class TestPrompt(unittest.TestCase):
    def test_payload_and_prompt(self):
        payloads = [rt.verb_payload(e) for e in FIXTURES[:3]]
        self.assertEqual(payloads[0]["headword"], "閉める")           # furigana stripped
        self.assertEqual(len(payloads[0]["examples"]), 2)            # first two only
        self.assertEqual(payloads[0]["examples"][0]["ja"], "例1閉める。")  # link + furigana stripped
        self.assertEqual(payloads[1]["examples"], [])
        prompt = rt.build_prompt(payloads)
        for p in payloads:
            self.assertIn(p["id"], prompt)
        self.assertIn("〜する", prompt)                               # suru-verb guidance
        self.assertIn('"both"', prompt)
        self.assertIn("JSON array", prompt)
        self.assertNotIn("{閉|し}める", prompt)
        self.assertLess(prompt.count("Example"), 7)


class TestParser(unittest.TestCase):
    def test_valid_and_invalid_items(self):
        ids = ["18701_shimeru", "18702_shimaru", "18706_kanryousuru"]
        parsed = [
            {"id": "18701_shimeru", "transitivity": "Transitive", "pair": "閉まる", "confidence": 0.97},
            {"id": "18702", "transitivity": "intransitive", "pair": "null", "confidence": "0.9"},
            {"id": "18706_kanryousuru", "transitivity": "ambitransitive", "pair": None, "confidence": 1.7},
            {"id": "99999_nope", "transitivity": "transitive", "pair": None, "confidence": 1},
            "junk",
        ]
        results, problems = rt.parse_batch(parsed, ids)
        self.assertEqual([r["id"] for r in results], ids)
        self.assertEqual(results[0]["transitivity"], "transitive")
        self.assertEqual(results[0]["pair"], "閉まる")
        self.assertIsNone(results[1]["pair"])
        self.assertEqual(results[1]["confidence"], 0.9)
        self.assertEqual(results[2]["transitivity"], "both")
        self.assertEqual(results[2]["confidence"], 1.0)              # clamped
        self.assertTrue(any("99999_nope" in p for p in problems))
        self.assertTrue(any("not an object" in p for p in problems))

    def test_missing_and_invalid_transitivity(self):
        results, problems = rt.parse_batch(
            [{"id": "18701_shimeru", "transitivity": "maybe", "confidence": 0.5}],
            ["18701_shimeru", "18702_shimaru"])
        self.assertEqual(results, [])
        self.assertTrue(any("invalid transitivity" in p for p in problems))
        self.assertTrue(any("18702_shimaru: no result" in p for p in problems))
        self.assertEqual(rt.parse_batch({"results": []}, ["x"])[0], [])

    def test_plumbing_with_fenced_reply(self):
        reply = {"choices": [{"message": {"content": '```json\n[{"id": "18701_shimeru", '
                                                    '"transitivity": "transitive", "pair": "閉まる (intransitive)", '
                                                    '"confidence": 0.95}]\n```'}}]}
        parsed = parse_model_response(reply)
        results, problems = rt.parse_batch(parsed, ["18701_shimeru"])
        self.assertEqual(problems, [])
        self.assertEqual(results[0]["pair"], "閉まる")


class TestApply(unittest.TestCase):
    def run_plan(self, root, results, threshold=0.9):
        index = xc.load_index(root)
        changes, stats, details = rt.plan_apply(results, index, threshold)
        return index, changes, stats, details

    def test_plan_and_apply(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = write_fixtures(Path(tmp) / "entries")
            before = {p: p.read_bytes() for p in root.glob("*/*.json")}
            results = {
                "18701_shimeru": {"id": "18701_shimeru", "transitivity": "transitive", "pair": "閉まる", "confidence": 0.95},
                "18703_akeru": {"id": "18703_akeru", "transitivity": "transitive", "pair": "開く", "confidence": 0.99},
                "18706_kanryousuru": {"id": "18706_kanryousuru", "transitivity": "both", "pair": None, "confidence": 0.92},
                "18702_shimaru": {"id": "18702_shimaru", "transitivity": "intransitive", "pair": "閉める", "confidence": 0.6},
                "18707_hashiru": {"id": "18707_hashiru", "transitivity": "transitive", "pair": None, "confidence": 0.95},
                "18708_deru": {"id": "18708_deru", "transitivity": "intransitive", "pair": "出す", "confidence": 0.99},
                "18710_mado": {"id": "18710_mado", "transitivity": "transitive", "pair": None, "confidence": 1.0},
                "00001_missing": {"id": "00001_missing", "transitivity": "transitive", "pair": None, "confidence": 1.0},
            }
            index, changes, stats, details = self.run_plan(root, results)
            self.assertEqual(changes["18701_shimeru"]["transitivity"], "transitive")
            self.assertEqual(changes["18701_shimeru"]["psa"],
                             [{"target_id": "18702_shimaru", "reading": "しまる", "headword": "{閉|し}まる",
                               "note": "intransitive"}])
            self.assertEqual(changes["18702_shimaru"]["psa"][0]["note"], "transitive")
            self.assertIsNone(changes["18702_shimaru"]["transitivity"])     # below threshold: tag not set
            self.assertEqual(changes["18703_akeru"]["transitivity"], "transitive")
            self.assertEqual(changes["18703_akeru"]["psa"], [])              # 開く ambiguous
            self.assertEqual(stats["pair-ambiguous"], 1)
            self.assertEqual(changes["18706_kanryousuru"]["transitivity"], "both")
            self.assertNotIn("18707_hashiru", changes)                       # existing tag never overwritten
            self.assertEqual(stats["conflict-existing-tag"], 1)
            self.assertNotIn("18708_deru", changes)                          # already tagged, link exists
            self.assertEqual(stats["pair-link-exists"], 1)
            self.assertEqual(changes["18709_dasu"]["psa"][0]["target_id"], "18708_deru")  # back-link only
            self.assertNotIn("18710_mado", changes)
            self.assertEqual(stats["not-a-verb"], 1)
            self.assertEqual(stats["entry-missing"], 1)
            self.assertEqual(stats["below-threshold"], 1)

            written = rt.apply_changes(changes, index, modified="2026-09-02T00:00:00Z")
            self.assertEqual(sorted(written), sorted(changes))
            for p, raw in before.items():
                if p.stem in written:
                    self.assertNotEqual(p.read_bytes(), raw)
                else:
                    self.assertEqual(p.read_bytes(), raw, f"{p.stem} should be untouched")
            shimeru = json.loads((root / "18500" / "18701_shimeru.json").read_text(encoding="utf-8"))
            self.assertEqual(shimeru["metadata"]["tags"]["transitivity"], "transitive")
            self.assertEqual(shimeru["metadata"]["modified"], "2026-09-02T00:00:00Z")
            self.assertEqual(shimeru["prominent_see_also"][0]["target_id"], "18702_shimaru")
            self.assertLess(list(shimeru).index("prominent_see_also"), list(shimeru).index("metadata"))
            shimaru_raw = (root / "18500" / "18702_shimaru.json").read_bytes()
            self.assertFalse(shimaru_raw.endswith(b"\n"))                    # convention preserved
            shimaru = json.loads(shimaru_raw.decode("utf-8"))
            self.assertIsNone(shimaru["metadata"]["tags"]["transitivity"])
            self.assertEqual(shimaru["prominent_see_also"][0]["note"], "transitive")
            try:
                import jsonschema
            except ImportError:
                return
            schema = json.loads((_BUILD / "schema.json").read_text(encoding="utf-8"))
            for eid in written:
                path = next(root.glob(f"*/{eid}.json"))
                jsonschema.validate(json.loads(path.read_text(encoding="utf-8")), schema)
            # idempotent: a second plan on the updated copy has nothing left to write
            index2, changes2, stats2, _ = self.run_plan(root, results)
            self.assertEqual(changes2, {})

    def test_load_results_keeps_latest(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d / "a.jsonl").write_text('{"id": "x", "transitivity": "transitive", "reviewed_at": "2026-01-01T00:00:00Z"}\n'
                                       'not json\n', encoding="utf-8")
            (d / "b.jsonl").write_text('{"id": "x", "transitivity": "both", "reviewed_at": "2026-02-01T00:00:00Z"}\n',
                                       encoding="utf-8")
            res = rt.load_results(out_dir=d)
            self.assertEqual(res["x"]["transitivity"], "both")


if __name__ == "__main__":
    unittest.main()
