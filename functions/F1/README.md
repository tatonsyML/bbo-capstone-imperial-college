# Function 1: inputs, outputs and model evidence

**2 input dimensions · 10 starting observations · 13 submitted queries · best observed output `1.99999999967618`.**

F1 revealed a sharp, high-value region after several near-zero returns. Its original complete sequence of trained models has not been retained.

## Every weekly portal submission

Each output is **measured**, not a GP prediction. **↑** marks a new best relative to all earlier real observations, including the course starting data. The third column shows the actual Round score; the fourth shows best-so-far, which is different.

| Round | Actual submitted coordinates | Actual portal output | Best so far | Historical rationale and available code |
|---:|---|---:|---:|---|
| [1](../../journey/round_01/README.md) | `0.02-0.98` | `0.0` | `7.710875115e-16` | [Evidence](../../journey/round_01/README.md) |
| [2](../../journey/round_02/README.md) | `0.052001-0.865999` | `-1.9632454298284602e-233` | `7.710875115e-16` | [Evidence](../../journey/round_02/README.md) · [code](../../journey/round_02/week2_ucb_course_aligned.py) |
| [3](../../journey/round_03/README.md) | `0.636406-0.206433` | `2.69213108614911e-65` | `7.710875115e-16` | [Evidence](../../journey/round_03/README.md) |
| [4](../../journey/round_04/README.md) | `0.999999-0.999999` | `1.517648729565899e-192` | `7.710875115e-16` | [Evidence](../../journey/round_04/README.md) · [code](../../journey/round_04/capstone_bbo_week4_module15.py) |
| [5](../../journey/round_05/README.md) | `0.75-0.75` | `1.3319145509281447e-22` | `7.710875115e-16` | [Evidence](../../journey/round_05/README.md) |
| [6](../../journey/round_06/README.md) | `0.732524-0.7389` | `3.2554751168755075e-17` | `7.710875115e-16` | [Evidence](../../journey/round_06/README.md) · [code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) |
| [7](../../journey/round_07/README.md) | `0.730874-0.7318` | `1.3142529628112004e-15` **↑** | `1.314252963e-15` | [Evidence](../../journey/round_07/README.md) |
| [8](../../journey/round_08/README.md) | `0.735874-0.729467` | `4.1970039548686525e-16` | `1.314252963e-15` | [Evidence](../../journey/round_08/results/round8_queries.csv) · [code](../../journey/round_08/capstone_bbo_module19_round8.py) |
| [9](../../journey/round_09/README.md) | `0.729874-0.7318` | `1.921280788064022e-15` **↑** | `1.921280788e-15` | [Evidence](../../journey/round_09/results/round9_queries.csv) · [code](../../journey/round_09/round9_controlled_fits.py) |
| [10](../../journey/round_10/README.md) | `0.582552-0.558941` | `0.000007264001184177771` **↑** | `0.000007264001184` | [Evidence](../../journey/round_10/round10_candidates.csv) · [code](../../src/bbo/optimizer.py) |
| [11](../../journey/round_11/README.md) | `0.628540-0.628540` | `1.9999999996761817` **↑** | `2.000000000` | [Evidence](../../journey/round_11/README.md) |
| [12](../../journey/round_12/README.md) | `0.628540-0.628540` | `1.9999999996761817` | `2.000000000` | [Evidence](../../journey/round_12/README.md) |
| [13](../../journey/round_13/README.md) | `0.628540-0.628540` | `1.9999999996761817` | `2.000000000` | [Evidence](../../journey/round_13/README.md) |

## Per-function evidence

- [All observations](observations.csv): 10 initial records plus 13 submitted and returned scores, preserved at source precision.
- [Decision and provenance ledger](selection_history.csv): the 13 actual inputs, outcomes, pre-round data counts, rationales, related scripts, code-evidence status and available forecasts.
- [Replay and fitted-model guidance](model_runs/README.md): how to refit a **new** GP using only observations from before the chosen Round, and inspect learned kernel lengthscales.


## Method and code provenance

Historical code references are linked in the round table where retained. A script related to a round is **not proof that those exact model settings generated every submitted input**. Exact saved GP model objects and per-round fitted lengthscales have not been retained for all 104 decisions.

No fully authenticated source equation is claimed for this function.

Our [shared GP code](../../src/bbo/surrogates.py), [acquisition functions](../../src/bbo/acquisition.py) and [candidate-generation utilities](../../src/bbo/search.py) apply to all eight functions with **separate fitted models**. [HEBO-inspired and TuRBO-style challengers](../../src/bbo/optimizer.py) differ from the [later official HEBO / BoTorch TuRBO-1 benchmark](../../research/full_optimisers/README.md); neither full reference engine is claimed as the historical submitter.

[All functions](../README.md) · [Chronological journey](../../journey/README.md) · [Final model card](../../MODEL_CARD.md).
