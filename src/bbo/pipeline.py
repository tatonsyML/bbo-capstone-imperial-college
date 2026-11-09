"""Re-run the preserved, historical Week 9 optimisation challenger snapshot.

This is an educational diagnostic pipeline, NOT a replay of final portal
submissions and not a post-capstone full HEBO/TuRBO comparison.
"""
from __future__ import annotations

from pathlib import Path
import pandas as pd

from .diagnostics import load_function, current_best, f8_additive_quadratic
from .optimizer import hebo_inspired_committee, turbo_style_candidate


def run(repo_root=None):
    """Show historical incumbents and unobserved model candidate suggestions.

    The data loader uses observations through Week 9, preserving the data
    available before the Round 10 decisions. It must not silently load the
    final Round 13 results, which would introduce future-information leakage.
    """
    root = Path(repo_root or Path(__file__).resolve().parents[2])
    print("Historical best through Week 9")
    print(current_best(root).to_string(index=False))
    print("\nChallenger proposals (not portal scores)")

    rows = []
    for function in range(1, 9):
        X, y = load_function(root, function)
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
