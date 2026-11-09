# Function 8: inputs, outputs and model evidence

**8 input dimensions · 40 starting observations · 13 submitted queries · best observed output `10.0000000000000`.**

F8's additive quadratic led to a Round 10 portal-confirmed value of ten. Independent 40/13 validation was performed later.

## Every weekly portal submission

Each output is **measured**, not a GP prediction. **↑** marks a new best relative to all earlier real observations, including the course starting data. The third column shows the actual Round score; the fourth shows best-so-far, which is different.

| Round | Actual submitted coordinates | Actual portal output | Best so far | Historical rationale and available code |
|---:|---|---:|---:|---|
| [1](../../journey/round_01/README.md) | `0.088526-0.03196-0.048494-0.063991-0.991333-0.224689-0.073759-0.537568` | `9.8321123600691` **↑** | `9.832112360` | [Evidence](../../journey/round_01/README.md) |
| [2](../../journey/round_02/README.md) | `0.321822-0.045429-0.355724-0.015612-0.965914-0.090106-0.138377-0.028859` | `9.4977489881389` | `9.832112360` | [Evidence](../../journey/round_02/README.md) · [code](../../journey/round_02/week2_ucb_course_aligned.py) |
| [3](../../journey/round_03/README.md) | `0.099253-0.051531-0.055571-0.074437-0.985751-0.228722-0.118577-0.53735` | `9.8634785625365` **↑** | `9.863478563` | [Evidence](../../journey/round_03/README.md) |
| [4](../../journey/round_04/README.md) | `0.104617-0.061316-0.05911-0.07966-0.98296-0.230739-0.140986-0.537241` | `9.8754707823449` **↑** | `9.875470782` | [Evidence](../../journey/round_04/README.md) · [code](../../journey/round_04/capstone_bbo_week4_module15.py) |
| [5](../../journey/round_05/README.md) | `0.109981-0.071101-0.062649-0.084883-0.980169-0.232756-0.163395-0.537132` | `9.8850021313761` **↑** | `9.885002131` | [Evidence](../../journey/round_05/README.md) |
| [6](../../journey/round_06/README.md) | `0.115345-0.080886-0.066188-0.090106-0.977378-0.234773-0.185804-0.537023` | `9.8920726096301` **↑** | `9.892072610` | [Evidence](../../journey/round_06/README.md) · [code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) |
| [7](../../journey/round_07/README.md) | `0.128076-0.104109-0.074587-0.102502-0.970754-0.23956-0.238989-0.536764` | `9.8990020095864` **↑** | `9.899002010` | [Evidence](../../journey/round_07/README.md) |
| [8](../../journey/round_08/README.md) | `0.128076-0.104109-0.074587-0.102502-0.970754-0.26456-0.238989-0.536764` | `9.9113990095864` **↑** | `9.911399010` | [Evidence](../../journey/round_08/results/round8_queries.csv) · [code](../../journey/round_08/capstone_bbo_module19_round8.py) |
| [9](../../journey/round_09/README.md) | `0.128076-0.104109-0.074587-0.102502-0.970754-0.31456-0.238989-0.536764` | `9.9324430095864` **↑** | `9.932443010` | [Evidence](../../journey/round_09/results/round9_queries.csv) · [code](../../journey/round_09/round9_controlled_fits.py) |
| [10](../../journey/round_10/README.md) | `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000` | `10` **↑** | `10.00000000` | [Evidence](../../journey/round_10/round10_candidates.csv) · [code](../../src/bbo/optimizer.py) |
| [11](../../journey/round_11/README.md) | `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000` | `10` | `10.00000000` | [Evidence](../../journey/round_11/README.md) |
| [12](../../journey/round_12/README.md) | `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000` | `10` | `10.00000000` | [Evidence](../../journey/round_12/README.md) |
| [13](../../journey/round_13/README.md) | `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000` | `10` | `10.00000000` | [Evidence](../../journey/round_13/README.md) |

## Per-function evidence

- [All observations](observations.csv): 40 initial records plus 13 submitted and returned scores, preserved at source precision.
- [Decision and provenance ledger](selection_history.csv): the 13 actual inputs, outcomes, pre-round data counts, rationales, related scripts, code-evidence status and available forecasts.
- [Replay and fitted-model guidance](model_runs/README.md): how to refit a **new** GP using only observations from before the chosen Round, and inspect learned kernel lengthscales.


## Preserved prospective forecasts

Recorded pre-result forecasts are distinguished from reconstructed estimates. Blank entries in the CSV mean no such numerical forecast was retained.

| Round | Recorded forecast | Actual result | Status |
|---:|---:|---:|---|
| 9 | `9.933511308824693` | `9.9324430095864` | recorded before return |
| 10 | `10` | `10` | recorded structural prediction before return |

## Method and code provenance

Historical code references are linked in the round table where retained. A script related to a round is **not proof that those exact model settings generated every submitted input**. Exact saved GP model objects and per-round fitted lengthscales have not been retained for all 104 decisions.

[F8 structural validation](../../src/bbo/structural_validation.py) retrospectively fits the initial 40 points and validates against 13 later outcomes. This fit was not performed in Round 1.

Our [shared GP code](../../src/bbo/surrogates.py), [acquisition functions](../../src/bbo/acquisition.py) and [candidate-generation utilities](../../src/bbo/search.py) apply to all eight functions with **separate fitted models**. [HEBO-inspired and TuRBO-style challengers](../../src/bbo/optimizer.py) differ from the [later official HEBO / BoTorch TuRBO-1 benchmark](../../research/full_optimisers/README.md); neither full reference engine is claimed as the historical submitter.

[All functions](../README.md) · [Chronological journey](../../journey/README.md) · [Final model card](../../MODEL_CARD.md).
