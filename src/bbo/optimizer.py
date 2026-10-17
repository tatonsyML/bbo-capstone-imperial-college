from __future__ import annotations
import numpy as np
import pandas as pd
from scipy.stats import qmc
from .surrogates import fit_gp, inverse_mean
from .acquisition import expected_improvement, probability_improvement, upper_confidence_bound
from .search import portal_string, trust_region_bounds, scale_to_box


def hebo_inspired_committee(X, y, seed=100, n_power=15):
    """HEBO-inspired challenger, not the official HEBO implementation."""
    X=np.asarray(X,float); y=np.asarray(y,float); d=X.shape[1]
    S=np.clip(qmc.Sobol(d=d,scramble=True,seed=seed).random_base2(n_power),1e-6,.999999)
    rows=[]
    for kernel in ['RBF','Matern15','Matern25']:
        gp,tr,yt=fit_gp(X,y,kernel,'yeo-johnson',seed=seed)
        mu,sd=gp.predict(S,return_std=True); best=float(yt.max())
        A=np.vstack([
            expected_improvement(mu,sd,best),
            probability_improvement(mu,sd,best),
            upper_confidence_bound(mu,sd,1.96),
        ])
        ranks=np.vstack([np.argsort(np.argsort(a))/(len(a)-1) for a in A])
        robust=np.quantile(ranks,.25,axis=0); i=int(np.argmax(robust))
        rows.append({'kernel':kernel,'candidate':portal_string(S[i]),'robust_rank':float(robust[i]),
                     'predicted_mean':float(inverse_mean([mu[i]],tr)[0]),'transformed_sd':float(sd[i])})
    return pd.DataFrame(rows)


def turbo_style_candidate(X, y, length=0.20, seed=900):
    """Lightweight TuRBO-style local challenger using EI inside an incumbent-centred trust region."""
    X=np.asarray(X,float); y=np.asarray(y,float); d=X.shape[1]
    center=X[int(np.argmax(y))]
    lo,hi=trust_region_bounds(center,length)
    U=qmc.Sobol(d=d,scramble=True,seed=seed).random_base2(15)
    S=scale_to_box(U,lo,hi)
    gp,tr,yt=fit_gp(X,y,'Matern25','yeo-johnson',seed=seed)
    mu,sd=gp.predict(S,return_std=True)
    ei=expected_improvement(mu,sd,float(yt.max()))
    i=int(np.argmax(ei))
    return {'candidate':portal_string(S[i]),'predicted_mean':float(inverse_mean([mu[i]],tr)[0]),'ei_transformed':float(ei[i])}


def official_hebo_suggest(X, y):
    """Optional official HEBO adapter. Requires the external HEBO package."""
    try:
        from hebo.design_space.design_space import DesignSpace
        from hebo.optimizers.hebo import HEBO
    except ImportError as exc:
        raise RuntimeError('Install HEBO to use official_hebo_suggest') from exc
    X=np.asarray(X,float); y=np.asarray(y,float).reshape(-1,1); d=X.shape[1]
    cols=[f'x{i+1}' for i in range(d)]
    space=DesignSpace().parse([{'name':c,'type':'num','lb':0.0,'ub':0.999999} for c in cols])
    opt=HEBO(space); hist=pd.DataFrame(X,columns=cols); opt.observe(hist,-y)
    rec=opt.suggest(n_suggestions=1)
    return rec[cols].to_numpy(float)[0]
