# Black-Box Optimisation: Learning to Make Better Decisions

**Imperial College London · Professional Certificate in Machine Learning and Artificial Intelligence**

[![Core Python tests](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/core-tests.yml/badge.svg)](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/core-tests.yml)

**8 hidden functions** · **2–8 input dimensions** · **13 completed rounds** · **279 recorded evaluations**

> **The question:** With only one evaluation per function per round, how do you decide which experiment is worth running next?

This project documents an evidence-led black-box optimisation capstone. I started with Gaussian-process-based Bayesian optimisation, tested alternative models and acquisition rules, and eventually used mathematical reconstruction where the observations supported it. The central result is not a single winning algorithm: **predicting a point accurately, searching the right region and understanding the underlying structure are different achievements.**

**Final evidence status (9 November 2026):** 175 course-provided initial observations plus 104 returned personal evaluations (13 rounds × eight functions) = **279 records**, including repeats. All eight final outputs have been verified.

## For assessors: Component 25.3

The **[five-criterion assessment checklist](docs/assessment_25_3.md)** is the best place to start. It links each required item to the precise file and explains how to reproduce the evidence.

| Rubric criterion | Direct evidence |
|---|---|
| Clear, commented, runnable code and reproducible results | **[Final Jupyter walkthrough](notebooks/Capstone_Final_Walkthrough.ipynb)** · [run instructions](docs/assessment_25_3.md#how-to-reproduce) · [CI checks](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/core-tests.yml) |
| Complete datasheet | **[Final datasheet](DATASHEET.md)** |
| Complete model card | **[Final model card](MODEL_CARD.md)** |
| Approximately 100-word non-technical explanation | [Read below](#the-project-in-about-100-words) |
| Organised, complete and linked repository | [Assessment map](docs/assessment_25_3.md) · [data index](data/README.md) · [visual gallery](docs/visual_gallery.md) |

## The project in about 100 words

This project searches for the best settings of eight hidden functions. Each takes between two and eight numbers, but its formula is unknown. I had one query per function in each round, so every experiment mattered. I began with a statistical model to estimate promising settings and how uncertain those predictions were, then compared its suggestions with controlled tests and simpler formulas. Across 13 rounds I recorded 104 returned queries alongside 175 starting observations. My final round improved three functions. For Function 8, a simple formula fitted to 40 original observations predicted all 13 later scores almost exactly. This repository documents the decisions, results, code and limitations.

## Results at a glance

![Cumulative best scores for F1 to F8, each on its own scale](results/figures/progress.svg)

The diagram tracks the **best observed score so far** from the initial data to Round 13. **Each tile has a separate vertical scale**: it shows *progress*, not a valid numerical comparison between functions.

| Function | Inputs | Initial best | Final best through R13 | First attained | Evidence |
|:--|--:|--:|--:|:--:|:--|
| [F1](docs/function_guide.md#f1--finding-a-narrow-signal) | 2 | 7.71 × 10⁻¹⁶ | **1.999999999676** | R11 | Portal |
| [F2](docs/function_guide.md#f2--an-unreliable-local-forecast) | 2 | 0.611205 | **0.744250** | R13 | Portal |
| [F3](docs/function_guide.md#f3--improving-a-negative-valued-objective) | 3 | −0.034835 | **−0.003753** | R13 | Portal |
| [F4](docs/function_guide.md#f4--accurate-prediction-poor-search) | 4 | −4.025542 | **0.746898** | R13 | Portal |
| [F5](docs/function_guide.md#f5--the-feasible-boundary) | 4 | 1,088.860 | **8,662.405** | R10 | Portal |
| [F6](docs/function_guide.md#f6--challenging-unstable-local-models) | 5 | −0.714265 | **−0.037519** | R12 | Portal |
| [F7](docs/function_guide.md#f7--a-structural-forecast-confirmed) | 6 | 1.364968 | **3.322368** | R12 | Portal |
| [F8](docs/function_guide.md#f8--the-17-coefficient-quadratic) | 8 | 9.598482 | **10.000000** | R10 | Portal |

The final round established **three additional personal bests**: F2, F3 and F4. The other five were first achieved in R10–R12. These are best-so-far observations, not one-round scores. Their scales differ and must not be added or averaged.

[Final bests and inputs (CSV)](results/current_best_after_week13.csv) · [Round 13 portal returns](data/portal_rounds_13.csv) · [Final-round evidence](docs/round13_evidence.md)

## Visualise the eight functions

The **[2D and 3D gallery](docs/visual_gallery.md)** includes reconstructed mathematical slices for F5, F7 and F8, and actual observation-only plots for F1, F2, F3, F4 and F6. Each function has a plain-English explanation of its characteristics and the remaining uncertainty.

<table><tr>
<td width="50%"><a href="docs/visual_gallery.md#f8-a-testable-additive-quadratic"><img src="results/figures/f8_3d.svg" width="450" alt="F8 reconstructed quadratic surface, x3 and x8 varied"></a><p><strong>F8:</strong> documented model slice</p></td>
<td width="50%"><a href="docs/visual_gallery.md#f2-a-different-region-succeeds"><img src="results/figures/f2_2d.svg" width="450" alt="F2 observed input positions, no invented surface"></a><p><strong>F2:</strong> measured observations only</p></td>
</tr></table>

[Explore all eight functions](docs/visual_gallery.md) · [Rebuild the graphics](results/figures/build_visual_gallery.mjs)

## Three discoveries worth reading

**Final-round update:** F2 **0.695337 → 0.744250**; F3 **−0.005709 → −0.003753**; F4 **0.730459 → 0.746898**. [Read the R13 result audit](docs/round13_evidence.md).

**1. A failed forecast does not prove convergence (F2).** A prediction of **0.730502** returned **0.505526**, but a different R13 region subsequently returned **0.744250**. Model trust and search coverage must be checked separately.

**2. An accurate forecast can still lead to the wrong decision (F4).** A local prediction missed by only about **1.6 × 10⁻⁹**, yet microscopic steps kept the search near **0.659**. A wider R11 move returned **0.730459**, followed by another improvement to **0.746898** in R13.

**3. The simplest suitable model can outperform further search (F8).** A fitted **17-coefficient additive quadratic** identified an interior vertex with value **10**. A *separate retrospective check* fitted that model to **only 40 starting observations** and predicted the next **13 personal portal returns** to numerical precision. The fit from only the starting data was performed *after* the optimisation, not during Round 1.

[Read the complete case studies](docs/function_guide.md) · [Read the evidence and chronology](docs/round12_evidence.md)

## Data, model and optimisation settings

**Data:** The complete dataset has **279 rows and is about 40 KB**, so it is stored directly in this repository. No large datasets are hosted here. [Data guide](data/README.md) · [Final datasheet](DATASHEET.md).

**Model:** Gaussian Process models with RBF or Matérn kernels, compared with simpler fitted equations where appropriate. [Model card](MODEL_CARD.md).

**Hyperparameter optimisation:** The GP code compares RBF and Matérn 1.5/2.5 kernels, with one lengthscale per input (ARD) and a WhiteKernel noise term. It fits GP parameters by marginal likelihood (four optimiser restarts by default), and supports Yeo–Johnson or signed-log output transformations. Candidate scoring includes UCB with β = 1.96 and Expected Improvement with ξ = 0; the historical TuRBO-style challenger uses a fixed 0.20-width local box. The short notebook demonstration uses zero restarts to execute quickly. [Code and algorithm explanation](docs/optimisation_algorithms.md).

**Contact:** [Open a GitHub issue](https://github.com/tatonsyML/bbo-capstone-imperial-college/issues) for questions about reproducibility.

## Methods, in one view

| Approach | Role in this project | Lesson |
|---|---|---|
| GP with RBF/Matérn kernels and ARD | Baseline predictions, uncertainty and local comparisons | Validate unseen predictions, not just training fit |
| EI, UCB and local probes | Query selection and exploration–exploitation choices | Search width matters as much as acquisition settings |
| Small neural-network and polynomial challengers | Test whether the GP representation remains suitable | More complex is not always better |
| HEBO-inspired committees and TuRBO-style trust regions | Original lightweight challenger mechanisms | **Not full official algorithms; see separate post-capstone benchmark** |
| Structural reconstruction on F1/F5/F7/F8 | Explain observed patterns and propose justified test points | Distinguish prospective successes from retrospective explanations |

[Algorithm and source-code guide](docs/optimisation_algorithms.md) · [Approach and validation](docs/strategy_and_validation.md) · [Mathematical evidence](docs/structural_reconstruction.md) · [Decision record](docs/decision_log.md)

## Source code and algorithm comparison

For the instructor, start with the **[annotated optimisation code guide](docs/optimisation_algorithms.md)**. It explains the original GP/EI/UCB pipeline, the **HEBO-inspired versus official HEBO** distinction, the original **TuRBO-style versus full TuRBO-1** distinction, and why a fair comparison is not the same as claiming a better portal score.

The [post-capstone HEBO and TuRBO-1 benchmark](research/full_optimisers/README.md) provides commented source and tests for an **equal-budget simulation on the F8 reconstructed quadratic**. The optional full-algorithm comparison has not yet been run, so no simulated comparison scores are claimed.

[Historical source](src/bbo/README.md) · [Reference comparison source](research/full_optimisers/benchmark.py) · [Reproduction guide](docs/reproduce.md)

## Reproduce the strongest reproducible result

The checked experiment fits the F8 quadratic using **40 initial observations only**, tests its predictions against **13 later portal returns**, and verifies the F5 permitted-corner value.

```bash
python -m pip install -r requirements.txt
PYTHONPATH=src python -m bbo.structural_validation
PYTHONPATH=src python -m pytest -q
```

Run these commands from the repository root in a Unix-like shell. See [reproduction and scope](docs/reproduce.md) for the expected output, other platforms and the distinction between executable tests and archived exploratory work.

## Where everything lives

```text
README.md                 Project overview and non-technical introduction
DATASHEET.md              Final description of the dataset and its limitations
MODEL_CARD.md             Final explanation of the models, decisions and evidence
USAGE_AND_PERMISSIONS.md  Data provenance and reuse information
requirements.txt          Core Python dependencies
requirements-notebook.txt Notebook and Jupyter dependencies
requirements-advanced.txt Historical optional dependencies (not the benchmark env)
pyproject.toml            Plain pytest configuration
assets/                   Data-derived progress visual
configs/                  Historical optimisation settings
data/                     Complete observations and historical records
docs/                     Assessor guide, methods and detailed evidence
experiments/              Queries, outputs and notes for all 13 rounds
notebooks/                Executed final notebook and earlier explorations
results/                  Verified results, plots and forecast audits
scripts/                  Reproduce scientific plots and check links
src/bbo/                  Commented optimisation code and validation
benchmarks/               Optional post-capstone HEBO/TuRBO comparison (unrun)
submissions/              Preserved Stage 1 and Stage 2 coursework
tests/                    Automated checks
```

[Assessment checklist](docs/assessment_25_3.md) · [Full documentation index](docs/README.md) · [Visual gallery](docs/visual_gallery.md) · [Reports index](results/README.md) · [Assessment archive](submissions/README.md)

## Limitations and responsible interpretation

**Usage and data permissions:** [Read the publication and course-data statement](USAGE_AND_PERMISSIONS.md). Original course-supplied numeric observations are already included in public CSVs; redistribution permission requires confirmation.


- **Not every equation is solved.** F1, F5, F7 and F8 have supported reconstructed forms, with different evidence strengths; F2, F3, F4 and F6 remain unresolved.
- **Source matters.** Course-supplied starting observations, personal portal returns, prospective predictions, retrospective analysis and external published observations are not interchangeable. The [final datasheet](DATASHEET.md) states that the 175 course-supplied numerical values are already in public CSV files, pending a redistribution-permission check. External results informed some choices but do not count as my personal evaluations.
- **History is not overwritten.** Early model cards, submissions and notebooks are dated snapshots and can contain statements that were correct when written but are superseded by later returns.
- **Known gaps are visible.** The exact Round 11 F7 input is missing from the retained log. Round 13 outcomes are verified. The GP pipeline demonstration uses an earlier data cut, not the complete 13-round history.

[Data provenance](docs/evidence_provenance.md) · [Evidence limitations](docs/round12_evidence.md) · [Reproduction scope](docs/reproduce.md)

---

*Project focus: learn how to select, validate and explain the next expensive experiment, not only how to maximise a score.*
