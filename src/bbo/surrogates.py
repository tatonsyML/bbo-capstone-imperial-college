from __future__ import annotations
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF, Matern, WhiteKernel
from sklearn.preprocessing import PowerTransformer


def transform_y(y, mode='raw'):
    y=np.asarray(y,float).reshape(-1)
    if mode=='raw':
        return y, None
    if mode=='yeo-johnson':
        pt=PowerTransformer(method='yeo-johnson', standardize=True)
        return pt.fit_transform(y[:,None]).ravel(), pt
    if mode=='signed-log':
        z=np.sign(y)*np.log1p(np.abs(y)); mu=float(z.mean()); sd=float(z.std() or 1.0)
        return (z-mu)/sd, ('signed-log',mu,sd)
    raise ValueError(mode)


def inverse_mean(z, transform):
    z=np.asarray(z,float).reshape(-1)
    if transform is None:
        return z
    if isinstance(transform, PowerTransformer):
        return transform.inverse_transform(z[:,None]).ravel()
    _,mu,sd=transform; q=z*sd+mu
    return np.sign(q)*np.expm1(np.abs(q))


def fit_gp(X, y, kernel='Matern25', transform='yeo-johnson', seed=0, restarts=4):
    X=np.asarray(X,float); y=np.asarray(y,float).reshape(-1)
    yt,tr=transform_y(y,transform)
    d=X.shape[1]
    if kernel=='RBF':
        base=RBF(np.ones(d),(1e-3,10.0))
    elif kernel=='Matern15':
        base=Matern(np.ones(d),(1e-3,10.0),nu=1.5)
    elif kernel=='Matern25':
        base=Matern(np.ones(d),(1e-3,10.0),nu=2.5)
    else:
        raise ValueError(kernel)
    k=ConstantKernel(1.0,(1e-3,1e3))*base + WhiteKernel(1e-4,(1e-8,1.0))
    gp=GaussianProcessRegressor(kernel=k,normalize_y=False,n_restarts_optimizer=restarts,random_state=seed)
    gp.fit(X,yt)
    return gp,tr,yt
