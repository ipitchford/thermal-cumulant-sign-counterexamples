"""Independent exact audit of the thermal proof's polynomial identities.

No imports from either other verification implementation. Only standard library.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial
from pathlib import Path
import json


class Poly:
    def __init__(self, d=None, n=3, cap=None):
        self.n, self.cap = n, cap
        self.d = {m: F(c) for m, c in (d or {}).items() if c}

    def same(self, d):
        return Poly(d, self.n, self.cap)

    def const(self, x):
        return self.same({(0,) * self.n: F(x)})

    def coerce(self, x):
        return x if isinstance(x, Poly) else self.const(x)

    def __add__(self, other):
        other = self.coerce(other)
        d = self.d.copy()
        for m, c in other.d.items():
            d[m] = d.get(m, F()) + c
        return self.same(d)

    __radd__ = __add__

    def __neg__(self):
        return self.same({m: -c for m, c in self.d.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        d = {}
        for m, c in self.d.items():
            for n, e in other.d.items():
                z = tuple(a + b for a, b in zip(m, n))
                if self.cap is not None and z[0] > self.cap:
                    continue
                d[z] = d.get(z, F()) + c * e
        return self.same(d)

    __rmul__ = __mul__

    def __pow__(self, k):
        p = self.const(1)
        for _ in range(k):
            p = p * self
        return p


def variables(n, cap=None):
    return [Poly({tuple(int(i == j) for i in range(n)): 1}, n, cap)
            for j in range(n)]


def determinant(M):
    z = M[0][0].const(0)
    for p in permutations(range(len(M))):
        inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))
        term = M[0][0].const((-1)**inv)
        for i, j in enumerate(p):
            term = term * M[i][j]
        z = z + term
    return z


results = {}

# Exact general active-pair-plus-trap identity, with t=exp(E z).
# Variable order: x, eps, a, b, c, d, alpha, beta, t.
x, eps, a, b, c, d, alpha, beta, t = variables(9)
tinv = Poly({(0,)*8 + (-1,): 1}, n=9)
u, v = a+c, b+d
M = [[x+u+eps*alpha, -(b+d*t), -eps*beta],
     [-(a+c*tinv), x+v, x.const(0)],
     [-eps*alpha, x.const(0), x+eps*beta]]
delta = a*d*(t-1)+b*c*(tinv-1)
claimed = x**3+(u+v+eps*(alpha+beta))*x**2+eps*(beta*(u+v)+alpha*v)*x-(x+eps*beta)*delta
assert not (determinant(M)-claimed).d
results['general_trap_characteristic_identity'] = True

# The two-state feasibility-bound identities, independent symbolic expansion.
f, y = variables(2)
N = f-6*f*f+(72*f-8)*y-120*y*y
lo = f*F(1,2)-F(1,16)
Nl = f-6*f*f+(72*f-8)*lo-120*lo*lo
assert not (Nl-F(1,32)).d
tt, = variables(1)
H = 1-F(7,2)*tt+F(9,2)*tt**2-F(15,8)*tt**3
bern = (1-tt)**4+F(1,2)*tt*(1-tt)**3+F(5,8)*tt**3*(1-tt)+F(1,8)*tt**4
assert not (H-bern).d
Nu = f-6*f*f+(72*f-8)*f*f-120*f**4
Hu = f*(1-14*f+72*f*f-120*f**3)
assert not (Nu-Hu).d
results['two_state_endpoint_and_positive_decomposition_identities'] = True

# Full-support family: substitute x=eps*y and z=eps*k first, then expand
# every entry through eps^2 and take the determinant. Variable order eps,y,k.
e, yy, kk = variables(3, cap=2)
E = [0, 2, 1]
# bath, source, destination, constant, power of epsilon
channels = [
    ('h',0,1,F(1),0), ('h',1,0,F(4),0),
    ('c',0,1,F(1,2),0), ('c',1,0,F(8),0),
    ('h',0,2,F(8),1), ('h',2,0,F(16),1),
    ('c',0,2,F(1),1), ('c',2,0,F(4),1),
    ('h',2,1,F(1),2), ('h',1,2,F(2),2),
    ('c',2,1,F(4),2), ('c',1,2,F(16),2),
]
W = [[e.const(0) for _ in E] for _ in E]
for bath, source, dest, rate, deg in channels:
    heat = E[source]-E[dest] if bath == 'c' else 0
    tilted = sum((rate*F(heat**j, factorial(j))*(e**(deg+j))*(kk**j)
                  for j in range(3-deg)), e.const(0))
    W[dest][source] = W[dest][source]+tilted
    W[source][source] = W[source][source]-rate*(e**deg)
M = [[-W[i][j]+(e*yy if i==j else 0) for j in range(3)] for i in range(3)]
D = determinant(M)
expected = F(27,2)*e**2*(yy**2+(28-F(8,9)*kk)*yy-F(160,9)*kk)
assert not (D-expected).d
results['full_family_scaled_characteristic_coefficient'] = {
    'eps0': '0', 'eps1': '0',
    'eps2': '(27/2)*(y^2+(28-8*k/9)*y-160*k/9)',
}

# Derive the limiting cumulants from its quadratic through an independent
# power-series recurrence. q[n] is the coefficient of k^n, not its derivative.
q = [F(0)]*5
s, j, b = F(28), F(8,9), F(20)
q[1] = b*j/s
for n in range(2,5):
    q[n] = (j*q[n-1]-sum((q[i]*q[n-i] for i in range(1,n)), F()))/s
cn = [q[n]*factorial(n) for n in range(1,5)]
assert cn == [F(40,63),F(320,27783),F(-640,1361367),F(-5120,1801088541)]
assert cn[2]/cn[0] == F(-16,21609)
assert cn[3]/cn[1] == F(-16,64827)
results['limiting_derivatives'] = list(map(str,cn))
results['limiting_ratio_coefficients'] = [str(cn[2]/cn[0]),str(cn[3]/cn[1])]

# Fixed stationary law and cold heat current, as polynomial identities.
pi = [F(40,63),F(5,63),F(18,63)]
W0 = [[e.const(0) for _ in E] for _ in E]
current = e.const(0)
for bath, source, dest, rate, deg in channels:
    W0[dest][source] = W0[dest][source]+rate*e**deg
    W0[source][source] = W0[source][source]-rate*e**deg
    if bath=='c':
        current = current + pi[source]*rate*e**deg*(E[source]-E[dest])
for row in W0:
    assert not sum((x*p for x,p in zip(row,pi)), e.const(0)).d
assert not (current-(40+32*e+8*e**2)*F(1,63)).d
results['stationarity_and_current_polynomial_identities'] = True
results['all_assertions_passed'] = True
out = Path(__file__).resolve().parent.parent/'evidence'/'independent_scaling_certificate.json'
out.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
