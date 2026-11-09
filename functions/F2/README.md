# Function 2: inputs, outputs and model evidence

**2 input dimensions · 10 starting observations · 13 submitted queries · best observed output `0.744250426302126`.**

F2's Round 9 local forecast failed; broader Round 13 searching improved the observed best.

## Every weekly portal submission

Each output is **measured**, not a GP prediction. **↑** marks a new best relative to all earlier real observations, including the course starting data. The third column shows the actual Round score; the fourth shows best-so-far, which is different.

| Round | Actual submitted coordinates | Actual portal output | Best so far | Historical rationale and available code |
|---:|---|---:|---:|---|
| [1](../../journey/round_01/README.md) | `0.7-0.5` | `0.379063270240082` | `0.6112052158` | [Evidence](../../journey/round_01/README.md) |
| [2](../../journey/round_02/README.md) | `0.672-0.999999` | `0.5860547049641637` | `0.6112052158` | [Evidence](../../journey/round_02/README.md) · [code](../../journey/round_02/week2_ucb_course_aligned.py) |
| [3](../../journey/round_03/README.md) | `0.7015-0.957999` | `0.653867607133911` **↑** | `0.6538676071` | [Evidence](../../journey/round_03/README.md) |
| [4](../../journey/round_04/README.md) | `0.705-0.999999` | `0.5912856598404541` | `0.6538676071` | [Evidence](../../journey/round_04/README.md) · [code](../../journey/round_04/capstone_bbo_week4_module15.py) |
| [5](../../journey/round_05/README.md) | `0.7015-0.959409` | `0.6548498709022528` **↑** | `0.6548498709` | [Evidence](../../journey/round_05/README.md) |
| [6](../../journey/round_06/README.md) | `0.7015-0.959816` | `0.6913148663237587` **↑** | `0.6913148663` | [Evidence](../../journey/round_06/README.md) · [code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) |
| [7](../../journey/round_07/README.md) | `0.7015-0.960223` | `0.5893476079120687` | `0.6913148663` | [Evidence](../../journey/round_07/README.md) |
| [8](../../journey/round_08/README.md) | `0.7015-0.95972` | `0.6130861312279376` | `0.6913148663` | [Evidence](../../journey/round_08/results/round8_queries.csv) · [code](../../journey/round_08/capstone_bbo_module19_round8.py) |
| [9](../../journey/round_09/README.md) | `0.7015-0.959912` | `0.5055255161847483` | `0.6913148663` | [Evidence](../../journey/round_09/results/round9_queries.csv) · [code](../../journey/round_09/round9_controlled_fits.py) |
| [10](../../journey/round_10/README.md) | `0.701500-0.959796` | `0.617259927400158` | `0.6913148663` | [Evidence](../../journey/round_10/round10_candidates.csv) · [code](../../src/bbo/optimizer.py) |
| [11](../../journey/round_11/README.md) | `0.692000-0.366000` | `0.6953368270741286` **↑** | `0.6953368271` | [Evidence](../../journey/round_11/README.md) |
| [12](../../journey/round_12/README.md) | `0.684399-0.368552` | `0.660671151390024` | `0.6953368271` | [Evidence](../../journey/round_12/README.md) |
| [13](../../journey/round_13/README.md) | `0.864900-0.500000` | `0.7442504263021256` **↑** | `0.7442504263` | [Evidence](../../journey/round_13/README.md) |

## Per-function evidence

- [All observations](observations.csv): 10 initial records plus 13 submitted and returned scores, preserved at source precision.
- [Decision and provenance ledger](selection_history.csv): the 13 actual inputs, outcomes, pre-round data counts, rationales, related scripts, code-evidence status and available forecasts.
- [Replay and fitted-model guidance](model_runs/README.md): how to refit a **new** GP using only observations from before the chosen Round, and inspect learned kernel lengthscales.


## Preserved prospective forecasts

Recorded pre-result forecasts are distinguished from reconstructed estimates. Blank entries in the CSV mean no such numerical forecast was retained.

| Round | Recorded forecast | Actual result | Status |
|---:|---:|---:|---|
| 9 | `0.7305023346561939` | `0.5055255161847483` | recorded before return |

## Method and code provenance

Historical code references are linked in the round table where retained. A script related to a round is **not proof that those exact model settings generated every submitted input**. Exact saved GP model objects and per-round fitted lengthscales have not been retained for all 104 decisions.

No fully authenticated source equation is claimed for this function.

Our [shared GP code](../../src/bbo/surrogates.py), [acquisition functions](../../src/bbo/acquisition.py) and [candidate-generation utilities](../../src/bbo/search.py) apply to all eight functions with **separate fitted models**. [HEBO-inspired and TuRBO-style challengers](../../src/bbo/optimizer.py) differ from the [later official HEBO / BoTorch TuRBO-1 benchmark](../../research/full_optimisers/README.md); neither full reference engine is claimed as the historical submitter.

[All functions](../README.md) · [Chronological journey](../../journey/README.md) · [Final model card](../../MODEL_CARD.md).
