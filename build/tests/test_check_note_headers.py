"""Unit tests for build/check_note_headers.py — the unknown-header baseline and
CI gate. Run with:
    python3 -m unittest build.tests.test_check_note_headers
"""
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

_BUILD = Path(__file__).resolve().parents[2] / "build"
if str(_BUILD) not in sys.path:
    sys.path.insert(0, str(_BUILD))
_spec = importlib.util.spec_from_file_location("check_note_headers", _BUILD / "check_note_headers.py")
ch = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ch)


def _entry(eid, notes):
    return {"id": eid, "headword": "x", "reading": "えっくす", "part_of_speech": "noun",
            "gloss": "x", "notes": notes,
            "metadata": {"created": "2026-01-01T00:00:01Z", "modified": "2026-01-01T00:00:01Z"}}


class TestGateLogic(unittest.TestCase):
    def test_gate_flags_only_new_headers(self):
        current = {"00001_a": ["ZZZ UNKNOWN SECTION", "NEW THING"], "00002_b": ["FIGURATIVE USE"]}
        baseline = {"00001_a": ["ZZZ UNKNOWN SECTION"]}
        self.assertEqual(ch.gate(current, baseline),
                         [("00001_a", "NEW THING"), ("00002_b", "FIGURATIVE USE")])
        self.assertEqual(ch.gate(current, {**baseline, "00001_a": ["ZZZ UNKNOWN SECTION", "NEW THING"],
                                           "00002_b": ["FIGURATIVE USE"]}), [])


class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.entries = self.root / "entries"
        (self.entries / "00000").mkdir(parents=True)
        self.baseline = self.root / "baseline.json"
        self._write("00001_a", "USAGE:\nfine.\n\nZZZ UNKNOWN SECTION:\n- x")
        self._write("00002_b", "COMMON COLLOCATIONS:\n- y")

    def tearDown(self):
        self.tmp.cleanup()

    def _write(self, eid, notes):
        p = self.entries / "00000" / f"{eid}.json"
        p.write_text(json.dumps(_entry(eid, notes), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def _run(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = ch.main(["--entries-dir", str(self.entries), "--baseline", str(self.baseline), *argv])
        return code, out.getvalue() + err.getvalue()

    def test_collect_unknown(self):
        vocab = ch.load_header_vocab()
        paths = list(ch.iter_entry_paths(self.entries))
        self.assertEqual(ch.collect_unknown(paths, vocab), {"00001_a": ["ZZZ UNKNOWN SECTION"]})

    def test_gate_without_baseline_exits_3(self):
        code, text = self._run("--gate")
        self.assertEqual(code, 3)
        self.assertIn("baseline not found", text)

    def test_write_baseline_then_gate_passes_then_drift_fails(self):
        code, text = self._run("--write-baseline")
        self.assertEqual(code, 0)
        data = json.loads(self.baseline.read_text(encoding="utf-8"))
        self.assertEqual(data["headers"], {"00001_a": ["ZZZ UNKNOWN SECTION"]})

        code, text = self._run("--gate")
        self.assertEqual(code, 0, text)

        # An alias is fine (normalized away); a brand-new unknown header is drift.
        self._write("00002_b", "COLLOCATIONS:\n- y\n\nBRAND NEW SECTION:\n- z")
        code, text = self._run("--gate")
        self.assertEqual(code, 1)
        self.assertIn("00002_b: 'BRAND NEW SECTION:'", text)
        self.assertNotIn("COLLOCATIONS", text.split("BRAND NEW SECTION")[0].split("baseline (introduced")[-1])

    def test_summary_and_list(self):
        code, text = self._run("--summary")
        self.assertEqual(code, 0)
        self.assertIn("Entries with unknown headers: 1", text)
        code, text = self._run("--list")
        self.assertIn("00001_a: ZZZ UNKNOWN SECTION:", text)

    def test_write_baseline_refuses_subsets(self):
        code, text = self._run("--write-baseline", "--range", "1", "1")
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
