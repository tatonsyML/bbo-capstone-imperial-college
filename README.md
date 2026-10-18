# Black-Box Optimisation Capstone

Imperial College London — Professional Certificate in Machine Learning and Artificial Intelligence

## Module 21.2 assessment: Datasheet and model card

**Reviewer quick start:** These two linked documents address the full 22-point rubric. They explain the data and model for readers without a technical background, then link to supporting code and evidence.

- **[Datasheet](docs/datasheet.md)** — what data I used, how it was collected and its limitations.
- **[Model card](docs/model_card.md)** — how the optimisation approach works, how it evolved, how it performed and where it remains uncertain.

Supporting material:

- [Decision log](docs/decision_log.md)
- [Project journey](docs/project_journey.md)
- [Module 21.2 assessment copies](submissions/stage_2/module_21/component_21_2/)
- [Round 10 confirmed portal inputs](experiments/round_10/queries.txt)
- [Round 10 revision and external-source audit](reports/round10_revision_audit.md)

## Project in plain English

This project asks a simple question with a difficult constraint: how do you find the best setting when you cannot see the formula and every test is expensive? I optimise eight hidden functions using a small number of experiments. I began with Gaussian-process Bayesian optimisation, then changed the method as evidence accumulated. Some functions responded well to local refinement; others needed broader exploration. I now compare model suggestions with direct experimental patterns and recorded forecasts before deciding what to test next. The repository keeps the data, code, results and decision history together so the progress can be followed from the first query to the current round.

## Progress through Week 9

The project started with 175 programme-supplied observations. Nine completed query rounds added 72 observations, giving **247 observed evaluations**.

| Function | Initial best | Best through Week 9 | Where the current best was found |
|---|---:|---:|---|
| F1 | 7.7109e-16 | 1.9213e-15 | Week 9 |
| F2 | 0.611205 | 0.691315 | Week 6 |
| F3 | -0.034835 | -0.020856 | Week 6 |
| F4 | -4.025542 | 0.658933 | Week 9 |
| F5 | 1088.860 | 6583.561 | Week 9 |
| F6 | -0.714265 | -0.541448 | Week 4 |
| F7 | 1.364968 | 1.786338 | Week 9 |
| F8 | 9.598482 | 9.932443 | Week 9 |

**Round 10 has been submitted and the eight input vectors have been confirmed. Its outputs are still pending.** The submitted inputs are preserved separately and the best-results table above remains based solely on measurements through Week 9. The [revision audit](reports/round10_revision_audit.md) records superseded provisional ideas and explains the provenance and limits of external evidence used to inform some choices.

## What this project shows

**A more sophisticated model does not automatically deserve more trust.** In Week 9, a simple local model forecast the F4 result to within about 1.6 × 10⁻⁹, while the F2 forecast missed by approximately 0.225. The project now compares candidates from different methods, reviews forecasting reliability and chooses experiments for improvement or information value.

The eight functions are not equivalent: F5 has shown nine consecutive measured improvements near a boundary, while F8 supports a 17-coefficient additive quadratic that predicts a score of 10 at an as-yet-unconfirmed Round 10 point. No unreturned score is represented as achieved.

## How the approach evolved

| Phase | Main idea |
|---|---|
| Early rounds | Gaussian-process surrogate models and acquisition functions to balance exploration and exploitation |
| Middle rounds | Function-specific diagnostics, alternative kernels, SVM and small neural-network checks |
| Later rounds | Controlled local experiments, quadratic fits and forecasts recorded before results |
| Current | Evidence-gated decisions: GP, local models, HEBO-inspired and TuRBO-style challengers compete with direct observed patterns |

The important change is that there is no longer one universal rule for all eight functions. Each function earns a different strategy from its own evidence.

## Where to start

If you want the **shortest non-technical route**, read:

1. [Project journey](docs/project_journey.md)
2. [Datasheet](docs/datasheet.md)
3. [Model card](docs/model_card.md)

If you want the **round-by-round history**, use:

- [Stage 2 module archive](submissions/stage_2/modules/README.md)
- [Query experiments](experiments/)

If you want the **technical implementation**, use:

- [Notebooks](notebooks/)
- [Reusable Python code](src/)
- [Reports and result tables](reports/)
- [Tests](tests/)

## Repository map

```text
bbo-capstone-imperial-college/
├── README.md                 ← start here
├── docs/                     ← datasheet, model card, decision log, project journey
├── submissions/              ← module-by-module capstone history
├── experiments/              ← queries, returned outputs and round notes
├── data/                     ← accumulated observation history
├── notebooks/                ← exploratory and model-comparison notebooks
├── reports/                  ← forecasts, current bests and challenger results
├── src/                      ← reusable optimisation code
├── tests/                    ← basic reproducibility checks
└── configs/                  ← optimisation settings
```

## Reproducibility

Core dependencies are listed in [requirements.txt](requirements.txt). Optional advanced optimisation packages are listed in [requirements-advanced.txt](requirements-advanced.txt).

```bash
python -m pip install -r requirements.txt
PYTHONPATH=src python -m bbo.pipeline
python -m pytest -q
```

The repository keeps current project files separate from the module-by-module history so the latest work remains easy to find without losing the development path.
