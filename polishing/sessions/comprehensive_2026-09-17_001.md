# Comprehensive Polish — 2026-09-17 #001

Routine run (mode: polish, reason: highest scheduler debt among eligible modes).

## Priority lane (polishing/priority/notes.txt lines 21494-21508, 15 entries)

Reviewed: 05347_nebokeru, 05352_kurukuru, 05365_pinpin, 05491_hocchikisu,
05566_kuraku, 05598_tenbin, 05645_mofumofu, 05700_kuku, 05718_ikanimo,
05722_hitasura, 05726_boubou, 05728_mareni, 05776_gokugoku, 05778_chibichibi,
05783_suyasuya.

- 05726_boubou: fixed a stale `noentry` link — ぼさぼさ now has an entry
  (29000_bosabosa) that check_stale_noentry.py hadn't caught yet; retargeted
  the link and fixed a cross-reference label missing its closing parenthesis
  ("roaring (fire, wind, water" → "...water)"). harvest_crossrefs then added
  the reciprocal contrast link on 29000_bosabosa itself.
  - This priority file was 15 days old (generated 2026-09-02, over the
    14-day threshold), so most of these entries had already been polished in
    the interim and needed no further change — regenerated the file with
    `make priorities` and reset the cursor to `line: 1` per the routine.
- 05778_chibichibi: removed a SIMILAR WORDS bullet that listed the entry's
  own headword ("ちびちび: sipping slowly, little by little").
- The rest (13 entries) were already correct, complete, and within the
  notes ceiling — no change needed.
- Candidates added: がぶがぶ (C23484, gulping greedily — mentioned in
  05776/05778's notes with no entry), 寝ぼすけ (C23485, sleepyhead — mentioned
  in 05347's notes with no entry). ぼさぼさ was already queued/created
  (29000_bosabosa); manage_candidates.py caught the duplicate.

## Frontier lane (params.start_id 07446, 20 entries)

Reviewed 07446-07465 (息を潜める through 心得) — a coherent idiom/vocabulary
batch created together on 2026-01-19. All were already well-formed:
correct glosses, complete cross-references, appropriate notes within the
character ceiling, no missing required sections. No edits needed.

- Candidate added: せせら笑う (C23486, to sneer — mentioned in 07449's notes
  with no entry).
- Advanced the frontier cursor to `next: 07466`.

## Self-check

Changed entries: 05726_boubou, 05778_chibichibi, 29000_bosabosa (the last
via the reciprocal cross-reference harvest_crossrefs added).

- `review_accuracy.py --ids 05726,05778,29000 --budget 0.40`: 0 issues on
  all three (~$0.0015).
- `review_links.py --ids 05726,05778,29000 --skip-decided --budget 0.10`:
  6 links judged, 0 flagged.
- Clean — no further action.

## Metrics

`pipeline/metrics_snapshot.py --mode polish --changed 3`: entries_changed=3,
flags_applied=6 (decisions.jsonl ledger since previous snapshot),
flags_rejected=5, flags_to_curator=0.

## Cursors

- `polishing/tasks/comprehensive/progress.txt`: next: 07466
- `polishing/tasks/comprehensive/priority-cursor.txt`: line: 1 (reset —
  priority file regenerated this run)
