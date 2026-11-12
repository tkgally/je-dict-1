#!/usr/bin/env python3
"""Curated groups for the Explore page: write, check and count them.

The Explore page (explore.html) shows places, each a sign with words around it.
Every semantic tag is a place to begin with. `explore/groups/<tag>.json` then
replaces a tag, entry by entry, with finer curated groups of roughly 6 to 40
entries that belong together ("Rain", "Cooking methods"). An entry that is in a
curated group leaves the tag-level places; the rest stay where they were, so
the page is complete at every stage. build/explore_data.py turns all this into
the files the page reads, at site build.

    python3 build/explore_groups.py status                 # how much is grouped, tag by tag
    python3 build/explore_groups.py next                   # the tag to work on next
    python3 build/explore_groups.py worklist weather       # its ungrouped entries, related ones adjacent
    python3 build/explore_groups.py apply plan.txt         # write groups from a plan (format below)
    python3 build/explore_groups.py show weather           # the tag's groups, each member with its gloss
    python3 build/explore_groups.py validate               # the CI gate (also: make gate)

A plan is plain text. A line starting with == opens a group of the tag named
on the first line: its id (lower-case words joined by hyphens), its Japanese
name with furigana on every kanji, and its English name (28 characters at
most), separated by " | ". The lines under it are entry ids; anything after a
space is ignored, so worklist lines can be pasted whole. A group id that
already exists in the tag's file takes the new members (the names may then be
left out).

    tag: weather
    == rain | {雨|あめ} | Rain
    00583_ame
    02711_tsuyu   梅雨
    == wind | {風|かぜ} | Wind
    00585_kaze
    == (none)
    03635_moyou   模様: fits no weather group

Entries under "== (none)" are deliberately left at tag level: they fit no
group. They are recorded in the file's "leftover" list so that the worklist
does not offer them again; putting one in a group later takes it off the list.

Rules the gate enforces: the tag is a semantic tag; group ids are unique in
their file; names carry furigana and fit the sign; every member is an entry;
a group has 3 to 45 members (aim for 6 to 40); an entry is in at most three
groups. Members need not carry the file's tag: 傘 may sit in weather's "Rain".
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import explore_data as xd  # noqa: E402
from validate_tags import VALID_SEMANTIC  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = ROOT / 'entries'
GROUPS_DIR = xd.GROUPS_DIR
TAGS_FILE = xd.TAGS_FILE

ID_RE = re.compile(r'^\d{5}_[a-z0-9_]+$')
SLUG_RE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
EN_MAX = 28
GROUP_MIN, GROUP_MAX = 3, 45            # hard limits (the gate)
GROUP_AIM_MIN, GROUP_AIM_MAX = 6, 40    # what a curator should aim for (warnings)
MAX_GROUPS_PER_ENTRY = 3
TIER_ORDER = {'basic': 0, 'core': 1, 'general': 2}


def entry_exists(entry_id: str) -> bool:
    if not ID_RE.match(entry_id or ''):
        return False
    rng = int(entry_id[:5]) // 500 * 500
    return (ENTRIES / f'{rng:05d}' / f'{entry_id}.json').exists()


def name_problem(ja: str, en: str) -> str:
    """Why a place name is not usable, or ''."""
    if not ja or not ja.strip():
        return 'no Japanese name'
    if ja.count('{') != ja.count('}') or re.search(r'\{[^|{}]*\}', ja):
        return f'malformed furigana braces in {ja!r}'
    bare = xd.bare_kanji(ja)
    if bare:
        return f'kanji without furigana in {ja!r}: {"".join(bare)}'
    for _base, reading in xd.FURIGANA_RE.findall(ja):
        if not re.fullmatch(r'[ぁ-ゟー]+', reading):
            return f'furigana must be hiragana in {ja!r}'
    if not en or not en.strip():
        return 'no English name'
    if len(en) > EN_MAX:
        return f'English name longer than {EN_MAX} characters: {en!r}'
    return ''


def read_file(tag: str) -> dict:
    path = GROUPS_DIR / f'{tag}.json'
    if not path.exists():
        return {'tag': tag, 'groups': []}
    return json.loads(path.read_text(encoding='utf-8'))


def write_file(tag: str, data: dict, groups_dir: Path = None) -> Path:
    groups_dir = groups_dir or GROUPS_DIR
    groups_dir.mkdir(parents=True, exist_ok=True)
    path = groups_dir / f'{tag}.json'
    out = {'tag': tag, 'groups': [{'id': g['id'], 'ja': g['ja'], 'en': g['en'], 'members': list(g['members'])}
                                  for g in data.get('groups') or []]}
    if data.get('leftover'):
        out['leftover'] = list(data['leftover'])
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return path


def group_files(groups_dir: Path = None) -> list:
    groups_dir = groups_dir or GROUPS_DIR
    return sorted(groups_dir.glob('*.json')) if groups_dir.exists() else []


def grouped_ids(with_leftover: bool = False) -> set:
    """Every entry id that is a member of some curated group (reads only explore/groups/).
    With `with_leftover`, also the entries deliberately left at tag level: together
    they are the entries a curator has already dealt with."""
    ids = set()
    for f in group_files():
        try:
            data = json.loads(f.read_text(encoding='utf-8'))
        except (ValueError, OSError):
            continue
        for g in data.get('groups') or []:
            ids.update(g.get('members') or [])
        if with_leftover:
            ids.update(data.get('leftover') or [])
    return ids


# ---------------------------------------------------------------- validate

def validate(exists=entry_exists) -> tuple:
    """(errors, warnings) for explore/tags.json and explore/groups/*.json."""
    errors, warnings = [], []
    try:
        names = xd.load_tag_names()
    except (OSError, ValueError, KeyError) as e:
        return [f'explore/tags.json: cannot be read ({e})'], warnings
    for tag in sorted(set(VALID_SEMANTIC) - set(names)):
        errors.append(f"explore/tags.json: no name for the semantic tag '{tag}'")
    for tag in sorted(set(names) - set(VALID_SEMANTIC)):
        errors.append(f"explore/tags.json: '{tag}' is not a semantic tag")
    for tag, n in sorted(names.items()):
        prob = name_problem(n.get('ja', ''), n.get('en', ''))
        if prob:
            errors.append(f'explore/tags.json: {tag}: {prob}')

    membership, left_over = defaultdict(list), {}
    for f in group_files():
        rel = f'explore/groups/{f.name}'
        try:
            data = json.loads(f.read_text(encoding='utf-8'))
        except ValueError as e:
            errors.append(f'{rel}: invalid JSON ({e})')
            continue
        tag = data.get('tag')
        if tag != f.stem:
            errors.append(f"{rel}: \"tag\" is {tag!r}; it must match the file name")
        if f.stem not in VALID_SEMANTIC:
            errors.append(f"{rel}: '{f.stem}' is not a semantic tag")
        seen_ids, seen_en = set(), set()
        for g in data.get('groups') or []:
            gid = g.get('id', '')
            where = f'{rel}: group {gid!r}'
            if not SLUG_RE.match(gid):
                errors.append(f'{where}: the id must be lower-case words joined by hyphens')
            if gid in seen_ids:
                errors.append(f'{where}: the id is used twice in this file')
            seen_ids.add(gid)
            prob = name_problem(g.get('ja', ''), g.get('en', ''))
            if prob:
                errors.append(f'{where}: {prob}')
            if g.get('en') in seen_en:
                errors.append(f"{where}: the English name {g.get('en')!r} is used twice in this file")
            seen_en.add(g.get('en'))
            members = g.get('members') or []
            if len(set(members)) != len(members):
                errors.append(f'{where}: a member is listed twice')
            if not GROUP_MIN <= len(members) <= GROUP_MAX:
                errors.append(f'{where}: {len(members)} members; a group has {GROUP_MIN} to {GROUP_MAX}')
            elif not GROUP_AIM_MIN <= len(members) <= GROUP_AIM_MAX:
                warnings.append(f'{where}: {len(members)} members (aim for {GROUP_AIM_MIN} to {GROUP_AIM_MAX})')
            missing = [m for m in members if not exists(m)]
            if missing:
                errors.append(f"{where}: not entries: {', '.join(missing[:8])}"
                              + (f' and {len(missing) - 8} more' if len(missing) > 8 else ''))
            for m in set(members):
                membership[m].append(f'{f.stem}.{gid}')
        leftover = data.get('leftover') or []
        if len(set(leftover)) != len(leftover):
            errors.append(f'{rel}: leftover: an entry is listed twice')
        missing = [m for m in leftover if not exists(m)]
        if missing:
            errors.append(f"{rel}: leftover: not entries: {', '.join(missing[:8])}")
        left_over[f.stem] = set(leftover)
    for tag, ids in sorted(left_over.items()):
        both = sorted(i for i in ids if i in membership)
        if both:
            errors.append(f"explore/groups/{tag}.json: leftover entries that are in a group: {', '.join(both[:8])}")
    for m, where in sorted(membership.items()):
        if len(where) > MAX_GROUPS_PER_ENTRY:
            errors.append(f"{m} is in {len(where)} groups ({', '.join(where)}); at most {MAX_GROUPS_PER_ENTRY}")
    return errors, warnings


# ---------------------------------------------------------------- counting

def survey(entries: list) -> dict:
    """Per tag: entries carrying it, how many still wait for a curator (in no curated group
    and not marked leftover), and how many of those are basic or core."""
    done = grouped_ids(with_leftover=True)
    in_group = grouped_ids()
    tags = defaultdict(lambda: {'entries': 0, 'ungrouped': 0, 'ungrouped_basic_core': 0})
    ungrouped = 0
    for e in entries:
        free = e['id'] not in done
        ungrouped += free
        for t in xd.entry_tags(e):
            row = tags[t]
            row['entries'] += 1
            if free:
                row['ungrouped'] += 1
                row['ungrouped_basic_core'] += xd.tier_of(e) != 'general'
    files = {f.stem: len(json.loads(f.read_text(encoding='utf-8')).get('groups') or []) for f in group_files()}
    for t, n in files.items():
        tags[t]['groups'] = n
    return {'entries': len(entries), 'grouped': sum(1 for e in entries if e['id'] in in_group),
            'leftover': sum(1 for e in entries if e['id'] in done and e['id'] not in in_group), 'ungrouped': ungrouped,
            'groups': sum(files.values()), 'tags': dict(tags)}


def next_tags(s: dict) -> list:
    """Tags still holding ungrouped entries, the one to work on first.

    A tag whose file is already begun comes first (finish what is started);
    then the tags with the most basic and core entries left, since those are
    the words learners meet first; then by size."""
    rows = [(t, r) for t, r in s['tags'].items() if r['ungrouped']]
    rows.sort(key=lambda kv: (0 if kv[1].get('groups') else 1, -kv[1]['ungrouped_basic_core'],
                              -kv[1]['ungrouped'], kv[0]))
    return rows


def worklist(entries: list, tag: str, limit: int = 0) -> list:
    """Entries of a tag that still wait for a curator, basic and core first,
    cross-referenced entries next to each other."""
    done = grouped_ids(with_leftover=True)
    by_id = {e['id']: e for e in entries}
    mine = [e for e in entries if e['id'] not in done and tag in xd.entry_tags(e)]
    adj = defaultdict(set)
    for e in mine:
        for x in e.get('cross_references') or []:
            t = x.get('target_id')
            if t in by_id and t != e['id']:
                adj[e['id']].add(t)
                adj[t].add(e['id'])
    rows = []
    for band in (('basic', 'core'), ('general',)):
        ids = sorted(e['id'] for e in mine if xd.tier_of(e) in band)
        for shard in xd.cluster(ids, adj, target=40, min_cluster=2):
            rows.extend(shard)
    if limit:
        rows = rows[:limit]
    out = []
    for i in rows:
        e = by_id[i]
        refs = [xd.plain(x.get('headword', '')) for x in (e.get('cross_references') or [])[:4] if x.get('headword')]
        out.append('\t'.join([i, xd.plain(e.get('headword', '')), e.get('reading', ''), xd.short_gloss(e.get('gloss', ''), 40),
                              xd.tier_of(e), e.get('part_of_speech', ''), '→ ' + '、'.join(refs) if refs else '']))
    return out


# ---------------------------------------------------------------- apply

def parse_plan(text: str) -> tuple:
    """(tag, [{'id', 'ja', 'en', 'members'}]) from a plan (see the module docstring)."""
    tag, groups, cur = None, [], None
    for n, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        if line.lower().startswith('tag:'):
            tag = line.split(':', 1)[1].strip()
            continue
        if line.startswith('==') and line[2:].strip().lower() in ('(none)', 'none', '-'):
            cur = {'id': None, 'ja': '', 'en': '', 'members': []}          # deliberately left at tag level
            groups.append(cur)
            continue
        if line.startswith('=='):
            parts = [p.strip() for p in line[2:].split(' | ')]
            cur = {'id': parts[0], 'ja': parts[1] if len(parts) > 1 else '', 'en': parts[2] if len(parts) > 2 else '',
                   'members': []}
            groups.append(cur)
            continue
        if cur is None:
            raise ValueError(f'line {n}: an entry id before any "==" group line')
        entry_id = line.split()[0]
        if not ID_RE.match(entry_id):
            raise ValueError(f'line {n}: {entry_id!r} is not an entry id')
        if entry_id not in cur['members']:
            cur['members'].append(entry_id)
    if not tag:
        raise ValueError('the plan needs a first line "tag: <semantic tag>"')
    return tag, groups


def apply_plan(text: str, dry_run: bool = False) -> dict:
    tag, planned = parse_plan(text)
    data = read_file(tag)
    by_id = {g['id']: g for g in data['groups']}
    added = new_groups = 0
    leftover = list(data.get('leftover') or [])
    for p in planned:
        if p['id'] is None:
            leftover.extend(m for m in p['members'] if m not in leftover)
            continue
        g = by_id.get(p['id'])
        if g is None:
            if not p['ja'] or not p['en']:
                raise ValueError(f"new group {p['id']!r} needs a Japanese and an English name")
            g = {'id': p['id'], 'ja': p['ja'], 'en': p['en'], 'members': []}
            data['groups'].append(g)
            by_id[g['id']] = g
            new_groups += 1
        else:
            g['ja'] = p['ja'] or g['ja']
            g['en'] = p['en'] or g['en']
        for m in p['members']:
            if m not in g['members']:
                g['members'].append(m)
                added += 1
    members = {m for g in data['groups'] for m in g['members']}
    data['leftover'] = [m for m in leftover if m not in members]      # an entry that found a group is no longer left over
    if not dry_run:
        write_file(tag, data)
    return {'tag': tag, 'new_groups': new_groups, 'groups': len(data['groups']), 'members_added': added,
            'leftover': len(data['leftover'])}


# ---------------------------------------------------------------- retire / rename (called by build/retire_entry.py)

def replace_member(old: str, new: str, dry_run: bool = False, groups_dir: Path = None) -> list:
    """Point group memberships of `old` at `new` (dropping `old` where `new` is already a member).
    Returns the files changed, as explore/groups/<file>."""
    changed = []
    for f in group_files(groups_dir):
        raw = f.read_text(encoding='utf-8')
        if f'"{old}"' not in raw:
            continue
        data = json.loads(raw)
        touched = False
        for g in data.get('groups') or []:
            members = g.get('members') or []
            if old not in members:
                continue
            out = []
            for m in members:
                m = new if m == old else m
                if m not in out:
                    out.append(m)
            g['members'] = out
            touched = True
        if old in (data.get('leftover') or []):
            data['leftover'] = [m for m in dict.fromkeys(new if m == old else m for m in data['leftover'])]
            touched = True
        if touched:                                   # an entry merged into one that is in a group is no longer left over
            members = {m for g in data.get('groups') or [] for m in g.get('members') or []}
            data['leftover'] = [m for m in data.get('leftover') or [] if m not in members]
        if not touched:
            continue
        changed.append(f'explore/groups/{f.name}')
        if not dry_run:
            write_file(f.stem, data, groups_dir)
    return changed


# ---------------------------------------------------------------- CLI

def main() -> int:
    ap = argparse.ArgumentParser(description='Curated groups for the Explore page.',
                                 epilog='See the module docstring for the plan format.')
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('validate', help='check explore/tags.json and explore/groups/ (CI gate)')
    p = sub.add_parser('status', help='how much is grouped')
    p.add_argument('--json', action='store_true')
    sub.add_parser('next', help='the tag to work on next')
    p = sub.add_parser('worklist', help="a tag's ungrouped entries")
    p.add_argument('tag')
    p.add_argument('--limit', type=int, default=0, help='at most this many entries')
    p = sub.add_parser('show', help="a tag's groups with each member's headword and gloss")
    p.add_argument('tag')
    p = sub.add_parser('apply', help='write groups from a plan file')
    p.add_argument('plan', type=Path)
    p.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    if args.cmd == 'validate':
        errors, warnings = validate()
        for w in warnings:
            print(f'warning: {w}')
        for e in errors:
            print(f'ERROR: {e}')
        n = sum(len(json.loads(f.read_text(encoding="utf-8")).get("groups") or []) for f in group_files()) if not errors else 0
        print(f'explore: {len(errors)} error(s), {len(warnings)} warning(s)'
              + (f'; {len(group_files())} group file(s), {n} group(s)' if not errors else ''))
        return 1 if errors else 0

    if args.cmd == 'apply':
        try:
            r = apply_plan(args.plan.read_text(encoding='utf-8'), dry_run=args.dry_run)
        except ValueError as e:
            print(f'error: {e}', file=sys.stderr)
            return 2
        print(f"{r['tag']}: {r['members_added']} membership(s) added, {r['new_groups']} new group(s), "
              f"{r['groups']} group(s) in the file, {r['leftover']} left at tag level" + (' (dry run, nothing written)' if args.dry_run else ''))
        return 0

    entries = xd.load_entries()
    if args.cmd == 'status':
        s = survey(entries)
        if args.json:
            print(json.dumps(s, ensure_ascii=False, indent=2))
            return 0
        print(f"{s['entries']:,} entries: {s['grouped']:,} in {s['groups']} curated group(s), "
              f"{s['leftover']:,} deliberately left at tag level, {s['ungrouped']:,} still to do")
        print(f"{'tag':<20}{'entries':>9}{'ungrouped':>11}{'basic+core':>12}{'groups':>8}")
        for t, r in sorted(s['tags'].items(), key=lambda kv: -kv[1]['ungrouped']):
            print(f"{t:<20}{r['entries']:>9,}{r['ungrouped']:>11,}{r['ungrouped_basic_core']:>12,}{r.get('groups', 0):>8}")
        return 0
    if args.cmd == 'next':
        rows = next_tags(survey(entries))
        if not rows:
            print('Every entry is in a curated group.')
            return 0
        for t, r in rows[:8]:
            print(f"{t}\t{r['ungrouped']} ungrouped ({r['ungrouped_basic_core']} basic or core)"
                  + (f"\t{r['groups']} group(s) so far" if r.get('groups') else ''))
        return 0
    if args.cmd == 'show':
        by_id = {e['id']: e for e in entries}
        for g in read_file(args.tag)['groups']:
            print(f"== {g['id']} | {g['ja']} | {g['en']}   ({len(g['members'])})")
            for m in g['members']:
                e = by_id.get(m)
                print(f"   {m}\t{xd.plain(e.get('headword', '')) if e else '(not an entry)'}\t"
                      f"{xd.short_gloss(e.get('gloss', ''), 40) if e else ''}\t{xd.tier_of(e) if e else ''}")
        return 0
    if args.cmd == 'worklist':
        if args.tag not in VALID_SEMANTIC:
            print(f"error: '{args.tag}' is not a semantic tag", file=sys.stderr)
            return 2
        data = read_file(args.tag)
        if data['groups']:
            print(f"# groups already in explore/groups/{args.tag}.json:")
            for g in data['groups']:
                print(f"#   {g['id']} | {g['ja']} | {g['en']}   ({len(g['members'])})")
        for line in worklist(entries, args.tag, args.limit):
            print(line)
        return 0
    return 2


if __name__ == '__main__':
    sys.exit(main())
