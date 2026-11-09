"""Capstone BBO Week 4 / Module 15 analysis.

Course-aligned, reproducible support for the 15.1 reflection:
- Gaussian Process remains the primary surrogate.
- SVMs are used as good/bad boundary diagnostics.
- A small one-hidden-layer neural network is used as a diagnostic regressor/classifier.
- Neural-network input sensitivities are estimated locally and repeated across random seeds.
- Round 4 query points are stored explicitly because the final selection was deliberately
  hybrid and function-specific rather than the output of one universal acquisition rule.
"""

from __future__ import annotations

import ast
import math
import warnings
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.exceptions import ConvergenceWarning
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF, WhiteKernel
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

RANDOM_STATE = 42
NN_SEEDS = tuple(range(10))

HERE = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
SOURCE_DIR = HERE / "source_data"
WORK_DIR = HERE / "_working"
RESULTS_DIR = HERE / "results"
WORK_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)

INITIAL_ZIP = SOURCE_DIR / "Initial_data_points_starter(1).zip"
ROUND_INPUTS_FILE = SOURCE_DIR / "inputs_rounds_1_to_3.txt"
ROUND_OUTPUTS_FILE = SOURCE_DIR / "outputs_rounds_1_to_3.txt"
INITIAL_EXTRACT_DIR = WORK_DIR / "initial"
INITIAL_DATA_DIR = INITIAL_EXTRACT_DIR / "initial_data"


def ensure_initial_data_extracted() -> None:
    """Extract the personalised initial data once."""
    if INITIAL_DATA_DIR.exists():
        return
    with zipfile.ZipFile(INITIAL_ZIP) as archive:
        archive.extractall(INITIAL_EXTRACT_DIR)


def parse_numpy_rounds(path: Path) -> list[list[np.ndarray]]:
    """Parse top-level lists containing numpy-style array(...) entries.

    The portal-generated file contains one Python list per round, with long arrays
    sometimes wrapped over multiple physical lines. Bracket counting therefore works
    more reliably than line-by-line parsing.
    """
    text = path.read_text(encoding="utf-8")
    blocks: list[str] = []
    depth = 0
    start: int | None = None

    for idx, char in enumerate(text):
        if char == "[":
            if depth == 0:
                start = idx
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0 and start is not None:
                blocks.append(text[start : idx + 1])
                start = None

    rounds = []
    for block in blocks:
        # The environment is deliberately restricted to numpy.array only.
        parsed = eval(block, {"array": np.array, "__builtins__": {}}, {})
        rounds.append([np.asarray(point, dtype=float) for point in parsed])
    return rounds


def parse_output_rounds(path: Path) -> list[np.ndarray]:
    """Parse one list of eight function outputs per round."""
    return [
        np.asarray(ast.literal_eval(line), dtype=float)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


ensure_initial_data_extracted()
ROUND_INPUTS = parse_numpy_rounds(ROUND_INPUTS_FILE)
ROUND_OUTPUTS = parse_output_rounds(ROUND_OUTPUTS_FILE)

if len(ROUND_INPUTS) != 3 or len(ROUND_OUTPUTS) != 3:
    raise ValueError("Expected exactly three completed query rounds.")
if any(len(r) != 8 for r in ROUND_INPUTS + ROUND_OUTPUTS):
    raise ValueError("Each round must contain results for all eight functions.")


def load_initial(function_number: int) -> tuple[np.ndarray, np.ndarray]:
    folder = INITIAL_DATA_DIR / f"function_{function_number}"
    X = np.load(folder / "initial_inputs.npy")
    y = np.load(folder / "initial_outputs.npy").reshape(-1)
    return np.asarray(X, dtype=float), np.asarray(y, dtype=float)


def build_dataset(function_number: int, rounds: int = 3) -> tuple[np.ndarray, np.ndarray]:
    """Return initial observations plus the requested number of completed rounds."""
    X, y = load_initial(function_number)
    for r in range(rounds):
        X = np.vstack([X, ROUND_INPUTS[r][function_number - 1]])
        y = np.append(y, ROUND_OUTPUTS[r][function_number - 1])
    return X, y


def portal_format(point: np.ndarray) -> str:
    return "-".join(f"{float(v):.6f}" for v in point)


# -----------------------------------------------------------------------------
# 1. Progression through the completed rounds
# -----------------------------------------------------------------------------
progress_rows = []
for fn in range(1, 9):
    X0, y0 = load_initial(fn)
    running_best = float(np.max(y0))
    initial_best = running_best
    row = {
        "Function": fn,
        "Dimensions": X0.shape[1],
        "Initial n": len(y0),
        "Initial best": initial_best,
    }
    for r in range(3):
        value = float(ROUND_OUTPUTS[r][fn - 1])
        row[f"Round {r+1} output"] = value
        row[f"Round {r+1} new best"] = value > running_best
        running_best = max(running_best, value)
    row["Best after Round 3"] = running_best
    progress_rows.append(row)

progress_df = pd.DataFrame(progress_rows)
progress_df.to_csv(RESULTS_DIR / "progression_summary.csv", index=False)


# -----------------------------------------------------------------------------
# 2. Gaussian Process surrogate (primary optimisation model)
# -----------------------------------------------------------------------------
def fit_gp(X: np.ndarray, y: np.ndarray, seed: int) -> GaussianProcessRegressor:
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
        random_state=seed,
    )
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ConvergenceWarning)
        model.fit(X, y)
    return model


gp_rows = []
for fn in range(1, 9):
    X, y = build_dataset(fn, rounds=3)
    gp = fit_gp(X, y, seed=RANDOM_STATE + fn)
    best_idx = int(np.argmax(y))
    mu, std = gp.predict(X[best_idx : best_idx + 1], return_std=True)
    gp_rows.append(
        {
            "Function": fn,
            "n": len(y),
            "Best observed output": float(y[best_idx]),
            "Best observed point": portal_format(X[best_idx]),
            "GP mean at best point": float(mu[0]),
            "GP std at best point": float(std[0]),
            "Fitted kernel": str(gp.kernel_),
        }
    )

gp_df = pd.DataFrame(gp_rows)
gp_df.to_csv(RESULTS_DIR / "gp_summary.csv", index=False)


# -----------------------------------------------------------------------------
# 3. Good/bad classification and SVM support vectors
# -----------------------------------------------------------------------------
def good_bad_labels(y: np.ndarray) -> tuple[np.ndarray, float]:
    """Top third = good; remainder = bad, using the 2/3 empirical quantile."""
    threshold = float(np.quantile(y, 2 / 3))
    labels = (y >= threshold).astype(int)
    return labels, threshold


def classifier_models(seed: int) -> dict[str, Pipeline]:
    return {
        "Logistic regression": Pipeline(
            [
                ("scale", StandardScaler()),
                ("model", LogisticRegression(max_iter=3000, random_state=seed)),
            ]
        ),
        "Linear SVM": Pipeline(
            [
                ("scale", StandardScaler()),
                ("model", SVC(kernel="linear", C=1.0, class_weight="balanced")),
            ]
        ),
        "RBF SVM": Pipeline(
            [
                ("scale", StandardScaler()),
                (
                    "model",
                    SVC(
                        kernel="rbf",
                        C=1.0,
                        gamma="scale",
                        class_weight="balanced",
                    ),
                ),
            ]
        ),
        "Small NN classifier": Pipeline(
            [
                ("scale", StandardScaler()),
                (
                    "model",
                    MLPClassifier(
                        hidden_layer_sizes=(8,),
                        activation="relu",
                        alpha=0.01,
                        solver="lbfgs",
                        max_iter=3000,
                        random_state=seed,
                    ),
                ),
            ]
        ),
    }


classification_rows = []
support_vector_rows = []
for fn in range(1, 9):
    X, y = build_dataset(fn, rounds=3)
    labels, threshold = good_bad_labels(y)
    counts = np.bincount(labels, minlength=2)
    max_splits = int(min(4, counts.min()))
    if max_splits < 2:
        raise ValueError(f"Function {fn}: insufficient class counts for CV")
    cv = StratifiedKFold(n_splits=max_splits, shuffle=True, random_state=RANDOM_STATE)

    for name, model in classifier_models(RANDOM_STATE + fn).items():
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ConvergenceWarning)
            scores = cross_val_score(
                model,
                X,
                labels,
                cv=cv,
                scoring="balanced_accuracy",
            )
        classification_rows.append(
            {
                "Function": fn,
                "Good threshold": threshold,
                "Good observations": int(labels.sum()),
                "Bad observations": int((1 - labels).sum()),
                "Model": name,
                "CV balanced accuracy mean": float(scores.mean()),
                "CV balanced accuracy std": float(scores.std()),
            }
        )

    # Fit the RBF SVM to all current observations and count formal support vectors.
    rbf = classifier_models(RANDOM_STATE + fn)["RBF SVM"]
    rbf.fit(X, labels)
    svc: SVC = rbf.named_steps["model"]
    n_support = int(svc.n_support_.sum())
    support_vector_rows.append(
        {
            "Function": fn,
            "n": len(y),
            "Number of RBF-SVM support vectors": n_support,
            "Support-vector fraction": n_support / len(y),
            "Support vectors in bad class": int(svc.n_support_[0]),
            "Support vectors in good class": int(svc.n_support_[1]),
        }
    )

classification_df = pd.DataFrame(classification_rows)
classification_df.to_csv(RESULTS_DIR / "classification_cv.csv", index=False)
support_vectors_df = pd.DataFrame(support_vector_rows)
support_vectors_df.to_csv(RESULTS_DIR / "rbf_support_vectors.csv", index=False)


# -----------------------------------------------------------------------------
# 4. Small NN regression and local input sensitivities
# -----------------------------------------------------------------------------
def fit_nn_regressor(X: np.ndarray, y: np.ndarray, seed: int) -> Pipeline:
    """One hidden layer; deliberately small for the sparse capstone data."""
    model = Pipeline(
        [
            ("scale", StandardScaler()),
            (
                "model",
                MLPRegressor(
                    hidden_layer_sizes=(8,),
                    activation="relu",
                    alpha=0.01,
                    solver="lbfgs",
                    max_iter=3000,
                    random_state=seed,
                ),
            ),
        ]
    )
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ConvergenceWarning)
        model.fit(X, y)
    return model


def finite_difference_gradient(
    model: Pipeline,
    point: np.ndarray,
    step: float = 1e-4,
) -> np.ndarray:
    """Estimate d(prediction)/d(input_i) in original input units.

    Central differences are used away from the 0/1 boundaries; one-sided differences
    are used when the point lies close to a boundary.
    """
    point = np.asarray(point, dtype=float)
    gradient = np.zeros_like(point)
    base_prediction = float(model.predict(point.reshape(1, -1))[0])

    for j in range(point.size):
        lower = point.copy()
        upper = point.copy()
        can_lower = point[j] - step >= 0.0
        can_upper = point[j] + step <= 1.0

        if can_lower and can_upper:
            lower[j] -= step
            upper[j] += step
            y_low = float(model.predict(lower.reshape(1, -1))[0])
            y_high = float(model.predict(upper.reshape(1, -1))[0])
            gradient[j] = (y_high - y_low) / (2 * step)
        elif can_upper:
            upper[j] += step
            y_high = float(model.predict(upper.reshape(1, -1))[0])
            gradient[j] = (y_high - base_prediction) / step
        elif can_lower:
            lower[j] -= step
            y_low = float(model.predict(lower.reshape(1, -1))[0])
            gradient[j] = (base_prediction - y_low) / step

    return gradient


gradient_rows = []
for fn in range(1, 9):
    X, y = build_dataset(fn, rounds=3)
    best_idx = int(np.argmax(y))
    best_point = X[best_idx]
    seed_gradients = []

    for seed in NN_SEEDS:
        nn = fit_nn_regressor(X, y, seed=1000 + 100 * fn + seed)
        seed_gradients.append(finite_difference_gradient(nn, best_point))

    G = np.asarray(seed_gradients)
    median_gradient = np.median(G, axis=0)
    median_abs_gradient = np.median(np.abs(G), axis=0)
    sign_consistency = np.abs(np.mean(np.sign(G), axis=0))
    robust_score = median_abs_gradient * sign_consistency

    for j in range(X.shape[1]):
        gradient_rows.append(
            {
                "Function": fn,
                "Input": f"x{j+1}",
                "Median local gradient": float(median_gradient[j]),
                "Median absolute gradient": float(median_abs_gradient[j]),
                "Sign consistency (0-1)": float(sign_consistency[j]),
                "Robust sensitivity score": float(robust_score[j]),
            }
        )

gradients_df = pd.DataFrame(gradient_rows)
gradients_df["Rank within function"] = (
    gradients_df.groupby("Function")["Robust sensitivity score"]
    .rank(method="first", ascending=False)
    .astype(int)
)
gradients_df = gradients_df.sort_values(["Function", "Rank within function"])
gradients_df.to_csv(RESULTS_DIR / "nn_gradient_summary.csv", index=False)


# -----------------------------------------------------------------------------
# 5. NN versus a simpler linear regressor
# -----------------------------------------------------------------------------
regression_rows = []
for fn in range(1, 9):
    X, y = build_dataset(fn, rounds=3)
    # Four folds where possible, otherwise three. Shuffling avoids relying on data order.
    n_splits = min(4, len(y))
    cv = KFold(n_splits=n_splits, shuffle=True, random_state=RANDOM_STATE)
    models = {
        "Linear regression": Pipeline(
            [("scale", StandardScaler()), ("model", LinearRegression())]
        ),
        "Small NN regressor": Pipeline(
            [
                ("scale", StandardScaler()),
                (
                    "model",
                    MLPRegressor(
                        hidden_layer_sizes=(8,),
                        activation="relu",
                        alpha=0.01,
                        solver="lbfgs",
                        max_iter=3000,
                        random_state=RANDOM_STATE + fn,
                    ),
                ),
            ]
        ),
    }

    y_scale = max(float(np.std(y)), 1e-12)
    for name, model in models.items():
        fold_nrmse = []
        for train_idx, test_idx in cv.split(X):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", ConvergenceWarning)
                model.fit(X[train_idx], y[train_idx])
            pred = model.predict(X[test_idx])
            rmse = math.sqrt(mean_squared_error(y[test_idx], pred))
            fold_nrmse.append(rmse / y_scale)
        regression_rows.append(
            {
                "Function": fn,
                "Model": name,
                "CV normalised RMSE mean": float(np.mean(fold_nrmse)),
                "CV normalised RMSE std": float(np.std(fold_nrmse)),
            }
        )

regression_df = pd.DataFrame(regression_rows)
regression_df.to_csv(RESULTS_DIR / "regression_cv.csv", index=False)


# -----------------------------------------------------------------------------
# 6. Round 4 queries
# -----------------------------------------------------------------------------
# These are stored explicitly because the final choice was hybrid and function-specific:
# GP evidence was combined with local observation, SVM boundary checks, NN sensitivity,
# and a deliberate decision about exploration versus exploitation for each function.
ROUND4_QUERIES = {
    1: np.array([0.999999, 0.999999]),
    2: np.array([0.705000, 0.999999]),
    3: np.array([0.490000, 0.620000, 0.360000]),
    4: np.array([0.425128, 0.426376, 0.368659, 0.411895]),
    5: np.array([0.508373, 0.999999, 0.999999, 0.999999]),
    6: np.array([0.481359, 0.256800, 0.814241, 0.999999, 0.057285]),
    7: np.array([0.015000, 0.369270, 0.256273, 0.262985, 0.391467, 0.834089]),
    8: np.array(
        [0.104617, 0.061316, 0.059110, 0.079660, 0.982960, 0.230739, 0.140986, 0.537241]
    ),
}

ROUND4_RATIONALE = {
    1: "Exploration: observations remain effectively flat around zero.",
    2: "Controlled exploitation near the new Round 3 best.",
    3: "Return to the successful local region after the poor Round 2 excursion.",
    4: "Tight local refinement because nearby points show rapid output change.",
    5: "Exploit the strong high-x2/high-x3/high-x4 region; x3/x4 already at the upper bound.",
    6: "Continue the successful local direction from Round 3 rather than the failed Round 2 move.",
    7: "Local refinement after the Round 3 improvement, with a deliberate change in x1.",
    8: "Cautious local continuation around the new best rather than a large global move.",
}

round4_rows = []
for fn, point in ROUND4_QUERIES.items():
    round4_rows.append(
        {
            "Function": fn,
            "Portal value": portal_format(point),
            "Rationale": ROUND4_RATIONALE[fn],
        }
    )
round4_df = pd.DataFrame(round4_rows)
round4_df.to_csv(RESULTS_DIR / "round4_queries.csv", index=False)
(RESULTS_DIR / "round4_portal_values.txt").write_text(
    "\n".join(
        f"Function {row['Function']}: {row['Portal value']}"
        for _, row in round4_df.iterrows()
    )
    + "\n",
    encoding="utf-8",
)


# -----------------------------------------------------------------------------
# 7. Compact evidence summary for the 15.1 reflection
# -----------------------------------------------------------------------------
print("\nROUND PROGRESSION")
print(progress_df.to_string(index=False))

print("\nCLASSIFICATION: MEAN BALANCED ACCURACY")
classification_pivot = classification_df.pivot(
    index="Function", columns="Model", values="CV balanced accuracy mean"
)
print(classification_pivot.round(3).to_string())

print("\nRBF-SVM SUPPORT-VECTOR FRACTIONS")
print(
    support_vectors_df[["Function", "Support-vector fraction"]]
    .round(3)
    .to_string(index=False)
)

print("\nTOP NN REGRESSION SENSITIVITIES")
print(
    gradients_df[gradients_df["Rank within function"] <= 3][
        [
            "Function",
            "Input",
            "Median local gradient",
            "Sign consistency (0-1)",
            "Robust sensitivity score",
            "Rank within function",
        ]
    ]
    .round(4)
    .to_string(index=False)
)

print("\nLINEAR REGRESSION VS SMALL NN: LOWER NRMSE IS BETTER")
regression_pivot = regression_df.pivot(
    index="Function", columns="Model", values="CV normalised RMSE mean"
)
print(regression_pivot.round(3).to_string())

print("\nROUND 4 PORTAL VALUES")
for _, row in round4_df.iterrows():
    print(f"Function {row['Function']}: {row['Portal value']}")

print("\nVerification note:")
print(
    "The clean repeated-seed NN regression check makes F5's x2/x4 directions particularly "
    "clear. For F7, x1 is a strong local signal, while the ranking of other dimensions is "
    "more model/seed dependent. Treat that instability as evidence to reduce confidence, "
    "not as a reason to force a single gradient story."
)