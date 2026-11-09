# Optimisation algorithms: source code, rationale and honest comparisons

[← Main README](../README.md) · [How to run the benchmark](../research/full_optimisers/README.md) · [Original model-card](model_card.md) · [Round 13 verified results](round13_evidence.md)

## What was implemented and when?

**The capstone and the later benchmark are deliberately separate.** During the 13-round challenge I used Gaussian-process surrogate models, acquisition functions, controlled probes, structural investigations and *HEBO-inspired* / *TuRBO-style* challenger mechanisms. The **full official-HEBO / BoTorch TuRBO-1 comparison code was added after the challenge**. It was not used to pick historical portal inputs. This distinction matters for an instructor reviewing methodological evidence.

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

## The logic behind the code

### 1. GP modelling

Each function has only a small number of observations relative to its dimension. `fit_gp` therefore uses a Gaussian Process to estimate both the response and its uncertainty. We compare RBF with Matérn 1.5 and 2.5 kernels because their smoothness assumptions differ. Automatic Relevance Determination (ARD) assigns one lengthscale to each input. A separate WhiteKernel permits observational noise, but does not prove the hidden function is noisy.

**Why output transformation?** F1's responses can be almost zero and F5's vary by thousands. Yeo–Johnson handles both positive and negative values, improving numerical scaling in some cases. `inverse_mean` reverses that transformation for readability; it is not an exact posterior expectation under a nonlinear transform.

### 2. Choosing one query

EI combines predicted improvement with uncertainty. PI considers the probability of beating an incumbent. UCB gives additional value to uncertainty. Their numerical units differ, so the custom committee **ranks** candidates within each acquisition function instead of directly adding raw acquisition values. The original course permitted only one query per function per round, making it important to audit the choice.

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

**Interpretation:** this tests methods on a **retrospectively fitted model** of F8, not their historical portal performance. Recovering F8 structure from the initial 40 is independently reproducible, but that does not authenticate the undisclosed source formula everywhere.

### Experiment B: eight one-step, unscored proposals

Read the same **through-Week-9** historical observation snapshot for each function, and ask each algorithm for one counterfactual candidate. These are not scored, because the capstone portal has not returned outputs at those new points. The comparison can report input feasibility and nearest-known-point distance. **Do not claim a method beat another method on F1–F7 from unobserved proposals.**

## What this code does *not* establish

- That complete HEBO or TuRBO was used in any of the user's real submitted rounds.
- That simulated F8 objective returns are real portal scores.
- That a single best candidate would dominate on eight different unknown functions.
- That a candidate chosen using the final history was actually available before its original submission date.
- That the optional HEBO and BoTorch engines have been executed here: **their packages are not available during the code review**, so no numeric algorithm-versus-algorithm verdict is recorded.

## Instructor's code-reading route

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
