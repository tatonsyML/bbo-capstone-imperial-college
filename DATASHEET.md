# Dataset Datasheet | Black-Box Optimisation Capstone

*Imperial College London · Professional Certificate in Machine Learning and Artificial Intelligence*

This datasheet documents the **279 observed input/output pairs** used during the thirteen-round capstone, completed in November 2026: **175 course-provided starting observations** and **104 personal portal evaluations**. It explains their origin, collection, preparation, limitations, performance and permissible use.

The supplied Module 25 datasheet template asks for answers **for each function**, not solely for the dataset as a whole. Those answers are provided in the [eight function-specific datasheets](docs/function_datasheets.md), covering function overview, data behaviour, strategy, preprocessing, weekly learning, results and practical implications. No unverified real-world meaning is assigned to the anonymous objectives.

[← Project home](README.md) · [Complete data CSV](data/all_observations.csv) · [Function-specific datasheets](docs/function_datasheets.md) · [Model card](MODEL_CARD.md)

## 1. Motivation and purpose

This dataset supports a sequential black-box optimisation exercise: select one input vector for each of eight hidden functions per round, observe a numeric score, and maximise the best observed output with few evaluations. The initial samples were supplied by the programme; the 13 later rounds of personal portal returns were submitted by the project author.

It is a historical record of *observed evaluations*, not a dataset of the true functions over their full domains.

## 2. Composition and fields

**279 recorded rows:** 175 course-provided initial observations and **104 personal portal evaluations** (13 rounds × 8 functions). The input dimensions are 2, 2, 3, 4, 4, 5, 6 and 8 for F1–F8 respectively.

| Field | Meaning |
|---|---|
| `function` | Function identifier, 1–8 |
| `round` | 0 for the supplied initial observations; 1–13 for personal queries |
| `stage` | Original source label, such as `Initial` or `Week 13` |
| `source`, `is_initial` | Distinguish course data from personally submitted queries |
| `sequence_in_stage` | Original ordering within the source stage |
| `input_status` | Status of the recorded inputs (all currently `confirmed`) |
| `x1`–`x8` | Input coordinates. Unused coordinates are blank for functions with fewer dimensions |
| `output` | Returned scalar score, preserving source precision where available |

All 279 recorded evaluations have their input coordinates and measured outputs. No synthetic results have been added.

## 3. Collection process and timing

The programme supplied 175 initial input/output pairs, then the author submitted one new query for each function in each of 13 rounds. The portal returned eight responses per round. The consolidated CSV combines the [per-function history through R10](data/accumulated/), [R11–12 returns](data/portal_rounds_11_12.csv) and [R13 returns](data/portal_rounds_13.csv). Duplicate query locations are retained because they represent actual evaluations.

## 4. Preparation and transformations

The CSV is a tidy union of already recorded numeric outputs, with provenance columns and unused dimensions left empty. It does **not** normalise response values, replace missing inputs or deduplicate repeated portal queries.

The working GP pipeline optionally applies Yeo–Johnson or signed-log transformations, and some visualisations use log-labelled scales. Those are *analysis and display choices*, not changes to the original `output` column.

## 5. Performance and results

The project records **279 outputs** in total: 175 starting observations and 104 personal portal returns. The final observed maxima are summarised below. Different functions have different scales; these values are not combined into one score.

| Function | Final personal best | First reached |
|---|---:|---|
| F1 | 1.9999999996761817 | R11 |
| F2 | 0.7442504263021256 | R13 |
| F3 | −0.0037530969187192596 | R13 |
| F4 | 0.7468979113807426 | R13 |
| F5 | 8662.405001248297 | R10 |
| F6 | −0.03751864724436928 | R12 |
| F7 | 3.3223680113931557 | R12 |
| F8 | 10 | R10 |

Each function-specific record also states its **best input vector**, initial NumPy array dimensions, observed behaviour, evidence for or against repeatability and limits on confidence in the global maximum. See the [eight function-specific datasheets](docs/function_datasheets.md).

## 6. Weekly iteration and learning

One personally submitted evaluation per function was returned in each of **13 rounds**. The [round archive](journey/README.md) records actual inputs and outputs; the [project journey](archive/notes/early_project_timeline.md) explains how the search policy changed. Early rounds used GP and UCB/EI suggestions, later rounds included controlled probes and structural hypotheses, and the final round improved F2, F3 and F4. Retrospective explanations are labelled rather than passed off as pre-submission predictions.

## 7. Biases, limitations and appropriate use

Initial samples are sparse in high dimensions; later queries were selected adaptively and favour regions already thought promising. The result is **not a uniform representative sample** of each function. F1 contains extremely small outputs, F5 has a large response scale, and some series cluster strongly near incumbents. Cross-function raw scores cannot sensibly be averaged.

**Appropriate:** learning GP optimisation, studying candidate-selection decisions, reproducing historical bests, testing simple surrogate hypotheses and evaluating held-out prediction.

**Inappropriate:** claiming a global optimum for unresolved functions, fitting the F8 model to all 53 points and calling the later 13 independent validation, or attributing peers' results to this participant. Chronological model-selection tests must avoid future-information leakage.

## 8. Distribution, permissions and privacy

Stage 2, required final capstone submission **25.3**, instructs participants to submit a **public GitHub repository** containing or linking to project data, code and presentation materials, with large datasets hosted externally. The **175 course-provided starting observations** are included as numerical evidence within the approximately 40 KB, 279-row dataset. The original `.npy` files are **not hosted here**. This publication follows the course's capstone-submission instructions; it does not grant unrestricted third-party redistribution or commercial reuse rights over programme-supplied data. See [usage and permissions](USAGE_AND_PERMISSIONS.md).

The dataset contains no reported personal identifiers or health records. The 175 supplied starting observations and 104 personally returned queries have separate source flags. External observations used as research evidence are **not** included among these 279 rows. [Data-use and redistribution statement](USAGE_AND_PERMISSIONS.md).

### Research context

Some model equations were fitted after the portal evaluations and are presented as later analyses. For F8, the 17-coefficient quadratic was subsequently fitted to just the 40 original course observations and tested against 13 later portal returns. This is a retrospective model test, not an additional portal experiment.

External observations mentioned in the research notes were not included in the 279-row dataset. Measured scores and model predictions are identified separately in the [function investigations](functions/README.md).

## 9. Reproducing the analysis

The [full CSV](data/all_observations.csv) is the final complete record. The [Jupyter walkthrough](notebooks/Capstone_Final_Walkthrough.ipynb) verifies counts, chronology, final bests and the F5/F8 structural checks. [Automated tests](tests/) and [GitHub Actions](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/core-tests.yml) provide independent verification.

[← Project home](README.md)
