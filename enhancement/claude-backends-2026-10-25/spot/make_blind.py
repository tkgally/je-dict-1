"""Stratified blind sample for a hand check: issues found only by sol, only by opus-tuned, by both."""
import json, random, sys
sys.path.insert(0, '.'); sys.path.insert(0, '../../build')
import review_accuracy as ra
items = {json.loads(l)['id']: json.loads(l) for l in open('sets/accuracy.jsonl')}
J = {}
for l in open('results/judge/gemini-4-argon.jsonl'):   # the "both" view uses argon's issue groups
    r = json.loads(l)
    for f in r['flags']:
        J[(r['id'], f['key'])] = f
s = json.load(open('accuracy_summary.json'))['reviewers']
found = lambda lab: set(s[lab]['both']['warn']['found'])
SOL = found('gpt-6.1-sol') | found('sol-hist'); OP = found('opus-tuned')
groups = {'S': sorted(SOL - OP), 'O': sorted(OP - SOL), 'B': sorted(SOL & OP)}
random.seed(7)
pick = ([('S', x) for x in random.sample(groups['S'], 12)] + [('O', x) for x in random.sample(groups['O'], 12)]
        + [('B', x) for x in random.sample(groups['B'], 6)])
random.shuffle(pick)
key = []
for n, (g, iss) in enumerate(pick, 1):
    eid, letter = iss.split(':', 1)
    fl = [f for (e, k), f in J.items() if e == eid and f['issue'] == letter and f['verdict'] == 'valid']
    want = {'S': ('gpt-6.1-sol', 'sol-hist'), 'O': ('opus-tuned',), 'B': ('gpt-6.1-sol', 'sol-hist')}[g]
    f = next((f for f in fl if set(f['reviewers']) & set(want)), fl[0])
    p = ra.entry_payload(items[eid]['entry'])
    loc = f['flag'].get('location', '')
    print(f"#{n} {eid} {p['headword']} ({p['reading']}) gloss={p['gloss']} tags={p['semantic_tags']} {p['formality']}/{p['politeness']}")
    if loc.startswith('examples['):
        i = int(loc[9:loc.index(']')])
        if i < len(p['examples']):
            print(f"   EX: {p['examples'][i]['japanese']} / {p['examples'][i]['english']}")
    for k in ('location', 'concern', 'quote', 'suggestion'):
        if f['flag'].get(k):
            print(f"   {k}: {f['flag'][k][:400]}")
    key.append({'n': n, 'group': g, 'issue': iss, 'reviewers': f['reviewers']})
json.dump(key, open('spot/key.json', 'w'), indent=1)
