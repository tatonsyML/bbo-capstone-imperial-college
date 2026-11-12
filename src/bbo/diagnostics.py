"""Diagnostics using only observations available through Week 9.

The eight files under data/accumulated/function_*/ preserve the evidence
known before Round 10. Model choices based on these snapshots can be
examined without importing information from later successful portal returns.

In particular, F8's additive quadratic is fitted to 49 accumulated points
(40 initial + 9 personal), which is DIFFERENT from the later independent
retrospective 40-initial/13-held-out fit in structural_validation.py.

Diagnostic predictions and fitted maxima are MODEL VALUES. Nothing in this
module produces a new course-portal observation or establishes identity
with an undisclosed source function.
"""
from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd


def load_function(repo_root, fn):
    """Read a function's pre-Round-10 data snapshot as (X, y) arrays.

    repo_root identifies the repository checkout and fn is an integer from
    1 to 8. The function filters input columns by their x-prefixed names
    in the saved snapshot; it does not query a live source, alter files or
    append later portal outcomes.
    """
    # Using the Week 9 snapshot prevents later portal results leaking into this fit.
    p=Path(repo_root)/'data'/'accumulated'/f'function_{fn}'/'observations_through_week9.csv'
    df=pd.read_csv(p)
    xs=[c for c in df.columns if c.startswith('x')]
    return df[xs].to_numpy(float), df['output'].to_numpy(float)


def f8_additive_quadratic(repo_root):
    """Fit an additive quadratic to 49 pre-Round-10 F8 records.

    The design has 17 columns: one intercept and, for each of eight inputs,
    a linear term x_j and a squared term x_j**2. It deliberately excludes
    cross-coordinate interactions, so the fit is interpretable but
    assumes separability.

    Returns
    -------
    coefficients : array of 17 floats
        Least-squares model parameters, not authenticated oracle constants.
    optimum : array of 8 floats
        Coordinate-wise vertex where concave, otherwise a chosen boundary
        within the legal input domain.
    predicted_score : float
        Value of the fitted quadratic at that proposed vector.
    maximum_absolute_residual : float
        Largest absolute discrepancy on the same 49 training rows.

    This was a historical modelling analysis, not the later holdout study.
    Small training residuals alone do not validate behaviour at unseen inputs.
    """
    X,y=load_function(repo_root,8)
    # Each input contributes x_j and x_j². Keeping them separate lets
    # calculus find each coordinate's vertex without interaction terms.
    cols=[np.ones(len(X))]
    for j in range(X.shape[1]):
        cols.extend([X[:,j],X[:,j]**2])
    Z=np.column_stack(cols)
    # A least-squares explanatory fit is not access to the original hidden formula.
    coef=np.linalg.lstsq(Z,y,rcond=None)[0]
    # This is a TRAINING residual on the 49 known points, not a held-out
    # prediction error or a confidence estimate on the true hidden function.
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
    """Summarise the highest *measured* score for each function by Week 9.

    Returns one pandas row per function with the best observed output and
    its recorded vector in portal-style six-decimal notation. This baseline
    is computed from saved observations, not the predictions of the GP or
    any HEBO-inspired/TuRBO-style suggested candidates.
    """
    rows=[]
    for fn in range(1,9):
        X,y=load_function(repo_root,fn)
        i=int(np.argmax(y))
        rows.append({'Function':fn,'Best_output':float(y[i]),'Best_input':'-'.join(f'{v:.6f}' for v in X[i])})
    return pd.DataFrame(rows)
