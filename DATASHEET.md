# Datasheet for Datasets | Black-Box Optimisation Capstone

*Imperial College London · Professional Certificate in Machine Learning and Artificial Intelligence*

**Dataset:** Eight anonymous black-box functions, thirteen rounds  
**Author and curator:** Tamer El-Tonsy  
**Observations:** 279 (175 course-provided; 104 personal portal evaluations)  
**Research completed:** 9 November 2026  
**Documentation updated:** 12 November 2026

[← Project home](README.md) · [Complete observations](data/all_observations.csv) · [Eight function investigations](functions/README.md) · [Model card](MODEL_CARD.md) · [Data permissions](USAGE_AND_PERMISSIONS.md)

This datasheet follows the seven dataset-lifecycle sections proposed in Gebru et al. (2021), *Datasheets for Datasets*. It also provides a route to all **29 questions** in the supplied Imperial College Module 25 template.

**Division of responsibility:** This page describes the **data**: origin, collection, quality, preparation, limitations, use and maintenance. The eight [function investigations](functions/README.md) remain the full accounts of optimisation methods, weekly choices, submitted inputs, results, plots, code links and lessons. [Appendix A](#appendix-a-function-specific-data-profiles) adds only function-specific dataset information and concise answers not otherwise explicit in those stories. [Appendix B](#appendix-b-module-25-template-coverage) maps the template to the relevant material.

The published observations identify F1–F8 as numerical objectives without physical units. **The programme FAQ says function descriptions and real-world analogies were supplied**, but those original function briefs are not included in the public data checked here. Their precise scenario labels are therefore **unverified in this repository**, not assumed absent. Research analogies are not asserted to describe the hidden functions.

## 1. Motivation

The dataset supports a sequential black-box optimisation exercise: maximise eight unknown objective functions, with one new portal evaluation per function in each of thirteen rounds.

The research examines how an optimiser selects informative experiments when responses are expensive or limited, and how new evidence changes the balance between exploration, exploitation and structural understanding. It also supports comparison of predicted scores with subsequently observed outcomes.

The programme supplied the 175 initial input/output pairs and the evaluation portal. Tamer El-Tonsy selected the 104 subsequent input vectors, recorded the returned scores and consolidated the observations and supporting research.

**Funding:** The participant's independent work was self-funded, with no external research grant or sponsor reported. Funding arrangements for the original course-provided observations are not known.

**Audience:** Students, researchers and practitioners studying Bayesian optimisation, Gaussian Process surrogates, experimental design, model validation and mathematical reconstruction. This is an educational research record, not a validated industrial benchmark.

## 2. Composition

### What an observation represents

Each row contains a continuous numerical input vector and the **actual scalar score** returned by its black-box function. The objective is maximisation, including for functions whose recorded scores are negative. The functions have unrelated output scales; their raw scores should not be averaged or compared directly.

| Function | Input dimensions | Initial X shape | Initial y shape | Initial rows | Later rows | Total |
|---|---:|---|---|---:|---:|---:|
| [F1](functions/F1/README.md) | 2 | (10, 2) | (10,) | 10 | 13 | 23 |
| [F2](functions/F2/README.md) | 2 | (10, 2) | (10,) | 10 | 13 | 23 |
| [F3](functions/F3/README.md) | 3 | (15, 3) | (15,) | 15 | 13 | 28 |
| [F4](functions/F4/README.md) | 4 | (30, 4) | (30,) | 30 | 13 | 43 |
| [F5](functions/F5/README.md) | 4 | (20, 4) | (20,) | 20 | 13 | 33 |
| [F6](functions/F6/README.md) | 5 | (20, 5) | (20,) | 20 | 13 | 33 |
| [F7](functions/F7/README.md) | 6 | (30, 6) | (30,) | 30 | 13 | 43 |
| [F8](functions/F8/README.md) | 8 | (40, 8) | (40,) | 40 | 13 | 53 |
| **Total** | | | | **175** | **104** | **279** |

The [master CSV](data/all_observations.csv) contains the fields `function`, `round`, `stage`, `source`, `is_initial`, `sequence_in_stage`, `input_status`, `x1`–`x8` and `output`. Round 0 identifies initial observations; rounds 1–13 identify personal portal evaluations. Unused input columns are intentionally blank for lower-dimensional functions.

**Completeness:** All 279 recorded outputs have input coordinates for their respective dimensions. No synthetic outputs or unobserved portal returns have been inserted. Repeated input vectors are retained as genuine additional evaluations, rather than deduplicated.

**Range:** Personal portal submissions used up to six decimal places within the permitted coordinate range from 0 to 0.999999.

### Sampling, coverage and uncertainty

The initial samples are sparse, especially in six and eight dimensions. Later inputs were selected adaptively and increasingly targeted regions considered promising at the time. This creates **selection bias**, not a representative random sample of the complete functions.

Some repeated input locations returned numerically consistent scores. This gives evidence of **repeatability at those locations**, not a general proof of deterministic behaviour. A fitted GP noise term likewise does not establish randomness in the hidden function. Function-specific repeatability and sensitivity observations are in [Appendix A](#appendix-a-function-specific-data-profiles).

No physical, demographic or personal attributes are present in the numerical dataset. Questions about human subject demographics, personal consent or sensitive-person identification are **not applicable**.

### Recommended data splits

Prefer chronological training and evaluation: a model predicting a round must use only observations available **before** that round's return. Randomly mixing earlier and later adaptive queries risks future-information leakage.

For example, the F8 retrospective quadratic check fits on its 40 initial observations and tests against its 13 later returns. This is a **retrospective held-out test**, not evidence that the initial model was discovered in Round 1. See the [F8 investigation](functions/F8/README.md).

## 3. Collection Process

The programme provided starting NumPy input and output arrays for each function. Their original generation mechanism, dates and undisclosed source equations are not documented in the public project.

Across thirteen rounds, the author reviewed available observations, investigated candidates, submitted one vector for each function through the course portal, recorded eight returned scores and revised the next decisions. Each round added eight evaluations. The resulting **104 personal queries** were deliberately chosen, not randomly sampled.

The [thirteen-round journey](journey/README.md) holds the chronological submissions, returns and surviving working material. Each [function story](functions/README.md) explains the changing strategy at the level of the individual objective. Git commit dates indicate repository publication, not necessarily the original date of every early experiment.

The consolidated data were checked against preserved inputs, returned scores and historical records; [automated tests](tests/) support consistency checking. Supplementary peer observations and simulated model feedback are **not** among these 279 portal observations.

No human subjects were recruited or compensated to create this numerical dataset; human consent, crowd-labelling and subject-ethics review are therefore not part of the collection procedure.

## 4. Preprocessing, Cleaning and Labelling

The source observations were assembled into one tabular structure with source, ordering and round metadata. The original numerical coordinates and scores were retained. No category encoding, score imputation, deduplication or general outlier deletion was applied. Blank non-applicable input columns are structural, not missing observations.

The returned scalar scores are system-generated measurements, **not human-assigned labels**.

During *analysis*, individual experiments used Gaussian Processes with RBF or Matérn kernels, ARD lengthscales, target standardisation, Yeo–Johnson or signed-log transformations, alternative noise assumptions and acquisition settings. Local polynomial fits, neural-network challengers and mathematical reconstructions were also investigated. These choices affected working models, **not the stored observation values**.

For function-specific model choices and preprocessing, follow the [methods guide](docs/methods.md), [model card](MODEL_CARD.md) and the relevant [function investigation](functions/README.md). The [final notebook](notebooks/Capstone_Final_Walkthrough.ipynb) provides reproducible calculations; historical round files provide the original development context.

## 5. Uses

**Appropriate uses:** Education and research in black-box optimisation, sample-efficient experiments, GP surrogate modelling, chronological predictive validation, acquisition-policy comparisons, sensitivity analysis and testing structural hypotheses.

**Restrictions and limitations:**

- Sparse observations and adaptive sampling limit claims about the full input space.
- A good local prediction does not guarantee a useful next experiment. F2 and F4 provide instructive examples in their [research stories](functions/README.md).
- The course did not disclose certified global maxima or original source equations for the hidden functions. A best observed portal result is not, by itself, a globally proven optimum.
- Retrospective models, mathematical surfaces, external observations and simulated HEBO/TuRBO feedback must not be counted as new original portal evaluations.
- Raw outputs from different functions have different scales and should not be combined without a defensible evaluation criterion.
- The published numeric records do not establish domain-specific operating constraints, costs, hazards or physical units. Performance does not establish suitability for consequential industrial or financial decisions.

For the detailed success, failures, methods, best vectors, forecast checks and lessons for each objective, use its [function page](functions/README.md). The [model card](MODEL_CARD.md) covers architecture, performance and model-specific trade-offs.

## 6. Distribution

**Location:** [Public project repository](https://github.com/tatonsyML/bbo-capstone-imperial-college), especially [data/all_observations.csv](data/all_observations.csv) and [function-specific observation files](functions/README.md). The original course-provided NumPy binaries are not published here. No independent dataset DOI is registered in this repository.

**Rights:** The repository's [MIT Licence](LICENSE) covers the author's original code and documentation **to the extent the author holds those rights**. It does not automatically cover the 175 course-provided observations, the hidden evaluation service or third-party material. The course required a public GitHub capstone submission, but **no separate unrestricted redistribution or commercial reuse permission for course-provided data has been confirmed**.

Public access is not an unrestricted data licence. Users planning redistribution should consult [Usage and permissions](USAGE_AND_PERMISSIONS.md) and the applicable original terms. Users may substitute independently authorised data when reusing the code.

There is no repository access fee. [CITATION.cff](CITATION.cff) provides citation metadata; cite the author and the precise repository version used.

## 7. Maintenance

**Curator:** Tamer El-Tonsy, repository owner. Questions and proposed corrections can be raised through [GitHub Issues](https://github.com/tatonsyML/bbo-capstone-imperial-college/issues).

The thirteen-round record is complete. Updates should correct documented errors or clarify methods without rewriting historical decisions. Any correction to a portal observation should identify its source and retain a descriptive Git history.

New post-capstone experiments, derived model outputs or peer data should be labelled separately; they are **not** additions to the 104 personal portal returns. Historical snapshots remain useful for chronological reproducibility.

---

## Appendix A. Function-specific data profiles

The seven sections above describe the data shared by all eight functions. The profiles below add only **function-specific data characteristics, quality and limitations**. To follow a model, experiment or decision through thirteen rounds, open the linked [function investigation](functions/README.md). The original research narratives are not repeated here.

### F1 · Near-zero scores and the need for scaling

**What the data contain:** Two continuous inputs, 10 starting observations and 13 personal evaluations. The observed incumbent rose from `7.710875114502849e-16` to `1.9999999996761817` in Round 11. Outcomes have no confirmed physical units.

**Data treatment and quality:** Most early scores are many orders of magnitude smaller than the later high-response point. Transforming the modelling target helped explore this disparity; the raw recorded scores have not been changed. Repeating the same Round 11 input in Rounds 12 and 13 produced identical returns, demonstrating repeatability only at that location.

**Interpretation and limits:** A conventional smooth fit near almost-zero observations may overlook a narrow positive region. The separate mathematical reconstruction is a later validation of an already proposed family, not the original candidate-selection method. The limited record does not prove a global optimum. [Full F1 research](functions/F1/README.md) · [F1 observations](functions/F1/observations.csv).

### F2 · Forecast error and missing coverage

**What the data contain:** Two inputs, 10 starting observations and 13 portal evaluations. The highest recorded score increased from `0.6112052157614438` to `0.7442504263021256` in Round 13. Scores are numerical rewards with no published physical units.

**Data treatment and quality:** Adaptive choices placed more observations in previously promising areas, not uniformly across the input square. GP and local polynomial experiments used stored observations with model-specific transformations. There is no exact repeated-input experiment sufficient to quantify observation noise.

**Interpretation and limits:** One prospective model forecast around `0.730502` was followed by an actual return around `0.505526`. That discrepancy demonstrates poor prediction for the tested input, not necessarily a stochastic objective. Unsampled regions remain uncertain, and the best observed score does not certify a global maximum. F2 is useful for testing chronological calibration and the consequences of local extrapolation. [Full F2 research](functions/F2/README.md) · [F2 observations](functions/F2/observations.csv).

### F3 · Negative outputs and local search bias

**What the data contain:** Three inputs, 15 starting observations and 13 personal evaluations. All recorded outputs are negative, so maximising means moving closer to zero. The best improved from `-0.034835313350078584` initially to `-0.0037530969187192596` in the final round.

**Data treatment and quality:** Subsequent points were selected adaptively, yielding uneven coverage rather than a representative sample of the three-dimensional domain. Local GP, polynomial and other surrogate experiments did not alter the stored outputs. Two-dimensional projections do not control the unplotted third coordinate.

**Interpretation and limits:** The record contains insufficient independent coverage to conclude that a fitted local peak is the true maximum. No validated analytical source equation or exact-input replication series establishes noise properties. F3 is suitable for examining selection bias, the risk of local optimisation and whether exploring another region improves a previously strong incumbent. [Full F3 research](functions/F3/README.md) · [F3 observations](functions/F3/observations.csv).

### F4 · Local precision without decision value

**What the data contain:** Four inputs, 30 starting observations and 13 evaluations. The best measured output improved from `-4.025542281908162` to `0.7468979113807426`, first achieved in Round 13.

**Data treatment and quality:** Several late inputs concentrated around one promising region. This increases local information without establishing how the rest of the domain behaves. One contemporaneous forecast differed from the returned score by approximately `1.6 × 10⁻⁹`, while tiny candidate changes brought little improvement. The same Round 11 and Round 12 input yielded the same measured value.

**Interpretation and limits:** Prediction accuracy and optimisation success must be assessed separately. A model which reproduces local changes can still guide inefficient experiments. Model target scaling and GP fitting do not change original scores, and repeated data at one point do not establish global determinism. The recorded incumbent is not a proof of the undisclosed function's maximum. [Full F4 research](functions/F4/README.md) · [F4 observations](functions/F4/observations.csv).

### F5 · Large scores and boundary measurements

**What the data contain:** Four inputs, 20 starting observations and 13 portal returns. F5 operates on a much larger score scale than other functions. The measured best grew from `1088.8596181962705` to `8662.405001248297` at the legal upper-coordinate boundary in Round 10.

**Data treatment and quality:** Model-specific response transformations help compare candidates numerically; original portal outputs are retained. Exact repetitions of the same upper-corner vector in Rounds 11, 12 and 13 returned the same score. Combining F5's unscaled results with other function scores would be misleading.

**Interpretation and limits:** The later power-sum reconstruction closely matches tested returns but was developed after the original boundary decision. Its fitted behaviour is not independently authenticated across every possible input. Repeat measurements provide local consistency rather than broader sampling coverage. F5 illustrates the consequences of output scale, strong boundary trends and spending later evaluation budgets on repeats. [Full F5 research](functions/F5/README.md) · [F5 observations](functions/F5/observations.csv).

### F6 · Nearby points with differing responses

**What the data contain:** Five inputs, 20 starting observations and 13 subsequent returns. All measured scores are negative, with the incumbent improving from `-0.7142649478202404` to `-0.03751864724436928` in Round 12.

**Data treatment and quality:** Some inputs close in coordinate space produce substantially different outcomes. Local GPs, neural-network challengers and controlled probes were analytical tools; the original numerical measurements remain unchanged. No exact-repeat series permits a reliable separation of steep deterministic response from stochastic noise.

**Interpretation and limits:** With five dimensions, twenty initial samples offer limited coverage. A two-dimensional scatter projection does not hold the other three coordinates constant and should not be interpreted as a full surface. A narrow fitted neighbourhood may understate uncertainty elsewhere, and the highest measured result is not a certified global optimum. F6 is especially useful for evaluating sensitivity checks and when to abandon a locally unreliable predictor. [Full F6 research](functions/F6/README.md) · [F6 observations](functions/F6/observations.csv).

### F7 · Structural hypothesis in six dimensions

**What the data contain:** Six inputs, 30 starting observations and 13 portal evaluations. The best recorded score increased from `1.3649683044991994` to `3.3223680113931557` in Round 12. The Round 11 vector and output are included in the master record.

**Data treatment and quality:** A positive Hartmann-6 hypothesis predicted approximately `3.32236801` before the Round 12 return, which closely matched the measured score. Later numerical checks of the reconstruction are separate from that prospective forecast. Round 13 changed one coordinate slightly and was not an exact repeat.

**Interpretation and limits:** A close prediction at one tested point strengthens a specific hypothesis; it does not establish the undisclosed equation everywhere. The six-dimensional domain is sparsely observed. Modelled plots holding four coordinates fixed are different from projections of actual observations. F7 supports study of testable structural forecasts, local sensitivity and the costs of exploring higher dimensions. [Full F7 research](functions/F7/README.md) · [F7 observations](functions/F7/observations.csv).

### F8 · Sparse eight-dimensional data with a simple fitted model

**What the data contain:** Eight inputs, 40 initial observations and 13 personal returns. The starting best was `9.598482002566342`; the portal returned `10` at a fitted vertex in Round 10.

**Data treatment and quality:** The measured scores agree closely with a 17-coefficient additive quadratic representation. A later retrospective check fitted the family using only forty initial observations and evaluated its predictions against thirteen subsequent portal returns. This later held-out test is distinct from the model developed around the Round 10 decision. The identical vertex input was returned in Rounds 10–13, each with score 10.

**Interpretation and limits:** The fitted quadratic has a mathematically established maximum at its vertex. That does not certify the undisclosed source equation over all possible inputs. Eight-dimensional coverage remains sparse despite strong numerical agreement. F8 illustrates interpretable modelling, the importance of chronological validation and the risks of unnecessary surrogate complexity. [Full F8 research](functions/F8/README.md) · [F8 observations](functions/F8/observations.csv).

**Scope:** These are descriptions of the recorded data, not substitutes for the function histories or model card.

## Appendix B. Module 25 template coverage

The course template contains **29 questions across seven sections**. Shared questions are answered in Sections 1–7; the eight profiles in [Appendix A](#appendix-a-function-specific-data-profiles) supply additional function-level data detail. For method and weekly-iteration questions, follow the existing investigations instead of duplicating thirteen rounds.

| Template section | Questions | Answer location |
|---|---:|---|
| **Function overview** | 5 | [Composition](#2-composition) (identifier, dimensions, initial shapes, output meaning, unverified original-brief context) and each [function introduction](functions/README.md) |
| **Nature of the data** | 4 | [Composition](#2-composition) (structure, sampling and coverage), [Appendix A](#appendix-a-function-specific-data-profiles) (repeatability and noise), and each function's observed progress and analysis |
| **Optimisation strategy** | 4 | [Function stories](functions/README.md), especially each expandable thirteen-round development section and recorded strategy changes |
| **Data handling and preprocessing** | 4 | [Preprocessing](#4-preprocessing-cleaning-and-labelling), [methods](docs/methods.md), and original modelling evidence linked in the function stories |
| **Weekly iteration and learning** | 4 | Each function's thirteen-round development and closing lessons; restart improvements are explicit in [Appendix A](#appendix-a-function-specific-data-profiles) |
| **Performance and results** | 4 | The best input and output table, chart and mathematical analysis at the top of **each function page**; confidence limits and missing physical targets are described [above](#5-uses) and in Appendix A |
| **Ethical, practical and general considerations** | 4 | [Uses](#5-uses), [Distribution](#6-distribution) and the linked function conclusions, including limits on scaling to expensive real-world settings |
| **Total** | **29** | One datasheet plus eight complete function investigations |

## Reference

Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). *Datasheets for Datasets*. *Communications of the ACM*, **64**(12), 86–92. https://doi.org/10.1145/3458723

[← Project home](README.md) · [Function investigations](functions/README.md)
