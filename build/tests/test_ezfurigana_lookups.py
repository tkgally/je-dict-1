"""Tests for build/ezfurigana_lookups.py (triage of ezFurigana lookup reports)."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import brainstorm_candidates as bc  # noqa: E402
import ezfurigana_lookups as ez  # noqa: E402

HEADER = "surface\treading\tcategory\ttkgje_existing_spelling\tlookups\tfirst_seen_utc\tlast_seen_utc\n"


class EzfuriganaTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.saved = (bc.ENTRIES_INDEX, bc.CANDIDATES)
        bc.ENTRIES_INDEX = root / "entries_index.json"
        bc.CANDIDATES = root / "candidate_words.json"
        bc.ENTRIES_INDEX.write_text(json.dumps({"entries": [
            {"id": "00426_yomu", "headword": "{読|よ}む", "reading": "よむ", "gloss": "to read"},
            {"id": "02249_hi", "headword": "{日|ひ}", "reading": "ひ", "gloss": "sun"},
        ]}), encoding="utf-8")
        bc.CANDIDATES.write_text(json.dumps({"candidates": [
            {"id": "C1", "word": "ペリカン", "reading": "ぺりかん"}]}), encoding="utf-8")
        self.received = root / "received"
        self.received.mkdir()
        self.ledger = root / "ledger.jsonl"

    def tearDown(self):
        bc.ENTRIES_INDEX, bc.CANDIDATES = self.saved
        self.tmp.cleanup()

    def write(self, name, rows):
        (self.received / name).write_text(HEADER + "".join("\t".join(map(str, r)) + "\n" for r in rows),
                                          encoding="utf-8")

    def test_pending_drops_entries_candidates_and_decided(self):
        self.write("2026-10-26_a.tsv", [
            ("読む", "よむ", "not in TKGJE", "", 2, "2026-06-01T00:00:00Z", "2026-06-02T00:00:00Z"),
            ("ペリカン", "ぺりかん", "not in TKGJE", "", 1, "2026-06-01T00:00:00Z", "2026-06-02T00:00:00Z"),
            ("陽", "ひ", "not in TKGJE", "", 3, "2026-06-01T00:00:00Z", "2026-06-02T00:00:00Z"),
            ("幽閉", "ゆうへい", "not in TKGJE", "", 6, "2026-06-01T00:00:00Z", "2026-06-02T00:00:00Z"),
        ])
        out, counts = ez.pending(received=self.received, ledger=self.ledger)
        self.assertEqual([x["surface"] for x in out], ["幽閉", "陽"])
        self.assertEqual(out[1]["same_reading"], ["02249_hi 日"])
        self.assertEqual(counts["entry_now"], 1)
        self.assertEqual(counts["candidate_now"], 1)
        ez.record([{"surface": "陽", "reading": "ひ", "verdict": "variant", "entry_id": "02249_hi"}],
                  received=self.received, ledger=self.ledger)
        out, counts = ez.pending(received=self.received, ledger=self.ledger)
        self.assertEqual([x["surface"] for x in out], ["幽閉"])
        self.assertEqual(counts["decided_before"], 1)
        line = json.loads(self.ledger.read_text(encoding="utf-8"))
        self.assertEqual((line["lookups"], line["category"]), (3, "not in TKGJE"))

    def test_latest_report_wins(self):
        self.write("2026-10-26_a.tsv", [
            ("幽閉", "ゆうへい", "not in TKGJE", "", 6, "2026-06-01T00:00:00Z", "2026-09-30T00:00:00Z")])
        self.write("2026-12-01_b.tsv", [
            ("幽閉", "ゆうへい", "not in TKGJE", "", 9, "2026-06-01T00:00:00Z", "2026-11-20T00:00:00Z")])
        out, _ = ez.pending(received=self.received, ledger=self.ledger)
        self.assertEqual(out[0]["lookups"], 9)

    def test_bad_verdict_refused(self):
        with self.assertRaises(SystemExit):
            ez.record([{"surface": "陽", "reading": "ひ", "verdict": "maybe"}],
                      received=self.received, ledger=self.ledger)


if __name__ == "__main__":
    unittest.main()
