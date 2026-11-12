#!/usr/bin/env python3
"""Post-capstone, reproducible HEBO versus BoTorch TuRBO-1 benchmark.

This is NOT the optimiser used to submit the original 13 course rounds.

Two deliberately different experiments are available:
  1. "f8": both algorithms begin with exactly the same 40 course F8 points
     and receive an equal number of NEW evaluations from a fitted-quadratic
     SIMULATOR, not from the private capstone portal.
  2. "proposals": generate UNOBSERVED one-step candidates for F1-F8 using
     the Week 9 observation cutoff. These candidates have no known score.

Use --engine hebo and --engine turbo in separate environments if necessary.
Both engines generate one six-decimal query at a time. Every simulated
evaluation, including repeats and restarts, is charged against the budget.

Official HEBO source: https://github.com/huawei-noah/HEBO/tree/master/HEBO
TuRBO reference: https://botorch.org/docs/tutorials/turbo_1
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from importlib import metadata
import math
from pathlib import Path
import random
import warnings

import numpy as np
import pandas as pd

# Portal inputs were six-decimal real numbers, with 1.000000 disallowed.
UPPER = 0.999999
DIMS = (2, 2, 3, 4, 4, 5, 6, 8)


def coordinates(rows: pd.DataFrame, dim: int) -> tuple[np.ndarray, np.ndarray]:
    """Extract x and y WITHOUT mixing external classmates' observations."""
    x = rows[[f"x{i}" for i in range(1, dim + 1)]].to_numpy(float)
    y = rows["output"].to_numpy(float)
    if len(y) == 0 or not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError("Missing, empty or non-finite observations")
    if (x < 0).any() or (x > UPPER + 1e-10).any():
        raise ValueError("Observed coordinates outside the permitted portal domain")
    return x, y


def week9_history(root: Path, function: int) -> tuple[np.ndarray, np.ndarray]:
    """Same fixed historical cutoff for all one-step counterfactuals.

    We intentionally do not allow Week 10-13 outcomes to leak into an
    algorithm supposedly making a decision at the end of Week 9.
    """
    if not (1 <= function <= 8):
        raise ValueError("Function must be 1 through 8")
    path = root / "data/accumulated" / f"function_{function}" / "observations_through_week9.csv"
    return coordinates(pd.read_csv(path), DIMS[function - 1])


def portal_point(x: np.ndarray) -> np.ndarray:
    """Convert a suggested real vector into a legal six-decimal query."""
    z = np.asarray(x, float).reshape(-1)
    if not np.isfinite(z).all():
        raise ValueError("Optimizer returned non-finite input")
    return np.round(np.clip(z, 0, UPPER), 6)


def portal_text(x: np.ndarray) -> str:
    return "-".join(f"{v:.6f}" for v in portal_point(x))


def f8_design(x: np.ndarray) -> np.ndarray:
    """Additive quadratic basis: constant + 8 linear + 8 squared = 17.

    Deliberately omit cross-products. Testing this structural hypothesis
    is part of the retrospective analysis, not an assertion about
    the unknown underlying code.
    """
    x = np.asarray(x, float).reshape(-1, 8)
    return np.column_stack([np.ones(len(x))] +
                           [col for i in range(8) for col in (x[:, i], x[:, i] ** 2)])


def build_f8_simulator(root: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict]:
    """Fit only the 40 initial course observations and test 13 later returns.

    The held-out portal results never enter the fitted coefficients.
    This model supplies an affordable artificial evaluator for comparing
    algorithms under controlled, *simulated* feedback.
    """
    path = root / "data/accumulated/function_8/observations_through_week13.csv"
    rows = pd.read_csv(path)
    course = rows.loc[rows["is_initial"].astype(str).str.lower() == "true"]
    holdout = rows.loc[rows["is_initial"].astype(str).str.lower() != "true"]
    if len(course) != 40 or len(holdout) != 13:
        raise ValueError("Expected 40 course observations and 13 later F8 returns")
    x0, y0 = coordinates(course, 8)
    xh, yh = coordinates(holdout, 8)
    design = f8_design(x0)
    coef, _, rank, _ = np.linalg.lstsq(design, y0, rcond=None)
    if rank != 17:
        raise ValueError("Initial F8 points do not identify 17 coefficients")
    error = float(np.max(np.abs(f8_design(xh) @ coef - yh)))
    # A failed external-to-fit check would make this an unsuitable evaluator.
    if error > 1e-6:
        raise ValueError(f"F8 simulator fails held-out validation: {error}")
    linear, quadratic = coef[1::2], coef[2::2]
    centre = -linear / (2 * quadratic)
    peak = (f8_design(centre) @ coef).item()
    meta = {"initial_points": len(x0), "held_out_points": len(xh),
            "max_holdout_error": error, "fitted_peak": peak,
            "centre": portal_text(centre)}
    return x0, y0, coef, meta


def simulated_f8_score(coefficients: np.ndarray, query: np.ndarray) -> float:
    """F8 QUADRATIC MODEL prediction, never a private portal return."""
    return (f8_design(portal_point(query)) @ coefficients).item()


def set_seed(seed: int) -> None:
    """Seed random sampling without implying complete cross-version determinism."""
    np.random.seed(seed)
    random.seed(seed)
    try:
        import torch
        torch.manual_seed(seed)
        torch.set_num_threads(1)
    except ImportError:
        pass


def new_hebo(x: np.ndarray, y: np.ndarray, seed: int):
    """Instantiate and warm-start the OFFICIAL HEBO package.

    HEBO minimises: observe negative observed scores to maximise the capstone
    function. This negation must also be used for every subsequent feedback.
    """
    try:
        from hebo.design_space.design_space import DesignSpace
        from hebo.optimizers.hebo import HEBO
    except ImportError as exc:
        raise RuntimeError("Official HEBO is missing. Install benchmark HEBO requirements.") from exc
    set_seed(seed)
    labels = [f"x{i}" for i in range(1, x.shape[1] + 1)]
    space = DesignSpace().parse(
        [{"name": c, "type": "num", "lb": 0.0, "ub": UPPER} for c in labels]
    )
    optimiser = HEBO(space)
    optimiser.observe(pd.DataFrame(x, columns=labels), -y.reshape(-1, 1))
    return optimiser


def hebo_next(optimiser) -> np.ndarray:
    return portal_point(optimiser.suggest(n_suggestions=1).iloc[0].to_numpy(float))


def hebo_feedback(optimiser, query: np.ndarray, score: float) -> None:
    """Tell official HEBO about the paid evaluation (negative for minimisation)."""
    labels = [f"x{i}" for i in range(1, len(query) + 1)]
    optimiser.observe(pd.DataFrame([query], columns=labels),
                      np.asarray([[-float(score)]]))


@dataclass
class TurboState:
    """Single trust-region state modelled on the published BoTorch TuRBO-1.

    Unlike the capstone's old 'TuRBO-style' EI-in-a-box challenger, this state
    *actually changes length* after consecutive gains or failures and triggers
    restarts. Settings follow the paper's success_tolerance=3 for batch=1.
    """
    dim: int
    length: float = 0.8
    length_min: float = 0.5 ** 7
    length_max: float = 1.6
    success_tolerance: int = 3
    success_counter: int = 0
    failure_counter: int = 0
    best_value: float = -float("inf")
    restart_triggered: bool = False

    @property
    def failure_tolerance(self) -> int:
        # One evaluation per step; higher dimensions need more failures before shrinkage.
        return math.ceil(max(4.0, float(self.dim)))

    def update(self, value: float) -> None:
        # Relative improvement avoids expanding for numerical noise alone.
        improvement = value > self.best_value + 1e-3 * abs(self.best_value)
        if improvement:
            self.success_counter += 1
            self.failure_counter = 0
        else:
            self.failure_counter += 1
            self.success_counter = 0
        if self.success_counter >= self.success_tolerance:
            self.length = min(self.length * 2, self.length_max)
            self.success_counter = 0
        elif self.failure_counter >= self.failure_tolerance:
            self.length /= 2
            self.failure_counter = 0
        self.best_value = max(self.best_value, float(value))
        if self.length < self.length_min:
            self.restart_triggered = True


def turbo_next(x: np.ndarray, y: np.ndarray, state: TurboState, seed: int) -> np.ndarray:
    """BoTorch-based TuRBO-1 proposal, using ARD Matérn GP and Thompson sampling.

    The GP learns from the CURRENT trust-region observations, not fabricated
    black-box calls. Axis-dependent lengthscales stretch each dimension
    differently. Posterior sampling then chooses an uncertain/promising point
    from a Sobol-generated perturbation pool.
    """
    try:
        import torch
        from botorch.fit import fit_gpytorch_mll
        from botorch.generation import MaxPosteriorSampling
        from botorch.models import SingleTaskGP
        from gpytorch.constraints import Interval
        from gpytorch.kernels import MaternKernel, ScaleKernel
        from gpytorch.likelihoods import GaussianLikelihood
        from gpytorch.mlls import ExactMarginalLogLikelihood
    except ImportError as exc:
        raise RuntimeError("BoTorch/GPyTorch missing. Install TuRBO benchmark requirements.") from exc

    if not len(y):
        raise ValueError("TuRBO needs evaluated local points before proposing a query")
    set_seed(seed)
    d = x.shape[1]
    tx = torch.as_tensor(x, dtype=torch.double)
    ty = torch.as_tensor(y, dtype=torch.double).reshape(-1, 1)
    # The GP's objective scale is standardised for stable hyperparameter fitting.
    scale = torch.clamp(ty.std(unbiased=False), min=1e-6)
    train_y = (ty - ty.mean()) / scale
    kernel = ScaleKernel(MaternKernel(nu=2.5, ard_num_dims=d,
                        lengthscale_constraint=Interval(0.005, 4.0)))
    likelihood = GaussianLikelihood(noise_constraint=Interval(1e-8, 1e-3))
    model = SingleTaskGP(tx, train_y, covar_module=kernel, likelihood=likelihood)
    mll = ExactMarginalLogLikelihood(model.likelihood, model)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fit_gpytorch_mll(mll)
    model.eval()

    centre = tx[int(torch.argmax(ty)), :]
    # Normalised per-dimension GP lengthscales define the trust-region shape.
    with torch.no_grad():
        lengthscales = model.covar_module.base_kernel.lengthscale.flatten()
        weights = lengthscales / lengthscales.mean()
        weights = weights / torch.prod(weights.pow(1.0 / d))
        lower = torch.clamp(centre - weights * state.length / 2, 0, UPPER)
        upper = torch.clamp(centre + weights * state.length / 2, 0, UPPER)

        # Generate local Sobol proposals and perturb a subset of dimensions.
        n_candidates = min(5000, max(2000, 200 * d))
        sobol = torch.quasirandom.SobolEngine(d, scramble=True, seed=seed)
        proposals = lower + (upper - lower) * sobol.draw(n_candidates).to(torch.double)
        mask = torch.rand(n_candidates, d) <= min(20.0 / d, 1.0)
        empty = torch.where(mask.sum(dim=1) == 0)[0]
        if len(empty):
            mask[empty, torch.randint(0, d, (len(empty),))] = True
        choices = centre.expand(n_candidates, d).clone()
        choices[mask] = proposals[mask]
        sample = MaxPosteriorSampling(model, replacement=False)(choices, num_samples=1)
        result = sample.reshape(-1).cpu().numpy()
    return portal_point(result)


def versions() -> pd.DataFrame:
    names = ("HEBO", "botorch", "gpytorch", "torch", "numpy", "pandas", "scipy")
    rows = []
    for name in names:
        try:
            version = metadata.version(name)
        except metadata.PackageNotFoundError:
            version = "NOT INSTALLED"
        rows.append({"package": name, "version": version})
    return pd.DataFrame(rows)


def run_f8(root: Path, out: Path, engine: str, budget: int, seeds: list[int]) -> None:
    """Closed-loop model simulation, with identical data and a paid query budget.

    The only evaluator here is simulated_f8_score. F8 portal observations in
    Weeks 1-13 are NEVER supplied as feedback to these counterfactual runs.
    """
    x0, y0, coef, meta = build_f8_simulator(root)
    pd.DataFrame([meta]).to_csv(out / "f8_oracle_validation.csv", index=False)
    records = []

    for seed in seeds:
        set_seed(seed)
        # Global history records all paid queries; local history is reset by TuRBO.
        global_x = x0.copy()
        global_best = float(y0.max())
        local_x, local_y = x0.copy(), y0.copy()
        pending_restart: list[np.ndarray] = []
        if engine == "hebo":
            optimiser = new_hebo(local_x, local_y, seed)
        else:
            state = TurboState(dim=8, best_value=global_best)

        for step in range(1, budget + 1):
            phase = "model"
            if engine == "hebo":
                query = hebo_next(optimiser)
            elif pending_restart:
                phase = "paid_restart_initialisation"
                query = pending_restart.pop(0)
            else:
                query = turbo_next(local_x, local_y, state, seed + 1000 * step)

            # Six-decimal rounding is applied BEFORE evaluating or counting repeats.
            query = portal_point(query)
            duplicate = bool(np.any(np.all(np.round(global_x, 6) == query, axis=1)))
            result = simulated_f8_score(coef, query)
            old_best = global_best
            global_best = max(global_best, result)
            global_x = np.vstack([global_x, query])
            records.append({
                "engine": engine, "seed": seed, "step": step, "phase": phase,
                "candidate": portal_text(query), "SIMULATED_output": result,
                "SIMULATED_best": global_best, "SIMULATED_gain": global_best - old_best,
                "duplicate": duplicate, "trust_region_length":
                    (state.length if engine == "turbo" else np.nan),
            })

            if engine == "hebo":
                hebo_feedback(optimiser, query, result)
                continue

            # TuRBO updates the trust region only after REAL feedback from
            # this benchmark's fitted simulator, never from an unobserved point.
            local_x = np.vstack([local_x, query])
            local_y = np.append(local_y, result)
            if phase == "paid_restart_initialisation":
                # New trust region is usable after its paid initial design arrives.
                if not pending_restart:
                    state = TurboState(dim=8, best_value=float(local_y.max()))
            else:
                state.update(result)

            if state.restart_triggered and step < budget:
                # TuRBO restarts require NEW evaluations, not free random seeds.
                remaining = budget - step
                count = min(2 * 8, remaining)
                from torch.quasirandom import SobolEngine
                points = SobolEngine(8, scramble=True, seed=seed + 100000 + step)
                pending_restart = [portal_point(z) for z in points.draw(count).numpy()]
                local_x = np.empty((0, 8))
                local_y = np.empty((0,))
                state = TurboState(dim=8)
                records[-1]["restart_triggered"] = True

    # Separate per-engine files permit dependency-incompatible virtualenvs.
    pd.DataFrame(records).to_csv(out / f"f8_simulation_{engine}.csv", index=False)
    print(f"{engine}: wrote {len(records)} SIMULATED evaluation records. No portal queries made.")


def run_proposals(root: Path, out: Path, engine: str, seeds: list[int]) -> None:
    """No evaluator exists for unqueried F1-F8 points; DO NOT assign outputs."""
    records = []
    for fn in range(1, 9):
        x, y = week9_history(root, fn)
        for seed in seeds:
            if engine == "hebo":
                query = hebo_next(new_hebo(x, y, seed))
            else:
                query = turbo_next(x, y, TurboState(dim=len(x[0]),
                                   best_value=float(y.max())), seed)
            distance = float(np.min(np.linalg.norm(x - query, axis=1)))
            records.append({
                "function": fn, "engine": engine, "seed": seed,
                "candidate": portal_text(query), "nearest_past_distance": distance,
                "historic_best": float(y.max()), "portal_output": "NOT OBSERVED",
            })
    pd.DataFrame(records).to_csv(out / f"one_step_proposals_{engine}.csv", index=False)
    print(f"{engine}: wrote {len(records)} UNSCORED retrospective proposals.")


def compare_f8(out: Path) -> pd.DataFrame:
    """Compare only real stored SIMULATION rows, never invented portal scores."""
    frames = []
    for engine in ("hebo", "turbo"):
        path = out / f"f8_simulation_{engine}.csv"
        if not path.exists():
            raise FileNotFoundError(f"First execute and save the {engine} run: {path}")
        frame = pd.read_csv(path)
        if not {"engine", "seed", "step", "SIMULATED_best", "duplicate"}.issubset(frame):
            raise ValueError(f"Wrong benchmark schema: {path}")
        frames.append(frame)
    full = pd.concat(frames, ignore_index=True)
    if full.duplicated(["engine", "seed", "step"]).any():
        raise ValueError("Duplicate engine/seed/step keys")
    counts = full.groupby(["engine", "seed"]).step.nunique()
    if counts.nunique() != 1:
        raise ValueError("Budget mismatch: algorithms must receive equal evaluations")
    seeded = full.groupby(["engine", "seed"], as_index=False).agg(
        evaluations=("step", "max"), SIMULATED_final_best=("SIMULATED_best", "last"),
        duplicate_queries=("duplicate", "sum"))
    for seed in seeded.seed.unique():
        if set(seeded.loc[seeded.seed == seed, "engine"]) != {"hebo", "turbo"}:
            raise ValueError(f"Unequal seed coverage: {seed}")
    validation = pd.read_csv(out / "f8_oracle_validation.csv")
    seeded["SIMULATED_regret_to_model_peak"] = (
        float(validation.fitted_peak.iloc[0]) - seeded.SIMULATED_final_best
    )
    seeded.to_csv(out / "f8_simulation_comparison.csv", index=False)
    return seeded


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."),
                        help="Capstone repository root containing data/accumulated")
    parser.add_argument("--out", type=Path, default=Path("results/full_hebo_turbo"))
    parser.add_argument("--engine", choices=["hebo", "turbo", "both"], default="both")
    parser.add_argument("--mode", choices=["f8", "proposals", "all", "compare"], default="all")
    parser.add_argument("--budget", type=int, default=12)
    parser.add_argument("--seeds", type=int, nargs="+", default=[0, 1, 2])
    args = parser.parse_args()
    if args.budget < 1 or not args.seeds:
        parser.error("Supply positive budget and at least one seed")
    args.out.mkdir(parents=True, exist_ok=True)

    if args.mode == "compare":
        print(compare_f8(args.out).to_string(index=False))
        return

    # Record the installed runtime; different engine environments need not
    # be combined if the official packages have conflicting requirements.
    for engine in (["hebo", "turbo"] if args.engine == "both" else [args.engine]):
        versions().to_csv(args.out / f"versions_{engine}.csv", index=False)
        if args.mode in ("f8", "all"):
            run_f8(args.root, args.out, engine, args.budget, args.seeds)
        if args.mode in ("proposals", "all"):
            run_proposals(args.root, args.out, engine, args.seeds)


if __name__ == "__main__":
    main()
