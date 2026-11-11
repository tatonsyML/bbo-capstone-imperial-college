"""Numerical tests for the retrospective F1 reconstruction (no peer data)."""
from __future__ import annotations

import numpy as np
from bbo.f1_reconstruction import (
    REFERENCE, fit_initial_only, load_own_observations,
    predict, validate_held_out,
)


def test_f1_self_data_fit_and_holdout():
    x, y, initial = load_own_observations()
    assert x.shape == (23, 2)
    assert y.shape == (23,)
    assert initial.sum() == 10
    params = fit_initial_only(x[initial], y[initial])
    np.testing.assert_allclose(
        params.as_array(), REFERENCE.as_array(),
        rtol=0, atol=1e-8,
    )
    checks = validate_held_out(x[~initial], y[~initial], params)
    assert checks["count"] == 13
    assert checks["zero_count"] == 1
    assert checks["max_relative_error_nonzero"] < 1e-10


def test_f1_round11_result_and_nonzero_sign():
    x = np.array([[0.628540, 0.628540], [0.6501140597987644, 0.6815263520602101]])
    got = predict(x)
    np.testing.assert_allclose(
        got, [1.9999999996761817, -0.0036060626443634764],
        rtol=1e-12, atol=0,
    )
    assert np.all(np.isfinite(got))


def test_f1_rejects_invalid_shape():
    import pytest
    with pytest.raises(ValueError):
        predict(np.array([0.62854, 0.62854]))
