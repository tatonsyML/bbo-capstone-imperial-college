# Black-Box Optimisation
### Eight unknown functions. Thirteen rounds. An evolving search for better decisions.

**Imperial College London · Machine Learning & AI capstone**

[![Python tests](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/core-tests.yml/badge.svg)](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/core-tests.yml)

**8 functions** · **2–8 input dimensions** · **13 rounds** · **279 recorded evaluations**

[Explore the functions](functions/README.md) · [Follow the journey](journey/README.md) · [Explore the methods](methods/README.md) · [Run the notebook](notebooks/Capstone_Final_Walkthrough.ipynb)

> How do you choose your next experiment when the equation is hidden and every evaluation matters?

## The project

I set out to maximise eight unknown mathematical functions. Each function accepted between two and eight numerical inputs, each ranging from **0.000000 to 0.999999 (six decimal places)**, and returned a numerical score.

My objective was to identify the combination of inputs that produced the highest score. I was allowed **one evaluation per function per round**, making every decision important.

I began with Gaussian Process models and acquisition functions. As observations arrived, I challenged their predictions with alternative models, neural-network diagnostics, local search, controlled experiments and mathematical reconstruction. Some highly accurate forecasts were poor optimisation decisions. In other cases, a simple structural explanation was more useful than another complicated model.

This repository shows **what I tried, what actually happened, what failed and how my decisions changed**. It also separates experiments performed during the challenge from subsequent research.

### What is in the evidence

- **175** course-supplied initial observations and **104** personal portal evaluations, including repeated queries.
- Eight function-specific narratives with measured progress, mathematical investigations and visualisations.
- Thirteen chronological round records, with surviving historical code and notes where available.
- Reproducible code for selected mathematical checks, plus a separately labelled post-capstone HEBO/TuRBO comparison.

[Read the dataset](data/all_observations.csv) · [How the evidence is handled](docs/EVIDENCE_RULES.md)

## Choose your route

| I want to… | Begin here |
|---|---|
| Follow one problem from its first observation to the final result | **[Eight function stories](functions/README.md)** |
| Understand how the overall strategy evolved week by week | **[Thirteen-round journey](journey/README.md)** |
| Compare algorithms and understand the implementation | **[Methods and experiments](methods/README.md)** |
| Examine recovered equations and their limitations | **[Mathematical reconstructions](reconstruction/README.md)** |
| See the progress charts, observations and modelled surfaces | **[Visual gallery](visualisations/README.md)** |
| Find final runnable code and reproduction instructions | **[Final implementations](final/README.md)** |
| Inspect the original round evidence and historical Python code | **[Historical code and round archive](journey/README.md)** |

## 1. Eight functions, eight investigations

Each function page begins with observed behaviour and results, then follows the decisions across thirteen expandable rounds. It links to historical evidence, graphs and the strongest supported mathematical interpretation.

| Function | Inputs | Best measured score | First achieved | What it taught me |
|---|---:|---:|:---:|---|
| **[F1 · Finding the signal](functions/F1/README.md)** | 2 | **1.999999999676** | R11 | Near-zero responses concealed valuable structure |
| **[F2 · Challenge the forecast](functions/F2/README.md)** | 2 | **0.744250426302** | R13 | A confident local prediction failed |
| **[F3 · Brittle local peaks](functions/F3/README.md)** | 3 | **−0.003753096919** | R13 | Alternative regions beat an over-narrow local search |
| **[F4 · Accuracy versus progress](functions/F4/README.md)** | 4 | **0.746897911381** | R13 | Precise predictions did not guarantee improvement |
| **[F5 · Towards the boundary](functions/F5/README.md)** | 4 | **8,662.405001** | R10 | Controlled tests exposed a productive boundary |
| **[F6 · Unstable local behaviour](functions/F6/README.md)** | 5 | **−0.037518647244** | R12 | Local smoothness assumptions proved unreliable |
| **[F7 · From local to structural](functions/F7/README.md)** | 6 | **3.322368011393** | R12 | A structural model made a testable forecast |
| **[F8 · Recovering a quadratic](functions/F8/README.md)** | 8 | **10.000000** | R10 | A simple fitted equation turned searching into solving |

![Measured best-so-far score histories of all eight functions](results/figures/progress.svg)

*Each panel has its own vertical scale. All curves use **measured** best-so-far values, including the supplied initial samples, not predictions.*

[Explore all functions](functions/README.md) · [Read how to interpret the graphs](docs/functions.md)

## 2. How my strategy evolved

The [chronological journey](journey/README.md) preserves **Round 1 through Round 13**, with the inputs submitted, outputs returned, surviving original code and the thinking behind each decision.

| Rounds | Main focus | Learning |
|---|---|---|
| [1–3](journey/round_01/README.md) | GP baseline, UCB and function-specific acquisitions | A uniform policy did not work equally well on every function |
| [4–6](journey/round_04/README.md) | Alternative surrogate models, neural networks and controlled probes | Greater model complexity needed independent validation |
| [7–9](journey/round_07/README.md) | ARD, prospective forecasts and local-search decisions | Prediction error and search quality are different measures |
| [10](journey/round_10/README.md) | Boundary testing and mathematical structure | F5 reached the legal boundary; F8 reached 10 |
| [11–13](journey/round_11/README.md) | Structural testing, refined searches and final decisions | F1, F2, F3, F4, F6 and F7 made later gains |

**How to read an entry:** *What was known → What was predicted (if retained) → What was submitted → What returned → What changed afterwards.* Retrospective reasoning is labelled; a later reconstruction is never presented as an earlier forecast.

[Open all thirteen rounds](journey/README.md) · [Read the provenance rules](docs/EVIDENCE_RULES.md)

## 3. Mathematical reconstruction and visual evidence

The objective began as finding high-scoring inputs. For some functions I later tested whether a mathematical equation explained the observations. Each reconstruction has different levels of evidence.

| Function | Current mathematical evidence | Explore |
|---|---|---|
| F1 | Oscillatory, Gaussian-modulated reconstruction, informed by supplementary published observations; complete coefficients are not published here | [F1](functions/F1/README.md) |
| F2, F3, F4, F6 | Local models, observations and projections; no validated complete hidden-function equation is claimed | [Function index](functions/README.md) |
| F5 | Retrospective interacting power-sum representation, recovered **after** its R10 boundary query | [Equation and graph](functions/F5/README.md) |
| F7 | Positive Hartmann-6 reconstruction with a successful **pre-result** R12 forecast | [Equation evidence and graph](functions/F7/README.md) |
| F8 | 17-coefficient additive quadratic, fitting 40 initial samples and predicting 13 held-out returns to floating-point precision in a retrospective check | [Equation and graph](functions/F8/README.md) |

**F8 example:** the fitted form is `f̂₈(x) = 10 − Σ wᵢ(xᵢ − cᵢ)²`. The model has a maximum of **10** at the fitted centre, verified by an actual portal return in R10. This is a strongly validated reconstruction, **not** an authenticated copy of the undisclosed source function.

[See mathematical details and provenance](reconstruction/README.md) · [Inspect the F8 validation code](src/bbo/structural_validation.py) · [Browse the gallery](visualisations/README.md)

For higher-dimensional functions, 2D/3D surfaces are **fixed-coordinate slices** or observed projections, not complete visualisations of an 8D landscape. Published peer observations used as external evidence are acknowledged separately from personal portal returns.

## 4. Methods, alternatives and code

The historical work includes GP surrogates (RBF/Matérn with ARD), EI/PI/UCB, output transformations, regional searches, controlled coordinate probes, neural-network and SVM diagnostics, and *HEBO-inspired* / *TuRBO-style* challengers.

**Important distinction:** the full HEBO package and BoTorch TuRBO-1 implementations were added in **post-capstone research**. They did not generate historical portal queries. Other approaches mentioned in my working history, including **Ava** and **PDA**, are held for source verification before their implementation details are asserted.

[Methods and evidence index](methods/README.md) · [Implementation guide](docs/methods.md) · [Source modules](src/bbo/README.md) · [Later full-optimiser comparisons](research/full_optimisers/README.md)

## 5. Original code and final reproduction

The [round archive](journey/README.md) is the chronological home for original scripts, notebooks, submitted inputs, outputs and notes. It identifies missing candidate-selection scripts and distinguishes related surviving code from verified query generators. The final code offers a separate, easier reproduction route.

Python 3.11 is recommended. From the repository root:

```bash
python -m pip install -r requirements-notebook.txt
python -m pytest -q
jupyter notebook notebooks/Capstone_Final_Walkthrough.ipynb
```

[Final code and run instructions](final/README.md) · [Executable Jupyter notebook](notebooks/Capstone_Final_Walkthrough.ipynb) · [Historical code](journey/README.md)

## 6. Research documentation and reuse

| Document | Purpose |
|---|---|
| [MODEL_CARD.md](MODEL_CARD.md) | Models, use, validation, limitations and evaluation |
| [DATASHEET.md](DATASHEET.md) | Dataset composition, sources, provenance and limitations |
| [Evidence principles](docs/EVIDENCE_RULES.md) | Contemporary records versus retrospective analysis |
| [Usage and permissions](USAGE_AND_PERMISSIONS.md) | Data rights, attribution and restrictions |
| [LICENSE](LICENSE) | **All rights reserved at present**; no open-source permission has yet been granted |
| [CITATION.cff](CITATION.cff) | Suggested citation metadata for the repository |

**Rights notice:** the 175 course-supplied observations are currently included in the public CSV, but permission to redistribute them has not been independently verified. Their availability does not mean unrestricted reuse is authorised.

## What this work taught me

**Forecast accuracy is not decision quality.** F4's highly precise micro-steps produced little progress, while a wider move helped.

**Model complexity is a choice, not a goal.** F8 showed how testing a simple hypothesis revealed structure that was not immediately obvious from more sophisticated search.

**Different problems reward different strategies.** Boundary effects, narrow regions, interacting variables and dimensionality required different decisions.

**The research history matters.** Original observations, original decisions, later explanations and external research evidence must remain distinguishable.

---

**Author:** [Tamer El-Tonsy](https://github.com/tatonsyML) · **Project:** Imperial College London Machine Learning & AI capstone

[Repository home](https://github.com/tatonsyML/bbo-capstone-imperial-college) · [Questions and corrections](https://github.com/tatonsyML/bbo-capstone-imperial-college/issues)
