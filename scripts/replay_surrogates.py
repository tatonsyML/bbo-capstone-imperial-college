#!/usr/bin/env python3
"""Retrospective GP diagnostics, not the historical query-selection algorithm.

Only observations available strictly before the selected round enter training.
No portal outcome is fabricated; newly proposed inputs are unscored.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from bbo.acquisition import expected_improvement, probability_improvement, upper_confidence_bound  # noqa: E402
from bbo.search import portal_string, sobol_points  # noqa: E402
from bbo.surrogates import fit_gp, inverse_mean  # noqa: E402

DIMENSIONS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}


def read_rows(function: int) -> list[dict[str, str]]:
    """Read canonical scores; never train on synthetic or peer returns."""
    with (ROOT / "data" / "all_observations.csv").open(
        newline="", encoding="utf-8"
    ) as handle:
        return [r for r in csv.DictReader(handle) if int(r["function"]) == function]


def load_before_round(function: int, round_number: int):
    """Use only earlier complete X/Y pairs; exclude unknown coordinates."""
    earlier = [r for r in read_rows(function) if int(r["round"]) < round_number]
    d = DIMENSIONS[function]
    pairs = [
        r for r in earlier
        if r["output"].strip() and
        all(r[f"x{i}"].strip() for i in range(1, d + 1))
    ]
    excluded = len(earlier) - len(pairs)
    X = np.asarray([
        [float(r[f"x{i}"]) for i in range(1, d + 1)]
        for r in pairs
    ], dtype=float).reshape(-1, d)
    y = np.asarray([float(r["output"]) for r in pairs], dtype=float)
    if not len(y):
        raise ValueError("No complete training input/output pairs")
    return X, y, excluded, earlier


def actual_submission(function: int, round_number: int):
    """Return recorded portal point; missing historical inputs stay missing."""
    matches = [r for r in read_rows(function) if int(r["round"]) == round_number]
    if len(matches) != 1:
        raise ValueError("Expected precisely one portal record for the round")
    d = DIMENSIONS[function]
    values = [matches[0][f"x{i}"] for i in range(1, d + 1)]
    return [float(v) for v in values] if all(values) else None


def replay(function: int, round_number: int, kernel: str,
           acquisition: str, restarts: int, seed: int, n_power: int,
           beta: float, xi: float) -> dict:
    X, y, excluded, earlier = load_before_round(function, round_number)
    gp, transformer, transformed_y = fit_gp(
        X, y, kernel=kernel, transform="yeo-johnson",
        seed=seed, restarts=restarts,
    )
    pool = sobol_points(DIMENSIONS[function], n_power=n_power, seed=seed)
    mu, sd = gp.predict(pool, return_std=True)
    incumbent = float(np.max(transformed_y))
    if acquisition == "EI":
        acquisition_values = expected_improvement(mu, sd, incumbent, xi=xi)
    elif acquisition == "PI":
        acquisition_values = probability_improvement(mu, sd, incumbent, xi=xi)
    else:
        acquisition_values = upper_confidence_bound(mu, sd, beta=beta)

    winner = int(np.argmax(acquisition_values))
    proposal = np.clip(np.round(pool[winner], 6), 0.0, 0.999999)
    posterior_mu, posterior_sd = gp.predict(
        proposal.reshape(1, -1), return_std=True,
    )

    submitted = actual_submission(function, round_number)
    logged_point_prediction = None
    if submitted is not None:
        known_mu, known_sd = gp.predict(
            np.asarray(submitted, dtype=float).reshape(1, -1),
            return_std=True,
        )
        logged_point_prediction = {
            "submitted_coordinates": submitted,
            "newly_refitted_prediction_raw_location": float(
                inverse_mean(known_mu, transformer)[0]
            ),
            "prediction_sd_transformed_scale": float(known_sd[0]),
            "warning": "Retrospective refit, NOT the recorded original forecast",
        }

    # fit_gp defines covariance as ConstantKernel * base_ARD + WhiteKernel.
    fitted = gp.kernel_
    lengthscales = np.atleast_1d(fitted.k1.k2.length_scale)
    return {
        "provenance": "RETROSPECTIVE_COUNTERFACTUAL_NOT_ORIGINAL_SUBMISSION",
        "function": function,
        "target_round": round_number,
        "training_cut": f"round < {round_number}",
        "earlier_observed_scores": len(earlier),
        "usable_training_pairs": len(y),
        "excluded_rows_with_missing_inputs": excluded,
        "historical_observed_best_before_round": max(
            float(r["output"]) for r in earlier
        ),
        "surrogate": "GaussianProcessRegressor",
        "target_transform": "Yeo-Johnson standardised on pre-round training y",
        "kernel_replay_choice": kernel,
        "fitted_kernel_string": str(fitted),
        "learned_ard_lengthscales": [float(v) for v in lengthscales],
        "learned_signal_variance": float(fitted.k1.k1.constant_value),
        "learned_white_noise_variance": float(fitted.k2.noise_level),
        "optimiser_restarts": restarts,
        "random_seed": seed,
        "acquisition": acquisition,
        "ei_pi_xi": xi if acquisition in ("EI", "PI") else None,
        "ucb_beta": beta if acquisition == "UCB" else None,
        "sobol_candidate_count": len(pool),
        "logged_submission_retrospective_prediction": logged_point_prediction,
        "NEW_UNOBSERVED_counterfactual_candidate": {
            "coordinates": proposal.tolist(),
            "portal_string": portal_string(proposal),
            "predicted_raw_location": float(
                inverse_mean(posterior_mu, transformer)[0]
            ),
            "prediction_sd_transformed_scale": float(posterior_sd[0]),
            "acquisition_score_transformed_scale": float(
                acquisition_values[winner]
            ),
            "real_portal_score": None,
        },
        "limitations": (
            "No claim is made that this kernel, training configuration, "
            "fitted parameters, or newly proposed candidate generated "
            "the actual historical submission. Inverse-transforming a GP "
            "mean is not an exact posterior expectation."
        ),
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--function", type=int, required=True, choices=range(1, 9))
    p.add_argument("--round", type=int, required=True, choices=range(1, 14))
    p.add_argument("--kernel", choices=("RBF", "Matern15", "Matern25"), default="Matern25")
    p.add_argument("--acquisition", choices=("EI", "PI", "UCB"), default="EI")
    p.add_argument("--restarts", type=int, default=4)
    p.add_argument("--seed", type=int, default=909)
    p.add_argument("--n-power", type=int, default=10)
    p.add_argument("--xi", type=float, default=0.0)
    p.add_argument("--beta", type=float, default=1.96)
    p.add_argument("--output", type=Path, help="Optional output path for labelled JSON")
    args = p.parse_args()
    if args.restarts < 0 or not 4 <= args.n_power <= 18:
        p.error("restarts must be non-negative and n-power must be from 4 to 18")
    result = replay(
        args.function, args.round, args.kernel, args.acquisition,
        args.restarts, args.seed, args.n_power, args.beta, args.xi,
    )
    body = json.dumps(result, indent=2, allow_nan=False) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(body, encoding="utf-8")
    print(body, end="")


if __name__ == "__main__":
    main()
