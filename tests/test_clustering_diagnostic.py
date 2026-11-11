"""Check retrospective density diagnostics without confusing them with R11 code."""
from pathlib import Path
import importlib.util
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/diagnostics/clustering/clustering_audit.py"
SPEC = importlib.util.spec_from_file_location("round10_clustering_diagnostic", SCRIPT)
CLUSTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CLUSTER)


def test_all_255_round10_observations_and_eps_sensitivity():
    summary, details = CLUSTER.analyse(ROOT)
    assert len(summary) == 56
    assert len(details) == 16
    assert summary.groupby("function")["n_unique"].first().sum() == 255
    for function, eps, clusters, noise in [
        (1, .02, 1, 15), (2, .005, 1, 13), (3, .02, 1, 20),
        (4, .02, 1, 32), (5, .05, 0, 30), (6, .03, 1, 23),
        (7, .05, 1, 35), (8, .05, 2, 43),
    ]:
        selected = summary[(summary.function == function) & (summary.eps == eps)]
        assert len(selected) == 1
        assert int(selected.iloc[0].n_clusters) == clusters
        assert int(selected.iloc[0].n_noise) == noise
    observed_best = details[details.cluster == "best_observation"].set_index("function")
    assert observed_best.loc[1, "best_is_noise"] == True
    assert observed_best.loc[2, "best_is_noise"] == False
    assert observed_best.loc[4, "best_is_noise"] == False
    assert observed_best.loc[8, "best_is_noise"] == True
    assert abs(observed_best.loc[8, "best_output"] - 10) < 1e-12


def test_outputs_generated_from_existing_data_and_canonical_model(tmp_path):
    summary, selected = CLUSTER.analyse(ROOT)
    CLUSTER.plot_f1(ROOT, tmp_path / "f1.png")
    image = (tmp_path / "f1.png").read_bytes()
    assert image.startswith(b"\x89PNG\r\n\x1a\n")
    assert len(image) > 20_000
    # Published summaries match the algorithm, rather than manually edited counts.
    published = SCRIPT.parent
    pd.testing.assert_frame_equal(pd.read_csv(published / "dbscan_eps_sensitivity.csv"), summary, check_dtype=False)
    pd.testing.assert_frame_equal(pd.read_csv(published / "selected_cluster_summary.csv").fillna(""),
                                  selected.fillna(""), check_dtype=False, check_exact=False, rtol=1e-10)
