"""Historical Week 9 diagnostics; see structural_validation.py for final held-out tests.

This module intentionally uses the pre-Round-10 evidence cut to avoid
introducing future portal returns into historical model decisions.
"""
from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd


def load_function(repo_root, fn):
    """Load only training observations returned by Week 9."""
    # Using the Week 9 snapshot prevents later portal results leaking into this fit.
    p=Path(repo_root)/'data'/'accumulated'/f'function_{fn}'/'observations_through_week9.csv'
    df=pd.read_csv(p)
    xs=[c for c in df.columns if c.startswith('x')]
    return df[xs].to_numpy(float), df['output'].to_numpy(float)


def f8_additive_quadratic(repo_root):
    """Historical 17-coefficient F8 fit using the 49 available Week 9 points.

    Different from the final check fitting 40 initial points and holding out 13.
    Basis: intercept plus each dimension's linear and squared contribution.
    """
    X,y=load_function(repo_root,8)
    cols=[np.ones(len(X))]
    for j in range(X.shape[1]):
        cols.extend([X[:,j],X[:,j]**2])
    Z=np.column_stack(cols)
    # A least-squares explanatory fit is not access to the original hidden formula.
    coef=np.linalg.lstsq(Z,y,rcond=None)[0]
    residual=np.max(np.abs(Z@coef-y))
    opt=[]; k=1
    for j in range(8):
        a,b=coef[k],coef[k+1]; k+=2
        # Concave coordinate terms peak at their vertex; otherwise examine a boundary.
        x=-a/(2*b) if b<0 else (0.999999 if a+b>0 else 0.0)
        opt.append(float(np.clip(x,0,.999999)))
    z=[1.0]
    for x in opt:
        z.extend([x,x*x])
    return coef,np.asarray(opt),float(np.dot(z,coef)),float(residual)


def current_best(repo_root):
    """Return observed incumbents through Week 9, not model forecasts."""
    rows=[]
    for fn in range(1,9):
        X,y=load_function(repo_root,fn)
        i=int(np.argmax(y))
        rows.append({'Function':fn,'Best_output':float(y[i]),'Best_input':'-'.join(f'{v:.6f}' for v in X[i])})
    return pd.DataFrame(rows)
