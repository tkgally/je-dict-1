"""Tests for the Explore page's data: build/explore_data.py (places, shards, word
files) and build/explore_groups.py (curated groups: plans, validation, retire)."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import explore_data as xd  # noqa: E402
import explore_groups as xg  # noqa: E402

TAG_NAMES = {'weather': {'ja': '{天気|てんき}', 'en': 'Weather'}, 'food': {'ja': '{食|た}べ{物|もの}', 'en': 'Food & drink'},
             'general': {'ja': 'その{他|た}', 'en': 'Other words'}}


def entry(num, romaji, tags, tier='general', pos='noun', refs=(), examples=()):
    eid = f'{num:05d}_{romaji}'
    return {'id': eid, 'headword': romaji, 'reading': romaji, 'gloss': f'gloss of {romaji}; more', 'part_of_speech': pos,
            'examples': [{'id': f'{eid}_ex{i + 1}', 'japanese': j, 'english': 'e'} for i, j in enumerate(examples)],
            'cross_references': [{'type': t, 'target_id': tid, 'headword': 'x'} for tid, t in refs],
            'metadata': {'vocabulary_tier': tier, 'tags': {'pos': [pos], 'semantic': list(tags)}}}


class HelpersTest(unittest.TestCase):
    def test_strip_links_keeps_surface_and_furigana(self):
        self.assertEqual(xd.strip_links('⟦{雨|あめ}→雨：00583_ame⟧が⟦{降|ふ}る→降る：00001_furu⟧。'), '{雨|あめ}が{降|ふ}る。')
        self.assertEqual(xd.plain('⟦{雨|あめ}→雨：00583_ame⟧だ'), '雨だ')

    def test_word_cat_takes_the_first_decisive_tag(self):
        self.assertEqual(xd.word_cat(['adverb', 'verb-suru']), 'adv')
        self.assertEqual(xd.word_cat(['noun', 'verb-suru']), 'noun')
        self.assertEqual(xd.word_cat(['verb-godan']), 'verb')
        self.assertEqual(xd.word_cat(['adjective-na']), 'adj')
        self.assertEqual(xd.word_cat(['expression']), 'expr')
        self.assertEqual(xd.word_cat([]), 'expr')

    def test_entry_tags_fall_back_to_the_catch_all(self):
        self.assertEqual(xd.entry_tags(entry(1, 'a', [])), ['general'])
        self.assertEqual(xd.entry_tags(entry(1, 'a', ['food', 'food', 'weather'])), ['food', 'weather'])

    def test_bare_kanji(self):
        self.assertEqual(xd.bare_kanji('{天気|てんき}'), [])
        self.assertEqual(xd.bare_kanji('天{気|き}'), ['天'])


class ClusterTest(unittest.TestCase):
    def test_every_id_lands_in_exactly_one_shard_and_linked_ids_stay_together(self):
        ids = [f'{i:05d}_w' for i in range(100)]
        adj = {}
        for a, b in zip(ids[:30], ids[1:30]):          # a chain of 30
            adj.setdefault(a, set()).add(b)
            adj.setdefault(b, set()).add(a)
        shards = xd.cluster(ids, adj, target=40, min_cluster=10)
        flat = [i for s in shards for i in s]
        self.assertEqual(sorted(flat), ids)
        self.assertEqual(len(flat), len(set(flat)))
        home = next(s for s in shards if ids[0] in s)
        self.assertTrue(set(ids[:30]) <= set(home))
        self.assertTrue(all(len(s) <= 40 + 9 for s in shards))

    def test_is_deterministic(self):
        ids = [f'{i:05d}_w' for i in range(60)]
        adj = {ids[i]: {ids[(i * 7) % 60]} for i in range(60)}
        self.assertEqual(xd.cluster(ids, adj), xd.cluster(list(reversed(ids)), adj))


class PlanAndBuildTest(unittest.TestCase):
    def setUp(self):
        self.entries = [entry(i, f'w{i}', ['weather'], tier='basic' if i < 5 else 'general',
                              refs=[(f'{i + 1:05d}_w{i + 1}', 'related')] if i < 19 else []) for i in range(20)]
        self.entries.append(entry(30, 'pan', ['food', 'weather'], pos='verb-godan',
                                  examples=['⟦パン→パン：00030_pan⟧だ。', 'b', 'c']))
        self.entries.append(entry(31, 'nothing', []))

    def test_groups_take_entries_out_of_tag_places(self):
        groups = [{'tag': 'weather', 'id': 'rain', 'ja': '{雨|あめ}', 'en': 'Rain',
                   'members': ['00000_w0', '00001_w1', '00030_pan', '99999_gone']}]
        p = xd.plan(self.entries, TAG_NAMES, groups)
        places = {pl['id']: pl for pl in p['places']}
        self.assertEqual(places['weather.rain']['shards'][0]['ids'], ['00000_w0', '00001_w1', '00030_pan'])
        weather = [i for s in places['weather']['shards'] for i in s['ids']]
        self.assertNotIn('00000_w0', weather)
        self.assertNotIn('00030_pan', weather)
        self.assertNotIn('food', places)                      # its only entry is in a curated group
        self.assertEqual(p['entry_places']['00030_pan'], ['weather.rain'])
        self.assertEqual(p['entry_places']['00031_nothing'], ['general'])
        self.assertTrue(any('99999_gone' in m for m in p['problems']))

    def test_tag_places_are_split_by_tier_band(self):
        p = xd.plan(self.entries, TAG_NAMES, [])
        weather = next(pl for pl in p['places'] if pl['id'] == 'weather')
        files = {s['file']: s['ids'] for s in weather['shards']}
        self.assertEqual(sorted(files['weather-a00']), [f'{i:05d}_w{i}' for i in range(5)])
        self.assertIn('00030_pan', files['weather-g00'])

    def test_a_tag_without_a_name_is_reported(self):
        p = xd.plan(self.entries, {'weather': TAG_NAMES['weather'], 'general': TAG_NAMES['general']}, [])
        self.assertTrue(any("'food'" in m for m in p['problems']))

    def test_build_writes_index_shards_and_lookup(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            r = xd.build_explore(self.entries, out, tag_names=TAG_NAMES, groups=[], stores={'a1': 'https://x/'}, quiet=True)
            self.assertEqual(r['entries'], 22)
            index = json.loads((out / 'explore' / 'index.json').read_text(encoding='utf-8'))
            self.assertEqual([p['id'] for p in index['places']], ['food', 'general', 'weather'])
            weather = index['places'][2]
            self.assertEqual(sum(sum(s['n']) for s in weather['sh']), 21)
            a = next(s for s in weather['sh'] if s['f'] == 'weather-a00')
            self.assertEqual(a['n'][0 * 5 + 0], 5)            # five basic nouns
            self.assertEqual(a['near'], [1])                   # cross-referenced from the general shard
            words = json.loads((out / 'explore' / 's' / 'food-g00.json').read_text(encoding='utf-8'))['words']
            w = words[0]
            self.assertEqual((w['i'], w['t'], w['c'], w['pl']), ('00030_pan', 2, 1, ['food', 'weather']))
            self.assertEqual(w['e'][0]['j'], 'パンだ。')
            self.assertEqual(len(w['e']), 2)
            lookup = json.loads((out / 'explore' / 'w' / '00000.json').read_text(encoding='utf-8'))
            self.assertEqual(len(lookup['00030_pan']), 2)      # in the food place and the weather place
            first = json.loads((out / 'explore' / 's' / 'weather-a00.json').read_text(encoding='utf-8'))['words']
            w0 = next(x for x in first if x['i'] == '00000_w0')
            self.assertEqual(w0['x'], [['00001_w1', 'r', 'w1', 'gloss of w1']])


class GroupsToolTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.saved = xg.GROUPS_DIR
        xg.GROUPS_DIR = Path(self.tmp.name) / 'explore' / 'groups'

    def tearDown(self):
        xg.GROUPS_DIR = self.saved
        self.tmp.cleanup()

    PLAN = """tag: weather
== rain | {雨|あめ} | Rain
00001_ame   雨 あめ rain
00002_tsuyu
00003_kasa
== wind | {風|かぜ} | Wind
00004_kaze
00005_arashi
00006_taifuu
"""

    def test_apply_writes_groups_and_a_second_plan_extends_them(self):
        r = xg.apply_plan(self.PLAN)
        self.assertEqual((r['tag'], r['new_groups'], r['members_added']), ('weather', 2, 6))
        r = xg.apply_plan('tag: weather\n== rain\n00007_niwakaame\n00001_ame\n')
        self.assertEqual((r['new_groups'], r['members_added']), (0, 1))
        data = xg.read_file('weather')
        self.assertEqual(data['groups'][0]['members'], ['00001_ame', '00002_tsuyu', '00003_kasa', '00007_niwakaame'])
        self.assertEqual(data['groups'][0]['ja'], '{雨|あめ}')
        self.assertEqual(xg.grouped_ids(), {f'0000{i}_{r}' for i, r in
                                            enumerate(['ame', 'tsuyu', 'kasa', 'kaze', 'arashi', 'taifuu', 'niwakaame'], 1)})

    def test_leftovers_are_recorded_and_leave_the_worklist(self):
        r = xg.apply_plan(self.PLAN + '== (none)\n00008_moyou  fits nowhere\n00001_ame\n')
        self.assertEqual(r['leftover'], 1)                         # 00001_ame is in a group, so not left over
        self.assertEqual(xg.read_file('weather')['leftover'], ['00008_moyou'])
        self.assertIn('00008_moyou', xg.grouped_ids(with_leftover=True))
        self.assertNotIn('00008_moyou', xg.grouped_ids())
        entries = [entry(8, 'moyou', ['weather']), entry(9, 'new', ['weather'])]
        self.assertEqual([ln.split('\t')[0] for ln in xg.worklist(entries, 'weather')], ['00009_new'])
        self.assertEqual(xg.survey(entries)['ungrouped'], 1)
        xg.apply_plan('tag: weather\n== rain\n00008_moyou\n')    # later it finds a group
        self.assertNotIn('leftover', xg.read_file('weather'))
        errors, _ = xg.validate(exists=lambda i: True)
        self.assertEqual(errors, [])

    def test_plan_errors(self):
        with self.assertRaises(ValueError):
            xg.parse_plan('== rain | {雨|あめ} | Rain\n00001_ame\n')          # no tag line
        with self.assertRaises(ValueError):
            xg.parse_plan('tag: weather\n00001_ame\n')                          # member before a group
        with self.assertRaises(ValueError):
            xg.parse_plan('tag: weather\n== rain | {雨|あめ} | Rain\nnot-an-id\n')
        with self.assertRaises(ValueError):
            xg.apply_plan('tag: weather\n== rain\n00001_ame\n')                 # a new group needs names

    def test_validate_accepts_a_good_file_and_names_each_problem(self):
        xg.apply_plan(self.PLAN)
        errors, _ = xg.validate(exists=lambda i: True)
        self.assertEqual(errors, [])
        xg.write_file('weather', {'groups': [
            {'id': 'Rain', 'ja': '雨', 'en': 'A name that is much too long for the sign', 'members': ['00001_ame', '00001_ame']},
            {'id': 'wind', 'ja': '{風|カゼ}', 'en': 'Wind', 'members': ['00004_kaze', '00005_arashi', '00009_gone']},
        ]})
        errors, _ = xg.validate(exists=lambda i: i != '00009_gone')
        text = '\n'.join(errors)
        for needle in ('lower-case words', 'kanji without furigana', 'listed twice', 'a group has 3 to 45',
                       'furigana must be hiragana', 'not entries: 00009_gone'):
            self.assertIn(needle, text)

    def test_validate_limits_an_entry_to_three_groups(self):
        members = ['00001_a', '00002_b', '00003_c']
        xg.write_file('weather', {'groups': [{'id': f'g{i}', 'ja': 'あ', 'en': f'G{i}', 'members': members} for i in range(4)]})
        errors, _ = xg.validate(exists=lambda i: True)
        self.assertTrue(any('is in 4 groups' in e for e in errors))

    def test_the_repository_files_pass(self):
        xg.GROUPS_DIR = self.saved
        errors, _ = xg.validate()
        self.assertEqual(errors, [])

    def test_replace_member_follows_a_retired_or_renamed_entry(self):
        xg.apply_plan(self.PLAN)
        changed = xg.replace_member('00002_tsuyu', '00002_baiu')
        self.assertEqual(changed, ['explore/groups/weather.json'])
        self.assertEqual(xg.read_file('weather')['groups'][0]['members'], ['00001_ame', '00002_baiu', '00003_kasa'])
        xg.replace_member('00003_kasa', '00001_ame')           # merged into an entry already in the group
        self.assertEqual(xg.read_file('weather')['groups'][0]['members'], ['00001_ame', '00002_baiu'])
        self.assertEqual(xg.replace_member('00099_none', '00001_ame'), [])

    def test_survey_and_next_tags(self):
        xg.apply_plan('tag: weather\n== rain | {雨|あめ} | Rain\n00000_w0\n00001_w1\n00002_w2\n')
        entries = [entry(i, f'w{i}', ['weather'], tier='basic') for i in range(5)] + [entry(9, 'pan', ['food'])]
        s = xg.survey(entries)
        self.assertEqual((s['entries'], s['grouped'], s['leftover'], s['ungrouped'], s['groups']), (6, 3, 0, 3, 1))
        self.assertEqual(s['tags']['weather']['ungrouped_basic_core'], 2)
        self.assertEqual([t for t, _ in xg.next_tags(s)], ['weather', 'food'])   # the tag already begun comes first
        lines = xg.worklist(entries, 'weather')
        self.assertEqual([ln.split('\t')[0] for ln in lines], ['00003_w3', '00004_w4'])


if __name__ == '__main__':
    unittest.main()
