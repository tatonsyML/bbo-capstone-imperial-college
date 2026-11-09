# Function 5: inputs, outputs and model evidence

**4 input dimensions · 20 starting observations · 13 submitted queries · best observed output `8662.40500124830`.**

Measured boundary changes culminated in a Round 10 legal-upper-corner improvement.

## Every weekly portal submission

Each output is **measured**, not a GP prediction. **↑** marks a new best relative to all earlier real observations, including the course starting data. The third column shows the actual Round score; the fourth shows best-so-far, which is different.

| Round | Actual submitted coordinates | Actual portal output | Best so far | Historical rationale and available code |
|---:|---|---:|---:|---|
| [1](../../journey/round_01/README.md) | `0.1-0.75-0.9-0.98` | `1426.0897645116545` **↑** | `1426.089765` | [Evidence](../../journey/round_01/README.md) |
| [2](../../journey/round_02/README.md) | `0.522156-0.922246-0.999259-0.99589` | `3722.27447382346` **↑** | `3722.274474` | [Evidence](../../journey/round_02/README.md) · [code](../../journey/round_02/week2_ucb_course_aligned.py) |
| [3](../../journey/round_03/README.md) | `0.508373-0.970147-0.999999-0.999999` | `4295.86773060836` **↑** | `4295.867731` | [Evidence](../../journey/round_03/README.md) |
| [4](../../journey/round_04/README.md) | `0.508373-0.999999-0.999999-0.999999` | `4694.317308235808` **↑** | `4694.317308` | [Evidence](../../journey/round_04/README.md) · [code](../../journey/round_04/capstone_bbo_week4_module15.py) |
| [5](../../journey/round_05/README.md) | `0.558373-0.999999-0.999999-0.999999` | `4807.986076589498` **↑** | `4807.986077` | [Evidence](../../journey/round_05/README.md) |
| [6](../../journey/round_06/README.md) | `0.608373-0.999999-0.999999-0.999999` | `4957.571711515816` **↑** | `4957.571712` | [Evidence](../../journey/round_06/README.md) · [code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) |
| [7](../../journey/round_07/README.md) | `0.658373-0.999999-0.999999-0.999999` | `5151.047725485012` **↑** | `5151.047725` | [Evidence](../../journey/round_07/README.md) |
| [8](../../journey/round_08/README.md) | `0.758373-0.999999-0.999999-0.999999` | `5709.3613198927205` **↑** | `5709.361320` | [Evidence](../../journey/round_08/results/round8_queries.csv) · [code](../../journey/round_08/capstone_bbo_module19_round8.py) |
| [9](../../journey/round_09/README.md) | `0.858373-0.999999-0.999999-0.999999` | `6583.56144525802` **↑** | `6583.561445` | [Evidence](../../journey/round_09/results/round9_queries.csv) · [code](../../journey/round_09/round9_controlled_fits.py) |
| [10](../../journey/round_10/README.md) | `0.999999-0.999999-0.999999-0.999999` | `8662.405001248297` **↑** | `8662.405001` | [Evidence](../../journey/round_10/round10_candidates.csv) · [code](../../src/bbo/optimizer.py) |
| [11](../../journey/round_11/README.md) | `0.999999-0.999999-0.999999-0.999999` | `8662.405001248297` | `8662.405001` | [Evidence](../../journey/round_11/README.md) |
| [12](../../journey/round_12/README.md) | `0.999999-0.999999-0.999999-0.999999` | `8662.405001248297` | `8662.405001` | [Evidence](../../journey/round_12/README.md) |
| [13](../../journey/round_13/README.md) | `0.999999-0.999999-0.999999-0.999999` | `8662.405001248297` | `8662.405001` | [Evidence](../../journey/round_13/README.md) |

## Per-function evidence

- [All observations](observations.csv): 20 initial records plus 13 submitted and returned scores, preserved at source precision.
- [Decision and provenance ledger](selection_history.csv): the 13 actual inputs, outcomes, pre-round data counts, rationales, related scripts, code-evidence status and available forecasts.
- [Replay and fitted-model guidance](model_runs/README.md): how to refit a **new** GP using only observations from before the chosen Round, and inspect learned kernel lengthscales.


## Preserved prospective forecasts

Recorded pre-result forecasts are distinguished from reconstructed estimates. Blank entries in the CSV mean no such numerical forecast was retained.

| Round | Recorded forecast | Actual result | Status |
|---:|---:|---:|---|
| 9 | `6454.0` | `6583.56144525802` | recorded before return |

## Method and code provenance

Historical code references are linked in the round table where retained. A script related to a round is **not proof that those exact model settings generated every submitted input**. Exact saved GP model objects and per-round fitted lengthscales have not been retained for all 104 decisions.

[F5 structural validation](../../src/bbo/structural_validation.py) documents a later analytic reconstruction.

Our [shared GP code](../../src/bbo/surrogates.py), [acquisition functions](../../src/bbo/acquisition.py) and [candidate-generation utilities](../../src/bbo/search.py) apply to all eight functions with **separate fitted models**. [HEBO-inspired and TuRBO-style challengers](../../src/bbo/optimizer.py) differ from the [later official HEBO / BoTorch TuRBO-1 benchmark](../../research/full_optimisers/README.md); neither full reference engine is claimed as the historical submitter.

[All functions](../README.md) · [Chronological journey](../../journey/README.md) · [Final model card](../../MODEL_CARD.md).
