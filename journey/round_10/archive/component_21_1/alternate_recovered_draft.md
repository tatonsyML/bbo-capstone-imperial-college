# Stage 2: Required Capstone Component 21.1

## 1. Reasoning behind Round 10

By Round 10, I had stopped treating the eight functions as variations of the same problem. I used the complete history through Week 9, forecasts recorded before their results, local geometry and competing model recommendations. HEBO-inspired output warping and acquisition comparison, and TuRBO-style trust-region logic, were used as challengers rather than automatically replacing stronger observed evidence.

F1 leaves the current basin for a global restart near (0.4728, 0.4557): repeated refinement around 0.73 still produced only microscopic values. F2 takes the opposite approach. Week 9 rejected my wider quadratic forecast, so I use a much tighter bracket at x2≈0.959796 around the best observed region. F3 also restarts because repeated local refinement has stalled.

F4 has unusually strong local evidence. Four comparable x1 micro-steps followed an almost exact line, and my Week 9 forecast missed the portal result by only about 1.6x10-9. I therefore expand the successful step rather than add model complexity. F5 moves all four inputs to 0.999999 because its controlled boundary trajectory is still accelerating. F6 leaves a stalled and unstable incumbent region for a multi-model restart.

F7 remains a precision problem; its latest controlled observations place the local quadratic vertex near x1=0.223588. F8 produced the strongest structural result: an additive quadratic with 17 coefficients fits all 49 observed values to numerical precision, with maximum residual around 1.8x10-14, implying (0.10,0.15,0.13,0.15,0.80,0.50,0.20,0.60) with predicted value 10. I treat this as a strong hypothesis, not proof, until the portal tests it.

## 2. Transparency and reproducibility

A rerunnable model is not the same as a reproducible decision.

Another researcher would need the original .npy data, chronological query/output log, code and package versions, random seeds, transformations, kernels, acquisition settings, search bounds, candidate-generation rules and six-decimal rounding. They would also need the decision register showing which candidates were accepted, rejected or manually overridden. A best-so-far curve alone would hide much of that reasoning.

I now separate four evidence classes: observed portal results, forecasts recorded before results, retrospective challenger analyses and later interpretation. My datasheet records provenance, dimensions, adaptive sampling and coverage gaps; the model card records assumptions, validation, intended use and known failure modes. Earlier rounds did not retain every rejected candidate, which remains a transparency gap.

## 3. Assumptions

The main assumption is local continuity: nearby observations remain informative about nearby candidates. GPs express this through covariance and smoothness; local quadratics and trust regions make a similar assumption more explicitly.

F1, F2 and F6 show where this becomes fragile. I also assume the observed relationship is sufficiently stable across rounds; if noise varies by location, or the relationship is less stable than assumed, nearby observations become harder to interpret.

F8 makes the stronger assumption that the additive quadratic structure identified on observed points continues into unsampled space. Exact agreement is powerful evidence, but extrapolation remains an assumption.

## 4. Data gaps and potential bias

The data are adaptively collected, not representative. After nine rounds the functions contain 19, 19, 24, 39, 29, 29, 39 and 49 observations respectively, yet successful regions receive disproportionate attention.

This creates adaptive sampling bias: the model helps choose the data, then uses those data as evidence for itself. F4 and F7 are now highly localised, while F5 is concentrated near one boundary. Large competing regions therefore remain weakly represented, especially in higher dimensions.

There is also analyst and LLM confirmation bias: once a promising explanation exists, later observations are easier to interpret through it. Recording forecasts before results and retaining failed hypotheses are my safeguards against that.

## 5. Significant limitation

The largest limitation is the small evaluation budget combined with adaptive sampling. There are too few observations, and they are too concentrated by earlier optimisation decisions, to test every plausible region or modelling assumption.

This also creates missing counterfactual evidence. If retrospective HEBO, TuRBO or another challenger would have selected a different historical point, its true portal value is unknowable because it was never queried. Retrospective analysis can compare calibration, assumptions and recommendations; it cannot prove that the alternative would have scored better.

I therefore keep observed performance separate from counterfactual claims. With few evaluations remaining, each query must either improve the incumbent or resolve an uncertainty that changes the next decision.
