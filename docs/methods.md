# Optimisation methods, source code and reproduction

[← Main README](../README.md) · [How to run the benchmark](../research/full_optimisers/README.md) · [Model card](../MODEL_CARD.md) · [Final measured results](../journey/round_13/README.md)

## What was implemented and when?

**The capstone and the later benchmark are deliberately separate.** During the 13-round challenge I used Gaussian-process surrogate models, acquisition functions, controlled probes, structural investigations and *HEBO-inspired* / *TuRBO-style* challenger mechanisms. The **full official-HEBO / BoTorch TuRBO-1 comparison code was added after the challenge**. It was not used to pick historical portal inputs. This distinction matters when checking methodology against the historical evidence.

| Method | Code | What it actually does | Status |
|---|---|---|---|
| Gaussian Process with ARD RBF/Matérn | [surrogates.py](../src/bbo/surrogates.py) | Fits a probabilistic surrogate and an optional response transform | Historical implementation |
| EI, PI, UCB | [acquisition.py](../src/bbo/acquisition.py) | Ranks proposed inputs using model means and uncertainty | Historical implementation |
| Sobol / local bounds | [search.py](../src/bbo/search.py) | Generates feasible candidate pools | Historical implementation |
| HEBO-inspired committee | [optimizer.py: hebo_inspired_committee](../src/bbo/optimizer.py) | Compares three kernels with transformed EI/PI/UCB rank consensus | **Not official HEBO** |
| TuRBO-style local candidate | [optimizer.py: turbo_style_candidate](../src/bbo/optimizer.py) | Fits a GP and maximises EI inside one fixed incumbent-centred box | **Not full TuRBO** |
| Actual HEBO library | [benchmark.py: new_hebo](../research/full_optimisers/benchmark.py) | Calls `HEBO`, supplies observed negative scores, and feeds back subsequent simulated evaluations | Post-capstone reference engine |
| BoTorch-based TuRBO-1 | [benchmark.py: TurboState/turbo_next](../research/full_optimisers/benchmark.py) | Uses ARD Matérn GP, Thompson-sampling candidates, adaptive trust-region length and budgeted restarts | Post-capstone reference implementation |
| F8 structural challenger | [structural_validation.py](../src/bbo/structural_validation.py) | Fit 17 coefficients to original 40 and predict 13 later returned portal scores | Retrospective independent test |
| GP robustness and input/output warping | [robust_and_warp.py](../journey/round_12/original/robust_and_warp.py) | Test how transformations and excluded sources affect GP predictions | Week 12 analysis |
| PCA, kernel PCA, Extra Trees, MLP, PLS and Bayesian Ridge | [review_round12.py](../journey/round_12/original/review_round12.py) | Compare model families and dimensional structure | Week 12 analysis |
| Optuna TPE and local quadratic fits | [tpe_local.py](../journey/round_12/original/tpe_local.py) | Propose candidates using TPE and study F4 local curvature | Week 12 analysis |
| Trust-region Thompson sampling | [trust_region_ts.py](../journey/round_12/original/trust_region_ts.py) | Test feedback-dependent trust-region proposals | Week 12 analysis |
| Controlled coordinate probes | [Round 5](../journey/round_05/README.md) · [F5](../functions/F5/README.md) | Assess local sensitivity and boundary effects | Original round experiments |
| DBSCAN analysis of search density | [Clustering study](../research/diagnostics/clustering/README.md) | Compare observed clusters with high-scoring points; published code is a later reproducible diagnostic | Week 11 analysis, later diagnostic |

**Saved historical candidate comparisons:** [HEBO-inspired committee suggestions](../results/hebo_inspired_committee.csv), [TuRBO-style local proposals](../results/turbo_style_challengers.csv) and [structural candidate alternatives](../results/structural_challengers.csv). These contain model proposals and forecasts, **not additional portal measurements**. The [279 observed returns and starting points](../data/all_observations.csv) remain the source for measured outcomes.

## The logic behind the code

### 1. GP modelling

Each function has only a small number of observations relative to its dimension. `fit_gp` therefore uses a Gaussian Process to estimate both the response and its uncertainty. We compare RBF with Matérn 1.5 and 2.5 kernels because their smoothness assumptions differ. Automatic Relevance Determination (ARD) assigns one lengthscale to each input. A separate WhiteKernel permits observational noise, but does not prove the hidden function is noisy.

**Why output transformation?** F1's responses can be almost zero and F5's vary by thousands. Yeo–Johnson handles both positive and negative values, improving numerical scaling in some cases. `inverse_mean` reverses that transformation for readability; it is not an exact posterior expectation under a nonlinear transform.

### 2. Choosing one query

EI combines predicted improvement with uncertainty. PI considers the probability of beating an incumbent. UCB gives additional value to uncertainty. Their numerical units differ, so the custom committee **ranks** candidates within each acquisition function instead of directly adding raw acquisition values. The original course permitted only one query per function per round, making each selected input worth its limited evaluation budget.

### 3. What the original 'TuRBO-style' code missed

A single fixed box around the current incumbent helps local optimisation. **Full TuRBO-1 also needs feedback-dependent length changes, lengthscale-weighted trust regions, perturbation sampling, restart rules and a new paid initialisation after a restart.** Those mechanisms appear in the new benchmark implementation, not in the historical `turbo_style_candidate`.

### 4. Why official HEBO is different from a HEBO-inspired committee

The original committee explored model and acquisition diversity, but does not reproduce HEBO's own full fitting and evolutionary acquisition optimisation. The benchmark calls Huawei's **actual HEBO package** and follows its minimisation convention: to maximise capstone score \(f(x)\), we pass **\(-f(x)\)** to `observe`.

## Fair comparison: two experiments, not one misleading leaderboard

### Experiment A: identical-budget F8 simulation

1. Fit a 17-coefficient additive quadratic **only to 40 original F8 course observations**.
2. Check it independently against **13 later F8 portal returns**. These results do not enter fitting.
3. Give official HEBO and BoTorch TuRBO-1 the **same 40 initial observed inputs and outputs**.
4. Allow each algorithm, for each random seed, **12 new queries** by default. New queries, duplicates, and TuRBO restarts all consume the same budget.
5. Return numerical feedback from the **fitted F8 quadratic simulator**, not from the private portal.
6. Compare best simulated value, simulated regret to the fitted peak and duplicate rates. Record package versions and seeds.

**Interpretation:** this tests methods on a **retrospectively fitted model** of F8, not their historical portal performance. Fitting F8 structure from the initial 40 is independently reproducible, but that does not authenticate the undisclosed source formula everywhere.

### Experiment B: eight one-step, unscored proposals

Read the same **through-Week-9** historical observation snapshot for each function, and ask each algorithm for one counterfactual candidate. These are not scored, because the capstone portal has not returned outputs at those new points. The comparison can report input feasibility and nearest-known-point distance. **Do not claim a method beat another method on F1–F7 from unobserved proposals.**

## What this code does *not* establish

- That complete HEBO or TuRBO was used in any of the user's real submitted rounds.
- That simulated F8 objective returns are real portal scores.
- That a single best candidate would dominate on eight different unknown functions.
- That a candidate chosen using the final history was actually available before its original submission date.
- That the optional HEBO and BoTorch engines have been executed here: **their packages are not available during the code review**, so no numeric algorithm-versus-algorithm verdict is recorded.

## Code-reading route

1. [optimizer.py](../src/bbo/optimizer.py): historical mechanisms, input, output and explanatory comments.
2. [surrogates.py](../src/bbo/surrogates.py) + [acquisition.py](../src/bbo/acquisition.py): model assumptions and the exploration/exploitation trade-off.
3. [Historical pipeline](../src/bbo/pipeline.py): how candidates were generated from the Week 9 snapshot.
4. [Full comparison benchmark](../research/full_optimisers/benchmark.py): model simulation, feedback loop, fair budgets and restarts.
5. [Benchmark unit tests](../research/full_optimisers/test_benchmark.py): the 17-parameter model, exact held-out check, trust-region state and failure tests.
6. [Run instructions and interpretation](../research/full_optimisers/README.md).

## Technical sources

- [Huawei Noah's Ark official HEBO repository](https://github.com/huawei-noah/HEBO/tree/master/HEBO) and [documented HEBO minimisation API](https://hebo.readthedocs.io/en/latest/).
- [BoTorch TuRBO-1 example](https://botorch.org/docs/tutorials/turbo_1). The benchmark follows the documented state/adaptive-region algorithm; it does not claim to be the upstream authors' source file.
- Eriksson et al., *Scalable Global Optimization via Local Bayesian Optimization* (TuRBO).
- Cowen-Rivers et al., *HEBO: Pushing the Limits of Sample-Efficient Hyperparameter Optimisation*.

[← Back to homepage](../README.md)


---

## How the evidence changed my decisions

Across the thirteen rounds I did not adopt one immutable optimiser. The [chronological journey](../journey/README.md) records when I trusted a GP forecast, tested a controlled local step or changed the representation entirely. Three checks mattered most:

### The three decision checks

**Prediction reliability — F2.** Pre-outcome forecast **0.730502**, returned **0.505526**. A single miss challenges this local forecast; it does not by itself establish a noise model.

**Search adequacy — F4.** Forecast error near **1.6 × 10⁻⁹**, while repeated microsteps left the best near **0.659**. Widening the local search returned **0.730459**. Accurate prediction and good query selection are different tests.

**Representation — F8.** A GP forecast could be accurate while an additive quadratic supplied a more complete mathematical explanation and identified a vertex of **10**. The original-40-only test was performed **retrospectively** and predicted the next 13 returned observations at numerical precision.

### Practical model-selection rule

1. Keep a simple baseline and a probabilistic model.
2. Record the proposed query, forecast and reason **before** the result.
3. Evaluate on points not used for fitting, preferably in chronological order.
4. When a simpler model consistently predicts better and survives a targeted structural check, consider promoting it to candidate selection.
5. Use any remaining evaluation budget in proportion to what a result could change.

The last step is especially important with a finite horizon: an exploratory query in R13 cannot provide knowledge for an R14 that does not exist.

### External evidence and provenance

Published external input-output records helped check some equations and influence later candidate regions. These records are **not** personal portal returns. Some later exploratory comparisons used small, adaptively collected holdouts and are **not** unbiased measures of deployment error.

[Provenance and attribution requirements](../DATASHEET.md) · [Round 10 research](../journey/round_10/README.md) · [Full model card](../MODEL_CARD.md) · [Final verified results](../journey/round_13/README.md)

## Reproduce the supported results

### Quick start

Requirements: Python, pip, a shell and access to the repository root. The package dependencies are pinned in [requirements.txt](../requirements.txt), except for the minimum pytest version.

```bash
python -m pip install -r requirements.txt
PYTHONPATH=src python -m bbo.structural_validation
PYTHONPATH=src python -m pytest -q
```

On Windows PowerShell, replace `PYTHONPATH=src <command>` with `$env:PYTHONPATH = 'src'` followed by the command.

### What the structural validation checks

| Check | Input | Expected conclusion |
|---|---|---|
| F8 full-rank fit | 40 initial course observations | 17 identifiable coefficients |
| F8 post-fit validation | 13 later personal portal returns, excluded from fit | Maximum absolute error under `2e-14` (test threshold) |
| F8 predicted vertex | Fitted quadratic | Centre approximately `(0.10,0.15,0.13,0.15,0.80,0.50,0.20,0.60)`, maximum approximately 10 |
| F5 permitted corner | Four inputs of `0.999999` | Approximately `8662.405001248297` |

The code is in [src/bbo/structural_validation.py](../src/bbo/structural_validation.py) and tests in [tests/test_structural_validation.py](../tests/test_structural_validation.py). The [F8 CSV](../data/accumulated/function_8/observations_through_week13.csv) labels initial versus later points. The model fits **only the initial 40**.

The test demonstrates a strong retrospective fit and held-out prediction for that equation family. It is not evidence that this model was used in Round 1.

### Other source material

The historical GP and acquisition pipeline is available in [src/bbo](../src/bbo/) with [python -m bbo.pipeline](../src/bbo/pipeline.py), [notebooks](../notebooks/) and [configs](../journey/round_10/optimisation.yaml).

```bash
PYTHONPATH=src python -m bbo.pipeline
```

**Scope:** the pipeline is a preserved older demonstration with a data cut through Week 9. It **does not** reproduce every Round 11–13 candidate-selection experiment and must not be presented as such. Some notebooks are short exploratory snapshots rather than polished end-to-end applications.

### Reading model outputs

Use the [279-row recorded dataset](../data/all_observations.csv) for measured scores. The [function pages](../functions/README.md) distinguish submitted portal inputs from model proposals, and the [round-by-round account](../journey/README.md#how-to-read-the-results) distinguishes prospective forecasts from later structural reconstructions. External participant observations used in exploratory comparisons are not counted as personal returns.

The Round 11 F7 input was `0.233000-0.128000-0.522000-0.276000-0.310000-0.667000`, returning `3.278967926227992`. This confirmed result belongs to the historical dataset, independently of which original selector script survives.

### Regenerate the visual gallery

From the repository root, with **Node.js 18+**, without installing further packages:

```bash
node results/figures/build_visual_gallery.mjs
```

This rebuilds the [16 SVG images](functions.md) and [manifest](../results/figures/gallery_manifest.json) from the available portal histories and the documented F5/F7/F8 equations. It checks these three formula evaluations against confirmed portal returns. F1/F2/F3/F4/F6 images contain **only observed points**, no fitted continuous surfaces. F7's Round 11 result is included in the measured-data charts.

The 3D pictures are static SVG projections, intended to render directly in GitHub. [Interpretation and limitations](functions.md).



The optional full HEBO / BoTorch TuRBO-1 simulation remains separate: [research/full_optimisers](../research/full_optimisers/README.md). Its synthetic F8 evaluations are not portal outcomes. [Final notebook](../notebooks/Capstone_Final_Walkthrough.ipynb) is the main reproducible walkthrough.
