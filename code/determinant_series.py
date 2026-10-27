"""Exact rational characteristic-polynomial power series, degree four."""
from fractions import Fraction as F
from itertools import permutations
from math import factorial
import json
NMAX=4

def sa(a,b):return [a[i]+b[i] for i in range(NMAX+1)]
def sm(a,b):return [sum((a[k]*b[i-k] for k in range(i+1)),F()) for i in range(NMAX+1)]
def sc(a,r):return [x*r for x in a]
def sp(a,n):
 b=[F(1)]+[F(0)]*NMAX
 for _ in range(n):b=sm(b,a)
 return b
def scalar(r):return [F(r)]+[F(0)]*NMAX

def pa(a,b):
 c={k:v.copy() for k,v in a.items()}
 for k,v in b.items():c[k]=sa(c.get(k,scalar(0)),v)
 return c
def pm(a,b):
 c={}
 for k,v in a.items():
  for j,w in b.items():c[k+j]=sa(c.get(k+j,scalar(0)),sm(v,w))
 return c

def analyse(energies,channels):
 n=len(energies)
 # channels: bath name, source, dest, rate, with reverse separately
 W=[[scalar(0) for _ in range(n)] for _ in range(n)]
 for bath,j,i,rate in channels:
  q=F(energies[j]-energies[i]) if bath=='cold' else F(0)
  W[i][j]=sa(W[i][j],[rate*q**k/F(factorial(k)) for k in range(NMAX+1)])
  W[j][j][0]-=rate
 M=[[{0:sc(W[i][j],-1)} for j in range(n)] for i in range(n)]
 for i in range(n):M[i][i][1]=scalar(1)
 D={}
 for perm in permutations(range(n)):
  sig=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
  term={0:scalar(sig)}
  for i in range(n):term=pm(term,M[i][perm[i]])
  D=pa(D,term)
 assert D[0][0]==0
 assert D[1][0]>0
 x=scalar(0)
 for k in range(1,NMAX+1):
  resid=scalar(0)
  for j,coef in D.items():resid=sa(resid,sm(coef,sp(x,j)))
  x[k]=-resid[k]/D[1][0]
 resid=scalar(0)
 for j,coef in D.items():resid=sa(resid,sm(coef,sp(x,j)))
 assert all(v==0 for v in resid),resid
 return [x[k]*factorial(k) for k in range(1,NMAX+1)],D

def edge(channels,bath,lo,hi,up,down):
 channels.append((bath,lo,hi,F(up)));channels.append((bath,hi,lo,F(down)))

