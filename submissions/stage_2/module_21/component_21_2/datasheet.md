# Datasheet: BBO Query History and Function Evaluations

**Project:** Black-Box Optimisation Capstone  
**Status:** Observed data through Week 9; Round 10 candidate set recorded separately and not yet treated as an observation  
**Maintainer:** Tamer El-Tonsy  
**Purpose:** Transparency, auditability and reproducible sequential optimisation

## 1. Motivation

This dataset was created to support a capstone challenge in which eight unknown black-box functions must be maximised under a strict evaluation budget. The internal formulae and gradients are unavailable. The only way to learn about each function is to submit an input vector and observe the returned scalar output.

The dataset therefore serves two purposes. First, it is the evidence base for sequential black-box optimisation. Second, it is an audit trail of how the optimisation strategy changed as new evidence arrived. This distinction matters because the later observations were not sampled independently: they were partly selected by models fitted to earlier observations.

The initial data were supplied by the programme. I generated the later query points and recorded the returned results. I did not generate the initial sample and therefore do not infer or claim a sampling design for it unless that design is documented by the programme.

## 2. Composition

Each instance is one black-box evaluation: a vector `x` within the unit hypercube and one scalar output `y=f(x)`. All functions are maximisation problems.

| Function | Dimensions | Initial observations | Week 1–9 observations | Observed total |
|---|---:|---:|---:|---:|
| F1 | 2 | 10 | 9 | 19 |
| F2 | 2 | 10 | 9 | 19 |
| F3 | 3 | 15 | 9 | 24 |
| F4 | 4 | 30 | 9 | 39 |
| F5 | 4 | 20 | 9 | 29 |
| F6 | 5 | 20 | 9 | 29 |
| F7 | 6 | 30 | 9 | 39 |
| F8 | 8 | 40 | 9 | 49 |
| **Total** |  | **175** | **72** | **247** |

The working project stores the programme-supplied seed arrays as NumPy files. They are not redistributed publicly here until the programme's redistribution terms are confirmed. The public working history is represented in chronological CSV tables containing the function identifier, stage, submitted input and observed output.

### Known gaps and data-quality issues

The recorded evaluations have no known missing output fields and the Week 9 audit found no exact duplicate submitted points. The more important gaps are structural:

- **Adaptive sampling:** later queries concentrate where earlier models or observed trajectories suggested value. The dataset is a search history, not a representative survey of each domain.
- **High-dimensional sparsity:** 49 observations in 8D and 39 in 6D leave almost all of the corresponding hypercubes unobserved.
- **Uneven information density:** F4 and F7 contain dense local sequences; F5 is concentrated near an upper boundary trajectory; F1 contains values spanning extreme orders of magnitude.
- **No counterfactual outcomes:** when an alternative optimiser would have proposed another point, its portal value is unknown because it was never queried.
- **Unknown observation noise:** the budget did not support systematic repeat measurements, so determinism is not assumed merely because the portal returns a precise number.
- **Rounding:** submitted coordinates are constrained to six decimal places. The stored raw course inputs and derived modelling values may contain greater precision, but the portal observation corresponds to the submitted six-decimal vector.

## 3. Collection process

### Initial data

The programme supplied the initial input/output pairs for all eight functions. Their provenance and counts are preserved even where the original binary files are not redistributed publicly.

### Sequential queries

One new point per function was selected and submitted in each completed round. The strategy evolved with the evidence rather than remaining fixed:

| Stage | Main collection logic |
|---|---|
| Early rounds | Gaussian-process Bayesian optimisation, uncertainty-aware acquisition and broad exploration |
| Middle rounds | Alternative kernels and diagnostic models, cross-validation, local search and function-specific treatment |
| Later rounds | Controlled one-coordinate experiments, local quadratic fits, pre-result forecasting, model-authority reduction after forecast failure, and function-specific exploration/exploitation |
| Round 10 preparation | HEBO-inspired warping/acquisition challengers, TuRBO-style trust-region logic, multi-model restarts where incumbents stalled, and direct structural modelling where the data supported it |

Human judgement remained part of the collection mechanism. A model recommendation was not automatically submitted. In later rounds the decision increasingly considered prospective forecast accuracy, local evidence, disagreement between models, potential objective gain and the information a failed query would still provide.

The reasoning for a query was recorded before its output arrived whenever practical. This reduces hindsight bias and separates prediction from later interpretation.

## 4. Preprocessing, cleaning and labelling

The raw observations are preserved. No observation has been deleted, relabelled or replaced because it was inconvenient for the model.

Inputs already lie in the bounded search domain, so no permanent input rescaling is written back to the raw data. Portal submissions are rounded to six decimal places as required.

Model-specific transformations have been tested where the scale or distribution justified them, including standardisation and log-like transforms. These are modelling artefacts, not replacements for the raw outcomes. Derived datasets and forecasts are kept separate from the authoritative portal observations.

No conventional class labels are present. Derived fields such as `best_so_far`, `new_best`, forecast error or strategy tag are analytical annotations and should not be confused with original measurements.

## 5. Intended and inappropriate uses

### Intended uses

- sequential black-box optimisation under a small evaluation budget;
- reproducing and auditing the project's query history;
- comparing surrogate and acquisition strategies using only information available at the time;
- studying forecast calibration, exploration/exploitation and model failure on sparse data;
- teaching how an adaptive dataset differs from an independently sampled regression dataset.

### Inappropriate uses

- claiming the complete global shape or global maximum of a hidden function from these observations alone;
- treating the observations as independent and identically distributed;
- using the data as an unbiased general regression benchmark;
- inferring causal feature importance from correlations created by an adaptive query policy;
- assigning true scores to retrospective HEBO, TuRBO or other counterfactual recommendations that were never submitted;
- transferring conclusions directly to a real operational system without new domain validation, constraints and safety analysis.

## 6. Distribution and terms of use

The project is published in this public GitHub repository with the datasheet, model card, code, results and analysis linked from the main README.

The author's own code and documentation may be licensed separately. No blanket licence is asserted here over programme-provided seed data or the hidden objective functions. Redistribution and reuse of course-provided material remain subject to the programme's terms.

There are no personal, demographic or directly identifiable records in this dataset.

## 7. Maintenance and versioning

The dataset is maintained by the project author. Each new portal result is appended rather than overwriting previous history. Observed results, pending queries, prospective forecasts and retrospective analyses are kept as separate evidence classes.

Git commits identify the data cut used by each notebook or report. After the final capstone round, the observation dataset will be frozen; later analytical work should create a new derived version rather than silently altering the historical record.

## 8. Transparency note

The largest risk to interpretation is not a missing cell. It is the data-generating process itself. Because earlier models influenced later queries, the dataset increasingly reflects what the optimiser chose to inspect. A reader should therefore interpret strong local evidence as local evidence, not as proof that unvisited regions are unimportant.
