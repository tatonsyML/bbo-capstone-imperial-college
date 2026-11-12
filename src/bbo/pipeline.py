"""Run the preserved Week 9 candidate-selection demonstration.

This entry point combines snapshot loading, HEBO-*inspired* committee
ranking, fixed-box TuRBO-*style* proposals and a fitted F8 quadratic.
It prints exploratory comparisons that could have been calculated from
observations available before Round 10. It does not send portal queries,
score suggestions against a private oracle, or rerun the later official
HEBO / TuRBO-1 simulator benchmark.

The canonical experimental history is recorded separately under data/
and journey/. Printed challenger locations must not be counted as new
measured objective values or claimed as the original submitted inputs.
"""
from __future__ import annotations

from pathlib import Path
import pandas as pd

from .diagnostics import load_function, current_best, f8_additive_quadratic
from .optimizer import hebo_inspired_committee, turbo_style_candidate


def run(repo_root=None):
    """Print the Week 9 baseline, challenger suggestions and an F8 model fit.

    Parameters
    ----------
    repo_root : path-like or None
        Repository root containing the accumulated Week 9 CSV files. By
        default the path is derived relative to this Python module.

    Side effects
    ------------
    Prints text tables only. No new objective is evaluated or written to
    the measured record.

    Method
    ------
    Each function uses its own saved pre-Round-10 observations. The
    HEBO-inspired committee returns three kernel-specific candidates; the
    row with the largest lower-quartile acquisition consensus rank is
    displayed. The TuRBO-style method independently suggests a candidate
    inside a *static* incumbent-centred box. Neither proposal is an
    observed score or an official full-algorithm run.
    """
    root = Path(repo_root or Path(__file__).resolve().parents[2])
    print("Historical best through Week 9")
    print(current_best(root).to_string(index=False))
    print("\nChallenger proposals (not portal scores)")

    # Treat each objective separately; their output scales and dimensions
    # differ, so combining raw scores across functions would be invalid.
    rows = []
    for function in range(1, 9):
        X, y = load_function(root, function)
        # Independent reproducible seeds avoid accidentally reusing the same
        # candidate design across objectives with different dimensions.
        committee = hebo_inspired_committee(X, y, seed=100 + function)
        trust_region = turbo_style_candidate(X, y, seed=900 + function)

        # A committee produces one candidate per kernel. Use the strongest
        # robust acquisition-rank entry, without implying it was submitted.
        chosen = committee.sort_values("robust_rank").iloc[-1]
        rows.append({
            "Function": function,
            "HEBO_inspired": chosen["candidate"],
            "TuRBO_style": trust_region["candidate"],
        })

    print(pd.DataFrame(rows).to_string(index=False))

    # Independent diagnostic: the F8 quadratic was supported by the data
    # and later confirmed by the portal; this line is a model calculation.
    _, point, predicted, residual = f8_additive_quadratic(root)
    coordinates = "-".join(f"{v:.6f}" for v in point)
    print(
        f"\nF8 structural model: {coordinates} -> predicted {predicted:.12f}; "
        f"max residual {residual:.3e}"
    )


if __name__ == "__main__":
    run()
