#!/usr/bin/env python3
"""Random census of three-state, two-bath thermal networks (numerical evidence only).

Samples networks with bathwise local detailed balance, computes the cold-bath
heat cumulants C1..C4 by the Poisson recursion in floating point, and rechecks
every sign violation with exact rational arithmetic.  Writes evidence/census.json.
Run from any directory:  uv run python3 -I code/census.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import json
from fractions import Fraction as Fr
from math import comb
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
N = 3
PAIRS = [(i, j) for i in range(N) for j in range(i)]


def float_cumulants(L, Ls, pi):
    one = np.ones(N)
    A = L.copy(); A[0, :] = 1.0
    v = [pi]; C = [None]
    for n in range(1, 5):
        s = sum(comb(n, j) * Ls[j] @ v[n - j] for j in range(1, n + 1))
        Cn = one @ s; C.append(Cn)
        rhs = Cn * pi + sum(comb(n, j) * C[j] * v[n - j] for j in range(1, n)) - s
        rhs[0] = 0.0
        v.append(np.linalg.solve(A, rhs))
    return C[1:]


def exact_cumulants(rates, E):
    """rates: list of (bath, j, i, k) with Fraction k; transition j->i."""
    L = [[Fr(0)] * N for _ in range(N)]
    Ls = [None] + [[[Fr(0)] * N for _ in range(N)] for _ in range(4)]
    for b, j, i, kk in rates:
        L[i][j] += kk; L[j][j] -= kk
        if b == 'c':
            for n in range(1, 5):
                Ls[n][i][j] += kk * (E[j] - E[i]) ** n

    def solve(M, rhs):
        M = [row[:] + [r] for row, r in zip(M, rhs)]
        for c in range(N):
            p = next(r for r in range(c, N) if M[r][c] != 0)
            M[c], M[p] = M[p], M[c]
            for r in range(N):
                if r != c and M[r][c] != 0:
                    f = M[r][c] / M[c][c]
                    M[r] = [a - f * bb for a, bb in zip(M[r], M[c])]
        return [M[r][N] / M[r][r] for r in range(N)]

    A = [row[:] for row in L]; A[0] = [Fr(1)] * N
    pi = solve(A, [Fr(1)] + [Fr(0)] * (N - 1))
    mv = lambda M, x: [sum(M[r][c] * x[c] for c in range(N)) for r in range(N)]
    v = [pi]; C = [None]
    for n in range(1, 5):
        s = [sum(comb(n, j) * mv(Ls[j], v[n - j])[r] for j in range(1, n + 1)) for r in range(N)]
        Cn = sum(s); C.append(Cn)
        rhs = [Cn * pi[r] + sum(comb(n, j) * C[j] * v[n - j][r] for j in range(1, n)) - s[r] for r in range(N)]
        rhs[0] = Fr(0)
        v.append(solve(A, rhs))
    return C[1:]


def build(E, betas, k_low):
    """k_low[(pair,bath)] = rate j->i for i>j (index order); reverse by LDB."""
    L = np.zeros((N, N)); Ls = [None] + [np.zeros((N, N)) for _ in range(4)]
    rates = []
    for (i, j) in PAIRS:
        for bname, beta in zip('hc', betas):
            kij = k_low[(i, j, bname)]
            kji = kij * np.exp(beta * (E[i] - E[j]))
            for (r, s, kk) in ((i, j, kij), (j, i, kji)):
                L[r, s] += kk; L[s, s] -= kk
                rates.append((bname, s, r, kk))
                if bname == 'c':
                    for n in range(1, 5):
                        Ls[n][r, s] += kk * (E[s] - E[r]) ** n
    ks = [kk for *_, kk in rates]
    if not np.all(np.isfinite(ks)) or max(ks) / min(ks) > 1e12:
        return None
    A = L.copy(); A[0, :] = 1.0
    pi = np.linalg.solve(A, np.eye(N)[0])
    return L, Ls, pi, rates


def sample(rng, scheme, spread):
    if scheme == 'source':          # Ptaszynski (2022) Sec. III D scheme
        e = rng.uniform(0, 1, N); E = e / (1 - e)
        t = rng.uniform(0, 1, 2); T = np.sort(t / (1 - t))[::-1]   # hot, cold
        k_low = {(i, j, b): rng.uniform(0, 1) for (i, j) in PAIRS for b in 'hc'}
    else:                            # log-uniform prefactors over `spread` decades
        E = rng.uniform(0, 3, N)
        T = np.sort(1 / rng.uniform(0.2, 3, 2))[::-1]
        k_low = {(i, j, b): 10 ** rng.uniform(-spread, 0) for (i, j) in PAIRS for b in 'hc'}
    return E, 1 / T, k_low


def run(scheme, spread, n, seed):
    rng = np.random.default_rng(seed)
    out = dict(scheme=scheme, spread_decades=spread, samples=n, S_neg=0, K_neg=0,
               min_disparity_violation=None, min_norm_skew=None, min_norm_kurt=None)
    for _ in range(n):
        E, betas, k_low = sample(rng, scheme, spread)
        with np.errstate(over='ignore'):
            built = build(E, betas, k_low)
        if built is None:
            out['skipped_ill_conditioned'] = out.get('skipped_ill_conditioned', 0) + 1
            continue
        L, Ls, pi, rates = built
        C1, C2, C3, C4 = float_cumulants(L, Ls, pi)
        if C1 <= 1e-12 or C2 <= 0:
            continue
        ns, nk = C3 * C1 / C2 ** 2, C4 * C1 ** 2 / C2 ** 3
        out['min_norm_skew'] = ns if out['min_norm_skew'] is None else min(ns, out['min_norm_skew'])
        out['min_norm_kurt'] = nk if out['min_norm_kurt'] is None else min(nk, out['min_norm_kurt'])
        if C3 < 0 or C4 < 0:
            Ef = [Fr(float(x)) for x in E]
            ex = exact_cumulants([(b, j, i, Fr(float(kk))) for b, j, i, kk in rates], Ef)
            s_neg, k_neg = ex[2] / ex[0] < 0, ex[3] / ex[1] < 0
            out['S_neg'] += int(s_neg); out['K_neg'] += int(k_neg)
            if s_neg or k_neg:
                ks = [kk for *_, kk in rates]
                disp = max(ks) / min(ks)
                m = out['min_disparity_violation']
                out['min_disparity_violation'] = disp if m is None else min(m, disp)
    out['frac_S_neg'] = out['S_neg'] / n
    out['frac_K_neg'] = out['K_neg'] / n
    return out


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
    res = [run('source', None, n, 1)]
    for i, sp in enumerate([0.5, 1, 2, 3, 4]):
        res.append(run('loguniform', sp, n, 10 + i))
        print(res[-1], flush=True)
    print(res[0])
    (ROOT / 'evidence').mkdir(exist_ok=True)
    (ROOT / 'evidence/census.json').write_text(json.dumps(res, indent=1) + '\n')
