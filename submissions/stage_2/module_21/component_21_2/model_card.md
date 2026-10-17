# Model Card: Evidence-Gated Function-Specific Black-Box Optimisation

**Version:** Module 21 / pre-Round 10  
**Status:** Experimental educational optimisation framework  
**Author:** Tamer El-Tonsy  
**Observed performance cut:** Portal results through Week 9; Round 10 candidate set is prospective

## 1. Overview

This project is not a single fixed surrogate model. It is a sequential decision framework for eight independent black-box optimisation problems with 2–8 continuous inputs.

The approach began with Gaussian-process Bayesian optimisation and evolved into a function-specific evidence gate. Candidate points can be proposed by GP surrogates, alternative kernels, local quadratic fits, controlled one-coordinate experiments, model committees and, for Round 10, HEBO-inspired and TuRBO-style challengers. A human decision layer determines whether a model has earned enough authority to influence the expensive portal query.

The governing rule is simple: **a more sophisticated model does not automatically outrank stronger direct evidence.**

## Version history

| Version | Project stage | Main change |
|---|---|---|
| v1 | Early rounds | GP-led Bayesian optimisation and uncertainty-aware acquisition |
| v2 | Middle rounds | Function-specific models, diagnostics and controlled local experiments |
| v3 | Weeks 7–9 | Cross-validation, rolling/prospective forecasts and explicit reduction of model authority after failure |
| v4 | Round 10 preparation | Evidence-gated optimisation with HEBO/TuRBO challengers, structural models and decision-value tests |

The current code is reproducible from the repository snapshot. The complete historical decision process is reproducible only to the extent that its original settings, forecasts and judgement calls were preserved.

## 2. Intended use and audience

### Suitable for

- expensive continuous black-box optimisation on bounded domains;
- low-to-moderate dimensions with only tens of observations;
- sequential settings in which uncertainty, information value and opportunity cost matter;
- research or educational workflows where a human reviews the final recommendation.

### Not recommended for

- safety-critical autonomous deployment without domain constraints and independent validation;
- high-dimensional problems where the available observations are too sparse to support the chosen surrogate;
- discrete or categorical spaces unless those variables are explicitly encoded with a suitable model;
- strongly discontinuous or time-varying systems without methods designed for those behaviours;
- claims of guaranteed global optimality.

The main audience is assessors, ML practitioners, future maintainers of the repository and readers who want to understand not only what point was chosen, but why.

## 3. How the approach decides

The final decision process separates four evidence classes:

1. **Observed evidence:** portal-returned input/output history.
2. **Prospective evidence:** forecasts and rationale recorded before the next result arrives.
3. **Retrospective evidence:** later re-analysis using alternative models, without rewriting the original decision.
4. **Interpretation:** what changed after the new observation was seen.

A candidate is judged on more than its predicted mean. Depending on the function, the decision may consider forecast calibration, predictive uncertainty, expected improvement, model/acquisition agreement, distance from the incumbent, information value and what a failure would teach.

This makes the optimisation decision more interpretable without pretending that the hidden mathematical function itself has been explained.

## 4. Strategy evolution across the ten query decisions

| Stage | Main techniques | What changed |
|---|---|---|
| Weeks 1–2 | GP surrogate, EI/UCB, broad exploration | Established the BO workflow and uncertainty-aware search |
| Weeks 3–4 | History-aware regional search, alternative kernels, SVM/NN diagnostics | Began treating functions differently rather than using one universal policy |
| Weeks 5–6 | Controlled local experiments and quadratic peak fitting | Reduced confounding by changing one variable where practical |
| Week 7 | Cross-validation, rolling-origin prediction and kernel comparison | Shifted attention from in-sample fit to next-result prediction |
| Week 8 | Pre-result forecasts, micro-steps, model committees | A model lost authority when direct local evidence contradicted it |
| Week 9 | Scaling/forecast audit and function-specific risk allocation | Quantified where extra modelling paid for itself and where it did not |
| Round 10 preparation | HEBO-inspired acquisition/warping challengers, TuRBO-style trust-region logic, global restarts and structural recovery | Advanced methods became challengers, not automatic replacements for validated evidence |

The approach therefore evolved from **model-led Bayesian optimisation** towards **evidence-gated sequential experimentation**.

## 5. Performance

### Metrics

The primary metric is the maximum observed portal output for each function. Supporting metrics include:

- number of post-initial rounds that established a new best;
- prospective forecast error where a numerical forecast was recorded before the result;
- rolling/cross-validated surrogate error;
- uncertainty calibration and model disagreement where available;
- qualitative decision value when a diagnostic query rules out a hypothesis.

Relative percentage improvement is not used as a universal metric because some functions start near zero or with negative values, where percentages can be misleading.

### Best observed results through Week 9

| Function | Initial best | Best observed through W9 | New-best rounds / 9 | Current interpretation |
|---|---:|---:|---:|---|
| F1 | 7.7109e-16 | 1.9213e-15 | 2 | Extreme scale; incumbent basin still offers little absolute signal |
| F2 | 0.611205 | 0.691315 | 3 | Strong but very narrow incumbent; smooth local forecasts have failed |
| F3 | -0.034835 | -0.020856 | 2 | Improved, then stalled; alternative basin now worth testing |
| F4 | -4.025542 | 0.658933 | 5 | Strong local trajectory; recent prospective forecast was exceptionally accurate |
| F5 | 1088.8596 | 6583.5614 | 9 | Every completed round improved the incumbent; upper-bound trajectory is still accelerating |
| F6 | -0.714265 | -0.541448 | 3 | Best set in Week 4; incumbent neighbourhood remains unstable |
| F7 | 1.364968 | 1.786338 | 6 | Consistent local gains, now approaching a fitted local vertex |
| F8 | 9.598482 | 9.932443 | 8 | Strong progression; observed history supports a simple structural model |

### Prospective Week 9 audit

The forecast audit is part of model performance, not an appendix to it. Week 9 gave sharply different outcomes:

| Function | Pre-result forecast | Actual | Absolute error | Interpretation |
|---|---:|---:|---:|---|
| F2 | 0.730502 | 0.505526 | 0.224977 | Local smooth forecast failed; model authority reduced |
| F3 | -0.020112 | -0.025816 | 0.005704 | Direction plausible, magnitude not reliable enough |
| F4 | 0.658932869 | 0.658932867 | 1.56e-9 | Direct local model strongly validated |
| F5 | 6454.0 | 6583.561 | 129.561 | Direction correct; gain was underestimated |
| F7 | 1.786415 | 1.786338 | 7.69e-5 | Local quadratic strongly supported |
| F8 | 9.933511 | 9.932443 | 0.001068 | Direction and scale well supported |

F1 and F6 deliberately had no trustworthy numerical Week 9 forecast. Not issuing a number where the evidence did not support one is treated as a transparency feature rather than a missing metric.

## 6. Function-specific Round 10 rationale

The prospective Round 10 strategy is deliberately heterogeneous. F1, F3 and F6 use higher-risk restarts because their incumbent regions do not offer enough competitive upside. F2 uses a tighter local diagnostic bracket. F4 expands a validated local step. F5 moves to the all-upper-bound candidate. F7 refines its fitted local vertex. F8 tests the maximiser of an additive quadratic that fits all 49 observed values to numerical precision.

The exact F1, F3 and F6 challenger coordinates in the current configuration remain provisional and should be rerun before portal submission. All Round 10 candidates remain prospective until the portal returns results.

## 7. Assumptions

### Local continuity

GPs, local quadratics and trust regions all assume, in different ways, that nearby observations provide useful information about nearby candidates. F1, F2 and F6 show how fragile this can become when useful behaviour is extremely narrow or locally unstable.

### Stability of the data-generating process

The approach assumes that an observation remains relevant to later decisions. The project does not have enough replicate measurements to establish the noise process or determinism of every function independently.

### Surrogate uncertainty is only useful when calibrated

A GP standard deviation is model uncertainty under the fitted assumptions, not a guarantee about the hidden function. Forecast misses therefore reduce the authority given to acquisition functions that depend on that uncertainty.

### Structural assumptions are local claims unless tested globally

The strongest example is F8. An additive quadratic with 17 coefficients fits all 49 observed values with a maximum residual around 1.8e-14 and implies a candidate with predicted value 10. This is unusually strong evidence, but the unobserved domain remains unobserved until the portal tests the candidate.

## 8. Limitations and failure modes

### Adaptive sampling bias

The model helps choose the data and then uses those data as evidence for itself. Dense local success can therefore make the model increasingly confident in a region it repeatedly chose to inspect while leaving alternative regions poorly characterised.

### Missing counterfactual outcomes

Retrospective HEBO, TuRBO or other challengers can be replayed without leakage, but an unsubmitted historical candidate has no true portal result. Counterfactual optimisation performance must not be invented.

### Sparse high-dimensional evidence

The 6D and 8D functions contain only 39 and 49 observed points respectively. Good local performance does not establish global coverage.

### Human and LLM confirmation bias

The project uses human judgement and LLM assistance for coding, hypothesis generation and critique. Once a narrative becomes attractive, later evidence can be interpreted through it. The controls are pre-result forecasts, preserved failures, explicit overrides and keeping retrospective analysis separate from the historical decision.

### Computational and methodological scope

Exact GP fitting is practical at the current sample sizes, but more complex model portfolios cost time and can create false confidence. Complexity is retained only when it improves validation, calibration or decision value.

### Delayed feedback

Each expensive result arrives after the query decision. A surprising observation cannot be followed immediately with a second query, increasing the opportunity cost of a poor choice.

## 9. Ethical considerations, transparency and interpretability

No personal data is used, so privacy and demographic fairness are not the primary ethical risks. The relevant risks are overclaiming, unearned confidence and unsafe transfer of a method outside the setting in which it was tested.

Transparency is therefore treated as part of model quality. Negative results, forecast failures, manual overrides and changes of mind are retained because they explain how the final method was reached. The raw observations are preserved, and prospective claims are kept separate from retrospective interpretation.

Interpretability in this project means a reviewer can understand why a query was chosen and what evidence would change that decision. It does **not** mean that the optimiser has recovered the causal mechanism of the hidden function.

For real-world adaptation, a good score on these synthetic functions would not justify direct deployment. The data-generating process, measurement system, constraints, costs and failure consequences would need to be re-established in the target environment. A model that works under one collection process should not be assumed portable to another.

## 10. Is this level of detail sufficient?

Yes for the capstone model card. The card contains the decision logic, evidence cut, performance, assumptions, failure modes and appropriate-use boundaries needed to judge the approach. More detailed kernel fits, candidate scores and per-round diagnostics belong in linked notebooks and audit tables rather than in the card itself.

That separation is deliberate: transparency requires enough detail to verify a claim, while interpretability also requires cognitive tractability. A document that contains every intermediate number can become less useful rather than more transparent.

## 11. Reproducibility checklist

A reviewer should be able to reconstruct the public working analysis from the chronological CSV history, exact code revision, Python/package versions, random seeds, model and acquisition settings, transformations, candidate-search bounds, six-decimal portal rounding, prospective forecast records and the decision log documenting manual overrides. Full byte-for-byte reproduction of the original programme seed files additionally requires those files to be available under the programme's permitted terms.

Bitwise reproduction is not the same as decision reproduction. Where numerical optimisation is stochastic or library-dependent, the repository should preserve the environment and seed and state an acceptable tolerance; where judgement selected between candidates, the rationale must be recorded as data about the decision process.
