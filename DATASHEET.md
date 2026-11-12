# Datasheet for Datasets | Black-Box Optimisation Capstone

*Imperial College London · Professional Certificate in Machine Learning and Artificial Intelligence*

**Dataset:** Eight anonymous black-box functions, thirteen rounds  
**Author and curator:** Tamer El-Tonsy  
**Observations:** 279 (175 course-provided; 104 personal portal evaluations)  
**Research completed:** 9 November 2026  
**Documentation updated:** 12 November 2026

[← Project home](README.md) · [Complete observations](data/all_observations.csv) · [Eight function investigations](functions/README.md) · [Model card](MODEL_CARD.md) · [Data permissions](USAGE_AND_PERMISSIONS.md)

This datasheet follows the seven dataset-lifecycle sections proposed in Gebru et al. (2021), *Datasheets for Datasets*. It also provides a route to all **29 questions** in the supplied Imperial College Module 25 template.

**Division of responsibility:** This page describes the **data**: origin, collection, quality, preparation, limitations, use and maintenance. The eight [function investigations](functions/README.md) remain the full accounts of optimisation methods, weekly choices, submitted inputs, results, plots, code links and lessons. [Appendix A](#appendix-a-function-specific-dataset-notes) adds only function-specific dataset information and concise answers not otherwise explicit in those stories. [Appendix B](#appendix-b-module-25-template-coverage) maps the template to the relevant material.

The objectives F1–F8 were presented as anonymous numerical functions. **No official real-world scenario or physical unit was supplied for an individual function.** Examples in the research stories are analogies or contemporary working hypotheses, not authenticated descriptions of the hidden functions.

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

Some repeated input locations returned numerically consistent scores. This gives evidence of **repeatability at those locations**, not a general proof of deterministic behaviour. A fitted GP noise term likewise does not establish randomness in the hidden function. Function-specific repeatability and sensitivity observations are in [Appendix A](#appendix-a-function-specific-dataset-notes).

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
- The exercises contain no verified real-world operating constraints, costs, hazards or domain-specific targets. Performance does not establish suitability for consequential industrial or financial decisions.

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

## Appendix A. Function-specific dataset notes

The following table supplies the **data-documentation detail** that is not central to the eight full research narratives. It also gives a concise response to the Module 25 prompt, *“If you restarted, what would you do differently?”* The complete strategy, weekly learning, results, best inputs, equations, visualisations and code links stay in the linked stories.

| Function | Dataset characteristics and uncertainty | What I would change if restarting | Full investigation |
|---|---|---|---|
| **F1** | Early outputs are extremely small, making target scaling important. Identical R11–R13 inputs returned the same high score; this is a local repeatability check only. | Test distant regions earlier, before repeatedly refining near-zero observations. | [F1](functions/F1/README.md) |
| **F2** | No exact repeated query supports a direct noise test. Local forecasts are not reliably representative of other regions. | Reserve more queries for competing regions and check prospective forecast calibration sooner. | [F2](functions/F2/README.md) |
| **F3** | All recorded scores are negative. There is no exact-input repeat test sufficient to separate noise from local sensitivity. | Challenge apparent local peaks sooner with out-of-region probes. | [F3](functions/F3/README.md) |
| **F4** | Identical R11/R12 queries returned the same score. Reliable local forecasts do not establish broad domain coverage. | Choose experiments by likely improvement, not predictive precision alone; widen unproductive search regions. | [F4](functions/F4/README.md) |
| **F5** | Output values are orders of magnitude larger than for most functions; raw target scaling matters. R10–R13 boundary repeats are consistent. | Test controlled boundary directions earlier and reserve some queries for alternatives. | [F5](functions/F5/README.md) |
| **F6** | Nearby inputs can return different negative scores. Without exact repeats, local geometric sensitivity is not evidence of stochastic noise. | Probe multiple coordinates and alternative regions earlier; check robustness before trusting a local surrogate. | [F6](functions/F6/README.md) |
| **F7** | Six-dimensional coverage is sparse. R12/R13 differ slightly in one input, so their near-equal returns are **not** an exact-input noise test. | Compare separate promising regions earlier and test structural hypotheses on subsequent returns. | [F7](functions/F7/README.md) |
| **F8** | Eight-dimensional observations are strongly consistent with an additive quadratic. R10–R13 repeat the same vertex. Its initial-40-only fitted model was evaluated retrospectively against later returns. | Examine simple polynomial structure sooner, before escalating surrogate complexity. | [F8](functions/F8/README.md) |

**No official expectations by domain:** Because the course did not assign the anonymous functions a verified physical scenario, the Module 25 question about alignment with *the problem description* is evaluated against the **working hypothesis and prior results**, not an invented industrial benchmark. Each function's weekly story identifies where those expectations succeeded or failed.

**Confidence:** The best input and highest observed score are reported at the top of each function page. Repeated queries, local agreement and mathematical reconstructions strengthen specific claims, but the finite observations alone do not certify the undisclosed global optima.

## Appendix B. Module 25 template coverage

The supplied template has **29 questions across seven sections**. The linked function pages form part of this datasheet's supporting documentation; they are not duplicated here.

| Template section | Questions | Answer location |
|---|---:|---|
| **Function overview** | 5 | [Composition](#2-composition) (identifier, dimensions, initial shapes, output meaning, no disclosed scenario) and each [function introduction](functions/README.md) |
| **Nature of the data** | 4 | [Composition](#2-composition) (structure, sampling and coverage), [Appendix A](#appendix-a-function-specific-dataset-notes) (repeatability and noise), and each function's observed progress and analysis |
| **Optimisation strategy** | 4 | [Function stories](functions/README.md), especially each expandable thirteen-round development section and recorded strategy changes |
| **Data handling and preprocessing** | 4 | [Preprocessing](#4-preprocessing-cleaning-and-labelling), [methods](docs/methods.md), and original modelling evidence linked in the function stories |
| **Weekly iteration and learning** | 4 | Each function's thirteen-round development and closing lessons; restart improvements are explicit in [Appendix A](#appendix-a-function-specific-dataset-notes) |
| **Performance and results** | 4 | The best input and output table, chart and mathematical analysis at the top of **each function page**; confidence limits and missing physical targets are described [above](#5-uses) and in Appendix A |
| **Ethical, practical and general considerations** | 4 | [Uses](#5-uses), [Distribution](#6-distribution) and the linked function conclusions, including limits on scaling to expensive real-world settings |
| **Total** | **29** | One datasheet plus eight complete function investigations |

## Reference

Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). *Datasheets for Datasets*. *Communications of the ACM*, **64**(12), 86–92. https://doi.org/10.1145/3458723

[← Project home](README.md) · [Function investigations](functions/README.md)
