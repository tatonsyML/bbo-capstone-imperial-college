# Model Card | Evidence-Gated, Function-Specific Black-Box Optimisation

**Model name:** Evidence-Gated BBO Optimiser  
**Type:** Sequential Bayesian optimisation with human-reviewed surrogate and structural challengers  
**Version:** 4.1, Module 21 / Round 10 submitted  
**Developer and maintainer:** Project author  
**Evidence cut:** Portal-returned results through **Week 9** (247 evaluations); **Round 10 scores pending**  
**Code:** [src/bbo/](../src/bbo/) | **Data:** [docs/datasheet.md](datasheet.md) | **Decisions:** [docs/decision_log.md](decision_log.md)

> **In plain English:** When every experiment is expensive and the formula is hidden, an algorithm predicts which setting to try next. This project goes one step further: it checks whether that algorithm has been reliable *before* allowing its prediction to drive the next experiment.

## 1. At a glance

The task is to obtain the **highest observed score** for each of eight unknown functions. Each function accepts between two and eight numeric settings. I can submit only one new setting per function per round and receive the answer later.

There is **no single model** that works equally well on every function. My framework asks several models for proposals, reviews their past forecast errors, and chooses one legal input for the portal.

**Core decision principle: The most confident or complicated model does not automatically get the deciding vote. Evidence of past predictive accuracy matters more.**

### Quick definitions

| Term | Meaning for a non-specialist |
|---|---|
| **Gaussian Process (GP)** | A statistical model that predicts a score *and* expresses uncertainty about that prediction |
| **Acquisition function** | A rule for choosing whether to pursue a promising estimate or explore an uncertain region |
| **EI / PI / UCB** | Expected Improvement / Probability of Improvement / Upper Confidence Bound: three different ways to rank possible next experiments |
| **HEBO-inspired committee** | Several GP kernels and acquisition rules provide alternative recommendations rather than one model dictating the answer |
| **TuRBO-style search** | A more detailed search near a strong observed result, rather than searching the whole domain at once |
| **Structural model** | A simpler equation, such as a quadratic, fitted when observations suggest a recognisable mathematical pattern |
| **Evidence gate** | The documented review of predictive accuracy, direct observations, model disagreement and the value of a new experiment |

## 2. Intended use

**Suitable for:** Educational or research optimisation of expensive, bounded, continuously valued black-box functions; tens of observations rather than thousands; one query at a time; and projects where an analyst reviews proposals before evaluation.

**Not suitable without substantial redesign for:** Safety-critical automatic decisions, discrete or categorical variables without appropriate encoding, rapidly changing functions, abrupt discontinuities, very noisy outputs, extremely high dimensions, or any application requiring a *guaranteed* global maximum.

**Who should use this card?** Course assessors, other students, maintainers and practitioners who want to understand what the optimiser does, why it chose particular points and what the results do *not* establish.

## 3. How the approach decides

The pipeline combines **measured results**, **model-generated candidates** and **a documented human decision**:

1. **Load only information available at decision time.** Start with the course's original observations and append each completed portal response. Do not train historical forecasts on later results.
2. **Generate alternatives.** Fit suitable GPs, compare kernels and acquisitions, examine local or structural fits, and optionally propose a regional-search candidate.
3. **Check the evidence.** Compare prospective forecasts against their actual returned scores; review local experiments, model disagreement, plausible gain and the likely information from a failure.
4. **Apply the decision gate.** Prefer models with a credible forecasting record. Reduce the influence of models that confidently missed. A simple fit supported by controlled observations can overrule a more elaborate GP.
5. **Enforce submission requirements.** Inputs must lie from 0.000000 to 0.999999 inclusive, with six decimal places. Check for unhelpful duplicates and preserve the selected vector **before** the portal returns a result.

**Important qualification:** This is a human-reviewed decision procedure, not a fully automated, numerical acceptance threshold. Model reliability and expected information value are criteria for review, but I have not implemented a formally calibrated universal model-voting rule.

### What HEBO-inspired and TuRBO-style mean here

The implementation in [src/bbo/optimizer.py](../src/bbo/optimizer.py) makes the distinction auditable:

- **HEBO-inspired:** Fits RBF, Matérn 1.5 and Matérn 2.5 GPs with a Yeo–Johnson transformation. It evaluates EI, PI and UCB over a seeded Sobol candidate pool and compares robust candidate ranks. This is **not** a complete implementation of HEBO.
- **TuRBO-style:** Fits a GP and evaluates EI over a Sobol pool restricted to a region around the best observed point. The coded default region width is **0.20** in normalised input space. This is a local challenger, **not** the complete TuRBO method with automatic expansion, contraction and restarts.
- **Other challengers:** Controlled one-coordinate steps, local quadratics, structural polynomial models and additional retrospectives using alternative kernels, noise levels or output transforms.

An optional adapter to the official HEBO package exists in the code. Its presence does **not** establish that official HEBO was run for the submitted rounds.

## 4. How the strategy evolved

| Stage | What changed | Why |
|---|---|---|
| **Weeks 1–2** | GP-led Bayesian optimisation using EI and UCB; relatively broad exploration | Learn a useful starting workflow with limited observations |
| **Weeks 3–4** | Alternative kernels, regional searches and supplementary SVM/neural-network diagnostics | Different functions responded differently to the same search strategy |
| **Weeks 5–6** | Controlled local adjustments and quadratic fitting where the pattern warranted it | Isolate the effect of a coordinate instead of changing too many variables together |
| **Week 7** | Cross-validation and comparisons of predictions against later points | Distinguish a model that fits historical data from one that predicts useful new results |
| **Week 8** | Recorded pre-result forecasts, smaller steps and alternative candidate reviews | Make model failures visible and reduce unearned confidence |
| **Week 9** | Quantified forecast errors and function-specific allocation of risk | Reward reliable local models; stop blindly following poor forecasts |
| **Round 10** | HEBO-inspired and TuRBO-style challenger evaluation, additional quadratic/cubic comparisons and separate peer-informed external research | Test neglected regions without discarding strong direct evidence |

**The decisive lesson from Week 9:** The F4 local model predicted 0.658932869 and the portal returned 0.658932867, an error of about **1.56 × 10⁻⁹**. F2's prediction of 0.730502 returned 0.505526, an error of **0.224977**. Treating these two models as equally reliable would be difficult to justify.

The refinement is therefore not simply “more algorithms”. It is a stronger rule for deciding **when an algorithm should be trusted**.

## 5. Performance: what actually happened?

**Primary metric:** The best **portal-observed** score per function. Larger is better, including when scores are negative. Improvements in F1 or negative-valued functions are not expressed as simple percentages because that would be misleading.

**Secondary measures:** New-best rounds, error in forecasts recorded before outcomes, rolling/leave-one-out prediction error where assessed, uncertainty disagreement, and information gained by a deliberately diagnostic query.

### Official best observations through Week 9

| Function | Dimensions | Best in starting data | Best measured by Week 9 | New bests in 9 rounds | What it shows |
|---|---:|---:|---:|---:|---|
| **F1** | 2 | 7.7109 × 10⁻¹⁶ | **1.9213 × 10⁻¹⁵** | 2 | Extreme scale makes an apparently precise local peak practically uninformative |
| **F2** | 2 | 0.611205 | **0.691315** | 3 | Some improvement, but the latest smooth local forecast failed substantially |
| **F3** | 3 | −0.034835 | **−0.020856** | 2 | Improved then stalled, suggesting value in investigating another region |
| **F4** | 4 | −4.025542 | **0.658933** | 5 | Large measured gain and unusually reliable fine local predictions |
| **F5** | 4 | 1,088.860 | **6,583.561** | 9 | Improved in every completed round while approaching the upper boundary |
| **F6** | 5 | −0.714265 | **−0.541448** | 3 | Improvement is real, but later local changes have been inconsistent |
| **F7** | 6 | 1.364968 | **1.786338** | 6 | Consistent local progress does not rule out a better distant region |
| **F8** | 8 | 9.598482 | **9.932443** | 8 | Strong improvement and evidence for a remarkably simple fitted structure |

**Observed total:** 175 initial values + 9 completed rounds × 8 functions = **247**. The next eight inputs were submitted for Round 10 but do not have verified outputs in this assessment cut.

### A closer look at four revealing cases

**F2: A failed forecast.** The Week 9 forecast error of 0.224977 was large relative to the improvement being sought. The model's numerical confidence was not enough to warrant another wide move.

**F4: A model that earned trust.** Fine local changes tracked the observed result so closely that further controlled refinement was defensible. Here a simple model had stronger evidence than a complicated global search.

**F5: A useful change in mathematical model.** Retrospective experiments compared additive quadratic and additive cubic fits against a small external hold-out set. In that experiment, the best tested cubic achieved RMSE **61.80** versus **1,033.44** for the tested quadratic. That supports the *model form* and upper-bound direction, but these settings were selected after testing alternatives on a small external set. The apparent improvement is **not** an independent guarantee of a future score.

**F8: A structural discovery.** An additive quadratic with **17 coefficients** fitted all **49 personal observations** to around numerical precision. It also predicted **five external held-out scores** with error around **1.35 × 10⁻¹⁰** when trained on my own data. Its mathematically implied vertex is:

**0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000**

Its fitted score is **10**. This remains a **predicted**, not a portal-returned, Round 10 value. These external checks support the functional shape, but the independent points are still selected rather than randomly sampled; absolute global optimality is not established by the portal evidence.

## 6. The Round 10 submission: decisions, not outcomes

The final [Round 10 query record](../experiments/round_10/queries.txt) stores eight six-decimal input strings. Their rationale is summarised below.

| Function | Decision | Evidence and uncertainty |
|---|---|---|
| **F1** | Test a nearby positive-response region, away from 0.73 | Better external positive results suggest an alternative search area; exact local peak remains unknown |
| **F2** | A small diagnostic move near the incumbent | The previous broad forecast failed |
| **F3** | Target a different promising neighbourhood | External observations suggest stronger scores; interpolation remains exploratory |
| **F4** | Preserve controlled local refinement | The preceding prospective local forecast was exceptionally accurate |
| **F5** | Query all four legal upper bounds | Nine successive measured improvements support the direction |
| **F6** | Explore a peer-informed alternative region | Ensemble-predicted mean changed from about −0.262 to −0.192, **not** a measured gain |
| **F7** | Test a different high-performing region | Ensemble-predicted mean changed from about 1.73 to 2.79; the model range remains wide |
| **F8** | Query the fitted additive-quadratic vertex | Predicted score 10 with unusually strong external prediction tests |

**External evidence disclosure:** Some Round 10 proposals arose from supplementary experiments informed by publicly shared classmates' evaluated points. These observations were used for **external benchmarking and experimental models**, not merged with the 247 personal portal observations. Sources and their role are documented in the [datasheet](datasheet.md). Their acceptability in assessed query design must be checked against the programme's collaboration requirements.

## 7. Assumptions, constraints and failure modes

| Assumption or limitation | What it means | What might go wrong |
|---|---|---|
| **Local continuity and smoothness** | Nearby settings usually give related scores | A narrow spike, cliff or discontinuity may be missed or smoothed away |
| **Stationarity** | A kernel's notion of distance applies similarly across the domain | Different areas may behave differently; a single length scale can mislead |
| **Noise and stability** | Earlier observations remain informative in later rounds | Location-dependent randomness could make a promising signal look reliable when it is not |
| **Sparse sampling** | A few dozen observations must guide a large search | Predictive uncertainty outside visited areas is mostly a modelling assumption |
| **Adaptive sampling bias** | Earlier recommendations shape later training points | Repeated success in one region may hide a better region elsewhere |
| **Polynomial structure** | Fitted trends continue into untested locations | Excellent interpolation alone does not guarantee global optimality |
| **Single query and delayed feedback** | Only one new experiment per function is evaluated at a time | Contradictory model recommendations cannot be checked immediately |
| **Human and LLM judgement** | Code generation and interpretation involve review | Incorrect explanations, confirmation bias and unrecorded overrides threaten reproducibility |

**A concrete failure mode:** Models that fitted F2 locally still produced a large Week 9 forecast error. By contrast, F4 and F8 show why a narrow or structurally simple model can sometimes be more useful than a more flexible alternative.

Exact GP fitting and candidate searching are manageable at these sample sizes. Computation is **not** the main constraint here; the limited number of *real evaluations* is.

## 8. Transparency, ethics and real-world adaptation

There are no personal records in this synthetic challenge, so demographic fairness and privacy are not primary dataset risks. The important ethical risks are **overclaiming**, **concealing failures**, **misusing external evidence** and **transferring a classroom method into high-consequence settings without validation**.

Transparency supports practical trust in four ways:

1. **Keep observations separate from forecasts.** A predicted score is not an achieved result.
2. **Record reasoning before feedback.** This reduces the temptation to invent an explanation for a successful outcome afterwards.
3. **Show failed models as well as successful ones.** A model earns its influence from tested performance, not its reputation.
4. **Keep human decisions inspectable.** The code can regenerate candidates, but past manual choices also require a decision record.

In manufacturing, agriculture or clinical research, an optimisation query might waste material, create environmental harm or present a safety risk. The current educational model is **not** suitable for those tasks without domain-specific limits, independent tests, explicit risk tolerances and appropriate human oversight.

## 9. Reproducibility: what is possible and what is not?

**Available now:** Chronological CSVs for the personal observations, exact round inputs/outputs, current Python pipeline, documented kernels/acquisitions and the forecast/decision files linked below.

**To reproduce numerical experiments:** Use the same observation cut, code revision, Python dependencies and random seeds. The core pipeline uses a seeded Sobol candidate generator; numerical optimisation may still vary slightly with library versions and computing environments.

**To reproduce original historical judgements:** Some early discarded alternatives and manual settings were not saved. Those choices cannot be reconstructed perfectly from the final scripts. This is a documented limitation, not a claim of complete historical reproducibility.

**To reproduce initial source files:** The original programme-distributed NumPy arrays must be obtained through authorised channels. The public project does not claim redistribution rights over them.

Useful starting points:
- [Dataset and provenance](datasheet.md)
- [Chronological queries and outcomes](../experiments/)
- [Current implementation](../src/bbo/)
- [Best measured scores](../reports/current_best_after_week9.csv)
- [Forecast audit](../reports/week9_forecast_audit.csv)
- [F8 quadratic coefficients](../reports/f8_additive_quadratic_coefficients.csv)
- [Decision log](decision_log.md)

## 10. Does the model card need more detail?

**Not in the main narrative.** This card explains the task, how candidate decisions are made, the measured evidence, what failed and what should not be concluded. A reader should be able to follow that in a few minutes.

The **next useful additions** are a per-function forecast-calibration table, a machine-readable candidate decision register and confirmed Round 10 outputs when available. Those belong in linked evidence files rather than making the central explanation harder to read.

**Bottom line:** The optimiser is best understood as a disciplined sequence of expensive experiments. The most valuable improvement was learning to judge the quality of its recommendations, not simply adding more sophisticated algorithms.
