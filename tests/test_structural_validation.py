import numpy as np
from bbo.structural_validation import F8_C, F8_W, recover_f8, f5_at

def test_original_40_recover_f8_and_predict_later_12():
    r = recover_f8()
    assert r["rank"] == 17
    assert r["initial_count"] == 40
    assert r["holdout_count"] == 12
    np.testing.assert_allclose(r["centre"], F8_C, atol=1e-12, rtol=0)
    np.testing.assert_allclose(r["weights"], F8_W, atol=1e-12, rtol=0)
    assert abs(r["maximum"]-10) < 1e-12
    assert r["max_holdout_error"] < 2e-14

def test_f5_corner():
    assert abs(f5_at(np.full(4,.999999))-8662.405001248297) < 1e-9
