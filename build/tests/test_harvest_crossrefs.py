"""Unit tests for build/harvest_crossrefs.py (bullet parsing, header typing,
resolution, reciprocity, cap, and apply on a temp copy).

Run with:  python3 -m unittest build.tests.test_harvest_crossrefs
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
_spec = importlib.util.spec_from_file_location("harvest_crossrefs", _BUILD / "harvest_crossrefs.py")
hc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hc)
import xref_common as xc  # noqa: E402


def make_entry(eid, headword, reading, gloss, pos, notes="", transitivity=None,
               cross_references=None, prominent_see_also=None):
    entry = {
        "id": eid, "headword": headword, "reading": reading, "part_of_speech": pos[0],
        "gloss": gloss, "notes": notes,
        "metadata": {"created": "2026-01-01T00:00:00Z", "modified": "2026-01-01T00:00:00Z",
                     "vocabulary_tier": "general",
                     "tags": {"pos": list(pos), "transitivity": transitivity}},
    }
    if cross_references is not None:
        entry["cross_references"] = cross_references
    if prominent_see_also is not None:
        entry["prominent_see_also"] = prominent_see_also
    return entry


FIXTURES = [
    make_entry("20001_enjosuru", "{援助|えんじょ}する", "えんじょする", "to aid; to assist",
               ["verb-suru"],
               notes="SIMILAR WORDS:\n"
                     "- {支援|しえん}する: to support — often institutional\n"
                     "- ⟦{応援|おうえん}する→応援する：20003_ouensuru⟧ — to cheer on\n"
                     "- {妨害|ぼうがい}する: the opposite — to obstruct\n"
                     "- {援助|えんじょ}: noun form\n"
                     "- 〜的: adjectival suffix\n"
                     "- けれども — although\n"
                     "- {不明|ふめい}: no such entry\n"
                     "- Note: this line is prose\n"
                     "RELATED WORDS:\n"
                     "- {資金|しきん}: funds\n"
                     "- ⟦{寄付|きふ}→寄付：noentry⟧: donation\n"),
    make_entry("20002_shiensuru", "{支援|しえん}する", "しえんする", "to support", ["verb-suru"]),
    make_entry("20003_ouensuru", "{応援|おうえん}する", "おうえんする", "to cheer on", ["verb-suru"],
               cross_references=[{"type": "synonym", "reading": "えんじょする",
                                  "headword": "{援助|えんじょ}する", "label": "to aid"}]),
    make_entry("20004_bougaisuru", "{妨害|ぼうがい}する", "ぼうがいする", "to obstruct", ["verb-suru"]),
    make_entry("20005_enjo", "{援助|えんじょ}", "えんじょ", "aid", ["noun"]),
    make_entry("20006_keredomo", "けれども", "けれども", "although; but", ["conjunction"]),
    make_entry("20007_shikin", "{資金|しきん}", "しきん", "funds; capital", ["noun"]),
    make_entry("20008_shimeru", "{閉|し}める", "しめる", "to close (transitive)", ["verb-ichidan"],
               transitivity="transitive",
               notes="TRANSITIVITY:\n- Type: {他動詞|たどうし} (transitive)\n"
                     "- Pair: {閉|し}まる (intransitive, to close)\n"),
    make_entry("20009_shimaru", "{閉|し}まる", "しまる", "to close (intransitive)", ["verb-godan"],
               transitivity="intransitive"),
    make_entry("20010_taberu", "{食|た}べる", "たべる", "to eat", ["verb-ichidan"],
               notes="KEIGO:\n- {召|め}し{上|あ}がる (honorific)\n- いただく (humble)\n- ごはん: casual variant\n"
                     "RELATED WORDS:\n- {食|た}べ{物|もの}: food\n",
               cross_references=[{"type": "related", "target_id": "20021_tabemono", "reading": "たべもの",
                                  "headword": "{食|た}べ{物|もの}", "label": "food"}]),
    make_entry("20021_tabemono", "{食|た}べ{物|もの}", "たべもの", "food", ["noun"]),
    make_entry("20020_shikashi", "しかし", "しかし", "however; but", ["conjunction"],
               notes="SIMILAR WORDS:\n- けれども — although\n- {人名|じんめい}: unrelated noun\n"),
    make_entry("20022_jinmei_a", "{人名|じんめい}", "じんめい", "person's name", ["noun"],
               notes="SIMILAR WORDS:\n- {人命|じんめい} — human life (same reading, different kanji)\n"
                     "- {反対語|はんたいご}: antonym — an everyday synonym\n"
                     "- {対岸|たいがん}: the opposite bank — more formal\n"),
    make_entry("20023_jinmei_b", "{人命|じんめい}", "じんめい", "human life", ["noun"]),
    make_entry("20024_hantaigo", "{反対語|はんたいご}", "はんたいご", "antonym", ["noun"]),
    make_entry("20025_taigan", "{対岸|たいがん}", "たいがん", "opposite shore", ["noun"]),
    make_entry("20011_meshiagaru", "{召|め}し{上|あ}がる", "めしあがる", "to eat (honorific)", ["verb-godan"]),
    make_entry("20012_itadaku", "いただく", "いただく", "to receive (humble)", ["verb-godan"]),
    make_entry("20013_gohan", "ごはん", "ごはん", "rice; meal", ["noun"]),
    # two entries with the same plain headword: resolution by reading
    make_entry("20014_kanjou_a", "{感情|かんじょう}", "かんじょう", "emotion", ["noun"]),
    make_entry("20015_kanjou_b", "{勘定|かんじょう}", "かんじょう", "bill", ["noun"]),
    make_entry("20016_ame_rain", "{雨|あめ}", "あめ", "rain", ["noun"]),
    make_entry("20017_ame_candy", "{飴|あめ}", "あめ", "candy", ["noun"],
               notes="SIMILAR WORDS:\n- あめ: ambiguous kana term\n- {雨|あめ}: homophone rain\n"),
    make_entry("20018_kaishou", "{解消|かいしょう}", "かいしょう", "cancellation", ["noun"]),
    make_entry("20019_kaiketsu", "{解決|かいけつ}する", "かいけつする", "to solve", ["verb-suru"],
               notes="SIMILAR WORDS:\n- {解消|かいしょう}する: to eliminate — for problems\n"),
]


def write_fixtures(root, fixtures=FIXTURES, no_newline_ids=("20002_shiensuru",)):
    root = Path(root)
    for e in fixtures:
        n = int(e["id"][:5])
        d = root / f"{(n // 500) * 500:05d}"
        d.mkdir(parents=True, exist_ok=True)
        text = json.dumps(e, ensure_ascii=False, indent=2)
        if e["id"] not in no_newline_ids:
            text += "\n"
        (d / f"{e['id']}.json").write_text(text, encoding="utf-8")
    return root


class TestHeaders(unittest.TestCase):
    def test_canonical_alias_fuzzy_and_skips(self):
        self.assertEqual(hc.classify_header("SIMILAR WORDS")[:2], ("SIMILAR WORDS", "contrast"))
        self.assertEqual(hc.classify_header("SIMILAR VERBS")[:2], ("SIMILAR WORDS", "contrast"))
        self.assertEqual(hc.classify_header("CONTRAST")[:2], ("SIMILAR WORDS", "contrast"))
        self.assertEqual(hc.classify_header("COMPARED WITH")[1], "contrast")
        self.assertEqual(hc.classify_header("ANTONYMS")[1], "antonym")
        self.assertEqual(hc.classify_header("OPPOSITE")[1], "antonym")
        self.assertEqual(hc.classify_header("RELATED TERMS")[:2], ("RELATED WORDS", "related"))
        self.assertEqual(hc.classify_header("SEE ALSO")[1], "related")
        self.assertEqual(hc.classify_header("HONORIFIC FORMS")[:2], ("KEIGO", "keigo"))
        self.assertEqual(hc.classify_header("TRANSITIVITY")[1], "transitivity")
        self.assertEqual(hc.classify_header("INTRANSITIVE PAIR")[0], "TRANSITIVITY")
        self.assertEqual(hc.classify_header("RELATED TIME WORDS")[:3], ("RELATED WORDS", "related", "fuzzy"))
        self.assertEqual(hc.classify_header("CONTRAST WITH SIMILAR WORDS")[1], "contrast")
        self.assertEqual(hc.classify_header("SIMILAR ～{種|しゅ} WORDS")[1], "related")
        self.assertEqual(hc.classify_header("COMMON COLLOCATIONS")[0], None)   # other canonical
        self.assertEqual(hc.classify_header("RELATED PATTERNS")[2], "non-word")
        self.assertEqual(hc.classify_header("ZZZ NOT A KNOWN HEADER")[2], "unknown")

    def test_iter_sections(self):
        notes = "USAGE:\nprose\n\nSIMILAR WORDS:\n- a: b\n- c: d\nREGISTER: Formal.\n- x"
        secs = list(hc.iter_sections(notes))
        self.assertEqual([h for h, _ in secs], ["USAGE", "SIMILAR WORDS", "REGISTER"])
        self.assertEqual([l for l in secs[1][1] if l], ["- a: b", "- c: d"])


class TestBullets(unittest.TestCase):
    def test_colon_dash_link_and_paren_forms(self):
        b = hc.parse_bullet("- {援助|えんじょ}する: to aid — often implies help")
        self.assertEqual(b["terms"][0].plain, "援助する")
        self.assertEqual(b["terms"][0].reading, "えんじょする")
        self.assertEqual(b["gloss"], "to aid — often implies help")
        b = hc.parse_bullet("- {応援|おうえん}する — to cheer on")
        self.assertEqual((b["sep"], b["gloss"]), ("dash", "to cheer on"))
        b = hc.parse_bullet("- けれども — although…")
        self.assertEqual((b["terms"][0].plain, b["terms"][0].reading), ("けれども", "けれども"))
        b = hc.parse_bullet("- ⟦{援助|えんじょ}する→援助する：08123_enjosuru⟧: gloss")
        self.assertEqual(b["terms"][0].link_id, "08123_enjosuru")
        self.assertEqual(b["terms"][0].plain, "援助する")
        b = hc.parse_bullet("・{雰囲気|ふんいき} (atmosphere - more general)")
        self.assertEqual((b["sep"], b["gloss"]), ("paren", "atmosphere - more general"))
        b = hc.parse_bullet("- ⟦{寄付|きふ}→寄付：noentry⟧: donation")
        self.assertTrue(b["terms"][0].link_noentry)

    def test_prefix_multi_term_and_prose(self):
        b = hc.parse_bullet("- Pair: {閉|し}まる (intransitive, to close)")
        self.assertEqual(b["prefix"], "Pair")
        self.assertEqual(b["terms"][0].plain, "閉まる")
        b = hc.parse_bullet("- デフレーション / デフレ: deflation")
        self.assertEqual([t.plain for t in b["terms"]], ["デフレーション", "デフレ"])
        self.assertIsNone(hc.parse_bullet("- Note: オタク is a different word"))
        self.assertIsNone(hc.parse_bullet("- {快勝|かいしょう} ↔ {大敗|たいはい} (heavy defeat)"))
        self.assertIsNone(hc.parse_bullet("{根回|ねまわ}し refers specifically to groundwork."))
        self.assertIsNone(hc.parse_bullet("This is English prose."))
        self.assertIsNone(hc.parse_bullet("- {貯水|ちょすい}{タンク}: water storage tank"))
        self.assertIsNone(hc.parse_bullet(""))

    def test_pair_note_and_keigo_label(self):
        b = hc.parse_bullet("- Pair: {閉|し}まる (intransitive, to close)")
        self.assertEqual(hc.pair_note_from_bullet(b, b["terms"][0]), "intransitive")
        b = hc.parse_bullet("- Intransitive form: {置|お}き{換|か}わる (to be replaced)")
        self.assertEqual(hc.pair_note_from_bullet(b, b["terms"][0]), "intransitive")
        b = hc.parse_bullet("- {千切|ちぎ}る (transitive — to tear off)")
        self.assertEqual(hc.pair_note_from_bullet(b, b["terms"][0]), "transitive")
        b = hc.parse_bullet("- {千切|ちぎ}る: to tear off")
        self.assertIsNone(hc.pair_note_from_bullet(b, b["terms"][0]))
        self.assertEqual(hc.keigo_label("- いただく (humble)"), "humble")
        self.assertEqual(hc.keigo_label("- ご覧になる: honorific for 見る"), "honorific")
        self.assertIsNone(hc.keigo_label("- ママ: mom (casual)"))


class TestLabels(unittest.TestCase):
    def test_clean_label(self):
        self.assertEqual(hc.clean_label("to aid — often implies help"), "to aid — often implies help")
        self.assertEqual(hc.clean_label("shorthand, a specialised kind of {筆記|ひっき}"),
                         "shorthand, a specialised kind")
        self.assertEqual(hc.clean_label("casual abbreviation of ⟦{合成皮革|ごうせいひかく}→合成皮革：1⟧"),
                         "casual abbreviation")
        long = "secondment — temporary assignment to another company, with the original employment maintained"
        lab = hc.clean_label(long)
        self.assertTrue(lab.endswith("…"))
        self.assertLessEqual(len(lab), hc.MAX_LABEL_LEN + 1)
        self.assertEqual(lab, "secondment — temporary assignment to another company…")
        self.assertEqual(hc.clean_label("to {愛|あい}する"), "")
        self.assertEqual(hc.clean_label(""), "")

    def test_antonym_hint(self):
        for text in ("opposite of 開ける", "the opposite", "Antonym: to open", "long-lived (direct opposite)",
                     "synthetic leather — the formal opposite", "to waste — the opposite of {節約|せつやく}"):
            self.assertTrue(hc.ANTONYM_HINT_RE.search(hc.clean_label(text, max_len=999)), text)
        for text in ("used in the opposite situation", "to open", "opposing team", "the opposite bank — formal"):
            self.assertFalse(hc.ANTONYM_HINT_RE.search(text), text)


class TestHarvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = write_fixtures(Path(cls.tmp.name) / "entries")
        cls.index = xc.load_index(cls.root, keep_notes_for=True)
        cls.harvest = hc.run_harvest(cls.index, sorted(cls.index.entries), reciprocal=True)
        cls.by_pair = {(p.source_id, p.target_id): p for p in cls.harvest.proposals}

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_direct_proposals_types_and_labels(self):
        p = self.by_pair[("20001_enjosuru", "20002_shiensuru")]
        self.assertEqual((p.kind, p.type, p.label, p.how), ("cr", "contrast", "to support", "headword"))
        p = self.by_pair[("20001_enjosuru", "20003_ouensuru")]
        self.assertEqual((p.type, p.label, p.how), ("contrast", "to cheer on", "link"))
        p = self.by_pair[("20001_enjosuru", "20004_bougaisuru")]
        self.assertEqual(p.type, "antonym")                        # gloss starts with "the opposite"
        p = self.by_pair[("20020_shikashi", "20006_keredomo")]
        self.assertEqual((p.type, p.label, p.how), ("contrast", "although", "kana"))
        # a conjunction listed under a verb's SIMILAR WORDS: kana match with incompatible POS is skipped
        self.assertNotIn(("20001_enjosuru", "20006_keredomo"), self.by_pair)
        self.assertGreaterEqual(self.harvest.skipped["kana-pos-mismatch"], 1)
        p = self.by_pair[("20022_jinmei_a", "20023_jinmei_b")]
        self.assertEqual(p.type, "homophone")                      # same reading, different word
        p = self.by_pair[("20022_jinmei_a", "20024_hantaigo")]
        self.assertEqual(p.type, "synonym")                        # "antonym" here is the gloss, not a cue
        p = self.by_pair[("20022_jinmei_a", "20025_taigan")]
        self.assertEqual(p.type, "synonym")                        # "the opposite bank" is a gloss too
        self.assertIn(("20023_jinmei_b", "20022_jinmei_a"), self.by_pair)   # homophone back-link
        p = self.by_pair[("20001_enjosuru", "20007_shikin")]
        self.assertEqual((p.type, p.label), ("related", "funds"))
        p = self.by_pair[("20019_kaiketsu", "20018_kaishou")]     # 解消する -> noun 解消
        self.assertEqual((p.type, p.how), ("synonym", "headword-suru"))

    def test_skips(self):
        sk = self.harvest.skipped
        self.assertGreaterEqual(sk["suffix"], 2)          # 援助 (N of Nする) and 〜的
        self.assertGreaterEqual(sk["no-entry"], 1)        # 不明
        self.assertGreaterEqual(sk["noentry-link"], 1)    # 寄付
        self.assertGreaterEqual(sk["ambiguous"], 1)       # あめ (2 entries)
        self.assertGreaterEqual(sk["exists"], 1)          # 食べる already links 食べ物
        self.assertGreaterEqual(sk["keigo-no-keyword"], 1)  # ごはん: casual variant
        # the "- Type: {他動詞|たどうし} (transitive)" bullet is prose: nothing but the pair is proposed
        self.assertEqual([p.target_id for p in self.harvest.per_entry["20008_shimeru"]], ["20009_shimaru"])
        self.assertNotIn(("20001_enjosuru", "20005_enjo"), self.by_pair)
        # the kana-only bullet あめ is ambiguous (two entries), but {雨|あめ} resolves by headword+reading
        self.assertIn(("20017_ame_candy", "20016_ame_rain"), self.by_pair)
        self.assertEqual(self.by_pair[("20017_ame_candy", "20016_ame_rain")].type, "homophone")

    def test_transitivity_pair_becomes_psa(self):
        p = self.by_pair[("20008_shimeru", "20009_shimaru")]
        self.assertEqual((p.kind, p.note), ("psa", "intransitive"))
        back = self.by_pair[("20009_shimaru", "20008_shimeru")]
        self.assertEqual((back.kind, back.note, back.how), ("psa", "transitive", "reciprocal"))

    def test_keigo_labels_and_no_reverse(self):
        p = self.by_pair[("20010_taberu", "20011_meshiagaru")]
        self.assertEqual((p.type, p.label), ("keigo", "honorific"))
        p = self.by_pair[("20010_taberu", "20012_itadaku")]
        self.assertEqual((p.type, p.label), ("keigo", "humble"))
        self.assertNotIn(("20011_meshiagaru", "20010_taberu"), self.by_pair)
        self.assertEqual(len(self.harvest.keigo_reverse_skipped), 2)
        self.assertNotIn(("20010_taberu", "20013_gohan"), self.by_pair)

    def test_reciprocals(self):
        back = self.by_pair[("20002_shiensuru", "20001_enjosuru")]
        self.assertEqual((back.type, back.label, back.how), ("contrast", "to aid", "reciprocal"))
        # 20003 already has a forward reference (reading+headword) to 20001 -> no back-link
        self.assertNotIn(("20003_ouensuru", "20001_enjosuru"), self.by_pair)
        back = self.by_pair[("20004_bougaisuru", "20001_enjosuru")]
        self.assertEqual(back.type, "antonym")

    def test_items_carry_target_fields(self):
        p = self.by_pair[("20001_enjosuru", "20002_shiensuru")]
        item = p.to_item(self.index)
        self.assertEqual(item, {"type": "contrast", "target_id": "20002_shiensuru", "reading": "しえんする",
                                "headword": "{支援|しえん}する", "label": "to support"})


class TestCap(unittest.TestCase):
    def test_cap_keeps_direct_first(self):
        harvest = hc.Harvest()
        props = [hc.Proposal("cr", "A", f"T{i}", "related", how="headword") for i in range(6)]
        props += [hc.Proposal("cr", "A", f"R{i}", "related", how="reciprocal") for i in range(5)]
        props += [hc.Proposal("psa", "A", "P", "pair", note="transitive", how="headword")]
        kept = hc.apply_cap(props, harvest, cap=8)
        self.assertEqual(len([p for p in kept if p.kind == "cr"]), 8)
        self.assertEqual([p.target_id for p in kept if p.how == "reciprocal"], ["R0", "R1"])
        self.assertEqual(harvest.over_cap, {"A": 3})
        self.assertEqual(len([p for p in kept if p.kind == "psa"]), 1)


class TestApply(unittest.TestCase):
    def test_apply_writes_only_changed_files_and_keeps_conventions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = write_fixtures(Path(tmp) / "entries")
            before = {p: p.read_bytes() for p in root.glob("*/*.json")}
            index = xc.load_index(root, keep_notes_for=True)
            harvest = hc.run_harvest(index, sorted(index.entries), reciprocal=True)
            changed = hc.apply_proposals(harvest, index, modified="2026-09-02T00:00:00Z")
            self.assertEqual(sorted(changed), sorted(harvest.per_entry))
            for p, raw in before.items():
                eid = p.stem
                if eid in changed:
                    self.assertNotEqual(p.read_bytes(), raw)
                else:
                    self.assertEqual(p.read_bytes(), raw, f"{eid} should be untouched")
            # trailing-newline convention preserved per file
            src = root / "20000" / "20001_enjosuru.json"
            self.assertTrue(src.read_bytes().endswith(b"\n"))
            nonl = root / "20000" / "20002_shiensuru.json"
            self.assertIn("20002_shiensuru", changed)
            self.assertFalse(nonl.read_bytes().endswith(b"\n"))
            e = json.loads(src.read_text(encoding="utf-8"))
            self.assertEqual(e["metadata"]["modified"], "2026-09-02T00:00:00Z")
            targets = [r["target_id"] for r in e["cross_references"]]
            self.assertIn("20002_shiensuru", targets)
            self.assertNotIn("20005_enjo", targets)
            # key placed before metadata
            keys = list(e.keys())
            self.assertLess(keys.index("cross_references"), keys.index("metadata"))
            shimaru = json.loads((root / "20000" / "20009_shimaru.json").read_text(encoding="utf-8"))
            self.assertEqual(shimaru["prominent_see_also"],
                             [{"target_id": "20008_shimeru", "reading": "しめる", "headword": "{閉|し}める",
                               "note": "transitive"}])
            # every rewritten entry still validates against the schema
            try:
                import jsonschema
            except ImportError:
                return
            schema = json.loads((_BUILD / "schema.json").read_text(encoding="utf-8"))
            for eid in changed:
                path = next(root.glob(f"*/{eid}.json"))
                jsonschema.validate(json.loads(path.read_text(encoding="utf-8")), schema)
            # a second run finds nothing new (idempotent)
            index2 = xc.load_index(root, keep_notes_for=True)
            harvest2 = hc.run_harvest(index2, sorted(index2.entries), reciprocal=True)
            self.assertEqual(harvest2.proposals, [])


if __name__ == "__main__":
    unittest.main()
