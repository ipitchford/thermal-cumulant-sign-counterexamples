"""Exact rational verification of the fully coupled thermal counterexample.
Only Python standard library. Run from any directory using this file's path.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial
import json
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from determinant_series import analyse,edge
from pathlib import Path

def family(eps):
 ch=[]
 edge(ch,'hot',0,1,1,4);edge(ch,'cold',0,1,F(1,2),8)
 edge(ch,'hot',0,2,8*eps,16*eps);edge(ch,'cold',0,2,eps,4*eps)
 edge(ch,'hot',2,1,eps**2,2*eps**2);edge(ch,'cold',2,1,4*eps**2,16*eps**2)
 return ch

E=[0,2,1]; pi=[F(40,63),F(5,63),F(18,63)]
reports=[]
for eps in [F(1,1000),F(1,10000),F(1,100000)]:
 ch=family(eps)
 rates={(b,j,i):r for b,j,i,r in ch}
 assert len(rates)==12 and all(r>0 for r in rates.values())
 for (b,j,i),r in rates.items():
  base=F(2 if b=='hot' else 4)
  assert r/rates[(b,i,j)]==base**(E[j]-E[i])
 balance=[F(0)]*3
 for b,j,i,r in ch:
  balance[i]+=pi[j]*r;balance[j]-=pi[j]*r
 assert balance==[F(0)]*3
 J=sum(pi[j]*r*(E[j]-E[i]) for b,j,i,r in ch if b=='cold')
 assert J==(40+32*eps+8*eps**2)/63
 cs,_=analyse(E,ch)
 assert cs[0]==J and cs[1]>0 and cs[2]<0 and cs[3]<0
 lam=F(40)/(40+32*eps+8*eps**2)
 scaled=[lam*c for c in cs]
 assert scaled[0]==F(40,63)
 rec={'epsilon':str(eps),'lambda':str(lam),'stationary':[str(v) for v in pi],
      'cumulants':[str(c) for c in scaled],
      'S':str(cs[2]/cs[0]),'K':str(cs[3]/cs[1]),
      'S_float':float(cs[2]/cs[0]),'K_float':float(cs[3]/cs[1]),
      'stationarity':True,'local_detailed_balance':True,'exact_cumulants':True,
      'strict_negative_C3_C4':True,'full_support':True}
 reports.append(rec)
 print('epsilon',eps, 'S',rec['S_float'],'K',rec['K_float'])

# Sparse polynomials in (epsilon, y, k), truncated at epsilon degree 2.
def add(a,b):
 c=a.copy()
 for mon,v in b.items():c[mon]=c.get(mon,F(0))+v
 return {m:v for m,v in c.items() if v}
def mul(a,b):
 c={}
 for m,v in a.items():
  for n,w in b.items():
   mon=tuple(x+y for x,y in zip(m,n))
   if mon[0]<=2:c[mon]=c.get(mon,F(0))+v*w
 return {m:v for m,v in c.items() if v}
def scalar(v):return {(0,0,0):F(v)} if v else {}
def neg(a):return {m:-v for m,v in a.items()}
# Bath/source/destination/rate coefficient/epsilon exponent.
poly_ch=[('hot',0,1,F(1),0),('hot',1,0,F(4),0),
 ('cold',0,1,F(1,2),0),('cold',1,0,F(8),0),
 ('hot',0,2,F(8),1),('hot',2,0,F(16),1),
 ('cold',0,2,F(1),1),('cold',2,0,F(4),1),
 ('hot',2,1,F(1),2),('hot',1,2,F(2),2),
 ('cold',2,1,F(4),2),('cold',1,2,F(16),2)]
W=[[{} for _ in range(3)]for _ in range(3)]
for b,j,i,r,pow_e in poly_ch:
 q=E[j]-E[i] if b=='cold' else 0
 term={(pow_e+n,0,n):r*F(q**n,factorial(n)) for n in range(3-pow_e)}
 W[i][j]=add(W[i][j],term)
 W[j][j]=add(W[j][j],{(pow_e,0,0):-r})
M=[[neg(W[i][j]) for j in range(3)]for i in range(3)]
for i in range(3):M[i][i]=add(M[i][i],{(1,1,0):F(1)})
D={}
for perm in permutations(range(3)):
 sig=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
 term=scalar(sig)
 for i in range(3):term=mul(term,M[i][perm[i]])
 D=add(D,term)
expected={(2,2,0):F(27,2),(2,1,0):F(378),(2,1,1):-F(12),(2,0,1):-F(240)}
assert D==expected,(D,expected)
print('Exact scaled determinant leading polynomial:',D)
# y^2+(R-jk)y-beta*j*k=0, solve formal coefficients through order4.
R=F(28);j=F(8,9);beta=F(20)
y=[F(0)]*5
y[1]=beta*j/R
for n in range(2,5):y[n]=(j*y[n-1]-sum(y[m]*y[n-m] for m in range(1,n)))/R
leads=[y[n]*factorial(n) for n in range(1,5)]
assert leads==[F(40,63),F(320,27783),-F(640,1361367),-F(5120,1801088541)]
assert leads[2]/leads[0]==-F(16,21609)
assert leads[3]/leads[1]==-F(16,64827)
print('Leading cumulants:',leads)
print('Leading ratio coefficients:',leads[2]/leads[0],leads[3]/leads[1])
json.dump({'instances':reports,'scaled_det_leading':{str(k):str(v) for k,v in D.items()},'leading_cumulants':[str(x) for x in leads],'verified':True},open(Path(__file__).resolve().parent.parent/'evidence'/'determinant_certificate.json','w'),indent=2)
print('PASS: all exact checks completed.')
