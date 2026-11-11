# Methods and experiments

[← Project overview](../README.md) · [Eight function stories](../functions/README.md) · [Thirteen-round history](../journey/README.md)

The capstone was a **human-reviewed, function-specific optimisation process**, not a single algorithm repeatedly run without intervention. This guide tells readers where to find the implementations and which claims the surviving evidence supports.

## Historical techniques

| Approach | Purpose | Evidence and code |
|---|---|---|
| Gaussian Processes: RBF, Matérn and ARD | Model response and uncertainty from sparse observations | [Recovered original R12 comparison](../journey/round_12/original/review_round12.py) · [Reusable surrogate implementation](../src/bbo/surrogates.py) · [Explanation](../docs/methods.md) |
| EI, PI, UCB | Rank candidates by improvement and exploration | [Acquisition functions](../src/bbo/acquisition.py) |
| Sobol and local candidate search | Generate feasible global and regional candidates | [Search utilities](../src/bbo/search.py) |
| Neural networks, MLP and SVM diagnostics | Challenge local GP modelling and investigate input sensitivity | [Round 4](../journey/round_04/README.md) · [Round 6](../journey/round_06/README.md) |
| Controlled coordinate probes | Test local sensitivities and boundary effects | [Round 5](../journey/round_05/README.md) · [F5](../functions/F5/README.md) |
| **Optuna TPE and regularised local quadratics** | Independent/multivariate TPE candidate searches and F4 local curvature tests | [Recovered original R12 TPE script](../journey/round_12/original/tpe_local.py) |
| **PCA, kernel PCA and heterogeneous surrogate comparison** | Test dimensionality and compare GPs with Extra Trees, MLP, PLS and Bayesian Ridge | [Recovered original Round 12 review](../journey/round_12/original/review_round12.py) |
| HEBO-inspired committee | Cross-validated model ranking, robust ensemble scoring, EI/UCB and experimental input/output warping | [Recovered Round 12 committee](../journey/round_12/original/review_round12.py) · [Warping/robustness](../journey/round_12/original/robust_and_warp.py) · [Later reusable adaptation](../src/bbo/optimizer.py) |
| TuRBO-style local search | Use historical success/failure trust-region updates and GP Thompson proposals; not full official TuRBO | [Original Round 12 experiment](../journey/round_12/original/trust_region_ts.py) · [Later reusable adaptation](../src/bbo/optimizer.py) |
| Mathematical reconstruction | Test equations explaining the observed functions | [Reconstruction index](../reconstruction/README.md) |

**Terminology matters.** The historical HEBO-inspired committee is not official HEBO. The historical TuRBO-style candidate routine is not a complete TuRBO implementation. [See the comparison and distinctions](../docs/methods.md).

## Full reference optimisers, after the capstone

The later [full-optimiser comparison](../research/full_optimisers/README.md) contains the official HEBO library and a BoTorch/GPyTorch TuRBO-1 implementation, evaluated on a **retrospectively fitted F8 simulator**, not the private portal. It was created after the thirteen rounds and is **not** evidence of original submissions.

## Additional historical methods awaiting source verification

The working research discussion also mentions **Ava** and **PDA**. Their precise names, versions, scripts and timing have **not** been established in the repository evidence reviewed for this index. They are recorded here as **unverified inventory items**, not presented as validated historical implementations. When matching original files are recovered, they should be linked to the appropriate round and function, with dates and outcomes.

## Find original code without duplicates

Use the [round archive](../journey/README.md) for original weekly files, submissions, forecasts and returns. Code linked from a function page points to that same archive; it is not a separate rewritten copy. Some historical candidate-generation scripts were not retained, which is explicitly disclosed.

[Source modules](../src/bbo/README.md) · [Executable final walkthrough](../final/README.md) · [Model card](../MODEL_CARD.md)
