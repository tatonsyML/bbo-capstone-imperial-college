"""Archive integrity and canonical portal-result checks for recovered Week 12.

These tests do not execute the costly historical model-search scripts or claim
their recorded metrics were re-produced. Original bytes remain immutable.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from zipfile import ZipFile
import csv

REPO = Path(__file__).resolve().parents[1]
ROUND = REPO / "journey" / "round_12"
NAMES = [
    "review_round12.py",
    "robust_and_warp.py",
    "tpe_local.py",
    "trust_region_ts.py",
]
ORIGINAL_SHA256 = {
    "review_round12.py": "d70bd3b992c152d76b824bcecacd58dc13457ada3f8ba94629a29f3b6e8a2537",
    "robust_and_warp.py": "b9725881c963321e069bd7ae8ac68f472b6a979b1ee36d6ad72c6add4dfa9133",
    "tpe_local.py": "98a43bbb1ba2abd8021868254e6a18eb1c6b87ca8e3ff64b83d0f21ce9fe0707",
    "trust_region_ts.py": "768425c1fe721719a71934e31641201c718b884da74bf6c041e47253d562f96d",
}
ASSETS_SHA256 = "776d585b9efc801c9bc15242b21f31802263a21cf58c69e6478a21d8060ffafd"
REQUIRED_ASSETS = {
    "bbo_verified_F2.txt", "bbo_verified_F3.txt", "bbo_verified_F6.txt",
    "round12_new_benchmark.json", "round12_robustness_warp.json",
    "round12_tpe_and_local.json", "round12_turbo_ts.json",
    "week12_candidate_comparison_2026-11-02.csv",
    "week12_final_points_2026-11-02.txt",
    "week12_full_review_2026-11-02.md",
}
ORIGINAL_DIR = "/mnt/data/bbo_week12_deep_review"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def test_four_original_scripts_are_unmodified():
    for filename, expected in ORIGINAL_SHA256.items():
        original = (ROUND / "original" / filename).read_bytes()
        assert digest(original) == expected, filename
        compile(original, filename, "exec")
        portable = (ROUND / "portable" / filename).read_bytes()
        expected_portable = original.replace(
            f"Path('{ORIGINAL_DIR}')".encode(),
            b"Path(__file__).resolve().parent",
        )
        assert portable == expected_portable, filename
        compile(portable, filename, "exec")


def test_original_assets_are_exact_and_all_ten_files_are_present():
    data = (ROUND / "original" / "week12_original_assets.zip").read_bytes()
    assert digest(data) == ASSETS_SHA256
    with ZipFile(ROUND / "original" / "week12_original_assets.zip") as z:
        assert set(z.namelist()) == REQUIRED_ASSETS
        for name in z.namelist():
            assert z.read(name), name
        points = z.read("week12_final_points_2026-11-02.txt").decode()
    with (REPO / "data" / "portal_rounds_11_12.csv").open(newline="") as stream:
        observed = list(csv.DictReader(stream))
    # Proposals preceded results; the submitted coordinates subsequently
    # matched, but saved forecasts are not treated as actual returns.
    for f in range(1, 9):
        proposed = re.search(rf"^Function {f}: (.+)$", points, flags=re.M)
        assert proposed, f
        actual = next(r for r in observed if r["Function"] == str(f) and r["Round"] == "12")
        assert [float(v) for v in proposed.group(1).split("-")] == [
            float(v) for v in actual["Input"].split("-")
        ]
