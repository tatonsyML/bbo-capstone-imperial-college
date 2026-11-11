"""Retrospective DBSCAN diagnostic using ONLY the eight own through-Week-10 datasets.

This is supporting research performed AFTER Round 10, not original Round 11
candidate-selection code. The original clustering package motivated this audit.
No third-party observations are imported, and no original CSVs are copied.

Run from any directory:
    python research/diagnostics/clustering/clustering_audit.py --repo .

Outputs (in the script's own folder by default):
    dbscan_eps_sensitivity.csv
    selected_cluster_summary.csv
    f1_clustering_diagnostic.png

The retrospective F1 mathematical background uses the repository's existing
canonical F1 model; no new equation fitting or validation is performed here.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")  # Reproducible in GitHub Actions and headless environments.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN

EPS_GRID = (0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.12)
SELECTED_EPS = {1: 0.02, 2: 0.005, 3: 0.02, 4: 0.02, 5: 0.05, 6: 0.03, 7: 0.05, 8: 0.05}
DIMENSIONS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}
EXPECTED_COUNTS = {1: 20, 2: 20, 3: 25, 4: 40, 5: 30, 6: 30, 7: 40, 8: 50}
MIN_SAMPLES = 3


def load_observations(repo: Path, number: int):
    path = repo / f"data/accumulated/function_{number}/observations_through_week10.csv"
    data = pd.read_csv(path)
    columns = [f"x{i}" for i in range(1, DIMENSIONS[number] + 1)]
    required = set(columns + ["function", "stage", "is_initial", "output"])
    if not required.issubset(data.columns):
        raise ValueError(f"Unexpected schema in {path}: {sorted(required - set(data.columns))}")
    if len(data) != EXPECTED_COUNTS[number] or (data["function"] != number).any():
        raise ValueError(f"Unexpected number or function identity in {path}")
    if data[columns + ["output"]].isna().any().any():
        raise ValueError(f"Missing values in {path}")
    # The current 255 observations have no identical vectors. Retain all
    # observations and *fail* if duplicates appear, rather than silently
    # changing the effective sample size or handling repeat scores arbitrarily.
    if data.duplicated(subset=columns).any():
        raise ValueError(f"Repeated input vectors require an explicit policy: {path}")
    return data, columns


def analyse(repo: Path):
    sensitivity, selected = [], []
    for number in DIMENSIONS:
        df, columns = load_observations(repo, number)
        x = df[columns].to_numpy(float)
        y = df["output"].to_numpy(float)
        for eps in EPS_GRID:
            labels = DBSCAN(eps=eps, min_samples=MIN_SAMPLES, metric="euclidean").fit_predict(x)
            clusters = sorted(set(labels) - {-1})
            sensitivity.append({
                "function": number, "eps": eps,
                "min_samples": MIN_SAMPLES, "n_unique": len(df),
                "n_clusters": len(clusters), "n_noise": int(np.sum(labels == -1))
            })
            if eps != SELECTED_EPS[number]:
                continue
            for cluster in clusters:
                mask = labels == cluster
                row = {
                    "function": number, "eps": eps,
                    "cluster": str(cluster), "size": int(mask.sum()),
                    "mean_output": float(np.mean(y[mask])),
                    "best_output": float(np.max(y[mask])),
                    "best_is_noise": ""
                }
                row.update({c: float(np.mean(x[mask, j])) for j, c in enumerate(columns)})
                selected.append(row)
            best = int(np.argmax(y))
            best_row = {
                "function": number, "eps": eps, "cluster": "best_observation",
                "size": 1, "mean_output": float(y[best]),
                "best_output": float(y[best]),
                "best_is_noise": bool(labels[best] == -1)
            }
            best_row.update({c: float(x[best, j]) for j, c in enumerate(columns)})
            selected.append(best_row)
    return pd.DataFrame(sensitivity), pd.DataFrame(selected)


def plot_f1(repo: Path, path: Path):
    # Import the EXISTING reconstruction, avoiding a second F1 evaluator.
    sys.path.insert(0, str(repo / "src"))
    from bbo.f1_reconstruction import predict, REFERENCE

    df, columns = load_observations(repo, 1)
    x = df[columns].to_numpy(float)
    y = df["output"].to_numpy(float)
    labels = DBSCAN(eps=SELECTED_EPS[1], min_samples=MIN_SAMPLES).fit_predict(x)
    clustered = labels >= 0
    best = int(np.argmax(y))

    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.6), dpi=140)
    fig.suptitle("F1 | Round 10 input-space clustering and later model interpretation", fontsize=13, weight="bold")
    ax = axes[0]
    ax.scatter(x[~clustered, 0], x[~clustered, 1], marker="o", s=42,
               facecolors="none", edgecolors="0.4", linewidths=1, label=f"Unclustered: {(~clustered).sum()}")
    ax.scatter(x[clustered, 0], x[clustered, 1], marker="o", s=44,
               label=f"DBSCAN cluster: {clustered.sum()}")
    ax.scatter(*x[best], marker="*", s=140, linewidths=1.2,
               label="Highest observed score through R10")
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="x1", ylabel="x2",
           title="Actual sampled inputs (all 20)")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(alpha=0.15)
    ax.legend(loc="lower left", fontsize=7.8, framealpha=0.93)

    ax = axes[1]
    t = np.linspace(0.30, 0.79, 251)
    xx, yy = np.meshgrid(t, t)
    pred = predict(np.column_stack([xx.ravel(), yy.ravel()]), REFERENCE).reshape(xx.shape)
    levels = [-.15, -.05, -.01, -.001, 0, .001, .01, .1, .5, 1, 1.5, 2.01]
    chart = ax.contourf(xx, yy, pred, levels=levels, extend="min")
    ax.scatter(x[~clustered, 0], x[~clustered, 1], marker="o", s=25,
               facecolors="none", edgecolors="0.25", linewidths=0.7,
               label="Round 10 unclustered inputs")
    ax.scatter(x[clustered, 0], x[clustered, 1], marker="o", s=27,
               edgecolors="white", linewidths=0.6, label="Round 10 cluster")
    ax.scatter(*x[best], marker="*", s=170, linewidths=1.0,
               label="Best input observed by R10")
    ax.scatter([REFERENCE.minor_centre, REFERENCE.major_centre],
               [REFERENCE.minor_centre, REFERENCE.major_centre], marker="x", s=70,
               label="Retrospective model centres")
    ax.set(xlim=(0.30, 0.79), ylim=(0.30, 0.79), xlabel="x1", ylabel="x2",
           title="Later F1 reconstruction (model scores)")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(alpha=0.12)
    fig.colorbar(chart, ax=ax, fraction=0.048, pad=.03, label="Predicted score (not a portal evaluation)")
    ax.legend(fontsize=7.2, loc="upper left", framealpha=0.93)
    fig.text(.5, .012,
             "DBSCAN: Euclidean inputs, eps=0.02, min_samples=3.  "
             "The F1 surface was reconstructed later; it was not known from this clustering analysis.",
             ha="center", fontsize=8.6)
    fig.tight_layout(rect=(0, .035, 1, .965))
    fig.savefig(path, dpi=140, bbox_inches="tight", metadata={"Software": "Matplotlib"})
    plt.close(fig)


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    cli.add_argument("--output", type=Path, default=Path(__file__).resolve().parent)
    args = cli.parse_args()
    repo = args.repo.resolve()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    a, b = analyse(repo)
    a.to_csv(output / "dbscan_eps_sensitivity.csv", index=False, float_format="%.12g")
    b.to_csv(output / "selected_cluster_summary.csv", index=False, float_format="%.12g")
    plot_f1(repo, output / "f1_clustering_diagnostic.png")
    print(f"Checked {a[a['eps'] == 0.02]['n_unique'].sum()} records across {len(DIMENSIONS)} functions")
    print(f"Wrote {len(a)} sensitivity rows and {len(b)} selected rows to {output}")
    for f in DIMENSIONS:
        item = b[(b['function'] == f) & (b['cluster'] == 'best_observation')].iloc[0]
        print(f"F{f}: best-through-R10 in DBSCAN noise = {item['best_is_noise']}")


if __name__ == "__main__":
    main()
