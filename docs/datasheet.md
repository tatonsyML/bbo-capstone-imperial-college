# Datasheet | Black-Box Optimisation Query History

**Dataset version:** Module 21, observed through Week 9 (18 October 2026 documentation update)  
**Maintainer:** Project author  
**Repository:** https://github.com/tatonsyML/bbo-capstone-imperial-college  
**Important status:** Round 10 inputs have been submitted, but their outputs have not yet been received or added to the observed dataset.

> **In plain English:** This is a record of 247 experiments on eight unknown functions. It shows what settings were tried, what scores came back, and how those results shaped the next experiments. It is a record of a *search*, not a map of every possible outcome.

## 1. Why was this dataset created?

The Imperial College London machine-learning capstone asks participants to **maximise eight hidden numerical functions** with very few opportunities to test new settings. A function takes between two and eight numerical inputs and returns one score. Higher scores are better; the formula is hidden.

The dataset supports three tasks:

1. **Optimisation:** Learn from earlier evaluations and select the next promising input.
2. **Evaluation:** Measure whether each new query improved the best score and whether predictions were reliable.
3. **Accountability:** Make it possible to inspect why a particular point was chosen, including mistakes and changes of strategy.

The course supplied the starting input/output observations and the evaluation portal. I selected the subsequent queries and recorded the responses. I do not claim to have generated the original data or to know the hidden function definitions.

## 2. What is in the dataset?

One **observation** is one input vector (the settings sent to a function) paired with the scalar score returned by the portal. The eight functions must be analysed separately: their dimensions and output scales differ.

| Function | Input variables | Course starting observations | Completed personal queries | Observed total |
|---|---:|---:|---:|---:|
| F1 | 2 | 10 | 9 | 19 |
| F2 | 2 | 10 | 9 | 19 |
| F3 | 3 | 15 | 9 | 24 |
| F4 | 4 | 30 | 9 | 39 |
| F5 | 4 | 20 | 9 | 29 |
| F6 | 5 | 20 | 9 | 29 |
| F7 | 6 | 30 | 9 | 39 |
| F8 | 8 | 40 | 9 | 49 |
| **Total** | | **175** | **72** | **247** |

**Current observation cut:** Nine completed additional evaluations for each function. The eight Round 10 coordinate strings are **submitted queries without returned scores** and must not be counted as eight further observations.

### Format and fields

- **Initial source:** paired NumPy files (initial_inputs.npy and initial_outputs.npy), supplied through the programme.
- **Public working history:** chronological CSV files in **data/accumulated/function_1/** through **function_8/**, each named **observations_through_week9.csv**.
- **Columns:** function, stage, sequence_in_stage, is_initial, x1 ... xD, output. The stage separates the initial course sample from Weeks 1–9.
- **Round evidence:** submitted query strings, returned portal values and notes in **experiments/round_01/** through **round_09/**.
- **Calculated summaries:** best values, forecast errors and challenger proposals in **reports/**. These are *derived analysis*, not new portal observations.

Input coordinates are bounded between **0.000000 and 0.999999**. Submitted queries contain exactly six decimal places per coordinate. Starting inputs may contain more precision; do not silently round them when reproducing an earlier fit. Scores are real numbers and can be negative or extremely small.

The public repository preserves the derived numerical history but does **not** redistribute the original course-provided binary arrays pending confirmation of redistribution rights. Anyone requiring byte-for-byte reconstruction of the initial source must obtain those files through an authorised programme route.

### What is missing, and what is biased?

There are no known missing score fields in the completed CSV records. But **complete records do not mean complete coverage**:

- **F1:** Outputs have extreme magnitude differences, with most readings too close to zero to reveal a useful gradient.
- **F2:** Results have been difficult to predict consistently; the available evidence does not establish whether variation is observation noise, rapidly changing local behaviour or both.
- **F3:** Repeated searches around an earlier promising region produced limited further progress. Competing regions remain weakly sampled.
- **F4 and F7:** Small steps around successful points yield excellent *local* detail while leaving other regions relatively unexplored.
- **F5:** The later observations concentrate near the upper boundary, not across the full four-dimensional domain.
- **F6:** The incumbent neighbourhood remains difficult to model reliably.
- **F8:** Forty-nine points are still sparse in eight dimensions, even where a simple mathematical pattern fits exceptionally well.

There is no independently measured global optimum, no comprehensive repeat-measurement programme to identify noise, and no observed outcomes for unsubmitted HEBO, TuRBO or other counterfactual candidates.

## 3. How and when were the observations collected?

The programme provided 175 starting evaluations. Across **Modules 12–20**, I made one new submission per function each round, collected its returned score and appended it to that function's history. **Module 21 / Round 10** represents the next submitted query set, still awaiting scores.

Later queries were **not random draws**. They were chosen using everything already learnt, then reviewed before submission:

| Project phase | Selection approach | Why it changed |
|---|---|---|
| Early rounds | Gaussian Processes (GPs) with Expected Improvement or Upper Confidence Bound | Balance promising predictions against exploration of uncertain areas |
| Middle rounds | Alternative kernels, diagnostic models, regional search and controlled one-coordinate changes | A single modelling rule did not work equally well across all eight functions |
| Weeks 7–9 | Cross-validation, forecasts written before results and local polynomial fitting | Reward models whose predictions actually worked; challenge those that failed |
| Round 10 decision | HEBO-inspired acquisition comparisons, TuRBO-style local challenger and polynomial structure, with human evidence review | Choose the next experiment by credible gain **or** the information it would provide |

**HEBO-inspired** means I compare candidate recommendations from multiple GP kernels and acquisition criteria. **TuRBO-style** means I search in a restricted area around a promising result. The code implements educational adaptations rather than the complete published algorithms.

The human selection step is part of the collection process: a more complex algorithm was not automatically preferred over a simpler model backed by better experimental evidence.

## 4. What preparation or transformations were applied?

The **authoritative history keeps the actual portal outputs**. No score is replaced with a fitted or transformed value, and unsuccessful queries remain in the record.

- Inputs are already on the programme's common zero-to-one scale.
- Model fitting sometimes uses standardisation, Yeo–Johnson or signed-log-like transformations to handle difficult score scales. These are temporary model inputs, **not edits to the saved outcomes**.
- Polynomial coefficients, surrogate forecasts, uncertainty values and labels such as *new best* are computed from the observations and kept in separate reports.
- Proposals are clipped to legal bounds and formatted to six decimal places **before submission**.
- Modelling experiments and peer-informed tests are distinguished from the participant's own portal-returned observations.

**Additional provenance:** Supplementary retrospective research compared this history against publicly shared classmates' query/output records. Those peer observations were used as **external research evidence**, not inserted into my 247-row dataset or mislabelled as my own results. Some revised Round 10 candidates were informed by this research. The public sources include the repositories of [Rishin Mitra](https://github.com/mitrarishinoracleace/AIML), [Andreia Bilé-Silva](https://github.com/andreia-bs/Capstone-project), [Ugo Isiocha](https://github.com/u-isiocha/Capstone) and [Hilton Patel](https://github.com/HP014/Machine-Learning-Capstone-Project). The use of evaluated peer outcomes for assessed work remains subject to programme collaboration rules; publicly readable data is not automatically unrestricted for reuse.

## 5. Intended uses and uses to avoid

**Appropriate:** Replaying completed rounds; teaching sequential Bayesian optimisation; comparing candidate-selection strategies without future-data leakage; inspecting prediction failures; and examining how sparse, adaptively collected evidence shapes decisions.

**Inappropriate:** Treating these points as an unbiased statistical survey; claiming a global maximum or complete function formula; comparing raw scores across functions with different scales; inferring cause from correlations where several settings changed together; treating untested recommendations as successful experiments; or transferring the method to safety-critical operations without new validation.

**Why the distinction matters:** A dataset containing many observations near one peak describes that area well. It says little about a distant region that was never tested.

## 6. Where is it available, and under what terms?

- **Repository:** https://github.com/tatonsyML/bbo-capstone-imperial-college
- **Working data:** [data/accumulated/](../data/accumulated/)
- **Round records:** [experiments/](../experiments/)
- **Model card:** [docs/model_card.md](model_card.md)
- **Decision log:** [docs/decision_log.md](decision_log.md)

The repository is shared for educational review. **No blanket open-source licence is asserted for the programme's starting data, objective functions or any third-party observations.** Permissions to redistribute or reuse those assets must be checked with their respective rights holders. The repository does not presently declare a general licence for its contents.

There are no personal, demographic or directly identifying records; privacy and group fairness are therefore not directly evaluated in this synthetic dataset.

## 7. Who maintains it, and how will it change?

The project author maintains the dataset and the accompanying decision records. When Round 10 scores arrive, they should be appended as eight **new observations**, preserving the earlier rows. Reports and the model card should then be versioned to show the new observation cut.

Versioning should always distinguish: **observed results**, **pre-result forecasts**, **retrospective comparisons**, and **interpretation after results**. The same input cannot have both an unobserved predicted score and a claimed actual score.

## 8. What a reviewer should remember

**The greatest risk is not a missing CSV value; it is mistaking an intelligently selected search history for unbiased evidence about the entire search space.** This datasheet records both what the project learnt and where it still has no reliable information.
