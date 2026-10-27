#!/usr/bin/env python3
"""Independent exact checks by eigenvector/Poisson recursion.

Uses fractions and Gaussian elimination only: no characteristic polynomial,
finite differences, simulation, or external numerical packages are needed.
Heat is positive when delivered to the cold bath. Matrices act on columns.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def solve(a, b):
    n = len(b)
    t = [[F(x) for x in row] + [F(y)] for row, y in zip(a, b)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if t[i][k])
        t[k], t[pivot] = t[pivot], t[k]
        p = t[k][k]
        t[k] = [x / p for x in t[k]]
        for i in range(n):
            if i != k:
                p = t[i][k]
                t[i] = [x - p * y for x, y in zip(t[i], t[k])]
    return [row[-1] for row in t]


def mv(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def thermal_model(energies, pairs, scale=F(1)):
    """pairs=(lower-state, upper-state, hot-up/down, cold-up/down)."""
    edges = []
    for i, j, hu, hd, cu, cd in pairs:
        gap = energies[j] - energies[i]
        assert F(hu) / F(hd) == F(1, 2) ** gap
        if cu or cd:
            assert F(cu) / F(cd) == F(1, 4) ** gap
        for bath, up, down in [('h', hu, hd), ('c', cu, cd)]:
            if up or down:
                edges += [(i, j, F(up)*scale, -gap if bath == 'c' else 0),
                          (j, i, F(down)*scale, gap if bath == 'c' else 0)]
    return energies, edges


def cumulants(model, order=4):
    energies, edges = model
    size = len(energies)
    deriv = [[[F(0) for _ in range(size)] for _ in range(size)]
             for _ in range(order+1)]
    for source, dest, rate, heat in edges:
        deriv[0][source][source] -= rate
        for k in range(order+1):
            deriv[k][dest][source] += rate * F(heat)**k
    generator = deriv[0]
    constrained = generator[:-1] + [[F(1)] * size]
    pi = solve(constrained, [F(0)]*(size-1)+[F(1)])
    assert mv(generator, pi) == [0]*size
    assert all(p > 0 for p in pi)
    assert all(sum(generator[i][j] for i in range(size)) == 0
               for j in range(size))
    vectors, rates = [pi], [F(0)]
    for n in range(1, order+1):
        forcing = [F(0)] * size
        for k in range(1, n+1):
            term = mv(deriv[k], vectors[n-k])
            forcing = [a + comb(n,k)*b for a,b in zip(forcing,term)]
        rate = sum(forcing)
        rates.append(rate)
        rhs = [rate*p-a for p,a in zip(pi,forcing)]
        for k in range(1,n):
            rhs = [a+comb(n,k)*rates[k]*b
                   for a,b in zip(rhs,vectors[n-k])]
        vector = solve(constrained,rhs[:-1]+[F(0)])
        assert sum(vector) == 0 and mv(generator,vector) == rhs
        vectors.append(vector)
    return pi, rates[1:]


def simple(eps):
    return thermal_model([0,1,0], [(0,1,1,2,1,4), (0,2,eps,eps,0,0)])


def full_support(eps):
    lam = F(40)/(40+32*eps+8*eps*eps)
    return thermal_model([0,2,1], [
        (0,1,1,4,F(1,2),8),
        (0,2,8*eps,16*eps,eps,4*eps),
        (2,1,eps*eps,2*eps*eps,4*eps*eps,16*eps*eps)
    ], lam)


def certify():
    cases = []
    for den in [100,1000,10000]:
        eps = F(1,den)
        pi, c = cumulants(simple(eps))
        expected = [F(1,7), (6+145*eps)/(343*eps),
                    (1531*eps*eps+2595*eps-18)/(16807*eps*eps),
                    (214549*eps**3+402264*eps*eps-15924*eps-792)
                    /(823543*eps**3)]
        assert c == expected and pi == [F(3,7),F(1,7),F(3,7)]
        cases.append({'model':'simple','epsilon':str(eps),
                      'pi':list(map(str,pi)),'cumulants':list(map(str,c)),
                      'S':str(c[2]/c[0]),'K':str(c[3]/c[1])})
    for den in [1000,10000,100000,1000000]:
        eps=F(1,den)
        pi,c=cumulants(full_support(eps))
        assert pi == [F(40,63),F(5,63),F(18,63)]
        assert c[0] == F(40,63) and c[1] > 0
        if den>=10000:
            assert c[2]<0 and c[3]<0
        cases.append({'model':'full_support_fixed_stationary',
                      'epsilon':str(eps),'pi':list(map(str,pi)),
                      'cumulants':list(map(str,c)),
                      'S':str(c[2]/c[0]),'K':str(c[3]/c[1]),
                      'epsilon_squared_S':float(eps**2*c[2]/c[0]),
                      'epsilon_squared_K':float(eps**2*c[3]/c[1])})
    expected_S,expected_K=-F(16,21609),-F(16,64827)
    # Exact rational finite certificates plus convergence diagnostics.
    output={'method':'Exact eigenvector/Poisson recursion',
            'all_assertions_passed':True,'cases':cases,
            'full_support_limits':{'epsilon_squared_S':str(expected_S),
                                   'epsilon_squared_K':str(expected_K)}}
    dest=Path(__file__).resolve().parent.parent/'evidence'/'poisson_certificate.json'
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(output,indent=2)+'\n')
    for case in cases:
        print(case['model'],case['epsilon'],
              'S=',float(F(case['S'])),'K=',float(F(case['K'])))
    print('All exact rational assertions passed; certificate:',dest)


if __name__=='__main__':
    certify()
