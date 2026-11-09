"""Test GP regression, target transforms and legal-domain trust regions."""
import numpy as np
from bbo.surrogates import transform_y, inverse_mean, fit_gp
from bbo.search import trust_region_bounds, sobol_points, scale_to_box

def test_yeo_johnson_round_trip():
    y = np.array([-3.0, -0.7, 0.0, 0.3, 4.0])
    z, mapping = transform_y(y, "yeo-johnson")
    np.testing.assert_allclose(inverse_mean(z, mapping), y, atol=1e-10)

def test_signed_log_round_trip():
    y = np.array([-50.0, -0.01, 0.0, 0.3, 20.0])
    z, mapping = transform_y(y, "signed-log")
    np.testing.assert_allclose(inverse_mean(z, mapping), y, atol=1e-10)

def test_gp_predicts_mean_and_uncertainty():
    X = np.array([[.1,.2],[.3,.4],[.5,.2],[.7,.8],[.9,.5],[.1,.9]])
    y = np.array([.1,.5,.25,.8,.7,.05])
    model, transform, trained = fit_gp(X, y, "Matern25", "raw", seed=1, restarts=0)
    mean, sd = model.predict(X[:3], return_std=True)
    assert mean.shape == sd.shape == (3,)
    assert np.isfinite(mean).all()
    assert np.isfinite(sd).all()
    assert (sd >= 0).all() and transform is None and len(trained) == 6

def test_trust_region_respects_portal_bounds():
    lower, upper = trust_region_bounds(np.array([0.0, .999999]), length=.2)
    np.testing.assert_allclose(lower, [0.0, .899999], atol=1e-12)
    np.testing.assert_allclose(upper, [.1, .999999], atol=1e-12)
    pool = sobol_points(2, n_power=5, seed=7)
    scaled = scale_to_box(pool, lower, upper)
    assert scaled.shape == (32, 2)
    assert (scaled >= lower).all() and (scaled <= upper).all()
