"""Unit tests for build/normalize_common.py (shared plumbing of the
normalization tools): ID parsing, path filtering, trailing-newline
preservation. Run with:
    python3 -m unittest build.tests.test_normalize_common
"""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

_BUILD = Path(__file__).resolve().parents[2] / "build"
if str(_BUILD) not in sys.path:
    sys.path.insert(0, str(_BUILD))
_spec = importlib.util.spec_from_file_location("normalize_common", _BUILD / "normalize_common.py")
nc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(nc)


def _write(path: Path, entry: dict, newline: bool):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(entry, ensure_ascii=False, indent=2) + ("\n" if newline else ""),
                    encoding="utf-8")


class TestParseIds(unittest.TestCase):
    def test_accepts_numbers_and_full_ids(self):
        self.assertEqual(nc.parse_ids("01000,1186_tekubi, 30001"), {"01000", "01186", "30001"})

    def test_empty(self):
        self.assertEqual(nc.parse_ids(None), set())
        self.assertEqual(nc.parse_ids(""), set())

    def test_rejects_garbage(self):
        with self.assertRaises(ValueError):
            nc.parse_ids("tekubi")


class TestIterAndWrite(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for nid, nl in ((1, True), (600, False), (1200, True)):
            eid = f"{nid:05d}_x"
            _write(self.root / f"{(nid // 500) * 500:05d}" / f"{eid}.json",
                   {"id": eid, "metadata": {"modified": "2026-01-01T00:00:00Z"}}, nl)

    def tearDown(self):
        self.tmp.cleanup()

    def test_iter_all_sorted(self):
        names = [p.name for p in nc.iter_entry_paths(self.root)]
        self.assertEqual(names, ["00001_x.json", "00600_x.json", "01200_x.json"])

    def test_iter_filters(self):
        self.assertEqual([p.name for p in nc.iter_entry_paths(self.root, ids={"00600"})],
                         ["00600_x.json"])
        self.assertEqual([p.name for p in nc.iter_entry_paths(self.root, id_range=(500, 1300))],
                         ["00600_x.json", "01200_x.json"])

    def test_write_preserves_trailing_newline_convention(self):
        with_nl = self.root / "00000" / "00001_x.json"
        without_nl = self.root / "00500" / "00600_x.json"
        for path in (with_nl, without_nl):
            entry, raw = nc.load_entry(path)
            entry["headword"] = "x"
            nc.write_entry(path, entry, raw)
        self.assertTrue(with_nl.read_text(encoding="utf-8").endswith("}\n"))
        self.assertTrue(without_nl.read_text(encoding="utf-8").endswith("}"))
        self.assertEqual(json.loads(with_nl.read_text(encoding="utf-8"))["headword"], "x")

    def test_touch_modified_format(self):
        entry = {"metadata": {}}
        nc.touch_modified(entry, "2026-09-02T01:02:03Z")
        self.assertEqual(entry["metadata"]["modified"], "2026-09-02T01:02:03Z")
        nc.touch_modified(entry)
        self.assertRegex(entry["metadata"]["modified"], r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


if __name__ == "__main__":
    unittest.main()
