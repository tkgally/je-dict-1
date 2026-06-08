#!/usr/bin/env python3
"""
Prune spurious conjugation tables and stray verb_class tags from non-verb,
non-i-adjective entries.

An entry is "spurious" when metadata.tags.pos contains NONE of
verb-godan / verb-ichidan / verb-suru / verb-kuru / verb-irregular / adjective-i
yet the entry has a `conjugation` field and/or a `verb_class` tag.

By default, entries whose POS includes `expression` are NOT pruned — they are
printed for manual review (some are mis-tagged single verbs that should be
re-tagged rather than stripped). Pass --include-expressions to prune them too
once you have reviewed the list.

Usage:
    python3 build/prune_nonverb_conjugations.py                      # dry run
    python3 build/prune_nonverb_conjugations.py --apply              # prune non-expressions
    python3 build/prune_nonverb_conjugations.py --apply --include-expressions
"""
import json
import glob
import argparse
from datetime import datetime, timezone

VERB_POS = {'verb-godan', 'verb-ichidan', 'verb-suru', 'verb-kuru', 'verb-irregular'}
KEEP_POS = VERB_POS | {'adjective-i'}


def is_spurious(d: dict) -> bool:
    tags = (d.get('metadata') or {}).get('tags', {})
    pos = tags.get('pos', []) or []
    if any(p in KEEP_POS for p in pos):
        return False
    return bool(d.get('conjugation')) or bool(tags.get('verb_class'))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='write changes')
    ap.add_argument('--include-expressions', action='store_true',
                    help='also prune entries whose POS includes "expression"')
    args = ap.parse_args()

    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    pruned, review = 0, 0

    for path in sorted(glob.glob('entries/*/*.json')):
        with open(path, encoding='utf-8') as f:
            d = json.load(f)
        if not is_spurious(d):
            continue
        pos = (d.get('metadata') or {}).get('tags', {}).get('pos', []) or []
        ctype = (d.get('conjugation') or {}).get('type')

        if 'expression' in pos and not args.include_expressions:
            print(f"REVIEW (expression, skipped): {d['id']}  pos={'|'.join(pos)}  type={ctype}")
            review += 1
            continue

        print(f"{'PRUNE' if args.apply else 'WOULD PRUNE'}: {d['id']}  "
              f"pos={'|'.join(pos)}  type={ctype}")
        if args.apply:
            d.pop('conjugation', None)
            d['metadata']['tags'].pop('verb_class', None)
            d['metadata']['modified'] = now
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
                f.write('\n')
            pruned += 1

    print(f"\n{'Pruned' if args.apply else 'Would prune'}: {pruned}")
    if review:
        print(f"Expression entries needing review (not touched): {review}")


if __name__ == '__main__':
    main()
