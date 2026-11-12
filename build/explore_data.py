#!/usr/bin/env python3
"""Data for the Explore page (explore.html): the dictionary as a 3D word cloud.

The page shows a handful of *places*, each a sign with a dozen or so words
around it, and lines between words that cross-reference each other. This
module turns the entries into the files the page reads.

Where places come from
    * Every semantic tag is a place (`explore/tags.json` gives its Japanese and
      English name). A tag place holds the tag's entries that are in no curated
      group yet.
    * `explore/groups/<tag>.json` holds curated groups: finer places of roughly
      6 to 40 entries, each with its own name. An entry that is in a curated
      group leaves the tag places. `python3 build/explore_groups.py` is the
      tool for writing and checking those files.

Where connections come from
    The entries' own cross-references. Nothing about them is stored here.

What is written (under <site>/explore/, generated, never tracked)
    index.json      places, their shards (word counts by tier and word type, and
                    the shards of the same place most linked to each), the audio stores
    s/<shard>.json  the words of one shard: headword, reading, gloss, tier, word
                    type, cross-references, places, two examples with recordings
    w/<range>.json  entry id → the shards that hold it (for explore.html?w=<id>)

A tag place can hold thousands of entries, and the page wants about a dozen at
a time, so a tag's entries are cut into shards of about 48: first by tier band
(basic and core together, general apart, so that a level filter never needs
many files), then along the cross-reference graph, so that the words of one
shard are connected to each other. A curated group is one shard.

    python3 build/explore_data.py --out /tmp/site     # write <out>/explore/
    python3 build/explore_data.py --stats             # counts only
"""
import argparse
import json
import re
import sys
from collections import defaultdict, deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from audio_manifest import valid_record  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
EXPLORE_DIR = ROOT / 'explore'
TAGS_FILE = EXPLORE_DIR / 'tags.json'
GROUPS_DIR = EXPLORE_DIR / 'groups'

OTHER_TAG = 'general'          # the catch-all place: entries tagged "general" or carrying no semantic tag
SHARD_TARGET = 48              # words per shard of a tag place
SHARD_MIN_CLUSTER = 10         # a connected cluster smaller than this is packed with others
TIERS = ('basic', 'core', 'general')
CATS = ('noun', 'verb', 'adj', 'adv', 'expr')
# cross-reference type → one-letter code read by build/templates/explore.js
XREF_CODES = {'contrast': 'c', 'related': 'r', 'see_also': 'r', 'synonym': 's', 'antonym': 'a',
              'pair': 'p', 'keigo': 'k', 'homophone': 'h'}

FURIGANA_RE = re.compile(r'\{([^|{}]+)\|([^{}]+)\}')
LINK_RE = re.compile(r'⟦([^⟧→]*)→[^⟧]*⟧')
KANJI_RE = re.compile(r'[㐀-䶿一-鿿豈-﫿々〆ヶ]')


def strip_links(text: str) -> str:
    """Example markup without inline links: ⟦surface→base：id⟧ becomes surface (furigana kept)."""
    return LINK_RE.sub(lambda m: m.group(1), text or '')


def plain(text: str) -> str:
    """Text with links and furigana removed."""
    return FURIGANA_RE.sub(lambda m: m.group(1), strip_links(text))


def bare_kanji(text: str) -> list:
    """Kanji in `text` that stand outside any {漢字|かんじ} brace."""
    return KANJI_RE.findall(FURIGANA_RE.sub('', text or ''))


def word_cat(pos_tags) -> str:
    """One of CATS, from the entry's part-of-speech tags (the first decisive tag wins)."""
    for t in pos_tags or []:
        if t == 'adverb':
            return 'adv'
        if t.startswith('verb'):
            return 'verb'
        if 'adjective' in t or t.startswith('pre-noun'):
            return 'adj'
        if t in ('noun', 'pronoun', 'number', 'counter'):
            return 'noun'
    return 'expr'


def short_gloss(gloss: str, limit: int = 30) -> str:
    g = (gloss or '').split(';')[0].strip()
    if len(g) > 24 and ',' in g:
        g = g.split(',')[0].strip()
    if len(g) > limit:
        g = g[:limit - 2].rstrip() + '…'
    return g


def entry_tags(entry: dict) -> list:
    """The entry's places at tag level: its semantic tags, or the catch-all."""
    tags = []
    for t in entry.get('metadata', {}).get('tags', {}).get('semantic') or []:
        if t and t not in tags:
            tags.append(t)
    return tags or [OTHER_TAG]


# ---------------------------------------------------------------- curated sources

def load_tag_names(path: Path = None) -> dict:
    """{tag: {'ja': ..., 'en': ...}} from explore/tags.json."""
    path = path or TAGS_FILE
    data = json.loads(path.read_text(encoding='utf-8'))
    return data['tags']


def load_groups(groups_dir: Path = None) -> list:
    """Every curated group, in file then file order:
    [{'tag', 'id' (slug within the tag), 'ja', 'en', 'members': [entry ids]}]."""
    groups_dir = groups_dir or GROUPS_DIR
    out = []
    if not groups_dir.exists():
        return out
    for f in sorted(groups_dir.glob('*.json')):
        data = json.loads(f.read_text(encoding='utf-8'))
        for g in data.get('groups') or []:
            out.append({'tag': data.get('tag', f.stem), 'id': g['id'], 'ja': g['ja'], 'en': g['en'],
                        'members': list(g.get('members') or [])})
    return out


# ---------------------------------------------------------------- shards

def cluster(ids: list, adj: dict, target: int = SHARD_TARGET, min_cluster: int = SHARD_MIN_CLUSTER) -> list:
    """Cut `ids` into lists of about `target`, keeping cross-referenced entries together.

    Deterministic: seeds are taken by number of connections inside the set
    (most first), then by id; each seed grows breadth-first to `target`.
    Clusters smaller than `min_cluster` (and unconnected entries) are packed
    together in id order.
    """
    inside = set(ids)
    local = {i: sorted(n for n in adj.get(i, ()) if n in inside and n != i) for i in ids}
    done, shards, small = set(), [], []
    for seed in sorted(ids, key=lambda i: (-len(local[i]), i)):
        if seed in done:
            continue
        group, queue = [], deque([seed])
        done.add(seed)
        while queue and len(group) < target:
            cur = queue.popleft()
            group.append(cur)
            for nb in local[cur]:
                if nb not in done and len(group) + len(queue) < target:
                    done.add(nb)
                    queue.append(nb)
        group.extend(queue)
        (shards if len(group) >= min_cluster else small).append(group)
    pack = []
    for group in small:
        if pack and len(pack) + len(group) > target:
            shards.append(pack)
            pack = []
        pack = pack + group
    if pack:
        if len(pack) < min_cluster and shards:
            min(shards, key=len).extend(pack)      # a few stragglers join the smallest shard
        else:
            shards.append(pack)
    return shards


# ---------------------------------------------------------------- the build

def near_shards(shards: list, adj: dict, keep: int = 3) -> list:
    """For each shard of one place, the indexes of the (up to `keep`) other shards
    it shares the most cross-references with, strongest first. The page uses this
    to show familiar words next to the new words related to them."""
    home = {}
    for si, shard in enumerate(shards):
        for i in shard['ids']:
            home[i] = si
    counts = [defaultdict(int) for _ in shards]
    for i, si in home.items():
        for nb in adj.get(i, ()):
            sj = home.get(nb)
            if sj is not None and sj != si:
                counts[si][sj] += 1
    return [[sj for sj, _ in sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))[:keep]] for c in counts]


def word_record(entry: dict, by_id: dict, places: list, stores_seen: set) -> dict:
    meta = entry.get('metadata', {})
    xs, seen = [], set()
    for x in entry.get('cross_references') or []:
        tid, code = x.get('target_id'), XREF_CODES.get(x.get('type'))
        target = by_id.get(tid)
        if not target or not code or tid in seen or tid == entry['id']:
            continue
        seen.add(tid)
        xs.append([tid, code, target.get('headword', ''), short_gloss(target.get('gloss', ''))])
    examples = entry.get('examples') or []
    recorded = [(ex, valid_record(ex)) for ex in examples[:6]]
    recorded = [(ex, r) for ex, r in recorded if r]
    if len(recorded) > 2:                              # the two shortest recorded examples, in their own order
        keep = sorted(recorded, key=lambda p: len(plain(p[0].get('japanese', ''))))[:2]
        recorded = [p for p in recorded if p in keep]
    chosen = recorded or [(ex, None) for ex in examples[:2]]
    exs = []
    for ex, rec in chosen:
        item = {'j': strip_links(ex.get('japanese', '')), 'e': ex.get('english', '')}
        if rec:
            item['a'] = [rec['s'], rec['f']]
            stores_seen.add(rec['s'])
        exs.append(item)
    return {
        'i': entry['id'], 'h': entry.get('headword', ''), 'r': entry.get('reading', ''), 'g': entry.get('gloss', ''),
        't': TIERS.index(tier_of(entry)),
        'c': CATS.index(word_cat(meta.get('tags', {}).get('pos'))), 'p': entry.get('part_of_speech', ''),
        'x': xs, 'pl': places, 'e': exs,
    }


def tier_of(entry: dict) -> str:
    t = entry.get('metadata', {}).get('vocabulary_tier')
    return t if t in TIERS else 'general'


def plan(entries: list, tag_names: dict, groups: list) -> dict:
    """Decide the places and shards. Returns
    {'places': [{'id', 'ja', 'en', 'kind', 'tag', 'shards': [{'file', 'ids'}]}],
     'entry_places': {entry id: [place ids]}, 'grouped': set of ids in a curated group,
     'problems': [str]}.
    """
    by_id = {e['id']: e for e in entries}
    problems = []
    adj = defaultdict(set)
    for e in entries:
        for x in e.get('cross_references') or []:
            t = x.get('target_id')
            if t in by_id and t != e['id'] and x.get('type') in XREF_CODES:
                adj[e['id']].add(t)
                adj[t].add(e['id'])

    places, entry_places, grouped = [], defaultdict(list), set()
    for g in groups:
        pid = f"{g['tag']}.{g['id']}"
        members = [m for m in g['members'] if m in by_id]
        missing = [m for m in g['members'] if m not in by_id]
        if missing:
            problems.append(f"group {pid}: {len(missing)} member(s) are not entries: {', '.join(missing[:5])}")
        if not members:
            continue
        name = tag_names.get(g['tag'], {})
        places.append({'id': pid, 'ja': g['ja'], 'en': g['en'], 'kind': 'group', 'tag': g['tag'],
                       'tag_en': name.get('en', g['tag']), 'shards': [{'file': pid, 'ids': members}]})
        for m in members:
            grouped.add(m)
            entry_places[m].append(pid)

    by_tag = defaultdict(list)
    for e in entries:
        if e['id'] in grouped:
            continue
        for t in entry_tags(e):
            by_tag[t].append(e['id'])
    for tag in sorted(by_tag):
        name = tag_names.get(tag)
        if not name:
            problems.append(f"tag '{tag}' has no name in explore/tags.json ({len(by_tag[tag])} entries left out)")
            continue
        shards = []
        for band, tiers in (('a', ('basic', 'core')), ('g', ('general',))):
            ids = sorted(i for i in by_tag[tag] if tier_of(by_id[i]) in tiers)
            for k, shard in enumerate(cluster(ids, adj)):
                shards.append({'file': f'{tag}-{band}{k:02d}', 'ids': shard})
        if not shards:
            continue
        places.append({'id': tag, 'ja': name['ja'], 'en': name['en'], 'kind': 'tag', 'tag': tag,
                       'tag_en': name['en'], 'shards': shards})
        for i in by_tag[tag]:
            entry_places[i].append(tag)
    return {'places': places, 'entry_places': entry_places, 'grouped': grouped, 'problems': problems, 'adj': adj}


def build_explore(entries: list, out_dir: Path, tag_names: dict = None, groups: list = None,
                  stores: dict = None, quiet: bool = False) -> dict:
    """Write <out_dir>/explore/. Returns counts for the build log."""
    tag_names = load_tag_names() if tag_names is None else tag_names
    groups = load_groups() if groups is None else groups
    by_id = {e['id']: e for e in entries}
    p = plan(entries, tag_names, groups)
    base = out_dir / 'explore'
    (base / 's').mkdir(parents=True, exist_ok=True)
    (base / 'w').mkdir(parents=True, exist_ok=True)
    for old in list((base / 's').glob('*.json')) + list((base / 'w').glob('*.json')):
        old.unlink()                                    # shard names change from build to build

    stores_seen, where = set(), defaultdict(list)
    index_places, n_shards, n_words = [], 0, 0
    for pi, place in enumerate(p['places']):
        shards = []
        for si, shard in enumerate(place['shards']):
            words = [word_record(by_id[i], by_id, p['entry_places'][i], stores_seen) for i in shard['ids']]
            counts = [0] * (len(TIERS) * len(CATS))
            for w in words:
                counts[w['t'] * len(CATS) + w['c']] += 1
                where[w['i']].append([pi, si])
            (base / 's' / f"{shard['file']}.json").write_text(
                json.dumps({'words': words}, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
            shards.append({'f': shard['file'], 'n': counts})
            n_shards += 1
            n_words += len(words)
        for si, near in enumerate(near_shards(place['shards'], p['adj'])):
            if near:
                shards[si]['near'] = near
        index_places.append({'id': place['id'], 'ja': place['ja'], 'en': place['en'], 'k': place['kind'][0],
                             'tag': place['tag'], 'ten': place['tag_en'], 'sh': shards})

    if stores is None:
        try:
            cfg = json.loads((ROOT / 'audio' / 'config.json').read_text(encoding='utf-8'))
            stores = {s['id']: s['base_url'] for s in cfg.get('stores', [])}
        except (OSError, ValueError, KeyError):
            stores = {}
    index = {'version': 1, 'tiers': list(TIERS), 'cats': list(CATS),
             'audio': {k: v for k, v in stores.items() if k in stores_seen}, 'places': index_places}
    (base / 'index.json').write_text(json.dumps(index, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')

    ranges = defaultdict(dict)
    for wid, refs in where.items():
        num = int(wid.split('_')[0])
        ranges[f'{num // 500 * 500:05d}'][wid] = refs
    for rng, table in ranges.items():
        (base / 'w' / f'{rng}.json').write_text(json.dumps(table, ensure_ascii=False, separators=(',', ':')),
                                                encoding='utf-8')
    result = {'places': len(index_places), 'groups': sum(1 for x in index_places if x['k'] == 'g'),
              'shards': n_shards, 'word_slots': n_words, 'entries': len(where), 'grouped': len(p['grouped']),
              'problems': p['problems']}
    if not quiet:
        for msg in p['problems']:
            print(f'  WARNING (explore): {msg}')
    return result


def load_entries(root: Path = ROOT) -> list:
    entries = []
    for f in sorted((root / 'entries').glob('**/*.json')):
        entries.append(json.loads(f.read_text(encoding='utf-8')))
    return entries


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--out', type=Path, help='site directory; writes <out>/explore/')
    ap.add_argument('--stats', action='store_true', help='print counts without writing files')
    args = ap.parse_args()
    entries = load_entries()
    if args.stats or not args.out:
        p = plan(entries, load_tag_names(), load_groups())
        sizes = [len(s['ids']) for pl in p['places'] for s in pl['shards'] if pl['kind'] == 'tag']
        print(f"{len(entries):,} entries; {len(p['places'])} places "
              f"({sum(1 for x in p['places'] if x['kind'] == 'group')} curated groups); "
              f"{len(sizes)} tag shards of {min(sizes) if sizes else 0}–{max(sizes) if sizes else 0} words; "
              f"{len(p['grouped']):,} entries in curated groups")
        for msg in p['problems']:
            print(f'WARNING: {msg}')
        return 0
    r = build_explore(entries, args.out)
    print(f"explore/: {r['places']} places ({r['groups']} curated groups), {r['shards']} shards, "
          f"{r['entries']:,} entries")
    return 0


if __name__ == '__main__':
    sys.exit(main())
