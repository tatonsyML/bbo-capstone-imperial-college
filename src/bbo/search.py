from __future__ import annotations
import numpy as np
from scipy.stats import qmc


def portal_string(x):
    return '-'.join(f'{float(v):.6f}' for v in x)


def sobol_points(d, n_power=15, seed=0):
    return np.clip(qmc.Sobol(d=d,scramble=True,seed=seed).random_base2(n_power),1e-6,.999999)


def trust_region_bounds(center, length):
    c=np.asarray(center,float)
    return np.maximum(0.0,c-length/2), np.minimum(.999999,c+length/2)


def scale_to_box(unit_points, lower, upper):
    u=np.asarray(unit_points,float); lo=np.asarray(lower,float); hi=np.asarray(upper,float)
    return lo+(hi-lo)*u
