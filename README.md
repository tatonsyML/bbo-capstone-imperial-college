# Black-box optimisation · Eight functions, thirteen decisions each

**An Imperial College London Machine Learning & AI capstone, presented as an open, reproducible learning project.**

[![Python tests](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/core-tests.yml/badge.svg)](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/core-tests.yml)

**8 functions** · **2–8 inputs** · **13 rounds** · **279 actual observations**

> How do you choose your next experiment when the formula is hidden and every evaluation matters?

## The project in plain English

I tried to find the best settings for eight unknown mathematical functions. Each function accepts between two and eight numbers and returns a score. I could test only one new setting per function in each round. I began with machine-learning models that estimated useful settings and their uncertainty. As results arrived, I checked their predictions, investigated different regions and tested simpler mathematical explanations. Some apparently excellent predictions led to poor decisions; a few mathematical reconstructions were more useful than another complicated model. This repository shows what I tried, what happened, what failed and how my choices changed across thirteen rounds.

## Choose a function and follow its story

Each function page starts with its observed behaviour, final result and **measured progress chart**. Open any of the **13 expandable weekly sections** to see the original reasoning, actual inputs and outputs, forecasts where recorded, code evidence and subsequent lessons. Each page finishes with two visualisations and the strength or limits of its mathematical reconstruction.

| Function | Inputs | Best observed score | First achieved | Central lesson |
|:--|--:|--:|:--:|---|
| **[F1](functions/F1/README.md)** | 2 | **1.999999999676** | R11 | Near-zero responses concealed useful structure |
| **[F2](functions/F2/README.md)** | 2 | **0.744250426302** | R13 | A confident local forecast missed badly |
| **[F3](functions/F3/README.md)** | 3 | **−0.003753096919** | R13 | Alternative regions beat brittle local fits |
| **[F4](functions/F4/README.md)** | 4 | **0.746897911381** | R13 | An accurate prediction was not a good search |
| **[F5](functions/F5/README.md)** | 4 | **8,662.405001** | R10 | Controlled experiments exposed a strong boundary |
| **[F6](functions/F6/README.md)** | 5 | **−0.037518647244** | R12 | Nearby points did not always behave smoothly |
| **[F7](functions/F7/README.md)** | 6 | **3.322368011393** | R12 | A pre-result structural forecast succeeded |
| **[F8](functions/F8/README.md)** | 8 | **10.000000** | R10 | A quadratic turned searching into solving |

[**Browse the full function index**](functions/README.md)

![Eight best-so-far score histories, each plotted on its own scale](results/figures/progress.svg)

*The panels have different vertical scales. Each curve shows best **measured** score so far, including the original observations.*

## Three turning points

**F2 — Challenge the forecast.** A local model predicted **0.730502** but returned **0.505526**. Instead of assuming convergence, a later query tested a competing region and returned **0.744250**.

**F4 — Challenge the search.** Predictions were accurate to around **1.6 × 10⁻⁹**, yet micro-steps kept the score near 0.659. A wider local step reached **0.730459**, with a further improvement to **0.746898**.

**F8 — Challenge the model.** An additive quadratic with **17 coefficients** identified a maximum of **10**, confirmed by the portal. Fitting the same form to just the initial 40 observations in a separate retrospective test reproduced all later returns to floating-point precision. This supports the reconstructed model, not an assertion that the hidden source code has been recovered.

## Reproduce the results

Python 3.11 is recommended. From the repository root:

```bash
python -m pip install -r requirements-notebook.txt
python -m pytest -q
jupyter notebook notebooks/Capstone_Final_Walkthrough.ipynb
```

The [executable notebook](notebooks/Capstone_Final_Walkthrough.ipynb) reproduces the main data checks and mathematical validations. The [source modules](src/bbo/README.md) and [methods guide](docs/methods.md) explain the GP, acquisition functions and later challengers. Retrospective code is **never** presented as the unrecorded generator of an original query.

## Data, evidence and history

| Start here | What's inside |
|---|---|
| [Function stories](functions/README.md) | The main reading experience, one function through 13 rounds |
| [Complete observations](data/all_observations.csv) | **175 original** and **104 personal portal** input/output records, repeats retained |
| [Historical round archive](journey/README.md) | Original code, notes and outputs organised by week |
| [Datasheet](DATASHEET.md) · [Model card](MODEL_CARD.md) | Data provenance, model choices, limitations and validation |
| [Charts and their meanings](docs/functions.md) | Which plots show measured points and which show model slices |
| [Older material and supplementary work](archive/README.md) | Historical snapshots and documents kept out of the main path |

**Evidence matters.** The original weekly reflections establish what was intended. The portal returns establish what was submitted and measured. Some scripts or forecasts are missing, and later structural explanations are marked as retrospective. External published points are separately attributed and are not counted among my 104 returns.

**Data rights:** Course-supplied observations are included in the current public dataset. Permission to redistribute them has not been independently verified; see [usage and permissions](USAGE_AND_PERMISSIONS.md) before reusing those values.

Questions, corrections and reproduction findings are welcome through [GitHub Issues](https://github.com/tatonsyML/bbo-capstone-imperial-college/issues).
