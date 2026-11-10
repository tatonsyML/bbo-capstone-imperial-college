"""Clustering and structural-equation diagnostics for the Imperial BBO project.

Recovered from an indexed October 2026 working file. This repository copy is
transcribed from the recovered text, not verified byte-for-byte against the
unavailable raw original. It is an analytical audit, NOT the original Round 11
candidate-selection script.

Run from the repository root:
  python journey/round_11/supplementary_analysis/bbo_clustering_audit.py --repo . --output analysis/clustering
Dependencies: numpy, pandas, scikit-learn, matplotlib, scipy.
Data: personal observations through Round 10 (no classmates' points).
"""
from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

EPS_GRID = (0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.12)
EPS_CASES = {1: 0.02, 2: 0.005, 3: 0.02, 4: 0.02, 5: 0.05,
             6: 0.03, 7: 0.05, 8: 0.05}
MIN_SAMPLES = 3


def f1_exact(x):
    x = np.asarray(x, dtype=float)
    c1 = 0.5 - np.pi / 40
    c2 = 0.55 + np.pi / 40

    def component(c):
        delta = x - c
        return np.exp(-1600 * np.sum(delta ** 2, axis=-1)) * np.prod(
            np.cos(40 * delta), axis=-1
        )
    return component(c1) + 2 * component(c2)


def f8_exact(x):
    x = np.asarray(x, dtype=float)
    centre = np.array([.1, .15, .13, .15, .8, .5, .2, .6])
    weights = np.array([2, 1, 3, 1, .5, 1, 2, .1])
    return 10 - np.sum(weights * (x - centre) ** 2, axis=-1)


def load(repo, function):
    p = repo / f"data/accumulated/function_{function}/observations_through_week10.csv"
    df = pd.read_csv(p)
    features = [f"x{i}" for i in range(1, function + 10)
                if f"x{i}" in df.columns]
    df = df.drop_duplicates(subset=features).reset_index(drop=True)
    return df, features


def perform(repo, out):
    out.mkdir(parents=True, exist_ok=True)
    summary, detail = [], []
    for function in range(1, 9):
        df, features = load(repo, function)
        X = df[features].to_numpy(float)
        y = df["output"].to_numpy(float)
        for eps in EPS_GRID:
            labels = DBSCAN(eps=eps, min_samples=MIN_SAMPLES).fit_predict(X)
            clusters = sorted(set(labels) - {-1})
            summary.append(dict(function=function, eps=eps,
                                min_samples=MIN_SAMPLES, n_unique=len(df),
                                n_clusters=len(clusters),
                                n_noise=int(np.sum(labels == -1))))
            if eps != EPS_CASES[function]:
                continue
            for cluster in clusters:
                mask = labels == cluster
                row = dict(function=function, eps=eps, cluster=cluster,
                           size=int(mask.sum()),
                           mean_output=float(np.mean(y[mask])),
                           best_output=float(np.max(y[mask])))
                row.update({name: float(np.mean(X[mask, j]))
                            for j, name in enumerate(features)})
                detail.append(row)
            best_idx = int(np.argmax(y))
            detail.append(dict(
                function=function, eps=eps, cluster="best_observation",
                size=1, mean_output=float(y[best_idx]),
                best_output=float(y[best_idx]),
                best_is_noise=bool(labels[best_idx] == -1),
                **{name: float(X[best_idx, j])
                   for j, name in enumerate(features)}
            ))
        if function in (1, 8):
            predicted = f1_exact(X) if function == 1 else f8_exact(X)
            err = predicted - y
            nonzero = y != 0
            relative = np.abs(err[nonzero] / y[nonzero])
            pd.DataFrame(dict(
                function=[function], n=[len(y)],
                max_abs_error=[float(np.max(np.abs(err)))],
                max_relative_error=[
                    float(np.max(relative)) if len(relative) else 0
                ],
                rmse=[float(np.sqrt(np.mean(err ** 2)))]
            )).to_csv(out / f"f{function}_equation_validation.csv", index=False)
            pd.DataFrame(dict(
                **{k: df[k] for k in features},
                observed=y, predicted=predicted,
                absolute_residual=np.abs(err)
            )).to_csv(out / f"f{function}_prediction_residuals.csv", index=False)

    pd.DataFrame(summary).to_csv(out / "dbscan_eps_sensitivity.csv",
                                 index=False)
    pd.DataFrame(detail).to_csv(out / "selected_cluster_summary.csv",
                                index=False)

    # The contour is generated from an analytical hypothesis, not portal points.
    z = np.linspace(.34, .72, 381)
    xx, yy = np.meshgrid(z, z)
    response = f1_exact(np.column_stack([xx.ravel(), yy.ravel()])).reshape(xx.shape)
    fig, ax = plt.subplots(figsize=(7, 5.5))
    levels = [-.05, -.01, -.001, -.00001, 0, .00001, .001, .01,
              .1, .5, 1, 1.5, 2]
    ax.contourf(xx, yy, response, levels=levels, extend="both")
    ax.contour(xx, yy, response, levels=[.1, .5, 1], linewidths=.9)
    observations, _ = load(repo, 1)
    ax.scatter(observations.x1, observations.x2, s=17,
               facecolors="none", edgecolors="black",
               linewidths=.75, label="Own measured inputs")
    c1 = .5 - np.pi / 40
    c2 = .55 + np.pi / 40
    ax.scatter([c1, c2], [c1, c2], marker="x", s=80,
               label="Recovered model centres")
    ax.set(title="F1: two modelled peaks and actual sampled locations",
           xlabel="x1", ylabel="x2", xlim=(.34, .72), ylim=(.34, .72))
    ax.legend(loc="upper left", fontsize=7)
    fig.tight_layout()
    fig.savefig(out / "f1_model_clusters_vs_samples.png", dpi=180)
    plt.close(fig)

    # Count connected high-response regions in the model-generated grid.
    from scipy.ndimage import label
    tagged, n_regions = label(response > .1)
    regions = []
    for i in range(1, n_regions + 1):
        py, px = np.where(tagged == i)
        best = np.argmax(response[py, px])
        regions.append(dict(
            region=i, n_grid_cells=len(px),
            peak_x1=float(z[px[best]]), peak_x2=float(z[py[best]]),
            approx_peak_score=float(response[py[best], px[best]])
        ))
    pd.DataFrame(regions).to_csv(
        out / "f1_modelled_high_response_regions.csv", index=False
    )
    print("Analytical high-response regions:", regions)
    print("Outputs:", out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path,
                        default=Path("analysis/clustering"))
    args = parser.parse_args()
    perform(args.repo, args.output)
