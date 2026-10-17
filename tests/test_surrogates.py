from pathlib import Path
import numpy as np
from bbo.diagnostics import f8_additive_quadratic

ROOT=Path(__file__).resolve().parents[1]

def test_f8_structure_recovery():
    _,x,y,err=f8_additive_quadratic(ROOT)
    expected=np.array([.10,.15,.13,.15,.80,.50,.20,.60])
    assert err < 1e-10
    assert np.max(np.abs(x-expected)) < 1e-6
    assert abs(y-10.0) < 1e-9
