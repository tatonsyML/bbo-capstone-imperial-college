# Black-Box Optimisation

**Eight unknown functions. Thirteen rounds. An evolving approach to making better decisions under uncertainty.**

**Black-Box Optimisation capstone · Imperial College London's [25-week Professional Certificate in Machine Learning and Artificial Intelligence](https://www.imperial.ac.uk/lifelong-learning/courses/professional-certificate-ml-and-ai/)**

[![Python tests](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/core-tests.yml/badge.svg)](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/core-tests.yml) · [MIT Licence](LICENSE) · [Reuse and attribution](USAGE_AND_PERMISSIONS.md)

**8 functions** · **2–8 input dimensions** · **13 rounds** · **279 recorded observations**

## The project

I set out to maximise eight unknown mathematical functions. Each function accepted between two and eight numerical inputs, with each value ranging from **0.000000 to 0.999999 (six decimal places)**, and returned a single score.

I could evaluate each function **only once per round**. With no access to the underlying equations and a limited number of evaluations, I needed to decide where to explore, when to exploit promising regions and how much confidence to place in model predictions.

I began by examining the supplied observations and choosing function-specific exploratory inputs. I then introduced Gaussian Process models and acquisition functions, compared alternative models, tested controlled changes and investigated mathematical structure. As the evidence grew, I adapted the strategy to each function rather than forcing one method across all eight.

This repository documents **what I tried, what worked, what failed and how my reasoning evolved across thirteen rounds**. It brings together the submissions, observed results, Python code, model comparisons, visualisations and subsequent mathematical investigations.

## Why black-box optimisation matters

Black-box optimisation (BBO) addresses problems where the relationship between inputs and outcomes is unknown, difficult to model or expensive to evaluate. Every experiment provides information, but experiments cost time, money or a limited evaluation budget.

Real-world applications include **engineering design**, **machine-learning hyperparameter tuning**, **manufacturing process optimisation** and **scientific experiments**. In each case, the aim is to identify better settings without exhaustively testing every possible combination.

BBO balances **exploration** (learning about uncertain regions) with **exploitation** (improving the best solution found so far). This project examines how that balance changes when predictions succeed, fail or reveal new structure.

## Explore the research

**Suggested reading order:** Start with the [eight function results](functions/README.md), follow the [thirteen-round methodology and decisions](journey/README.md), then examine the [recorded evidence and reproducible notebook](notebooks/README.md). The [complete observations](data/all_observations.csv) are available for independent checks.

| Start here | What you will find |
|---|---|
| **[Eight function investigations](functions/README.md)** | Each function's behaviour, decisions, results, progress and mathematical evidence |
| **[Thirteen-round journey](journey/README.md)** | How the strategy evolved, with submitted inputs, actual returns and surviving code |
| **[Methods and experiments](docs/methods.md)** | Gaussian Processes, acquisition functions, model comparisons, local search and alternatives |
| **[Run the final notebook](notebooks/Capstone_Final_Walkthrough.ipynb)** | Reproducible analyses, numerical checks and working optimisation examples |

[Mathematical reconstructions](docs/reconstruction.md) · [Visual gallery](docs/visualisations.md) · [Complete observations](data/all_observations.csv)

## Eight functions, eight investigations

| Function | Inputs | Best measured score | First reached | Main finding |
|---|---:|---:|:---:|---|
| **[F1 · Finding the signal](functions/F1/README.md)** | 2 | **1.999999999676** | R11 | Near-zero observations concealed two narrow, valuable regions |
| **[F2 · Challenging the forecast](functions/F2/README.md)** | 2 | **0.744250426302** | R13 | Confident local forecasts did not always hold |
| **[F3 · Brittle local peaks](functions/F3/README.md)** | 3 | **−0.003753096919** | R13 | Exploring alternative regions improved the final result |
| **[F4 · Accuracy versus progress](functions/F4/README.md)** | 4 | **0.746897911381** | R13 | Tiny prediction errors did not guarantee useful search steps |
| **[F5 · Towards the boundary](functions/F5/README.md)** | 4 | **8,662.405001** | R10 | Controlled tests revealed a productive boundary |
| **[F6 · Unstable local behaviour](functions/F6/README.md)** | 5 | **−0.037518647244** | R12 | Local models needed stronger robustness checks |
| **[F7 · From local to structural](functions/F7/README.md)** | 6 | **3.322368011393** | R12 | A structural hypothesis supported a testable improvement |
| **[F8 · Understanding the quadratic](functions/F8/README.md)** | 8 | **10.000000** | R10 | A simple mathematical model identified the optimum |

![Best measured score so far across all eight functions](results/figures/progress.svg)

*These curves use recorded evaluations, including the initial observations. Each function has its own vertical scale; the lines are not model predictions.*

## How the approach evolved

| Rounds | Focus | What changed |
|---|---|---|
| **[1–3](journey/round_01/README.md)** | Exploration, GP/UCB and function-specific acquisition rules | I moved beyond a uniform search policy |
| **[4–6](journey/round_04/README.md)** | Alternative models, neural-network diagnostics and controlled experiments | More complexity did not automatically mean better predictions |
| **[7–9](journey/round_07/README.md)** | Model calibration, forecast checks and local search | I separated prediction accuracy from decision quality |
| **[10–13](journey/round_10/README.md)** | Boundary tests, structural hypotheses and targeted final queries | Mathematical insight increasingly guided where to search |

The [full chronological record](journey/README.md) shows what I knew before each query, what I submitted, what the portal returned and how the result influenced the next decision.

## What the experiments taught me

**A good prediction is not necessarily a good decision.** For F4, extremely accurate local predictions produced little improvement until I widened the search.

**Simple explanations sometimes outperform elaborate models.** For F8, an additive quadratic explained the observed behaviour and identified an input returning the maximum score of **10**.

**The best strategy depends on the function.** Narrow peaks, boundaries, interacting coordinates and unstable local behaviour required different methods and different levels of exploration.

Some equations were investigated or validated **after** the relevant portal submissions. The [reconstruction guide](docs/reconstruction.md) distinguishes these later analyses from forecasts made during the challenge. The [executed official HEBO and TuRBO-1 comparison](research/full_optimisers/README.md#executed-f8-model-only-comparison--12-november-2026) uses **post-capstone simulated F8 feedback**, not new portal evaluations.

## Run the research

Python **3.11** is recommended. From the repository root:

```bash
python -m pip install -r requirements-notebook.txt
python -m pytest -q
jupyter lab notebooks/Capstone_Final_Walkthrough.ipynb
```

The notebook reproduces supported analyses and demonstrates optimisation methods. It does **not** claim to regenerate every original candidate choice where the historical selection code is unavailable.

[Notebook instructions](notebooks/README.md) · [Python source](src/bbo/README.md) · [Week-by-week code and results](journey/README.md)

## Data, documentation and reuse

The record contains **175 course-provided initial observations** and **104 personal portal evaluations**, including repeated queries. Inputs and actual returns remain distinct from fitted-model predictions and externally reported participant observations.

[Dataset datasheet](DATASHEET.md) · [Model card](MODEL_CARD.md) · [Evidence and limitations](docs/EVIDENCE_RULES.md) · [Citation](CITATION.cff)

My original code and documentation are available under the **[MIT Licence](LICENSE)**, which permits copying, modification and reuse, including commercially, with the required copyright and licence notices. Course-supplied and third-party data are **not** relicensed under MIT. See [usage and permissions](USAGE_AND_PERMISSIONS.md).

---

**Author:** [Tamer El-Tonsy](https://github.com/tatonsyML) · **Project:** Imperial College London Machine Learning & AI capstone

[Repository home](https://github.com/tatonsyML/bbo-capstone-imperial-college) · [Questions and corrections](https://github.com/tatonsyML/bbo-capstone-imperial-college/issues)
