"""Inline-SVG chart helpers for the report (colors via CSS custom properties)."""
import math
from html import escape

BLUE = ["#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5", "#2a78d6", "#256abf",
        "#1c5cab", "#184f95", "#104281", "#0d366b"]


def ramp(v, lo, hi):
    """Sequential blue step for value v in [lo, hi]; returns (fill, text-color)."""
    t = 0 if hi == lo else max(0, min(1, (v - lo) / (hi - lo)))
    i = round(t * (len(BLUE) - 1))
    return BLUE[i], ("#ffffff" if i >= 6 else "#0b1a2e")


def heatmap(rows, cols, val, lo, hi, row_label, groups=None, fmt="{:.0f}", tip=None):
    """rows: list of row keys; groups: {row_key: group label shown before first row of group}."""
    cw, ch, lw, top = 84, 26, 200, 52
    gap_rows = sum(1 for r in rows if groups and r in groups)
    w = lw + cw * len(cols) + 8
    h = top + ch * len(rows) + gap_rows * 22 + 6
    out = [f'<svg class="chart heat" viewBox="0 0 {w} {h}" width="{w}" role="img" aria-label="Heat map">']
    for j, c in enumerate(cols):
        x = lw + j * cw + cw / 2
        words = c.split(" ", 1)
        for k, wd in enumerate(words):
            out.append(f'<text class="axis-lab" x="{x}" y="{top - 26 + 14 * k}" text-anchor="middle">{escape(wd)}</text>')
    y = top
    for r in rows:
        if groups and r in groups:
            out.append(f'<text class="grp-lab" x="0" y="{y + 15}">{escape(groups[r])}</text>')
            y += 22
        out.append(f'<text class="row-lab" x="{lw - 10}" y="{y + ch / 2 + 4}" text-anchor="end">{escape(row_label(r))}</text>')
        for j, c in enumerate(cols):
            v = val(r, c)
            x = lw + j * cw
            if v is None:
                out.append(f'<rect x="{x + 1}" y="{y + 1}" width="{cw - 2}" height="{ch - 2}" rx="3" class="cell-na"/>'
                           f'<text class="cell-txt na" x="{x + cw / 2}" y="{y + ch / 2 + 4}" text-anchor="middle">n/a</text>')
                continue
            fill, ink = ramp(v, lo, hi)
            t = escape(tip(r, c) if tip else f"{row_label(r)} · {c}: {fmt.format(v)}")
            out.append(f'<g class="hov"><title>{t}</title><rect x="{x + 1}" y="{y + 1}" width="{cw - 2}" height="{ch - 2}" rx="3" fill="{fill}"/>'
                       f'<text class="cell-txt" x="{x + cw / 2}" y="{y + ch / 2 + 4}" text-anchor="middle" fill="{ink}">{fmt.format(v)}</text></g>')
        y += ch
    out.append("</svg>")
    return "\n".join(out)


def scatter_logx(points, xlab, ylab, xmin, xmax, ymin, ymax, w=720, h=380):
    """points: dicts with x, y, cls ('dec'|'llm'), label, show(bool)."""
    ml, mr, mt, mb = 56, 24, 16, 48
    pw, ph = w - ml - mr, h - mt - mb
    lx0, lx1 = math.log10(xmin), math.log10(xmax)

    def X(v):
        return ml + (math.log10(v) - lx0) / (lx1 - lx0) * pw

    def Y(v):
        return mt + (1 - (v - ymin) / (ymax - ymin)) * ph
    out = [f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(ylab)} against {escape(xlab)}">']
    for e in range(math.ceil(lx0), math.floor(lx1) + 1):
        x = X(10 ** e)
        out.append(f'<line class="grid" x1="{x}" x2="{x}" y1="{mt}" y2="{mt + ph}"/>')
        lab = f"${10 ** e:g}" if e >= 0 else f"${10 ** e:.{-e}f}"
        out.append(f'<text class="tick" x="{x}" y="{mt + ph + 18}" text-anchor="middle">{lab}</text>')
    step = 0.1
    v = math.ceil(ymin / step) * step
    while v <= ymax + 1e-9:
        y = Y(v)
        out.append(f'<line class="grid" x1="{ml}" x2="{ml + pw}" y1="{y}" y2="{y}"/>')
        out.append(f'<text class="tick" x="{ml - 8}" y="{y + 4}" text-anchor="end">{v * 100:.0f}%</text>')
        v += step
    out.append(f'<text class="axis-lab" x="{ml + pw / 2}" y="{h - 8}" text-anchor="middle">{escape(xlab)}</text>')
    out.append(f'<text class="axis-lab" transform="translate(14 {mt + ph / 2}) rotate(-90)" text-anchor="middle">{escape(ylab)}</text>')
    for p in sorted(points, key=lambda p: p["cls"] == "llm"):
        x, y = X(p["x"]), Y(p["y"])
        shape = (f'<circle cx="{x}" cy="{y}" r="6" class="pt-{p["cls"]}"/>' if p["cls"] == "dec" else
                 f'<rect x="{x - 6}" y="{y - 6}" width="12" height="12" rx="2" class="pt-{p["cls"]}"/>')
        out.append(f'<g class="hov"><title>{escape(p["tip"])}</title>{shape}</g>')
        if p.get("show"):
            anchor = p.get("anchor", "start")
            dx = 10 if anchor == "start" else -10
            out.append(f'<text class="pt-lab" x="{x + dx}" y="{y + p.get("dy", 4)}" text-anchor="{anchor}">{escape(p["label"])}</text>')
    out.append("</svg>")
    return "\n".join(out)


def hbars(items, vmax, fmt, w=720, unit=""):
    """items: list of (label, value, cls, tip). Horizontal bars, one series color per cls."""
    lw, bh, gap, mt = 250, 18, 10, 6
    pw = w - lw - 70
    h = mt + len(items) * (bh + gap) + 4
    out = [f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="Bar chart">']
    for i, (lab, v, cls, tip) in enumerate(items):
        y = mt + i * (bh + gap)
        out.append(f'<text class="row-lab" x="{lw - 10}" y="{y + bh / 2 + 4}" text-anchor="end">{escape(lab)}</text>')
        bw = max(2, pw * (v / vmax)) if v else 0
        out.append(f'<g class="hov"><title>{escape(tip)}</title><rect x="{lw}" y="{y}" width="{pw}" height="{bh}" class="track"/>'
                   f'<rect x="{lw}" y="{y}" width="{bw}" height="{bh}" rx="3" class="bar-{cls}"/></g>')
        out.append(f'<text class="val" x="{lw + bw + 6}" y="{y + bh / 2 + 4}">{fmt(v)}{unit}</text>')
    out.append("</svg>")
    return "\n".join(out)


def grouped_bars(cats, series, val, w=720, h=300, ylab=""):
    """Vertical grouped bars. series: list of (key, label, cls)."""
    ml, mr, mt, mb = 48, 10, 14, 56
    pw, ph = w - ml - mr, h - mt - mb
    gw = pw / len(cats)
    bw = min(22, (gw - 16) / len(series))
    out = [f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(ylab)}">']
    for v in (0, 0.25, 0.5, 0.75, 1.0):
        y = mt + (1 - v) * ph
        out.append(f'<line class="grid" x1="{ml}" x2="{ml + pw}" y1="{y}" y2="{y}"/>'
                   f'<text class="tick" x="{ml - 8}" y="{y + 4}" text-anchor="end">{v * 100:.0f}%</text>')
    for i, (ck, clab) in enumerate(cats):
        gx = ml + i * gw + (gw - bw * len(series) - 2 * (len(series) - 1)) / 2
        for j, (sk, slab, cls) in enumerate(series):
            v = val(ck, sk)
            if v is None:
                continue
            x = gx + j * (bw + 2)
            bh_ = max(1.5, v * ph)
            out.append(f'<g class="hov"><title>{escape(slab)} · {escape(clab)}: {v * 100:.0f}%</title>'
                       f'<rect x="{x}" y="{mt + ph - bh_}" width="{bw}" height="{bh_}" rx="2" class="bar-{cls}"/></g>')
        lines = clab.split("\n")
        for k, ln in enumerate(lines):
            out.append(f'<text class="tick" x="{ml + i * gw + gw / 2}" y="{mt + ph + 16 + 13 * k}" text-anchor="middle">{escape(ln)}</text>')
    out.append(f'<line class="axis" x1="{ml}" x2="{ml + pw}" y1="{mt + ph}" y2="{mt + ph}"/>')
    out.append("</svg>")
    return "\n".join(out)
