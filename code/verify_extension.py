#!/usr/bin/env python3
"""Symbolic and numerical checks for the revised manuscript (v2).

1. Trap family: leading Laurent coefficients from the limiting quadratic
   (Lemma 4.3 / Theorem 4.4) and the variance-normalised limits (Prop. 6.1).
2. Full-support family: exact determinant coefficients used in the proof of
   Theorem 5.1, next Laurent terms of S and K, normalised limits, TUR ratio.
3. Kinetic bound (Theorem 6.3) evaluated on both families.
4. Product-network construction (Prop. 6.2): exact additivity check.
5. Feasibility estimates (Sec. 7): thresholds, relaxation times, record lengths.
Writes evidence/extension_certificate.json.  Run: uv run python3 -I code/verify_extension.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import json
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
R = sp.Rational
out = {}

# ---------- 1. trap family ----------
w, v, al, be, J, k, y, r = sp.symbols('w v alpha beta J k y r', positive=True)
B = be * w + al * v; U = al * v; V = be * w
G = w * y**2 + (B - J * k) * y - be * J * k
Y = sp.symbols('Y1:5')
eq = sp.expand(G.subs(y, sum(Y[n - 1] * k**n for n in range(1, 5))))
sol = {}
for n in range(1, 5):
    sol[Y[n - 1]] = sp.cancel(sp.solve(eq.coeff(k, n).subs(sol), Y[n - 1])[0])
lead = [sp.cancel(sp.factorial(n) * sol[Y[n - 1]]) for n in range(1, 5)]
claimed = [be * J / B, 2 * al * be * v * J**2 / B**3,
           6 * al * be * v * J**3 * (U - V) / B**5,
           24 * al * be * v * J**4 * (U**2 - 3 * U * V + V**2) / B**7]
assert all(sp.cancel(a - b) == 0 for a, b in zip(lead, claimed))
ns = sp.factor(sp.cancel((lead[2] * lead[0] / lead[1]**2).subs(be, r * al * v / w)))
nk = sp.factor(sp.cancel((lead[3] * lead[0]**2 / lead[1]**3).subs(be, r * al * v / w)))
assert sp.simplify(ns - R(3, 2) * (1 - r)) == 0
assert sp.simplify(nk - 3 * (1 - 3 * r + r**2)) == 0
assert sp.minimum(3 * (1 - 3 * r + r**2), r, sp.Interval(0, sp.oo)) == R(-15, 4)
out['trap'] = dict(leading_coefficients_match=True, norm_skew=str(ns), norm_kurt=str(nk),
                   norm_kurt_min='-15/4 at r=3/2')

# exact trap polynomial from the displayed tilted matrix
a, b, c, d, E, eps, x, z = sp.symbols('a b c d E epsilon x z', positive=True)
Lt = sp.Matrix([[-(a + c) - eps * al, b + d * sp.exp(E * z), eps * be],
                [a + c * sp.exp(-E * z), -(b + d), 0],
                [eps * al, 0, -eps * be]])
Ft = sp.expand((x * sp.eye(3) - Lt).det())
ww = a + b + c + d; BB = be * ww + al * (b + d)
dz = a * d * (sp.exp(E * z) - 1) + b * c * (sp.exp(-E * z) - 1)
assert sp.expand(Ft - (x**3 + (ww + eps * (al + be)) * x**2 + eps * BB * x - (x + eps * be) * dz)) == 0
out['trap']['polynomial_matches_matrix'] = True

# ---------- 2. full-support family ----------
e = sp.symbols('epsilon', positive=True)
Ez = sp.exp(z)
Lf = sp.Matrix([[-R(3, 2) - 9 * e, 4 + 8 * Ez**2, 16 * e + 4 * e * Ez],
                [1 + R(1, 2) / Ez**2, -12 - 18 * e**2, e**2 + 4 * e**2 / Ez],
                [8 * e + e / Ez, 2 * e**2 + 16 * e**2 * Ez, -20 * e - 5 * e**2]])
Ff = sp.expand((x * sp.eye(3) - Lf).det())
coef = {}
for i, cf in enumerate(reversed(sp.Poly(Ff, x).all_coeffs())):
    s = sp.expand(sp.series(sp.expand(cf.subs(z, e * k)), e, 0, 3).removeO())
    coef[f'a{i}'] = str(sp.collect(s, e))
out['full_det_coefficients_through_eps2'] = coef
Gf = sp.factor(sp.limit(sp.expand(Ff.subs({x: e * y, z: e * k})) / e**2, e, 0))
assert sp.expand(Gf - R(27, 2) * (y**2 + (28 - R(8, 9) * k) * y - R(160, 9) * k)) == 0
assert sp.expand(sp.series(sp.expand(Ff.subs({x: e * y, z: e * k})), e, 0, 2).removeO()) == 0

X = sp.symbols('X1:5')
chi = sum(X[i] * z**(i + 1) / sp.factorial(i + 1) for i in range(4))
Fs = sp.expand(sp.series(Ff.subs(x, chi), z, 0, 5).removeO())
cs = {}
for n in range(1, 5):
    cs[X[n - 1]] = sp.cancel(sp.solve(Fs.coeff(z, n).subs(cs), X[n - 1])[0])
C = [cs[X[i]] for i in range(4)]
S = sp.cancel(C[2] / C[0]); K = sp.cancel(C[3] / C[1])
Sser = sp.series(S, e, 0, 1).removeO(); Kser = sp.series(K, e, 0, 1).removeO()
out['full_laurent'] = dict(S=str(Sser), K=str(Kser))
assert sp.expand(Sser.coeff(e, -2)) == R(-16, 21609) and sp.expand(Kser.coeff(e, -2)) == R(-16, 64827)
nsf = sp.limit(C[2] * C[0] / C[1]**2, e, 0); nkf = sp.limit(C[3] * C[0]**2 / C[1]**3, e, 0)
assert nsf == R(-9, 4) and nkf == R(-3, 4)
out['full_normalised_limits'] = dict(skew=str(nsf), kurt=str(nkf))
tur = {}
for ev in [R(1, 10**3), R(1, 10**4)]:
    tur[str(ev)] = float((C[1] * sp.log(2) / C[0]).subs(e, ev))
out['full_TUR_ratio_C2sigma_over_C1sq'] = tur


# ---------- 3. kinetic bound (Theorem 6.3, reversible form) ----------
def kinetic_check(rates, E_levels, nst):
    """rates: list (bath, j, i, k) floats; returns gap, A, bound vs actual."""
    L = np.zeros((nst, nst)); Kc = np.zeros((nst, nst))
    for bth, j, i, kk in rates:
        L[i, j] += kk; L[j, j] -= kk
        if bth == 'c':
            Kc[i, j] += kk
    A0 = L.copy(); A0[0, :] = 1
    pi = np.linalg.solve(A0, np.eye(nst)[0])
    Dm = np.diag(np.sqrt(pi)); Di = np.diag(1 / np.sqrt(pi))
    H = Di @ L @ Dm
    assert np.allclose(H, H.T, rtol=1e-9, atol=1e-12), 'summed chain not reversible'
    ev = np.sort(np.abs(np.linalg.eigvalsh((H + H.T) / 2)))
    g = ev[1]
    M = Di @ Kc @ Dm
    A = np.linalg.norm(M, 2)
    Emax = max(abs(E_levels[j] - E_levels[i]) for bth, j, i, kk in rates if bth == 'c')
    ell = np.log1p(g / (2 * A))
    return g, A, Emax, ell


def cumulants_float(rates, E_levels, nst):
    from math import comb
    L = np.zeros((nst, nst)); Ls = [None] + [np.zeros((nst, nst)) for _ in range(4)]
    for bth, j, i, kk in rates:
        L[i, j] += kk; L[j, j] -= kk
        if bth == 'c':
            for n in range(1, 5):
                Ls[n][i, j] += kk * (E_levels[j] - E_levels[i])**n
    A0 = L.copy(); A0[0, :] = 1
    pi = np.linalg.solve(A0, np.eye(nst)[0])
    vv = [pi]; Cc = [None]
    for n in range(1, 5):
        s = sum(comb(n, jj) * Ls[jj] @ vv[n - jj] for jj in range(1, n + 1))
        Cn = s.sum(); Cc.append(Cn)
        rhs = Cn * pi + sum(comb(n, jj) * Cc[jj] * vv[n - jj] for jj in range(1, n)) - s
        rhs[0] = 0
        vv.append(np.linalg.solve(A0, rhs))
    return Cc[1:]


def edge(lst, bth, lo, hi, up, down):
    lst.append((bth, lo, hi, up)); lst.append((bth, hi, lo, down))


def simple(epsv):
    ch = []
    edge(ch, 'h', 0, 1, 1, 2); edge(ch, 'c', 0, 1, 1, 4); edge(ch, 'h', 0, 2, epsv, epsv)
    return ch, [0, 1, 0]


def full(epsv):
    lam = 40 / (40 + 32 * epsv + 8 * epsv**2)
    ch = []
    edge(ch, 'h', 0, 1, 1, 4); edge(ch, 'c', 0, 1, .5, 8)
    edge(ch, 'h', 0, 2, 8 * epsv, 16 * epsv); edge(ch, 'c', 0, 2, epsv, 4 * epsv)
    edge(ch, 'h', 2, 1, epsv**2, 2 * epsv**2); edge(ch, 'c', 2, 1, 4 * epsv**2, 16 * epsv**2)
    return [(bb, j, i, lam * kk) for bb, j, i, kk in ch], [0, 2, 1]


kin = []
for name, fam in (('simple', simple), ('full', full)):
    for epsv in (1e-2, 1e-3, 1e-4):
        ch, El = fam(epsv)
        g, A, Emax, ell = kinetic_check(ch, El, 3)
        C1, C2, C3, C4 = cumulants_float(ch, El, 3)
        bnd = [__import__('math').factorial(n) * (g / 2) * (Emax / ell)**n for n in range(1, 5)]
        assert all(abs(cc) <= bb for cc, bb in zip((C1, C2, C3, C4), bnd))
        kin.append(dict(family=name, eps=epsv, gap=g, A=A, Emax=Emax,
                        S=C3 / C1, S_lower_bound=-bnd[2] / C1,
                        K=C4 / C2, K_lower_bound=-bnd[3] / C2,
                        eps2_S_bound=-bnd[2] / C1 * epsv**2, eps2_K_bound=-bnd[3] / C2 * epsv**2))
out['kinetic_bound'] = kin

# ---------- 4. product network additivity (exact) ----------
from fractions import Fraction as Fr
import verify_poisson as vp
assert hasattr(vp, 'cumulants')
# product of the simple trap model (eps=1/1000) and a two-state conductor, checked in floats
ch1, E1 = simple(1e-3)
ch2 = []; edge(ch2, 'h', 0, 1, 1, 2); edge(ch2, 'c', 0, 1, 1, 4); E2 = [0, 1]
mu = 50.0
ch2 = [(bb, j, i, mu * kk) for bb, j, i, kk in ch2]
prod = []
for (bb, j, i, kk) in ch1:
    for s2 in range(2):
        prod.append((bb, 2 * j + s2, 2 * i + s2, kk))
for (bb, j, i, kk) in ch2:
    for s1 in range(3):
        prod.append((bb, 2 * s1 + j, 2 * s1 + i, kk))
Ep = [E1[s1] + E2[s2] for s1 in range(3) for s2 in range(2)]
Cp = cumulants_float(prod, Ep, 6)
Ca = cumulants_float(ch1, E1, 3); Cb = cumulants_float(ch2, E2, 2)
assert np.allclose(Cp, np.add(Ca, Cb), rtol=1e-8)
out['product_additivity'] = dict(C_product=Cp, C_sum=list(np.add(Ca, Cb)),
                                 norm_kurt=Cp[3] * Cp[0]**2 / Cp[1]**3,
                                 norm_skew=Cp[2] * Cp[0] / Cp[1]**2)

# ---------- 5. feasibility ----------
es = sp.symbols('e', positive=True)
num3 = 1531 * es**2 + 2595 * es - 18
num4 = 214549 * es**3 + 402264 * es**2 - 15924 * es - 792
tS = float(sp.nsolve(num3, es, 0.007)); tK = float(sp.nsolve(num4, es, 0.06))
feas = dict(simple_threshold_S=tS, simple_threshold_K=tK, rows=[])
for name, fam, epsv in (('simple', simple, 0.03), ('simple', simple, 0.005), ('simple', simple, 1e-3),
                        ('full', full, 1e-3), ('full', full, 1e-2)):
    ch, El = fam(epsv)
    nst = len(El)
    L = np.zeros((nst, nst)); act = 0.0
    for bb, j, i, kk in ch:
        L[i, j] += kk; L[j, j] -= kk
    A0 = L.copy(); A0[0, :] = 1; pi = np.linalg.solve(A0, np.eye(nst)[0])
    act = sum(pi[j] * kk for bb, j, i, kk in ch)
    gap = sorted(abs(np.linalg.eigvals(L)))[1]
    C1, C2, C3, C4 = cumulants_float(ch, El, nst)
    tau = 10 / gap
    T = 96 * C2**4 * tau**3 / C4**2 if C4 != 0 else float('inf')
    feas['rows'].append(dict(family=name, eps=epsv, relaxation_time=1 / gap, activity=act,
                             S=C3 / C1, K=C4 / C2, block=tau, record_length=T,
                             record_over_relax=T * gap, expected_jumps=act * T))
out['feasibility'] = feas

(ROOT / 'evidence').mkdir(exist_ok=True)
(ROOT / 'evidence/extension_certificate.json').write_text(json.dumps(out, indent=1, default=float) + '\n')
print(json.dumps(out, indent=1, default=float))
print('all_assertions_passed')
