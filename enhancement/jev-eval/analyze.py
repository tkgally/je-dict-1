import json, sys, collections
def auc(pos, neg):
    """Probability a random positive scores higher than a random negative (ties 0.5)."""
    pos = [p for p in pos if p is not None]; neg = [n for n in neg if n is not None]
    if not pos or not neg: return None
    s = 0.0
    for p in pos:
        for n in neg:
            s += 1.0 if p > n else 0.5 if p == n else 0.0
    return s / (len(pos) * len(neg))
def pr_at(scores_labels, thr, pos_label):
    tp = sum(1 for s, l in scores_labels if s is not None and s >= thr and l == pos_label)
    fp = sum(1 for s, l in scores_labels if s is not None and s >= thr and l != pos_label)
    fn = sum(1 for s, l in scores_labels if s is not None and s < thr and l == pos_label)
    prec = tp / (tp + fp) if tp + fp else None; rec = tp / (tp + fn) if tp + fn else None
    return tp, fp, fn, prec, rec
