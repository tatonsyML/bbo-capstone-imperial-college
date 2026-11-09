# Function 7: inputs, outputs and model evidence

**6 input dimensions · 30 starting observations · 13 submitted queries · best observed output `3.32236801139316`.**

F7's Round 12 pre-result structural forecast succeeded. The Round 11 coordinates were subsequently recovered from the official course-results email; the original selection script is still unavailable.

## Every weekly portal submission

Each output is **measured**, not a GP prediction. **↑** marks a new best relative to all earlier real observations, including the course starting data. The third column shows the actual Round score; the fourth shows best-so-far, which is different.

| Round | Actual submitted coordinates | Actual portal output | Best so far | Historical rationale and available code |
|---:|---|---:|---:|---|
| [1](../../journey/round_01/README.md) | `0.034737-0.246867-0.265123-0.307852-0.362506-0.937209` | `1.3605555033645358` | `1.364968304` | [Evidence](../../journey/round_01/README.md) |
| [2](../../journey/round_02/README.md) | `0.074002-0.315323-0.247287-0.026732-0.35885-0.832838` | `1.020402279048806` | `1.364968304` | [Evidence](../../journey/round_02/README.md) · [code](../../journey/round_02/week2_ucb_course_aligned.py) |
| [3](../../journey/round_03/README.md) | `0.046316-0.36927-0.256273-0.262985-0.391467-0.834089` | `1.6137963046751616` **↑** | `1.613796305` | [Evidence](../../journey/round_03/README.md) |
| [4](../../journey/round_04/README.md) | `0.015-0.36927-0.256273-0.262985-0.391467-0.834089` | `1.5516324818204723` | `1.613796305` | [Evidence](../../journey/round_04/README.md) · [code](../../journey/round_04/capstone_bbo_week4_module15.py) |
| [5](../../journey/round_05/README.md) | `0.06-0.36927-0.256273-0.262985-0.391467-0.834089` | `1.638440146032503` **↑** | `1.638440146` | [Evidence](../../journey/round_05/README.md) |
| [6](../../journey/round_06/README.md) | `0.1-0.36927-0.256273-0.262985-0.391467-0.834089` | `1.7006596900158717` **↑** | `1.700659690` | [Evidence](../../journey/round_06/README.md) · [code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) |
| [7](../../journey/round_07/README.md) | `0.15-0.36927-0.256273-0.262985-0.391467-0.834089` | `1.7557182120997592` **↑** | `1.755718212` | [Evidence](../../journey/round_07/README.md) |
| [8](../../journey/round_08/README.md) | `0.23407-0.36927-0.256273-0.262985-0.391467-0.834089` | `1.785862549726479` **↑** | `1.785862550` | [Evidence](../../journey/round_08/results/round8_queries.csv) · [code](../../journey/round_08/capstone_bbo_module19_round8.py) |
| [9](../../journey/round_09/README.md) | `0.228702-0.36927-0.256273-0.262985-0.391467-0.834089` | `1.786338197796892` **↑** | `1.786338198` | [Evidence](../../journey/round_09/results/round9_queries.csv) · [code](../../journey/round_09/round9_controlled_fits.py) |
| [10](../../journey/round_10/README.md) | `0.190478-0.171014-0.347582-0.283057-0.283946-0.639922` | `3.149458800087033` **↑** | `3.149458800` | [Evidence](../../journey/round_10/round10_candidates.csv) · [code](../../src/bbo/optimizer.py) |
| [11](../../journey/round_11/README.md) | `0.233000-0.128000-0.522000-0.276000-0.310000-0.667000` | `3.278967926227992` **↑** | `3.278967926` | [Evidence](../../journey/round_11/README.md) |
| [12](../../journey/round_12/README.md) | `0.201689-0.150011-0.476874-0.275332-0.311652-0.657301` | `3.3223680113931557` **↑** | `3.322368011` | [Evidence](../../journey/round_12/README.md) |
| [13](../../journey/round_13/README.md) | `0.201690-0.150011-0.476874-0.275332-0.311652-0.657301` | `3.322368011392718` | `3.322368011` | [Evidence](../../journey/round_13/README.md) |

## Per-function evidence

- [All observations](observations.csv): 30 initial records plus 13 submitted and returned scores, preserved at source precision.
- [Decision and provenance ledger](selection_history.csv): the 13 actual inputs, outcomes, pre-round data counts, rationales, related scripts, code-evidence status and available forecasts.
- [Replay and fitted-model guidance](model_runs/README.md): how to refit a **new** GP using only observations from before the chosen Round, and inspect learned kernel lengthscales.


## Preserved prospective forecasts

Recorded pre-result forecasts are distinguished from reconstructed estimates. Blank entries in the CSV mean no such numerical forecast was retained.

| Round | Recorded forecast | Actual result | Status |
|---:|---:|---:|---|
| 9 | `1.786415130748528` | `1.786338197796892` | recorded before return |
| 12 | `3.32236801` | `3.3223680113931557` | approximate pre result forecast in round 12 notes |

## Method and code provenance

Historical code references are linked in the round table where retained. A script related to a round is **not proof that those exact model settings generated every submitted input**. Exact saved GP model objects and per-round fitted lengthscales have not been retained for all 104 decisions.

[Round 12 analysis](../../journey/round_12/README.md) documents the pre-result Hartmann-6 structural forecast; it does not prove the hidden source formula.

Our [shared GP code](../../src/bbo/surrogates.py), [acquisition functions](../../src/bbo/acquisition.py) and [candidate-generation utilities](../../src/bbo/search.py) apply to all eight functions with **separate fitted models**. [HEBO-inspired and TuRBO-style challengers](../../src/bbo/optimizer.py) differ from the [later official HEBO / BoTorch TuRBO-1 benchmark](../../research/full_optimisers/README.md); neither full reference engine is claimed as the historical submitter.

[All functions](../README.md) · [Chronological journey](../../journey/README.md) · [Final model card](../../MODEL_CARD.md).
