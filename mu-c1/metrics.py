def f_score(fp, fn, tp):
    return (2 * tp) / ((2 * tp) + fp + fn) if (2 * tp) + fp + fn else 0


def kappa(tn, fp, fn, tp, rand_tn, rand_fp, rand_fn, rand_tp):
    obs_acc = acc(tn, fp, fn, tp)
    rand_acc = acc(rand_tn, rand_fp, rand_fn, rand_tp)
    return (obs_acc - rand_acc) / (1 - rand_acc) if (1 - rand_acc) else 0


def pct_dth(tn, fp, fn, tp):
    dth_fpr = fpr(tn, fp)
    dth_fnr = fnr(fn, tp)
    return ((dth_fnr ** 2 + dth_fpr ** 2) ** 0.5) / (2 ** 0.5)


def inform(tn, fp, fn, tp):
    inform_tpr = tpr(fn, tp)
    inform_tnr = tnr(tn, fp)
    return inform_tpr + inform_tnr - 1


def acc(tn, fp, fn, tp):
    return (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) else 0


def tnr(tn, fp):
    return tn / (tn + fp) if (tn + fp) else 0


def fpr(tn, fp):
    return fp / (fp + tn) if (fp + tn) else 0


def tpr(fn, tp):
    return tp / (tp + fn) if (tp + fn) else 0


def fnr(fn, tp):
    return fn / (fn + tp) if (fn + tp) else 0
