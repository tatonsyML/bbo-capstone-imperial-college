# Model Card | Black-Box Optimisation Methods

*Imperial College London · Professional Certificate in Machine Learning and Artificial Intelligence*

This model card describes my function-specific optimisation workflow across **eight black-box objectives and thirteen returned rounds**, completed in November 2026. It covers what the models accept and predict, how candidate decisions were made, performance against actual portal outcomes, limitations and trade-offs. The later [HEBO/TuRBO-1 simulator benchmark](research/full_optimisers/README.md) is independent post-capstone research, not an additional set of original portal evaluations.

[← Project home](README.md) · [Executable Jupyter notebook](notebooks/Capstone_Final_Walkthrough.ipynb) · [Dataset datasheet and function-specific data notes](DATASHEET.md)

## 1. Model summary

**Inputs:** One function identifier (F1–F8) and a continuous candidate vector of **2–8 coordinates** in the legal range `[0, 0.999999]`. Surrogate fitting uses only historical input/output observations available at the particular decision point, not later portal returns.

**Outputs:** A Gaussian Process produces a **predicted score (mean) and uncertainty estimate** for candidate inputs. Acquisition functions produce a ranking or next-query proposal; the external portal separately returns the **measured scalar objective score**. Predictions are not measured results.

**Model architecture:** This is not a single neural network or an unchanged automated optimiser. The baseline comprises **function-specific Gaussian Process surrogates** with RBF/Matérn kernels and automatic relevance determination (ARD) lengthscales. Expected Improvement (EI), Probability of Improvement (PI) and Upper Confidence Bound (UCB) balance predicted reward against uncertainty. Controlled coordinate experiments, alternative models and later mathematical reconstructions were also assessed.

The goal was to maximise the unknown functions within one paid portal evaluation per function per round. There was no access to their underlying source equations or gradients.

**This is not one fully automated policy used unchanged for 13 rounds.** The human-reviewed, function-specific decision process is itself a feature of the project.

## 2. Intended use and out-of-scope use

**Intended:** educational sequential optimisation on sparse, relatively expensive numeric evaluations; explaining how evidence changes a query decision; evaluating model fit and candidate-search limits.

**Not intended:** production risk-critical autonomous control, certified global optimisation, inference of the hidden source code, generalisation to unseen functions without validation, or claiming that the later benchmark implementations generated historical portal submissions.

## 3. Strategy, decisions and rationale

1. **Initial GP baseline:** fit only the observations available at decision time, predict candidate mean and uncertainty, and rank exploration–exploitation proposals.
2. **Model challenge:** compare RBF with Matérn 1.5/2.5 and alternative transforms, watching real forecast errors rather than trusting training fit.
3. **Controlled experiments:** vary promising coordinates or broaden a stagnant local region when a GP becomes overconfident.
4. **Structure test:** try a simple explanatory equation when the numerical evidence justifies it. Record whether its prediction was made before the portal response or reconstructed afterwards.
5. **Budget-aware selection:** one query per function per round requires a clear improvement or information rationale; repeats consume the same limited evaluations.

The historically implemented **HEBO-inspired** committee and **TuRBO-style** trust region are adaptations, not complete official HEBO or TuRBO. Full reference-algorithm code was added *after* the capstone and is separated in [benchmarks](research/full_optimisers/README.md).

## 4. Development timeline: Rounds 1–13

This table separates the strategy I was considering from the **results the portal actually returned**. Historical notes contain fewer details for the early rounds, so I have not invented a complete decision log.

| Rounds | Main emphasis | What changed in my understanding |
|---|---|---|
| **1–4** | Gaussian Processes, UCB/EI proposals and initial exploration | A shared acquisition policy did not perform equally across functions; some responses were extremely small, while F5 showed strong scale and boundary effects |
| **5–7** | Controlled local probes, alternative kernel fits and model checks | A good local fit was useful but did not ensure a good next query; F2 and F7 benefited from more targeted investigation |
| **8–9** | Forecast auditing, ARD GP comparisons and experiment selection | F4's local forecast was accurate to around 1.6 × 10⁻⁹ while F2's missed by 0.224977, showing that prediction reliability differed by function |
| **10** | Structural investigations and targeted exploitation | F5 reached 8662.405 at the legal boundary; F8 reached 10. The explicit F5 formula and initial-40-only F8 fit were reconstructed retrospectively |
| **11** | Challenging overly narrow refinements and exploring better regions | F1 reached almost 2 and F4 rose to 0.730459; F2/F3 also improved |
| **12** | Structural forecast checks and further local tests | F6 reached −0.037519; F7's pre-result Hartmann-6 prediction closely matched 3.322368 |
| **13** | Final exploitation and selected alternative regions | F2, F3 and F4 reached new personal bests. F1/F5/F8 repeated earlier scores, F7 remained numerically equivalent and F6 did not improve |

The [round-by-round archive](journey/README.md) and [project journey](archive/notes/early_project_timeline.md) distinguish recorded returns from retrospective interpretation.

## 5. Trade-offs and decisions

| Choice | Benefit | Cost or risk | My response |
|---|---|---|---|
| **Exploration versus exploitation** | Exploring finds regions outside the current best; exploitation refines a promising point | Too much exploration spends scarce queries; too much exploitation causes early stagnation | I moved towards function-specific choices, especially after the F2 forecast miss and F4 local plateau |
| **GP versus simpler structural models** | A GP provides a flexible prediction and uncertainty; a simpler equation is easier to audit | GP uncertainty depends on its assumptions; an incorrectly chosen equation can look convincing locally | I compared kernels and introduced power-sum/quadratic hypotheses only where the evidence justified them |
| **Local trust region versus wider search** | Local search can refine an incumbent efficiently | A narrow region can exclude better solutions | F4's improvement after widening its search was a direct example |
| **Complex ensemble versus a single interpretable fit** | Multiple models expose disagreement | More parameters and search rules increase cost and reduce explainability | For F8, the simple 17-coefficient quadratic gave a particularly strong independently testable account |
| **Repeat a good point versus test a neighbour** | Repeating checks consistency at one setting | Identical inputs add little spatial information | Repeats were retained in the dataset and counted against the same evaluation budget |

**Interpretation:** there was no universal winning optimiser. The most useful method was the one whose assumptions, search region and predicted results were supported by the next observed return.

## 6. Performance: measured results (final confirmed personal bests)

| Function | Inputs | Best confirmed output | First attained |
|---|---:|---:|---|
| F1 | 2 | 1.9999999996761817 | R11 |
| F2 | 2 | 0.7442504263021256 | R13 |
| F3 | 3 | −0.0037530969187192596 | R13 |
| F4 | 4 | 0.7468979113807426 | R13 |
| F5 | 4 | 8662.405001248297 | R10 |
| F6 | 5 | −0.03751864724436928 | R12 |
| F7 | 6 | 3.3223680113931557 | R12 |
| F8 | 8 | 10.0 | R10 |

All values are personally confirmed portal results. They differ drastically in scale; no overall sum or average is meaningful. **Performance is measured by the best observed portal output after each round**, including the supplied initial best; the figure below plots those measured trajectories, not surrogate predictions.

![Best observed output by function over thirteen rounds, with separate vertical scales](results/figures/progress.svg)

*Each function has its own vertical scale. For numerical comparisons use the values and the [279-row observation dataset](data/all_observations.csv), not the apparent relative heights of lines across functions.*

**F7 evidence correction:** Round 11 submitted input `0.233000-0.128000-0.522000-0.276000-0.310000-0.667000`, score `3.278967926227992`, was confirmed from the official results email. **The original selection script is missing; the input is not.** See [verified facts](docs/VERIFIED_FACTS.md).

**Evidence-specific observations:**

- **F2:** one forecast of 0.730502 returned 0.505526. A different final-round region later returned 0.744250. A poor local forecast did not imply global convergence.
- **F4:** one local forecast was accurate to about 1.6 × 10⁻⁹, yet tiny search steps stagnated near 0.659. A wider strategy found 0.730459, followed by 0.746898 in R13.
- **F5:** a boundary query achieved 8662.405 at the legal upper coordinates. Its power-sum explanation was reconstructed *after* the successful query.
- **F7:** a positive Hartmann-6 structural forecast of 3.32236801 was recorded before the R12 portal return of 3.322368011393.
- **F8:** an additive 17-parameter quadratic located 10 at an interior vertex. A *separate retrospective* fit using only the 40 supplied starting observations fitted a full-rank model and predicted 13 later portal returns with maximum absolute error **below 2 × 10⁻¹⁴** across the 13 later scores (the last displayed digits can vary slightly by numerical environment). This does not mean the equation was identified in R1.

## 7. Evaluation methods and quantitative validation

The [final notebook](notebooks/Capstone_Final_Walkthrough.ipynb) recomputes counts, historical bests, GP illustrative decisions and F8/F5 structural checks from versioned data. [Automated tests](tests/) independently check numerical calculations. Performance evidence comes from **175 course-provided starting inputs and 104 personally evaluated portal inputs**, not simulated scores. Forecast errors are compared only against subsequently observed returns.

**Examples of predictive performance:** F2's prospective 0.730502 forecast returned 0.505526 (absolute error about **0.225**). F4 had a local forecast error near **1.6 × 10⁻⁹** without materially improving the objective. In a separate **retrospective** F8 structural test, a 17-coefficient quadratic fitted to the **40 initial F8 observations** predicted the **13 later F8 returns** with maximum absolute error below **2 × 10⁻¹⁴**; those thirteen returns were held out from coefficient fitting. These measure different kinds of performance and must not be combined into a single optimiser accuracy score.

**Forecast accuracy and finding a good region are different tests.** Some GP predictions were precise locally while failing to locate better regions. The capstone did not provide an unbiased global-optimiser ranking of HEBO versus TuRBO: unsubmitted candidates have unknown true outputs.

## 8. Assumptions, limitations and potential failure modes

- GP kernels assume a degree of smoothness or local similarity that sharp peaks, interactions or heteroscedastic noise can violate.
- GP fitted uncertainty is conditional on model assumptions; calibration has to be checked on later portal returns.
- With 2–8 dimensions and few points, adaptive sampling concentrates near previous successes, producing selection bias.
- Repeated locations spend evaluation budget while adding limited new spatial information.
- F2/F3/F4/F6 remain without confirmed closed-form expressions. F1 now has a published **retrospective Gaussian–cosine reconstruction**, [six fitted coefficients and a reproducible 10-initial/13-holdout test](src/bbo/f1_reconstruction.py). Its functional family was provided by separate working code and did not emerge from a blind fit; the historical Round 11 provenance remains separate.
- F5/F7/F8 mathematical models are numerically supported but **not authenticated copies of the undisclosed source code**.
- F7's R11 inputs and full-precision output were confirmed from the official course-results email; they are not surrogate-inferred. Its exact historical selection script remains unavailable.

## 9. Ethics, access and redistribution

No reported personal data is required to run the optimisation. The 175 supplied starting observations are included in public CSVs as part of the **public GitHub capstone deliverable required by Stage 2, Component 25.3**; original course binary files are not hosted. The course's publication instructions are not a licence for unrestricted third-party reuse of those observations. The [usage and permissions statement](USAGE_AND_PERMISSIONS.md) explains this distinction. External peer observations are not counted among my own 104 portal returns.

The same approach would require additional validation, security checks and hard operational limits before use in payroll or other high-consequence systems.

## 10. Reproducibility and maintenance

**Quick start:** install [requirements-notebook.txt](requirements-notebook.txt), run the [final notebook](notebooks/Capstone_Final_Walkthrough.ipynb), then `python -m pytest -q`. The [reproduction guide](docs/methods.md) covers other available scripts. [Full records](data/all_observations.csv), [final inputs](results/current_best_after_week13.csv) and the [visual gallery](docs/visualisations.md) allow a reviewer to verify the claims.

Historical coursework, original decision evidence and retrospective reference benchmarks are labelled separately. Further changes should document data cutoff, fitted model, package versions and why an algorithm was selected.

[← Project home](README.md)
