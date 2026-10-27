#!/usr/bin/env python3
"""Plot exact rational cumulants; only drawing and axis placement use floats."""
from pathlib import Path
from fractions import Fraction as F
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from verify_poisson import cumulants, full_support

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'figures'
OUT.mkdir(exist_ok=True)
rows=[]
for den in np.unique(np.geomspace(1000,10000000,80).round().astype(int)):
    e=F(1,int(den))
    pi,c=cumulants(full_support(e))
    s,k=c[2]/c[0],c[3]/c[1]
    assert s<0 and k<0 and c[0]==F(40,63)
    rows.append((float(e),float(s),float(k),float(e*e*s),float(e*e*k)))
with (ROOT/'evidence/divergence.csv').open('w',newline='') as f:
    wr=csv.writer(f)
    wr.writerow(['epsilon','C3_over_C1','C4_over_C2','epsilon_squared_S','epsilon_squared_K'])
    wr.writerows(rows)
a=np.array(rows)
plum,copper,grey='#69456F','#A86732','#65666C'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
                     'axes.spines.top':False,'axes.spines.right':False,
                     'axes.labelcolor':'#303036','text.color':'#303036'})
fig,ax=plt.subplots(1,2,figsize=(10.8,4.0),layout='constrained')
ax[0].loglog(a[:,0],-a[:,1],color=plum,lw=2.2,label=r'$-C_3/C_1$')
ax[0].loglog(a[:,0],-a[:,2],color=copper,lw=2.2,label=r'$-C_4/C_2$')
ax[0].set(xlabel=r'Weak coupling $\varepsilon$',ylabel='Magnitude of the negative ratio',
          title='Both ratios diverge to minus infinity')
ax[0].legend(frameon=False)
ax[1].semilogx(a[:,0],a[:,3],color=plum,lw=2.2,label=r'$\varepsilon^2 C_3/C_1$')
ax[1].semilogx(a[:,0],a[:,4],color=copper,lw=2.2,label=r'$\varepsilon^2 C_4/C_2$')
ax[1].axhline(-16/21609,color=plum,ls='--',alpha=.65,lw=1.2)
ax[1].axhline(-16/64827,color=copper,ls='--',alpha=.65,lw=1.2)
ax[1].set(xlabel=r'Weak coupling $\varepsilon$',ylabel='Scaled ratio',
          title=r'Exact values approach the $\varepsilon^{-2}$ limits')
ax[1].ticklabel_format(axis='y',style='sci',scilimits=(-3,-3),useMathText=True)
ax[1].legend(frameon=False,loc='lower right')
for x in ax:
    x.grid(True,which='major',color='#DCD8DF',alpha=.65,lw=.6)
    x.invert_xaxis()
fig.savefig(OUT/'thermal_divergence.png',dpi=220,metadata={'Software':None})
fig.savefig(OUT/'thermal_divergence.pdf',metadata={'CreationDate':None,'Producer':None})
print('Saved exact-cumulant divergence figure and numeric table.')
