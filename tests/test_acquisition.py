import numpy as np
from bbo.acquisition import expected_improvement, probability_improvement, upper_confidence_bound

def test_acquisition_shapes_and_bounds():
    mu=np.array([0.0,1.0]); sd=np.array([0.2,0.3]); best=0.5
    ei=expected_improvement(mu,sd,best)
    pi=probability_improvement(mu,sd,best)
    ucb=upper_confidence_bound(mu,sd)
    assert ei.shape==(2,) and np.all(ei>=0)
    assert np.all((pi>=0)&(pi<=1))
    assert ucb.shape==(2,)
