/* Explore page (explore.html): the dictionary as a 3D word cloud.

   Places (semantic groups) and their words come from explore/index.json and
   explore/s/<shard>.json, written by build/explore_data.py at site build; the
   lines between words are the entries' own cross-references. Each visit picks
   places and words at random, so no two arrangements are alike.
   No dependencies: one canvas, drawn with the 2D context. */
(() => {
'use strict';
const BASE = 'explore/';

/* ------------------------------------------------------------------ helpers */
const $ = id => document.getElementById(id);
const TAU = Math.PI * 2;
const clamp = (v, a, b) => v < a ? a : v > b ? b : v;
const lerp = (a, b, t) => a + (b - a) * t;
const smooth = (a, b, v) => { const t = clamp((v - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); };
function mulberry32(a) { return function () { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
function shuffle(a, rng) { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rng() * (i + 1)); const t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
function hsl2rgb(h, s, l) { s /= 100; l /= 100; const k = n => (n + h / 30) % 12, a = s * Math.min(l, 1 - l); const f = n => l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1))); return [f(0) * 255, f(8) * 255, f(4) * 255]; }
const rgb = c => `rgb(${c[0] | 0},${c[1] | 0},${c[2] | 0})`;
const mix = (a, b, t) => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t];
const hex = h => [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)];

function segs(s) { const out = []; const re = /\{([^|{}]+)\|([^{}]+)\}/g; let i = 0, m; while ((m = re.exec(s))) { if (m.index > i) out.push({ b: s.slice(i, m.index) }); out.push({ b: m[1], r: m[2] }); i = re.lastIndex; } if (i < s.length) out.push({ b: s.slice(i) }); return out; }
const plain = s => segs(s).map(g => g.b).join('');
function rubyInto(el, s) { for (const g of segs(s)) { if (g.r) { const r = document.createElement('ruby'); r.textContent = g.b; const rt = document.createElement('rt'); rt.textContent = g.r; r.appendChild(rt); el.appendChild(r); } else el.appendChild(document.createTextNode(g.b)); } return el; }
function el(tag, cls, text) { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
function shortGloss(w) { let g = w.g.split(';')[0].trim(); if (g.length > 24 && g.includes(',')) g = g.split(',')[0].trim(); if (g.length > 30) g = g.slice(0, 28).trim() + '…'; return g; }

/* ------------------------------------------------------------------ data */
let INDEX = null;                    // explore/index.json
const PLACES = new Map();            // place id → its record in the index
const WORDS = new Map();             // entry id → word, for every word fetched so far
const shardCache = new Map();        // shard file → promise of its words
const TIER_NAMES = ['basic', 'core', 'general'], CAT_NAMES = ['noun', 'verb', 'adj', 'adv', 'expr'];
const REL = { c: 'compare', r: 'related', s: 'similar', a: 'opposite', p: 'pair', k: 'keigo', h: 'same sound' };
const fetchJSON = url => fetch(url).then(r => { if (!r.ok) throw new Error(url + ': HTTP ' + r.status); return r.json(); });
const rangeOf = id => String(Math.floor(parseInt(id, 10) / 500) * 500).padStart(5, '0');
const entryUrl = id => `entries/${rangeOf(id)}/${id}.html`;
function adoptWord(w) {
  let o = WORDS.get(w.i);
  if (!o) {
    o = { id: w.i, hw: w.h, r: w.r, g: w.g, t: TIER_NAMES[w.t], cat: CAT_NAMES[w.c], pos: w.p, grp: w.pl,
      x: w.x.map(x => ({ id: x[0], type: x[1], hw: x[2], g: x[3] })),
      ex: w.e.map(e => ({ ja: e.j, en: e.e, a: e.a && INDEX.audio[e.a[0]] ? INDEX.audio[e.a[0]] + e.a[1] : null })) };
    WORDS.set(o.id, o);
  }
  return o;
}
function loadShard(file) {
  let p = shardCache.get(file);
  if (!p) { p = fetchJSON(`${BASE}s/${file}.json`).then(d => d.words.map(adoptWord)); shardCache.set(file, p); p.catch(() => shardCache.delete(file)); }
  return p;
}
const TIERS = [['basic', 'Basic'], ['core', 'Core'], ['general', 'General']];
const CATS = [['noun', 'Nouns'], ['verb', 'Verbs'], ['adj', 'Adjectives'], ['adv', 'Adverbs'], ['expr', 'Expressions']];
const HUES = [212, 352, 150, 276, 34, 186, 322, 96, 242, 14, 56, 128];
const TIER_SIZE = { basic: 1.22, core: 1.0, general: 0.86 };

/* ------------------------------------------------------------------ state */
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
const S = {
  world: 'sky', time: 'day', labels: 'furi',
  tiers: { basic: true, core: true, general: true }, cats: { noun: true, verb: true, adj: true, adv: true, expr: true },
  nGroups: 8, perGroup: 12, links: 'all', speed: 1, tour: !reduceMotion,
  seed: (Math.random() * 9000 + 1000) | 0,
};
const PREF_VALUES = { world: ['sky', 'mountains', 'city'], time: ['day', 'night'], labels: ['ja', 'furi', 'en'], links: ['off', 'sel', 'all'] };
try { const p = JSON.parse(localStorage.getItem('explore-prefs') || '{}'); for (const k in PREF_VALUES) if (PREF_VALUES[k].includes(p[k])) S[k] = p[k]; } catch (e) {}
function savePrefs() { try { localStorage.setItem('explore-prefs', JSON.stringify({ world: S.world, time: S.time, labels: S.labels, links: S.links })); } catch (e) {} }

let arr = null;     // arrangement: which groups and words are shown
let scene = null;   // 3D layout of the arrangement in the current world
let selected = null, hovered = null, activeGroup = null;

/* ------------------------------------------------------------------ arrangement (what is shown) */
// How many words of a shard pass the level and word-type filters. band 0: basic and core, 1: general, undefined: all.
function eligible(sh, band) {
  let n = 0;
  for (let t = 0; t < 3; t++) {
    if (!S.tiers[TIER_NAMES[t]] || (band === 0 && t === 2) || (band === 1 && t < 2)) continue;
    for (let c = 0; c < 5; c++) if (S.cats[CAT_NAMES[c]]) n += sh.n[t * 5 + c];
  }
  return n;
}
function weightedPick(items, weight, rng) {
  let total = 0; for (const it of items) total += weight(it);
  let r = rng() * total;
  for (const it of items) { r -= weight(it); if (r <= 0) return it; }
  return items[items.length - 1];
}
// Pick the places, fetch enough of their words, and choose which words to show.
// focus = { id, pi, si }: an entry that must be in the cloud (explore.html?w=<id>).
async function chooseArrangement(focus) {
  const rng = mulberry32(S.seed * 7919 + 13), per = S.perGroup;
  // 1. topics: one place per semantic tag, bigger tags a little more often
  const byTag = new Map();
  for (const p of INDEX.places) {
    const n = p.sh.reduce((s, sh) => s + eligible(sh), 0);
    if (n < 4) continue;
    if (!byTag.has(p.tag)) byTag.set(p.tag, { list: [], n: 0 });
    const t = byTag.get(p.tag); t.list.push({ p, n }); t.n += n;
  }
  const chosen = [];
  const focusPlace = focus ? INDEX.places[focus.pi] : null;
  if (focusPlace) { chosen.push(focusPlace); byTag.delete(focusPlace.tag); }
  let pool = [...byTag.values()];
  while (chosen.length < S.nGroups && pool.length) {
    const t = weightedPick(pool, x => Math.sqrt(Math.min(x.n, 400)), rng);
    pool = pool.filter(x => x !== t);
    chosen.push(weightedPick(t.list, x => Math.sqrt(x.n), rng).p);
  }
  // 2. shards: about half familiar words (basic, core) and half new ones (general) when all levels are on
  const wantA = S.tiers.basic || S.tiers.core ? (S.tiers.general ? Math.ceil(per / 2) : per) : 0;
  const plans = chosen.map(p => {
    const files = [], order = shuffle(p.sh.slice(), rng);
    if (p === focusPlace) files.push(p.sh[focus.si]);
    let a = files.reduce((s, sh) => s + eligible(sh, 0), 0), g = files.reduce((s, sh) => s + eligible(sh, 1), 0), na = 0, ng = 0;
    // prefer a shard that is cross-referenced from one already chosen, so familiar words sit beside related new ones
    const next = band => {
      const ok = sh => !files.includes(sh) && eligible(sh, band) > 0;
      const near = []; for (const f of files) for (const i of f.near || []) if (ok(p.sh[i]) && !near.includes(p.sh[i])) near.push(p.sh[i]);
      return near.length ? near[(rng() * Math.min(near.length, 2)) | 0] : order.find(ok);
    };
    for (let sh; a < wantA * 1.5 && na < 3 && (sh = next(0)); na++) { files.push(sh); a += eligible(sh, 0); g += eligible(sh, 1); }
    const wantG = S.tiers.general ? per - Math.min(wantA, a) : 0;
    for (let sh; g < wantG * 1.5 && ng < 3 && (sh = next(1)); ng++) { files.push(sh); a += eligible(sh, 0); g += eligible(sh, 1); }
    return { p, files };
  });
  const loaded = await Promise.all(plans.map(pl => Promise.all(pl.files.map(sh => loadShard(sh.f)))));
  // 3. words: grow each place along the cross-references, so that what is shown is connected
  const hues = shuffle(HUES.slice(), rng), groups = [], place = new Map();
  plans.forEach((pl, k) => {
    const cand = new Map();
    for (const list of loaded[k]) for (const w of list) if (!place.has(w.id) && ((S.tiers[w.t] && S.cats[w.cat]) || (focus && w.id === focus.id))) cand.set(w.id, w);
    const all = shuffle([...cand.values()], rng);
    const A = all.filter(w => w.t !== 'general'), G_ = all.filter(w => w.t === 'general');
    let qa = Math.min(A.length, wantA), qg = Math.min(G_.length, per - qa); qa = Math.min(A.length, per - qg);
    const take = [], taken = new Set();
    const add = w => { take.push(w); taken.add(w.id); if (w.t === 'general') qg--; else qa--; };
    const room = w => !taken.has(w.id) && (w.t === 'general' ? qg > 0 : qa > 0);
    if (focus && cand.has(focus.id)) add(cand.get(focus.id));
    while (qa + qg > 0) {
      let next = null;
      if (take.length && rng() < 0.8) {
        const near = [];
        for (const w of take) for (const x of w.x) { const o = cand.get(x.id); if (o && room(o)) near.push(o); }
        if (near.length) next = near[(rng() * near.length) | 0];
      }
      if (!next) { const from = (qa >= qg ? A : G_).find(room) || A.find(room) || G_.find(room); if (!from) break; next = from; }
      add(next);
    }
    if (take.length < 3) return;
    const Gp = { g: pl.p, hue: hues[groups.length % hues.length], words: take, i: groups.length };
    groups.push(Gp);
    for (const w of take) place.set(w.id, Gp);
  });
  const links = [], seen = new Set();
  for (const [id] of place) for (const x of WORDS.get(id).x) {
    if (!place.has(x.id)) continue;
    const key = id < x.id ? id + '|' + x.id : x.id + '|' + id;
    if (!seen.has(key)) { seen.add(key); links.push([id, x.id, x.type]); }
  }
  return { groups, place, links };
}

/* ------------------------------------------------------------------ layout (where it is shown) */
function spread(n, rng, minSep) {
  const R = minSep * 0.6 * Math.sqrt(n), pts = [];
  for (let i = 0; i < n; i++) { const a = rng() * TAU, r = Math.sqrt(rng()) * R; pts.push({ x: Math.cos(a) * r, z: Math.sin(a) * r }); }
  for (let it = 0; it < 160; it++) {
    for (let i = 0; i < n; i++) for (let j = i + 1; j < n; j++) {
      let dx = pts[j].x - pts[i].x, dz = pts[j].z - pts[i].z, d = Math.hypot(dx, dz);
      if (d < 1e-3) { dx = 1; dz = 0; d = 1; }
      if (d < minSep) { const p = (minSep - d) / 2 / d; pts[i].x -= dx * p; pts[i].z -= dz * p; pts[j].x += dx * p; pts[j].z += dz * p; }
    }
    if (it < 130) for (const p of pts) { p.x *= 0.985; p.z *= 0.985; }
  }
  let mx = 0, mz = 0; for (const p of pts) { mx += p.x; mz += p.z; } for (const p of pts) { p.x -= mx / n; p.z -= mz / n; }
  return pts;
}
function makeNoise(seed) {
  const h = (x, z) => { let n = Math.imul(x, 374761393) + Math.imul(z, 668265263) + seed; n = Math.imul(n ^ n >>> 13, 1274126177); return ((n ^ n >>> 16) >>> 0) / 4294967296; };
  const v = (x, z) => { const xi = Math.floor(x), zi = Math.floor(z), fx = x - xi, fz = z - zi, ux = fx * fx * (3 - 2 * fx), uz = fz * fz * (3 - 2 * fz); return lerp(lerp(h(xi, zi), h(xi + 1, zi), ux), lerp(h(xi, zi + 1), h(xi + 1, zi + 1), ux), uz); };
  return (x, z) => v(x, z) * 0.6 + v(x * 2.1 + 9, z * 2.1 + 4) * 0.28 + v(x * 4.3 + 2, z * 4.3 + 7) * 0.12;
}

const PAL = {
  sky: {
    day:   { top: '#2c79d0', hor: '#bfe1fb', low: '#eaf5fd', fogS: 500, fogE: 2600, link: [28, 58, 110], puff: [255, 255, 255], puffA: 0.9 },
    night: { top: '#060a20', hor: '#2a3470', low: '#141b46', fogS: 500, fogE: 2600, link: [200, 214, 255], puff: [128, 142, 210], puffA: 0.5 },
  },
  mountains: {
    day:   { top: '#4f97dc', hor: '#d5e8f4', ground: '#3c78aa', fogS: 420, fogE: 2300, link: [255, 244, 190] },
    night: { top: '#060a1c', hor: '#27335a', ground: '#183672', fogS: 420, fogE: 2300, link: [255, 232, 170] },
  },
  city: {
    day:   { top: '#6aaee8', hor: '#e3edf5', ground: '#b4bac4', fogS: 420, fogE: 2300, link: [52, 64, 88], win: 'rgba(60,84,120,.38)' },
    night: { top: '#06081a', hor: '#40265a', ground: '#0e101e', fogS: 420, fogE: 2300, link: [255, 236, 190], win: 'rgba(255,212,128,.8)' },
  },
};
const pal = () => PAL[S.world][S.time];

function buildScene() {
  const rng = mulberry32(S.seed * 104729 + { sky: 1, mountains: 2, city: 3 }[S.world]);
  const P = pal(), night = S.time === 'night';
  const sc = { world: S.world, items: [], labels: new Map(), groups: arr.groups, links: [], height: null, terrain: null, minY: -1e9, R: 1000, stars: null };
  const n = arr.groups.length;
  const fog = hex(P.hor);

  if (S.world === 'sky') {
    const cs = spread(n, rng, 600);
    arr.groups.forEach((G, i) => {
      const c = G.words.length, r = 62 + 21 * Math.sqrt(c);
      G.c = { x: cs[i].x, y: (rng() - 0.5) * 300, z: cs[i].z }; G.radius = r;
      const pts = []; let minD = 54, tries = 0;
      while (pts.length < c) {
        const p = { x: (rng() * 2 - 1), y: (rng() * 2 - 1), z: (rng() * 2 - 1) };
        if (p.x * p.x + p.y * p.y + p.z * p.z > 1) continue;
        p.x *= r; p.y *= r * 0.55; p.z *= r;
        if (pts.every(q => Math.hypot(q.x - p.x, q.y - p.y, q.z - p.z) > minD)) pts.push(p);
        else if (++tries > 60) { tries = 0; minD *= 0.92; }
      }
      G.words.forEach((w, k) => addLabel(sc, w, G, G.c.x + pts[k].x, G.c.y + pts[k].y, G.c.z + pts[k].z, false, null));
      addSign(sc, G, G.c.x, G.c.y + r * 0.55 + 40, G.c.z, false, null);
      const np = 7 + (rng() * 4 | 0);
      for (let k = 0; k < np; k++) {
        const a = rng() * TAU, d = rng() * r * 1.05;
        sc.items.push({ k: 2, x: G.c.x + Math.cos(a) * d, y: G.c.y - r * 0.5 - 30 - rng() * 70, z: G.c.z + Math.sin(a) * d, r: 110 + rng() * 120, v: rng() * 3 | 0, a: 0.75 + rng() * 0.25, d: 0 });
      }
    });
    sc.R = Math.max(...arr.groups.map(G => Math.hypot(G.c.x, G.c.z))) + 500;
    for (let k = 0; k < 46; k++) { const a = rng() * TAU, d = Math.sqrt(rng()) * sc.R * 1.5; sc.items.push({ k: 2, x: Math.cos(a) * d, y: -260 - rng() * 320 + (rng() < 0.25 ? 700 : 0), z: Math.sin(a) * d, r: 130 + rng() * 220, v: rng() * 3 | 0, a: 0.55 + rng() * 0.3, d: 0 }); }
  }

  if (S.world === 'mountains') {
    const cs = spread(n, rng, 660), noise = makeNoise((rng() * 1e9) | 0);
    arr.groups.forEach((G, i) => { G.c = { x: cs[i].x, y: 0, z: cs[i].z }; G.peak = 175 + rng() * 135; G.sig = 150 + rng() * 45; G.radius = G.sig * 2.05; });
    const Rmax = Math.max(...arr.groups.map(G => Math.hypot(G.c.x, G.c.z)));
    const E = Rmax + 560; sc.R = E;
    const raw = (x, z) => {                       // height before the sea level cut: negative values are the sea bed
      let h = (noise(x / 260, z / 260) - 0.46) * 110;
      for (const G of arr.groups) { const dx = x - G.c.x, dz = z - G.c.z, q = (dx * dx + dz * dz) / (2 * G.sig * G.sig); if (q < 9) h += G.peak * Math.exp(-q) * (0.9 + 0.2 * noise(x / 70 + G.i, z / 70)); }
      return h - smooth(Rmax + 250, E, Math.hypot(x, z)) * 150;
    };
    const height = (x, z) => Math.max(0, raw(x, z));
    sc.height = height;
    const N = 64, cell = 2 * E / N, V = N + 1, SUB = 4, FN = N * SUB, FV = FN + 1, fcell = 2 * E / FN;
    // fine height field (four samples per mesh cell): raw height, slope, and a slow "patchiness" noise
    const fr = new Float32Array(FV * FV), gX = new Float32Array(FV * FV), gZ = new Float32Array(FV * FV), pn = new Float32Array(FV * FV);
    for (let j = 0; j < FV; j++) for (let i = 0; i < FV; i++) { const x = -E + i * fcell, z = -E + j * fcell; fr[j * FV + i] = raw(x, z); pn[j * FV + i] = noise(x / 150 + 40, z / 150 + 7); }
    const hc = (i, j) => Math.max(0, fr[clamp(j, 0, FN) * FV + clamp(i, 0, FN)]);
    for (let j = 0; j < FV; j++) for (let i = 0; i < FV; i++) { gX[j * FV + i] = (hc(i + 1, j) - hc(i - 1, j)) / (2 * fcell); gZ[j * FV + i] = (hc(i, j + 1) - hc(i, j - 1)) / (2 * fcell); }
    const hs = new Float32Array(V * V), vx = new Float32Array(V), col = new Uint8Array(N * N * 3), qc = new Float32Array(N * N * 3);
    for (let i = 0; i < V; i++) vx[i] = -E + i * cell;
    for (let j = 0; j < V; j++) for (let i = 0; i < V; i++) hs[j * V + i] = Math.max(0, fr[j * SUB * FV + i * SUB]);

    // ground texture: one image of the whole island, coloured by altitude, slope and noise, with the sun's shading baked in
    const TS = 1024, tex = document.createElement('canvas'); tex.width = tex.height = TS;
    const tctx = tex.getContext('2d'), img = tctx.createImageData(TS, TS), px = img.data;
    const Ll = Math.hypot(0.5, 0.62, 0.6), L0 = 0.5 / Ll, L1 = 0.62 / Ll, L2 = 0.6 / Ll;
    const upRow = new Float32Array(TS);
    for (let ty = 0, o = 0; ty < TS; ty++) {
      const fz = (ty + 0.5) / TS * FN, j = Math.min(FN - 1, fz | 0), v = fz - j, wz = -E + (ty + 0.5) / TS * 2 * E;
      let left = 0.5;
      for (let tx = 0; tx < TS; tx++, o += 4) {
        const fx = (tx + 0.5) / TS * FN, i = Math.min(FN - 1, fx | 0), u = fx - i, a = j * FV + i, wx = -E + (tx + 0.5) / TS * 2 * E;
        const w00 = (1 - u) * (1 - v), w10 = u * (1 - v), w01 = (1 - u) * v, w11 = u * v;
        const hr = fr[a] * w00 + fr[a + 1] * w10 + fr[a + FV] * w01 + fr[a + FV + 1] * w11;
        const n2 = pn[a] * w00 + pn[a + 1] * w10 + pn[a + FV] * w01 + pn[a + FV + 1] * w11;
        const n1 = noise(wx / 17, wz / 17);
        let g = Math.imul(tx * 374761393 + ty * 668265263, 1274126177); g = ((g ^ g >>> 15) >>> 0) / 4294967296;   // per-texel grain
        let r, gg, b;
        if (hr <= 0) {                               // sea: pale in the shallows, darker with depth, a line of surf at the shore
          const dp = -hr, t = smooth(0, 42, dp), f = 1 - smooth(0, 2.6, dp), wv = 0.97 + 0.06 * n1;
          r = (lerp(108, 60, t) * wv) * (1 - f * 0.6) + 236 * f * 0.6; gg = (lerp(188, 120, t) * wv) * (1 - f * 0.6) + 242 * f * 0.6; b = (lerp(198, 170, t) * wv) * (1 - f * 0.6) + 240 * f * 0.6;
        } else {
          const dx = gX[a] * w00 + gX[a + 1] * w10 + gX[a + FV] * w01 + gX[a + FV + 1] * w11, dz = gZ[a] * w00 + gZ[a + 1] * w10 + gZ[a + FV] * w01 + gZ[a + FV + 1] * w11;
          const alt = hr + (n2 - 0.5) * 46, slope = Math.hypot(dx, dz);
          const dry = smooth(0.62, 0.85, n1) * 0.5;                                       // grassland with drier patches
          r = lerp(lerp(150, 108, n2), 178, dry); gg = lerp(lerp(182, 156, n2), 170, dry); b = lerp(lerp(96, 80, n2), 108, dry);
          const fw = smooth(26, 58, alt) * (1 - smooth(150, 188, alt)), sp = 0.86 + 0.28 * g;   // forest, speckled like a canopy
          r = lerp(r, lerp(50, 76, n1) * sp, fw); gg = lerp(gg, lerp(96, 124, n1) * sp, fw); b = lerp(b, lerp(56, 70, n1) * sp, fw);
          const mw = smooth(150, 188, alt) * (1 - smooth(212, 244, alt));                  // alpine meadow above the tree line
          r = lerp(r, lerp(152, 128, n1), mw); gg = lerp(gg, lerp(160, 146, n1), mw); b = lerp(b, lerp(104, 92, n1), mw);
          const strata = 0.93 + 0.07 * Math.sin(hr * 0.42 + n2 * 9);                       // bare rock: high ground and steep faces
          const rk = Math.max(smooth(212, 244, alt), smooth(0.78, 1.2, slope + (n1 - 0.5) * 0.35) * smooth(6, 20, hr));
          r = lerp(r, lerp(142, 184, n1) * strata, rk); gg = lerp(gg, lerp(126, 170, n1) * strata, rk); b = lerp(b, lerp(104, 150, n1) * strata, rk);
          const sw = smooth(242, 262, alt + (n1 - 0.5) * 30) * (1 - smooth(1.05, 1.6, slope));   // snow, thin on steep faces
          r = lerp(r, 245, sw); gg = lerp(gg, 248, sw); b = lerp(b, 252, sw);
          const sd = 1 - smooth(3, 9, hr + (n1 - 0.5) * 4);                                 // beach
          r = lerp(r, 222, sd); gg = lerp(gg, 208, sd); b = lerp(b, 160, sd);
          const bump = (1.2 + 3.2 * rk) * (1 - 0.6 * sw), nx = -(dx + (n1 - left) * bump), nz = -(dz + (n1 - upRow[tx]) * bump);
          const sh = (0.6 + 0.62 * Math.max(0, (nx * L0 + L1 + nz * L2) / Math.hypot(nx, 1, nz))) * (0.96 + 0.08 * g);
          r *= sh; gg *= sh; b *= sh;
        }
        left = n1; upRow[tx] = n1;
        if (night) { r = r * 0.27 + 8; gg = gg * 0.33 + 14; b = b * 0.48 + 32; }
        px[o] = r > 255 ? 255 : r; px[o + 1] = gg > 255 ? 255 : gg; px[o + 2] = b > 255 ? 255 : b; px[o + 3] = 255;
      }
    }
    tctx.putImageData(img, 0, 0);
    const tc = TS / N;
    for (let j = 0; j < N; j++) for (let i = 0; i < N; i++) {      // each cell's average colour, for the hazy distance
      const q = j * N + i; let r = 0, g = 0, b = 0;
      for (let a = 0; a < 4; a++) for (let c = 0; c < 4; c++) { const o = (((j + (a + 0.5) / 4) * tc) | 0) * TS * 4 + (((i + (c + 0.5) / 4) * tc) | 0) * 4; r += px[o]; g += px[o + 1]; b += px[o + 2]; }
      col[q * 3] = r / 16; col[q * 3 + 1] = g / 16; col[q * 3 + 2] = b / 16;
      qc[q * 3] = vx[i] + cell / 2; qc[q * 3 + 1] = (hs[j * V + i] + hs[j * V + i + 1] + hs[(j + 1) * V + i] + hs[(j + 1) * V + i + 1]) / 4; qc[q * 3 + 2] = vx[j] + cell / 2;
    }
    let pat = null, mat = null; try { pat = ctx.createPattern(tex, 'no-repeat'); mat = new DOMMatrix(); pat.setTransform(mat); } catch (e) { pat = null; }
    sc.terrain = { N, V, cell, hs, vx, col, qc, pat, mat, tc, ds: cell / 96 * 512 / tc, cam: new Float32Array(V * V * 3), scr: new Float32Array(V * V * 2), code: new Uint8Array(V * V), items: Array.from({ length: N * N }, (_, q) => ({ k: 0, q, d: 0 })) };
    arr.groups.forEach(G => {
      const c = G.words.length, order = G.words.slice().sort((a, b) => ({ general: 0, core: 1, basic: 2 }[a.t] - { general: 0, core: 1, basic: 2 }[b.t]));
      const a0 = rng() * TAU;
      order.forEach((w, k) => {
        const rr = G.sig * (0.5 + 1.45 * (k + 0.5) / c), a = a0 + k * 2.39996 + (rng() - 0.5) * 0.4;
        const x = G.c.x + Math.cos(a) * rr, z = G.c.z + Math.sin(a) * rr, gy = height(x, z);
        addLabel(sc, w, G, x, gy + 17 + rng() * 9, z, true, gy);
      });
      const top = height(G.c.x, G.c.z); G.top = top;
      addSign(sc, G, G.c.x, top + 36, G.c.z, true, top);
    });
    sc.minY = 0;
  }

  if (S.world === 'city') {
    const cols = Math.ceil(Math.sqrt(n)), rows = Math.ceil(n / cols), pitch = 66;
    const ks = arr.groups.map(G => Math.max(4, Math.ceil(Math.sqrt(G.words.length * 1.7))));
    const P2 = Math.max(...ks) * pitch + 170;
    const cells = []; for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) cells.push([c, r]);
    shuffle(cells, rng);
    const litFace = night ? [0.78, 1.0, 0.62, 0.9, 1.18] : [0.84, 1.0, 0.72, 0.92, 1.1];
    const pick = a => a[(rng() * a.length) | 0];
    const WALLS = {
      office: [[196, 196, 190], [214, 204, 186], [178, 186, 194], [226, 224, 216]],
      brick: [[158, 96, 78], [142, 84, 70], [176, 120, 92]],
      ribbon: [[232, 228, 218], [220, 214, 200], [206, 214, 220]],
      glass: [[70, 88, 104], [54, 72, 92], [84, 100, 110]],
      fins: [[92, 92, 98], [120, 112, 104], [64, 70, 82]],
      house: [[236, 230, 214], [224, 214, 192], [122, 88, 60], [98, 72, 52]],
      shop: [[222, 212, 196], [200, 206, 210], [214, 196, 176]],
    };
    const TILES = [[70, 76, 88], [92, 66, 56], [60, 84, 82], [52, 56, 66]];
    const tone = c => night ? [c[0] * 0.16 + 10, c[1] * 0.16 + 11, c[2] * 0.2 + 22] : c;
    const faces = c => litFace.map(f => c.map(v => clamp(v * f, 0, 255)));
    const addB = (x, z, w, d, h, hue) => {
      let st = h < 50 ? pick(['house', 'house', 'hip', 'shop', 'brick']) : h < 92 ? pick(['ribbon', 'brick', 'office', 'shop', 'ribbon', 'office']) : pick(['office', 'glass', 'fins', 'setback', 'glass']);
      const kind = st === 'hip' ? 'house' : st === 'setback' ? pick(['glass', 'office']) : st;
      let wall = pick(WALLS[kind]);
      if (hue != null) wall = mix(wall, hsl2rgb(hue, 45, kind === 'glass' || kind === 'fins' ? 42 : 62), 0.3);       // a district keeps a tinge of its colour
      wall = tone(wall);
      let wallH = h, roof = 'flat', rh = 0, roofC = null, win, lit = 0.4, awn = null; const ups = [];
      if (kind === 'house') { w *= 0.86; d *= 0.86; rh = clamp(h * 0.36, 9, 17); wallH = h - rh; roof = st === 'hip' ? 'hip' : 'gable'; roofC = tone(pick(TILES)); const fl = wallH > 24 ? 2 : 1; win = { mode: 'grid', bay: 15, fh: (wallH - 3) / fl, ww: 0.36, wh: 0.4, base: 1, topm: 2 }; lit = 0.65; }
      else if (kind === 'shop') { win = { mode: 'grid', bay: 11, fh: 11.5, ww: 0.6, wh: 0.5, base: 13, shop: true }; awn = tone(hsl2rgb(hue != null ? hue : rng() * 360, 62, 48)); if (night) awn = awn.map(v => v * 2.2); lit = 0.5; }
      else if (kind === 'brick') { win = { mode: 'grid', bay: 10.5, fh: 12.5, ww: 0.42, wh: 0.6, base: 3 }; lit = 0.45; }
      else if (kind === 'office') { win = { mode: 'grid', bay: 9.5, fh: 12, ww: 0.62, wh: 0.56, base: 4 }; lit = 0.38; }
      else if (kind === 'ribbon') { win = { mode: 'ribbon', bay: 9, fh: 11, ww: 1, wh: 0.45, base: 3, m: 2.5 }; lit = 0.45; }
      else if (kind === 'glass') { win = { mode: 'grid', bay: 7.5, fh: 10.5, ww: 0.86, wh: 0.82, base: 2, topm: 2 }; lit = 0.3; }
      else { win = { mode: 'fins', bay: 8, ww: 0.46, base: 10, topm: 5, fh: 12 }; lit = 0.5; }
      const x0 = x - w / 2, x1 = x + w / 2, z0 = z - d / 2, z1 = z + d / 2, col = faces(wall);
      if (st === 'setback') { wallH = h * (0.5 + rng() * 0.15); const ix = w * 0.2, iz = d * 0.2; ups.push({ x0: x0 + ix, x1: x1 - ix, z0: z0 + iz, z1: z1 - iz, y0: wallH, y1: h, col, win: { ...win, base: 1 } }); }
      else if (roof === 'flat' && h > 40 && rng() < 0.6) { const tx = x + (rng() < 0.5 ? -1 : 1) * w * 0.24, tz = z + (rng() < 0.5 ? -1 : 1) * d * 0.24, ts = 4 + rng() * 2.5; ups.push({ x0: tx - ts, x1: tx + ts, z0: tz - ts, z1: tz + ts, y0: h, y1: h + 5 + rng() * 3, col: faces(wall.map(v => v * 0.82)), win: null }); }
      const glassy = kind === 'glass';
      const wB = night ? (glassy ? [20, 28, 50] : [13, 15, 29]) : (glassy ? [146, 192, 222] : kind === 'house' ? [70, 84, 100] : [78, 100, 128]);
      const wA = night ? pick(glassy || kind === 'office' ? [[255, 226, 160], [214, 232, 255], [255, 210, 128]] : [[255, 210, 128], [255, 222, 150]]) : mix(wB, [206, 228, 242], 0.42);
      const b = { k: 1, x, y: h * 0.5, z, d: 0, x0, x1, z0, z1, h: wallH, col, win, wA, wB, fracA: night ? lit : 0.24, awn, roof, rh, ridgeX: w >= d, ups, seed: (rng() * 1e9) | 0,
        roofCol: roofC ? [0.8, 1.05, 0.7, 0.95].map(f => roofC.map(v => clamp(v * f * (night ? 1.25 : 1), 0, 255))) : null };
      sc.items.push(b); return b;
    };
    arr.groups.forEach((G, i) => {
      const k = ks[i], span = k * pitch;
      G.c = { x: (cells[i][0] - (cols - 1) / 2) * P2, y: 0, z: (cells[i][1] - (rows - 1) / 2) * P2 }; G.radius = span * 0.62; G.span = span;
      const tint = hsl2rgb(G.hue, night ? 45 : 40, night ? 15 : 80);
      sc.items.push({ k: 6, x0: G.c.x - span / 2 - 18, x1: G.c.x + span / 2 + 18, z0: G.c.z - span / 2 - 18, z1: G.c.z + span / 2 + 18, col: tint, d: 1e12 });
      const lots = []; for (let a = 0; a < k; a++) for (let b = 0; b < k; b++) lots.push([a, b]);
      shuffle(lots, rng);
      lots.forEach((lot, li) => {
        const x = G.c.x + (lot[0] - (k - 1) / 2) * pitch, z = G.c.z + (lot[1] - (k - 1) / 2) * pitch;
        const w = G.words[li];
        if (w) {
          const hgt = w.t === 'basic' ? 22 + rng() * 26 : w.t === 'core' ? 48 + rng() * 40 : 90 + rng() * 60;
          addB(x, z, 36 + rng() * 12, 36 + rng() * 12, hgt, G.hue);
          addLabel(sc, w, G, x, hgt + 7, z, true, hgt);
        } else if (rng() < 0.55) {
          addB(x, z, 30 + rng() * 18, 30 + rng() * 18, 16 + rng() * rng() * 120, null);
        }
      });
      addSign(sc, G, G.c.x, 196, G.c.z, true, 0);
    });
    sc.R = Math.max(...arr.groups.map(G => Math.hypot(G.c.x, G.c.z))) + 700;
    sc.minY = 5;
  }

  // connections
  const K = 9;
  for (const [a, b, t] of arr.links) {
    const A = sc.labels.get(a), B = sc.labels.get(b); if (!A || !B) continue;
    const link = { a: A, b: B, type: t, cross: A.G !== B.G };
    const ay = A.cy, by = B.cy, dist = Math.hypot(B.x - A.x, by - ay, B.z - A.z);
    const pts = [];
    for (let i = 0; i <= K; i++) {
      const u = i / K, x = lerp(A.x, B.x, u), z = lerp(A.z, B.z, u); let y;
      if (S.world === 'mountains') y = Math.max(sc.height(x, z) + 3, (i === 0 || i === K) ? 0 : 0);
      else y = lerp(ay, by, u) + Math.sin(u * Math.PI) * (S.world === 'city' ? 26 + dist * 0.16 : dist * 0.13);
      pts.push([x, y, z]);
    }
    if (S.world === 'mountains') { pts[0][1] = A.ground + 3; pts[K][1] = B.ground + 3; }
    for (let i = 0; i < K; i++) sc.items.push({ k: 5, p: pts[i], q: pts[i + 1], x: (pts[i][0] + pts[i + 1][0]) / 2, y: (pts[i][1] + pts[i + 1][1]) / 2, z: (pts[i][2] + pts[i + 1][2]) / 2, link, mid: i === (K >> 1), first: i === 0, last: i === K - 1, d: 0 });
    sc.links.push(link);
  }
  if (night) { sc.stars = []; const r2 = mulberry32(S.seed + 5); for (let i = 0; i < 170; i++) { const a = r2() * TAU, e = Math.asin(r2() * 0.98 + 0.02); sc.stars.push([Math.cos(e) * Math.sin(a), Math.sin(e), Math.cos(e) * Math.cos(a), 0.4 + r2() * 0.6]); } }
  sc.fog = fog;
  return sc;
}
function addLabel(sc, w, G, x, y, z, bottom, ground) {
  const it = { k: 3, w, G, x, y, z, bottom, ground, size: (S.world === 'sky' ? 13.5 : 12) * TIER_SIZE[w.t], cy: y, d: 0 };
  if (bottom) it.cy = y + it.size * 0.9;
  sc.items.push(it); sc.labels.set(w.id, it); return it;
}
function addSign(sc, G, x, y, z, bottom, ground) { const it = { k: 4, G, x, y, z, bottom, ground, size: 22, cy: y + 18, d: 0 }; G.sign = it; sc.items.push(it); }

/* ------------------------------------------------------------------ sprites */
const JP = '"Hiragino Sans","Hiragino Kaku Gothic ProN","Noto Sans JP","Noto Sans CJK JP","Yu Gothic",Meiryo,sans-serif';
const UI = '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
const mctx = document.createElement('canvas').getContext('2d');
const sprites = new Map(); let hiKeys = [];
function clearSprites() { sprites.clear(); hiKeys = []; }
function labelStyle(hue) {
  const n = S.time === 'night';
  if (S.world === 'sky') return n ? { plate: '#0e1434', stroke: `hsl(${hue} 78% 68%)`, lw: 2.2, text: `hsl(${hue} 88% 86%)`, sub: '#c5cdea', ruby: `hsl(${hue} 60% 80%)` }
                                  : { plate: '#ffffff', stroke: `hsl(${hue} 58% 42%)`, lw: 2.2, text: `hsl(${hue} 72% 23%)`, sub: '#3b4758', ruby: `hsl(${hue} 50% 32%)` };
  if (S.world === 'mountains') return n ? { plate: '#1f2538', stroke: `hsl(${hue} 62% 66%)`, lw: 2, text: '#f3eee2', sub: '#b9b6ae', ruby: '#cfc9bb' }
                                        : { plate: '#fffaf0', stroke: `hsl(${hue} 48% 36%)`, lw: 2, text: '#27221c', sub: '#5f574b', ruby: '#5f574b' };
  return n ? { plate: '#090b1a', stroke: `hsl(${hue} 96% 62%)`, lw: 2.4, glow: `hsl(${hue} 100% 58%)`, text: `hsl(${hue} 100% 82%)`, sub: '#cbd3ea', ruby: `hsl(${hue} 80% 80%)` }
           : { plate: '#ffffff', stroke: `hsl(${hue} 62% 42%)`, lw: 3, text: `hsl(${hue} 72% 25%)`, sub: '#4a5361', ruby: `hsl(${hue} 45% 34%)` };
}
function layoutJa(text, main, rb, showRuby) {
  const parts = segs(text); let x = 0, hasRuby = false;
  for (const p of parts) {
    mctx.font = `600 ${main}px ${JP}`; p.bw = mctx.measureText(p.b).width; p.w = p.bw;
    if (showRuby && p.r) { mctx.font = `500 ${rb}px ${JP}`; p.rw = mctx.measureText(p.r).width; p.w = Math.max(p.bw, p.rw + 3); hasRuby = true; }
    p.x = x; x += p.w;
  }
  return { parts, w: x, hasRuby };
}
function rr(g, x, y, w, h, r) { g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath(); }
function drawJa(g, L, x0, baseY, main, rb, st, showRuby) {
  g.textBaseline = 'alphabetic'; g.textAlign = 'center'; g.lineJoin = 'round';
  for (const p of L.parts) {
    const cx = x0 + p.x + p.w / 2;
    g.font = `600 ${main}px ${JP}`;
    if (st.outline) { g.strokeStyle = st.outline; g.lineWidth = main * 0.17; g.strokeText(p.b, cx, baseY); }
    if (st.glow) { g.shadowColor = st.glow; g.shadowBlur = main * 0.35; }
    g.fillStyle = st.text; g.fillText(p.b, cx, baseY); g.shadowBlur = 0;
    if (showRuby && p.r) {
      g.font = `500 ${rb}px ${JP}`;
      if (st.outline) { g.strokeStyle = st.outline; g.lineWidth = rb * 0.22; g.strokeText(p.r, cx, baseY - main * 0.98); }
      g.fillStyle = st.ruby; g.fillText(p.r, cx, baseY - main * 0.98);
    }
  }
}
function wordSprite(it, hi) {
  const key = it.w.id + (hi ? '|h' : '|l'); let sp = sprites.get(key); if (sp) return sp;
  const k = hi ? 2.6 : 1, st = labelStyle(it.G.hue), mode = S.labels, main = 40, rb = 17, gl = 18;
  const L = layoutJa(it.w.hw, main, rb, mode !== 'ja');
  let gw = 0; const gloss = shortGloss(it.w);
  if (mode === 'en') { mctx.font = `500 ${gl}px ${UI}`; gw = mctx.measureText(gloss).width; }
  const m = st.glow ? 12 : 3, padX = st.plate ? 13 : 7, padY = st.plate ? 8 : 5;
  const rubyH = L.hasRuby ? rb + 2 : 0, glossH = mode === 'en' ? gl + 8 : 0;
  const iw = Math.max(L.w, gw) + padX * 2, ih = padY * 2 + rubyH + main * 1.06 + glossH;
  const dw = iw + m * 2, dh = ih + m * 2;
  const c = document.createElement('canvas'); c.width = Math.ceil(dw * k); c.height = Math.ceil(dh * k);
  const g = c.getContext('2d'); g.scale(k, k);
  if (st.plate) {
    rr(g, m, m, iw, ih, 7); g.fillStyle = st.plate;
    if (st.glow) { g.shadowColor = st.glow; g.shadowBlur = 11; }
    g.fill(); g.lineWidth = st.lw; g.strokeStyle = st.stroke; g.stroke(); g.shadowBlur = 0;
  }
  const baseY = m + padY + rubyH + main * 0.87;
  drawJa(g, L, m + (iw - L.w) / 2, baseY, main, rb, st, mode !== 'ja');
  if (mode === 'en') {
    g.font = `500 ${gl}px ${UI}`; g.textAlign = 'center';
    if (st.outline) { g.strokeStyle = st.outline; g.lineWidth = gl * 0.24; g.strokeText(gloss, dw / 2, baseY + gl + 9); }
    g.fillStyle = st.sub; g.fillText(gloss, dw / 2, baseY + gl + 9);
  }
  sp = { c, dw, dh, m, upp: it.size / main };
  sprites.set(key, sp);
  if (hi) { hiKeys.push(key); if (hiKeys.length > 40) sprites.delete(hiKeys.shift()); }
  return sp;
}
function signSprite(G) {
  const key = 'sign|' + G.g.id; let sp = sprites.get(key); if (sp) return sp;
  const k = 2, main = 40, rb = 15, en = 19, n = S.time === 'night', city = S.world === 'city';
  const L = layoutJa(G.g.ja, main, rb, true);
  mctx.font = `600 ${en}px ${UI}`; const ew = mctx.measureText(G.g.en.toUpperCase()).width + G.g.en.length * 1.2;
  const padX = 22, iw = Math.max(L.w, ew) + padX * 2, ih = 14 + rb + main * 1.05 + en + 16, m = 6, top = city ? 78 : 0;
  const dw = iw + m * 2, dh = ih + m * 2 + top;
  const c = document.createElement('canvas'); c.width = Math.ceil(dw * k); c.height = Math.ceil(dh * k);
  const g = c.getContext('2d'); g.scale(k, k);
  const fill = `hsl(${G.hue} ${n ? 70 : 64}% ${n ? 46 : 38}%)`;
  if (city) {  // advertising balloon carrying the district banner
    g.strokeStyle = n ? 'rgba(255,255,255,.6)' : 'rgba(40,50,70,.7)'; g.lineWidth = 1.5; g.beginPath(); g.moveTo(dw / 2, 56); g.lineTo(dw / 2, top + m); g.stroke();
    const gr = g.createRadialGradient(dw / 2 - 9, 22, 3, dw / 2, 30, 30); gr.addColorStop(0, `hsl(${G.hue} 90% 88%)`); gr.addColorStop(1, `hsl(${G.hue} 78% 52%)`);
    g.fillStyle = gr; g.beginPath(); g.arc(dw / 2, 30, 27, 0, TAU); g.fill();
  }
  rr(g, m, top + m, iw, ih, 10); g.fillStyle = fill; g.fill(); g.lineWidth = 2.5; g.strokeStyle = 'rgba(255,255,255,.9)'; g.stroke();
  const st = { text: '#ffffff', ruby: 'rgba(255,255,255,.9)' };
  const baseY = top + m + 12 + rb + main * 0.87;
  drawJa(g, L, m + (iw - L.w) / 2, baseY, main, rb, st, true);
  g.font = `600 ${en}px ${UI}`; g.textAlign = 'center'; g.fillStyle = 'rgba(255,255,255,.95)';
  try { g.letterSpacing = '1.2px'; } catch (e) {}
  g.fillText(G.g.en.toUpperCase(), dw / 2, baseY + en + 9);
  sp = { c, dw, dh, m, upp: 22 / main };
  sprites.set(key, sp); return sp;
}
function relSprite(type, hot) {
  const key = 'rel|' + type + (hot ? 'h' : ''); let sp = sprites.get(key); if (sp) return sp;
  const k = 2, fs = 20, txt = REL[type] || type; mctx.font = `600 ${fs}px ${UI}`;
  const iw = mctx.measureText(txt).width + 22, ih = fs + 12, dw = iw + 4, dh = ih + 4;
  const c = document.createElement('canvas'); c.width = Math.ceil(dw * k); c.height = Math.ceil(dh * k);
  const g = c.getContext('2d'); g.scale(k, k); const n = S.time === 'night';
  rr(g, 2, 2, iw, ih, ih / 2); g.fillStyle = hot ? '#ffb020' : (n ? '#161c36' : '#ffffff'); g.fill(); g.lineWidth = 1.5; g.strokeStyle = hot ? '#8a5a00' : (n ? '#6b78a3' : '#8d99ad'); g.stroke();
  g.font = `600 ${fs}px ${UI}`; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillStyle = hot ? '#2a1a00' : (n ? '#dfe5f7' : '#2b3545'); g.fillText(txt, dw / 2, dh / 2 + 1);
  sp = { c, dw, dh, m: 2, upp: 5.4 / fs }; sprites.set(key, sp); return sp;
}
let puffs = null, puffKey = '';
function puffSprites() {
  const key = S.time; if (puffs && puffKey === key) return puffs;
  const col = PAL.sky[S.time].puff, r = mulberry32(77); puffs = []; puffKey = key;
  for (let v = 0; v < 3; v++) {
    const c = document.createElement('canvas'); c.width = 320; c.height = 200; const g = c.getContext('2d');
    for (let i = 0; i < 14; i++) {
      const x = 62 + r() * 196, edge = 1 - Math.abs(x - 160) / 150, rad = (26 + r() * 30) * (0.55 + 0.6 * edge), y = 138 - rad * 0.55 - r() * 34 * edge;
      const gr = g.createRadialGradient(x, y, 0, x, y, rad * 1.5); gr.addColorStop(0, `rgba(${col[0]},${col[1]},${col[2]},.8)`); gr.addColorStop(0.5, `rgba(${col[0]},${col[1]},${col[2]},.5)`); gr.addColorStop(1, `rgba(${col[0]},${col[1]},${col[2]},0)`);
      g.fillStyle = gr; g.fillRect(0, 0, 320, 200);
    }
    g.globalCompositeOperation = 'source-atop'; const sh = g.createLinearGradient(0, 80, 0, 170); sh.addColorStop(0, 'rgba(90,120,170,0)'); sh.addColorStop(1, 'rgba(90,120,170,.22)'); g.fillStyle = sh; g.fillRect(0, 0, 320, 200);
    puffs.push(c);
  }
  return puffs;
}

/* ------------------------------------------------------------------ camera + renderer */
const cv = $('cv'), ctx = cv.getContext('2d', { alpha: false }), stage = $('stage'), main = $('xp-main');
// Compact layout (phones, and any window too short for the side panel): the cloud fills the page and everything else floats over it.
const compactMQ = matchMedia('(max-width: 760px), (max-height: 520px)'), isCompact = () => compactMQ.matches;
const cam = { x: 0, y: 0, z: -600, yaw: 0, pitch: 0 };
const vel = { x: 0, y: 0, z: 0 };
let W = 1, H = 1, U = 1, F = 600, CX = 0, CY = 0, cxT = 0, cyT = 0, quality = 1;
let sY = 0, cY = 1, sP = 0, cP = 1;
const NEAR = 5;
let PX = 0, PY = 0, PZ = 0;
function proj(x, y, z) { const dx = x - cam.x, dy = y - cam.y, dz = z - cam.z, x1 = dx * cY - dz * sY, z1 = dx * sY + dz * cY; PZ = dy * sP + z1 * cP; if (PZ < NEAR) return false; const s = F / PZ; PX = CX + x1 * s; PY = CY - (dy * cP - z1 * sP) * s; return true; }
const tmp = new Float32Array(3);
function toCam(x, y, z, o, i) { const dx = x - cam.x, dy = y - cam.y, dz = z - cam.z, x1 = dx * cY - dz * sY, z1 = dx * sY + dz * cY; o[i] = x1; o[i + 1] = dy * cP - z1 * sP; o[i + 2] = dy * sP + z1 * cP; }
const clipBuf = new Float32Array(48), polyBuf = new Float32Array(24);
function polyPath(pts, n) {
  let m = 0; const o = clipBuf;
  for (let i = 0; i < n; i++) {
    const a = i * 3, b = ((i + 1) % n) * 3, az = pts[a + 2], bz = pts[b + 2], ain = az >= NEAR, bin = bz >= NEAR;
    if (ain) { o[m++] = pts[a]; o[m++] = pts[a + 1]; o[m++] = az; }
    if (ain !== bin) { const t = (NEAR - az) / (bz - az); o[m++] = pts[a] + (pts[b] - pts[a]) * t; o[m++] = pts[a + 1] + (pts[b + 1] - pts[a + 1]) * t; o[m++] = NEAR; }
  }
  if (m < 9) return false;
  ctx.beginPath();
  for (let i = 0; i < m; i += 3) { const s = F / o[i + 2], X = CX + o[i] * s, Y = CY - o[i + 1] * s; if (i) ctx.lineTo(X, Y); else ctx.moveTo(X, Y); }
  ctx.closePath(); return true;
}

function resize() {
  const r = stage.getBoundingClientRect(); if (r.width < 2 || r.height < 2) return;
  const dpr = Math.min(window.devicePixelRatio || 1, 2) * quality;
  U = dpr; W = Math.round(r.width * dpr); H = Math.round(r.height * dpr);
  if (cv.width !== W || cv.height !== H) { cv.width = W; cv.height = H; }
  F = 0.9 * H * clamp(W / H * 1.1, 0.6, 1);
  viewCenter(true); dirty = true;
}
function viewCenter(snap) {
  const r = stage.getBoundingClientRect(), d = $('detail'); let sw = 0, sh = 0;
  if (isCompact() && !d.hidden) {                 // the word card covers part of the cloud (a sheet along the bottom, or a card on the right): centre what is left
    if (d.offsetWidth > r.width * 0.8) sh = Math.min(d.offsetHeight, r.height - 110); else sw = Math.min(r.width - d.offsetLeft, r.width - 110);
  }
  main.style.setProperty('--sheet-h', sh + 'px'); main.style.setProperty('--sheet-w', sw + 'px');
  cxT = (r.width - sw) / 2 * U; cyT = (r.height - sh) / 2 * U;
  if (snap) { CX = cxT; CY = cyT; }
}

let hits = [], vis = [], dirty = true, frameMs = 16, slowFrames = 0;
let frameId = 0, lastDt = 0.016, snapLayout = true, layoutStuck = 0; const bodies = [];
const fogT = d => { const P = pal(); return smooth(P.fogS, P.fogE, d); };

function drawBackdrop() {
  const P = pal(), horY = CY + F * Math.tan(cam.pitch), span = H * 1.25;
  const g = ctx.createLinearGradient(0, horY - span, 0, horY);
  g.addColorStop(0, P.top); g.addColorStop(1, P.hor);
  ctx.fillStyle = g; ctx.fillRect(0, 0, W, Math.max(0, Math.min(H, horY + 1)));
  if (horY < H) {
    if (S.world === 'sky') { const g2 = ctx.createLinearGradient(0, horY, 0, horY + span); g2.addColorStop(0, P.hor); g2.addColorStop(1, P.low); ctx.fillStyle = g2; }
    else {
      const g2 = ctx.createLinearGradient(0, horY, 0, horY + H), gc = hex(P.ground), fc = hex(P.hor), hgt = Math.max(8, cam.y);
      for (const u of [0, 0.02, 0.05, 0.1, 0.2, 0.4, 1]) { const dist = u === 0 ? 1e9 : hgt * F / (u * H) / Math.max(0.3, Math.cos(cam.pitch)); g2.addColorStop(u, rgb(mix(gc, fc, fogT(dist)))); }
      ctx.fillStyle = g2;
    }
    ctx.fillRect(0, Math.max(0, horY), W, H - Math.max(0, horY));
  }
  // stars, sun or moon (directions only)
  const dir = (dx, dy, dz) => { const x1 = dx * cY - dz * sY, z1 = dx * sY + dz * cY; PZ = dy * sP + z1 * cP; if (PZ < 0.05) return false; PX = CX + x1 * F / PZ; PY = CY - (dy * cP - z1 * sP) * F / PZ; return true; };
  if (scene.stars) { ctx.fillStyle = '#fff'; for (const s of scene.stars) if (dir(s[0], s[1], s[2]) && PY < horY) { ctx.globalAlpha = s[3] * 0.85; const r = (0.7 + s[3]) * U; ctx.fillRect(PX, PY, r, r); } ctx.globalAlpha = 1; }
  if (dir(0.52, 0.42, 0.74)) {
    const night = S.time === 'night', r = (night ? 26 : 34) * U * (F / (700 * U));
    const gl = ctx.createRadialGradient(PX, PY, r * 0.4, PX, PY, r * 5); gl.addColorStop(0, night ? 'rgba(210,220,255,.35)' : 'rgba(255,250,225,.7)'); gl.addColorStop(1, 'rgba(255,255,255,0)');
    ctx.fillStyle = gl; ctx.fillRect(PX - r * 5, PY - r * 5, r * 10, r * 10);
    ctx.fillStyle = night ? '#eef1ff' : '#fffbe8'; ctx.beginPath(); ctx.arc(PX, PY, r, 0, TAU); ctx.fill();
  }
}

function render() {
  sY = Math.sin(cam.yaw); cY = Math.cos(cam.yaw); sP = Math.sin(cam.pitch); cP = Math.cos(cam.pitch);
  ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.globalAlpha = 1;
  drawBackdrop();
  const P = pal(), fog = scene.fog, fogE2 = P.fogE * P.fogE;
  vis.length = 0; hits.length = 0;
  const tx = Math.max(CX, W - CX) / F * 1.02, ty = Math.max(CY, H - CY) / F * 1.02;

  const T = scene.terrain;
  if (T) {
    const { V, N, hs, vx, cam: tc, scr, code } = T;
    for (let j = 0, p = 0; j < V; j++) for (let i = 0; i < V; i++, p++) {
      toCam(vx[i], hs[p], vx[j], tc, p * 3);
      const x = tc[p * 3], y = tc[p * 3 + 1], z = tc[p * 3 + 2]; let c = 0;
      if (z < NEAR) c = 16; else { const s = F / z; scr[p * 2] = CX + x * s; scr[p * 2 + 1] = CY - y * s; }
      if (x < -z * tx) c |= 1; if (x > z * tx) c |= 2; if (y < -z * ty) c |= 4; if (y > z * ty) c |= 8;
      code[p] = c;
    }
    const qc = T.qc;
    for (let j = 0, q = 0; j < N; j++) for (let i = 0; i < N; i++, q++) {
      const a = j * V + i;
      if (code[a] & code[a + 1] & code[a + V] & code[a + V + 1]) continue;
      const dx = qc[q * 3] - cam.x, dy = qc[q * 3 + 1] - cam.y, dz = qc[q * 3 + 2] - cam.z, d = dx * dx + dy * dy + dz * dz;
      if (d > fogE2 * 1.1) continue;
      const it = T.items[q]; it.d = d; vis.push(it);
    }
  }
  const linkMode = S.links, skyWorld = S.world === 'sky';
  for (const it of scene.items) {
    if (it.k === 6) { vis.push(it); continue; }
    if (it.k === 5) { const hot = isHot(it.link); if (linkMode === 'off' || (linkMode === 'sel' && !hot)) continue; }
    const dx = it.x - cam.x, dy = it.y - cam.y, dz = it.z - cam.z; let d = dx * dx + dy * dy + dz * dz;
    if (it.k === 3) { if (d > 2600 * 2600) continue; d -= 900; }
    else if (it.k === 5) { it.d0 = d; d = skyWorld ? d + 5e8 : d - 400; }          // in the sky, connections run behind every word
    else if (it.k === 2) { if (d > fogE2 * 1.2) continue; it.d0 = d; d += 1e9; }    // clouds never veil a word
    else if (it.k !== 4 && d > fogE2 * 1.2) continue;
    it.d = d; vis.push(it);
  }
  vis.sort((a, b) => b.d - a.d);

  // Screen-space layout: every word, sign and connection label is a box; overlapping boxes push each other apart.
  frameId++; bodies.length = 0;
  for (const it of vis) { if (it.k === 3 || it.k === 4) layoutBillboard(it); else if (it.k === 5 && it.mid) layoutRel(it); }
  solveOverlaps(lastDt);

  const lineU = Math.max(1, U);
  for (const it of vis) {
    switch (it.k) {
      case 0: {
        const { V, N, cam: tc, scr, code, col } = T, q = it.q, j = (q / N) | 0, i = q - j * N, a = j * V + i, b = a + 1, c = a + V + 1, d = a + V;
        const t = fogT(Math.sqrt(it.d)), k3 = q * 3, clipped = (code[a] | code[b] | code[c] | code[d]) & 16;
        if (clipped || t > 0.7 || !T.pat) {             // far away (or cut by the camera): one flat colour is enough
          const fs = `rgb(${(col[k3] + (fog[0] - col[k3]) * t) | 0},${(col[k3 + 1] + (fog[1] - col[k3 + 1]) * t) | 0},${(col[k3 + 2] + (fog[2] - col[k3 + 2]) * t) | 0})`;
          if (clipped) {
            const pb = polyBuf; let o = 0; for (const v of [a, b, c, d]) { pb[o++] = tc[v * 3]; pb[o++] = tc[v * 3 + 1]; pb[o++] = tc[v * 3 + 2]; }
            if (!polyPath(pb, 4)) break;
          } else { ctx.beginPath(); ctx.moveTo(scr[a * 2], scr[a * 2 + 1]); ctx.lineTo(scr[b * 2], scr[b * 2 + 1]); ctx.lineTo(scr[c * 2], scr[c * 2 + 1]); ctx.lineTo(scr[d * 2], scr[d * 2 + 1]); ctx.closePath(); }
          ctx.fillStyle = fs; ctx.fill(); ctx.strokeStyle = fs; ctx.lineWidth = 1; ctx.stroke();
          break;
        }
        // near: map the ground texture onto the cell, one affine piece per triangle
        const ax = scr[a * 2], ay = scr[a * 2 + 1], bx = scr[b * 2], by = scr[b * 2 + 1], cx2 = scr[c * 2], cy2 = scr[c * 2 + 1], dx = scr[d * 2], dy = scr[d * 2 + 1];
        const k = T.tc, u0 = i * k, v0 = j * k, m = T.mat, pat = T.pat, dist = Math.sqrt(it.d);
        const land = T.hs[a] + T.hs[b] + T.hs[c] + T.hs[d] > 0, dp = land ? detailPattern() : null, da = dp ? 0.6 * (1 - smooth(240, 620, dist)) : 0, ds = T.ds;
        const grit = () => { m.a /= ds; m.b /= ds; m.c /= ds; m.d /= ds; dp.setTransform(m); ctx.globalCompositeOperation = 'overlay'; ctx.globalAlpha = da; ctx.fillStyle = dp; ctx.fill(); ctx.globalCompositeOperation = 'source-over'; ctx.globalAlpha = 1; };
        m.a = (bx - ax) / k; m.b = (by - ay) / k; m.c = (dx - ax) / k; m.d = (dy - ay) / k; m.e = ax - m.a * u0 - m.c * v0; m.f = ay - m.b * u0 - m.d * v0;
        pat.setTransform(m); ctx.fillStyle = pat; ctx.beginPath(); triPath(ax, ay, bx, by, dx, dy); ctx.fill(); if (da > 0.03) grit();
        m.a = (cx2 - dx) / k; m.b = (cy2 - dy) / k; m.c = (cx2 - bx) / k; m.d = (cy2 - by) / k; m.e = cx2 - m.a * (u0 + k) - m.c * (v0 + k); m.f = cy2 - m.b * (u0 + k) - m.d * (v0 + k);
        pat.setTransform(m); ctx.fillStyle = pat; ctx.beginPath(); triPath(bx, by, cx2, cy2, dx, dy); ctx.fill(); if (da > 0.03) grit();
        if (t > 0.02) { ctx.fillStyle = `rgba(${fog[0] | 0},${fog[1] | 0},${fog[2] | 0},${t.toFixed(3)})`; ctx.beginPath(); triPath(ax, ay, bx, by, dx, dy); triPath(bx, by, cx2, cy2, dx, dy); ctx.fill(); }
        break;
      }
      case 6: {
        const pb = polyBuf; toCam(it.x0, 0, it.z0, pb, 0); toCam(it.x1, 0, it.z0, pb, 3); toCam(it.x1, 0, it.z1, pb, 6); toCam(it.x0, 0, it.z1, pb, 9);
        if (polyPath(pb, 4)) { const dd = Math.hypot((it.x0 + it.x1) / 2 - cam.x, cam.y, (it.z0 + it.z1) / 2 - cam.z); ctx.fillStyle = rgb(mix(it.col, fog, fogT(dd) * 0.9)); ctx.fill(); }
        break;
      }
      case 1: drawBuilding(it, fogT(Math.sqrt(it.d)), fog, P); break;
      case 2: {
        if (!proj(it.x, it.y, it.z)) break;
        const dist = Math.sqrt(it.d0), s = F / PZ, w = it.r * 2 * s, h = w * 0.625;
        if (PX + w / 2 < 0 || PX - w / 2 > W || PY + h / 2 < 0 || PY - h / 2 > H) break;
        const al = P.puffA * it.a * (1 - fogT(dist) * 0.85) * clamp((PZ - 30) / (it.r * 0.9), 0, 1);
        if (al < 0.02) break;
        ctx.globalAlpha = al; ctx.drawImage(puffSprites()[it.v], PX - w / 2, PY - h / 2, w, h); ctx.globalAlpha = 1;
        break;
      }
      case 3: case 4: drawBillboard(it, false); break;
      case 5: {
        const L = it.link, hot = isHot(L), snap = S.world !== 'mountains';
        let x0, y0, z0, x1, y1, z1, ok = true;
        if (snap && it.first && L.a.vf === frameId) { x0 = L.a.ax + L.a.ox; y0 = L.a.ay + L.a.oy; z0 = L.a.pz; }
        else if (proj(it.p[0], it.p[1], it.p[2])) { x0 = PX; y0 = PY; z0 = PZ; } else ok = false;
        if (ok) { if (snap && it.last && L.b.vf === frameId) { x1 = L.b.ax + L.b.ox; y1 = L.b.ay + L.b.oy; z1 = L.b.pz; }
          else if (proj(it.q[0], it.q[1], it.q[2])) { x1 = PX; y1 = PY; z1 = PZ; } else ok = false; }
        const dist = Math.sqrt(it.d0), al = hot ? 0.95 : (L.cross ? 0.3 : 0.5) * (1 - fogT(dist));
        if (ok && al >= 0.03) {
          const c = hot ? [255, 176, 32] : P.link;
          ctx.strokeStyle = `rgba(${c[0]},${c[1]},${c[2]},${al})`; ctx.lineWidth = clamp((hot ? 3.2 : 1.7) * F / ((z0 + z1) / 2) * 0.55, hot ? 2 * lineU : 0.8 * lineU, (hot ? 5 : 2.6) * lineU);
          if (S.world === 'mountains') { const dsh = clamp(9 * F / z1, 2 * lineU, 16 * lineU); ctx.setLineDash([dsh, dsh * 0.7]); }
          ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke(); ctx.setLineDash([]);
        }
        if (it.mid && it.vf === frameId && it.ra > 0.03) { const sp = it.sp, w = sp.dw * it.px, h = sp.dh * it.px; ctx.globalAlpha = it.ra; ctx.drawImage(sp.c, it.ax + it.ox - w / 2, it.ay + it.oy - h / 2, w, h); ctx.globalAlpha = 1; }
        break;
      }
    }
  }
  ctx.globalAlpha = 1;
  if (selected) { const it = scene.labels.get(selected.id); if (it) drawBillboard(it, true); }
  if (fade) { ctx.globalAlpha = clamp(fade.a, 0, 1); ctx.drawImage(fade.c, 0, 0, W, H); ctx.globalAlpha = 1; }
}
function triPath(x1, y1, x2, y2, x3, y3) {      // a triangle grown by a fraction of a pixel, so neighbours leave no hairline gaps
  const mx = (x1 + x2 + x3) / 3, my = (y1 + y2 + y3) / 3, e = 0.8;
  let dx = x1 - mx, dy = y1 - my, l = Math.hypot(dx, dy) || 1; x1 += dx / l * e; y1 += dy / l * e;
  dx = x2 - mx; dy = y2 - my; l = Math.hypot(dx, dy) || 1; x2 += dx / l * e; y2 += dy / l * e;
  dx = x3 - mx; dy = y3 - my; l = Math.hypot(dx, dy) || 1; x3 += dx / l * e; y3 += dy / l * e;
  ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.lineTo(x3, y3); ctx.closePath();
}
let detailPat;                                 // fine tileable grain (soil, turf, scree) laid over the ground close to the camera
function detailPattern() {
  if (detailPat !== undefined) return detailPat;
  try {
    const TS = 512, c = document.createElement('canvas'); c.width = c.height = TS;
    const g = c.getContext('2d'), img = g.createImageData(TS, TS), px = img.data;
    const h = (x, y, s) => { let n = Math.imul(x, 374761393) + Math.imul(y, 668265263) + s; n = Math.imul(n ^ n >>> 13, 1274126177); return ((n ^ n >>> 16) >>> 0) / 4294967296; };
    const tn = (x, y, f, s) => { const fx = x * f / TS, fy = y * f / TS, xi = Math.floor(fx), yi = Math.floor(fy), u = fx - xi, v = fy - yi, ux = u * u * (3 - 2 * u), vy = v * v * (3 - 2 * v), x1 = (xi + 1) % f, y1 = (yi + 1) % f;
      return lerp(lerp(h(xi, yi, s), h(x1, yi, s), ux), lerp(h(xi, y1, s), h(x1, y1, s), ux), vy); };
    for (let y = 0, o = 0; y < TS; y++) for (let x = 0; x < TS; x++, o += 4) {
      const v = 128 + ((tn(x, y, 8, 1) - 0.5) * 0.5 + (tn(x, y, 24, 2) - 0.5) * 0.7 + (tn(x, y, 72, 3) - 0.5) * 0.8 + (tn(x, y, 192, 4) - 0.5) * 0.7 + (h(x, y, 5) - 0.5) * 0.35) * 120;
      px[o] = px[o + 1] = px[o + 2] = v < 0 ? 0 : v > 255 ? 255 : v; px[o + 3] = 255;
    }
    g.putImageData(img, 0, 0); detailPat = ctx.createPattern(c, 'repeat');
  } catch (e) { detailPat = null; }
  return detailPat;
}
function isHot(L) { return (selected && (L.a.w === selected || L.b.w === selected)) || (hovered && hovered.k === 3 && (L.a === hovered || L.b === hovered)); }

function gridHeight(T, x, z) {
  const fx = (x - T.vx[0]) / T.cell, fz = (z - T.vx[0]) / T.cell, i = Math.floor(fx), j = Math.floor(fz);
  if (i < 0 || j < 0 || i >= T.N || j >= T.N) return 0;
  const u = fx - i, v = fz - j, a = j * T.V + i;
  return lerp(lerp(T.hs[a], T.hs[a + 1], u), lerp(T.hs[a + T.V], T.hs[a + T.V + 1], u), v);
}
function hiddenByTerrain(x, y, z) {          // is the line of sight from the camera blocked by a mountain?
  const T = scene.terrain; if (!T) return false;
  for (let s = 1; s <= 8; s++) { const t = s / 9.5; if (gridHeight(T, lerp(x, cam.x, t), lerp(z, cam.z, t)) > lerp(y, cam.y, t) + 3) return true; }
  return false;
}
function asBody(it, mass, tier) {             // tier 3 stays put (selected), 2 words and signs, 1 connection labels, 0 hidden connection labels
  if (it.bf !== frameId - 1) { it.tx = it.ty = it.ox = it.oy = it.vx = it.vy = 0; it.ra = 0; }
  it.bf = frameId; it.mass = mass; it.tier = tier; bodies.push(it);
}
function layoutBillboard(it) {
  it.vf = 0;
  if (!proj(it.x, it.y, it.z)) return;
  const X = PX, Y = PY, Z = PZ, isWord = it.k === 3, sel = isWord && it.w === selected;
  let alpha = 1;
  if (isWord && !sel) alpha = smooth(55, 95, Z);          // a word right at the camera steps out of the way
  if (alpha < 0.03) return;
  let px = it.size / 40 * F / Z;                          // screen px per design px
  if (!isWord) px = clamp(px, 0.2 * U, 0.85 * U);          // signs stay legible far away and modest close up
  const sp = isWord ? wordSprite(it, px * 40 > 46) : signSprite(it.G);
  const m = sp.m * px, top = (S.world === 'city' && !isWord) ? 78 * px : 0;
  const bw = sp.dw * px - 2 * m, bh = sp.dh * px - 2 * m - top, ay = it.bottom ? Y - bh / 2 : Y;
  const mg = 90 * U;
  if (X + bw / 2 < -mg || X - bw / 2 > W + mg || ay + bh / 2 < -mg || ay - bh / 2 > H + mg) return;
  it.vf = frameId; it.ax = X; it.ay = ay; it.hw = bw / 2; it.hh = bh / 2; it.px = px; it.sp = sp; it.alpha = alpha; it.pz = Z; it.top = top;
  it.hasG = false;
  if (it.bottom && it.ground != null && proj(it.x, it.ground, it.z)) { it.hasG = true; it.gx = PX; it.gy = PY; }
  const solid = (isWord ? (px * 40 >= 5 * U && Z >= 95) || sel : true) && !hiddenByTerrain(it.x, it.cy, it.z);
  if (solid) asBody(it, bw * bh * (isWord ? (it === hovered ? 4 : 1) : 3), sel ? 3 : 2);
  else it.ox = it.oy = 0;
}
function layoutRel(it) {
  it.vf = 0; const L = it.link, hot = isHot(L);
  if (!proj(it.x, it.y, it.z)) return;
  if (!hot && it.d0 > 420 * 420) return;
  const sp = relSprite(L.type, hot); let px = sp.upp * F / PZ * (hot ? 1.5 : 1); if (hot) px = Math.max(px, 0.62 * U);
  if (px * 20 < 8 * U) return;
  px = Math.min(px, 0.8 * U);
  const w = sp.dw * px, h = sp.dh * px;
  if (PX + w < 0 || PX - w > W || PY + h < 0 || PY - h > H || hiddenByTerrain(it.x, it.y + 2, it.z)) return;
  it.vf = frameId; it.ax = PX; it.ay = PY; it.hw = w / 2; it.hh = h / 2; it.px = px; it.sp = sp;
  asBody(it, w * h, hot ? 2 : (it.ra < 0.5 && !it.want ? 0 : 1));      // labels of the selected word's connections always get room
  if (hot) it.ra = 1;
}
function solveOverlaps(dt) {
  const n = bodies.length, gap = 5 * U, snap = snapLayout || reduceMotion, dec = snapLayout ? 1 : Math.pow(0.985, dt * 60);
  for (let i = 0; i < n; i++) { bodies[i].tx *= dec; bodies[i].ty *= dec; }          // ease back toward the true position
  let left = 0;
  for (let iter = snapLayout ? 80 : 8; iter > 0; iter--) {
    let any = false; left = 0;
    for (let i = 0; i < n; i++) {
      const a = bodies[i], acx = a.ax + a.tx, acy = a.ay + a.ty;
      for (let j = i + 1; j < n; j++) {
        const b = bodies[j], dx = b.ax + b.tx - (a.ax + a.tx), px = a.hw + b.hw + gap - Math.abs(dx); if (px <= 0) continue;
        const dy = b.ay + b.ty - (a.ay + a.ty), py = a.hh + b.hh + gap - Math.abs(dy); if (py <= 0) continue;
        any = true; if (a.tier > 1 && b.tier > 1 && Math.min(px, py) > gap + U) left++;
        const wa = a.tier !== b.tier ? (a.tier < b.tier ? 1 : 0) : clamp(b.mass / (a.mass + b.mass), 0.2, 0.8), wb = 1 - wa;   // the lower tier gives way; within a tier the smaller box moves more
        if (py <= px) { const sg = dy > 0 || (dy === 0 && (i + j) % 2) ? 1 : -1; a.ty -= sg * py * wa; b.ty += sg * py * wb; }
        else { const sg = dx >= 0 ? 1 : -1; a.tx -= sg * px * wa; b.tx += sg * px * wb; }
      }
    }
    if (!any) break;
  }
  const K = 150, C = 11; let moving = false;
  for (let i = 0; i < n; i++) {                           // a connection label that finds no free spot fades out instead of covering something
    const a = bodies[i]; if (a.tier > 1) continue;
    let free = Math.hypot(a.tx, a.ty) < 64 * U;
    for (let j = 0; free && j < n; j++) { const b = bodies[j]; if (b === a || b.tier === 0) continue; if (a.hw + b.hw + U - Math.abs(b.ax + b.tx - a.ax - a.tx) > 0 && a.hh + b.hh + U - Math.abs(b.ay + b.ty - a.ay - a.ty) > 0) free = false; }
    a.want = free; const goal = free ? 1 : 0;
    a.ra = snap ? goal : clamp(a.ra + (goal - a.ra > 0 ? 1 : -1) * dt * 5, 0, 1);
    if (a.ra !== goal) moving = true;
  }                                           // under-damped spring: a slight bounce
  for (let i = 0; i < n; i++) {
    const b = bodies[i];
    if (snap) { b.ox = b.tx; b.oy = b.ty; b.vx = b.vy = 0; continue; }
    b.vx += (K * (b.tx - b.ox) - C * b.vx) * dt; b.vy += (K * (b.ty - b.oy) - C * b.vy) * dt; b.ox += b.vx * dt; b.oy += b.vy * dt;
    if (Math.abs(b.vx) + Math.abs(b.vy) > 5 * U || Math.abs(b.tx - b.ox) + Math.abs(b.ty - b.oy) > 0.6 * U) moving = true;
  }
  snapLayout = false;
  if (left) { if (++layoutStuck < 240) moving = true; } else layoutStuck = 0;      // keep working on a crowded view for a few seconds
  if (moving) dirty = true;
}
function drawBillboard(it, onTop) {
  if (it.vf !== frameId) return;
  const isWord = it.k === 3, sel = isWord && it.w === selected, hov = it === hovered;
  if (sel && !onTop) return;                              // the selected word is drawn last, on top
  const px = it.px, sp = it.sp, m = sp.m * px, cx = it.ax + it.ox, cy = it.ay + it.oy;
  if (it.hasG) {                                          // pole or tether down to the ground or roof
    const night = S.time === 'night';
    ctx.globalAlpha = it.alpha * (isWord ? 0.9 : 0.75);
    ctx.strokeStyle = S.world === 'city' ? (isWord ? (night ? '#8c93b4' : '#59616f') : (night ? 'rgba(255,255,255,.55)' : 'rgba(40,50,70,.6)')) : (night ? '#a59c8a' : '#6b5a45');
    ctx.lineWidth = clamp((isWord ? 1.4 : 0.8) * F / it.pz, 0.7 * U, 4 * U);
    ctx.beginPath(); ctx.moveTo(cx, cy + it.hh); ctx.lineTo(it.gx, it.gy); ctx.stroke();
  }
  ctx.globalAlpha = it.alpha;
  ctx.drawImage(sp.c, cx - sp.dw * px / 2, cy - it.hh - it.top - m, sp.dw * px, sp.dh * px);
  ctx.globalAlpha = 1;
  const hx = cx - it.hw, hy = cy - it.hh, hw = it.hw * 2, hh = it.hh * 2;
  if (sel || hov) {
    ctx.lineWidth = (sel ? 3 : 2) * U; ctx.strokeStyle = sel ? '#ffb020' : (S.time === 'night' ? '#ffffff' : '#111827');
    rr(ctx, hx - 2.5 * U, hy - 2.5 * U, hw + 5 * U, hh + 5 * U, 7 * U); ctx.stroke();
  }
  if (it.alpha > 0.25) hits.push({ x: hx - 3 * U, y: hy - 3 * U, w: hw + 6 * U, h: hh + 6 * U, it });
}

const bc = new Float32Array(24), fq = new Float32Array(12), rb = new Float32Array(12);
const fogRGB = (c, t, fog) => `rgb(${(c[0] + (fog[0] - c[0]) * t) | 0},${(c[1] + (fog[1] - c[1]) * t) | 0},${(c[2] + (fog[2] - c[2]) * t) | 0})`;
function drawBuilding(b, t, fog) {
  const below = cam.y < b.h;                 // from below, whatever stands on the roof is drawn first so the walls hide its foot
  if (below) for (const u of b.ups) drawBox(b, u.x0, u.x1, u.z0, u.z1, u.y0, u.y1, u.col, u.win, true, 40, t, fog);
  drawBox(b, b.x0, b.x1, b.z0, b.z1, 0, b.h, b.col, b.win, b.roof === 'flat', 0, t, fog);
  if (b.roof !== 'flat') drawRoof(b, t, fog);
  if (!below) for (const u of b.ups) drawBox(b, u.x0, u.x1, u.z0, u.z1, u.y0, u.y1, u.col, u.win, true, 40, t, fog);
}
function drawBox(b, x0, x1, z0, z1, y0, y1, col, win, top, fo, t, fog) {
  for (let i = 0; i < 8; i++) toCam(i & 1 ? x1 : x0, i & 4 ? y1 : y0, i & 2 ? z1 : z0, bc, i * 3);
  let allBehind = true; for (let i = 0; i < 8; i++) if (bc[i * 3 + 2] >= NEAR) { allBehind = false; break; }
  if (allBehind) return;
  const face = (i0, i1, i2, i3, ci, wd, fi) => {
    for (let k = 0; k < 3; k++) { fq[k] = bc[i0 * 3 + k]; fq[3 + k] = bc[i1 * 3 + k]; fq[6 + k] = bc[i2 * 3 + k]; fq[9 + k] = bc[i3 * 3 + k]; }
    if (!polyPath(fq, 4)) return;
    const fs = fogRGB(col[ci], t, fog); ctx.fillStyle = fs; ctx.fill(); ctx.strokeStyle = fs; ctx.lineWidth = 1; ctx.stroke();
    if (win && fi >= 0 && t < 0.6) drawWindows(b, win, wd, y1 - y0, fi + fo, t, fog);
  };
  if (cam.z < z0) face(0, 1, 5, 4, 0, x1 - x0, 0);
  if (cam.z > z1) face(3, 2, 6, 7, 1, x1 - x0, 1);
  if (cam.x < x0) face(2, 0, 4, 6, 2, z1 - z0, 2);
  if (cam.x > x1) face(1, 3, 7, 5, 3, z1 - z0, 3);
  if (top && cam.y > y1) face(4, 5, 7, 6, 4, 0, -1);
}
// Windows are laid out on the wall itself (in metres, as it were) and each corner is projected, so rows and columns stay true in perspective.
function drawWindows(b, win, wd, ht, fi, t, fog) {
  if (fq[2] < NEAR || fq[5] < NEAR || fq[8] < NEAR || fq[11] < NEAR) return;
  const fh = win.fh, zavg = (fq[2] + fq[5] + fq[8] + fq[11]) / 4;
  if (fh * F / zavg < 2.4 * U) return;                    // too small on screen to matter
  const ox = fq[0], oy = fq[1], oz = fq[2], ux = (fq[3] - ox) / wd, uy = (fq[4] - oy) / wd, uz = (fq[5] - oz) / wd, vx = (fq[9] - ox) / ht, vy = (fq[10] - oy) / ht, vz = (fq[11] - oz) / ht;
  const pa = new Path2D(), pb = new Path2D();
  const pt = (p, u, v, first) => { const s = F / (oz + uz * u + vz * v), X = CX + (ox + ux * u + vx * v) * s, Y = CY - (oy + uy * u + vy * v) * s; if (first) p.moveTo(X, Y); else p.lineTo(X, Y); };
  const quad = (p, u0, u1, v0, v1) => { pt(p, u0, v0, true); pt(p, u1, v0); pt(p, u1, v1); pt(p, u0, v1); p.closePath(); };
  const hsh = (i, j) => { let n = Math.imul(b.seed + fi * 7919 + i * 131 + j * 31337, 2654435761); n ^= n >>> 15; n = Math.imul(n, 2246822519); return ((n ^ n >>> 13) >>> 0) / 4294967296 < b.fracA; };
  const m = win.m || 0, cols = Math.max(1, Math.round((wd - 2 * m) / win.bay)), bay = (wd - 2 * m) / cols, base = win.base, topm = win.topm == null ? 3 : win.topm;
  if (win.mode === 'fins') {
    for (let i = 0; i < cols; i++) { const u0 = m + i * bay + bay * (1 - win.ww) / 2; quad(hsh(i, 0) ? pa : pb, u0, u0 + bay * win.ww, base, ht - topm); }
  } else {
    const rows = Math.min(16, Math.floor((ht - base - topm) / fh + 0.001)), off = base + (ht - base - topm - rows * fh) / 2;
    for (let j = 0; j < rows; j++) {
      const v0 = off + j * fh + fh * (1 - win.wh) / 2, v1 = v0 + fh * win.wh;
      for (let i = 0; i < cols; i++) {
        const on = hsh(i, j); let e = i;
        if (win.ww === 1) while (e + 1 < cols && hsh(e + 1, j) === on) e++;       // a ribbon: neighbouring panes of one kind join up
        quad(on ? pa : pb, m + i * bay + bay * (1 - win.ww) / 2, m + e * bay + bay * (1 + win.ww) / 2, v0, v1); i = e;
      }
    }
  }
  if (win.shop) quad(pa, 2.5, wd - 2.5, 1.5, base - 3.5);                        // shop front
  ctx.fillStyle = fogRGB(b.wB, t, fog); ctx.fill(pb); ctx.fillStyle = fogRGB(b.wA, t, fog); ctx.fill(pa);
  if (win.shop && b.awn) { const p = new Path2D(); quad(p, 0, wd, base - 3.2, base - 0.6); ctx.fillStyle = fogRGB(b.awn, t, fog); ctx.fill(p); }
}
function drawRoof(b, t, fog) {                 // pitched tile roofs: a gable (two slopes) or a hip (four slopes to a point)
  const o = 2.5, x0 = b.x0 - o, x1 = b.x1 + o, z0 = b.z0 - o, z1 = b.z1 + o, h = b.h, r = b.rh, xc = (x0 + x1) / 2, zc = (z0 + z1) / 2, y = cam.y - h;
  const poly = (c, ...p) => { const n = p.length / 3; for (let i = 0; i < n; i++) toCam(p[i * 3], p[i * 3 + 1], p[i * 3 + 2], rb, i * 3); if (!polyPath(rb, n)) return; const fs = fogRGB(c, t, fog); ctx.fillStyle = fs; ctx.fill(); ctx.strokeStyle = fs; ctx.lineWidth = 1; ctx.stroke(); };
  const S_ = y * (zc - z0) - (cam.z - z0) * r > 0, N_ = y * (z1 - zc) + (cam.z - z1) * r > 0, W_ = y * (xc - x0) - (cam.x - x0) * r > 0, E_ = y * (x1 - xc) + (cam.x - x1) * r > 0, rc = b.roofCol;
  if (b.roof === 'hip') {
    if (S_) poly(rc[0], x0, h, z0, x1, h, z0, xc, h + r, zc); if (N_) poly(rc[1], x1, h, z1, x0, h, z1, xc, h + r, zc);
    if (W_) poly(rc[2], x0, h, z1, x0, h, z0, xc, h + r, zc); if (E_) poly(rc[3], x1, h, z0, x1, h, z1, xc, h + r, zc);
  } else if (b.ridgeX) {
    if (cam.x < b.x0) poly(b.col[2], b.x0, h, b.z0, b.x0, h, b.z1, b.x0, h + r, zc); if (cam.x > b.x1) poly(b.col[3], b.x1, h, b.z0, b.x1, h, b.z1, b.x1, h + r, zc);
    if (S_) poly(rc[0], x0, h, z0, x1, h, z0, x1, h + r, zc, x0, h + r, zc); if (N_) poly(rc[1], x1, h, z1, x0, h, z1, x0, h + r, zc, x1, h + r, zc);
  } else {
    if (cam.z < b.z0) poly(b.col[0], b.x0, h, b.z0, b.x1, h, b.z0, xc, h + r, b.z0); if (cam.z > b.z1) poly(b.col[1], b.x0, h, b.z1, b.x1, h, b.z1, xc, h + r, b.z1);
    if (W_) poly(rc[2], x0, h, z1, x0, h, z0, xc, h + r, z0, xc, h + r, z1); if (E_) poly(rc[3], x1, h, z0, x1, h, z1, xc, h + r, z1, xc, h + r, z0);
  }
}

/* ------------------------------------------------------------------ flight */
const keys = Object.create(null);
let fly = null, orbit = null, tourIdx = 0;
const ease = t => t * t * t * (t * (6 * t - 15) + 10);          // gentle start, gentle stop
const angDiff = (a, b) => { let d = (a - b) % TAU; if (d > Math.PI) d -= TAU; if (d < -Math.PI) d += TAU; return d; };
function look(from, to) { const dx = to.x - from.x, dy = to.y - from.y, dz = to.z - from.z; return { yaw: Math.atan2(dx, dz), pitch: Math.atan2(dy, Math.hypot(dx, dz)) }; }
function groundClamp(p) { if (!scene) return; let m = scene.minY; if (scene.height) m = scene.height(p.x, p.z) + 14; if (p.y < m) p.y = m; }
// Fly to pos and end up looking at target. The camera travels around the target (its bearing and its distance from
// the target both change smoothly, so it never passes through or over it) and turns toward it a little ahead of the
// travel: a word that was clicked glides to the middle of the view and then comes closer.
let fade = null;                                // reduced motion: the old view dissolves into the new one instead
function flyTo(pos, target, then) {
  groundClamp(pos);
  const r0 = Math.hypot(cam.x - target.x, cam.z - target.z), r1 = Math.hypot(pos.x - target.x, pos.z - target.z);
  const th0 = Math.atan2(cam.x - target.x, cam.z - target.z), dth = r0 > 1 ? angDiff(Math.atan2(pos.x - target.x, pos.z - target.z), th0) : 0;
  const l0 = look(cam, target), oy = angDiff(cam.yaw, l0.yaw), op = cam.pitch - l0.pitch;
  const len = Math.hypot(r1 - r0, pos.y - cam.y) + Math.abs(dth) * (r0 + r1) / 2;
  layoutStuck = 0;
  if (reduceMotion && scene && W > 1) { const c = document.createElement('canvas'); c.width = W; c.height = H; c.getContext('2d').drawImage(cv, 0, 0); fade = { c, a: 1 }; }
  fly = { target: { ...target }, r0, r1, th0: r0 > 1 ? th0 : Math.atan2(pos.x - target.x, pos.z - target.z), dth, y0: cam.y, y1: pos.y, oy, op, t: 0,
    dur: reduceMotion ? 0.01 : clamp(0.8 + len / 560 + Math.hypot(oy, op) * 0.8, 1.7, 4.6), then };
  orbit = null; vel.x = vel.y = vel.z = 0;
}
function overview(G) {
  if (scene.world === 'sky') return { c: { x: G.c.x, y: G.c.y, z: G.c.z }, r: G.radius * 1.7 + 95, h: G.radius * 0.34 };
  if (scene.world === 'mountains') return { c: { x: G.c.x, y: G.top * 0.5, z: G.c.z }, r: G.sig * 2.7 + 150, h: G.top * 0.42 + 70 };
  return { c: { x: G.c.x, y: 48, z: G.c.z }, r: G.span * 0.8 + 140, h: 178 };
}
function gotoGroup(G, jump) {
  const o = overview(G); activeGroup = G; markPlaces();
  let a = Math.atan2(cam.x - o.c.x, cam.z - o.c.z);
  if (jump) a = mulberry32(S.seed + G.i)() * TAU;
  const pos = { x: o.c.x + Math.sin(a) * o.r, y: o.c.y + o.h, z: o.c.z + Math.cos(a) * o.r };
  const start = () => { orbit = { ...o, a, time: 0, w: reduceMotion ? 0 : 0.055 }; };
  if (jump) { groundClamp(pos); const l = look(pos, o.c); Object.assign(cam, pos, l); fly = null; vel.x = vel.y = vel.z = 0; start(); }
  else flyTo(pos, o.c, start);
  dirty = true;
}
function gotoWord(w) {
  const it = scene.labels.get(w.id); if (!it) return;
  const tgt = { x: it.x, y: it.cy, z: it.z }; let dx, dz;
  if (scene.world === 'mountains') { dx = it.x - it.G.c.x; dz = it.z - it.G.c.z; }
  else { dx = cam.x - it.x; dz = cam.z - it.z; }
  const l = Math.hypot(dx, dz) || 1, dist = 150 * (it.size / 12) * (S.labels === 'en' ? 1.15 : 1);
  const pos = { x: it.x + dx / l * dist, y: it.cy + (scene.world === 'sky' ? 12 : 26), z: it.z + dz / l * dist };
  activeGroup = it.G; markPlaces();
  flyTo(pos, tgt, null);
}
function userFlying() { layoutStuck = 0; if (fly || orbit) { fly = null; orbit = null; } if (S.tour) { S.tour = false; syncTour(); } hideHint(); }
function update(dt) {
  CX = lerp(CX, cxT, 1 - Math.exp(-dt * 6)); CY = lerp(CY, cyT, 1 - Math.exp(-dt * 6));
  if (Math.abs(CX - cxT) > 0.5 || Math.abs(CY - cyT) > 0.5) dirty = true;
  const kf = (keys.KeyW ? 1 : 0) - (keys.KeyS ? 1 : 0), kr = (keys.KeyD ? 1 : 0) - (keys.KeyA ? 1 : 0), ku = (keys.KeyR || keys.KeyE ? 1 : 0) - (keys.KeyF || keys.KeyQ ? 1 : 0);
  const kt = (keys.ArrowRight ? 1 : 0) - (keys.ArrowLeft ? 1 : 0), kp = (keys.ArrowUp ? 1 : 0) - (keys.ArrowDown ? 1 : 0);
  if (kf || kr || ku || kt || kp) userFlying();
  if (fade) { fade.a -= dt / 0.45; if (fade.a <= 0) fade = null; dirty = true; }
  if (fly) {
    fly.t = Math.min(1, fly.t + dt / fly.dur); const e = ease(fly.t), turned = ease(Math.min(1, fly.t / 0.7)), T = fly.target;
    const th = fly.th0 + fly.dth * e, r = lerp(fly.r0, fly.r1, e);
    cam.x = T.x + Math.sin(th) * r; cam.z = T.z + Math.cos(th) * r; cam.y = lerp(fly.y0, fly.y1, e);
    groundClamp(cam);
    const l = look(cam, T); cam.yaw = l.yaw + fly.oy * (1 - turned); cam.pitch = clamp(l.pitch + fly.op * (1 - turned), -1.35, 1.35);
    if (fly.t >= 1) { const th = fly.then; fly = null; if (th) th(); }
    dirty = true; return;
  }
  if (orbit) {
    if (orbit.w) {
      orbit.a += orbit.w * dt; orbit.time += dt;
      cam.x = orbit.c.x + Math.sin(orbit.a) * orbit.r; cam.z = orbit.c.z + Math.cos(orbit.a) * orbit.r; cam.y = orbit.c.y + orbit.h; groundClamp(cam);
      const l = look(cam, orbit.c); cam.yaw = l.yaw; cam.pitch = l.pitch; dirty = true;
      if (S.tour && orbit.time > 10 && !selected && scene.groups.length > 1) { tourIdx = (scene.groups.indexOf(activeGroup) + 1) % scene.groups.length; gotoGroup(scene.groups[tourIdx]); }
    }
    return;
  }
  const acc = 560 * S.speed * (keys.ShiftLeft || keys.ShiftRight ? 2.4 : 1);
  const fx = sY * cP, fy = sP, fz = cY * cP;
  vel.x += (fx * kf + cY * kr) * acc * dt; vel.y += (fy * kf + ku) * acc * dt; vel.z += (fz * kf - sY * kr) * acc * dt;
  const damp = Math.exp(-2.6 * dt); vel.x *= damp; vel.y *= damp; vel.z *= damp;
  cam.yaw += kt * 1.3 * dt; cam.pitch = clamp(cam.pitch + kp * 0.9 * dt, -1.35, 1.35);
  const sp2 = vel.x * vel.x + vel.y * vel.y + vel.z * vel.z;
  if (sp2 > 0.5 || kt || kp) {
    cam.x += vel.x * dt; cam.y += vel.y * dt; cam.z += vel.z * dt;
    const lim = scene.R * 1.7, r = Math.hypot(cam.x, cam.z); if (r > lim) { cam.x *= lim / r; cam.z *= lim / r; }
    cam.y = clamp(cam.y, -900, 1100); groundClamp(cam); dirty = true;
  }
}
let last = 0;
function frame(t) {
  const dt = Math.min(0.05, (t - last) / 1000 || 0.016); last = t;
  if (!scene) { requestAnimationFrame(frame); return; }
  update(dt);
  if (dirty) {
    dirty = false; lastDt = dt; const t0 = performance.now(); render(); const ms = performance.now() - t0;
    frameMs = frameMs * 0.9 + ms * 0.1;
    if (frameMs > 24) { if (++slowFrames > 50 && quality > 0.55) { quality *= 0.82; slowFrames = 0; frameMs = 16; resize(); } } else slowFrames = Math.max(0, slowFrames - 1);
  }
  requestAnimationFrame(frame);
}

/* ------------------------------------------------------------------ pointer, wheel, keys */
const pointers = new Map(); let drag = null, pinch = 0;
const pos = e => { const r = cv.getBoundingClientRect(); return { x: (e.clientX - r.left) * U, y: (e.clientY - r.top) * U }; };
function hitTest(x, y) { for (let i = hits.length - 1; i >= 0; i--) { const h = hits[i]; if (x >= h.x && x <= h.x + h.w && y >= h.y && y <= h.y + h.h) return h.it; } return null; }
cv.addEventListener('pointerdown', e => {
  if (panel) setPanel(null);
  cv.setPointerCapture(e.pointerId); const p = pos(e); pointers.set(e.pointerId, p);
  if (pointers.size === 1) drag = { x: p.x, y: p.y, moved: 0 }; else { drag = null; pinch = 0; }
});
cv.addEventListener('pointermove', e => {
  const p = pos(e);
  if (pointers.has(e.pointerId)) {
    const o = pointers.get(e.pointerId); pointers.set(e.pointerId, p);
    if (pointers.size === 1 && drag) {
      const dx = p.x - o.x, dy = p.y - o.y; drag.moved += Math.abs(dx) + Math.abs(dy);
      if (drag.moved > 6 * U) { userFlying(); cv.classList.add('grabbing'); cam.yaw -= dx / F; cam.pitch = clamp(cam.pitch + dy / F, -1.35, 1.35); dirty = true; }
    } else if (pointers.size === 2) {
      const [a, b] = [...pointers.values()], d = Math.hypot(a.x - b.x, a.y - b.y);
      if (pinch) { userFlying(); const k = (d - pinch) * 2.2 / U * S.speed; vel.x += sY * cP * k; vel.y += sP * k; vel.z += cY * cP * k; }
      pinch = d;
    }
    return;
  }
  const h = hitTest(p.x, p.y);
  if (h !== hovered) { hovered = h; cv.classList.toggle('pointing', !!h); dirty = true; }
});
function endPointer(e) {
  const had = pointers.has(e.pointerId); pointers.delete(e.pointerId); cv.classList.remove('grabbing'); pinch = 0;
  if (had && drag && drag.moved <= 6 * U && e.type === 'pointerup') { const p = pos(e), h = hitTest(p.x, p.y); if (h) { if (h.k === 3) selectWord(h.w); else { if (S.tour) { S.tour = false; syncTour(); } gotoGroup(h.G); } } hideHint(); }
  if (!pointers.size) drag = null;
}
cv.addEventListener('pointerup', endPointer); cv.addEventListener('pointercancel', endPointer);
cv.addEventListener('pointerleave', () => { if (hovered) { hovered = null; cv.classList.remove('pointing'); dirty = true; } });
cv.addEventListener('wheel', e => { e.preventDefault(); userFlying(); const k = -e.deltaY * (e.deltaMode === 1 ? 16 : 1) * 1.5 * S.speed; vel.x += sY * cP * k; vel.y += sP * k; vel.z += cY * cP * k; }, { passive: false });
const FLY_KEYS = new Set(['KeyW', 'KeyA', 'KeyS', 'KeyD', 'KeyR', 'KeyF', 'KeyQ', 'KeyE', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'ShiftLeft', 'ShiftRight']);
window.addEventListener('keydown', e => {
  const t = e.target; if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return;
  if (e.code === 'Escape' && (panel || selected)) { if (panel) setPanel(null); else closeDetail(); return; }
  if (e.metaKey || e.ctrlKey || e.altKey) return;
  if (FLY_KEYS.has(e.code)) { keys[e.code] = true; if (e.code.startsWith('Arrow')) e.preventDefault(); }
});
window.addEventListener('keyup', e => { keys[e.code] = false; });
window.addEventListener('blur', () => { for (const k in keys) keys[k] = false; });
function hold(btn, code) {
  const on = e => { e.preventDefault(); keys[code] = true; }, off = () => { keys[code] = false; };
  btn.addEventListener('pointerdown', on); btn.addEventListener('pointerup', off); btn.addEventListener('pointerleave', off); btn.addEventListener('pointercancel', off);
  btn.addEventListener('keydown', e => { if (e.key === ' ' || e.key === 'Enter') keys[code] = true; }); btn.addEventListener('keyup', off); btn.addEventListener('contextmenu', e => e.preventDefault());
}
hold($('btn-fwd'), 'KeyW'); hold($('btn-back'), 'KeyS');

/* ------------------------------------------------------------------ word card */
let player = null, playingBtn = null;
function stopAudio() { if (player) player.pause(); if (playingBtn) { playingBtn.classList.remove('on'); playingBtn = null; } }
function playExample(url, btn, note) {
  if (playingBtn === btn) { stopAudio(); return; }
  stopAudio();
  const failed = () => { if (playingBtn === btn) { note.hidden = false; note.textContent = 'The recording could not be played.'; stopAudio(); } };
  if (!player) { player = new Audio(); player.addEventListener('ended', stopAudio); }
  player.onerror = failed;
  player.src = url; playingBtn = btn; btn.classList.add('on');
  const p = player.play(); if (p && p.catch) p.catch(failed);
}
const CHEVRON = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 10l5-5 5 5"/></svg>';
let sheetOpen = false;                        // compact layout: is the word card unfolded (examples, connections) or only its head showing?
function setSheet(open) { sheetOpen = open; main.classList.toggle('sheet-open', open); const b = $('detail').querySelector('.more-toggle'); if (b) b.setAttribute('aria-expanded', String(open)); }
function selectWord(w) {
  selected = w; if (S.tour) { S.tour = false; syncTour(); }
  setPanel(null);
  const it = scene.labels.get(w.id), d = $('detail'); d.textContent = ''; d.hidden = false; $('detail-empty').hidden = true; main.classList.add('has-detail'); $('side').scrollTop = 0;
  const head = el('div', 'head'), more = el('div', 'more'), wrap = el('div', 'more-wrap'); wrap.appendChild(more);
  const grab = el('div', 'grab'); grab.setAttribute('aria-hidden', 'true'); grab.onclick = () => setSheet(!sheetOpen); head.appendChild(grab);
  const close = el('button', 'close', '×'); close.setAttribute('aria-label', 'Close'); close.onclick = closeDetail; head.appendChild(close);
  if (it) { const tag = el('button', 'place-tag'); const dot = el('span', 'dot'); dot.style.background = `hsl(${it.G.hue} 65% 45%)`; const tj = el('span', null, plain(it.G.g.ja)); tj.lang = 'ja'; tag.append(dot, tj, document.createTextNode(' · ' + it.G.g.en)); tag.onclick = () => gotoGroup(it.G); head.appendChild(tag); }
  const h = rubyInto(el('h2'), w.hw); h.lang = 'ja'; head.appendChild(h);
  const meta = el('div', 'meta'); const rd = el('span', null, w.r); rd.lang = 'ja'; meta.append(rd, el('span', null, '·'), el('span', null, w.pos), el('span', 'tier', w.t)); head.appendChild(meta);
  head.appendChild(el('p', 'gloss', w.g));
  if (w.ex.length) {
    more.appendChild(el('h3', null, w.ex.length > 1 ? 'Examples' : 'Example'));
    const note = el('p', 'audio-note'); note.hidden = true;
    for (const x of w.ex) {
      const row = el('div', 'ex'); const b = el('button', 'play'); b.innerHTML = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 1.2v9.6L10.5 6z"/></svg>'; b.setAttribute('aria-label', 'Play the recording');
      if (x.a) b.onclick = () => playExample(x.a, b, note); else b.disabled = true;
      const ja = rubyInto(el('div', 'ja'), x.ja); ja.lang = 'ja'; row.append(b, ja, el('div', 'en', x.en)); more.appendChild(row);
    }
    more.appendChild(note);
  }
  const conns = w.x.slice().sort((a, b) => (scene.labels.has(b.id) ? 1 : 0) - (scene.labels.has(a.id) ? 1 : 0));
  if (conns.length) {
    more.appendChild(el('h3', null, 'Connections')); const box = el('div', 'conns');
    for (const c of conns.slice(0, 10)) {
      const here = scene.labels.has(c.id), b = el(here ? 'button' : 'a'); const ww = rubyInto(el('span', 'w'), c.hw); ww.lang = 'ja';
      b.append(el('span', 'rel', REL[c.type] || 'related'), ww, el('span', 'g', c.g));
      if (here) { b.type = 'button'; b.onclick = () => selectWord(WORDS.get(c.id)); }
      else { b.href = entryUrl(c.id); b.target = '_blank'; b.rel = 'noopener'; b.title = 'Not in this cloud: opens the entry'; }
      box.appendChild(b);
    }
    more.appendChild(box);
  }
  const others = w.grp.filter(g => (!it || g !== it.G.g.id) && PLACES.has(g));
  if (others.length) {
    more.appendChild(el('h3', null, 'Also belongs to')); const box = el('div', 'also');
    for (const gid of others) { const g = PLACES.get(gid), G = arr.groups.find(x => x.g.id === gid), c = el(G ? 'button' : 'span'); const j = el('span', null, plain(g.ja)); j.lang = 'ja'; c.append(j, document.createTextNode(g.en)); if (G) { c.type = 'button'; c.onclick = () => gotoGroup(G); } box.appendChild(c); }
    more.appendChild(box);
  }
  const a = el('a', 'entry-link', 'Open the full entry');
  a.href = entryUrl(w.id); a.target = '_blank'; a.rel = 'noopener'; more.appendChild(a);
  const what = [w.ex.length ? (w.ex.length > 1 ? 'examples' : 'example') : '', conns.length ? 'connections' : ''].filter(Boolean).join(' and ') || 'more';
  const tg = el('button', 'more-toggle'); tg.type = 'button'; tg.appendChild(el('span', null, what[0].toUpperCase() + what.slice(1))); tg.insertAdjacentHTML('beforeend', CHEVRON); tg.onclick = () => setSheet(!sheetOpen); head.appendChild(tg);
  d.append(head, wrap); setSheet(sheetOpen);
  viewCenter(false); gotoWord(w); dirty = true;
}
function closeDetail() { selected = null; $('detail').hidden = true; $('detail-empty').hidden = false; main.classList.remove('has-detail'); setSheet(false); stopAudio(); viewCenter(false); dirty = true; }
// The bottom sheet answers to a swipe on its head: up unfolds it, down folds it, down again closes it.
const sheetAtBottom = () => isCompact() && !$('detail').hidden && $('detail').offsetWidth > stage.clientWidth * 0.8;
let swipe = null, swipedAt = 0;
$('detail').addEventListener('pointerdown', e => { swipe = sheetAtBottom() && e.target.closest('.head') ? { y: e.clientY, id: e.pointerId } : null; });
window.addEventListener('pointerup', e => {
  if (!swipe || swipe.id !== e.pointerId) return; const dy = e.clientY - swipe.y; swipe = null; if (Math.abs(dy) < 28) return;
  swipedAt = performance.now(); if (dy < 0) setSheet(true); else if (sheetOpen) setSheet(false); else closeDetail();
});
window.addEventListener('pointercancel', () => { swipe = null; });
$('detail').addEventListener('click', e => { if (performance.now() - swipedAt < 400) { e.stopPropagation(); e.preventDefault(); } }, true);   // a swipe that began on a button is not a press
new ResizeObserver(() => { viewCenter(false); dirty = true; }).observe($('detail'));

/* ------------------------------------------------------------------ controls */
function segControl(id, opts, get, set) {
  const box = $(id); box.setAttribute('role', 'group');
  for (const [v, label] of opts) { const b = el('button', null, label); b.type = 'button'; b.dataset.v = v; b.onclick = () => { set(v); sync(); }; box.appendChild(b); }
  const sync = () => { for (const b of box.children) b.setAttribute('aria-pressed', String(b.dataset.v === get())); }; sync(); return sync;
}
function chipControl(id, opts, obj, onChange) {
  const box = $(id);
  for (const [v, label] of opts) {
    const b = el('button', null, label); b.type = 'button'; b.setAttribute('aria-pressed', String(obj[v]));
    b.onclick = () => { const on = !obj[v]; if (!on && Object.values(obj).filter(Boolean).length === 1) return; obj[v] = on; b.setAttribute('aria-pressed', String(on)); onChange(); };
    box.appendChild(b);
  }
}
function markPlaces() {
  for (const b of $('places').querySelectorAll('.place')) b.setAttribute('aria-current', String(activeGroup && b.dataset.g === activeGroup.g.id));
  const pill = $('btn-places'), G = activeGroup; pill.hidden = !G; if (!G) return;       // compact layout: one button names the place and opens the list
  pill.children[0].style.background = `hsl(${G.hue} 65% 45%)`; pill.children[1].textContent = plain(G.g.ja); pill.children[2].textContent = G.g.en;
  pill.setAttribute('aria-label', `Places. Now at ${G.g.en}`);
}
function fillPlaces() {
  const box = $('places'); box.textContent = ''; box.appendChild(el('span', 'lab', 'Places'));
  for (const G of arr.groups) {
    const b = el('button', 'place'); b.type = 'button'; b.dataset.g = G.g.id;
    const dot = el('span', 'dot'); dot.style.background = `hsl(${G.hue} 65% 45%)`;
    const ja = el('span', 'ja', plain(G.g.ja)); ja.lang = 'ja';
    b.append(dot, ja, el('span', 'en', G.g.en), el('span', 'n', String(G.words.length)));
    b.onclick = () => { if (S.tour) { S.tour = false; syncTour(); } setPanel(null); gotoGroup(G); hideHint(); };
    box.appendChild(b);
  }
}
function syncTour() { $('btn-tour').setAttribute('aria-pressed', String(S.tour)); $('btn-tour').textContent = S.tour ? 'Touring' : 'Tour'; }
let panel = null;                             // compact layout: which panel is open over the cloud ('menu', 'settings', 'places'), if any
function setPanel(name) {
  panel = name;
  document.body.classList.toggle('xp-menu', panel === 'menu'); $('btn-menu').setAttribute('aria-expanded', String(panel === 'menu'));
  $('settings').hidden = isCompact() && panel !== 'settings'; $('btn-settings').setAttribute('aria-pressed', String(panel === 'settings'));
  main.classList.toggle('places-open', panel === 'places'); $('btn-places').setAttribute('aria-expanded', String(panel === 'places'));
}
const togglePanel = name => { setPanel(panel === name ? null : name); hideHint(); };
let hintGone = false;
function hideHint() { if (!hintGone) { hintGone = true; $('hint').classList.add('gone'); } }

let buildNo = 0;
function setStatus(text) { const s = $('status'); s.hidden = !text; s.textContent = text || ''; }
async function rebuild(kind, focus) {
  if (!INDEX) return;
  if (kind === 'arr') {
    const no = ++buildNo; let next;
    if (!arr) setStatus('Gathering words…');
    try { next = await chooseArrangement(focus); }
    catch (e) { if (no === buildNo) setStatus('The words could not be loaded. Check the connection and reload the page.'); return; }
    if (no !== buildNo) return;                    // a newer request overtook this one
    arr = next; setStatus('');
  } else if (!arr) return;
  clearSprites(); snapLayout = true; layoutStuck = 0;
  const keep = kind === 'style' ? { ...cam } : null;
  scene = buildScene();
  if (kind === 'arr') { fillPlaces(); if (selected && !arr.place.has(selected.id)) closeDetail(); $('arr-no').textContent = 'Arrangement ' + S.seed; }
  const total = arr.groups.reduce((s, G) => s + G.words.length, 0);
  $('tier-note').textContent = total ? `${total} words in ${arr.groups.length} places. Larger words are more basic.` : 'No words match these settings.';
  if (!total) setStatus('No words match these settings.');
  if (!arr.groups.length) { activeGroup = null; markPlaces(); fly = orbit = null; dirty = true; return; }
  if (keep) { Object.assign(cam, keep); dirty = true; if (orbit && activeGroup) { const a = orbit.a, t = orbit.time; orbit = { ...overview(activeGroup), a, time: t, w: orbit.w }; } return; }
  const G = (selected && arr.place.get(selected.id)) || arr.groups[0];
  gotoGroup(G, true);
  if (selected) { if (kind === 'arr') selectWord(selected); else gotoWord(selected); }
}

segControl('seg-world', [['sky', 'Sky'], ['mountains', 'Mountains'], ['city', 'City']], () => S.world, v => { if (v !== S.world) { S.world = v; savePrefs(); rebuild('world'); } });
segControl('seg-time', [['day', 'Day'], ['night', 'Night']], () => S.time, v => { if (v !== S.time) { S.time = v; savePrefs(); rebuild('style'); } });
segControl('seg-labels', [['ja', 'Japanese'], ['furi', '+ Furigana'], ['en', '+ English']], () => S.labels, v => { S.labels = v; savePrefs(); clearSprites(); dirty = true; });
segControl('seg-links', [['off', 'Off'], ['sel', 'Selected'], ['all', 'All']], () => S.links, v => { S.links = v; savePrefs(); dirty = true; });
chipControl('chips-tier', TIERS, S.tiers, () => rebuild('arr'));
chipControl('chips-cat', CATS, S.cats, () => rebuild('arr'));
function range(id, out, key, fmt, commit) { const r = $(id); r.value = S[key]; const show = () => { if (out) $(out).textContent = fmt(S[key]); }; show(); r.addEventListener('input', () => { S[key] = +r.value; show(); if (!commit) return; }); if (commit) r.addEventListener('change', commit); }
range('rng-groups', 'out-groups', 'nGroups', String, () => rebuild('arr'));
range('rng-per', 'out-per', 'perGroup', String, () => rebuild('arr'));
range('rng-speed', null, 'speed', String, null);
$('btn-new').onclick = () => { let s; do { s = (Math.random() * 9000 + 1000) | 0; } while (s === S.seed); S.seed = s; if (selected) closeDetail(); rebuild('arr'); };
$('btn-settings').onclick = () => togglePanel('settings');
$('btn-menu').onclick = () => togglePanel('menu');
$('settings-close').onclick = () => setPanel(null);
$('btn-places').onclick = () => togglePanel('places');
$('btn-tour').onclick = () => { S.tour = !S.tour; syncTour(); hideHint(); if (S.tour && arr && arr.groups.length) { if (selected) closeDetail(); gotoGroup(activeGroup && !orbit ? activeGroup : arr.groups[(arr.groups.indexOf(activeGroup) + 1) % arr.groups.length]); if (orbit) orbit.w = 0.055; } };
$('find').addEventListener('input', () => {
  const q = $('find').value.trim().toLowerCase(), box = $('find-results'); box.textContent = ''; if (!q || !scene) return;
  const res = []; for (const it of scene.labels.values()) { const w = it.w; if (plain(w.hw).includes(q) || w.r.includes(q) || w.g.toLowerCase().includes(q)) res.push(w); if (res.length >= 6) break; }
  if (!res.length) { box.appendChild(el('span', 'note', 'No word in this cloud matches.')); return; }
  for (const w of res) { const b = el('button'); b.type = 'button'; const j = el('span', null, plain(w.hw)); j.lang = 'ja'; b.append(j, el('span', 'g', shortGloss(w))); b.onclick = () => selectWord(w); box.appendChild(b); }
});

/* ------------------------------------------------------------------ start */
const coarse = matchMedia('(pointer: coarse)').matches;
$('hint').textContent = coarse ? 'Drag to look · pinch or hold the arrows to fly · tap a word' : 'Drag to look · scroll or W A S D to fly · click a word';
const siteNav = document.querySelector('.nav-header'); if (siteNav) { siteNav.id = siteNav.id || 'site-nav'; $('btn-menu').setAttribute('aria-controls', siteNav.id); }
setPanel(null); compactMQ.addEventListener('change', () => { setPanel(null); viewCenter(false); dirty = true; });
syncTour();
new ResizeObserver(resize).observe(stage);
resize();
requestAnimationFrame(frame);
(async () => {
  try { INDEX = await fetchJSON(BASE + 'index.json'); }
  catch (e) { setStatus('The words could not be loaded. Check the connection and reload the page.'); return; }
  for (const p of INDEX.places) PLACES.set(p.id, p);
  // explore.html?w=<entry id> opens the cloud around that entry
  let focus = null; const want = new URLSearchParams(location.search).get('w');
  if (want && /^\d{5}_[a-z0-9_]+$/.test(want)) {
    try { const refs = (await fetchJSON(`${BASE}w/${rangeOf(want)}.json`))[want]; if (refs && refs.length) focus = { id: want, pi: refs[0][0], si: refs[0][1] }; } catch (e) {}
  }
  await rebuild('arr', focus);
  if (focus && arr && arr.place.has(focus.id)) selectWord(WORDS.get(focus.id));
})();
window.__explore = { S, cam, get scene() { return scene; }, get arr() { return arr; }, get index() { return INDEX; }, get flying() { return !!fly; }, get selected() { return selected; }, selectWord, gotoGroup, rebuild, WORDS, get frameMs() { return frameMs; }, get hits() { return hits; }, get bodies() { return bodies; }, get U() { return U; } };
})();
