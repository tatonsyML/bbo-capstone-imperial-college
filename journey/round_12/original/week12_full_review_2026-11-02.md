# Week 12 Black-Box Optimisation: Rebuilt Multi-Method Review

**Analysis date:** 2 November 2026. **Status:** recommendations only, not submitted. The repository was not modified.

## Critical chronology correction

Week 11 was submitted and has known outcomes. All candidate modelling in this review includes the user's Week 11 results. Prior work erroneously called Week 12 candidates Week 11; any conclusions ignoring Week 11 are superseded. Values labelled observed below were evaluated in the black-box system; values labelled predicted are output from offline surrogates.

## Final recommended Week 12 inputs

| Function | Point | Primary justification |
|---|---|---|
| F1 | `0.628540-0.628540` | High: already near upper peak |
| F2 | `0.684399-0.368552` | Moderate-low: model +0.0035 over reusing W11, smaller than observed noise |
| F3 | `0.313581-0.474345-0.485191` | Moderate: peer observed -0.00309987; model advantage tiny |
| F4 | `0.415000-0.417000-0.366500-0.413000` | High: hold 0.730459 observed; new extrapolated peaks unreliable |
| F5 | `0.999999-0.999999-0.999999-0.999999` | High: best permitted boundary |
| F6 | `0.415080-0.344119-0.644062-0.776818-0.076258` | Moderate-low: new ensemble difference ~0.0058, dependent on Nayeem |
| F7 | `0.201689-0.150011-0.476874-0.275332-0.311652-0.657301` | High: analytically verified Hartmann6 optimum |
| F8 | `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000` | High: analytically verified maximum 10 |

## Week 11 actual observed scores (not predictions)

| Function | Week 11 score |
|---|---:|
| F1 | 1.999999999676 |
| F2 | 0.695336827074 |
| F3 | -0.005709220276 |
| F4 | 0.730459421326 |
| F5 | 8662.405001248297 |
| F6 | -0.123761480163 |
| F7 | 3.278967926228 |
| F8 | 10.000000000000 |

## Algorithms examined

- Gaussian Process surrogates: RBF and Matérn, isotropic and ARD, alternative noise strengths, training-only standardisation.
- Output-warped GP using Yeo–Johnson; input- and output-warped GP with monotonic Kumaraswamy-type parameterisations and a linear-plus-Matérn covariance approximation. These test **HEBO mechanisms, not the complete official HEBO algorithm**. Multi-acquisition selection, EI and UCB were also studied.
- Local GP trust-region exploration with historical success/failure length updates and posterior Thompson sampling, plus robust acquisition within a local region. These test **TuRBO-1 mechanisms, not the complete official TuRBO algorithm**. A full online rollout cannot be established without new portal feedback.
- **Actual Optuna TPE** (independent and multivariate) proposals from historical observations. The TPE proposals were not evaluated in the black box, so no performance claims can be made for them.
- Unsupervised input PCA, RBF kernel PCA transformations with ridge regression, and input-space K-means clustering and isolation forest as diagnostics. Partial least squares and Bayesian ridge regression tested whether simpler low-dimensional predictors add value.
- Extra Trees, XGBoost, multilayer perceptron neural networks, and the previous cross-cohort GP committee.
- EI, GP-UCB, trust-region Thompson sampling, multicriterion mean/disagreement ranking and source-exclusion sensitivity.

**Limitations:** The official `hebo`, `botorch`, `gpytorch`, `turbo` packages were unavailable in this execution environment. HEBO/TuRBO are sequential optimisers, so offline one-step proposals cannot verify their relative regret. Model comparison is retrospective and variants are chosen on the same cohorts used to inform the strategy. The datasets contain repeated inputs and cohorts sharing initial data; identical coordinates were averaged before fitting. Predictions are not calibrated confidence intervals. Input-space PCA/clustering describes historical *sampling strategies* as well as possible structure of the hidden objective.

## Retrospective source-held-out comparison

Score: average high-output-region MAE across available external cohorts, differing by function; lower is better. These values are model-selection diagnostics, **not** prospective optimisation scores, and should not be compared across functions. Fixed parametric settings are preliminary, not an exhaustive tuning sweep.

| Function | Model | Average held-out high-region MAE |
|---|---|---:|
| F2 | Yeo–Johnson warped GP | 0.0591 |
| F2 | Extra Trees | 0.0646 |
| F2 | Matérn GP | 0.0650 |
| F2 | Kernel PCA + ridge | 0.0741 |
| F2 | Linear PCA + ridge | 0.1784 |
| F3 | Matérn GP | 0.0280 |
| F3 | ARD GP | 0.0288 |
| F3 | Extra Trees | 0.0302 |
| F3 | Kernel PCA + ridge | 0.0415 |
| F3 | Linear PCA + ridge | 0.0469 |
| F4 | Kernel PCA + ridge | 0.1965 |
| F4 | Warped GP | 0.2789 |
| F6 | Kernel PCA + ridge | 0.0671 |
| F6 | RBF GP | 0.0681 |
| F6 | ARD GP | 0.0760 |
| F6 | Linear PCA + ridge | 0.2738 |

F4 validation is particularly unreliable because of uneven historical sampling and high model disagreement. Its apparently high kernel-PCA predictions at novel points were not corroborated across models or observed in the oracle. Repeating our observed F4 result is the risk-controlled choice.

## Effect of PCA and unsupervised learning

PCA on sampled *inputs* does not denoise stochastic black-box outputs and can remove coordinates that determine the objective. Historical sampling creates biased input correlations. The first two input PCs for F3 explain about 71.4% of sampled-input variance, not objective information. The first three PCs for F6 explain about 81.2%, leaving important unexplained directions. Standard PCA plus ridge underperformed full-dimensional GP.

RBF kernel PCA + ridge worked comparatively well for F6 (held-out MAE 0.0671 versus 0.0681 for the nearest GP); however, with eight kernel components for five original coordinates, this is **nonlinear feature expansion**, not dimensionality reduction. It does not demonstrate a superiority likely to persist prospectively. For F4 it sometimes predicted maxima unsupported by other methods, so extrapolation was rejected.

K-means on top-quartile observed F2 points split into two regions near (0.701,0.354) and (0.705,0.875), suggesting two well-sampled promising ridges. This is evidence of sampled high outcomes, not evidence of two true local maxima. F4 top-quartile points also split into two sampled regions; the highest actual Week 11 result remains the safer incumbent. Isolation Forest flags atypical input locations, not high objective value; it should not drive maximisation on its own.

## Candidate-level comparison

**F2:** The old Week 12 candidate `[0.696286, 0.488640]` receives committee mean about **0.59595**, versus **0.62597** for new `[0.684399, 0.368552]` and **0.62243** for the observed Week 11 location `[0.692000, 0.366000]`. The predicted +0.00354 versus repeating Week 11 is far smaller than noise/model error and is not a guaranteed improvement. Robust removal of peer cohorts keeps the new ridge competitive; TPE and exploratory GP acquisition did not establish a reliably superior alternative.

**F3:** Earlier Week 12 `[0.489838, 0.498896, 0.486446]` committee mean approximately **-0.01585**; independently peer-observed `[0.313581, 0.474345, 0.485191]` has actual **-0.00309987** and committee mean **-0.01013**; Week 11 has actual **-0.00570922** with committee mean **-0.01149**. One trust-region alternative `[0.331989, 0.413022, 0.437884]` reached committee **-0.00621**, but out-of-sample/source-exclusion sensitivity and physically unsupported positive GP extrapolations undermine it. Use the peer-evaluated point; not a promise of improvement.

**F4:** Actual Week 11 **0.730459** exceeds all checked peer observations, including Vugar's **0.681621**. Proposed Week 12 `[0.418700, 0.415988, 0.363637, 0.413858]` has no strong evidence of improvement. Kernel-PCA expansion and naive local polynomial extrapolation produced overconfident maxima not supported by held-out evidence. **Repeat the observed Week 11 point**.

**F6:** Old proposed `[0.401093, 0.323286, 0.666764, 0.777577, 0.090679]` committee mean **-0.16622**, spread **0.07001**. Updated `[0.415080, 0.344119, 0.644062, 0.776818, 0.076258]` mean **-0.16041**, spread **0.05771**. This modest predicted advantage is not robust to all individual model families and is materially influenced by Nayeem's strong observed record **-0.04163238**. Omitting Nayeem degrades both candidates; the updated candidate is somewhat less sensitive. This is a cautiously preferred experiment, not verified improvement.

**F1, F5, F7, F8:** Hold F1 near its observed 2.0 and F5 at the highest permitted all-coordinate boundary. F7 can be identified with the *positive* Hartmann-6 benchmark; recommended point evaluates to about **3.32236801** analytically. F8's exact additive quadratic reaches **10.0** at the retained coordinates.

## Why more modelling does not establish optimality

An unlimited collection of algorithms is not a substitute for new evaluations. Additional offline fitting on the same small, adaptively sampled datasets risks overfitting the model-selection process itself. F2/F3/F6 suggestions differ by much less than the error measured against held-out peer cohorts. Full HEBO/TuRBO require appropriate package availability and a sequence of new objective responses. After Week 12 outputs, update models, compare predictions with actual outcomes, and reassess the Week 13 strategy.

## Data provenance

- Own weekly observations (through Week 10) plus the **actual Week 11 portal results** supplied in this conversation: https://github.com/tatonsyML/bbo-capstone-imperial-college
- Eduardo (Wizen Labs): https://github.com/Wizen-Labs/you-sank-my-function-bbo-challenge
- Vugar: https://github.com/vugarnv/Capstone
- Nayeem: https://github.com/Nayeem-MH/Capstone-Project
- 100HIVES: https://github.com/100HIVES/Imperial-AI-ML-Capstone
- Carmen (published maxima): https://github.com/carmen-timpau/BBO-Capstone-Project
- HEBO paper: https://mlanthology.org/jair/2022/cowenrivers2022jair-hebo/

The F4 exploration uses a transcribed/rounded subset of confirmed peer data and the own initial + weekly records, so its quantitative holdout results should not be interpreted as exhaustive full-dataset validation. The rest use the verified input transcripts in the included archive plus W11. The user GitHub repository remains read-only.
