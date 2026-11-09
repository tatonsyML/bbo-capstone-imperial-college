# Strategy, validation and experimental decisions

The objective was to maximise eight unknown functions within a strict **one-query-per-function-per-round** budget. Each evaluation had a cost, and the model did not have access to gradients or hidden equations.

## How the approach evolved

| Period | Working approach | Decision lesson |
|---|---|---|
| R1–R3 | Inspect course data; GP, UCB, EI and broad/local candidate searches | Build reproducible baselines and differentiate functions |
| R4–R6 | Controlled coordinate probes; small neural-network and polynomial challengers | Check models against observed local changes |
| R7–R9 | ARD RBF/Matérn GP fits, rolling-origin forecasts and acquisition audits | A credible local forecast does not imply a good search |
| R10 | HEBO-inspired committees, TuRBO-style regional candidates and externally informed supplemental comparisons | Test model disagreement, boundaries and alternative regions |
| R11 | Mathematical reconstruction for F1; wider F4 search and other refinements | Change representation or search region when progress stalls |
| R12 | Hartmann-6 structural F7 forecast, F6 refinement and four confirmation repeats | Separate useful evidence gathering from redundant evaluations |
| R13 | Final returned queries, with F2/F3/F4 new personal bests | A plateau is not proof of convergence; keep pre-result hypotheses distinct from observed returns |

## The three decision checks

**Prediction reliability — F2.** Pre-outcome forecast **0.730502**, returned **0.505526**. A single miss challenges this local forecast; it does not by itself establish a noise model.

**Search adequacy — F4.** Forecast error near **1.6 × 10⁻⁹**, while repeated microsteps left the best near **0.659**. Widening the local search returned **0.730459**. Accurate prediction and good query selection are different tests.

**Representation — F8.** A GP forecast could be accurate while an additive quadratic supplied a more complete mathematical explanation and identified a vertex of **10**. The original-40-only test was performed **retrospectively** and predicted the next 12 observations at numerical precision.

## Final-round findings

**F2 = 0.744250**, **F3 = −0.003753**, and **F4 = 0.746898** were new R13 personal bests. F6 scored below its prior best, F1/F5/F8 repeated exact results, and F7 changed by only around 4.38 × 10⁻¹³ at a nearly identical input. These are post-result observations, not evidence of any forecast that was not recorded in advance. [Read the final audit](round13_evidence.md).

## Which methods were actually evaluated?

| Method | Status | What is supported |
|---|---|---|
| GPs with RBF / Matérn ARD kernels | Implemented | Surrogate predictions and comparisons on the retained historical cuts |
| EI / UCB / local searches | Implemented | Candidate generation and dated returned evaluations |
| Small neural networks / regressions | Challengers | Per-function comparisons, not universal superiority |
| HEBO-inspired kernel/transform/acquisition committee | Partial adaptation | Selected mechanisms and [comparison report](../reports/hebo_inspired_committee.csv); **not official HEBO** |
| TuRBO-style trust regions | Partial adaptation | Selected candidate mechanisms and [comparison report](../reports/turbo_style_challengers.csv); **not official TuRBO** |
| F8 additive quadratic | Independently testable | Fit only initial 40; validate on 13 later returns |
| F5 power-sum equation | Independently checkable at corner | Reconstructed after the successful boundary query |
| F1 / F7 structural explanations | Documented historical analysis | Numerically supported; historical research scripts are not fully captured in this project |

## Practical model-selection rule

1. Keep a simple baseline and a probabilistic model.
2. Record the proposed query, forecast and reason **before** the result.
3. Evaluate on points not used for fitting, preferably in chronological order.
4. When a simpler model consistently predicts better and survives a targeted structural check, consider promoting it to candidate selection.
5. Use any remaining evaluation budget in proportion to what a result could change.

The last step is especially important with a finite horizon: an exploratory query in R13 cannot provide knowledge for an R14 that does not exist.

## External evidence and provenance

Published external input-output records helped check some equations and influence later candidate regions. These records are **not** personal portal returns. Some later exploratory comparisons used small, adaptively collected holdouts and are **not** unbiased measures of deployment error.

[Provenance and attribution requirements](evidence_provenance.md) · [Dated audit](../reports/round10_revision_audit.md) · [Full model card](model_card.md) · [Final verified results](round13_evidence.md)

## Reproducible code and subsequent research

The [annotated algorithms guide](optimisation_algorithms.md) explains how the original GP, EI/PI/UCB, HEBO-inspired committee and TuRBO-style local search were implemented, and why they differ from the complete reference algorithms.

After the capstone, a separately labelled [official HEBO / BoTorch TuRBO-1 benchmark](../benchmarks/full_optimisers/README.md) was developed. It offers a **controlled F8 quadratic-model simulation** and **unscored** one-step proposals for all eight functions. The optional full algorithms have **not been executed in this runtime**. No new real portal outcomes or full-algorithm performance comparisons are claimed.
