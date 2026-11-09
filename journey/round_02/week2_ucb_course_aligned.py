"""Course-aligned Week 2 capstone analysis using Gaussian Processes and UCB."""

from __future__ import annotations

import ast
import json
import warnings
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist
from sklearn.exceptions import ConvergenceWarning
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF, WhiteKernel

BASE = Path(".")
INITIAL_ZIP = BASE / "source_data" / "Initial_data_points_starter(1).zip"
WEEK1_ZIP = BASE / "source_data" / "capstoneprojectweek1submissionprocessed.zip"

WORK = BASE / "_working"
INITIAL_DIR = WORK / "initial"
WEEK1_DIR = WORK / "week1"

WORK.mkdir(exist_ok=True)

with zipfile.ZipFile(INITIAL_ZIP) as archive:
    archive.extractall(INITIAL_DIR)

with zipfile.ZipFile(WEEK1_ZIP) as archive:
    archive.extractall(WEEK1_DIR)

INITIAL_DATA_DIR = INITIAL_DIR / "initial_data"

print("Data loaded.")

inputs_text = (WEEK1_DIR / "inputs.txt").read_text(encoding="utf-8")
outputs_text = (WEEK1_DIR / "outputs.txt").read_text(encoding="utf-8")

clean_inputs_text = inputs_text.replace("array(", "").replace(")", "")
week1_inputs = [
    np.asarray(point, dtype=float)
    for point in ast.literal_eval(clean_inputs_text)
]
week1_outputs = np.asarray(ast.literal_eval(outputs_text), dtype=float)

for number, (point, output) in enumerate(
    zip(week1_inputs, week1_outputs),
    start=1,
):
    print(f"Function {number}: {point} -> {output}")

def load_original_data(function_number):
    folder = INITIAL_DATA_DIR / f"function_{function_number}"
    X_original = np.load(folder / "initial_inputs.npy")
    y_original = np.load(folder / "initial_outputs.npy").reshape(-1)
    return X_original, y_original

def append_week1_result(function_number):
    X_original, y_original = load_original_data(function_number)

    X_updated = np.vstack(
        [X_original, week1_inputs[function_number - 1]]
    )
    y_updated = np.append(
        y_original, week1_outputs[function_number - 1]
    )

    return X_original, y_original, X_updated, y_updated

def fit_gaussian_process(X, y, random_state):
    dimensions = X.shape[1]

    kernel = (
        ConstantKernel(1.0, (1e-3, 1e3))
        * RBF(
            length_scale=np.full(dimensions, 0.2),
            length_scale_bounds=(0.01, 2.0),
        )
        + WhiteKernel(
            noise_level=1e-6,
            noise_level_bounds=(1e-10, 1e-1),
        )
    )

    model = GaussianProcessRegressor(
        kernel=kernel,
        normalize_y=True,
        n_restarts_optimizer=8,
        random_state=random_state,
    )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ConvergenceWarning)
        model.fit(X, y)

    return model

def create_candidates(dimensions, random_state):
    if dimensions == 2:
        values = np.linspace(0.000001, 0.999999, 501)
        x1_grid, x2_grid = np.meshgrid(values, values)

        return np.column_stack(
            [x1_grid.ravel(), x2_grid.ravel()]
        )

    rng = np.random.default_rng(random_state)

    return rng.uniform(
        low=0.000001,
        high=0.999999,
        size=(300_000, dimensions),
    )

def choose_with_ucb(model, candidates, evaluated_inputs, kappa):
    predicted_mean, predicted_std = model.predict(
        candidates,
        return_std=True,
    )

    ucb_scores = predicted_mean + kappa * predicted_std

    minimum_distances = cdist(
        candidates,
        evaluated_inputs,
    ).min(axis=1)

    ucb_scores[minimum_distances < 0.003] = -np.inf

    selected_index = int(np.argmax(ucb_scores))

    return (
        candidates[selected_index],
        float(predicted_mean[selected_index]),
        float(predicted_std[selected_index]),
        float(ucb_scores[selected_index]),
        float(minimum_distances[selected_index]),
    )

KAPPA = {
    1: 3.0,
    2: 2.5,
    3: 2.0,
    4: 1.0,
    5: 1.0,
    6: 1.0,
    7: 2.0,
    8: 1.5,
}

STRATEGY = {
    1: "Strong exploration",
    2: "Exploration-led balance",
    3: "Balanced",
    4: "Exploitation-led",
    5: "Exploitation-led",
    6: "Exploitation-led",
    7: "Balanced",
    8: "Moderate exploitation",
}

results = []

for function_number in range(1, 9):
    X_original, y_original, X_updated, y_updated = (
        append_week1_result(function_number)
    )

    previous_best_index = int(np.argmax(y_original))
    updated_best_index = int(np.argmax(y_updated))

    model = fit_gaussian_process(
        X_updated,
        y_updated,
        random_state=42 + function_number,
    )

    candidates = create_candidates(
        dimensions=X_updated.shape[1],
        random_state=100 + function_number,
    )

    (
        selected_point,
        predicted_mean,
        predicted_std,
        ucb_score,
        nearest_distance,
    ) = choose_with_ucb(
        model,
        candidates,
        X_updated,
        KAPPA[function_number],
    )

    portal_value = "-".join(
        f"{coordinate:.6f}"
        for coordinate in selected_point
    )

    results.append(
        {
            "Function": function_number,
            "Dimensions": X_updated.shape[1],
            "Previous best output": y_original[previous_best_index],
            "Week 1 output": week1_outputs[function_number - 1],
            "Week 1 produced new best": (
                week1_outputs[function_number - 1]
                > y_original[previous_best_index]
            ),
            "Updated best output": y_updated[updated_best_index],
            "Kappa": KAPPA[function_number],
            "Strategy": STRATEGY[function_number],
            "Portal value": portal_value,
            "Predicted mean": predicted_mean,
            "Predicted standard deviation": predicted_std,
            "UCB score": ucb_score,
            "Distance from nearest evaluated point": nearest_distance,
            "Fitted kernel": str(model.kernel_),
        }
    )

results_df = pd.DataFrame(results)
results_df

for _, row in results_df.iterrows():
    print(f"Function {row['Function']}: {row['Portal value']}")

results_df.to_csv("week2_ucb_results.csv", index=False)